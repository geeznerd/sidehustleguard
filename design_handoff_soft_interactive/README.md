# Handoff: SideHustleGuard — "Soft Interactive" redesign

## Overview

This is a full-site redesign direction for **SideHustleGuard** (sidehustleguard.com), moving the brand away from its current navy / gold / Playfair editorial look toward a softer, more interactive aesthetic anchored by **deep indigo + warm apricot on a cream paper background**, with **Fraunces** serif as the voice and **Inter** as the workhorse.

The direction is internally codenamed **"Direction E — Soft Interactive."** It came out of an exploration of five candidate aesthetics; this is the one the stakeholder picked. It targets a feel that is **quietly thorough** — confident and a little editorial, but warm, calm, and motion-aware. Not minimal. Not loud. Built for a personal-finance audience who needs to trust the brand.

## About the design files

The HTML files in this bundle are **design references** — a clickable prototype showing the intended look and behavior of one representative section ("What we check"), plus full documentation of the design system that should be applied across the entire site.

**You are not shipping this HTML.** You're using it as a fidelity reference to recreate the design in the target codebase. The current site lives at `sidehustleguard/` as a set of static HTML files with inline `<style>` blocks — your job is to restyle every page (`index.html`, `tool.html`, `guides.html`, the individual `*-taxes.html` guides, etc.) using this design system.

If you decide a CSS framework or build step would meaningfully improve the project, propose it. Otherwise, keep the static-HTML deployment model and update the existing files in place.

## Fidelity

**High-fidelity.** All colors, type scales, spacing, motion timings, and interactions in this document are final and should be implemented as specified. Where the prototype only shows one section, **apply the same tokens and patterns consistently** to every other section of the site.

---

## Design tokens

### Colors

| Token | Hex | Usage |
|---|---|---|
| `--indigo` | `#2d3068` | Primary text, headlines, dark surfaces, primary CTA fill |
| `--indigo-70` | `rgba(45,48,104,0.7)` | Secondary body text on cream |
| `--indigo-55` | `rgba(45,48,104,0.55)` | Tertiary text, metadata |
| `--indigo-35` | `rgba(45,48,104,0.35)` | Inactive numerals, hairlines |
| `--indigo-08` | `rgba(45,48,104,0.08)` | Soft borders on light surfaces |
| `--apricot` | `#e89464` | Accent — italic words, active states, indicators, prices, links |
| `--apricot-soft` | `rgba(232,148,100,0.18)` | Soft glow backgrounds |
| `--cream` | `#f0ece1` | Page background |
| `--paper` | `#fbf8ee` | Card surfaces on cream |
| `--paper-70` | `rgba(251,248,238,0.7)` | Body copy on indigo |
| `--paper-55` | `rgba(251,248,238,0.55)` | Tertiary text on indigo |
| `--paper-12` | `rgba(251,248,238,0.12)` | Hairlines on indigo |

**Status colors** (use sparingly, for the compliance score / report mock only):

| Token | Hex |
|---|---|
| `--good` | `#5a7a4f` (muted moss green — *not* the gold-green from the old palette) |
| `--warn` | `#c98a3a` (muted amber) |
| `--risk` | `#c2533a` (clay red, NOT pure red) |

### Typography

Load both via Google Fonts. **Do not use Playfair Display or DM Sans anywhere** — they are being retired.

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..700,0..100;1,9..144,300..700,0..100&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

**Fraunces** (variable serif) — used for ALL display headlines, all italic accents, numerals in metrics, decorative numerals (01, 02…) in lists. Set `font-variation-settings: 'opsz' 144, 'SOFT' 30` on display sizes to get the soft, slightly rounded character that defines the look. Italic Fraunces is the signature voice — every page should have at least one italic Fraunces word.

**Inter** — used for all UI text, body copy, eyebrow labels, button labels, navigation, form fields, kickers, metadata. Default weight 400, 500 for emphasis, 600 for buttons/labels.

#### Type scale

| Role | Family | Size | Weight | Line-height | Letter-spacing | Notes |
|---|---|---|---|---|---|---|
| Display XL (hero h1) | Fraunces | clamp(56px, 7vw, 96px) | 400 | 0.98 | -0.025em | `'opsz' 144, 'SOFT' 30`; italicize the accent word |
| Display L (section h2) | Fraunces | clamp(40px, 5vw, 64px) | 400 | 1.0 | -0.022em | Same variation settings |
| Display M | Fraunces | 32px | 400 | 1.1 | -0.015em | Card titles inside dark surfaces |
| Title | Inter | 15.5px | 600 | 1.3 | -0.005em | Row titles, list-item titles |
| Body | Inter | 15.5px | 400 | 1.65 | 0 | Long-form copy |
| Body small | Inter | 13.5px | 400 | 1.65 | 0 | Card body |
| Caption | Inter | 12.5px | 400 | 1.5 | 0 | Row sub-text |
| Eyebrow / kicker | Inter | 12px | 600 | 1 | 0.14em UPPER | Section labels; color apricot |
| Mono / meta | Inter | 11px | 600 | 1 | 0.16em UPPER | "Check 03 of 06"-style markers; color apricot or paper-55 |
| Metric numeral | Fraunces italic | 18–38px (context) | 500 | 1 | -0.01em | Always italic, often apricot |

