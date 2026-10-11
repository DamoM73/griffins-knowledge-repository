"""Build docs/reference/glossary.md from the Terminology callouts.

Pages are read in nav order (from zensical.toml). Each `- **term** – definition.`
line inside a `!!! terms "Terminology"` callout becomes a glossary entry that
links back to its page. A term that appears on more than one page is reported,
because each term belongs only on the first page that explains it.
"""

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = DOCS / "reference" / "glossary.md"

ENTRY = re.compile(r"^\s+- \*\*(.+?)\*\* – (.+)$")


def walk(nav, found, section=None):
    """Collect (title, path) pairs in nav order.

    Lesson titles repeat across robots ("Lesson 2: First Program"), so a
    page inside a nav section gets the section's name added in brackets.
    """
    for item in nav:
        if isinstance(item, str):
            found.append((None, item))
        else:
            for title, value in item.items():
                if isinstance(value, str):
                    if section and title.startswith("Lesson"):
                        title = f"{title} ({section})"
                    found.append((title, value))
                else:
                    walk(value, found, title)
    return found


def page_title(path):
    for line in (DOCS / path).read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path


def terms_on(path):
    lines = (DOCS / path).read_text(encoding="utf-8").splitlines()
    result = []
    inside = False
    for line in lines:
        if line.startswith('!!! terms "Terminology"'):
            inside = True
            continue
        if inside:
            if line.strip() and not line.startswith("    "):
                break
            match = ENTRY.match(line)
            if match:
                result.append((match.group(1), match.group(2)))
    return result


def main():
    config = tomllib.loads((ROOT / "zensical.toml").read_text(encoding="utf-8"))
    pages = walk(config["project"]["nav"], [])
    seen = {}
    problems = []
    for title, path in pages:
        if path == "reference/glossary.md":
            continue
        for term, definition in terms_on(path):
            key = term.lower()
            if key in seen:
                problems.append(f"'{term}' is on {seen[key][2]} and {path}")
                continue
            seen[key] = (term, definition, path, title or page_title(path))

    groups = {}
    for key in sorted(seen, key=str.lower):
        term, definition, path, title = seen[key]
        letter = key[0].upper() if key[0].isalpha() else "0–9"
        link = Path("..") / path
        groups.setdefault(letter, []).append(f"- **{term}** – {definition} ([{title}]({link.as_posix()}))")

    letters = sorted(groups, key=lambda l: (l != "0–9", l))
    jump = " · ".join(f"[{l}](#{'0-9' if l == '0–9' else l.lower()})" for l in letters)
    out = [
        "# Glossary",
        "",
        "This glossary lists every technical term introduced on this site, in alphabetical order. "
        "Each term links to the page where it is first explained, and each page lists its new terms "
        "in a Terminology callout at the top.",
        "",
        jump,
        "",
    ]
    for letter in letters:
        heading = "## 0–9 { #0-9 }" if letter == "0–9" else f"## {letter}"
        out += [heading, ""] + groups[letter] + [""]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"{len(seen)} terms written to {OUT.relative_to(ROOT)}")
    for problem in problems:
        print("DUPLICATE", problem)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
