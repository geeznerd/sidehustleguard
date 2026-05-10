# Short-Term Rental Content — Launch Checklist

Updated: 2026-05-10
Latest commit: 9656097

All 27 scaffold files are noindex, placeholder-free, and carry the correct
4-level breadcrumb: SideHustleGuard → Guides → Short-Term Rentals → [Title].

Remove `<meta name="robots" content="noindex, nofollow">` from each file as
body copy is completed, then re-run `node generate-sitemap.js`.

---

## Platform Guides (8 files)
*Add cards to guides.html `id="short-term-rentals"` section when live*

- [x] **airbnb-host-taxes.html** — LIVE (body copy complete, indexed)
- [ ] **vrbo-host-taxes.html** — TODO body copy · 8 min read
- [ ] **booking-com-host-taxes.html** — TODO body copy · 8 min read
- [ ] **turo-host-taxes.html** — TODO body copy · 8 min read
- [ ] **hipcamp-host-taxes.html** — TODO body copy · 8 min read
- [ ] **rv-rental-host-taxes.html** — TODO body copy · 8 min read
- [ ] **furnished-finder-taxes.html** — TODO body copy · 8 min read
- [ ] **neighbor-storage-host-taxes.html** — TODO body copy · 8 min read

---

## STR Tax Strategy Guides (11 files)
*Add cards to guides.html `id="short-term-rentals"` section when live*

- [ ] **airbnb-14-day-rule.html** — scaffold complete (FAQs written) · 8 min read
- [ ] **schedule-c-vs-schedule-e-str.html** — TODO body copy · 8 min read
- [ ] **short-term-rental-loophole.html** — TODO body copy · 8 min read
- [ ] **cost-segregation-str.html** — TODO body copy · 8 min read
- [ ] **lodging-tax-by-state.html** — TODO body copy · 8 min read
- [ ] **airbnb-self-employment-tax.html** — TODO body copy · 8 min read
- [ ] **airbnb-deductions-checklist.html** — TODO body copy · 8 min read
- [ ] **mixed-use-rental-taxes.html** — TODO body copy · 8 min read
- [ ] **house-hacking-taxes.html** — TODO body copy · 8 min read
- [ ] **str-business-structure.html** — TODO body copy · 8 min read
- [ ] **airbnb-1099-k.html** — TODO body copy · 8 min read
- [ ] **quarterly-taxes-for-airbnb-hosts.html** — TODO body copy · 8 min read

---

## STR State Rule Guides (8 files)
*Add cards to guides.html `id="short-term-rentals"` section when live*

- [ ] **california-short-term-rental-rules.html** — scaffold drafted (Prompt 4) · 10 min read
- [ ] **new-york-short-term-rental-rules.html** — TODO body copy · 10 min read
- [ ] **florida-short-term-rental-taxes.html** — TODO body copy · 10 min read
- [ ] **hawaii-short-term-rental-rules.html** — TODO body copy · 10 min read
- [ ] **texas-short-term-rental-taxes.html** — TODO body copy · 10 min read
- [ ] **colorado-short-term-rental-taxes.html** — TODO body copy · 10 min read
- [ ] **tennessee-short-term-rental-taxes.html** — TODO body copy · 10 min read
- [ ] **arizona-short-term-rental-taxes.html** — TODO body copy · 10 min read

---

## Per-file launch steps (repeat for each file above)

1. **Write body copy** — fill in all `<!-- TODO ... -->` sections
2. **Proof FAQ** — FAQs are pre-written; verify for accuracy
3. **Verify related cards** — confirm all linked slugs exist and are indexed
4. **OG image** — create `/images/og/{slug}.png` + `.webp` at 1200×630
5. **Remove noindex** — delete `<meta name="robots" content="noindex, nofollow">`
6. **Add article card to guides.html** — in `id="short-term-rentals"` section; increment count
7. **Regenerate sitemap** — `node generate-sitemap.js`

---

## guides.html Short-Term Rentals section
`id="short-term-rentals"` section is live with 1 card (Airbnb Host Taxes).
Add article cards here as each scaffold goes live. Increment `<span class="cat-count">` with each addition.

---

## Internal links from airbnb-host-taxes.html

| Target | Anchor location | Status |
|---|---|---|
| /airbnb-14-day-rule | After 14-day rule section | ✅ Live |
| /schedule-c-vs-schedule-e-str | After Schedule C/E section | ✅ Live |
| /short-term-rental-loophole | After depreciation section | ✅ Live |
| /cost-segregation-str | No natural spot yet — defer | — |

