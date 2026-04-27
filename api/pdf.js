import PDFDocument from 'pdfkit';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const F = (name) => path.join(__dirname, '..', 'fonts', name);

// ── FONTS ─────────────────────────────────────────────────────────────────────
const FONT = {
  body:    F('DMSans-400.ttf'),
  medium:  F('DMSans-500.ttf'),
  semibold:F('DMSans-600.ttf'),
  bold:    F('DMSans-700.ttf'),
  serif:   F('PlayfairDisplay-700.ttf'),
};

// ── BRAND COLORS ──────────────────────────────────────────────────────────────
const NAVY    = '#1c2b4a';
const GOLD    = '#c9973a';
const GOLD_LT = '#ddb06a';
const CREAM   = '#faf8f4';
const CREAMD  = '#f0ece3';
const WHITE   = '#ffffff';
const MUTED   = '#6b7a96';
const DIM     = '#9aa3b5';
const BORDER  = '#e2e8f0';
const GREEN   = '#276944';
const RED     = '#b83232';
const AMBER   = '#a86c0a';

const RISK_COLOR = { Low: GREEN,       Moderate: AMBER,     High: RED };
const RISK_BG    = { Low: '#f0f9f4',   Moderate: '#fdf7ed', High: '#fdf1f1' };
const DOT_COLOR  = { red: RED,         amber: AMBER,        green: GREEN };
const TL_COLOR   = { 'This week': RED, 'This month': AMBER, 'Ongoing': NAVY };
const TL_BG      = { 'This week': '#fdf1f1', 'This month': '#fdf7ed', 'Ongoing': '#edf0f7' };

