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

# Call-tracking number (client-supplied 2026-08-03). Every Team Azizi number
# on the site — this one and all nineteen in agents.py — points here so the
# tracking provider sees every inbound call; a site that leaves untracked
# numbers lying around measures nothing.
#
# Two consequences the client owns, recorded so nobody has to rediscover them:
#   1. NAP consistency. This number is what the site, its schema and its
#      footer now assert. GBP, Compass, Zillow and the social profiles must
#      carry the SAME number, or the entity cleanup in HANDOFF §2 is fighting
#      itself — a knowledge graph reading two phone numbers for one business
#      trusts neither. Set it on the GBP profile at creation.
#   2. Routing. Nineteen licensees' direct lines now resolve to one line, so
#      the tracking provider has to route (or forward) per destination if
#      "call this agent" is still meant to reach that agent.
# The prior main line was (858) 847-8067 — Nilab's direct number.
PHONE_DISPLAY = "(858) 201-2899"
PHONE_SCHEMA = "+18582012899"
PHONE_HREF = "tel:+18582012899"
EMAIL = "teamazizi@compass.com"

# Approximate rooftop coordinates for the Carmel Valley Compass office.
# MUST be re-pinned to the GBP location once the profile exists — schema
# and GBP disagreeing is the exact failure mode this file exists to prevent.
GEO = {"lat": 32.9465, "lon": -117.2318, "verified": False}

LEAD_AGENT = "Nilab Azizi"
LEAD_DRE = "02047962"
BROKERAGE = "Compass California III, Inc."
BROKERAGE_DRE = "01527365"

# Google Street View Static API key, for the photograph of the property on
# /home-valuation. Empty means the page still works and simply shows no
# photograph — the flow degrades rather than breaking.
#
# This key is necessarily public: it goes into an <img> src the browser
# fetches. That is normal for the Static APIs and safe ONLY with an HTTP
# referrer restriction locking it to teamazizi.com in the Google Cloud
# console. An unrestricted key on a public page is somebody else's free
# quota and the client's bill.
GOOGLE_MAPS_KEY = ""

# Zillow's public search URL. We link people to their own Zestimate in a new
# tab rather than reproducing it: Zillow retired the public Zestimate API in
# 2021 and everything else on the market is a scraper, but a hyperlink is
# just a hyperlink. This also puts the number on Zillow's page where it
# belongs, rather than making Zillow the authority on our own site.
ZILLOW_SEARCH = "https://www.zillow.com/homes/{address}_rb/"

# Footer "Explore" column — ONLY pages that have actually been built.
#
# This list existed implicitly in components.py and named seven pages, none of
# which had been generated: /sell, /buy, /concierge, /testimonials, /blog,
# /contact and /terms-and-conditions. Every one of the 43 pages therefore
# shipped seven dead links in its footer. A link audit is now part of
# validate.py so this cannot come back silently — add the entry here at the
# same time as the page, not before.
FOOTER_EXPLORE = (
    ("Neighborhood Guides", "/neighborhoods"),
    ("Mello-Roos Lookup", "/mello-roos"),
    ("What's My Home Worth?", "/home-valuation"),
    ("Sell Your Home", "/sell"),
    ("Buy a Home", "/buy"),
    ("Compass Concierge", "/concierge"),
    ("Homes for Sale", "/properties/sale"),
    ("Recently Sold", "/properties/sold"),
    ("Meet the Team", "/team"),
    ("Journal", "/blog"),
    ("Contact", "/contact"),
)

# Neighborhood column in the footer, which appears on every page and is
# therefore the single largest source of internal links on the site.
#
# It used to render NAV_ORDER — the original six — so Escondido, the largest
# market in the team's book at ~96 closed sales, received no footer link at
# all, while Del Mar at six sales received one on all 48 pages. A link audit
# showed the North County guides sitting on two inbound links each against
# the originals' five or more. That is link equity pointed away from the
# evidence.
#
# Ordered by what the team can actually evidence, then by page strength. Not
# all sixteen: a footer column of sixteen is a list nobody reads, and the
# hub link at the end carries the rest.
FOOTER_HOODS = (
    "escondido",      # ~96 closed sales — the largest market in the book
    "del-sur",        # 18
    "4s-ranch",       # 18
    "carmel-valley",  # 11
    "scripps-ranch",  # 9
    "oceanside",      # named in salesRecord.md as a top market; count pending
    "fallbrook",      # same
    "san-marcos",     # 91 CFDs — the strongest single page on the site
)

