"""Mello-Roos / CFD facts, from the primary source.

Source: County of San Diego Auditor & Controller, **Active Mello-Roos
Districts (CFD) for FY 2025-2026**
https://www.sandiegocounty.gov/content/dam/sdc/auditor/pdf/cfd.pdf
Retrieved 2026-07-25.

Why this file exists: `research/competitors.md` found that **not one
competitor page mentions Mello-Roos at all**, despite it being the single most
repeated buyer question in 92127. Everyone writes around it because getting it
right requires a primary source. This is that source.

**The honesty rule that governs every string here.** The Auditor's list names
districts; it does not map parcels. "No district in the list is named for
Scripps Ranch" is a fact. "Scripps Ranch has no Mello-Roos" is an inference,
and a homeowner could be in a differently-named district. Every claim below is
written as the former, and every page carries the instruction to check the
actual tax bill, which is where the truth for a given parcel lives.
"""

from __future__ import annotations

SOURCE_NAME = (
    "County of San Diego Auditor & Controller, "
    "Active Mello-Roos Districts (CFD) for FY 2025-2026"
)
SOURCE_URL = "https://www.sandiegocounty.gov/content/dam/sdc/auditor/pdf/cfd.pdf"
RETRIEVED = "2026-07-25"

# The line every page repeats. A CFD amount is parcel-specific and varies by
# district, improvement area and build phase — publishing a single number
# would be the same kind of false precision the AVM pages criticise.
VERIFY_NOTE = (
    "A Mello-Roos amount is specific to the parcel, not the neighborhood: it "
    "varies by district, improvement area and the phase a home was built in. "
    "The authoritative figure is the line item on the property tax bill, which "
    "names the district and gives a contact number."
)

# Districts relevant to the six communities, verbatim from the report.
DISTRICTS = {
    "del-sur": {
        "has_cfd": True,
        "districts": [
            ("Poway Unified CFD #12 (Blk Mtn Rch)", "6122-20", "KeyAnalytics", "(877) 575-0265"),
            ("Black Mountain Ranch Villages CFD #4", "6086-09", "Charmane Custodio", "(888) 892-2480"),
        ],
        "note": (
            "Del Sur sits inside the Black Mountain Ranch master plan and "
            "inside Poway Unified. Homes there can carry both a school-district "
            "CFD and a community CFD — which is why two similar homes on the "
            "same street can have materially different tax bills."
        ),
    },
    "4s-ranch": {
        "has_cfd": True,
        "districts": [
            ("Poway Unified CFD #6 and #6 IA B", "6122-06 / 6122-18", "KeyAnalytics", "(877) 575-0265"),
            ("Poway Unified CFD #10 and #10 IA B", "6122-10 / 6122-12", "KeyAnalytics", "(877) 575-0265"),
        ],
        "note": (
            "Poway Unified administers at least 19 separate community "
            "facilities districts across its boundary — the reason a single "
            "'4S Ranch Mello-Roos' figure does not exist. Which one applies "
            "depends on the parcel."
        ),
    },
    "scripps-ranch": {
        "has_cfd": False,
        "districts": [],
        "note": (
            "No community facilities district in the County Auditor's active "
            "FY 2025-26 list is named for Scripps Ranch. That is the "
            "documented basis for the widely-repeated claim that Scripps Ranch "
            "homes generally do not carry Mello-Roos — but it is a statement "
            "about district names, not a parcel-level guarantee."
        ),
    },
    "carmel-valley": {
        "has_cfd": False,
        "districts": [],
        "note": (
            "No community facilities district in the County Auditor's active "
            "FY 2025-26 list is named for Carmel Valley or Torrey Highlands. "
            "Neighbouring Black Mountain Ranch villages do carry districts, so "
            "the boundary matters and the tax bill is the place to confirm it."
        ),
    },
    "del-mar": {
        "has_cfd": False,
        "districts": [],
        "note": (
            "The Auditor's active FY 2025-26 list carries no community "
            "facilities district named for the city of Del Mar. Del Mar's "
            "property-tax questions are usually about Prop 13 basis after a "
            "long hold, and about Coastal Zone permitting, rather than CFDs."
        ),
    },
    "rancho-santa-fe": {
        "has_cfd": True,
        "districts": [
            ("Rancho Santa Fe CFD #1 (Community Service District)", "6870-04", "Paula Melendrez", "(760) 479-4150"),
        ],
        "note": (
            "Rancho Santa Fe has one community facilities district in the "
            "active list, administered by the Community Service District. It "
            "is not the dominant cost question in the Covenant — HOA and club "
            "membership obligations, septic, and Art Jury review usually are."
        ),
    },
}

