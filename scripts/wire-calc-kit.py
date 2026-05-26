#!/usr/bin/env python3
"""
Phase 21.2 stage 2 — Wire money inputs to CalcKit on each calculator.

After scripts/apply-tool-kit.py converted .input-money → .tool-input
markup AND stripped inline `oninput="recalc()"` handlers, the calcs
no longer recompute on input. Also, the inputs now display formatted
strings ("75,000") that break `parseFloat(input.value)`.

This script applies two fixes per file:

  1. Add a CalcKit binding block at the end of the inline <script>:

       ['id1','id2',...].forEach(function(id){
         var el = document.getElementById(id);
         if (el) CalcKit.bindMoneyInput(el, function(){ recalc(); });
       });

     The IDs come from inputs that now sit inside .tool-input wrappers
     (discovered by parsing the page's current markup).

  2. Patch the existing recalc function so parseFloat calls handle
     comma-formatted values:

        parseFloat(document.getElementById('X').value)
          →  parseFloat(document.getElementById('X').value.replace(/,/g,''))

     Only applied to money input IDs — keeps non-money parsing intact.

Idempotent — re-running is safe.

Run from repo root:  python3 scripts/wire-calc-kit.py
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


def find_money_input_ids(text: str) -> list[str]:
    """
    Find every <input id="X" ...> nested inside a <div class="tool-input ...">
    wrapper. These are the money inputs that need CalcKit binding +
    comma-stripped parsing.
    """
    pattern = re.compile(
        r'<div class="tool-input[^"]*">[^<]*'
        r'<span class="prefix"[^>]*>\$</span>[^<]*'
        r'<input[^>]*\bid="([^"]+)"',
        re.DOTALL,
    )
    return pattern.findall(text)


def patch_parsefloat(text: str, ids: list[str]) -> tuple[str, int]:
    """
    For each money-input ID, rewrite parseFloat reads from its .value
    to strip commas first. Catches both single + double quote forms
    and the common `getElementById('X').value` pattern.
    """
    n = 0
    for id_ in ids:
        for quote in ("'", '"'):
            old = f"document.getElementById({quote}{id_}{quote}).value"
            new = f"document.getElementById({quote}{id_}{quote}).value.replace(/,/g,'')"
            # Only replace inside parseFloat(...) calls so we don't touch
            # any non-numeric reads. Use a regex with a capture group.
            pattern = re.compile(
                r"(parseFloat\(\s*)" + re.escape(old) + r"(\s*\))"
            )
            text, count = pattern.subn(lambda m: m.group(1) + new + m.group(2), text)
            n += count
    return text, n


def inject_kit_binding(text: str, ids: list[str]) -> tuple[str, bool]:
    """
    Add the CalcKit.bindMoneyInput wiring at the end of the calculator's
    inline <script> (right before the closing </script>).

    Searches for the LAST </script> before </body> that contains a
    recalc function, then injects the binding block just before it.
    """
    if "CalcKit.bindMoneyInput" in text:
        return text, False  # already wired
    if not ids:
        return text, False  # no money inputs to bind

    ids_literal = ",".join(f"'{i}'" for i in ids)
    snippet = (
        "\n\n// ── Phase 21.2 — Wire money inputs to CalcKit ──────────────\n"
        "// Live thousand-separator formatting + recalc on every keystroke.\n"
        "// recalc() is the existing calculator-specific compute function.\n"
        f"[{ids_literal}].forEach(function(id){{\n"
        "  var el = document.getElementById(id);\n"
        "  if (el && window.CalcKit) CalcKit.bindMoneyInput(el, function(){ recalc(); });\n"
        "});\n"
    )

    # Find the inline <script> that contains recalc — inject snippet just
    # before its closing </script>.
    pattern = re.compile(
        r'(<script>\s*(?:(?!</script>).)*?function\s+recalc\s*\(.*?)(</script>)',
        re.DOTALL,
    )
    m = pattern.search(text)
    if not m:
        return text, False
    return text[:m.start(2)] + snippet + text[m.start(2):], True


def process(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    ids = find_money_input_ids(text)
    text, n_patched = patch_parsefloat(text, ids)
    text, wired    = inject_kit_binding(text, ids)
    path.write_text(text, encoding="utf-8")
    return {"ids": ids, "patched": n_patched, "wired": wired}


def main() -> int:
    width = max(len(t) for t in TARGETS)
    for fname in TARGETS:
        path = ROOT / fname
        if not path.exists():
            print(f"  [MISSING] {fname}")
            continue
        r = process(path)
        ids_str = ",".join(r["ids"]) if r["ids"] else "(none)"
        print(f"  [{fname:<{width}}]  ids={ids_str}  patched={r['patched']}  wired={'✓' if r['wired'] else 'x'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
