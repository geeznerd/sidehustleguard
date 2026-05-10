# STR Guides — Content Audit Report

Generated: 2026-05-10  
Covers: 27 scaffold files (7 platform · 12 topic · 8 state)  
Mechanical fixes applied: read times corrected in all 27 files.  
Parts 2–4: proposals only — no edits made.

---

## Part 1 — Mechanical Audit

### Legend
- **Breadcrumb OK?** — HTML visible + JSON-LD both correct 4-level chain  
- **Sibling links** — unique STR guide hrefs anywhere in page (body + related section; hub `/short-term-rentals` counted separately)  
- **Flags**: 🔴 = fix before ANY launch · 🟡 = fix before launch · ✅ = clean  

### Universal issues (all 27 files — resolve once, apply to all)

| Issue | Detail |
|---|---|
| No hub link | Zero files link to `/short-term-rentals`. Every page should link to the hub at least once — natural place: after the intro paragraph or in the related section. |
| Related section non-STR cards | Every related grid includes `/side-hustle-taxes` and `/quarterly-taxes-self-employed`. These belong in the general site but not as primary related links on STR-specific pages. Replace with STR siblings as more pages go live. |
| JSON-LD `&amp;` in NY title | `new-york-short-term-rental-rules.html` BreadcrumbList block has `"New York Short-Term Rental Rules &amp; Taxes"` — parse-valid but renders the literal ampersand entity in structured data. Fix: replace with `&`. |

---

### Audit table

