#!/usr/bin/env python3
"""
Phase 19 — Build niche variants of /expense-swiper.

The /expense-swiper engine is now path-routed: it reads
window.location.pathname against EXPENSE_SWIPER_PATHS in
/assets/js/expense-swiper-data.js to pick a dataset.

This script takes expense-swiper.html (delivery v1, our canonical
template) and emits 4 niche pages with per-page meta swapped in:
  - etsy-deduction-swiper.html
  - airbnb-deduction-swiper.html
  - onlyfans-deduction-swiper.html
  - tutor-deduction-swiper.html

Each generated page keeps the SAME engine + CSS + data loader. We
swap only the per-page strings (title, description, hero text, intro
copy, schemas, SEO content section).

The hand-tuned delivery FAQPage schema block is stripped from each
niche output — the engine's injectDynamicFAQSchema() builds a fresh
one from the active hustle's card array on page load.

Run from repo root:  python3 scripts/build-niche-swipers.py
"""
import re
from pathlib import Path

ROOT     = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "expense-swiper.html"

# ─── Per-niche meta. Each block is everything that's not engine code. ──
NICHES = {
    "etsy": {
        "slug":      "etsy-deduction-swiper",
        "count":     22,
        "title":     "Can I Deduct This? Tax Deduction Swipe for Etsy Sellers — SideHustleGuard",
        "metadesc":  "Tap or swipe through 22 real expenses an Etsy seller might claim — shipping labels, Cricut blades, photo backdrops, Etsy fees, COGS materials. See which are deductible under IRS Pub 535.",
        "ogtitle":   "Can I Deduct This? Tax Deduction Swipe for Etsy Sellers",
        "ogdesc":    "22 real expenses. Swipe deductible or personal. Find out where IRS Pub 535 actually lands for handmade and print-on-demand sellers.",
        "schema_name": "Tax Deduction Swipe — Etsy Sellers",
        "schema_desc": "Interactive tool to test which Etsy seller expenses are likely deductible under IRS Pub 535.",
        "crumb_label": "Etsy Tax Deduction Swipe",
        "hero_badge":  "Free · Etsy sellers",
        "hero_h1":     "Can I <em>deduct</em> this?",
        "hero_sub":    "Swipe through 22 real expenses every Etsy seller runs into — shipping labels, photo backdrops, Cricut blades, COGS materials. Find out which the IRS lets you write off.",
        "intro_title_strong": "22 expenses. <em>Personal</em> or <em>deductible</em>?",
        "intro_p":     "For each card: would the IRS let an Etsy seller write this off? Tap the buttons (or swipe the card) to guess. We'll show you the answer + explanation after each one.",
        "intro_li_yes":"<strong>Swipe right</strong> or tap <strong>Deductible</strong> if you think an Etsy seller can claim it.",
        "intro_li_total": "At the end, you'll see all 22 with the IRS-aligned verdict + reasoning.",
        "results_headline": "Nice work. Here's the IRS-aligned breakdown for all 22 expenses.",
        "seo_html": """  <h2>How <em>Etsy seller</em> deductions actually work</h2>
  <p>If you sell on Etsy — handmade goods, vintage finds, digital downloads, or print-on-demand — you're self-employed. You file a Schedule C, you pay self-employment tax on net profit, and you can deduct ordinary and necessary business expenses against your sales.</p>
  <p>The IRS test for any business deduction is whether it's <strong>ordinary and necessary</strong> for your trade. For an Etsy seller, that usually means: things directly tied to making, photographing, packaging, and shipping product (materials, tools, shipping labels, Etsy fees, listing photos) are clearly deductible. Personal lifestyle expenses (gym, your own coffee, a winter coat you wear all year) usually aren't, even if you can rationalize them.</p>

  <h2>The <em>COGS</em> wrinkle Etsy sellers get wrong</h2>
  <p>Materials that go INTO your finished product (yarn, beads, fabric, wood, resin, blank mugs, printer ink for prints) are <strong>cost of goods sold</strong> — reported on Schedule C Part III, not as a regular expense. Tools you use repeatedly (Cricut, sewing machine, kiln) are usually depreciated or Section 179'd separately. Etsy and PayPal fees, listing fees, and promoted listing spend are normal Schedule C expenses on Line 17 (Legal & Professional) or Line 8 (Advertising).</p>
  <p>If you sell physical goods, you also need to <strong>track ending inventory</strong> at year-end — the materials and finished pieces sitting in your studio on Dec 31. Most Etsy sellers under the $30M small-business threshold can use the cash method and treat all materials purchased in-year as COGS, which is simpler. Confirm with your tax pro.</p>

  <h2>What this tool <em>isn't</em></h2>
  <p>This is an educational swipe — not tax advice. Real deductibility depends on how you actually use the item, what records you keep, and whether the item is COGS, an expense, or a depreciable asset. The verdicts here are based on IRS Pub 535 (Business Expenses) and Pub 538 (Accounting Periods and Methods) as of 2026. <strong>Verify with a licensed tax pro before claiming any deduction on your return.</strong></p>
""",
    },
    "airbnb": {
        "slug":      "airbnb-deduction-swiper",
        "count":     22,
        "title":     "Can I Deduct This? Tax Deduction Swipe for Airbnb Hosts — SideHustleGuard",
        "metadesc":  "Tap or swipe through 22 real expenses an Airbnb / VRBO host might claim — cleaning, linens, Wi-Fi, mortgage interest, utilities, listing photos. See which are deductible under IRS Pub 527.",
        "ogtitle":   "Can I Deduct This? Tax Deduction Swipe for Airbnb Hosts",
        "ogdesc":    "22 real expenses. Swipe deductible or personal. Find out where IRS Pub 527 lands for short-term rental hosts on Schedule E or C.",
        "schema_name": "Tax Deduction Swipe — Airbnb Hosts",
        "schema_desc": "Interactive tool to test which short-term rental expenses are likely deductible under IRS Pub 527 and Pub 535.",
        "crumb_label": "Airbnb Tax Deduction Swipe",
        "hero_badge":  "Free · Airbnb hosts",
        "hero_h1":     "Can I <em>deduct</em> this?",
        "hero_sub":    "Swipe through 22 real expenses every Airbnb and VRBO host runs into — cleaning fees, towels, mortgage interest, utilities, smart locks. Find out which the IRS lets you write off.",
        "intro_title_strong": "22 expenses. <em>Personal</em> or <em>deductible</em>?",
        "intro_p":     "For each card: would the IRS let an Airbnb host write this off? Tap the buttons (or swipe the card) to guess. We'll show you the answer + explanation after each one.",
        "intro_li_yes":"<strong>Swipe right</strong> or tap <strong>Deductible</strong> if you think a short-term rental host can claim it.",
        "intro_li_total": "At the end, you'll see all 22 with the IRS-aligned verdict + reasoning.",
        "results_headline": "Nice work. Here's the IRS-aligned breakdown for all 22 expenses.",
        "seo_html": """  <h2>How <em>Airbnb host</em> deductions actually work</h2>
  <p>If you rent a property short-term on Airbnb, VRBO, or any platform, the IRS treats it either as <strong>passive rental income on Schedule E</strong> (most hosts) or <strong>a business on Schedule C</strong> if you provide substantial services like daily housekeeping, breakfast, or concierge. Most hosts are Schedule E.</p>
  <p>The IRS test for any business deduction is whether it's <strong>ordinary and necessary</strong>. For a host, that usually means: things directly tied to the rental (cleaning, towels, Wi-Fi, listing photos, mortgage interest on the rental portion, utilities, repairs) are deductible. Personal lifestyle expenses while you stay there yourself usually aren't — and personal-use days reduce what you can deduct.</p>

  <h2>The <em>14-day</em> rule and personal-use math</h2>
  <p>If you personally use the property more than <strong>14 days OR 10% of total rental days</strong> in the year, it counts as a residence. Deductions get capped at gross rental income — you can't show a tax loss. Track every night you stay there. Also: rentals of fewer than 14 days total in the year are <em>completely tax-free</em> (the "Augusta rule") — you don't even report the income.</p>
  <p>For mixed-use properties, you also have to <strong>prorate</strong> mortgage interest, property tax, utilities, and depreciation by rental days vs personal days. A property you rented 200 days and used personally for 20 days gets a 200/220 = 91% allocation on shared costs.</p>

  <h2>What this tool <em>isn't</em></h2>
  <p>This is an educational swipe — not tax advice. Real deductibility depends on Schedule E vs C classification, your personal-use days, whether your activity hits the "material participation" tests, and whether the STR loophole applies to your situation. Verdicts are based on IRS Pub 527 (Residential Rental Property) and Pub 535 as of 2026. <strong>Verify with a licensed tax pro before claiming any deduction.</strong></p>
""",
    },
    "onlyfans": {
        "slug":      "onlyfans-deduction-swiper",
        "count":     22,
        "title":     "Can I Deduct This? Tax Deduction Swipe for OnlyFans Creators — SideHustleGuard",
        "metadesc":  "Tap or swipe through 22 real expenses an OnlyFans, Patreon, or content creator might claim — ring lights, editing software, wardrobe, makeup, set decor. See which are deductible under IRS Pub 535.",
        "ogtitle":   "Can I Deduct This? Tax Deduction Swipe for OnlyFans & Content Creators",
        "ogdesc":    "22 real expenses. Swipe deductible or personal. Find out where IRS Pub 535 lands for content creators, streamers, and subscription-platform talent.",
        "schema_name": "Tax Deduction Swipe — Content Creators",
        "schema_desc": "Interactive tool to test which content creator expenses are likely deductible under IRS Pub 535.",
        "crumb_label": "Creator Tax Deduction Swipe",
        "hero_badge":  "Free · Content creators",
        "hero_h1":     "Can I <em>deduct</em> this?",
        "hero_sub":    "Swipe through 22 real expenses every OnlyFans, Patreon, and content creator runs into — ring lights, editing software, wardrobe, set decor, home studio. Find out which the IRS lets you write off.",
        "intro_title_strong": "22 expenses. <em>Personal</em> or <em>deductible</em>?",
        "intro_p":     "For each card: would the IRS let a content creator write this off? Tap the buttons (or swipe the card) to guess. We'll show you the answer + explanation after each one.",
        "intro_li_yes":"<strong>Swipe right</strong> or tap <strong>Deductible</strong> if you think a content creator can claim it.",
        "intro_li_total": "At the end, you'll see all 22 with the IRS-aligned verdict + reasoning.",
        "results_headline": "Nice work. Here's the IRS-aligned breakdown for all 22 expenses.",
        "seo_html": """  <h2>How <em>creator</em> deductions actually work</h2>
  <p>If you earn from OnlyFans, Patreon, YouTube, Twitch, TikTok, Substack, or any subscription / ad-share platform, you're self-employed. You file Schedule C, pay self-employment tax on net profit, and can deduct ordinary and necessary business expenses against your creator income.</p>
  <p>The IRS test for any deduction is whether it's <strong>ordinary and necessary</strong> for your trade. For a creator, that usually means: things directly tied to producing content (cameras, lighting, microphones, editing software, set decor, platform fees, tax/accounting help) are deductible. Personal lifestyle expenses that "could" tie to content — gym, cosmetic surgery, your regular streaming subs — usually aren't, even when they appear on camera.</p>

  <h2>The <em>"appears on camera"</em> trap</h2>
  <p>Creators often try to deduct wardrobe, makeup, and grooming because "I bought it for content." The IRS generally rejects this: if the item has <strong>ordinary personal utility</strong> — clothing you could wear outside the shoot, makeup that doubles for daily wear, a haircut you'd get anyway — it's not deductible regardless of intent. Costumes, props, and stage wear unsuitable for street wear can be deductible. Document the specificity.</p>
  <p>The same logic applies to "content trips" — a vacation you filmed isn't automatically deductible just because cameras ran. To deduct travel, the <strong>primary purpose</strong> of the trip has to be business, with a documented work itinerary. Same for "competitor research" subscriptions to other creators — if you'd watch the content anyway, it's personal.</p>

  <h2>What this tool <em>isn't</em></h2>
  <p>This is an educational swipe — not tax advice. Real deductibility depends on how you use the item, what records you keep, and the business-use percentage you can document. Many items here are <em>conditional</em> — partial deductions are common. Verdicts are based on IRS Pub 535 (Business Expenses) as of 2026. <strong>Verify with a licensed tax pro before claiming anything.</strong></p>
""",
    },
    "tutor": {
        "slug":      "tutor-deduction-swiper",
        "count":     22,
        "title":     "Can I Deduct This? Tax Deduction Swipe for Online Tutors — SideHustleGuard",
        "metadesc":  "Tap or swipe through 22 real expenses an online tutor (VIPKid, Outschool, private students) might claim — Zoom Pro, lesson plans, iPad, mileage, liability insurance. See which are deductible under IRS Pub 535.",
        "ogtitle":   "Can I Deduct This? Tax Deduction Swipe for Online Tutors",
        "ogdesc":    "22 real expenses. Swipe deductible or personal. Find out where IRS Pub 535 lands for online tutors, K-12 contractors, and test-prep instructors.",
        "schema_name": "Tax Deduction Swipe — Online Tutors",
        "schema_desc": "Interactive tool to test which online tutor expenses are likely deductible under IRS Pub 535.",
        "crumb_label": "Tutor Tax Deduction Swipe",
        "hero_badge":  "Free · Online tutors",
        "hero_h1":     "Can I <em>deduct</em> this?",
        "hero_sub":    "Swipe through 22 real expenses every online tutor and private instructor runs into — Zoom Pro, iPad, lesson materials, mileage, platform fees. Find out which the IRS lets you write off.",
        "intro_title_strong": "22 expenses. <em>Personal</em> or <em>deductible</em>?",
        "intro_p":     "For each card: would the IRS let an online tutor write this off? Tap the buttons (or swipe the card) to guess. We'll show you the answer + explanation after each one.",
        "intro_li_yes":"<strong>Swipe right</strong> or tap <strong>Deductible</strong> if you think a tutor can claim it.",
        "intro_li_total": "At the end, you'll see all 22 with the IRS-aligned verdict + reasoning.",
        "results_headline": "Nice work. Here's the IRS-aligned breakdown for all 22 expenses.",
        "seo_html": """  <h2>How <em>online tutor</em> deductions actually work</h2>
  <p>If you tutor through VIPKid, Outschool, Preply, Wyzant, Varsity Tutors, or with your own private students, you're an independent contractor in nearly every case. You file Schedule C, pay self-employment tax on net profit, and can deduct ordinary and necessary business expenses against your tutoring income.</p>
  <p>The IRS test for any deduction is whether it's <strong>ordinary and necessary</strong> for your trade. For a tutor, that usually means: things directly tied to teaching (Zoom Pro, lesson materials, your tutoring iPad, platform fees, mileage to in-person sessions, liability insurance, CEU courses) are deductible. Personal lifestyle expenses (your own coffee, lunch, a gym membership) usually aren't.</p>

  <h2>Tutors vs <em>W-2 teachers</em> on deductions</h2>
  <p>Important distinction: K-12 W-2 teachers can only claim the $300 <strong>Educator Expense Deduction</strong> on Schedule 1 — most classroom spending is otherwise lost since the Tax Cuts and Jobs Act eliminated unreimbursed-employee deductions through 2025. <strong>Self-employed tutors are different.</strong> You deduct everything ordinary and necessary on Schedule C — no $300 cap, no employment classification limits.</p>
  <p>If you teach from home, you may also qualify for the <strong>home office deduction</strong> — but only if a specific room (or a clearly identifiable part of one) is used <em>regularly and exclusively</em> for tutoring. A corner of your kitchen doesn't count if anyone else uses that table. Document it with a floor plan and a list of business uses.</p>

  <h2>What this tool <em>isn't</em></h2>
  <p>This is an educational swipe — not tax advice. Real deductibility depends on how you actually use the item, what records you keep, and your business-use percentage. Many tools and devices need to be prorated. Verdicts are based on IRS Pub 535 (Business Expenses) and Pub 587 (Home Office) as of 2026. <strong>Verify with a licensed tax pro before claiming anything on your return.</strong></p>
""",
    },
}