# Licensees named in the footer of every page, in display order.
#
# California requires the responsible licensee's name and DRE number on
# advertising. Naming more than one is a choice rather than an obligation, and
# the reason to make it is that this is a family team: Nilab leads it, Sofia
# and Zohra are the other two Azizi licensees, and a visitor who arrived from
# an Instagram post by one of them should find that person's licence on the
# page rather than only the team lead's.
#
# Slugs, not names and numbers. The DRE numbers live in agents.py and are
# resolved from there, so there is exactly one place to correct one — and
# validate.py fails the build if a slug here is not on the roster.
FOOTER_LICENSEES = ("nilab-azizi", "sofia-azizi", "zohra-azizi")

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
    # ⚠️ DO NOT PUBLISH until RealTrends' methodology is confirmed. RealTrends
    # assigns each team a business city and ranks within it; Team Azizi's
    # assigned city is Del Mar. Their Compass record shows SIX Del Mar sales
    # ever, against 92 sides in 2025 alone. The rank is very likely an artifact
    # of where the team is registered, not Del Mar market share — but a reader
    # will infer market share. See research/salesRecord.md §2.
    "del_mar_rank_UNVERIFIED": "#1 in Del Mar by sides, #2 by volume",
    "sdbj_top10": "One of the top 10 real estate teams in the county "
                  "(San Diego Business Journal, October 2025)",
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

# Client decision 2026-07-25: Sonia's profiles will not be used. Her YouTube
# channel is therefore removed from consideration entirely rather than left
# pending — the decision is made, not deferred.
NOT_USING = [
    (
        "https://www.youtube.com/channel/UC31bOFUD8jFGMSiAhO45J2g",
        "Sonia Azizi's channel — client has decided not to use her profiles.",
    ),
    (
        "https://www.instagram.com/soniasellssd/",
        "9,412 followers, the largest audience in the entity graph, but the "
        "client has decided not to use it. Recorded so nobody 'discovers' it "
        "again and reopens a settled family decision.",
    ),
]

# The neighborhood tour videos are hosted on @lifeinsandiego — Nicholas
# Miele's personal channel, 12.4K subscribers. The client confirms the team
# paid for the video, so the site embeds it with credit. Deliberately NOT
# added to sameAs: paying for production is a licence to use, not a claim
# that the channel is a Team Azizi entity, and asserting otherwise would be
# exactly the sort of sloppy entity signal this build exists to avoid.
VIDEO_CHANNEL = "https://www.youtube.com/@lifeinsandiego"
VIDEO_CHANNEL_NAME = "Living in San Diego"
VIDEO_CHANNEL_OWNER = "Nicholas Miele"

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
]

# --------------------------------------------------------------------------
# Neighborhoods — the six claimed farm areas. Order here is the *content
# priority* order from HANDOFF §2 (winnability, not prestige); navigation
# order is set separately in the page data.
# --------------------------------------------------------------------------

NEIGHBORHOODS = [
    {
        "slug": "del-sur",
        "video": {"id": "6nrzXgXyngA", "title": 'INSANE Community in San Diego You HAVE to See | 4S Ranch & Del Sur in San Diego'},
        "name": "Del Sur",
        "zip": "92127",
        "district": "Poway Unified School District",
        "wikipedia": None,  # no article found — do not invent a sameAs
        "priority": 1,
        "angle": "No market content exists anywhere. Fastest possible AI win.",
    },
    {
        "slug": "4s-ranch",
        "video": {"id": "6nrzXgXyngA", "title": 'INSANE Community in San Diego You HAVE to See | 4S Ranch & Del Sur in San Diego'},
        "name": "4S Ranch",
        "zip": "92127",
        "district": "Poway Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/4S_Ranch,_California",
        "priority": 2,
        "angle": "Incumbent answers are City-Data forum threads from the 2000s.",
    },
    {
        "slug": "scripps-ranch",
        "video": None,  # no tour exists on the channel — commission one
        "name": "Scripps Ranch",
        "zip": "92131",
        "district": "San Diego Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Scripps_Ranch,_San_Diego",
        "priority": 3,
        "angle": "AI answer held by two paid press releases. Cheap to contest.",
    },
    {
        "slug": "carmel-valley",
        "video": {"id": "IGpVk4vTGjg", "title": 'EVERYTHING You NEED to Know About Living in Carmel Valley in San Diego'},
        "name": "Carmel Valley",
        "zip": "92130",
        "district": "Del Mar Union / San Dieguito Union (boundary-dependent)",
        "wikipedia": "https://en.wikipedia.org/wiki/Carmel_Valley,_San_Diego",
        "priority": 4,
        "angle": "Home office. Primary tracking keyword. Crowded but winnable.",
    },
    {
        "slug": "del-mar",
        "video": {"id": "G-12EJiUSsw", "title": 'Living in Solana Beach & Del Mar California [Everything You Need to Know]'},
        "name": "Del Mar",
        "zip": "92014",
        "district": "Del Mar Union / San Dieguito Union",
        "wikipedia": "https://en.wikipedia.org/wiki/Del_Mar,_California",
        "priority": 5,
        "angle": "#1 by sides — provable. Lead with RealTrends, not head terms.",
    },
    {
        "slug": "rancho-santa-fe",
        "video": {"id": "LXO2cS7l36Q", "title": 'Living in Rancho Santa Fe California [Everything You Need to Know]'},
        "name": "Rancho Santa Fe",
        "zip": "92067",
        "district": "Rancho Santa Fe School District (Roger Rowe, K-8)",
        "wikipedia": "https://en.wikipedia.org/wiki/Rancho_Santa_Fe,_California",
        "priority": 6,
        "angle": "Hardest SERP in the county. Covenant/ARB/septic explainers.",
    },
]