| file | placeholder leaks | read time was → now | breadcrumb OK? | sibling links (excl. hub) | word count | flags |
|---|---|---|---|---|---|---|
| **PLATFORM GUIDES** | | | | | | |
| vrbo-host-taxes | 0 | 8 → 5 min | ✅ | 1 | 811 | 🔴 1 sibling link (< 3) · 🟡 no hub link · 🟡 related has non-STR cards |
| booking-com-host-taxes | 0 | 8 → 5 min | ✅ | 1 | 853 | 🔴 1 sibling link (< 3) · 🟡 no hub link · 🟡 related has non-STR cards |
| turo-host-taxes | 0 | 8 → 5 min | ✅ | 1 | 845 | 🔴 1 sibling link (< 3) · 🟡 no hub link · 🟡 related has non-STR cards |
| hipcamp-host-taxes | 0 | 8 → 5 min | ✅ | 1 | 895 | 🔴 1 sibling link (< 3) · 🟡 no hub link · 🟡 related has non-STR cards |
| rv-rental-host-taxes | 0 | 8 → 5 min | ✅ | 1 | 890 | 🔴 1 sibling link (< 3) · 🟡 no hub link · 🟡 related has non-STR cards |
| furnished-finder-taxes | 0 | 8 → 5 min | ✅ | 1 | 846 | 🔴 1 sibling link (< 3) · 🟡 no hub link · 🟡 related has non-STR cards |
| neighbor-storage-host-taxes | 0 | 8 → 5 min | ✅ | 1 | 874 | 🔴 1 sibling link (< 3) · 🟡 no hub link · 🟡 related has non-STR cards |
| **TOPIC GUIDES** | | | | | | |
| airbnb-14-day-rule | 0 | 8 → 5 min | ✅ | 4 | 867 | 🟡 no hub link · 🟡 related has 2 non-STR cards · 🟡 day-counting examples in TODO (not rendered) |
| schedule-c-vs-schedule-e-str | 0 | 8 → 5 min | ✅ | 4 | 927 | 🟡 no hub link · 🟡 related has 2 non-STR cards · 🟡 decision tree in TODO (not rendered) · 🟡 ≤30-day+services branch not mentioned |
| short-term-rental-loophole | 0 | 8 → 5 min | ✅ | 4 | 956 | 🟡 no hub link · 🟡 related has 2 non-STR cards · 🟡 only 2 of 7 material participation tests listed |
| cost-segregation-str | 0 | 8 → 5 min | ✅ | 4 | 951 | 🟡 no hub link · 🟡 related has 2 non-STR cards · 🟡 phase-down table in TODO (not rendered) · 🟡 one-size-fits-all caveat in TODO |
| lodging-tax-by-state | 0 | 8 → 5 min | ✅ | 4 | 984 | 🔴 no 50-state rate table built (page name implies it exists) · 🟡 no hub link · 🟡 related has 2 non-STR cards |
| airbnb-self-employment-tax | 0 | 8 → 5 min | ✅ | 4 | 992 | 🟡 no hub link · 🟡 related has 2 non-STR cards |
| airbnb-deductions-checklist | 0 | 8 → 5 min | ✅ | 4 | 995 | 🟡 no hub link · 🟡 related has 2 non-STR cards |
| mixed-use-rental-taxes | 0 | 8 → 6 min | ✅ | 4 | 1,028 | 🟡 no hub link · 🟡 related has 2 non-STR cards |
| house-hacking-taxes | 0 | 8 → 6 min | ✅ | 4 | 1,057 | 🟡 no hub link · 🟡 related has 2 non-STR cards |
| str-business-structure | 0 | 8 → 6 min | ✅ | 3 | 1,020 | 🟡 no hub link · 🟡 related has 2 non-STR cards + `/llc-vs-sole-proprietor` · 🟡 S-corp threshold discrepancy vs. `/llc-vs-sole-proprietor` not explained (see Part 3) |
| airbnb-1099-k | 0 | 8 → 6 min | ✅ | 4 | 1,019 | 🟡 no hub link · 🟡 related has 2 non-STR cards |
| quarterly-taxes-for-airbnb-hosts | 0 | 8 → 5 min | ✅ | 3 | 983 | 🟡 no hub link · 🟡 related has 3 non-STR cards |
| **STATE GUIDES** | | | | | | |
| california-short-term-rental-rules | 0 | 10 → 6 min | ✅ | 4 | 1,045 | 🔴 body copy is mostly TODO stubs — far thinner than other state guides (2,500+ words) · 🟡 no hub link · 🟡 related has 2 non-STR cards |
| new-york-short-term-rental-rules | 0 | 10 → 14 min | ✅ | 4 | 2,631 | 🟡 `&amp;` entity in JSON-LD name string · 🟡 no hub link · 🟡 related has 2 non-STR cards |
| florida-short-term-rental-taxes | 0 | 10 → 14 min | ✅ | 4 | 2,627 | 🟡 no hub link · 🟡 related has 2 non-STR cards |
| hawaii-short-term-rental-rules | 0 | 10 → 14 min | ✅ | 4 | 2,712 | 🟡 no hub link · 🟡 related has 2 non-STR cards |
| texas-short-term-rental-taxes | 0 | 10 → 14 min | ✅ | 4 | 2,738 | 🟡 no hub link · 🟡 related has 2 non-STR cards |
| colorado-short-term-rental-taxes | 0 | 10 → 13 min | ✅ | 4 | 2,510 | 🟡 no hub link · 🟡 related has 2 non-STR cards |
| tennessee-short-term-rental-taxes | 0 | 10 → 13 min | ✅ | 4 | 2,544 | 🟡 no hub link · 🟡 related has 2 non-STR cards |
| arizona-short-term-rental-taxes | 0 | 10 → 13 min | ✅ | 4 | 2,552 | 🟡 no hub link · 🟡 related has 2 non-STR cards |

### Summary counts
- Placeholder leaks: **0** (clean)
- noindex/nofollow status: **27/27** correct
- JSON-LD validity: **27/27** parse-valid (NY has semantic `&amp;` issue, not a parse error)
- Breadcrumb 4-level chain: **27/27** correct
- Word count under 800: **0** (vrbo is 811, the floor)
- Word count over 4,000: **0**
- Missing hub link: **27/27** — universal fix needed
- Sibling links < 3: **7** (all platform guides)
- Related section all-STR: **0/27** — universal fix needed as more pages go live
- Read time corrected: **27/27** (all updated to match actual word count)

### Recommended batch fixes (do these once, not per-file)
1. **Add hub link to all 27** — insert `<p>← <a href="/short-term-rentals">Short-Term Rental Tax Hub</a></p>` after the hero intro on each page. One sed pass across all 27.
2. **Swap non-STR related cards** — as more STR guides go live, replace `/side-hustle-taxes` and `/quarterly-taxes-self-employed` slots with STR siblings. This is a content decision deferred until the STR catalog is larger.
3. **Fix NY `&amp;`** — one-line sed on `new-york-short-term-rental-rules.html`.
4. **Add platform sibling links** — platform guides currently link only to `/airbnb-host-taxes`. Each platform guide should also link to 2–3 relevant topic guides (e.g., Vrbo → `/airbnb-14-day-rule`, `/schedule-c-vs-schedule-e-str`, `/lodging-tax-by-state`).

