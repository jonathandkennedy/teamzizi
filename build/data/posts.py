"""Blog posts.

Each post is a dict of the same shape the guides use — a dek, then a list of
answer blocks. The blocks are what an AI Mode sub-query actually retrieves, so
a post is written as a set of standalone answers rather than an essay with a
conclusion. Anything that only makes sense read top to bottom is a post that
gets skipped.

The bar for adding one: it must answer something the sixteen neighborhood
guides do not, or it is cannibalising them. A post that restates a guide
splits the signal for that query across two URLs and helps nobody.

Every factual claim traces to a named source — a school district, a county
office, a state agency. No market figures that go stale, no invented detail.
"""

from __future__ import annotations

POSTS: list[dict] = [
    {
        "slug": "san-diego-school-district-by-address",
        "title": "Your San Diego address does not tell you your school district",
        "dek": (
            "A Carlsbad home can feed Encinitas schools. A San Diego address "
            "can feed Del Mar Union. Scripps Ranch is not in Poway Unified. "
            "Here is where the boundaries actually cross in North San Diego "
            "County, and how to check yours before you make an offer."
        ),
        "date": "2026-07-25",
        "author": "nilab-azizi",
        "description": (
            "School district boundaries in North San Diego County cross city "
            "lines and ZIP codes. Which Carlsbad, Carmel Valley, Scripps "
            "Ranch and Encinitas addresses feed which districts — and how to "
            "verify a specific address."
        ),
        "blocks": [
            {
                "anchor": "why-it-crosses",
                "question": "Why does my San Diego address feed a different city's school district?",
                "lead": (
                    "School district boundaries in San Diego County were "
                    "drawn independently of city boundaries and ZIP codes, "
                    "often decades earlier, and neither has been redrawn to "
                    "match the other since. A district is its own unit of "
                    "local government with its own elected board and its own "
                    "territory, and that territory routinely crosses city "
                    "lines in both directions."
                ),
                "body": (
                    "<p>The practical consequence is that the city on an "
                    "envelope predicts the school district poorly, and the "
                    "ZIP code predicts it worse. Buyers pay for school "
                    "assignment, so getting this wrong is expensive in both "
                    "directions &mdash; paying a premium for an assignment "
                    "that does not apply, or passing on a home that had the "
                    "one you wanted.</p>"
                ),
            },
            {
                "anchor": "carlsbad",
                "question": "Do all Carlsbad homes go to Carlsbad Unified?",
                "lead": (
                    "Not every Carlsbad home is assigned to Carlsbad Unified "
                    "School District. Homes in southern Carlsbad can be "
                    "assigned to Encinitas Union School District for "
                    "elementary and San Dieguito Union High School District "
                    "for secondary, and homes on the eastern edge can fall "
                    "into San Marcos Unified. A Carlsbad address does not by "
                    "itself determine the school."
                ),
                "body": (
                    "<p>This is the single most misjudged school question in "
                    "North San Diego County, and it moves real money. The "
                    "boundary follows neither the city line nor any of "
                    "Carlsbad&rsquo;s four ZIP codes. See the "
                    "<a href=\"/neighborhoods/carlsbad\">Carlsbad guide</a> "
                    "for how the four ZIPs otherwise differ.</p>"
                ),
            },
            {
                "anchor": "carmel-valley",
                "question": "Which district serves Carmel Valley if the address says San Diego?",
                "lead": (
                    "Much of Carmel Valley is served by Del Mar Union School "
                    "District for kindergarten through sixth grade and San "
                    "Dieguito Union High School District for grades seven "
                    "through twelve &mdash; despite the homes carrying City "
                    "of San Diego addresses. A San Diego address does not "
                    "mean San Diego Unified here."
                ),
                "body": (
                    "<p>Torrey Pines High School is a San Dieguito Union "
                    "school, and assignment to it is set by that "
                    "district&rsquo;s attendance areas rather than by being "
                    "in Carmel Valley at all. San Dieguito Union also runs a "
                    "school choice process, so the school a student is "
                    "assigned and the school a student attends are two "
                    "separate questions. More in the "
                    "<a href=\"/neighborhoods/carmel-valley\">Carmel Valley "
                    "guide</a>.</p>"
                ),
            },
            {
                "anchor": "scripps-ranch",
                "question": "Is Scripps Ranch in Poway Unified?",
                "lead": (
                    "Scripps Ranch is in San Diego Unified School District, "
                    "not Poway Unified &mdash; which catches buyers comparing "
                    "it against the 92127 communities a few miles north. "
                    "Scripps Ranch High School, Marshall Middle and the "
                    "community&rsquo;s elementary schools are all San Diego "
                    "Unified schools."
                ),
                "body": (
                    "<p>That fact also explains the tax difference people "
                    "notice between the two. Scripps Ranch carries no "
                    "community facilities district named for it in the County "
                    "Auditor&rsquo;s active list, while the Poway Unified "
                    "communities to the north carry several &mdash; different "
                    "district, different financing history, different bill. "
                    "See <a href=\"/mello-roos\">the Mello-Roos lookup</a>.</p>"
                ),
            },
            {
                "anchor": "cardiff",
                "question": "Does Cardiff-by-the-Sea have its own school district?",
                "lead": (
                    "Cardiff-by-the-Sea has its own separate elementary "
                    "district &mdash; the Cardiff School District &mdash; "
                    "even though it sits inside the City of Encinitas, where "
                    "the rest of the city is served by Encinitas Union School "
                    "District. Both then feed San Dieguito Union High School "
                    "District for grades seven through twelve."
                ),
                "body": (
                    "<p>So an Encinitas address involves two assignments to "
                    "verify, and which elementary district applies depends on "
                    "which of the city&rsquo;s five recognised communities the "
                    "parcel sits in. The "
                    "<a href=\"/neighborhoods/encinitas\">Encinitas guide</a> "
                    "covers all five.</p>"
                ),
            },
            {
                "anchor": "pusd-reach",
                "question": "How far does Poway Unified extend beyond the city of Poway?",
                "lead": (
                    "Poway Unified School District extends well beyond the "
                    "city of Poway, covering the 92127 communities of Del "
                    "Sur, 4S Ranch and the Black Mountain Ranch villages "
                    "&mdash; all of which carry City of San Diego addresses. "
                    "The district name describes its origin, not the limit of "
                    "its territory."
                ),
                "body": (
                    "<p>That reach is what makes the tax comparison worth "
                    "running. The district administers 19 active community "
                    "facilities districts, but the bulk of that load sits in "
                    "the newer 92127 communities rather than in the older "
                    "city of Poway, which was largely built before those "
                    "districts were formed. Same schools, materially "
                    "different monthly cost &mdash; see the "
                    "<a href=\"/neighborhoods/poway\">Poway guide</a>.</p>"
                ),
            },
            {
                "anchor": "escondido-two",
                "question": "Why does Escondido have two school districts?",
                "lead": (
                    "Escondido is served by two separate districts rather "
                    "than one unified district: Escondido Union School "
                    "District runs kindergarten through eighth grade, and "
                    "Escondido Union High School District runs ninth through "
                    "twelfth. Elementary and high school assignment are "
                    "therefore two different questions with two different "
                    "answers."
                ),
                "body": (
                    "<p>Outlying addresses complicate it further &mdash; "
                    "homes with Escondido mailing addresses on the eastern "
                    "and northern edges can fall into San Pasqual Union, "
                    "Valley Center-Pauma Unified or Bonsall Unified instead. "
                    "Fallbrook has the same two-tier structure, with Fallbrook "
                    "Union Elementary and Fallbrook Union High as separate "
                    "districts.</p>"
                ),
            },
            {
                "anchor": "how-to-check",
                "question": "How do I check the school district for a specific San Diego address?",
                "lead": (
                    "Confirm a San Diego County address with the district "
                    "office directly, using the full street address rather "
                    "than the city or ZIP code. Districts publish attendance "
                    "area lookups and will answer by phone, and their answer "
                    "is the only one that counts &mdash; a portal listing, a "
                    "listing description and a school-rating site are all "
                    "downstream of it and all go stale."
                ),
                "body": (
                    "<p>Two further cautions. Attendance areas are redrawn "
                    "from time to time, so an answer from three years ago is "
                    "not an answer now. And where a district runs a school "
                    "choice process, being assigned to a school and getting "
                    "into it are different things &mdash; ask how the process "
                    "works before treating an assignment as guaranteed.</p>"
                    "<p>Every <a href=\"/neighborhoods\">neighborhood "
                    "guide</a> states which districts serve that community "
                    "and where the boundaries are known to cross.</p>"
                ),
            },
        ],
    },
]


def by_slug(slug: str) -> dict | None:
    return next((p for p in POSTS if p["slug"] == slug), None)
