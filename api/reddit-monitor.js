// Reddit Thread Monitor
// Triggered daily by GitHub Actions cron → emails a digest of fresh threads worth engaging

const QUERIES = [
  { q: 'side hustle taxes',               label: 'Side hustle taxes'      },
  { q: 'etsy taxes 1099',                 label: 'Etsy taxes / 1099'      },
  { q: 'do I need LLC side hustle',       label: 'LLC for side hustle'     },
  { q: 'quarterly taxes self employed',   label: 'Quarterly taxes'         },
  { q: 'freelancer taxes how much owe',   label: 'Freelancer taxes'        },
  { q: 'self employment tax calculator',  label: 'SE tax calculator'       },
];

const MIN_SCORE    = 3;   // minimum upvotes to include
const MIN_COMMENTS = 2;   // OR minimum comments to include
const MAX_AGE_HRS  = 36;  // only threads posted in the last 36 hours
const TOP_N        = 8;   // max threads in the digest

const SUGGESTED_LINKS = {
  'Side hustle taxes':    'sidehustleguard.com/tool or /side-hustle-taxes',
  'Etsy taxes / 1099':   'sidehustleguard.com/etsy-taxes or /paypal-1099k-etsy',
  'LLC for side hustle':  'sidehustleguard.com/llc-vs-sole-proprietor',
  'Quarterly taxes':      'sidehustleguard.com/quarterly-taxes-self-employed',
  'Freelancer taxes':     'sidehustleguard.com/freelancer-taxes',
  'SE tax calculator':    'sidehustleguard.com/self-employment-tax-calculator',
};

module.exports = async (req, res) => {
  // Simple auth check — set MONITOR_SECRET in Vercel env to lock it down
  const secret = process.env.MONITOR_SECRET;
  if (secret && req.headers['x-monitor-secret'] !== secret) {
    return res.status(401).json({ error: 'Unauthorized' });
  }

  const results = [];

  for (const { q, label } of QUERIES) {
    try {
      const url = `https://www.reddit.com/search.json?q=${encodeURIComponent(q)}&sort=new&t=day&limit=8&restrict_sr=false`;
      const r = await fetch(url, {
        headers: { 'User-Agent': 'SideHustleGuard-Monitor/1.0 (contact: richard@sidehustleguard.com)' },
      });
      if (!r.ok) continue;
      const data = await r.json();

      for (const post of data.data?.children ?? []) {
        const p = post.data;
        if (!p || p.is_self === false && p.score < MIN_SCORE) continue;

        const ageHrs = (Date.now() / 1000 - p.created_utc) / 3600;
        if (ageHrs > MAX_AGE_HRS) continue;
        if (p.score < MIN_SCORE && p.num_comments < MIN_COMMENTS) continue;

        results.push({
          label,
          title:     p.title,
          subreddit: p.subreddit_name_prefixed,
          url:       `https://reddit.com${p.permalink}`,
          score:     p.score,
          comments:  p.num_comments,
          ageHrs:    Math.round(ageHrs),
          link:      SUGGESTED_LINKS[label] ?? 'sidehustleguard.com/tool',
        });
      }
    } catch (e) {
      console.error(`Query "${q}" failed:`, e.message);
    }
  }

  // Deduplicate + sort by engagement
  const seen = new Set();
  const unique = results
    .filter(r => { if (seen.has(r.url)) return false; seen.add(r.url); return true; })
    .sort((a, b) => (b.score + b.comments * 3) - (a.score + a.comments * 3))
    .slice(0, TOP_N);

  // If no Resend key, return JSON (useful for testing: GET /api/reddit-monitor)
  const resendKey = process.env.RESEND_API_KEY;
  if (!resendKey) {
    return res.status(200).json({ threads: unique, note: 'Set RESEND_API_KEY to enable email delivery' });
  }

  if (unique.length === 0) {
    return res.status(200).json({ sent: false, reason: 'No qualifying threads found today' });
  }

  const emailRes = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${resendKey}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from:    'SideHustleGuard Monitor <onboarding@resend.dev>',
      to:      process.env.DIGEST_EMAIL ?? 'unpaidcomics@outlook.com',
      subject: `🔍 ${unique.length} Reddit threads worth engaging today`,
      html:    buildEmail(unique),
    }),
  });

  const emailData = await emailRes.json();
  return res.status(200).json({ sent: true, count: unique.length, resend: emailData });
};