---

## Part 2 — Deep Content Review (5 high-priority guides)

> Proposals only. No edits made. Verify flagged items with a CPA before going live.

---

### 1. `airbnb-14-day-rule`

**What the page gets right**
- §280A(g) is cited by statute number — good
- Binary/on-off nature of the rule is clear: 14 rental days or fewer = income fully excluded; day 15 = all income retroactively taxable for the year
- The personal-use day test (§280A(d), the "10% rule") is correctly treated as a separate rule, not an alternative trigger for the §280A(g) exclusion
- Applies-to-rooms: FAQ correctly confirms the exclusion covers renting a room within a primary residence, not just the full home

**Factual claims to verify with a CPA before launch**

| Claim | Concern |
|---|---|
| "Day 15 makes ALL income taxable, including the first 14 days" | This is the correct interpretation of the binary structure of §280A(g) — but verify with a CPA that this retroactivity framing is standard and won't confuse hosts about tax-free partial-year treatment |
| "§280A(g) does NOT apply to vacation homes or dedicated rental properties" | Verify: the exclusion is specifically for a "dwelling unit" that is the taxpayer's residence (primary or secondary used as residence). Vacation homes rented occasionally may qualify if the owner meets the personal-use day test. This needs clarification. |
| "Applies to primary residences only" | The statute says "dwelling unit" used as a residence — this can include a second home the owner personally uses, not only the primary residence. The page may be over-restricting scope. |

**Content gaps**

| Gap | Detail |
|---|---|
| Day-counting examples are in TODO | The concrete examples (12 days OK, 15 days over the cliff) are in HTML comment `<!-- TODO -->` blocks — not rendered. These are the most useful content on the page for readers. Must be written before launch. |
| "Days rented" definition | How does the IRS count a rental day? If a guest books Fri–Mon, is that 3 nights = 3 days or 4 days? The page should clarify that the IRS counts the number of days the unit is actually used for rental purposes. |
| Impact on deductions | When §280A(g) applies, the host CANNOT deduct rental expenses (since the income is excluded). This is the trade-off the page should mention — it's not purely free money; you lose the deduction too. |
| VRBO/platform difference | Day counting works the same regardless of which platform is used; confirm the page says this (or add it). |

**Proposed citations to add**

- IRS Publication 527 (Residential Rental Property), Chapter 5 — the IRS's own plain-English explanation of the 14-day rule
- §280A(g) statutory text (as a footnote)
- Tax Court: _Bolton v. Commissioner_ is the foundational case on personal-use day counting — worth citing
- IRS FAQ on short-term rentals: irs.gov/faqs

---

### 2. `schedule-c-vs-schedule-e-str`

**What the page gets right**
- Average rental period ≤7 days → Schedule C (active business, SE tax applies): correct per Reg. §1.469-1T(e)(3)(ii)(A)
- "Substantial services" distinction (daily cleaning/meals = Schedule C; furnishings/Wi-Fi = Schedule E): broadly accurate per IRS guidance
- SE tax consequence is clearly explained (15.3% on Schedule C net profit)

**Factual claims to verify with a CPA before launch**

| Claim | Concern |
|---|---|
| "≤7 days automatically means Schedule C" | Not quite accurate — the ≤7 day rule means the activity is NOT a passive rental activity, but it doesn't automatically become Schedule C. It becomes an active business, which typically reports on Schedule C. But if the host is a real estate professional, it may still report differently. Clarify the "typically" qualifier. |
| "Average rental period > 7 days + no substantial services = Schedule E" | This is the most common outcome for typical Airbnb hosts and is correctly described. But: what if average period is >7 and ≤30 days WITH substantial services? This case is missing (see gap below). |
| SE tax rate of 15.3% | Correct for net earnings up to the Social Security wage base ($160,200 in 2023; ~$168,600 in 2024). Above that, only the 2.9% Medicare portion applies. Add the wage-base qualifier. |

**Content gaps**

