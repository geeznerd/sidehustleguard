"""
Audit every HTML page for content thinness.

For each page, measures word count of body prose by stripping nav, footer,
scripts, and the related-section, then counting words in everything else.

Buckets:
- substantive   (1500+ words)  →  keep, include in sitemap
- borderline    (700-1499)     →  keep but flag for expansion
- thin          (300-699)      →  keep but consider expanding/noindexing
- scaffold      (<300)         →  hard noindex, almost certainly placeholder
"""
import os, re, glob

REPO = "/Users/dork/Desktop/sidehustleguard"

# Pages to never include in the sitemap regardless of content
ALWAYS_EXCLUDE = {
    "og-image.html",
    "tool.html",
    "guide-section-options.html",
    "tax-affiliate-options.html",
    "tax-checklist.html",
    "_template-article.html",
    "_template-article-card.html",
}

def measure(path):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    # Strip elements that aren't body prose
    cleaned = raw
    # Scripts and styles
    cleaned = re.sub(r"<script\b[^>]*>.*?</script>", " ", cleaned, flags=re.DOTALL | re.IGNORECASE)
    cleaned = re.sub(r"<style\b[^>]*>.*?</style>", " ", cleaned, flags=re.DOTALL | re.IGNORECASE)
    cleaned = re.sub(r"<noscript\b[^>]*>.*?</noscript>", " ", cleaned, flags=re.DOTALL | re.IGNORECASE)
    # Nav
    cleaned = re.sub(r"<nav\b[^>]*>.*?</nav>", " ", cleaned, flags=re.DOTALL | re.IGNORECASE)
    # Footer
    cleaned = re.sub(r"<footer\b[^>]*>.*?</footer>", " ", cleaned, flags=re.DOTALL | re.IGNORECASE)
    # JSON-LD (also caught by <script> above but belt-and-suspenders)
    cleaned = re.sub(r"<head\b[^>]*>.*?</head>", " ", cleaned, flags=re.DOTALL | re.IGNORECASE)
    # Comments
    cleaned = re.sub(r"<!--.*?-->", " ", cleaned, flags=re.DOTALL)

    # Count <h2> and <p> BEFORE we strip tags
    h2_count = len(re.findall(r"<h2\b", cleaned, flags=re.IGNORECASE))
    p_count  = len(re.findall(r"<p\b",  cleaned, flags=re.IGNORECASE))

    # Strip all remaining HTML tags
    text = re.sub(r"<[^>]+>", " ", cleaned)
    # Decode common entities
    text = text.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", "\"").replace("&#39;", "'")
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()
    words = len(text.split())
    return words, h2_count, p_count

def bucket(words):
    if words >= 1500: return "substantive"
    if words >= 700:  return "borderline"
    if words >= 300:  return "thin"
    return "scaffold"

if __name__ == "__main__":
    rows = []
    for path in sorted(glob.glob(os.path.join(REPO, "*.html"))):
        name = os.path.basename(path)
        if name in ALWAYS_EXCLUDE or name.startswith("_"):
            rows.append((name, 0, 0, 0, "EXCLUDED"))
            continue
        words, h2, p = measure(path)
        rows.append((name, words, h2, p, bucket(words)))

    counts = {"substantive": 0, "borderline": 0, "thin": 0, "scaffold": 0, "EXCLUDED": 0}
    for name, words, h2, p, b in rows:
        counts[b] = counts.get(b, 0) + 1

    print(f"{'Page':<45s} {'Words':>7s} {'H2':>4s} {'P':>4s}  Bucket")
    print("-" * 80)
    bucket_order = {"scaffold": 0, "thin": 1, "borderline": 2, "substantive": 3, "EXCLUDED": 4}
    rows.sort(key=lambda r: (bucket_order[r[4]], r[1]))
    for name, words, h2, p, b in rows:
        print(f"{name:<45s} {words:>7d} {h2:>4d} {p:>4d}  {b}")

    print("-" * 80)
    print(f"TOTAL: {len(rows)} pages")
    for b, c in counts.items():
        if c > 0: print(f"  {b:<14s} {c}")
