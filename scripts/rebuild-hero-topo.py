#!/usr/bin/env python3
"""
Phase 22.5 — Rebuild the rotating hero-backdrop topo SVG with a
square-bounded viewBox so rotation stops showing rectangle corners.

The pre-existing SVG on calc pages used viewBox="0 0 1200 360" — a
wide-short rectangle matching the hero shape. When that SVG rotates
via Phase 21.2's .tool-drift animation, its corners sweep through
the visible hero area, exposing the SVG's rectangular edge.

The crypto-tax-calculator doesn't have this problem because its
hero is much taller (full-page section) and its SVG viewBox is
closer to square (1400x900). On short calc-page heroes, the
aspect-ratio mismatch makes the rotation feel jagged.

Fix: replace each calc page's wide-short SVG with a SQUARE 2000x2000
viewBox containing topo lines distributed across THREE clusters
(lower-left + center + upper-right). Also update the CSS via inline
<style> so .hero-backdrop.tool-drift extends well beyond the hero
(inset negative on all sides, width 120%, height 220%) — its
rectangular bounds sit outside the hero's clip region throughout
the rotation.

Run from repo root:  python3 scripts/rebuild-hero-topo.py
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

TARGETS = [
    "audit-risk-estimator.html",
    "tax-guard-calculator.html",
    "scorp-savings-calculator.html",
    "quarterly-tax-calculator.html",
    "self-employment-tax-calculator.html",
    "1099k-threshold-calculator.html",
    "tax-penalty-estimator.html",
    "w4-withholding-calculator.html",
]


# New square-bounded topo SVG. ViewBox 2000x2000 with apricot + indigo
# ellipse clusters distributed across the canvas. preserveAspectRatio
# "xMidYMid slice" lets the SVG scale to fill its element while keeping
# the topo lines coherent regardless of crop.
NEW_SVG = (
    '<svg class="hero-backdrop tool-drift" '
    'viewBox="0 0 2000 2000" '
    'preserveAspectRatio="xMidYMid slice" '
    'aria-hidden="true">'
    # Lower-left apricot cluster
    '<g fill="none" stroke="#e89464" stroke-opacity="0.18" stroke-width="1">'
    '<ellipse cx="400" cy="1600" rx="680" ry="280" transform="rotate(-12 400 1600)"/>'
    '<ellipse cx="408" cy="1576" rx="620" ry="248" transform="rotate(-10 408 1576)"/>'
    '<ellipse cx="416" cy="1552" rx="560" ry="216" transform="rotate(-8 416 1552)"/>'
    '<ellipse cx="424" cy="1528" rx="500" ry="184" transform="rotate(-6 424 1528)"/>'
    '<ellipse cx="432" cy="1504" rx="440" ry="152" transform="rotate(-4 432 1504)"/>'
    '</g>'
    # Upper-right apricot cluster
    '<g fill="none" stroke="#e89464" stroke-opacity="0.18" stroke-width="1">'
    '<ellipse cx="1600" cy="400" rx="540" ry="220" transform="rotate(18 1600 400)"/>'
    '<ellipse cx="1608" cy="388" rx="480" ry="194" transform="rotate(16 1608 388)"/>'
    '<ellipse cx="1616" cy="376" rx="416" ry="166" transform="rotate(14 1616 376)"/>'
    '<ellipse cx="1624" cy="364" rx="354" ry="138" transform="rotate(12 1624 364)"/>'
    '<ellipse cx="1632" cy="352" rx="290" ry="110" transform="rotate(10 1632 352)"/>'
    '</g>'
    # Indigo center cluster (filler so rotation never shows blank corners)
    '<g fill="none" stroke="#2d3068" stroke-opacity="0.06" stroke-width="1">'
    '<ellipse cx="1000" cy="1000" rx="780" ry="360" transform="rotate(30 1000 1000)"/>'
    '<ellipse cx="1000" cy="1000" rx="680" ry="320" transform="rotate(45 1000 1000)"/>'
    '<ellipse cx="1000" cy="1000" rx="580" ry="280" transform="rotate(60 1000 1000)"/>'
    '<ellipse cx="1000" cy="1000" rx="480" ry="240" transform="rotate(75 1000 1000)"/>'
    '</g>'
    '</svg>'
)


# CSS to extend the SVG element beyond the hero so rotation corners
# stay clipped. Injected into each calc page's inline <style> block.
NEW_CSS = """
/* Phase 22.5 — extend the rotating topo SVG beyond the hero on all
 * sides so its rectangular corners stay outside the hero's overflow
 * clip during rotation. Without this overscan the SVG edges sweep
 * into view on every quarter-turn (visible on short-hero calc pages
 * because the original 1200×360 viewBox is too wide-short to hide
 * its corners). */
.hero-backdrop.tool-drift {
  position: absolute;
  left: -10%; right: -10%;
  top: -60%; bottom: -60%;
  width: 120%;
  height: 220%;
  pointer-events: none;
  transform-origin: center;
}
"""


def replace_svg(text: str) -> tuple[str, bool]:
    """
    Replace the existing hero-backdrop tool-drift SVG block with the new
    square-bounded version. Matches the multi-line <svg> ... </svg> block.
    """
    # Pattern matches any <svg class="hero-backdrop tool-drift" ...>...</svg>
    pattern = re.compile(
        r'<svg class="hero-backdrop tool-drift"[^>]*>.*?</svg>',
        re.DOTALL,
    )
    if not pattern.search(text):
        return text, False
    new_text = pattern.sub(NEW_SVG, text, count=1)
    return new_text, True


def inject_overscan_css(text: str) -> tuple[str, bool]:
    """Inject the overscan CSS into the inline <style> block (right before </style>).
    Uses the FIRST </style> tag (the inline page styles, before any
    JSON-LD <script> blocks that may sit between </style> and </head>). """
    if "Phase 22.5 — extend the rotating topo SVG" in text:
        return text, False
    idx = text.find('</style>')
    if idx == -1:
        return text, False
    new_text = text[:idx] + NEW_CSS + "\n" + text[idx:]
    return new_text, True


def main() -> int:
    width = max(len(t) for t in TARGETS)
    for fname in TARGETS:
        path = ROOT / fname
        if not path.exists():
            print(f"  [MISSING] {fname}")
            continue
        text = path.read_text(encoding="utf-8")
        text, svg_ok = replace_svg(text)
        text, css_ok = inject_overscan_css(text)
        path.write_text(text, encoding="utf-8")
        print(f"  [{fname:<{width}}]  svg={'✓' if svg_ok else 'x'}  css={'✓' if css_ok else 'x'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
