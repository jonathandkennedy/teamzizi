"""Per-community answer blocks: the depth layer under every guide page.

Why this file exists
--------------------
`build/generate.py` gives every neighborhood the same three blocks — tax
district, school district, track record. That is enough to be *correct* and
nowhere near enough to be *cited*. A page that says only what a county PDF
says is a page an AI has no reason to prefer over the county PDF.

`build/data/fanout.py` already lists the sub-queries each community has to
answer. This file supplies the passages that answer them. One entry per
sub-query, each written to survive being lifted out of the page: names the
place, opens without a pronoun, and answers the question completely before
it stops.

The evidence rule
-----------------
Everything here is a **structural** fact — which district, which boundary,
which jurisdiction, which agency to call. Structural facts are verifiable,
they are stable for years, and they are precisely what no competitor
publishes because looking them up is work.

Deliberately absent: prices, medians, days-on-market, appreciation, school
ratings. Those move, and a stale number is worse than no number. Where a
figure would genuinely help, the passage says which agency holds it rather
than guessing at it.

Fair Housing
------------
Every passage describes *places and processes*, never people. No
"family-friendly", no "safe", no "desirable", no characterisation of who
lives anywhere. Buyers get told which district assigns the school and how to
confirm it; they do not get told what to conclude about the neighbours.
"""

from __future__ import annotations

# Repeated verbatim wherever a school-boundary claim appears. School
# attendance is the single most consequential thing buyers get wrong, and the
# district office is the only authority on it.
CONFIRM_SCHOOL = (
    "District boundaries are assigned by address and are redrawn from time to "
    "time, so confirm any specific address with the district office before "
    "relying on it."
)

# Unincorporated communities are governed by the County, not by a city. This
# changes who issues permits and who hears a land-use appeal.
COUNTY_LAND_USE = (
    "Land-use questions there go to the County of San Diego Planning &amp; "
    "Development Services rather than to a city planning counter, and there "
    "is no city council to appeal to &mdash; the Board of Supervisors sits at "
    "the top of that process instead."
)


