#!/usr/bin/env python3
"""
Replace the nav CTA's pseudo-element apricot end-cap (rendered via
`nav .btn-cta::after` with an inlined SVG background-image) with real
DOM nodes: a span for the circle + a real <svg> child for the arrow.

Why: animating `background-position` on hover (current approach for the
arrow shift) triggers paint. Animating `transform: translateX()` on a
real SVG element composites on the GPU — same visual, no paint cost.
Per Emil Kowalski's design-engineering review.

Only the NAV CTA is migrated. Hero / CTA-band `.btn-cta` instances use
different copy ("Run my free check", "Start free check", etc.) and
don't have an end-cap circle, so they're left alone.

Patterns matched (precise — text-anchored so hero CTAs are untouched):

  1) Standard nav CTA (90+ pages):
       <a class="btn btn-cta" href="/tool">Check my hustle</a>

  2) index.html variant with aria-label:
       <a class="btn btn-cta" href="/tool" aria-label="...">Check my hustle</a>

Both become:

       <a class="btn btn-cta" href="/tool" [aria-label=...]>Check my hustle<span
         class="cta-arrow-cap" aria-hidden="true"><svg class="cta-arrow-svg"
         viewBox="0 0 16 16" fill="none" stroke="currentColor"
         stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"
         ><path d="M3 8 H12 M8 4 L12 8 L8 12"/></svg></span></a>

Run from project root. --dry-run flag previews without writing.
"""

import os
import re
import sys

# The new arrow markup. `currentColor` on stroke lets CSS color the arrow
# without re-declaring the value in the SVG itself.
ARROW_MARKUP = (
    '<span class="cta-arrow-cap" aria-hidden="true">'
    '<svg class="cta-arrow-svg" viewBox="0 0 16 16" fill="none" '
    'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
    'stroke-linejoin="round">'
    '<path d="M3 8 H12 M8 4 L12 8 L8 12"/>'
    '</svg></span>'
)

PATTERNS = [
    # Standard one-line nav CTA (without aria-label) — 90+ pages
    (
        re.compile(r'(<a class="btn btn-cta" href="/tool">Check my hustle)(</a>)'),
        r'\1' + ARROW_MARKUP + r'\2',
    ),
    # index.html variant with aria-label
    (
        re.compile(r'(<a class="btn btn-cta" href="/tool" aria-label="[^"]*">Check my hustle)(</a>)'),
        r'\1' + ARROW_MARKUP + r'\2',
    ),
]


def process(path: str, write: bool):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    hits = 0
    for pat, rep in PATTERNS:
        content, n = pat.subn(rep, content)
        hits += n
    # Skip if the file already contains the new arrow markup (idempotent)
    if hits == 0:
        return 0
    # Sanity check: don't double-apply if a file somehow has both
    # the old AND new patterns mixed
    if content.count('cta-arrow-cap') > content.count('btn-cta') * 2:
        print(f"  SKIP (looks already-migrated or weird): {path}")
        return 0
    if write:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    return hits


def main():
    dry = '--dry-run' in sys.argv
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    updated = 0
    total_hits = 0
    for entry in sorted(os.listdir(root)):
        if not entry.endswith('.html'):
            continue
        path = os.path.join(root, entry)
        hits = process(path, write=not dry)
        if hits:
            updated += 1
            total_hits += hits
            print(f"  {'WOULD UPDATE' if dry else 'updated'}: {entry} ({hits} hit{'s' if hits > 1 else ''})")
    print(
        f"\n{'Dry-run: ' if dry else ''}{updated} file{'s' if updated != 1 else ''} touched, "
        f"{total_hits} arrow{'s' if total_hits != 1 else ''} inlined."
    )


if __name__ == '__main__':
    main()