# --------------------------------------------------------------------------
# North County expansion, added 2026-07-25.
#
# Ordered by the team's ACTUAL transaction record (research/salesRecord.md),
# not by prestige. Escondido leads because ~96 of their 1,009 sales are there
# — more than all six original target communities combined.
#
# `sold` is None where the per-community count has not been verified from the
# full sales export. The page omits the track-record claim entirely rather
# than inventing a number, which is the same rule the original six follow.
# --------------------------------------------------------------------------

NORTH_COUNTY = [
    {
        "slug": "escondido",
        "name": "Escondido",
        "zip": "92025, 92026, 92027, 92029",
        "district": "Escondido Union School District (K-8) and Escondido Union High School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Escondido,_California",
        "video": None,
        "priority": 1,
        "angle": "~96 team sales — the single largest market in the book, and no competitor in the research owns it.",
    },
    {
        "slug": "oceanside",
        "name": "Oceanside",
        "zip": "92054, 92056, 92057, 92058",
        "district": "Oceanside Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Oceanside,_California",
        "video": None,
        "priority": 2,
        "angle": "Consistent volume across all four ZIPs; coastal North County at attainable prices.",
    },
    {
        "slug": "fallbrook",
        "name": "Fallbrook",
        "zip": "92028",
        "district": "Fallbrook Union Elementary and Fallbrook Union High School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Fallbrook,_California",
        "video": None,
        "priority": 3,
        "angle": "Real repeat volume. Rural-residential and acreage buyers ask different questions than tract buyers.",
    },
    {
        "slug": "san-marcos",
        "name": "San Marcos",
        "zip": "92069, 92078",
        "district": "San Marcos Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/San_Marcos,_California",
        "video": None,
        "priority": 4,
        "angle": "91 active CFDs — the most Mello-Roos-complex city in the county, and the single best place for the tax-data moat.",
    },
    {
        "slug": "carlsbad",
        "name": "Carlsbad",
        "zip": "92008, 92009, 92010, 92011",
        "district": "Carlsbad Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Carlsbad,_California",
        "video": None,
        "priority": 5,
        "angle": "Holds the team's top sale ever ($6.1M, Obelisco Circle). Coastal at a range they genuinely transact in.",
    },
    {
        "slug": "vista",
        "name": "Vista",
        "zip": "92081, 92083, 92084",
        "district": "Vista Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Vista,_California",
        "video": None,
        "priority": 6,
        "angle": "No CFD in the county's active list — a clean answer to the tax question, unlike its neighbours.",
    },
    {
        "slug": "poway",
        "name": "Poway",
        "zip": "92064",
        "district": "Poway Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Poway,_California",
        "video": None,
        "priority": 7,
        "angle": "Poway Unified without the 92127 Mello-Roos load — the comparison inland buyers actually run.",
    },
    {
        "slug": "encinitas",
        "name": "Encinitas",
        "zip": "92024",
        "district": "Encinitas Union School District (K-6) and San Dieguito Union High School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Encinitas,_California",
        "video": None,
        "priority": 8,
        "angle": "Multiple sales above $3M. The coastal market where their record is strongest after Del Mar.",
    },
    {
        "slug": "valley-center",
        "name": "Valley Center",
        "zip": "92082",
        "district": "Valley Center-Pauma Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Valley_Center,_California",
        "video": None,
        "priority": 9,
        "angle": "Acreage buyers. Well, septic and fire-zone questions no tract-focused competitor answers.",
    },
    {
        "slug": "ramona",
        "name": "Ramona",
        "zip": "92065",
        "district": "Ramona Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Ramona,_California",
        "video": None,
        "priority": 10,
        "angle": "Large-parcel rural. Same well/septic/fire questions as Valley Center, different market.",
    },
]

