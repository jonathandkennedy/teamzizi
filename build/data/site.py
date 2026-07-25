"""Canonical site data — the single source of truth for every string that
appears in more than one place.

HANDOFF.md §3 is explicit: schema, footer NAP and (once it exists) the Google
Business Profile must be one entity or they are three. Nothing in this file
may be retyped by hand elsewhere in the build.

Anything still awaiting client confirmation is marked with a `PENDING_`
constant or a `verified` flag so validate.py can refuse to ship an
unconfirmed claim.
"""

# --------------------------------------------------------------------------
# Identity — HANDOFF.md §3
# --------------------------------------------------------------------------

NAME = "Team Azizi"
NAME_LONG = "Team Azizi Real Estate | Compass San Diego"
# The long form disambiguates from Azizi Developments (Dubai), which
# dominates generic "Azizi real estate" results. Pending client confirm,
# but everything ships with one string either way.
NAME_CONFIRMED_BY_CLIENT = False

DOMAIN = "https://teamazizi.com"

STREET = "12860 El Camino Real, Suite 100"
CITY = "San Diego"
REGION = "CA"
POSTAL = "92130"
COUNTRY = "US"

PHONE_DISPLAY = "(858) 847-8067"
PHONE_SCHEMA = "+18588478067"
PHONE_HREF = "tel:+18588478067"
EMAIL = "teamazizi@compass.com"

# Approximate rooftop coordinates for the Carmel Valley Compass office.
# MUST be re-pinned to the GBP location once the profile exists — schema
# and GBP disagreeing is the exact failure mode this file exists to prevent.
GEO = {"lat": 32.9465, "lon": -117.2318, "verified": False}

LEAD_AGENT = "Nilab Azizi"
LEAD_DRE = "02047962"
BROKERAGE = "Compass California III, Inc."
BROKERAGE_DRE = "01527365"

# Strings to purge on sight — every one of these is live somewhere on the
# web today and is actively corrupting the entity (research/social.md §NAP).
STALE_STRINGS = (
    "10550 Craftsman Way",
    "11682 El Camino Real",
    "16092 Falcon Crest",
    "(619) 929-9691",
    "619-929-9691",
    "sonia@teamazizi.com",
    "nilab.azizi@compass.com",  # old site footer; team address is canonical
    "Upstart Residential",
    "Upstart Real Estate",
    "01426453",
    "45 Ranch",
    "Luxury Presence",
    "Top 1%",  # old-site claim, never third-party verified — use RealTrends
)

# --------------------------------------------------------------------------
# Proof points — every one third-party verifiable. HANDOFF.md §3.
# No invented stats, no aggregateRating, ever.
# --------------------------------------------------------------------------

PROOF = {
    "volume_2025": "$105.59M",
    "sides_2025": "92",
    "del_mar_rank": "#1 in Del Mar by sides, #2 by volume",
    "ca_rank": "#58 in California by volume",
    "national_rank": "#265 nationally by volume",
    "closed_sales": "1,016",
    "closed_rentals": "43",
    "active_range": "$369,000 – $5,875,000",
    "top_sold": "$6,100,000",
    "sdbj": "Named among San Diego's Best Teams, San Diego Business Journal 2025",
    # The list is published under RealTrends' 2026 program and reports 2025
    # production. Naming both matters: cite it as "2025" alone and a reader who
    # clicks through lands on a page headed "2026 Best Real Estate Large Teams
    # in California" and thinks the number is stale.
    "list_name": "2026 Best Real Estate Large Teams in California",
    "list_rank": "#58",
    "source": (
        "RealTrends Verified 2026 program (2025 production) · "
        "San Diego Business Journal · Compass"
    ),
    "source_url": (
        "https://www.realtrends.com/ranking/best-real-estate-agents-california/"
        "large-teams-volume/"
    ),
    "profile_url": (
        "https://www.realtrends.com/team-profile/team-azizi-california-compass/"
    ),
}

