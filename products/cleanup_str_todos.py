"""
Remove unfinished TODO sections from STR/platform pages — DOM-aware version.

For each page with TODOs:
1. Extract all TODO content to a reference file so the notes aren't lost.
2. Parse HTML, find every <h2> followed by a TODO comment, remove both.
3. Remove the "In this guide" TOC block (most links would point to deleted h2s).
4. Recount remaining body content.
5. If body too thin (<800 words), set robots meta to noindex,follow.

Uses BeautifulSoup for proper DOM walking — no regex on HTML structure.
"""
import os, re, glob, datetime
from bs4 import BeautifulSoup, Comment, NavigableString

REPO = "/Users/dork/Desktop/sidehustleguard"
TODAY = datetime.date.today().isoformat()
INDEX_THRESHOLD = 800

def find_todo_pages():
    pages = []
    for path in sorted(glob.glob(os.path.join(REPO, "*.html"))):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "<!-- TODO" in content or "<!--TODO" in content:
            pages.append(path)
    return pages

def archive_todos(pages):
    lines = [
        f"# STR / Platform Page TODOs — archived {TODAY}",
        "",
        "Unfinished section notes that were removed from guide pages during",
        "cleanup. Saved here so you can write platform-specific content later",
        "when you have traffic data on which pages matter most.",
        "",
        "---",
        "",
    ]
    for path in pages:
        name = os.path.basename(path)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        soup = BeautifulSoup(content, "html.parser")
        # Find all comments and check if they start with TODO
        sections = []
        for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
            text = comment.strip()
            if not text.upper().startswith("TODO"):
                continue
            # Find the preceding h2 sibling, if any
            prev = comment.previous_sibling
            while prev is not None and isinstance(prev, NavigableString) and not str(prev).strip():
                prev = prev.previous_sibling
            heading = "(no heading)"
            section_id = ""
            if prev is not None and prev.name == "h2":
                heading = prev.get_text(strip=True)
                section_id = prev.get("id", "")
            sections.append((section_id, heading, text))
        if not sections:
            continue
        lines.append(f"## {name}")
        lines.append("")
        for sid, heading, todo in sections:
            anchor = f"`#{sid}` — " if sid else ""
            lines.append(f"### {anchor}{heading}")
            lines.append("")
            lines.append("```")
            lines.append(todo)
            lines.append("```")
            lines.append("")
        lines.append("---")
        lines.append("")
    archive_path = os.path.join(REPO, "products", "STR_TODOS_ARCHIVE.md")
    with open(archive_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return archive_path

def cleanup_page(path):
    """DOM-aware cleanup: remove h2 sections whose body is just a TODO comment."""
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()
    soup = BeautifulSoup(original, "html.parser")

    todos_removed = 0
    # Walk every h2. If the very next non-whitespace sibling is a TODO comment, remove both.
    for h2 in list(soup.find_all("h2")):
        nxt = h2.next_sibling
        # Skip whitespace text nodes
        while nxt is not None and isinstance(nxt, NavigableString) and not str(nxt).strip():
            nxt = nxt.next_sibling
        if isinstance(nxt, Comment) and nxt.strip().upper().startswith("TODO"):
            # Also eat any whitespace text node directly after the TODO
            after = nxt.next_sibling
            nxt.extract()
            h2.extract()
            todos_removed += 1
            # Clean up the dangling blank lines that may remain
            if after is not None and isinstance(after, NavigableString) and not str(after).strip():
                # Leave one newline for readability
                pass

    # Remove the "In this guide" TOC block — every link inside points to deleted h2s
    toc_removed = False
    toc = soup.find("div", class_="toc-box")
    if toc is not None:
        toc.decompose()
        toc_removed = True

    # Serialize and clean up excess blank lines
    new_html = str(soup)
    new_html = re.sub(r"\n{4,}", "\n\n\n", new_html)

    # Measure remaining body content
    # Make a copy of soup for measuring
    measure_soup = BeautifulSoup(new_html, "html.parser")
    for tag in measure_soup.find_all(["nav", "footer", "script", "style", "head"]):
        tag.decompose()
    body_text = measure_soup.get_text(" ", strip=True)
    words = len(body_text.split())

    # Decide robots meta
    if words < INDEX_THRESHOLD:
        new_robots = '<meta name="robots" content="noindex, follow">'
        noindexed = True
    else:
        new_robots = '<meta name="robots" content="index, follow">'
        noindexed = False

    # Replace robots meta in the raw HTML (bs4 sometimes reorders attributes)
    if re.search(r'<meta\s+name="robots"\s+content="[^"]*"\s*/?>', new_html, re.IGNORECASE):
        new_html = re.sub(
            r'<meta\s+name="robots"\s+content="[^"]*"\s*/?>',
            new_robots,
            new_html,
            count=1,
            flags=re.IGNORECASE,
        )
    else:
        new_html = re.sub(
            r'(<meta charset="[^"]+">)',
            r"\1\n" + new_robots,
            new_html,
            count=1,
        )

    changed = new_html != original
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)

    return {
        "name": os.path.basename(path),
        "todos_removed": todos_removed,
        "toc_removed": toc_removed,
        "words_after": words,
        "noindexed": noindexed,
    }

if __name__ == "__main__":
    pages = find_todo_pages()
    print(f"Found {len(pages)} pages with TODO sections")

    archive_path = archive_todos(pages)
    print(f"Archived TODO notes → {archive_path}")
    print()

    results = []
    for path in pages:
        r = cleanup_page(path)
        results.append(r)

    print(f"{'Page':<45s} {'TODOs':>7s} {'TOC':>5s} {'Words':>7s}  Robots")
    print("-" * 80)
    for r in sorted(results, key=lambda x: x["words_after"]):
        toc = "✓" if r["toc_removed"] else "-"
        robots = "noindex" if r["noindexed"] else "INDEX"
        print(f"{r['name']:<45s} {r['todos_removed']:>7d} {toc:>5s} {r['words_after']:>7d}  {robots}")

    print("-" * 80)
    print(f"Total pages cleaned: {len(results)}")
    print(f"  noindexed: {sum(1 for r in results if r['noindexed'])}")
    print(f"  still indexable: {sum(1 for r in results if not r['noindexed'])}")
