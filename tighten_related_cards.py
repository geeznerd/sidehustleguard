#!/usr/bin/env python3
"""
Replace the 500px related-grid media query on all pages with a tighter version
that reduces card padding, grid gap, and section spacing on mobile.
"""

from glob import glob
import re

OLD = '@media(max-width:500px){.related-grid{grid-template-columns:1fr!important}}'

NEW = (
    '@media(max-width:500px){'
    '.related-grid{grid-template-columns:1fr!important;gap:7px}'
    '.related-section{padding-top:20px;padding-bottom:28px;margin-top:16px}'
    '.related-card{padding:10px 12px}'
    '.related-card-arrow{margin-bottom:2px}'
    '}'
)

files = sorted(glob('/Users/dork/Desktop/sidehustleguard/*.html'))
fixed = []
skipped = []

for filepath in files:
    name = filepath.split('/')[-1]
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    if OLD not in content:
        skipped.append(name)
        continue

    new_content = content.replace(OLD, NEW, 1)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    fixed.append(name)

print(f'Fixed {len(fixed)} files, skipped {len(skipped)}')
for n in fixed:
    print(f'  ✅ {n}')
