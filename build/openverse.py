"""Find freely-licensed neighborhood photography on Openverse.

    python3 build/openverse.py                 # areas that still have no photo
    python3 build/openverse.py encinitas       # one area

Same contract as build/commons.py: this finds CANDIDATES and installs
nothing. Every image is looked at by a human, and its caption read, before it
ships.

Why a second source
-------------------
Commons was exhausted at ten of sixteen areas. The six that came up empty —
4S Ranch, Carmel Valley, Encinitas, Fallbrook, Ramona, Valley Center — are
ordinary residential North County, not tourist destinations, and Commons is
an encyclopaedia's image library: it has the landmark and the courthouse, not
the suburb.

Openverse indexes Flickr, and Flickr is where people who actually live
somewhere post pictures of it. It also indexes US government accounts, whose
work is public domain outright. The Fallbrook result is the case in point:
Commons had nothing, and Openverse's top hit is a USDA photograph of an
avocado farm on Aguila Road, in the town that grows most of California's
avocados.

Licence handling
----------------
`license_type=commercial,modification` is asked of the API rather than
filtered afterwards, so NC and ND never enter the result set. The check is
repeated locally anyway, because a filter you did not verify is a filter you
are trusting on someone else's word.

  pdm, cc0   no obligation
  by, by-sa  attribution required and rendered; by-sa additionally makes any
             crop an adaptation that inherits the licence

Flickr caveat
-------------
A Flickr uploader chooses their own licence and can be wrong about it, in a
way a Commons reviewer usually catches. Where two candidates are equally good,
prefer the government account or the Commons file.
"""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

API = "https://api.openverse.org/v1/images/"
UA = "TeamAziziSiteBuild/1.0 (https://teamazizi.com; teamazizi@compass.com)"

OK_LICENCES = {"pdm", "cc0", "by", "by-sa"}

# The same trap as Commons: a place name matches events, signage and
# unrelated subject matter as readily as a streetscape.
REJECT_WORDS = (
    "protest", "rally", "sign ", "signage", "map", "diagram", "logo", "flag",
    "seal", "chart", "graph", "plaque", "gravestone", "cemetery", "crash",
    "fire", "wildfire", "flood", "damage", "wreck", "police", "arrest",
    "portrait", "headshot", "poster", "ballot", "election", "concert",
    "wedding", "birthday", "selfie",
)

# Search terms per area. A bare community name is too weak for the small ones
# — "Ramona" alone returns people named Ramona — so each is anchored to
# something that only exists in that place.
TERMS = {
    "encinitas": [
        "Encinitas California",
        "Self-Realization Fellowship Encinitas",
        "Moonlight Beach Encinitas",
    ],
    "fallbrook": [
        "Fallbrook California",
        "Fallbrook avocado grove",
    ],
    "ramona": [
        "Ramona California",
        "Ramona San Diego County",
        "Ramona Grasslands Preserve",
    ],
    "valley-center": [
        "Valley Center California",
        "Valley Center San Diego County",
    ],
    "carmel-valley": [
        "Carmel Valley San Diego",
        "Torrey Pines Carmel Valley San Diego",
    ],
    "4s-ranch": [
        "4S Ranch San Diego",
        "Rancho Bernardo San Diego",
    ],
}


def api(params: dict, *, tries: int = 4) -> dict:
    """GET with backoff. Openverse returns 504 under load often enough that a
    single-shot request loses whole areas to a transient gateway error."""
    url = f"{API}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code < 500 or attempt == tries - 1:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == tries - 1:
                raise
        time.sleep(2 ** attempt)
    return {}


# Flickr serves a size ladder off one photo id; Openverse indexes whichever
# rendition it saw, usually _b (1024px). Asking for the larger rungs first
# gets a hero-sized file instead of one that has to be upscaled.
FLICKR_LADDER = ("_k", "_h", "_b")


def biggest_flickr(url: str) -> str:
    """Try Flickr's larger renditions, falling back to the indexed one."""
    import re  # noqa: PLC0415

    match = re.search(r"^(.*)_(?:[bhkco])\.jpg$", url)
    if not match or "staticflickr" not in url:
        return url
    for rung in FLICKR_LADDER:
        candidate = f"{match.group(1)}{rung}.jpg"
        try:
            probe = urllib.request.Request(
                candidate, method="HEAD", headers={"User-Agent": UA}
            )
            with urllib.request.urlopen(probe, timeout=20) as response:
                if response.status == 200:
                    return candidate
        except Exception:  # noqa: BLE001 — a missing rung is not an error
            continue
    return url


def search(term: str, limit: int = 20) -> list[dict]:
    data = api({
        "q": term,
        "license_type": "commercial,modification",
        "page_size": str(limit),
        "mature": "false",
    })
    out = []
    for item in data.get("results", []):
        licence = (item.get("license") or "").lower()
        title = (item.get("title") or "").lower()

        if licence not in OK_LICENCES:
            continue
        if any(word in title for word in REJECT_WORDS):
            continue

        url = item.get("url") or ""
        # SVGs here are always the Wikipedia county locator map — a shaded
        # outline of where the town is, not a photograph of it.
        if url.lower().endswith(".svg"):
            continue

        width, height = item.get("width") or 0, item.get("height") or 0
        # Landscape only: a hero crops to a wide band, and a portrait file
        # loses its subject to that crop.
        if width and height and width < height:
            continue
        # 1024 is Flickr's common indexed rendition and the floor already
        # shipping on this site (san-marcos is 1024 wide). Below that a hero
        # would have to be upscaled.
        if width and width < 1024:
            continue

        out.append({
            "title": item.get("title") or "",
            "licence": f"{licence.upper()} {item.get('license_version') or ''}".strip(),
            "author": item.get("creator") or "",
            "author_url": item.get("creator_url") or "",
            "licence_url": item.get("license_url") or "",
            "url": url,
            "page": item.get("foreign_landing_url") or "",
            "source": item.get("source") or "",
            "size": f"{width}x{height}" if width else "?",
        })
    return out


def main() -> int:
    from data import photos  # noqa: PLC0415

    wanted = [a for a in sys.argv[1:] if not a.startswith("--")]
    slugs = wanted or [s for s in TERMS if s not in photos.CREDITS]

    for slug in slugs:
        print(f"\n=== {slug} ===")
        seen = set()
        for term in TERMS.get(slug, [slug.replace('-', ' ') + " California"]):
            for item in search(term):
                if item["url"] in seen:
                    continue
                seen.add(item["url"])
                print(f"  {item['title'][:70]}")
                print(
                    f"    {item['licence']} · {item['size']} · "
                    f"{item['author'][:30]} · {item['source']}"
                )
                print(f"    {item['url']}")
                print(f"    {item['page']}")
        if not seen:
            print("  no usable candidates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
