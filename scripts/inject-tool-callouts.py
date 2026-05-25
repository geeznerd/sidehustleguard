#!/usr/bin/env python3
"""
Phase 19.1 — Wire in-article tool callouts from existing high-traffic
guides into the 5 deduction swipers.

Each article gets ONE tool-callout aside inserted right before a
specific H2 anchor (chosen because that's where readers are already
thinking about deductibility). Idempotent: if a tool-callout already
exists on a page, the page is skipped.

The callout markup is rendered using the `.tool-callout` CSS pattern
added to /assets/css/design-system.css in this phase. No emoji
(CLAUDE.md rule) — uses a Fraunces italic apricot glyph instead.

Run from repo root:  python3 scripts/inject-tool-callouts.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


# (file, anchor_h2_substring, tool_url, glyph, title_html, blurb)
# anchor_h2_substring is a unique substring of the H2 line we insert ABOVE.
INJECTIONS = [
    # ─── Etsy → /etsy-deduction-swiper ───────────────────────────────
    ("etsy-taxes.html",
     'id="what-deductions-can-etsy-sellers-claim"',
     "/etsy-deduction-swiper",
     "E",
     "Test your <em>Etsy</em> deduction instincts",
     "22 real expenses an Etsy seller runs into — Cricut blades, photo backdrops, shipping labels, COGS materials. Swipe deductible or personal, see the IRS verdict + Pub 535 cite on each."),

    ("etsy-schedule-c.html",
     'id="part-ii-expenses-where-you-reduce-your-tax-bill"',
     "/etsy-deduction-swiper",
     "E",
     "Stuck on a <em>Schedule C</em> line item?",
     "Tap through 22 common Etsy seller expenses — what's a Part II expense, what's COGS, what's personal. 60 seconds, free, no sign-up."),

    ("llc-etsy-seller.html",
     'id="can-an-llc-save-me-money-on-taxes"',
     "/etsy-deduction-swiper",
     "E",
     "Know your <em>deductible</em> from your personal?",
     "An LLC saves you nothing if you can't tell a deduction from a personal expense. Swipe 22 real Etsy expenses — see the IRS verdict on each before you file."),

    ("etsy-home-office-deduction.html",
     'id="two-ways-to-calculate-the-deduction"',
     "/etsy-deduction-swiper",
     "E",
     "What else can an <em>Etsy</em> seller deduct?",
     "Home office is one of 22 deductions on our Etsy swiper — alongside Cricut blades, photo backdrops, COGS materials, Etsy fees. Quick game, IRS citations on every card."),

    # ─── Airbnb / STR → /airbnb-deduction-swiper ─────────────────────
    ("airbnb-host-taxes.html",
     'id="what-can-airbnb-hosts-deduct"',
     "/airbnb-deduction-swiper",
     "A",
     "Test your <em>Airbnb</em> deduction instincts",
     "22 real expenses every short-term rental host runs into — cleaning, towels, mortgage interest, listing photos, smart locks. Swipe deductible or personal, see the IRS verdict + Pub 527 cite on each."),

    ("airbnb-deductions-checklist.html",
     'id="frequently-asked-questions"',
     "/airbnb-deduction-swiper",
     "A",
     "Want it as a <em>game</em> instead?",
     "Same deductions, but as a 22-card swipe game. Tap through real expenses, get instant IRS-aligned verdicts. 60 seconds, free."),

    ("vrbo-host-taxes.html",
     'id="frequently-asked-questions"',
     "/airbnb-deduction-swiper",
     "A",
     "What can a <em>VRBO</em> host actually write off?",
     "22 real short-term rental expenses, IRS-aligned verdicts on every one — works for VRBO, Airbnb, Booking.com, direct bookings. 60-second swipe."),

    ("short-term-rentals.html",
     '>STR tax rules that apply to <em>every</em> host</h2>',  # no id on this H2 — match by inner text instead
     "/airbnb-deduction-swiper",
     "A",
     "Deductible or <em>personal</em>?",
     "22 real STR expenses — cleaning, smart locks, mortgage interest, listing photos. Swipe through and see the IRS verdict on each. Free, 60 seconds."),

    # ─── OnlyFans / Creators → /onlyfans-deduction-swiper ────────────
    ("onlyfans-taxes.html",
     'id="what-can-onlyfans-creators-deduct"',
     "/onlyfans-deduction-swiper",
     "O",
     "<em>Wardrobe?</em> Makeup? Gym? Test what's actually deductible.",
     "The IRS rejects most creator wardrobe + grooming deductions (the Pevsner rule). Swipe through 22 real creator expenses — ring light, content travel, set decor, surgery — and see where the line is."),

    ("patreon-taxes.html",
     'id="top-deductions-for-patreon-creators"',
     "/onlyfans-deduction-swiper",
     "O",
     "Test your <em>creator</em> deduction instincts",
     "22 real creator expenses — ring lights, editing software, set decor, content travel, competitor subs. Swipe deductible or personal, see the IRS verdict on each."),

    ("twitch-taxes.html",
     'id="streaming-equipment-deductions"',
     "/onlyfans-deduction-swiper",
     "O",
     "What else can a <em>streamer</em> deduct?",
     "Streaming gear is just the start. Swipe through 22 real creator expenses — green screens, editing tools, content trips, home studios — with IRS-aligned verdicts on each."),

    ("youtube-taxes.html",
     'id="equipment-and-production-deductions"',
     "/onlyfans-deduction-swiper",
     "O",
     "Test your <em>YouTuber</em> deduction instincts",
     "22 real content creator expenses — 4K webcams, mics, wardrobe, content travel, lighting kits. Swipe deductible or personal, see the IRS verdict + Pub 535 cite on each."),

    ("tiktok-taxes.html",
     'id="deductions-for-tiktok-creators"',
     "/onlyfans-deduction-swiper",
     "O",
     "Can <em>TikTokers</em> deduct that?",
     "22 real creator expenses — ring lights, props, wardrobe, makeup, content travel. Swipe through and see the IRS verdict. Free, 60 seconds, no sign-up."),

    # ─── Delivery → /expense-swiper (existing tool, now needs inbound links) ─
    ("doordash-taxes.html",
     'id="the-mileage-deduction-your-biggest-weapon"',
     "/expense-swiper",
     "D",
     "Test your <em>DoorDash</em> deduction instincts",
     "25 real expenses every delivery driver runs into — hot bags, dashcams, gym memberships, speeding tickets. Swipe deductible or personal, get the IRS verdict + Pub 463 / 535 cite on each."),

    ("uber-eats-taxes.html",
     'id="the-mileage-deduction-for-uber-eats"',
     "/expense-swiper",
     "D",
     "Test your <em>Uber Eats</em> deduction instincts",
     "25 real delivery expenses — hot bags, phone mounts, car washes, sunglasses, tolls. Swipe through and see the IRS verdict on each. 60 seconds, free."),

    ("grubhub-taxes.html",
     'id="the-mileage-deduction-your-biggest-break"',
     "/expense-swiper",
     "D",
     "Test your <em>Grubhub</em> deduction instincts",
     "25 real delivery driver expenses, IRS-aligned verdicts on each — hot bags, mileage apps, phone bills, parking tickets. 60-second swipe, free."),

    ("instacart-taxes.html",
     'id="the-mileage-deduction-for-instacart-shoppers"',
     "/expense-swiper",
     "D",
     "Test your <em>Instacart</em> deduction instincts",
     "25 real shopper expenses, IRS-aligned verdicts — reusable totes, hand sanitizer, AAA, sunglasses, car washes. 60-second swipe."),

    ("uber-lyft-taxes.html",
     'id="the-mileage-deduction-every-mile-counts"',
     "/expense-swiper",
     "D",
     "Test your <em>rideshare</em> deduction instincts",
     "25 real driver expenses, IRS-aligned verdicts on each — phone mount, car wash, AAA, dashcam, speeding tickets. 60-second swipe."),
]


# CSS glyph: use a single Fraunces italic letter (matches the swiper page
# numerals + the guides-page monogram tiles). NOT an emoji.
def render(glyph: str, tool_url: str, title_html: str, blurb: str) -> str:
    return (
        '<aside class="tool-callout" aria-label="Interactive tool">'
        '<div class="tool-callout-glyph" aria-hidden="true">' + glyph + '</div>'
        '<div class="tool-callout-body">'
        '<span class="tool-callout-eyebrow">Free · 60-second swipe</span>'
        '<p class="tool-callout-title">' + title_html + '</p>'
        '<p class="tool-callout-blurb">' + blurb + '</p>'
        '</div>'
        '<a class="tool-callout-cta" href="' + tool_url + '">Play the swiper →</a>'
        '</aside>'
    )


def inject(path: Path, anchor_substr: str, callout_html: str) -> str:
    text = path.read_text(encoding="utf-8")

    # Idempotent: if a tool-callout already exists on the page, skip.
    if 'class="tool-callout"' in text:
        return "already-has-callout"

    # Locate the anchor substring (either an H2 id attribute or a chunk of
    # the H2's inner text), then walk back to the start of the enclosing
    # `<h2` tag and insert the callout immediately before it.
    pos = text.find(anchor_substr)
    if pos == -1:
        return f"anchor-not-found ({anchor_substr})"
    h2_start = text.rfind("<h2", 0, pos)
    if h2_start == -1:
        return f"h2-start-not-found ({anchor_substr})"

    insertion = "\n" + callout_html + "\n"
    new_text = text[:h2_start] + insertion + text[h2_start:]
    path.write_text(new_text, encoding="utf-8")
    return "injected"


def main() -> int:
    results = {}
    for fname, anchor, url, glyph, title, blurb in INJECTIONS:
        path = ROOT / fname
        if not path.exists():
            results[fname] = "missing-file"
            continue
        callout = render(glyph, url, title, blurb)
        status = inject(path, anchor, callout)
        results[fname] = status

    width = max(len(k) for k in results)
    for fname, status in results.items():
        print(f"  [{status:>22}]  {fname:<{width}}")
    bad = [k for k, v in results.items() if v not in ("injected", "already-has-callout")]
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