### Spacing

8px base unit. Common multiples actually used:

- **Tight:** 8, 14, 18, 22 — within cards, between adjacent text
- **Section interior:** 28, 32, 44, 48 — between blocks inside a card; between subheading and body
- **Section padding:** 56–64px vertical on desktop, 44px on mobile
- **Page gutter:** 60–72px desktop, 20–24px mobile
- **Grid gap:** 14px (tight grid) or 48px (column gap on split layouts)

### Radii

- **Small** 8px — pills, inline tags, mono metadata chips
- **Medium** 14px — list items, segmented controls
- **Card** 18px — content cards on cream
- **Container** 22px — major dark surfaces (the indigo preview card, the list container)
- **Pill / button** 100px — all buttons, all badges

### Shadows

The design is **largely shadowless** — depth comes from the indigo-on-cream contrast and the apricot indicator, not from elevation. Use shadows only on the few elements that should "lift":

- **Hero CTA / sticky elements:** `0 6px 24px rgba(45,48,104,0.12)`
- **Focused / hovered cards:** `0 12px 32px rgba(45,48,104,0.08)` (subtle)
- **Modals / dialogs:** `0 30px 80px rgba(45,48,104,0.18)`

### Motion

This is the most important non-color part of the system. The site should feel **alive but unhurried**.

- **Default easing:** `cubic-bezier(0.4, 0, 0.2, 1)` (Material standard easing — confident, not bouncy)
- **Default duration:** `.25s` for hover/state changes; `.35s` for layout-affecting transitions (sliding indicators, expanding panels)
- **Long durations:** `.45s` for hero/section entry animations
- **No springs, no bounces, no overshoot.** This brand is calm.
- **Sliding indicator pattern:** when a user hovers/clicks one of a vertical list of items, an apricot-bordered cream pill slides between positions over 350ms — see "Component patterns → Sliding list" below.
- **Color transitions:** numerals and titles fade from indigo-35 to apricot over 250ms when active.
- **No scroll-jacking, no parallax.** Subtle blob backgrounds (radial-gradient) are static.

### Accent shapes (the "blob")

There's a single recurring decorative motif: a soft radial-gradient circle in apricot, ~380–460px, positioned offscreen at a corner so only the edge bleeds onto the page. Used **once per major section, not more**. Example:

```css
.blob {
  position: absolute;
  bottom: -120px;
  left: -100px;
  width: 380px;
  height: 380px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(232,148,100,0.18), transparent 65%);
  pointer-events: none;
}
```

---

## Component patterns

These are the building blocks. Apply them throughout the site.

### 1. Eyebrow + headline pair

Every section opens with this pair.

```html
<div class="eyebrow">What we check ✦</div>
<h2 class="display-l">
  Quietly thorough.<br>
  <em>Built for sleep.</em>
</h2>
```

- Eyebrow: Inter 600, 12px, uppercase, 0.14em tracking, apricot.
- The `✦` glyph (or `—`, `→`) appears after the eyebrow text. Use sparingly; not on every eyebrow.
- Headline: Fraunces 400, italic on the accent word, color shifts to apricot on the italic word.

### 2. Sliding list (the signature interaction)

A vertical stack of items where hovering or clicking any item slides an apricot-bordered cream "indicator" pill to that row, and the row's numeral + metric fade to apricot.

**Behavior:**
- Container is `paper` (`#fbf8ee`) with 22px radius, 10px inner padding, 1px `indigo-08` border.
- Each row is exactly 68px tall, three columns: 44px numeral / flex-1 title block / auto metric.
- The indicator is `position: absolute`, full-width inside the padding, 68px tall, 14px radius, `cream` fill, 1px apricot border. Animate `top` over 350ms with default easing.
- Initial active row index is 0.

**Where to use it on the site:**
- The current "What we check" section — the canonical use.
- The pricing FAQ comparison (Free vs Full Report — turn each feature row into a list item).
- The guide index — each tax topic becomes a row.
- The current `<select>`-style state picker in the tool — replace it with a sliding list if vertical space allows.

### 3. Paired hero card

The signature layout: **two-column split**, ~0.9fr / 1.1fr.

