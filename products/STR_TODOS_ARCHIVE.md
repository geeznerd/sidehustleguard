# STR / Platform Page TODOs — archived 2026-05-22

Unfinished section notes that were removed from guide pages during
cleanup. Saved here so you can write platform-specific content later
when you have traffic data on which pages matter most.

---

## airbnb-1099-k.html

### `#what-the-1099-k-reports` — What the 1099-K actually reports

```
TODO: 2–3 paragraphs covering:
    - The 1099-K is a gross payment report, not a net income report. It captures: every dollar
      Airbnb paid out before deductions, cleaning fees (which Airbnb includes in the payout and
      then remits to the host — the host then pays to cleaners), and in some cases, occupancy
      taxes that Airbnb collects and remits on the host's behalf (varies by jurisdiction).
    - The Airbnb host service fee (typically 3%) has already been deducted before payout — so
      that $3,000 fee is NOT in your 1099-K amount. Your 1099-K reflects gross payout received,
      not gross booking value.
    - Callout-amber: "Do not plug your 1099-K amount directly into Schedule E as gross income.
      You will overpay taxes on pass-through amounts that aren't actually your income."
```

### `#2025-threshold-changes` — 2025 threshold: who gets a 1099-K from Airbnb

```
TODO: 2–3 paragraphs covering:
    - Current status: The IRS has been delaying the $600 threshold for several years. For 2024
      and 2025, a transitional relief threshold of $5,000 applies (or the prior $20,000 + 200
      transactions threshold in some cases, depending on IRS guidance at filing time). Always
      check IRS.gov for the current year's threshold.
    - State thresholds: several states (Vermont, Massachusetts, Maryland, Virginia, DC) have
      their own lower thresholds — some as low as $600. Airbnb will send 1099-Ks according to
      both federal and applicable state thresholds.
    - Callout-amber: "State thresholds may differ from federal. If you're in a lower-threshold
      state, you may receive a state 1099-K even if you're under the federal threshold."
```

### `#no-1099-k-income-still-taxable` — No 1099-K doesn't mean no taxes

```
TODO: 2–3 paragraphs covering:
    - Critical misconception: many hosts believe that if they don't receive a 1099-K, their
      income isn't taxable. This is wrong.
    - The 1099-K is an information return — its purpose is to help the IRS cross-check reported
      income. The underlying income is taxable regardless of whether a 1099-K was issued.
    - If Airbnb didn't send you a 1099-K because your earnings were below the threshold, you
      still must report the income on Schedule E.
    - Callout-amber: "The IRS gets a copy of your 1099-K if one is issued. They compare it to
      your return. Missing a 1099-K on your return triggers matching errors. Report income
      regardless of whether a 1099-K arrives."
```

### `#reconciling-the-1099-k` — How to reconcile the 1099-K on Schedule E

```
TODO: Step-by-step reconciliation:
    (1) Start with the 1099-K gross payout amount.
    (2) Identify passthrough amounts: if Airbnb collected and remitted occupancy taxes on your
        behalf, those may be in the gross payout — subtract them (they're not your income,
        they're government funds you never kept).
    (3) Cleaning fees collected and paid to third-party cleaners: the amount you collected from
        guests and immediately paid to cleaners isn't your profit — deduct it as a cleaning
        expense.
    (4) The result is closer to your gross rental income.
    (5) Apply all other Schedule E deductions to get to net rental income.
    You can explain any discrepancy between 1099-K and Schedule E gross income in a note or
    your records — the IRS expects the Schedule E amount to be less than the 1099-K.
```

### `#if-your-1099-k-is-wrong` — What to do if your 1099-K is incorrect

```
TODO: 2–3 paragraphs covering:
    - Airbnb 1099-Ks can include errors: wrong dollar amount, wrong TIN, incorrect address, or
      amounts from a cancelled transaction.
    - How to request a correction: contact Airbnb through the Help Center or account settings,
      specifically requesting a corrected 1099-K. Airbnb will issue a revised form if the error
      is confirmed.
    - If you can't get a correction before filing: report your actual correct income on Schedule
      E, keep documentation of the discrepancy, and be prepared to explain the difference if
      the IRS flags a mismatch. Do not simply copy the wrong 1099-K amount onto your return.
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - The 1099-K is a starting point, not the finish line. Your actual taxable rental income —
      after removing passthroughs and applying deductions — is usually significantly less.
    - Keep records of all payout components throughout the year so you can reconcile accurately
      at tax time.
```

---

## airbnb-14-day-rule.html

### `#what-is-the-14-day-rule` — What is the 14-day rule —§280A(g) explained

```
TODO: 2–3 paragraphs covering:
    - IRC §280A(g) statutory language in plain English: a dwelling unit used as a residence
      may exclude rental income if the unit is rented for fewer than 15 days during the year
    - Common name: the "Augusta Rule" — named for Masters Tournament homeowners in Augusta, GA
      who rent their homes for huge sums during the tournament week (7–10 days) tax-free
    - How it interacts with §280A generally: §280A ordinarily limits deductions for
      "personal residences," but subsection (g) carves out the 14-day full exclusion
    - What "primary residence" means: the home where you live for the majority of the year;
      generally the same standard as the §121 home-sale exclusion
    - Callout-green: real Augusta Rule example — rent your home for 12 days at $2,000/night
      = $24,000 completely tax-free. No Schedule E. No deductions claimed either.
```

### `#what-counts-as-a-rental-day` — What counts as a "rental day"

```
TODO: 2–3 paragraphs covering:
    - Definition: any day the property is rented at or above fair market value to ANY person
    - Partial days: the IRS has not issued clear regulations on this, but tax professionals
      generally treat any day on which a guest occupies the property (including check-in and
      check-out days) as a full rental day — conservative approach is safest
    - Days that do NOT count toward the 14-day limit:
        • Days the property is available but not booked
        • Days you personally use the property
        • Days the property is vacant between bookings
    - Days that DO count:
        • Each night of a multi-night stay (a 5-night booking = 5 rental days)
        • Check-in and check-out days if the guest occupies the space
    - Comparison table: "Counts as rental day" vs "Does not count" with examples
    - Callout-amber: "A common mistake — hosts count bookings, not nights. A 3-booking
      stay of 5 nights each is 15 rental days, not 3. Day-count matters, not booking-count."
```

### `#primary-residence-requirement` — Primary residence requirement —vacation homes don't qualify

```
TODO: 2–3 paragraphs covering:
    - §280A(g) applies only to a "dwelling unit used as a residence" — the IRS interprets
      this as your primary home, not a vacation cabin or investment property
    - "Used as a residence" test: you must personally use it for the greater of 14 days or
      10% of total rental days during the year — OR it is your primary home
    - What happens with a second home: if you rent your vacation cabin year-round and never
      personally use it for 14+ days, the rules revert to standard Schedule E rental rules
      (no 14-day exclusion applies, but full deductions available)
    - What happens with the home itself during the rental period: you don't have to move out —
      some hosts rent a specific room or a portion of the home while remaining present
      (see house-hacking section cross-link)
    - Callout-amber: "Own a ski cabin and an Airbnb in your primary city? Only the primary
      home gets the §280A(g) exclusion — the ski cabin's income is fully taxable."
```

### `#crossing-the-threshold` — What happens when you cross day 15

```
TODO: 2–3 paragraphs covering:
    - The all-or-nothing flip: the moment total rental days reach 15 in the year, the exclusion
      is gone and ALL rental income for the year becomes reportable on Schedule E
    - This includes retroactive tax on the first 14 days — there is no "first 14 days free"
      partial benefit once the threshold is crossed
    - Real scenario: host rents 12 days in January ($5,000). Then rents 3 more days in June
      ($2,000). Total = 15 days. ALL $7,000 is now taxable. Had they stopped at 14 days,
      $5,000 would have been tax-free.
    - Decision calculus: if you're at 13 days, a 2-day booking worth $800 may trigger tax
      on $5,000+ of already-received income — know your day count before accepting bookings
    - Callout-amber: "Hosts who don't track their rental day count mid-year are the most
      likely to accidentally blow the exclusion with a last-minute booking"
```

### `#14-day-rule-and-deductions` — The 14-day rule and deductions —the trade-off

```
TODO: 2–3 paragraphs covering:
    - The exclusion and deductions are mutually exclusive: if income is tax-free (14 days
      or fewer), rental expenses are non-deductible. You can't claim the $0 income AND
      deduct the cleaning fees and utilities.
    - The flip side: once you cross 15 days and report income, you can deduct all legitimate
      rental expenses — cleaning, supplies, repairs, depreciation, Airbnb service fee, the
      rental-use % of mortgage interest, utilities, insurance
    - Math check: when is it worth crossing the threshold intentionally? Cover the break-even
      analysis — if potential deductions + additional rental income > tax on all income,
      crossing the line may be worth it
    - Callout-navy: "Some hosts who have significant unreimbursed rental expenses and
      depreciation may actually pay less tax by renting MORE than 14 days, because the
      deductions wipe out a large portion of the taxable income"
```

### `#common-miscounting-mistakes` — Common miscounting mistakes

```
TODO: 5 numbered H3 subsections:
    1. Counting bookings instead of nights — a 5-night booking is 5 rental days, not 1
    2. Forgetting check-in and check-out days — if a guest checks in Thursday and out Monday,
       that's 4 nights = 4 rental days (Thursday, Friday, Saturday, Sunday)
    3. Including multiple platforms — days on Vrbo and days on Airbnb count toward the SAME
       14-day limit; the limit is per-property, not per-platform
    4. Counting personal-use days as rental days — days you personally stay in the property
       are NOT rental days and don't count toward the 14-day limit
    5. Applying the rule to a property that isn't a primary residence — the rule only works
       for your primary home, not a vacation cabin or dedicated rental
```

### `#platform-tracking` — Does Airbnb count days for you?

```
TODO: 2 paragraphs covering:
    - Airbnb's calendar shows booked nights, but it doesn't tell you your "rental day count"
      for §280A(g) purposes — you have to track this yourself
    - How to pull the data: Airbnb's "Transaction History" export (CSV) shows all completed
      stays with dates. Count nights, not reservations. Check-in + length of stay = rental days.
    - Vrbo has a similar "Earnings Report" export. If listing on multiple platforms, combine both.
    - Callout-navy: recommend keeping a running calendar spreadsheet — one row per booking,
      check-in date, check-out date, nights. Running total column. Stop accepting bookings
      when you're at 13 if you want to preserve the exclusion.
    - When to stop accepting bookings: set a manual block on your calendar once you hit
      14 confirmed nights for the year if you want to preserve the tax-free status
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - The 14-day rule is genuinely valuable — a clean, legal path to thousands in tax-free
      income for hosts who want to rent occasionally without tax complexity
    - The three things that kill it: renting a non-primary-residence property, miscounting
      nights vs. bookings, and accepting one last booking that pushes total days to 15
    - Action items: track rental days yourself (don't rely on platform calendars), count
      nights not bookings, block your calendar once you hit 14, and remember the rule covers
      ALL platforms combined toward the same limit
```

---

## airbnb-deductions-checklist.html

### `#platform-fees-and-direct-costs` — Platform fees and direct rental costs

```
TODO: 2–3 paragraphs covering:
    - Fully deductible (no allocation needed — 100% rental): Airbnb host service fee
      (typically 3% of booking subtotal), cleaning fees you pay to a third-party cleaner
      (not the guest cleaning fee you collect — that's income), supplies purchased exclusively
      for guests (toiletries, paper goods, coffee, welcome basket items), guest communication
      platform costs, smart lock subscriptions, keypad entry systems, and professional
      photography of the listing.
```