| Gap | Detail |
|---|---|
| Missing ≤30-day + services branch | Reg. §1.469-1T(e)(3)(ii)(B): if the average rental period is >7 days but ≤30 days AND significant personal services are provided, the activity is ALSO not a passive rental. This is a second path to Schedule C the page doesn't address. |
| Decision tree not rendered | The page outline includes a comparison table/decision tree, but it's in a TODO block. This is the clearest way to explain the matrix. Must be written before launch. |
| QBI deduction interaction | Schedule E rental income may qualify for the §199A QBI deduction (20% deduction on qualified business income) under the right circumstances; Schedule C STR income also may qualify. This is a significant tax benefit the page should mention. |
| State tax implications | A few states treat STR income differently from the federal default (e.g., some states always require Schedule C treatment). Add a note pointing to the state guides. |

**Proposed citations to add**

- Reg. §1.469-1T(e)(3) — the full text of the rental activity exception
- IRS Publication 527 — Residential Rental Property
- Chief Counsel Advice 200021072 — IRS analysis of hotel-like services
- _Balsamo v. Commissioner_ (T.C. Memo) — Tax Court on substantial services test

---

### 3. `short-term-rental-loophole`

**What the page gets right**
- IRC §469 passive activity rules correctly framed as the baseline the loophole escapes
- 7-day average rental period requirement clearly stated
- Audit risk prominently flagged (answer box + dedicated FAQ + TOC section)
- Combination with cost segregation correctly described as a complementary strategy
- Time-log requirement mentioned

**Factual claims to verify with a CPA before launch**

| Claim | Concern |
|---|---|
| "Only Tests 1 and 3 listed" | The page only explicitly names the 500-hour test (Test 1) and the 100-hours-plus-most test (Test 3) out of 7 tests in Reg. §1.469-5T. Tests 2 (substantially all participation), 4 (prior year), 5 (participation < 100 hrs but exceeds passive), 6 (combination), and 7 (facts and circumstances) are not described. At minimum, Test 2 should be added — it's the easiest to meet for hands-on hosts who do ALL the work (even if not 500 hours). |
| "Losses can be deducted against W-2 income dollar-for-dollar" | Confirm: this is correct only when BOTH conditions are met — average rental ≤7 days AND material participation. Neither condition alone is sufficient. Verify the page states both as conjunctive (not disjunctive) requirements. |
| "The normal $25,000 passive loss cap does not apply" | Technically correct — but explain WHY: the activity is reclassified as non-passive (active), not that the passive loss cap is waived. The $25,000 allowance applies to passive losses from rental real estate; this strategy removes the activity from passive classification entirely. |
| "Losses from depreciation are the main driver" | True for most hosts using cost segregation, but operating losses (mortgage interest, maintenance) can also contribute. Don't imply depreciation is required. |

**Content gaps**

| Gap | Detail |
|---|---|
| Real estate professional alternative | If a host qualifies as a real estate professional (750 hours, more than 50% of personal services), they can deduct passive rental losses without the 7-day rule. This is a separate path worth mentioning — many hosts pursuing the loophole would also qualify to explore REP status. |
| Grouping election | Hosts who own multiple properties must be careful about the grouping election (Reg. §1.469-4). If properties are grouped, the average rental period and material participation are tested at the group level, not property-by-property. This nuance affects multi-property hosts. |
| At-risk limitations | Even if passive activity rules are cleared, the at-risk rules under §465 can limit deductibility. Add a sentence. |
| Spouse participation | One FAQ-worthy point: does a spouse's participation hours count toward the material participation tests? (Yes, generally, for spouses who file jointly.) |

**Proposed citations to add**

- Reg. §1.469-5T — Material participation tests (all 7)
- Reg. §1.469-1T(e)(3)(ii) — Average rental period rule
- _Akers v. Commissioner_ (T.C. Memo 2014) — Tax Court case on STR material participation
- IRS Audit Technique Guide: Passive Activity Losses — cites specific documentation requirements
- CCA 201428012 — IRS Chief Counsel on STR grouping elections

---

### 4. `cost-segregation-str`

**What the page gets right**
- 2025 bonus depreciation rate (40%) correctly stated in the rendered FAQ
- Cost segregation study cost range ($5,000–$15,000) and property threshold ($500K+) are reasonable rules of thumb
- Recapture risk acknowledged
- Combination with the STR loophole correctly presented as a complementary strategy

**Factual claims to verify with a CPA before launch**

