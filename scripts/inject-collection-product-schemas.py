#!/usr/bin/env python3
"""
Phase 18.1 — Add JSON-LD to the two remaining schema gaps:
  - /guides → CollectionPage + ItemList (all 79 guides + tools)
  - /quarterly-tax-system → Product + Offer (the $17 bundle)

Both also get a matching BreadcrumbList. Schemas are inserted right
before the </head> closing tag.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://www.sidehustleguard.com"


def build_guides_itemlist():
    """Scrape guides.html for all guide-card + mega-card links and titles."""
    text = (ROOT / "guides.html").read_text(encoding="utf-8")
    pattern = re.compile(
        r'<a class="(?:guide-card[^"]*|mega-card)"[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
        re.DOTALL
    )
    items = []
    for m in pattern.finditer(text):
        href, body = m.group(1), m.group(2)
        title_m = re.search(
            r'class="(?:guide-title|mega-title)"[^>]*>(.*?)</(?:span|h3)>',
            body, re.DOTALL
        )
        if title_m:
            title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip()
            # Normalize whitespace + decode common entities
            title = re.sub(r'\s+', ' ', title)
            title = (title.replace('&amp;', '&').replace('&#39;', "'")
                          .replace('&quot;', '"'))
            url = href if href.startswith('http') else BASE + href
            items.append((url, title))
    return items


def guides_schemas():
    items = build_guides_itemlist()
    collection = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "All Side Hustle Tax Guides + Tools — SideHustleGuard",
        "description": "Plain-English tax + legal guides for every kind of US side hustle, plus free interactive calculators and tools.",
        "url": BASE + "/guides",
        "mainEntity": {
            "@type": "ItemList",
            "numberOfItems": len(items),
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i + 1,
                    "url": url,
                    "name": name
                }
                for i, (url, name) in enumerate(items)
            ]
        }
    }
    crumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": BASE + "/guides"}
        ]
    }
    return [collection, crumb]


def qts_schemas():
    product = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": "Quarterly Tax System 2026 — Side Hustle Bundle",
        "description": "A spreadsheet, a 15-page survival guide, an IRS penalty abatement letter template, a 50-state cheat sheet, a CPA handoff checklist, and a calendar file with every IRS estimated tax deadline. Designed for side hustlers, freelancers, and 1099 contractors. One download.",
        "url": BASE + "/quarterly-tax-system",
        "brand": {
            "@type": "Brand",
            "name": "SideHustleGuard"
        },
        "offers": {
            "@type": "Offer",
            "url": BASE + "/quarterly-tax-system",
            "price": "17.00",
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock",
            "seller": {
                "@type": "Organization",
                "name": "SideHustleGuard"
            }
        }
    }
    crumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": BASE + "/guides"},
            {"@type": "ListItem", "position": 3, "name": "Quarterly Tax System",
             "item": BASE + "/quarterly-tax-system"}
        ]
    }
    return [product, crumb]


def inject(path: Path, schemas):
    text = path.read_text(encoding="utf-8")
    # Skip if a CollectionPage or Product schema is already present
    if '"@type": "CollectionPage"' in text or '"@type":"CollectionPage"' in text:
        return "already-has-collection"
    if '"@type": "Product"' in text or '"@type":"Product"' in text:
        return "already-has-product"

    blocks = []
    for schema in schemas:
        blocks.append('<script type="application/ld+json">\n'
                      + json.dumps(schema, indent=2)
                      + '\n</script>')
    insertion = "\n" + "\n".join(blocks) + "\n"

    if "</head>" not in text:
        return "no-head"
    new_text = text.replace("</head>", insertion + "</head>", 1)
    path.write_text(new_text, encoding="utf-8")
    return "injected"


def main() -> int:
    targets = [
        ("guides.html", guides_schemas()),
        ("quarterly-tax-system.html", qts_schemas())
    ]
    for fname, schemas in targets:
        path = ROOT / fname
        if not path.exists():
            print(f"  [MISSING] {fname}")
            continue
        status = inject(path, schemas)
        print(f"  [{status:>22}] {fname}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