# Resolved 2026-07-25 — the client supplied the RealTrends listing directly,
# confirming #58 of all California Large Teams by volume.
#
# This does NOT substantiate the "Top 1% in SD County" line in their Instagram
# bio: different denominator (California large teams vs every agent in San
# Diego County) and no published source behind it. It makes that line
# unnecessary instead. "#58 Large Team in California, RealTrends Verified" is
# a stronger claim precisely because a reader can click it and check — and it
# is not the identical string their most direct competitor already uses.
#
# Recommendation to the client: adopt this language in the bio too, so the
# site and the profile assert the same checkable thing.
BIO_CLAIM_TO_REPLACE = "Top 1% in SD County"

# --------------------------------------------------------------------------
# Services — mirrored exactly into schema hasOfferCatalog and, later, the
# GBP services menu. Descriptions are required: "lists of services with
# descriptions, not just names" (research/aiPlaybook.md §5).
# --------------------------------------------------------------------------

SERVICES = [
    {
        "slug": "listing-representation",
        "name": "Listing Representation",
        "description": (
            "Full-service representation for sellers across North San Diego "
            "County, including pricing strategy, preparation, photography and "
            "marketing, negotiation and close management."
        ),
    },
    {
        "slug": "buyer-representation",
        "name": "Buyer Representation",
        "description": (
            "Buyer-side representation from search through close, including "
            "neighborhood and school-boundary guidance, offer strategy in "
            "competitive situations, and inspection and contingency management."
        ),
    },
    {
        "slug": "home-valuation",
        "name": "Home Valuation",
        "description": (
            "A comparative market analysis of a specific property prepared "
            "from MLS and county records, covering recent comparable sales, "
            "current competing inventory and a realistic pricing range."
        ),
    },
    {
        "slug": "compass-concierge",
        "name": "Compass Concierge",
        "description": (
            "Compass Concierge fronts the cost of preparing a home for market "
            "— staging, cosmetic renovation, landscaping and repairs — with no "
            "interest and no upfront payment, repaid at closing."
        ),
    },
    {
        "slug": "relocation",
        "name": "Relocation Services",
        "description": (
            "Support for buyers relocating to San Diego, including remote "
            "touring, neighborhood and commute comparison for the Sorrento "
            "Valley, UTC and downtown employment centers, and timeline "
            "coordination with an out-of-area sale."
        ),
    },
    {
        "slug": "investment-and-development",
        "name": "Investment & Development Representation",
        "description": (
            "Representation for investors and developers, including "
            "whole-building and new-development sales — Team Azizi currently "
            "represents seven units at a single La Jolla condominium project."
        ),
    },
    {
        "slug": "leasing",
        "name": "Leasing",
        "description": (
            "Landlord and tenant representation across San Diego County, with "
            "43 closed rentals on the team's Compass profile."
        ),
    },
]

# --------------------------------------------------------------------------
# Entity graph — sameAs.
#
# Only profiles that are accurate TODAY go in SAME_AS. A sameAs pointing at a
# profile carrying a stale brokerage name or the old phone number tells the
# knowledge graph that the wrong data is authoritative. Items in
# SAME_AS_PENDING move up once the Phase 2 cleanup sweep fixes them.
# --------------------------------------------------------------------------

SAME_AS = [
    "https://www.compass.com/agents/team-azizi/",
    "https://www.realtrends.com/team-profile/team-azizi-california-compass/",
    "https://www.facebook.com/TeamAziziRealEstate/",
    "https://www.instagram.com/teamazizi_realestate/",
    "https://www.zillow.com/profile/nilabazizi",
]

