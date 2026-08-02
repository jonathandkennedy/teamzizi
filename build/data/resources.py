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

VERIFIED = "August 2026"

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


# ---- City of San Diego shared entries ----------------------------------

SDUSD_FINDER = {
    "label": "San Diego Unified — School Finder",
    "url": "https://www.sandiegounified.org/schools/school_finder",
    "note": (
        "the district's own address lookup for attendance boundaries — "
        "the authority on which school an address feeds"
    ),
}

SD_DSD = {
    "label": "City of San Diego Development Services",
    "url": "https://www.sandiego.gov/development-services",
    "note": (
        "permit lookup and the development-projects map — what is "
        "actually proposed near a given parcel"
    ),
}


# ---- Per-area lists ----------------------------------------------------
# Populated by the August 2026 verification pass (five parallel passes, one
# per area cluster; every URL loaded and its page title read before entry).
# Order within a list is roughly the order a buyer's questions arrive:
# land-use authority, schools, taxes, then the area-specific records.
#
# Catches from the pass, kept as a warning to future editors: the guessable
# helixwater.org is dead (503) — Helix Water District lives at hwd.com; the
# Downtown community-plan URL 301s to a Development Services page; SDSU
# planning moved to pdc.sdsu.edu. Verify, don't guess.

# Poway Unified's own special-tax page — the authority for the CFD math the
# 92127 guides walk through. Shared by three areas.
PUSD_CFD = {
    "label": "Poway Unified — Community Facilities Districts",
    "url": "https://www.powayusd.com/apps/pages/cfd",
    "note": (
        "the district's own Mello-Roos page — boundary maps, "
        "disclosures and prepayment procedures"
    ),
}

PUSD = {
    "label": "Poway Unified School District",
    "url": "https://www.powayusd.com/",
    "note": "the district — enrollment, schools and calendars",
}

PUSD_BOUNDARIES = {
    "label": "PUSD boundaries and district maps",
    "url": "https://www.powayusd.com/apps/pages/boundaries-and-district-maps",
    "note": (
        "attendance boundaries by level and the feeder-school chart — "
        "the authority on which school an address feeds"
    ),
}