# Default delivery values, used to find the strings to substitute.
DELIVERY = {
    "title":     "Can I Deduct This? Tax Deduction Swipe for Delivery Drivers — SideHustleGuard",
    "metadesc":  "Tap or swipe through 25 real expenses a DoorDash, Uber Eats, Grubhub, or Instacart driver might claim. See which are likely deductible, which aren't, and why — based on IRS Pub 535 and Pub 463.",
    "canonical": "https://www.sidehustleguard.com/expense-swiper",
    "ogtitle":   "Can I Deduct This? Tax Deduction Swipe for Delivery Drivers",
    "ogdesc":    "25 real expenses. Swipe deductible or personal. Find out where IRS Pub 535 actually lands — and what to verify with your tax pro.",
    "ogurl":     "https://www.sidehustleguard.com/expense-swiper",
    "schema_name": "Tax Deduction Swipe — Delivery Drivers",
    "schema_desc": "Interactive tool to test your knowledge of which delivery-driver expenses are likely deductible under IRS Pub 535.",
    "schema_url":  "https://www.sidehustleguard.com/expense-swiper",
    "crumb_label": "Can I Deduct This? Tax Swipe",
    "crumb_url":   "https://www.sidehustleguard.com/expense-swiper",
    "hero_badge":  "Free · Delivery drivers",
    "hero_sub":    "Swipe through 25 real expenses every DoorDash, Uber Eats, Grubhub, and Instacart driver runs into. Find out which are likely deductible — and where the IRS draws the line.",
    "intro_title_strong": "25 expenses. <em>Personal</em> or <em>deductible</em>?",
    "intro_p":     "For each card: would the IRS let a delivery driver write this off? Tap the buttons (or swipe the card) to guess. We'll show you the answer + explanation after each one.",
    "intro_li_yes":"<strong>Swipe right</strong> or tap <strong>Deductible</strong> if you think a delivery driver can claim it.",
    "intro_li_total": "At the end, you'll see all 25 with the IRS-aligned verdict + reasoning.",
    "p_total_init":   '<strong id="p-total">25</strong>',
    "r_total_init":   '<span id="r-total">25</span>',
    "results_headline":"Nice work. Here's the IRS-aligned breakdown for all 25 expenses.",
}


