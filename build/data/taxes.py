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