### `#home-expenses-by-rental-percentage` — Home expenses: the rental-use percentage

```
TODO: 2–3 paragraphs covering:
    - For properties used both personally and as a rental, expenses are deductible in proportion
      to rental use. Standard allocation method: rental days ÷ (rental days + personal use days).
    - Example: 90 rental days, 30 personal days = 90/120 = 75% deductible.
    - Expenses allocated: mortgage interest (deductible on Schedule A as personal use, on
      Schedule E as rental use), property taxes (same split), homeowners insurance, utilities
      (electric, gas, water, internet if rental is the full property), HOA fees, general
      maintenance costs.
    - Callout-navy: "If you rent the entire property and never use it personally (full-property
      STR that's not your primary home), the allocation is 100% — all expenses are deductible
      with no personal-use math."
```

### `#depreciation` — Depreciation —your largest deduction

```
TODO: 2–3 paragraphs covering:
    - Depreciation is the annual deduction for the "wear and tear" of the property. For
      residential rental property, the IRS uses a 27.5-year straight-line schedule.
    - Only the building is depreciable — not the land.
    - How to calculate: (purchase price + improvements − land value) ÷ 27.5 = annual
      depreciation.
    - Land value: use the county assessor's allocation or an appraisal.
    - Example: $300,000 purchase price, $60,000 land = $240,000 depreciable basis ÷ 27.5 =
      $8,727/year.
    - For mixed-use properties, multiply by the rental-use percentage.
    - Note: furniture and appliances depreciate on 5-year schedules (or Section 179 immediate
      expense); this is separate from building depreciation.
```

### `#repairs-vs-improvements` — Repairs vs improvements —the most common confusion

```
TODO: 2–3 paragraphs covering:
    - Repairs: deducted in full in the year incurred. Definition: restores the property to its
      original condition without adding value or extending useful life. Examples: replacing a
      broken window, fixing a leaky pipe, patching drywall, repainting, replacing a broken
      appliance with a like-kind equivalent.
    - Improvements: capitalized and depreciated over the asset's life. Definition: adds value,
      extends useful life, or adapts the property to a new use. Examples: adding a deck,
      remodeling a kitchen, adding a room, installing new HVAC.
    - The $2,500 safe harbor (per invoice, per item) allows routine maintenance and small
      replacements to be expensed immediately.
    - Callout-amber: "Replacing all the carpeting before a rental season = capital improvement.
      Patching a damaged section = repair. When in doubt, consult your CPA — the IRS
      distinguishes these carefully."
```

### `#professional-fees-and-other` — Professional fees, marketing, and other deductions

```
TODO: 2–3 paragraphs covering:
    - Fully deductible: CPA or tax preparer fees attributable to the rental activity, property
      management fees, advertising costs (beyond Airbnb — social media ads, own website), legal
      fees related to the rental, subscription fees for rental management software (Guesty,
      Hospitable, etc.), travel to the property for maintenance or inspection (if it's not your
      primary home), cell phone percentage used for rental management.
    - Also: local lodging tax paid to authorities (if you collect and remit yourself), insurance
      premiums for landlord or short-term rental policies, home warranty plans covering the
      rental.
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - The biggest deductions — depreciation, mortgage interest, and property taxes — require
      proper allocation for mixed-use properties and accurate record-keeping.
    - The Airbnb service fee and direct guest-serving expenses are clean 100% deductions.
    - Track all expenses throughout the year with receipts; don't reconstruct at tax time.
```

---

## airbnb-self-employment-tax.html

### `#schedule-e-no-se-tax` — Schedule E: why most hosts owe no SE tax

```
TODO: 2–3 paragraphs covering:
    - Rental income reported on Schedule E is "passive income" under IRC §469. Passive income
      is not subject to self-employment tax (Social Security + Medicare).
    - A host who provides a space for guests — without substantial hotel-like services — is
      earning passive rental income, not operating a business.
    - The 15.3% SE tax that applies to freelancers and sole proprietors simply does not touch
      Schedule E rental income.
    - This is one of the most misunderstood distinctions in side-hustle taxation.
```

### `#when-se-tax-applies` — When SE tax applies to Airbnb hosts

```
TODO: 2–3 paragraphs covering:
    - Cover the Schedule C trigger: (1) average rental period of 7 days or fewer AND
      (2) substantial services provided (daily cleaning, meals, concierge, transportation).
    - When both are true, the IRS treats the activity as a trade or business, income is reported
      on Schedule C, and SE tax applies to net profit.
    - Also briefly mention that some hosts choose Schedule C incorrectly — they should not
      self-elect Schedule C just because they feel "active." The facts of the rental activity
      determine the correct schedule.
```

### `#what-se-tax-costs` — What SE tax actually costs —the 15.3% math

```
TODO: 2–3 paragraphs covering:
    - SE tax composition: 12.4% Social Security (on first $176,100 of net SE income in 2025)
      + 2.9% Medicare (no cap) = 15.3% total.
    - Reduced base: self-employment income × 92.35% before applying the rate (accounts for the
      employer-equivalent deduction).
    - Example: $40,000 net STR profit on Schedule C → $40,000 × 92.35% = $36,940 × 15.3% =
      $5,652 in SE tax.
    - Silver lining: deduct half of SE tax ($2,826) as an above-the-line deduction on Form 1040.
    - Callout-amber with the full example calculation.
```

### `#quarterly-estimated-payments` — SE tax and quarterly estimated payments

```
TODO: 2–3 paragraphs covering:
    - Schedule C hosts must make quarterly estimated payments to cover both income tax and SE tax.
    - SE tax is not withheld by Airbnb — it accumulates as a year-end liability if ignored.
    - Quarterly deadlines: April 15, June 15, Sept 15, Jan 15.
    - Safe harbor: pay 100% of prior year total tax (110% if prior-year AGI > $150K) in equal
      installments.
    - Callout-navy: "If you're on Schedule E, your quarterly payments are lower — SE tax isn't
      in the equation. This is another reason the Schedule C vs E distinction matters practically."
```

### `#reducing-se-tax` — Reducing SE tax —deductions and the S-Corp strategy

```
TODO: 2–3 paragraphs covering:
    - Two approaches: (1) Deduct all legitimate business expenses — they reduce net profit,
      which reduces the SE tax base. Every $1 of deduction at a combined 30% income + 15.3% SE
      rate saves ~$0.45. (2) S-Corp election for high earners: set a reasonable salary (subject
      to payroll taxes), take the rest as a distribution (not subject to SE tax).
    - Typically saves SE tax on income above the salary.
    - Break-even for S-Corp usually around $80K+ net profit due to payroll administration costs.
    - Callout-amber: "The S-Corp strategy is only relevant for Schedule C hosts — it provides
      zero SE tax savings on Schedule E passive income."
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - Most Airbnb hosts are safe on Schedule E with zero SE tax — the key is not accidentally
      triggering Schedule C by providing substantial services or marketing as a hotel-style
      accommodation.
    - If you are on Schedule C, factor SE tax into pricing from day one, make quarterly
      payments, and consider S-Corp if net profit consistently exceeds $80K.
```

---

## arizona-short-term-rental-taxes.html

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing the Arizona STR tax situation — 5.5% state TPT plus city add-ons, centralized AZTaxes.gov filing system, strong preemption law preventing city STR bans, 2.5% flat income tax advantage, and ongoing political tension in cities like Sedona over local authority.
```

---

## booking-com-host-taxes.html

### `#merchant-vs-agency-model` — Merchant vs Agency Model —the key tax distinction

```
TODO: 2–3 paragraphs covering:
    - Merchant Model: Booking.com charges guest's card at booking, remits net to host after
      deducting commission (~15%). Booking.com IS the merchant of record. May issue 1099-K.
      Booking.com typically handles lodging tax collection in supported markets.
    - Agency Model: Guest pays host directly at check-in (credit card, cash, or bank transfer).
      Booking.com invoices host for its commission afterward. Host IS the merchant of record.
      No 1099-K from Booking.com. Host responsible for collecting and remitting lodging taxes.
    - Comparison table: Merchant vs Agency (who collects payment, who remits tax, who issues 1099)
    - Note: Which model applies to a given property depends on market, property type, and
      Booking.com's regional agreements — check your Extranet settings under "Payments"
```

### `#does-booking-com-send-a-1099` — Does Booking.com send a 1099?

```
TODO: 2 paragraphs covering:
    - Merchant Model: Booking.com may issue 1099-K at federal threshold ($2,500 in 2025)
      if it processes payments on your behalf
    - Agency Model: Booking.com does not process guest payments, so no 1099-K. You may
      receive 1099s from individual payment processors (Stripe, Square) if volume exceeds thresholds
    - In both cases: you owe tax on all rental income regardless of whether a 1099 arrives
    - Booking.com commission is deductible as a rental expense in both models
```

### `#sales-tax-on-direct-bookings` — Sales tax on direct bookings

```
TODO: 2 paragraphs covering:
    - Agency Model hosts collect payment directly → they may owe state/county sales or lodging tax
      on each booking — Booking.com won't collect it
    - Some states classify short-term rentals as "retail sales" and apply sales tax in addition to
      lodging tax — especially relevant in states like Texas and Arizona
    - Registration requirement: most states require STR hosts collecting their own payment to
      register as a tax collector (separate from income tax registration)
    - Callout-amber: "Agency Model hosts: check your state's lodging tax registration requirements
      BEFORE your first booking — retroactive registration is much harder"
```

### `#withholding-for-non-us-hosts` — Withholding rules and W-8BEN

```
TODO: 1–2 paragraphs covering:
    - This section is relevant for US-based readers as context (Booking.com has a much larger
      share of non-US hosts than Airbnb/Vrbo, which affects how co-hosting arrangements work)
    - If a US host uses a non-US co-host or property manager, withholding rules may apply
    - W-9 requirement: US hosts should have a W-9 on file with Booking.com to avoid backup
      withholding on Merchant Model payments
    - Callout-navy: "US hosts: make sure your W-9 is on file in Booking.com Extranet under
      Finance > Tax Information to avoid 24% backup withholding"
```

### `#what-booking-com-hosts-can-deduct` — What Booking.com hosts can deduct

```
TODO: 2 paragraphs covering:
    - Booking.com commission (typically 15% of booking value) — 100% deductible as rental expense
    - All same direct and shared expenses as Airbnb/Vrbo: cleaning, supplies, maintenance,
      utilities (rental %), mortgage interest (rental %), depreciation
    - One Booking.com-specific note: if you're on Agency Model and use a payment processor
      (Stripe, Square), those processing fees are also deductible
```

### `#state-and-local-lodging-taxes` — State and local lodging taxes

```
TODO: 2 paragraphs covering:
    - Booking.com collects and remits in some markets but less comprehensively than Airbnb
    - Check Extranet > Finance > Tax Information to see what's collected in your market
    - Agency Model hosts bear full responsibility — Booking.com won't collect any tax
    - Brief overview of how to register for lodging tax collection in your state
```

### `#should-booking-com-hosts-form-an-llc` — Should Booking.com hosts form an LLC?

```
TODO: 2 paragraphs covering:
    - Same liability rationale as Airbnb/Vrbo: guest injuries and property disputes expose
      personal assets without LLC protection
    - Booking.com's larger share of international guests may increase dispute risk for US hosts —
      slightly stronger argument for LLC than domestic-only platforms
    - Note that LLC doesn't change the payment model or tax filing requirements
```

### `#common-mistakes` — Common mistakes Booking.com hosts make

