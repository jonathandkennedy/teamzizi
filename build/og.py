"""Generate a per-page Open Graph card.

    python3 build/og.py [--force]

Why
---
All fifty pages shared one default OG image, so every share of a
neighborhood guide, the Mello-Roos lookup and the homepage looked
identical — and the preview an AI assistant or a messaging app renders
carried no information about the page at all.

These cards are typographic, not photographic. They set the page's own
title and a line of its own facts over the same abstract textures the fact
plates use. That is deliberate and it is the same rule as everywhere else
in this repo: a generated image may never depict a real place. A card that
says "Escondido · 4 ZIP codes · 1 Mello-Roos district" is honest and
useful; a synthetic photograph captioned Escondido is not.

Brand fonts
-----------
Reem Kufi Fun and Lato are shipped as woff2 for the browser, which Pillow
cannot read. fontTools decompiles them to TTF at build time into a scratch
directory — the TTFs are never committed, because the woff2 files are the
source of truth and two copies of a font drift.
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).parent))

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
OUT = SITE / "assets/img/og"
TEXTURES = SITE / "assets/img/textures"

# Facebook, LinkedIn, X and iMessage all render 1200x630 well; it is also
# the size Google uses for the large-image result treatment.
W, H = 1200, 630
MARGIN = 80

INK = (20, 17, 14)
GOLD = (141, 113, 32)
MUTED = (122, 122, 122)


def brand_fonts() -> tuple[Path, Path]:
    """Decompile the shipped woff2 to TTF in a scratch dir. Never committed."""
    tmp = Path(tempfile.mkdtemp(prefix="ta-fonts-"))
    paths = []
    for name in ("reem-kufi-fun-400", "lato-700"):
        font = TTFont(SITE / f"assets/fonts/{name}.woff2")
        font.flavor = None
        dst = tmp / f"{name}.ttf"
        font.save(dst)
        paths.append(dst)
    return paths[0], paths[1]


def wrap(draw: ImageDraw.ImageDraw, text: str, font, max_width: int) -> list[str]:
    words, lines, current = text.split(), [], ""
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def card(*, title: str, meta: str, texture: str, dest: Path) -> None:
    base = Image.open(TEXTURES / f"{texture}.jpg").convert("RGB")
    # Cover-crop the texture to the card, then lighten it so type stays
    # legible — the same job the scrim does on the photographic bands.
    ratio = max(W / base.width, H / base.height)
    base = base.resize((int(base.width * ratio), int(base.height * ratio)), Image.LANCZOS)
    left = (base.width - W) // 2
    top = (base.height - H) // 2
    img = base.crop((left, top, left + W, top + H))
    img = Image.blend(img, Image.new("RGB", (W, H), (255, 255, 255)), 0.45)

    draw = ImageDraw.Draw(img)
    display_path, ui_path = brand_fonts()

    size = 72
    while size > 34:
        display = ImageFont.truetype(str(display_path), size)
        lines = wrap(draw, title, display, W - MARGIN * 2)
        if len(lines) <= 3:
            break
        size -= 6
    display = ImageFont.truetype(str(display_path), size)
    lines = wrap(draw, title, display, W - MARGIN * 2)

    ui = ImageFont.truetype(str(ui_path), 24)
    line_h = size * 1.22
    block_h = line_h * len(lines) + 90
    y = (H - block_h) / 2

    for line in lines:
        draw.text((MARGIN, y), line, font=display, fill=INK)
        y += line_h

    y += 18
    if meta:
        draw.text((MARGIN, y), meta.upper(), font=ui, fill=GOLD)
        y += 42

    # Brand line, bottom left. No logo file: the PNG logos carry their own
    # padding and would need masking, and the wordmark reads better set.
    brand = ImageFont.truetype(str(ui_path), 22)
    draw.text((MARGIN, H - MARGIN + 10), "TEAM AZIZI  ·  COMPASS", font=brand, fill=MUTED)
    draw.line(
        [(MARGIN, H - MARGIN - 14), (MARGIN + 60, H - MARGIN - 14)],
        fill=GOLD, width=3,
    )

    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, "JPEG", quality=86, optimize=True, progressive=True)


def main() -> int:
    from data import agents, posts, site, taxes  # noqa: PLC0415
    import textures  # noqa: PLC0415

    force = "--force" in sys.argv
    jobs: list[tuple[str, str, str, str]] = []  # slug, title, meta, texture

    jobs.append((
        "home",
        "Who Represents You Matters",
        f"{len(site.ALL_AREAS)} North San Diego communities",
        "wash",
    ))
    jobs.append((
        "mello-roos",
        "Every active Mello-Roos district in North San Diego County",
        "From the County Auditor's FY 2025-26 list",
        "grid",
    ))
    jobs.append((
        "neighborhoods",
        "North San Diego neighborhood guides",
        f"{len(site.ALL_AREAS)} communities, sourced",
        "contour",
    ))

    for area in site.ALL_AREAS:
        cfd = taxes.for_hood(area["slug"]) or {}
        zips = len(area["zip"].split(","))
        if area["slug"] == "san-marcos":
            tax = "91 CFDs"
        elif cfd.get("has_cfd"):
            n = len(cfd.get("districts", []))
            tax = f"{n} Mello-Roos district{'s' if n != 1 else ''}"
        else:
            tax = "No CFD in the county list"
        jobs.append((
            f"hood-{area['slug']}",
            f"{area['name']} Real Estate Guide",
            f"{zips} ZIP code{'s' if zips != 1 else ''} · {tax}",
            textures.ASSIGNMENT.get(area["slug"], "grain"),
        ))

    for post in posts.POSTS:
        author = agents.by_slug(post["author"])
        jobs.append((
            f"post-{post['slug']}", post["title"], author["name"], "contour",
        ))

    made = 0
    for slug, title, meta, texture in jobs:
        dest = OUT / f"{slug}.jpg"
        if dest.exists() and not force:
            continue
        card(title=title, meta=meta, texture=texture, dest=dest)
        made += 1

    total = sum(p.stat().st_size for p in OUT.glob("*.jpg"))
    print(
        f"{made} card(s) written, {len(jobs)} total · "
        f"{total / 1024:.0f} KB in {OUT.relative_to(ROOT)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
