#!/usr/bin/env python3
"""
Fix the hero topo SVG so it stretches consistently full-width across all
article pages.

The article template (and 65+ sibling guides) currently has:

    .hero { padding:64px 48px 48px; max-width:820px; margin:0 auto;
            position:relative; overflow:hidden }
    .hero-content { position:relative; z-index:1 }

This constrains the .hero (and its topo SVG child) to 820px max-width.
Result: the topo swirls render at 820px on articles but full-viewport
on index.html / guides.html / tool.html, creating page-to-page
inconsistency.

Fix (mirroring index.html's working pattern):

    .hero { padding:64px 48px 48px; position:relative; overflow:hidden }
    .hero-content { position:relative; z-index:1;
                    max-width:820px; margin:0 auto }

The hero now spans the full viewport (so the topo SVG fills horizontally),
and the readable content stays constrained to 820px via .hero-content.

Also bumps .content padding-top so the picture below the hero has clear
breathing room from the hero's bottom — fixes the user-reported visual
bleed between the article-hero topo and the OG image's own baked-in topo.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path('/Users/dork/Desktop/sidehustleguard')

SKIP = {
    # Pages that already use the correct full-width hero pattern OR
    # don't have an article-style hero at all
    'index.html', 'guides.html', 'tool.html', 'dashboard.html',
    'tax-checklist.html', 'quarterly-tax-system.html',
    'short-term-rentals.html', 'tax-affiliate-options.html',
    'audit-risk-estimator.html', 'self-employment-tax-calculator.html',
    'quarterly-tax-calculator.html', 'scorp-savings-calculator.html',
    'tax-guard-calculator.html', 'privacy.html', 'terms.html',
    '_template-article-card.html', 'guide-section-options.html',
    'og-image.html',
}

# The two .hero patterns observed across the 67 article files.
# The first variant: padding:64px 48px 48px
# (used by doordash-taxes.html template and most clones)
OLDS_HERO = [
    '.hero{padding:64px 48px 48px;max-width:820px;margin:0 auto;position:relative;overflow:hidden}',
]
NEW_HERO = '.hero{padding:64px 48px 48px;position:relative;overflow:hidden}'

# .hero-content gets max-width:820px + margin:0 auto added so the
# CONTENT stays readable while the .hero/topo stretches full-width.
OLD_HERO_CONTENT = '.hero-content{position:relative;z-index:1}'
NEW_HERO_CONTENT = '.hero-content{position:relative;z-index:1;max-width:820px;margin:0 auto}'

# .content needs more padding-top so the OG image below the hero has
# clear visual separation. Default has no padding-top.
OLD_CONTENT = '.content{max-width:800px;margin:0 auto;padding:0 48px 80px}'
NEW_CONTENT = '.content{max-width:800px;margin:0 auto;padding:32px 48px 80px}'


def migrate(path: Path) -> dict:
    src = path.read_text(encoding='utf-8')
    out = src
    diag = {'file': path.name, 'hero': False, 'hero_content': False, 'content': False}

    for old in OLDS_HERO:
        if old in out:
            out = out.replace(old, NEW_HERO)
            diag['hero'] = True
            break
    if OLD_HERO_CONTENT in out:
        out = out.replace(OLD_HERO_CONTENT, NEW_HERO_CONTENT)
        diag['hero_content'] = True
    if OLD_CONTENT in out:
        out = out.replace(OLD_CONTENT, NEW_CONTENT)
        diag['content'] = True

    if out != src:
        path.write_text(out, encoding='utf-8')
    return diag


def main():
    targets = []
    for p in sorted(ROOT.glob('*.html')):
        if p.name in SKIP:
            continue
        targets.append(p)

    results = [migrate(t) for t in targets]
    print(f'Processed: {len(results)}')
    hero_updated = sum(1 for r in results if r['hero'])
    content_updated = sum(1 for r in results if r['hero_content'])
    body_updated = sum(1 for r in results if r['content'])
    print(f'  .hero pattern fixed:         {hero_updated}')
    print(f'  .hero-content updated:       {content_updated}')
    print(f'  .content padding-top added:  {body_updated}')

    missed = [r for r in results if not r['hero']]
    if missed:
        print('\nFiles where .hero pattern wasn\'t matched (skipped):')
        for r in missed[:20]:
            print(f'  {r["file"]}')


if __name__ == '__main__':
    main()
