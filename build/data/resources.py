"""Official-resource links: the "check the record" layer under every guide.

Why this file exists
--------------------
The guides' evidence rule (build/data/guides.py) is that every passage names
the agency that holds the fact — "CAL FIRE publishes those maps", "the
district office is the only authority". Naming without linking makes the
reader do the finding. This file turns each guide's named authorities into a
verified link list rendered at the bottom of the neighborhood page, so
"checkable" means clickable.

It is also the honest version of what listing-embed competitor pages skip
entirely: the page ranking for "4S Ranch" at the time this file was created
linked to zero community resources — no district, no association, no county
page. Linking out to the actual authorities is a user service first and a
citation-credibility signal second; both are why it exists.

The rule
--------
Official sources only: government agencies, school districts, water and fire
districts, community master associations' own sites, official project pages.
Never: portals, ratings sites (school-rating links would also collide with
the HANDOFF §8 compliance line), news coverage, chambers of commerce,
Wikipedia, or anyone's realtor site. Every URL here was loaded and confirmed
official before it was added — the entry's `note` says what question the
page answers, and VERIFIED records the pass date. Re-verify annually with
the guide-refresh pass; government sites reorganise and a dead "official"
link reads worse than none.

Rendering: build/generate.py `build_neighborhood`. The links are followed
(no rel=nofollow) on purpose — citations to the authorities that hold the
record are the point, not a leak to be plugged.
"""

from __future__ import annotations

VERIFIED = "July 2026"

# ---- Shared entries (county/state-wide) --------------------------------
# Each area's list is explicit about which of these it includes — a Del Mar
# page has no business linking the county CFD list it isn't on.

AUDITOR_CFD = {
    "label": "County Auditor — active Mello-Roos district list",
    "url": "https://www.sandiegocounty.gov/content/dam/sdc/auditor/pdf/cfd.pdf",
    "note": (
        "the county's official list of every active CFD, with the "
        "administrator phone number for payoff and duration questions"
    ),
}

SPECIAL_ASSESSMENTS = {
    "label": "County special-assessments lookup",
    "url": "https://specialassessments.sandiegocounty.gov/",
    "note": (
        "enter a parcel number for the current-year breakdown of every "
        "fixed charge on the tax bill"
    ),
}

CALFIRE_FHSZ = {
    "label": "State Fire Marshal — Fire Hazard Severity Zone maps",
    "url": (
        "https://osfm.fire.ca.gov/what-we-do/community-wildfire-"
        "preparedness-and-mitigation/fire-hazard-severity-zones"
    ),
    "note": (
        "the address-lookup viewer for a parcel's official fire hazard "
        "severity zone designation"
    ),
}

COUNTY_PDS = {
    "label": "County of San Diego Planning & Development Services",
    "url": "https://www.sandiegocounty.gov/pds/",
    "note": (
        "the land-use and permitting authority for unincorporated "
        "communities — there is no city planning counter here"
    ),
}

SDUSD = {
    "label": "San Diego Unified School District",
    "url": "https://www.sandiegounified.org/",
    "note": (
        "the district that assigns schools here — confirm any specific "
        "address with its enrollment office"
    ),
}

STRO = {
    "label": "City Treasurer — short-term rental (STRO) program",
    "url": "https://www.sandiego.gov/treasurer/short-term-residential-occupancy",
    "note": (
        "license tiers, current availability counts and the rules that "
        "govern any rental under one month"
    ),
}


# ---- Per-area lists ----------------------------------------------------
# Populated by the July 2026 verification pass. Order within a list is
# roughly the order a buyer's questions arrive: land-use authority, schools,
# taxes, then the area-specific records.

RESOURCES: dict[str, list[dict]] = {}


def for_hood(slug: str) -> list[dict]:
    return RESOURCES.get(slug, [])
