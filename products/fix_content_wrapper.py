"""
Fix the .content wrapper that closes prematurely on guide pages.

Structure problem (pattern repeats across ~50 pages):

  <div class="content">
    [article body, product cards, mid-page CTA]
  </div>                                <-- closes here
                                        <-- ORPHAN: full-width sprawl
  <h2>FAQ</h2>
  <div class="faq-item">...</div>
  <hr>
  <h2>Bottom line</h2>
  <p>...</p>
  <div class="nw-card">...</div>
  <div class="cta-box">...</div>
                                        <-- END ORPHAN
  <div class="content" style="padding-top:0">
    <div class="related-section">...</div>
  </div>

Fix: walk the body. Find the first <div class="content">. Find the
<div class="related-section">. Move every sibling between them INSIDE
the first .content div. Then unwrap the redundant second .content that
holds the related-section so the related-section sits at the body level
where it already has its own styling.
"""
import os, glob
from bs4 import BeautifulSoup

REPO = "/Users/dork/Desktop/sidehustleguard"

EXCLUDE = {"_template-article.html", "_template-article-card.html",
           "og-image.html", "tool.html", "guide-section-options.html",
           "tax-affiliate-options.html", "tax-checklist.html",
           "index.html", "guides.html", "dashboard.html",
           "privacy.html", "terms.html",
           "tax-guard-calculator.html", "scorp-savings-calculator.html",
           "quarterly-tax-calculator.html", "self-employment-tax-calculator.html",
           "audit-risk-estimator.html", "short-term-rentals.html",
           "state-tax-rates.html",
           "california-side-hustle.html"}

def fix_page(path):
    """Fix any case where FAQ / bottom-line / final CTAs sit outside .content.

    Both variants:
      A) Second .content div wraps related-section, with FAQ orphaned between them
      B) Single .content div closes early, FAQ orphaned, related-section at body level

    In both cases: move all sibling nodes between .content and related-section
    INTO .content, then ensure related-section sits as sibling of .content.
    """
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()
    soup = BeautifulSoup(original, "html.parser")

    first_content = soup.find("div", class_="content")
    related = soup.find("div", class_="related-section")
    if not first_content or not related:
        return "structure-mismatch"

    # If FAQ is already inside .content, no fix needed
    faq = soup.find("h2", id="frequently-asked-questions")
    if faq is None:
        return "no-faq"
    if faq.find_parent("div", class_="content") is first_content:
        return "no-fix-needed"

    # Identify the second-level wrapper (if related-section sits in one)
    related_wrapper = related.parent

    # Move every sibling between first_content and the wrapper-of-related
    # into first_content
    target_stop = related_wrapper if (
        related_wrapper.name == "div" and "content" in (related_wrapper.get("class") or [])
    ) else related

    nodes_to_move = []
    cursor = first_content.next_sibling
    while cursor is not None and cursor is not target_stop:
        nodes_to_move.append(cursor)
        cursor = cursor.next_sibling

    for node in nodes_to_move:
        first_content.append(node.extract())

    # If related-section was wrapped in a second .content div, pull it out and
    # delete the now-empty wrapper.
    if (target_stop is related_wrapper
            and related_wrapper is not first_content
            and related_wrapper.name == "div"
            and "content" in (related_wrapper.get("class") or [])):
        related.extract()
        first_content.insert_after(related)
        if not related_wrapper.find(True):
            related_wrapper.decompose()
        else:
            related_wrapper.unwrap()

    new_html = str(soup)
    if new_html == original:
        return "no-change"
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    return "fixed"

if __name__ == "__main__":
    fixed = []
    no_fix = []
    for path in sorted(glob.glob(os.path.join(REPO, "*.html"))):
        name = os.path.basename(path)
        if name in EXCLUDE or name.startswith("_"):
            continue
        result = fix_page(path)
        if result == "fixed":
            fixed.append(name)
        else:
            no_fix.append((name, result))

    print(f"Fixed: {len(fixed)} pages")
    for n in fixed[:6]:
        print(f"  ✓ {n}")
    if len(fixed) > 6:
        print(f"  ... and {len(fixed)-6} more")
    print()
    print(f"No fix needed / structure different: {len(no_fix)} pages")
