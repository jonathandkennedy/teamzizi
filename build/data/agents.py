"""Roster, and which neighborhood each agent farms.

The site's information architecture is neighborhood-first: a visitor arrives
at a place, and a named, licensed human owns that place. That is not a styling
choice. A page authored by "Team Azizi" is a company saying something; a page
authored by a named licensee with a DRE number, a direct line and a sold record
in that specific neighborhood is a person who can be checked — which is what
E-E-A-T rewards and what an assistant is willing to cite.

**`farms` is client data and cannot be inferred.** Nothing published anywhere
says which agent works which community; research/compass.md has the roster and
nothing about territory. So every assignment starts as None and the page falls
back to the team lead, who is a real, verifiable, accountable licensee. When the
client confirms, each assignment is a one-line change and the byline, the
schema author, the contact block and the /team grouping all follow from it.

Roster verbatim from the Compass team profile (research/compass.md). Titles are
as published — do not tidy them.
"""

from __future__ import annotations

# Neighborhood slug each agent farms, or None until the client confirms.
# See PROPOSED_ASSIGNMENTS below for the question to put to them.
ROSTER: list[dict] = [
    {
        "slug": "nilab-azizi",
        "instagram": "https://www.instagram.com/nilab.azizi_realtor/",
        "name": "Nilab Azizi",
        "title": "Team Lead | REALTOR®",
        "dre": "02047962",
        "phone": "858.847.8067",
        "compass": "nilab-azizi",
        "photo": "/assets/img/team/headshot-nilab-azizi.jpg",
        "farms": None,
        "lead": True,
    },
    {
        "slug": "sofia-azizi",
        "sales": 24,
        "instagram": "https://www.instagram.com/sofiaa_azizi/",
        "name": "Sofia Azizi",
        "title": "REALTOR® | DRE 02108624",
        "dre": "02108624",
        "phone": "858.705.5454",
        "compass": "sofia-azizi",
        "photo": "/assets/img/team/headshot-sofia-azizi.jpg",
        "farms": None,
    },
    {
        "slug": "zohra-azizi",
        "sales": 47,
        "name": "Zohra Azizi",
        "title": "Realtor® | DRE# 01992847",
        "dre": "01992847",
        "phone": "619.876.0110",
        "compass": "zohra-legler",  # Compass slug uses a surname variant
        "photo": "/assets/img/team/headshot-zohra-azizi.jpg",
        "farms": None,
    },
    {
        "slug": "masooma-azizi",
        "sales": 0,
        "name": "Masooma Azizi",
        "title": "Chief Financial Officer",
        "dre": None,
        "phone": "619.746.3669",
        "compass": "masooma-azizi",
        "photo": None,
        "farms": None,
        "operations": True,
    },
    {
        "slug": "dari-ahranjani",
        "sales": 17,
        "instagram": "https://www.instagram.com/dari.ahranjani/",
        "name": "Dari Ahranjani",
        "title": "REALTOR® | DRE# 02130344",
        "dre": "02130344",
        "phone": "760.505.2340",
        "compass": "dari-ahranjani",
        "photo": "/assets/img/team/headshot-dari-ahranjani.jpg",
        "farms": None,
    },
    {
        "slug": "candice-casares",
        "sales": 31,
        "name": "Candice Casares",
        "title": "REALTOR® | DRE# 02160651",
        "dre": "02160651",
        "phone": "760.505.5493",
        "compass": "candice-medina",
        "photo": "/assets/img/team/headshot-candice-casares.jpg",
        "farms": None,
    },
    {
        "slug": "sara-forgnone",
        "sales": 8,
        "name": "Sara Forgnone",
        "title": "Realtor® | DRE# 02045480",
        "dre": "02045480",
        "phone": "858.859.8527",
        "compass": "sara-forgnone",
        "photo": "/assets/img/team/headshot-sara-forgnone.jpg",
        "farms": None,
    },
    {
        "slug": "charisma-gallegos",
        "sales": 0,
        "name": "Charisma Gallegos",
        "title": "Assistant to The Azizi Team",
        "dre": None,
        "phone": "619.300.5530",
        "compass": "charisma-gallegos-sd",
        "photo": None,
        "farms": None,
        "operations": True,
    },
    {
        "slug": "melissa-lopez",
        "sales": 94,
        "languages": ['English', 'Spanish'],
        "name": "Melissa Lopez",
        "title": "REALTOR® | DRE# 01329108",
        "dre": "01329108",
        "phone": "760.855.3081",
        "compass": "melissa-gutierrez",
        "photo": "/assets/img/team/headshot-melissa-lopez.jpg",
        "farms": None,
    },
    {
        "slug": "candace-kirk",
        "sales": 35,
        "name": "Candace Kirk",
        "title": "Realtor® | DRE# 02059754",
        "dre": "02059754",
        "phone": "619.988.1143",
        "compass": "candace-kirk",
        "photo": "/assets/img/team/headshot-candace-kirk.jpg",
        "farms": None,
    },
    {
        "slug": "sarah-rivas",
        "sales": 11,
        "name": "Sarah Rivas",
        "title": "REALTOR® | DRE# 02112696",
        "dre": "02112696",
        "phone": "619.607.9000",
        "compass": "sarah-rivas",
        "photo": "/assets/img/team/headshot-sarah-rivas.jpg",
        "farms": None,
    },
    {
        "slug": "nicholas-miele",
        "sales": 75,
        "instagram": "https://www.instagram.com/nickmeh/",
        "name": "Nicholas Miele",
        "title": "REALTOR® | DRE# 02089615",
        "dre": "02089615",
        "phone": "760.685.7956",
        "compass": "nicholas-miele",
        "photo": "/assets/img/team/headshot-nicholas-miele.jpg",
        "farms": None,
    },
    {
        "slug": "jared-stransky",
        "sales": 51,
        "name": "Jared Stransky",
        "title": "Realtor® | DRE# 02081146",
        "dre": "02081146",
        "phone": "908.752.3747",
        "compass": "jared-stransky",
        "photo": "/assets/img/team/headshot-jared-stransky.jpg",
        "farms": None,
    },
    {
        "slug": "gabriela-santiago",
        "sales": 53,
        "languages": ['English', 'Spanish'],
        "name": "Gabriela Santiago",
        "title": "Agent | DRE# 01955750",
        "dre": "01955750",
        "phone": "619.577.2443",
        "compass": "gabriela-santiago",
        "photo": "/assets/img/team/headshot-gabriela-santiago.jpg",
        "farms": None,
    },
    {
        "slug": "tiffney-cipriani",
        "sales": 3,
        "instagram": "https://www.instagram.com/tiffneycipriani_realtor/",
        "name": "Tiffney Cipriani",
        "title": "REALTOR® | DRE# 02186323",
        "dre": "02186323",
        "phone": "314.610.3554",
        "compass": "tiffney-cipriani",
        "photo": None,
        "farms": None,
    },
    {
        "slug": "javier-hernandez",
        "sales": 95,
        "name": "Javier Hernandez",
        "title": "Realtor® | DRE# 02004707",
        "dre": "02004707",
        "phone": "619.738.4006",
        "compass": "javier-hernandez",
        "photo": None,
        "farms": None,
    },
    {
        "slug": "malcolm-schick",
        "sales": 33,
        "instagram": "https://www.instagram.com/sandiegomalcolm/",
        "name": "Malcolm Schick",
        "title": "REALTOR® | DRE# 02010355",
        "dre": "02010355",
        "phone": "619.316.3223",
        "compass": "malcolm-schick",
        "photo": None,
        "farms": None,
    },
    {
        "slug": "michael-angotta",
        "sales": 177,
        "instagram": "https://www.instagram.com/michael_angotta/",
        "website": "https://mikeangottasellssandiego.com/",
        "name": "Michael Angotta",
        "title": "REALTOR® | DRE 02177007",
        "dre": "02177007",
        "phone": "323.533.9452",
        "compass": "michael-angotta",
        "photo": "/assets/img/team/headshot-michael-angotta.jpg",
        "farms": "del-mar",  # confirmed by client 2026-07-25
    },
    {
        "slug": "mahan-taleshpour",
        "sales": 25,
        "languages": ['English', 'Farsi'],
        "name": "Mahan Taleshpour",
        "title": "REALTOR® | DRE# 02050744",
        "dre": "02050744",
        "phone": "818.939.1841",
        "compass": "mahan-taleshpour",
        "photo": None,
        "farms": None,
    },
]

