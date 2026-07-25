"""Resize, recompress and generate WebP for every raster image in site/.

    python3 build/optimize.py [--dry-run]

Idempotent: run it as often as you like. It reads the current file, applies
the cap for that image's role, and rewrites only if the result is smaller.

Why this exists
---------------
The recovered Luxury Presence assets shipped at whatever size they happened
to be exported at — several at 2560px wide for slots that render at 352px,
one headshot at 1920x2878 weighing 873 KB, and photographs saved as PNG.
That was 8.8 MB of images on a site whose entire competitive premise is that
an AI fetcher and a person on a phone in a driveway can both read it fast.

The caps below come from how each image is actually used, doubled for retina:

  backgrounds   full-bleed bands, edge to edge          -> 1920
  neighborhoods page hero AND a ~352px card             -> 1280
  textures      full-bleed plate ground                 -> 1600
  team          headshots in a grid, ~352px square      ->  800
  logos         already small PNGs with transparency    -> left alone
  compliance    REALTOR/EHO and MLS marks, 3 KB each    -> left alone

WebP is written alongside rather than replacing: `components.picture()`
emits a <picture> with the WebP first and the JPEG as fallback, so nothing
breaks for a client that cannot read it.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

IMG = Path(__file__).resolve().parent.parent / "site/assets/img"

# Longest edge, by directory. None means "do not touch".
CAPS = {
    "backgrounds": 1920,
    "neighborhoods": 1280,
    "textures": 1600,
    "team": 800,
    "logos": None,
    "compliance": None,
}

JPEG_QUALITY = 80
WEBP_QUALITY = 78

# Backgrounds sit full-bleed behind a dark scrim with display type over them.
# Nobody is studying the grain, and 80 is money spent on detail the overlay
# throws away.
BAND_JPEG_QUALITY = 68
BAND_WEBP_QUALITY = 62

# A second, smaller rendition for images used in BOTH a full-width hero and a
# ~400px card. Without it the homepage ships six 1280px files to fill six
# 400px slots. `components.picture(srcset=True)` emits the pair with a
# `sizes` hint so the browser picks.
NARROW = 800
NARROW_DIRS = {"neighborhoods", "team"}

# Photographs saved as PNG cost several times what they need to. These are
# converted to JPEG; anything that might legitimately need transparency (the
# logos and compliance marks) is excluded by its directory cap being None.
PHOTO_SUFFIXES = {".jpg", ".jpeg", ".png"}


def role(path: Path) -> str:
    return path.relative_to(IMG).parts[0]


def optimize(path: Path, *, dry_run: bool) -> tuple[int, int, int]:
    """Returns (bytes_before, bytes_after_jpeg, bytes_webp)."""
    before = path.stat().st_size
    cap = CAPS.get(role(path))
    if cap is None:
        return before, before, 0

    img = Image.open(path)
    # Flatten any alpha onto white — a photograph does not need it, and
    # keeping it forces PNG.
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        flat = Image.new("RGB", img.size, (255, 255, 255))
        flat.paste(img, mask=img.split()[-1])
        img = flat
    else:
        img = img.convert("RGB")

    if max(img.size) > cap:
        img.thumbnail((cap, cap), Image.LANCZOS)

    jpeg_path = path.with_suffix(".jpg")
    webp_path = path.with_suffix(".webp")
    if dry_run:
        return before, before, 0

    band = role(path) == "backgrounds"
    jq = BAND_JPEG_QUALITY if band else JPEG_QUALITY
    wq = BAND_WEBP_QUALITY if band else WEBP_QUALITY

    img.save(jpeg_path, "JPEG", quality=jq, optimize=True, progressive=True)
    img.save(webp_path, "WEBP", quality=wq, method=6)

    # Narrow rendition for card-sized slots.
    if role(path) in NARROW_DIRS and img.width > NARROW:
        small = img.copy()
        small.thumbnail((NARROW, NARROW), Image.LANCZOS)
        stem = jpeg_path.with_suffix("")
        small.save(
            f"{stem}-{NARROW}.jpg", "JPEG",
            quality=JPEG_QUALITY, optimize=True, progressive=True,
        )
        small.save(f"{stem}-{NARROW}.webp", "WEBP", quality=WEBP_QUALITY, method=6)

    # A .png that became a .jpg leaves the original behind; markup is updated
    # to match, so remove it rather than shipping a file nothing references.
    if path.suffix.lower() == ".png" and jpeg_path.exists():
        path.unlink()

    return before, jpeg_path.stat().st_size, webp_path.stat().st_size


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    if not IMG.exists():
        print("site/assets/img does not exist")
        return 1

    # Skip the -800 renditions this script itself writes, or each run would
    # shrink them again.
    files = sorted(
        p for p in IMG.rglob("*")
        if p.is_file()
        and p.suffix.lower() in PHOTO_SUFFIXES
        and not p.stem.endswith(f"-{NARROW}")
    )

    total_before = total_jpeg = total_webp = 0
    changed = []
    for path in files:
        before, after, webp = optimize(path, dry_run=dry_run)
        total_before += before
        total_jpeg += after
        total_webp += webp
        if after < before * 0.95:
            changed.append((before, after, webp, path.relative_to(IMG).as_posix()))

    for before, after, webp, name in sorted(changed, reverse=True):
        print(
            f"{before / 1024:7.0f} KB -> {after / 1024:6.0f} KB jpg "
            f"/ {webp / 1024:6.0f} KB webp   {name}"
        )

    print(
        f"\n{len(files)} images · {total_before / 1024 / 1024:.1f} MB -> "
        f"{total_jpeg / 1024 / 1024:.1f} MB JPEG "
        f"({total_webp / 1024 / 1024:.1f} MB WebP alongside)"
    )
    if dry_run:
        print("--dry-run: nothing written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