# Poway Unified operates the largest CFD footprint of any agency in the
# county list. Both Del Sur and 4S Ranch are inside it.
PUSD_CFD_COUNT = 19
PUSD_ADMIN = ("KeyAnalytics", "(877) 575-0265")


def for_hood(slug: str) -> dict | None:
    return DISTRICTS.get(slug)

# --------------------------------------------------------------------------
# North County, added 2026-07-25 from the same County Auditor report.
#
# The headline: San Marcos runs 91 active districts — by far the most
# CFD-complex city in the county, and therefore the single best place for
# this data to be worth something.
#
# A caution recorded so nobody repeats the mistake: searching the report for
# "Vista" matches CHULA VISTA, which is South Bay. Vista proper has none.
# --------------------------------------------------------------------------

DISTRICTS.update({
    "san-marcos": {
        "has_cfd": True,
        "districts": [
            ("San Marcos CFD 98-02 — dozens of numbered improvement areas", "6090-xx", "CFD Administration", "(760) 744-1050"),
        ],
        "note": (
            "San Marcos carries 91 active community facilities districts in "
            "the County Auditor's list — more than any other city in San Diego "
            "County. Most are improvement areas within CFD 98-02, numbered "
            "individually, and which one applies is a question about the "
            "parcel rather than the city. Anyone quoting a single 'San Marcos "
            "Mello-Roos figure' has not looked."
        ),
    },
    "escondido": {
        "has_cfd": True,
        "districts": [
            ("Escondido Union SD CFD No. 2019-1", "6121-01", "KeyAnalytics", "(877) 575-0265"),
        ],
        "note": (
            "Escondido has one active district in the county list, a school "
            "district CFD formed in 2019, so it applies to newer development "
            "rather than the older housing stock that makes up most of the "
            "city. Most Escondido homes carry no CFD at all."
        ),
    },
    "carlsbad": {
        "has_cfd": True,
        "districts": [
            ("Carlsbad CFD #1", "6010-15", "Special District Financing", "(760) 233-2630"),
            ("Carlsbad Unified CFD #1 and #4", "6115-01 / 6115-04", "Willdan Public Info", "(866) 807-6864"),
        ],
        "note": (
            "Carlsbad has three active districts — one city, two school. "
            "Coverage is uneven across the four ZIPs, so the tax bill is the "
            "only reliable answer for a specific address."
        ),
    },
    "encinitas": {
        "has_cfd": True,
        "districts": [
            ("Encinitas CFD #1", "6036-42", "Willdan Financial", "(866) 807-6864"),
        ],
        "note": (
            "Encinitas has a single active district in the county list. Most "
            "of the city's housing predates CFD formation and carries none."
        ),
    },
    "valley-center": {
        "has_cfd": True,
        "districts": [
            ("Valley Center Fire Protection District CFD 2000-1", "3150-02", "Joe Napier", "(760) 751-7600"),
        ],
        "note": (
            "Valley Center's active district is a fire protection CFD rather "
            "than a school or development one — which is itself the useful "
            "signal for a buyer weighing a rural parcel: fire service here is "
            "funded, and separately assessed."
        ),
    },
    # Verified absences. Each is a fact about the county's district list, and
    # each is more useful to a buyer than the silence every competitor offers.
    "oceanside": {"has_cfd": False, "districts": [], "note": (
        "No community facilities district in the County Auditor's active "
        "FY 2025-26 list is named for Oceanside. For a buyer comparing "
        "Oceanside against San Marcos or 92127, that is a real monthly "
        "difference and it is rarely mentioned.")},
    "vista": {"has_cfd": False, "districts": [], "note": (
        "No community facilities district in the active list is named for "
        "Vista. Note that searching that list for 'Vista' returns Chula Vista "
        "districts, which are in South Bay — a confusion worth avoiding.")},
    "fallbrook": {"has_cfd": False, "districts": [], "note": (
        "No community facilities district in the active list is named for "
        "Fallbrook. Rural parcels there raise different cost questions "
        "instead — well, septic and fire insurance.")},
    "ramona": {"has_cfd": False, "districts": [], "note": (
        "No community facilities district in the active list is named for "
        "Ramona. As with Fallbrook, the real cost questions on a large parcel "
        "are well, septic and fire insurance rather than Mello-Roos.")},
    "poway": {"has_cfd": True, "districts": [
        ("Poway Unified CFDs — 19 active districts across the boundary", "6122-xx", "KeyAnalytics", "(877) 575-0265"),
    ], "note": (
        "Poway is inside Poway Unified, which administers 19 active districts "
        "— but most of that CFD load sits in the newer 92127 communities "
        "rather than in the city of Poway itself. That distinction is exactly "
        "the comparison inland buyers are trying to make, and almost nobody "
        "spells it out.")},
})

