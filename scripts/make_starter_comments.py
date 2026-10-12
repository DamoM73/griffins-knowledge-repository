"""Write the instruction comment at the top of every exercise starter.

Each exercise on a lesson page looks like this:

    ### Exercise 1

    Can you ...? It should:

    1. ...

    Starter code:

    ```python linenums="1"
    --8<-- "examples/other/pu_robot/lesson_03/ex1_heart_walk/main.py"
    ```

This script copies the exercise text (from the heading to "Starter code:")
into a comment block at the top of the starter file, so the two always
match. Any comment block already at the top of the file is replaced. Run it
after changing an exercise's wording.
"""

import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

HEADING = re.compile(r"^### (Exercise \d+)\s*$")
SNIPPET = re.compile(r'--8<--\s+"([^"]+)"')


def plain(text):
    """Remove markdown formatting from one line of exercise text."""
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = text.replace("**", "").replace("`", "").replace("***", "")
    return text.rstrip()


def comment_block(title, lines):
    out = [f"# {title}"]
    for line in lines:
        if not line.strip():
            out.append("#")
            continue
        bullet = re.match(r"^(\s*)(\d+\.|-)\s+(.*)$", line)
        if bullet:
            marker = bullet.group(2) + " "
            wrapped = textwrap.wrap(bullet.group(3), 74 - len(marker))
            out.append("# " + marker + wrapped[0])
            out += ["# " + " " * len(marker) + w for w in wrapped[1:]]
        else:
            out += ["# " + w for w in textwrap.wrap(line.strip(), 74)]
    while out and out[-1] == "#":
        out.pop()
    out.append("#")
    return out


def strip_header(code):
    lines = code.splitlines()
    while lines and lines[0].startswith("#"):
        lines.pop(0)
    while lines and not lines[0].strip():
        lines.pop(0)
    return lines


def main():
    count = 0
    for page in sorted(DOCS.rglob("*.md")):
        lines = page.read_text(encoding="utf-8").splitlines()
        index = 0
        while index < len(lines):
            heading = HEADING.match(lines[index])
            if not heading:
                index += 1
                continue
            title = heading.group(1)
            body = []
            index += 1
            while index < len(lines) and not lines[index].startswith("Starter code:"):
                if lines[index].startswith("#"):
                    break
                body.append(plain(lines[index]))
                index += 1
            if index >= len(lines) or not lines[index].startswith("Starter code:"):
                continue
            snippet = None
            while index < len(lines) and snippet is None:
                match = SNIPPET.search(lines[index])
                if match:
                    snippet = match.group(1)
                index += 1
            target = DOCS / snippet
            code = strip_header(target.read_text(encoding="utf-8"))
            header = comment_block(title, body)
            target.write_text("\n".join(header + code) + "\n", encoding="utf-8")
            count += 1
    print(f"{count} starter file(s) updated")


if __name__ == "__main__":
    main()
