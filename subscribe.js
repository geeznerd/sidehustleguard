// SideHustleGuard — /api/subscribe
// Adds an email to the Kit form. Best-effort — if Kit fails, we still
// let the caller proceed (they should see their report regardless).
//
// Env vars required:
//   KIT_API_KEY    (V4 API key from Kit)

const FORM_ID = '9372241';
const ALLOWED_ORIGIN = 'https://www.sidehustleguard.com';
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

function setCors(req, res) {
  const origin = req.headers.origin || '';
  const ok =
    origin === ALLOWED_ORIGIN ||
    origin === 'https://sidehustleguard.com' ||
    /^http:\/\/localhost(:\d+)?$/.test(origin);
  res.setHeader('Access-Control-Allow-Origin', ok ? origin : ALLOWED_ORIGIN);
  res.setHeader('Vary', 'Origin');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
}

export default async function handler(req, res) {
  setCors(req, res);
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const body = req.body || {};
  const emailRaw = typeof body.email === 'string' ? body.email.trim().toLowerCase() : '';
  if (!emailRaw || !EMAIL_RE.test(emailRaw) || emailRaw.length > 254) {
    return res.status(400).json({ error: 'Invalid email' });
  }

  if (!process.env.KIT_API_KEY) {
    console.error('KIT_API_KEY not configured');
    // Don't tell the client our internal config is missing — just say it failed.
    return res.status(500).json({ error: 'Email service not configured' });
  }

  try {
    // Kit V3 API: subscribe to a form. V3 takes the api_key in the JSON body.
    const r = await fetch(`https://api.convertkit.com/v3/forms/${FORM_ID}/subscribe`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        api_key: process.env.KIT_API_KEY,
        email: emailRaw,
      }),
    });

    if (!r.ok) {
      const text = await r.text().catch(() => '');
      console.error('Kit subscribe error:', r.status, text.slice(0, 500));
      return res.status(502).json({ error: 'Subscription failed', code: r.status });
    }

    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error('Subscribe handler error:', err);
    return res.status(500).json({ error: 'Server error' });
  }
}
