# Short-Term Rental Content — Launch Checklist

Generated: 2026-05-10
Commit baseline: c332c9e

This checklist covers all 27 scaffold files from Prompts 3 and 4.
Infrastructure (breadcrumbs, sitemap, robots, section anchors) is done — `c332c9e`.
Remove `<meta name="robots" content="noindex, nofollow">` from each file as body copy is completed.
Re-run `node generate-sitemap.js` after each batch of noindex removals.

---

## Platform Guides (2 files)
*Goes in guides.html section id="str-platforms" — to be added*

- [ ] **airbnb-14-day-rule.html** — body copy drafted (Prompt 3); review & finalize
- [ ] **vrbo-host-taxes.html** — TODO body copy

---

## STR Tax Strategy Guides (12 files)
*Goes in guides.html section id="str-tax-guides" — to be added*

- [ ] **schedule-c-vs-schedule-e-str.html** — TODO body copy
- [ ] **short-term-rental-loophole.html** — TODO body copy
- [ ] **cost-segregation-str.html** — TODO body copy
- [ ] **lodging-tax-by-state.html** — TODO body copy
- [ ] **airbnb-self-employment-tax.html** — TODO body copy
- [ ] **airbnb-deductions-checklist.html** — TODO body copy
- [ ] **mixed-use-rental-taxes.html** — TODO body copy
- [ ] **house-hacking-taxes.html** — TODO body copy
- [ ] **str-business-structure.html** — TODO body copy
- [ ] **airbnb-1099-k.html** — TODO body copy
- [ ] **quarterly-taxes-for-airbnb-hosts.html** — TODO body copy

---

## STR State Rule Guides (8 files)
*Goes in guides.html section id="str-state-rules" — to be added*

- [ ] **california-short-term-rental-rules.html** — body copy drafted (Prompt 4); review & finalize
- [ ] **new-york-short-term-rental-rules.html** — TODO body copy
- [ ] **florida-short-term-rental-rules.html** — TODO body copy
- [ ] **hawaii-short-term-rental-rules.html** — TODO body copy
- [ ] **texas-short-term-rental-rules.html** — TODO body copy
- [ ] **colorado-short-term-rental-rules.html** — TODO body copy
- [ ] **tennessee-short-term-rental-rules.html** — TODO body copy
- [ ] **arizona-short-term-rental-rules.html** — TODO body copy

---

## Per-file launch steps (repeat for each file above)

1. **Write body copy** — fill in all `<!-- TODO ... -->` sections
2. **Proof FAQ** — FAQs are pre-written; verify accuracy
3. **Verify related cards** — confirm all 6 linked slugs exist and are live (index'd)
4. **OG image** — create `/images/og/{slug}.png` + `.webp` at 1200×630
5. **Remove noindex** — delete `<meta name="robots" content="noindex, nofollow">`
6. **Add to guides.html** — add article card to the correct STR section
7. **Regenerate sitemap** — `node generate-sitemap.js`
8. **Internal links** — add backlinks from related live articles (see notes below)

---

## guides.html STR sections to add
*(deferred until first batch of body copy is ready)*

Three new `.cat-section` blocks need to be added to guides.html:

```html
<!-- Short-Term Rental Platforms -->
<div class="cat-section" id="str-platforms">
  <!-- airbnb-host-taxes (move from gig-work-and-delivery), vrbo-host-taxes -->
</div>

<!-- STR Tax Guides -->
<div class="cat-section" id="str-tax-guides">
  <!-- 12 topic guides -->
</div>

<!-- STR State Rules -->
<div class="cat-section" id="str-state-rules">
  <!-- 8 state guides -->
</div>
```

Note: When `airbnb-host-taxes` moves from Gig Work to STR Platforms, update its breadcrumb
from `gig-work-and-delivery` to `str-platforms`.

---

## Internal links to add from live articles

| Source article | Add link to | Natural anchor location |
|---|---|---|
| airbnb-host-taxes.html | /airbnb-14-day-rule | After "15+ days, regular rules apply…" para |
| airbnb-host-taxes.html | /schedule-c-vs-schedule-e-str | After "avoids self-employment tax entirely…" para |
| airbnb-host-taxes.html | /cost-segregation-str | After "Furniture, appliances…typically 5–7 years" para |
| airbnb-host-taxes.html | /short-term-rental-loophole | No natural spot — defer to deep-dive pages |

*(Awaiting user approval — see Prompt 5 proposal)*

---

## OG images needed (27 total)

Platform guides:
- `/images/og/airbnb-14-day-rule.png` + `.webp`
- `/images/og/vrbo-host-taxes.png` + `.webp`

Strategy guides:
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
- `/images/og/florida-short-term-rental-rules.png` + `.webp`
- `/images/og/hawaii-short-term-rental-rules.png` + `.webp`
- `/images/og/texas-short-term-rental-rules.png` + `.webp`
- `/images/og/colorado-short-term-rental-rules.png` + `.webp`
- `/images/og/tennessee-short-term-rental-rules.png` + `.webp`
- `/images/og/arizona-short-term-rental-rules.png` + `.webp`

---

## STR hub page (proposed)

- [ ] **short-term-rentals.html** — proposed; awaiting approval
  - H1: Short-Term Rental Taxes: The Complete Playbook
  - 3 sections: Platform Guides, Tax Strategy, State Rules
  - Add to sitemap after launch

---

## Done (infrastructure)

- [x] guides.html: section `id` attributes on all 6 existing sections
- [x] guides.html: `id="str-platforms"`, `id="str-tax-guides"`, `id="str-state-rules"` — planned, add with cards
- [x] robots.txt: `Disallow: /_template-article*` added
- [x] sitemap.xml: replaced with `generate-sitemap.js` output (51 live URLs, noindex excluded)
- [x] generate-sitemap.js: script created — re-run after each noindex removal
- [x] 39 live articles: breadcrumbs upgraded to 4-level JSON-LD + 3-level HTML
- [x] airbnb-14-day-rule.html: scaffold complete (4-level breadcrumb, FAQs written)
- [x] 12 STR topic guides: scaffolded (noindex, JSON-LD, FAQ, key questions)
- [x] 8 STR state guides: scaffolded (noindex, JSON-LD, FAQ, 9 H2 structure)
