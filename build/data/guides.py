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


def for_hood(slug: str) -> list[dict]:
    """Extra answer blocks for a community, in page order. May be empty."""
    return GUIDES.get(slug, [])


def anchors(slug: str) -> list[str]:
    return [b["anchor"] for b in for_hood(slug)]