GUIDES: dict[str, list[dict]] = {
    # ---------------------------------------------------------------- #1
    # Escondido — the largest market in the team's book by a wide margin.
    # ---------------------------------------------------------------- #
    "escondido": [
        {
            "anchor": "sub-areas",
            "question": "What are the different parts of Escondido?",
            "lead": (
                "Escondido covers four ZIP codes that behave as separate "
                "markets: 92025 around downtown and Old Escondido, 92026 "
                "north toward Hidden Meadows, 92027 east toward Valley Center "
                "and the San Pasqual Valley, and 92029 west toward Harmony "
                "Grove and Elfin Forest. The housing stock in each was built "
                "in different decades, which is why a single citywide figure "
                "describes none of them well."
            ),
            "body": (
                "<p>Two of those distinctions carry real consequences. The "
                "Old Escondido Historic District, immediately south of "
                "downtown, applies design review to exterior changes &mdash; "
                "the city's Planning Division confirms whether a given parcel "
                "falls inside it. And several communities with Escondido "
                "mailing addresses, including Hidden Meadows and parts of "
                "Harmony Grove, are outside the city limits in unincorporated "
                "county, so the permitting authority and the school "
                "assignment can both differ from the city proper.</p>"
            ),
        },
        {
            "anchor": "schools-structure",
            "question": "Why does Escondido have two school districts?",
            "lead": (
                "Escondido is served by two separate districts rather than "
                "one unified district: Escondido Union School District runs "
                "kindergarten through eighth grade, and Escondido Union High "
                "School District runs ninth through twelfth. Elementary "
                "assignment and high school assignment are therefore two "
                "different questions with two different answers, and a home "
                "can sit in a well-regarded elementary boundary while feeding "
                "a high school on the other side of the city."
            ),
            "body": (
                "<p>Outlying addresses complicate it further. Homes with "
                "Escondido mailing addresses on the eastern and northern "
                "edges can fall into San Pasqual Union, Valley Center-Pauma "
                "Unified or Bonsall Unified instead. "
                f"{CONFIRM_SCHOOL}</p>"
            ),
        },
        {
            "anchor": "getting-around",
            "question": "What is the commute like from Escondido?",
            "lead": (
                "Escondido sits at the junction of Interstate 15 and State "
                "Route 78, which is the practical reason the city works as a "
                "base for people who commute in more than one direction "
                "&mdash; south toward Kearny Mesa and downtown San Diego on "
                "the 15, or west toward the coast and the 5 on the 78."
            ),
            "body": (
                "<p>Escondido Transit Center is also the eastern terminus of "
                "the SPRINTER, the light rail line that runs across North "
                "County to Oceanside, where it connects to the COASTER and "
                "Amtrak. That connection is rarely mentioned in Escondido "
                "listings and it is the difference between a car-dependent "
                "address and one with a rail option.</p>"
            ),
        },
        {
            "anchor": "vs-san-marcos",
            "question": "Escondido or San Marcos — what actually differs?",
            "lead": (
                "The largest structural difference between Escondido and San "
                "Marcos is Mello-Roos. San Marcos carries 91 active community "
                "facilities districts in the County Auditor's FY&nbsp;2025-26 "
                "list, the most of any city in San Diego County; Escondido "
                "carries one, a school district CFD formed in 2019 that "
                "applies only to newer development. Comparable homes in the "
                "two cities can carry very different total monthly costs for "
                "that reason alone."
            ),
            "body": (
                "<p>The second difference is school structure. San Marcos "
                "Unified is a single unified district covering K-12; "
                "Escondido splits it across two districts. The third is age "
                "of stock &mdash; much of San Marcos's growth is recent "
                "master-planned construction, while Escondido's core is "
                "substantially older, which changes what inspections tend to "
                "find.</p>"
            ),
        },
    ],

    # ---------------------------------------------------------------- #2
    # Oceanside — the coastal entry point, and the VA-loan market.
    # ---------------------------------------------------------------- #
    "oceanside": [
        {
            "anchor": "sub-areas",
            "question": "What are the different parts of Oceanside?",
            "lead": (
                "Oceanside runs from the sand to well inland across four ZIP "
                "codes, and the neighborhoods behave very differently: South "
                "Oceanside and Fire Mountain south of the pier, the downtown "
                "and harbor area at the centre, Rancho del Oro and Ocean "
                "Hills inland to the east, and the Guajome and Mission Avenue "
                "corridor between them. Distance from the coast is the single "
                "largest variable in the city."
            ),
            "body": (
                "<p>The practical consequence sits at Interstate 5. Much of "
                "Oceanside west of the freeway falls inside the California "
                "Coastal Zone, where exterior work can require a coastal "
                "development permit in addition to a building permit. That "
                "adds time and cost to a remodel, and it is worth "
                "establishing before an offer rather than after.</p>"
            ),
        },
        {
            "anchor": "va-loans",
            "question": "Is Oceanside a good place to buy with a VA loan?",
            "lead": (
                "Oceanside borders Marine Corps Base Camp Pendleton, and VA "
                "financing is consequently a routine part of the market there "
                "rather than an exception &mdash; which matters to sellers as "
                "much as to buyers, because listing agents in Oceanside "
                "encounter VA appraisals and their repair requirements often "
                "enough to price and prepare for them."
            ),
            "body": (
                "<p>Two things follow. A seller who reflexively discounts VA "
                "offers is discarding a large share of the Oceanside buyer "
                "pool for no good reason. And a VA buyer competing here is "
                "not the unusual case they might be in an inland market, so "
                "the offer needs to be structured to compete on its actual "
                "merits rather than apologise for the loan type.</p>"
            ),
        },
        {
            "anchor": "getting-around",
            "question": "What public transport does Oceanside have?",
            "lead": (
                "Oceanside Transit Center is the only station in San Diego "
                "County where four rail services meet: the COASTER south to "
                "downtown San Diego, Amtrak's Pacific Surfliner, Metrolink "
                "north into Orange County and Los Angeles, and the SPRINTER "
                "east across North County to Escondido. No other North County "
                "city has that."
            ),
            "body": (
                "<p>For a buyer who commutes to Orange County or to downtown "
                "San Diego, that station is a genuine substitute for the "
                "freeway rather than a novelty, and proximity to it is a "
                "durable feature of an address in a way that few amenities "
                "are.</p>"
            ),
        },
        {
            "anchor": "vs-carlsbad",
            "question": "Oceanside or Carlsbad — how do they compare?",
            "lead": (
                "Oceanside and Carlsbad share a border and a coastline, and "
                "differ on two structural points. Carlsbad carries three "
                "active community facilities districts in the County "
                "Auditor's FY&nbsp;2025-26 list; no district in that list is "
                "named for Oceanside. And Carlsbad's school assignment "
                "crosses into three separate districts depending on the "
                "address, while Oceanside is served principally by a single "
                "unified district."
            ),
            "body": (
                "<p>Both cities have Coastal Zone frontage, both have a "
                "COASTER station, and both have walkable village cores. The "
                "decision between them is usually made on price per foot and "
                "on which school boundary a specific street falls into "
                "&mdash; not on any citywide characterisation.</p>"
            ),
        },
    ],

    # ---------------------------------------------------------------- #3
    # Fallbrook — unincorporated, agricultural, and a different rule set.
    # ---------------------------------------------------------------- #
    "fallbrook": [
        {
            "anchor": "unincorporated",
            "question": "Is Fallbrook a city?",
            "lead": (
                "Fallbrook is not an incorporated city. It is an "
                "unincorporated community governed directly by the County of "
                "San Diego, which means there is no Fallbrook city council, "
                "no city building department and no city zoning code. "
                f"{COUNTY_LAND_USE}"
            ),
            "body": (
                "<p>The Fallbrook Community Planning Group, a county-"
                "recognised advisory body, reviews projects and makes "
                "recommendations, but the decisions are the County's. For a "
                "buyer planning an addition, a second unit or a lot split, "
                "that changes both the timeline and the counter to approach "
                "&mdash; and it is the first thing to establish, not the "
                "last.</p>"
            ),
        },
        {
            "anchor": "well-septic",
            "question": "Do Fallbrook homes have well water and septic?",
            "lead": (
                "Many Fallbrook properties, particularly the larger parcels, "
                "are on private wells and septic systems rather than on "
                "municipal water and sewer &mdash; while homes closer to the "
                "village core are more often served by Fallbrook Public "
                "Utility District. Which applies is a parcel-level question, "
                "and the answer changes the inspection list, the financing "
                "and the running cost."
            ),
            "body": (
                "<p>A well means testing yield and water quality, not just "
                "confirming a well exists. A septic system means a functional "
                "inspection and locating the leach field, because replacing "
                "one is a five-figure item. Neither shows up in an automated "
                "valuation, and neither is optional to check.</p>"
            ),
        },
        {
            "anchor": "fire-insurance",
            "question": "Can you get fire insurance in Fallbrook?",
            "lead": (
                "Fire insurance availability is the question to settle first "
                "on a Fallbrook property, before the inspection and ideally "
                "before the offer. Much of the community sits in a state-"
                "designated high or very high fire hazard severity zone, and "
                "carriers have narrowed what they will write in those zones "
                "&mdash; which can leave the California FAIR Plan plus a "
                "difference-in-conditions policy as the route to coverage."
            ),
            "body": (
                "<p>The cost gap between a standard policy and that "
                "combination is large enough to change what a buyer can "
                "afford, and a lender will not fund without bound coverage. "
                "Getting a quote on the specific address during the "
                "contingency period, rather than assuming a rate, is the "
                "difference between a smooth close and a collapse at the end "
                "of escrow.</p>"
            ),
        },
        {
            "anchor": "agriculture",
            "question": "What should I know about Fallbrook's avocado groves?",
            "lead": (
                "Fallbrook has a long agricultural history built on avocado "
                "and citrus, and a working grove attached to a home is a "
                "business with costs rather than a garden. Irrigation water "
                "is the dominant one, and agricultural water rates, grove "
                "maintenance and harvest logistics all need pricing before a "
                "buyer treats acreage as a straightforward amenity."
            ),
            "body": (
                "<p>There is also an assessment question worth raising early. "
                "Land under a Williamson Act contract carries a reduced "
                "property tax assessment in exchange for a commitment to keep "
                "it in agricultural use, and those contracts run with the "
                "land and take years to unwind. Whether a parcel is under one "
                "is a matter of public record and should be established "
                "before the plans for it are.</p>"
            ),
        },
    ],

    # ---------------------------------------------------------------- #4
    # San Marcos — 91 CFDs. The single strongest Mello-Roos page available.
    # ---------------------------------------------------------------- #
    "san-marcos": [
        {
            "anchor": "why-so-many-cfds",
            "question": "Why does San Marcos have so much Mello-Roos?",
            "lead": (
                "San Marcos carries 91 active community facilities districts "
                "in the County Auditor's FY&nbsp;2025-26 list &mdash; more "
                "than any other city in San Diego County &mdash; because the "
                "city grew fast and late, and the infrastructure for that "
                "growth was financed through districts levied on the new "
                "homes rather than through general city funds. Most of those "
                "91 entries are separately numbered improvement areas within "
                "a small number of parent districts."
            ),
            "body": (
                "<p>The practical effect is that no single 'San Marcos "
                "Mello-Roos figure' exists, and any source quoting one has "
                "not looked at the list. Two houses on the same street, built "
                "in different phases, can sit in different improvement areas "
                "with different levies and different remaining terms. The "
                "authoritative answer is the line item on the tax bill for "
                "the specific parcel, which names the district and gives a "
                "contact number.</p>"
            ),
        },
        {
            "anchor": "sub-areas",
            "question": "What are the different parts of San Marcos?",
            "lead": (
                "San Marcos splits between older and newer development in a "
                "way that maps closely onto the tax question. San Elijo Hills "
                "is a hilltop master-planned community with its own town "
                "centre, built largely in the 2000s and the heart of the "
                "city's CFD footprint. Older San Marcos around Mission Road "
                "and Richmar predates that growth. Discovery Hills, Rancho "
                "Santalina and the Twin Oaks Valley corridor sit between "
                "them, and unincorporated Lake San Marcos, adjacent to the "
                "city, is not in the city at all."
            ),
        },
        {
            "anchor": "schools-structure",
            "question": "What school district serves San Marcos homes?",
            "lead": (
                "San Marcos is served principally by San Marcos Unified "
                "School District, a single K-12 unified district &mdash; "
                "which makes assignment simpler than in cities split across "
                "an elementary and a high school district. San Marcos Unified "
                "also extends beyond the city limits, so some homes with "
                "Carlsbad and Escondido addresses are assigned to it. "
                f"{CONFIRM_SCHOOL}"
            ),
        },
        {
            "anchor": "university",
            "question": "How does Cal State San Marcos affect the housing market?",
            "lead": (
                "California State University San Marcos sits inside the city "
                "and is one of its largest institutions, which shapes the "
                "rental market near campus and puts a SPRINTER station at its "
                "edge. For an owner-occupier the relevance is mostly traffic "
                "and rail access; for an investor it is a rental demand "
                "pattern that follows the academic year rather than the "
                "general market."
            ),
        },
    ],

    # ---------------------------------------------------------------- #5
    # Carlsbad — four ZIPs, three school districts, and a boundary that
    # genuinely surprises people.
    # ---------------------------------------------------------------- #
    "carlsbad": [
        {
            "anchor": "sub-areas",
            "question": "What is the difference between Carlsbad's four ZIP codes?",
            "lead": (
                "Carlsbad's four ZIP codes are four distinct markets. 92008 "
                "covers the Village, the Barrio and Olde Carlsbad near the "
                "coast; 92009 covers La Costa, Bressi Ranch and Rancho "
                "Carrillo inland to the south; 92010 covers Calavera Hills "
                "and the eastern side; and 92011 covers Aviara and the "
                "Poinsettia corridor near Batiquitos Lagoon. Age of stock, "
                "lot size and distance to the sand all differ sharply between "
                "them."
            ),
            "body": (
                "<p>Three coastal lagoons &mdash; Buena Vista, Agua Hedionda "
                "and Batiquitos &mdash; cut across the city and are the "
                "reason its neighborhoods are as separated as they are. They "
                "also constrain the road network, which is why a drive "
                "between two Carlsbad addresses can take longer than the map "
                "distance suggests.</p>"
            ),
        },
        {
            "anchor": "schools-structure",
            "question": "Do all Carlsbad homes go to Carlsbad schools?",
            "lead": (
                "Not every Carlsbad home is assigned to Carlsbad schools, and "
                "this is the question Carlsbad buyers get wrong most often. "
                "Carlsbad Unified School District serves "
                "much of the city, but homes in southern Carlsbad can be "
                "assigned to Encinitas Union School District for elementary "
                "and San Dieguito Union High School District for secondary, "
                "and homes on the eastern edge can fall into San Marcos "
                "Unified. A Carlsbad address does not by itself determine the "
                "school."
            ),
            "body": (
                "<p>That single fact moves real money, because buyers pay for "
                "school assignment and the boundary does not follow the city "
                "line or the ZIP code. "
                f"{CONFIRM_SCHOOL} Ask before the offer, not during the "
                "inspection period.</p>"
            ),
        },
        {
            "anchor": "coastal-zone",
            "question": "How does the Coastal Zone affect Carlsbad remodels?",
            "lead": (
                "Carlsbad property west of Interstate 5 and around the "
                "lagoons largely falls inside the California Coastal Zone, "
                "where exterior alterations, additions and rebuilds can "
                "require a coastal development permit alongside the ordinary "
                "building permit. Carlsbad administers most of that process "
                "under its own certified Local Coastal Program, with some "
                "categories still going to the Coastal Commission."
            ),
            "body": (
                "<p>For a buyer intending to alter a house, that is a "
                "timeline and a budget item that an inland comparable does "
                "not carry, and it is worth confirming with the city's "
                "planning counter for the specific parcel before assuming a "
                "project is straightforward.</p>"
            ),
        },
        {
            "anchor": "village",
            "question": "What is Carlsbad Village like to live in?",
            "lead": (
                "Carlsbad Village is the walkable core of the city: a "
                "compact grid of streets between the ocean and the railway, "
                "with a COASTER station at its centre providing rail service "
                "south to downtown San Diego and connections north. Housing "
                "there is generally older and on smaller lots than the "
                "master-planned areas inland, which is the trade being made."
            ),
        },
    ],

    # ---------------------------------------------------------------- #6
    # Vista — the Chula Vista trap turned into a genuinely unique passage.
    # ---------------------------------------------------------------- #
    "vista": [
        {
            "anchor": "mello-roos-confusion",
            "question": "I found Vista Mello-Roos figures online — are they real?",
            "lead": (
                "Mello-Roos figures published for &ldquo;Vista&rdquo; are "
                "very often Chula Vista figures. No community "
                "facilities district in the County Auditor's active "
                "FY&nbsp;2025-26 list is named for the city of Vista in North "
                "County, but Chula Vista in South Bay has several &mdash; and "
                "a search for &ldquo;Vista Mello-Roos&rdquo; returns those, "
                "forty miles from where you are looking."
            ),
            "body": (
                "<p>Two different cities, two different ends of the county, "
                "one substring. Anyone budgeting a Vista purchase off a "
                "figure found that way is budgeting for the wrong city. The "
                "tax bill for the specific parcel settles it.</p>"
            ),
        },
        {
            "anchor": "sub-areas",
            "question": "What are the different parts of Vista?",
            "lead": (
                "Vista covers three ZIP codes and sits roughly seven miles "
                "inland, close enough to the coast to catch some marine "
                "influence and far enough to run warmer than Oceanside or "
                "Carlsbad on a summer afternoon. Shadowridge in the south is "
                "a master-planned area built around a golf course; the "
                "Vista Village core to the north is older and more compact; "
                "and the eastern side toward Bonsall runs to larger, more "
                "rural parcels."
            ),
        },
        {
            "anchor": "getting-around",
            "question": "How do you get around from Vista?",
            "lead": (
                "Vista has two SPRINTER stations &mdash; Vista Transit Center "
                "and Civic Center &mdash; on the light rail line that runs "
                "between Oceanside and Escondido, connecting at Oceanside to "
                "the COASTER, Amtrak and Metrolink. State Route 78 crosses "
                "the city and links Interstate 5 at Oceanside to Interstate "
                "15 at Escondido."
            ),
            "body": (
                "<p>That combination is the practical argument for Vista: "
                "inland pricing with a rail connection to the coastal line, "
                "which most inland North County cities do not have.</p>"
            ),
        },
        {
            "anchor": "vs-oceanside",
            "question": "Vista or Oceanside — which should I look at?",
            "lead": (
                "Vista and Oceanside share the State Route 78 corridor and "
                "the SPRINTER line, and neither has a community facilities "
                "district named for it in the County Auditor's active list. "
                "The difference is the coast: Oceanside has beachfront, a "
                "Coastal Zone permitting overlay on its western half, and "
                "prices that reflect both. Vista has neither the frontage nor "
                "the overlay."
            ),
            "body": (
                "<p>For a buyer who wants square footage and a shorter "
                "permitting path, that trade generally favours Vista. For a "
                "buyer who wants to walk to the sand, it does not. Both are "
                "in separate unified school districts, so the assignment "
                "question has to be asked separately in each.</p>"
            ),
        },
    ],

    # ---------------------------------------------------------------- #7
    # Poway — the best structural insight on the whole site.
    # ---------------------------------------------------------------- #
    "poway": [
        {
            "anchor": "pusd-without-cfd",
            "question": "Can I get Poway Unified schools without paying Mello-Roos?",
            "lead": (
                "The city of Poway is where buyers who want Poway Unified "
                "schools without a large Mello-Roos bill should look first. "
                "Poway Unified School District administers 19 "
                "active community facilities districts, but the bulk of that "
                "CFD load sits in the newer 92127 communities the district "
                "also serves &mdash; Del Sur, 4S Ranch and the Black Mountain "
                "Ranch villages &mdash; rather than in the older city of "
                "Poway itself, which was largely built before those districts "
                "were formed."
            ),
            "body": (
                "<p>That is the comparison inland buyers are usually trying "
                "to make and almost nobody spells out: the same district, "
                "materially different total monthly cost, older housing stock "
                "and larger lots in exchange. It is a parcel-level question "
                "rather than a guarantee &mdash; the tax bill for a specific "
                "address is what confirms it &mdash; but it is a real and "
                "checkable structural difference, not a sales line.</p>"
            ),
        },
        {
            "anchor": "sub-areas",
            "question": "What are the different parts of Poway?",
            "lead": (
                "Poway calls itself the City in the Country, and the phrase "
                "describes an actual zoning pattern rather than a slogan: the "
                "city deliberately retained large-lot rural residential "
                "zoning across much of its area, with horse properties and "
                "an extensive trail network alongside conventional "
                "subdivisions. Old Poway around Midland Road is the historic "
                "core; the Green Valley and Garden Road areas are "
                "conventional suburban; and the northern and eastern edges "
                "toward Lake Poway run to acreage."
            ),
            "body": (
                "<p>For a buyer, the zoning is the point. Rural residential "
                "parcels carry minimum lot sizes and animal-keeping rights "
                "that a standard subdivision does not, and those rights are "
                "attached to the zoning designation rather than to the "
                "listing description. The city's Development Services "
                "Department confirms the designation for a given "
                "address.</p>"
            ),
        },
        {
            "anchor": "getting-around",
            "question": "What is the commute like from Poway?",
            "lead": (
                "Poway has no freeway inside the city and no rail station. "
                "Access runs through Poway Road west to Interstate 15, "
                "through Scripps Poway Parkway to the 15 further south, or "
                "east to State Route 67. That absence of a freeway through "
                "the middle is part of why the city stayed as low-density as "
                "it did, and it is also the main practical cost of living "
                "there."
            ),
        },
        {
            "anchor": "outdoors",
            "question": "What outdoor access does Poway have?",
            "lead": (
                "Poway has an unusual amount of protected open space for a "
                "city of its size: Lake Poway and its surrounding "
                "recreation area, the Blue Sky Ecological Reserve adjoining "
                "it, Iron Mountain on the eastern edge, and a trail system "
                "the city maintains across the rural residential areas. Much "
                "of that land is permanently protected, which means the "
                "views and the trail access attached to an address are "
                "durable rather than pending someone else's entitlement."
            ),
        },
    ],

    # ---------------------------------------------------------------- #8
    # Encinitas — five communities and a school structure nobody explains.
    # ---------------------------------------------------------------- #
    "encinitas": [
        {
            "anchor": "sub-areas",
            "question": "What are the five communities of Encinitas?",
            "lead": (
                "Encinitas was incorporated in 1986 from five distinct "
                "communities that the city still recognises by name: "
                "Leucadia in the north, Old Encinitas around the downtown "
                "and the coast, New Encinitas inland around Encinitas "
                "Ranch, Cardiff-by-the-Sea in the south, and Olivenhain "
                "inland to the east. They differ in housing stock, lot size "
                "and street pattern more than a single city name suggests."
            ),
            "body": (
                "<p>Olivenhain is the outlier and the one buyers most often "
                "misjudge: semi-rural, large-lot, with horse-keeping and a "
                "trail network, sitting inside the same city as the coastal "
                "village streets of Leucadia. A citywide average describes "
                "neither.</p>"
            ),
        },
        {
            "anchor": "schools-structure",
            "question": "Which school district serves Encinitas?",
            "lead": (
                "Encinitas is served by more than one elementary district, "
                "which surprises buyers who assume the city name settles it. "
                "Encinitas Union School District covers kindergarten through "
                "sixth grade across most of the city, but Cardiff-by-the-Sea "
                "has its own separate K-6 district, the Cardiff School "
                "District. Both then feed into San Dieguito Union High School "
                "District for grades seven through twelve."
            ),
            "body": (
                "<p>So an Encinitas address involves two assignments to "
                "verify, and which elementary district applies depends on "
                "which of the five communities the parcel sits in. "
                f"{CONFIRM_SCHOOL}</p>"
            ),
        },
        {
            "anchor": "coastal-bluff",
            "question": "What should I know about buying on the Encinitas bluff?",
            "lead": (
                "Bluff-top property in Encinitas carries a regulatory and "
                "engineering question that no other local factor matches. "
                "Coastal bluff erosion is actively managed along this stretch "
                "of coast, and permits for seawalls, bluff retention devices "
                "and even some repairs run through the city's certified "
                "Local Coastal Program and, in some categories, the "
                "California Coastal Commission."
            ),
            "body": (
                "<p>A geotechnical report on the specific parcel, and a clear "
                "picture of what has already been permitted and what has "
                "not, belong in the contingency period rather than after it. "
                "This is one of the few situations in residential real estate "
                "where the ground itself is the primary due diligence "
                "item.</p>"
            ),
        },
        {
            "anchor": "getting-around",
            "question": "How do you commute from Encinitas?",
            "lead": (
                "Encinitas Station sits in the downtown village on the "
                "COASTER line, giving rail access south to Solana Beach, Old "
                "Town and downtown San Diego and north to Oceanside. "
                "Interstate 5 runs the length of the city, and Coast Highway "
                "101 parallels it through Leucadia, Old Encinitas and "
                "Cardiff as the slower local alternative."
            ),
        },
    ],

    # ---------------------------------------------------------------- #9
    # Valley Center — the fire district CFD is the story.
    # ---------------------------------------------------------------- #
    "valley-center": [
        {
            "anchor": "unincorporated",
            "question": "Is Valley Center a city?",
            "lead": (
                "Valley Center is an unincorporated community rather than an "
                "incorporated city, governed directly by the County of San "
                "Diego. "
                f"{COUNTY_LAND_USE}"
            ),
            "body": (
                "<p>The Valley Center Community Planning Group advises the "
                "County on projects in the area, and the Valley Center "
                "Community Plan sets the land-use framework the County "
                "applies. For anyone buying acreage with a plan for it, that "
                "plan and the parcel's zoning designation are the documents "
                "that decide what is possible.</p>"
            ),
        },
        {
            "anchor": "fire-cfd",
            "question": "Why does Valley Center have a fire protection Mello-Roos?",
            "lead": (
                "Valley Center's one active community facilities district is "
                "a fire protection district rather than a school or "
                "development one &mdash; the Valley Center Fire Protection "
                "District CFD 2000-1 &mdash; and that is a genuinely useful "
                "signal for a buyer weighing a rural parcel. It means fire "
                "service in the community is funded through a dedicated "
                "assessment rather than competing for general funds."
            ),
            "body": (
                "<p>Rural buyers are usually told to worry about Mello-Roos "
                "and separately to worry about fire response times. In Valley "
                "Center those are the same line item, and the assessment is "
                "buying the thing the insurance question turns on. Whether it "
                "applies to a specific parcel, and at what amount, is on the "
                "tax bill.</p>"
            ),
        },
        {
            "anchor": "water",
            "question": "Where does Valley Center get its water?",
            "lead": (
                "Valley Center properties are served either by the Valley "
                "Center Municipal Water District or by private wells, and "
                "which one applies changes both the monthly cost and the "
                "inspection list. The district also offers agricultural water "
                "rates for qualifying growers, which matters on the citrus "
                "and avocado parcels that make up much of the area."
            ),
            "body": (
                "<p>On a well, the diligence is yield testing and water "
                "quality analysis rather than a meter reading, and a low-"
                "producing well on a large parcel is a materially different "
                "asset from a high-producing one. Neither distinction appears "
                "in an automated valuation.</p>"
            ),
        },
        {
            "anchor": "fire-insurance",
            "question": "Is fire insurance available in Valley Center?",
            "lead": (
                "Fire insurance should be quoted on a Valley Center address "
                "before the offer rather than during escrow. Much of the "
                "community sits in a state-designated high or very high fire "
                "hazard severity zone, admitted carriers have narrowed what "
                "they write in those zones, and the California FAIR Plan plus "
                "a difference-in-conditions policy is a common result."
            ),
            "body": (
                "<p>That combination costs materially more than a standard "
                "homeowner's policy, and a lender will not fund without bound "
                "coverage in place. A quote on the specific address is "
                "therefore not a formality &mdash; it is a condition of the "
                "purchase being affordable at all.</p>"
            ),
        },
    ],

    # ---------------------------------------------------------------- #10
    # Ramona — backcountry, and the honest version of that.
    # ---------------------------------------------------------------- #
    "ramona": [
        {
            "anchor": "unincorporated",
            "question": "Is Ramona a city?",
            "lead": (
                "Ramona is an unincorporated community in the county's "
                "backcountry rather than an incorporated city. "
                f"{COUNTY_LAND_USE}"
            ),
            "body": (
                "<p>The Ramona Community Planning Group advises the County on "
                "development in the area under the Ramona Community Plan. "
                "Buyers planning to build, add a unit or split a parcel "
                "should read the zoning designation and that plan before "
                "committing, because the answer is set there rather than at "
                "a city counter.</p>"
            ),
        },
        {
            "anchor": "sub-areas",
            "question": "What are the different parts of Ramona?",
            "lead": (
                "Ramona spans the town centre along Main Street, the "
                "surrounding Santa Maria Valley, and San Diego Country "
                "Estates to the south-east &mdash; a large planned community "
                "with its own homeowners association, golf course and equestrian "
                "facilities. Parcel sizes range from conventional town lots "
                "to working acreage, and the rules attached to them differ "
                "accordingly."
            ),
            "body": (
                "<p>San Diego Country Estates is the distinction to draw "
                "early. A home there carries HOA governance and assessments "
                "that a parcel in the open valley does not, and the "
                "association's documents are a due-diligence item in their "
                "own right.</p>"
            ),
        },
        {
            "anchor": "well-septic",
            "question": "Do Ramona homes have well water and septic?",
            "lead": (
                "Ramona properties are served either by the Ramona Municipal "
                "Water District or, on outlying parcels, by private wells and "
                "septic systems. Which applies is a parcel-level fact that "
                "changes the inspection list, the running cost and sometimes "
                "the financing, and it is established from the property "
                "records rather than assumed from the address."
            ),
            "body": (
                "<p>A well needs yield and water quality testing; a septic "
                "system needs a functional inspection and the leach field "
                "located. Both are ordinary parts of a backcountry purchase "
                "and both are routinely skipped by buyers who came from a "
                "city and did not know to ask.</p>"
            ),
        },
        {
            "anchor": "fire-insurance",
            "question": "What about fire risk and insurance in Ramona?",
            "lead": (
                "Ramona sits in the county's backcountry fire environment, "
                "and insurance availability is the first thing to price on "
                "any address there. Much of the area falls in a state-"
                "designated high or very high fire hazard severity zone, "
                "where admitted carriers have withdrawn capacity and the "
                "California FAIR Plan plus a difference-in-conditions policy "
                "is a common outcome."
            ),
            "body": (
                "<p>CAL FIRE operates the Ramona Air Attack Base at Ramona "
                "Airport, one of the state's aerial firefighting bases, which "
                "is a genuine local fact worth knowing &mdash; but it does "
                "not substitute for a quote on the specific parcel. Defensible "
                "space condition, roof type and access width all affect what "
                "a carrier will write, and all are inspectable before the "
                "contingency period ends.</p>"
            ),
        },
    ],
}


