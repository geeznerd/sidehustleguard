"""
Build the year-end CPA handoff checklist PDF.
One printable letter-size page.
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, Flowable
)
import os

NAVY      = HexColor("#1c2b4a")
GOLD      = HexColor("#c9973a")
GOLD_PALE = HexColor("#fdf5e8")
CREAM     = HexColor("#faf8f4")
GREEN     = HexColor("#276944")
GREEN_BG  = HexColor("#eaf5ef")
MUTED     = HexColor("#6b7a96")
BORDER    = HexColor("#e5e7ed")

ss = getSampleStyleSheet()
title_style = ParagraphStyle("T", parent=ss["Normal"], fontName="Times-Bold", fontSize=26, leading=30, textColor=NAVY, spaceAfter=4)
sub_style   = ParagraphStyle("S", parent=ss["Normal"], fontName="Helvetica", fontSize=11, leading=15, textColor=MUTED, spaceAfter=14)
eye_style   = ParagraphStyle("E", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=9, leading=11, textColor=GOLD, spaceAfter=2)
section_h   = ParagraphStyle("H", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=NAVY, spaceBefore=8, spaceAfter=4)
item_style  = ParagraphStyle("I", parent=ss["Normal"], fontName="Helvetica", fontSize=10, leading=14, textColor=HexColor("#333333"), leftIndent=18, spaceAfter=2)
hint_style  = ParagraphStyle("X", parent=ss["Normal"], fontName="Helvetica-Oblique", fontSize=8.5, leading=12, textColor=MUTED, leftIndent=18, spaceAfter=4)
foot_style  = ParagraphStyle("F", parent=ss["Normal"], fontName="Helvetica-Oblique", fontSize=8.5, leading=11, textColor=MUTED, spaceBefore=10)

def checkbox_item(label, hint=None):
    """Return a tiny inline flowable: a checkbox cell + label."""
    cb = Table([["☐"]], colWidths=[0.22*inch])
    cb.setStyle(TableStyle([
        ("FONTSIZE", (0,0), (-1,-1), 14),
        ("TEXTCOLOR", (0,0), (-1,-1), GOLD),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    body_cells = [[Paragraph(f"<b>{label}</b>", item_style)]]
    if hint:
        body_cells.append([Paragraph(hint, hint_style)])
    body = Table(body_cells, colWidths=[6.5*inch])
    body.setStyle(TableStyle([
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
    ]))
    row = Table([[cb, body]], colWidths=[0.3*inch, 6.7*inch])
    row.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 1),
        ("BOTTOMPADDING", (0,0), (-1,-1), 1),
    ]))
    return row

# ── BUILD ──
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cpa-year-end-handoff-checklist.pdf")
doc = SimpleDocTemplate(
    out, pagesize=LETTER,
    leftMargin=0.7*inch, rightMargin=0.7*inch,
    topMargin=0.6*inch, bottomMargin=0.55*inch,
    title="Year-End CPA Handoff Checklist",
    author="SideHustleGuard"
)

story = []

# Header band
header_table = Table(
    [[Paragraph("YEAR-END BONUS · QUARTERLY TAX SYSTEM", eye_style),
      Paragraph("SideHustleGuard", ParagraphStyle("HR", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=10, leading=12, textColor=GOLD, alignment=2))]],
    colWidths=[5.2*inch, 1.8*inch]
)
header_table.setStyle(TableStyle([
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ("BOTTOMPADDING", (0,0), (-1,-1), 0),
]))
story.append(header_table)
story.append(Paragraph("CPA Year-End Handoff Checklist", title_style))
story.append(Paragraph("Print this. Tick boxes as you gather. Hand the whole stack to your CPA — they'll thank you.", sub_style))

# Gold divider
div = Table([[" "]], colWidths=[7.0*inch], rowHeights=[2])
div.setStyle(TableStyle([("LINEBELOW", (0,0), (-1,-1), 1.5, GOLD)]))
story.append(div)
story.append(Spacer(1, 6))

# ── SECTION 1: Income documents ──
story.append(Paragraph("1. INCOME DOCUMENTS (gather originals or PDFs)", section_h))
story.append(checkbox_item("All 1099-NEC forms", "From every client or platform that paid you $600+ this year. Should arrive by Jan 31."))
story.append(checkbox_item("All 1099-K forms", "From payment processors (Stripe, PayPal, Venmo for business, Uber, DoorDash, Etsy, etc.). Threshold is $5,000 for 2025; check current year."))
story.append(checkbox_item("All W-2s", "Day-job income, if any. Box 2 (federal tax withheld) is the number that affects your quarterly calculation."))
story.append(checkbox_item("All 1099-INT, 1099-DIV, 1099-B", "Interest, dividends, brokerage activity — even small amounts count."))
story.append(checkbox_item("K-1s (if a partner in a partnership/S-corp)", "These often arrive late — March is common. Don't file without them."))
story.append(checkbox_item("Anything else with \"1099\" in the name", "1099-G unemployment, 1099-R retirement, 1099-MISC rents/royalties, etc."))

# ── SECTION 2: Records you produced this year ──
story.append(Paragraph("2. RECORDS YOU PRODUCED THIS YEAR", section_h))
story.append(checkbox_item("Quarterly payment log (from the Quarterly Tax System)",
    "All four quarterly payments — date paid, amount, federal vs state, confirmation numbers. Form 1040 line 26 needs this total."))
story.append(checkbox_item("Mileage log (if you used standard mileage)",
    "From the Mileage Tracker or your own log. CPA needs total business miles, total miles all year, and your business-use %."))
story.append(checkbox_item("Income & expense ledger or QuickBooks/spreadsheet export",
    "Categorized profit & loss for the year. Schedule C needs this broken out by category (advertising, supplies, software, etc.)."))
story.append(checkbox_item("Bank & credit card statements (business)",
    "12 months of statements for any account where business money flowed. CPA may not need them all — but if they ask, you're ready."))
story.append(checkbox_item("Receipts for major business purchases (>$500)",
    "Especially if you might depreciate them (computer, camera, vehicle). Smaller receipts are usually fine to keep summarized."))
story.append(checkbox_item("Home office square footage (if claiming)",
    "Total sq ft of the home AND of the dedicated work area. CPA picks simplified vs actual method based on these numbers."))

# ── SECTION 3: Personal info ──
story.append(Paragraph("3. PERSONAL INFO YOUR CPA NEEDS", section_h))
story.append(checkbox_item("Social Security numbers (you, spouse, dependents)",
    "Yes — even if your CPA \"already has them.\" Confirms nothing changed."))
story.append(checkbox_item("Bank routing & account numbers (for direct refund)",
    "Speeds refunds by 2–4 weeks vs paper check."))
story.append(checkbox_item("Estimated payments made under spouse's name (joint filers)",
    "Easy thing to miss — IRS posts these by SSN; mismatch can delay or lose them."))
story.append(checkbox_item("Last year's return (if new CPA)",
    "First page especially — last year's AGI determines this year's safe harbor multiplier."))

# ── SECTION 4: Questions to ask ──
story.append(Paragraph("4. ASK YOUR CPA THESE QUESTIONS", section_h))
story.append(checkbox_item("\"Do I qualify for the QBI deduction this year?\"",
    "The Qualified Business Income deduction is worth 20% off your business income for most self-employed under the income limits. Often missed by first-time filers."))
story.append(checkbox_item("\"Am I on track to hit the SE income threshold where S-corp election makes sense?\"",
    "Generally above $40–50K of profit, S-corp can save you on SE tax. Important to plan a YEAR ahead."))
story.append(checkbox_item("\"What should my Q1 estimated payment be next year?\"",
    "Lock this in before you leave the meeting. Update the Setup tab in your Quarterly Tax System the moment you get home."))
story.append(checkbox_item("\"Any deductions I'm missing?\"",
    "Common ones overlooked by side-hustlers: phone (business %), professional development, business insurance, retirement contributions (SEP-IRA, solo 401k)."))

# Footer
story.append(Spacer(1, 6))
story.append(div)
story.append(Paragraph(
    "Educational tool only — not legal or tax advice. Your CPA may need additional items based on your specific situation. "
    "Made by SideHustleGuard · sidehustleguard.com",
    foot_style))

doc.build(story)
print(f"Saved: {out}")
print(f"Size:  {os.path.getsize(out)/1024:.1f} KB")