```
TODO: 4–5 numbered H3 subsections:
    1. Not knowing which payment model applies to their property
    2. Assuming Booking.com handles all taxes (Agency Model hosts have full tax responsibility)
    3. Forgetting to file a W-9 with Booking.com, triggering 24% backup withholding
    4. Not deducting the Booking.com commission as a rental expense
    5. Not reconciling gross bookings against net payouts before reporting income
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - Booking.com income is taxed like all other STR income — Schedule E, same deductions,
      same depreciation rules. The platform-specific work is understanding your payment model
      and ensuring your tax registrations match it
    - Action items: check your Extranet payment model, file your W-9, verify lodging tax
      coverage for your market, deduct Booking.com commission, and track all income regardless
      of 1099 receipt
```

---

## california-short-term-rental-rules.html

### `#state-registration` — State-level registration and permitting —California's patchwork approach

```
TODO: 2–3 paragraphs covering:
    - No California state agency issues STR licenses or permits — this is entirely a local
      jurisdiction matter (city, county, or both depending on whether you're in an
      incorporated city or unincorporated county land)
    - California's AB-1217 (California Home Sharing Act, effective January 1, 2024): limits
      cities' ability to COMPLETELY prohibit owner-occupied primary-residence STRs. Cities
      may still regulate (require permits, restrict nights, mandate primary residency, require
      liability insurance), but a blanket ban on primary-residence hosting is no longer
      allowed. Key limitation: applies only to the owner's primary residence — cities retain
      full authority to ban or restrict investment/non-primary STRs.
    - Common local requirements hosts face: STR permit/license (annual fee), TOT registration
      certificate, proof of primary residency, property owner consent if renting, liability
      insurance minimums (some cities require $1M+ policies), safety inspections (smoke
      detectors, CO detectors, fire extinguishers), posting permit number in all listings
    - HOA caveat: California HOAs may still prohibit or limit STRs regardless of city law
      and regardless of AB-1217 — check your CC&Rs before listing
    - Notable city stances (overview, details in city/county section):
        • Los Angeles: STR ordinance fully enforced since 2023 — primary residence only,
          120-night cap (extendable), must register and display permit number on listing
        • San Francisco: Home Sharing Ordinance — primary residence only, host must be
          present or it's a "unhosted" rental (different rules), annual registration $750
        • San Diego: STR permits required, tiered permit system (Tier 1 owner-occupied,
          Tier 2 non-owner-occupied with caps), significant demand for limited Tier 2 permits
        • Santa Monica: Effectively bans non-hosted STRs under 30 days; hosted STRs allowed
          with registration
    - Callout-amber: "Your city's STR rules are the starting point, not this guide. Rules
      change frequently — LA, SF, and San Diego all updated their ordinances between 2023
      and 2025. Check your city's official website for current permit availability."
```

### `#state-taxes` — State-level taxes on California rental income

```
TODO: 2 paragraphs covering:
    - California does NOT have a statewide transient occupancy tax (TOT) — all TOT is
      imposed at the city/county level (covered in next section)
    - California sales tax (base 7.25% + local add-ons): residential rental income is
      EXEMPT from California sales tax — you do not collect or remit California sales tax
      on STR bookings. This is a common misconception.
    - California state income tax: rental income is taxable for California income tax
      purposes. Report on California Schedule CA (FTB). California follows federal passive
      activity rules — Schedule E rental income is passive, not subject to SDI (State
      Disability Insurance equivalent). Rate depends on California marginal bracket
      (1%–13.3% depending on income).
    - California FTB Form 568 (LLC return): hosts operating through a single-member LLC
      must file Form 568 and pay the $800 annual LLC minimum franchise tax, even if no
      California income tax is owed. This applies regardless of profitability.
    - No California self-employment tax equivalent: California does not have a state-level
      SE tax — only the federal 15.3% SE tax applies (and only for Schedule C filers)
    - Callout-navy: "The $800 annual LLC minimum tax is one of the most common surprise
      costs for California hosts who form an LLC. It's owed every year regardless of whether
      the rental was profitable."
```

### `#what-platforms-collect` — What Airbnb and Vrbo collect automatically in California

```
TODO: 2 paragraphs covering:
    - Airbnb's California coverage: Airbnb has tax collection and remittance agreements
      with most major California cities and counties. Where an agreement exists, Airbnb
      adds TOT to the guest's booking total, collects it, and remits directly to the local
      authority. The host receives payouts net of Airbnb's host fee but does NOT receive
      the TOT portion — Airbnb holds and remits it.
    - How to verify your jurisdiction: Airbnb's Help Center has a "Local tax collection"
      page with a searchable list of every U.S. jurisdiction where Airbnb collects. If your
      city is on the list, you're covered for TOT — but you may still need to register for
      a local STR permit separately (TOT collection ≠ STR permit).
    - Vrbo (Expedia): also has collection agreements with many California jurisdictions,
      but coverage does not always match Airbnb's. If you list on both platforms, check
      each one's coverage list independently.
    - Important gap: even if Airbnb remits your city's TOT, they do NOT handle local STR
      permit registration on your behalf. You must register for a permit independently.
    - Direct bookings: any guest you book outside Airbnb/Vrbo is entirely your
      responsibility — you collect TOT, register with the city, and remit on schedule.
    - Callout-navy: "Check Airbnb's tax collection page every year before the new tax
      season — coverage agreements are updated as new cities sign on and existing
      agreements are modified."
```

### `#filing-schedule` — Filing schedule and where to file

```
TODO: 2 paragraphs covering:
    - For jurisdictions where you are responsible for TOT (not covered by platform agreements,
      or direct bookings): you must register, file returns, and remit taxes on the schedule
      set by your local authority — typically monthly or quarterly for new registrants,
      sometimes annually for low-volume operators.
    - Where to file: each city and county has its own process — there is no unified California
      STR filing portal. Common portals: San Francisco's Treasurer & Tax Collector website,
      Los Angeles Office of Finance portal, San Diego Treasury portal. Smaller cities may
      still use paper forms submitted by mail.
    - Registration steps (general): (1) go to your city/county finance or treasurer website,
      (2) find the "transient occupancy tax" or "short-term rental registration" section,
      (3) complete the registration form and receive your TOT certificate and account number,
      (4) include this registration number in your Airbnb/Vrbo listing (most cities now
      require this), (5) file returns on the required schedule and remit taxes collected.
    - State income tax (California FTB): STR income goes on your California Form 540,
      Schedule CA. California closely mirrors federal treatment — rental income/losses
      from Schedule E feed through to California taxable income. File by April 15 (or
      October 15 with extension).
    - Callout-navy: "Most California city TOT portals now offer online filing and
      electronic payment. Paper filing by mail is still available but significantly
      slower — build in extra time near deadlines."
```

### `#penalties` — Penalties for non-compliance

```
TODO: 2 paragraphs covering:
    - Operating without a permit: fines vary significantly by city. San Francisco: up to
      $1,000 per day. Los Angeles: civil penalties + required cessation of hosting until
      permitted. San Diego: fines per violation. Platforms (Airbnb, Vrbo) have enforcement
      sharing agreements with several California cities — they will delist non-compliant
      properties when notified by the city.
    - Failure to collect/remit TOT: hosts are personally liable for all uncollected TOT plus:
      interest at 1.5% per month (18% per year in many California jurisdictions) from the
      date the tax was due, plus a 25% civil penalty on the unpaid amount. Some cities
      impose additional penalties for willful non-compliance. Voluntary disclosure programs
      exist in some cities to reduce penalties — if you discover an unregistered obligation,
      registering proactively and remitting what's owed is almost always better than waiting
      to be caught.
    - Callout-amber: "The interest and penalty stack on unpaid TOT can exceed the original
      tax itself within 2–3 years. A $500 uncollected TOT liability from 2022 could be a
      $750+ liability by 2025 after interest and penalties. Don't wait."
```

### `#recent-changes` — Recent rule changes —2024–2026

```
TODO: 2–3 paragraphs covering:
    - AB-1217 (California Home Sharing Act, effective January 1, 2024): The most significant
      state-level change. Prohibits local governments from enacting or enforcing a complete
      ban on short-term rentals of owner-occupied primary residences. Cities may still
      impose: permit requirements, annual night caps (many cities use 90–120 nights/year),
      primary residency requirements, health and safety standards, noise and neighbor
      complaint procedures. Does NOT apply to non-primary-residence or investment STRs.
      Note: AB-1217 is being challenged and interpreted at the city level — some cities
      have updated ordinances to comply while maintaining strong restrictions; verify current
      city-specific status.
    - Los Angeles STR enforcement tightening (2023–2024): LA's Home Sharing Ordinance
      reached full enforcement with Airbnb removing non-compliant listings that lacked
      valid registration numbers. LA also updated its primary-residency verification
      requirements and now cross-references listing permit numbers against its database.
    - San Diego tiered permit changes (2023–2024): San Diego's tiered STR permit system
      created a cap on Tier 2 (non-owner-occupied) permits. Demand far exceeded supply —
      many Tier 2 operators were left without permits and had to cease operations or sell.
    - Airbnb/Vrbo added additional California coverage agreements (2024–2025): Several
      smaller California cities signed new platform collection agreements, reducing the
      number of hosts who must self-remit TOT. Check current coverage list.
    - Callout-amber: "STR regulation in California is among the most actively changing in
      the country. Rules that applied in 2022 may have been superseded. Verify your
      city's current ordinance before each hosting season — not just when you first list."
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - California STR compliance is entirely local — your city or county's website is the
      authoritative source, not this guide. The three things you need before your first
      booking: (1) local STR permit or registration, (2) TOT registration if your platform
      doesn't cover it, and (3) your permit number posted in your listing as most cities
      now require.
    - AB-1217 gave primary-residence owners some protection from outright bans, but strong
      local regulation remains the norm in the state's highest-density markets. Check your
      city's ordinance annually — rules are evolving faster in California than almost anywhere
      else in the country.
```

---

## colorado-short-term-rental-taxes.html

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing the Colorado STR tax situation — no statewide lodging tax but 2.9% state sales tax, home-rule city complexity requiring multiple registrations, Denver primary-residency permit requirement, rapidly tightening ski-country regulations, and the need to verify city-specific rules before listing.
```

---

## cost-segregation-str.html

### `#what-is-cost-segregation` — What is a cost segregation study?

```
TODO: Explain that a cost seg study is conducted by an engineering or accounting firm. They physically inspect the property and classify every component by its IRS asset class and recovery period. The result is a report that reclassifies a portion of the property's cost basis from 27.5-year residential real property to shorter-lived asset categories. Cost of a study: typically $3,000–$15,000 depending on property value and complexity. Most cost-effective above $500,000 property value.
```

### `#depreciation-categories` — Depreciation categories: 5-year, 7-year, 15-year, 27.5-year

```
TODO: Cover each asset class with examples: 5-year (carpeting, appliances, furniture, certain fixtures), 7-year (office furniture and fixtures in some cases), 15-year (land improvements: driveways, fences, landscaping, outdoor lighting, parking areas), 27.5-year (structural components of the building itself). Table showing component → recovery period → example items. Note: land itself is not depreciable.
```

### `#bonus-depreciation` — Bonus depreciation — the accelerator

```
TODO: Cover bonus depreciation under TCJA §168(k). 100% bonus in 2022, 80% in 2023, 60% in 2024, 40% in 2025, 20% in 2026, 0% in 2027 unless Congress acts. Bonus depreciation applies to 5-, 7-, and 15-year property (not 27.5-year). This means: in 2025, 40% of reclassified components can be deducted immediately. Example: $200,000 reclassified as 5-year property → $80,000 bonus depreciation deduction in year one (2025 rates).
```

