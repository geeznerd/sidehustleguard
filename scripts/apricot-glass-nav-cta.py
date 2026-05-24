#!/usr/bin/env python3
"""
Phase 9 — Replace the indigo .nav-cta inline rule on every article/calc page
with the new apricot "liquid glass" treatment that matches .btn-cta from
design-system.css.

The current inline rule has 3 known variants (padding 8px/9px, with/without
trailing transition declaration). We match the rule defensively with a
regex and rewrite as a single canonical apricot+glass block.

Idempotent — re-running on an already-migrated page is a no-op (we detect
the new linear-gradient signature).
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Pages without a nav (or with bespoke nav handling) — skip even if matched
EXCLUDE = {
    "_template-article.html",
    "_template-article-card.html",
    "guide-section-options.html",
    "og-image.html",
    "tax-affiliate-options.html",
}

# Detect already-migrated pages
ALREADY_RE = re.compile(r"\.nav-cta\{[^}]*linear-gradient")

# Match the .nav-cta block (any inline format, any subset of declarations)
# plus the optional :hover rule. Anchored on `background: var(--indigo)`
# inside the body so we only catch the indigo nav CTA, not any other style.
# The ALREADY_RE check above guards against double-migration.
OLD_RE = re.compile(
    r"\.nav-cta\s*\{[^{}]*background\s*:\s*var\(--indigo\)[^{}]*\}"
    r"(?:\s*\.nav-cta:hover\s*\{[^{}]*background\s*:\s*var\(--indigo-hover\)[^{}]*\})?"
)

# Canonical replacement — apricot gradient + ::before specular sheen + glow.
# Keep one-liner format to match the rest of the inline article CSS style.
NEW_RULE = (
    ".nav-cta{position:relative;overflow:hidden;"
    "background:linear-gradient(180deg,#f0a075 0%,#e89464 55%,#d97c4a 100%);"
    "color:var(--indigo);padding:9px 20px;border-radius:100px;"
    "font-size:13px;font-weight:600;text-decoration:none;"
    "box-shadow:inset 0 1px 0 rgba(255,255,255,0.45),"
    "inset 0 -1px 0 rgba(45,48,104,0.12),"
    "0 6px 18px rgba(232,148,100,0.32),"
    "0 2px 5px rgba(45,48,104,0.10);"
    "transition:background .2s,box-shadow .2s,transform .15s}"
    ".nav-cta::before{content:'';position:absolute;top:0;left:0;right:0;"
    "height:55%;background:linear-gradient(180deg,"
    "rgba(255,255,255,0.32) 0%,rgba(255,255,255,0) 100%);"
    "border-radius:100px 100px 0 0;pointer-events:none}"
    ".nav-cta:hover{background:linear-gradient(180deg,#f4ad84 0%,"
    "#ed9d72 55%,#e08c5e 100%);"
    "box-shadow:inset 0 1px 0 rgba(255,255,255,0.55),"
    "inset 0 -1px 0 rgba(45,48,104,0.14),"
    "0 8px 22px rgba(232,148,100,0.42),"
    "0 3px 7px rgba(45,48,104,0.14)}"
    "@media(prefers-reduced-motion:no-preference){"
    ".nav-cta:hover{transform:translateY(-1px)}}"
)


def migrate(path: Path) -> str:
    if path.name in EXCLUDE:
        return "skipped"
    text = path.read_text(encoding="utf-8")
    if ALREADY_RE.search(text):
        return "already"
    new_text, n = OLD_RE.subn(NEW_RULE, text, count=1)
    if n == 0:
        return "no-match"
    path.write_text(new_text, encoding="utf-8")
    return "migrated"


def main() -> int:
    counts = {"migrated": 0, "already": 0, "skipped": 0, "no-match": 0}
    for p in sorted(ROOT.glob("*.html")):
        status = migrate(p)
        counts[status] += 1
        if status in ("migrated", "no-match"):
            print(f"  [{status:>9}] {p.name}")
    print()
    print(
        f"Done. migrated={counts['migrated']} "
        f"already={counts['already']} "
        f"skipped={counts['skipped']} "
        f"no-match={counts['no-match']}"
    )
    return 0 if counts["no-match"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
