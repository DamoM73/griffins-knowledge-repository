"""Create placeholder images for any Blocks screenshot that doesn't exist yet.

Each Blocks tab shows `![...](.../assets/blocks/<kit>/<name>.png){ .blocks }`.
This script finds those image paths and, for each missing file, writes a grey
placeholder that names the program, so the page still builds. Replace each
placeholder with a real MakeCode screenshot of the same name.

Needs Pillow: pip install pillow
"""

import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]*assets/blocks/[^)]+\.png)\)")


def font(size):
    for name in ("DejaVuSans.ttf", "arial.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def placeholder(path, label):
    img = Image.new("RGB", (900, 260), "#f2f4f5")
    draw = ImageDraw.Draw(img)
    draw.rectangle([4, 4, 895, 255], outline="#9aa5ab", width=3)
    draw.text((30, 70), "Blocks screenshot to come", fill="#545f65", font=font(34))
    draw.text((30, 130), label, fill="#545f65", font=font(22))
    draw.text((30, 180), path.relative_to(DOCS).as_posix(), fill="#7b868c", font=font(18))
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)


def main():
    made = 0
    for page in sorted(DOCS.rglob("*.md")):
        for alt, link in IMAGE.findall(page.read_text(encoding="utf-8")):
            target = (page.parent / link).resolve()
            if not target.exists():
                placeholder(target, alt)
                made += 1
    print(f"{made} placeholder(s) created")


if __name__ == "__main__":
    main()
