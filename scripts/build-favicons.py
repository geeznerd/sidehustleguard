#!/usr/bin/env python3
"""
Regenerate SideHustleGuard favicons properly.

PROBLEM IT FIXES:
The existing arc-dot.favicon-{32,64,192}.png files have the artwork
stuck in the top-left corner of an otherwise empty/transparent canvas.
At Google SERP scale that renders as effectively blank, so Google falls
back to a default white-circle placeholder.

This script draws the Arc & Dot mark (indigo + apricot) using PIL
primitives, properly CENTERED on a SOLID CREAM background, at every
size Google + iOS + browsers expect.

OUTPUT:
  /favicon.ico                                  (multi-res: 16/32/48)
  /assets/logos/arc-dot.favicon-16.png
  /assets/logos/arc-dot.favicon-32.png
  /assets/logos/arc-dot.favicon-48.png          (Google SERP min)
  /assets/logos/arc-dot.favicon-64.png
  /assets/logos/arc-dot.favicon-96.png
  /assets/logos/arc-dot.favicon-192.png         (apple-touch-icon)
  /assets/logos/arc-dot.favicon-512.png         (PWA / future-proof)

USAGE:
  python3 scripts/build-favicons.py
"""

import os
from PIL import Image, ImageDraw

# Brand palette (Direction E)
INDIGO  = (45, 48, 104, 255)
APRICOT = (232, 148, 100, 255)
CREAM   = (240, 236, 225, 255)  # solid bg — visible on light + dark SERP

# Source viewBox bounding box of the Arc & Dot mark
# (taken from arc-dot.svg: dome control y=4 to dot bottom y=38.4)
SRC_X_MIN, SRC_X_MAX = 6.0, 42.0          # outer arc spans 6..42
SRC_Y_MIN, SRC_Y_MAX = 4.0, 38.4          # dome apex to dot bottom
SRC_W = SRC_X_MAX - SRC_X_MIN              # 36
SRC_H = SRC_Y_MAX - SRC_Y_MIN              # 34.4


def quadratic_bezier(t, p0, p1, p2):
    """Quadratic bezier interpolation."""
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return (x, y)


def draw_smooth_arc(draw, p0, p1, p2, color, width, segments=96):
    """Draw a Q-bezier as many short connected segments + endpoint caps."""
    pts = [quadratic_bezier(i / segments, p0, p1, p2) for i in range(segments + 1)]
    for i in range(segments):
        draw.line([pts[i], pts[i + 1]], fill=color, width=width)
    # Round caps via filled circles at the endpoints
    r = width / 2.0
    for (x, y) in (pts[0], pts[-1]):
        draw.ellipse([x - r, y - r, x + r, y + r], fill=color)


def render(size, bg=CREAM):
    """Render Arc & Dot mark at `size`×`size`, centered on `bg`."""
    img = Image.new('RGBA', (size, size), bg)
    draw = ImageDraw.Draw(img)

    # Inset the artwork by ~12% of canvas on each side — gives visual breathing room
    pad = size * 0.12
    inset = size - 2 * pad

    # Uniform scale that fits the wider dimension; preserves aspect ratio
    scale = inset / max(SRC_W, SRC_H)
    # Pixel dimensions of the artwork at this scale
    art_w = SRC_W * scale
    art_h = SRC_H * scale
    # Top-left offset to center the artwork in the canvas
    off_x = (size - art_w) / 2 - SRC_X_MIN * scale
    off_y = (size - art_h) / 2 - SRC_Y_MIN * scale

    def s(p):
        """Map a source-viewBox point to canvas pixel coordinates."""
        return (off_x + p[0] * scale, off_y + p[1] * scale)

    # Stroke width: ~6.5% of canvas — bold enough to read clearly at small sizes
    stroke = max(2, round(size * 0.065))

    # Outer arc — indigo dome (the "shield")
    draw_smooth_arc(draw, s((6, 30)), s((24, 4)), s((42, 30)), INDIGO, stroke)
    # Inner arc — apricot inner curve (the "guard")
    draw_smooth_arc(draw, s((14, 32)), s((24, 18)), s((34, 32)), APRICOT, stroke)
    # Dot — indigo
    dot_cx, dot_cy = s((24, 36))
    dot_r = max(2, size * 0.06)
    draw.ellipse(
        [dot_cx - dot_r, dot_cy - dot_r, dot_cx + dot_r, dot_cy + dot_r],
        fill=INDIGO,
    )

    return img


def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    logos_dir = os.path.join(repo_root, 'assets', 'logos')
    os.makedirs(logos_dir, exist_ok=True)

    sizes = [16, 32, 48, 64, 96, 192, 512]
    rendered = {}
    for sz in sizes:
        img = render(sz)
        out = os.path.join(logos_dir, f'arc-dot.favicon-{sz}.png')
        img.save(out, optimize=True)
        rendered[sz] = img
        print(f'  ✓ wrote {out}')

    # Multi-resolution favicon.ico at the root (Google requests /favicon.ico)
    # PIL's ICO save bundles the sizes into one .ico file.
    ico_path = os.path.join(repo_root, 'favicon.ico')
    rendered[48].save(
        ico_path,
        format='ICO',
        sizes=[(16, 16), (32, 32), (48, 48)],
    )
    print(f'  ✓ wrote {ico_path} (multi-res 16/32/48)')


if __name__ == '__main__':
    main()
