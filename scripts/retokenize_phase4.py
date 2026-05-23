#!/usr/bin/env python3
"""
Phase 4 retokenization.

Two passes:

  1. Strip multi-line inline :root{...} blocks (and adjacent inline base reset
     rules) that the Phase 3 single-line regex missed. design-system.css owns
     these tokens and resets now.

  2. Sweep legacy CSS var references to the new token names site-wide so the
     legacy alias block can be safely removed from design-system.css.

Mappings mirror the legacy alias block we are about to delete:

    --navy        -> --indigo
    --gold        -> --apricot
    --gold-lt     -> --apricot-hover
    --gold-pale   -> --apricot-soft
    --cream-d     -> --cream
    --white       -> --paper
    --muted       -> --indigo-70
    --dim         -> --indigo-55
    --border      -> --indigo-08
    --green       -> --good
    --green-bg    -> --good-bg
    --amber       -> --warn
    --amber-bg    -> --warn-bg
    --red         -> --risk
    --red-bg      -> --risk-bg

The replacement is scoped to `var(--name)` references so we don't accidentally
touch CSS variable *declarations* on pages that still define their own block
(those declarations get stripped in pass 1 anyway).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path("/Users/dork/Desktop/sidehustleguard")

# Files we never touch
SKIP = {
    "og-image.html",
    "_template-article-card.html",
    "guide-section-options.html",
}

# ---- Pass 1: strip multi-line :root + base reset ------------------------

# Matches multi-line :root{...} blocks like:
#   :root {
#     --navy:#2d3068; ...
#     --cream:#f0ece1; ...
#   }
ROOT_BLOCK_RE = re.compile(
    r":root\s*\{[^{}]*\}\s*\n",
    re.MULTILINE,
)

# Adjacent inline reset rules we can safely drop (the same rules live in
# design-system.css). We only drop them if they directly follow the :root block.
RESET_LINES = [
    r"\*,\*::before,\*::after\s*\{[^}]*\}\s*\n",
    r"img,picture,video,canvas,svg\s*\{[^}]*\}\s*\n",
    r"html\s*\{[^}]*\}\s*\n",
]


def strip_inline_root(text: str) -> str:
    # Only strip the FIRST :root block; later ones (if any) are page-specific overrides.
    new, n = ROOT_BLOCK_RE.subn("", text, count=1)
    if n == 0:
        return text
    # Try to also drop the adjacent base resets at the same position
    for r in RESET_LINES:
        new = re.sub(r, "", new, count=1)
    return new


# ---- Pass 2: var() reference rename ------------------------------------

VAR_MAP = {
    "--navy":      "--indigo",
    "--gold":      "--apricot",
    "--gold-lt":   "--apricot-hover",
    "--gold-pale": "--apricot-soft",
    "--cream-d":   "--cream",
    "--white":     "--paper",
    "--muted":     "--indigo-70",
    "--dim":       "--indigo-55",
    "--border":    "--indigo-08",
    "--green":     "--good",
    "--green-bg":  "--good-bg",
    "--amber":     "--warn",
    "--amber-bg":  "--warn-bg",
    "--red":       "--risk",
    "--red-bg":    "--risk-bg",
}

# Order matters: longest match first so `--gold-lt` doesn't get partially-renamed
# by the `--gold` rule.
VAR_ORDER = sorted(VAR_MAP.keys(), key=len, reverse=True)


def rename_var_refs(text: str) -> str:
    for old in VAR_ORDER:
        new = VAR_MAP[old]
        # Match var(--name) optionally with whitespace and ignore inside CSS
        # declarations (already covered: declarations stripped in pass 1).
        text = re.sub(
            r"var\(\s*" + re.escape(old) + r"\s*\)",
            f"var({new})",
            text,
        )
    return text


# ---- Driver ------------------------------------------------------------


def process(path: Path, dry_run: bool = False) -> dict:
    src = path.read_text(encoding="utf-8")
    out = strip_inline_root(src)
    out = rename_var_refs(out)
    changed = out != src
    if changed and not dry_run:
        path.write_text(out, encoding="utf-8")
    return {
        "file": path.name,
        "changed": changed,
        "stripped_root": ":root" not in out or src.count(":root") > out.count(":root"),
        "residue_navy": "var(--navy" in out,
        "residue_gold": "var(--gold" in out and "var(--gold-" not in out.replace("var(--gold)", ""),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    results = []
    for p in sorted(ROOT.glob("*.html")):
        if p.name in SKIP:
            continue
        results.append(process(p, dry_run=args.dry_run))

    changed = sum(1 for r in results if r["changed"])
    print(f"Processed: {len(results)}  changed: {changed}")

    residues = [
        r
        for r in results
        if "var(--navy" in (ROOT / r["file"]).read_text() or "var(--gold)" in (ROOT / r["file"]).read_text()
    ]
    if residues:
        print("\nResidue:")
        for r in residues:
            print(f"  {r['file']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