# Regex that matches the entire hand-tuned FAQPage <script> block from the
# delivery template. Engine auto-injects a fresh one for niche variants.
FAQ_SCHEMA_PATTERN = re.compile(
    r'\n<script type="application/ld\+json">\s*\{\s*"@context": "https://schema\.org",\s*"@type": "FAQPage".*?\}\s*</script>\n',
    re.DOTALL,
)


def build_niche(template_html: str, niche_key: str) -> str:
    cfg = NICHES[niche_key]
    slug = cfg["slug"]
    out = template_html

    # 1. Strip the hand-tuned delivery FAQPage block. Engine will auto-inject.
    out, n = FAQ_SCHEMA_PATTERN.subn("\n", out, count=1)
    if n != 1:
        raise SystemExit(f"[{slug}] FAQPage block not stripped — pattern mismatch")

    # 2. Per-page meta swaps. Replace delivery values with niche values.
    canonical = f"https://www.sidehustleguard.com/{slug}"
    swaps = [
        # <title>
        (DELIVERY["title"], cfg["title"]),
        # description meta
        (DELIVERY["metadesc"], cfg["metadesc"]),
        # canonical link
        (DELIVERY["canonical"], canonical),
        # og:title / og:description / og:url
        (DELIVERY["ogtitle"], cfg["ogtitle"]),
        (DELIVERY["ogdesc"],  cfg["ogdesc"]),
        # (ogurl matches canonical pattern — same string)
        # WebApplication schema fields
        (DELIVERY["schema_name"], cfg["schema_name"]),
        (DELIVERY["schema_desc"], cfg["schema_desc"]),
        # BreadcrumbList: 3rd position name + item URL
        (DELIVERY["crumb_label"], cfg["crumb_label"]),
        # Hero
        (DELIVERY["hero_badge"], cfg["hero_badge"]),
        (DELIVERY["hero_sub"],   cfg["hero_sub"]),
        # Intro card
        (DELIVERY["intro_title_strong"], cfg["intro_title_strong"]),
        (DELIVERY["intro_p"],     cfg["intro_p"]),
        (DELIVERY["intro_li_yes"], cfg["intro_li_yes"]),
        (DELIVERY["intro_li_total"], cfg["intro_li_total"]),
        # Initial progress counts (engine overwrites on first paint, but
        # avoid a "25" flash on a 22-card niche page)
        (DELIVERY["p_total_init"], f'<strong id="p-total">{cfg["count"]}</strong>'),
        (DELIVERY["r_total_init"], f'<span id="r-total">{cfg["count"]}</span>'),
        (DELIVERY["results_headline"], cfg["results_headline"]),
    ]
    for old, new in swaps:
        if old not in out:
            raise SystemExit(f"[{slug}] substitution miss: {old[:60]!r}")
        out = out.replace(old, new, 1)

    # Both canonical + og:url + schema url + breadcrumb item url all
    # use the same delivery URL string — replace ALL of them in one pass.
    out = out.replace(DELIVERY["canonical"], canonical)

    # 3. SEO content section at the bottom. Find the <div class="content">
    # block (Phase 14-era hand-written delivery copy) and replace its
    # children with the niche-specific copy.
    seo_pattern = re.compile(
        r'(<div class="content">)(.*?)(</div>\s*<footer>)',
        re.DOTALL,
    )
    m = seo_pattern.search(out)
    if not m:
        raise SystemExit(f"[{slug}] SEO content section not found")
    new_inner = "\n" + cfg["seo_html"]
    out = out[:m.start(2)] + new_inner + out[m.end(2):]

    return out


def main() -> int:
    template = TEMPLATE.read_text(encoding="utf-8")
    for key in NICHES:
        cfg  = NICHES[key]
        out  = build_niche(template, key)
        dest = ROOT / f"{cfg['slug']}.html"
        dest.write_text(out, encoding="utf-8")
        print(f"  [built] {cfg['slug']}.html ({len(out):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