# --------------------------------------------------------------------------
# Southwest Riverside County, added 2026-07-30. A DIFFERENT COUNTY: the San
# Diego Auditor's list above says nothing about these cities, so each entry
# below carries its own source (the city's published CFD/debt records) and
# its own lead sentence, and tax_block/mello-roos render those instead of
# the San Diego defaults. The last tuple element is a website rather than a
# phone number — the renderers detect the "(" prefix to decide tel: linking.
# Facts verified 2026-07-30 against the pages cited per entry.
# --------------------------------------------------------------------------

DISTRICTS.update({
    "temecula": {
        "has_cfd": True,
        "districts": [
            ("Crowne Hill", "03-01", "City of Temecula", "temeculaca.gov"),
            ("Roripaugh Ranch", "03-02", "City of Temecula", "temeculaca.gov"),
            ("Wolf Creek", "03-03", "City of Temecula", "temeculaca.gov"),
            ("Harveston II", "03-06", "City of Temecula", "temeculaca.gov"),
        ],
        "lead": (
            "Temecula does carry Mello-Roos, extensively: the City of "
            "Temecula's own debt disclosures name city community facilities "
            "districts including Crowne Hill, Roripaugh Ranch, Wolf Creek "
            "and Harveston II, and Temecula Valley Unified School District "
            "levies its own special taxes in many tracts on top of the "
            "city's."
        ),
        "note": (
            "The city's districts are obligations of the property owners "
            "within each district boundary, not of the City of Temecula — "
            "and the school district's levies are separate again, so a "
            "Temecula tax bill can carry both a city and a school CFD line. "
            "The bill names each district that applies to the parcel."
        ),
        "source_name": "City of Temecula, Debt Management (community facilities district disclosures)",
        "source_url": "https://temeculaca.gov/509/Debt-Management",
        "retrieved": "2026-07-30",
    },
    "murrieta": {
        "has_cfd": True,
        "districts": [
            ("Springbrook", "2005-1", "City of Murrieta", "murrietaca.gov"),
            ("Gierson Ranch — noticed for bond authorization in 2026", "2026-1", "City of Murrieta", "murrietaca.gov"),
            ("Murrieta Valley USD districts", "2001-4 and 2004-1 among them", "the school district", "murrieta.k12.ca.us"),
        ],
        "lead": (
            "Murrieta does carry Mello-Roos: the City of Murrieta has "
            "formed ten community facilities districts to date under the "
            "Mello-Roos Act, and Murrieta Valley Unified School District "
            "levies special taxes through districts of its own."
        ),
        "note": (
            "New districts are still being formed — the city noticed the "
            "Gierson Ranch district for bond authorization in 2026 — so a "
            "brand-new tract's special-tax load is set at formation, before "
            "the first home sells. Western Municipal Water District also "
            "operates community facilities financing in the area. The tax "
            "bill names every district that applies."
        ),
        "source_name": "City of Murrieta, Community Facilities District pages",
        "source_url": "https://www.murrietaca.gov/1304/Community-Facilities-District",
        "retrieved": "2026-07-30",
    },
    "menifee": {
        "has_cfd": True,
        "districts": [
            ("Citywide maintenance CFD — every new development annexes in; 34 zones to date", "2015-2", "City of Menifee", "menifee.ca.gov"),
            ("Original city bond districts", "four formed at incorporation era", "City of Menifee", "menifee.ca.gov"),
            ("Menifee Union School District CFDs", "2014-3 among them", "the school district", "menifeeusd.org"),
        ],
        "lead": (
            "Menifee does carry Mello-Roos, and more of it on newer homes: "
            "the City of Menifee established four original bond districts "
            "and, since April 2015, a citywide maintenance district that "
            "every new development annexes into — thirty-four development "
            "zones so far — while the school and water districts levy "
            "separately."
        ),
        "note": (
            "Menifee's special taxes are billed through the County of "
            "Riverside and appear as separate line items on the property "
            "tax bill — the same reading skill the San Diego pages teach "
            "applies here, with different district names. Eastern Municipal "
            "Water District participates in community facilities financing "
            "for new development as well."
        ),
        "source_name": "City of Menifee, Special Districts (LLMD, CSA & CFD)",
        "source_url": "https://www.menifee.ca.gov/680/Special-Districts",
        "retrieved": "2026-07-30",
    },
})
