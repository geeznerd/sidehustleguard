#!/usr/bin/env python3
"""
Phase 18 — Backfill FAQPage + BreadcrumbList JSON-LD on the 5 new tools.

Each new tool currently has only WebApplication + Offer schema. The OLD
calculators have richer schema (FAQPage, BreadcrumbList, Article, etc.)
so the new tools should match.

This script inserts two new JSON-LD blocks right after the existing
WebApplication schema in each tool's <head>. Idempotent — bails on
files that already have FAQPage schema.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://www.sidehustleguard.com"

# Per-tool config: page slug, display name (for breadcrumb), and the FAQ Q&A pairs
TOOLS = {
    "1099k-threshold-calculator.html": {
        "slug": "1099k-threshold-calculator",
        "breadcrumb_name": "1099-K Threshold Calculator",
        "faq": [
            ("Why does the 1099-K threshold keep changing?",
             "The American Rescue Plan Act of 2021 dropped the federal 1099-K threshold from $20,000 + 200 transactions to $600 with no transaction minimum. The IRS phased the change in over multiple years: $5,000 for tax year 2024, $2,500 for 2025, and $600 for 2026."),
            ("What if I don't get a 1099-K?",
             "A 1099-K is a reporting form, not a tax bill. If your net self-employment income (sales minus business expenses) is $400 or more, you still owe self-employment tax and must file Schedule C and Schedule SE — whether or not a platform sent you a 1099-K."),
            ("Do multiple platforms combine for the 1099-K threshold?",
             "No. Each payment processor evaluates its own threshold independently. If you made $1,200 on Etsy and $1,200 on PayPal in 2025, neither will issue a 1099-K (each is under $2,500 federal) — but you still earned $2,400 of taxable income that you must report."),
            ("Are state 1099-K thresholds lower than federal?",
             "Yes, several states have set lower 1099-K thresholds: Massachusetts, Vermont, Virginia, Maryland, and DC all use $600 regardless of the federal rule. Illinois is $1,000 + 3 transactions, New Jersey is $1,000."),
            ("How do I reconcile a 1099-K on my tax return?",
             "The 1099-K reports gross payment volume — before platform fees, refunds, and chargebacks. Net taxable income is much less. Keep records of platform fees, refunds and chargebacks, sales tax collected, and business expenses. Net business income (Schedule C) is usually a fraction of the 1099-K gross figure.")
        ]
    },
    "tax-penalty-estimator.html": {
        "slug": "tax-penalty-estimator",
        "breadcrumb_name": "Tax Penalty Estimator",
        "faq": [
            ("How does the IRS calculate the failure-to-file penalty?",
             "Under IRC § 6651(a)(1), the failure-to-file penalty is 5% of the unpaid tax per month or part of a month, up to a maximum of 25%. If your return is more than 60 days late, the minimum penalty is the smaller of $510 (2025+ inflation-adjusted) or 100% of the tax owed."),
            ("How does the IRS calculate the failure-to-pay penalty?",
             "Under IRC § 6651(a)(2), failure-to-pay is 0.5% of unpaid tax per month or part of a month, capped at 25%. The rate increases to 1% per month if the IRS issues a notice of intent to levy, and decreases to 0.25%/month if you're on an approved installment agreement."),
            ("What is the IRS interest rate on unpaid taxes?",
             "Per IRC § 6621, the IRS interest rate is the federal short-term rate plus 3 percentage points, updated quarterly. For most of 2024 and 2025 it has been 8% per year, compounded daily."),
            ("What if I miss a quarterly estimated tax payment?",
             "Quarterly underpayment is calculated under IRC § 6654, not § 6651. There's no failure-to-file or failure-to-pay penalty — just an interest-style charge from the missed due date until you pay (or April 15 of the following year). The rate matches the federal short-term + 3% (currently 8% APR)."),
            ("Can I get IRS penalties abated?",
             "Sometimes. The IRS offers first-time penalty abatement (FTA) for filers with a clean compliance history — typically removing failure-to-file + failure-to-pay penalties for one tax year if you've been on time the previous three. Request it by phone or with a one-page letter. Reasonable-cause abatement is harder to qualify for."),
            ("How do state penalties differ from federal?",
             "Most states with income tax mirror the federal structure: 5%/month failure-to-file capped at 25%, 0.5-1%/month failure-to-pay, and 5-10% APR interest. No-income-tax states (AK, FL, NV, NH, SD, TN, TX, WA, WY) won't charge state income tax penalties.")
        ]
    },
    "expense-swiper.html": {
        "slug": "expense-swiper",
        "breadcrumb_name": "Can I Deduct This? Tax Swipe",
        "faq": [
            ("How do delivery driver tax deductions work?",
             "Delivery drivers are independent contractors who file Schedule C. The IRS test for any deduction is whether it's ordinary and necessary for your trade. Things directly tied to delivery (mileage, hot bags, phone mount, tolls) are usually deductible. Personal lifestyle expenses (gym, Spotify, your own meals) usually aren't, even if they help you work."),
            ("Should delivery drivers use standard mileage or actual expenses?",
             "Standard mileage deducts a flat rate per business mile (70¢ in 2026) and includes gas, insurance, repairs, and depreciation. Actual expense method deducts the business-use percentage of each car cost — more recordkeeping, often a smaller deduction. Most delivery drivers come out ahead with standard mileage."),
            ("Are speeding and parking tickets deductible?",
             "Never. Per IRC § 162(f), fines and penalties paid to a government for any law violation are explicitly non-deductible — even when incurred during business driving. This applies to speeding tickets, parking tickets, and any other government-issued fine."),
            ("Can I deduct my phone bill as a delivery driver?",
             "Partially. You can deduct the business-use portion of your phone bill. If you spend ~60% of phone time on delivery apps and customer calls, deduct 60% of the bill. A dedicated second cell phone line used only for delivery work is 100% deductible.")
        ]
    },
    "quarterly-tax-deadline.html": {
        "slug": "quarterly-tax-deadline",
        "breadcrumb_name": "Quarterly Tax Deadline Countdown",
        "faq": [
            ("Why do quarterly estimated taxes exist?",
             "Self-employed people don't have an employer withholding tax from each paycheck, so the IRS expects payment throughout the year via quarterly estimated payments (Form 1040-ES). This applies to anyone expecting to owe $1,000+ in federal tax after withholding and credits."),
            ("Who is required to make estimated tax payments?",
             "Per IRC § 6654, you must make estimated payments if both (a) you expect to owe $1,000+ in federal tax for the year after withholding and credits, AND (b) your withholding won't cover at least 90% of this year's tax or 100% of last year's (110% if prior AGI > $150k — the safe harbor rule)."),
            ("When are the IRS quarterly tax deadlines?",
             "Q1 is April 15 for income earned January-March. Q2 is June 15 for income earned April-May. Q3 is September 15 for income earned June-August. Q4 is January 15 of the following year for income earned September-December. If a date falls on a weekend or federal holiday, it shifts to the next business day."),
            ("What happens if I miss a quarterly tax deadline?",
             "The IRS charges an underpayment penalty for the missed quarter — interest on the missing amount from the due date until you pay (or April 15 of the following year). The rate is the federal short-term rate plus 3% — currently around 8% APR."),
            ("How do I pay quarterly estimated taxes?",
             "Use IRS Direct Pay (free, online, 5 minutes) at irs.gov/payments/direct-pay, EFTPS (free, requires enrollment) at eftps.gov, a debit or credit card via an IRS-approved processor (small fee), or mail a check with Form 1040-ES voucher.")
        ]
    },
    "w4-withholding-calculator.html": {
        "slug": "w4-withholding-calculator",
        "breadcrumb_name": "W-4 Withholding Calculator",
        "faq": [
            ("Can I skip quarterly estimated taxes by adjusting my W-4?",
             "Yes, if you have a W-2 job. Per IRC § 6654(g)(1), payroll withholding is considered paid evenly throughout the year regardless of when it's actually withheld. So bumping your W-2 employer's withholding by enough to cover both your day-job tax AND your side hustle tax satisfies the quarterly safe harbor automatically — no estimated payments needed."),
            ("How do I fill out my W-4 to cover side hustle income?",
             "On Form W-4, go to Step 4(c) labeled 'Extra withholding'. Enter the dollar amount you want withheld per pay period in addition to standard withholding. Sign and date the form, hand it to HR. New withholding starts the next pay cycle. Do not change Step 4(a) for this purpose."),
            ("Should I use W-4 Line 4(a) or 4(c) for side hustle income?",
             "Use 4(c). Line 4(a) ('Other income') tells your employer to use standard withholding tables as if you had a higher salary — which can over-withhold because of graduated bracket logic. Line 4(c) ('Extra withholding') is a predictable, exact dollar amount per pay period."),
            ("When does the W-4 withholding hack NOT work?",
             "When you don't have a W-2 job (no paycheck to withhold from — use quarterly estimates instead), when your side hustle dwarfs your day job (the extra withholding could exceed take-home), when your W-2 exceeds the Social Security wage base (FICA math changes), or when you're a high earner with Net Investment Income Tax exposure."),
            ("Does this work for state taxes too?",
             "Yes, but state withholding is handled separately. Each state with income tax has its own W-4 equivalent — California DE-4, New York IT-2104, etc. Bump your state withholding similarly via the state-specific form. No-income-tax states (AK, FL, NV, NH, SD, TN, TX, WA, WY) require no state withholding adjustment.")
        ]
    }
}


def make_faqpage(faq_pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            }
            for q, a in faq_pairs
        ]
    }


def make_breadcrumb(slug, name):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": BASE + "/guides"},
            {"@type": "ListItem", "position": 3, "name": name, "item": f"{BASE}/{slug}"}
        ]
    }


# Pattern: find the existing WebApplication </script> closing in <head>
# and inject the two new schema blocks right after it.
WEBAPP_CLOSE_RE = re.compile(
    r'(<script type="application/ld\+json">\s*\{[^<]*?"@type":\s*"WebApplication"[^<]*?\}\s*</script>)',
    re.DOTALL
)


def inject(path: Path, config) -> str:
    text = path.read_text(encoding="utf-8")
    if '"@type": "FAQPage"' in text or '"@type":"FAQPage"' in text:
        return "already-has-faq"

    faq_json = json.dumps(make_faqpage(config["faq"]), indent=2)
    crumb_json = json.dumps(make_breadcrumb(config["slug"], config["breadcrumb_name"]), indent=2)

    insertion = (
        '\n\n<script type="application/ld+json">\n' + faq_json + '\n</script>'
        '\n\n<script type="application/ld+json">\n' + crumb_json + '\n</script>'
    )

    new_text, n = WEBAPP_CLOSE_RE.subn(lambda m: m.group(1) + insertion, text, count=1)
    if n == 0:
        return "no-webapp-anchor"

    path.write_text(new_text, encoding="utf-8")
    return "injected"


def main() -> int:
    counts = {"injected": 0, "already-has-faq": 0, "no-webapp-anchor": 0}
    for fname, config in TOOLS.items():
        p = ROOT / fname
        if not p.exists():
            print(f"  [MISSING] {fname}")
            continue
        status = inject(p, config)
        counts[status] += 1
        print(f"  [{status:>16}] {fname}")
    print()
    print(f"Done. " + " ".join(f"{k}={v}" for k, v in counts.items()))
    return 0 if counts["no-webapp-anchor"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
