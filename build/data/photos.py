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

What actually worked, in the order it was tried
-----------------------------------------------
1. Commons text search on "<Name>, California" — got six areas, and would
   have got three wrong ones too if the captions had not been read.
2. Commons GEOsearch on the community centroid (build/commons.py near()) —
   three more. Immune to the same-name trap by construction, but only as
   good as the geotags, and Fallbrook's are wrong: every hit is San Luis Rey
   Mission Church, which is in Oceanside.
3. Openverse (build/openverse.py) — indexes Flickr, where people who live in
   a place post pictures of it, plus US government accounts whose work is
   public domain. This is what found Encinitas.
4. Commons text search on the DISAMBIGUATED name — "Carmel Valley San Diego",
   not "Carmel Valley, California"; "4S Ranch", not "4S Ranch, California".
   This is the step that should have been first. Commons keeps a category
   per community ("Carmel Valley, San Diego", "4S Ranch, California"), and
   a file carrying that category has been placed by a human who knew which
   Carmel Valley they meant. It found the last four.

The category is the strongest signal available and the cheapest to check.
Prefer it over description text, which is often just the file name again.
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
    "carmel-valley": {
        # Categorised "Carmel Valley, San Diego" on Commons — the category
        # that distinguishes it from Carmel Valley, Monterey County, which
        # is the wrong-place photograph the old site actually published.
        "title": "Carmel Valley San Diego",
        "author": "Navirav",
        "licence": "CC BY-SA 4.0",
        "licence_url": "https://creativecommons.org/licenses/by-sa/4.0/",
        "source": "https://commons.wikimedia.org/wiki/File:Carmel_Valley_San_Diego_2.JPG",
        "depicts": "Carmel Valley in San Diego, looking north from the south "
                   "rim across the canyon to the ridgeline development.",
    },
    "encinitas": {
        "title": "Boathouses, Encinitas",
        "author": "Invertzoo",
        "licence": "CC BY-SA 3.0",
        "licence_url": "https://creativecommons.org/licenses/by-sa/3.0/",
        "source": "https://commons.wikimedia.org/wiki/File:Boathouses,_Encinitas.JPG",
        "depicts": "The SS Encinitas and SS Moonlight — two houses built in "
                   "the shape of boats in the late 1920s, on Third Street.",
    },
    "ramona": {
        "title": "Montecito Ranch, Ramona",
        "author": "Jerrye & Roy Klotz, M.D.",
        "licence": "CC BY-SA 4.0",
        "licence_url": "https://creativecommons.org/licenses/by-sa/4.0/",
        "source": "https://commons.wikimedia.org/wiki/File:MONTECITO_RANCH,_RAMONA,_SAN_DIEGO_COUNTY.jpg",
        "depicts": "The 1880s ranch house at Montecito Ranch in Ramona, "
                   "later owned by the actor James Cagney.",
    },
    "fallbrook": {
        # Geotagged 33.4426, -117.2842 and categorised "Geography of
        # Fallbrook, California". Chosen over a USDA avocado-grove frame
        # from the same search because that one is a portrait of a named
        # farmer, not a picture of the place.
        "title": "Lynda Lane, Fallbrook",
        "author": "cultivar413",
        "licence": "CC BY 2.0",
        "licence_url": "https://creativecommons.org/licenses/by/2.0/",
        "source": "https://commons.wikimedia.org/wiki/File:180214_17_Fallbrook,_CA_-_Walk_around_Ross_Lake,_Lynda_Lane.jpg",
        "depicts": "A lane climbing past a hillside house near Ross Lake in "
                   "Fallbrook.",
    },
    "valley-center": {
        # This one was rejected on the first pass and that was wrong. The
        # file carries "Laguna Mountains (California)" alongside "Valley
        # Center, California" — two places fifty kilometres apart — and a
        # self-contradicting file is normally a stop. What settled it was
        # asking a different question: not "what does the file claim?" but
        # "who relies on it?" It is the lead image on the Valley Center,
        # California article across twenty-seven Wikipedias and is bound to
        # Wikidata Q2861838, and an editor deliberately recategorised it TO
        # "Valley Center, California" in 2020, removing the broader county
        # and CDP categories by hand. The Laguna Mountains tag is a stale
        # leftover; they are visible looking east from Valley Center.
        #
        # Usage is a stronger signal than metadata, because metadata is one
        # uploader and usage is many editors with something to lose.
        "title": "Valley Center, California",
        "author": "Vcdrummer",
        "licence": "CC BY 3.0",
        "licence_url": "https://creativecommons.org/licenses/by/3.0/",
        "source": "https://commons.wikimedia.org/wiki/File:Valley_Center.jpg",
        "depicts": "A dirt road past a coast live oak in the grassland and "
                   "low hills of Valley Center.",
        # Shot on a 2008 compact camera and flat straight out of it. Levels,
        # contrast, saturation and sharpening only — the response curve
        # applied to pixels that were already in the frame, which is what a
        # darkroom print does. Nothing added, nothing removed.
        "modified": "Cropped to fit; colour and contrast adjusted.",
    },
    "4s-ranch": {
        "title": "4S Ranch from Black Mountain",
        "author": "Peard33",
        "licence": "Public domain",
        "licence_url": "",
        "source": "https://commons.wikimedia.org/wiki/File:4sranch.JPG",
        "depicts": "4S Ranch seen from Black Mountain, looking across the "
                   "community to the hills beyond.",
    },
}


# Empty, and worth leaving in place. All sixteen areas are covered.
#
# It is here for the next area added to the book. When a search comes back
# with nothing verifiable, record the reason here rather than leaving the
# slot silently blank — otherwise the next person repeats the same search,
# and the risk is not that they find nothing again, it is that they are less
# careful and install the wrong place. That has already happened once on
# this site: Carmel Valley shipped a Monterey County vineyard, four hundred
# miles from the neighborhood it was selling.
REJECTED: dict[str, str] = {}


def for_hood(slug: str) -> dict | None:
    return CREDITS.get(slug)