SAME_AS_PENDING = [
    (
        "https://www.linkedin.com/company/teamazizirealestate",
        'Company page is still named "Team Azizi Upstart Real Estate" — rename '
        "before linking, or it reinforces the stale brokerage.",
    ),
    (
        "https://www.yelp.com/biz/sonia-azizi-team-azizi-san-diego-3",
        "Listing carries the founder's name, the old Craftsman Way address and "
        "the old (619) phone. Needs the NAP fix and a family decision first.",
    ),
    (
        "https://www.youtube.com/channel/UC31bOFUD8jFGMSiAhO45J2g",
        "Sonia Azizi's channel. Real entity equity, but every decision about "
        "her profiles routes through the client and family (HANDOFF §2).",
    ),
]

# --------------------------------------------------------------------------
# Neighborhoods — the six claimed farm areas. Order here is the *content
# priority* order from HANDOFF §2 (winnability, not prestige); navigation
# order is set separately in the page data.
# --------------------------------------------------------------------------

NEIGHBORHOODS = [
    {
        "slug": "del-sur",
        "name": "Del Sur",
        "zip": "92127",
        "district": "Poway Unified School District",
        "wikipedia": None,  # no article found — do not invent a sameAs
        "priority": 1,
        "angle": "No market content exists anywhere. Fastest possible AI win.",
    },
    {
        "slug": "4s-ranch",
        "name": "4S Ranch",
        "zip": "92127",
        "district": "Poway Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/4S_Ranch,_California",
        "priority": 2,
        "angle": "Incumbent answers are City-Data forum threads from the 2000s.",
    },
    {
        "slug": "scripps-ranch",
        "name": "Scripps Ranch",
        "zip": "92131",
        "district": "San Diego Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Scripps_Ranch,_San_Diego",
        "priority": 3,
        "angle": "AI answer held by two paid press releases. Cheap to contest.",
    },
    {
        "slug": "carmel-valley",
        "name": "Carmel Valley",
        "zip": "92130",
        "district": "Del Mar Union / San Dieguito Union (boundary-dependent)",
        "wikipedia": "https://en.wikipedia.org/wiki/Carmel_Valley,_San_Diego",
        "priority": 4,
        "angle": "Home office. Primary tracking keyword. Crowded but winnable.",
    },
    {
        "slug": "del-mar",
        "name": "Del Mar",
        "zip": "92014",
        "district": "Del Mar Union / San Dieguito Union",
        "wikipedia": "https://en.wikipedia.org/wiki/Del_Mar,_California",
        "priority": 5,
        "angle": "#1 by sides — provable. Lead with RealTrends, not head terms.",
    },
    {
        "slug": "rancho-santa-fe",
        "name": "Rancho Santa Fe",
        "zip": "92067",
        "district": "Rancho Santa Fe School District (Roger Rowe, K-8)",
        "wikipedia": "https://en.wikipedia.org/wiki/Rancho_Santa_Fe,_California",
        "priority": 6,
        "angle": "Hardest SERP in the county. Covenant/ARB/septic explainers.",
    },
]

NAV_ORDER = [
    "carmel-valley",
    "del-mar",
    "rancho-santa-fe",
    "del-sur",
    "4s-ranch",
    "scripps-ranch",
]

# --------------------------------------------------------------------------
# Compliance — real estate is not generic marketing. HANDOFF.md §6.
# --------------------------------------------------------------------------

DISCLAIMER = (
    "Team Azizi is a team of real estate licensees affiliated with Compass, a "
    "licensed real estate broker. Compass California III, Inc. dba Compass, "
    f"CA DRE# {BROKERAGE_DRE}. All information is deemed reliable but is not "
    "guaranteed and should be independently verified. Equal Housing "
    "Opportunity."
)

TCPA_CONSENT = (
    "By submitting this form, I consent to be contacted by Team Azizi and "
    "Compass by phone, text message and email at the number and address "
    "provided, including by automated means and prerecorded or artificial "
    "voices, about real estate services. Consent is not a condition of any "
    "purchase. Message and data rates may apply. Reply STOP to opt out."
)


def address_one_line() -> str:
    return f"{STREET}, {CITY}, {REGION} {POSTAL}"