# Southwest Riverside County — the I-15 corridor over the county line, added
# at client request 2026-07-30. A different county: Riverside's own district
# records govern the tax facts (taxes.py carries per-entry sources), and the
# Compass sales sweep has no record here, so every page publishes structural
# facts and no volume claims. Fallbrook is the geographic hinge between this
# list and North County.
SW_RIVERSIDE = [
    {
        "slug": "temecula",
        "name": "Temecula",
        "zip": "92590, 92591, 92592",
        "district": "Temecula Valley Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Temecula,_California",
        "video": None,
        "priority": 1,
        "angle": "The corridor anchor. City CFDs plus school-district CFDs, and a Wine Country jurisdiction trap nobody explains.",
    },
    {
        "slug": "murrieta",
        "name": "Murrieta",
        "zip": "92562, 92563",
        "district": "Murrieta Valley Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Murrieta,_California",
        "video": None,
        "priority": 2,
        "angle": "The 15/215 hinge. La Cresta's county-estate edge and districts still forming in 2026.",
    },
    {
        "slug": "menifee",
        "name": "Menifee",
        "zip": "92584, 92585, 92586, 92587",
        "district": "Menifee Union School District (K-8) and Perris Union High School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Menifee,_California",
        "video": None,
        "priority": 3,
        "angle": "2008 incorporation, three school systems, heaviest new-construction CFD load on the corridor.",
    },
]

# City of San Diego neighborhoods south of the original farm, added
# 2026-07-30 at client request. These are San Diego communities (La Jolla
# included — its cityhood question is answered honestly on its page), so
# they take the "{name}, San Diego, CA" areaServed form and San Diego
# Unified as the district.
SD_CITY = [
    {
        "slug": "la-jolla",
        "name": "La Jolla",
        "zip": "92037",
        "district": "San Diego Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/La_Jolla",
        "video": None,
        "priority": 1,
        "angle": "The 6710 La Jolla Blvd development representation justifies the page (GAMEPLAN §9). Cityhood question is live news.",
    },
    {
        "slug": "pacific-beach",
        "name": "Pacific Beach",
        "zip": "92109",
        "district": "San Diego Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Pacific_Beach,_San_Diego",
        "video": None,
        "priority": 2,
        "angle": "STRO license math is the question every buyer asks and few pages answer with the actual tiers.",
    },
    {
        "slug": "ocean-beach",
        "name": "Ocean Beach",
        "zip": "92107",
        "district": "San Diego Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Ocean_Beach,_San_Diego",
        "video": None,
        "priority": 3,
        "angle": "Height limit + community plan explain the whole market; overflight is checkable block by block.",
    },
    {
        "slug": "hillcrest",
        "name": "Hillcrest",
        "zip": "92103",
        "district": "San Diego Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Hillcrest,_San_Diego",
        "video": None,
        "priority": 4,
        "angle": "The 2024 plan amendment (~17,000 homes) is a generational rezoning almost nobody explains to owners.",
    },
    {
        "slug": "north-park",
        "name": "North Park",
        "zip": "92104",
        "district": "San Diego Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/North_Park,_San_Diego",
        "video": None,
        "priority": 5,
        "angle": "Historic districts + Mills Act + ADU rules — three regulatory layers on Craftsman stock.",
    },
    {
        "slug": "downtown-san-diego",
        "name": "Downtown San Diego",
        "zip": "92101",
        "district": "San Diego Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Downtown_San_Diego",
        "video": None,
        "priority": 6,
        "angle": "Condo-regime market: HOA docs, FAA height caps, district-by-district differences.",
    },
    {
        "slug": "college-area",
        "name": "College Area",
        "zip": "92115",
        "district": "San Diego Unified School District",
        "wikipedia": "https://en.wikipedia.org/wiki/College_Area,_San_Diego",
        "video": None,
        "priority": 7,
        "angle": "SDSU drives the economics; owner-occupants and investors underwrite the same house differently.",
    },
]

