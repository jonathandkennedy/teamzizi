"""Find freely-licensed neighborhood photography on Wikimedia Commons.

    python3 build/commons.py                 # candidates for every area with no photo
    python3 build/commons.py escondido       # one area

This finds CANDIDATES. It does not install anything. Every image has to be
looked at by a human before it ships, because Commons will happily return a
photo of a protest, a road sign or a car park for a city search, and a
wrong-place hero is the exact failure that put a Monterey County vineyard on
the Carmel Valley page.

Why this source
---------------
The obvious alternative was the team's own Compass listing photography. That
is a dead end for three independent reasons, checked rather than assumed:

  1. The images carry a "SAN DIEGO | MLS" watermark — they are MLS-licensed
     listing photos, not the team's own assets, and reuse is restricted.
  2. The agent pages expose no reliable image-to-city mapping, so picking one
     for a given neighborhood would be guesswork.
  3. They are interiors. An empty bedroom is not a picture of Escondido.

Commons, by contrast, gives a licence, an author, a description and often
coordinates — everything needed to publish a photograph honestly and credit
it properly.

Licence handling
----------------
Public domain and CC0 files are preferred: no attribution obligation and no
share-alike, so cropping to a hero carries no downstream condition. CC BY and
CC BY-SA are usable with attribution, but note that a crop of a share-alike
image is an adaptation and inherits the licence. Anything non-commercial or
no-derivatives is excluded outright — this is a commercial site.
"""

from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

API = "https://commons.wikimedia.org/w/api.php"
UA = "TeamAziziSiteBuild/1.0 (https://teamazizi.com; teamazizi@compass.com)"

# Licences that permit commercial reuse. NC and ND are excluded: this is a
# commercial real estate site and a no-derivatives image cannot be cropped.
OK_LICENCES = (
    "public domain", "cc0", "cc by 2.0", "cc by 3.0", "cc by 4.0",
    "cc by-sa 2.0", "cc by-sa 2.5", "cc by-sa 3.0", "cc by-sa 4.0",
)

# Terms that reliably return something other than a usable establishing shot.
# Commons search is broad; a city name matches protest coverage, road signs,
# fire maps and car park photography as readily as a streetscape.
REJECT_WORDS = (
    "protest", "rally", "sign", "signage", "map", "diagram", "logo", "flag",
    "seal", "chart", "graph", "plaque", "gravestone", "cemetery", "crash",
    "fire", "wildfire", "flood", "damage", "wreck", "police", "arrest",
    "portrait", "headshot", "poster", "ballot", "election",
)


def api(params: dict) -> dict:
    url = f"{API}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def candidates(term: str, limit: int = 12) -> list[dict]:
    data = api({
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": f"filetype:bitmap {term}", "gsrnamespace": "6",
        "gsrlimit": str(limit), "prop": "imageinfo",
        "iiprop": "url|extmetadata|size", "iiurlwidth": "1600",
    })
    pages = (data.get("query") or {}).get("pages", {})
    out = []
    for page in pages.values():
        info = page.get("imageinfo", [{}])[0]
        meta = info.get("extmetadata", {})
        licence = meta.get("LicenseShortName", {}).get("value", "")
        title = page.get("title", "")

        if licence.lower() not in OK_LICENCES:
            continue
        if any(word in title.lower() for word in REJECT_WORDS):
            continue
        # A hero is wide; portrait-orientation files crop badly into a band.
        if info.get("width", 0) < info.get("height", 0):
            continue

        out.append({
            "title": title,
            "licence": licence,
            "author": strip_html(meta.get("Artist", {}).get("value", "")),
            "description": strip_html(
                meta.get("ImageDescription", {}).get("value", "")
            )[:160],
            "url": info.get("thumburl") or info.get("url"),
            "page": info.get("descriptionurl", ""),
            "size": f"{info.get('width')}x{info.get('height')}",
        })
    return out


def strip_html(value: str) -> str:
    import re  # noqa: PLC0415

    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", value)).strip()


def main() -> int:
    from data import site  # noqa: PLC0415
    import generate  # noqa: PLC0415

    wanted = [a for a in sys.argv[1:] if not a.startswith("--")]
    if wanted:
        areas = [a for a in site.ALL_AREAS if a["slug"] in wanted]
    else:
        areas = [
            a for a in site.ALL_AREAS
            if a["slug"] in generate.HOOD_IMAGE_MISSING
        ]

    for area in areas:
        print(f"\n=== {area['name']} ===")
        found = candidates(f"{area['name']}, California")
        if not found:
            print("  no usable candidates")
        for item in found[:6]:
            print(f"  {item['title'][:64]}")
            print(f"    {item['licence']} · {item['size']} · {item['author'][:40]}")
            if item["description"]:
                print(f"    {item['description'][:110]}")
            print(f"    {item['url']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
