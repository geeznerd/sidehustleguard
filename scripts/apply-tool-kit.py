#!/usr/bin/env python3
"""
Phase 21.2 — Apply the interactive-tool kit to the remaining 7 calc pages.

This script handles the *common* transformations that every calculator
needs identically:

  1. Inject  <script src="/assets/js/calc-kit.js"></script>  after the
     <link href="/assets/css/design-system.css">  so the kit utilities
     are available before any inline <script> runs.

  2. Add  class="tool-drift"  to the hero-backdrop SVG so it slowly
     rotates (120s linear, gated on prefers-reduced-motion).

  3. Inject  <div class="tool-aurora" aria-hidden="true"></div>
     immediately after the hero-backdrop SVG, so the apricot/green
     glow blobs render over the topo.

  4. Convert  .hero-badge  markup → .tool-eye  with a pulsing dot:
        <div class="hero-badge">Text</div>
        →
        <span class="tool-eye"><span class="pulse" aria-hidden="true"></span> Text</span>

  5. Convert money input wrappers from .input-money (CSS ::before $)
     to .tool-input (real <span class="prefix">$</span> + bare input):
        <div class="input-money [input-lg]">
          <input id="x" type="number" ...oninput="recalc()"... />
        </div>
        →
        <div class="tool-input [is-lg]">
          <span class="prefix" aria-hidden="true">$</span>
          <input id="x" type="text" inputmode="decimal" ... />
        </div>
     The script removes inline `oninput="recalc()"` because CalcKit's
     bindMoneyInput attaches its own input listener (caller wires the
     callback in their inline <script>).

  6. Standardize hero / calc-wrap / calc-card / content padding to a
     uniform spec across all 8 calc pages.

Idempotent — re-running is safe (each transformation checks if it's
already applied). Pages that don't have a particular pattern (e.g.
no .hero-badge) just skip that transformation.

What this script does NOT do (per-page hand work):
  - Convert filing-status <select> → .tool-seg segmented control
  - Restructure the big-result markup to use <em>$</em>NNN format
  - Rewire JS to use CalcKit.bindMoneyInput + CalcKit.animateNumber
  - Restyle dark results-cards to light cream gradient

Those need per-page judgment + math preservation, so they're applied
manually after this script runs.

Run from repo root:  python3 scripts/apply-tool-kit.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TARGETS = [
    "self-employment-tax-calculator.html",
    "quarterly-tax-calculator.html",
    "1099k-threshold-calculator.html",
    "scorp-savings-calculator.html",
    "w4-withholding-calculator.html",
    "tax-penalty-estimator.html",
    "audit-risk-estimator.html",
]


# Uniform padding spec — applied to inline <style> in every calc.
# These are find/replace pairs targeting the specific values that
# existed across the calcs before standardization. Some pages already
# use these exact values; the script no-ops there.
PADDING_REPLACEMENTS = [
    # Hero — desktop
    (r"\.hero\{padding:[^;}]*", ".hero{padding:72px 24px 44px"),
    # calc-wrap / tool-wrap — desktop
    (r"\.calc-wrap\{[^}]*padding:[^;}]*", lambda m: re.sub(
        r"padding:[^;}]*", "padding:0 48px 32px", m.group(0))),
    (r"\.tool-wrap\{[^}]*padding:[^;}]*", lambda m: re.sub(
        r"padding:[^;}]*", "padding:0 48px 32px", m.group(0))),
]


def inject_kit_script(text: str) -> tuple[str, bool]:
    """Add the calc-kit.js <script> tag right after design-system.css."""
    if "/assets/js/calc-kit.js" in text:
        return text, False
    needle = '<link href="/assets/css/design-system.css" rel="stylesheet"/>'
    if needle not in text:
        return text, False
    new = (
        needle
        + "\n<!-- Interactive tool kit — shared utilities (Phase 21) -->"
        + '\n<script src="/assets/js/calc-kit.js"></script>'
    )
    return text.replace(needle, new, 1), True


def add_drift_to_topo(text: str) -> tuple[str, bool]:
    """Add .tool-drift class to the hero-backdrop SVG so it rotates."""
    if 'class="hero-backdrop tool-drift"' in text:
        return text, False
    return (
        text.replace(
            '<svg class="hero-backdrop"',
            '<svg class="hero-backdrop tool-drift"', 1
        ),
        True,
    )


def inject_aurora(text: str) -> tuple[str, bool]:
    """Inject <div class="tool-aurora"> right after the hero-backdrop SVG."""
    if 'class="tool-aurora"' in text:
        return text, False
    # Find the </svg> that closes the hero-backdrop SVG. We anchor on
    # the opening <svg class="hero-backdrop"... and walk to its matching
    # </svg>. Pages with multiple <svg> elements will only match the
    # first one because we use a non-greedy regex.
    pattern = re.compile(
        r'(<svg class="hero-backdrop[^"]*"[^>]*>.*?</svg>)',
        re.DOTALL,
    )
    m = pattern.search(text)
    if not m:
        return text, False
    insert = m.group(1) + '\n<div class="tool-aurora" aria-hidden="true"></div>'
    return text[:m.start()] + insert + text[m.end():], True


def convert_hero_badge(text: str) -> tuple[str, bool]:
    """Convert the static .hero-badge into the animated .tool-eye."""
    if 'class="tool-eye"' in text:
        return text, False
    pattern = re.compile(
        r'<div class="hero-badge"[^>]*>\s*(.*?)\s*</div>',
        re.DOTALL,
    )
    m = pattern.search(text)
    if not m:
        return text, False
    inner = re.sub(r"\s+", " ", m.group(1)).strip()
    replacement = (
        '<span class="tool-eye"><span class="pulse" aria-hidden="true"></span> '
        + inner + "</span>"
    )
    return text[:m.start()] + replacement + text[m.end():], True


def convert_money_input(text: str) -> tuple[str, int]:
    """
    Convert each `<div class="input-money [input-lg]"> <input ...> </div>`
    block to the `.tool-input` pattern with a real <span class="prefix">$</span>.

    The inline `oninput="recalc()"` is stripped — pages will wire the
    callback via CalcKit.bindMoneyInput in their inline <script> instead.
    `type="number"` is rewritten to `type="text" inputmode="decimal"` so
    thousand-separator commas can be displayed live.

    Returns (new_text, count_replaced).
    """
    pattern = re.compile(
        r'<div class="input-money(?P<mods>[^"]*)">\s*'
        r'(?P<inp><input[^>]+>)\s*</div>',
        re.DOTALL,
    )

    def rewrite(m: re.Match) -> str:
        mods = m.group("mods").strip()
        # input-lg becomes is-lg
        is_lg = " is-lg" if "input-lg" in mods else ""
        inp = m.group("inp")
        # rewrite type + remove oninput recalc + add inputmode + autocomplete
        inp = re.sub(r'\btype="number"',          'type="text"', inp)
        inp = re.sub(r'\binputmode="[^"]*"',      'inputmode="decimal"', inp)
        if 'inputmode=' not in inp:
            inp = inp.replace('<input ', '<input inputmode="decimal" ', 1)
        inp = re.sub(r'\soninput="recalc\(\)"',   '', inp)
        inp = re.sub(r'\sonchange="recalc\(\)"',  '', inp)
        if 'autocomplete=' not in inp:
            inp = inp.replace('<input ', '<input autocomplete="off" ', 1)
        return (
            f'<div class="tool-input{is_lg}">'
            f'<span class="prefix" aria-hidden="true">$</span>'
            f'{inp}'
            f'</div>'
        )

    new_text, n = pattern.subn(rewrite, text)
    return new_text, n


def standardize_padding(text: str) -> tuple[str, int]:
    """Apply the uniform padding spec to inline <style> blocks."""
    n = 0
    for needle, replacement in PADDING_REPLACEMENTS:
        if callable(replacement):
            new, count = re.subn(needle, replacement, text)
        else:
            new, count = re.subn(needle, replacement, text)
        if count > 0 and new != text:
            text = new
            n += count
    return text, n


def process(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    report = {}

    text, did = inject_kit_script(text);     report["kit-script"] = did
    text, did = add_drift_to_topo(text);     report["drift"]      = did
    text, did = inject_aurora(text);         report["aurora"]     = did
    text, did = convert_hero_badge(text);    report["eye-pill"]   = did
    text, n   = convert_money_input(text);   report["tool-input"] = n
    text, n   = standardize_padding(text);   report["padding"]    = n

    path.write_text(text, encoding="utf-8")
    return report


def main() -> int:
    width = max(len(t) for t in TARGETS)
    for fname in TARGETS:
        path = ROOT / fname
        if not path.exists():
            print(f"  [MISSING] {fname}")
            continue
        r = process(path)
        parts = ", ".join(
            f"{k}:{('✓' if v is True else 'x' if v is False else v)}"
            for k, v in r.items()
        )
        print(f"  [{fname:<{width}}]  {parts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
