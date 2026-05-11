"""
Inject the Quarterly Tax System product card into 32+ guide pages where the
audience is self-employed and quarterly tax is a real pain.

- Adds product-card CSS if not present (mileage tracker may already have added it).
- Inserts the card right before the FAQ h2.
- If the Mileage Tracker card is already present, the Quarterly card lands
  immediately AFTER it (so the visual order is Mileage → Quarterly → FAQ).
- Idempotent: rerun safely.
"""
import os, re

REPO = "/Users/dork/Desktop/sidehustleguard"

# Live URL — replace after the Gumroad listing is published.
GUMROAD_URL = "https://sidehustleguard.gumroad.com/l/QUARTERLY_PENDING"

PAGES = [
    # Tier 1 — directly about quarterly / SE tax
    ("quarterly-tax-calculator.html",        "self-employed filers"),
    ("quarterly-taxes-self-employed.html",   "self-employed filers"),
    ("quarterly-taxes-for-airbnb-hosts.html","Airbnb & STR hosts"),
    ("self-employment-tax-calculator.html",  "self-employed filers"),
    ("california-self-employment-tax.html",  "California self-employed"),
    ("new-york-self-employment-tax.html",    "New York self-employed"),
    ("texas-self-employment-tax.html",       "Texas self-employed"),
    ("side-hustle-taxes.html",               "side hustlers"),
    ("freelancer-taxes.html",                "freelancers"),
    ("airbnb-self-employment-tax.html",      "Airbnb hosts subject to SE tax"),

    # Tier 2 — gig drivers (stacks after the Mileage Tracker card)
    ("doordash-taxes.html",                  "DoorDash drivers"),
    ("uber-lyft-taxes.html",                 "Uber & Lyft drivers"),
    ("uber-eats-taxes.html",                 "Uber Eats drivers"),
    ("grubhub-taxes.html",                   "Grubhub drivers"),
    ("instacart-taxes.html",                 "Instacart shoppers"),
    ("amazon-flex-taxes.html",               "Amazon Flex drivers"),
    ("taskrabbit-taxes.html",                "TaskRabbit Taskers"),
    ("rover-taxes.html",                     "Rover sitters & walkers"),

    # Tier 3 — freelance, reseller, creator
    ("upwork-taxes.html",                    "Upwork freelancers"),
    ("fiverr-taxes.html",                    "Fiverr sellers"),
    ("etsy-taxes.html",                      "Etsy sellers"),
    ("ebay-taxes.html",                      "eBay sellers"),
    ("poshmark-taxes.html",                  "Poshmark sellers"),
    ("mercari-taxes.html",                   "Mercari sellers"),
    ("shopify-taxes.html",                   "Shopify store owners"),
    ("reseller-taxes.html",                  "online resellers"),
    ("youtube-taxes.html",                   "YouTube creators"),
    ("twitch-taxes.html",                    "Twitch streamers"),
    ("tiktok-taxes.html",                    "TikTok creators"),
    ("onlyfans-taxes.html",                  "OnlyFans creators"),
    ("patreon-taxes.html",                   "Patreon creators"),
    ("substack-taxes.html",                  "Substack writers"),
]

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

def quarterly_card_html(audience):
    return f"""<div class="product-card" data-product="quarterly-tax-system">
  <div class="product-card-icon" aria-hidden="true">📅</div>
  <div class="product-card-body">
    <div class="product-card-eyebrow">Quarterly tax tool · spreadsheet</div>
    <div class="product-card-title">Quarterly Tax System 2026</div>
    <div class="product-card-desc">Built for {audience}. Tells you exactly what to send the IRS (and your state) for Q1, Q2, Q3, Q4 — and whether you've hit safe harbor so the underpayment penalty never lands on you. Excel + Google Sheets.</div>
    <div class="product-card-feats">
      <span>✓ SE tax + federal + state, calculated</span>
      <span>✓ Q1–Q4 due dates &amp; targets</span>
      <span>✓ Safe-harbor check (both rules)</span>
      <span>✓ Payment log w/ on-track status</span>
      <span>✓ Penalty-free year, every year</span>
    </div>
    <div class="product-card-cta-row">
      <a href="{GUMROAD_URL}" class="product-card-btn" target="_blank" rel="noopener">Get the system — $17 →</a>
      <span class="product-card-meta">Instant download · Excel &amp; Google Sheets</span>
    </div>
  </div>
</div>
"""

def patch_file(path, audience):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if 'data-product="quarterly-tax-system"' in content:
        return "already-patched"

    # 1. Ensure CSS exists
    if ".product-card{" not in content:
        if "</style>" not in content:
            return "no-style-block"
        content = content.replace("</style>", PRODUCT_CARD_CSS + "\n</style>", 1)

    # 2. Locate FAQ landmark
    faq_pattern = re.compile(r'(<h2[^>]*id="frequently-asked-questions"[^>]*>)', re.IGNORECASE)
    if not faq_pattern.search(content):
        return "no-faq-landmark"

    card = quarterly_card_html(audience)

    # 3. If Mileage Tracker card exists, insert AFTER it.
    #    Otherwise, insert right before the FAQ h2.
    mileage_pattern = re.compile(
        r'(<div class="product-card" data-product="gig-driver-mileage-tracker">.*?</div>\s*</div>)',
        re.DOTALL
    )
    if mileage_pattern.search(content):
        content = mileage_pattern.sub(r"\1\n" + card, content, count=1)
    else:
        content = faq_pattern.sub(card + r"\1", content, count=1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return "patched"

if __name__ == "__main__":
    results = {}
    for filename, audience in PAGES:
        path = os.path.join(REPO, filename)
        if not os.path.exists(path):
            results[filename] = "missing"
            continue
        results[filename] = patch_file(path, audience)
    for k, v in results.items():
        print(f"  {v:18s} {k}")
    print()
    print(f"Total patched: {sum(1 for v in results.values() if v=='patched')}")
    print(f"Already had it: {sum(1 for v in results.values() if v=='already-patched')}")
    print(f"Missing landmark: {sum(1 for v in results.values() if v=='no-faq-landmark')}")
    print(f"Missing file: {sum(1 for v in results.values() if v=='missing')}")
