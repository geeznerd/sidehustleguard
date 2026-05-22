"""
Three-in-one SEO + trust-signal pass:

1. Regenerate /sitemap.xml from the actual file inventory, with today's lastmod
   and priority/changefreq based on content depth.
2. Add a visible author byline to every guide page's hero-meta block.
3. Upgrade JSON-LD Article schema:
   - Author becomes a Person (Richard Srey), not just an Organization.
   - dateModified updated to today.

This is a Google E-E-A-T pass — Experience, Expertise, Authoritativeness,
Trustworthiness. YMYL (tax/legal) sites need these signals more than
typical sites, and currently the site has zero personal-author attribution.
"""
import os, re, glob, datetime, json

REPO   = "/Users/dork/Desktop/sidehustleguard"
TODAY  = datetime.date.today().isoformat()        # "2026-05-22"
HUMAN_MONTH = datetime.date.today().strftime("%B %Y")   # "May 2026"

AUTHOR_NAME = "Richard Srey"
AUTHOR_URL  = "https://www.sidehustleguard.com/#author"
SITE_URL    = "https://www.sidehustleguard.com"

# Pages to never include in sitemap / never modify
EXCLUDE_FROM_SITEMAP = {
    "og-image.html", "tool.html", "guide-section-options.html",
    "tax-affiliate-options.html", "tax-checklist.html",
    "_template-article.html", "_template-article-card.html",
}

# High-priority pages (set to 1.0/0.9)
HIGH_PRIORITY = {
    "index.html": ("1.0", "weekly"),
    "guides.html": ("0.9", "weekly"),
    "short-term-rentals.html": ("0.85", "weekly"),
}

# Tier-1 product/calculator/landing pages
TIER1 = {
    "tax-guard-calculator.html",
    "scorp-savings-calculator.html",
    "quarterly-tax-calculator.html",
    "self-employment-tax-calculator.html",
    "audit-risk-estimator.html",
    "dashboard.html",
}

# ────────────────────────────────────────────────────────────────────
# PASS 1 — Regenerate sitemap.xml
# ────────────────────────────────────────────────────────────────────
def regenerate_sitemap():
    entries = []
    for path in sorted(glob.glob(os.path.join(REPO, "*.html"))):
        name = os.path.basename(path)
        if name in EXCLUDE_FROM_SITEMAP or name.startswith("_"):
            continue
        slug = name.replace(".html", "")
        if slug == "index":
            url = f"{SITE_URL}/"
        else:
            url = f"{SITE_URL}/{slug}"

        if name in HIGH_PRIORITY:
            prio, freq = HIGH_PRIORITY[name]
        elif name in TIER1:
            prio, freq = "0.8", "weekly"
        elif name in ("privacy.html", "terms.html"):
            prio, freq = "0.3", "yearly"
        else:
            prio, freq = "0.7", "monthly"

        entries.append((url, prio, freq))

    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, prio, freq in entries:
        xml += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{TODAY}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{prio}</priority>",
            "  </url>",
        ]
    xml.append("</urlset>\n")

    out = os.path.join(REPO, "sitemap.xml")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(xml))
    return len(entries)

# ────────────────────────────────────────────────────────────────────
# PASS 2 — Add byline to hero-meta on every guide page
# ────────────────────────────────────────────────────────────────────
# Existing: <div class="hero-meta"><time datetime="2026-04-01">Updated April 2026 · 7 min read</time></div>
# New:      <div class="hero-meta"><span class="byline">By <a href="/#author" rel="author">Richard Srey</a></span> · <time datetime="2026-05-22">Updated May 2026</time> · 7 min read</div>

HERO_META = re.compile(
    r'<div class="hero-meta"><time datetime="[^"]*">Updated [A-Za-z]+ \d{4}(?: · (\d+ min read))?</time></div>',
)

def update_hero_meta(content):
    """Replace the existing hero-meta with a byline + updated date version."""
    def replacer(m):
        read_time = m.group(1) or "7 min read"
        return (
            f'<div class="hero-meta">'
            f'<span class="byline">By <a href="/#author" rel="author">{AUTHOR_NAME}</a></span>'
            f' · <time datetime="{TODAY}">Updated {HUMAN_MONTH}</time>'
            f' · {read_time}'
            f'</div>'
        )
    new = HERO_META.sub(replacer, content, count=1)
    return new, new != content

# ────────────────────────────────────────────────────────────────────
# PASS 3 — Upgrade JSON-LD Article author to Person + bump dateModified
# ────────────────────────────────────────────────────────────────────
# Existing pattern:
#   "author": {
#     "@type": "Organization",
#     "name": "SideHustleGuard",
#     "url": "https://www.sidehustleguard.com"
#   },
# We replace with a Person author and bump "dateModified".

OLD_AUTHOR_PATTERN = re.compile(
    r'"author":\s*\{\s*"@type":\s*"Organization",\s*'
    r'"name":\s*"SideHustleGuard",\s*'
    r'"url":\s*"https://www\.sidehustleguard\.com"\s*\}',
)
NEW_AUTHOR_BLOCK = (
    '"author": {'
    '"@type": "Person",'
    f' "name": "{AUTHOR_NAME}",'
    f' "url": "{AUTHOR_URL}",'
    ' "jobTitle": "Founder, SideHustleGuard",'
    ' "knowsAbout": ["self-employment tax", "1099 reporting", "short-term rental tax compliance", "small-business filing"]'
    '}'
)
DATE_MOD = re.compile(r'"dateModified":\s*"[\d-]+"')

def update_json_ld(content):
    changes = 0
    if OLD_AUTHOR_PATTERN.search(content):
        content = OLD_AUTHOR_PATTERN.sub(NEW_AUTHOR_BLOCK, content, count=1)
        changes += 1
    if DATE_MOD.search(content):
        content = DATE_MOD.sub(f'"dateModified": "{TODAY}"', content, count=1)
        changes += 1
    return content, changes

# ────────────────────────────────────────────────────────────────────
# Run all three passes
# ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    n_sitemap = regenerate_sitemap()
    print(f"✓ Sitemap regenerated: {n_sitemap} URLs, lastmod={TODAY}")
    print()

    byline_updated = 0
    schema_updated = 0
    date_updated = 0
    skipped = []

    for path in sorted(glob.glob(os.path.join(REPO, "*.html"))):
        name = os.path.basename(path)
        if name in EXCLUDE_FROM_SITEMAP or name.startswith("_"):
            skipped.append(name)
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content, byline_changed = update_hero_meta(content)
        new_content, schema_changes = update_json_ld(new_content)

        if new_content != content:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            if byline_changed: byline_updated += 1
            if schema_changes >= 1: schema_updated += 1
            if schema_changes >= 2: date_updated += 1

    print(f"✓ Byline added to hero-meta:   {byline_updated} pages")
    print(f"✓ JSON-LD author → Person:     {schema_updated} pages")
    print(f"✓ dateModified bumped to today: {date_updated} pages")
    if skipped:
        print(f"  (skipped {len(skipped)}: {', '.join(skipped[:5])}{'...' if len(skipped)>5 else ''})")