### `#when-it-makes-sense` — When cost segregation makes sense

```
TODO: Break-even analysis: study costs $5,000–$10,000, generates X in deductions, at a 35% marginal rate saves Y. Generally worth it for properties $500K+. Other factors: are you in a high tax bracket? Do you have non-passive income to offset (STR loophole)? Are you planning to hold long-term (recapture on sale makes it less attractive for short holds)? Callout-navy: "A cost seg study that generates $100,000 in accelerated deductions saves a taxpayer in the 37% bracket $37,000 in federal tax — often 4–7× the study cost."
```

### `#depreciation-recapture-on-sale` — Depreciation recapture — the trade-off

```
TODO: Under §1250, accelerated depreciation on real property above straight-line is recaptured as ordinary income upon sale. Unrecaptured §1250 gain is taxed at a maximum of 25%. If you depreciated $150,000 in accelerated components and later sell, you owe recapture tax on that $150,000 even if you qualify for long-term capital gains rates on the rest of the gain. Cost seg is a timing strategy — it shifts tax liability from now to the future, often a smart trade-off.
```

### `#the-bottom-line` — The bottom line

```
TODO: Summarize: cost seg is a powerful tool for the right investor — high income, STR loophole eligible, planning to hold for several years. It is not a silver bullet; recapture is real and must be planned for. Work with a CPA who has done cost seg before.
```

---

## florida-short-term-rental-taxes.html

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - The three Florida STR obligations every host must address: DBPR license, state sales
      tax registration, and county TDT registration (even if Airbnb collects on your behalf).
    - Florida's preemption law and no-income-tax advantage. Reminder to verify county TDT
      rates annually and maintain DBPR license renewal.
```

---

## furnished-finder-taxes.html

### `#mid-term-rental-tax-rules` — Mid-term rental tax rules —what changes at 30 days

```
TODO: 2–3 paragraphs covering:
    - Definition: "mid-term rental" is not an IRS term — it's industry shorthand for 30+ day stays
      that legally classify as residential leases, not short-term rentals
    - The two key tax differences from STRs: (1) occupancy/lodging tax usually doesn't apply at 30+
      days in most states; (2) landlord-tenant law (not platform rules) governs the relationship
    - Mid-term income still goes on Schedule E just like short-term — same form, same passive-income
      classification, same deduction rules
    - Callout-navy: "The 30-day threshold is a state and local tax line, not a federal income
      tax line — you still owe federal income tax on every dollar of mid-term rental income"
```

### `#schedule-e-for-furnished-finder` — Schedule E for Furnished Finder hosts

```
TODO: 2 paragraphs covering:
    - Schedule E (Form 1040, Part I) is the right form for rental income — passive, no SE tax
    - When does it tip to Schedule C? If you provide substantial services to tenants (daily
      cleaning, linens service, meals) — rare for mid-term hosts, but worth checking
    - Furnished Finder's own positioning as "landlord-tenant" platform (vs AirBnB's "hospitality")
      reinforces Schedule E treatment — no concierge, no nightly turnover service
```

### `#furnished-finder-1099-reporting` — Does Furnished Finder send a 1099?

```
TODO: 2 paragraphs covering:
    - Furnished Finder does NOT process payments — it's a listing platform, not a payment
      processor. Hosts collect rent via Zelle, Venmo, Stripe, check, or direct bank transfer
    - Because no payment processor is involved, no 1099-K is issued by Furnished Finder
    - Your tenants (travel nurse agencies, corporate relocation companies, individual nurses)
      may issue a 1099-MISC or 1099-NEC if they pay $600+ — but most won't bother for
      rental payments (vs. service payments)
    - You are fully responsible for tracking all rental income — no platform safety net
```

### `#what-furnished-finder-hosts-can-deduct` — What Furnished Finder hosts can deduct

```
TODO: 2–3 paragraphs + H3 subsections covering:
    H3: Furniture and appliances — depreciation or Section 179
    - Furniture and appliances used for the rental: 5–7 year depreciation OR Section 179
      immediate expensing (up to limits) — this is often the biggest deduction FF hosts miss
    - Bonus depreciation: 60% in 2024, 40% in 2025 — reduces basis for future years
    H3: Shared expenses (rental-use %)
    - Mortgage interest, property taxes, utilities, insurance, HOA — rental portion
    - If unit is rented 10/12 months, roughly 83% of shared expenses deductible
    H3: Furnished Finder listing fee
    - Annual subscription fee to list on Furnished Finder — 100% deductible
    H3: Depreciation on the structure
    - Same 27.5-year rule as other residential rentals — most hosts skip this entirely
```

### `#the-travel-nurse-tenant-angle` — The travel-nurse tenant angle

```
TODO: 2 paragraphs covering:
    - Travel nurses and healthcare workers are the dominant tenant type on Furnished Finder
    - Their housing stipends come from hospitals or staffing agencies — this is the TENANT's
      income, not yours. You receive rent, which is treated the same regardless of where
      the tenant's money comes from
    - Practical note: travel nurse contracts typically run 13 weeks (about 3 months) — many
      hosts treat this like a 3-month lease. That complicates mid-year mixed-use calculations
      if the host occupies the unit between contracts
    - Some staffing agencies pay rent directly to the host — in that case, get the agency's EIN
      for your records in case of an audit
```

### `#state-occupancy-tax-exemptions` — State occupancy tax exemptions for 30+ day stays

```
TODO: 2 paragraphs covering:
    - Most states exempt rentals of 30+ consecutive days from occupancy/lodging tax
    - List 4–5 states that DO apply occupancy tax regardless of duration (or have lower thresholds)
    - Note that some cities have their own ordinances that differ from state law
    - Callout-amber: "Verify your state and county rules before assuming you're exempt —
      a few jurisdictions apply hotel taxes to all rental lengths"
```

### `#should-furnished-finder-hosts-form-an-llc` — Should Furnished Finder hosts form an LLC?

```
TODO: 2 paragraphs covering:
    - Liability exposure: mid-term tenants have stronger legal rights than STR guests and can
      sue for habitability issues, security deposit disputes, or injury
    - LLC adds a liability barrier between the rental property and your personal assets
    - Mid-term hosts with a standalone unit (separate from primary residence) should strongly
      consider an LLC — same reasons as vacation rental hosts
    - Mortgage clause warning: don't transfer title without checking with lender and attorney
```

### `#common-mistakes` — Common mistakes Furnished Finder hosts make

```
TODO: 4–5 numbered H3 subsections:
    1. Assuming no 1099 = no reporting obligation — income must be reported regardless
    2. Not depreciating furniture (the most unique missed deduction for furnished rentals)
    3. Failing to track rental vs. personal-use days when they use the unit between stays
    4. Treating ALL expenses as 100% deductible when personal use reduces the eligible %
    5. Not using a written lease — mid-term hosts with no lease have weaker audit documentation
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - Furnished Finder is one of the most tax-favorable rental models: Schedule E, no SE tax,
      occupancy-tax exemption in most markets, and strong depreciation opportunities on furnishings
    - Action items: track all rental income manually (no 1099 reminder coming), depreciate
      furniture and the structure, keep a rental-use calendar if you occupy the unit personally,
      and consider a simple lease agreement for every tenant for documentation purposes
```

---

## hawaii-short-term-rental-rules.html

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - Hawaii hosts face the highest combined STR tax rates in the country — 17.75% stacked
      from TAT, county TAT surcharges, and GET. Airbnb handles collection but registration
      remains the host's obligation. Maintain active TAT, GET, and county surcharge filings.
    - The zoning/permit situation on Oahu and Maui is the most restrictive in the country
      for new entrants — verify county permit availability before purchasing or listing.
      Rules continue to evolve in response to Hawaii's housing crisis.
```

---

## hipcamp-host-taxes.html

### `#how-hipcamp-income-is-taxed` — How Hipcamp income is taxed —Schedule E, F, or C?

```
TODO: 2–3 paragraphs covering:
    - Schedule E (Part I): the default for most Hipcamp hosts — you're renting land/space,
      passive rental income, no self-employment tax
    - Schedule F: applies only if the camping is part of an active farming operation and
      the income qualifies as farm income — consult a CPA, this is a fact-intensive determination
      (see IRS Publication 225 for farm income definitions)
    - Schedule C: applies if you provide substantial experiences — guided hikes, horseback tours,
      farm stays with meals/activities that cross into active hospitality
    - Comparison table: E vs F vs C (when it applies, SE tax, what it means for deductions)
    - Note: most casual land-rental Hipcamp hosts are Schedule E
```

### `#does-hipcamp-send-a-1099` — Does Hipcamp send a 1099?

```
TODO: 2 paragraphs covering:
    - Yes — Hipcamp processes payments and issues 1099-K at the federal threshold
      ($2,500 in 2025 gross payments)
    - Hipcamp's payout is net of its host fee (typically 20% of booking value)
    - You owe tax on all rental income (gross) — the 1099 is informational only
    - Keep your own records: Hipcamp's annual earnings summary in the host dashboard
```

### `#land-improvements-and-depreciation` — Land improvements and depreciation

```
TODO: 2–3 paragraphs covering:
    - Key rule: land itself cannot be depreciated. But IMPROVEMENTS to land CAN.
    - Land improvements (gravel pads, tent platforms, fire rings, electrical hookups,
      water connections, pit toilets, fencing specific to the campsite) depreciate over 15 years
    - Contrast with residential structures (27.5 years) — land improvements are faster
    - Callout-green: real example — $10,000 in campsite improvements = ~$667/year in deductions
      for 15 years. Modest but meaningful over time.
    - Glamping structures (yurts, cabins, small structures on a foundation) may qualify as
      residential property at 27.5 years — get a cost segregation study if you have multiple
      structures
```

### `#agricultural-land-and-tax-exemptions` — Agricultural land and tax exemptions

```
TODO: 2–3 paragraphs covering:
    - Most states offer reduced property tax rates for agricultural land (greenbelt laws,
      "ag use" exemptions, current-use taxation)
    - Key risk: if a portion of ag land is rented for camping, assessors may reclassify that
      area as commercial use — losing the ag exemption on that acreage
    - How to protect the exemption: fence off the camping area, keep camping % of total acreage
      small, document the primary agricultural use of the full parcel
    - Callout-amber: "Check with your county assessor BEFORE listing — retroactive reclassification
      can mean back taxes + penalties going back 3–5 years in some states"
    - Note: IRS Publication 225 covers farm income — link in footer
```

### `#conservation-easements-and-hosting` — Conservation easements and hosting income

```
TODO: 2 paragraphs covering:
    - Conservation easements restrict certain uses of land in exchange for tax benefits
    - Camping and recreation may be permitted uses under many easements — but "commercial
      recreation" may not be. Review your specific easement deed before listing.
    - If the easement prohibits commercial activity and you receive payment for camping,
      you could be in breach — which can trigger repayment of past tax benefits
    - Callout-amber: "If your land has a conservation easement, have an attorney review
      the deed before listing on Hipcamp — 'recreational use' and 'commercial recreation'
      are often treated differently"
```

### `#what-hipcamp-hosts-can-deduct` — What Hipcamp hosts can deduct

```
TODO: 2 paragraphs + H3 subsections:
    H3: Direct camping expenses (100% deductible)
    - Hipcamp host fee (20% of booking value) — fully deductible
    - Site maintenance: mowing, gravel replenishment, fire ring maintenance
    - Supplies: firewood, toilet paper for pit toilets, camp lighting, signage
    - Insurance specific to the camping operation
    H3: Land improvements (15-year depreciation)
    - All permanent improvements enumerated above
    H3: Shared expenses if camping is on land used for other purposes
    - If the land is also your primary residence property, deduct the camping-area %
      of shared expenses (property taxes, insurance, utilities)
```