---

## OG images needed (27 total)

Platform guides:
- `/images/og/vrbo-host-taxes.png` + `.webp`
- `/images/og/booking-com-host-taxes.png` + `.webp`
- `/images/og/turo-host-taxes.png` + `.webp`
- `/images/og/hipcamp-host-taxes.png` + `.webp`
- `/images/og/rv-rental-host-taxes.png` + `.webp`
- `/images/og/furnished-finder-taxes.png` + `.webp`
- `/images/og/neighbor-storage-host-taxes.png` + `.webp`

Strategy guides:
- `/images/og/airbnb-14-day-rule.png` + `.webp`
- `/images/og/schedule-c-vs-schedule-e-str.png` + `.webp`
- `/images/og/short-term-rental-loophole.png` + `.webp`
- `/images/og/cost-segregation-str.png` + `.webp`
- `/images/og/lodging-tax-by-state.png` + `.webp`
- `/images/og/airbnb-self-employment-tax.png` + `.webp`
- `/images/og/airbnb-deductions-checklist.png` + `.webp`
- `/images/og/mixed-use-rental-taxes.png` + `.webp`
- `/images/og/house-hacking-taxes.png` + `.webp`
- `/images/og/str-business-structure.png` + `.webp`
- `/images/og/airbnb-1099-k.png` + `.webp`
- `/images/og/quarterly-taxes-for-airbnb-hosts.png` + `.webp`

State guides:
- `/images/og/california-short-term-rental-rules.png` + `.webp`
- `/images/og/new-york-short-term-rental-rules.png` + `.webp`
- `/images/og/florida-short-term-rental-taxes.png` + `.webp`
- `/images/og/hawaii-short-term-rental-rules.png` + `.webp`
- `/images/og/texas-short-term-rental-taxes.png` + `.webp`
- `/images/og/colorado-short-term-rental-taxes.png` + `.webp`
- `/images/og/tennessee-short-term-rental-taxes.png` + `.webp`
- `/images/og/arizona-short-term-rental-taxes.png` + `.webp`

---

## STR hub page (deferred)

- [ ] **short-term-rentals.html** — build when first batch of scaffold pages go live
  - H1: Short-Term Rental Taxes: The Complete Playbook
  - 3 card groups: Platform Guides, Tax Strategy, State Rules
  - Add to sitemap after launch

---

## Scaffold audit (2026-05-10)

| File | Exists | noindex | No placeholders | Breadcrumb |
|---|---|---|---|---|
| airbnb-14-day-rule | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| vrbo-host-taxes | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| booking-com-host-taxes | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| turo-host-taxes | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| hipcamp-host-taxes | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| rv-rental-host-taxes | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| furnished-finder-taxes | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| neighbor-storage-host-taxes | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| schedule-c-vs-schedule-e-str | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| short-term-rental-loophole | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| cost-segregation-str | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| lodging-tax-by-state | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| airbnb-self-employment-tax | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| airbnb-deductions-checklist | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| mixed-use-rental-taxes | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| house-hacking-taxes | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| str-business-structure | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| airbnb-1099-k | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| quarterly-taxes-for-airbnb-hosts | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| california-short-term-rental-rules | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| new-york-short-term-rental-rules | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| florida-short-term-rental-taxes | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| hawaii-short-term-rental-rules | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| texas-short-term-rental-taxes | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| colorado-short-term-rental-taxes | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| tennessee-short-term-rental-taxes | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |
| arizona-short-term-rental-taxes | ✅ | ✅ | ✅ | ✅ Short-Term Rentals |

---

## Infrastructure done

- [x] guides.html: `id="short-term-rentals"` section created (1 card: Airbnb)
- [x] guides.html: Gig Work & Delivery count corrected to 8
- [x] guides.html: section `id` attrs on all sections including new STR section
- [x] robots.txt: `Disallow: /_template-article*`
- [x] vercel.json: `^/_[^/].*` → 404 (blocks all `/_*` routes)
- [x] sitemap.xml: script-generated, noindex files excluded (51 live URLs)
- [x] generate-sitemap.js: re-run after each noindex removal
- [x] 39 existing live articles: 4-level JSON-LD breadcrumbs
- [x] airbnb-host-taxes.html: internal links to /airbnb-14-day-rule, /schedule-c-vs-schedule-e-str, /short-term-rental-loophole
- [x] airbnb-host-taxes.html: breadcrumb updated to Short-Term Rentals section
- [x] All 27 scaffolds: placeholder-free, noindex, correct breadcrumbs, read times set