| Claim | Concern |
|---|---|
| Bonus depreciation phase-down: 60% 2024, 40% 2025, 20% 2026, 0% 2027 | This reflects TCJA as originally enacted. As of mid-2026, Congress may have extended or modified these rates. The page MUST note that legislation could alter this schedule and recommend verifying with a CPA for the current year. The TODO body copy has the right schedule but the rendered FAQ only states 2025's rate. |
| "Cost segregation most beneficial above $500K property value" | This is a common rule of thumb but the real driver is the tax benefit (depreciation reclaimed × marginal rate) vs. study cost. A $300K property with a 37% marginal rate may still pencil out. Consider reframing as "typical break-even point" rather than a hard threshold. |
| "$5,000–$15,000 study cost" | Verify this range is current (2025–2026). The market has changed with AI-assisted cost seg tools entering. Ranges can now be $3,000–$10,000 for residential properties. |

**Content gaps**

| Gap | Detail |
|---|---|
| Phase-down table not rendered | The full 2023–2027 bonus depreciation schedule is in a TODO comment, not rendered. This is core information for a page about cost segregation — a host deciding whether to do a study in 2025 vs. 2026 needs this table. Must be written before launch. |
| "Not one-size-fits-all" caveat not rendered | The acknowledgment that this isn't universal (income level, holding period, future sale plans all matter) is in a TODO block. This is important for compliance purposes — the rendered page currently reads more promotional than it should. |
| Depreciation recapture math example | The recapture rate on accelerated depreciation is 25% (§1250 unrecaptured gain). A concrete example showing the net benefit after recapture would make this page more useful. |
| TCJA extension uncertainty | The Tax Cuts and Jobs Act's bonus depreciation provisions are scheduled to phase out. Congress has discussed extensions multiple times. The page should explicitly note: "If TCJA is extended, these rates may change. Check the current year's schedule before committing to a cost seg study." |
| Qualified Opportunity Fund interaction | For hosts who may sell appreciated property, pairing cost seg with a QOF can defer both regular gain and recapture. Worth a brief mention for sophisticated readers. |

**Proposed citations to add**

- IRC §168(k) — Bonus depreciation statutory provision
- Rev. Proc. 87-56 — Asset class lives used in cost segregation
- IRS Publication 946 (How to Depreciate Property)
- TCJA original text (Pub. L. 115-97, §13201)
- American Society of Cost Segregation Professionals (ASCSP) — industry body, adds credibility

---

### 5. `lodging-tax-by-state`

**Critical finding: the page does not contain a state-by-state rate table.**

This is the most serious content gap in the 27-guide catalog. The page's title, meta description, and position in the hub's navigation all imply users will find state lodging tax rates here. The page currently covers:
- What lodging/occupancy tax is
- Platform collection (Airbnb, Vrbo, Booking.com nuances)
- How to register with your state/county
- FAQs

What is missing:
- Any table of state-level lodging tax rates (even approximate)
- City/county surcharge examples
- Last-verified dates
- State revenue department links

**Factual claims to verify with a CPA or tax attorney before building the table**

| Claim | Concern |
|---|---|
| "Airbnb collects and remits in many but not all jurisdictions" | True, but Airbnb's coverage map changes frequently. The page should link to Airbnb's own tax FAQ page (which lists covered locations) rather than stating coverage as fact, since it can go stale. |
| "Vrbo has narrower coverage than Airbnb" | True as of 2023–2024, but verify current coverage. Vrbo expanded its collection program significantly in 2022–2023. |
| "Booking.com agency model collects; merchant model does not" | Verify this is still accurate. Booking.com's model varies by market and has been evolving. |

**Content gaps**

| Gap | Detail |
|---|---|
| No 50-state table | This is the primary purpose of the page. Without it, the page should either be retitled (e.g., "How Lodging Tax Works for STR Hosts") or the table must be built. Building a 50-state table with state-level rates requires research for each state — recommend doing only the top 15–20 STR markets at launch with a clear "more states coming" note. |
| No "last verified" dates | Tax rates change. Every row in the eventual table needs a last-verified date. Consider a site-wide policy: audit rates annually every January. |
| No local rate examples | State rates are often the floor; city and county surcharges can dwarf them. An example (e.g., Nashville city + Davidson County + TN state = combined 17.25%) would illustrate why "check local rules" matters. |
| No disclaimer on reliance | This page will be relied upon by hosts making real financial decisions. It needs a prominent disclaimer: "Rates shown are for informational purposes. Confirm current rates with your state/county tax authority before remitting. Local rules vary significantly within states." |
| No links to state revenue departments | Each state row (when built) should link to the official state revenue department's lodging tax page. |