### `#state-and-local-taxes` — State and local taxes on outdoor hosting

```
TODO: 2 paragraphs covering:
    - Occupancy/lodging tax applicability varies widely for camping — many states exempt
      primitive camping but tax glamping and RV sites
    - Hipcamp collects and remits in many jurisdictions — verify in your host dashboard
    - Some states require a separate "campground license" regardless of platform
    - A few states apply sales tax to outdoor recreational admissions — check your state
```

### `#should-hipcamp-hosts-form-an-llc` — Should Hipcamp hosts form an LLC?

```
TODO: 2 paragraphs covering:
    - Guest injury risk on land is significant: uneven terrain, fire hazards, wildlife,
      water access — all create liability exposure
    - An LLC owning the land (or a separate LLC for the camping operation) creates a barrier
      between the camping business and the host's personal assets and primary farm operation
    - Callout-navy: note that property/casualty insurance specific to campground operations
      is equally important — an LLC alone doesn't substitute for adequate coverage
```

### `#common-mistakes` — Common mistakes Hipcamp hosts make

```
TODO: 4–5 numbered H3 subsections:
    1. Not depreciating land improvements (the biggest missed deduction for outdoor hosts)
    2. Assuming camping income is exempt from all taxes — it's not exempt from federal income tax
    3. Not checking with county assessor about ag exemption before listing
    4. Ignoring conservation easement restrictions before taking commercial bookings
    5. Underestimating liability exposure on raw land — minimal insurance or no LLC
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - Hipcamp income is taxable and almost always Schedule E — same basic rules as residential
      rental income but with land-specific deductions most hosts miss entirely
    - Action items: depreciate land improvements, check with county assessor about ag exemption,
      review any conservation easement before listing, verify lodging tax in your Hipcamp dashboard,
      and consider an LLC + campground-specific liability insurance
```

---

## house-hacking-taxes.html

### `#what-is-house-hacking` — What is house hacking?

```
TODO: 2–3 paragraphs covering:
    - Define house hacking: renting one or more units, rooms, or accessory dwelling units (ADUs)
      in a property where the owner also lives. Types: renting a spare bedroom in your primary
      home (short-term via Airbnb or long-term to a tenant), renting a basement apartment or
      in-law suite, renting a detached ADU or garage apartment while living in the main house,
      buying a small multi-family (duplex, triplex) and living in one unit while renting others.
    - Tax treatment varies slightly by structure — key distinction is whether the rented space
      has its own separate utilities and is truly separate.
```

### `#the-allocation-formula` — The allocation formula —rented square footage

```
TODO: 2–3 paragraphs covering:
    - Most common method: rented sq ft ÷ total home sq ft = rental-use percentage.
    - Example: 300 sq ft bedroom in a 1,500 sq ft home = 20% rental use.
    - Apply this percentage to shared home expenses: mortgage interest, property taxes, utilities,
      homeowners insurance, repairs and maintenance. The remaining 80% is personal — deductible
      on Schedule A (mortgage interest, property taxes) or just non-deductible (utilities,
      insurance).
    - For short-term rentals of a room (Airbnb), you may also need a time-based allocation if the
      room is only rented periodically.
    - Callout-navy: a rented space with truly separate utilities (its own electric meter, separate
      entrance) is easier to allocate and argue at audit.
```

### `#what-you-can-deduct` — What you can deduct on Schedule E

```
TODO: 2–3 paragraphs covering:
    - Rental portion of: mortgage interest, property taxes, homeowners insurance, utilities
      (electric, gas, water, internet).
    - 100% deductible without allocation: Airbnb host fee, cleaning fees paid to third parties,
      supplies purchased for the rented space, rental-specific repairs, locks and security for
      the rented unit, advertising costs.
    - Depreciation on the rented portion (see next section).
    - Property management fees if used.
    - Note: for long-term tenants, the same allocations apply but there's typically no platform
      fee to deduct.
```

### `#depreciation-on-rented-portion` — Depreciation on the rented portion

```
TODO: 2–3 paragraphs covering:
    - You may depreciate the portion of the home used for rental purposes.
    - Calculate: (home's cost basis − land value) × rental-use percentage ÷ 27.5 years =
      annual depreciation deduction.
    - Example: $400,000 home, $80,000 land, 20% rental use → $320,000 depreciable basis × 20%
      = $64,000 rental basis ÷ 27.5 = $2,327/year.
    - Furniture and furnishings in the rented space depreciate on 5–7 year schedules (or can be
      expensed under §179).
    - Warning section leading into next H2: this depreciation WILL be recaptured when you sell.
```

### `#121-home-sale-exclusion-impact` — §121 home-sale exclusion and depreciation recapture

```
TODO: 2–3 paragraphs covering:
    - The §121 exclusion allows homeowners to exclude up to $250,000 ($500,000 MFJ) of capital
      gain on the sale of a primary residence — but depreciation taken on the rental portion
      does NOT qualify for this exclusion.
    - Depreciation recapture: all depreciation claimed on the rental portion over the years is
      taxed as ordinary income at up to 25% (§1250 unrecaptured gain) when you sell, regardless
      of the §121 exclusion.
    - Example: took $10,000 of depreciation over 4 years → owe recapture tax on $10,000 at
      ordinary income rates at sale.
    - However: there is no capital gains tax on the rental portion of appreciation (beyond the
      recapture), as long as you meet the use-and-ownership tests.
    - Callout-amber: "Before you sell, ask your CPA to calculate your accumulated depreciation
      recapture. Surprise recapture bills are a common oversight for house hackers."
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - House hacking creates real tax benefits — deductions, depreciation, and Schedule E passive
      income treatment — but requires tracking from day one.
    - The allocation ratio, the depreciation schedule, and the §121 recapture exposure all need
      to be documented and recalculated at sale.
    - Don't start depreciating without understanding what it means when you sell.
```

---

## mixed-use-rental-taxes.html

### `#what-is-mixed-use` — What is a mixed-use rental property?

```
TODO: 2–3 paragraphs covering:
    - Define a mixed-use rental as any property the owner both rents to guests at fair market
      value AND personally uses during the year. Examples: renting your beach house for 3 months
      and vacationing there yourself for 2 weeks; listing your home on Airbnb while keeping some
      weeks blocked for personal use; a ski cabin you both rent and use.
    - Distinct from house hacking (renting a portion while living in another portion — that's a
      different allocation).
    - The tax rules are governed primarily by IRC §280A. Key threshold: the "vacation home" rule
      — if personal use exceeds 14 days OR 10% of rental days (whichever is greater), the
      property is classified as a personal residence with restricted loss deductions.
```

### `#two-allocation-methods` — The two allocation methods —and why they differ

```
TODO: 2–3 paragraphs covering:
    - IRS method (Rev. Rul. 75-14): allocate mortgage interest and property taxes by total days
      in the year. Formula: rental days ÷ 365. Example: 90 rental days → 90/365 = 24.7%
      deductible on Schedule E; remaining 75.3% on Schedule A (if itemizing).
    - Tax Court method (Bolton v. Commissioner): allocate by actual total days of use. Formula:
      rental days ÷ (rental days + personal use days). Example: 90 rental days + 20 personal
      days = 110 total use days → 90/110 = 81.8% deductible on Schedule E; remaining 18.2%
      on Schedule A.
    - The difference is significant: the Tax Court method produces a higher rental percentage
      for Schedule E and leaves less trapped as a Schedule A itemized deduction.
    - The IRS officially disagrees with the Tax Court method but courts have consistently upheld
      it.
```

### `#expense-categories-and-treatment` — Expense categories and how each is treated

```
TODO: 2–3 paragraphs covering:
    - Three tiers of deductions:
      Tier 1 — always fully deductible regardless of rental use percentage (not applicable here
        — these apply to vacation home rules).
      Tier 2 — allocated between personal and rental use: mortgage interest, property taxes,
        insurance, utilities, depreciation, repairs, maintenance. Apply the rental-use ratio.
      Tier 3 — rental-specific costs that are 100% deductible (no allocation): Airbnb host fee,
        booking platform costs, rental-specific advertising, property management fees for the
        rental periods, direct cleaning costs attributable to rental stays.
```

### `#passive-activity-loss-limits` — Passive activity loss limits for mixed-use rentals

```
TODO: 2–3 paragraphs covering:
    - If the property generates a tax loss (after all deductions including depreciation), the
      passive activity loss rules under IRC §469 limit how much of that loss you can deduct in
      the current year against non-rental income.
    - The $25,000 passive loss allowance for "active participants": available if you actively
      participate (make management decisions) and your MAGI is under $100K (phases out at $150K).
    - Losses above the allowance carry forward to future years or until you sell.
    - Mixed-use properties: personal use above the threshold can further limit deductible losses.
    - Callout-amber: "Excess deductions that exceed rental income are suspended when personal use
      is too high. They don't disappear — they carry forward — but they can't offset your W-2
      this year."
```

### `#14-day-personal-use-rule` — When personal use converts to a "vacation home"

```
TODO: 2–3 paragraphs covering:
    - The personal use threshold: if you use the property for personal purposes more than 14 days
      OR more than 10% of total rental days (whichever is greater), it becomes a "vacation home"
      or "personal residence" under §280A.
    - Consequences: deductible rental expenses cannot exceed rental gross income — you cannot
      create a tax loss from the rental. Expenses in excess of income are not deductible in the
      current year (though mortgage interest and property taxes remain deductible on Schedule A
      within the personal-use percentage).
    - Cross-link to airbnb-14-day-rule for the separate question of the §280A(g) exclusion for
      short stays ≤14 rental days.
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - For mixed-use properties, the allocation method matters — the Tax Court method is more
      favorable but requires being prepared to defend it.
    - Minimize personal use days to stay under the vacation-home threshold if you want to deduct
      losses.
    - Track personal vs rental days meticulously throughout the year.
```

---

## neighbor-storage-host-taxes.html

### `#why-storage-income-is-schedule-e` — Why storage rental income is Schedule E —not Schedule C

```
TODO: 2–3 paragraphs covering:
    - Renting space (garage, driveway, basement, spare room) is passive rental income under
      IRC Section 61 and reported on Schedule E, Part I
    - No self-employment tax because you're providing space, not labor or services
    - When does it cross to Schedule C? If you actively manage and handle renter's belongings
      (loading, organizing, transport), you've created a storage service — Schedule C territory.
      Simply renting the space while the renter handles everything = Schedule E.
    - Comparison table: Schedule E vs C for storage (when each applies, SE tax, key examples)
```

### `#does-neighbor-send-a-1099` — Does Neighbor send a 1099?

```
TODO: 2 paragraphs covering:
    - Yes — Neighbor processes payments and issues 1099-K at the federal $2,500 threshold for 2025
    - Neighbor's service fee (4.9% + $0.30 per transaction for the standard plan) is deducted
      from payouts and is a deductible rental expense
    - You receive net payouts but owe tax on gross rental amounts (before Neighbor's fee)
    - Keep Neighbor's annual earnings summary as backup documentation for your records
```

### `#what-storage-hosts-can-deduct` — What storage hosts can deduct

```
TODO: 2–3 paragraphs + H3 subsections:
    H3: Neighbor service fee — 100% deductible
    - Neighbor's transaction fee (4.9% + $0.30) is a direct rental expense, fully deductible
    H3: Space-proportionate shared expenses
    - Calculate rental-use percentage: storage sq ft ÷ total home sq ft
    - Apply that % to: homeowner's insurance, property taxes (owner), rent (renter),
      utilities (if electricity/heat shared with the storage area), internet (if applicable)
    - Example: 200 sq ft garage rented in a 2,000 sq ft home = 10% of shared expenses deductible
    H3: Storage-specific direct expenses
    - Locks, security cameras, lighting installed for the storage tenant
    - Repairs specific to the storage area (garage door opener, shelving units provided)
    - These are 100% deductible if exclusively used for the rental area
```

