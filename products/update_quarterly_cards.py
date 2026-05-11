"""
Replace the existing Quarterly Tax System product cards on every page with
the upgraded version that advertises the bonus PDF + new Dashboard/Examples
tabs.

Preserves the per-page audience string ("Built for [audience]...").
"""
import os, re, glob

REPO = "/Users/dork/Desktop/sidehustleguard"
GUMROAD_URL = "https://sidehustleguard.gumroad.com/l/QUARTERLY_PENDING"

# Match an existing quarterly product card on a page and capture the audience.
OLD_CARD_PATTERN = re.compile(
    r'<div class="product-card" data-product="quarterly-tax-system">'
    r'.*?Built for ([^.]+?)\.'
    r'.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)

# Some early variants have phrasing differences — try a few fallback patterns
ALT_CARD_PATTERN = re.compile(
    r'<div class="product-card" data-product="quarterly-tax-system">.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)

def new_card_html(audience):
    return f"""<div class="product-card" data-product="quarterly-tax-system">
  <div class="product-card-icon" aria-hidden="true">📅</div>
  <div class="product-card-body">
    <div class="product-card-eyebrow">Quarterly tax system · spreadsheet + 15-page guide</div>
    <div class="product-card-title">Quarterly Tax System 2026</div>
    <div class="product-card-desc">Built for {audience}. A complete system for paying quarterly taxes without the IRS underpayment penalty. Spreadsheet calculates SE tax + federal + state, tracks Q1–Q4 with a color-coded status dashboard, and checks both safe-harbor rules. Includes a <strong>15-page survival guide PDF</strong> that explains every rule in plain English.</div>
    <div class="product-card-feats">
      <span>✓ Dashboard + 8 working tabs</span>
      <span>✓ SE + federal + state tax math</span>
      <span>✓ Both IRS safe-harbor rules</span>
      <span>✓ Color-coded payment tracker</span>
      <span>✓ 3 worked-out examples</span>
      <span>✓ BONUS: 15-page guide PDF</span>
    </div>
    <div class="product-card-cta-row">
      <a href="{GUMROAD_URL}" class="product-card-btn" target="_blank" rel="noopener">Get the system + guide — $17 →</a>
      <span class="product-card-meta">Instant download · Excel + Google Sheets + PDF</span>
    </div>
  </div>
</div>"""

def patch(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if 'data-product="quarterly-tax-system"' not in content:
        return "no-card"

    # Try the rich pattern first (with audience capture)
    m = OLD_CARD_PATTERN.search(content)
    if m:
        audience = m.group(1).strip()
        new = new_card_html(audience)
        new_content = OLD_CARD_PATTERN.sub(new.replace("\\", "\\\\"), content, count=1)
        # Note: regex sub backreference safety — use plain string replacement via group span
        new_content = content[:m.start()] + new + content[m.end():]
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return f"patched ({audience})"

    # Fallback: replace the whole card with a generic audience
    m2 = ALT_CARD_PATTERN.search(content)
    if m2:
        new = new_card_html("self-employed filers")
        new_content = content[:m2.start()] + new + content[m2.end():]
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return "patched (generic)"

    return "no-match"

if __name__ == "__main__":
    results = {}
    for path in glob.glob(os.path.join(REPO, "*.html")):
        name = os.path.basename(path)
        r = patch(path)
        if r != "no-card":
            results[name] = r
    for k, v in sorted(results.items()):
        print(f"  {v:35s} {k}")
    print()
    print(f"Total updated: {len(results)}")
