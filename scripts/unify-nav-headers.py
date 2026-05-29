#!/usr/bin/env python3
"""
Unify all page headers to use the shared .ds-nav classes from
/assets/css/design-system.css (matching the homepage style).

Replaces the inline <nav>...</nav> block and strips redundant inline
CSS rules. Mobile-nav rules in @media queries are also dropped — they
live in design-system.css now.

USAGE: python3 scripts/unify-nav-headers.py [--dry-run]

NEW canonical nav (matches index.html exactly):
  <nav class="ds-nav">
    [logo lockup]
    <div class="ds-nav-right">
      [How it works / Pricing / FAQ / Guides / CTA]
    </div>
  </nav>
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DRY_RUN = '--dry-run' in sys.argv

# Pages we DON'T touch (already use ds-nav or are templates)
SKIP = {
    'index.html',
    'guides.html',           # has ds-nav already
    'tool.html',             # has ds-nav already
    'dashboard.html',        # has its own complex nav
    'og-image.html',         # not a real page (1200x630 OG image renderer)
    '_template-article.html',
    '_template-article-card.html',
    'tax-affiliate-options.html',
    'guide-section-options.html',
}

# ─── CANONICAL NAV MARKUP (matches index.html exactly) ───
NEW_NAV = '''<nav class="ds-nav">
  <a class="logo" href="/">
    <svg class="logo-mark" viewBox="0 0 48 48" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M6 30 Q24 4 42 30" stroke="#2d3068" stroke-width="2.4" stroke-linecap="round" fill="none"/>
      <path d="M14 32 Q24 18 34 32" stroke="#e89464" stroke-width="2.4" stroke-linecap="round" fill="none"/>
      <circle cx="24" cy="36" r="2.4" fill="#2d3068"/>
    </svg>
    <span class="logo-text">
      <span class="logo-base">SideHustle</span><span class="logo-accent">guard</span>
    </span>
  </a>
  <div class="ds-nav-right">
    <a class="ds-nav-link" href="/#how-it-works">How it works</a>
    <a class="ds-nav-link" href="/#pricing">Pricing</a>
    <a class="ds-nav-link" href="/#faq">FAQ</a>
    <a class="ds-nav-link always-visible" href="/guides">Guides <span class="ds-nav-link-tag">75+ free</span></a>
    <a class="btn btn-cta" href="/tool">Check my hustle →</a>
  </div>
</nav>'''

# Regexes to strip the now-redundant inline CSS (after the nav swap).
# Each pattern targets a specific rule. Whitespace-tolerant.
CSS_RULES_TO_STRIP = [
    # Top-level nav element rule
    r'^nav\s*\{[^}]*\}\s*\n?',
    # Logo + logo-* rules (now in design-system.css)
    r'^\.logo\s*\{[^}]*\}\s*\n?',
    r'^\.logo-icon\s*\{[^}]*\}\s*\n?',
    r'^\.logo-icon\s+svg\s*\{[^}]*\}\s*\n?',
    r'^\.logo-text\s*\{[^}]*\}\s*\n?',
    r'^\.logo-text\s+span\s*\{[^}]*\}\s*\n?',
    # Old nav-* class rules
    r'^\.nav-right\s*\{[^}]*\}\s*\n?',
    r'^\.nav-link\s*\{[^}]*\}\s*\n?',
    r'^\.nav-link[:.][^{]*\{[^}]*\}\s*\n?',  # .nav-link:hover, .nav-link.foo
    r'^\.nav-cta\s*\{[^}]*\}\s*\n?',
    r'^\.nav-cta[:.][^{]*\{[^}]*\}\s*\n?',   # .nav-cta:hover, etc.
    # Mobile-nav rules inside @media — only the nav-* references
    # (we keep the @media block, just strip nav rules from it)
    r'\.nav-link\s*\{\s*display:\s*none\s*\}\s*',
    r'\.nav-cta\s*\{[^}]*\}\s*',
    r'\.logo-text\s*\{[^}]*font-size[^}]*\}\s*',
    r'\.nav-right\s*\{[^}]*gap[^}]*\}\s*',
    r'\.nav-link\.nav-guides\s*\{[^}]*\}\s*',
    # @media-no-preference orphan transforms
    r'@media\s*\(\s*prefers-reduced-motion:\s*no-preference\s*\)\s*\{\s*\.nav-cta:hover\s*\{[^}]*\}\s*\}\s*\n?',
]


def replace_nav_block(html: str) -> tuple[str, bool]:
    """Replace the first <nav>...</nav> block with the canonical .ds-nav markup."""
    # Match the nav block (greedy, handles whitespace + multi-line)
    pattern = re.compile(r'<nav[^>]*>[\s\S]*?</nav>', re.MULTILINE)
    if not pattern.search(html):
        return html, False
    new_html = pattern.sub(NEW_NAV, html, count=1)
    return new_html, True


def strip_inline_nav_css(html: str) -> str:
    """Remove redundant inline nav-related CSS rules."""
    for pattern in CSS_RULES_TO_STRIP:
        html = re.sub(pattern, '', html, flags=re.MULTILINE)
    # Collapse runs of blank lines we may have created
    html = re.sub(r'\n{3,}', '\n\n', html)
    return html


def process_file(path: Path) -> dict:
    """Process one HTML file. Returns stats dict."""
    original = path.read_text(encoding='utf-8')
    html, nav_replaced = replace_nav_block(original)
    if not nav_replaced:
        return {'skipped_reason': 'no <nav> block found'}
    html = strip_inline_nav_css(html)
    if html == original:
        return {'skipped_reason': 'no change after processing'}
    if not DRY_RUN:
        path.write_text(html, encoding='utf-8')
    return {
        'bytes_before': len(original),
        'bytes_after':  len(html),
        'delta':        len(html) - len(original),
    }


def main():
    html_files = sorted([
        p for p in ROOT.glob('*.html')
        if p.name not in SKIP
    ])

    print(f'Processing {len(html_files)} HTML files... '
          f'({"DRY-RUN — no writes" if DRY_RUN else "WRITING CHANGES"})\n')

    updated = 0
    skipped = 0
    for p in html_files:
        result = process_file(p)
        if 'skipped_reason' in result:
            skipped += 1
            print(f'  · {p.name:<55} skipped — {result["skipped_reason"]}')
        else:
            updated += 1
            delta = result['delta']
            sign = '-' if delta < 0 else '+'
            print(f'  ✓ {p.name:<55} {sign}{abs(delta):>5} bytes')

    print(f'\nResults: {updated} updated, {skipped} skipped (of {len(html_files)} total)')
    if DRY_RUN:
        print('Dry-run mode — no files were actually changed. Re-run without --dry-run to apply.')


if __name__ == '__main__':
    main()