# --------------------------------------------------------------------------
# The original six. `fanout.py` has carried researched sub-queries for these
# since the first build and nothing answered them — the generator emitted the
# same three blocks here as everywhere else. These are those sub-queries,
# answered, under the same evidence rules as the North County set above.
# --------------------------------------------------------------------------

GUIDES.update({
    "del-sur": [
        {
            "anchor": "cfd-term",
            "question": "When does Mello-Roos end in Del Sur?",
            "lead": (
                "A Del Sur Mello-Roos levy ends when the bonds it services "
                "are retired, and the remaining term is set in the formation "
                "documents for the specific district rather than being a "
                "single Del Sur-wide date. Because Del Sur homes can sit "
                "inside both Poway Unified CFD&nbsp;#12 and Black Mountain "
                "Ranch Villages CFD&nbsp;#4, a parcel can have two terms "
                "running on two different schedules."
            ),
            "body": (
                "<p>One distinction is worth understanding before assuming an "
                "end date. Many community facilities districts levy for two "
                "things: a bond component that retires when the debt is paid, "
                "and a services component that funds ongoing maintenance and "
                "does not expire. A district can therefore &ldquo;end&rdquo; "
                "and still leave an annual charge on the bill.</p>"
                "<p>The district administrators named on the tax bill will "
                "state the remaining term for a specific parcel. That is the "
                "only answer worth acting on.</p>"
            ),
        },
        {
            "anchor": "vs-4s-ranch",
            "question": "Del Sur or 4S Ranch — what actually differs?",
            "lead": (
                "Del Sur and 4S Ranch share a ZIP code, a school district and "
                "a Mello-Roos burden, and differ mainly in age and layout. Del "
                "Sur is the newer of the two, built out through the 2000s and "
                "2010s inside the Black Mountain Ranch master plan around an "
                "unusually large program of pools, parks, gardens and trails. "
                "4S Ranch is slightly older and organised around a larger "
                "retail core."
            ),
            "body": (
                "<p>The tax detail differs too, and it is not a matter of one "
                "being cheaper. Del Sur parcels can carry Poway Unified "
                "CFD&nbsp;#12 alongside Black Mountain Ranch Villages "
                "CFD&nbsp;#4; 4S Ranch parcels sit under Poway Unified "
                "CFD&nbsp;#6 or #10 and their improvement areas. Which "
                "specific districts apply, and at what amount, is a "
                "parcel-level fact on the tax bill rather than a community "
                "characteristic.</p>"
                "<p>Buyers weighing either against a lower tax bill in the "
                "same school district should also look at "
                "<a href=\"/neighborhoods/poway\">the city of Poway</a>, which "
                "is inside Poway Unified but largely predates these "
                "districts.</p>"
            ),
        },
        {
            "anchor": "climate",
            "question": "Is Del Sur hotter than the coast?",
            "lead": (
                "Del Sur sits inland of the coastal ridgelines, and summer "
                "afternoons there run warmer than Del Mar or Carmel Valley "
                "while the marine layer clears earlier in the day. That is the "
                "standard inland-versus-coastal pattern in San Diego County "
                "rather than anything specific to the community, and the "
                "National Weather Service San Diego office publishes the "
                "actual climate normals for anyone who wants the figures "
                "instead of the impression."
            ),
            "body": (
                "<p>The practical consequence is cooling load. An inland home "
                "of the same size and vintage will generally run its air "
                "conditioning more than a coastal one, which is worth asking "
                "a seller about directly &mdash; utility history is "
                "disclosable and far more informative than a temperature "
                "average.</p>"
            ),
        },
        {
            "anchor": "amenities",
            "question": "What amenities does Del Sur have?",
            "lead": (
                "Del Sur was planned around a shared amenity program rather "
                "than a single clubhouse: multiple neighborhood pools, a trail "
                "network connecting the villages, parks and community gardens, "
                "all administered by the Del Sur Community Association. "
                "Access comes with the property rather than by separate "
                "membership."
            ),
            "body": (
                "<p>That program is funded by the HOA assessment, which sits "
                "alongside the Mello-Roos levy rather than replacing it. A "
                "true cost comparison against a community with fewer shared "
                "facilities has to count both, and the association&rsquo;s "
                "current budget and reserve study &mdash; both disclosable "
                "documents &mdash; are where the real numbers are.</p>"
            ),
        },
    ],

    "4s-ranch": [
        {
            "anchor": "cfd-worth-it",
            "question": "Is the Mello-Roos in 4S Ranch worth it?",
            "lead": (
                "Whether 4S Ranch Mello-Roos is worth paying is arithmetic "
                "rather than opinion, and the comparison most buyers skip is "
                "the useful one: 4S Ranch against a home in the same Poway "
                "Unified boundary that carries no community facilities "
                "district. The districts financed the schools, roads and "
                "parks that made the community; the question is what the same "
                "school access costs elsewhere."
            ),
            "body": (
                "<p>Run it as total monthly cost &mdash; principal, interest, "
                "base property tax, the CFD levy and the HOA assessment "
                "&mdash; against the same figure for "
                "<a href=\"/neighborhoods/poway\">the city of Poway</a>, which "
                "sits in the same district and was largely built before these "
                "CFDs were formed. The trade is usually newer construction "
                "and walkable retail on one side against a lower monthly "
                "obligation, older stock and larger lots on the other. Both "
                "are defensible; only one is usually presented.</p>"
            ),
        },
        {
            "anchor": "vs-del-sur",
            "question": "4S Ranch or Del Sur — taxes and amenities compared?",
            "lead": (
                "4S Ranch and Del Sur are adjacent, share the 92127 ZIP code "
                "and both sit in Poway Unified, so the choice between them is "
                "not about schools. 4S Ranch is organised around 4S Commons "
                "Town Center and its everyday retail; Del Sur is newer and "
                "organised around a distributed program of pools, parks and "
                "trails run by its community association."
            ),
            "body": (
                "<p>On tax, neither is categorically cheaper. 4S Ranch parcels "
                "sit under Poway Unified CFD&nbsp;#6 or #10 and their "
                "improvement areas; Del Sur parcels can carry CFD&nbsp;#12 "
                "plus the Black Mountain Ranch Villages district. Comparing "
                "two specific tax bills settles it; comparing two community "
                "reputations does not.</p>"
            ),
        },
        {
            "anchor": "walkability",
            "question": "What can you walk to in 4S Ranch?",
            "lead": (
                "4S Commons Town Center is the reason walkability comes up in "
                "4S Ranch at all: a grocery-anchored retail centre with "
                "everyday services, restaurants and a cinema, sited so that "
                "much of the surrounding residential development reaches it "
                "on foot or by bike through the trail and sidewalk network."
            ),
            "body": (
                "<p>How much that is worth depends entirely on which part of "
                "the community an address sits in &mdash; 92127 is large and "
                "hilly, and a half-mile on the map can be a serious climb. "
                "Walking the actual route from a specific house, once, is "
                "worth more than any published walkability score.</p>"
            ),
        },
        {
            "anchor": "fire-insurance",
            "question": "Is 4S Ranch in a fire zone, and can you insure it?",
            "lead": (
                "4S Ranch borders open space and canyon terrain on its "
                "northern and eastern edges, and parts of the 92127 area fall "
                "within or adjacent to state-designated fire hazard severity "
                "zones. CAL FIRE publishes those maps by parcel, and the "
                "designation for a specific address is checkable before an "
                "offer rather than after."
            ),
            "body": (
                "<p>The designation matters mostly through insurance. "
                "Carriers have narrowed what they write near open space, and "
                "a quote on the specific address during the contingency "
                "period is the difference between a smooth close and a "
                "financing problem at the end of escrow &mdash; a lender will "
                "not fund without bound coverage. Defensible space condition, "
                "roof type and access are all inspectable and all affect what "
                "a carrier will offer.</p>"
            ),
        },
    ],

    "scripps-ranch": [
        {
            "anchor": "which-district",
            "question": "Is Scripps Ranch in Poway Unified or San Diego Unified?",
            "lead": (
                "Scripps Ranch is in San Diego Unified School District, not "
                "Poway Unified &mdash; a distinction that catches buyers "
                "comparing it against the 92127 communities a few miles north, "
                "which are in Poway Unified. Scripps Ranch High School, "
                "Marshall Middle and the community&rsquo;s elementary schools "
                "are all San Diego Unified schools."
            ),
            "body": (
                "<p>That single fact explains the other one buyers notice: "
                "Scripps Ranch carries no community facilities district named "
                "for it in the County Auditor&rsquo;s active list, while the "
                "Poway Unified communities to the north carry several. "
                "Different district, different financing history, different "
                "tax bill. "
                f"{CONFIRM_SCHOOL}</p>"
            ),
        },
        {
            "anchor": "wildfire",
            "question": "What is the wildfire risk in Scripps Ranch?",
            "lead": (
                "Scripps Ranch has a documented fire history: the 2003 Cedar "
                "Fire burned into the community and destroyed homes there. "
                "That is a matter of public record rather than a hypothetical, "
                "and it is the honest starting point for anyone buying against "
                "the canyon edges the community is built around."
            ),
            "body": (
                "<p>What follows from it is practical. CAL FIRE publishes fire "
                "hazard severity zone maps by parcel; the City of San Diego "
                "enforces brush management requirements on properties adjacent "
                "to open space; and insurance availability should be quoted on "
                "the specific address early rather than assumed from a "
                "neighbouring one. Homes rebuilt since 2003 were built to "
                "later codes than those around them, which is worth "
                "establishing from the permit history.</p>"
            ),
        },
        {
            "anchor": "jet-noise",
            "question": "Is MCAS Miramar jet noise a problem in Scripps Ranch?",
            "lead": (
                "Scripps Ranch sits north of Marine Corps Air Station Miramar, "
                "and aircraft noise is a real and legally recognised factor "
                "rather than a matter of opinion. San Diego County adopted an "
                "Airport Land Use Compatibility Plan for MCAS Miramar that "
                "maps noise contours and an airport influence area, and "
                "California law requires disclosure when a property sits "
                "within that influence area."
            ),
            "body": (
                "<p>Exposure varies sharply across the community depending on "
                "position relative to the flight paths, so the answer for one "
                "street is not the answer for another. The compatibility plan "
                "maps are public, the disclosure is part of the transaction, "
                "and standing on the property at different times of day is "
                "the check no document replaces.</p>"
            ),
        },
        {
            "anchor": "lake-miramar",
            "question": "What can you do at Lake Miramar?",
            "lead": (
                "Lake Miramar is a City of San Diego reservoir on the edge of "
                "Scripps Ranch with a paved loop road of roughly five miles "
                "used for walking, running and cycling, plus shore and boat "
                "fishing with a city permit and seasonal boat rental. Being "
                "a working reservoir rather than a park, it is city-managed "
                "open space and not subject to a developer&rsquo;s "
                "entitlement."
            ),
            "body": (
                "<p>For a buyer, that permanence is the point. The loop and "
                "the water are a durable feature of the community rather than "
                "an amenity that could be built over, which is a different "
                "kind of value from a private clubhouse.</p>"
            ),
        },
    ],

    "carmel-valley": [
        {
            "anchor": "not-monterey",
            "question": "Is Carmel Valley near Carmel-by-the-Sea?",
            "lead": (
                "Carmel Valley in this context is a community of the City of "
                "San Diego in the 92130 ZIP code, roughly 20 miles north of "
                "downtown San Diego. It is unrelated to Carmel Valley in "
                "Monterey County, some 400 miles north, and searches for the "
                "name return both &mdash; which is worth knowing before "
                "trusting a photograph or a market figure attached to it."
            ),
        },
        {
            "anchor": "schools-structure",
            "question": "Do Carmel Valley homes fall in the Del Mar Union district?",
            "lead": (
                "Much of Carmel Valley is served by Del Mar Union School "
                "District for kindergarten through sixth grade and San "
                "Dieguito Union High School District for grades seven through "
                "twelve &mdash; despite the homes carrying City of San Diego "
                "addresses. A San Diego address does not mean San Diego "
                "Unified here, and that surprises buyers who assume the city "
                "name settles the district."
            ),
            "body": (
                "<p>The boundaries do not follow the ZIP code, so two homes a "
                "few streets apart can be assigned differently, and buyers pay "
                "for the assignment. "
                f"{CONFIRM_SCHOOL}</p>"
            ),
        },
        {
            "anchor": "torrey-pines",
            "question": "Which Carmel Valley homes feed Torrey Pines High School?",
            "lead": (
                "Torrey Pines High School is a San Dieguito Union High School "
                "District school, and assignment to it is set by the "
                "district&rsquo;s attendance areas rather than by being in "
                "Carmel Valley. San Dieguito Union also runs a school choice "
                "process, so the school a student is assigned to and the "
                "school a student attends are two separate questions with two "
                "separate answers."
            ),
            "body": (
                "<p>Anyone buying specifically for a named high school should "
                "confirm the current attendance area for the exact address "
                "with the district, and understand how the choice process "
                "works before treating an assignment as guaranteed. "
                "Attendance areas are redrawn from time to time.</p>"
            ),
        },
        {
            "anchor": "pacific-highlands-ranch",
            "question": "Is Pacific Highlands Ranch part of Carmel Valley?",
            "lead": (
                "Pacific Highlands Ranch is a separate master-planned "
                "community immediately north-east of Carmel Valley, inside "
                "the City of San Diego, and it is frequently marketed as part "
                "of Carmel Valley because the two share the 92130 ZIP code. "
                "Structurally they are not the same place: Pacific Highlands "
                "Ranch is newer, built under its own subarea plan, and has "
                "its own community governance."
            ),
            "body": (
                "<p>The distinction reaches the tax bill. Carmel Valley proper "
                "has no community facilities district named for it in the "
                "County Auditor&rsquo;s active list, while the Black Mountain "
                "Ranch villages that adjoin Pacific Highlands Ranch do carry "
                "districts. Where a specific parcel falls is therefore worth "
                "establishing rather than assuming from the ZIP code.</p>"
            ),
        },
        {
            "anchor": "marine-layer",
            "question": "How bad is the marine layer in Carmel Valley?",
            "lead": (
                "Carmel Valley sits close enough to the coast to get the "
                "regional late-spring and early-summer marine layer &mdash; "
                "the overcast mornings locally called May Gray and June Gloom "
                "&mdash; and far enough inland that it burns off earlier than "
                "it does in Del Mar. Position within the community matters: "
                "addresses on the western canyon rims hold cloud longer than "
                "those on the eastern edge."
            ),
        },
    ],

    "del-mar": [
        {
            "anchor": "train-station",
            "question": "Does Del Mar have a train station?",
            "lead": (
                "Del Mar has no passenger rail station. The rail corridor runs "
                "along the Del Mar bluff and through the city, but trains do "
                "not stop there &mdash; the nearest station is Solana Beach, "
                "immediately north, which serves the COASTER commuter line and "
                "Amtrak&rsquo;s Pacific Surfliner."
            ),
            "body": (
                "<p>The bluff section carries a second consequence worth "
                "knowing about. That stretch of track sits on an eroding "
                "coastal bluff and is the subject of long-running regional "
                "planning work on stabilisation and eventual realignment, "
                "which is a live public process rather than a settled one. "
                "Anyone buying near the corridor should read the current "
                "SANDAG planning material rather than rely on how things look "
                "today.</p>"
            ),
        },
        {
            "anchor": "coastal-zone",
            "question": "What does the Coastal Zone mean for remodeling in Del Mar?",
            "lead": (
                "Del Mar lies almost entirely within the California Coastal "
                "Zone, which means most exterior alterations, additions and "
                "rebuilds require a coastal development permit in addition to "
                "an ordinary building permit. Del Mar administers that through "
                "its own certified Local Coastal Program, with some categories "
                "of decision appealable to the California Coastal Commission."
            ),
            "body": (
                "<p>For a buyer intending to change a house, that is a "
                "timeline, a cost and a risk that an inland comparable does "
                "not carry &mdash; and it is the single largest reason two "
                "similar Del Mar homes can be worth materially different "
                "amounts. What has already been permitted, and what has been "
                "refused, is on file with the city and worth reading before "
                "an offer rather than after.</p>"
            ),
        },
        {
            "anchor": "view-premium",
            "question": "How much more does an ocean view cost in Del Mar?",
            "lead": (
                "An ocean view in Del Mar carries a premium that no formula "
                "captures, because the durable question is not how good the "
                "view is today but whether it is protected. A view secured by "
                "topography &mdash; nothing can be built in front of it "
                "&mdash; is a different asset from one that depends on a "
                "neighbour&rsquo;s roofline staying where it is."
            ),
            "body": (
                "<p>Del Mar regulates building height and applies design "
                "review, and the city&rsquo;s rules on view impacts are part "
                "of the record for any specific parcel. Establishing what "
                "could be built on the lots between a house and the water, "
                "under current zoning, is the analysis worth paying for. A "
                "comparative market analysis that prices the view without "
                "answering that question is pricing an assumption.</p>"
            ),
        },
        {
            "anchor": "days-on-market",
            "question": "Why do Del Mar homes sit on the market so long?",
            "lead": (
                "Del Mar is a small, high-price market, and both of those "
                "facts lengthen marketing times independently of how any "
                "individual home is priced. Few homes trade in a given year, "
                "so the pool of buyers for any one of them is small, and the "
                "comparable sales an appraiser or a pricing analysis can draw "
                "on are correspondingly thin."
            ),
            "body": (
                "<p>Days-on-market figures for a market this size swing hard "
                "from quarter to quarter for that reason, which is why no "
                "number is published here &mdash; a stale one would be worse "
                "than none. The current figure is available from the MLS on "
                "request for a specific price band and property type, which "
                "is the only form in which it means anything.</p>"
            ),
        },
        {
            "anchor": "vs-encinitas-solana",
            "question": "Del Mar, Encinitas or Solana Beach — how do they differ?",
            "lead": (
                "Del Mar, Solana Beach and Encinitas are three adjacent "
                "coastal cities that differ on two structural points buyers "
                "can actually check. Rail: Solana Beach and Encinitas each "
                "have a COASTER station, Del Mar has none. Schools: Del Mar "
                "and Solana Beach feed different elementary districts &mdash; "
                "Del Mar Union and Solana Beach School District respectively "
                "&mdash; while Encinitas splits between Encinitas Union and "
                "the separate Cardiff School District."
            ),
            "body": (
                "<p>All three then feed San Dieguito Union High School "
                "District, and all three sit substantially inside the Coastal "
                "Zone with the permitting consequences that carries. The "
                "choice between them is generally made on price point, on lot "
                "and street character, and on which elementary assignment "
                "applies &mdash; not on any citywide characterisation.</p>"
            ),
        },
    ],

    "rancho-santa-fe": [
        {
            "anchor": "the-covenant",
            "question": "What is the Covenant in Rancho Santa Fe?",
            "lead": (
                "The Covenant is the original core of Rancho Santa Fe: roughly "
                "6,200 acres governed by a protective covenant recorded in the "
                "1920s and administered today by the Rancho Santa Fe "
                "Association. Membership is not optional &mdash; it runs with "
                "the land &mdash; and it brings both the Association&rsquo;s "
                "assessment and its architectural review process."
            ),
            "body": (
                "<p>Not every property with a Rancho Santa Fe address is in "
                "the Covenant, and the difference is substantial: different "
                "governance, different assessments, different rules about what "
                "can be built. Establishing whether a specific parcel is "
                "inside it is the first question on any Rancho Santa Fe "
                "purchase, not a detail for later.</p>"
            ),
        },
        {
            "anchor": "art-jury",
            "question": "How strict is the Rancho Santa Fe Art Jury?",
            "lead": (
                "The Art Jury is the Rancho Santa Fe Association&rsquo;s "
                "architectural review body, and within the Covenant its "
                "approval is required for exterior work &mdash; new "
                "construction, additions, significant remodels, and in many "
                "cases landscape and hardscape changes. Review is against the "
                "community&rsquo;s adopted regulations rather than against "
                "individual taste, but it is a real approval process with real "
                "timelines."
            ),
            "body": (
                "<p>For a buyer planning to renovate, that process sits on "
                "top of County permitting rather than replacing it, and both "
                "have to be budgeted. The Association publishes its "
                "regulations and its meeting schedule; reading them before "
                "committing to a project is considerably cheaper than "
                "discovering them afterwards.</p>"
            ),
        },
        {
            "anchor": "sewer-septic",
            "question": "Do Rancho Santa Fe homes have sewer or septic?",
            "lead": (
                "Rancho Santa Fe has both, and which one applies is a "
                "parcel-level fact rather than a community-wide one. Many "
                "properties there, particularly larger Covenant lots, are on septic "
                "systems rather than connected to a sewer, while other parts "
                "of the community are served by the Rancho Santa Fe Community "
                "Services District. Water comes from the Santa Fe Irrigation "
                "District."
            ),
            "body": (
                "<p>On septic, the diligence is a functional inspection and "
                "locating the leach field, and the system&rsquo;s capacity "
                "constrains what can be added to the house &mdash; a bedroom "
                "count is a septic question before it is an architectural one. "
                "That constraint is invisible in an automated valuation and "
                "decisive for anyone planning to expand.</p>"
            ),
        },
        {
            "anchor": "communities",
            "question": "Covenant, The Bridges, Cielo or Fairbanks Ranch — what is the difference?",
            "lead": (
                "Several distinct communities share the Rancho Santa Fe "
                "mailing address and are governed very differently. The "
                "Covenant is the historic core under the Rancho Santa Fe "
                "Association and its Art Jury. The Bridges and Fairbanks Ranch "
                "are gated homeowner associations, The Bridges built around a "
                "private golf club with its own membership structure. Cielo "
                "sits further east on higher ground with its own association."
            ),
            "body": (
                "<p>The differences that matter are governance and obligation: "
                "who reviews exterior changes, what the annual assessment "
                "covers, and whether a club membership is required, optional "
                "or unavailable. Those are answered by the governing documents "
                "for the specific community, all of which are disclosable in "
                "a transaction. The Auditor&rsquo;s active district list shows "
                "one community facilities district for Rancho Santa Fe, "
                "administered by the Community Service District, but "
                "association and club obligations are usually the larger "
                "recurring cost in this market.</p>"
            ),
        },
        {
            "anchor": "days-on-market",
            "question": "Why do Rancho Santa Fe homes take so long to sell?",
            "lead": (
                "Rancho Santa Fe is a low-volume, high-price market on large "
                "parcels, and each of those attributes lengthens marketing "
                "time on its own. The buyer pool for any individual property "
                "is small, the homes are highly differentiated from one "
                "another, and thin comparable data makes pricing genuinely "
                "harder than in a tract market where twenty near-identical "
                "homes trade a year."
            ),
            "body": (
                "<p>No days-on-market figure is published here because in a "
                "market this size the number swings hard between quarters and "
                "a stale one would mislead. The current figure for a specific "
                "price band is available from the MLS on request, which is the "
                "only form in which it is worth anything.</p>"
            ),
        },
    ],
})