async function verifyStripeSession(sessionId) {
  if (!sessionId || typeof sessionId !== 'string') return false;
  if (!/^cs_(test|live)_[A-Za-z0-9_]+$/.test(sessionId)) return false;
  if (!process.env.STRIPE_SECRET_KEY) return false;
  try {
    const resp = await fetch(
      `https://api.stripe.com/v1/checkout/sessions/${encodeURIComponent(sessionId)}`,
      { headers: { Authorization: `Bearer ${process.env.STRIPE_SECRET_KEY}` } }
    );
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
      margins: { top: 72, bottom: 56, left: 56, right: 56 },
      info: {
        Title:   'SideHustleGuard Compliance & Tax Report',
        Author:  'SideHustleGuard',
        Subject: 'Side hustle compliance and tax analysis',
      },
    });

    doc.on('data', chunk => chunks.push(chunk));

    const PW = doc.page.width;
    const PH = doc.page.height;
    const ML = 56;
    const W  = PW - ML * 2;
    let   y  = 76;
    let   pageNum = 1;

    // ── SHIELD LOGO HELPER ────────────────────────────────────────────────────
    function drawShield(x, sy, scale) {
      const ox = x - 4 * scale;
      const oy = sy - 2 * scale;
      doc.save();
      doc.transform(scale, 0, 0, scale, ox, oy);
      doc.path('M18 2L4 6.5V19C4 28 10.5 35.5 18 38C25.5 35.5 32 28 32 19V6.5L18 2Z')
         .lineWidth(3).fillAndStroke(CREAM, NAVY);
      doc.path('M11 19.5L16 24.5L26 13.5')
         .lineWidth(4.5).lineCap('round').lineJoin('round').stroke(GOLD);
      doc.restore();
    }
    function shieldSize(scale) {
      return { w: (32 - 4) * scale, h: (38 - 2) * scale };
    }

    // ── CARD HELPER ───────────────────────────────────────────────────────────
    function drawCard(x, cy, w, h, radius, bgColor, accentColor, accentW = 4) {
      doc.save();
      doc.roundedRect(x, cy, w, h, radius).clip();
      doc.rect(x, cy, w, h).fillColor(bgColor).fill();
      if (accentColor) doc.rect(x, cy, accentW, h).fillColor(accentColor).fill();
      doc.restore();
    }

    // ── FOOTER ────────────────────────────────────────────────────────────────
    function drawFooter() {
      const bm = doc.page.margins.bottom;
      doc.page.margins.bottom = 0;
      const fy = PH - 28;
      doc.rect(0, fy, PW, 28).fill(CREAMD);
      doc.moveTo(0, fy).lineTo(PW, fy).lineWidth(0.5).strokeColor(BORDER).stroke();
      doc.font(FONT.body).fontSize(6.5).fillColor(DIM)
         .text(
           'Educational purposes only — not legal or tax advice. Consult a licensed CPA or attorney.',
           ML, fy + 9, { lineBreak: false, width: W - 80 }
         );
      doc.font(FONT.body).fontSize(6.5).fillColor(DIM)
         .text(
           `sidehustleguard.com  ·  p. ${pageNum}`,
           ML, fy + 9, { align: 'right', width: W, lineBreak: false }
         );
      doc.page.margins.bottom = bm;
    }

    // ── CONTINUATION HEADER ───────────────────────────────────────────────────
    function drawContinuationHeader() {
      pageNum++;
      const CH = 36;
      const CS = 0.42;
      const csz = shieldSize(CS);
      doc.rect(0, 0, PW, CH).fillColor(NAVY).fill();
      doc.rect(0, CH, PW, 2.5).fillColor(GOLD).fill();
      doc.rect(0, CH + 2.5, 3, PH - CH - 2.5 - 28).fillColor(GOLD).fill();
      const cShieldTop = (CH - csz.h) / 2;
      drawShield(ML, cShieldTop, CS);
      const wmX2 = ML + csz.w + 7;
      const wmY2 = (CH - 11) / 2 - 1;
      doc.font(FONT.bold).fontSize(11).fillColor(WHITE)
         .text('SideHustle', wmX2, wmY2, { continued: true });
      doc.fillColor(GOLD).text('Guard', { continued: false });
      doc.font(FONT.body).fontSize(7).fillColor(DIM)
         .text(
           `${r.client || 'Your Report'}  ·  Confidential`,
           ML, wmY2 + 1, { align: 'right', width: W, lineBreak: false }
         );
      y = CH + 2.5 + 18;
    }

    // ── SPACE CHECK ───────────────────────────────────────────────────────────
    function checkSpace(needed) {
      if (y + needed > PH - 68) {
        drawFooter();
        doc.addPage();
        drawContinuationHeader();
      }
    }

    // ── SECTION LABEL ─────────────────────────────────────────────────────────
    function sectionLabel(text) {
      checkSpace(30);
      doc.font(FONT.semibold).fontSize(7).fillColor(GOLD)
         .text(text.toUpperCase(), ML, y, { characterSpacing: 1.2 });
      y += 13;
      doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.5).strokeColor(BORDER).stroke();
      y += 11;
    }

    // ── PAGE 1 HEADER ─────────────────────────────────────────────────────────
    const HDR_H    = 66;
    const SCALE_P1 = 0.58;
    const SZ       = shieldSize(SCALE_P1);

    doc.rect(0, 0, PW, HDR_H).fillColor(NAVY).fill();
    doc.rect(0, HDR_H, PW, 3).fillColor(GOLD).fill();
    doc.rect(0, HDR_H + 3, 3, PH - HDR_H - 3 - 28).fillColor(GOLD).fill();

    const shieldTop = (HDR_H - SZ.h) / 2;
    drawShield(ML, shieldTop, SCALE_P1);

    const wmX = ML + SZ.w + 9;
    const wmY = (HDR_H - 15) / 2 - 1;
    doc.font(FONT.bold).fontSize(15).fillColor(WHITE)
       .text('SideHustle', wmX, wmY, { continued: true });
    doc.fillColor(GOLD).text('Guard', { continued: false });

    const badgeLabel = 'Compliance & Tax Report';
    const badgeW = doc.font(FONT.semibold).fontSize(8).widthOfString(badgeLabel) + 20;
    const badgeH = 22;
    const badgeX = ML + W - badgeW;
    const badgeY = (HDR_H - badgeH) / 2;
    doc.roundedRect(badgeX, badgeY, badgeW, badgeH, 11)
       .fillColor('rgba(255,255,255,0.10)').fill();
    doc.roundedRect(badgeX, badgeY, badgeW, badgeH, 11)
       .lineWidth(0.75).strokeColor('rgba(255,255,255,0.20)').stroke();
    doc.font(FONT.semibold).fontSize(8).fillColor(WHITE).opacity(0.80)
       .text(badgeLabel, badgeX, badgeY + (badgeH - 8) / 2,
             { width: badgeW, align: 'center', lineBreak: false });
    doc.opacity(1);

    // ── INFO STRIP ────────────────────────────────────────────────────────────
    const STRIP_Y = HDR_H + 3;
    const STRIP_H = 38;
    doc.rect(0, STRIP_Y, PW, STRIP_H).fillColor(CREAMD).fill();
    doc.moveTo(0, STRIP_Y + STRIP_H).lineTo(PW, STRIP_Y + STRIP_H)
       .lineWidth(0.5).strokeColor(BORDER).stroke();

    const rc0 = RISK_COLOR[r.risk_level] || AMBER;
    doc.font(FONT.semibold).fontSize(7).fillColor(MUTED)
       .text('OVERALL RISK', ML + 10, STRIP_Y + 8, { characterSpacing: 0.8, lineBreak: false });
    doc.font(FONT.bold).fontSize(11).fillColor(rc0)
       .text((r.risk_level || 'Moderate').toUpperCase(), ML + 10, STRIP_Y + 18, { lineBreak: false });

    doc.moveTo(ML + 110, STRIP_Y + 8).lineTo(ML + 110, STRIP_Y + STRIP_H - 8)
       .lineWidth(0.5).strokeColor(BORDER).stroke();

    doc.font(FONT.semibold).fontSize(7).fillColor(MUTED)
       .text('REPORT TYPE', ML + 122, STRIP_Y + 8, { characterSpacing: 0.8, lineBreak: false });
    doc.font(FONT.body).fontSize(10).fillColor(NAVY)
       .text('Tax & Compliance', ML + 122, STRIP_Y + 18, { lineBreak: false });

    doc.moveTo(ML + 280, STRIP_Y + 8).lineTo(ML + 280, STRIP_Y + STRIP_H - 8)
       .lineWidth(0.5).strokeColor(BORDER).stroke();

    doc.font(FONT.semibold).fontSize(7).fillColor(MUTED)
       .text('CLASSIFICATION', ML + 292, STRIP_Y + 8, { characterSpacing: 0.8, lineBreak: false });
    doc.font(FONT.body).fontSize(10).fillColor(NAVY)
       .text(r.client || 'Your Report', ML + 292, STRIP_Y + 18, { lineBreak: false });

    y = STRIP_Y + STRIP_H + 20;

    // ── OVERALL RISK ──────────────────────────────────────────────────────────
    const rc = RISK_COLOR[r.risk_level] || AMBER;
    const rb = RISK_BG[r.risk_level]   || '#fdf7ed';

    drawCard(ML, y, W, 58, 6, rb, rc, 4);

    doc.font(FONT.semibold).fontSize(7.5).fillColor(rc)
       .text('OVERALL RISK', ML + 16, y + 10, { characterSpacing: 0.8 });
    doc.font(FONT.serif).fontSize(24).fillColor(rc)
       .text((r.risk_level || 'Moderate').toUpperCase(), ML + 16, y + 20);
    doc.font(FONT.body).fontSize(9.5).fillColor(NAVY)
       .text(r.opening || '', ML + 152, y + 11, { width: W - 158, lineGap: 3 });

    y += 72;

    // ── KEY INSIGHT ───────────────────────────────────────────────────────────
    checkSpace(80);
    sectionLabel("What most people in your position don't realize");

    const insightX = ML + 16;
    const insightW = W - 16;
    doc.font(FONT.bold).fontSize(10).fillColor(NAVY)
       .text(r.key_insight || '', insightX, y, { width: insightW, lineGap: 3 });
    const insightBottom = doc.y;
    const insightH = insightBottom - y + 10;

    doc.rect(ML, y - 2, 3, insightH + 4).fillColor(GOLD).fill();
    doc.font(FONT.bold).fontSize(10).fillColor(NAVY)
       .text(r.key_insight || '', insightX, y, { width: insightW, lineGap: 3 });

    y = insightBottom + 16;

    // ── QUICK WINS ────────────────────────────────────────────────────────────
    checkSpace(100);
    sectionLabel('Fastest way to reduce your risk (under 1 hour)');

    const qwY = y;

    // Pass 1: measure height
    y += 12;
    (r.quick_wins || []).forEach((win) => {
      doc.font(FONT.bold).fontSize(9.5).fillColor(NAVY)
         .text(win, ML + 38, y, { width: W - 38 });
      y = doc.y + 8;
    });
    if (r.quick_wins_note) {
      doc.font(FONT.bold).fontSize(9).fillColor(GREEN)
         .text(r.quick_wins_note, ML + 38, y, { width: W - 38 });
      y = doc.y + 6;
    }
    const qwH = y - qwY + 10;

    drawCard(ML, qwY, W, qwH, 6, '#eef7f2', GREEN, 4);

    // Pass 2: redraw content
    y = qwY + 12;
    (r.quick_wins || []).forEach((win, i) => {
      doc.circle(ML + 22, y + 7, 9).fillColor(NAVY).fill();
      doc.font(FONT.bold).fontSize(8.5).fillColor(WHITE)
         .text(String(i + 1), ML + 18, y + 4, { width: 9, align: 'center', lineBreak: false });
      doc.font(FONT.bold).fontSize(9.5).fillColor(NAVY)
         .text(win, ML + 36, y, { width: W - 40 });
      y = doc.y + 8;
    });
    if (r.quick_wins_note) {
      doc.font(FONT.bold).fontSize(9).fillColor(GREEN)
         .text(r.quick_wins_note, ML + 36, y, { width: W - 40 });
      y = doc.y + 6;
    }
    y += 14;

    // ── WHAT STANDS OUT ───────────────────────────────────────────────────────
    checkSpace(80);
    sectionLabel('What stands out');

    (r.issues || []).forEach((issue, idx) => {
      checkSpace(50);
      const dc = DOT_COLOR[issue.status] || AMBER;
      const isLast = idx === (r.issues.length - 1);

      doc.circle(ML + 5, y + 7, 4.5).fillColor(dc).fill();
      doc.font(FONT.bold).fontSize(9.5).fillColor(NAVY)
         .text(issue.title, ML + 16, y, { width: W - 16 });
      y = doc.y + 3;
      doc.font(FONT.body).fontSize(9).fillColor(MUTED)
         .text(issue.detail, ML + 16, y, { width: W - 16, lineGap: 2.5 });
      y = doc.y + 5;
      if (!isLast) {
        doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.4).strokeColor(BORDER).stroke();
        y += 9;
      }
    });
    y += 14;

    // ── TAX REALITY ───────────────────────────────────────────────────────────
    checkSpace(120);
    sectionLabel('Tax reality');

    const bw = (W - 12) / 2;
    const bh = 54;

    drawCard(ML, y, bw, bh, 6, '#fdf2f2', RED, 4);
    doc.font(FONT.body).fontSize(7.5).fillColor(DIM)
       .text('Effective rate', ML + 14, y + 10, { lineBreak: false });
    doc.font(FONT.serif).fontSize(22).fillColor(RED)
       .text(r.tax_rate || '—', ML + 14, y + 22);

    const bx2 = ML + bw + 12;
    drawCard(bx2, y, bw, bh, 6, '#fdf8ed', AMBER, 4);
    doc.font(FONT.body).fontSize(7.5).fillColor(DIM)
       .text('Est. tax owed (yr 1)', bx2 + 14, y + 10, { lineBreak: false });
    doc.font(FONT.serif).fontSize(20).fillColor(AMBER)
       .text(r.tax_owed_est || '—', bx2 + 14, y + 23);

    y += bh + 14;

    if (r.tax_note) {
      checkSpace(52);
      doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.5).strokeColor(BORDER).stroke();
      y += 11;
      doc.font(FONT.bold).fontSize(8.5).fillColor(AMBER)
         .text('What people usually get wrong:', ML, y, { lineBreak: false });
      y += 15;
      doc.font(FONT.body).fontSize(9).fillColor(NAVY)
         .text(r.tax_note, ML + 10, y, { width: W - 10, lineGap: 2.5 });
      y = doc.y + 16;
    }

    // ── WHAT'S WORKING ────────────────────────────────────────────────────────
    checkSpace(70);
    sectionLabel("What you're doing right");

    (r.working || []).forEach((item, idx) => {
      checkSpace(26);
      const isLast = idx === (r.working.length - 1);
      doc.font(FONT.bold).fontSize(13).fillColor(GREEN)
         .text('•', ML + 1, y - 1, { lineBreak: false });
      doc.font(FONT.body).fontSize(9).fillColor(NAVY)
         .text(item, ML + 16, y, { width: W - 16, lineGap: 2.5 });
      y = doc.y + 5;
      if (!isLast) {
        doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.4).strokeColor(BORDER).stroke();
        y += 8;
      }
    });
    y += 14;

    // ── ACTION PLAN ───────────────────────────────────────────────────────────
    checkSpace(90);
    sectionLabel('What to do next');

    (r.action_plan || []).forEach((step, i) => {
      checkSpace(52);
      const label    = step.timeline || 'Ongoing';
      const text     = step.step || step;
      const tc       = TL_COLOR[label] || NAVY;
      const tbg      = TL_BG[label]    || '#edf0f7';
      const rowY     = y;
      const isLast   = i === (r.action_plan.length - 1);
      const contentX = ML + 28;
      const contentW = W - 28;

      doc.circle(ML + 9, rowY + 9, 9.5).fillColor(NAVY).fill();
      doc.font(FONT.bold).fontSize(8.5).fillColor(WHITE)
         .text(String(i + 1), ML + 5, rowY + 6, { width: 9, align: 'center', lineBreak: false });

      const pillW = doc.font(FONT.semibold).fontSize(7).widthOfString(label) + 16;
      doc.roundedRect(contentX, rowY, pillW, 14, 3).fillColor(tbg).fill();
      doc.font(FONT.semibold).fontSize(7).fillColor(tc)
         .text(label, contentX + 5, rowY + 4, { width: pillW - 10, lineBreak: false });

      doc.font(FONT.body).fontSize(9).fillColor(NAVY)
         .text(text, contentX, rowY + 19, { width: contentW, lineGap: 2.5 });
      y = doc.y + 6;

      if (!isLast) {
        doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.4).strokeColor(BORDER).stroke();
        y += 10;
      }
    });
    y += 16;

    // ── DEADLINES ─────────────────────────────────────────────────────────────
    if (r.deadlines && r.deadlines.length) {
      checkSpace(80);
      sectionLabel('Key deadlines');

      const dlColor = { red: RED, amber: AMBER, navy: NAVY };
      r.deadlines.forEach((d, idx) => {
        checkSpace(24);
        const isLast = idx === (r.deadlines.length - 1);
        const dc2    = dlColor[d.urgency] || NAVY;
        doc.font(FONT.bold).fontSize(9).fillColor(dc2)
           .text(d.date, ML, y, { width: 96, lineBreak: false });
        doc.font(FONT.body).fontSize(9).fillColor(MUTED)
           .text(d.event, ML + 100, y, { width: W - 100, lineGap: 2 });
        y = Math.max(doc.y, y) + 4;
        if (!isLast) {
          doc.moveTo(ML, y).lineTo(ML + W, y).lineWidth(0.4).strokeColor(BORDER).stroke();
          y += 9;
        }
      });
      y += 16;
    }

    // ── BOTTOM LINE ───────────────────────────────────────────────────────────
    checkSpace(80);
    sectionLabel('Bottom line');

    const blY = y;
    doc.font(FONT.serif).fontSize(10.5).fillColor(NAVY)
       .text(r.closing || '', ML + 16, y, { width: W - 16, lineGap: 3.5 });
    const blH = doc.y - blY + 18;

    drawCard(ML, blY - 4, W, blH + 4, 6, '#edf0f7', GOLD, 4);

    doc.font(FONT.serif).fontSize(10.5).fillColor(NAVY)
       .text(r.closing || '', ML + 16, blY, { width: W - 16, lineGap: 3.5 });

    y = blY + blH + 20;

    // ── AFFILIATE CARD ────────────────────────────────────────────────────────
    checkSpace(72);
    const affH = 62;
    drawCard(ML, y, W, affH, 8, NAVY, GOLD, 4);

    doc.font(FONT.bold).fontSize(9.5).fillColor(GOLD_LT)
       .text('Northwest Registered Agent', ML + 16, y + 13, { lineBreak: false });
    doc.font(FONT.semibold).fontSize(8).fillColor(GOLD_LT)
       .text('northwestregisteredagent.com →', ML + 16, y + 15,
             { align: 'right', width: W - 32, lineBreak: false });
    doc.font(FONT.body).fontSize(8.5).fillColor(WHITE).opacity(0.65)
       .text(
         'For LLC formation — handles the paperwork, keeps your personal address private, and includes registered agent service.',
         ML + 16, y + 31, { width: W - 32, lineGap: 2 }
       );
    doc.opacity(1);

    y += affH + 12;

    // ── FOOTER (final page) ───────────────────────────────────────────────────
    drawFooter();

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
