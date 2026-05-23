#!/usr/bin/env python3
"""
Phase 7 — Newsletter widget injection.

Injects <script src="/assets/js/newsletter-widget.js" defer></script>
immediately before </body> on every production HTML page.

Skips:
  - Pages already containing the script tag (idempotent)
  - Internal/template/render-target pages listed in EXCLUDE
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXCLUDE = {
    "_template-article-card.html",
    "_template-article.html",
    "guide-section-options.html",
    "og-image.html",
    "tax-affiliate-options.html",
}

SCRIPT_TAG = '<script src="/assets/js/newsletter-widget.js" defer></script>'
# Detect both with and without the defer attribute, just in case it gets edited later
DETECT_RE = re.compile(r'src=["\']/assets/js/newsletter-widget\.js["\']')

# Match </body> wherever it appears — most pages have it on its own line with
# whitespace indent, but a few minified ones have it appended to other tags
# (e.g. "</div></body>"). Inject the script tag immediately before it.
BODY_CLOSE_RE = re.compile(r'</body>')


def inject(path: Path) -> str:
    """Return 'skipped', 'already', 'injected', or 'no-body'."""
    if path.name in EXCLUDE:
        return "skipped"
    text = path.read_text(encoding="utf-8")
    if DETECT_RE.search(text):
        return "already"
    m = BODY_CLOSE_RE.search(text)
    if not m:
        return "no-body"
    # Inject script tag right before </body>. If the page is minified
    # (</body> appears mid-line), don't add a trailing newline that would
    # introduce stray whitespace into the rendered output.
    new_text = text[: m.start()] + SCRIPT_TAG + text[m.start():]
    path.write_text(new_text, encoding="utf-8")
    return "injected"


def main() -> int:
    pages = sorted(ROOT.glob("*.html"))
    counts = {"injected": 0, "already": 0, "skipped": 0, "no-body": 0}
    for p in pages:
        status = inject(p)
        counts[status] += 1
        if status in ("injected", "no-body"):
            print(f"  [{status:>8}] {p.name}")
    print()
    print(
        "Done. "
        f"injected={counts['injected']} "
        f"already={counts['already']} "
        f"skipped={counts['skipped']} "
        f"no-body={counts['no-body']}"
    )
    return 0 if counts["no-body"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
