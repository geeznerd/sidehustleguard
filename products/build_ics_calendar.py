"""
Build the .ics calendar file with all federal quarterly tax deadlines for
2026 and 2027, plus reminders at 7 days and 1 day before each.

Drag into Apple Calendar, Google Calendar, or Outlook — events + alerts
import in one shot.
"""
import os
from datetime import datetime

def fmt_date(y, m, d):
    return f"{y:04d}{m:02d}{d:02d}"

def fmt_dt_utc():
    return datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

# (year, month, day, quarter_label, period_label)
deadlines = [
    (2026, 4, 15,  "Q1", "January – March"),
    (2026, 6, 15,  "Q2", "April – May"),
    (2026, 9, 15,  "Q3", "June – August"),
    (2027, 1, 15,  "Q4", "September – December 2026"),
    (2027, 4, 15,  "Q1", "January – March"),
    (2027, 6, 15,  "Q2", "April – May"),
    (2027, 9, 15,  "Q3", "June – August"),
    (2028, 1, 15,  "Q4", "September – December 2027"),
]

dtstamp = fmt_dt_utc()

events = []
for y, m, d, q, period in deadlines:
    # The tax year the payment APPLIES TO (which is what the buyer cares about)
    tax_year = y if q != "Q4" else y - 1
    end_y, end_m, end_d = (y, m, d + 1) if d < 28 else (y, m + 1, 1) if m < 12 else (y + 1, 1, 1)
    uid = f"{q.lower()}-{tax_year}@sidehustleguard.com"

    body = (
        rf"Federal quarterly estimated tax payment due to the IRS\, covering "
        rf"{period} of tax year {tax_year}.\n\n"
        rf"Pay one of three ways:\n"
        rf"  • IRS Direct Pay — irs.gov/payments/direct-pay (fastest)\n"
        rf"  • EFTPS — eftps.gov (best for permanent payment history)\n"
        rf"  • Mail Form 1040-ES with a check\n\n"
        rf"If you live in a state with income tax\, you likely owe a state quarterly "
        rf"payment on the same date — check your state revenue department's site.\n\n"
        rf"This calendar from your Quarterly Tax System purchase from SideHustleGuard.\n"
        rf"sidehustleguard.com"
    )

    events.append(f"""BEGIN:VEVENT
UID:{uid}
DTSTAMP:{dtstamp}
DTSTART;VALUE=DATE:{fmt_date(y,m,d)}
DTEND;VALUE=DATE:{fmt_date(end_y,end_m,end_d)}
SUMMARY:{q} Estimated Tax Payment Due (Tax Year {tax_year})
DESCRIPTION:{body}
LOCATION:irs.gov/payments/direct-pay
CATEGORIES:Tax,SideHustleGuard
TRANSP:TRANSPARENT
BEGIN:VALARM
TRIGGER:-P7D
ACTION:DISPLAY
DESCRIPTION:{q} quarterly tax due in 1 week ({fmt_date(y,m,d)})
END:VALARM
BEGIN:VALARM
TRIGGER:-P1D
ACTION:DISPLAY
DESCRIPTION:{q} quarterly tax due TOMORROW
END:VALARM
END:VEVENT""")

ics = (
    "BEGIN:VCALENDAR\n"
    "VERSION:2.0\n"
    "PRODID:-//SideHustleGuard//Quarterly Tax Deadlines//EN\n"
    "CALSCALE:GREGORIAN\n"
    "METHOD:PUBLISH\n"
    "X-WR-CALNAME:Quarterly Tax Deadlines (2026–2027)\n"
    "X-WR-CALDESC:US federal quarterly estimated tax deadlines from SideHustleGuard's Quarterly Tax System. Most states with income tax mirror these dates.\n"
    + "\n".join(events) + "\n"
    "END:VCALENDAR\n"
)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quarterly-tax-deadlines.ics")
with open(out, "w", encoding="utf-8") as f:
    f.write(ics)

print(f"Saved: {out}")
print(f"Size:  {os.path.getsize(out)/1024:.1f} KB")
print(f"Events: {len(events)} (2026 + 2027 quarterlies, each with -7d and -1d alarms)")
