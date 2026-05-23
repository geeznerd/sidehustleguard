#!/usr/bin/env python3
"""
Phase 5 article-template migration.

Applies the doordash-taxes.html template transforms (Commit 4) to the
65 other *-taxes.html article guides. Per-page transformations:

  1. Hero CSS: bump h1 to weight 400 + opsz/SOFT settings, larger clamp;
     wrap .hero in position:relative + overflow:hidden + inline topo SVG.
  2. h2 weight 700 → 400 with same settings.
  3. body p/li weight 300 → 400.
  4. Callout CSS: migrate left-border-strip pattern to Pattern #4 tinted
     paper cards. Class names stay the same so existing markup still
     works without touching it.
  5. cta-box CSS: add apricot blob + heavier H3 treatment.
  6. .hero-eyebrow CSS rule injected (paper pill with apricot dot).
  7. FAQ .faq-item CSS upgraded to Pattern #9 accordion (works for both
     flat <h3>/<p> markup AND <details>/<summary> markup).
  8. product-card .product-card-icon CSS upgraded to monogram-tile
     styling (rounded apricot-12 square with Fraunces italic letter).
     The page markup keeps its emoji content — pages that want monogram
     tiles need to swap the emoji for a letter manually. This script
     just updates the visual treatment.

The script is conservative: it edits CSS rules and leaves markup
content untouched (except for the hero topo SVG injection which is
required for the new layout to render correctly). Article body content,
JSON-LD blocks, internal links, affiliate URLs, and Gumroad URLs are
not touched.

Skips:
  - doordash-taxes.html (already restyled in Commit 4 as the template)
  - Non-article HTML (calculators, dashboard, tool, etc.)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path("/Users/dork/Desktop/sidehustleguard")

SKIP = {
    "doordash-taxes.html",
    "index.html",
    "guides.html",
    "tool.html",
    "dashboard.html",
    "quarterly-tax-system.html",
    "tax-checklist.html",  # Phase 5 Commit 6
    "short-term-rentals.html",  # Phase 5 Commit 8
    "audit-risk-estimator.html",
    "self-employment-tax-calculator.html",
    "quarterly-tax-calculator.html",
    "scorp-savings-calculator.html",
    "tax-guard-calculator.html",
    "privacy.html",
    "terms.html",
    "_template-article-card.html",
    "guide-section-options.html",
    "og-image.html",
}

# ============================================================================
# CSS rule rewrites — match a wide variety of pre-Phase-5 formulations
# ============================================================================

# Hero CSS pattern — must add hero-backdrop positioning. Use a flexible match
# that accepts the various padding/max-width values seen across pages.
HERO_CSS_RE = re.compile(
    r"\.hero\{padding:[^;]+;max-width:\d+px;margin:0 auto\}",
)

# Replacement for the matched .hero rule (preserves max-width by using a default)
# Note: leaves max-width at 820 which is article-friendly. Pages that want
# wider can override locally.
NEW_HERO_CSS = (
    ".hero{padding:64px 48px 48px;max-width:820px;margin:0 auto;position:relative;overflow:hidden}"
    "\n.hero .hero-backdrop{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}"
    "\n.hero-content{position:relative;z-index:1}"
    "\n.hero-eyebrow{display:inline-flex;align-items:center;gap:8px;background:var(--paper);"
    "border:1px solid var(--indigo-08);padding:8px 16px;border-radius:100px;font-size:11.5px;"
    "font-weight:600;color:var(--apricot);letter-spacing:.14em;text-transform:uppercase;"
    "margin-bottom:20px;line-height:1}"
    "\n.hero-eyebrow::before{content:'';width:6px;height:6px;border-radius:50%;background:var(--apricot);flex-shrink:0}"
)

# H1 weight + size — matches common pre-Phase-5 formulations
H1_PATTERNS = [
    (
        re.compile(
            r"h1\{font-family:'Fraunces',Georgia,serif;font-size:clamp\(\d+px,\d+(?:\.\d+)?vw,\d+px\);"
            r"font-weight:700;line-height:1\.\d+;color:var\(--indigo\);margin-bottom:\d+px\}",
        ),
        "h1{font-family:'Fraunces',Georgia,serif;font-size:clamp(38px,5vw,60px);font-weight:400;line-height:1.04;letter-spacing:-0.022em;color:var(--indigo);font-variation-settings:'opsz' 144,'SOFT' 30;margin-bottom:18px}",
    ),
]

H1_EM_PATTERN = (
    re.compile(r"h1 em\{font-style:italic;color:var\(--apricot\)\}"),
    "h1 em{font-style:italic;color:var(--apricot);font-weight:500}",
)

H2_PATTERN = (
    re.compile(
        r"h2\{font-family:'Fraunces',Georgia,serif;font-size:\d+px;font-weight:700;color:var\(--indigo\);margin:\d+px 0 \d+px;line-height:1\.\d+\}",
    ),
    "h2{font-family:'Fraunces',Georgia,serif;font-size:30px;font-weight:400;color:var(--indigo);margin:48px 0 14px;line-height:1.15;letter-spacing:-0.015em;font-variation-settings:'opsz' 144,'SOFT' 30}",
)

H2_EM_PATTERN = (
    re.compile(r"h2 em\{font-style:italic;color:var\(--apricot\)\}"),
    "h2 em{font-style:italic;color:var(--apricot);font-weight:500}",
)

# Body text weight (font-weight:300 → 400)
P_PATTERN = (
    re.compile(
        r"p\{font-size:\d+px;color:var\(--indigo-70\);line-height:1\.\d+;margin-bottom:\d+px;font-weight:300\}",
    ),
    "p{font-size:15.5px;color:var(--indigo-70);line-height:1.7;margin-bottom:14px;font-weight:400}",
)

LI_PATTERN = (
    re.compile(
        r"li\{font-size:\d+px;color:var\(--indigo-70\);line-height:1\.\d+;margin-bottom:\d+px;font-weight:300\}",
    ),
    "li{font-size:15.5px;color:var(--indigo-70);line-height:1.7;margin-bottom:6px;font-weight:400}",
)

# Callouts — left-border-strip → tinted paper cards
CALLOUT_BASE_PATTERN = (
    re.compile(r"\.callout\{border-radius:\d+px;padding:\d+px \d+px;margin:\d+px 0\}"),
    ".callout{background:var(--paper);border:1px solid var(--indigo-08);border-radius:14px;padding:18px 22px;margin:24px 0}",
)

CALLOUT_AMBER_PATTERN = (
    re.compile(r"\.callout-amber\{background:var\(--warn-bg\);border-left:\d+px solid var\(--warn\)\}"),
    ".callout-amber{background:var(--warn-bg);border-color:rgba(201,138,58,.18)}",
)

CALLOUT_GREEN_PATTERN = (
    re.compile(r"\.callout-green\{background:var\(--good-bg\);border-left:\d+px solid var\(--good\)\}"),
    ".callout-green{background:var(--good-bg);border-color:rgba(90,122,79,.18)}",
)

CALLOUT_NAVY_PATTERN = (
    re.compile(r"\.callout-navy\{background:rgba\(45,48,104,0\.\d+\);border-left:\d+px solid var\(--indigo\)\}"),
    ".callout-navy{background:var(--apricot-10);border-color:var(--apricot-soft)}",
)

# CTA box — add blob + better H3 styling
CTA_BOX_PATTERN = (
    re.compile(r"\.cta-box\{background:var\(--indigo\);border-radius:\d+px;padding:\d+px;text-align:center;margin:\d+px 0\}"),
    (".cta-box{background:var(--indigo);border-radius:22px;padding:48px 36px;text-align:center;margin:48px 0;position:relative;overflow:hidden}"
     "\n.cta-box::before{content:'';position:absolute;top:-120px;right:-100px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,var(--apricot-soft),transparent 65%);pointer-events:none}"
     "\n.cta-box > *{position:relative;z-index:1}"
     "\n.cta-box-eyebrow{font-size:11.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--apricot);margin-bottom:14px}"),
)

CTA_BOX_H3_PATTERN = (
    re.compile(r"\.cta-box h3\{font-family:'Fraunces',Georgia,serif;font-size:\d+px;color:var\(--paper\);margin-bottom:\d+px;font-weight:700\}"),
    ".cta-box h3{font-family:'Fraunces',Georgia,serif;font-size:clamp(26px,3.2vw,34px);color:var(--paper);margin-bottom:10px;font-weight:400;line-height:1.12;letter-spacing:-0.015em;font-variation-settings:'opsz' 144,'SOFT' 30}",
)

CTA_BOX_H3_EM_PATTERN = (
    re.compile(r"\.cta-box h3 em\{font-style:italic;color:var\(--apricot-hover\)\}"),
    ".cta-box h3 em{font-style:italic;color:var(--apricot);font-weight:500}",
)

CTA_BOX_P_PATTERN = (
    re.compile(r"\.cta-box p\{color:rgba\(255,255,255,\.\d+\);font-size:\d+px;margin-bottom:\d+px;font-weight:300\}"),
    ".cta-box p{color:var(--paper-70);font-size:15px;margin-bottom:22px;font-weight:400;line-height:1.55;max-width:480px;margin-left:auto;margin-right:auto}",
)

# Product card icon — emoji font size → monogram tile (apricot-12 rounded square)
PRODUCT_CARD_PATTERN = (
    re.compile(r"\.product-card\{background:var\(--cream\);border:1\.5px solid rgba\(232,148,100,\.\d+\);border-radius:\d+px;padding:\d+px \d+px;margin:\d+px 0;display:flex;gap:\d+px;align-items:flex-start\}"),
    ".product-card{background:var(--paper);border:1px solid var(--apricot-soft);border-radius:18px;padding:24px 28px;margin:32px 0;display:flex;gap:20px;align-items:flex-start}",
)

PRODUCT_CARD_ICON_PATTERN = (
    re.compile(r"\.product-card-icon\{font-size:\d+px;line-height:1;flex-shrink:0;margin-top:\d+px\}"),
    ".product-card-icon{width:48px;height:48px;border-radius:12px;background:var(--apricot-12);color:var(--apricot);font-family:'Fraunces',Georgia,serif;font-style:italic;font-weight:500;font-variation-settings:'opsz' 144,'SOFT' 30;font-size:26px;display:inline-flex;align-items:center;justify-content:center;line-height:1;flex-shrink:0;margin-top:2px}",
)

# Hero intro weight
HERO_INTRO_PATTERN = (
    re.compile(r"\.hero-intro\{font-size:\d+px;color:var\(--indigo-70\);font-weight:300;line-height:1\.\d+;max-width:\d+px;margin-bottom:\d+px\}"),
    ".hero-intro{font-size:17px;color:var(--indigo-70);font-weight:400;line-height:1.65;max-width:640px;margin-bottom:32px}",
)

# Topographic SVG block to inject inside .hero
TOPO_SVG = (
    '<svg class="hero-backdrop" viewBox="0 0 1200 360" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
    '<defs><radialGradient id="articleHeroGlow" cx="20%" cy="80%" r="55%">'
    '<stop offset="0%" stop-color="#e89464" stop-opacity="0.16"/>'
    '<stop offset="100%" stop-color="#e89464" stop-opacity="0"/>'
    '</radialGradient></defs>'
    '<rect width="1200" height="360" fill="url(#articleHeroGlow)"/>'
    '<g fill="none" stroke="#2d3068" stroke-opacity="0.06" stroke-width="1">'
    '<ellipse cx="220" cy="280" rx="400" ry="170" transform="rotate(-12 220 280)"/>'
    '<ellipse cx="214" cy="266" rx="365" ry="152" transform="rotate(-10.5 220 280)"/>'
    '<ellipse cx="208" cy="252" rx="330" ry="134" transform="rotate(-9 220 280)" class="contour-inner-3"/>'
    '<ellipse cx="202" cy="238" rx="295" ry="116" transform="rotate(-7.5 220 280)" class="contour-inner-3"/>'
    '<ellipse cx="196" cy="224" rx="260" ry="98" transform="rotate(-6 220 280)"/>'
    '</g>'
    '<g fill="none" stroke="#e89464" stroke-opacity="0.18" stroke-width="1">'
    '<ellipse cx="1040" cy="110" rx="240" ry="106" transform="rotate(14 1040 110)"/>'
    '<ellipse cx="1044" cy="102" rx="210" ry="92" transform="rotate(12 1040 110)" class="contour-inner-3"/>'
    '<ellipse cx="1048" cy="94" rx="180" ry="78" transform="rotate(10 1040 110)"/>'
    '</g>'
    '</svg>'
)

# FAQ accordion CSS — replaces the flat .faq-item CSS
# Note: works for both the flat h3/p markup (graceful fallback) and the new
# <details>/<summary> markup. The CSS targets .faq-item summary, so flat
# pages just won't have a summary and will fall back to the old h3/p look.
FAQ_CSS_PATTERN = (
    re.compile(
        r"\.faq-item\{border-bottom:1px solid var\(--indigo-08\);padding:\d+px 0\}"
        r"\s*\.faq-item:last-child\{border-bottom:none\}"
        r"\s*\.faq-item h3\{font-size:\d+px;font-weight:600;color:var\(--indigo\);margin:0 0 \d+px;line-height:1\.\d+\}"
        r"\s*\.faq-item p\{font-size:\d+px;color:var\(--indigo-70\);line-height:1\.\d+;margin:0;font-weight:300\}"
        r"\s*\.faq-item p strong\{color:var\(--indigo\);font-weight:600\}"
        r"\s*\.faq-item p a\{color:var\(--apricot\);text-decoration:none\}"
        r"\s*\.faq-item p a:hover\{text-decoration:underline\}",
    ),
    (
        "/* Pattern #9 accordion */\n"
        ".faq-item{border-bottom:1px solid var(--indigo-08)}\n"
        ".faq-item:last-child{border-bottom:none}\n"
        ".faq-item details{padding:0}\n"
        ".faq-item summary{list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:20px 0;font-size:16px;font-weight:500;color:var(--indigo);line-height:1.4}\n"
        ".faq-item summary::-webkit-details-marker{display:none}\n"
        ".faq-item summary::after{content:'';width:24px;height:24px;border-radius:50%;border:1px solid var(--indigo-18);background-image:linear-gradient(to right,var(--indigo) 0,var(--indigo) 100%),linear-gradient(to bottom,var(--indigo) 0,var(--indigo) 100%);background-size:10px 1.5px,1.5px 10px;background-position:center;background-repeat:no-repeat;flex-shrink:0;transition:transform var(--dur-default) var(--ease-default)}\n"
        ".faq-item details[open] summary::after{background-image:linear-gradient(to right,var(--apricot) 0,var(--apricot) 100%);background-size:10px 1.5px;border-color:var(--apricot)}\n"
        ".faq-item h3{font-size:16px;font-weight:500;color:var(--indigo);margin:0 0 8px;line-height:1.4;padding:20px 0 0}\n"
        ".faq-item h3 + p{padding:0 0 22px}\n"
        ".faq-item p{font-size:14.5px;color:var(--indigo-70);line-height:1.65;margin:0 0 10px;font-weight:400}\n"
        ".faq-item p:last-child{margin-bottom:0}\n"
        ".faq-item p strong{color:var(--indigo);font-weight:600}\n"
        ".faq-item p a{color:var(--apricot);text-decoration:none}\n"
        ".faq-item p a:hover{text-decoration:underline}"
    ),
)


# Answer-box restyling (indigo preview-card)
ANSWER_BOX_PATTERN = (
    re.compile(r"\.answer-box\{background:var\(--warn-bg\);border-left:\d+px solid var\(--warn\);border-radius:0 \d+px \d+px 0;padding:\d+px \d+px;margin-bottom:\d+px;font-size:\d+px;font-weight:500;color:var\(--indigo\);line-height:1\.\d+\}"),
    (".answer-box{background:var(--indigo);color:var(--paper);border-radius:18px;padding:24px 28px;margin-bottom:40px;font-size:15px;font-weight:400;line-height:1.65;position:relative;overflow:hidden}"
     "\n.answer-box::before{content:'';position:absolute;top:-60px;right:-60px;width:180px;height:180px;border-radius:50%;background:radial-gradient(circle,var(--apricot-soft),transparent 65%);pointer-events:none}"
     "\n.answer-box-inner{position:relative;z-index:1;display:flex;gap:14px;align-items:flex-start}"
     "\n.answer-box-icon{flex-shrink:0;color:var(--apricot);margin-top:1px}"
     "\n.answer-box-icon svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}"
     "\n.answer-box-body{flex:1;min-width:0}"
     "\n.answer-box-body strong{color:var(--apricot);font-weight:500;font-family:'Fraunces',Georgia,serif;font-style:italic;font-variation-settings:'opsz' 144,'SOFT' 30}"),
)


# Hero markup wrapper — wraps the .hero div content in .hero-content and
# inserts the topo SVG. Only fires if the page doesn't already have
# .hero-backdrop (i.e., wasn't already migrated).
HERO_MARKUP_RE = re.compile(
    r'<div class="hero">\s*\n?(.*?)\n?</div>\s*\n\s*<div class="content"',
    re.DOTALL,
)


def upgrade(path: Path, dry_run: bool = False) -> dict:
    src = path.read_text(encoding="utf-8")
    out = src
    diag = {"file": path.name}

    if "hero-backdrop" in out:
        diag["status"] = "already-migrated"
        return diag

    # CSS substitutions
    for label, (pat, rep) in [
        ("h1", H1_PATTERNS[0]),
        ("h1_em", H1_EM_PATTERN),
        ("h2", H2_PATTERN),
        ("h2_em", H2_EM_PATTERN),
        ("p", P_PATTERN),
        ("li", LI_PATTERN),
        ("callout_base", CALLOUT_BASE_PATTERN),
        ("callout_amber", CALLOUT_AMBER_PATTERN),
        ("callout_green", CALLOUT_GREEN_PATTERN),
        ("callout_navy", CALLOUT_NAVY_PATTERN),
        ("cta_box", CTA_BOX_PATTERN),
        ("cta_box_h3", CTA_BOX_H3_PATTERN),
        ("cta_box_h3_em", CTA_BOX_H3_EM_PATTERN),
        ("cta_box_p", CTA_BOX_P_PATTERN),
        ("product_card", PRODUCT_CARD_PATTERN),
        ("product_card_icon", PRODUCT_CARD_ICON_PATTERN),
        ("hero_intro", HERO_INTRO_PATTERN),
        ("answer_box", ANSWER_BOX_PATTERN),
        ("faq_css", FAQ_CSS_PATTERN),
    ]:
        new_out, n = pat.subn(rep, out, count=1)
        if n > 0:
            diag[label] = "swapped"
            out = new_out

    # Hero CSS rule (the simple .hero{...} declaration)
    new_out, n = HERO_CSS_RE.subn(NEW_HERO_CSS, out, count=1)
    if n > 0:
        diag["hero_css"] = "swapped"
        out = new_out

    # Markup: wrap .hero in topo backdrop + hero-content
    m = HERO_MARKUP_RE.search(out)
    if m:
        inner = m.group(1).strip()
        replacement = (
            '<div class="hero">\n'
            + TOPO_SVG + "\n"
            + '<div class="hero-content">\n'
            + inner + "\n"
            + "</div>\n"
            + "</div>\n"
            + '<div class="content"'
        )
        out = out[: m.start()] + replacement + out[m.end():]
        diag["markup_wrap"] = "done"

    if out != src:
        diag["status"] = "changed"
        if not dry_run:
            path.write_text(out, encoding="utf-8")
    else:
        diag["status"] = "no-change"

    return diag


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", nargs="*")
    args = ap.parse_args()

    targets: list[Path] = []
    if args.only:
        targets = [ROOT / name for name in args.only]
    else:
        for p in sorted(ROOT.glob("*.html")):
            if p.name in SKIP:
                continue
            targets.append(p)

    results = [upgrade(t, dry_run=args.dry_run) for t in targets]
    changed = sum(1 for r in results if r["status"] == "changed")
    nochange = sum(1 for r in results if r["status"] == "no-change")
    skipped = sum(1 for r in results if r["status"] == "already-migrated")
    print(f"Processed: {len(results)}")
    print(f"  changed:           {changed}")
    print(f"  no-change:         {nochange}")
    print(f"  already-migrated:  {skipped}")

    # Per-step success rate
    steps = (
        "hero_css", "h1", "h2", "p", "li", "hero_intro", "answer_box",
        "callout_base", "callout_amber", "cta_box", "product_card_icon",
        "faq_css", "markup_wrap",
    )
    step_counts = {s: sum(1 for r in results if r.get(s)) for s in steps}
    print("\nStep success counts (out of {}):".format(len(results)))
    for s in steps:
        print(f"  {s:25s}  {step_counts[s]:3d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
