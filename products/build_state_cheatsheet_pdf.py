"""
Build the 50-state + DC quarterly tax cheat sheet PDF.
Output: state-quarterly-tax-cheat-sheet.pdf (landscape, 2 pages)
"""
from reportlab.lib.pagesizes import landscape, LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
import os

NAVY      = HexColor("#1c2b4a")
GOLD      = HexColor("#c9973a")
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

# ── DATA ──
# (state, top_rate_pct_or_None, portal_or_form, special_note)
# None for top_rate means "no state income tax."
# Notes kept short (~25 chars max) to fit the column.
STATES = [
    ("Alabama",         5.00, "myalabamataxes.alabama.gov",  "Form 40ES"),
    ("Alaska",          None, "—",                           "No income tax"),
    ("Arizona",         2.50, "aztaxes.gov",                 "Flat tax (Form 140ES)"),
    ("Arkansas",        4.40, "atap.arkansas.gov",           "Form AR1000ES"),
    ("California",      13.3, "ftb.ca.gov/pay",              "FTB Web Pay / Form 540-ES"),
    ("Colorado",        4.40, "tax.colorado.gov",            "Form 104EP"),
    ("Connecticut",     6.99, "portal.ct.gov/drs",           "Form CT-1040ES"),
    ("Delaware",        6.60, "revenue.delaware.gov",        "Form 200-ES"),
    ("DC",              10.75,"mytax.dc.gov",                "Form D-40ES"),
    ("Florida",         None, "—",                           "No income tax"),
    ("Georgia",         5.39, "gtc.dor.ga.gov",              "Form 500-ES"),
    ("Hawaii",          11.0, "hitax.hawaii.gov",            "Form N-200V"),
    ("Idaho",           5.80, "tax.idaho.gov",               "Form 51"),
    ("Illinois",        4.95, "mytax.illinois.gov",          "Form IL-1040-ES (flat)"),
    ("Indiana",         3.05, "dor.in.gov/online-services",  "Form ES-40"),
    ("Iowa",            5.70, "tax.iowa.gov",                "Q1 due Apr 30, not 15"),
    ("Kansas",          5.70, "ksrevenue.gov",               "Form K-40ES"),
    ("Kentucky",        4.00, "revenue.ky.gov",              "Form 740-ES"),
    ("Louisiana",       4.25, "revenue.louisiana.gov",       "Form IT-540ES"),
    ("Maine",           7.15, "maine.gov/revenue",           "Form 1040ES-ME"),
    ("Maryland",        5.75, "marylandtaxes.gov",           "Form 502D"),
    ("Massachusetts",   9.00, "mtc.dor.state.ma.us",         "Form 1-ES"),
    ("Michigan",        4.25, "michigan.gov/treasury",       "Form MI-1040ES"),
    ("Minnesota",       9.85, "revenue.state.mn.us",         "Form M14"),
    ("Mississippi",     4.40, "tap.dor.ms.gov",              "Form 80-106"),
    ("Missouri",        4.70, "dor.mo.gov",                  "Form MO-1040ES"),
    ("Montana",         5.90, "mtrevenue.gov",               "Form 2-ES"),
    ("Nebraska",        5.84, "revenue.nebraska.gov",        "Form 1040N-ES"),
    ("Nevada",          None, "—",                           "No income tax"),
    ("New Hampshire",   None, "—",                           "No tax on wages*"),
    ("New Jersey",      10.75,"state.nj.us/treasury/taxation","Form NJ-1040-ES"),
    ("New Mexico",      5.90, "tax.newmexico.gov",           "Form PIT-ES"),
    ("New York",        10.9, "tax.ny.gov",                  "Form IT-2105"),
    ("North Carolina",  4.50, "ncdor.gov",                   "Form NC-40"),
    ("North Dakota",    2.50, "tax.nd.gov",                  "Form ND-1ES"),
    ("Ohio",            3.50, "tax.ohio.gov",                "Form IT 1040ES"),
    ("Oklahoma",        4.75, "oktap.tax.ok.gov",            "Form OW-8-ES"),
    ("Oregon",          9.90, "oregon.gov/dor",              "Form OR-40-V"),
    ("Pennsylvania",    3.07, "mypath.pa.gov",               "Form PA-40ESR (flat)"),
    ("Rhode Island",    5.99, "tax.ri.gov",                  "Form RI-1040ES"),
    ("South Carolina",  6.20, "dor.sc.gov",                  "Form SC1040ES"),
    ("South Dakota",    None, "—",                           "No income tax"),
    ("Tennessee",       None, "—",                           "No income tax"),
    ("Texas",           None, "—",                           "No income tax"),
    ("Utah",            4.55, "tap.utah.gov",                "Flat tax (Form TC-546)"),
    ("Vermont",         8.75, "tax.vermont.gov",             "Form IN-114"),
    ("Virginia",        5.75, "tax.virginia.gov",            "Form 760ES"),
    ("Washington",      None, "—",                           "No income tax"),
    ("West Virginia",   4.82, "mytaxes.wvtax.gov",           "Form IT-140ES"),
    ("Wisconsin",       7.65, "revenue.wi.gov",              "Form 1-ES"),
    ("Wyoming",         None, "—",                           "No income tax"),
]