**Recommendation before launch:** Do not index this page until a minimum-viable 50-state table is built. The title creates an expectation the current content cannot fulfill. A host who visits expecting rates and finds none will immediately bounce — and that signals a quality problem to Google.

---

## Part 3 — Style and Voice Audit

**Benchmark:** The SHG voice is plain English, short sentences, "knowledgeable friend" tone. The established examples are the rendered FAQ sections and answer boxes visible in the scaffold files.

> Note: The majority of body copy for platform guides and most topic guides is still in `<!-- TODO -->` blocks and cannot be audited for style. This audit covers rendered content (hero intro, answer box, FAQ). Full style review required once body copy is written.

---

### Style flags table

| file | jargon / IRS-speak | passive voice in key instructions | cross-guide contradiction | missing "what to do next" | other |
|---|---|---|---|---|---|
| vrbo-host-taxes | ✅ | ✅ | ✅ | ✅ NW card + CTA box both present | Body not written — full style review pending |
| booking-com-host-taxes | ✅ | ✅ | ✅ | ✅ | Body not written |
| turo-host-taxes | ✅ | ✅ | ✅ | ✅ | Body not written |
| hipcamp-host-taxes | ✅ | ✅ | ✅ | ✅ | Body not written |
| rv-rental-host-taxes | ✅ | ✅ | ✅ | ✅ | Body not written |
| furnished-finder-taxes | ✅ | ✅ | ✅ | ✅ | Body not written |
| neighbor-storage-host-taxes | ✅ | ✅ | ✅ | ✅ | Body not written |
| airbnb-14-day-rule | 🟡 FAQ uses "§280A(g)" without plain-English label on first use | ✅ | ✅ | ✅ | Body not written; rendered FAQ good |
| schedule-c-vs-schedule-e-str | 🟡 FAQ cites "Reg. §1.469-1T(e)(3)" bare — dense for a knowledgeable-friend tone | ✅ | ✅ | ✅ | Body decision tree not written |
| short-term-rental-loophole | 🟡 Answer box uses "passive activity classification" without defining it first | ✅ | ✅ | ✅ | Good audit-risk framing in rendered content |
| cost-segregation-str | 🟡 FAQ uses "bonus depreciation" and "MACRS" without layered definitions | ✅ | ✅ | ✅ | Phase-down table not rendered |
| lodging-tax-by-state | ✅ | ✅ | ✅ | ✅ | Critical: no rate table (see Part 2) |
| airbnb-self-employment-tax | ✅ | ✅ | ✅ | ✅ | Body not written |
| airbnb-deductions-checklist | ✅ | ✅ | ✅ | ✅ | Body not written |
| mixed-use-rental-taxes | ✅ | ✅ | ✅ | ✅ | Body not written |
| house-hacking-taxes | ✅ | ✅ | ✅ | ✅ | Body not written |
| str-business-structure | 🟡 FAQ cites "$80,000–$100,000" S-corp threshold without explaining why it's higher than the $40K–$50K figure in `/llc-vs-sole-proprietor` | ✅ | 🟡 See note below | ✅ | `/llc-vs-sole-proprietor` in related grid (appropriate, but needs cross-ref note) |
| airbnb-1099-k | ✅ | ✅ | ✅ | ✅ | Body not written |
| quarterly-taxes-for-airbnb-hosts | ✅ | ✅ | ✅ | ✅ | Body not written |
| california-short-term-rental-rules | ✅ | ✅ | ✅ | ✅ | Mostly TODO stub — full style review needed |
| new-york-short-term-rental-rules | ✅ | ✅ | ✅ | ✅ | Body fully written; voice consistent with SHG style |
| florida-short-term-rental-taxes | ✅ | ✅ | ✅ | ✅ | Body fully written; voice consistent |
| hawaii-short-term-rental-rules | 🟡 Hawaii-specific tax terms (GET = General Excise Tax, TAT = Transient Accommodations Tax, OTAT) introduced without plain-English labels in the FAQ | ✅ | ✅ | ✅ | Body fully written; acronyms need one-line definitions on first use |
| texas-short-term-rental-taxes | ✅ | ✅ | ✅ | ✅ | Body fully written; voice consistent |
| colorado-short-term-rental-taxes | ✅ | ✅ | ✅ | ✅ | Body fully written; voice consistent |
| tennessee-short-term-rental-taxes | ✅ | ✅ | ✅ | ✅ | Body fully written; voice consistent |
| arizona-short-term-rental-taxes | ✅ | ✅ | ✅ | ✅ | Body fully written; voice consistent |

