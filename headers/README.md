# SideHustleGuard — OG Header Images (Direction E)

40 Open Graph header images for the guide pages, redesigned to match the **Direction E — Soft Interactive** brand system.

- **Palette:** indigo `#2d3068` + apricot `#e89464` on cream `#f0ece1`
- **Type:** Fraunces (italic display) + Inter (UI)
- **Mark:** Arc & Dot logo top-left, italic monogram on the right
- **Backdrop:** topographic contour clusters with an apricot glow
- **Output spec:** 1200 × 630 PNG (Open Graph + Twitter card)

## Files in this folder

```
headers/
├── renderer.html         ← the design source (open in browser to preview)
├── generate.mjs          ← Node + Puppeteer script to render all 40 PNGs
├── package.json
├── README.md             ← this file
├── preview/              ← lower-res preview captures (924×540) from the design canvas
└── output/               ← production PNGs (1200×630) — produced by generate.mjs
```

## To regenerate the production PNGs

```bash
cd headers/
npm install
npm run generate
```

This launches headless Chrome, opens `renderer.html`, calls `window.renderHeader(i)` for each of the 40 entries, and screenshots the `.og` element at exactly 1200×630 (with 2× DPR for retina sharpness). Takes about 15 seconds.

The headers/output/ folder is populated with one PNG per slug — drop them into `sidehustleguard/images/og/` and update the `<meta property="og:image">` references on each page.

## To preview the design in a browser

Open `renderer.html` in any browser. Use the console:

```js
window.renderHeader(0)   // doordash-taxes
window.renderHeader(8)   // etsy-taxes
window.renderHeader(40)  // (out of range — array has 40 entries, indices 0-39)
```

The page auto-scales the 1200×630 design to fit your viewport so you see the full composition.

## To add a new header

Edit the `window.HEADERS` array in `renderer.html`. Each entry is:

```js
["slug-name", "Title Main", "italic accent", "subtitle copy", "Eyebrow Tag", "M"]
//  ^slug      ^h1 left    ^h1 right (italic) ^body              ^pill        ^monogram letter
```

Then re-run `npm run generate`.

## Design notes

- The headline auto-fits across 4 sizes (92px / 78px / 66px / 56px) — if it still overflows, it falls back to a stacked layout (main on line 1, italic accent on line 2).
- The monogram is **always one character** — the first letter of the slug for most, or the leading digit for guides like "1099-K for Etsy" (`1`) or "14-day rule" (`1`).
- The eyebrow tag uses the same vocabulary as the rest of the site: "Tax Guide" / "State Tax Guide" / "Deduction Guide" / "Tax Form Guide" / "Business Structure" / "Self-Employed" / "Free Tool" / "Free Resource".
- The hairline frame inset at 24px gives the cards a finished, printable feel without competing for attention.
- No emoji. Ever.

## What was retired

The previous header system used navy `#1c2b4a`, gold `#c9973a`, Playfair Display + DM Sans, a literal shield logo, and a gold left-edge accent bar. All of that is gone. Don't re-introduce any of it.
