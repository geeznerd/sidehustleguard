#!/usr/bin/env python3
"""
Phase 3 migration: apply Direction E design system to article guides.

Replicates the transformations applied by hand to doordash-taxes.html:
  1. Head: drop old Playfair/DM Sans link, add favicons + new fonts + design-system.css
  2. Style block: strip inline :root{...} + 3 base reset rules (now in design-system.css)
  3. Replace body declaration with minimal Inter/cream/indigo version
  4. Font name swaps (Playfair Display -> Fraunces, DM Sans -> Inter)
  5. Hex code sweeps (navy -> indigo, gold variants -> apricot, status colors)
  6. RGBA sweeps (same alpha, new color triple)
  7. logo-icon svg sizing (26x30 -> 32x32)
  8. Shield SVG -> Arc & Dot mark (nav)
  9. Wordmark Guard -> italic 'guard' (nav + footer)

Skips:
  - Files already migrated (contain 'design-system.css' link)
  - Phase 4 pages (calculators + legal)
  - Non-article HTML
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path("/Users/dork/Desktop/sidehustleguard")

# Pages handled in later phases or not part of Phase 3
PHASE4_PAGES = {
    "audit-risk-estimator.html",
    "self-employment-tax-calculator.html",
    "quarterly-tax-calculator.html",
    "scorp-savings-calculator.html",
    "tax-guard-calculator.html",
    "privacy.html",
    "terms.html",
}

# Already restyled in Phase 2 / Phase 3 template
SKIP_PAGES = {
    "index.html",
    "guides.html",
    "tool.html",
    "dashboard.html",
    "quarterly-tax-system.html",
    "doordash-taxes.html",
    "guide-section-options.html",  # not user-facing
    "_template-article-card.html",
    "404.html",
    "thanks.html",
}

# ---- Head injection blocks ----------------------------------------------

# Replace the single Playfair+DM Sans Google Fonts <link> with the Fraunces+Inter
# block plus the favicons and design-system.css link.
HEAD_INJECTION = (
    '\n<!-- Favicons -->'
    '\n<link rel="icon" type="image/svg+xml" href="/assets/logos/arc-dot.svg"/>'
    '\n<link rel="icon" type="image/png" sizes="32x32" href="/assets/logos/arc-dot.favicon-32.png"/>'
    '\n<link rel="icon" type="image/png" sizes="64x64" href="/assets/logos/arc-dot.favicon-64.png"/>'
    '\n<link rel="apple-touch-icon" href="/assets/logos/arc-dot.favicon-192.png"/>'
    '\n'
    '\n<!-- Fonts -->'
    '\n<link href="https://fonts.googleapis.com" rel="preconnect"/>'
    '\n<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>'
    '\n<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..700,0..100;1,9..144,300..700,0..100&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"/>'
    '\n'
    '\n<!-- Shared design system -->'
    '\n<link href="/assets/css/design-system.css" rel="stylesheet"/>'
)

# The body line that replaces the inline :root + reset rules + old body
NEW_BODY_LINE = (
    "body{font-family:'Inter',sans-serif;background:var(--cream);"
    "color:var(--indigo);line-height:1.65;font-size:16px;overflow-x:clip}"
)

# ---- Logo replacements --------------------------------------------------

ARC_DOT_SVG = (
    '<div class="logo-icon">'
    '<svg fill="none" viewBox="0 0 48 48" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
    '<path d="M6 30 Q24 4 42 30" stroke="#2d3068" stroke-width="2.4" stroke-linecap="round" fill="none"/>'
    '<path d="M14 32 Q24 18 34 32" stroke="#e89464" stroke-width="2.4" stroke-linecap="round" fill="none"/>'
    '<circle cx="24" cy="36" r="2.4" fill="#2d3068"/>'
    '</svg>'
    '</div>'
)

NAV_WORDMARK = (
    '<span class="logo-text">SideHustle'
    '<span style="font-family:\'Fraunces\',serif;font-style:italic;font-weight:500;'
    'color:var(--apricot);font-variation-settings:\'opsz\' 144,\'SOFT\' 30">guard</span>'
    '</span>'
)

FOOTER_WORDMARK = (
    '<span class="footer-logo">SideHustle'
    '<span style="font-family:\'Fraunces\',serif;font-style:italic;font-weight:500;'
    'color:var(--apricot)">guard</span>'
    '</span>'
)

# ---- Color sweeps -------------------------------------------------------

HEX_MAP = {
    # Brand
    "#1c2b4a": "#2d3068",   # navy -> indigo
    "#c9973a": "#e89464",   # gold -> apricot
    "#ddb06a": "#f0a075",   # gold-lt -> apricot-hover
    "#fdf5e8": "#fde8d5",   # gold-pale -> apricot-pale (light tint)
    # Surfaces
    "#faf8f4": "#f0ece1",   # cream -> new cream
    "#f0ece3": "#fbf8ee",   # cream-d -> paper
    "#fffef9": "#fbf8ee",   # off-white -> paper
    "#f3ebd9": "#fde8d5",   # gold pale alt -> apricot-pale
    # Status
    "#276944": "#5a7a4f",   # green -> good (moss)
    "#eaf5ef": "#e8edd9",   # green-bg -> good-bg tint
    "#b83232": "#c2533a",   # red -> risk (clay)
    "#a86c0a": "#c98a3a",   # amber -> warn
    "#fef6e8": "#f9ecd6",   # amber-bg
    # Neutrals — keep these the same; they already work
    # "#6b7a96" muted, "#9aa3b5" dim, "#fff" white — untouched
}

# RGBA sweeps: same alpha, new color triple
# (\d+) (\d+) (\d+) captured so we can preserve alpha values exactly as written
RGBA_MAP = {
    "28,43,74":   "45,48,104",     # navy -> indigo
    "201,151,58": "232,148,100",   # gold -> apricot
    "221,176,106":"240,160,117",   # gold-lt
    "168,108,10": "201,138,58",    # amber dark
    "39,105,68":  "90,122,79",     # green -> good
    "184,50,50":  "194,83,58",     # red -> risk
}

# Font swaps
FONT_PATTERNS = [
    (re.compile(r"'Playfair Display'"), "'Fraunces',Georgia"),
    (re.compile(r"\"Playfair Display\""), '"Fraunces",Georgia'),
    (re.compile(r"'DM Sans'"), "'Inter'"),
    (re.compile(r"\"DM Sans\""), '"Inter"'),
    # Google fonts link itself — replace the whole stylesheet href so we don't 404 on Playfair
    # (the link tag is removed by replace_fonts_link, but in case of stragglers)
]

# ---- Transformations ----------------------------------------------------


def already_migrated(text: str) -> bool:
    return "design-system.css" in text


def replace_fonts_link(text: str) -> str:
    """Strip old Playfair/DM Sans link and adjacent preconnect, inject our block.

    Source pages typically have:
        <link href="https://fonts.googleapis.com" rel="preconnect"/>
        <link href="https://fonts.googleapis.com/css2?family=Playfair+Display..." rel="stylesheet"/>

    We replace those two lines (and any crossorigin preconnect) with HEAD_INJECTION.
    """
    # Pattern for the two old font links (preconnect + the Playfair stylesheet)
    # Use a permissive multi-line match.
    pattern = re.compile(
        r'(?:<link[^>]+fonts\.googleapis\.com"\s+rel="preconnect"\s*/?>\s*\n?)?'
        r'(?:<link[^>]+fonts\.gstatic\.com[^>]*crossorigin[^>]*/?>\s*\n?)?'
        r'<link[^>]+Playfair\+Display[^>]+rel="stylesheet"\s*/?>\s*\n?',
        re.IGNORECASE,
    )
    new_text, n = pattern.subn(HEAD_INJECTION + "\n", text, count=1)
    if n == 0:
        # Fall back: simpler match if the preconnect block is structured differently
        pattern2 = re.compile(
            r'<link[^>]+Playfair\+Display[^>]+rel="stylesheet"\s*/?>\s*\n?',
            re.IGNORECASE,
        )
        new_text, n = pattern2.subn(HEAD_INJECTION + "\n", text, count=1)
    return new_text


def strip_inline_root_and_reset(text: str) -> str:
    """Drop inline :root{...} block + the 3 base reset rules + old body line.

    The doordash template replaced these 5 lines with a single new body declaration.
    """
    pattern = re.compile(
        r":root\{[^}]*\}\s*\n"                                          # :root tokens
        r"(?:\*,\*::before,\*::after\{[^}]*\}\s*\n)?"                  # box-sizing reset
        r"(?:img,picture,video,canvas,svg\{[^}]*\}\s*\n)?"             # media reset
        r"(?:html\{[^}]*\}\s*\n)?"                                     # html scroll/clip
        r"body\{[^}]*\}\s*\n",                                          # old body
        re.MULTILINE,
    )
    return pattern.sub(
        "/* Page-specific styles only — tokens come from design-system.css. */\n"
        + NEW_BODY_LINE + "\n",
        text,
        count=1,
    )


def swap_fonts(text: str) -> str:
    for pat, repl in FONT_PATTERNS:
        text = pat.sub(repl, text)
    return text


def swap_hex(text: str) -> str:
    # Case-insensitive replacement, preserve case in output (always lower)
    for old, new in HEX_MAP.items():
        # Match both upper and lower case forms
        text = re.sub(re.escape(old), new, text, flags=re.IGNORECASE)
    return text


def swap_rgba(text: str) -> str:
    for old, new in RGBA_MAP.items():
        # Match the color triple in any rgba/rgb call, preserve the alpha part
        # Example pattern: rgba(28,43,74,0.09) or rgba(28, 43, 74, .9)
        triple_pat = old.replace(",", r",\s*")
        pattern = re.compile(
            r"(rgba?\(\s*)" + triple_pat + r"(\s*[,)])",
            re.IGNORECASE,
        )
        # Use a callable replacement so digits in `new` aren't interpreted as group refs.
        text = pattern.sub(lambda m, n=new: m.group(1) + n + m.group(2), text)
    return text


def fix_logo_svg_size(text: str) -> str:
    return text.replace(
        ".logo-icon svg{width:26px;height:30px}",
        ".logo-icon svg{width:32px;height:32px}",
    )


# Matches the old shield SVG. Handles both self-closing (`<path ... />`) and
# explicit-close (`<path ...></path>`) syntaxes. Color attributes inside the
# paths may have been hex-swapped already (we run hex sweeps before shield
# replacement), so we don't anchor on specific fill/stroke values.
SHIELD_RE = re.compile(
    r'<div class="logo-icon">\s*'
    r'<svg[^>]*?height="30"[^>]*>'
    r'\s*<path d="M18 2L4 6\.5V19[^"]*"[^>]*?>(?:</path>)?'
    r'\s*<path d="M11 19\.5L16 24\.5L26 13\.5"[^>]*?>(?:</path>)?'
    r'\s*</svg>\s*</div>',
    re.IGNORECASE | re.DOTALL,
)


def replace_shield(text: str) -> str:
    return SHIELD_RE.sub(ARC_DOT_SVG, text)


def replace_wordmarks(text: str) -> str:
    text = text.replace(
        '<span class="logo-text">SideHustle<span>Guard</span></span>',
        NAV_WORDMARK,
    )
    text = text.replace(
        '<span class="footer-logo">SideHustle<span>Guard</span></span>',
        FOOTER_WORDMARK,
    )
    return text


# ---- Driver -------------------------------------------------------------


def migrate_file(path: Path, dry_run: bool = False) -> dict:
    src = path.read_text(encoding="utf-8")
    if already_migrated(src):
        return {"file": path.name, "status": "skip-already-migrated"}

    out = src
    out = replace_fonts_link(out)
    out = strip_inline_root_and_reset(out)
    out = swap_fonts(out)
    out = swap_hex(out)
    out = swap_rgba(out)
    out = fix_logo_svg_size(out)
    out = replace_shield(out)
    out = replace_wordmarks(out)

    changed = out != src

    # Diagnostics: did each major transformation actually fire?
    diag = {
        "design_system_added": "design-system.css" in out,
        "new_body_present": NEW_BODY_LINE in out,
        "arc_dot_present": 'M6 30 Q24 4 42 30' in out,
        "italic_guard_present": ">guard</span>" in out,
        "playfair_residue": "Playfair Display" in out,
        "dm_sans_residue": "DM Sans" in out,
        "old_navy_hex_residue": "#1c2b4a" in out.lower(),
        "old_gold_hex_residue": "#c9973a" in out.lower(),
    }

    if changed and not dry_run:
        path.write_text(out, encoding="utf-8")

    return {
        "file": path.name,
        "status": "migrated" if changed else "no-change",
        **diag,
    }


def list_targets(only: list[str] | None) -> list[Path]:
    if only:
        return [ROOT / name for name in only]
    targets = []
    for p in sorted(ROOT.glob("*.html")):
        if p.name in PHASE4_PAGES or p.name in SKIP_PAGES:
            continue
        targets.append(p)
    return targets


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", nargs="*", help="Optional explicit file list")
    args = ap.parse_args()

    targets = list_targets(args.only)
    results = [migrate_file(t, dry_run=args.dry_run) for t in targets]

    # Summary
    migrated = sum(1 for r in results if r["status"] == "migrated")
    skipped = sum(1 for r in results if r["status"].startswith("skip"))
    nochange = sum(1 for r in results if r["status"] == "no-change")

    # Flag any residues
    residue_keys = (
        "playfair_residue",
        "dm_sans_residue",
        "old_navy_hex_residue",
        "old_gold_hex_residue",
    )
    flagged = [r for r in results if any(r.get(k) for k in residue_keys)]

    print(f"Processed: {len(results)}")
    print(f"  migrated:  {migrated}")
    print(f"  no-change: {nochange}")
    print(f"  skipped:   {skipped}")
    if flagged:
        print("\nFlagged files (residue detected):")
        for r in flagged:
            keys = [k for k in residue_keys if r.get(k)]
            print(f"  {r['file']}: {','.join(keys)}")
    else:
        print("\nNo residue detected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
