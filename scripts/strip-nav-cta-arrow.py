#!/usr/bin/env python3
"""
Strip the literal " →" character from the nav CTA text on every page.

After this runs, the markup becomes:
    <a class="btn btn-cta" href="/tool">Check my hustle</a>
The visual arrow is supplied by the `nav .btn-cta::after` rule in
assets/css/design-system.css (apricot circle + inlined SVG arrow).

Targets two patterns:

  1) The standard one-line link used on every guide + landing + calc
     page (~88 occurrences):
       <a class="btn btn-cta" href="/tool">Check my hustle →</a>

  2) The index.html "desktop variant" span inside the more elaborate
     nav CTA composite (1 occurrence):
       <span class="ds-cta-desktop">Check my hustle →</span>

Anything else with "Check my hustle →" (hero buttons, body content,
comments) is left alone — only the two specific nav patterns above
are rewritten.

Run from project root. Dry-run flag previews without writing.
"""

import os
import re
import sys

PATTERNS = [
    # Standard nav CTA used everywhere except index.html
    (
        re.compile(r'(<a class="btn btn-cta" href="/tool">Check my hustle) →(</a>)'),
        r'\1\2',
    ),
    # index.html desktop-variant span inside the composite CTA
    (
        re.compile(r'(<span class="ds-cta-desktop">Check my hustle) →(</span>)'),
        r'\1\2',
    ),
]


def process(path: str, write: bool):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    hits = 0
    for pat, rep in PATTERNS:
        content, n = pat.subn(rep, content)
        hits += n
    if hits == 0:
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
        f"{total_hits} arrow{'s' if total_hits != 1 else ''} stripped."
    )


if __name__ == '__main__':
    main()