function buildEmail(threads) {
  const rows = threads.map(t => `
    <tr>
      <td style="padding:16px 0;border-bottom:1px solid #e2e6ef;vertical-align:top">
        <div style="display:inline-block;background:#fdf5e8;color:#c9973a;font-size:11px;font-weight:600;padding:2px 8px;border-radius:100px;margin-bottom:6px;letter-spacing:.04em">${t.label}</div>
        <div style="font-size:12px;color:#9aa3b5;margin-bottom:4px">${t.subreddit} &nbsp;·&nbsp; ${t.score} pts &nbsp;·&nbsp; ${t.comments} comments &nbsp;·&nbsp; ${t.ageHrs}h ago</div>
        <div style="font-size:15px;font-weight:500;color:#1c2b4a;margin-bottom:8px;line-height:1.4">${escHtml(t.title)}</div>
        <a href="${t.url}" style="font-size:13px;color:#c9973a;text-decoration:none;margin-right:16px">View thread →</a>
        <span style="font-size:12px;color:#9aa3b5">Suggested: ${t.link}</span>
      </td>
    </tr>`).join('');

  return `
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#f0ece3;font-family:'DM Sans',Helvetica,Arial,sans-serif">
  <div style="max-width:600px;margin:32px auto;background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(28,43,74,.08)">
    <!-- Header -->
    <div style="background:#1c2b4a;padding:28px 32px;display:flex;align-items:center">
      <div style="width:6px;height:40px;background:#c9973a;border-radius:3px;margin-right:16px"></div>
      <div>
        <div style="font-size:18px;font-weight:700;color:#fff">SideHustle<span style="color:#c9973a">Guard</span></div>
        <div style="font-size:12px;color:rgba(255,255,255,.45);margin-top:2px">Daily Reddit Digest — ${new Date().toLocaleDateString('en-US',{weekday:'long',month:'long',day:'numeric'})}</div>
      </div>
    </div>
    <!-- Body -->
    <div style="padding:28px 32px">
      <p style="font-size:14px;color:#6b7a96;margin:0 0 20px;line-height:1.6">
        ${threads.length} fresh thread${threads.length !== 1 ? 's' : ''} worth a genuine, helpful reply today.
        Drop a real answer — the link is secondary. Aim for <strong style="color:#1c2b4a">1–2 comments max per day</strong> to stay authentic.
      </p>
      <table style="width:100%;border-collapse:collapse">
        ${rows}
      </table>
    </div>
    <!-- Tips -->
    <div style="background:#faf8f4;padding:20px 32px;border-top:1px solid #e2e6ef">
      <div style="font-size:11px;font-weight:600;color:#c9973a;letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px">Quick comment tip</div>
      <p style="font-size:13px;color:#6b7a96;margin:0;line-height:1.6">
        Answer the question fully first. Only add your link at the end as "I built a free tool for exactly this" — not as the lead.
        A comment that stands on its own will never get flagged.
      </p>
    </div>
    <!-- Footer -->
    <div style="padding:16px 32px;text-align:center;border-top:1px solid #e2e6ef">
      <span style="font-size:12px;color:#9aa3b5">SideHustleGuard · <a href="https://sidehustleguard.com" style="color:#c9973a;text-decoration:none">sidehustleguard.com</a></span>
    </div>
  </div>
</body>
</html>`;
}

function escHtml(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
