# Short-Term Rental Content — Launch Checklist

Updated: 2026-05-10
Latest commit: (pending)

All 27 scaffold files are live and indexed. Hub page live at /short-term-rentals.
guides.html STR section shows 28 cards. Sitemap at 79 URLs.

---

## Platform Guides (8 files)

- [x] **airbnb-host-taxes.html** — LIVE (body copy complete, indexed)
- [x] **vrbo-host-taxes.html** — LIVE (indexed 2026-05-10)
- [x] **booking-com-host-taxes.html** — LIVE (indexed 2026-05-10)
- [x] **turo-host-taxes.html** — LIVE (indexed 2026-05-10)
- [x] **hipcamp-host-taxes.html** — LIVE (indexed 2026-05-10)
- [x] **rv-rental-host-taxes.html** — LIVE (indexed 2026-05-10)
- [x] **furnished-finder-taxes.html** — LIVE (indexed 2026-05-10)
- [x] **neighbor-storage-host-taxes.html** — LIVE (indexed 2026-05-10)

---

## STR Tax Strategy Guides (12 files)

- [x] **airbnb-14-day-rule.html** — LIVE (indexed 2026-05-10)
- [x] **schedule-c-vs-schedule-e-str.html** — LIVE (indexed 2026-05-10)
- [x] **short-term-rental-loophole.html** — LIVE (indexed 2026-05-10)
- [x] **cost-segregation-str.html** — LIVE (indexed 2026-05-10)
- [x] **lodging-tax-by-state.html** — LIVE (body copy complete + 50-state table, indexed 2026-05-10)
- [x] **airbnb-self-employment-tax.html** — LIVE (indexed 2026-05-10)
- [x] **airbnb-deductions-checklist.html** — LIVE (indexed 2026-05-10)
- [x] **mixed-use-rental-taxes.html** — LIVE (indexed 2026-05-10)
- [x] **house-hacking-taxes.html** — LIVE (indexed 2026-05-10)
- [x] **str-business-structure.html** — LIVE (indexed 2026-05-10)
- [x] **airbnb-1099-k.html** — LIVE (indexed 2026-05-10)
- [x] **quarterly-taxes-for-airbnb-hosts.html** — LIVE (indexed 2026-05-10)

---

## STR State Rule Guides (8 files)

- [x] **california-short-term-rental-rules.html** — LIVE (indexed 2026-05-10)
- [x] **new-york-short-term-rental-rules.html** — LIVE (indexed 2026-05-10)
- [x] **florida-short-term-rental-taxes.html** — LIVE (indexed 2026-05-10)
- [x] **hawaii-short-term-rental-rules.html** — LIVE (indexed 2026-05-10)
- [x] **texas-short-term-rental-taxes.html** — LIVE (indexed 2026-05-10)
- [x] **colorado-short-term-rental-taxes.html** — LIVE (indexed 2026-05-10)
- [x] **tennessee-short-term-rental-taxes.html** — LIVE (indexed 2026-05-10)
- [x] **arizona-short-term-rental-taxes.html** — LIVE (indexed 2026-05-10)

---

## STR Hub Page

- [x] **short-term-rentals.html** — LIVE (indexed, 52nd URL, committed 46f182f)
  - H1: Short-Term Rental Taxes: The Complete Playbook
  - Decision tree, 28-card grid, FAQ, CTA

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

`id="short-term-rentals"` section live with 28 cards + hub card link.
Filter chips active (all / platforms / topics / state rules).
Count badge: `28 guides`.

---

## Internal links from airbnb-host-taxes.html

| Target | Anchor location | Status |
|---|---|---|
| /airbnb-14-day-rule | After 14-day rule section | ✅ Live |
| /schedule-c-vs-schedule-e-str | After Schedule C/E section | ✅ Live |
| /short-term-rental-loophole | After depreciation section | ✅ Live |
| /cost-segregation-str | No natural spot yet — defer | — |

---

## OG images needed (27 total — not yet created)

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

## Scaffold audit (2026-05-10)

| File | Exists | noindex | No placeholders | Breadcrumb |
|---|---|---|---|---|
| airbnb-14-day-rule | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| vrbo-host-taxes | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| booking-com-host-taxes | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| turo-host-taxes | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| hipcamp-host-taxes | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| rv-rental-host-taxes | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| furnished-finder-taxes | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| neighbor-storage-host-taxes | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| schedule-c-vs-schedule-e-str | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| short-term-rental-loophole | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| cost-segregation-str | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| lodging-tax-by-state | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| airbnb-self-employment-tax | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| airbnb-deductions-checklist | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| mixed-use-rental-taxes | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| house-hacking-taxes | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| str-business-structure | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| airbnb-1099-k | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| quarterly-taxes-for-airbnb-hosts | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| california-short-term-rental-rules | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| new-york-short-term-rental-rules | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| florida-short-term-rental-taxes | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| hawaii-short-term-rental-rules | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| texas-short-term-rental-taxes | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| colorado-short-term-rental-taxes | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| tennessee-short-term-rental-taxes | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |
| arizona-short-term-rental-taxes | ✅ | ✅ removed | ✅ | ✅ Short-Term Rentals |

---

## Infrastructure done

- [x] guides.html: `id="short-term-rentals"` section — 28 cards live, filter chips active
- [x] guides.html: meta description + OG description updated (74 resources / 67 guides)
- [x] guides.html: Gig Work & Delivery count corrected to 8
- [x] guides.html: section `id` attrs on all sections including new STR section
- [x] robots.txt: `Disallow: /_template-article*`
- [x] vercel.json: `^/_[^/].*` → 404 (blocks all `/_*` routes)
- [x] sitemap.xml: 79 live URLs (script-generated, noindex files excluded)
- [x] generate-sitemap.js: re-run after each noindex removal
- [x] 39 existing live articles: 4-level JSON-LD breadcrumbs
- [x] airbnb-host-taxes.html: internal links to /airbnb-14-day-rule, /schedule-c-vs-schedule-e-str, /short-term-rental-loophole
- [x] airbnb-host-taxes.html: breadcrumb updated to Short-Term Rentals section
- [x] All 27 scaffolds: placeholder-free, noindex removed, correct breadcrumbs, read times corrected
- [x] lodging-tax-by-state.html: full body copy + 50-state tax rate table (16 verified + 34 estimated with † caveat)
- [x] short-term-rentals.html: hub page live (decision tree, 28-card grid, FAQ)
