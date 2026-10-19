"""List example code and Blocks screenshots that no page uses.

Run from the repo root:  python scripts/find_unused_files.py

Prints one path per line: each Python file under docs/examples/ that no page
includes with --8<--, and each image under docs/assets/blocks/ that no page
shows. After renumbering lessons, these are the old copies to
remove with git rm -r.
"""

import re
from pathlib import Path

DOCS = Path("docs")

pages = "\n".join(p.read_text(encoding="utf-8") for p in DOCS.rglob("*.md"))
snippets = set(re.findall(r'--8<--\s+"([^"]+)"', pages))
images = {m.split("assets/", 1)[-1] for m in re.findall(r"\(([^)\s]+\.png)", pages)}

unused = []
for code in sorted((DOCS / "examples").rglob("*.py")):
    rel = code.relative_to(DOCS).as_posix()
    if rel not in snippets:
        unused.append(code.as_posix())
for png in sorted((DOCS / "assets" / "blocks").rglob("*.png")):
    if png.relative_to(DOCS / "assets").as_posix() not in images:
        unused.append(png.as_posix())

print("\n".join(unused))
print(f"{len(unused)} unused path(s) found")