RESOURCES: dict[str, list[dict]] = {
    # ---- 92127 / Poway Unified cluster --------------------------------
    # Recorded misses so nobody guesses later: 4sranch.org is a summer-camp
    # business, not the HOA; the 4S Ranch Master Association site could not
    # be verified (403 to all fetch methods) and so is not listed.
    "4s-ranch": [
        PUSD,
        PUSD_BOUNDARIES,
        PUSD_CFD,
        {
            "label": "County Parks — 4S Ranch community parks",
            "url": (
                "https://www.sdparks.org/content/sdparks/en/park-pages/"
                "4SRanchParks.html"
            ),
            "note": (
                "the six county-operated parks including the Sports "
                "Park — county-run because 4S Ranch is unincorporated"
            ),
        },
        {
            "label": "Rancho Santa Fe Fire Protection District",
            "url": "https://www.ranchosantafefire.gov/",
            "note": (
                "the fire agency for 4S Ranch — its service area "
                "extends well beyond Rancho Santa Fe itself"
            ),
        },
        {
            "label": "Olivenhain Municipal Water District",
            "url": "https://www.olivenhain.com/",
            "note": "water and wastewater provider for 4S Ranch",
        },
    ],
    "del-sur": [
        PUSD,
        PUSD_BOUNDARIES,
        PUSD_CFD,
        {
            "label": "Del Sur Community Association",
            "url": "https://delsurcommunity.org/",
            "note": (
                "the master association — pools, the Ranch House, "
                "design review and board records"
            ),
        },
        {
            "label": "Black Mountain Ranch Community Plan",
            "url": (
                "https://www.sandiego.gov/planning/community-plans/"
                "black-mountain-ranch"
            ),
            "note": (
                "the City of San Diego plan area that contains Del Sur "
                "— the community's actual land-use jurisdiction"
            ),
        },
    ],
    "poway": [
        {
            "label": "City of Poway",
            "url": "https://poway.org/",
            "note": "city hall — permits, services and water billing",
        },
        PUSD,
        PUSD_BOUNDARIES,
        PUSD_CFD,
        {
            "label": "Lake Poway Recreation Area",
            "url": "https://poway.org/401/Lake-Poway",
            "note": "the city-run lake — hours, fishing and trailheads",
        },
    ],
    "scripps-ranch": [
        SDUSD_FINDER,
        {
            "label": "Scripps Miramar Ranch Community Plan",
            "url": (
                "https://www.sandiego.gov/planning/community-plans/"
                "scripps-miramar-ranch"
            ),
            "note": "the city plan page for the southern plan area",
        },
        {
            "label": "Miramar Ranch North Community Plan",
            "url": (
                "https://www.sandiego.gov/planning/community-plans/"
                "miramar-ranch-north"
            ),
            "note": (
                "the northern plan area — Scripps Ranch spans two city "
                "plans, not one"
            ),
        },
        {
            "label": "Scripps Ranch Recreation Center",
            "url": (
                "https://www.sandiego.gov/park-and-recreation/centers/"
                "recctr/scripps"
            ),
            "note": "the city rec center and its programs",
        },
        CALFIRE_FHSZ,
    ],
    "carmel-valley": [
        {
            "label": "Del Mar Union School District",
            "url": "https://www.dmusd.org/",
            "note": "the K-6 district for most of Carmel Valley",
        },
        {
            "label": "DMUSD school boundaries and option areas",
            "url": (
                "https://www.dmusd.org/Departments/Enrollment/"
                "School-Boundaries-and-Option-Areas/index.html"
            ),
            "note": "the district's own locator and option-area maps",
        },
        {
            "label": "San Dieguito Union High School District",
            "url": "https://www.sduhsd.net/",
            "note": "the 7-12 district",
        },
        {
            "label": "SDUHSD boundaries map",
            "url": (
                "https://www.sduhsd.net/Our-District/About-Us-History/"
                "Boundaries-Map-/index.html"
            ),
            "note": (
                "attendance areas by elementary feeder — how Torrey "
                "Pines assignment actually gets decided"
            ),
        },
        {
            "label": "Carmel Valley Community Plan",
            "url": (
                "https://www.sandiego.gov/planning/community-plans/"
                "carmel-valley"
            ),
            "note": (
                "the city plan page — plan document, planning group "
                "agendas, facilities financing"
            ),
        },
    ],
    "rancho-santa-fe": [
        {
            "label": "Rancho Santa Fe Association",
            "url": "https://www.rsfassociation.org/",
            "note": (
                "the Covenant's governing association — design review, "
                "the Patrol and member records"
            ),
        },
        {
            "label": "Rancho Santa Fe School District",
            "url": "https://www.rsfschool.net/",
            "note": "the Covenant's own K-8 district — R. Roger Rowe School",
        },
        {
            "label": "SDUHSD boundaries map",
            "url": (
                "https://www.sduhsd.net/Our-District/About-Us-History/"
                "Boundaries-Map-/index.html"
            ),
            "note": (
                "which high school an RSF address feeds — the district's "
                "map shows the Torrey Pines / La Costa Canyon split"
            ),
        },
        {
            "label": "Rancho Santa Fe Fire Protection District",
            "url": "https://www.ranchosantafefire.gov/",
            "note": (
                "the fire district — note the official domain is "
                ".gov; the older rsf-fire.org redirects here"
            ),
        },
        {
            "label": "Santa Fe Irrigation District",
            "url": "https://www.sfidwater.org/",
            "note": "water provider for portions of the Ranch",
        },
        {
            "label": "County PDS — San Dieguito plan area",
            "url": (
                "https://www.sandiegocounty.gov/content/sdc/pds/gpupdate/"
                "comm/sdieguito.html"
            ),
            "note": (
                "the county planning page and community planning group "
                "for the unincorporated area — RSF has no city hall"
            ),
        },
    ],
    # ---- City of San Diego communities --------------------------------
    "la-jolla": [
        {
            "label": "La Jolla Community Plan",
            "url": "https://www.sandiego.gov/planning/community-plans/la-jolla",
            "note": (
                "the land-use plan that governs every La Jolla parcel "
                "while it remains City of San Diego territory"
            ),
        },
        {
            "label": "San Diego LAFCO — La Jolla incorporation",
            "url": (
                "https://www.sdlafco.org/resources/major-projects/"
                "la-jolla-incorporation-lafco-special-reorganization"
            ),
            "note": (
                "the official record of the cityhood proposal — every "
                "milestone in our tracker post cites this file"
            ),
        },
        SDUSD_FINDER,
        STRO,
    ],
    "pacific-beach": [
        {
            "label": "Pacific Beach Community Plan",
            "url": "https://www.sandiego.gov/planning/community-plans/pacific-beach",
            "note": (
                "the land-use plan for Pacific Beach, including the "
                "Balboa Avenue station-area plan on its eastern edge"
            ),
        },
        STRO,
        SDUSD_FINDER,
        {
            "label": "Mission Bay Park",
            "url": (
                "https://www.sandiego.gov/park-and-recreation/parks/"
                "regional/missionbay"
            ),
            "note": (
                "the city's page for the aquatic park that borders Crown "
                "Point and south PB"
            ),
        },
    ],
    "ocean-beach": [
        {
            "label": "Ocean Beach Community Plan",
            "url": "https://www.sandiego.gov/planning/community-plans/ocean-beach",
            "note": (
                "the plan behind the community's low-rise character — "
                "certified by the Coastal Commission in 2016"
            ),
        },
        STRO,
        SDUSD_FINDER,
        {
            "label": "Ocean Beach — city beach page",
            "url": "https://www.sandiego.gov/lifeguards/beaches/ob",
            "note": (
                "the lifeguard service's official page for the beach and "
                "pier conditions"
            ),
        },
    ],
    "hillcrest": [
        {
            "label": "Uptown Community Plan",
            "url": "https://www.sandiego.gov/planning/community-plans/uptown",
            "note": (
                "the governing plan for Hillcrest — the community sits "
                "inside the Uptown planning area"
            ),
        },
        {
            "label": "Hillcrest Focused Plan Amendment",
            "url": (
                "https://www.sandiego.gov/planning/community-plans/uptown/"
                "hillcrest-focused-plan-amendment"
            ),
            "note": (
                "the city's page for the 2024 rezone — what density now "
                "applies to which corridor"
            ),
        },
        {
            "label": "UC San Diego — Hillcrest campus rebuild",
            "url": "https://hillcrest.ucsd.edu/",
            "note": (
                "the university's own project page for the hospital "
                "replacement and campus phasing"
            ),
        },
        SD_DSD,
        SDUSD_FINDER,
        STRO,
    ],
    "north-park": [
        {
            "label": "North Park Community Plan",
            "url": "https://www.sandiego.gov/planning/community-plans/north-park",
            "note": (
                "the land-use plan for Greater North Park, historic "
                "resources included"
            ),
        },
        SDUSD_FINDER,
        STRO,
    ],
    "downtown-san-diego": [
        {
            "label": "Downtown Development — City of San Diego",
            "url": (
                "https://www.sandiego.gov/development-services/"
                "news-programs/downtown-development"
            ),
            "note": (
                "the city's current downtown planning page and the "
                "Downtown Community Plan it carries"
            ),
        },
        SD_DSD,
        SDUSD_FINDER,
        STRO,
    ],
    "college-area": [
        {
            "label": "College Area Community Plan",
            "url": "https://www.sandiego.gov/planning/community-plans/college-area",
            "note": (
                "the plan update adopted December 2025, with rezones "
                "effective early 2026 — read it before pricing land here"
            ),
        },
        {
            "label": "SDSU Planning, Design & Construction",
            "url": "https://pdc.sdsu.edu/",
            "note": (
                "the university's campus master plan and capital "
                "projects — the institutional neighbor's own record"
            ),
        },
        SDUSD_FINDER,
        STRO,
    ],
    # ---- Rural North County + Del Mar ---------------------------------
    "fallbrook": [
        COUNTY_PDS,
        {
            "label": "Fallbrook Union Elementary School District",
            "url": "https://www.fuesd.org/",
            "note": "the K-8 district",
        },
        {
            "label": "Fallbrook Union High School District",
            "url": "https://www.fuhsd.net/",
            "note": "the separate high-school district",
        },
        {
            "label": "Fallbrook Public Utility District",
            "url": "https://www.fpud.com/",
            "note": "water and wastewater provider",
        },
        {
            "label": "North County Fire Protection District",
            "url": "https://www.ncfireca.gov/",
            "note": (
                "fire and EMS for Fallbrook, Bonsall and Rainbow — the "
                "official domain is now .gov"
            ),
        },
        CALFIRE_FHSZ,
    ],
    "valley-center": [
        COUNTY_PDS,
        {
            "label": "Valley Center-Pauma Unified School District",
            "url": "https://www.vcpusd.org/",
            "note": "the PK-12 district",
        },
        {
            "label": "Valley Center Municipal Water District",
            "url": "https://www.vcmwd.org/",
            "note": (
                "the water and wastewater district — the cost line "
                "rural buyers most often underestimate"
            ),
        },
        {
            "label": "Valley Center Fire Protection District",
            "url": "https://valleycenterfire.com/",
            "note": "the fire district — board agendas and station records",
        },
        CALFIRE_FHSZ,
    ],
    "ramona": [
        COUNTY_PDS,
        {
            "label": "Ramona Unified School District",
            "url": "https://www.ramonausd.net/",
            "note": "the K-12 district",
        },
        {
            "label": "Ramona Municipal Water District",
            "url": "https://www.rmwd.org/",
            "note": "water and wastewater provider",
        },
        CALFIRE_FHSZ,
    ],
    "del-mar": [
        {
            "label": "Del Mar Planning & Community Development",
            "url": "https://www.delmar.ca.us/156/Planning-Community-Development",
            "note": "permitting, design review and the city's zoning record",
        },
        {
            "label": "Del Mar short-term rentals",
            "url": "https://www.delmar.ca.us/563/Short-Term-Rentals",
            "note": (
                "the city's own STR system — a 129-permit citywide cap "
                "with a waitlist, separate from San Diego's"
            ),
        },
        {
            "label": "Del Mar rail projects hub",
            "url": "https://www.delmar.ca.us/838/SANDAGNCTD-Rail-Projects",
            "note": (
                "the city's one-stop page on bluff stabilization and "
                "the realignment our tracker post follows"
            ),
        },
        {
            "label": "SANDAG — LOSSAN rail realignment",
            "url": (
                "https://www.sandag.org/projects-and-programs/"
                "featured-projects/lossan-corridor-improvements/"
                "lossan-rail-realignment"
            ),
            "note": (
                "the agency's own project page for moving the tracks "
                "off the bluffs — routes, studies and comment windows"
            ),
        },
        {
            "label": "Del Mar Union School District",
            "url": "https://www.dmusd.org/",
            "note": "the K-6 district",
        },
        {
            "label": "San Dieguito Union High School District",
            "url": "https://www.sduhsd.net/",
            "note": "the 7-12 district",
        },
    ],
    # ---- Riverside corridor -------------------------------------------
    # Riverside County Planning (planning.rctlma.org) is bot-shielded and
    # could not be verified loading; the county's rivco.gov Wine Country
    # page stands in as the verified county link.
    "temecula": [
        {
            "label": "City of Temecula",
            "url": "https://www.temeculaca.gov/",
            "note": "city hall — planning, permits and services",
        },
        {
            "label": "Temecula Valley Unified School District",
            "url": "https://www.tvusd.k12.ca.us/",
            "note": "the K-12 district — this is the canonical domain",
        },
        {
            "label": "Rancho California Water District",
            "url": "https://www.ranchowater.com/",
            "note": "water provider for Temecula and parts of Murrieta",
        },
        {
            "label": "County of Riverside — Temecula Valley Wine Country",
            "url": "https://rivco.gov/temecula-valley-wine-country",
            "note": (
                "the county's Wine Country page — the vineyards are "
                "unincorporated county land, not city of Temecula"
            ),
        },
        CALFIRE_FHSZ,
    ],
    "murrieta": [
        {
            "label": "City of Murrieta",
            "url": "https://www.murrietaca.gov/",
            "note": "city hall — planning, permits and services",
        },
        {
            "label": "Murrieta Valley Unified School District",
            "url": "https://www.murrieta.k12.ca.us/",
            "note": "the PK-12 district for most city addresses",
        },
        {
            "label": "Western Municipal Water District",
            "url": "https://westernwaterca.gov/",
            "note": (
                "one of three water providers splitting Murrieta — "
                "which serves a parcel is an address-level fact"
            ),
        },
        {
            "label": "Eastern Municipal Water District",
            "url": "https://www.emwd.org/",
            "note": "another of Murrieta's water providers — confirm by address",
        },
        CALFIRE_FHSZ,
    ],
    "menifee": [
        {
            "label": "City of Menifee",
            "url": "https://www.menifee.ca.gov/",
            "note": (
                "city hall — the official domain is menifee.ca.gov; "
                "the older .us address redirects here"
            ),
        },
        {
            "label": "Menifee Union School District",
            "url": "https://www.menifeeusd.org/",
            "note": "the TK-8 district for most of the city",
        },
        {
            "label": "Perris Union High School District",
            "url": "https://www.puhsd.org/",
            "note": "the secondary district for much of Menifee",
        },
        {
            "label": "Romoland School District",
            "url": "https://www.romoland.net/",
            "note": (
                "the TK-8 district for the city's northeast — Menifee "
                "spans three school systems"
            ),
        },
        {
            "label": "Eastern Municipal Water District",
            "url": "https://www.emwd.org/",
            "note": "water and sewer provider",
        },
    ],
    # ---- North County cities ------------------------------------------
    # Same-acronym trap, recorded so nobody "fixes" it: Escondido Union is
    # eusd.org; Encinitas Union is eusd.net. Both verified 2026-08-02.
    "escondido": [
        {
            "label": "Escondido development projects",
            "url": "https://www.escondido.gov/244/Development-Project-Information",
            "note": (
                "the city's own dashboard of active projects — the "
                "record behind our housing-pipeline post"
            ),
        },
        {
            "label": "Escondido ADU program",
            "url": "https://www.escondido.gov/238/Accessory-Dwelling-Units",
            "note": (
                "the city's ADU rules and pre-approved plans — note the "
                "city allows rentals only at 30 days or longer"
            ),
        },
        {
            "label": "Escondido Union School District",
            "url": "https://www.eusd.org/",
            "note": "the K-8 district for most Escondido addresses",
        },
        {
            "label": "Escondido Union High School District",
            "url": "https://www.euhsd.org/",
            "note": (
                "the separate 9-12 district — its site carries the "
                "find-your-school map"
            ),
        },
        CALFIRE_FHSZ,
    ],
    "san-marcos": [
        {
            "label": "San Marcos planning projects",
            "url": (
                "https://www.sanmarcosca.gov/Business-Services/"
                "Development/Planning/Projects"
            ),
            "note": "the city's pipeline of proposed and approved projects",
        },
        {
            "label": "San Marcos Unified School District",
            "url": "https://www.smusd.org/",
            "note": "the K-12 district for nearly all of San Marcos",
        },
        {
            "label": "SMUSD attendance-area maps",
            "url": "https://www.smusd.org/attendance-area-maps",
            "note": (
                "the district's own boundary maps — it warns that new "
                "subdivisions can be re-assigned"
            ),
        },
        {
            "label": "Vallecitos Water District",
            "url": "https://www.vwd.org/",
            "note": "water and sewer provider for most of the city",
        },
        AUDITOR_CFD,
        SPECIAL_ASSESSMENTS,
    ],
    "vista": [
        {
            "label": "Vista Community Development",
            "url": "https://www.vista.gov/departments/community-development",
            "note": (
                "planning and permits, with the city's development-"
                "projects map and the Vista 2050 plan update"
            ),
        },
        {
            "label": "Vista Unified School District",
            "url": "https://www.vistausd.org/",
            "note": "the K-12 district serving Vista",
        },
        {
            "label": "VUSD enrollment and school locator",
            "url": (
                "https://www.vistausd.org/departments/educationalexcellence/"
                "student-support-services/enrollment-and-transfers"
            ),
            "note": "the district's address-lookup and transfer process",
        },
        {
            "label": "Vista Irrigation District",
            "url": "https://www.vidwater.org/",
            "note": "the water supplier for Vista addresses",
        },
    ],
    "oceanside": [
        {
            "label": "Oceanside Planning Division",
            "url": (
                "https://www.ci.oceanside.ca.us/government/"
                "development-services/planning"
            ),
            "note": (
                "zoning, coastal review and the project search behind "
                "our Mission Avenue build-out post"
            ),
        },
        {
            "label": "Oceanside short-term rental program",
            "url": "https://www.ci.oceanside.ca.us/residents/short-term-rentals",
            "note": (
                "the city's own STR permit system — new non-hosted "
                "rentals are prohibited outside the Coastal Zone"
            ),
        },
        {
            "label": "Oceanside Local Coastal Program update",
            "url": (
                "https://www.ci.oceanside.ca.us/government/"
                "development-services/planning/local-coastal-program-update"
            ),
            "note": (
                "the coastal-hazard and sea-level planning that governs "
                "west-of-Coast-Highway property"
            ),
        },
        {
            "label": "Oceanside Unified School District",
            "url": "https://www.oside.us/",
            "note": "the district for most Oceanside addresses",
        },
        {
            "label": "OUSD school boundaries",
            "url": (
                "https://www.oside.us/family-community/"
                "registration-information/school-boundaries-locator"
            ),
            "note": (
                "the district's locator — southern slivers of the city "
                "fall in Carlsbad Unified instead, so check the address"
            ),
        },
    ],
    "carlsbad": [
        {
            "label": "Carlsbad Community Development",
            "url": "https://www.carlsbadca.gov/departments/community-development",
            "note": (
                "planning, coastal permits and the city's development-"
                "research tools"
            ),
        },
        {
            "label": "Carlsbad short-term vacation rentals",
            "url": (
                "https://www.carlsbadca.gov/departments/"
                "community-development/short-term-vacation-rentals"
            ),
            "note": (
                "the city's STVR permit — allowed only in the Coastal "
                "Zone and one master-plan area"
            ),
        },
        {
            "label": "Carlsbad Unified School District",
            "url": "https://carlsbadusd.net/",
            "note": (
                "the district for most, not all, of Carlsbad — the "
                "boundary does not follow the city line"
            ),
        },
        {
            "label": "Encinitas Union School District",
            "url": "https://www.eusd.net/",
            "note": (
                "the elementary district for parts of southern Carlsbad "
                "— the most misjudged boundary in North County"
            ),
        },
        {
            "label": "San Dieguito Union High School District",
            "url": "https://www.sduhsd.net/",
            "note": "the 7-12 district for those same southern addresses",
        },
        {
            "label": "Carlsbad trails",
            "url": (
                "https://www.carlsbadca.gov/departments/parks-recreation/"
                "lagoons-trails-open-space/trails"
            ),
            "note": "the city's own inventory of its trail network",
        },
    ],
    "encinitas": [
        {
            "label": "Encinitas Development Services",
            "url": (
                "https://www.encinitasca.gov/government/departments/"
                "development-services"
            ),
            "note": "planning, housing policy, ADU and coastal programs",
        },
        {
            "label": "Encinitas short-term rental permits",
            "url": (
                "https://www.encinitasca.gov/government/departments/"
                "development-services/land-development-building/"
                "regulatory-permits/short-term-rental-permits"
            ),
            "note": (
                "the city's own STR permit — single-family and duplex "
                "only, with inspection and neighbor notice"
            ),
        },
        {
            "label": "Encinitas Union School District",
            "url": "https://www.eusd.net/",
            "note": "the K-6 district for most of the city",
        },
        {
            "label": "Cardiff School District",
            "url": "https://www.cardiffschools.com/",
            "note": (
                "the separate two-school elementary district serving "
                "Cardiff-by-the-Sea"
            ),
        },
        {
            "label": "San Dieguito Union High School District",
            "url": "https://www.sduhsd.net/",
            "note": "the 7-12 district for all of Encinitas",
        },
        {
            "label": "Olivenhain Municipal Water District",
            "url": "https://www.olivenhain.com/",
            "note": (
                "water provider for eastern Encinitas and operator of "
                "the Elfin Forest reserve"
            ),
        },
    ],
    # ---- South Bay / East County --------------------------------------
    "chula-vista": [
        {
            "label": "City of Chula Vista Development Services",
            "url": "https://www.chulavistaca.gov/departments/development-services",
            "note": "permits, zoning and code questions for either side of the 805",
        },
        {
            "label": "Chula Vista Elementary School District",
            "url": "https://www.cvesd.org",
            "note": "the K-6 district — enrollment and school assignment",
        },
        {
            "label": "CVESD community facilities districts portal",
            "url": "https://www.specialdistricttransparency.com/cvesd",
            "note": (
                "the elementary district's own CFD lookup — parcel "
                "number in, current tax and final year out"
            ),
        },
        {
            "label": "Sweetwater Union High CFD records",
            "url": "https://fiscal.sweetwaterschools.org/cfd",
            "note": (
                "the 7-12 district's Mello-Roos reports and formation "
                "documents, on its own fiscal-services site"
            ),
        },
        {
            "label": "Chula Vista short-term rental rules",
            "url": (
                "https://www.chulavistaca.gov/departments/"
                "development-services/short-term-rentals"
            ),
            "note": (
                "the city's own STR ordinance — separate from San "
                "Diego's system entirely"
            ),
        },
        {
            "label": "Chula Vista Bayfront project",
            "url": "https://www.chulavistaca.gov/residents/chula-vista-bayfront",
            "note": "the city's page for the 535-acre waterfront build-out",
        },
        SPECIAL_ASSESSMENTS,
    ],
    "santee": [
        {
            "label": "City of Santee",
            "url": "https://www.cityofsanteeca.gov",
            "note": "city hall — planning, permits and council agendas",
        },
        {
            "label": "Fanita Ranch project page",
            "url": "https://www.cityofsanteeca.gov/planning/fanita-ranch",
            "note": (
                "the city's official file on the project our tracker "
                "post follows — EIRs, hearings, applications"
            ),
        },
        {
            "label": "Santee School District",
            "url": "https://www.santeesd.net",
            "note": "the K-8 district serving the city",
        },
        {
            "label": "Grossmont Union High School District",
            "url": "https://www.guhsd.net",
            "note": "the high-school district for Santee addresses",
        },
        {
            "label": "Padre Dam Municipal Water District",
            "url": "https://www.padredam.org",
            "note": "water and sewer provider — rates and service maps",
        },
        {
            "label": "Santee Lakes Recreation Preserve",
            "url": "https://www.santeelakes.com",
            "note": (
                "the 190-acre park, owned and operated by Padre Dam — "
                "the district's own recreation site"
            ),
        },
        CALFIRE_FHSZ,
    ],
    "el-cajon": [
        {
            "label": "City of El Cajon",
            "url": "https://www.elcajon.gov",
            "note": "city hall — planning, permits and code questions",
        },
        {
            "label": "Cajon Valley Union School District",
            "url": "https://www.cajonvalley.net",
            "note": "the elementary and middle-school district",
        },
        {
            "label": "Grossmont Union High School District",
            "url": "https://www.guhsd.net",
            "note": "the high-school district, headquartered in El Cajon",
        },
        {
            "label": "Gillespie Field — County airports",
            "url": (
                "https://www.sandiegocounty.gov/content/sdc/dpw/airports/"
                "gillespie.html"
            ),
            "note": (
                "the county's own page for the airfield — flight "
                "patterns and operations, from the operator"
            ),
        },
    ],
    "spring-valley": [
        COUNTY_PDS,
        {
            "label": "Spring Valley Community Planning Group",
            "url": (
                "https://www.sandiegocounty.gov/content/sdc/pds/gpupdate/"
                "comm/springvly.html"
            ),
            "note": (
                "the county's page for the local land-use advisory "
                "group — agendas and minutes for every project heard"
            ),
        },
        {
            "label": "La Mesa-Spring Valley School District",
            "url": "https://www.lmsvschools.org",
            "note": "the K-8 district for most Spring Valley addresses",
        },
        {
            "label": "Grossmont Union High School District",
            "url": "https://www.guhsd.net",
            "note": "the high-school district",
        },
        {
            "label": "Helix Water District",
            "url": "https://www.hwd.com/",
            "note": (
                "water provider for northern and central Spring Valley "
                "— the district's site is hwd.com, not the guessable "
                "domain"
            ),
        },
        {
            "label": "Otay Water District",
            "url": "https://otaywater.gov/",
            "note": (
                "water and sewer provider for southern Spring Valley — "
                "which district serves a parcel is an address-level fact"
            ),
        },
    ],
    "lemon-grove": [
        {
            "label": "City of Lemon Grove",
            "url": "https://www.lemongrove.ca.gov",
            "note": "city hall — planning, permits and council agendas",
        },
        {
            "label": "Lemon Grove School District",
            "url": "https://www.lemongrovesd.net",
            "note": "the K-8 district serving the city",
        },
        {
            "label": "Grossmont Union High School District",
            "url": "https://www.guhsd.net",
            "note": "the high-school district",
        },
        {
            "label": "Helix Water District",
            "url": "https://www.hwd.com/",
            "note": "the water provider for Lemon Grove addresses",
        },
    ],
}


def for_hood(slug: str) -> list[dict]:
    return RESOURCES.get(slug, [])
