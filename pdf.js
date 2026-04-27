import PDFDocument from 'pdfkit';

// ── BRAND COLORS ─────────────────────────────────────────────────────────────
const NAVY   = '#1c2b4a';
const GOLD   = '#c9973a';
const MUTED  = '#6b7a96';
const DIM    = '#9aa3b5';
const BORDER = '#e2e6ef';
const GREEN  = '#276944';
const RED    = '#b83232';
const AMBER  = '#a86c0a';
const CREAM  = '#faf8f4';
const CREAMD = '#f0ece3';
const WHITE  = '#ffffff';

const RISK_COLOR = { Low: GREEN, Moderate: AMBER, High: RED };
const RISK_BG    = { Low: '#eaf5ef', Moderate: '#fef6e8', High: '#fdf0f0' };
const DOT_COLOR  = { red: RED, amber: AMBER, green: GREEN };
const TL_COLOR   = { 'This week': RED, 'This month': AMBER, 'Ongoing': NAVY };

async function verifyStripeSession(sessionId) {
  if (!sessionId || typeof sessionId !== 'string') return false;
  if (!/^cs_(test|live)_[A-Za-z0-9_]+$/.test(sessionId)) return false;
  if (!process.env.STRIPE_SECRET_KEY) return false;
  try {
    const resp = await fetch(`https://api.stripe.com/v1/checkout/sessions/${encodeURIComponent(sessionId)}`, {
      headers: { Authorization: `Bearer ${process.env.STRIPE_SECRET_KEY}` },
    });
    if (!resp.ok) return false;
    const session = await resp.json();
    return session && session.payment_status === 'paid';
  } catch (e) {
    return false;
  }
}

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).end();

  const body = req.body || {};
  const { session_id, report } = body;
  const r   = report || body;
  const sid = session_id || (req.query && req.query.session_id);

  if (!r || !r.risk_level) return res.status(400).json({ error: 'Missing report data' });

  const paid = await verifyStripeSession(sid);
  if (!paid) return res.status(402).json({ error: 'Payment required' });

  try {
    const chunks = [];
    const doc = new PDFDocument({
      size: 'LETTER',
      margins: { top: 76, bottom: 60, left: 56, right: 56 },
      info: {
        Title:   'SideHustleGuard Compliance & Tax Report',
        Author:  'SideHustleGuard',
        Subject: 'Side hustle compliance and tax analysis',
      },
    });

    doc.on('data', chunk => chunks.push(chunk));

    const PW  = doc.page.width;
    const PH  = doc.page.height;
    const ML  = 56;
    const W   = PW - ML - ML;
    let   y   = 80;
    let   pageNum = 1;

    // ── FOOTER (drawn on every page before adding a new one) ─────────────────
    function drawFooter() {
      const savedBottom = doc.page.margins.bottom;
      doc.page.margins.bottom = 0;
      const fy = PH - 30;
      doc.rect(0, fy, PW, 30).fill(CREAMD);
      doc.moveTo(0, fy).lineTo(PW, fy).lineWidth(0.4).stroke(BORDER);
      doc.font('Helvetica').fontSize(6.5).fill(DIM)
         .text(
           'Educational purposes only — not legal or tax advice. Consult a licensed CPA or attorney.',
           ML, fy + 10, { lineBreak: false, width: W - 90 }
         );
      doc.font('Helvetica').fontSize(6.5).fill(DIM)
         .text(
           `sidehustleguard.com  |  p. ${pageNum}`,
           ML, fy + 10, { align: 'right', width: W, lineBreak: false }
         );
      doc.page.margins.bottom = savedBottom;
    }

    // ── CONTINUATION PAGE HEADER ─────────────────────────────────────────────
    function drawContinuationHeader() {
      pageNum++;
      doc.rect(0, 0, PW, 34).fill(NAVY);
      doc.rect(0, 34, PW, 2).fill(GOLD);
      doc.rect(0, 36, 3, PH - 36 - 30).fill(GOLD);
      // FIX: 'SideHustle' (white) + 'Guard' (gold) — not 'SideHustleGuard' + 'Guard'
      doc.font('Helvetica-Bold').fontSize(10).fill(WHITE)
         .text('SideHustle', ML, 11, { continued: true });
      doc.fill(GOLD).text('Guard', { continued: false });
      doc.font('Helvetica').fontSize(7).fill(DIM)
         .text(
           `${r.client || 'Your Report'}  ·  Confidential`,
           ML, 12, { align: 'right', width: W, lineBreak: false }
         );
      y = 54;
    }

    // ── SPACE CHECK ──────────────────────────────────────────────────────────
    function checkSpace(needed) {
      if (y + needed > PH - 72) {
        drawFooter();
        doc.addPage();
        drawContinuationHeader();
      }
    }

    // ── SECTION LABEL ────────────────────────────────────────────────────────
    function sectionLabel(text) {
      checkSpace(28);
      doc.font('Helvetica-Bold').fontSize(7).fill(GOLD)
         .text(text.toUpperCase(), ML, y, { characterSpacing: 1.1 });
      y += 12;
      doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.4).stroke(BORDER);
      y += 10;
    }

    // ── PAGE 1 HEADER ────────────────────────────────────────────────────────
    doc.rect(0, 0, PW, 58).fill(NAVY);
    doc.rect(0, 58, PW, 3).fill(GOLD);
    doc.rect(0, 61, 3, PH - 61 - 30).fill(GOLD);

    doc.font('Helvetica-Bold').fontSize(15).fill(WHITE)
       .text('SideHustle', ML, 17, { continued: true });
    doc.fill(GOLD).text('Guard', { continued: false });

    doc.font('Helvetica').fontSize(8).fill(DIM)
       .text('Compliance & Tax Report', ML, 19, { align: 'right', width: W, lineBreak: false });
    doc.font('Helvetica').fontSize(7).fill(WHITE).opacity(0.55)
       .text(
         `${r.client || 'Your Report'}  ·  Confidential`,
         ML, 32, { align: 'right', width: W, lineBreak: false }
       );
    doc.opacity(1);

    y = 80;

    // ── OVERALL RISK ─────────────────────────────────────────────────────────
    const rc = RISK_COLOR[r.risk_level] || AMBER;
    const rb = RISK_BG[r.risk_level]   || '#fef6e8';
    const riskH = 56;

    doc.rect(ML, y, W, riskH).fill(rb);
    doc.rect(ML, y, 4, riskH).fill(rc);

    doc.font('Helvetica-Bold').fontSize(7).fill(rc)
       .text('OVERALL RISK', ML + 16, y + 9, { characterSpacing: 0.8 });
    doc.font('Helvetica-Bold').fontSize(22).fill(rc)
       .text((r.risk_level || 'Moderate').toUpperCase(), ML + 16, y + 19);

    const openingW = W - 148;
    doc.font('Helvetica').fontSize(9.5).fill(NAVY)
       .text(r.opening || '', ML + 148, y + 12, { width: openingW, lineGap: 2.5 });

    y += riskH + 20;

    // ── KEY INSIGHT ──────────────────────────────────────────────────────────
    checkSpace(72);
    sectionLabel("What most people in your position don't realize");

    const insightY = y;
    // measure height first
    doc.font('Helvetica-Bold').fontSize(10).fill(NAVY)
       .text(r.key_insight || '', ML + 14, y, { width: W - 14, lineGap: 3 });
    const insightH = doc.y - insightY + 12;
    // draw left rule
    doc.rect(ML, insightY, 3, insightH).fill(GOLD);
    // redraw text over rule
    doc.font('Helvetica-Bold').fontSize(10).fill(NAVY)
       .text(r.key_insight || '', ML + 14, insightY, { width: W - 14, lineGap: 3 });
    y = insightY + insightH + 8;

    // ── QUICK WINS ───────────────────────────────────────────────────────────
    checkSpace(90);
    sectionLabel('Fastest way to reduce your risk (under 1 hour)');

    const qwStartY = y;
    y += 10;

    // Pass 1: measure
    (r.quick_wins || []).forEach((win, i) => {
      doc.circle(ML + 10, y + 6, 7.5).fill(GOLD);
      doc.font('Helvetica-Bold').fontSize(8).fill(WHITE)
         .text(String(i + 1), ML + 7, y + 3, { width: 7, align: 'center', lineBreak: false });
      doc.font('Helvetica-Bold').fontSize(9.5).fill(NAVY)
         .text(win, ML + 24, y, { width: W - 24 });
      y = doc.y + 7;
    });
    if (r.quick_wins_note) {
      doc.font('Helvetica-Bold').fontSize(9).fill(GREEN)
         .text(r.quick_wins_note, ML + 10, y, { width: W - 10 });
      y = doc.y + 6;
    }
    const qwH = y - qwStartY + 8;

    // Draw background + left rule behind content
    doc.rect(ML, qwStartY, W, qwH).fill('#eaf5ef');
    doc.rect(ML, qwStartY, 3.5, qwH).fill(GREEN);

    // Pass 2: redraw content over background
    y = qwStartY + 10;
    (r.quick_wins || []).forEach((win, i) => {
      doc.circle(ML + 10, y + 6, 7.5).fill(GOLD);
      doc.font('Helvetica-Bold').fontSize(8).fill(WHITE)
         .text(String(i + 1), ML + 7, y + 3, { width: 7, align: 'center', lineBreak: false });
      doc.font('Helvetica-Bold').fontSize(9.5).fill(NAVY)
         .text(win, ML + 24, y, { width: W - 24 });
      y = doc.y + 7;
    });
    if (r.quick_wins_note) {
      doc.font('Helvetica-Bold').fontSize(9).fill(GREEN)
         .text(r.quick_wins_note, ML + 10, y, { width: W - 10 });
      y = doc.y + 6;
    }
    y += 14;

    // ── WHAT STANDS OUT ───────────────────────────────────────────────────────
    checkSpace(80);
    sectionLabel('What stands out');

    (r.issues || r.stands_out || []).forEach(issue => {
      checkSpace(48);
      const title  = issue.title  || issue[1] || '';
      const body   = issue.detail || issue.body || issue[2] || '';
      const status = issue.status || (issue[0] === true ? 'red' : 'amber');
      const dc     = DOT_COLOR[status] || AMBER;

      doc.circle(ML + 4.5, y + 6, 4).fill(dc);
      doc.font('Helvetica-Bold').fontSize(9.5).fill(NAVY)
         .text(title, ML + 14, y, { width: W - 14 });
      y = doc.y + 2;
      doc.font('Helvetica').fontSize(9).fill(MUTED)
         .text(body, ML + 14, y, { width: W - 14, lineGap: 2 });
      y = doc.y + 4;
      doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.4).stroke(BORDER);
      y += 9;
    });
    y += 6;

    // ── TAX REALITY ───────────────────────────────────────────────────────────
    checkSpace(110);
    sectionLabel('Tax reality');

    const boxW = (W - 10) / 2;
    const boxH = 52;

    doc.rect(ML, y, boxW, boxH).fill('#fdf0f0');
    doc.rect(ML, y, 3.5, boxH).fill(RED);
    doc.font('Helvetica').fontSize(7.5).fill(DIM)
       .text('Effective rate', ML + 12, y + 9, { lineBreak: false });
    doc.font('Helvetica-Bold').fontSize(22).fill(RED)
       .text(r.tax_rate || '—', ML + 12, y + 20);

    doc.rect(ML + boxW + 10, y, boxW, boxH).fill('#fef6e8');
    doc.rect(ML + boxW + 10, y, 3.5, boxH).fill(AMBER);
    doc.font('Helvetica').fontSize(7.5).fill(DIM)
       .text('Est. tax owed (yr 1)', ML + boxW + 22, y + 9, { lineBreak: false });
    doc.font('Helvetica-Bold').fontSize(18).fill(AMBER)
       .text(r.tax_owed_est || '—', ML + boxW + 22, y + 21);

    y += boxH + 12;

    if (r.tax_note) {
      checkSpace(48);
      doc.rect(ML, y, W, 1).fill(BORDER);
      y += 10;
      doc.font('Helvetica-Bold').fontSize(8.5).fill(AMBER)
         .text('What people usually get wrong:', ML, y, { lineBreak: false });
      y += 14;
      doc.font('Helvetica').fontSize(9).fill(NAVY)
         .text(r.tax_note, ML + 10, y, { width: W - 10, lineGap: 2.5 });
      y = doc.y + 14;
    }

    // ── WHAT'S WORKING ────────────────────────────────────────────────────────
    checkSpace(60);
    sectionLabel("What you're doing right");

    (r.working || []).forEach(item => {
      checkSpace(24);
      // Use bullet (U+2022) — safe in WinAnsi/Helvetica; checkmark U+2713 is not
      doc.font('Helvetica-Bold').fontSize(11).fill(GREEN)
         .text('•', ML, y, { lineBreak: false });
      doc.font('Helvetica').fontSize(9).fill(NAVY)
         .text(item, ML + 14, y, { width: W - 14, lineGap: 2 });
      y = doc.y + 4;
      doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.4).stroke(BORDER);
      y += 8;
    });
    y += 8;

    // ── ACTION PLAN ───────────────────────────────────────────────────────────
    checkSpace(80);
    sectionLabel('What to do next');

    (r.action_plan || []).forEach((step, i) => {
      checkSpace(36);
      const label = step.timeline || 'Ongoing';
      const text  = step.step || step;
      const tc    = TL_COLOR[label] || NAVY;

      const rowY = y;

      // Number circle
      doc.circle(ML + 9, rowY + 7, 9).fill(NAVY);
      doc.font('Helvetica-Bold').fontSize(8).fill(WHITE)
         .text(String(i + 1), ML + 5.5, rowY + 4, { width: 7, align: 'center', lineBreak: false });

      // Timeline pill
      const pillW = doc.font('Helvetica-Bold').fontSize(7).widthOfString(label) + 14;
      doc.roundedRect(ML + 24, rowY + 1, pillW, 13, 3).fill(tc + '28');
      doc.font('Helvetica-Bold').fontSize(7).fill(tc)
         .text(label, ML + 28, rowY + 4, { width: pillW - 8, lineBreak: false });

      // Step text — NAVY not MUTED
      doc.font('Helvetica').fontSize(9).fill(NAVY)
         .text(text, ML + 24 + pillW + 8, rowY, { width: W - 24 - pillW - 8, lineGap: 2 });
      y = doc.y + 3;
      doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.4).stroke(BORDER);
      y += 9;
    });
    y += 8;

    // ── DEADLINES ─────────────────────────────────────────────────────────────
    if (r.deadlines && r.deadlines.length) {
      checkSpace(70);
      sectionLabel('Key deadlines');

      const dlColor = { red: RED, amber: AMBER, navy: NAVY };
      (r.deadlines).forEach(d => {
        checkSpace(22);
        const dc2 = dlColor[d.urgency] || NAVY;
        doc.font('Helvetica-Bold').fontSize(9).fill(dc2)
           .text(d.date, ML, y, { width: 100, lineBreak: false });
        doc.font('Helvetica').fontSize(9).fill(MUTED)
           .text(d.event, ML + 104, y, { width: W - 104, lineGap: 2 });
        y = Math.max(doc.y, y) + 3;
        doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.4).stroke(BORDER);
        y += 9;
      });
      y += 8;
    }

    // ── BOTTOM LINE ───────────────────────────────────────────────────────────
    checkSpace(72);
    sectionLabel('Bottom line');

    const blStartY = y;
    // Measure height
    doc.font('Helvetica-Bold').fontSize(10).fill(NAVY)
       .text(r.closing || '', ML + 14, y, { width: W - 14, lineGap: 3 });
    const blH = doc.y - blStartY + 20;

    // Draw background + left rule
    doc.rect(ML, blStartY, W, blH).fill('#edf0f7');
    doc.rect(ML, blStartY, 3.5, blH).fill(GOLD);

    // Redraw text over background
    doc.font('Helvetica-Bold').fontSize(10).fill(NAVY)
       .text(r.closing || '', ML + 14, blStartY, { width: W - 14, lineGap: 3 });
    y = blStartY + blH + 16;

    // ── AFFILIATE CARD ────────────────────────────────────────────────────────
    checkSpace(72);
    const affH = 60;
    doc.rect(ML, y, W, affH).fill(NAVY);
    doc.rect(ML, y, 3.5, affH).fill(GOLD);

    doc.font('Helvetica-Bold').fontSize(9.5).fill(GOLD)
       .text('Northwest Registered Agent', ML + 14, y + 10, { lineBreak: false });
    doc.font('Helvetica').fontSize(8.5).fill(WHITE).opacity(0.75)
       .text(
         'For LLC formation — handles the paperwork, keeps your personal address private, ' +
         'and includes registered agent service.',
         ML + 14, y + 26, { width: W - 90, lineGap: 2 }
       );
    doc.opacity(1);

    // CTA label on right
    doc.font('Helvetica-Bold').fontSize(8).fill(GOLD)
       .text('northwestregisteredagent.com →', ML, y + 24, { align: 'right', width: W - 14, lineBreak: false });

    y += affH + 16;

    // ── FOOTER on final page ──────────────────────────────────────────────────
    drawFooter();

    // ── FINALIZE ─────────────────────────────────────────────────────────────
    doc.end();

    await new Promise(resolve => doc.on('end', resolve));

    const pdfBuffer = Buffer.concat(chunks);

    res.setHeader('Content-Type', 'application/pdf');
    res.setHeader('Content-Disposition', 'attachment; filename="sidehustleguard-report.pdf"');
    res.setHeader('Content-Length', pdfBuffer.length);
    res.status(200).send(pdfBuffer);

  } catch (err) {
    console.error('PDF error:', err);
    res.status(500).json({ error: 'PDF generation failed', message: err.message });
  }
}
