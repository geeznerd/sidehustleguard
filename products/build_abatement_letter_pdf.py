"""
Build the IRS First-Time Penalty Abatement letter template.
Output: penalty-abatement-letter-template.pdf (2 pages — explainer + letter)
        penalty-abatement-letter-template.txt (plain-text letter for easy editing)
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
import os

NAVY      = HexColor("#1c2b4a")
GOLD      = HexColor("#c9973a")
GOLD_PALE = HexColor("#fdf5e8")
CREAM     = HexColor("#faf8f4")
GREEN     = HexColor("#276944")
GREEN_BG  = HexColor("#eaf5ef")
AMBER     = HexColor("#a86c0a")
AMBER_BG  = HexColor("#fef6e8")
MUTED     = HexColor("#6b7a96")
BORDER    = HexColor("#e5e7ed")

ss = getSampleStyleSheet()
title_style = ParagraphStyle("T", parent=ss["Normal"], fontName="Times-Bold", fontSize=24, leading=28, textColor=NAVY, spaceAfter=4)
sub_style   = ParagraphStyle("S", parent=ss["Normal"], fontName="Helvetica", fontSize=11, leading=15, textColor=MUTED, spaceAfter=12)
eye_style   = ParagraphStyle("E", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=9, leading=11, textColor=GOLD, spaceAfter=2)
h2_style    = ParagraphStyle("H2", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=12, leading=16, textColor=NAVY, spaceBefore=8, spaceAfter=4)
body_style  = ParagraphStyle("B", parent=ss["Normal"], fontName="Helvetica", fontSize=10.5, leading=15, textColor=HexColor("#333333"), spaceAfter=8, alignment=TA_JUSTIFY)
bullet_style= ParagraphStyle("Bu", parent=body_style, leftIndent=14, bulletIndent=2, spaceAfter=4)
letter_style= ParagraphStyle("L", parent=ss["Normal"], fontName="Helvetica", fontSize=10.5, leading=15, textColor=HexColor("#222222"), spaceAfter=10, alignment=TA_LEFT)
bracket_style = ParagraphStyle("BR", parent=letter_style, textColor=GOLD)
foot_style  = ParagraphStyle("F", parent=ss["Normal"], fontName="Helvetica-Oblique", fontSize=8.5, leading=11, textColor=MUTED, spaceBefore=10)

def callout(text, bg=AMBER_BG, border=AMBER):
    t = Table([[Paragraph(text, body_style)]], colWidths=[7.0*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("LEFTPADDING", (0,0), (-1,-1), 14),
        ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("LINEBEFORE", (0,0), (0,-1), 3, border),
    ]))
    return t

def divider():
    t = Table([[" "]], colWidths=[7.0*inch], rowHeights=[2])
    t.setStyle(TableStyle([("LINEBELOW", (0,0), (-1,-1), 1, GOLD)]))
    return t

# ──────────────────────────────────────────────────────────────────────
# PDF
# ──────────────────────────────────────────────────────────────────────
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "penalty-abatement-letter-template.pdf")
doc = SimpleDocTemplate(
    out, pagesize=LETTER,
    leftMargin=0.7*inch, rightMargin=0.7*inch,
    topMargin=0.7*inch, bottomMargin=0.6*inch,
    title="IRS First-Time Penalty Abatement Letter Template",
    author="SideHustleGuard"
)

story = []

# ── PAGE 1: Explainer ──
story.append(Paragraph("BONUS · QUARTERLY TAX SYSTEM", eye_style))
story.append(Paragraph("If you got hit with an underpayment penalty<br/>— ask the IRS to refund it.", title_style))
story.append(Paragraph(
    "The First-Time Abatement (FTA) program. The letter most CPAs charge $200+ to write. Yours, ready to send.",
    sub_style))
story.append(divider())
story.append(Spacer(1, 8))

story.append(Paragraph("What is First-Time Penalty Abatement?", h2_style))
story.append(Paragraph(
    "FTA is an IRS administrative waiver that <b>removes most penalties</b> if you have a clean compliance "
    "record for the prior 3 years. It applies to failure-to-file, failure-to-pay, and (most importantly for "
    "self-employed people) <b>the estimated tax underpayment penalty</b>. The IRS has been administering this "
    "since 2001. Most taxpayers who qualify never ask for it — because they don't know it exists.",
    body_style))

story.append(Paragraph("Do you qualify?", h2_style))
story.append(Paragraph("You qualify for FTA if <b>ALL three</b> of these are true:", body_style))
story.append(Paragraph("• You filed all required returns (or filed an extension) for the past 3 years.", bullet_style))
story.append(Paragraph("• You paid (or arranged to pay) any tax due for those 3 years.", bullet_style))
story.append(Paragraph("• You had <b>no penalties</b> in those 3 years — or any penalties you did have were removed under FTA itself.", bullet_style))

story.append(Spacer(1, 4))
story.append(callout(
    "<b>Important:</b> FTA only applies to ONE tax period at a time. If the IRS hit you with penalties for both "
    "Q2 and Q3 of the same year, FTA waives them both. But if you got penalties in 2024 AND 2025, FTA only "
    "applies to one of those years — pick the year with the larger penalty.",
    bg=GOLD_PALE, border=GOLD))

story.append(Paragraph("How to use this template", h2_style))
story.append(Paragraph("1. <b>Get the IRS notice in front of you.</b> The letter they sent you assessing the penalty.", body_style))
story.append(Paragraph("2. <b>Fill in the bracketed fields</b> on page 2 with your information from the notice.", body_style))
story.append(Paragraph("3. <b>Sign and date it.</b> Mail it to the IRS address on the original penalty notice (usually the IRS office that issued it). Keep a copy.", body_style))
story.append(Paragraph("4. <b>Expect a response in 2–4 months.</b> Most FTA requests are approved when the qualification rules are met. If approved, the IRS removes the penalty and refunds any amount you already paid.", body_style))

story.append(Spacer(1, 6))
story.append(callout(
    "<b>Faster alternative:</b> You can also request FTA <i>by phone</i> by calling the IRS at "
    "<b>1-800-829-1040</b> (individuals). Many agents can approve FTA on the call. But the written letter is "
    "the better paper trail — and required if your case is complex or you've been denied verbally.",
    bg=GREEN_BG, border=GREEN))

story.append(PageBreak())

# ── PAGE 2: The letter ──
story.append(Paragraph("THE LETTER · PAGE 2 OF 2", eye_style))
story.append(Paragraph("Penalty Abatement Request", title_style))
story.append(Paragraph(
    "Replace every <font color='#c9973a'><b>[BRACKETED ITEM]</b></font> with your information. "
    "Print, sign, and mail to the IRS address on your original penalty notice.",
    sub_style))
story.append(divider())
story.append(Spacer(1, 10))

# Letter body
letter_lines = [
    "<font color='#c9973a'><b>[YOUR FULL NAME]</b></font><br/>"
    "<font color='#c9973a'><b>[YOUR STREET ADDRESS]</b></font><br/>"
    "<font color='#c9973a'><b>[CITY, STATE, ZIP]</b></font><br/>"
    "<font color='#c9973a'><b>[PHONE]</b></font>",
    "<font color='#c9973a'><b>[TODAY'S DATE]</b></font>",
    "Internal Revenue Service<br/>"
    "<font color='#c9973a'><b>[IRS ADDRESS FROM YOUR PENALTY NOTICE]</b></font>",
    "<b>Re: Request for First-Time Penalty Abatement</b><br/>"
    "Taxpayer: <font color='#c9973a'><b>[YOUR NAME]</b></font><br/>"
    "SSN/EIN: <font color='#c9973a'><b>[YOUR SSN OR EIN]</b></font><br/>"
    "Tax form: <font color='#c9973a'><b>[FORM NUMBER, e.g., 1040]</b></font><br/>"
    "Tax period: <font color='#c9973a'><b>[TAX YEAR, e.g., December 31, 2025]</b></font><br/>"
    "Notice / letter number: <font color='#c9973a'><b>[NOTICE NUMBER FROM IRS LETTER]</b></font>",
    "To Whom It May Concern:",
    "I am writing to request abatement of the penalty assessed in the notice referenced above, "
    "in the amount of <font color='#c9973a'><b>[PENALTY AMOUNT]</b></font>, under the IRS First-Time "
    "Abatement (FTA) administrative waiver as described in Internal Revenue Manual section 20.1.1.3.6.1.",
    "I qualify for First-Time Abatement because all three of the following statements are true:",
    "1. I have filed all required tax returns (or filed valid extensions) for the three tax years "
    "preceding the period for which I am requesting abatement.",
    "2. I have paid, or arranged to pay through an installment agreement, all tax due for those three "
    "preceding tax years.",
    "3. I have not been assessed any penalties (or any prior penalties were themselves abated) during "
    "those three preceding tax years.",
    "Based on these facts, I respectfully request that the IRS waive the penalty assessed for the "
    "<font color='#c9973a'><b>[TAX YEAR]</b></font> tax period and refund any amount I have already paid "
    "toward this penalty.",
    "If you require additional information or documentation, please contact me at the phone number "
    "above. Thank you for your time and consideration.",
    "Sincerely,",
    "<br/><br/><font color='#c9973a'><b>[YOUR SIGNATURE]</b></font><br/>"
    "<font color='#c9973a'><b>[YOUR PRINTED NAME]</b></font>",
]
for line in letter_lines:
    story.append(Paragraph(line, letter_style))

# Footer note
story.append(Spacer(1, 14))
story.append(divider())
story.append(Paragraph(
    "<b>Tips before mailing:</b> Send via Certified Mail with Return Receipt — costs ~$8, gives you proof "
    "of delivery and the date. Keep a complete copy of the letter and the IRS notice. If you don't hear "
    "back in 90 days, call 1-800-829-1040 with your notice number and ask for status.",
    body_style))
story.append(Paragraph(
    "Educational tool only — not legal or tax advice. The FTA program rules can change; verify current "
    "qualification rules at irs.gov before sending. For complex situations or large penalty amounts, "
    "consult a CPA or enrolled agent.",
    foot_style))
story.append(Paragraph(
    "Made by SideHustleGuard · sidehustleguard.com",
    foot_style))

doc.build(story)
print(f"Saved: {out}")
print(f"Size:  {os.path.getsize(out)/1024:.1f} KB")

# ──────────────────────────────────────────────────────────────────────
# TXT version (copy-paste editable)
# ──────────────────────────────────────────────────────────────────────
txt = """IRS FIRST-TIME PENALTY ABATEMENT — LETTER TEMPLATE
═══════════════════════════════════════════════════════════════════