### `#depreciation-for-storage-structures` — Depreciation for storage structures

```
TODO: 2 paragraphs covering:
    H3: Attached structures (garage, basement as part of the home)
    - If the storage area is part of your primary residence, depreciate the rental-use %
      of the structure over 27.5 years
    - Example: a $300,000 home with a 200 sq ft storage garage out of 2,000 sq ft total:
      rental % = 10%. Depreciable basis = $300,000 × 80% (structure, not land) × 10% = $24,000.
      Annual depreciation = $24,000 / 27.5 = ~$873/year.
    H3: Detached storage structures (standalone shed, standalone garage)
    - If the storage structure is a standalone building separate from your home,
      it depreciates as a commercial/residential rental property — also 27.5 or 39 years
      depending on how it's classified
    - Callout-amber: depreciation recapture applies when you sell the property — same 25% rate as
      residential rental properties
```

### `#mixed-use-garage-and-home-space` — Mixed-use garage and home space rules

```
TODO: 2 paragraphs covering:
    - The most common Neighbor scenario: a garage that the host also uses for parking or
      personal storage alongside the rented portion
    - You can only deduct the rented portion — if you rent half the garage, deduct 50% of
      garage-specific expenses (not the whole house %)
    - Document: take photos of the rented space, note dimensions, keep the Neighbor listing
      as evidence of the rental arrangement
    - Callout-navy: if a renter has exclusive access to a clearly demarcated area, the
      deduction is cleaner. Shared-access storage is harder to defend in an audit.
```

### `#state-and-local-taxes` — State and local taxes on storage rentals

```
TODO: 2 paragraphs covering:
    - Most states do not apply occupancy or lodging tax to storage rentals (storage is not
      a transient lodging use)
    - Some states apply sales tax to self-storage — whether peer-to-peer storage qualifies
      is a gray area in several states (check your state revenue department)
    - Neighbor collects sales tax where required — verify in your host dashboard
    - If you operate multiple storage units at scale, you may cross into "commercial storage
      business" classification in some states — consult a CPA
```

### `#should-storage-hosts-form-an-llc` — Should storage hosts form an LLC?

```
TODO: 2 paragraphs covering:
    - Liability risk: a renter whose stored goods are damaged, stolen, or accessed without
      permission could sue the host. An LLC limits personal exposure.
    - Single-garage hosts: the formation cost ($50–500+) may exceed the liability benefit
      for low-revenue storage. Adequate homeowner's insurance (with a storage rider) may
      be sufficient for small-scale hosts.
    - Multi-unit operators or hosts with a standalone storage structure: LLC makes more sense —
      the structure represents a significant asset and the liability surface is larger.
    - Northwest Registered Agent keeps your home address off filings — important if you don't
      want tenants knowing your personal address.
```

### `#common-mistakes` — Common mistakes storage hosts make

```
TODO: 4–5 numbered H3 subsections:
    1. Not reporting income because "it's just a garage" — all rental income is taxable
    2. Deducting 100% of home expenses instead of the storage-area percentage only
    3. Forgetting to deduct Neighbor's service fee as a rental expense
    4. Not depreciating the storage structure or the rental-use % of the home
    5. Commingling personal stored items with renter's items — muddies the mixed-use calculation
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - Neighbor storage income is one of the simplest rental tax situations: Schedule E,
      space-percentage deductions, no SE tax. The main work is calculating the right
      rental-use percentage and depreciating the structure.
    - Action items: calculate your storage sq ft %, deduct Neighbor's fee, deduct space-
      proportionate shared expenses, consider depreciation on the structure, and ensure
      homeowner's insurance covers tenant-stored property (or add a rider)
```

---

## new-york-short-term-rental-rules.html

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - For NYC hosts: the key requirements under Local Law 18, the registration process, and
      the hosted-only rule. For compliant hosts, Airbnb handles hotel taxes.
    - For upstate/outside-NYC hosts: state 4% hotel/motel tax plus county add-ons; verify
      platform coverage and file ST-809 if not covered.
```

---

## quarterly-taxes-for-airbnb-hosts.html

### `#who-needs-to-pay` — Who needs to make quarterly estimated payments

```
TODO: 2–3 paragraphs covering:
    - Cover the $1,000 threshold rule: if you expect to owe $1,000 or more in federal income
      tax from Airbnb income (after withholding from any W-2 job), you are required to make
      quarterly estimated payments.
    - Airbnb does not withhold any federal or state income tax from payouts — it's completely
      unwithheld income.
    - Even if you have a day job with tax withheld, significant Airbnb income can create an
      underpayment situation if your W-2 withholding doesn't cover the additional liability.
    - Callout-amber: "The most common mistake new hosts make: waiting until April to deal with
      Airbnb taxes. By then, they've missed 3 of 4 quarterly deadlines and owe both back taxes
      and underpayment penalties."
```

### `#quarterly-deadlines` — The 2025 quarterly deadlines

```
TODO: 2–3 paragraphs covering:
    - Q1 (January–March income): due April 15, 2026.
      Q2 (April–May income): due June 16, 2026.
      Q3 (June–August income): due September 15, 2026.
      Q4 (September–December income): due January 15, 2027.
    - Note: "quarters" are not equal in duration — Q2 covers only 2 months.
    - Callout-navy: include a simple table showing Q1–Q4 coverage periods and due dates for
      2025 income.
    - Also note: if the due date falls on a weekend or holiday, it shifts to the next
      business day.
```

### `#how-to-calculate-your-payment` — How to calculate each quarterly payment

```
TODO: 2–3 paragraphs covering:
    - Two approaches:
      (1) Annualized income method (Form 2210, Schedule AI): estimate your total Airbnb income
          for the year, subtract expenses, apply your marginal tax rate. Divide by 4 for equal
          quarterly payments. More accurate but requires estimating annual income mid-year.
      (2) Safe harbor method (simpler, described in next section): pay 25% of last year's
          total tax each quarter.
    - Also cover: how to actually pay — IRS Direct Pay at irs.gov/payments, EFTPS (Electronic
      Federal Tax Payment System), or check mailed with Form 1040-ES voucher.
    - Many hosts also need to pay state estimated taxes — check your state's revenue department
      for similar quarterly requirements.
```

### `#the-safe-harbor-rule` — The safe harbor rule —the simplest way to avoid penalties

```
TODO: 2–3 paragraphs covering:
    - The safe harbor rule: pay 100% of your prior year's total tax liability (from line 24 of
      your Form 1040) in equal quarterly installments. If your prior-year AGI exceeded
      $150,000, the threshold is 110%.
    - If you pay at least this amount across four equal quarterly payments, the IRS cannot
      charge an underpayment penalty — even if you end up owing significantly more when
      you file.
    - Callout-green: "The safe harbor is the easiest path for most Airbnb hosts with variable
      income. You don't need to predict this year's rental income accurately — just look at
      last year's tax return and divide line 24 by 4."
    - Note the limitation: the safe harbor eliminates underpayment penalties but you still owe
      the balance due at filing time.
```

### `#underpayment-penalty` — The underpayment penalty —what it costs to miss

```
TODO: 2–3 paragraphs covering:
    - IRS Form 2210 computes the underpayment penalty. The penalty rate is the federal
      short-term rate + 3 percentage points (approximately 7–8% per year as of 2025).
    - It's calculated per-quarter: if you underpaid Q1, interest accumulates from Q1's due
      date through filing. The penalty is not huge for most casual hosts — missing $1,000 in
      quarterly payments for one quarter might cost $15–20 in penalty. But the math adds up
      across all four quarters, and the administrative burden of fixing it is more annoying
      than the dollar amount.
    - Callout-navy: "The underpayment penalty is an interest charge, not a fine. Paying late
      hurts but it's rarely catastrophic for most hosts. The real risk is a large surprise
      bill in April when you've already spent the money."
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - Set up quarterly payments from your first year of Airbnb income. Use the safe harbor
      method if income is unpredictable — look up last year's tax bill and divide by 4. Pay
      via IRS Direct Pay online in 10 minutes.
    - And don't forget state estimated taxes if your state has an income tax.
```

---

## rv-rental-host-taxes.html

### `#rv-rental-schedule-c` — RV rental income is Schedule C —not Schedule E

```
TODO: 2–3 paragraphs covering:
    - Same rationale as Turo: vehicle rental is an active business, not passive real estate.
      IRS treats peer-to-peer vehicle rental as Schedule C.
    - Self-employment tax (15.3% on net profit) applies. But all ordinary and necessary
      business expenses are deductible — potentially making net income much lower than gross.
    - Contrast with Airbnb/Vrbo hosts who get Schedule E treatment. RV hosts who also own
      a vacation property on Airbnb file both Schedule C (RV) and Schedule E (property).
    - Callout-navy: "Some RV hosts have argued their RV constitutes a 'dwelling unit' and
      should be Schedule E. The IRS has not clearly ruled on this for peer-to-peer rental
      platforms. Most CPAs default to Schedule C for safety."
```

### `#rvshare-vs-outdoorsy-1099` — RVshare vs Outdoorsy —1099 reporting differences

```
TODO: 2 paragraphs covering:
    - Both platforms send 1099-K at the federal threshold ($2,500 in 2025)
    - If you list on both, you receive two separate 1099-Ks — combine income from both on
      the same Schedule C (one business, two income sources)
    - Timing difference: RVshare and Outdoorsy may have slightly different payout schedules
      and 1099 issue dates — check your dashboard on each
    - Commission structures differ: RVshare ~25% + insurance fee; Outdoorsy ~20–35% +
      protection fee. Both fees are deductible as business expenses.
```

### `#rv-listed-property-depreciation` — RV depreciation —the listed-property rules

```
TODO: 2–3 paragraphs covering:
    - "Listed property" definition: assets that can be easily used for personal purposes —
      cars, computers, entertainment equipment, and certain vehicles including RVs
    - The 50% business-use threshold: if your RV is used for business (rental) more than 50%
      of total use, you can use MACRS accelerated depreciation. If business use drops to 50%
      or below in any year, you must switch to straight-line and recapture the difference.
    - MACRS recovery period for RVs: typically 5 years (passenger vehicles) or 7 years
      depending on classification and weight — verify with a CPA
    - Section 179 and bonus depreciation: may apply to RVs in the first year if business use
      exceeds 50%, subject to limits. Luxury auto caps don't typically apply to larger RVs.
    - Callout-amber: "If you personally vacation in your RV and also rent it, track days
      carefully — a bad year of personal use can cost you previously claimed depreciation"
```

### `#personal-use-and-the-50-percent-rule` — Personal use and the 50% rule

```
TODO: 2 paragraphs covering:
    - Practical tracking: keep a log of rental days (via platform calendar) + personal-use days
    - Business-use % = rental days / (rental days + personal-use days)
    - All deductible expenses (depreciation, insurance, maintenance, fuel for delivery) are
      prorated by this business-use %
    - Example: RV rented 120 days/year, personally used 60 days/year = 67% business use.
      $50,000 RV × 67% = $33,500 depreciable basis. Still above 50% threshold.
    - Callout-amber: what happens when personal use is HIGH — full example of dropping below
      50% and losing accelerated depreciation
```

### `#what-rv-hosts-can-deduct` — What RV rental hosts can deduct