# ── STYLES ──
ss = getSampleStyleSheet()
title_style = ParagraphStyle("T", parent=ss["Normal"], fontName="Times-Bold", fontSize=24, leading=28, textColor=NAVY, spaceAfter=4)
sub_style   = ParagraphStyle("S", parent=ss["Normal"], fontName="Helvetica", fontSize=10.5, leading=14, textColor=MUTED, spaceAfter=10)
eye_style   = ParagraphStyle("E", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=9, leading=11, textColor=GOLD, spaceAfter=2)
h2_style    = ParagraphStyle("H2", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=NAVY, spaceBefore=8, spaceAfter=4)
body_style  = ParagraphStyle("B", parent=ss["Normal"], fontName="Helvetica", fontSize=9.5, leading=13, textColor=HexColor("#333333"), spaceAfter=6)
foot_style  = ParagraphStyle("F", parent=ss["Normal"], fontName="Helvetica-Oblique", fontSize=8, leading=11, textColor=MUTED, spaceBefore=8)

def divider(width=10.0):
    t = Table([[" "]], colWidths=[width*inch], rowHeights=[2])
    t.setStyle(TableStyle([("LINEBELOW", (0,0), (-1,-1), 1, GOLD)]))
    return t

def make_table(rows_data):
    """Build a styled state table from a list of [state, rate, portal, note]."""
    header = [["State", "Income tax?", "Top rate", "How to pay (portal / form)", "Notes"]]
    body = []
    fills = []  # tuples (row_idx, color)
    for i, (state, rate, portal, note) in enumerate(rows_data):
        if rate is None:
            tax_label = "No"
            rate_str = "—"
            fills.append((i + 1, CREAM_D))  # gray-cream for no-tax states
        else:
            tax_label = "Yes"
            rate_str = f"{rate:.2f}%"
            if i % 2 == 1:
                fills.append((i + 1, GOLD_PALE))
        body.append([state, tax_label, rate_str, portal, note])
    data = header + body
    t = Table(data, colWidths=[1.2*inch, 0.7*inch, 0.7*inch, 1.7*inch, 1.6*inch])
    style = [
        # Header
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("TEXTCOLOR",  (0,0), (-1,0), white),
        ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1,0), 8.5),
        # Body
        ("FONTNAME",   (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",   (0,1), (-1,-1), 7.5),
        ("FONTNAME",   (0,1), (0,-1), "Helvetica-Bold"),  # state column bold
        ("TEXTCOLOR",  (0,1), (-1,-1), HexColor("#333333")),
        # Layout
        ("ALIGN",      (1,0), (2,-1), "CENTER"),
        ("ALIGN",      (0,0), (0,-1), "LEFT"),
        ("ALIGN",      (3,0), (-1,-1), "LEFT"),
        ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("GRID",       (0,0), (-1,-1), 0.5, BORDER),
    ]
    for row_idx, color in fills:
        style.append(("BACKGROUND", (0, row_idx), (-1, row_idx), color))
    t.setStyle(TableStyle(style))
    return t

# ──────────────────────────────────────────────────────────────────────
# BUILD
# ──────────────────────────────────────────────────────────────────────
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state-quarterly-tax-cheat-sheet.pdf")
doc = SimpleDocTemplate(
    out, pagesize=landscape(LETTER),
    leftMargin=0.5*inch, rightMargin=0.5*inch,
    topMargin=0.55*inch, bottomMargin=0.5*inch,
    title="State Quarterly Tax Cheat Sheet",
    author="SideHustleGuard"
)

story = []

# Header
story.append(Paragraph("BONUS · QUARTERLY TAX SYSTEM 2026", eye_style))
story.append(Paragraph("State Quarterly Tax Cheat Sheet", title_style))
story.append(Paragraph(
    "All 50 states + DC. Where to pay, top marginal rate, and the exception cases you'd otherwise have to Google. "
    "Most states mirror federal due dates (Apr 15 / Jun 15 / Sep 15 / Jan 15).",
    sub_style))

# Split states alphabetically into two columns (left + right of page)
half = (len(STATES) + 1) // 2  # 26 on left, 25 on right
left = STATES[:half]
right = STATES[half:]

# Two side-by-side tables
left_tbl = make_table(left)
right_tbl = make_table(right)
two_col = Table(
    [[left_tbl, right_tbl]],
    colWidths=[5.0*inch, 5.0*inch],
)
two_col.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 4),
    ("TOPPADDING", (0,0), (-1,-1), 0),
    ("BOTTOMPADDING", (0,0), (-1,-1), 0),
]))
story.append(two_col)

# Bottom notes
story.append(Spacer(1, 8))
story.append(divider(10.0))
story.append(Spacer(1, 6))

notes_table = Table([[
    Paragraph(
        "<b>* New Hampshire</b> taxes only interest and dividend income, and that's been phasing out — most NH "
        "residents owe nothing at the state level on wages or 1099 income. "
        "<b>Top rates shown</b> are top marginal rates as of late 2025 — most filers fall in lower brackets. "
        "Your effective rate is usually 40–60% of the top rate. Update the State rate in your Quarterly Tax "
        "System's Setup tab with your actual bracket if you want precision.",
        body_style),
    Paragraph(
        "<b>Due dates:</b> if not noted otherwise, the state mirrors the federal calendar (Apr 15 / Jun 15 / "
        "Sep 15 / Jan 15 of the following year). <b>Iowa</b> is the main exception — Q1 is due April 30 instead "
        "of April 15. Several states' deadlines move to the next business day if they fall on a weekend or "
        "holiday — check each year.",
        body_style),
]], colWidths=[5.0*inch, 5.0*inch])
notes_table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
]))
story.append(notes_table)

story.append(Spacer(1, 4))
story.append(Paragraph(
    "Educational only — not legal or tax advice. State tax laws change every year. Verify current rates "
    "and forms at your state's revenue department website before filing. "
    "Made by SideHustleGuard · sidehustleguard.com",
    foot_style))

doc.build(story)
print(f"Saved: {out}")
print(f"Size:  {os.path.getsize(out)/1024:.1f} KB")