# --------------------------------------------------------------------------
# City neighborhoods, East County and South Bay, added 2026-07-30 at client
# request — southward to where salesRecord.md says the book actually lives.
# Same rules: structural facts only, places and processes never people.
# Live regulatory facts verified 2026-07-30: STRO tiers per the city's
# ordinance, the Hillcrest Focused Plan Amendment (adopted 2024-07-30), the
# La Jolla incorporation timeline per SD LAFCO, the county CFD list re-read
# in full (see taxes.py).
# --------------------------------------------------------------------------

GUIDES.update({
    "la-jolla": [
        {
            "anchor": "own-city",
            "question": "Is La Jolla its own city?",
            "lead": (
                "La Jolla is not its own city today &mdash; it is a "
                "community of the City of San Diego with its own postal "
                "identity (92037) &mdash; and an active incorporation "
                "effort is testing that: LAFCO advanced a cityhood "
                "application in 2025, the state-required fiscal analysis "
                "began in 2026, and organizers aim for a 2028 ballot."
            ),
            "body": (
                "<p>Two facts keep the question honest. Incorporation "
                "would need approval from La Jolla voters <em>and</em> "
                "voters in the rest of San Diego, and until any of that "
                "happens the City of San Diego&rsquo;s rules govern every "
                "permit, tax and service in La Jolla. The San Diego LAFCO "
                "project page is the record; a transaction today is a "
                "City of San Diego transaction.</p>"
            ),
        },
        {
            "anchor": "height-limit",
            "question": "Why are most La Jolla buildings low-rise?",
            "lead": (
                "A 30-foot coastal height limit, adopted by San Diego "
                "voters in 1972&rsquo;s Proposition D, governs new "
                "construction across the city&rsquo;s coastal zone "
                "including La Jolla &mdash; the reason the skyline stops "
                "where it does, and a hard constraint on any remodel that "
                "adds a story."
            ),
            "body": (
                "<p>The limit predates almost every current owner and "
                "survives legal challenge better than buyers assume. What "
                "it means in practice: redevelopment value on a La Jolla "
                "lot is set by what thirty feet can hold, and any plan "
                "premised on building higher needs the specific "
                "parcel&rsquo;s zoning read before money moves.</p>"
            ),
        },
        {
            "anchor": "micro-areas",
            "question": "What are the different parts of La Jolla?",
            "lead": (
                "La Jolla divides into named micro-areas &mdash; the "
                "Village, La Jolla Shores, the Muirlands, Bird Rock and "
                "others &mdash; that differ structurally in lot size, "
                "slope, walkability and stock age, which is why "
                "community-wide generalizations mislead more in La Jolla "
                "than almost anywhere in San Diego."
            ),
            "body": (
                "<p>The Village and Bird Rock are walkable commercial "
                "spines with smaller lots; the Shores flattens to the "
                "beach; the Muirlands and the hillsides above carry the "
                "large view parcels. Pricing, insurance and renovation "
                "questions all answer differently by micro-area, which is "
                "why the useful comparison set is the micro-area, not "
                "&ldquo;La Jolla.&rdquo;</p>"
            ),
        },
    ],
    "pacific-beach": [
        {
            "anchor": "str-license",
            "question": "Can you run a short-term rental in Pacific Beach?",
            "lead": (
                "Short-term rentals in Pacific Beach run under the City "
                "of San Diego&rsquo;s STRO ordinance: whole-home licenses "
                "outside Mission Beach (Tier 3) are capped citywide at "
                "about one percent of the city&rsquo;s housing stock, "
                "home-sharing tiers are separate, and only Mission Beach "
                "carries its own higher cap."
            ),
            "body": (
                "<p>The practical consequence for a Pacific Beach "
                "purchase premised on rental income: the license path "
                "has to be confirmed before close, not assumed &mdash; "
                "licenses are issued to hosts rather than attaching to "
                "the property, and the citywide cap means availability "
                "changes over time. The city&rsquo;s STRO pages carry "
                "the current tier rules and counts.</p>"
            ),
        },
        {
            "anchor": "flood-zones",
            "question": "Do parts of Pacific Beach sit in a flood zone?",
            "lead": (
                "Low-lying blocks of Pacific Beach around Mission Bay "
                "&mdash; Crown Point among them &mdash; sit in mapped "
                "FEMA flood zones, and the designation is a parcel-level "
                "fact that decides whether a lender requires flood "
                "insurance."
            ),
            "body": (
                "<p>FEMA&rsquo;s flood maps are public and searchable by "
                "address, and the answer belongs in the affordability "
                "math alongside the mortgage quote &mdash; flood "
                "premiums on the bay-adjacent blocks are real money. Two "
                "streets of elevation routinely separate a mapped zone "
                "from an unmapped one.</p>"
            ),
        },
        {
            "anchor": "micro-areas",
            "question": "How do North PB, Crown Point and the beach blocks differ?",
            "lead": (
                "Pacific Beach splits structurally into the ocean-front "
                "and boardwalk blocks, the flat central grid, Crown "
                "Point on the bay, and North Pacific Beach rising toward "
                "Bird Rock &mdash; with stock age, noise exposure and "
                "rental concentration all changing block by block."
            ),
            "body": (
                "<p>North Pacific Beach carries more owner-occupied "
                "single-family stock; the blocks nearest the boardwalk "
                "carry the densest rental and nightlife exposure &mdash; "
                "a difference any buyer can verify with two evening "
                "visits. The useful question is never &ldquo;what is PB "
                "like&rdquo; but &ldquo;what is this block like at 11 "
                "pm.&rdquo;</p>"
            ),
        },
    ],
    "ocean-beach": [
        {
            "anchor": "low-rise",
            "question": "Why has Ocean Beach stayed low-rise while other beach towns built up?",
            "lead": (
                "Ocean Beach sits inside the coastal zone governed by "
                "San Diego&rsquo;s 30-foot height limit (Proposition D, "
                "1972), and its community plan has held a low-scale line "
                "for decades &mdash; together they are why the cottage "
                "fabric survives and why redevelopment assumptions that "
                "pencil elsewhere do not pencil in Ocean Beach."
            ),
            "body": (
                "<p>For a buyer the constraint cuts both ways: it limits "
                "what can be built on a lot, and it protects the scale "
                "that makes the neighborhood worth buying into. Plans "
                "premised on maximizing a parcel need the community "
                "plan and coastal rules read first &mdash; Ocean Beach "
                "is where those documents bind hardest.</p>"
            ),
        },
        {
            "anchor": "overflight",
            "question": "How loud is airport overflight in Ocean Beach?",
            "lead": (
                "Aircraft departing San Diego International climb west "
                "over the Point Loma peninsula, and parts of Ocean Beach "
                "hear it &mdash; how much varies block by block, and the "
                "airport authority publishes noise contour maps that put "
                "a checkable line under what an afternoon visit "
                "suggests."
            ),
            "body": (
                "<p>Overflight is a mapped, disclosed condition rather "
                "than a rumor: the contours exist, the disclosure "
                "obligations exist, and an hour on the specific block at "
                "departure-heavy times answers the question no listing "
                "will. Sensitivity to it is personal; the facts about it "
                "are not.</p>"
            ),
        },
        {
            "anchor": "cottage-stock",
            "question": "What should an inspection focus on in an Ocean Beach cottage?",
            "lead": (
                "Ocean Beach&rsquo;s housing stock skews old and coastal "
                "&mdash; beach cottages from the early and mid twentieth "
                "century &mdash; so inspections there earn their fee on "
                "foundations, framing moisture, original electrical, "
                "sewer laterals and salt-air corrosion rather than on "
                "cosmetics."
            ),
            "body": (
                "<p>None of that is a reason to avoid the stock; it is "
                "the reason inspection contingencies exist. A cottage "
                "that has had its systems renewed is a different "
                "purchase from one wearing new paint over 1940s wiring, "
                "and the permit history &mdash; public record &mdash; "
                "usually says which one is on offer.</p>"
            ),
        },
    ],
    "hillcrest": [
        {
            "anchor": "plan-amendment",
            "question": "What did the 2024 Hillcrest plan amendment change?",
            "lead": (
                "San Diego&rsquo;s City Council adopted the Hillcrest "
                "Focused Plan Amendment on July 30, 2024, creating "
                "capacity for roughly 17,000 additional homes with "
                "densities that allow high-rise construction &mdash; a "
                "generational rezoning of the neighborhood&rsquo;s "
                "core."
            ),
            "body": (
                "<p>A plan sets capacity; construction follows financing "
                "and takes years &mdash; so the amendment&rsquo;s "
                "near-term effect is on land value and development "
                "interest, not on next year&rsquo;s skyline. For owners "
                "the practical questions are parcel-specific: what "
                "density now applies to this lot, and what is proposed "
                "nearby. The city&rsquo;s plan page and development "
                "tracker answer both.</p>"
            ),
        },
        {
            "anchor": "medical-campus",
            "question": "What is happening to the UCSD hospital campus in Hillcrest?",
            "lead": (
                "UC San Diego is redeveloping its Hillcrest medical "
                "campus under a long-range development plan &mdash; a "
                "multi-year rebuild that keeps the institution in the "
                "neighborhood while replacing most of the aging "
                "site &mdash; and construction phasing there is a "
                "years-long fact of life for the surrounding blocks."
            ),
            "body": (
                "<p>Institutional campuses run on published plans: the "
                "LRDP and its environmental documents state what gets "
                "built, roughly when, and how traffic and staging are "
                "handled. A buyer near the campus reads those documents "
                "rather than guessing &mdash; the difference between a "
                "construction season and a construction decade is in "
                "them.</p>"
            ),
        },
        {
            "anchor": "stock-eras",
            "question": "What kind of housing stock does Hillcrest actually have?",
            "lead": (
                "Hillcrest layers a century of stock &mdash; early "
                "1900s streetcar-suburb houses, mid-century apartment "
                "courts, 1970s&ndash;80s condo conversions, and newer "
                "mixed-use buildings &mdash; and each era carries its "
                "own inspection and ownership questions."
            ),
            "body": (
                "<p>Conversion-era condos deserve particular attention "
                "to HOA reserves and building systems &mdash; a 1970s "
                "building&rsquo;s pipes do not care about its renovated "
                "kitchens. On the older houses, the usual pre-war items "
                "&mdash; foundations, laterals, original wiring &mdash; "
                "apply as they do across the urban core.</p>"
            ),
        },
    ],
    "north-park": [
        {
            "anchor": "historic-districts",
            "question": "Do North Park homes fall under historic-district rules?",
            "lead": (
                "Parts of North Park sit inside designated historic "
                "districts &mdash; the Dryden District among them &mdash; "
                "where City of San Diego historical-resource rules attach "
                "to contributing homes: exterior changes route through "
                "historic review, and Mills Act contracts can reduce "
                "property taxes in exchange for preservation "
                "obligations."
            ),
            "body": (
                "<p>Historic status is parcel-specific and checkable "
                "before an offer: the city&rsquo;s historical resources "
                "records state whether a home is designated or "
                "contributing, and escrow will surface an existing Mills "
                "Act contract &mdash; an obligation and a tax benefit "
                "that transfer with the house. Neither is a surprise "
                "anyone needs to have.</p>"
            ),
        },
        {
            "anchor": "adu-activity",
            "question": "Why do North Park lots carry so many ADUs?",
            "lead": (
                "North Park&rsquo;s transit-adjacent zoning made it one "
                "of the City of San Diego&rsquo;s most active areas for "
                "accessory dwelling units under the city&rsquo;s bonus "
                "rules &mdash; and those rules have been revised more "
                "than once, so what a lot could build last year, this "
                "year and next are three different questions."
            ),
            "body": (
                "<p>The current municipal code, not the neighbors&rsquo; "
                "lot, is the authority on what an ADU plan can be "
                "&mdash; and for a buyer, existing unpermitted units are "
                "the thing to smoke out in inspection and permit "
                "history. The <a href=\"/blog/adu-rules-san-diego-"
                "county-2026\">ADU rules explainer</a> covers the state "
                "layer and how to check a specific parcel.</p>"
            ),
        },
        {
            "anchor": "craftsman-stock",
            "question": "What does buying a North Park Craftsman actually involve?",
            "lead": (
                "North Park&rsquo;s signature stock is pre-war &mdash; "
                "Craftsman and California bungalows from the 1910s and "
                "1920s &mdash; which makes foundations, original "
                "electrical, sewer laterals and a century of "
                "renovation-over-renovation the substance of an "
                "inspection there."
            ),
            "body": (
                "<p>Permit history is the shortcut: a bungalow with "
                "documented system renewals is a different risk from an "
                "undocumented flip, at the same list price. And where a "
                "home might qualify as a historic resource, that status "
                "changes the renovation path &mdash; check it before "
                "planning, not after.</p>"
            ),
        },
    ],
    "downtown-san-diego": [
        {
            "anchor": "hoa-regime",
            "question": "What does an HOA actually cover in a Downtown San Diego high-rise?",
            "lead": (
                "A Downtown San Diego condominium is a share of a "
                "building run by its association: the HOA assessment "
                "carries the master insurance, building systems, staff "
                "and amenities, and the documents that price the "
                "purchase are the association&rsquo;s budget, reserve "
                "study and CC&amp;Rs &mdash; not the unit&rsquo;s "
                "finishes."
            ),
            "body": (
                "<p>Reserve funding is the number that separates "
                "similar-looking buildings: an under-reserved tower "
                "meets its roof and elevator bills through special "
                "assessments, and those arrive as five-figure surprises. "
                "Escrow delivers the documents; reading them is the "
                "inspection.</p>"
            ),
        },
        {
            "anchor": "districts",
            "question": "What are the different districts of Downtown San Diego?",
            "lead": (
                "Downtown San Diego is seven districts behaving "
                "differently &mdash; the Gaslamp Quarter, East Village, "
                "Marina, Columbia, Cortez Hill, Little Italy and the "
                "Core &mdash; with noise, construction pipeline and "
                "building age varying enough that the district matters "
                "more than the word downtown."
            ),
            "body": (
                "<p>Little Italy and Marina skew established and "
                "quieter; East Village carries the largest construction "
                "pipeline and the widest variance block to block; the "
                "Gaslamp is a nightlife district first. The same "
                "two-evening test that serves beach buyers serves "
                "downtown buyers: visit the block at night before "
                "pricing the view.</p>"
            ),
        },
        {
            "anchor": "height-caps",
            "question": "Why do Downtown San Diego towers stop at similar heights?",
            "lead": (
                "Aircraft on approach to San Diego International "
                "descend directly over Downtown San Diego, and federal "
                "airspace surfaces cap building heights below what "
                "zoning alone would allow &mdash; the reason the "
                "skyline plateaus rather than spikes."
            ),
            "body": (
                "<p>For an owner the practical edge of that fact is "
                "view durability: a protected view exists only where "
                "the parcel between you and the water cannot build "
                "higher, and the height caps make that calculable "
                "rather than hopeful. Overflight noise is the same "
                "checkable, block-varying fact it is everywhere on the "
                "approach path.</p>"
            ),
        },
    ],
    "college-area": [
        {
            "anchor": "sdsu-economics",
            "question": "How does SDSU shape the College Area housing market?",
            "lead": (
                "San Diego State University sits inside the College "
                "Area, and the community&rsquo;s housing economics run "
                "on it: a substantial share of the stock operates as "
                "student rentals, the city regulates high-occupancy "
                "conversions, and the university&rsquo;s own housing "
                "construction shifts the rental balance year to year."
            ),
            "body": (
                "<p>The consequence is two different underwritings of "
                "the same house: an owner-occupant prices quiet and "
                "condition; an investor prices bedrooms and the "
                "city&rsquo;s rental rules. Knowing which buyer a "
                "listing is priced for &mdash; and which one you are "
                "&mdash; is most of the negotiation in the College "
                "Area.</p>"
            ),
        },
        {
            "anchor": "trolley",
            "question": "Is the College Area on the trolley?",
            "lead": (
                "The trolley&rsquo;s Green Line serves the College Area "
                "through the SDSU Transit Center &mdash; an underground "
                "station beneath the campus &mdash; connecting toward "
                "Mission Valley and downtown, which puts genuine "
                "rail transit inside a neighborhood that otherwise "
                "reads as postwar suburbia."
            ),
            "body": (
                "<p>Transit adjacency also carries zoning consequences "
                "in San Diego &mdash; density and parking rules relax "
                "near stations &mdash; so proximity to the station is "
                "both a commute fact and a development-potential fact, "
                "each checkable against the current code.</p>"
            ),
        },
        {
            "anchor": "stock",
            "question": "What is the housing stock like in the College Area?",
            "lead": (
                "The College Area&rsquo;s stock is predominantly "
                "postwar &mdash; 1940s through 1960s ranches and "
                "minimal-traditional homes on modest lots, with canyon "
                "and view pockets on the ridges &mdash; and its "
                "inspection profile follows that era: original panels, "
                "galvanized supply lines, aging laterals."
            ),
            "body": (
                "<p>Condition variance is wide because use has been "
                "wide: long-held family homes and decades-hard rentals "
                "sit on the same street at the same list price. The "
                "permit record and a thorough inspection separate them "
                "&mdash; which is the entire game in this "
                "neighborhood.</p>"
            ),
        },
    ],
    "chula-vista": [
        {
            "anchor": "east-west",
            "question": "Why do eastern and western Chula Vista feel like different markets?",
            "lead": (
                "Chula Vista splits at Interstate 805: western Chula "
                "Vista is the older city &mdash; mid-century stock, "
                "largely free of Mello-Roos &mdash; while the east side "
                "is master-planned (Eastlake, Otay Ranch, Millenia) and "
                "carries the densest community-facilities-district "
                "concentration in the county list."
            ),
            "body": (
                "<p>The same list price therefore buys two different "
                "monthly payments, and the Mello-Roos block above is "
                "where the difference lives &mdash; a single east-side "
                "parcel can carry city, elementary-district and "
                "high-school-district special-tax lines at once. "
                "Comparing east to west without the tax lines is "
                "comparing nothing.</p>"
            ),
        },
        {
            "anchor": "two-districts",
            "question": "Why does Chula Vista have two school districts instead of one?",
            "lead": (
                "Chula Vista has no unified school district: Chula "
                "Vista Elementary School District &mdash; among the "
                "largest elementary-only districts in California "
                "&mdash; runs kindergarten through sixth grade, and "
                "Sweetwater Union High School District runs seventh "
                "through twelfth."
            ),
            "body": (
                "<p>Both districts also levy their own Mello-Roos on "
                "the east side, which is the unusual part &mdash; the "
                "school-assignment question and the school-tax question "
                "are separate checks on the same address. Assignment "
                "itself follows each district&rsquo;s boundary maps, "
                "confirmed with the district for the exact address.</p>"
            ),
        },
        {
            "anchor": "bayfront",
            "question": "What is happening on the Chula Vista bayfront?",
            "lead": (
                "The Chula Vista Bayfront is mid-transformation: the "
                "Gaylord Pacific resort and convention center opened in "
                "2025 as the anchor of a decades-planned redevelopment "
                "of the industrial waterfront, with further phases "
                "entitled around it."
            ),
            "body": (
                "<p>Waterfront redevelopment moves on public documents "
                "&mdash; the port district&rsquo;s master plan and its "
                "phase approvals &mdash; and its effects on the west "
                "side are the trackable kind: employment, traffic "
                "patterns, and what happens to the blocks between the "
                "bay and Broadway. Watching the filings beats watching "
                "the renderings.</p>"
            ),
        },
    ],
    "santee": [
        {
            "anchor": "floodplain",
            "question": "Does the San Diego River flood in Santee?",
            "lead": (
                "The San Diego River runs the length of Santee, and "
                "parts of the valley floor sit in mapped FEMA "
                "floodplain &mdash; a parcel-level designation that "
                "decides whether a lender requires flood insurance and "
                "what site drainage a project must handle."
            ),
            "body": (
                "<p>The maps are public and address-searchable, and "
                "elevation moves fast on the valley edges &mdash; "
                "streets a quarter mile apart map differently. The "
                "check costs nothing before an offer and a premium "
                "surprise after one.</p>"
            ),
        },
        {
            "anchor": "fanita-ranch",
            "question": "What is Fanita Ranch and why does it keep coming up?",
            "lead": (
                "Fanita Ranch is a long-contested plan for roughly "
                "3,000 homes on Santee&rsquo;s northern hillsides, "
                "approved by the city more than once and repeatedly "
                "challenged in court &mdash; the single land-use "
                "decision most likely to change Santee&rsquo;s housing "
                "supply, traffic and evacuation planning."
            ),
            "body": (
                "<p>Whichever way it resolves, it is the variable: "
                "supply on that scale moves a small city&rsquo;s "
                "market. The city&rsquo;s records and the court docket "
                "are the sources that matter; anything else is "
                "advocacy from one side or the other, worth reading "
                "as such.</p>"
            ),
        },
        {
            "anchor": "sr52",
            "question": "What does the SR-52 commute mean for Santee?",
            "lead": (
                "State Route 52 begins in Santee and is its direct "
                "line west toward Kearny Mesa, UTC and the coastal "
                "job centers &mdash; and its peak-hour behavior is the "
                "honest cost of Santee&rsquo;s price advantage over "
                "communities nearer the coast."
            ),
            "body": (
                "<p>The corridor test-drives in an hour: westbound in "
                "the morning window, eastbound in the evening one. "
                "Trolley access &mdash; the Green Line terminates in "
                "Santee &mdash; is the alternative worth pricing for "
                "downtown-bound commuters.</p>"
            ),
        },
    ],
    "el-cajon": [
        {
            "anchor": "rancho-san-diego",
            "question": "Is Rancho San Diego part of El Cajon?",
            "lead": (
                "Rancho San Diego is not inside the city of El Cajon "
                "&mdash; it is unincorporated county territory southeast "
                "of the city line, carrying El Cajon mailing addresses "
                "&mdash; while Fletcher Hills and Granite Hills sit "
                "inside the city; the jurisdiction, not the address, "
                "decides whose rules and services apply."
            ),
            "body": (
                "<p>The pattern repeats across the county and this "
                "site keeps saying so because it keeps costing buyers "
                "money: mailing city is postal, jurisdiction is legal. "
                "For any El Cajon-addressed parcel, the county&rsquo;s "
                "and city&rsquo;s own maps say which government you are "
                "dealing with.</p>"
            ),
        },
        {
            "anchor": "monthly-cost",
            "question": "Why is the monthly cost lower in El Cajon than in newer communities at the same price?",
            "lead": (
                "El Cajon carries no community facilities district in "
                "the County Auditor&rsquo;s active list, and most of "
                "its stock predates HOA-financed development &mdash; so "
                "at the same purchase price, the monthly payment runs "
                "lower than in Mello-Roos communities, and the "
                "difference is structural rather than promotional."
            ),
            "body": (
                "<p>The honest comparison is total monthly cost: base "
                "taxes on older East County stock against base plus "
                "special taxes plus HOA in the newer master plans. The "
                "<a href=\"/mello-roos\">Mello-Roos lookup</a> makes "
                "the comparison concrete, community by community.</p>"
            ),
        },
        {
            "anchor": "gillespie",
            "question": "What is Gillespie Field and does it affect El Cajon homes?",
            "lead": (
                "Gillespie Field is the county-operated airport on El "
                "Cajon&rsquo;s northern edge &mdash; general aviation, "
                "not commercial service &mdash; and its traffic "
                "pattern, published land-use compatibility plan and "
                "disclosure rules are mapped facts a buyer near it can "
                "check rather than guess."
            ),
            "body": (
                "<p>Airport influence areas run on documents here as "
                "they do everywhere in the county: the compatibility "
                "plan defines the zones, and time on the specific "
                "street answers the subjective half of the question. "
                "The pattern matches Ramona&rsquo;s airfield and "
                "French Valley&rsquo;s &mdash; small airports are "
                "checkable neighbors.</p>"
            ),
        },
    ],
    "spring-valley": [
        {
            "anchor": "unincorporated",
            "question": "Is Spring Valley a city?",
            "lead": (
                "Spring Valley is unincorporated San Diego County "
                "&mdash; no city hall, with the Sheriff, county fire "
                "and county planning providing services &mdash; which "
                "puts a suburban community under the same governance "
                "the rural east county pages describe."
            ),
            "body": (
                "<p>Unincorporated status is practical, not "
                "ceremonial: permits route to county Planning &amp; "
                "Development Services, code questions to county "
                "ordinances, and service levels differ from the "
                "incorporated cities next door. La Mesa and Lemon "
                "Grove sit across a line that matters legally and "
                "invisibly.</p>"
            ),
        },
        {
            "anchor": "micro-areas",
            "question": "What are the different parts of Spring Valley?",
            "lead": (
                "Spring Valley&rsquo;s two ZIP codes cover distinct "
                "terrain &mdash; the valley-floor grid, Dictionary "
                "Hill&rsquo;s view slopes, and the Casa de Oro and "
                "Mount Helix edges shared with unincorporated La Mesa "
                "&mdash; with lot size, slope and stock age changing "
                "accordingly."
            ),
            "body": (
                "<p>Hillside parcels bring hillside questions &mdash; "
                "retaining walls, drainage, access grade &mdash; and "
                "the Mount Helix edge carries estate lots that price "
                "like a different community because structurally they "
                "are one. Per-street reading beats per-community "
                "reading here.</p>"
            ),
        },
        {
            "anchor": "value-structure",
            "question": "Why has Spring Valley been a volume market for value buyers?",
            "lead": (
                "Spring Valley combines mid-century stock, no "
                "community facilities district in the county&rsquo;s "
                "active list, and freeway position between SR-125, "
                "SR-94 and the South Bay job corridors &mdash; the "
                "structural ingredients of an entry-price market that "
                "moves on volume."
            ),
            "body": (
                "<p>The same structure sets the inspection agenda: "
                "older systems, additions of varying permit status, "
                "and hillside conditions. A permit-history read and a "
                "thorough inspection are where value purchases in "
                "Spring Valley are actually won.</p>"
            ),
        },
    ],
    "lemon-grove": [
        {
            "anchor": "own-city",
            "question": "Is Lemon Grove its own city?",
            "lead": (
                "Lemon Grove incorporated in 1977 and is one of San "
                "Diego County&rsquo;s smallest cities by area &mdash; "
                "a full-service municipality of roughly four square "
                "miles with the Orange Line trolley running through "
                "its center."
            ),
            "body": (
                "<p>Small-city status is a governance fact with "
                "practical texture: one planning counter, one council, "
                "and city-level decisions that move faster than big-"
                "city ones. The trolley stop &mdash; rail transit in a "
                "town this size &mdash; is the infrastructure fact "
                "most listings undersell.</p>"
            ),
        },
        {
            "anchor": "position",
            "question": "How central is Lemon Grove, actually?",
            "lead": (
                "Lemon Grove sits at the junction of SR-94 and SR-125 "
                "&mdash; the position that puts downtown San Diego, "
                "the South Bay and East County each one freeway away "
                "&mdash; and centrality, not size, is the "
                "community&rsquo;s structural argument."
            ),
            "body": (
                "<p>Commute claims deserve the same skepticism "
                "everywhere: the freeways are adjacent, and their "
                "peak-hour behavior is the real number. The trolley "
                "&mdash; Orange Line toward downtown &mdash; prices "
                "the alternative for anyone working along it.</p>"
            ),
        },
        {
            "anchor": "stock",
            "question": "What does the older Lemon Grove housing stock mean for an inspection?",
            "lead": (
                "Lemon Grove&rsquo;s houses are predominantly "
                "mid-century &mdash; 1940s through 1960s bungalows and "
                "ranches on usable lots &mdash; so inspections there "
                "concentrate on the era&rsquo;s systems: original "
                "panels, galvanized plumbing, sewer laterals and the "
                "permit status of decades of additions."
            ),
            "body": (
                "<p>Usable lots also make Lemon Grove a practical ADU "
                "candidate under state law &mdash; the same rules "
                "covered in <a href=\"/blog/adu-rules-san-diego-county-"
                "2026\">the ADU explainer</a> apply, with the "
                "city&rsquo;s own standards layered on. Check the "
                "specific parcel; the lot sizes here often clear the "
                "practical bar.</p>"
            ),
        },
    ],
})

