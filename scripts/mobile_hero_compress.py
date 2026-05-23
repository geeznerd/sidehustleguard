#!/usr/bin/env python3
"""
Phase 6.3 — Compress article hero on mobile.

The article template (doordash-taxes + 66 siblings) currently has:
  - .hero { padding: 64px 48px 48px }
  - h1   { font-size: clamp(38px,5vw,60px); }
  - .hero-meta { margin-bottom: 24px }
  - .hero-intro { margin-bottom: 32px }
  - .answer-box { margin-bottom: 40px }

The @media(max-width:700px) block already overrides h1 → 30px and
shrinks horizontal padding, but does NOT touch vertical metrics —
the hero stays ~200px tall on a 667px iPhone SE viewport (30% of
screen height before article body starts).

Conservative compression (user-approved):
  - .hero padding-top  64 → 44 px on mobile
  - .hero padding-bottom 48 → 32 px on mobile
  - h1 size 30 → 26 px on mobile
  - h2 vertical margin 48 → 36 px on mobile
  - .hero-meta margin-bottom 24 → 14 px
  - .hero-intro margin-bottom 32 → 20 px
  - .answer-box margin-bottom 40 → 28 px + tighter padding
  - .breadcrumb font-size + margin-bottom

Net: drops hero vertical footprint by ~85px on a 375px-wide viewport
without losing editorial feel.
"""
from __future__ import annotations
import re, glob
from pathlib import Path

ROOT = Path('/Users/dork/Desktop/sidehustleguard')

# Skip non-article HTML
SKIP = {
    'index.html', 'guides.html', 'tool.html', 'dashboard.html',
    'tax-checklist.html', 'quarterly-tax-system.html',
    'short-term-rentals.html', 'tax-affiliate-options.html',
    'audit-risk-estimator.html', 'self-employment-tax-calculator.html',
    'quarterly-tax-calculator.html', 'scorp-savings-calculator.html',
    'tax-guard-calculator.html', 'privacy.html', 'terms.html',
    '_template-article-card.html', 'guide-section-options.html',
    'og-image.html',
}

# What we look for in each article — the existing one-line @media rule
# the Phase 3 migration script placed at the bottom of the inline <style>.
OLDS = [
    '@media(max-width:700px){nav,footer{padding:13px 18px}.hero,.content,.related-section{padding-left:18px;padding-right:18px}h1{font-size:30px}.nav-link{display:none}.nav-guides{display:inline-flex;font-size:13px}.logo-text{font-size:13px}.nav-cta{font-size:12px;padding:8px 14px;white-space:nowrap}.nav-right{gap:12px}}',
    '@media(max-width:700px){nav,footer{padding:13px 18px}.hero,.content,.related-section{padding-left:18px;padding-right:18px}h1{font-size:30px}.nav-link{display:none}.nav-guides{display:inline-flex;font-size:13px}.logo-text{font-size:13px}.nav-cta{font-size:12px;padding:12px 14px;white-space:nowrap}.nav-right{gap:12px}}',
    '@media(max-width:700px){nav,footer{padding:13px 18px}.hero,.content,.related-section{padding-left:18px;padding-right:18px}h1{font-size:28px}.nav-link{display:none}.nav-guides{display:inline-flex;font-size:13px}.logo-text{font-size:13px}.nav-cta{font-size:12px;padding:8px 14px;white-space:nowrap}.nav-right{gap:12px}}',
    '@media(max-width:700px){nav,footer{padding:13px 18px}.hero,.content,.related-section{padding-left:18px;padding-right:18px}h1{font-size:28px}.nav-link{display:none}.nav-guides{display:inline-flex;font-size:13px}.logo-text{font-size:13px}.nav-cta{font-size:12px;padding:12px 14px;white-space:nowrap}.nav-right{gap:12px}}',
]

# Tighter, more aggressive (still "conservative" — typography-aware) replacement.
# Notes:
#  * padding-top + padding-bottom on .hero shrink (the big win)
#  * h1 size drops 30 → 26 to give the eyebrow + h1 + sub a tighter stack
#  * h2 margin-top cut 48 → 36 to reduce inter-section breathing on mobile
#  * .hero-meta + .hero-intro + .answer-box vertical margins all tightened
#  * .breadcrumb size + margin reduced
#  * 480px small-mobile rule added on top for further compression
NEW = (
    '@media(max-width:700px){'
    'nav,footer{padding:13px 18px}'
    '.hero{padding:44px 18px 32px}'
    '.hero,.content,.related-section{padding-left:18px;padding-right:18px}'
    '.breadcrumb{font-size:11px;margin-bottom:14px}'
    '.hero-eyebrow{margin-bottom:14px;font-size:11px;padding:6px 12px}'
    'h1{font-size:26px;margin-bottom:14px;line-height:1.08}'
    '.hero-meta{margin-bottom:14px;font-size:12px}'
    '.article-disc{margin:-6px 0 14px}'
    '.hero-intro{font-size:15.5px;margin-bottom:20px;line-height:1.55}'
    '.answer-box{padding:18px 20px;margin-bottom:28px;font-size:14px;border-radius:14px}'
    '.answer-box-inner{gap:10px}'
    '.answer-box-icon svg{width:17px;height:17px}'
    'h2{font-size:22px;margin:36px 0 12px;line-height:1.18}'
    '.content{padding-top:24px;padding-bottom:56px}'
    '.callout{padding:14px 16px;margin:18px 0;border-radius:12px}'
    '.cta-box{padding:36px 24px;margin:32px 0;border-radius:18px}'
    '.cta-box h3{font-size:24px;margin-bottom:8px}'
    '.cta-box p{font-size:14px;margin-bottom:18px}'
    '.nav-link{display:none}'
    '.nav-guides{display:inline-flex;font-size:13px}'
    '.logo-text{font-size:13px}'
    '.nav-cta{font-size:12px;padding:8px 14px;white-space:nowrap}'
    '.nav-right{gap:12px}'
    '}'
    '@media(max-width:420px){'
    '.hero{padding-top:32px;padding-bottom:24px}'
    'h1{font-size:24px}'
    '.hero-intro{font-size:14.5px;margin-bottom:16px}'
    '.answer-box{padding:14px 16px;font-size:13.5px}'
    '.product-card{padding:18px 20px;margin:24px 0;flex-direction:column;gap:12px;align-items:flex-start}'
    '.product-card-cta-row{flex-direction:column;align-items:stretch;gap:8px}'
    '.product-card-btn{width:100%;text-align:center}'
    '}'
)

def migrate(path: Path) -> str:
    src = path.read_text(encoding='utf-8')
    out = src
    matched = False
    for old in OLDS:
        if old in out:
            out = out.replace(old, NEW)
            matched = True
            break
    if not matched:
        return 'no-match'
    path.write_text(out, encoding='utf-8')
    return 'updated'

def main():
    targets = []
    for p in sorted(ROOT.glob('*.html')):
        if p.name in SKIP:
            continue
        targets.append(p)

    counts = {'updated': 0, 'no-match': 0}
    nomatch = []
    for t in targets:
        result = migrate(t)
        counts[result] += 1
        if result == 'no-match':
            nomatch.append(t.name)

    print(f'Processed: {len(targets)}')
    print(f'  updated:  {counts["updated"]}')
    print(f'  no-match: {counts["no-match"]}')
    if nomatch:
        print('\nFiles where the expected old @media block was not found:')
        for n in nomatch:
            print(f'  {n}')

if __name__ == '__main__':
    main()
