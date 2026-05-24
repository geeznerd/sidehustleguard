#!/usr/bin/env python3
"""
Phase 9 polish — tighten the nav .nav-cta apricot pill and switch text to
white. Touches only the v2 (apricot+glass) inline rule that Phase 9 added;
won't disturb other pages or the canonical .btn-cta in design-system.css.

The substring we look for is unique to the Phase 9 nav-cta rule:
  ;color:var(--indigo);padding:9px 20px;border-radius:100px;font-size:13px;
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OLD = ";color:var(--indigo);padding:9px 20px;border-radius:100px;font-size:13px;"
NEW = ";color:#fff;padding:7px 16px;border-radius:100px;font-size:13px;"

EXCLUDE = {
    "_template-article.html",
    "_template-article-card.html",
    "guide-section-options.html",
    "og-image.html",
    "tax-affiliate-options.html",
}

def main() -> int:
    counts = {"polished": 0, "already": 0, "skipped": 0, "no-rule": 0}
    for p in sorted(ROOT.glob("*.html")):
        if p.name in EXCLUDE:
            counts["skipped"] += 1
            continue
        text = p.read_text(encoding="utf-8")
        if NEW in text:
            counts["already"] += 1
            continue
        if OLD not in text:
            counts["no-rule"] += 1
            continue
        p.write_text(text.replace(OLD, NEW), encoding="utf-8")
        counts["polished"] += 1
        print(f"  [polished] {p.name}")
    print()
    print(
        f"Done. polished={counts['polished']} "
        f"already={counts['already']} "
        f"skipped={counts['skipped']} "
        f"no-rule={counts['no-rule']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
