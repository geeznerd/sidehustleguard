#!/usr/bin/env python3
"""
Apply Phase 5 hero treatment to the 5 calculator pages.

Each calculator currently has:
  .hero { padding:60px 48px 32px; max-width:880px; margin:0 auto; text-align:center }
  .hero-badge { ... small apricot pill ... }
  h1 { font-weight:700; ... }

This script upgrades them to:
  - Hero gets topo backdrop wrapper (.hero-relative)
  - .hero-badge gets a 6px apricot dot prefix + matching .ds-eyebrow-pill scale
  - H1 drops to font-weight:400 with 'opsz' 144,'SOFT' 30 variation settings
  - H1 size bumped slightly (matches .display-l proportions)
  - <div class="hero">...</div> wraps content in .hero-content and inserts
    an inline topographic SVG above

Other transformations not in this script (per-calculator unique work like
Pattern #6 paired pricing for scorp, Pattern #2 sliding list for quarterly,
killing the audit-risk shield SVG) happen as targeted manual edits below.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path("/Users/dork/Desktop/sidehustleguard")
CALC_PAGES = [
    "audit-risk-estimator.html",
    "self-employment-tax-calculator.html",
    "quarterly-tax-calculator.html",
    "scorp-savings-calculator.html",
    "tax-guard-calculator.html",
]

OLD_HERO_CSS = ".hero{padding:60px 48px 32px;max-width:880px;margin:0 auto;text-align:center}"
NEW_HERO_CSS = (
    ".hero{padding:72px 24px 44px;max-width:980px;margin:0 auto;text-align:center;position:relative;overflow:hidden}"
    "\n.hero .hero-backdrop{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}"
    "\n.hero-content{position:relative;z-index:1;max-width:760px;margin:0 auto}"
)

OLD_BADGE_CSS = (
    ".hero-badge{display:inline-flex;align-items:center;gap:8px;background:var(--apricot-soft);"
    "border:1px solid rgba(232,148,100,.25);padding:6px 14px;border-radius:100px;font-size:11px;"
    "font-weight:600;color:var(--apricot);letter-spacing:.06em;text-transform:uppercase;margin-bottom:18px}"
)
NEW_BADGE_CSS = (
    ".hero-badge{display:inline-flex;align-items:center;gap:8px;background:var(--paper);"
    "border:1px solid var(--indigo-08);padding:8px 16px;border-radius:100px;font-size:11.5px;"
    "font-weight:600;color:var(--apricot);letter-spacing:.14em;text-transform:uppercase;margin-bottom:22px;line-height:1}"
    "\n.hero-badge::before{content:'';width:6px;height:6px;border-radius:50%;background:var(--apricot);flex-shrink:0}"
)

OLD_H1 = "h1{font-family:'Fraunces',Georgia,serif;font-size:clamp(32px,4.5vw,52px);font-weight:700;line-height:1.15;color:var(--indigo);margin-bottom:14px}"
NEW_H1 = "h1{font-family:'Fraunces',Georgia,serif;font-size:clamp(40px,5.2vw,60px);font-weight:400;line-height:1.04;letter-spacing:-0.022em;color:var(--indigo);font-variation-settings:'opsz' 144,'SOFT' 30;margin-bottom:18px}"
NEW_H1_EM = "h1 em{font-style:italic;color:var(--apricot);font-weight:500}"

# Topographic SVG block injected at the start of the .hero div
TOPO_SVG = (
    '<svg class="hero-backdrop" viewBox="0 0 1200 360" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
    '<defs><radialGradient id="calcHeroGlow" cx="20%" cy="80%" r="55%">'
    '<stop offset="0%" stop-color="#e89464" stop-opacity="0.18"/>'
    '<stop offset="100%" stop-color="#e89464" stop-opacity="0"/>'
    '</radialGradient></defs>'
    '<rect width="1200" height="360" fill="url(#calcHeroGlow)"/>'
    '<g fill="none" stroke="#2d3068" stroke-opacity="0.07" stroke-width="1">'
    '<ellipse cx="240" cy="280" rx="420" ry="180" transform="rotate(-12 240 280)"/>'
    '<ellipse cx="234" cy="266" rx="385" ry="162" transform="rotate(-10.5 240 280)"/>'
    '<ellipse cx="228" cy="252" rx="350" ry="144" transform="rotate(-9 240 280)" class="contour-inner-3"/>'
    '<ellipse cx="222" cy="238" rx="315" ry="126" transform="rotate(-7.5 240 280)" class="contour-inner-3"/>'
    '<ellipse cx="216" cy="224" rx="280" ry="108" transform="rotate(-6 240 280)"/>'
    '<ellipse cx="210" cy="210" rx="245" ry="90" transform="rotate(-4.5 240 280)"/>'
    '</g>'
    '<g fill="none" stroke="#e89464" stroke-opacity="0.18" stroke-width="1">'
    '<ellipse cx="1020" cy="110" rx="270" ry="120" transform="rotate(18 1020 110)"/>'
    '<ellipse cx="1024" cy="102" rx="240" ry="106" transform="rotate(16 1020 110)"/>'
    '<ellipse cx="1028" cy="94" rx="210" ry="92" transform="rotate(14 1020 110)" class="contour-inner-3"/>'
    '<ellipse cx="1032" cy="86" rx="180" ry="78" transform="rotate(12 1020 110)" class="contour-inner-3"/>'
    '<ellipse cx="1036" cy="78" rx="150" ry="64" transform="rotate(10 1020 110)"/>'
    '</g>'
    '</svg>'
)


def upgrade_calc(path: Path) -> dict:
    src = path.read_text(encoding="utf-8")
    out = src
    diag = {"file": path.name}

    # CSS swaps
    if OLD_HERO_CSS in out:
        out = out.replace(OLD_HERO_CSS, NEW_HERO_CSS, 1)
        diag["hero_css"] = "swapped"
    if OLD_BADGE_CSS in out:
        out = out.replace(OLD_BADGE_CSS, NEW_BADGE_CSS, 1)
        diag["badge_css"] = "swapped"
    if OLD_H1 in out:
        out = out.replace(OLD_H1, NEW_H1, 1)
        diag["h1_css"] = "swapped"
        # Append h1 em rule if not already specifying weight:500
        if "h1 em{font-style:italic;color:var(--apricot);font-weight:500}" not in out:
            # try the original h1 em rule (font-weight likely missing or different)
            out = re.sub(
                r"h1 em\{[^}]*\}",
                NEW_H1_EM,
                out,
                count=1,
            )

    # Markup: wrap hero in topo backdrop
    # Find the FIRST `<div class="hero">` and inject topo SVG + .hero-content wrapper
    # Use a regex to find the div opening and the matching closing div
    pattern = re.compile(
        r'<div class="hero">\s*\n?(.*?)\n?</div>',
        re.DOTALL,
    )
    m = pattern.search(out)
    if m:
        inner = m.group(1).strip()
        replacement = (
            '<div class="hero">\n'
            + TOPO_SVG + '\n'
            + '<div class="hero-content">\n'
            + inner + '\n'
            + '</div>\n'
            + '</div>'
        )
        # Only do this if hero-content isn't already present
        if 'hero-content' not in m.group(0):
            out = out[:m.start()] + replacement + out[m.end():]
            diag["markup_wrap"] = "done"

    if out != src:
        path.write_text(out, encoding="utf-8")
        diag["status"] = "changed"
    else:
        diag["status"] = "no-change"
    return diag


def main() -> int:
    for name in CALC_PAGES:
        path = ROOT / name
        result = upgrade_calc(path)
        print(result)
    return 0


if __name__ == "__main__":
    main()