# On the old site's /team but not on the current Compass roster. Held here
# rather than deleted: whether they departed is a client question, and their
# old /agent/{slug} URLs are still indexed and need a deliberate 301 either
# way. Not rendered.
FORMER = ["deanna-colby", "coby-herzog"]

# --------------------------------------------------------------------------
# Evidence-based proposals, 2026-07-25.
#
# These are now derived rather than guessed: a full sweep of all 1,009 Compass
# past sales plus the 18 individual agent pages. See research/salesRecord.md.
#
# They remain *proposals*. `farms` above stays None until the client confirms,
# because a transaction record shows where someone has closed, not where they
# have chosen to farm — and 1,009 sales attribute only 45 to these six
# communities in total.
# --------------------------------------------------------------------------

PROPOSED = {
    # 18 team sales in 92127. Del Sur and 4S Ranch are NOT separable by ZIP —
    # 92127 also covers Rancho Bernardo and Santaluz — so a per-community
    # split needs street-level data.
    "del-sur": ("zohra-azizi", "moderate", "6 sales in 92127; Sofia Azizi next at 3"),
    "4s-ranch": ("zohra-azizi", "moderate", "same 92127 pool; not separable from Del Sur by ZIP"),
    # Sofia holds both top Scripps sales ($3.5M, $3.2M); Zohra leads by count.
    "scripps-ranch": ("sofia-azizi", "moderate", "9 team sales; holds both top sales in 92131"),
    # See the Angotta caution below before publishing this one.
    "del-mar": ("michael-angotta", "CONFIRMED by client 2026-07-25", "3 of 6 team sales, plus hosted the Mira Montana launch"),
    "carmel-valley": (None, "low", "contested: Hernandez 3, Angotta 3, Miele 2 — Miele holds the $4.75M top sale"),
    # One sale in the entire 1,009-record history.
    "rancho-santa-fe": (None, "none", "ONE lifetime team sale (5918 Fairway Place, $2.9M). No basis for an expert page."),
}