# --------------------------------------------------------------------------
# Southwest Riverside County, added 2026-07-30 at client request. Same rules
# as everything above: structural facts only, no prices, no ratings, places
# and processes never people. Sources: city CFD/debt pages (see taxes.py
# entries), district boundary tools, county land-use records. The recurring
# theme is deliberate — mailing addresses cross jurisdiction lines here just
# as they cross district lines in San Diego County.
# --------------------------------------------------------------------------

GUIDES.update({
    "temecula": [
        {
            "anchor": "wine-country-jurisdiction",
            "question": "Is Wine Country part of the city of Temecula?",
            "lead": (
                "Temecula Valley Wine Country is not inside the city of "
                "Temecula: the vineyard district east of the city line is "
                "unincorporated Riverside County territory with Temecula "
                "mailing addresses, governed by the county&rsquo;s Wine "
                "Country policies rather than by city hall."
            ),
            "body": (
                "<p>The distinction decides practical things &mdash; which "
                "planning counter permits a project, whose short-term-rental "
                "rules apply, and which agency answers a zoning question. A "
                "&ldquo;Temecula&rdquo; address settles none of it; the "
                "parcel&rsquo;s jurisdiction does, and the county&rsquo;s "
                "and city&rsquo;s own maps are where to check.</p>"
            ),
        },
        {
            "anchor": "tvusd-reach",
            "question": "Does Temecula Valley Unified stop at the Temecula city line?",
            "lead": (
                "Temecula Valley Unified School District extends beyond the "
                "city of Temecula &mdash; the French Valley area to the "
                "north, with Winchester mailing addresses, feeds TVUSD "
                "schools &mdash; and the district&rsquo;s own boundary maps, "
                "not the city line, decide any specific address."
            ),
            "body": (
                "<p>The same reading applies in reverse for buyers "
                "comparing across the valley: a Murrieta-adjacent address "
                "does not by itself mean Murrieta Valley Unified. Districts "
                "publish attendance lookups, and the guide&rsquo;s standing "
                "advice holds &mdash; confirm the exact address with the "
                "district before an offer, not after.</p>"
            ),
        },
        {
            "anchor": "commute-south",
            "question": "What is the commute from Temecula into San Diego County?",
            "lead": (
                "Temecula sits at the top of the Interstate 15 corridor "
                "into San Diego County &mdash; roughly thirty miles north "
                "of Escondido &mdash; and the southbound run through the "
                "Rainbow and Fallbrook grades is the trade that buys "
                "Riverside County pricing on a San Diego County paycheck."
            ),
            "body": (
                "<p>The corridor is the connective tissue of this whole "
                "guide set: <a href=\"/neighborhoods/fallbrook\">"
                "Fallbrook</a> sits just over the county line to the "
                "southwest, and <a href=\"/neighborhoods/escondido\">"
                "Escondido</a> anchors the San Diego end of the same "
                "freeway. Peak-window congestion northbound in the evening "
                "is the honest cost to test-drive before committing to "
                "it.</p>"
            ),
        },
        {
            "anchor": "airport-noise",
            "question": "Does airplane noise affect north Temecula?",
            "lead": (
                "French Valley Airport sits just north of the Temecula "
                "city limits, and its traffic pattern crosses the northern "
                "tracts &mdash; a general-aviation field rather than a "
                "commercial airport, but audible, and worth visiting a "
                "specific street at different hours before an offer."
            ),
            "body": (
                "<p>Airport influence areas are mapped land-use facts, not "
                "matters of opinion: the county&rsquo;s airport land-use "
                "compatibility plans define them, and disclosure obligations "
                "attach near an airport. A buyer sensitive to overflight "
                "noise gets a better answer from an evening on the street "
                "than from any listing description.</p>"
            ),
        },
    ],
    "murrieta": [
        {
            "anchor": "la-cresta",
            "question": "Is La Cresta part of the city of Murrieta?",
            "lead": (
                "La Cresta and the Santa Rosa Plateau estates west of "
                "Interstate 15 carry Murrieta mailing addresses but sit in "
                "unincorporated Riverside County &mdash; large-acreage "
                "ranch parcels under county zoning, commonly on private "
                "wells and septic rather than city services."
            ),
            "body": (
                "<p>That makes the west-of-15 estates a different purchase "
                "from a Murrieta tract home in every way that costs money: "
                "well yield and septic condition need their own "
                "inspections, fire-zone insurance needs quoting early, and "
                "the county &mdash; not city hall &mdash; is the planning "
                "authority. The same rural checklist that governs "
                "<a href=\"/neighborhoods/valley-center\">Valley Center</a> "
                "and <a href=\"/neighborhoods/ramona\">Ramona</a> applies "
                "here.</p>"
            ),
        },
        {
            "anchor": "district-edges",
            "question": "Do all Murrieta addresses feed Murrieta Valley Unified schools?",
            "lead": (
                "A Murrieta mailing address does not guarantee Murrieta "
                "Valley Unified assignment: the postal city reaches into "
                "unincorporated French Valley, where addresses feed "
                "Temecula Valley Unified, and the district&rsquo;s own "
                "boundary maps decide every edge case."
            ),
            "body": (
                "<p>School assignment by mailing address is the single "
                "most repeated mistake in this valley, exactly as it is in "
                "San Diego County &mdash; the method for checking an "
                "address is the same one <a href=\"/blog/san-diego-school-"
                "district-by-address\">the school-district guide</a> "
                "teaches, applied to a different county&rsquo;s "
                "districts.</p>"
            ),
        },
        {
            "anchor": "i15-i215-split",
            "question": "Why does the I-15 / I-215 split matter in Murrieta?",
            "lead": (
                "Murrieta sits at the junction where Interstate 215 "
                "splits from Interstate 15, which makes it the "
                "corridor&rsquo;s hinge: the 15 runs south toward Temecula "
                "and San Diego County, the 215 north toward Menifee and "
                "Riverside, and commute direction is the practical "
                "difference between otherwise similar Murrieta tracts."
            ),
            "body": (
                "<p>A household commuting south cares about on-ramp "
                "position relative to the merge; one working north up the "
                "215 prices a different morning entirely. The split is "
                "also why Murrieta pairs naturally with "
                "<a href=\"/neighborhoods/menifee\">Menifee</a> in a "
                "search &mdash; same corridor, one freeway apart.</p>"
            ),
        },
        {
            "anchor": "new-districts",
            "question": "Are new Mello-Roos districts still being formed in Murrieta?",
            "lead": (
                "New community facilities districts are still being formed "
                "in Murrieta &mdash; the city noticed the Gierson Ranch "
                "district for bond authorization in 2026 &mdash; so a "
                "brand-new tract&rsquo;s special-tax load is set at "
                "formation, before the first home sells."
            ),
            "body": (
                "<p>For a new-construction buyer the sequence matters: the "
                "special tax exists before the sales office opens, it is "
                "disclosed in the purchase documents, and it is knowable "
                "to the dollar before contract. The Mello-Roos block above "
                "carries the district list and the city&rsquo;s own source "
                "for it.</p>"
            ),
        },
    ],
    "menifee": [
        {
            "anchor": "newest-city",
            "question": "When did Menifee become a city?",
            "lead": (
                "Menifee incorporated in 2008, making it one of Riverside "
                "County&rsquo;s newest cities &mdash; a municipal "
                "government younger than much of its housing stock, which "
                "is why districts formed under the county still appear on "
                "Menifee tax bills alongside the city&rsquo;s own."
            ),
            "body": (
                "<p>Incorporation date is not trivia here: it explains the "
                "layered special-district landscape the Mello-Roos block "
                "documents, and it explains why service questions &mdash; "
                "roads, lighting, landscape maintenance &mdash; route to "
                "different agencies depending on when a tract was "
                "built.</p>"
            ),
        },
        {
            "anchor": "three-districts",
            "question": "Why does Menifee span three school systems?",
            "lead": (
                "Menifee splits across school systems the way Escondido "
                "does: Menifee Union School District runs kindergarten "
                "through eighth grade for most of the city, Perris Union "
                "High School District runs the high schools, and the "
                "northern Romoland area is served by Romoland School "
                "District for the elementary years."
            ),
            "body": (
                "<p>Elementary and high-school assignment are therefore "
                "two separate questions with two separate answers, and a "
                "north-Menifee address needs the third check. The "
                "verification method is the same one that governs every "
                "guide on this site: the district office and the exact "
                "street address, never the city name.</p>"
            ),
        },
        {
            "anchor": "sun-city",
            "question": "What is Sun City, and is all of Menifee age-restricted?",
            "lead": (
                "Sun City is the historic core of Menifee &mdash; a Del "
                "Webb retirement development dating to the early 1960s "
                "&mdash; and its age-qualified communities operate under "
                "federal senior-housing rules, while most of modern "
                "Menifee is conventional all-ages housing."
            ),
            "body": (
                "<p>Age qualification is a recorded, community-specific "
                "legal status &mdash; not something to assume from the Sun "
                "City name in either direction. The governing documents "
                "state it, escrow discloses it, and a buyer or heir "
                "dealing with a specific property should verify that "
                "community&rsquo;s status rather than the "
                "neighborhood&rsquo;s reputation.</p>"
            ),
        },
        {
            "anchor": "water-sewer",
            "question": "Who provides water and sewer in Menifee?",
            "lead": (
                "Water and sewer service in Menifee comes from Eastern "
                "Municipal Water District rather than city hall, and EMWD "
                "participates in community facilities financing for new "
                "development &mdash; one more line on a new-construction "
                "tax bill that predates any individual buyer."
            ),
            "body": (
                "<p>On the corridor&rsquo;s newer tracts the practical "
                "consequence is a tax bill with city, school and water "
                "lines from three different agencies &mdash; each with its "
                "own contact, each answerable, none of them guessable "
                "from the listing. The Mello-Roos block above names the "
                "districts and sources.</p>"
            ),
        },
    ],
})


def for_hood(slug: str) -> list[dict]:
    """Extra answer blocks for a community, in page order. May be empty."""
    return GUIDES.get(slug, [])


def anchors(slug: str) -> list[str]:
    return [b["anchor"] for b in for_hood(slug)]
