"""Blog posts.

Each post is a dict of the same shape the guides use — a dek, then a list of
answer blocks. The blocks are what an AI Mode sub-query actually retrieves, so
a post is written as a set of standalone answers rather than an essay with a
conclusion. Anything that only makes sense read top to bottom is a post that
gets skipped.

The bar for adding one: it must answer something the sixteen neighborhood
guides do not, or it is cannibalising them. A post that restates a guide
splits the signal for that query across two URLs and helps nobody.

Every factual claim traces to a named source — a school district, a county
office, a state agency. No market figures that go stale, no invented detail.
"""

from __future__ import annotations

POSTS: list[dict] = [
    {
        "slug": "san-diego-school-district-by-address",
        "title": "Your San Diego address does not tell you your school district",
        "dek": (
            "A Carlsbad home can feed Encinitas schools. A San Diego address "
            "can feed Del Mar Union. Scripps Ranch is not in Poway Unified. "
            "Here is where the boundaries actually cross in North San Diego "
            "County, and how to check yours before you make an offer."
        ),
        "date": "2026-07-25",
        "author": "nilab-azizi",
        "description": (
            "School district boundaries in North San Diego County cross city "
            "lines and ZIP codes. Which Carlsbad, Carmel Valley, Scripps "
            "Ranch and Encinitas addresses feed which districts — and how to "
            "verify a specific address."
        ),
        # Pre-wrapped to the rendered page's 6-space indentation; this string
        # must reproduce the disclaimer exactly as it shipped before the
        # footnote became per-post data.
        "footnote": (
            "      District boundaries are set by the districts themselves and are redrawn\n"
            "      from time to time. Every assignment above should be confirmed with the\n"
            "      district office for the specific address before it is relied on."
        ),
        "blocks": [
            {
                "anchor": "why-it-crosses",
                "question": "Why does my San Diego address feed a different city's school district?",
                "lead": (
                    "School district boundaries in San Diego County were "
                    "drawn independently of city boundaries and ZIP codes, "
                    "often decades earlier, and neither has been redrawn to "
                    "match the other since. A district is its own unit of "
                    "local government with its own elected board and its own "
                    "territory, and that territory routinely crosses city "
                    "lines in both directions."
                ),
                "body": (
                    "<p>The practical consequence is that the city on an "
                    "envelope predicts the school district poorly, and the "
                    "ZIP code predicts it worse. Buyers pay for school "
                    "assignment, so getting this wrong is expensive in both "
                    "directions &mdash; paying a premium for an assignment "
                    "that does not apply, or passing on a home that had the "
                    "one you wanted.</p>"
                ),
            },
            {
                "anchor": "carlsbad",
                "question": "Do all Carlsbad homes go to Carlsbad Unified?",
                "lead": (
                    "Not every Carlsbad home is assigned to Carlsbad Unified "
                    "School District. Homes in southern Carlsbad can be "
                    "assigned to Encinitas Union School District for "
                    "elementary and San Dieguito Union High School District "
                    "for secondary, and homes on the eastern edge can fall "
                    "into San Marcos Unified. A Carlsbad address does not by "
                    "itself determine the school."
                ),
                "body": (
                    "<p>This is the single most misjudged school question in "
                    "North San Diego County, and it moves real money. The "
                    "boundary follows neither the city line nor any of "
                    "Carlsbad&rsquo;s four ZIP codes. See the "
                    "<a href=\"/neighborhoods/carlsbad\">Carlsbad guide</a> "
                    "for how the four ZIPs otherwise differ.</p>"
                ),
            },
            {
                "anchor": "carmel-valley",
                "question": "Which district serves Carmel Valley if the address says San Diego?",
                "lead": (
                    "Much of Carmel Valley is served by Del Mar Union School "
                    "District for kindergarten through sixth grade and San "
                    "Dieguito Union High School District for grades seven "
                    "through twelve &mdash; despite the homes carrying City "
                    "of San Diego addresses. A San Diego address does not "
                    "mean San Diego Unified here."
                ),
                "body": (
                    "<p>Torrey Pines High School is a San Dieguito Union "
                    "school, and assignment to it is set by that "
                    "district&rsquo;s attendance areas rather than by being "
                    "in Carmel Valley at all. San Dieguito Union also runs a "
                    "school choice process, so the school a student is "
                    "assigned and the school a student attends are two "
                    "separate questions. More in the "
                    "<a href=\"/neighborhoods/carmel-valley\">Carmel Valley "
                    "guide</a>.</p>"
                ),
            },
            {
                "anchor": "scripps-ranch",
                "question": "Is Scripps Ranch in Poway Unified?",
                "lead": (
                    "Scripps Ranch is in San Diego Unified School District, "
                    "not Poway Unified &mdash; which catches buyers comparing "
                    "it against the 92127 communities a few miles north. "
                    "Scripps Ranch High School, Marshall Middle and the "
                    "community&rsquo;s elementary schools are all San Diego "
                    "Unified schools."
                ),
                "body": (
                    "<p>That fact also explains the tax difference people "
                    "notice between the two. Scripps Ranch carries no "
                    "community facilities district named for it in the County "
                    "Auditor&rsquo;s active list, while the Poway Unified "
                    "communities to the north carry several &mdash; different "
                    "district, different financing history, different bill. "
                    "See <a href=\"/mello-roos\">the Mello-Roos lookup</a>.</p>"
                ),
            },
            {
                "anchor": "cardiff",
                "question": "Does Cardiff-by-the-Sea have its own school district?",
                "lead": (
                    "Cardiff-by-the-Sea has its own separate elementary "
                    "district &mdash; the Cardiff School District &mdash; "
                    "even though it sits inside the City of Encinitas, where "
                    "the rest of the city is served by Encinitas Union School "
                    "District. Both then feed San Dieguito Union High School "
                    "District for grades seven through twelve."
                ),
                "body": (
                    "<p>So an Encinitas address involves two assignments to "
                    "verify, and which elementary district applies depends on "
                    "which of the city&rsquo;s five recognised communities the "
                    "parcel sits in. The "
                    "<a href=\"/neighborhoods/encinitas\">Encinitas guide</a> "
                    "covers all five.</p>"
                ),
            },
            {
                "anchor": "pusd-reach",
                "question": "How far does Poway Unified extend beyond the city of Poway?",
                "lead": (
                    "Poway Unified School District extends well beyond the "
                    "city of Poway, covering the 92127 communities of Del "
                    "Sur, 4S Ranch and the Black Mountain Ranch villages "
                    "&mdash; all of which carry City of San Diego addresses. "
                    "The district name describes its origin, not the limit of "
                    "its territory."
                ),
                "body": (
                    "<p>That reach is what makes the tax comparison worth "
                    "running. The district administers 19 active community "
                    "facilities districts, but the bulk of that load sits in "
                    "the newer 92127 communities rather than in the older "
                    "city of Poway, which was largely built before those "
                    "districts were formed. Same schools, materially "
                    "different monthly cost &mdash; see the "
                    "<a href=\"/neighborhoods/poway\">Poway guide</a>.</p>"
                ),
            },
            {
                "anchor": "escondido-two",
                "question": "Why does Escondido have two school districts?",
                "lead": (
                    "Escondido is served by two separate districts rather "
                    "than one unified district: Escondido Union School "
                    "District runs kindergarten through eighth grade, and "
                    "Escondido Union High School District runs ninth through "
                    "twelfth. Elementary and high school assignment are "
                    "therefore two different questions with two different "
                    "answers."
                ),
                "body": (
                    "<p>Outlying addresses complicate it further &mdash; "
                    "homes with Escondido mailing addresses on the eastern "
                    "and northern edges can fall into San Pasqual Union, "
                    "Valley Center-Pauma Unified or Bonsall Unified instead. "
                    "Fallbrook has the same two-tier structure, with Fallbrook "
                    "Union Elementary and Fallbrook Union High as separate "
                    "districts.</p>"
                ),
            },
            {
                "anchor": "how-to-check",
                "question": "How do I check the school district for a specific San Diego address?",
                "lead": (
                    "Confirm a San Diego County address with the district "
                    "office directly, using the full street address rather "
                    "than the city or ZIP code. Districts publish attendance "
                    "area lookups and will answer by phone, and their answer "
                    "is the only one that counts &mdash; a portal listing, a "
                    "listing description and a school-rating site are all "
                    "downstream of it and all go stale."
                ),
                "body": (
                    "<p>Two further cautions. Attendance areas are redrawn "
                    "from time to time, so an answer from three years ago is "
                    "not an answer now. And where a district runs a school "
                    "choice process, being assigned to a school and getting "
                    "into it are different things &mdash; ask how the process "
                    "works before treating an assignment as guaranteed.</p>"
                    "<p>Every <a href=\"/neighborhoods\">neighborhood "
                    "guide</a> states which districts serve that community "
                    "and where the boundaries are known to cross.</p>"
                ),
            },
        ],
    },
    # ------------------------------------------------------------------
    # 2026-07-30 batch. Topics from community listening pass #1
    # (research/communityVoice.md); every regulatory fact below was traced
    # to its primary source before writing — CDI-approved rate filing as
    # reported at approval, cfpnet.com's own program description, AB 976 and
    # AB 1033 at leginfo, and the County's ADU ordinance page — per the
    # runbook rule that no secondary-source number ships.
    # ------------------------------------------------------------------
    {
        "slug": "california-fair-plan-san-diego",
        "title": (
            "The California FAIR Plan, explained for San Diego homeowners "
            "— before the October 15 rate change"
        ),
        "dek": (
            "Admitted carriers have narrowed what they write in the "
            "county&rsquo;s fire-hazard zones, and more San Diego households "
            "are landing on the state&rsquo;s insurer of last resort &mdash; "
            "right as its rates change on October 15, 2026. What the FAIR "
            "Plan actually covers, what it doesn&rsquo;t, and the sequence "
            "that keeps an escrow alive."
        ),
        "date": "2026-07-30",
        "author": "nilab-azizi",
        "description": (
            "What the California FAIR Plan covers, what changes with the "
            "rate plan effective October 15, 2026, which San Diego County "
            "communities rely on it, and how buyers and sellers in "
            "fire-hazard zones should sequence insurance."
        ),
        "footnote": (
            "      Insurance program terms and rates are set by carriers, the FAIR Plan\n"
            "      and the California Department of Insurance, and change with regulatory\n"
            "      action; figures above are as of the dates cited. A licensed insurance\n"
            "      broker is the source of a real quote for a specific address &mdash;\n"
            "      Team Azizi is a real estate team, not an insurance broker."
        ),
        "blocks": [
            {
                "anchor": "what-is-fair-plan",
                "question": "What is the California FAIR Plan?",
                "lead": (
                    "The California FAIR Plan is the state&rsquo;s statutory "
                    "insurer of last resort for basic property insurance "
                    "&mdash; the pool that writes fire coverage when admitted "
                    "carriers decline a property, which in San Diego County "
                    "increasingly means backcountry and canyon-edge homes."
                ),
                "body": (
                    "<p>The plan is an association of the licensed property "
                    "insurers doing business in California, created by "
                    "statute &mdash; not a state agency and not "
                    "taxpayer-funded. Policies are sold through licensed "
                    "brokers, and eligibility is not means-tested: the "
                    "qualifying condition is that the ordinary market will "
                    "not write the risk. The plan&rsquo;s own description of "
                    "its role is blunt &mdash; basic property insurance for "
                    "high-risk properties, owner- or tenant-occupied "
                    "dwellings of up to four units.</p>"
                ),
            },
            {
                "anchor": "not-homeowners-insurance",
                "question": (
                    "Does the FAIR Plan cover the same things as regular "
                    "homeowners insurance?"
                ),
                "lead": (
                    "A FAIR Plan dwelling policy is fire coverage, not the "
                    "full homeowners package a San Diego household and its "
                    "lender normally rely on &mdash; liability, theft, water "
                    "damage and loss-of-use protection are not part of it."
                ),
                "body": (
                    "<p>The plan itself points policyholders at the companion "
                    "product that fills the gap: a difference-in-conditions "
                    "policy, written by a separate carrier, that layers the "
                    "missing coverages back on. Priced together, FAIR Plan "
                    "plus DIC generally costs materially more than the "
                    "standard policy it replaces &mdash; which is why the "
                    "combination belongs in a buyer&rsquo;s affordability "
                    "math from the first showing rather than surfacing in "
                    "escrow. The <a href=\"/neighborhoods/fallbrook\">"
                    "Fallbrook</a>, <a href=\"/neighborhoods/valley-center\">"
                    "Valley Center</a> and <a href=\"/neighborhoods/ramona\">"
                    "Ramona</a> guides carry the per-community picture.</p>"
                ),
            },
            {
                "anchor": "october-15-change",
                "question": (
                    "What changes for FAIR Plan policyholders on October 15, "
                    "2026?"
                ),
                "lead": (
                    "FAIR Plan dwelling policies across California, San "
                    "Diego County included, price under a newly approved "
                    "rate plan when written or renewed on or after October "
                    "15, 2026 &mdash; the Department of Insurance granted an "
                    "overall 29.1% increase, scaled by wildfire risk, after "
                    "the plan requested 35.8%."
                ),
                "body": (
                    "<p>Scaled by risk means the increase is not uniform: "
                    "parcels with significant wildfire exposure carry more "
                    "of it, and some lower-risk policyholders will see "
                    "decreases. For an owner already on the plan, the "
                    "renewal date decides when the new rates arrive. For a "
                    "buyer writing offers in a fire-hazard zone this fall, a "
                    "quote gathered in September can be stale by close "
                    "&mdash; ask the broker to price against the effective "
                    "date, not the application date.</p>"
                ),
            },
            {
                "anchor": "which-communities",
                "question": (
                    "Which San Diego County communities rely on the FAIR "
                    "Plan most?"
                ),
                "lead": (
                    "FAIR Plan placement in San Diego County concentrates "
                    "where admitted carriers have pulled back hardest: the "
                    "backcountry and its edges &mdash; Fallbrook, Valley "
                    "Center, Ramona, the rural fringes of Escondido &mdash; "
                    "plus canyon-adjacent pockets of otherwise suburban "
                    "communities like Scripps Ranch and 4S Ranch."
                ),
                "body": (
                    "<p>The direction of travel is statewide and documented: "
                    "Stanford researchers put the FAIR Plan at roughly 5% of "
                    "California&rsquo;s single-family homes as of March "
                    "2026, up from 1.5% at the end of 2020. Address matters "
                    "more than community name &mdash; two homes a street "
                    "apart can sit on different sides of a fire hazard "
                    "severity zone line, and CAL&nbsp;FIRE&rsquo;s "
                    "parcel-level maps plus the property&rsquo;s own "
                    "insurance history are the checkable facts. The "
                    "<a href=\"/neighborhoods/scripps-ranch\">Scripps "
                    "Ranch</a> and <a href=\"/neighborhoods/4s-ranch\">4S "
                    "Ranch</a> guides cover how the canyon edges behave.</p>"
                ),
            },
            {
                "anchor": "buyer-sequence",
                "question": (
                    "How should a San Diego buyer sequence insurance in a "
                    "fire-hazard zone?"
                ),
                "lead": (
                    "Insurance on a fire-zone San Diego property is a "
                    "funding condition, not a closing formality &mdash; the "
                    "workable sequence is a hazard-map lookup before the "
                    "offer, a real quote on the address inside the "
                    "inspection contingency, and bound coverage confirmed "
                    "well before the loan funds."
                ),
                "body": (
                    "<p>Three steps, each checkable: look the parcel up on "
                    "CAL&nbsp;FIRE&rsquo;s fire hazard severity zone maps "
                    "before writing; ask the listing side for the current "
                    "carrier and premium &mdash; an existing admitted policy "
                    "that will re-write for a new owner is worth real money; "
                    "and if the answer comes back FAIR Plan plus DIC, price "
                    "that combination into the affordability decision while "
                    "the contingency still allows a clean exit. A lender "
                    "will not fund without bound coverage, which makes a "
                    "late insurance surprise an escrow-ending event rather "
                    "than a budgeting nuisance.</p>"
                ),
            },
            {
                "anchor": "seller-prep",
                "question": (
                    "What should a San Diego seller in a fire zone prepare "
                    "before listing?"
                ),
                "lead": (
                    "A San Diego seller in a designated fire-hazard zone "
                    "should assemble the property&rsquo;s insurance story "
                    "before the sign goes up: the current carrier and "
                    "premium, the defensible-space condition, and the "
                    "hardening work &mdash; roof class, vents, clearance "
                    "&mdash; a buyer&rsquo;s carrier will ask about."
                ),
                "body": (
                    "<p>Buyers do not walk from fire-zone homes because "
                    "coverage exists at a price; escrows die when the price "
                    "arrives late and unexplained. A listing that can state "
                    "&ldquo;currently insured with an admitted carrier&rdquo; "
                    "or &ldquo;quoted FAIR Plan plus DIC at a known "
                    "figure&rdquo; converts the county&rsquo;s hardest "
                    "objection into an underwriting fact the buyer can "
                    "verify &mdash; and the prep list doubles as the "
                    "checklist carriers use to decide what they will "
                    "write.</p>"
                ),
            },
        ],
    },
    {
        "slug": "selling-a-house-with-solar-panels-san-diego",
        "title": (
            "Selling a house with solar panels in San Diego: the contract "
            "is the deal"
        ),
        "dek": (
            "California has required solar on new homes since 2020, and "
            "North County&rsquo;s newer tracts were dense with it long "
            "before that &mdash; so the sale of a solar home runs on the "
            "paperwork behind the panels: owned or leased, net-metering "
            "vintage, and a recorded lien most sellers have never heard "
            "of. What to assemble before listing, and what buyers should "
            "read before assuming a payment."
        ),
        "date": "2026-07-30",
        "author": "sofia-azizi",
        "description": (
            "How solar panels affect a San Diego home sale: owned versus "
            "leased systems, lease assumption in escrow, the UCC-1 fixture "
            "filing, legacy net-metering transfer, and what sellers should "
            "disclose."
        ),
        "footnote": (
            "      Solar agreements are contract- and vintage-specific, and utility\n"
            "      tariff terms are set by the CPUC and SDG&amp;E. The lease document, the\n"
            "      lessor&rsquo;s transfer desk, SDG&amp;E and escrow/title are the\n"
            "      authorities for a specific home; nothing above substitutes for them."
        ),
        "blocks": [
            {
                "anchor": "owned-or-leased",
                "question": (
                    "Does it matter whether the solar panels are owned or "
                    "leased when selling a house?"
                ),
                "lead": (
                    "Ownership is the first fact to establish in any San "
                    "Diego solar-home sale: an owned system transfers with "
                    "the house like any other fixture, while a leased system "
                    "or power-purchase agreement is a running contract the "
                    "buyer must qualify for and formally assume."
                ),
                "body": (
                    "<p>Everything downstream &mdash; disclosure, escrow "
                    "timeline, even the buyer&rsquo;s loan approval &mdash; "
                    "branches on that fact. The governing document is the "
                    "original purchase or lease agreement; when it cannot be "
                    "found, the company named on the monthly statement will "
                    "reissue it. Leased systems resolve one of three ways in "
                    "a sale: the buyer assumes the lease, someone prepays or "
                    "buys out the remaining term, or the seller pays it off "
                    "and sells the system as owned.</p>"
                ),
            },
            {
                "anchor": "lease-assumption",
                "question": (
                    "How does a solar lease transfer to the buyer in escrow?"
                ),
                "lead": (
                    "A solar lease on a San Diego home transfers through the "
                    "lessor&rsquo;s own assignment process &mdash; typically "
                    "a credit application from the buyer and a signed "
                    "transfer agreement &mdash; and the lessor works on its "
                    "own timeline, not escrow&rsquo;s."
                ),
                "body": (
                    "<p>Starting the transfer at offer acceptance rather "
                    "than mid-escrow is the difference between a non-event "
                    "and a delayed closing. Two details deserve early "
                    "attention: the buyer&rsquo;s lender counts the lease "
                    "payment in debt-to-income, which can move a marginal "
                    "approval, and many leases carry annual escalator "
                    "clauses &mdash; the payment a buyer assumes in year "
                    "eight is not the year-one number on the brochure.</p>"
                ),
            },
            {
                "anchor": "ucc-1",
                "question": (
                    "What is the UCC-1 filing that shows up in a title "
                    "search on a solar home?"
                ),
                "lead": (
                    "Leased and loan-financed solar systems in San Diego "
                    "County commonly appear in the title search as a UCC-1 "
                    "fixture filing &mdash; the financing party&rsquo;s "
                    "recorded interest in the equipment &mdash; and escrow "
                    "needs it released or subordinated before the sale "
                    "closes."
                ),
                "body": (
                    "<p>The filing is routine and resolvable, but not "
                    "automatic: someone has to request the release or "
                    "subordination package from the lessor, and the request "
                    "should go out when escrow opens. A buyout or payoff "
                    "removes the filing entirely. Sellers who first discover "
                    "the UCC-1 in the buyer&rsquo;s title report have "
                    "usually lost a week to it.</p>"
                ),
            },
            {
                "anchor": "net-metering",
                "question": (
                    "Do the old net-metering rates transfer to the buyer of "
                    "a solar home?"
                ),
                "lead": (
                    "Net-metering status on a San Diego home belongs to the "
                    "system and the property rather than the person: a house "
                    "interconnected under an earlier NEM tariff keeps its "
                    "legacy billing terms for the remainder of the legacy "
                    "period after a sale, and SDG&amp;E can confirm the "
                    "remaining term for a specific address."
                ),
                "body": (
                    "<p>The clock runs from the system&rsquo;s original "
                    "interconnection date, not from the sale. The "
                    "distinction is worth real money in a listing: homes "
                    "under the current Solar Billing Plan are credited for "
                    "exports very differently, with batteries carrying more "
                    "of the value. &ldquo;Owned system, legacy net metering, "
                    "term confirmed with SDG&amp;E&rdquo; is a checkable "
                    "claim a buyer&rsquo;s agent can verify with the utility "
                    "&mdash; which is exactly what makes it worth stating "
                    "precisely, and nothing more.</p>"
                ),
            },
            {
                "anchor": "disclosure",
                "question": (
                    "What does a seller disclose about a solar system in a "
                    "San Diego sale?"
                ),
                "lead": (
                    "A San Diego seller&rsquo;s solar disclosure is the "
                    "contract itself and its live terms &mdash; lease or "
                    "ownership, monthly payment and any escalator, remaining "
                    "term, transfer requirements, and any performance "
                    "guarantee &mdash; assembled into the disclosure package "
                    "rather than summarized from memory."
                ),
                "body": (
                    "<p>The buyer is stepping into those terms, and the "
                    "transaction moves at the speed of the documents. A "
                    "seller who gathers the agreement, the last twelve "
                    "months of statements and the lessor&rsquo;s transfer "
                    "requirements before listing has answered, in advance, "
                    "every question that otherwise arrives as a "
                    "repair-request-shaped surprise in week three. The "
                    "<a href=\"/sell\">selling page</a> covers where this "
                    "fits in the broader prep.</p>"
                ),
            },
            {
                "anchor": "price-effect",
                "question": (
                    "Do solar panels change what a San Diego home sells for?"
                ),
                "lead": (
                    "A solar system&rsquo;s effect on a San Diego sale price "
                    "tracks the contract behind it: an owned system with "
                    "legacy net metering reads to buyers as a verifiable "
                    "utility-cost reduction, while a leased system is a "
                    "payment obligation the buyer must qualify to assume "
                    "&mdash; the market prices the paperwork, not the "
                    "panels."
                ),
                "body": (
                    "<p>California&rsquo;s building code has required solar "
                    "on new homes since 2020, so the newer tracts of "
                    "Escondido, San Marcos and the 92127 communities put "
                    "both kinds of system in most comparison sets &mdash; "
                    "and the honest pricing conversation uses those comps "
                    "rather than a rule of thumb. The "
                    "<a href=\"/neighborhoods/escondido\">Escondido</a> and "
                    "<a href=\"/neighborhoods/san-marcos\">San Marcos</a> "
                    "guides cover the communities where this arises "
                    "most.</p>"
                ),
            },
        ],
    },
    {
        "slug": "adu-rules-san-diego-county-2026",
        "title": (
            "An ADU can now be sold separately in San Diego County's "
            "unincorporated communities"
        ),
        "dek": (
            "The County adopted AB 1033 in March 2026: an accessory "
            "dwelling unit in Fallbrook, Valley Center, Ramona and the "
            "rest of the unincorporated county can be converted to a "
            "condominium and sold on its own. What the ordinance actually "
            "allows, where it does not apply, and the parcel-level facts "
            "that decide whether a backcountry ADU pencils."
        ),
        "date": "2026-07-30",
        "author": "zohra-azizi",
        "description": (
            "San Diego County ADU rules in 2026: the AB 1033 separate-sale "
            "ordinance for unincorporated communities (effective April 4, "
            "2026), owner-occupancy under AB 976, city-versus-county "
            "jurisdiction, and the septic, well and insurance math on "
            "rural parcels."
        ),
        "footnote": (
            "      Zoning and ADU standards are jurisdiction-specific and under active\n"
            "      revision. Ordinance details above are as adopted by the County of San\n"
            "      Diego on March 4, 2026 (effective April 4, 2026); the planning\n"
            "      department for the parcel&rsquo;s actual jurisdiction is the authority\n"
            "      for any specific project."
        ),
        "blocks": [
            {
                "anchor": "separate-sale",
                "question": (
                    "Can you sell an ADU separately from the main house in "
                    "San Diego County?"
                ),
                "lead": (
                    "San Diego County&rsquo;s Board of Supervisors voted on "
                    "March 4, 2026 to implement AB 1033, and since April 4, "
                    "2026 an accessory dwelling unit in the county&rsquo;s "
                    "unincorporated communities can be sold separately from "
                    "the primary home through a condominium conversion."
                ),
                "body": (
                    "<p>The mechanics are real-property mechanics, not a "
                    "shortcut: the conversion runs through the Subdivision "
                    "Map Act and the Davis-Stirling common-interest "
                    "framework, existing lienholders must consent, and the "
                    "County publishes an ADU condo guidance checklist for "
                    "determining whether a specific project qualifies. The "
                    "Board also directed staff to develop first-time-"
                    "homebuyer and owner-occupancy options, which went to "
                    "the Planning Commission in June 2026 &mdash; the "
                    "program is young and still moving.</p>"
                ),
            },
            {
                "anchor": "city-vs-county",
                "question": (
                    "Does the ADU separate-sale rule apply inside San Diego "
                    "city limits?"
                ),
                "lead": (
                    "The County of San Diego&rsquo;s separate-sale ordinance "
                    "covers only unincorporated territory &mdash; Fallbrook, "
                    "Valley Center, Ramona and communities like them &mdash; "
                    "while an address inside the city of San Diego, "
                    "Escondido, Oceanside, Carlsbad or any other "
                    "incorporated city follows that city&rsquo;s own ADU "
                    "rules."
                ),
                "body": (
                    "<p>AB 1033 is opt-in: a city has to pass its own "
                    "ordinance before an ADU there can be sold separately, "
                    "so the answer changes at the city line rather than the "
                    "mailing address. The trap that runs through school "
                    "districts runs through zoning too &mdash; a "
                    "&ldquo;Fallbrook&rdquo; or &ldquo;Escondido&rdquo; "
                    "mailing address does not say which jurisdiction "
                    "governs the parcel. The planning department that "
                    "issues the permit is the authority, and "
                    "<a href=\"/blog/san-diego-school-district-by-address\">"
                    "the same verify-the-actual-boundary habit</a> serves "
                    "buyers in both cases.</p>"
                ),
            },
            {
                "anchor": "owner-occupancy",
                "question": (
                    "Do you have to live on the property to rent out an ADU "
                    "in San Diego?"
                ),
                "lead": (
                    "California law bars local agencies from imposing "
                    "owner-occupancy requirements on accessory dwelling "
                    "units &mdash; AB 976 made the prohibition permanent in "
                    "October 2023 &mdash; so a San Diego ADU can be built "
                    "and rented without the owner living in either unit."
                ),
                "body": (
                    "<p>One boundary survives: local agencies may still "
                    "require rental terms of 30 days or longer, so an ADU "
                    "is not automatically a short-term rental. Reading the "
                    "owner-occupancy rule and the separate-sale ordinance "
                    "together shows what changed in 2026: an ADU in the "
                    "unincorporated county is no longer only a rental "
                    "income stream &mdash; it is a unit that can eventually "
                    "be sold on its own, which changes what the "
                    "construction cost buys.</p>"
                ),
            },
            {
                "anchor": "rural-math",
                "question": (
                    "Why is the ADU math different in Fallbrook, Valley "
                    "Center and Ramona?"
                ),
                "lead": (
                    "Large unincorporated parcels in Fallbrook, Valley "
                    "Center and Ramona clear the space constraints that "
                    "pinch suburban ADUs, but the same parcels bring septic "
                    "capacity, well yield and fire-zone insurance into the "
                    "equation &mdash; costs that do not exist on a sewered "
                    "city lot."
                ),
                "body": (
                    "<p>A septic system is sized to bedroom count, and an "
                    "added dwelling can trigger an upgraded or second "
                    "system; a shared well&rsquo;s yield has to support the "
                    "added household; and insuring a second structure in a "
                    "fire hazard severity zone runs into the same narrowed "
                    "market covered in <a href=\"/blog/california-fair-plan-"
                    "san-diego\">the FAIR Plan explainer</a>. None of these "
                    "kills a project, and all of them are quantifiable "
                    "before design money is spent. The "
                    "<a href=\"/neighborhoods/fallbrook\">Fallbrook</a>, "
                    "<a href=\"/neighborhoods/valley-center\">Valley "
                    "Center</a> and <a href=\"/neighborhoods/ramona\">"
                    "Ramona</a> guides carry the parcel-level land-use "
                    "picture.</p>"
                ),
            },
            {
                "anchor": "first-steps",
                "question": (
                    "How do you check what ADU rules apply to a specific "
                    "San Diego parcel?"
                ),
                "lead": (
                    "An ADU&rsquo;s real constraints in San Diego County are "
                    "parcel-level facts &mdash; jurisdiction, zoning, sewer "
                    "or septic, fire hazard designation &mdash; and every "
                    "one of them is checkable at the planning counter "
                    "before any money is spent."
                ),
                "body": (
                    "<p>Establish the jurisdiction first, because it "
                    "decides which ordinance governs and whether separate "
                    "sale is even on the table. Then the parcel&rsquo;s "
                    "zoning layer, the wastewater answer, and the fire "
                    "designation, in that order &mdash; each narrows the "
                    "design space and the budget before an architect is "
                    "engaged. For unincorporated parcels, the County&rsquo;s "
                    "ADU condo checklist states the separate-sale "
                    "eligibility conditions in full.</p>"
                ),
            },
        ],
    },
    # ------------------------------------------------------------------
    # 2026-07-30 batch #2 — the foundation-before-DNS build-out (client
    # direction). Payoff mechanics anchored to the Mello-Roos Act and the
    # district administrators already named in taxes.py; market figures are
    # SDAR's published June 2026 indicators, dated and attributed; rail
    # facts are SANDAG's published LOSSAN realignment materials.
    # ------------------------------------------------------------------
    {
        "slug": "mello-roos-payoff-early",
        "title": (
            "Paying off Mello-Roos early: how it works in San Diego County"
        ),
        "dek": (
            "The tax bill names the district; the district&rsquo;s own "
            "formation documents decide whether an early payoff exists and "
            "on what terms. How a payoff quote is obtained, what it removes "
            "from the bill and what it doesn&rsquo;t, and the three moments "
            "when the arithmetic is worth running."
        ),
        "date": "2026-07-30",
        "author": "sofia-azizi",
        "description": (
            "Whether Mello-Roos can be paid off early in San Diego County, "
            "how to get a parcel-specific payoff quote from the district "
            "administrator, why the services component survives a payoff, "
            "and when the math is worth running."
        ),
        "footnote": (
            "      Prepayment terms are set by each district&rsquo;s formation documents\n"
            "      and quoted by its administrator; tax consequences vary by owner. The\n"
            "      payoff decision is a numbers decision to run with the\n"
            "      administrator&rsquo;s quote and a tax professional &mdash; nothing above\n"
            "      is tax advice."
        ),
        "blocks": [
            {
                "anchor": "can-you-prepay",
                "question": (
                    "Can you pay off Mello-Roos early in San Diego County?"
                ),
                "lead": (
                    "Early payoff of a Mello-Roos special tax is possible in "
                    "San Diego County when the district&rsquo;s own formation "
                    "documents provide for it &mdash; the Mello-Roos "
                    "Community Facilities Act lets a district offer "
                    "prepayment, and each district&rsquo;s rate-and-method "
                    "decides whether, and on what terms."
                ),
                "body": (
                    "<p>Prepayment is therefore a district fact, not a "
                    "countywide rule: some rate-and-method documents "
                    "publish a full payoff formula, some allow partial "
                    "prepayment, and some provide none at all. The "
                    "governing document travels with the district, and the "
                    "administrator who levies the tax is the party who "
                    "states what applies to a given parcel. "
                    "<a href=\"/mello-roos\">The Mello-Roos lookup</a> "
                    "covers which districts operate in which "
                    "communities.</p>"
                ),
            },
            {
                "anchor": "payoff-quote",
                "question": "How do you get a Mello-Roos payoff quote?",
                "lead": (
                    "A payoff quote for a San Diego County parcel comes "
                    "from the district&rsquo;s administrator: the "
                    "Mello-Roos line on the property tax bill names the "
                    "district and a contact number, and that administrator "
                    "produces the parcel-specific payoff figure on request."
                ),
                "body": (
                    "<p>Parcel-specific is the operative word &mdash; the "
                    "figure depends on the district, the improvement area "
                    "and the phase the home was built in, which is why two "
                    "similar homes on one street can carry different "
                    "quotes. In the 92127 communities, the Poway Unified "
                    "districts that cover <a href=\"/neighborhoods/"
                    "del-sur\">Del Sur</a> and <a href=\"/neighborhoods/"
                    "4s-ranch\">4S Ranch</a> are handled by a named "
                    "administrator whose number appears on the bill "
                    "itself. Treat the quote like a loan payoff demand: "
                    "dated, expiring, and the only figure worth acting "
                    "on.</p>"
                ),
            },
            {
                "anchor": "what-payoff-removes",
                "question": (
                    "Does an early payoff remove the whole Mello-Roos line "
                    "from the tax bill?"
                ),
                "lead": (
                    "An early payoff on a San Diego County parcel retires "
                    "the bond-funded portion of the Mello-Roos levy, and "
                    "only that portion &mdash; many districts also levy a "
                    "services component for ongoing maintenance that does "
                    "not prepay and stays on the bill."
                ),
                "body": (
                    "<p>The <a href=\"/neighborhoods/del-sur#cfd-term\">"
                    "Del Sur guide</a> draws the same distinction about "
                    "district end dates, and it binds payoffs equally: ask "
                    "the administrator to split the quote into its bond "
                    "and services parts before treating a payoff as "
                    "removing the line item. A payoff that retires the "
                    "bonds and leaves a services charge is still worth "
                    "understanding &mdash; it is just a different number "
                    "than the bill&rsquo;s total suggests.</p>"
                ),
            },
            {
                "anchor": "resale-effect",
                "question": (
                    "Does paying off Mello-Roos change what a home sells "
                    "for?"
                ),
                "lead": (
                    "A paid-off Mello-Roos parcel in San Diego County "
                    "competes on total monthly cost: two otherwise similar "
                    "homes in the same community can carry materially "
                    "different special-tax lines, and buyers comparing "
                    "payment to payment see the difference directly."
                ),
                "body": (
                    "<p>Escrow surfaces the fact on its own &mdash; the "
                    "special-tax disclosure and the preliminary report "
                    "both carry it &mdash; so a documented payoff is a "
                    "checkable listing claim rather than marketing. "
                    "Whether the capital spent on a payoff comes back in "
                    "the sale price is a pricing question to run against "
                    "actual comparable sales, not a promise; what the "
                    "payoff verifiably changes is the monthly figure a "
                    "buyer&rsquo;s lender underwrites.</p>"
                ),
            },
            {
                "anchor": "when-to-run",
                "question": (
                    "When is the Mello-Roos payoff math worth running?"
                ),
                "lead": (
                    "The payoff arithmetic on a San Diego County parcel "
                    "earns its half hour at three moments: before listing "
                    "a home whose special-tax line makes buyers hesitate, "
                    "during a refinance when funds are already moving, and "
                    "at purchase when a seller credit could retire the "
                    "levy instead of buying down the rate."
                ),
                "body": (
                    "<p>Each is the same comparison &mdash; the "
                    "administrator&rsquo;s payoff quote against what the "
                    "same capital does elsewhere &mdash; run with real "
                    "numbers rather than the neighborhood&rsquo;s folklore "
                    "about what Mello-Roos costs. The inputs are one phone "
                    "call and one tax conversation, and the answer differs "
                    "by parcel, which is precisely why no blanket "
                    "recommendation appears here.</p>"
                ),
            },
        ],
    },
    {
        "slug": "north-county-market-pulse",
        "title": (
            "North County market pulse: what the mid-2026 numbers actually "
            "say"
        ),
        "dek": (
            "More homes for sale than at any point since 2020, and still "
            "not enough to tip the market. The June 2026 read from the "
            "REALTORS&rsquo; association&rsquo;s published indicators, "
            "what it means on each side of a deal, and why a single "
            "month&rsquo;s median deserves suspicion. Revised as new "
            "months publish."
        ),
        "date": "2026-07-30",
        "author": "sofia-azizi",
        "description": (
            "San Diego housing market, mid-2026: SDAR's June indicators — "
            "$950,000 combined median (+4.4% YoY), 3.2 months of supply, "
            "new listings down — and what the numbers mean for North "
            "County buyers and sellers."
        ),
        "footnote": (
            "      Market figures are the Greater San Diego Association of\n"
            "      REALTORS&rsquo; published monthly indicators as of the revision date\n"
            "      shown, quoted with their definitions; they describe the county-level\n"
            "      market, not any specific home. Figures are replaced, not\n"
            "      accumulated, as new months publish."
        ),
        "blocks": [
            {
                "anchor": "where-market-sits",
                "question": (
                    "Where does the San Diego housing market sit in "
                    "mid-2026?"
                ),
                "lead": (
                    "The San Diego market in mid-2026 is tighter than the "
                    "inventory headlines suggest: the Greater San Diego "
                    "Association of REALTORS&rsquo; June 2026 indicators "
                    "put the combined median sale price at $950,000, up "
                    "4.4% year over year, with detached homes at "
                    "$1,125,000 (up 5.1%) and attached homes at $670,000 "
                    "(up 1.1%)."
                ),
                "body": (
                    "<p>Every figure above is the association&rsquo;s "
                    "published series, quoted with its definitions and "
                    "dated &mdash; which matters, because market numbers "
                    "circulate stripped of both. Prices firmed while "
                    "supply grew, and holding those two facts together, "
                    "rather than picking one, is the honest read of "
                    "mid-2026.</p>"
                ),
            },
            {
                "anchor": "inventory-up",
                "question": (
                    "Is San Diego housing inventory actually improving in "
                    "2026?"
                ),
                "lead": (
                    "San Diego County carries more months of housing "
                    "supply in 2026 than at any point since 2020 &mdash; "
                    "roughly 3.2 months &mdash; and that is still barely "
                    "half of the six months conventionally treated as a "
                    "balanced market."
                ),
                "body": (
                    "<p>Both halves are true at once: buyers have more "
                    "choice than in any recent year, and the market has "
                    "stepped down from its sellers&rsquo;-market extremes "
                    "without tipping into a buyers&rsquo; market. The "
                    "supply side explains why &mdash; new listings fell "
                    "13.9% in June, and first-half detached listings ran "
                    "11.6% below last year, consistent with owners holding "
                    "low-rate mortgages staying put.</p>"
                ),
            },
            {
                "anchor": "sellers",
                "question": (
                    "What do the mid-2026 numbers mean for a North County "
                    "seller?"
                ),
                "lead": (
                    "A North County seller in mid-2026 faces more "
                    "competition than the 2021&ndash;2024 market supplied "
                    "and less than a balanced market would: pricing "
                    "against current comparable sales, rather than against "
                    "a neighbor&rsquo;s 2024 result, is what the supply "
                    "numbers reward."
                ),
                "body": (
                    "<p>With alternatives on the market, buyers can afford "
                    "to penalise the fixable &mdash; condition, "
                    "presentation, and the paperwork problems that surface "
                    "late. The two that kill North County escrows in the "
                    "final week are insurance and solar documentation, "
                    "both preparable in advance: see "
                    "<a href=\"/blog/california-fair-plan-san-diego\">the "
                    "FAIR Plan explainer</a> and <a href=\"/blog/"
                    "selling-a-house-with-solar-panels-san-diego\">the "
                    "solar-sale guide</a>.</p>"
                ),
            },
            {
                "anchor": "buyers",
                "question": (
                    "What do the mid-2026 numbers mean for a North County "
                    "buyer?"
                ),
                "lead": (
                    "A North County buyer in mid-2026 has more homes to "
                    "choose from than in any recent year and still little "
                    "pricing leverage on the well-presented ones &mdash; "
                    "3.2 months of supply rations patience, not price."
                ),
                "body": (
                    "<p>Leverage concentrates on the homes with a story: "
                    "condition issues, a solar lease mid-transfer, an "
                    "insurance bill that scared two earlier buyers off. "
                    "Those stories are checkable facts rather than "
                    "reasons to walk, and a buyer who can price a fire "
                    "zone or a lease assumption calmly &mdash; the "
                    "homework in the posts above &mdash; is bidding where "
                    "the competition thins out.</p>"
                ),
            },
            {
                "anchor": "median-caution",
                "question": (
                    "Why did the median price move — and does that mean "
                    "home values changed?"
                ),
                "lead": (
                    "A median sale price in San Diego County moves for two "
                    "reasons &mdash; homes repricing, and a different mix "
                    "of homes selling &mdash; and one month&rsquo;s median "
                    "cannot say which happened."
                ),
                "body": (
                    "<p>Mid-2026 is a live example: detached listings ran "
                    "11.6% below last year&rsquo;s first half, and when "
                    "the composition of what sells shifts, the median "
                    "shifts with it &mdash; no home need have changed "
                    "value. Read medians in runs of months, read the "
                    "detached and attached series separately, and treat "
                    "any single-month move quoted without its series as "
                    "a headline rather than a fact.</p>"
                ),
            },
            {
                "anchor": "data-source",
                "question": (
                    "Where do these San Diego market numbers come from, "
                    "and when do they update?"
                ),
                "lead": (
                    "Figures in this North County market pulse are the "
                    "Greater San Diego Association of REALTORS&rsquo; "
                    "published monthly indicators &mdash; the June 2026 "
                    "release in the current revision &mdash; and the page "
                    "is revised as new months publish rather than left to "
                    "age."
                ),
                "body": (
                    "<p>County-level numbers set context; they do not "
                    "price a home. The per-community picture &mdash; what "
                    "is actually closing in a particular school boundary "
                    "or tax district &mdash; is the conversation to have "
                    "with an agent working that area, and the "
                    "<a href=\"/neighborhoods\">sixteen neighborhood "
                    "guides</a> carry the structural facts that frame "
                    "it.</p>"
                ),
            },
        ],
    },
    {
        "slug": "del-mar-bluff-rail-what-owners-should-know",
        "title": (
            "The Del Mar bluff rail move: what property owners actually "
            "need to track"
        ),
        "dek": (
            "SANDAG plans to take the coastal tracks off the Del Mar "
            "bluffs and underground &mdash; a project measured in "
            "billions of dollars and ownership cycles, with no route yet "
            "chosen. The milestones that turn general concern into "
            "parcel-specific fact, for owners on the bluff and away from "
            "it. Revised as milestones land."
        ),
        "date": "2026-07-30",
        "author": "sofia-azizi",
        "description": (
            "SANDAG's LOSSAN rail realignment in Del Mar: the 1.7-mile "
            "bluff segment, the tunnel route alternatives under study, "
            "the mid-2030s horizon, and what bluff-area and inland "
            "property owners should watch at each milestone."
        ),
        "footnote": (
            "      Project facts above are from SANDAG&rsquo;s published LOSSAN Rail\n"
            "      Realignment materials and the City of Del Mar&rsquo;s project pages as\n"
            "      of July 2026; alignments, costs and dates are provisional until a\n"
            "      route is selected and funded. This page is revised as milestones\n"
            "      land."
        ),
        "blocks": [
            {
                "anchor": "whats-planned",
                "question": (
                    "What is actually planned for the Del Mar bluff rail "
                    "line?"
                ),
                "lead": (
                    "SANDAG&rsquo;s LOSSAN Rail Realignment would move the "
                    "1.7-mile segment of coastal track that runs atop the "
                    "Del Mar bluffs into a tunnel inland, replacing the "
                    "corridor&rsquo;s most fragile stretch &mdash; the "
                    "project is in environmental review, and no route has "
                    "been selected."
                ),
                "body": (
                    "<p>The stretch matters beyond Del Mar: the LOSSAN "
                    "corridor is among the busiest intercity passenger "
                    "rail corridors in the country, and the bluff segment "
                    "is its chokepoint &mdash; eroding, single-tracked, "
                    "and periodically closed for emergency stabilization. "
                    "SANDAG&rsquo;s rail realignment project pages are the "
                    "official record, and the claims worth acting on all "
                    "live there.</p>"
                ),
            },
            {
                "anchor": "routes",
                "question": (
                    "Which tunnel routes are under study in Del Mar?"
                ),
                "lead": (
                    "The alternatives SANDAG has published for the Del Mar "
                    "realignment differ in where the tunnel runs &mdash; "
                    "one tracks Interstate 5 with the longest tunnel, one "
                    "runs more directly beneath Del Mar itself, and one "
                    "keeps the shortest tunnel closest to the coast &mdash; "
                    "with published cost figures in the billions per "
                    "alignment."
                ),
                "body": (
                    "<p>The under-town options are what put easements on "
                    "the community&rsquo;s agenda: a tunnel passes beneath "
                    "somebody&rsquo;s parcel, and which parcels is exactly "
                    "what route selection decides. Route selection is "
                    "therefore the milestone that converts general concern "
                    "into parcel-specific fact &mdash; and the public "
                    "comment windows SANDAG runs before it are the point "
                    "of influence, not the construction hearings years "
                    "later.</p>"
                ),
            },
            {
                "anchor": "timeline",
                "question": (
                    "When would trains actually leave the Del Mar bluffs?"
                ),
                "lead": (
                    "Published planning for the Del Mar realignment points "
                    "at completion in the mid-2030s, with environmental "
                    "work and route selection still ahead of construction "
                    "&mdash; a horizon measured in ownership cycles, not "
                    "escrow periods."
                ),
                "body": (
                    "<p>The near-term reality is the opposite of the "
                    "long-term plan: continued stabilization work on the "
                    "existing bluff alignment to keep it running until a "
                    "replacement exists. Both timelines are trackable "
                    "&mdash; SANDAG for the realignment, the City of Del "
                    "Mar&rsquo;s project repository for bluff work &mdash; "
                    "and any specific completion year deserves to be "
                    "treated as provisional until a route is chosen and "
                    "funded.</p>"
                ),
            },
            {
                "anchor": "bluff-owners",
                "question": (
                    "What should bluff-area Del Mar owners watch?"
                ),
                "lead": (
                    "For Del Mar owners near the bluffs, the near-term "
                    "facts are stabilization construction on the existing "
                    "track and, on the long horizon, the question of what "
                    "replaces the rail corridor after trains move &mdash; "
                    "access, trails and slope work all route through the "
                    "city&rsquo;s and SANDAG&rsquo;s published project "
                    "records."
                ),
                "body": (
                    "<p>Construction windows, staging areas and closure "
                    "schedules are published facts, not rumors to trade "
                    "on &mdash; and a transaction near the corridor is "
                    "better served by citing them than by either "
                    "catastrophizing or waving them off. The "
                    "<a href=\"/neighborhoods/del-mar\">Del Mar guide</a> "
                    "carries the community-level picture, coastal-zone "
                    "rules included.</p>"
                ),
            },
            {
                "anchor": "inland-owners",
                "question": (
                    "Does the rail project matter for Del Mar homes away "
                    "from the bluff?"
                ),
                "lead": (
                    "Del Mar homes nowhere near the bluff still intersect "
                    "the rail project through route selection: an inland "
                    "tunnel passes beneath somebody, and easement, "
                    "vibration and staging questions attach to the chosen "
                    "alignment rather than to the coastline."
                ),
                "body": (
                    "<p>Until a route is selected, the parcel-specific "
                    "answer does not exist &mdash; which cuts both ways: "
                    "no inland parcel can claim immunity, and none should "
                    "be discounted on speculation. The actionable habit is "
                    "unglamorous: know which alternatives touch which "
                    "parts of town, and use the comment windows while the "
                    "decision is still open.</p>"
                ),
            },
        ],
    },
]


def by_slug(slug: str) -> dict | None:
    return next((p for p in POSTS if p["slug"] == slug), None)