REPLACE EVERY [BRACKETED ITEM] WITH YOUR INFORMATION.
Print, sign, and mail to the IRS address on your original penalty notice.

═══════════════════════════════════════════════════════════════════


[YOUR FULL NAME]
[YOUR STREET ADDRESS]
[CITY, STATE, ZIP]
[PHONE]


[TODAY'S DATE]


Internal Revenue Service
[IRS ADDRESS FROM YOUR PENALTY NOTICE]


Re: Request for First-Time Penalty Abatement
Taxpayer: [YOUR NAME]
SSN/EIN: [YOUR SSN OR EIN]
Tax form: [FORM NUMBER, e.g., 1040]
Tax period: [TAX YEAR, e.g., December 31, 2025]
Notice / letter number: [NOTICE NUMBER FROM IRS LETTER]


To Whom It May Concern:

I am writing to request abatement of the penalty assessed in the notice referenced above, in the amount of [PENALTY AMOUNT], under the IRS First-Time Abatement (FTA) administrative waiver as described in Internal Revenue Manual section 20.1.1.3.6.1.

I qualify for First-Time Abatement because all three of the following statements are true:

1. I have filed all required tax returns (or filed valid extensions) for the three tax years preceding the period for which I am requesting abatement.

2. I have paid, or arranged to pay through an installment agreement, all tax due for those three preceding tax years.

3. I have not been assessed any penalties (or any prior penalties were themselves abated) during those three preceding tax years.

Based on these facts, I respectfully request that the IRS waive the penalty assessed for the [TAX YEAR] tax period and refund any amount I have already paid toward this penalty.

If you require additional information or documentation, please contact me at the phone number above. Thank you for your time and consideration.


Sincerely,



[YOUR SIGNATURE]
[YOUR PRINTED NAME]


═══════════════════════════════════════════════════════════════════
TIPS BEFORE MAILING
═══════════════════════════════════════════════════════════════════

• Send via Certified Mail with Return Receipt (~$8). Proof of delivery
  matters if the IRS claims they never got it.

• Keep a complete copy of this letter AND your original IRS penalty
  notice in the same folder.

• If you don't hear back in 90 days, call 1-800-829-1040 with your
  notice number and ask for status.

• Faster alternative: call the IRS directly. Many agents can approve
  FTA on the phone in a single call. The written letter is the safer
  paper trail if your case is complex or you've been denied verbally.


Educational tool only — not legal or tax advice. The FTA program rules
can change; verify current qualification rules at irs.gov before sending.

Made by SideHustleGuard · sidehustleguard.com
"""
txt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "penalty-abatement-letter-template.txt")
with open(txt_path, "w", encoding="utf-8") as f:
    f.write(txt)
print(f"Saved: {txt_path}")
print(f"Size:  {os.path.getsize(txt_path)/1024:.1f} KB")
