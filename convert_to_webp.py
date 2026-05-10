#!/usr/bin/env python3
"""
1. Convert all OG images (images/og/*.png) + report-preview.png to WebP
2. Wrap <img> tags on guide pages + homepage in <picture> elements for WebP/PNG fallback
   OG meta tags are intentionally left as PNG (social platform compatibility)
"""

import os
import re
from glob import glob
from PIL import Image

BASE = '/Users/dork/Desktop/sidehustleguard'

# ── 1. Convert images to WebP ─────────────────────────────────────────────────
converted = []

# OG header images
for png_path in sorted(glob(f'{BASE}/images/og/*.png')):
    webp_path = png_path.replace('.png', '.webp')
    img = Image.open(png_path).convert('RGB')
    img.save(webp_path, 'WEBP', quality=88, method=6)
    saved = os.path.getsize(png_path) - os.path.getsize(webp_path)
    converted.append((os.path.basename(png_path), saved))

# report-preview.png (homepage)
rp_png = f'{BASE}/report-preview.png'
rp_webp = f'{BASE}/report-preview.webp'
img = Image.open(rp_png).convert('RGBA')  # preserve transparency if any
img.save(rp_webp, 'WEBP', quality=88, method=6)
converted.append(('report-preview.png', os.path.getsize(rp_png) - os.path.getsize(rp_webp)))

total_saved = sum(s for _, s in converted)
print(f'Converted {len(converted)} images, saved {total_saved/1024:.0f} KB total')


# ── 2. Update HTML files ──────────────────────────────────────────────────────

def wrap_with_picture(html, img_pattern, webp_src):
    """
    Wraps a matched <img> tag with a <picture> element adding a WebP <source>.
    Idempotent — skips if already wrapped.
    """
    def replacer(m):
        img_tag = m.group(0)
        # Skip if already inside a <picture>
        return img_tag  # handled below via context check

    # Use a broader search to check for existing <picture> wrapper
    # Replace all matching <img> tags that aren't already inside <picture>
    result = re.sub(
        img_pattern,
        lambda m: (
            m.group(0)  # already wrapped — leave as-is (checked separately)
        ),
        html
    )
    return result


updated_files = []

# Guide pages: <img src="/images/og/SLUG.png" ...>
for html_path in sorted(glob(f'{BASE}/*.html')):
    if html_path.endswith('index.html'):
        continue

    with open(html_path, encoding='utf-8') as f:
        content = f.read()

    # Match the img tag for OG image (not already in a <picture>)
    img_re = re.compile(
        r'<img\s+src="/images/og/([^"]+\.png)"([^>]*)>',
        re.DOTALL
    )

    def guide_replacer(m):
        slug_png = m.group(1)            # e.g. doordash-taxes.png
        slug_webp = slug_png.replace('.png', '.webp')
        rest = m.group(2)                # remaining attributes
        original_img = m.group(0)
        return (
            f'<picture>'
            f'<source srcset="/images/og/{slug_webp}" type="image/webp">'
            f'{original_img}'
            f'</picture>'
        )

    # Only replace if not already inside <picture>
    # Check by looking at context: if preceded by <source srcset, skip
    def safe_guide_replacer(m):
        start = max(0, m.start() - 80)
        context = content[start:m.start()]
        if '<picture>' in context:
            return m.group(0)
        return guide_replacer(m)

    new_content = img_re.sub(safe_guide_replacer, content)

    if new_content != content:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_files.append(os.path.basename(html_path))

# Homepage: <img src="/report-preview.png" ...>
index_path = f'{BASE}/index.html'
with open(index_path, encoding='utf-8') as f:
    content = f.read()

img_re_home = re.compile(
    r'<img\s+src="/report-preview\.png"([^>]*)>',
    re.DOTALL
)

def home_replacer(m):
    rest = m.group(1)
    original_img = m.group(0)
    return (
        f'<picture>'
        f'<source srcset="/report-preview.webp" type="image/webp">'
        f'{original_img}'
        f'</picture>'
    )

def safe_home_replacer(m):
    start = max(0, m.start() - 80)
    context = content[start:m.start()]
    if '<picture>' in context:
        return m.group(0)
    return home_replacer(m)

new_content = img_re_home.sub(safe_home_replacer, content)
if new_content != content:
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    updated_files.append('index.html')

print(f'\nUpdated {len(updated_files)} HTML files with <picture> WebP wrappers:')
for name in updated_files:
    print(f'  ✅ {name}')
