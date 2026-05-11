"""
Inject the Gig Driver Mileage Tracker product card into all 8 gig-worker guide pages.
- Adds product-card CSS to the <style> block if not present.
- Inserts the product card HTML right before the FAQ section.
Idempotent: re-running won't duplicate.
"""
import os, re

REPO = "/Users/dork/Desktop/sidehustleguard"

GIG_PAGES = [
    ("doordash-taxes.html",    "DoorDash drivers"),
    ("uber-lyft-taxes.html",   "Uber & Lyft drivers"),
    ("uber-eats-taxes.html",   "Uber Eats drivers"),
    ("grubhub-taxes.html",     "Grubhub drivers"),
    ("instacart-taxes.html",   "Instacart shoppers"),
    ("amazon-flex-taxes.html", "Amazon Flex drivers"),
    ("taskrabbit-taxes.html",  "TaskRabbit Taskers"),
    ("rover-taxes.html",       "Rover sitters & walkers"),
]

# Live Gumroad URL
GUMROAD_URL = "https://sidehustleguard.gumroad.com/l/fbkkdf"

PRODUCT_CARD_CSS = """
.product-card{background:var(--cream-d);border:1.5px solid rgba(201,151,58,.25);border-radius:14px;padding:24px 28px;margin:32px 0;display:flex;gap:20px;align-items:flex-start}
.product-card-icon{font-size:32px;line-height:1;flex-shrink:0;margin-top:2px}
.product-card-body{flex:1;min-width:0}
.product-card-eyebrow{font-size:10px;font-weight:700;letter-spacing:.1em;color:var(--gold);text-transform:uppercase;margin-bottom:6px}
.product-card-title{font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--navy);margin-bottom:8px;line-height:1.25}
.product-card-desc{font-size:13px;color:var(--muted);line-height:1.65;margin-bottom:12px;font-weight:300}
.product-card-feats{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:16px}
.product-card-feats span{font-size:11px;color:var(--muted);background:var(--white);border:1px solid var(--border);padding:3px 10px;border-radius:100px}
.product-card-cta-row{display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.product-card-btn{display:inline-block;background:var(--gold);color:var(--white);padding:10px 22px;border-radius:100px;font-size:13px;font-weight:600;text-decoration:none;transition:all .15s;white-space:nowrap}
.product-card-btn:hover{background:var(--gold-lt)}
.product-card-meta{font-size:11px;color:var(--dim)}
@media(max-width:560px){.product-card{flex-direction:column;gap:10px}}
"""

def product_card_html(audience):
    return f"""<div class="product-card" data-product="gig-driver-mileage-tracker">
  <div class="product-card-icon" aria-hidden="true">🚗</div>
  <div class="product-card-body">
    <div class="product-card-eyebrow">Mileage tracker · spreadsheet</div>
    <div class="product-card-title">Gig Driver Mileage Tracker 2026</div>
    <div class="product-card-desc">Built for {audience}. Log every trip in 10 seconds, auto-calculate your IRS standard mileage deduction, and hand a complete, audit-ready record to your CPA. Works in Excel and Google Sheets. Multi-vehicle, multi-platform.</div>
    <div class="product-card-feats">
      <span>✓ IRS-compliant log</span>
      <span>✓ Auto-calc deduction</span>
      <span>✓ Multi-vehicle</span>
      <span>✓ Monthly &amp; year-end summaries</span>
      <span>✓ Schedule C line 9 ready</span>
    </div>
    <div class="product-card-cta-row">
      <a href="{GUMROAD_URL}" class="product-card-btn" target="_blank" rel="noopener">Get the tracker — $9 →</a>
      <span class="product-card-meta">Instant download · Excel &amp; Google Sheets</span>
    </div>
  </div>
</div>
"""

def patch_file(path, audience):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if 'data-product="gig-driver-mileage-tracker"' in content:
        return "already-patched"

    original = content

    # 1. Inject CSS if not already present
    if ".product-card{" not in content:
        # Insert right before </style>
        content = content.replace("</style>", PRODUCT_CARD_CSS + "\n</style>", 1)

    # 2. Inject product card HTML before FAQ h2
    # Match <h2 ... id="frequently-asked-questions" ...>
    pattern = re.compile(r'(<h2[^>]*id="frequently-asked-questions"[^>]*>)', re.IGNORECASE)
    if not pattern.search(content):
        return "no-faq-landmark"

    content = pattern.sub(product_card_html(audience) + r"\1", content, count=1)

    if content == original:
        return "no-change"

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return "patched"

if __name__ == "__main__":
    for filename, audience in GIG_PAGES:
        path = os.path.join(REPO, filename)
        status = patch_file(path, audience)
        print(f"  {status:18s} {filename}")
    print("done")
