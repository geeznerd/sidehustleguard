# SideHustleGuard

A free, AI-powered legal & tax compliance checker for US side hustlers. Static HTML site deployed on Vercel.

## What this codebase is

- **Static HTML.** Every page is a self-contained `.html` file with inline `<style>` and `<script>` blocks. There is no build step, no bundler, no framework. The deploy pipeline is `vercel --prod`.
- **Pages of note:**
  - `index.html` — marketing homepage
  - `tool.html` — the 60-second compliance checker (a multi-step quiz that calls `/api/check` and renders a report)
  - `guides.html` — index of all tax guides
  - `dashboard.html` — combined Audit Risk + Tax Guard + S-Corp calculator
  - `*-taxes.html` (60+ files) — individual tax guide pages, all sharing a similar template
  - `audit-risk-estimator.html`, `tax-guard-calculator.html`, `scorp-savings-calculator.html`, `quarterly-tax-calculator.html`, `self-employment-tax-calculator.html`, `tax-checklist.html` — interactive tools
  - `privacy.html`, `terms.html` — legal pages
- **Backend:** Vercel serverless functions in `/api/` (`check.js`, `pdf.js`, `subscribe.js`, `reddit-monitor.js`).
- **Fonts:** loaded from Google Fonts. The current site uses Playfair Display + DM Sans (being retired).
- **Assets:** site images in `/images/`, and SVGs inlined into HTML.

## Current redesign

**A full visual redesign called "Direction E — Soft Interactive" is in flight.** The complete design system, component patterns, logo, and reference prototypes live in:

> **`design_handoff_soft_interactive/README.md`**

**Read that file before doing any visual work.** It's the source of truth for colors, type, motion, components, and per-page application notes. Treat it as a brief, not a suggestion. If you want to deviate from it, justify the deviation explicitly and confirm with the user.

The redesign retires the existing navy/gold/Playfair/DM Sans aesthetic and replaces it with:
- **Indigo `#2d3068` + apricot `#e89464` on cream `#f0ece1`**
- **Fraunces (italic display) + Inter (UI/body)**
- A new **"Arc & Dot" logo** — see `design_handoff_soft_interactive/assets/`
- A **topographic-contour SVG backdrop** on the homepage hero
- Reusable patterns: sliding-list interaction, paired hero, guide-card grid with monogram tiles, featured mega-cards, sticky category tabs, "Show N more" expanders

### Reference prototypes (open in browser to see)

- `design_handoff_soft_interactive/Direction E - standalone preview.html` — canonical "What we check" section
- `design_handoff_soft_interactive/Logo & Splash.html` — logo options + hero backdrop options (with rejected variants for context)
- `design_handoff_soft_interactive/Guides Redesign.html` — `/guides` page redesign at desktop + mobile

## Working in this repo — rules

1. **Preserve the static-HTML deploy model.** Do not introduce React, a bundler, or a build step without explicit user approval. If a feature is unwieldy in vanilla JS, propose the framework change first and wait for sign-off.
2. **Introduce a shared CSS file** (`/styles.css` or similar) as part of the redesign — the current per-page inline `<style>` blocks duplicate massive amounts of CSS and make consistent restyling impossible. Centralize the new tokens, type scale, component patterns, and utility classes; have each page link it instead of inlining.
3. **Preserve all query-string contracts.** Existing `?type=...` links from the homepage hustle picker land on `/tool` with prefilled state. The redesign must keep all encoded values identical (`Selling%20digital%20products`, etc.) so external links continue to work.
4. **Preserve all SEO.** `<title>`, meta descriptions, canonical URLs, `application/ld+json` schema blocks, sitemap entries, OG/Twitter cards — all must stay intact during restyling. The site relies on SEO traffic for the 60+ guide pages.
5. **Don't break the existing tools.** The calculators (`tax-guard-calculator.html`, `scorp-savings-calculator.html`, etc.) have working JS — restyle the chrome without touching the math. Test that the same inputs produce the same outputs.
6. **Mobile-first.** The README has explicit mobile specs for every pattern (smaller padding, single-column grids, 56px sticky-nav offset, horizontal-scroll category tabs). Implement them; don't just shrink the desktop layout.
7. **Accessibility.** Maintain proper heading hierarchy (one `<h1>` per page), `aria-label`s on icon-only controls, `aria-current` on active nav/tabs, `aria-expanded` on accordions. The README's "Accessibility" subsection lists per-pattern requirements.
8. **Reduced motion.** Wrap all motion-affecting CSS transitions inside `@media (prefers-reduced-motion: no-preference)`. The default state should be reduced-motion-safe.
9. **Performance.** Don't regress Lighthouse or Core Web Vitals. Specifically: keep `font-display: swap` on Google Fonts, avoid loading more font weights than the README specifies (400/500/600/700 for Inter; 400/500 for Fraunces), and keep the topographic SVG backdrop static (no JS animation).
10. **No emoji on production pages.** The current site is full of emoji in card labels — the redesign replaces them with Fraunces italic monogram tiles. Do not reintroduce emoji into restyled pages.

## Suggested order of work

Tackle in roughly this sequence to keep diffs reviewable:

1. **Shared CSS file** — extract all tokens, base styles, type, button styles, and nav/footer patterns from the README into `/styles.css`. Don't change any page yet.
2. **Logo + nav + footer** — these touch every page. Update once, link the shared CSS, and confirm visually on three pages before continuing.
3. **`index.html`** — hero (with topo backdrop), "How it works," "What we check" (use Pattern E from the prototype), pricing, FAQ, CTA band.
4. **`guides.html`** — implement the prototype at `Guides Redesign.html` precisely. This is the highest-traffic page; it should match.
5. **`tool.html`** — quiz UI restyle, report screen with compliance score visualization.
6. **The guide-page template** — figure out the shared structure of the `*-taxes.html` pages, update one as a reference, then mass-apply to the rest.
7. **`dashboard.html` and calculators** — restyle chrome only; don't touch logic.
8. **`og-image.html`** — regenerate `og-image.png` from it using the existing script (`generate-sample-pdf.mjs` is a similar pattern).
9. **Legal pages** — `privacy.html`, `terms.html` get token-level restyling; structure stays.

Commit per page, not per session. Push frequently. Use `vercel` for preview deploys before promoting to prod.

## What NOT to do

- Don't migrate to React/Next.js/Astro without explicit approval.
- Don't bulk-rewrite all 60+ guide pages before settling the template — you'll redo them three times.
- Don't add new copy or content the user didn't ask for. The README has principles about not padding designs with filler.
- Don't keep the old shield-and-checkmark logo as a fallback. The retire is total — every reference (including favicon, OG image, footer) gets the new mark.
- Don't change the brand wordmark casing from the new lowercase italic "guard." That softening is intentional.
- Don't add `<button>`s where `<a>`s belong, or vice versa. Navigation = anchor; in-page action = button.

## Asking the user

When in doubt, ask. Specifically prompt for confirmation when:
- A pattern in the README seems to conflict with an existing tool's behavior
- A page's existing structure doesn't map cleanly onto a new pattern
- You're about to touch a backend API file
- A change would alter the site's URL structure
- You want to deviate from the README

The user prefers small, reversible changes over large rewrites. Show your work, propose before you ship.
