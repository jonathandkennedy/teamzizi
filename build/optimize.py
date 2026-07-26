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

import hashlib
import json
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


def already_done(path: Path, cap: int) -> bool:
    """True when this file has already been through the optimiser.

    Without this the script re-encoded every JPEG on every run: a lossy
    generation each time, and the practical harm, forty binary files showing
    as modified in git on every build, for no change anyone asked for.

    Staleness is decided by the CONTENT HASH recorded in the manifest, not by
    mtime. mtime looks like the obvious signal and is wrong here: git writes
    files at checkout time in arbitrary order, so on a fresh clone half the
    derivatives appear older than their sources and the whole tree
    re-encodes, which is the churn this function exists to stop.

    The hash matters because replacing a source JPEG in place -- regrading a
    hero, recropping it -- used to leave the old .webp beside the new .jpg.
    `components.picture()` puts the WebP first, so every browser that can
    read WebP got the stale frame while the JPEG fallback nobody looks at
    was correct. Silent, and invisible in the markup.
    """
    if path.suffix.lower() != ".jpg":
        return False  # PNG sources still need converting

    if MANIFEST.get(path.relative_to(IMG).as_posix()) != source_hash(path):
        return False
    if not all(d.exists() for d in derived_for(path)):
        return False
    try:
        with Image.open(path) as img:
            return max(img.size) <= cap
    except Exception:
        return False


def derived_for(path: Path) -> list[Path]:
    """Every file `optimize()` writes alongside `path`.

    The narrow rendition is conditional on the source being WIDER than
    NARROW, matching the `img.width > NARROW` guard in optimize(). Getting
    that condition wrong in only one of the two places is not a cosmetic
    mismatch: the team headshots are capped at exactly 800, which is not
    greater than 800, so no -800 file is written for them — and a staleness
    check that demanded one would find it missing on every single run and
    re-encode all twenty of them forever.
    """
    out = [path.with_suffix(".webp")]
    if role(path) not in NARROW_DIRS:
        return out
    try:
        with Image.open(path) as img:
            wide = img.width > NARROW
    except Exception:  # noqa: BLE001
        return out
    if wide:
        stem = path.with_suffix("")
        out += [Path(f"{stem}-{NARROW}.jpg"), Path(f"{stem}-{NARROW}.webp")]
    return out


def source_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


# Committed alongside the images so a fresh clone starts in the "everything
# is current" state instead of re-encoding the whole tree on its first build.
MANIFEST_PATH = IMG / ".optimized.json"


def load_manifest() -> dict[str, str]:
    try:
        return json.loads(MANIFEST_PATH.read_text())
    except (OSError, ValueError):
        return {}


def save_manifest(manifest: dict[str, str]) -> None:
    MANIFEST_PATH.write_text(
        json.dumps(dict(sorted(manifest.items())), indent=1) + "\n"
    )


def optimize(path: Path, *, dry_run: bool) -> tuple[int, int, int]:
    """Returns (bytes_before, bytes_after_jpeg, bytes_webp)."""
    before = path.stat().st_size
    cap = CAPS.get(role(path))
    if cap is None:
        return before, before, 0
    if already_done(path, cap) and not FORCE:
        return before, before, path.with_suffix(".webp").stat().st_size

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

    # Record the hash of what we just WROTE, not of the input: the next run
    # sees the encoded JPEG, and that is the file whose hash has to match.
    MANIFEST[jpeg_path.relative_to(IMG).as_posix()] = source_hash(jpeg_path)

    return before, jpeg_path.stat().st_size, webp_path.stat().st_size


FORCE = "--force" in sys.argv
MANIFEST: dict[str, str] = {}


def seed_manifest(files: list[Path]) -> int:
    """Adopt files that are already correct, without re-encoding them.

    Run once, when the manifest is introduced or a new image is added by
    hand. Anything already within its cap with all its derivatives present
    is recorded as-is. Without this the first run after this change would
    re-encode the entire tree — a lossy generation on every image and a
    seventy-file binary diff, to reach a state that was already correct.
    """
    seeded = 0
    for path in files:
        key = path.relative_to(IMG).as_posix()
        if key in MANIFEST or path.suffix.lower() != ".jpg":
            continue
        cap = CAPS.get(role(path))
        if cap is None:
            continue
        if not all(d.exists() for d in derived_for(path)):
            continue
        try:
            with Image.open(path) as img:
                if max(img.size) > cap:
                    continue
        except Exception:  # noqa: BLE001
            continue
        MANIFEST[key] = source_hash(path)
        seeded += 1
    return seeded


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

    MANIFEST.update(load_manifest())
    if not FORCE:
        seeded = seed_manifest(files)
        if seeded:
            print(f"adopted {seeded} already-optimised file(s) into the manifest")

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
    else:
        save_manifest(MANIFEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
