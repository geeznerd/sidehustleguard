#!/usr/bin/env python3
"""
Fixes malformed related-grid sections across all HTML pages.

The bug: the internal linking script injected new cards INSIDE the
<div class="related-card-arrow"> of the first original card, displacing
its title outside the <a> tag.

Fix: extract all card hrefs+titles, deduplicate, rebuild cleanly.
"""

import re
import os
from glob import glob


def extract_cards_from_grid(grid_inner):
    """Extract all (href, title) pairs from related-grid inner HTML, handling malformed structure."""
    cards_ordered = []      # (href, title) in first-seen order
    seen_hrefs = {}         # href -> index in cards_ordered

    def add_card(href, title):
        href = href.strip()
        title = title.strip()
        if not href or not title:
            return
        if href in seen_hrefs:
            # Keep the longer/better title (originals tend to be more descriptive)
            idx = seen_hrefs[href]
            if len(title) > len(cards_ordered[idx][1]):
                cards_ordered[idx] = (href, title)
        else:
            seen_hrefs[href] = len(cards_ordered)
            cards_ordered.append((href, title))

    # Pattern A: well-formed multi-line cards
    for m in re.finditer(
        r'<a href="([^"]+)" class="related-card">\s*'
        r'<div class="related-card-arrow">→</div>\s*'
        r'<div class="related-card-title">([^<]+)</div>\s*</a>',
        grid_inner
    ):
        add_card(m.group(1), m.group(2))

    # Pattern B: inline-injected cards (single line, no extra whitespace)
    for m in re.finditer(
        r'<a href="([^"]+)" class="related-card">'
        r'<div class="related-card-arrow">→</div>'
        r'<div class="related-card-title">([^<]+)</div></a>',
        grid_inner
    ):
        add_card(m.group(1), m.group(2))

    # Pattern C: the outer malformed card — href from opening tag, title from displaced div
    # Outer card: <a href="..."> \n <div class="related-card-arrow">→\n (no </div> on same line)
    outer_m = re.search(
        r'<a href="([^"]+)" class="related-card">\s*\n\s*'
        r'<div class="related-card-arrow">→\s*\n',
        grid_inner
    )
    if outer_m:
        outer_href = outer_m.group(1)
        # Displaced title is the <div class="related-card-title"> that appears
        # AFTER </div>\n (which closes the arrow div) and before </a>
        displaced_m = re.search(
            r'</div>\s*\n\s*<div class="related-card-title">([^<]+)</div>',
            grid_inner
        )
        if displaced_m:
            add_card(outer_href, displaced_m.group(1))

    return cards_ordered


def build_clean_grid(cards):
    """Return clean <div class="related-grid">...</div> HTML."""
    card_lines = []
    for href, title in cards:
        card_lines.append(
            f'    <a href="{href}" class="related-card">\n'
            f'      <div class="related-card-arrow">→</div>\n'
            f'      <div class="related-card-title">{title}</div>\n'
            f'    </a>'
        )
    inner = '\n'.join(card_lines)
    return f'  <div class="related-grid">\n{inner}\n  </div>'


def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match the full related-grid div.
    # End boundary: </div>\s*\n</div> (grid closes, then related-section closes)
    grid_m = re.search(
        r'<div class="related-grid">(.*?)</div>\s*\n</div>',
        content, re.DOTALL
    )
    if not grid_m:
        return False, "no related-grid found"

    grid_inner = grid_m.group(1)

    # Only attempt fix if malformed (arrow div left open on its own line)
    if not re.search(r'<div class="related-card-arrow">→\s*\n', grid_inner):
        return False, "not malformed"

    # Extract all unique cards
    cards = extract_cards_from_grid(grid_inner)
    if not cards:
        return False, "no cards extracted — manual check needed"

    # Build replacement (clean grid + the related-section closing </div>)
    clean_grid = build_clean_grid(cards) + '\n</div>'

    # Replace old match (which includes the related-section </div>)
    old_block = grid_m.group(0)
    new_content = content.replace(old_block, clean_grid, 1)

    if new_content == content:
        return False, "replacement had no effect — check manually"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, f"{len(cards)} cards"


def main():
    html_files = sorted(glob('/Users/dork/Desktop/sidehustleguard/*.html'))
    fixed = []
    skipped_ok = []
    errors = []

    for filepath in html_files:
        name = os.path.basename(filepath)
        try:
            ok, msg = fix_file(filepath)
            if ok:
                fixed.append(f"  ✅ {name} ({msg})")
            else:
                if 'manual' in msg:
                    errors.append(f"  ⚠️  {name}: {msg}")
                else:
                    skipped_ok.append(f"  — {name}: {msg}")
        except Exception as e:
            errors.append(f"  ❌ {name}: {e}")

    print(f"\n{'='*60}")
    print(f"FIXED ({len(fixed)} files):")
    print('\n'.join(fixed) or "  (none)")
    print(f"\nSKIPPED — already clean ({len(skipped_ok)} files):")
    print('\n'.join(skipped_ok) or "  (none)")
    if errors:
        print(f"\nNEEDS MANUAL CHECK ({len(errors)}):")
        print('\n'.join(errors))
    print('='*60)


if __name__ == '__main__':
    main()