```
TODO: 2 paragraphs + H3 subsections:
    H3: Direct rental expenses (100% deductible, or % of business use)
    - Platform commission (RVshare/Outdoorsy fees) — 100% deductible
    - RV-specific insurance for the rental period
    - Maintenance and repairs: oil changes, tires, HVAC, appliance repairs within the RV
    - Cleaning between rentals: supplies or cleaning service
    - Roadside assistance plans
    - Delivery/pickup mileage (if you deliver to renters)
    H3: Depreciation (% of business use)
    - MACRS on the RV structure/chassis
    - Separately depreciable add-ons: slide-out upgrades, solar panels, generator
    H3: What you cannot deduct
    - Personal-use portion of any expense
    - Loan principal (only interest portion is deductible)
```

### `#state-and-local-taxes` — State and local taxes on RV rentals

```
TODO: 2 paragraphs covering:
    - Many states impose vehicle rental taxes on peer-to-peer RV rentals — similar to car rental
    - RVshare and Outdoorsy collect and remit in some states; verify in platform dashboard
    - Some states distinguish between "motorized" (taxable) and "towable" (sometimes exempt) RVs
    - Check whether your state requires a vehicle rental dealer license for multi-RV operations
```

### `#should-rv-hosts-form-an-llc` — Should RV rental hosts form an LLC?

```
TODO: 2 paragraphs covering:
    - Guest injury inside an RV, road accident, or property damage creates significant liability
    - An LLC creates a barrier between the RV business and personal assets
    - Multi-RV operators (2+ units) have a clear case; single-RV owners should weigh
      formation costs vs. liability exposure
    - Note: retitling the RV in the LLC name requires updating registration and insurance
```

### `#common-mistakes` — Common mistakes RV hosts make

```
TODO: 4–5 numbered H3 subsections:
    1. Filing on Schedule E instead of Schedule C
    2. Not tracking personal vs. rental use days — the listed-property rules require a log
    3. Assuming depreciation is always available — the 50% threshold means personal use matters
    4. Not deducting platform commissions from both RVshare and Outdoorsy
    5. Not carrying commercial RV rental insurance separate from personal coverage
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - RV rental is taxed like a vehicle-rental business (Schedule C, SE tax) not like
      real estate (Schedule E, no SE tax) — a distinction most new hosts get wrong
    - Action items: track rental vs. personal-use days from day one, depreciate the RV
      (stay above 50% business use), deduct platform commissions from both platforms,
      get commercial RV insurance, and consider an LLC if operating more than one unit
```

---

## schedule-c-vs-schedule-e-str.html

### `#schedule-e-the-default` — Schedule E: the default for most STR hosts

```
TODO: Cover why rental income is ordinarily passive (Schedule E, Part I). No SE tax. Losses subject to passive activity rules (PAL) — generally limited to $25K/year for active participants with MAGI under $100K, phasing out at $150K. Most Airbnb and Vrbo hosts fall here. IRS treats providing a dwelling as passive by default unless substantial services are involved.
```

### `#when-schedule-c-applies` — When Schedule C applies — the 7-day and services tests

```
TODO: Cover the two conditions that push income to Schedule C: (1) average rental period ≤7 days (IRS Reg. §1.469-1T(e)(3)) making the activity a "trade or business," and (2) the host provides "substantial services" comparable to a hotel. Both conditions together typically signal Schedule C. Average period = total rental days ÷ number of separate rentals during the year.
```

### `#what-counts-as-substantial-services` — What counts as "substantial services"

```
TODO: Cover what the IRS considers substantial services vs incidental services. Substantial: daily maid service, meals, guided tours, concierge, transportation. Not substantial (basic amenities): one-time cleaning between guests, furnishings, internet, cable, a welcome basket, self-check-in. Analogy: if the host is acting more like a hotel than a landlord, Schedule C applies. Callout-amber: "Providing self-service check-in and a clean space does not create a hotel-like service level. Most Airbnb hosts are NOT running a hotel."
```

### `#the-se-tax-impact` — The SE tax cost — 15.3% more on every dollar of profit

```
TODO: Explain SE tax: 12.4% Social Security + 2.9% Medicare on net Schedule C income. On $30,000 net profit, SE tax = $4,239 (after the employer-equivalent deduction). The deduction for half of SE tax reduces adjusted gross income. Compare: Schedule E host with same income owes $0 in SE tax. Callout-amber with break-even table showing the difference.
```

### `#material-participation-str-loophole` — Material participation and the STR loophole

```
TODO: Brief intro to the non-passive loss strategy for hosts who materially participate in STR with ≤7-day average stays. Even on Schedule E, these losses may be non-passive if the host meets one of the 7 material participation tests. Losses can then offset W-2 income. Cross-link to short-term-rental-loophole article.
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 paragraphs: (1) most hosts safely on Schedule E — keep it that way by not adding hotel-like services; (2) if growing into a services-heavy operation, factor SE tax into pricing and consider S-Corp election above ~$80K net profit.
```

---

## short-term-rental-loophole.html

### `#what-is-the-str-loophole` — What is the STR loophole?

```
TODO: Explain the passive activity loss (PAL) rules under IRC §469. Normally, rental losses are passive and can only offset passive income (with a $25K exception for active participants with MAGI under $100K). The "loophole": a short-term rental with an average stay of 7 days or fewer is classified as a trade or business activity under IRS Reg. §1.469-1T(e)(3) — not a rental activity. If the taxpayer also materially participates in that business, the losses become non-passive and offset any income.
```

### `#the-7-day-average-test` — The 7-day average rental period test

```
TODO: Explain how to calculate average rental period: total rental days ÷ number of separate rental agreements during the year. Example: 20 bookings totaling 100 rental days = 5-day average → qualifies. 10 bookings totaling 100 days = 10-day average → does NOT qualify. If you have both short-stay and long-stay bookings on the same property, the blended average determines classification. Cross-platform bookings (Airbnb + Vrbo) are combined.
```

### `#material-participation-tests` — The 7 material participation tests

```
TODO: List all 7 IRS material participation tests from Reg. §1.469-5T. The most commonly used for STR: (1) more than 500 hours during the year, (2) substantially all participation in the activity, (3) more than 100 hours and more than any other participant, (5) five of the last 10 years. Callout-amber: document everything — time logs, receipts, communications — because the IRS will ask for it. The 500-hour test is the clearest threshold to hit.
```

### `#how-the-losses-are-generated` — How the losses are generated — depreciation and cost segregation

```
TODO: Most STR investors don't lose money in cash — they generate paper losses through depreciation. Standard 27.5-year straight-line depreciation on residential property creates annual deductions even in profitable years. Cost segregation accelerates that by front-loading 5–15-year component depreciation. Bonus depreciation (80% in 2023, 60% in 2024, 40% in 2025) allows immediate expensing of qualifying components. A $500K property with a cost seg study might generate $100K+ in year-one paper losses.
```

### `#risks-and-audit-flags` — Risks, audit flags, and what the IRS looks for

```
TODO: IRS has specifically flagged STR loophole strategies in recent years. Audit risk factors: large losses against high W-2 income, first-year large depreciation deductions, insufficient documentation of material participation hours, property that is also used personally. Callout-amber: if audited, you must produce contemporaneous time logs (not reconstructed after the fact). Work with a CPA who specializes in real estate taxation.
```

### `#the-bottom-line` — The bottom line

```
TODO: Summarize who this strategy is for (high-W-2 earners who can materially participate, willing to invest in cost seg and professional tax help). Who it's not for (passive investors, part-time hosts who can't hit 500 hours). The strategy is real and legal but requires ongoing documentation and a qualified CPA.
```

---

## str-business-structure.html

### `#sole-proprietor-default` — The default: sole proprietor on Schedule E

```
TODO: 2–3 paragraphs covering:
    - Most Airbnb hosts never form a business entity — they file as sole proprietors, report
      income on Schedule E, and pay no SE tax. This is the correct and simplest approach for
      most hosts.
    - Sole proprietorship requires no formation paperwork, no state filing fees, no separate
      bank account (though recommended), and no annual reports. The host personally owns the
      property and is personally liable for any claims.
    - Callout-navy: "The sole proprietorship doesn't mean you're doing anything wrong — the
      vast majority of Schedule E rental hosts operate this way. The question is whether your
      liability exposure or income level warrants a more formal structure."
```

### `#llc-for-liability-protection` — LLC for liability protection —what it actually does

```
TODO: 2–3 paragraphs covering:
    - An LLC (limited liability company) is a pass-through entity — income and losses still
      flow to your personal return on Schedule E. The LLC itself doesn't change your federal
      tax treatment for passive rental income.
    - What it does provide: liability protection — if a guest is injured on the property and
      sues, your personal assets (other home, savings, car) are shielded if the LLC is properly
      maintained. Address privacy — many states allow the registered agent's address to appear
      on public filings instead of your home address. Clean bookkeeping — a dedicated LLC bank
      account and credit card create clean expense records.
    - Annual cost: $50–$800/year in state LLC fees depending on the state.
```

### `#llc-tax-treatment` — How an LLC is taxed —no automatic tax savings

```
TODO: 2–3 paragraphs covering:
    - A single-member LLC is a "disregarded entity" for tax purposes — the IRS ignores it and
      taxes the owner directly. For rental income, this means you still file Schedule E, still
      use the same passive activity rules, and still owe no SE tax (assuming Schedule E applies).
    - The LLC does not save self-employment tax because Schedule E rental income wasn't subject
      to SE tax in the first place.
    - Multi-member LLCs are taxed as partnerships (Form 1065) with K-1s to each member.
    - Callout-amber: "Don't let anyone sell you an LLC by promising tax savings on passive
      rental income. The LLC is a liability and privacy tool for most STR hosts — not a
      tax tool."
```

### `#s-corp-election` — S-Corp election —when it actually saves money

```
TODO: 2–3 paragraphs covering:
    - An S-Corp election (filed on Form 2553) converts a regular LLC to S-Corp tax status.
      The owner-employee pays themselves a "reasonable salary" (subject to payroll taxes) and
      takes the remainder as a distribution (not subject to SE tax or payroll taxes).
    - This only saves money if: (1) you're filing Schedule C (active STR with services — the
      typical Schedule E host has nothing to save), and (2) net profit consistently exceeds
      $80,000–$100,000, enough to justify payroll administration costs (~$1,500–$3,000/year).
    - Self-rental complications: you cannot be both the STR property owner and pay yourself
      rent from your own LLC in most structures — consult a CPA.
    - Callout-amber: "An S-Corp election on a Schedule E passive rental saves nothing. It's
      only relevant on Schedule C active STR income."
```

### `#multi-property-considerations` — Multi-property considerations

```
TODO: 2–3 paragraphs covering:
    - Options: (1) One LLC per property — maximum liability isolation between properties; if
      one property has a claim, it doesn't touch the other. Higher annual state fees.
      (2) One holding LLC with all properties inside — simpler administration, lower fees, but
      cross-liability if the LLC isn't structured carefully.
      (3) A series LLC (available in some states) — a single LLC with internal "series" that
      provide isolation between properties.
    - State fees vary significantly: California charges $800/year per LLC; Wyoming, Delaware,
      New Mexico charge $50–$100.
    - For hosts with multiple properties, the per-property fee structure should factor into
      the decision.
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - For a single passive rental on Schedule E, an LLC is a liability tool, not a tax tool.
      Form one if the liability exposure from guests concerns you, or if address privacy
      matters. Don't form one expecting tax savings on Schedule E income.
    - For Schedule C active STR operators netting $80K+, an S-Corp election is worth a
      conversation with your CPA.
```

