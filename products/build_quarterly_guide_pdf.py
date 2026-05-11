"""
Build the bonus PDF guide that ships with the Quarterly Tax System.
Outputs: quarterly-tax-survival-guide-2026.pdf
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Image, Flowable
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ── BRAND ──
NAVY      = HexColor("#1c2b4a")
GOLD      = HexColor("#c9973a")
GOLD_LT   = HexColor("#ddb06a")
GOLD_PALE = HexColor("#fdf5e8")
CREAM     = HexColor("#faf8f4")
CREAM_D   = HexColor("#f0ece3")
GREEN     = HexColor("#276944")
GREEN_BG  = HexColor("#eaf5ef")
AMBER     = HexColor("#a86c0a")
AMBER_BG  = HexColor("#fef6e8")
RED       = HexColor("#b83232")
RED_BG    = HexColor("#fbe9e9")
MUTED     = HexColor("#6b7a96")
DIM       = HexColor("#9aa3b5")
BORDER    = HexColor("#e5e7ed")

# ── STYLES ──
ss = getSampleStyleSheet()

title_style = ParagraphStyle(
    "Title", parent=ss["Normal"], fontName="Times-Bold", fontSize=42, leading=46,
    textColor=NAVY, alignment=TA_LEFT, spaceAfter=14
)
subtitle_style = ParagraphStyle(
    "Subtitle", parent=ss["Normal"], fontName="Helvetica", fontSize=14, leading=20,
    textColor=MUTED, alignment=TA_LEFT, spaceAfter=8
)
h1_style = ParagraphStyle(
    "H1", parent=ss["Normal"], fontName="Times-Bold", fontSize=22, leading=28,
    textColor=NAVY, alignment=TA_LEFT, spaceBefore=14, spaceAfter=10
)
h2_style = ParagraphStyle(
    "H2", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=14, leading=20,
    textColor=NAVY, alignment=TA_LEFT, spaceBefore=12, spaceAfter=6
)
body_style = ParagraphStyle(
    "Body", parent=ss["Normal"], fontName="Helvetica", fontSize=10.5, leading=16,
    textColor=HexColor("#333333"), alignment=TA_LEFT, spaceAfter=8
)
body_just = ParagraphStyle(
    "BodyJust", parent=body_style, alignment=TA_JUSTIFY
)
muted_style = ParagraphStyle(
    "Muted", parent=ss["Normal"], fontName="Helvetica-Oblique", fontSize=9.5, leading=14,
    textColor=MUTED, alignment=TA_LEFT, spaceAfter=6
)
callout_style = ParagraphStyle(
    "Callout", parent=ss["Normal"], fontName="Helvetica", fontSize=10.5, leading=16,
    textColor=NAVY, leftIndent=12, rightIndent=12, spaceAfter=10
)
bullet_style = ParagraphStyle(
    "Bullet", parent=body_style, fontSize=10.5, leading=16, leftIndent=14, bulletIndent=2, spaceAfter=4
)
page_title_style = ParagraphStyle(
    "PageTitle", parent=ss["Normal"], fontName="Times-Bold", fontSize=26, leading=32,
    textColor=NAVY, alignment=TA_LEFT, spaceAfter=4
)
eyebrow_style = ParagraphStyle(
    "Eyebrow", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=9, leading=12,
    textColor=GOLD, alignment=TA_LEFT, spaceAfter=2
)
toc_style = ParagraphStyle(
    "TOC", parent=ss["Normal"], fontName="Helvetica", fontSize=12, leading=22,
    textColor=NAVY, alignment=TA_LEFT
)

# ── HELPERS ──
def callout(text, bg=AMBER_BG, border=AMBER):
    p = Paragraph(text, callout_style)
    t = Table([[p]], colWidths=[6.3*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("LEFTPADDING", (0,0), (-1,-1), 16),
        ("RIGHTPADDING", (0,0), (-1,-1), 16),
        ("TOPPADDING", (0,0), (-1,-1), 12),
        ("BOTTOMPADDING", (0,0), (-1,-1), 12),
        ("LINEBEFORE", (0,0), (0,-1), 3, border),
    ]))
    return t

def kpi_table(rows, header_bg=NAVY, alt=False):
    """Render a small data table with brand styling."""
    t = Table(rows, colWidths=[2.4*inch, 1.5*inch, 1.5*inch, 0.9*inch])
    style = [
        ("BACKGROUND", (0,0), (-1,0), header_bg),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,0), 9),
        ("FONTSIZE", (0,1), (-1,-1), 10),
        ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
        ("TEXTCOLOR", (0,1), (-1,-1), HexColor("#333333")),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("GRID", (0,0), (-1,-1), 0.5, BORDER),
        ("ALIGN", (1,1), (-1,-1), "RIGHT"),
        ("ALIGN", (0,1), (0,-1), "LEFT"),
        ("ALIGN", (0,0), (-1,0), "LEFT"),
    ]
    if alt:
        for r in range(1, len(rows), 2):
            style.append(("BACKGROUND", (0,r), (-1,r), GOLD_PALE))
    t.setStyle(TableStyle(style))
    return t

def divider():
    t = Table([[" "]], colWidths=[6.3*inch], rowHeights=[1])
    t.setStyle(TableStyle([("LINEBELOW", (0,0), (-1,-1), 1, BORDER)]))
    return t

# ── PAGE TEMPLATE (header / footer on every page) ──
class CoverFlowable(Flowable):
    """Custom cover-page flowable."""
    def __init__(self, width, height):
        Flowable.__init__(self)
        self.width = width
        self.height = height
    def draw(self):
        c = self.canv
        # Navy background
        c.setFillColor(NAVY)
        c.rect(-0.7*inch, -0.7*inch, self.width + 1.4*inch, self.height + 1.4*inch, fill=1, stroke=0)
        # Gold glow
        c.setFillColorRGB(0.79, 0.59, 0.23, alpha=0.15)
        c.circle(self.width - 0.4*inch, 0.6*inch, 3.2*inch, fill=1, stroke=0)
        # Eyebrow badge
        c.setFillColor(GOLD_PALE)
        c.setStrokeColor(GOLD)
        c.roundRect(0, self.height - 0.6*inch, 2.2*inch, 0.35*inch, 0.17*inch, fill=1, stroke=1)
        c.setFillColor(GOLD)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(0.18*inch, self.height - 0.43*inch, "THE 2026 BONUS GUIDE")
        # Title
        c.setFillColor(white)
        c.setFont("Times-Bold", 36)
        c.drawString(0, self.height - 1.7*inch, "The Self-Employed")
        c.drawString(0, self.height - 2.25*inch, "Quarterly Tax")
        c.setFillColor(GOLD_LT)
        c.setFont("Times-BoldItalic", 36)
        c.drawString(0, self.height - 2.80*inch, "Survival Guide.")
        # Subtitle
        c.setFillColorRGB(1, 1, 1, alpha=0.75)
        c.setFont("Helvetica", 13)
        c.drawString(0, self.height - 3.4*inch, "How to never get hit with the IRS underpayment penalty again.")
        c.drawString(0, self.height - 3.7*inch, "Plain English. Real numbers. 2026 rules.")
        # Footer brand
        c.setFillColor(GOLD)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(0, 0.2*inch, "SideHustleGuard")
        c.setFillColorRGB(1, 1, 1, alpha=0.45)
        c.setFont("Helvetica", 10)
        c.drawString(1.5*inch, 0.2*inch, "sidehustleguard.com")

def on_later_pages(canvas_obj, doc):
    """Header + footer for non-cover pages."""
    canvas_obj.saveState()
    # Top hairline
    canvas_obj.setStrokeColor(BORDER)
    canvas_obj.setLineWidth(0.5)
    canvas_obj.line(0.7*inch, 10.7*inch, 7.8*inch, 10.7*inch)
    # Brand top-left
    canvas_obj.setFillColor(NAVY)
    canvas_obj.setFont("Helvetica-Bold", 9)
    canvas_obj.drawString(0.7*inch, 10.4*inch, "Quarterly Tax Survival Guide")
    canvas_obj.setFillColor(MUTED)
    canvas_obj.setFont("Helvetica", 9)
    canvas_obj.drawRightString(7.8*inch, 10.4*inch, "SideHustleGuard · 2026")
    # Bottom page number
    canvas_obj.setFillColor(MUTED)
    canvas_obj.setFont("Helvetica", 9)
    canvas_obj.drawRightString(7.8*inch, 0.45*inch, f"Page {doc.page}")
    canvas_obj.drawString(0.7*inch, 0.45*inch, "Educational only — not tax or legal advice")
    canvas_obj.restoreState()

def on_first_page(canvas_obj, doc):
    """Cover has no header/footer."""
    pass

# ── BUILD ──
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quarterly-tax-survival-guide-2026.pdf")
doc = SimpleDocTemplate(
    out, pagesize=LETTER,
    leftMargin=0.7*inch, rightMargin=0.7*inch,
    topMargin=0.9*inch, bottomMargin=0.7*inch,
    title="Quarterly Tax Survival Guide 2026",
    author="SideHustleGuard"
)

story = []

# ── COVER PAGE ──
story.append(CoverFlowable(6.5*inch, 8.5*inch))
story.append(PageBreak())

# ── TABLE OF CONTENTS ──
story.append(Paragraph("Inside this guide", page_title_style))
story.append(Paragraph("A 10-page survival map.", subtitle_style))
story.append(Spacer(1, 0.2*inch))

toc_entries = [
    ("1.", "Why quarterly taxes exist (and why W-2 people don't deal with this)"),
    ("2.", "The underpayment penalty — what it actually costs"),
    ("3.", "Safe Harbor Rule 1: 100% of last year's tax (or 110%)"),
    ("4.", "Safe Harbor Rule 2: 90% of this year's tax"),
    ("5.", "How to actually calculate your quarterly payment"),
    ("6.", "The four deadlines — and why two of them are unequally spaced"),
    ("7.", "State quarterly systems — three categories of states"),
    ("8.", "Where to pay: Direct Pay vs EFTPS vs mailed check"),
    ("9.", "What to do if you missed a quarter"),
    ("10.","Common mistakes (and the one that costs the most money)"),
    ("11.","Quick-reference card — print and keep"),
]
toc_data = [[Paragraph(f"<font color='#c9973a'><b>{num}</b></font>", toc_style),
             Paragraph(text, toc_style)] for num, text in toc_entries]
toc_table = Table(toc_data, colWidths=[0.4*inch, 6.0*inch])
toc_table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("TOPPADDING", (0,0), (-1,-1), 3),
    ("BOTTOMPADDING", (0,0), (-1,-1), 3),
]))
story.append(toc_table)
story.append(Spacer(1, 0.3*inch))
story.append(callout(
    "<b>Use this guide alongside the spreadsheet.</b> The spreadsheet calculates "
    "your numbers; this guide explains WHY those numbers matter, and what to do "
    "when reality doesn't match the math.", bg=GOLD_PALE, border=GOLD
))
story.append(PageBreak())

# ── PAGE 3: Why quarterly taxes exist ──
story.append(Paragraph("CHAPTER 1", eyebrow_style))
story.append(Paragraph("Why quarterly taxes exist", page_title_style))
story.append(Paragraph("The IRS doesn't trust you to save up. It's not personal.", subtitle_style))
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph(
    "The US tax system runs on a rule called <b>pay-as-you-go</b>. The government doesn't "
    "want to wait until April 15 to collect a year's worth of income tax. They want it spread "
    "evenly across the year — partly because they have bills to pay, and partly because they "
    "(probably correctly) believe most people won't have $15,000 sitting in a savings account "
    "when the bill comes due.",
    body_just))
story.append(Paragraph(
    "For W-2 employees, this happens invisibly: your employer holds back federal income tax, "
    "Social Security, and Medicare from every paycheck and forwards it to the IRS. By April, "
    "the W-2 employee has usually paid most or all of what they owe through withholding. "
    "Filing the return just reconciles whether they overpaid (refund) or underpaid (small balance due).",
    body_just))
story.append(Paragraph(
    "For self-employed people, there's no employer doing the withholding. Nobody is automatically "
    "sending the IRS money on your behalf. So the IRS asks you to do it yourself — four times a year. "
    "If you don't, they add a penalty.",
    body_just))
story.append(Spacer(1, 0.15*inch))
story.append(callout(
    "<b>Rule of thumb:</b> if you expect to owe the IRS more than $1,000 in tax for the year "
    "(after subtracting any W-2 withholding), you're supposed to make quarterly estimated tax payments. "
    "For most self-employed people, this kicks in the moment SE income passes about $5,000–$6,000 of net profit.",
    bg=AMBER_BG, border=AMBER))

story.append(Spacer(1, 0.15*inch))
story.append(Paragraph("Who this applies to", h2_style))
applies_items = [
    "Gig workers — DoorDash, Uber, Lyft, Instacart, Amazon Flex, Grubhub, TaskRabbit, Rover, Shipt",
    "Airbnb / Vrbo hosts whose income is subject to self-employment tax (services-heavy hosting)",
    "Etsy, eBay, Poshmark, Mercari, Shopify, and other reseller-platform sellers",
    "Freelancers — Upwork, Fiverr, direct clients",
    "Content creators — YouTube, Twitch, TikTok, Patreon, Substack, OnlyFans",
    "Anyone with a side business, consultancy, or 1099-NEC income",
    "W-2 employees with significant side income that withholding doesn't cover"
]
for item in applies_items:
    story.append(Paragraph(f"• {item}", bullet_style))

story.append(PageBreak())

# ── PAGE 4: The penalty math ──
story.append(Paragraph("CHAPTER 2", eyebrow_style))
story.append(Paragraph("What the penalty actually costs", page_title_style))
story.append(Paragraph("Smaller than horror stories suggest. Bigger than \"nothing.\"", subtitle_style))
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph(
    "The IRS underpayment penalty isn't a fixed dollar amount. It's an interest charge applied to the "
    "amount you should have paid but didn't, calculated quarterly. The rate equals the federal short-term "
    "rate plus 3% — in 2025 that worked out to roughly 8% annualized, applied per-quarter to the missed payment.",
    body_just))
story.append(Paragraph(
    "Real numbers, real scenarios:",
    body_style))

penalty_rows = [
    ["Annual tax bill", "Quarterly target", "Skipped quarters", "Approx. penalty"],
    ["$5,000",  "$1,250", "All 4",  "~$140"],
    ["$10,000", "$2,500", "All 4",  "~$275"],
    ["$15,000", "$3,750", "All 4",  "~$425"],
    ["$25,000", "$6,250", "All 4",  "~$700"],
    ["$15,000", "$3,750", "Just Q1","~$95"],
    ["$15,000", "$3,750", "Q1 + Q2","~$210"],
]
story.append(Spacer(1, 0.1*inch))
story.append(kpi_table(penalty_rows, alt=True))
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph(
    "Three things make this penalty feel worse than it looks on paper:",
    body_style))
story.append(Paragraph("• <b>It's non-deductible.</b> Unlike business expenses, you can't write off the penalty on next year's taxes. It's pure waste.", bullet_style))
story.append(Paragraph("• <b>It compounds with surprise bills.</b> If you didn't pay quarterly, you also didn't save quarterly. So the penalty hits at the same moment as the full tax bill.", bullet_style))
story.append(Paragraph("• <b>It signals you to the IRS.</b> Three years of underpayment is a known audit trigger. The penalty is small; the audit is not.", bullet_style))

story.append(Spacer(1, 0.15*inch))
story.append(callout(
    "<b>The math people miss:</b> if you genuinely can't afford to pay one quarter, paying late "
    "(after the deadline but before the next quarter) is dramatically cheaper than paying that quarter zero "
    "and catching up in April. Late payments stop the bleeding immediately.",
    bg=GOLD_PALE, border=GOLD
))
story.append(PageBreak())

# ── PAGE 5-6: Safe Harbor Rules ──
story.append(Paragraph("CHAPTER 3", eyebrow_style))
story.append(Paragraph("The two safe-harbor rules", page_title_style))
story.append(Paragraph("Hit either one. You only need one.", subtitle_style))
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph(
    "You don't have to pay the exact tax bill across the year to avoid the penalty. The IRS gives you two "
    "\"safe harbors\" — predictable formulas that, if you hit either one, mean the penalty literally cannot apply.",
    body_just))

story.append(Paragraph("Safe Harbor 1 — based on LAST year's tax", h2_style))
story.append(Paragraph(
    "Pay <b>100% of what you owed in tax last year</b>, spread across four equal quarterly payments. "
    "If you do that, you're penalty-safe for THIS year, no matter how big your income jumped.",
    body_just))
story.append(Paragraph(
    "If your prior-year AGI was over $150,000, the rule bumps up to <b>110% of last year's tax</b> "
    "(this is the IRS's way of capturing high earners who could otherwise drastically under-pay).",
    body_just))
story.append(callout(
    "<b>Why most side hustlers use this rule:</b> it doesn't care what you're earning right now. You just "
    "look at last year's return, find Form 1040 line 24 (\"Total tax\"), and divide by 4. That's your quarterly "
    "payment. Easy to plan around, easy to budget for.",
    bg=GREEN_BG, border=GREEN
))

story.append(Paragraph("Safe Harbor 2 — based on THIS year's tax", h2_style))
story.append(Paragraph(
    "Pay <b>90% of what you'll actually owe this year</b>. Because you don't know your final tax bill yet, "
    "you have to estimate it — exactly what the Tax Calculator tab in the spreadsheet does. If your payments "
    "cover 90% of that estimate, you're safe.",
    body_just))
story.append(Paragraph(
    "This rule is better when your income <b>drops significantly</b> from last year. If you earned $80K last "
    "year and only $40K this year, Safe Harbor 1 would have you paying way more than necessary. Safe Harbor 2 "
    "lets you pay based on the lower current-year reality.",
    body_just))

story.append(Spacer(1, 0.15*inch))
story.append(Paragraph("How to choose between them", h2_style))
choose_rows = [
    ["Your situation", "Easier rule", "Why"],
    ["Income growing year-over-year",      "Safe Harbor 1", "Locks in lower number"],
    ["Income flat or modestly up",         "Safe Harbor 1", "Predictable, easy to budget"],
    ["Income dropping",                    "Safe Harbor 2", "Avoids over-paying"],
    ["First year self-employed",           "Safe Harbor 2", "No prior-year baseline exists"],
    ["Wild swings, hard to forecast",      "Safe Harbor 1", "Doesn't require accurate forecast"],
]
ct = Table(choose_rows, colWidths=[2.6*inch, 1.6*inch, 2.1*inch])
ct.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), white),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 9),
    ("FONTSIZE", (0,1), (-1,-1), 10),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("TEXTCOLOR", (0,1), (-1,-1), HexColor("#333333")),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("GRID", (0,0), (-1,-1), 0.5, BORDER),
    ("BACKGROUND", (0,1), (-1,1), GOLD_PALE),
    ("BACKGROUND", (0,3), (-1,3), GOLD_PALE),
    ("BACKGROUND", (0,5), (-1,5), GOLD_PALE),
]))
story.append(ct)
story.append(PageBreak())

# ── PAGE 7: Calculating your payment ──
story.append(Paragraph("CHAPTER 4", eyebrow_style))
story.append(Paragraph("How to calculate your payment", page_title_style))
story.append(Paragraph("Step by step — but the spreadsheet does it for you.", subtitle_style))
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph(
    "Open the <b>Tax Calculator</b> tab in the spreadsheet for the live version. Here's what's actually happening "
    "underneath, so you understand what the numbers mean:",
    body_just))

steps_calc = [
    ("Step 1", "Estimate your annual net self-employment income",
     "Gross 1099 income minus all your business expenses (mileage, home office, supplies, software, fees). The "
     "spreadsheet's Income Forecast tab handles this month-by-month."),
    ("Step 2", "Calculate Self-Employment tax",
     "Multiply net SE income by 92.35%, then apply 12.4% (Social Security, capped at the SS wage base of $176,100 for 2025) "
     "plus 2.9% (Medicare, no cap). This is the part that hurts — it's the equivalent of paying both halves of FICA "
     "that an employer would normally split with you."),
    ("Step 3", "Calculate Adjusted Gross Income (AGI)",
     "Net SE income + W-2 wages − half of SE tax. The deductible half of SE tax is your only big above-the-line "
     "adjustment in this simplified model."),
    ("Step 4", "Subtract the standard deduction",
     "$15,750 single, $31,500 MFJ, $23,625 HoH (2025 amounts). What's left is your federal taxable income."),
    ("Step 5", "Apply federal tax brackets",
     "10% → 12% → 22% → 24% → 32% → 35% → 37%. Each rate applies only to the income that falls in that bracket — "
     "not your full income. The spreadsheet does this bracket-by-bracket math automatically."),
    ("Step 6", "Add state income tax",
     "Use a flat rate appropriate for your state (CA ~6%, NY ~5%, TX 0%, etc.) on your taxable income. The spreadsheet "
     "lets you override the rate if you have a more accurate number."),
    ("Step 7", "Subtract W-2 withholding (if any)",
     "If you also have a day job, your employer has been sending withholding to the IRS for you. That covers part of "
     "your obligation — only the remainder needs quarterly payments."),
    ("Step 8", "Divide by 4",
     "What's left is your annual quarterly tax obligation. Divide it across Q1–Q4 (equal payments unless your income "
     "is highly seasonal — see Chapter 6)."),
]
for label, head, body in steps_calc:
    story.append(Paragraph(f"<b><font color='#c9973a'>{label}</font></b>  <b>{head}</b>", body_style))
    story.append(Paragraph(body, ParagraphStyle("StepBody", parent=body_style, leftIndent=14, spaceAfter=10)))

story.append(PageBreak())

# ── PAGE 8: The four deadlines ──
story.append(Paragraph("CHAPTER 5", eyebrow_style))
story.append(Paragraph("The four deadlines", page_title_style))
story.append(Paragraph("Yes, they're unevenly spaced. No, it's not a typo.", subtitle_style))
story.append(Spacer(1, 0.15*inch))

deadlines = [
    ["Quarter", "Federal due", "Income period covered", "Days in period"],
    ["Q1", "April 15",    "January 1 – March 31",       "90 days"],
    ["Q2", "June 15",     "April 1 – May 31",           "61 days"],
    ["Q3", "September 15","June 1 – August 31",         "92 days"],
    ["Q4", "January 15 (next year)", "September 1 – December 31", "122 days"],
]
dt = Table(deadlines, colWidths=[0.7*inch, 1.5*inch, 2.5*inch, 1.6*inch])
dt.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), white),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 9),
    ("FONTSIZE", (0,1), (-1,-1), 10),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("GRID", (0,0), (-1,-1), 0.5, BORDER),
    ("BACKGROUND", (0,1), (-1,1), GOLD_PALE),
    ("BACKGROUND", (0,3), (-1,3), GOLD_PALE),
]))
story.append(dt)
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph(
    "Notice the unequal spacing. Q2 covers only April–May (61 days), but Q4 covers September–December (122 days). "
    "If your income is even throughout the year, you can still pay four equal quarterly amounts and you'll be fine "
    "— this is what Safe Harbor 1 effectively allows.",
    body_just))
story.append(Paragraph(
    "If your income is <b>seasonal</b> — a tax preparer who makes 80% of their money in Jan–April, a holiday "
    "Etsy seller who earns mostly in October–December — you have two options:",
    body_just))
story.append(Paragraph(
    "<b>Option A: Use Safe Harbor 1 and pay equally.</b> Doesn't care when income arrives. Easiest.",
    bullet_style))
story.append(Paragraph(
    "<b>Option B: Use Form 2210 Schedule AI (\"Annualized Income Installment Method\")</b> to pay less in slow quarters "
    "and more in busy ones. This is allowed but tedious — most people use Option A.",
    bullet_style))

story.append(Spacer(1, 0.2*inch))
story.append(callout(
    "<b>If a deadline falls on a weekend or holiday,</b> it shifts to the next business day. April 15, 2026 is a Wednesday, "
    "but check the calendar each year — Emancipation Day, weekends, and other federal holidays can move deadlines.",
    bg=AMBER_BG, border=AMBER
))

story.append(PageBreak())

# ── PAGE 9: State systems ──
story.append(Paragraph("CHAPTER 6", eyebrow_style))
story.append(Paragraph("State quarterly tax systems", page_title_style))
story.append(Paragraph("Three categories of states. Find yours.", subtitle_style))
story.append(Spacer(1, 0.15*inch))

# Category 1
story.append(Paragraph("Category 1 — States with no income tax (skip this entirely)", h2_style))
story.append(Paragraph(
    "These nine states don't have a personal income tax, so there's nothing to pay quarterly:",
    body_style))
story.append(Paragraph(
    "<b>Alaska · Florida · Nevada · New Hampshire · South Dakota · Tennessee · Texas · Washington · Wyoming</b>",
    callout_style))
story.append(Paragraph(
    "New Hampshire used to tax interest/dividends only; that's been phasing out. If you live in any of these, ignore "
    "the State Quarterly tab in the spreadsheet — set the state rate to 0% in Setup and you're done.",
    body_just))

# Category 2
story.append(Paragraph("Category 2 — States that mirror federal due dates (most states)", h2_style))
story.append(Paragraph(
    "These states copy the federal quarterly schedule exactly. Same dates, same logic — you just send a separate "
    "payment to the state revenue department each time you pay the IRS.",
    body_just))
story.append(Paragraph(
    "<b>Common ones:</b> California (FTB), New York (Tax & Finance), Illinois, Massachusetts, New Jersey, Pennsylvania, "
    "Virginia, Georgia, Arizona, Colorado, Oregon, Maryland, Minnesota, North Carolina, Ohio, Wisconsin, Michigan.",
    body_just))

# Category 3
story.append(Paragraph("Category 3 — States with weird schedules or thresholds", h2_style))
story.append(Paragraph(
    "A handful of states have non-standard quarterly rules. If you're in one of these, check the state's "
    "estimated tax instructions specifically:",
    body_style))
story.append(Paragraph("• <b>Iowa</b> — Q1 due April 30 (not 15).", bullet_style))
story.append(Paragraph("• <b>Hawaii</b> — Standard schedule but tighter penalty calculations.", bullet_style))
story.append(Paragraph("• <b>Indiana</b> — Different forms for residents vs non-residents.", bullet_style))
story.append(Paragraph("• <b>Louisiana</b> — Uses a different penalty formula.", bullet_style))

story.append(Spacer(1, 0.15*inch))
story.append(callout(
    "<b>Universal trick to find your state's portal:</b> Google \"[your state] estimated tax payment\" — it's "
    "always a one-page government site. California's is FTB Web Pay. New York's is via NY.gov or the IT-2105 voucher. "
    "Most states accept ACH/bank transfer in addition to checks.",
    bg=GOLD_PALE, border=GOLD
))

story.append(PageBreak())

# ── PAGE 10: Where to pay ──
story.append(Paragraph("CHAPTER 7", eyebrow_style))
story.append(Paragraph("How to actually send the money", page_title_style))
story.append(Paragraph("Three ways. One is best.", subtitle_style))
story.append(Spacer(1, 0.15*inch))

# Method 1
story.append(Paragraph("IRS Direct Pay (easiest)", h2_style))
story.append(Paragraph(
    "<b>irs.gov/payments/direct-pay</b><br/>"
    "Free. Takes 2 minutes per payment. Pulls directly from a bank account. No login required — just enter your "
    "Social Security number, name, and the amount. Confirmation emailed instantly. Save the confirmation.",
    body_just))
story.append(Paragraph(
    "<b>Pros:</b> Fast, free, no account needed.<br/>"
    "<b>Cons:</b> No permanent payment history (you rely on emails). Each payment is a separate flow — easy to "
    "miss confirming when busy.",
    body_just))

# Method 2
story.append(Paragraph("EFTPS (best for ongoing use)", h2_style))
story.append(Paragraph(
    "<b>eftps.gov</b><br/>"
    "Also free. One-time enrollment (they mail you a PIN — takes ~10 days). After that, you log in, enter a payment, done. "
    "Keeps a permanent payment history forever.",
    body_just))
story.append(Paragraph(
    "<b>Pros:</b> Permanent history, can schedule payments in advance, ideal if you'll be paying quarterly for years.<br/>"
    "<b>Cons:</b> Enrollment isn't instant. If you need to pay today and aren't enrolled, use Direct Pay this time.",
    body_just))

# Method 3
story.append(Paragraph("Mail a check with Form 1040-ES", h2_style))
story.append(Paragraph(
    "Old school. Print the voucher from Form 1040-ES, write a check made out to \"United States Treasury,\" "
    "mail it to the IRS address listed on the voucher for your state. Postmarked-by-the-due-date counts.",
    body_just))
story.append(Paragraph(
    "<b>Pros:</b> No online account at all.<br/>"
    "<b>Cons:</b> Mail can be slow, can be lost, no instant confirmation. Use only if you don't have a bank account or "
    "really hate computers.",
    body_just))

story.append(Spacer(1, 0.15*inch))
story.append(callout(
    "<b>My pick:</b> Direct Pay for your first 1–2 quarters while you're still figuring out the rhythm. "
    "Then enroll in EFTPS for permanent payment history once you're committed.",
    bg=GREEN_BG, border=GREEN
))

story.append(PageBreak())

# ── PAGE 11: If you missed a quarter ──
story.append(Paragraph("CHAPTER 8", eyebrow_style))
story.append(Paragraph("If you missed a quarter", page_title_style))
story.append(Paragraph("Calmly. Here's what to do.", subtitle_style))
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph(
    "Missing a quarterly payment isn't the end of the world. Here's what actually happens:",
    body_just))

story.append(Paragraph("Step 1 — Pay as soon as you can.", h2_style))
story.append(Paragraph(
    "The underpayment penalty accrues daily. Paying a missed quarter even 30 days late costs dramatically less than "
    "waiting until the next deadline. There's no \"backdating\" of payments, but stopping the clock matters.",
    body_just))

story.append(Paragraph("Step 2 — Don't try to label it.", h2_style))
story.append(Paragraph(
    "When you pay through Direct Pay or EFTPS, you select \"Estimated Tax (1040-ES)\" and the current tax year. "
    "The IRS doesn't ask which quarter; the payment just gets applied to your account. The penalty calculation "
    "happens separately when you file your return.",
    body_just))

story.append(Paragraph("Step 3 — Adjust your remaining quarters.", h2_style))
story.append(Paragraph(
    "If you missed Q1, consider front-loading Q2 — pay the missed amount plus Q2's normal amount in June. This "
    "doesn't undo the Q1 penalty (which already accrued), but it does shrink your year-end balance.",
    body_just))

story.append(Paragraph("Step 4 — Calculate the actual penalty if you want to.", h2_style))
story.append(Paragraph(
    "Form 2210 is the IRS's penalty calculation worksheet. It's optional — if you don't include it with your return, "
    "the IRS calculates the penalty for you and sends a bill. For most people, letting the IRS calculate it is fine "
    "(and sometimes lower than the worst-case estimate).",
    body_just))

story.append(Spacer(1, 0.15*inch))
story.append(callout(
    "<b>If you're chronically behind:</b> consider increasing your day-job W-2 withholding instead. Withholding "
    "is treated as if it were paid evenly throughout the year — even if it was actually all in December — so it "
    "can retroactively \"fix\" a missed quarter. File a new W-4 with your employer to bump it up.",
    bg=GOLD_PALE, border=GOLD
))

story.append(PageBreak())

# ── PAGE 12: Common mistakes ──
story.append(Paragraph("CHAPTER 9", eyebrow_style))
story.append(Paragraph("Common mistakes", page_title_style))
story.append(Paragraph("Including the one that costs the most.", subtitle_style))
story.append(Spacer(1, 0.15*inch))

mistakes = [
    ("Forgetting that SE tax exists at all.",
     "Self-employment tax (15.3% on most of your net SE income) is in addition to federal income tax — not instead "
     "of it. Many first-year self-employed people calculate their income tax, send that as quarterlies, and get "
     "blindsided in April by a $5,000–$10,000 SE tax bill they didn't budget for. The spreadsheet calculates "
     "both — make sure both are included in your quarterly target."),
    ("Using gross income instead of net.",
     "Quarterly tax is calculated on your NET profit (gross minus deductions), not your gross 1099 income. A "
     "DoorDash driver who grossed $58,000 but had $15,400 in mileage deductions only pays tax on $42,600. Forgetting "
     "the deductions makes you overpay by thousands."),
    ("Trusting platform 1099-K numbers as final.",
     "1099-K and 1099-NEC numbers report gross transaction amounts, not your taxable income. They don't subtract "
     "platform fees, returns, refunds, COGS, or any expense. Use your own records as the source of truth."),
    ("Paying federal but ignoring state.",
     "State quarterly tax is a separate payment to a separate place. The IRS doesn't share with your state. If you "
     "live in a state with income tax (most of them), you have two quarterly payments to make each cycle, not one."),
    ("Setting up Direct Pay but not saving the confirmation.",
     "Direct Pay only emails the confirmation. If your inbox is chaos, you'll lose proof of payment. Take a screenshot "
     "or forward the confirmation to a tagged folder/label. The spreadsheet's Payment Log tab is for this — fill it in "
     "right after each payment."),
    ("Not adjusting when income changes dramatically.",
     "If you blew past last year's income by July, your initial quarterlies (set off last year's tax) are no longer "
     "enough. You won't get a penalty — Safe Harbor 1 still protects you — but you'll owe a HUGE balance in April. "
     "Start saving the difference now so April doesn't bury you."),
    ("Mixing personal and business bank accounts.",
     "This isn't directly a quarterly tax issue, but it makes everything harder. Open a separate bank account "
     "for business income and expenses. Pay yourself a transfer, pay quarterlies from the business account. "
     "Bookkeeping for the year suddenly takes 30 minutes instead of 30 hours."),
]
for title, body in mistakes:
    story.append(Paragraph(f"<b>{title}</b>", h2_style))
    story.append(Paragraph(body, body_just))

story.append(PageBreak())

# ── PAGE 13: Quick reference card ──
story.append(Paragraph("CHAPTER 10", eyebrow_style))
story.append(Paragraph("Quick-reference card", page_title_style))
story.append(Paragraph("Print this. Tape it inside a folder. Done.", subtitle_style))
story.append(Spacer(1, 0.2*inch))

ref_data = [
    ["Item", "Value"],
    ["Q1 deadline", "April 15"],
    ["Q2 deadline", "June 15"],
    ["Q3 deadline", "September 15"],
    ["Q4 deadline", "January 15 (next year)"],
    ["Pay-as-you-go threshold", "Expect to owe more than $1,000 in tax"],
    ["SE tax rate", "12.4% Social Security (up to $176,100) + 2.9% Medicare = 15.3%"],
    ["Federal Direct Pay", "irs.gov/payments/direct-pay"],
    ["EFTPS", "eftps.gov"],
    ["Safe Harbor 1 (most people)", "100% of last year's tax (110% if AGI > $150K)"],
    ["Safe Harbor 2 (income dropping)", "90% of this year's projected tax"],
    ["Underpayment penalty rate (2025)", "~8% annualized, charged per-quarter on missed amount"],
    ["Form for quarterly voucher", "Form 1040-ES"],
    ["Where to record payments at tax time", "Form 1040, line 26"],
]
ref_table = Table(ref_data, colWidths=[2.7*inch, 4.0*inch])
ref_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), white),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 10),
    ("FONTSIZE", (0,1), (-1,-1), 10),
    ("FONTNAME", (0,1), (0,-1), "Helvetica-Bold"),
    ("FONTNAME", (1,1), (1,-1), "Helvetica"),
    ("TEXTCOLOR", (0,1), (-1,-1), HexColor("#333333")),
    ("TOPPADDING", (0,0), (-1,-1), 9),
    ("BOTTOMPADDING", (0,0), (-1,-1), 9),
    ("LEFTPADDING", (0,0), (-1,-1), 12),
    ("RIGHTPADDING", (0,0), (-1,-1), 12),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("GRID", (0,0), (-1,-1), 0.5, BORDER),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [CREAM, GOLD_PALE]),
]))
story.append(ref_table)

story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(
    "<i>Tax brackets, deductions, and the SS wage base change annually. The Setup tab in your spreadsheet has these "
    "as editable fields — update them each January when the IRS publishes the new numbers (search \"IRS standard "
    "deduction 2027\" or whatever year applies). The structure of this guide doesn't change year to year, but the "
    "specific dollar amounts do.</i>",
    muted_style
))

story.append(Spacer(1, 0.4*inch))
story.append(divider())
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph(
    "<b>Educational only. Not legal or tax advice.</b> Every situation has details this guide doesn't cover. "
    "For complex returns (multiple businesses, large investment income, QBI deduction optimization, foreign income, "
    "AMT), consult a CPA. The Quarterly Tax System spreadsheet and this guide get you 90% of the way; a CPA "
    "closes the last 10%.",
    muted_style
))
story.append(Spacer(1, 0.15*inch))
story.append(Paragraph(
    "Made by <b>SideHustleGuard</b> · sidehustleguard.com · Questions? richard@sidehustleguard.com",
    muted_style
))

# ── BUILD ──
doc.build(story, onFirstPage=on_first_page, onLaterPages=on_later_pages)
print(f"Saved: {out}")
print(f"Size:  {os.path.getsize(out)/1024:.1f} KB")
