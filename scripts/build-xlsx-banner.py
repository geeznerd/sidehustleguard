#!/usr/bin/env python3
"""
Build the branded hero banner PNG that gets embedded at the top of
the Dashboard sheet in the Quarterly Tax System .xlsx.

Direction E palette: indigo / apricot / cream / paper.
Falls back to system Georgia Italic for the wordmark since Fraunces
isn't guaranteed on buyers' machines (and we're rasterizing here,
not relying on Excel's font lookup).

Output: products/assets/qts-dashboard-banner.png (1600x320 @ 2x DPI)
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT  = ROOT / "products" / "assets" / "qts-dashboard-banner.png"
LOGO = ROOT / "assets" / "logos" / "arc-dot.favicon-192.png"

# Direction E
INDIGO    = (45, 48, 104)
APRICOT   = (232, 148, 100)
APRICOT_SOFT = (240, 220, 200)
CREAM     = (240, 236, 225)
PAPER     = (251, 248, 238)
INDIGO_55 = (95, 99, 133)

# 2x dpi for crisp embed in Excel
W, H = 1600, 320
DPR = 2  # we draw at 2x then let Excel scale, sharper on retina + zoom

def rounded_rect(d, box, radius, fill=None, outline=None, width=1):
    """Pillow doesn't have a rounded rectangle on older versions — fall back."""
    if hasattr(d, "rounded_rectangle"):
        d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)
    else:
        d.rectangle(box, fill=fill, outline=outline, width=width)


def font(path_candidates, size):
    """Try several font paths; return first that loads."""
    for p in path_candidates:
        try:
            return ImageFont.truetype(p, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)

    img = Image.new("RGB", (W, H), CREAM)
    d   = ImageDraw.Draw(img)

    # Apricot radial-ish glow on the left side (fake gradient by stacking
    # large translucent ellipses)
    glow = Image.new("RGBA", (W, H), (255, 255, 255, 0))
    gd = ImageDraw.Draw(glow)
    for i, alpha in enumerate([12, 18, 26, 34, 40]):
        r = 520 - i * 80
        gd.ellipse((140 - r, H//2 - r, 140 + r, H//2 + r),
                   fill=(*APRICOT, alpha))
    img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
    d   = ImageDraw.Draw(img)

    # Topographic contour lines on the right side
    for i in range(7):
        rx = 360 - i * 36
        ry = 180 - i * 18
        d.ellipse(
            (W - 360 - rx, H//2 - ry, W - 360 + rx, H//2 + ry),
            outline=(*INDIGO, 14 + i * 2),
            width=1
        )

    # Logo (arc-dot) — draw directly from the SVG primitives at proper
    # scale. The favicon PNG has whitespace padding that ruins crispness
    # when blown up to 96px. Recreating in Pillow from the SVG paths
    # gives a pixel-perfect mark.
    #
    # Source SVG viewBox = 48x48. Target = 112x112 on the banner.
    LOGO_SZ = 112
    LOGO_X, LOGO_Y = 72, (H - LOGO_SZ) // 2
    scale = LOGO_SZ / 48.0

    def pt(x, y):
        return (LOGO_X + int(x * scale), LOGO_Y + int(y * scale))

    def quad_bezier(p0, p1, p2, steps=40):
        """Approximate a quadratic Bezier as a polyline."""
        pts = []
        for i in range(steps + 1):
            t = i / steps
            x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
            y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
            pts.append((x, y))
        return pts

    # Outer arc: M6 30 Q24 4 42 30 — indigo
    stroke_w = max(2, int(2.6 * scale))
    pts = quad_bezier(pt(6, 30), pt(24, 4), pt(42, 30))
    d.line(pts, fill=INDIGO, width=stroke_w, joint="curve")

    # Inner arc: M14 32 Q24 18 34 32 — apricot
    pts = quad_bezier(pt(14, 32), pt(24, 18), pt(34, 32))
    d.line(pts, fill=APRICOT, width=stroke_w, joint="curve")

    # Dot: circle at (24, 36) r 2.4 — indigo
    cx, cy = pt(24, 36)
    r = int(2.6 * scale)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=INDIGO)

    logo_y = LOGO_Y
    logo_size = LOGO_SZ

    # Wordmark: "SideHustleguard" — sans + italic-serif mix
    sans_bold = font([
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ], 36)
    serif_italic = font([
        "/System/Library/Fonts/Supplemental/Georgia Italic.ttf",
    ], 38)

    wm_x = 72 + logo_size + 18
    wm_y = logo_y + 24
    d.text((wm_x, wm_y), "SideHustle", font=sans_bold, fill=INDIGO)
    sans_w = d.textlength("SideHustle", font=sans_bold)
    d.text((wm_x + sans_w + 2, wm_y - 2), "guard", font=serif_italic, fill=APRICOT)

    # Eyebrow under the wordmark
    eyebrow = font([
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ], 18)
    d.text((wm_x, wm_y + 50),
           "QUARTERLY  TAX  SYSTEM  ·  2026",
           font=eyebrow, fill=APRICOT)

    # Right-side editorial title — "What you'll owe in 2026"
    title_size = 64
    serif_bold_italic = font([
        "/System/Library/Fonts/Supplemental/Georgia Bold Italic.ttf",
    ], title_size)
    serif_bold = font([
        "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    ], title_size)

    # Two-piece title: "Know " (regular bold) + "exactly" (italic apricot)
    # + " what to send the IRS." (regular bold)
    # Keep it short so it fits in the banner width.
    title_a   = "Know "
    title_em  = "exactly"
    title_b   = " what to send."

    # Right-aligned anchor: title's right edge at W - 80
    right_edge = W - 80
    a_w  = d.textlength(title_a,  font=serif_bold)
    em_w = d.textlength(title_em, font=serif_bold_italic)
    b_w  = d.textlength(title_b,  font=serif_bold)
    total_w = a_w + em_w + b_w
    x0 = right_edge - total_w
    y0 = H // 2 - title_size // 2 - 6

    d.text((x0,            y0), title_a,  font=serif_bold,        fill=INDIGO)
    d.text((x0 + a_w,      y0), title_em, font=serif_bold_italic, fill=APRICOT)
    d.text((x0 + a_w+em_w, y0), title_b,  font=serif_bold,        fill=INDIGO)

    # Subline under the title (right-aligned)
    sub = font([
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ], 22)
    sub_text = "A penalty-safe quarterly tax plan, in one workbook."
    sub_w = d.textlength(sub_text, font=sub)
    d.text((right_edge - sub_w, y0 + title_size + 6),
           sub_text, font=sub, fill=INDIGO_55)

    img.save(OUT, "PNG", optimize=True)
    print(f"[built] {OUT.relative_to(ROOT)}  ({W}x{H}, {OUT.stat().st_size//1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
