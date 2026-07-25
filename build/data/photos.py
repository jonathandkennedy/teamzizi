"""Provenance for every neighborhood photograph that is not ours.

Each entry records where the image came from, who made it, and under what
licence — because a photograph published without that is a photograph nobody
can check, and this site's whole argument is that its claims are checkable.
CC BY and CC BY-SA additionally REQUIRE attribution; rendering it is not a
courtesy.

Verification rule
-----------------
An entry only exists here after a human has looked at the image AND read its
Commons description to confirm it depicts the right place. That is not
bureaucracy. Commons text search on a California city name is actively
dangerous:

  "Carmel Valley, California"  -> Carmel Valley Village, MONTEREY COUNTY
  "Vista, California"          -> the State Capitol in Sacramento; Rio Vista
  "Valley Center, California"  -> Fountain Valley, Mission Valley, Napa Valley

The first of those is the exact error that put a Monterey County vineyard on
the Carmel Valley page of the old site. Three of twelve areas returned a
wrong place as their TOP result. Nothing here may be auto-selected.

Better method for the rest: Commons geosearch (list=geosearch with the
community's coordinates and a radius) returns files by location rather than
by name, which cannot match a same-named place 400 miles away.
"""

from __future__ import annotations

CREDITS: dict[str, dict[str, str]] = {
    "escondido": {
        "title": "Downtown Escondido Grand & Broadway Intersection",
        "author": "CaliforniaUrbanist",
        "licence": "CC BY-SA 4.0",
        "licence_url": "https://creativecommons.org/licenses/by-sa/4.0/",
        "source": "https://commons.wikimedia.org/wiki/File:Downtown_Escondido_Grand_%26_Broadway_Intersection.jpg",
        "depicts": "Grand Avenue at Broadway, downtown Escondido, looking "
                   "north-east toward the mountains.",
    },
    "oceanside": {
        "title": "Oceanside, California 01",
        "author": "Tgormanbrown",
        "licence": "CC BY-SA 4.0",
        "licence_url": "https://creativecommons.org/licenses/by-sa/4.0/",
        "source": "https://commons.wikimedia.org/wiki/File:Oceanside,_California_01.jpg",
        "depicts": "The beach and palms at Oceanside, with the pier beyond.",
    },
    "san-marcos": {
        "title": "Cal State San Marcos library",
        "author": "Eamuscatuli at English Wikipedia",
        "licence": "Public domain",
        "licence_url": "",
        "source": "https://commons.wikimedia.org/wiki/File:Cal_State_San_Marcos_library.jpg",
        "depicts": "The library at California State University San Marcos.",
    },
}


def for_hood(slug: str) -> dict | None:
    return CREDITS.get(slug)
