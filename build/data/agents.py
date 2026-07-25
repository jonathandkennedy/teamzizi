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
        "name": "Nilab Azizi",
        "title": "Team Lead | REALTOR®",
        "dre": "02047962",
        "phone": "858.847.8067",
        "compass": "nilab-azizi",
        "photo": "/assets/img/team/headshot-nilab-azizi.png",
        "farms": None,
        "lead": True,
    },
    {
        "slug": "sofia-azizi",
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
        "name": "Michael Angotta",
        "title": "REALTOR® | DRE 02177007",
        "dre": "02177007",
        "phone": "323.533.9452",
        "compass": "michael-angotta",
        "photo": "/assets/img/team/headshot-michael-angotta.jpg",
        "farms": None,
    },
    {
        "slug": "mahan-taleshpour",
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

# The question to put to the client, one line per community. Six answers turn
# this whole system on.
PROPOSED_ASSIGNMENTS = """\
Which agent farms each of these? One name each; they become the page author,
the byline, the direct contact, and the schema author for that neighborhood.

  Del Sur (92127)          → ?
  4S Ranch (92127)         → ?
  Scripps Ranch (92131)    → ?
  Carmel Valley (92130)    → ?
  Del Mar (92014)          → ?
  Rancho Santa Fe (92067)  → ?

An agent may hold more than one. Any left unanswered keep the team lead as
author, which is accurate but weaker than a named local specialist.
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
