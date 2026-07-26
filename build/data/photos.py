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
    "carlsbad": {
        "title": "Carlsbad Santa Fe Depot",
        "author": "Jiobrien",
        "licence": "CC BY-SA 3.0",
        "licence_url": "https://creativecommons.org/licenses/by-sa/3.0/",
        "source": "https://commons.wikimedia.org/wiki/File:50D.CarlsbadSantaFeTrainStation.jpg",
        "depicts": "The Santa Fe Depot in Carlsbad Village, now the visitor "
                   "centre, beside the COASTER line.",
    },
    "poway": {
        "title": "Niles Nelson House",
        "author": "Visitor7",
        "licence": "CC BY-SA 3.0",
        "licence_url": "https://creativecommons.org/licenses/by-sa/3.0/",
        "source": "https://commons.wikimedia.org/wiki/File:Niles_Nelson_House-3.jpg",
        "depicts": "The Niles Nelson House, an original 1918 Poway farmhouse "
                   "relocated to Old Poway Park.",
    },
    "vista": {
        "title": "Alta Vista Gardens",
        "author": "Alan Islas",
        "licence": "CC BY-SA 4.0",
        "licence_url": "https://creativecommons.org/licenses/by-sa/4.0/",
        "source": "https://commons.wikimedia.org/wiki/File:Alta_Vista_Gardens_-_Dec_2020_-_Pic02.jpg",
        "depicts": "Alta Vista Gardens, the botanical garden on Brengle "
                   "Terrace in Vista.",
    },
}


REJECTED = {
    # Kept so nobody re-runs the same search and reaches the same wrong
    # conclusion. Every one of these was a TOP geosearch result.
    "fallbrook": "All top hits are San Luis Rey Mission Church, which is in "
                 "OCEANSIDE — the Commons geotags are wrong.",
    "valley-center": "Best hit is Daley Ranch, described as 'Escondido' with "
                     "'location is approximate'. The rest are an insect and a "
                     "child on a hay bale.",
    "carmel-valley": "Geosearch returns aquarium fish; name search returns "
                     "Monterey County. Nothing usable at either.",
    "4s-ranch": "Bongo drums, a group photo, an agave leaf close-up.",
    "encinitas": "Best hit is captioned only 'San Diego in September 2016' — "
                 "not verifiable as Encinitas.",
    "ramona": "Only archival black-and-white HABS survey photographs of a "
              "bridge. Correct place, wrong register for a hero.",
}


def for_hood(slug: str) -> dict | None:
    return CREDITS.get(slug)
