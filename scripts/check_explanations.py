"""Check that every Code explanation box covers its example's code lines.

For each `??? note "Code explanation"` box on a page, find the most recent
`--8<-- "path"` snippet above it (it may sit inside a Blocks/Python content
tab, with a PRIMM callout in between). Then compare the box's `line n` and
`lines n–m` references with the snippet file:

- BAD: a reference to a blank line, a comment line or a line past the end
- MISSING: a code line that has no explanation

Prints each problem, then `N issue(s) found`. Exits with 1 if there are issues.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

SNIPPET = re.compile(r'^\s*--8<--\s+"([^"]+)"')
BOX = re.compile(r'^(\s*)\?\?\?\+?\s+note\s+"Code explanation"')
REF = re.compile(r"\*\*lines?\s+(\d+)(?:\s*[–-]\s*(\d+))?\*\*")


def code_lines(path):
    """Return the line numbers that hold code (not blank, not a comment)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    result = set()
    for number, text in enumerate(lines, start=1):
        stripped = text.strip()
        if stripped and not stripped.startswith("#"):
            result.add(number)
    return result, len(lines)


def box_refs(lines, start, indent):
    """Collect the line references inside a Code explanation box."""
    refs = set()
    for text in lines[start + 1:]:
        if text.strip() and (len(text) - len(text.lstrip())) <= len(indent):
            break
        for match in REF.finditer(text):
            first = int(match.group(1))
            last = int(match.group(2) or first)
            refs.update(range(first, last + 1))
    return refs


def check_page(page):
    issues = []
    lines = page.read_text(encoding="utf-8").splitlines()
    last_snippet = None
    for index, text in enumerate(lines):
        snippet = SNIPPET.match(text)
        if snippet:
            last_snippet = snippet.group(1)
            continue
        box = BOX.match(text)
        if not box:
            continue
        where = f"{page.relative_to(ROOT)}:{index + 1}"
        if last_snippet is None:
            issues.append(f"{where} BAD Code explanation with no snippet above it")
            continue
        source = DOCS / last_snippet.split(":")[0]
        if not source.exists():
            issues.append(f"{where} BAD snippet file not found: {last_snippet}")
            continue
        wanted, length = code_lines(source)
        refs = box_refs(lines, index, box.group(1))
        for ref in sorted(refs):
            if ref > length or ref not in wanted:
                issues.append(f"{where} BAD line {ref} in {last_snippet} is blank, a comment or past the end")
        for ref in sorted(wanted - refs):
            issues.append(f"{where} MISSING line {ref} in {last_snippet}")
        last_snippet = None
    return issues


def main():
    issues = []
    for page in sorted(DOCS.rglob("*.md")):
        issues.extend(check_page(page))
    for issue in issues:
        print(issue)
    print(f"{len(issues)} issue(s) found")
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