---

## tennessee-short-term-rental-taxes.html

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing the Tennessee STR tax situation — no state income tax advantage (fully eliminated 2022), 7% state sales tax plus local add-ons, Nashville's separate Metro HOT registration requirement, Sevier County's active enforcement, and the 2023 STR preemption law limiting city bans while leaving local permit requirements intact.
```

---

## texas-short-term-rental-taxes.html

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing the Texas STR tax situation — no state income tax advantage, multi-layer HOT system requiring separate state + city registrations, Austin permit complexity, and the need to verify city-specific rules before listing.
```

---

## turo-host-taxes.html

### `#turo-schedule-c-not-schedule-e` — Turo is Schedule C —not Schedule E

```
TODO: 2–3 paragraphs covering:
    - The critical distinction: Schedule E is for real estate rental (passive income, no SE tax).
      Schedule C is for business income (active, 15.3% SE tax).
    - Vehicle rental is classified as an active business — the IRS views renting a car as a
      commercial activity, not passive income from an asset.
    - What this means practically: SE tax (15.3% on net profit) applies. But so do all ordinary
      and necessary business expense deductions — potentially making net taxable income
      much lower than gross earnings.
    - Comparison table: Schedule C vs Schedule E (form, SE tax, deductions, who it applies to)
    - Note: some Turo hosts have argued Schedule E based on their specific situation — this is a
      minority position not supported by current IRS guidance. Consult a CPA if your situation
      is unusual.
```

### `#does-turo-send-a-1099` — Does Turo send a 1099?

```
TODO: 2 paragraphs covering:
    - Yes — Turo sends a 1099-K at the federal $2,500 gross threshold for 2025
    - The 1099-K reflects gross booking amounts before Turo's host protection fee/commission
      (typically 15–40% depending on protection plan chosen)
    - Deduct Turo's fee as a business expense — report gross income, then deduct fees
    - Keep your own earnings records from the Turo host dashboard as backup documentation
```

### `#depreciation-vs-mileage-the-key-decision` — Depreciation vs mileage —the decision you can't undo

```
TODO: 3–4 paragraphs covering:
    - Two methods for deducting vehicle costs:
      (1) Actual expense method: depreciation (MACRS 5-year for passenger vehicles) +
          actual insurance, maintenance, gas, cleaning — all prorated to Turo-use %
      (2) Standard mileage rate ($0.70/mile in 2025) for miles driven for Turo business
          (pickup/dropoff, maintenance runs) — simpler but often lower
    - The irreversibility: once you use actual expenses + depreciation in year 1, you
      cannot switch to standard mileage for that vehicle. The reverse is also restricted.
    - Which is better? For a dedicated Turo-only car, actual expense / depreciation almost
      always wins. For a car you also use personally, the math gets more complicated.
    - Callout-amber: "This is one decision worth paying a CPA for — the first-year choice
      locks in your method for the life of that vehicle"
    - Section 179 / bonus depreciation for new Turo vehicles — you may be able to deduct
      the full vehicle cost in year one (subject to limits and luxury auto caps)
```

### `#what-turo-hosts-can-deduct` — What Turo hosts can deduct

```
TODO: 2 paragraphs + H3 subsections:
    H3: Under actual expense method
    - Depreciation (5-year MACRS for passenger vehicles; luxury auto limits apply)
    - Turo commission/host fee (15–40% of booking)
    - Insurance for the rental periods
    - Maintenance, oil changes, tires (% of rental use)
    - Car washes and detailing between rentals
    - Roadside assistance plans
    H3: Under standard mileage
    - IRS rate × business miles (pickup, dropoff, maintenance trips)
    - Turo fees and insurance still deductible separately
    - Interest on car loan (not principal) still deductible separately under either method
    H3: What you CANNOT deduct
    - Personal-use miles under standard mileage
    - The portion of actual expenses attributable to personal use
```

### `#turo-protection-plans-and-taxes` — Turo protection plans and taxes

```
TODO: 1–2 paragraphs covering:
    - Turo offers 60/75/90 protection plans — the host receives different % of the booking
      depending on plan chosen. The higher-protection plans (60) pay less to the host.
    - For tax purposes: the gross booking amount is income; the Turo fee (which varies by plan)
      is a deductible business expense. Net is the same regardless of plan.
    - Callout-navy: note that Turo's "protection" is NOT third-party insurance — it's Turo's
      own product. Hosts should understand whether they need separate commercial auto insurance
      (most personal auto policies exclude commercial vehicle use)
```

### `#state-and-local-taxes` — State and local vehicle rental taxes

```
TODO: 2 paragraphs covering:
    - Many states impose vehicle rental taxes (separate from income tax) on peer-to-peer
      car rentals — typically 6–11%
    - Turo collects and remits vehicle rental taxes in many but not all jurisdictions
    - Some states (e.g., California) have specific peer-to-peer car rental tax laws;
      others apply standard vehicle rental taxes; some have no specific rule
    - Check Turo's help center for your state's current status — this changes frequently
```

### `#should-turo-hosts-form-an-llc` — Should Turo hosts form an LLC?

```
TODO: 2 paragraphs covering:
    - A guest who causes an accident in your car, gets injured, or has a dispute could
      expose you to personal liability — an LLC creates a barrier
    - Turo's protection plan is NOT a substitute for an LLC — the plan covers Turo's liability,
      not necessarily yours in all scenarios
    - Multi-car Turo hosts operating a fleet have the clearest case for an LLC (and potentially
      an S-Corp election once net profit exceeds ~$40K)
    - Note: you'll likely need to re-title the vehicles in the LLC name — verify insurance
      implications with your provider before doing so
```

### `#common-mistakes` — Common mistakes Turo hosts make

```
TODO: 4–5 numbered H3 subsections:
    1. Filing on Schedule E instead of Schedule C (wrong form — SE tax and deductions both differ)
    2. Using standard mileage in year 1 for a high-value car where depreciation would be far larger
    3. Forgetting to track actual Turo-use % vs personal-use % when the car is used for both
    4. Not deducting the Turo commission as a business expense
    5. Relying on Turo's protection plan as insurance — not maintaining separate commercial coverage
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - Turo is fundamentally different from real estate STRs: Schedule C, SE tax, vehicle
      depreciation rules, and the irreversible method election make year-one planning critical
    - Action items: decide on actual expense vs mileage method before your first tax year ends,
      track Turo-use vs personal-use % meticulously, deduct all platform fees, consider an LLC
      if operating more than one vehicle, and get commercial auto insurance coverage
```

---

## vrbo-host-taxes.html

### `#how-vrbo-reports-your-income` — How Vrbo reports your income —1099-K rules

```
TODO: 2–3 paragraphs covering:
    - Federal 1099-K threshold for 2025: $2,500 in gross payments (same timeline as Airbnb, heading to $600)
    - Key distinction: Vrbo reports the FULL guest-facing payment (booking subtotal + cleaning fee +
      taxes collected on your behalf), NOT your net payout after Vrbo's host fee
    - Practical reconciliation: Vrbo's "Gross Earnings" vs "Net Payouts" reports in dashboard;
      how to reconcile the 1099-K amount against what you actually received
    - You owe tax on all rental income regardless of whether a 1099 arrives — the form is informational
```

### `#direct-booking-taxes` — Direct bookings —taxes Vrbo doesn't handle

```
TODO: 2–3 paragraphs covering:
    - Many Vrbo hosts accept off-platform bookings (repeat guests, referrals, own website)
      after meeting guests through Vrbo — this is common and legal but creates tax complexity
    - Off-platform income: no 1099 from anyone, 100% self-reported on Schedule E
    - Lodging/occupancy tax responsibility for direct bookings: when Vrbo isn't the payment
      processor, YOU must collect from the guest at booking and remit yourself — walk through
      the state registration process briefly
    - Callout-amber: "Direct bookings where you collect payment are entirely off Vrbo's radar —
      the IRS isn't, and neither are your state/county tax authorities"
```

### `#schedule-e-vs-schedule-c` — Schedule E vs Schedule C —which applies to you

```
TODO: 2–3 paragraphs covering:
    - Same substantial-services test as Airbnb: daily housekeeping, meals, concierge = Schedule C;
      standard hospitality (clean linens, Wi-Fi, supplies) = Schedule E
    - Most Vrbo hosts are Schedule E (passive rental) — no 15.3% self-employment tax
    - Comparison table: Schedule E vs C (form, when it applies, SE tax? columns)
    - Vrbo-specific nuance: hosts who manage multiple properties for OTHER owners (property mgmt)
      cross into Schedule C territory more readily — even without providing guest services
```

### `#what-vrbo-hosts-can-deduct` — What Vrbo hosts can deduct

```
TODO: 2–3 paragraphs + H3 subsections covering:
    H3: Direct expenses (100% deductible)
    - Vrbo host service fee (typically 5% of booking subtotal) — fully deductible
    - Vrbo annual subscription fee if on subscription plan — fully deductible
    - Cleaning fees paid to cleaners, supplies, linens, photography
    - Repairs, smart locks, security cameras specific to the rental
    H3: Shared expenses (% of rental use)
    - Mortgage interest, property taxes, utilities, insurance — rental-percentage only
    - HOA fees, internet — rental-percentage only
    H3: Depreciation — the deduction most hosts miss
    - 27.5-year depreciation on the structure; hot tub, dock, deck = land improvements
      at 15 years; furniture/appliances at 5–7 years
    - Callout-green: real depreciation example with numbers
```

### `#state-county-lodging-taxes` — State, county, and lodging taxes

```
TODO: 2–3 paragraphs covering:
    - Vrbo collects and remits in many jurisdictions but NOT all — link hosts to Vrbo's
      tax collection page to verify their specific market
    - Name 3–4 common problem spots where Vrbo doesn't remit (typically rural counties,
      small municipalities, certain states with local-only lodging taxes)
    - Short-term rental permit/license requirements: many cities require STR registration
      even when the platform handles tax collection — these are separate obligations
    - Callout-amber: "If your Vrbo dashboard shows $0 in taxes collected, you collect and remit"
```

### `#should-vrbo-hosts-form-an-llc` — Should Vrbo hosts form an LLC?

```
TODO: 2 paragraphs covering:
    - Same liability rationale as Airbnb: guest injuries, property damage, and disputes
      expose personal assets without LLC protection
    - Vrbo-specific angle: many Vrbo hosts have whole-home vacation properties (separate from
      primary residence) — these are more commonly worth putting in an LLC than a room rental,
      and have estate-planning benefits too
    - Warning: mortgage "due on sale" clause when transferring title to an LLC —
      consult an attorney before transferring
```

### `#common-mistakes-vrbo-hosts-make` — Common mistakes Vrbo hosts make

```
TODO: 5 numbered H3 subsections:
    1. Trusting Vrbo to handle all lodging taxes (coverage gaps are real)
    2. Not reconciling gross 1099-K vs net payout — overpaying by not subtracting
       taxes Vrbo collected on your behalf before claiming them as income
    3. Skipping depreciation entirely (same as Airbnb)
    4. Failing to track and report direct-booking income
    5. Not registering for an STR permit before listing — local enforcement is increasing
```

### `#the-bottom-line` — The bottom line

```
TODO: 2 closing paragraphs summarizing:
    - Vrbo income is treated nearly identically to Airbnb — Schedule E, same deductions,
      same depreciation rules — with two important differences: gross 1099-K reconciliation
      and less consistent lodging-tax collection
    - Action items: verify lodging tax coverage in your Vrbo dashboard, track direct bookings
      separately, don't skip depreciation, and consider an LLC if you have a standalone rental property
```

---
