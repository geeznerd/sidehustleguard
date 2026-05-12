"""
Fix the nesting bug introduced by inject_quarterly_card.py:
the Mileage Tracker card's outer </div> got eaten when the Quarterly card
was inserted right after it. The result is the Quarterly card rendering as
a flex child of the Mileage card instead of as a sibling.

Broken pattern:
    </div>      <- cta-row close (4-space indent)
  </div>        <- body close (2-space indent)
<div class="product-card" data-product="quarterly-tax-system">

Correct pattern:
    </div>      <- cta-row close
  </div>        <- body close
</div>          <- product-card outer close (MISSING)
<div class="product-card" data-product="quarterly-tax-system">
"""
import os, re, glob

REPO = "/Users/dork/Desktop/sidehustleguard"

# Match: body-close (2-space indent) directly followed by any product-card opening div.
# A correctly-closed card would have an additional unindented </div> in between.
BROKEN = re.compile(r'^  </div>\n(<div class="product-card")', re.MULTILINE)

fixed_files = []
for path in sorted(glob.glob(os.path.join(REPO, "*.html"))):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    new_content, n = BROKEN.subn(r"  </div>\n</div>\n\1", content)
    if n > 0:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        fixed_files.append((os.path.basename(path), n))

for name, n in fixed_files:
    print(f"  fixed {n} card{'s' if n!=1 else ''}: {name}")
print()
print(f"Total: {len(fixed_files)} pages, {sum(n for _,n in fixed_files)} cards re-closed")
