"""Generate abstract hero textures for communities with no photograph.

    OPENAI_API_KEY=... python3 build/textures.py [--force] [slug ...]

Why this exists, and the line it must not cross
-----------------------------------------------
Twelve of sixteen guides have no photograph. `docs/photography-brief.md` is
explicit that generated imagery must never be used to depict a real named
community: a synthetic photograph of Escondido is a fabricated depiction of a
real place, on a site whose entire pitch is that its facts are checkable. A
model does not know what Escondido looks like — it knows what the word
evokes — and anyone who lives there can tell in one second.

So these are **not** pictures of anywhere. They are non-representational
textures — grain, wash, contour, light — sitting behind a typographic hero
that carries the community's actual data. The texture is wallpaper. The
information is type. Nothing on the page claims the image is a place.

Every prompt below therefore bans, explicitly: buildings, streets, houses,
horizons, skylines, mountains, coastline, vegetation, vehicles, people, signage
and anything photographic. If a generated file comes back looking like a
landscape, it has failed and must be regenerated — see `--force`.

Provenance
----------
Each file is written alongside a `.json` sidecar recording the model, the exact
prompt and the date, so a year from now anyone can see how the asset was made
without having to guess. `assets/recovered/README.md` exists because that
guessing already cost this project a day.
"""

from __future__ import annotations

import base64
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from data import site  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "site/assets/img/textures"
MODEL = "gpt-image-2"
SIZE = "1536x1024"
TODAY = date.today().isoformat()

# The brand palette, named in words the model can act on. Sampled from
# site/assets/css/tokens.css so the textures sit in the same world as the type.
PALETTE = (
    "warm off-white paper (#f3f3f3), soft warm grey, muted antique gold "
    "(#8d7120) used sparingly as the only saturated note, and warm tan "
    "(#ccb091)"
)

# Repeated verbatim in every prompt. This is the guardrail, not decoration.
BAN = (
    "Strictly abstract and non-representational. Absolutely NO buildings, "
    "houses, streets, roads, cars, people, signage, text, letters, numbers, "
    "skylines, horizons, mountains, hills, coastline, beaches, water, trees, "
    "plants or any recognisable landscape or place. It must be impossible to "
    "mistake this for a photograph of anywhere. No photorealism. Think of a "
    "high-end printed endpaper or a fine-art monoprint, not a scene."
)

QUALITY = (
    "Extremely subtle and low-contrast, so dark display type remains legible "
    "over it. Fine paper grain. Generous empty space. Elegant, restrained, "
    "editorial. Flat — no vignette, no drop shadows, no 3D rendering."
)

# One texture per visual family rather than one per community: twelve
# near-identical abstracts would read as noise, and a small set used
# deliberately reads as a design system. Communities map onto these below.
TEXTURES = {
    "contour": (
        "An abstract composition of fine, evenly-spaced topographic contour "
        "lines, like an elevation map abstracted until it means nothing, "
        "drifting across a warm off-white ground. Thin hairline strokes. "
        f"Palette: {PALETTE}."
    ),
    "wash": (
        "A soft, wide gradient wash across a warm off-white ground, like ink "
        "diffusing into damp paper. Gentle tonal transition, no hard edges. "
        f"Palette: {PALETTE}."
    ),
    "grid": (
        "An abstract composition of fine intersecting hairlines forming an "
        "irregular, slightly broken grid on warm off-white, some lines fading "
        f"out entirely. Architectural but meaningless. Palette: {PALETTE}."
    ),
    "grain": (
        "A near-plain warm off-white field with rich fine-art paper grain and "
        "the faintest tonal drift from one corner to another. Almost nothing "
        f"happening, deliberately. Palette: {PALETTE}."
    ),
}

# Which family each community without a photograph uses. Grouped by character
# of the place rather than at random — the inland backcountry communities share
# a treatment, the coastal cities share another — so the set reads as
# considered rather than shuffled.
ASSIGNMENT = {
    # Inland valley and backcountry
    "escondido": "contour",
    "valley-center": "contour",
    "ramona": "contour",
    "fallbrook": "contour",
    # Coastal cities
    "oceanside": "wash",
    "carlsbad": "wash",
    "encinitas": "wash",
    # Master-planned / built grid
    "san-marcos": "grid",
    "4s-ranch": "grid",
    "carmel-valley": "grid",
    # Low-density inland
    "vista": "grain",
    "poway": "grain",
}


def generate(name: str, prompt: str) -> None:
    full = f"{prompt}\n\n{BAN}\n\n{QUALITY}"
    body = json.dumps({
        "model": MODEL,
        "prompt": full,
        "size": SIZE,
        "n": 1,
    }).encode()

    request = urllib.request.Request(
        "https://api.openai.com/v1/images/generations",
        data=body,
        headers={
            "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=300) as response:
        payload = json.load(response)

    image = payload["data"][0]
    raw = base64.b64decode(image["b64_json"])

    OUT.mkdir(parents=True, exist_ok=True)
    # The API returns ~2.5 MB of PNG. These are smooth, low-contrast washes
    # behind type — exactly the content JPEG handles well and PNG handles
    # badly — and the whole site was already 8.3 MB unoptimised. Ship JPEG at
    # a sane width; keep nothing lossless we do not need.
    from io import BytesIO  # noqa: PLC0415

    from PIL import Image  # noqa: PLC0415

    img = Image.open(BytesIO(raw)).convert("RGB")
    img.thumbnail((1600, 1600), Image.LANCZOS)
    img.save(OUT / f"{name}.jpg", "JPEG", quality=82, optimize=True, progressive=True)
    written = (OUT / f"{name}.jpg").stat().st_size
    (OUT / f"{name}.json").write_text(
        json.dumps(
            {
                "generated": True,
                "model": MODEL,
                "size": SIZE,
                "prompt": full,
                "date": TODAY,
                "note": (
                    "Abstract texture. Does NOT depict any real place. Used as "
                    "a background behind a typographic hero; never captioned "
                    "or presented as a photograph of a community."
                ),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"  wrote {name}.jpg ({written // 1024} KB, from {len(raw) // 1024} KB PNG)")


def main() -> int:
    if not os.environ.get("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is not set.")
        return 1

    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    wanted = args or list(TEXTURES)

    print(f"Generating {len(wanted)} texture(s) with {MODEL}\n")
    for name in wanted:
        if name not in TEXTURES:
            print(f"  skip {name}: not a known texture")
            continue
        if (OUT / f"{name}.jpg").exists() and not force:
            print(f"  skip {name}: already exists (--force to regenerate)")
            continue
        try:
            generate(name, TEXTURES[name])
        except urllib.error.HTTPError as err:
            print(f"  FAIL {name}: HTTP {err.code} {err.read()[:200]!r}")
            return 1

    print(
        f"\nDone. {len(ASSIGNMENT)} communities map onto these; "
        "see ASSIGNMENT in this file."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