---

### Cross-guide contradiction: `str-business-structure` vs. `llc-vs-sole-proprietor`

**The gap:** `/llc-vs-sole-proprietor` says S-corp elections "typically make sense at $40,000–$50,000+ in annual net profit." The `/str-business-structure` FAQ says "An S-Corp election only makes sense if your net profit consistently exceeds $80,000–$100,000."

**Is this a contradiction?** Not technically — the higher threshold in the STR guide is correct because:
1. Most Airbnb hosts report on Schedule E (passive income), which has **no SE tax** regardless of structure. An S-corp election on Schedule E income produces zero tax savings.
2. The S-corp threshold only applies to the minority of hosts on Schedule C (average rental ≤7 days, hotel-like services).
3. For those Schedule C hosts, the higher threshold may reflect additional complexity of running a real estate S-corp vs. a service-business S-corp.

**Proposed fix (one sentence to add in `/str-business-structure`):** In the S-corp FAQ answer, after the $80K–$100K threshold, add: "The threshold is higher than for service businesses because most hosts are on Schedule E — where an S-corp produces no SE-tax savings at all. The $40K–$50K rule of thumb you may have seen elsewhere applies to Schedule C businesses. STR hosts are a different case."

---

### Jargon fixes (proposals)

| File | Current phrasing | Proposed plain-English fix |
|---|---|---|
| airbnb-14-day-rule | "§280A(g)" on first use | "the 14-day rule (technically §280A(g))" |
| schedule-c-vs-schedule-e-str | "Reg. §1.469-1T(e)(3)" bare | "IRS passive activity rules (Reg. §1.469-1T)" |
| short-term-rental-loophole | "passive activity classification" without setup | "the 'passive activity' bucket — IRS's way of ring-fencing rental losses" |
| cost-segregation-str | "MACRS" without gloss | "standard depreciation schedule (MACRS)" |
| hawaii-short-term-rental-rules | "GET", "TAT", "OTAT" bare | "GET (General Excise Tax)", "TAT (Transient Accommodations Tax)", "OTAT (Oahu surcharge)" |

---

## Part 4 — Affiliate and CTA Consistency

**Current state:** Both `.nw-card` and `.cta-box` are already present in all 27 scaffold files (confirmed by grep). Every file has customized NW card copy (personalized to the platform or topic) and two CTA boxes (one mid-page, one footer).

The question is whether the NW card is *appropriate* in every guide, not whether to add it.

---

### Affiliate card appropriateness matrix

> ✅ = appropriate as-is · 🔄 = keep but adjust copy · ⚠️ = consider removing or replacing

