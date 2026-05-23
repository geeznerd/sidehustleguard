#!/usr/bin/env python3
"""
Phase 6.9 — Standardize calculator section spacing on mobile.

User-reported OCD: padding between sections on the 5 interactive tool
pages doesn't feel uniform. Audit found:
  - All 5 share hero padding (72px 24px 44px) — consistent ✓
  - But mobile horizontal padding varies: 16px on audit-risk, 18px on others
  - Wrap top padding is 0 across all 5 — no breathing room between
    hero and first form/wizard element on mobile (the only gap is
    the hero's own padding-bottom)
  - Mobile breakpoint splits across two values (700px vs 800px) so
    the same content jumps at different widths

This script appends a consistent supplemental @media rule to each of the
5 calculators that:
  - Adds .tool-wrap / .calc-wrap padding-top:18px on mobile (breathing
    room between hero band and first form element)
  - Standardizes horizontal padding to 18px (matches nav + article body)
  - Compresses hero on mobile: 72 → 40 top, 44 → 28 bottom (mirrors
    Phase 6.3 article compression so heroes feel uniform across the site)
  - Tightens hero-sub margin so the gap to the wrap is consistent
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path('/Users/dork/Desktop/sidehustleguard')

# The supplemental rule that gets appended just before </style> on each calc
SUPPLEMENT = """
/* Phase 6.9 — uniform mobile spacing across all 5 calculators */
@media (max-width: 700px) {
  /* Hero: tighter on mobile, matching the article-template compression */
  .hero { padding: 40px 18px 28px !important; }
  .hero-content { max-width: 100%; }
  .hero-badge { margin-bottom: 14px; font-size: 11px; padding: 7px 13px; }
  h1 { font-size: 28px !important; margin-bottom: 12px !important; line-height: 1.1 !important; }
  .hero-sub { font-size: 14.5px; margin: 0 auto 4px; line-height: 1.55; }

  /* Wrap: consistent breathing-room above the first form element */
  .tool-wrap,
  .calc-wrap { padding: 18px 18px 40px !important; }

  /* Progress bar / wizard / cards: tighter vertical rhythm */
  .progress-bar { margin-bottom: 22px; }
  .wizard-card { padding: 22px 18px !important; }
  .step-header { margin-bottom: 18px; }
  .calc-card,
  .results-card,
  .inputs-card { padding: 20px 18px !important; }
  .field { margin-bottom: 16px; }
}
"""

FILES = [
    'audit-risk-estimator.html',
    'self-employment-tax-calculator.html',
    'quarterly-tax-calculator.html',
    'scorp-savings-calculator.html',
    'tax-guard-calculator.html',
]

MARKER = '/* Phase 6.9 — uniform mobile spacing across all 5 calculators */'


def migrate(path: Path) -> str:
    text = path.read_text(encoding='utf-8')
    if MARKER in text:
        return 'already-applied'
    if '</style>' not in text:
        return 'no-style-block'
    text = text.replace('</style>', SUPPLEMENT + '\n</style>', 1)
    path.write_text(text, encoding='utf-8')
    return 'updated'


def main():
    for f in FILES:
        result = migrate(ROOT / f)
        print(f'  {result:18s} {f}')


if __name__ == '__main__':
    main()
