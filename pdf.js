import PDFDocument from 'pdfkit';

// ── BRAND COLORS (RGB) ────────────────────────────────────────────────────────
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

// Risk colors
const RISK_COLOR = { Low: GREEN, Moderate: AMBER, High: RED };
const RISK_BG    = { Low: '#eaf5ef', Moderate: '#fef6e8', High: '#fdf0f0' };
const DOT_COLOR  = { red: RED, amber: AMBER, green: GREEN };

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
  // Accept either { session_id, report } or legacy: full report at top level + ?session_id query
  const r = report || body;
  const sid = session_id || (req.query && req.query.session_id);

  if (!r || !r.risk_level) return res.status(400).json({ error: 'Missing report data' });

  const paid = await verifyStripeSession(sid);
  if (!paid) return res.status(402).json({ error: 'Payment required' });

  try {
    const chunks = [];
    const doc = new PDFDocument({
      size: 'LETTER',
      margins: { top: 72, bottom: 56, left: 56, right: 56 },
      info: { Title: 'SideHustleGuard Compliance Report', Author: 'SideHustleGuard' }
    });

    doc.on('data', chunk => chunks.push(chunk));

    const W = doc.page.width - 56 - 56;  // usable width
    const ML = 56;                         // left margin

    // ── HEADER ────────────────────────────────────────────────────────────────
    // Navy bar
    doc.rect(0, 0, doc.page.width, 52).fill(NAVY);
    // Gold accent
    doc.rect(0, 52, doc.page.width, 2).fill(GOLD);

    // Wordmark
    doc.font('Helvetica-Bold').fontSize(14).fill(WHITE)
       .text('SideHustle', ML, 18, { continued: true });
    doc.fill(GOLD).text('Guard');

    // Right side label
    doc.font('Helvetica').fontSize(7.5).fill(DIM)
       .text('Compliance & Tax Report', ML, 20, { align: 'right', width: W });
    doc.font('Helvetica').fontSize(7).fill(WHITE)
       .text(`${r.client || 'Your Report'}  ·  Confidential`, ML, 30, { align: 'right', width: W });

    // Gold left rule (full page height approximation — we'll draw it at the end)
    doc.rect(0, 54, 3, doc.page.height - 54 - 28).fill(GOLD);

    let y = 72;

    // ── HELPER: section label ─────────────────────────────────────────────────
    function sectionLabel(text) {
      doc.font('Helvetica-Bold').fontSize(7).fill(GOLD)
         .text(text.toUpperCase(), ML, y, { characterSpacing: 1 });
      y += 12;
      doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.5).stroke(BORDER);
      y += 10;
    }

    function checkSpace(needed) {
      if (y + needed > doc.page.height - 80) {
        doc.addPage();
        // Repeat thin header on new page
        doc.rect(0, 0, doc.page.width, 28).fill(NAVY);
        doc.rect(0, 28, doc.page.width, 2).fill(GOLD);
        doc.rect(0, 30, 3, doc.page.height - 30 - 28).fill(GOLD);
        doc.font('Helvetica-Bold').fontSize(9).fill(WHITE)
           .text('SideHustleGuard', ML, 9, { continued: true });
        doc.fill(GOLD).text('Guard', { continued: false });
        doc.font('Helvetica').fontSize(7).fill(DIM)
           .text(`${r.client || ''}  ·  sidehustleguard.com`, ML, 10, { align: 'right', width: W });
        y = 50;
      }
    }

    function wrapText(text, font, size, color, indent, maxW) {
      doc.font(font).fontSize(size).fill(color);
      doc.text(text, ML + indent, y, { width: maxW || (W - indent), lineGap: 2 });
      y = doc.y + 6;
    }

    // ── OVERALL RISK ──────────────────────────────────────────────────────────
    const rc = RISK_COLOR[r.risk_level] || AMBER;
    const rb = RISK_BG[r.risk_level]   || '#fef6e8';

    doc.rect(ML, y, W, 48).fill(rb);
    doc.rect(ML, y, 3.5, 48).fill(rc);

    doc.font('Helvetica-Bold').fontSize(7.5).fill(rc)
       .text('OVERALL RISK', ML + 14, y + 8, { characterSpacing: 0.8 });
    doc.font('Helvetica-Bold').fontSize(18).fill(rc)
       .text((r.risk_level || 'Moderate').toUpperCase(), ML + 14, y + 18);

    // Opening line
    const openingW = W - 140;
    doc.font('Helvetica').fontSize(9.5).fill(NAVY)
       .text(r.opening || '', ML + 140, y + 10, { width: openingW, lineGap: 2 });

    y += 58;

    // ── KEY INSIGHT ───────────────────────────────────────────────────────────
    checkSpace(70);
    sectionLabel("What most people in your position don't realize");

    doc.rect(ML, y, 3, 999).fill(GOLD);  // placeholder, clip later
    const insightY = y;
    doc.font('Helvetica-Bold').fontSize(10).fill(NAVY)
       .text(r.key_insight || '', ML + 12, y, { width: W - 12, lineGap: 3 });
    y = doc.y + 8;
    // Draw actual left rule
    doc.rect(ML, insightY, 3, y - insightY - 8).fill(GOLD);

    // ── QUICK WINS ────────────────────────────────────────────────────────────
    checkSpace(80);
    sectionLabel('Fastest way to reduce your risk (under 1 hour)');

    const qwBg = '#eaf5ef';
    const qwY = y;
    doc.rect(ML, y, W, 8).fill(qwBg); // top pad
    y += 10;

    (r.quick_wins || []).forEach((win, i) => {
      checkSpace(24);
      // Circle number
      doc.circle(ML + 10, y + 5.5, 7).fill(GOLD);
      doc.font('Helvetica-Bold').fontSize(8).fill(WHITE)
         .text(String(i + 1), ML + 7, y + 2, { width: 7, align: 'center' });
      doc.font('Helvetica-Bold').fontSize(9.5).fill(NAVY)
         .text(win, ML + 22, y, { width: W - 22 });
      y = doc.y + 6;
    });

    if (r.quick_wins_note) {
      doc.font('Helvetica-Bold').fontSize(9).fill(GREEN)
         .text(r.quick_wins_note, ML + 10, y, { width: W - 10 });
      y = doc.y + 6;
    }

    doc.rect(ML, qwY, W, y - qwY + 6).fill(qwBg);
    doc.rect(ML, qwY, 3, y - qwY + 6).fill(GREEN);

    // Redraw text over background
    y = qwY + 10;
    (r.quick_wins || []).forEach((win, i) => {
      doc.circle(ML + 10, y + 5.5, 7).fill(GOLD);
      doc.font('Helvetica-Bold').fontSize(8).fill(WHITE)
         .text(String(i + 1), ML + 7, y + 2, { width: 7, align: 'center' });
      doc.font('Helvetica-Bold').fontSize(9.5).fill(NAVY)
         .text(win, ML + 22, y, { width: W - 22 });
      y = doc.y + 6;
    });
    if (r.quick_wins_note) {
      doc.font('Helvetica-Bold').fontSize(9).fill(GREEN)
         .text(r.quick_wins_note, ML + 10, y, { width: W - 10 });
      y = doc.y + 6;
    }
    y += 12;

    // ── WHAT STANDS OUT ───────────────────────────────────────────────────────
    checkSpace(80);
    sectionLabel('What stands out');

    (r.issues || r.stands_out || []).forEach(issue => {
      checkSpace(44);
      const title  = issue.title  || issue[1] || '';
      const body   = issue.detail || issue.body || issue[2] || '';
      const status = issue.status || (issue[0] === true ? 'red' : 'amber');
      const dc = DOT_COLOR[status] || AMBER;

      doc.circle(ML + 4, y + 5, 3.5).fill(dc);
      doc.font('Helvetica-Bold').fontSize(9.5).fill(NAVY)
         .text(title, ML + 12, y, { width: W - 12 });
      y = doc.y + 2;
      doc.font('Helvetica').fontSize(9).fill(MUTED)
         .text(body, ML + 12, y, { width: W - 12, lineGap: 2 });
      y = doc.y + 2;
      doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.4).stroke(BORDER);
      y += 8;
    });
    y += 4;

    // ── TAX REALITY ───────────────────────────────────────────────────────────
    checkSpace(100);
    sectionLabel('Tax reality');

    // Two stat boxes
    const boxW = (W - 8) / 2;
    doc.rect(ML, y, boxW, 46).fill('#fdf0f0');
    doc.font('Helvetica').fontSize(7.5).fill(DIM)
       .text('Effective rate', ML + 10, y + 8);
    doc.font('Helvetica-Bold').fontSize(20).fill(RED)
       .text(r.tax_rate || '—', ML + 10, y + 18);

    doc.rect(ML + boxW + 8, y, boxW, 46).fill('#fef6e8');
    doc.font('Helvetica').fontSize(7.5).fill(DIM)
       .text('Est. tax owed (yr 1)', ML + boxW + 18, y + 8);
    doc.font('Helvetica-Bold').fontSize(16).fill(AMBER)
       .text(r.tax_owed_est || '—', ML + boxW + 18, y + 20);

    y += 56;

    if (r.tax_note) {
      doc.rect(ML, y, W, 1).fill(BORDER);
      y += 8;
      doc.font('Helvetica-Bold').fontSize(8.5).fill(AMBER)
         .text('What people usually get wrong:', ML, y);
      y += 13;
      doc.font('Helvetica').fontSize(9).fill(NAVY)
         .text(r.tax_note, ML + 12, y, { width: W - 12, lineGap: 2 });
      y = doc.y + 12;
    }

    // ── WHAT'S WORKING ────────────────────────────────────────────────────────
    checkSpace(60);
    sectionLabel("What you're doing right");

    (r.working || []).forEach(item => {
      checkSpace(20);
      doc.font('Helvetica-Bold').fontSize(10).fill(GREEN)
         .text('✓', ML, y);
      doc.font('Helvetica').fontSize(9).fill(NAVY)
         .text(item, ML + 14, y, { width: W - 14, lineGap: 2 });
      y = doc.y + 4;
      doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.4).stroke(BORDER);
      y += 6;
    });
    y += 6;

    // ── ACTION PLAN ───────────────────────────────────────────────────────────
    checkSpace(80);
    sectionLabel('What to do next');

    const tlColor = { 'This week': RED, 'This month': AMBER, 'Ongoing': NAVY };

    (r.action_plan || []).forEach((step, i) => {
      checkSpace(30);
      const label = step.timeline || 'Ongoing';
      const text  = step.step || step;
      const tc = tlColor[label] || NAVY;

      // Number badge
      doc.circle(ML + 9, y + 6, 9).fill(NAVY);
      doc.font('Helvetica-Bold').fontSize(8).fill(WHITE)
         .text(String(i + 1), ML + 5, y + 3, { width: 9, align: 'center' });

      // Timeline pill
      const pillW = doc.font('Helvetica-Bold').fontSize(7).widthOfString(label) + 12;
      doc.roundedRect(ML + 22, y + 1, pillW, 13, 3).fill(tc + '22');
      doc.font('Helvetica-Bold').fontSize(7).fill(tc)
         .text(label, ML + 27, y + 4, { width: pillW });

      // Step text
      doc.font('Helvetica').fontSize(9).fill(MUTED)
         .text(text, ML + 22 + pillW + 6, y, { width: W - 22 - pillW - 6, lineGap: 2 });
      y = doc.y + 2;
      doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.4).stroke(BORDER);
      y += 8;
    });
    y += 6;

    // ── DEADLINES ─────────────────────────────────────────────────────────────
    checkSpace(70);
    sectionLabel('Key deadlines');

    const dlColor = { red: RED, amber: AMBER, navy: NAVY };
    (r.deadlines || []).forEach(d => {
      checkSpace(20);
      const dc2 = dlColor[d.urgency] || NAVY;
      doc.font('Helvetica-Bold').fontSize(9).fill(dc2)
         .text(d.date, ML, y, { width: 95 });
      doc.font('Helvetica').fontSize(9).fill(MUTED)
         .text(d.event, ML + 100, y, { width: W - 100 });
      y = Math.max(doc.y, y) + 2;
      doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.4).stroke(BORDER);
      y += 8;
    });
    y += 6;

    // ── BOTTOM LINE ───────────────────────────────────────────────────────────
    checkSpace(60);
    sectionLabel('Bottom line');

    const blY = y;
    doc.font('Helvetica-Bold').fontSize(10).fill(NAVY)
       .text(r.closing || '', ML + 12, y, { width: W - 12, lineGap: 3 });
    const blH = doc.y - blY + 16;
    doc.rect(ML, blY, W, blH).fill('#edf0f7');
    doc.rect(ML, blY, 3.5, blH).fill(GOLD);
    doc.font('Helvetica-Bold').fontSize(10).fill(NAVY)
       .text(r.closing || '', ML + 12, blY, { width: W - 12, lineGap: 3 });
    y = blY + blH + 10;

    // ── AFFILIATE ─────────────────────────────────────────────────────────────
    checkSpace(55);
    doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(2).stroke(GOLD);
    y += 10;
    doc.font('Helvetica-Bold').fontSize(9.5).fill(GOLD)
       .text('Northwest Registered Agent', ML, y);
    y += 14;
    doc.font('Helvetica').fontSize(8.5).fill(MUTED)
       .text(
         'For LLC formation — handles the paperwork, keeps your personal address private, ' +
         'and includes registered agent service.  northwestregisteredagent.com',
         ML, y, { width: W, lineGap: 2 }
       );
    y = doc.y + 14;

    // ── FOOTER ────────────────────────────────────────────────────────────────
    const footerY = doc.page.height - 28;
    doc.rect(0, footerY, doc.page.width, 28).fill(CREAMD);
    doc.font('Helvetica').fontSize(6.5).fill(DIM)
       .text(
         'Educational purposes only — not legal or tax advice. Consult a licensed CPA or attorney.',
         ML, footerY + 9
       );
    doc.text('sidehustleguard.com', ML, footerY + 9, { align: 'right', width: W });

    // ── FINALIZE ──────────────────────────────────────────────────────────────
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