# East County and South Bay, added 2026-07-30 at client request — and this
# is where salesRecord.md says the book actually lives: Spring Valley, South
# Bay (incl. Chula Vista), Santee and El Cajon are named top markets. Counts
# stay unpublished until the full export lands (SOLD_RECORD = None).
EAST_SOUTH = [
    {
        "slug": "chula-vista",
        "name": "Chula Vista",
        "zip": "91910, 91911, 91913, 91914, 91915",
        "district": "Chula Vista Elementary School District (K-6) and Sweetwater Union High School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Chula_Vista,_California",
        "video": None,
        "priority": 1,
        "angle": "Named top market. The I-805 east/west split and the three-layer CFD bill are the whole story.",
    },
    {
        "slug": "santee",
        "name": "Santee",
        "zip": "92071",
        "district": "Santee School District (K-8) and Grossmont Union High School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Santee,_California",
        "video": None,
        "priority": 2,
        "angle": "Named top market. One CFD in the list; river floodplain and Fanita Ranch are the land-use facts.",
    },
    {
        "slug": "el-cajon",
        "name": "El Cajon",
        "zip": "92019, 92020, 92021",
        "district": "Cajon Valley Union School District (K-8) and Grossmont Union High School District",
        "wikipedia": "https://en.wikipedia.org/wiki/El_Cajon,_California",
        "video": None,
        "priority": 3,
        "angle": "Named top market. No Mello-Roos in the list — the monthly-cost story against newer communities.",
    },
    {
        "slug": "spring-valley",
        "name": "Spring Valley",
        "zip": "91977, 91978",
        "district": "La Mesa-Spring Valley Schools (K-8) and Grossmont Union High School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Spring_Valley,_San_Diego_County,_California",
        "video": None,
        "priority": 4,
        "angle": "Named top market, and unincorporated — the county-jurisdiction facts the rural pages pioneered, in a suburban setting.",
    },
    {
        "slug": "lemon-grove",
        "name": "Lemon Grove",
        "zip": "91945",
        "district": "Lemon Grove School District (K-8) and Grossmont Union High School District",
        "wikipedia": "https://en.wikipedia.org/wiki/Lemon_Grove,_California",
        "video": None,
        "priority": 5,
        "angle": "One of the county's smallest cities; its single CFD is commercial-corridor only — worth saying plainly.",
    },
]

# Everything the site covers. The original six stay first in navigation
# because the client claims them; North County follows in record order;
# the city neighborhoods, East County/South Bay and the Riverside corridor
# close the list.
ALL_AREAS = NEIGHBORHOODS + NORTH_COUNTY + SD_CITY + EAST_SOUTH + SW_RIVERSIDE

NORTH_COUNTY_ORDER = [a["slug"] for a in sorted(NORTH_COUNTY, key=lambda x: x["priority"])]
SD_CITY_ORDER = [a["slug"] for a in sorted(SD_CITY, key=lambda x: x["priority"])]
EAST_SOUTH_ORDER = [a["slug"] for a in sorted(EAST_SOUTH, key=lambda x: x["priority"])]
SW_RIVERSIDE_ORDER = [a["slug"] for a in sorted(SW_RIVERSIDE, key=lambda x: x["priority"])]

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


# --------------------------------------------------------------------------
# Lead delivery
#
# Every form on this site posts here and the submission is emailed. The
# valuation form in particular exists to capture one thing — a property
# address — so a submission that does not reach a human is a lost listing,
# not a lost newsletter signup.
#
# Formspree is the launch choice: no server, no build step, works with a
# static host. Two things to watch:
#   - The free tier caps around 50 submissions/month. This form is the
#     Instagram link-in-bio destination for 2,055 followers; budget for the
#     paid tier rather than silently dropping leads.
#   - It is a third-party dependency, which this project is otherwise built
#     to avoid. Swapping it for the client's CRM webhook is a one-line change
#     here precisely so that stays cheap.
#
# LEAD_ENDPOINT must be replaced with the real form ID before launch —
# validate.py fails the build while it still says PLACEHOLDER.
# --------------------------------------------------------------------------

LEAD_ENDPOINT = "https://formspree.io/f/PLACEHOLDER"
LEAD_NOTIFY = EMAIL  # where submissions land


def address_one_line() -> str:
    return f"{STREET}, {CITY}, {REGION} {POSTAL}"
