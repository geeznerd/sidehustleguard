// SideHustleGuard — /api/check
// Free tier: returns risk + scores + top 3 issues (titles only, details locked).
// Paid tier: requires a verified Stripe Checkout Session id; returns full report.
//
// Env vars required:
//   ANTHROPIC_API_KEY       (existing)
//   STRIPE_SECRET_KEY       (NEW — sk_live_... or sk_test_...)

const ALLOWED_ORIGIN = 'https://www.sidehustleguard.com';

const PAID_FIELDS = [
  'key_insight',
  'quick_wins',
  'quick_wins_note',
  'tax_rate',
  'tax_owed_est',
  'tax_note',
  'working',
  'action_plan',
  'deadlines',
  'closing',
];

function setCors(req, res) {
  const origin = req.headers.origin || '';
  // In prod, only allow your domain. In dev, also allow localhost.
  const ok =
    origin === ALLOWED_ORIGIN ||
    origin === 'https://sidehustleguard.com' ||
    /^http:\/\/localhost(:\d+)?$/.test(origin);
  res.setHeader('Access-Control-Allow-Origin', ok ? origin : ALLOWED_ORIGIN);
  res.setHeader('Vary', 'Origin');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
}

function buildPrompt(answers) {
  const a = answers || {};
  const PAY = ['Etsy marketplace','PayPal','Venmo or Cash App','Direct invoice to clients','Cash','Stripe or own website'];
  const extras = Array.isArray(a.extras) ? a.extras : [];
  const pays = extras.filter(e => PAY.includes(e)).join(', ') || 'not specified';
  const ctx  = extras.filter(e => !PAY.includes(e)).join(', ') || 'none';

  return `You are a tax and compliance advisor for US side hustlers. Return ONLY valid JSON. No markdown. No extra text before or after the JSON.

Hustle: ${a.type || 'not specified'}
Description: ${a.desc || 'not provided'}
State: ${a.state || 'not specified'}
Income: ${a.income || 'not specified'}
Payment methods: ${pays}
Bank account: ${a.bank || 'not specified'}
Registration: ${a.reg || 'not specified'}
Other context: ${ctx}

Rules: Write like a direct human advisor. Short sentences. Specific to this person. No fluff. No AI-sounding phrases.

Return this exact JSON:
{
  "risk_level": "Low|Moderate|High",
  "opening": "<1 sentence — what happens if ignored. Specific.>",
  "key_insight": "<2 sentences max — what they probably don't realize. Advisor tone.>",
  "tax_status": "Good|Fair|At Risk",
  "structure_status": "Good|Fair|At Risk",
  "compliance_status": "Good|Fair|At Risk",
  "quick_wins": ["<short action>", "<short action>", "<short action>"],
  "quick_wins_note": "<1 sentence — what doing these achieves>",
  "issues": [
    {"status": "red|amber|green", "title": "<5 words max>", "detail": "<2 sentences, specific>"},
    {"status": "red|amber|green", "title": "<5 words max>", "detail": "<2 sentences, specific>"},
    {"status": "red|amber|green", "title": "<5 words max>", "detail": "<2 sentences, specific>"},
    {"status": "red|amber|green", "title": "<5 words max>", "detail": "<2 sentences, specific>"},
    {"status": "red|amber|green", "title": "<5 words max>", "detail": "<2 sentences, specific>"}
  ],
  "tax_rate": "<range like 28-34%>",
  "tax_owed_est": "<estimate like ~$1,800-$2,400 based on income>",
  "tax_note": "<2 sentences on their tax situation and what people at this level usually get wrong>",
  "working": ["<1 sentence>", "<1 sentence>", "<1 sentence>"],
  "action_plan": [
    {"timeline": "This week", "step": "<specific action>"},
    {"timeline": "This week", "step": "<specific action>"},
    {"timeline": "This month", "step": "<specific action>"},
    {"timeline": "This month", "step": "<specific action>"},
    {"timeline": "This month", "step": "<specific action>"},
    {"timeline": "Ongoing", "step": "<recurring habit>"}
  ],
  "deadlines": [
    {"date": "<Mon DD, YYYY>", "event": "<short label>", "urgency": "red|amber|navy"},
    {"date": "<Mon DD, YYYY>", "event": "<short label>", "urgency": "red|amber|navy"},
    {"date": "<Mon DD, YYYY>", "event": "<short label>", "urgency": "amber"},
    {"date": "<Mon DD, YYYY>", "event": "<short label>", "urgency": "navy"}
  ],
  "closing": "<2-3 sentences. Honest and direct. Slightly reassuring but truthful.>"
}`;
}

function redactForFree(report) {
  const issues = (report.issues || []).slice(0, 3).map(i => ({
    status: i.status,
    title: i.title,
    // Only reveal detail for green (good news) items in the free tier
    detail: i.status === 'green' ? i.detail : null,
  }));
  return {
    risk_level: report.risk_level,
    opening: report.opening,
    tax_status: report.tax_status,
    structure_status: report.structure_status,
    compliance_status: report.compliance_status,
    issues,
    issues_total: (report.issues || []).length,
    locked: true,
  };
}

async function verifyStripeSession(sessionId) {
  if (!sessionId || typeof sessionId !== 'string') return false;
  if (!/^cs_(test|live)_[A-Za-z0-9_]+$/.test(sessionId)) return false;
  if (!process.env.STRIPE_SECRET_KEY) {
    console.error('STRIPE_SECRET_KEY not set — cannot verify payment');
    return false;
  }
  try {
    const r = await fetch(`https://api.stripe.com/v1/checkout/sessions/${encodeURIComponent(sessionId)}`, {
      headers: { Authorization: `Bearer ${process.env.STRIPE_SECRET_KEY}` },
    });
    if (!r.ok) return false;
    const session = await r.json();
    return session && session.payment_status === 'paid';
  } catch (e) {
    console.error('Stripe verify error:', e);
    return false;
  }
}

async function callAnthropic(prompt) {
  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': process.env.ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01',
    },
    body: JSON.stringify({
      model: 'claude-haiku-4-5-20251001',
      max_tokens: 1500,
      messages: [{ role: 'user', content: prompt }],
    }),
  });
  const data = await response.json();
  if (!response.ok) {
    const err = new Error('Anthropic API error');
    err.details = data;
    throw err;
  }
  const raw = (data.content?.[0]?.text || '').replace(/```json|```/g, '').trim();
  return JSON.parse(raw);
}

export default async function handler(req, res) {
  setCors(req, res);

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  if (!process.env.ANTHROPIC_API_KEY) {
    return res.status(500).json({ error: 'API key not configured' });
  }

  try {
    const body = req.body || {};
    const { answers, session_id } = body;

    // Backwards-compat: if old client passes a raw `prompt`, accept it as a free-tier call
    // (the response will be redacted just like a normal free call).
    let prompt;
    if (answers && typeof answers === 'object') {
      prompt = buildPrompt(answers);
    } else if (typeof body.prompt === 'string') {
      prompt = body.prompt;
    } else {
      return res.status(400).json({ error: 'Missing answers' });
    }

    const paid = await verifyStripeSession(session_id);

    const report = await callAnthropic(prompt);

    if (paid) {
      return res.status(200).json({ tier: 'paid', report });
    }
    return res.status(200).json({ tier: 'free', report: redactForFree(report) });
  } catch (err) {
    console.error('Handler error:', err);
    return res.status(500).json({ error: 'Server error', message: err.message });
  }
}