# RESOLVED 2026-07-25. The brokerage-change worry was a false alarm:
# @realestatebuyangotta (YB Realty) is an OLD account. Current handles are
# @michael_angotta and mikeangottasellssandiego.com, both Compass. Client
# confirms he farms Del Mar, so `farms` is set above.
#
# One fact remains unaddressed and is worth knowing rather than acting on:
# 136 of his 177 sales are in Connecticut. It does not contradict the Del Mar
# assignment — a farm is where you work now — but the "recently sold in Del
# Mar" block on his page draws from six team sales, not 177.
ANGOTTA_CAUTION = False

PROPOSED_ASSIGNMENTS = """\
Confirm the agent who FARMS each community. We now have a proposal for four of
the six, derived from all 1,009 Compass sales — but a closing record shows
where someone has sold, not where they have chosen to farm, so these need a
yes or a correction:

  Del Sur (92127)          → Zohra Azizi?      (6 sales in 92127)
  4S Ranch (92127)         → Zohra Azizi?      (same ZIP pool — can you split
                                                Del Sur from 4S Ranch?)
  Scripps Ranch (92131)    → Sofia Azizi?      (holds both top sales there)
  Del Mar (92014)          → Michael Angotta?  (3 of 6 — but see below)
  Carmel Valley (92130)    → ?                 (genuinely contested three ways)
  Rancho Santa Fe (92067)  → ?                 (ONE sale, ever)

Three things that need answering alongside:

1. Rancho Santa Fe. One lifetime sale. An expert page there would be the
   thinnest page on the site, in the hardest SERP in the county. Recommend
   dropping it until there is a record — or telling us who is actively
   farming it now, if someone is.

2. Michael Angotta. 136 of his 177 sales are in Connecticut, and one of his
   Instagram accounts links to YB Realty rather than Compass. Is he staying,
   and is San Diego his focus?

3. The bigger question. Across 1,009 sales, only 45 (4.5%) are in these six
   communities; the median sale is $650,000 and 77.5% are under $1M. The
   actual book is Escondido (~96), South Bay, Oceanside, Fallbrook, Spring
   Valley. Are the six the farm you are building toward, or the farm you
   have? Both are legitimate answers, but they produce different sites.
"""


def by_slug(slug: str) -> dict:
    return next(a for a in ROSTER if a["slug"] == slug)


def team_lead() -> dict:
    return next(a for a in ROSTER if a.get("lead"))


def agents_only() -> list[dict]:
    """Licensed agents, excluding operations staff."""
    return [a for a in ROSTER if not a.get("operations")]


def for_neighborhood(slug: str) -> tuple[dict, bool]:
    """Return (agent, confirmed).

    Falls back to the team lead when no assignment is confirmed. She is a real
    licensee genuinely accountable for the team's content, so the page ships
    with a checkable named author rather than a placeholder or a company name.
    """
    for agent in ROSTER:
        if agent.get("farms") == slug:
            return agent, True
    return team_lead(), False


def unassigned() -> list[str]:
    assigned = {a["farms"] for a in ROSTER if a.get("farms")}
    from data import site  # local import keeps this module dependency-light

    return [h["slug"] for h in site.NEIGHBORHOODS if h["slug"] not in assigned]
