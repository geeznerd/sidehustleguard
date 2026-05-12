"""
Replace existing Quarterly Tax System cards with the v3 version that
advertises the full 6-file bundle.

Preserves the per-page audience string.
"""
import os, re, glob

REPO = "/Users/dork/Desktop/sidehustleguard"
GUMROAD_URL = "https://sidehustleguard.gumroad.com/l/QUARTERLY_PENDING"

# Match any existing quarterly product card
OLD_CARD_PATTERN = re.compile(
    r'<div class="product-card" data-product="quarterly-tax-system">.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)

# Extract the audience from inside the card if possible
AUDIENCE_PATTERN = re.compile(r'Built for ([^.]+?)\.')

def new_card_html(audience):
    return f"""<div class="product-card" data-product="quarterly-tax-system">
  <div class="product-card-icon" aria-hidden="true">📅</div>
  <div class="product-card-body">
    <div class="product-card-eyebrow">Quarterly tax system · 6-file bundle</div>
    <div class="product-card-title">Quarterly Tax System 2026</div>
    <div class="product-card-desc">Built for {audience}. The complete system for paying quarterly taxes without the IRS underpayment penalty. Includes the spreadsheet (calculates SE + federal + state, tracks Q1–Q4, checks safe harbor) plus a <strong>15-page survival guide</strong>, a <strong>penalty abatement letter template</strong> (worth $200+ from a CPA), a <strong>50-state cheat sheet</strong>, a <strong>CPA handoff checklist</strong>, and a <strong>calendar file</strong> with all four deadline reminders pre-set.</div>
    <div class="product-card-feats">
      <span>✓ Dashboard + 8 working tabs</span>
      <span>✓ Both IRS safe-harbor rules</span>
      <span>✓ Color-coded payment tracker</span>
      <span>✓ BONUS: 15-page survival guide</span>
      <span>✓ BONUS: penalty abatement letter</span>
      <span>✓ BONUS: 50-state cheat sheet</span>
      <span>✓ BONUS: CPA handoff checklist</span>
      <span>✓ BONUS: .ics calendar reminders</span>
    </div>
    <div class="product-card-cta-row">
      <a href="{GUMROAD_URL}" class="product-card-btn" target="_blank" rel="noopener">Get the bundle — $17 →</a>
      <span class="product-card-meta">6 files · Excel + Sheets + 4 PDFs + .ics</span>
    </div>
  </div>
</div>"""

def patch(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    m = OLD_CARD_PATTERN.search(content)
    if not m:
        return None  # not patched on this page

    audience_match = AUDIENCE_PATTERN.search(m.group(0))
    audience = audience_match.group(1).strip() if audience_match else "self-employed filers"

    new_content = content[:m.start()] + new_card_html(audience) + content[m.end():]
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return audience

if __name__ == "__main__":
    count = 0
    for path in sorted(glob.glob(os.path.join(REPO, "*.html"))):
        result = patch(path)
        if result is not None:
            print(f"  ✓ {os.path.basename(path):40s}  ({result})")
            count += 1
    print()
    print(f"Updated: {count} pages")