| file | NW card (LLC formation) | Primary CTA (`/tool`) | Notes |
|---|---|---|---|
| **Platform guides** | | | |
| vrbo-host-taxes | ✅ | ✅ | Host structuring as LLC = natural next step |
| booking-com-host-taxes | ✅ | ✅ | Same |
| turo-host-taxes | 🔄 | ✅ | Turo hosts rent vehicles, not real property. NW card copy should emphasize liability protection for car rental activity rather than "keep home address off filings" framing |
| hipcamp-host-taxes | 🔄 | ✅ | Hipcamp hosts rent land. NW card copy should reference agricultural/land-use liability, not home address privacy |
| rv-rental-host-taxes | 🔄 | ✅ | Same as Turo — vehicle rental context, not real property |
| furnished-finder-taxes | ✅ | ✅ | Mid-term rental hosts benefit from LLC structure (tenant disputes, lease liability) |
| neighbor-storage-host-taxes | ⚠️ | ✅ | Storage hosts: LLC may be less compelling (low liability exposure, low income). Consider replacing with a simpler "do I need to register?" callout instead of a hard affiliate push |
| **Topic guides** | | | |
| airbnb-14-day-rule | ⚠️ | ✅ | The 14-day rule applies to personal residences used occasionally — these hosts almost never form LLCs for a property they live in. The NW card is low-relevance here. Replace with a reminder to check their state's lodging tax rules (`/lodging-tax-by-state`). |
| schedule-c-vs-schedule-e-str | ✅ | ✅ | Business structure is directly relevant to Schedule C determination |
| short-term-rental-loophole | ✅ | ✅ | Hosts pursuing the loophole often DO form LLCs; relevant |
| cost-segregation-str | ✅ | ✅ | Cost seg users are typically serious investors; LLC context is relevant |
| lodging-tax-by-state | ⚠️ | ✅ | Tax registration page — NW card is tangential. Replace with a "how to register your rental with your state" CTA |
| airbnb-self-employment-tax | ✅ | ✅ | SE tax discussion naturally leads to structure optimization |
| airbnb-deductions-checklist | 🔄 | ✅ | The NW card makes sense but copy should emphasize "home office deduction requires separate address" angle rather than generic LLC pitch |
| mixed-use-rental-taxes | ✅ | ✅ | Mixed-use hosts with investment property — LLC relevant |
| house-hacking-taxes | ⚠️ | ✅ | House hackers rent a portion of their primary residence — they generally do NOT need an LLC (the primary residence exemption complicates things). NW card may be actively misleading here. Replace with a `/airbnb-14-day-rule` CTA. |
| str-business-structure | ✅ | ✅ | Direct fit — this is the business structure guide |
| airbnb-1099-k | 🔄 | ✅ | The NW card is a weak fit for a reporting/paperwork guide. Replace with a `/airbnb-deductions-checklist` CTA card instead |
| quarterly-taxes-for-airbnb-hosts | ✅ | ✅ | Hosts thinking about quarterly taxes are managing a business — LLC is a natural step |
| **State guides** | | | |
| california-short-term-rental-rules | 🔄 | ✅ | California charges $800/year per LLC — the NW card should acknowledge this cost (it's in the FAQ already). The affiliate card copy should say "note: CA LLCs cost $800/year minimum — factor that in." |
| new-york-short-term-rental-rules | 🔄 | ✅ | NYC is one of the most heavily regulated STR markets; NY LLC formation has higher ongoing complexity. Copy should note this nuance |
| florida-short-term-rental-taxes | ✅ | ✅ | Florida is a major STR market; LLCs are common. Good fit. |
| hawaii-short-term-rental-rules | ✅ | ✅ | Hawaii's GET/TAT complexity makes professional structure more compelling |
| texas-short-term-rental-taxes | ✅ | ✅ | TX has no state income tax but strong LLC utility for liability |
| colorado-short-term-rental-taxes | ✅ | ✅ | CO is a high-activity STR market; good fit |
| tennessee-short-term-rental-taxes | ✅ | ✅ | Nashville market; good fit |
| arizona-short-term-rental-taxes | ✅ | ✅ | Phoenix/Scottsdale market; good fit |

---

### Summary

- **NW card appropriate as-is:** 16/27
- **NW card: adjust copy:** 7/27 (Turo, Hipcamp, RV, Furnished Finder, deductions checklist, NY, CA) — copy is too generic or doesn't fit the property type
- **NW card: consider replacing:** 4/27 (neighbor-storage, airbnb-14-day-rule, lodging-tax-by-state, house-hacking-taxes) — low relevance or potentially misleading
- **CTA box (`/tool`):** appropriate in all 27 — no changes proposed

### Proposed rule going forward
> "Show the NW card on every guide where the host has ongoing income from a property or vehicle they own. Remove or replace it on guides where the primary audience is casual/occasional renters (14-day rule, house hacking) or pure informational/reference pages (lodging tax rates)."

---

## Appendix — Files still needing body copy

This audit confirms that read times will increase significantly once body copy is written. Re-run `node generate-sitemap.js` and re-audit read times before removing noindex from each file.

| file | current word count | expected final range | read-time impact |
|---|---|---|---|
| All 7 platform guides | 811–895 | 2,000–2,500 | 5 min → 10–13 min |
| Most topic guides | 867–1,057 | 1,800–2,500 | 5–6 min → 9–13 min |
| california-short-term-rental-rules | 1,045 | 2,500–3,000 | 6 min → 13–15 min |
| State guides (7 of 8) | 2,510–2,738 | complete | 13–14 min stays |