- **Left column:** eyebrow → display-l headline → 1–2-line body → a dark indigo card (`#2d3068`, 22px radius, 26–28px padding) showing the currently-active item in expanded form. Always present, always visible.
- **Right column:** the sliding list (above).

This pattern should be reused for the hero (replace the existing 9-tile hustle picker with a sliding list of hustle types, and the indigo card shows what we'd check for that hustle), for pricing (the indigo card is the "Full report" tier, the sliding list is the feature comparison), and for "How it works."

### 4. Cards on cream

For ordinary content cards (FAQ items, guide cards, testimonial cards if added later):

- Background: `paper`
- Border: 1px `indigo-08`
- Radius: 18px
- Padding: 24px–26px
- Title: Fraunces 400, 22–26px, indigo
- Body: Inter 400, 13.5–14px, indigo-70
- Hover: translateY(-3px), border becomes apricot, 250ms

### 5. Buttons

**Primary** — for the main CTAs ("Free Check," "Get full report"):
```css
background: var(--indigo);
color: var(--paper);
padding: 14px 30px;
border-radius: 100px;
font: 600 15px/1 'Inter';
letter-spacing: 0;
transition: background .2s, transform .15s;
&:hover { background: #393d80; transform: translateY(-1px); }
```

**Accent** — for "unlock" and one-off important actions:
```css
background: var(--apricot);
color: var(--indigo);
/* same shape as primary */
&:hover { background: #f0a075; }
```

**Outline / secondary:**
```css
background: transparent;
color: var(--indigo);
border: 1.5px solid rgba(45,48,104,0.18);
padding: 14px 30px;
border-radius: 100px;
&:hover { border-color: var(--indigo); }
```

**Retire** the existing gold pill button entirely. The new accent button is apricot on indigo (note: the indigo is the text color on accent buttons, not the fill — this is the inverse of the old gold-on-white pattern, and is the correct reading).

### 6. Pricing card (paired)

Two cards side-by-side, 1fr / 1.06fr.

- **Free card:** paper background, 1.5px `indigo-08` border, 20px radius. Price numeral is Fraunces 60px indigo.
- **Full report card:** indigo background, no border, same radius. Price numeral is Fraunces 60px italic apricot. A small apricot pill badge sits above it: "Most complete — $5".

### 7. Compliance score visualization

For `tool.html` and the report mock on the homepage:

- Score number: Fraunces italic, 96–120px, color shifts based on band (good = moss, warn = amber, risk = clay).
- Score label below: Inter 600, 11px, uppercase, 0.16em tracking, indigo-55.
- Surrounding ring (if used): SVG circle, 4px stroke, color matches band, animate `stroke-dashoffset` from full to target value over 1.2s on mount.

### 8. Ticker (existing element)

The current scrolling ticker bar can remain conceptually, but **restyle it**:
- Background: `indigo`
- Text: `paper-55`, with every other item in `apricot` instead of gold-light
- Same scroll animation, same 22s loop

### 9. FAQ accordion

- Question row: Inter 500, 15.5px, indigo. 16px vertical padding, 1px `indigo-08` bottom border.
- Toggle: 24px circle, 1.5px `indigo-08` border, apricot "+" inside. When open, rotates 45deg and border becomes apricot.
- Answer: Inter 400, 14px, indigo-70, 1.65 line-height. Animate max-height 300ms.

### 10. Nav

- **Logo lockup:** use the new **"Arc & Dot"** mark (see `assets/logo-mark.svg` and the dedicated logo section below). The wordmark sits to the right: "SideHustle" in Inter 600 indigo, "guard" in Fraunces italic apricot. Gap between mark and wordmark = 10px.
- Links: Inter 400, 13px, `indigo-55`, hover to indigo.
- Primary CTA: pill button per spec above.
- Background: `rgba(240,236,225,0.96)` (cream with alpha) + `backdrop-filter: blur(16px)`.

---

## The logo — "Arc & Dot"

The retired navy/gold shield logo is replaced with a new mark called **Arc & Dot**. It's an abstract sheltering motif: two arcs (one indigo, one apricot, nested) protecting a small indigo dot. It reads as quiet protection without the literalism of a shield, and it carries the indigo-+-apricot pairing that defines Direction E.

### Construction

- **Viewbox:** 48 × 48
- **Outer arc (indigo `#2d3068`):** quadratic curve `M6 30 Q24 4 42 30`, stroke 2.4, round caps, no fill
- **Inner arc (apricot `#e89464`):** quadratic curve `M14 32 Q24 18 34 32`, stroke 2.4, round caps, no fill
- **Dot (indigo `#2d3068`):** circle at (24, 36) with radius 2.4, filled

The two arcs share a vertical axis and the dot sits centered below them, on the open side. The visual reading is: "something under cover."

### Variants

- **On cream / paper (default):** indigo arc + apricot arc + indigo dot. File: `assets/logo-mark.svg`.
- **On indigo (reversed):** paper-colored outer arc + apricot inner arc + paper-colored dot. File: `assets/logo-mark-on-indigo.svg`.
- **Lockup:** `assets/logo-lockup.svg` shows the mark + wordmark together. For production, render the **wordmark as live HTML text**, not SVG — accessibility and font-loading need the real Inter and Fraunces glyphs.

### Wordmark rules

```html
<a class="logo" href="/">
  <!-- inline SVG mark, or <img src="logo-mark.svg" /> -->
  <span class="logo-text">
    <span class="logo-base">SideHustle</span><span class="logo-accent">guard</span>
  </span>
</a>
```

```css
.logo { display: inline-flex; align-items: center; gap: 10px; text-decoration: none; }
.logo-text { display: inline-flex; align-items: baseline; line-height: 1; letter-spacing: -0.015em; }
.logo-base { font-family: 'Inter', sans-serif; font-weight: 600; font-size: 22px; color: var(--indigo); }
.logo-accent {
  font-family: 'Fraunces', serif;
  font-style: italic;
  font-weight: 500;
  font-size: 22px;
  color: var(--apricot);
  margin-left: 2px;
  font-variation-settings: 'opsz' 144, 'SOFT' 30;
}
```

Note: the brand was previously "SideHustle**Guard**" with a capital G in gold. The new lockup uses lowercase "guard" in italic apricot — this is intentional. It softens the read, makes "guard" feel verbal ("we guard you") rather than nominal, and lets the italic do the heavy lifting that the bolder color used to do.

### Spacing & sizing

- **Minimum size:** 24px tall for the mark; the wordmark must drop below 12px text-size only on favicons.
- **Clear space:** minimum padding around the lockup equal to the height of the mark's dot (2.4px at default size, scale proportionally).
- **Nav usage:** 28–32px mark height.
- **Hero / footer usage:** 36–48px mark height.
- **Favicon:** export the mark alone at 32×32 and 64×64 from `logo-mark.svg`.

### Don't

- Don't recolor the inner arc to anything other than apricot.
- Don't fill the area between the arcs — they're open shapes by design.
- Don't outline the dot or change its position relative to the arcs.
- Don't pair the mark with the wordmark in any case other than the specified "SideHustle" + italic "guard."
- Don't rotate the mark — the open side always faces down.

---

## Hero splash backdrop

The hero on `index.html` uses a **"topographic contours"** backdrop motif — two clusters of nested ovals like a paper map, with an apricot radial glow behind the larger cluster. It's quiet, papery, and gives the headline a lot of room to breathe.

### Implementation

Place this SVG as the first child of `<section class="hero">`, absolutely positioned to fill the section, `pointer-events: none`:

```html
<svg class="hero-backdrop" viewBox="0 0 1200 700" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs>
    <radialGradient id="heroGlow" cx="20%" cy="80%" r="55%">
      <stop offset="0%" stop-color="#e89464" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="#e89464" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1200" height="700" fill="url(#heroGlow)"/>

  <!-- Primary contour cluster (lower-left, indigo) — 9 nested ovals -->
  <g fill="none" stroke="#2d3068" stroke-opacity="0.07" stroke-width="1">
    <ellipse cx="300" cy="520" rx="460" ry="220" transform="rotate(-12 300 520)"/>
    <ellipse cx="294" cy="506" rx="425" ry="202" transform="rotate(-10.5 300 520)"/>
    <ellipse cx="288" cy="492" rx="390" ry="184" transform="rotate(-9 300 520)"/>
    <ellipse cx="282" cy="478" rx="355" ry="166" transform="rotate(-7.5 300 520)"/>
    <ellipse cx="276" cy="464" rx="320" ry="148" transform="rotate(-6 300 520)"/>
    <ellipse cx="270" cy="450" rx="285" ry="130" transform="rotate(-4.5 300 520)"/>
    <ellipse cx="264" cy="436" rx="250" ry="112" transform="rotate(-3 300 520)"/>
    <ellipse cx="258" cy="422" rx="215" ry="94" transform="rotate(-1.5 300 520)"/>
    <ellipse cx="252" cy="408" rx="180" ry="76" transform="rotate(0 300 520)"/>
  </g>

  <!-- Secondary contour cluster (upper-right, apricot) — 6 nested ovals -->
  <g fill="none" stroke="#e89464" stroke-opacity="0.18" stroke-width="1">
    <ellipse cx="1050" cy="180" rx="300" ry="140" transform="rotate(18 1050 180)"/>
    <ellipse cx="1054" cy="172" rx="270" ry="126" transform="rotate(16 1050 180)"/>
    <ellipse cx="1058" cy="164" rx="240" ry="112" transform="rotate(14 1050 180)"/>
    <ellipse cx="1062" cy="156" rx="210" ry="98" transform="rotate(12 1050 180)"/>
    <ellipse cx="1066" cy="148" rx="180" ry="84" transform="rotate(10 1050 180)"/>
    <ellipse cx="1070" cy="140" rx="150" ry="70" transform="rotate(8 1050 180)"/>
  </g>
</svg>
```

```css
.hero { position: relative; overflow: hidden; }
.hero-backdrop { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; }
.hero-content { position: relative; z-index: 1; }
```

### Behavior

- **Static** by default — no animation. The backdrop is texture, not motion.
- **Optional subtle motion:** if you want to add any, animate the apricot cluster's rotation by ±2° over 20s linear infinite. Anything more is too much.
- **Reduced motion:** kill all animation. The default is already reduced-motion-safe because it's static.
- **Below md viewport (768px):** scale the backdrop down so each cluster still bleeds offscreen on its anchored edge. Optionally drop the inner 3 ovals from each cluster to reduce visual noise.

### Why this works

Topographic contours read as "a map of something" — which matches the brand's promise: *we map out your tax and legal landscape*. The asymmetric placement (large indigo cluster anchoring the lower-left, small apricot cluster floating upper-right) gives the page a calm, off-balance composition that feels editorial rather than corporate. It pairs naturally with the **Arc & Dot** mark because both share the same vocabulary of nested curves.

### Headline layout pairing

The topographic backdrop is designed for a **centered** hero composition (single column, ~760px max-width) so the contours frame the content from the sides rather than fighting it. Use this structure:

1. Eyebrow pill, centered
2. Display-XL headline (Fraunces, ~96px on desktop), centered, with an italic apricot accent word on the second line
3. One-paragraph subhead, centered, max-width 540px
4. Two CTAs side-by-side: primary indigo pill ("Start free check →") + ghost link ("See sample report")
5. A row of three italic Fraunces stats below ("50 states · 60s median · 0 data stored"), separated by ample whitespace

The sliding-list hustle picker that appears in other layouts moves down to its own dedicated section just below the hero in this composition — it gets enough room to breathe as the page's first interactive moment.

---



## Section-by-section application notes

The current homepage (`sidehustleguard/index.html`, 803 lines) has these sections in order. For each, here's how the restyle should land.

### Fixed header (nav + ticker)
Apply patterns #10 and #8 above. Same structure, recolored.

### Hero
**Restructure** as the paired hero (pattern #3):
- Left: kicker "Free legal check ✦" → headline "Is your hustle <em>legally</em> protected?" (italicize "legally" in apricot Fraunces) → 1-sentence body → indigo card showing a sample check result for whatever hustle is hovered/active in the picker.
- Right: replace the current 9-tile emoji-laden grid with the sliding list. Each row is one hustle type (Digital products, Physical products, Freelance/services, Content creation, Reselling/flipping, Renting/hosting, Coaching/teaching, Rideshare, Delivery). No emoji — use the Fraunces italic numeral as the visual anchor instead.
- Clicking a row navigates to `/tool?type=<encoded>` exactly as the current picker does — preserve all query-string contracts.

### Intro context paragraph
Keep the copy. Apply body type tokens. Center the paragraph in a 760px max-width. Replace the bold navy spans with apricot italicized Fraunces inline runs for the three emphasized phrases.

### How it works (4 steps)
Convert the existing 4-cell horizontal grid into a 4-card layout using pattern #4. Each card has:
- Step number in Fraunces italic 44px apricot at the top-left
- Title in Fraunces 22px indigo
- Description in Inter 14px indigo-70
- Hover lifts the card per pattern.

### What we check (6 items)
**This is the section the prototype shows.** Implement it exactly as Direction E. Either the paired layout (preview card + sliding list) or, if vertical space is tight on the page, a 2×3 grid of pattern-#4 cards using the same content and numerals.

### Pricing
Apply pattern #6. The CPA comparison callout below ("$0 / $5 vs CPA $250+") keeps its structure but recolors:
- Strikethrough "$250+" in clay red
- The "$5" big numeral in Fraunces italic apricot
- Background of the callout becomes indigo with `paper` text

### Report preview (inline)
The existing report mock card is good — restyle to:
- Card background paper, 18px radius, soft shadow
- Header bar indigo with apricot logo accent
- Score row uses pattern #7 colors
- The "Unlock full report — $5" overlay text is Inter 600 12px apricot, on a cream→transparent gradient

### FAQ
Two-column layout, left column has the section eyebrow + h2 + 1-paragraph intro. Right column is the accordion (pattern #9).

### CTA band
Indigo full-width band (22px radius, 60–68px padding). Headline in Fraunces with italic apricot accent. Single apricot accent button. Add a single blob in the top-right corner per the "Accent shapes" rule.

### Guides index (`guides.html`)
The guides index gets its own dedicated treatment — see the dedicated **"Guides page patterns"** section below for the full spec. The signature moves are: topo backdrop + live-search hero, sticky category tabs, featured "mega-cards" for the Dashboard and STR overview, monogram tiles replacing emoji, sub-filter chips on the STR section, and "Show N more" expanders on long sections. Desktop is a 3-column grid; mobile drops to single column with horizontally-scrollable category tabs.

### Footer (bottom-bar)
Keep the trust-logos row. Update colors: divider line `indigo-08`, label text `indigo-35`. The wordmark uses the indigo/apricot split.

---

## Guides page patterns

The `/guides` index is one of the highest-traffic pages on the site and needed its own pattern vocabulary. See `Guides Redesign.html` for the full clickable prototype (desktop + mobile side-by-side) and `reference/guides-redesign.jsx` for the React source.

### Page architecture

```
[Nav]                      ← sticky, blurred cream
[Hero]                     ← topo backdrop + headline + search
[Category tabs]            ← sticky below nav, pill-style, horizontal-scroll on mobile
[Section: Interactive Tools]    ← features a "mega card" + 6 tool cards
[Section: Gig & Delivery]       ← 8 cards
[Section: Short-Term Rentals]   ← sub-filter chips + mega card + 12 cards + "Show 16 more"
[Section: Creator Economy]
[Section: E-commerce]
[Section: Freelancing]
[Section: State guides]
[CTA band]                 ← indigo, "Tell us your hustle"
[Footer]
```

### Pattern G1 — Live-search hero

The hero is centered (or left-aligned on mobile), with:
1. Eyebrow pill — "Free tax guides · 67 in total"
2. Display headline (Fraunces 72px desktop / 44px mobile), italic apricot accent word
3. Subhead body
4. **Pill-shaped search input** (Inter 14.5px, paper bg, 1px `indigo-12` border, 100px radius, magnifying-glass icon 18px from left, "×" clear button when populated)

Search filters across all sections in real time. When a query is active:
- Hide all featured mega-cards (they don't represent the search intent)
- Hide all "Show N more" expanders (search expands implicitly)
- Hide sub-filter chips
- Sections with zero matches collapse entirely (don't render the header)

### Pattern G2 — Sticky category tabs

Below the hero, a pill-tab strip sticks to the top of the viewport as the user scrolls. One tab per section + an "All" tab.

```css
.cat-tabs {
  position: sticky;
  top: 64px;  /* nav height */
  background: rgba(240,236,225,0.92);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--indigo-08);
  z-index: 10;
}
.cat-tab {
  font: 500 13px 'Inter';
  padding: 8px 16px;
  border-radius: 100px;
  border: none;
  background: transparent;
  color: var(--indigo-70);
  white-space: nowrap;
  transition: background .2s, color .2s;
}
.cat-tab[aria-current="true"] {
  background: var(--indigo);
  color: var(--paper);
}
```

- **Desktop:** wraps onto one line.
- **Mobile:** `overflow-x: auto`, horizontally scrollable. Tap to filter. Sticky-top offset becomes 56px to match mobile nav height. Hide the scrollbar (`scrollbar-width: none`).

Clicking a tab either filters in place (preferred) or scroll-jumps to the section anchor — pick one, don't do both. The prototype filters.

### Pattern G3 — Guide card

The atomic unit of the page. Replaces the emoji-prefixed text links on the existing site.

```html
<a class="guide-card" href="/uber-lyft-taxes">
  <div class="guide-card-head">
    <div class="guide-monogram">U</div>
    <div class="guide-title-row">
      <span class="guide-title">Uber & Lyft Taxes</span>
      <span class="guide-tag tag-new">New</span>  <!-- optional -->
    </div>
  </div>
  <p class="guide-desc">What every rideshare driver actually owes</p>
  <span class="guide-arrow">→</span>
</a>
```

Specs:
- Card: `paper` background, 16px radius, 1px `indigo-08` border, padding 18px 20px 16px.
- Monogram: 28×28px, 10px radius, `rgba(232,148,100,0.12)` background. Letter is Fraunces italic 16px apricot. Use the first letter of the platform/topic name; for numbered guides (e.g. "14-Day Rule", "2025 Tax Rates") use the leading digit.
- Title: Inter 600, 15px, indigo.
- Tag pill (optional): "New" (apricot bg + apricot text) or "Soon" (`indigo-08` bg + `indigo-55` text). Inter 600, 10px, uppercase, 0.08em tracking, 3px×8px padding, 100px radius.
- Description: Inter 400, 13px, `indigo-70`, 1.5 line-height.
- Arrow: positioned absolute bottom-right, 14px, color `indigo-35`. On card hover: color → apricot, translateX(+3px).
- Hover: border → apricot, translateY(-2px), 250ms.

### Pattern G4 — Featured mega-card

For Dashboard (Tools section) and Complete STR Guide (STR section). Spans all 3 columns on desktop, full-width on mobile.

```html
<a class="mega-card" href="/dashboard">
  <div class="mega-blob"></div>  <!-- the apricot radial glow -->
  <div class="mega-eyebrow">★ Featured</div>
  <h3 class="mega-title">
    Side Hustle <em>Dashboard</em>
  </h3>
  <p class="mega-blurb">…</p>
  <div class="mega-pills">
    <span>Audit Shield</span>
    <span>Tax Guard</span>
    <span>S-Corp Sim</span>
  </div>
  <span class="mega-cta">Open <span class="arrow">→</span></span>
</a>
```

Specs:
- Card: `indigo` background, 18px radius, padding 26px 30px 28px desktop / 22px mobile, color `paper`.
- Apricot radial blob in the top-right corner, 240×240px, absolutely positioned.
- Eyebrow: "★ Featured" (Inter 600, 11px, uppercase, 0.14em, apricot). The ★ is decorative; keep it.
- Title: Fraunces 36px desktop / 28px mobile, italic apricot on the accent word.
- Blurb: Inter 14.5px, `paper-70`.
- Pills (3 max): Inter 500, 12px, `rgba(251,248,238,0.1)` bg, `paper-85` text, 100px radius, 5px×11px padding.
- CTA: Inter 600, 13px, apricot, arrow translateX(+4px) on hover.
- Hover: translateY(-2px), 250ms.

### Pattern G5 — Sub-filter chips

Used only for sections that need a second level of cut (currently just STR with its 28 guides → Platforms / Topics / State rules).

Place row of chip buttons between the section header and the card grid. Active chip has apricot border + `rgba(232,148,100,0.1)` bg + apricot text; inactive is `paper` bg + `indigo-08` border + `indigo-70` text. 6px×13px padding, 100px radius, Inter 500 12px.

When a sub-filter is active, hide cards that don't match (you'll need to tag each guide with a category: platform/topic/state). Hide the sub-filter row when the global search has a non-empty query.

### Pattern G6 — "Show N more" expander

For sections > 12 cards (STR's 28, E-commerce's 12 if you decide to truncate). After the visible cards, render a single ghost button:

```html
<button class="show-more">Show 16 more →</button>
```

Styled like a guide-card tag pill but larger: `paper` bg, `indigo-08` border, Inter 500 13px apricot, 8px×16px padding, 100px radius. Clicking reveals the rest of the cards in place (don't navigate).

### Section header

```html
<div class="section-header">
  <h2 class="section-headline">Short-term rentals</h2>
  <span class="section-count">28 guides</span>
</div>
```

- Headline: Fraunces 400, 36px desktop / 26px mobile, color indigo. No italic by default in this context — the section-level italic happens in the hero only, to avoid italic fatigue across 7 sections.
- Count: Inter 600, 12px, uppercase, 0.1em tracking, `indigo-55`.
- Layout: space-between on desktop (baseline-aligned); stacked column on mobile.

### CTA band (end of page)

Indigo card, 22px radius, 52px×56px padding desktop / 32px×24px mobile. Apricot radial blob in top-right. Split layout (text left, button right) on desktop; stacked on mobile. Headline is Fraunces 40px/30px with italic apricot on the second line ("We'll figure out the rest."). Button is **apricot fill + indigo text** (the inverse of the page's primary button) to draw maximum attention.

### Mobile-specific notes

- Nav height drops from 64px to 56px.
- Hero padding: 40px 20px 32px (vs 72px 64px 48px).
- Hero text is **left-aligned**, not centered — left-aligned reads better in a narrow column. Headline 44px.
- Search input is full-width.
- Sticky category tabs offset becomes 56px and tabs scroll horizontally with `gap: 4px` (tighter than desktop's 6px).
- Sections: single column, 10px gap (vs 14px desktop), 48px bottom margin (vs 72px).
- Mega-cards: 22px padding, pills wrap to multiple rows comfortably.
- Section headers: stacked column, count below headline.
- CTA band: stacked, button gets `align-self: flex-start` and 14px×26px padding.
- Footer: stacked column.

### Accessibility

- Search input gets `aria-label="Search guides and tools"`.
- Category tabs use `aria-current="page"` on active.
- Sub-filter chips behave like a `role="tablist"` with `role="tab"` on each chip.
- "Show more" expanders use `aria-expanded`.
- All guide cards have descriptive link text (no "click here").
- Monogram tiles are `aria-hidden="true"` — they're decorative.

---



| Interaction | Trigger | Effect | Timing |
|---|---|---|---|
| Sliding list indicator | Hover row | Apricot pill slides to row's y-position | 350ms cubic-bezier(0.4,0,0.2,1) |
| Sliding list color | Hover row | Numeral + metric fade indigo-35 → apricot | 250ms ease |
| Card lift | Hover card | translateY(-3px), border → apricot | 250ms |
| Button press | Click | scale(0.97), revert on release | 80ms |
| FAQ toggle | Click | max-height animates open; "+" rotates 45° | 300ms |
| Ticker scroll | Always | translateX(0 → -50%) infinite | 22s linear |
| Hero indigo card swap | Active row change in hero picker | Cross-fade content via React `key={activeIndex}` | 200ms |
| Score ring on mount | Page load / report reveal | stroke-dashoffset animates to value | 1200ms ease-out |

**Reduced motion:** Wrap all motion-affecting transitions in `@media (prefers-reduced-motion: no-preference)`. Without that preference, indicator should snap to position instantly; cards should not lift; ticker should pause.

**No autoplay carousels anywhere.** The original direction C tried auto-cycling — it's been rejected as too aggressive for this brand.

---

## State management

The current site is static HTML with sprinkled vanilla JS. Match that. The only stateful pieces:

- **Sliding list active index** — local component state, default 0
- **Hustle picker selection** — drives the indigo preview card content + the CTA `href`
- **FAQ open/closed** — local state per item
- **Mobile nav open** — boolean

If you migrate to a build step / framework, that's a judgment call; document the reasoning if you do.

---

## Assets

All assets in `sidehustleguard/images/` (hustle-specific guide images) and the existing shield SVG in the nav stay as-is. **No new image assets are required for this restyle** — the design system is type-and-color-driven.

The shield SVG in the nav should be **replaced** with the new "Arc & Dot" mark — see the dedicated logo section above for full construction and rules. The mark's source files are in `assets/`.

The `og-image.png` and `report-preview.webp` should be regenerated to match the new palette **and use the new mark**; treat that as a follow-up task.

---

## Files in this handoff

- **`Direction E — standalone preview.html`** — open this in a browser to see the canonical "What we check" implementation. It's the source of truth for the sliding-list interaction.
- **`Logo & Splash.html`** — full canvas showing the four candidate logo marks (the chosen one is **03 · Arc & dot**) and three hero splash treatments (the chosen one is **B · Topographic contours**). Useful for context on what was considered and rejected.
- **`Guides Redesign.html`** — full clickable prototype of the `/guides` page in **both desktop (1440px) and mobile (390px)** views, side-by-side on a design canvas. See "Guides page patterns" section above for the full spec.
- **`assets/logo-mark.svg`** — chosen mark, default colors, for use on cream/paper.
- **`assets/logo-mark-on-indigo.svg`** — reversed variant for dark surfaces.
- **`assets/logo-lockup.svg`** — mark + wordmark mockup. In production, render the wordmark as live HTML text.
- **`reference/directions.jsx`** — React source for all five "What we check" directions. Look only at `DirectionSoftInteractive` (E).
- **`reference/logo-splash.jsx`** — React source for the logo lineup + hero splash explorations. The chosen pair is `LogoArc` + `SplashB`.
- **`reference/guides-redesign.jsx`** — React source for the `/guides` redesign. Renders both desktop and mobile from the same component via a `mobile` prop.
- **`reference/What We Check (canvas with all directions).html`** — full canvas with all five candidate "What we check" directions.
- **`reference/design-canvas.jsx`** — supporting component for the canvas viewer; not part of the design system.

The actual production codebase you'll be editing is the user's local folder `sidehustleguard/` — it is **not** included in this handoff. The task is to apply the system above to those existing static HTML files.

---

## Definition of done

- All five colors and both fonts replace the existing navy/gold/Playfair/DM Sans system across every page.
- Hero, "How it works," "What we check," pricing, and CTA band on `index.html` use the patterns above.
- At least one section per page uses the signature sliding-list interaction (or the paired hero variant).
- The 60-second tool flow at `tool.html` is restyled to match — quiz UI uses pattern #2 if possible, and the final report screen uses pattern #7 for the score.
- All static guide pages (`*-taxes.html`, `guides.html`) inherit the new tokens via a shared CSS file (introduce one if it doesn't exist).
- `og-image.html` is updated to match (regenerate `og-image.png` from it).
- Lighthouse / Core Web Vitals don't regress; in particular, font loading is non-blocking via `font-display: swap`.
- All existing `?type=` query-string contracts on hustle-picker links are preserved.
- Site looks correct down to 360px viewport width.
