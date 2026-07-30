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
                "anchor": "assessment-surcharge",
                "question": (
                    "Why is there a FAIR Plan charge on a regular San "
                    "Diego insurance bill?"
                ),
                "lead": (
                    "To cover Los Angeles fire losses, the FAIR Plan "
                    "levied a $1 billion assessment on its member "
                    "insurers in early 2025 &mdash; every admitted "
                    "property carrier in California &mdash; and "
                    "Department of Insurance bulletins allow carriers to "
                    "recover a share as a temporary supplemental fee on "
                    "ordinary policies statewide, San Diego included. A "
                    "Los Angeles superior court upheld that pass-through "
                    "framework on June 30, 2026; the department "
                    "describes the typical fee as a median of roughly "
                    "$28, recoverable over at most two years."
                ),
                "body": (
                    "<p>The practical readings: a household nowhere near "
                    "a fire zone still shares in the plan&rsquo;s losses "
                    "through this line item, the fee is a surcharge "
                    "rather than a coverage change, and the consumer "
                    "group that challenged it says it is weighing an "
                    "appeal &mdash; so the framework is settled for now, "
                    "not forever. Sacramento is also in motion: AB 1680, "
                    "which would restructure how the plan is financed, "
                    "passed the Assembly in May 2026 and is in Senate "
                    "committee process as of this revision. This page "
                    "updates as either moves.</p>"
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
                    "than a budgeting nuisance. "
                    "<a href=\"/blog/home-insurance-before-you-offer\">The "
                    "full pre-offer sequence</a> walks each step with the "
                    "maps, forms and deadlines.</p>"
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
                    "mailing address &mdash; and the map is moving. "
                    "Escondido opted in with its June 2026 ADU ordinance "
                    "overhaul, which makes ADU approval ministerial and "
                    "allows separate sale under the state framework. The "
                    "trap that runs through school "
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
    {
        "slug": "is-escondido-a-good-place-to-live",
        "title": (
            "Is Escondido a good place to live? Answer it with facts, "
            "not adjectives"
        ),
        "dek": (
            "The honest answer depends on which tradeoffs matter to the "
            "household asking &mdash; and every one of them is checkable. "
            "The housing stock and what it means for the tax line, the "
            "two-district school structure, the commute geometry, and an "
            "open-space inventory most listings never mention."
        ),
        "date": "2026-07-30",
        "author": "sofia-azizi",
        "description": (
            "Whether Escondido is a good place to live comes down to "
            "verifiable tradeoffs: older housing stock with no Mello-Roos "
            "on most addresses, two school districts, the I-15/SR-78 "
            "junction and SPRINTER rail, Daley Ranch and the city lakes, "
            "and where the published data lives for the questions "
            "adjectives can't answer."
        ),
        "footnote": (
            "      Facility and acreage facts above are from the City of Escondido&rsquo;s\n"
            "      published pages (Lakes Division, Daley Ranch, Kit Carson Park) as of\n"
            "      July 2026. District boundaries and hazard-zone designations are\n"
            "      redrawn from time to time; confirm any specific address with the\n"
            "      district office and the current maps before relying on it."
        ),
        "blocks": [
            {
                "anchor": "how-to-answer",
                "question": "Is Escondido a good place to live?",
                "lead": (
                    "Whether Escondido is a good place to live depends on "
                    "which tradeoffs matter to the household asking, and "
                    "every one of those tradeoffs is checkable: what era "
                    "the housing stock is and how that shapes the tax "
                    "line, how the two school districts assign, what the "
                    "I-15/SR-78 junction and the SPRINTER actually offer a "
                    "commute, and what the city&rsquo;s open space "
                    "contains. Fair housing law &mdash; and plain accuracy "
                    "&mdash; rule out answering with adjectives about the "
                    "people who live somewhere, so this page answers with "
                    "places and processes."
                ),
                "body": (
                    "<p>Escondido is four ZIP codes that behave as "
                    "separate markets, built in different decades, which "
                    "is why a single citywide verdict describes none of "
                    "them well. The "
                    "<a href=\"/neighborhoods/escondido\">Escondido "
                    "guide</a> maps the sub-areas; the blocks below cover "
                    "the decision-level facts the guide does not.</p>"
                ),
            },
            {
                "anchor": "older-stock",
                "question": (
                    "What does buying an older Escondido home involve "
                    "that a newer tract does not?"
                ),
                "lead": (
                    "Most Escondido homes pre-date the Mello-Roos era, so "
                    "the typical address carries no community facilities "
                    "district at all &mdash; the county&rsquo;s FY 2025-26 "
                    "list shows one active CFD in the city, a school "
                    "district CFD formed in 2019 that applies to newer "
                    "development. The tradeoff arrives at inspection "
                    "instead: housing stock from the 1950s through the "
                    "1980s makes roof age, electrical panels, plumbing "
                    "material and sewer laterals the questions that "
                    "actually price a purchase."
                ),
                "body": (
                    "<p>That is the structural difference between "
                    "Escondido and the master-planned communities a few "
                    "exits south &mdash; the "
                    "<a href=\"/neighborhoods/escondido#vs-san-marcos\">"
                    "guide&rsquo;s San Marcos comparison</a> puts numbers "
                    "on it, and <a href=\"/mello-roos\">the Mello-Roos "
                    "page</a> explains the mechanics. Two edge cases "
                    "worth knowing before offering: the Old Escondido "
                    "Historic District applies design review to exterior "
                    "changes, and several Escondido-addressed communities "
                    "sit outside the city limits in unincorporated "
                    "county, where the permitting authority differs.</p>"
                ),
            },
            {
                "anchor": "schools-check",
                "question": (
                    "How should schools figure into an Escondido home "
                    "decision?"
                ),
                "lead": (
                    "An Escondido address requires two school lookups, "
                    "not one: Escondido Union School District assigns "
                    "kindergarten through eighth grade and Escondido "
                    "Union High School District assigns ninth through "
                    "twelfth, from two different boundary maps &mdash; "
                    "and addresses on the city&rsquo;s edges can fall "
                    "into San Pasqual Union, Valley Center-Pauma or "
                    "Bonsall districts instead."
                ),
                "body": (
                    "<p>The method matters more than any ranking: run "
                    "the specific address through both districts&rsquo; "
                    "boundary tools, then confirm with the district "
                    "office before relying on it. The "
                    "<a href=\"/neighborhoods/escondido#schools-structure\">"
                    "guide</a> explains why the structure is split, and "
                    "<a href=\"/blog/san-diego-school-district-by-address\">"
                    "the district-by-address post</a> covers how North "
                    "County boundaries cross city lines generally.</p>"
                ),
            },
            {
                "anchor": "open-space",
                "question": (
                    "What outdoor space does Escondido actually have?"
                ),
                "lead": (
                    "Escondido&rsquo;s open-space inventory is larger "
                    "than most listings suggest: the city&rsquo;s Lakes "
                    "Division manages more than 4,500 acres, including "
                    "Daley Ranch &mdash; a habitat preserve of more than "
                    "3,000 acres the city bought in 1996 to protect in "
                    "perpetuity &mdash; plus Dixon Lake with fishing, "
                    "boating and camping, and seasonal Lake Wohlford."
                ),
                "body": (
                    "<p>Kit Carson Park adds 285 acres on the "
                    "city&rsquo;s south side &mdash; 100 developed, 185 "
                    "kept as natural habitat &mdash; and holds Queen "
                    "Califia&rsquo;s Magical Circle, the only American "
                    "sculpture garden by Niki de Saint Phalle. East of "
                    "the city, the San Pasqual Valley carries the San "
                    "Diego Zoo Safari Park and working agricultural "
                    "land. For a buyer weighing Escondido against "
                    "denser, newer communities, this inventory is a "
                    "real part of the ledger.</p>"
                ),
            },
            {
                "anchor": "is-it-safe",
                "question": "Is Escondido safe?",
                "lead": (
                    "&ldquo;Safe&rdquo; is a characterization no honest "
                    "professional can certify for Escondido or anywhere "
                    "else &mdash; what exists instead is published data, "
                    "and Escondido&rsquo;s is unusually accessible: the "
                    "city runs its own police department, whose "
                    "published route is the beat map plus ARJIS, the "
                    "regional crime-mapping system, and SANDAG&rsquo;s "
                    "Criminal Justice Research Division publishes the "
                    "county&rsquo;s crime statistics reports."
                ),
                "body": (
                    "<p>The workable method for any specific address: "
                    "look up its beat in ARJIS, read the trend over "
                    "several years rather than a single incident map, "
                    "and treat block-level differences as real &mdash; "
                    "citywide figures blur four distinct ZIP codes. On "
                    "the rural edges the hazard that actually prices "
                    "into a purchase is fire: CAL&nbsp;FIRE&rsquo;s "
                    "severity-zone maps carry the designations, and "
                    "<a href=\"/blog/california-fair-plan-san-diego\">"
                    "the FAIR Plan post</a> covers what they mean for "
                    "insurance.</p>"
                ),
            },
            {
                "anchor": "downtown",
                "question": (
                    "What is there to actually do in Escondido?"
                ),
                "lead": (
                    "Escondido&rsquo;s downtown is a functioning core "
                    "rather than a themed district: Grand Avenue runs "
                    "the historic commercial spine, Cruisin&rsquo; Grand "
                    "fills it with pre-1973 American classics on Friday "
                    "nights from April through September, and the "
                    "California Center for the Arts &mdash; a city-owned "
                    "campus with a concert hall, theater and museum, "
                    "open since 1994 &mdash; anchors the civic center."
                ),
                "body": (
                    "<p>The practical read for a buyer: the downtown "
                    "blocks and Old Escondido behind them are where the "
                    "city&rsquo;s older, character housing concentrates "
                    "&mdash; with the design-review overlay that "
                    "protects it &mdash; while the newer stock sits on "
                    "the edges. Which end of that range fits is a "
                    "housing-stock question, not a verdict about the "
                    "city.</p>"
                ),
            },
            {
                "anchor": "tradeoffs",
                "question": (
                    "What are the honest tradeoffs of living in "
                    "Escondido?"
                ),
                "lead": (
                    "The costs of Escondido are inland summer heat "
                    "compared with the coastal cities, an older housing "
                    "core whose systems need real inspection attention, "
                    "a two-district school structure that takes two "
                    "lookups, and fire-hazard designations on the rural "
                    "fringes. The offsets: the I-15/SR-78 junction and a "
                    "SPRINTER rail option, no Mello-Roos on most "
                    "addresses, more than 4,500 acres of city-managed "
                    "open space, and a downtown with working "
                    "institutions."
                ),
                "body": (
                    "<p>Households weigh those differently, which is the "
                    "whole point of answering with facts. Before an "
                    "offer on the rural edges, run the insurance check "
                    "&mdash; "
                    "<a href=\"/blog/home-insurance-before-you-offer\">"
                    "insurability before you offer</a> walks the "
                    "sequence &mdash; and for the commute reality, the "
                    "<a href=\"/neighborhoods/escondido#getting-around\">"
                    "guide&rsquo;s transit block</a> covers the "
                    "junction and the rail connection.</p>"
                ),
            },
        ],
    },
    {
        "slug": "escondido-housing-pipeline",
        "title": (
            "What is actually being built in Escondido &mdash; and what "
            "the state is demanding"
        ),
        "dek": (
            "A wave of downtown approvals is remaking Valley Parkway "
            "block by block while the state formally questions the "
            "city&rsquo;s housing-element compliance. The projects with "
            "real approvals, the scoreboard against the 9,607-unit "
            "mandate, and the one big project that is going nowhere. "
            "Revised quarterly."
        ),
        "date": "2026-07-30",
        "author": "zohra-azizi",
        "description": (
            "Escondido's housing pipeline in mid-2026: the downtown "
            "Valley Parkway approvals (The Maple, Valley Parkway "
            "Townhomes, KB Home, Quince Street), RHNA progress of "
            "roughly a quarter of 9,607 units, the December 2025 HCD "
            "letter of inquiry, and the stalled Harvest Hills proposal."
        ),
        "footnote": (
            "      Project facts above are from City of Escondido hearing notices and\n"
            "      council records, the California HCD letter of December 3, 2025, and\n"
            "      named local reporting (The Coast News, Voice of San Diego), as of the\n"
            "      dates cited. Approvals are not completions; construction status\n"
            "      changes. The city&rsquo;s agendas are the record, and this page is\n"
            "      revised quarterly."
        ),
        "blocks": [
            {
                "anchor": "whats-being-built",
                "question": (
                    "What housing is actually approved or under "
                    "construction in Escondido right now?"
                ),
                "lead": (
                    "Escondido&rsquo;s pipeline concentrates on and "
                    "around downtown&rsquo;s Valley Parkway: The Maple, "
                    "128 apartments in five stories across from City "
                    "Hall, approved January 2026; Valley Parkway "
                    "Townhomes, 94 for-sale homes approved unanimously "
                    "in June 2026; a 70-townhome KB Home project by the "
                    "transit center approved December 2025; and Quince "
                    "Street Senior Apartments, 145 affordable senior "
                    "homes already under construction across from the "
                    "transit center."
                ),
                "body": (
                    "<p>Behind those sit the wave&rsquo;s two largest "
                    "pieces: Palomar Heights, the 510-home redevelopment "
                    "of the former hospital site approved in 2021, and "
                    "the county&rsquo;s Valley Creek project at 620 E. "
                    "Valley Parkway &mdash; 134 affordable senior homes "
                    "plus a childcare facility on surplus county land, "
                    "in environmental review as of May 2026 with "
                    "construction expected in 2028. The pattern is "
                    "consistent: density is going downtown, near "
                    "transit, on already-developed land.</p>"
                ),
            },
            {
                "anchor": "rhna-scoreboard",
                "question": (
                    "Is Escondido on pace for its state housing "
                    "mandate?"
                ),
                "lead": (
                    "Escondido&rsquo;s state-assigned target for the "
                    "2021&ndash;2029 cycle is 9,607 homes, and the "
                    "city&rsquo;s own annual progress reporting puts "
                    "permits at roughly 2,300 through 2025 &mdash; about "
                    "a quarter of the mandate with the cycle past "
                    "half-run, and heavily tilted toward "
                    "market-rate homes."
                ),
                "body": (
                    "<p>The tilt is the part regulators watch: as "
                    "reported by Voice of San Diego from the city&rsquo;s "
                    "2025 figures, roughly 70% of that year&rsquo;s 369 "
                    "permits were above-moderate-income homes, and the "
                    "affordable categories sit far behind &mdash; on the "
                    "order of 11% of the very-low-income target and 6% "
                    "of moderate. Escondido is not unusual in lagging, "
                    "but the gap is what gives the state&rsquo;s "
                    "December letter its teeth.</p>"
                ),
            },
            {
                "anchor": "state-pressure",
                "question": (
                    "Why is the state questioning Escondido's housing "
                    "plan?"
                ),
                "lead": (
                    "On December 3, 2025, the state housing department "
                    "sent Escondido a formal letter of inquiry listing "
                    "eight overdue housing-element programs &mdash; from "
                    "an unadopted ADU ordinance to the never-established "
                    "affordable-housing trust fund &mdash; and warning "
                    "it may revoke the city&rsquo;s compliance finding, "
                    "an outcome that would expose the city to the "
                    "builder&rsquo;s remedy, under which qualifying "
                    "projects can bypass local zoning."
                ),
                "body": (
                    "<p>The first visible response landed in June 2026: "
                    "a unanimous overhaul of the city&rsquo;s ADU rules "
                    "making approval ministerial and allowing separate "
                    "ADU sale under state law. The harder item is "
                    "structural &mdash; the letter formally identifies "
                    "Proposition S, the 1998 measure requiring voter "
                    "approval for General Plan density increases, as a "
                    "constraint the city must mitigate. That collision "
                    "between a voter-approved measure and a state "
                    "mandate is the live storyline of Escondido "
                    "land-use politics.</p>"
                ),
            },
            {
                "anchor": "for-sale-shift",
                "question": (
                    "Is any of the new Escondido housing for sale, or "
                    "is it all apartments?"
                ),
                "lead": (
                    "The 2025&ndash;26 approvals mark a shift toward "
                    "ownership product in Escondido: 94 for-sale "
                    "townhomes on West Valley Parkway and 70 by the "
                    "transit center were approved within seven months, "
                    "and the council has been explicit about wanting "
                    "&ldquo;missing middle&rdquo; homes &mdash; the "
                    "duplex-to-cottage-court range &mdash; as an "
                    "ownership on-ramp."
                ),
                "body": (
                    "<p>The June 2026 approval came with a developer "
                    "expectation, per The Coast News, of pricing from "
                    "the low $600,000s &mdash; a dated, attributed "
                    "figure that will move, but a marker of what new "
                    "for-sale product downtown looks like. For buyers "
                    "priced against the newer master-planned inventory "
                    "elsewhere in North County, new construction "
                    "without Mello-Roos is a combination worth "
                    "understanding &mdash; "
                    "<a href=\"/blog/is-escondido-a-good-place-to-live\">"
                    "the Escondido decision post</a> covers the tax "
                    "structure.</p>"
                ),
            },
            {
                "anchor": "harvest-hills",
                "question": (
                    "What happened to Harvest Hills (Safari Highlands "
                    "Ranch)?"
                ),
                "lead": (
                    "Harvest Hills &mdash; the proposed 550-home "
                    "annexation on 1,098 unincorporated acres on "
                    "Escondido&rsquo;s eastern edge, east of Rancho San "
                    "Pasqual &mdash; remains where it has been for "
                    "years: application under review, no council vote "
                    "ever scheduled, and no hearing on any posted "
                    "agenda as of July 2026."
                ),
                "body": (
                    "<p>Its environmental review ran back in 2017, and "
                    "a council vote once expected in 2020 never "
                    "happened. Buyers near the eastern edges sometimes "
                    "hear the project cited as imminent in both "
                    "directions &mdash; as a threat and as a promise. "
                    "The checkable fact is narrower: the city&rsquo;s "
                    "own project page lists the application as pending "
                    "with staff, nothing more. Treat any claim beyond "
                    "that as unpublished until an agenda says "
                    "otherwise.</p>"
                ),
            },
            {
                "anchor": "how-to-track",
                "question": (
                    "How do you track what gets built next in "
                    "Escondido?"
                ),
                "lead": (
                    "Escondido&rsquo;s development record lives in "
                    "three public places: the City Council and Planning "
                    "Commission agendas, the city&rsquo;s project pages "
                    "for named developments, and the annual housing "
                    "progress report each spring &mdash; the same "
                    "sources this page is built from."
                ),
                "body": (
                    "<p>This post is revised quarterly as approvals "
                    "land or stall. For the community-level picture "
                    "&mdash; the four ZIP codes, the two school "
                    "districts, what the tax line looks like &mdash; "
                    "start with the "
                    "<a href=\"/neighborhoods/escondido\">Escondido "
                    "guide</a> and "
                    "<a href=\"/blog/is-escondido-a-good-place-to-live\">"
                    "the decision post</a>.</p>"
                ),
            },
        ],
    },
    {
        "slug": "oceanside-mission-avenue-mixed-use",
        "title": (
            "Mission Avenue is the spine of downtown Oceanside&rsquo;s "
            "build-out"
        ),
        "dek": (
            "Two high-rises totaling 503 homes were approved on adjacent "
            "Mission Avenue blocks within eight months &mdash; and they "
            "are the visible edge of a bigger wave: four more entitled "
            "projects, a rewritten density cap, a state transit-housing "
            "law, and a transit-center redevelopment waiting on one last "
            "approval. Revised as milestones land."
        ),
        "date": "2026-07-30",
        "author": "nilab-azizi",
        "description": (
            "Downtown Oceanside development in mid-2026: the 901 and "
            "801 Mission Avenue approvals (503 homes), the 86 du/acre "
            "density cap certified in February 2026, SB 79's arrival, "
            "the NCTD transit-center project awaiting Coastal "
            "Commission review, and what owners and buyers should "
            "actually track."
        ),
        "footnote": (
            "      Project and policy facts above are from City of Oceanside staff\n"
            "      reports and hearing records, California Coastal Commission and\n"
            "      CEQA filings, NCTD announcements, and named local reporting (The\n"
            "      Coast News, inewsource, KPBS), as of the dates cited. Approvals\n"
            "      are not completions, and construction status changes; this page is\n"
            "      revised as milestones land."
        ),
        "blocks": [
            {
                "anchor": "mission-pair",
                "question": (
                    "What are the two big projects approved on Mission "
                    "Avenue in Oceanside?"
                ),
                "lead": (
                    "The pair reshaping Mission Avenue sits on adjacent "
                    "blocks across from Oceanside High School: 901 "
                    "Mission, eight stories with 273 apartments "
                    "including 28 deed-restricted low-income homes, "
                    "approved October 2025; and 801 Mission, seven "
                    "stories with 230 apartments including 23 "
                    "affordable, approved unanimously in May 2026 "
                    "&mdash; 503 homes between them, both under state "
                    "density-bonus law."
                ),
                "body": (
                    "<p>Both replace low-rise and vacant parcels a few "
                    "blocks inland from the pier, and both cleared "
                    "under applications filed before the city&rsquo;s "
                    "current density and inclusionary rules took their "
                    "2024&ndash;26 form &mdash; part of why the "
                    "approvals came scaled as they did. Neither had "
                    "broken ground as of this writing; entitlement is "
                    "the milestone that has actually happened.</p>"
                ),
            },
            {
                "anchor": "bigger-wave",
                "question": (
                    "What else is entitled in downtown Oceanside right "
                    "now?"
                ),
                "lead": (
                    "Beyond the Mission Avenue pair, downtown "
                    "Oceanside&rsquo;s entitled wave includes 401 "
                    "Mission (326 homes plus a public plaza enlarged "
                    "60% after community pushback, approved October "
                    "2025), the 373-home Blocks 5 &amp; 20 project on "
                    "the North Myers parking site behind the Mission "
                    "Pacific hotel (approved January 2026), and Modera "
                    "Neptune on North Coast Highway &mdash; 360 homes "
                    "plus a 62-room hotel, approved 2024. One project "
                    "is verifiably under construction: the 179-studio "
                    "tower at 712 Seagaze Drive."
                ),
                "body": (
                    "<p>The honest distinction runs through every "
                    "conversation about this list: approved is not "
                    "built. Construction financing, permits and phasing "
                    "decide what rises when, and as of July 2026 the "
                    "public record confirms construction only at "
                    "Seagaze. What the approvals do settle is land use "
                    "&mdash; the downtown blocks now carry entitlements "
                    "measured in hundreds of homes each, and that fact "
                    "alone changes the calculus for owners around "
                    "them.</p>"
                ),
            },
            {
                "anchor": "why-now",
                "question": (
                    "Why is downtown Oceanside suddenly getting "
                    "high-rises?"
                ),
                "lead": (
                    "The rules changed twice: Oceanside&rsquo;s 1984 "
                    "coastal plan capped downtown at 43 homes per acre, "
                    "a 2019 amendment effective 2022 removed the cap "
                    "entirely &mdash; average approved density downtown "
                    "reached roughly 175 per acre &mdash; and in "
                    "February 2026 the Coastal Commission certified a "
                    "new 86-per-acre base maximum that state "
                    "density-bonus law can roughly double, which the "
                    "council accepted in June 2026."
                ),
                "body": (
                    "<p>Two state layers stack on top: the inclusionary "
                    "ordinance now requires 15% affordable homes on "
                    "projects of seven or more units with a 55-year "
                    "term, and SB 79 &mdash; effective July 1, 2026 in "
                    "San Diego County &mdash; permits mid-rise housing "
                    "near major transit stops regardless of some local "
                    "zoning, with the city adopting a phased "
                    "implementation plan across seven station areas. "
                    "The era of arguing about whether downtown gets "
                    "density is over; the live questions are which "
                    "blocks, and with what obligations.</p>"
                ),
            },
            {
                "anchor": "transit-center",
                "question": (
                    "What is happening with the Oceanside Transit "
                    "Center redevelopment?"
                ),
                "lead": (
                    "The largest single piece of downtown "
                    "Oceanside&rsquo;s build-out is the transit "
                    "center&rsquo;s redevelopment by NCTD and Toll "
                    "Brothers &mdash; 547 apartments with 15% "
                    "affordable, a 170-room hotel, retail and a new "
                    "NCTD headquarters &mdash; approved by the city in "
                    "late 2025 along with a companion 206-home project "
                    "at 810 Mission, and now waiting on its final "
                    "gate: California Coastal Commission review."
                ),
                "body": (
                    "<p>The commission&rsquo;s calendar puts it in "
                    "Oceanside itself on October 7, 2026 &mdash; the "
                    "date worth watching, though the project&rsquo;s "
                    "agenda placement is not yet published. For "
                    "context on what the site means beyond housing: "
                    "the transit center is where the SPRINTER, "
                    "COASTER, Amtrak and Metrolink meet &mdash; the "
                    "connection the "
                    "<a href=\"/neighborhoods/oceanside\">Oceanside "
                    "guide</a> covers for commuters.</p>"
                ),
            },
            {
                "anchor": "what-it-means",
                "question": (
                    "What does the downtown build-out mean for "
                    "Oceanside owners and buyers?"
                ),
                "lead": (
                    "For downtown Oceanside owners the near-term "
                    "realities are construction years and parking "
                    "transitions &mdash; the Blocks 5 &amp; 20 project "
                    "alone replaces a roughly 200-space public surface "
                    "lot &mdash; while the entitlements set what the "
                    "skyline and the rental stock look like by the "
                    "2030s. For buyers, the checkable question before "
                    "any downtown purchase is what is entitled on the "
                    "surrounding blocks, because several quiet parcels "
                    "now carry approvals measured in hundreds of "
                    "homes."
                ),
                "body": (
                    "<p>Add the street itself: the Coast Highway "
                    "corridor project &mdash; four lanes to two with "
                    "roundabouts from Surfrider Way to Oceanside "
                    "Boulevard &mdash; has construction plans due in "
                    "summer 2026 and a construction start targeted for "
                    "spring 2027. None of this is speculation; all of "
                    "it is on published city timelines, and all of it "
                    "belongs in a disclosure-era conversation about "
                    "any downtown block.</p>"
                ),
            },
            {
                "anchor": "how-to-track",
                "question": (
                    "How do you track downtown Oceanside projects from "
                    "here?"
                ),
                "lead": (
                    "Downtown Oceanside&rsquo;s development record "
                    "lives in the city council and planning commission "
                    "agendas, the state&rsquo;s CEQA database for each "
                    "project&rsquo;s filings, and the Coastal "
                    "Commission&rsquo;s meeting agendas for anything "
                    "in the coastal zone &mdash; the sources this page "
                    "is built from, and the ones that will say what "
                    "actually breaks ground next."
                ),
                "body": (
                    "<p>This post is revised as milestones land "
                    "&mdash; the Coastal Commission&rsquo;s October "
                    "Oceanside meeting is the next one on the "
                    "calendar. For the citywide picture &mdash; the "
                    "neighborhoods, schools and tax structure &mdash; "
                    "start with the "
                    "<a href=\"/neighborhoods/oceanside\">Oceanside "
                    "guide</a>, and the "
                    "<a href=\"/blog/north-county-market-pulse\">market "
                    "pulse</a> carries the county-level numbers.</p>"
                ),
            },
        ],
    },
    {
        "slug": "home-insurance-before-you-offer",
        "title": (
            "Check the insurance before you write the offer: a San "
            "Diego buyer&rsquo;s sequence"
        ),
        "dek": (
            "In San Diego County&rsquo;s fire-hazard zones, insurability "
            "is a purchase question, not a closing formality &mdash; and "
            "the standard purchase contract quietly agrees: it makes "
            "insurance the buyer&rsquo;s investigation-contingency "
            "problem on a default 17-day clock. The lookup, the quote, "
            "the paperwork the law attaches, and the fallback plan, in "
            "order."
        ),
        "date": "2026-07-30",
        "author": "zohra-azizi",
        "description": (
            "How a San Diego buyer checks home insurability before "
            "writing an offer: the CAL FIRE hazard-map lookup on the "
            "2025 maps, quotes and claims history inside the "
            "investigation contingency, AB 38 disclosures in high-hazard "
            "zones, hardening discounts, and the FAIR Plan plus DIC "
            "fallback."
        ),
        "footnote": (
            "      Statutes, maps, contract forms and insurance programs above are as of\n"
            "      the dates cited and change with regulatory and legislative action;\n"
            "      the current form and filing control. A licensed insurance broker is\n"
            "      the source of a real quote for a specific address &mdash; Team Azizi\n"
            "      is a real estate team, not an insurance broker, and nothing here is\n"
            "      insurance or legal advice."
        ),
        "blocks": [
            {
                "anchor": "why-before-offer",
                "question": (
                    "Why check home insurance before writing an offer "
                    "in San Diego?"
                ),
                "lead": (
                    "Because the standard California purchase agreement "
                    "already assigns the problem to the buyer: the "
                    "C.A.R. contract states that the ability to obtain "
                    "insurance, fire insurance included, is part of the "
                    "buyer&rsquo;s investigation-of-property contingency "
                    "&mdash; a window that defaults to 17 days &mdash; "
                    "and expressly not part of the loan contingency. In "
                    "a San Diego fire-hazard zone, an insurability "
                    "surprise discovered after that window closes has "
                    "no clean exit."
                ),
                "body": (
                    "<p>The lender side makes the deadline real: a "
                    "mortgage does not fund without proof of coverage, "
                    "per the federal consumer bureau&rsquo;s own "
                    "guidance, and coverage bound late arrives at "
                    "whatever price the last available market sets. The "
                    "sequence below front-loads every checkable fact "
                    "into the days when walking away is still free.</p>"
                ),
            },
            {
                "anchor": "hazard-map-lookup",
                "question": (
                    "How do you look up a San Diego property's fire "
                    "hazard zone?"
                ),
                "lead": (
                    "The State Fire Marshal&rsquo;s online viewers map "
                    "every parcel&rsquo;s fire hazard severity zone "
                    "&mdash; Moderate, High or Very High &mdash; and "
                    "San Diego County is on fresh maps: the state "
                    "released the county&rsquo;s updated local-area "
                    "maps on March 24, 2025, the first refresh in "
                    "roughly 14 years, and the county&rsquo;s "
                    "very-high acreage grew about 26% in the update."
                ),
                "body": (
                    "<p>Two readings keep the map honest. First, zones "
                    "climbed into ordinarily suburban territory &mdash; "
                    "which is why the lookup belongs in every San Diego "
                    "purchase, not just backcountry ones. Second, the "
                    "map measures physical hazard, not your quote: the "
                    "State Fire Marshal himself notes the zones do not "
                    "directly drive insurance decisions. Carriers price "
                    "from their own wildfire risk scores &mdash; which "
                    "state regulation since 2022 gives you the right "
                    "to see, and to appeal.</p>"
                ),
            },
            {
                "anchor": "quote-and-claims",
                "question": (
                    "What insurance diligence fits inside the "
                    "17-day investigation window?"
                ),
                "lead": (
                    "Three moves fit a San Diego escrow&rsquo;s "
                    "investigation window, all address-specific: get a "
                    "real quote on the property early in the window, ask the "
                    "listing side for the current carrier and premium "
                    "&mdash; an existing admitted policy that will "
                    "rewrite for a new owner is worth real money "
                    "&mdash; and get the property&rsquo;s claims "
                    "history, which in California&rsquo;s standard "
                    "contract the seller must disclose for the past "
                    "five years."
                ),
                "body": (
                    "<p>The claims file has a formal version: a "
                    "C.L.U.E. report covers seven years of insurance "
                    "claims on the property, and only the owner can "
                    "order it &mdash; so the buyer&rsquo;s move is to "
                    "ask the seller to pull their free annual copy. "
                    "Claims history moves premiums the way a carfax "
                    "moves a used-car price; a property that looks "
                    "identical to its neighbor can quote differently "
                    "for reasons only that report shows.</p>"
                ),
            },
            {
                "anchor": "high-zone-paperwork",
                "question": (
                    "What extra paperwork does a high fire-hazard zone "
                    "add to a San Diego sale?"
                ),
                "lead": (
                    "In a designated high or very high zone &mdash; "
                    "common across inland San Diego County &mdash; "
                    "California law attaches three things to the sale "
                    "itself: the "
                    "natural-hazard disclosure naming the zone, a "
                    "home-hardening disclosure for homes built before "
                    "2010 &mdash; listing specific vulnerabilities like "
                    "unenclosed vents, single-pane windows and "
                    "combustibles within five feet &mdash; and "
                    "documentation of defensible-space compliance, or a "
                    "written agreement that the buyer will obtain it "
                    "after closing."
                ),
                "body": (
                    "<p>Those documents are legal obligations under the "
                    "civil code, but the sharper way to read them is as "
                    "underwriting evidence: the same vent, roof and "
                    "clearance facts the disclosures force into the "
                    "open are what a carrier&rsquo;s inspection will "
                    "price. A seller who assembles them early is "
                    "building the insurability story; a buyer who reads "
                    "them closely is previewing the quote. The "
                    "<a href=\"/blog/california-fair-plan-san-diego\">"
                    "FAIR Plan post</a> covers the seller-side "
                    "preparation in detail.</p>"
                ),
            },
            {
                "anchor": "hardening-discounts",
                "question": (
                    "Do home-hardening upgrades actually lower "
                    "California insurance costs?"
                ),
                "lead": (
                    "For a San Diego owner the discount answer is set "
                    "by regulation: since late 2022, California "
                    "insurers that use wildfire risk in pricing must "
                    "file discounts for the state&rsquo;s Safer from "
                    "Wildfires measures &mdash; a Class-A roof, a "
                    "five-foot ember-resistant zone, upgraded vents, "
                    "multi-pane windows, cleared decks and the rest "
                    "&mdash; and even the FAIR Plan now applies up to "
                    "twelve hardening discounts on policies effective "
                    "November 15, 2025 or later."
                ),
                "body": (
                    "<p>For a buyer comparing two inland properties, "
                    "the hardening ledger is therefore part of the "
                    "price ledger &mdash; a retrofitted 1980s home and "
                    "an untouched one can carry meaningfully different "
                    "premiums for decades. The discount list is also "
                    "the negotiation list: work the seller already did "
                    "should be documented in the transaction, and work "
                    "not done is a knowable future cost, not a "
                    "mystery.</p>"
                ),
            },
            {
                "anchor": "fallback-plan",
                "question": (
                    "What is the fallback if no regular insurer will "
                    "write a San Diego home?"
                ),
                "lead": (
                    "The fallback for a San Diego home the admitted "
                    "market declines is the California FAIR Plan plus a "
                    "difference-in-conditions policy: the FAIR Plan "
                    "writes named-peril fire coverage up to $3 million "
                    "for dwellings when the admitted market declines, "
                    "and a DIC policy from a separate carrier &mdash; "
                    "the state insurance department lists roughly "
                    "nineteen offering one &mdash; layers back the "
                    "liability, theft and water coverages a lender and "
                    "a household actually need."
                ),
                "body": (
                    "<p>The fallback works; the point of this "
                    "post&rsquo;s sequence is to price it while the "
                    "contingency still allows a clean exit, because "
                    "the combination generally costs materially more "
                    "than the standard policy it replaces &mdash; and "
                    "FAIR Plan rates change on October 15, 2026. "
                    "<a href=\"/blog/california-fair-plan-san-diego\">"
                    "The FAIR Plan post</a> carries that change, the "
                    "statewide assessment surcharge, and the "
                    "communities where placement concentrates.</p>"
                ),
            },
            {
                "anchor": "market-direction",
                "question": (
                    "Is the California home-insurance market actually "
                    "improving in 2026?"
                ),
                "lead": (
                    "The direction in 2026, San Diego County included, "
                    "is re-entry on the "
                    "record: Farmers removed its cap on new California "
                    "homeowners policies in November 2025, Mercury and "
                    "CSAA won the first approvals under the "
                    "state&rsquo;s new catastrophe-modeling rules in "
                    "December 2025 with commitments to write in "
                    "wildfire-distressed areas, and Travelers "
                    "announced its own expansion in April 2026 &mdash; "
                    "each committed to writing more, not less, in the "
                    "zones this post is about."
                ),
                "body": (
                    "<p>Re-entry is not a guarantee for any single "
                    "address &mdash; underwriting stays "
                    "parcel-specific, which is the whole reason the "
                    "check-first sequence exists. But it does mean a "
                    "declined property from 2023 or 2024 may quote "
                    "differently today, and a quote worth having "
                    "expires: ask the broker to shop the admitted "
                    "market fresh rather than assuming last "
                    "year&rsquo;s answer. For what this looks like in "
                    "the communities that lean on the FAIR Plan most, "
                    "see <a href=\"/neighborhoods/fallbrook\">"
                    "Fallbrook</a>, <a href=\"/neighborhoods/valley-center\">"
                    "Valley Center</a> and "
                    "<a href=\"/neighborhoods/ramona\">Ramona</a>.</p>"
                ),
            },
        ],
    },
    {
        # Southern-expansion batch, post 1 of 5. The highest-intent topic the
        # twelve new coastal/city guides surfaced: the STRO system governs
        # every beach-area rental-income purchase, and no local competitor
        # publishes the actual counts. Counts verified on the live Treasurer
        # page 2026-07-30; they move, so the block cites its as-of date.
        "slug": "san-diego-short-term-rental-license",
        "title": (
            "The San Diego short-term rental license, explained for "
            "buyers and sellers"
        ),
        "dek": (
            "Whole-home short-term rentals in the City of San Diego run "
            "under a licensing system with hard caps &mdash; and the "
            "license dies at close of escrow rather than transferring "
            "with the deed. What the four tiers mean, where the caps "
            "stand right now, and what to verify before pricing rental "
            "income into an offer in Pacific Beach, La Jolla, Ocean "
            "Beach or Mission Beach."
        ),
        "date": "2026-07-30",
        "author": "zohra-azizi",
        "description": (
            "San Diego's STRO license system: the four tiers, the "
            "Tier 3 and Mission Beach caps with current availability, "
            "why licenses do not transfer on sale, fees and taxes, and "
            "which neighborhoods the ordinance covers."
        ),
        "footnote": (
            "      License counts, fees and tax rates above are from the Office of the\n"
            "      City Treasurer&rsquo;s STRO pages and the San Diego Municipal Code as\n"
            "      of July 2026. Counts change as licenses issue and expire, and the caps\n"
            "      recalculate every two years &mdash; confirm current availability with\n"
            "      the City Treasurer&rsquo;s STRO program before relying on it in a\n"
            "      transaction."
        ),
        "blocks": [
            {
                "anchor": "how-it-works",
                "question": (
                    "How does San Diego's short-term rental license "
                    "system work?"
                ),
                "lead": (
                    "Short-term rentals inside the City of San Diego "
                    "&mdash; any stay under one month &mdash; have "
                    "required a Short-Term Residential Occupancy "
                    "license since May 1, 2023, under Municipal Code "
                    "chapter 5, article 10. Licenses come in four "
                    "tiers: part-time (20 days a year or less), "
                    "home-sharing while the host lives onsite, "
                    "whole-home citywide, and whole-home Mission "
                    "Beach, which has its own rules."
                ),
                "body": (
                    "<p>Two structural facts drive everything else. "
                    "The license is issued to a <em>host</em> &mdash; "
                    "a natural person, not an LLC &mdash; and one "
                    "host may hold one license for one dwelling unit "
                    "at a time, so an owner of several rentals needs "
                    "a separate person as host for each. And the "
                    "whole-home tiers are capped in number citywide, "
                    "which is what makes the license a scarce asset "
                    "in the beach communities rather than a "
                    "formality.</p>"
                ),
            },
            {
                "anchor": "tier-3",
                "question": (
                    "Are whole-home short-term rental licenses still "
                    "available in San Diego?"
                ),
                "lead": (
                    "Tier 3 &mdash; whole-home rentals anywhere in "
                    "the City of San Diego outside Mission Beach "
                    "&mdash; is capped at one percent of the "
                    "city&rsquo;s housing stock, and the cap has not "
                    "yet been reached: the City Treasurer&rsquo;s "
                    "table showed 4,840 licenses issued and 821 "
                    "remaining as of July 17, 2026, with "
                    "applications open."
                ),
                "body": (
                    "<p>The margin is the number to watch. If the "
                    "cap is reached, the application period closes "
                    "within 45 days and later applicants go to a "
                    "waitlist ordered by a lottery held per "
                    "community planning area &mdash; the "
                    "Treasurer&rsquo;s 2025 lottery-administration "
                    "rule spells out the mechanics. A purchase "
                    "premised on Tier 3 income is therefore a "
                    "purchase premised on a number that moves "
                    "monthly, and checking the current count is a "
                    "thirty-second job on the Treasurer&rsquo;s STRO "
                    "page before an offer, not after.</p>"
                ),
            },
            {
                "anchor": "mission-beach",
                "question": (
                    "Why is Mission Beach different for short-term "
                    "rentals?"
                ),
                "lead": (
                    "Mission Beach has its own tier in San "
                    "Diego&rsquo;s STRO system &mdash; Tier 4 "
                    "&mdash; capped at 30 percent of the "
                    "community&rsquo;s housing units in recognition "
                    "of its century-old vacation-rental economy, and "
                    "that tier is currently closed: 1,098 licenses "
                    "issued, zero remaining, with a lottery-ordered "
                    "waitlist from the July&ndash;August 2025 "
                    "application window."
                ),
                "body": (
                    "<p>The waitlist itself is published on the "
                    "Treasurer&rsquo;s site and updates as licenses "
                    "become available; applications reopen for 45 "
                    "days once the list runs down to 25 names. For "
                    "buyers comparing Mission Beach against "
                    "<a href=\"/neighborhoods/pacific-beach\">Pacific "
                    "Beach</a> on rental income, the tiers cut both "
                    "ways: Mission Beach&rsquo;s cap is "
                    "proportionally thirty times more generous, but "
                    "today a Pacific Beach buyer can still apply for "
                    "a license and a Mission Beach buyer joins a "
                    "queue.</p>"
                ),
            },
            {
                "anchor": "buying-selling",
                "question": (
                    "Does a short-term rental license transfer when "
                    "the house is sold?"
                ),
                "lead": (
                    "A San Diego STRO license does not transfer with "
                    "the property &mdash; the Municipal Code states "
                    "that licenses are not transferable and the City "
                    "will not accept any request to transfer or "
                    "assign ownership or location of a license. The "
                    "seller&rsquo;s license is cancelled, and the "
                    "buyer applies new, subject to whatever "
                    "availability exists at that moment."
                ),
                "body": (
                    "<p>This is the fact that breaks deals priced on "
                    "\"turnkey Airbnb\" listings. The workable "
                    "sequence: a buyer in escrow may apply before "
                    "closing by attaching ownership-transfer "
                    "documentation, per the Treasurer&rsquo;s FAQ "
                    "&mdash; so the license application can run "
                    "parallel to the transaction rather than after "
                    "it. Two operating rules matter to the same "
                    "math: whole-home licenses require a minimum of "
                    "90 rental days a year with quarterly reports to "
                    "keep the license, and whole-home stays carry a "
                    "two-night minimum. There is no tier at all for "
                    "renting a non-primary home 21 to 89 days a "
                    "year &mdash; the ordinance simply does not "
                    "allow that pattern.</p>"
                ),
            },
            {
                "anchor": "costs",
                "question": (
                    "What does a San Diego short-term rental license "
                    "cost to hold?"
                ),
                "lead": (
                    "A whole-home San Diego STRO license costs "
                    "$1,129 plus a $41 application fee for its "
                    "two-year term at the rates effective March 1, "
                    "2025, and the "
                    "operating taxes are larger: transient occupancy "
                    "tax on every stay under one month at 11.75, "
                    "12.75 or 13.75 percent depending on the "
                    "property&rsquo;s zone, plus the city&rsquo;s "
                    "annual rental unit business tax."
                ),
                "body": (
                    "<p>The three-zone TOT structure dates to May 1, "
                    "2025, when Measure C took effect &mdash; the "
                    "zones tier by proximity to the Convention "
                    "Center, and the city publishes a lookup map. "
                    "Home-sharing tiers cost less to license ($33 "
                    "application, $193&ndash;$284 license) and carry "
                    "no caps. Renewal is not automatic protection: "
                    "the license runs two years from issuance, the "
                    "renewal notice arrives by email 60 days out, "
                    "and a missed expiration date means reapplying "
                    "from zero &mdash; against whatever remains of "
                    "the cap at that point.</p>"
                ),
            },
            {
                "anchor": "where-it-applies",
                "question": (
                    "Which neighborhoods does the San Diego STRO "
                    "ordinance actually cover?"
                ),
                "lead": (
                    "The STRO ordinance applies only inside City of "
                    "San Diego limits &mdash; which includes "
                    "<a href=\"/neighborhoods/la-jolla\">La Jolla</a>, "
                    "<a href=\"/neighborhoods/pacific-beach\">Pacific "
                    "Beach</a>, Mission Beach, "
                    "<a href=\"/neighborhoods/ocean-beach\">Ocean "
                    "Beach</a>, <a href=\"/neighborhoods/north-park\">"
                    "North Park</a>, "
                    "<a href=\"/neighborhoods/hillcrest\">Hillcrest</a> "
                    "and <a href=\"/neighborhoods/downtown-san-diego\">"
                    "Downtown</a> &mdash; while every neighboring "
                    "city runs its own separate short-term rental "
                    "rules: Chula Vista, Del Mar, Encinitas, "
                    "Oceanside and Carlsbad each license under their "
                    "own ordinances."
                ),
                "body": (
                    "<p>So the first question about any \"San "
                    "Diego\" short-term rental is which jurisdiction "
                    "the parcel actually sits in &mdash; Del "
                    "Mar&rsquo;s own ordinance, for instance, was "
                    "certified by the Coastal Commission in February "
                    "2026 with a citywide cap of 129 permits. One "
                    "more date worth knowing inside the city: the "
                    "tier-and-cap rules sunset in the Coastal "
                    "Overlay Zone on January 1, 2030, unless amended "
                    "or extended &mdash; meaning the coastal rules "
                    "get renegotiated with the Coastal Commission "
                    "before then. A license strategy with a horizon "
                    "past 2030 should watch that docket.</p>"
                ),
            },
        ],
    },
    {
        # Southern-expansion batch, post 2 of 5. News lane, revised as the
        # three tracks move. Density figures are from the CEQA Notice of
        # Determination (primary); anything sourced only to press coverage is
        # attributed inline. The "20-story towers" framing that circulates is
        # deliberately absent — adopted heights-in-feet never got verified to
        # a primary document, and the du/ac numbers did.
        "slug": "whats-changing-in-hillcrest",
        "title": (
            "What's changing in Hillcrest: the promenade, the "
            "rezone's first filings, and the hospital rebuild"
        ),
        "dek": (
            "Three projects are remaking Hillcrest on three different "
            "clocks &mdash; a pedestrian promenade opening first, a "
            "generational rezone whose first applications are just "
            "arriving, and a hospital replacement that runs to 2033. "
            "The dated record of each, and what an owner actually "
            "watches. Revised as milestones land."
        ),
        "date": "2026-07-30",
        "author": "zohra-azizi",
        "description": (
            "Hillcrest's three concurrent changes tracked with dates: "
            "the Normal Street Promenade's opening timeline, the first "
            "development filings under the 2024 plan amendment, the "
            "post office relocation, and UCSD's hospital replacement "
            "schedule through 2033."
        ),
        "footnote": (
            "      Dates and figures above are from the City of San Diego&rsquo;s plan\n"
            "      and project pages, the CEQA Notice of Determination, USPS notices, UC\n"
            "      San Diego&rsquo;s capital-program pages and UC Regents items as of July\n"
            "      2026, with press-reported details attributed inline. Construction\n"
            "      schedules move; this page is revised as milestones land."
        ),
        "blocks": [
            {
                "anchor": "rezone",
                "question": (
                    "What did the Hillcrest rezone actually change on "
                    "the ground?"
                ),
                "lead": (
                    "The Hillcrest Focused Plan Amendment &mdash; "
                    "adopted July 30, 2024, with its implementing "
                    "ordinances effective December 1, 2024 &mdash; "
                    "rezoned about 380 acres of Hillcrest and the "
                    "Medical Complex area, raising maximum "
                    "residential density from 109 dwelling units per "
                    "acre to 218, and up to 290 in community "
                    "commercial areas concentrated in the Hillcrest "
                    "core and between Richmond Street and Park "
                    "Boulevard."
                ),
                "body": (
                    "<p>Two mechanics matter more than the "
                    "headline numbers. The amendment mapped a "
                    "streamlined-review zone &mdash; a CPIOZ Type A "
                    "area along the Washington Street and University "
                    "Avenue corridors and south along Fourth, Fifth "
                    "and Sixth &mdash; where conforming projects "
                    "review ministerially rather than through "
                    "hearings. And the capacity is a 30-year "
                    "envelope, not a construction schedule: the "
                    "city&rsquo;s release put the added capacity at "
                    "17,200 homes, and what converts capacity into "
                    "buildings is the filings block below. The "
                    "<a href=\"/neighborhoods/hillcrest\">Hillcrest "
                    "guide</a> carries the ownership-level picture.</p>"
                ),
            },
            {
                "anchor": "first-filings",
                "question": (
                    "Has anything actually been proposed under the "
                    "new Hillcrest zoning?"
                ),
                "lead": (
                    "The first substantial applications in the "
                    "Hillcrest plan area are now on file: permit "
                    "applications submitted since July 2025 for the "
                    "post office block at 3911 Cleveland Avenue "
                    "&mdash; up to 270 homes in eight stories, as "
                    "reported by Times of San Diego &mdash; and "
                    "Hillcrest Hall at 1601 University Avenue, 97 "
                    "income-restricted apartments that the San Diego "
                    "Housing Commission board advanced on April 16, "
                    "2026."
                ),
                "body": (
                    "<p>A watch item rather than a filing: the "
                    "AT&amp;T building at Sixth and University lost "
                    "its landmark microwave tower in late 2025, and "
                    "neighboring owners have hired planning counsel "
                    "to explore redevelopment &mdash; but no "
                    "application exists. The honest read for owners: "
                    "two filings and one exploration, eighteen "
                    "months into a 30-year plan, is what the early "
                    "innings of a rezone look like. Parcel-level "
                    "questions &mdash; what density now applies to a "
                    "specific lot, what is proposed within a block "
                    "&mdash; are answered by the city&rsquo;s plan "
                    "page and development-tracker map, not by "
                    "renderings in the press.</p>"
                ),
            },
            {
                "anchor": "promenade",
                "question": (
                    "When does the Normal Street Promenade in "
                    "Hillcrest actually open?"
                ),
                "lead": (
                    "The Normal Street Promenade &mdash; Hillcrest&rsquo;s "
                    "conversion of Normal Street&rsquo;s west lanes "
                    "into a pedestrian promenade with an expanded "
                    "Pride Plaza and the 1.1-mile Eastern Hillcrest "
                    "Bikeway &mdash; began construction in February "
                    "2025 and is now expected to open by the end of "
                    "2026, with full project completion in 2027, per "
                    "the city&rsquo;s statements in July 2026 press "
                    "coverage."
                ),
                "body": (
                    "<p>The delay from the original schedule has a "
                    "concrete cause the city has described: "
                    "century-old infrastructure under the street "
                    "&mdash; abandoned streetcar lines and "
                    "disconnected storm drains &mdash; that had to "
                    "be rebuilt first. That work is done; what "
                    "remains is surface finish &mdash; the rainbow "
                    "bikeway painting, roughly a hundred new trees "
                    "(98 planted as of late July 2026, per local "
                    "coverage), shade structures and a restored "
                    "vintage trolley car. Adjacent reality worth "
                    "knowing: the University Avenue pipe replacement "
                    "next door runs to the end of 2027, so the "
                    "promenade opening does not end construction in "
                    "the immediate blocks.</p>"
                ),
            },
            {
                "anchor": "post-office",
                "question": (
                    "Is the Hillcrest post office moving?"
                ),
                "lead": (
                    "The Hillcrest post office is proposed to move "
                    "&mdash; but onto the promenade, not out of the "
                    "neighborhood: USPS announced on December 30, "
                    "2025, that it lost the lease at 3911 Cleveland "
                    "Avenue and proposes relocating to the former "
                    "Newbreak Church building fronting Normal "
                    "Street, next to the DMV. As of late July 2026, "
                    "no move date has been announced."
                ),
                "body": (
                    "<p>The two ends of the move tell one story. "
                    "The receiving end puts a post office, the DMV "
                    "and the promenade on one civic block. The "
                    "departing end is the redevelopment application "
                    "above &mdash; the Cleveland Avenue site is the "
                    "one carrying the 270-unit filing &mdash; which "
                    "makes this relocation the first visible "
                    "domino of the rezone rather than a footnote. "
                    "USPS relocations run through a public notice "
                    "and comment process, so the announcement "
                    "trail, not neighborhood rumor, is where the "
                    "actual dates will appear.</p>"
                ),
            },
            {
                "anchor": "ucsd",
                "question": (
                    "How far along is the UCSD Hillcrest hospital "
                    "rebuild?"
                ),
                "lead": (
                    "UC San Diego&rsquo;s Hillcrest campus rebuild "
                    "has finished its first phase &mdash; the "
                    "McGrath Outpatient Pavilion opened July 28, "
                    "2025, following the parking structure completed "
                    "in 2023 &mdash; and the main event is next: a "
                    "roughly 300-bed replacement hospital, with site "
                    "preparation and demolition expected to begin in "
                    "late summer 2026, major construction in summer "
                    "2027, and an operational date of 2033 per "
                    "UCSD&rsquo;s current capital-program page."
                ),
                "body": (
                    "<p>The driver is state hospital seismic law "
                    "&mdash; the existing 1963 tower does not meet "
                    "the requirements and was judged infeasible to "
                    "retrofit, so it operates through construction "
                    "and comes down after the replacement opens. UC "
                    "Regents approved $150 million in "
                    "preliminary-plans funding on March 19, 2025, "
                    "with the full budget to follow environmental "
                    "review. For the surrounding blocks that means "
                    "the construction phasing runs on published "
                    "documents with dates &mdash; and a buyer near "
                    "the campus edge is buying next to a "
                    "seven-year, phase-mapped project, not an "
                    "open-ended one. The 2019 campus plan also "
                    "carries up to 1,000 on-campus homes in its "
                    "later phases &mdash; housing supply on "
                    "Hillcrest&rsquo;s doorstep that predates the "
                    "2024 rezone.</p>"
                ),
            },
        ],
    },
    {
        # Southern-expansion batch, post 3 of 5. Update-in-place tracker on
        # the Del Mar bluff/rail pattern. Research note that matters for
        # future revisions: LAFCO's project page files the CFA-contract item
        # under a "May 4, 2026" heading, but every meeting-level document
        # (agenda, deck, staff report, executed contract) says the Commission
        # authorized it at the June 15, 2026 special meeting — cite June 15.
        # The applicant's ~$8M/yr revenue-neutrality figure is an ACLJ
        # estimate reported by lajolla.ca, labeled as such below.
        "slug": "la-jolla-cityhood-what-owners-should-know",
        "title": (
            "La Jolla cityhood: what is actually decided, and what an "
            "owner should watch"
        ),
        "dek": (
            "La Jolla&rsquo;s bid to leave the City of San Diego has "
            "cleared its petition, survived a court challenge, and "
            "entered the two-year fiscal analysis that decides whether "
            "it reaches a ballot. What the process actually requires, "
            "what would and would not change for property owners, and "
            "the dates that matter next. Revised as milestones land."
        ),
        "date": "2026-07-30",
        "author": "sofia-azizi",
        "description": (
            "The La Jolla incorporation effort tracked from primary "
            "records: the certified petition, the fiscal analysis "
            "underway, the dual-vote requirement and the dispute over "
            "it, what happens to property taxes and schools, and the "
            "timeline to a possible November 2028 election."
        ),
        "footnote": (
            "      Facts above are from San Diego LAFCO&rsquo;s published records &mdash;\n"
            "      staff reports, the June 15, 2026 meeting materials, the executed\n"
            "      consultant agreement &mdash; and the cited statutes as of July 2026,\n"
            "      with applicant materials and press reports labeled as such. The\n"
            "      analysis phase runs into 2028 and every conclusion in it is\n"
            "      provisional until the Commission acts. This page is revised as\n"
            "      milestones land."
        ),
        "blocks": [
            {
                "anchor": "where-it-stands",
                "question": (
                    "Where does the La Jolla cityhood effort stand "
                    "right now?"
                ),
                "lead": (
                    "The La Jolla incorporation proposal &mdash; "
                    "formally a special reorganization that would "
                    "detach about 14 square miles from the City of "
                    "San Diego &mdash; is past its petition stage "
                    "and into its analysis stage: LAFCO certified "
                    "6,772 valid signatures against a requirement of "
                    "6,750 in 2025, and the state-required "
                    "comprehensive fiscal analysis began fieldwork "
                    "in August 2026 under a contract authorized "
                    "June 15, 2026."
                ),
                "body": (
                    "<p>The petition&rsquo;s 22-signature margin "
                    "drew a formal objection from the mayor and a "
                    "lawsuit from the city; the trial court struck "
                    "the city&rsquo;s challenge in its entirety in "
                    "October 2025, per LAFCO&rsquo;s official "
                    "statement, and the analysis is proceeding. The "
                    "proposed boundary covers roughly the 92037 "
                    "footprint &mdash; the Village, La Jolla Shores "
                    "and Bird Rock, about 38,000 residents &mdash; "
                    "and excludes the UC San Diego campus. Until "
                    "any of the steps below happen, every permit, "
                    "tax and service in "
                    "<a href=\"/neighborhoods/la-jolla\">La Jolla</a> "
                    "remains City of San Diego business.</p>"
                ),
            },
            {
                "anchor": "the-vote",
                "question": (
                    "Who gets to vote on La Jolla leaving San "
                    "Diego?"
                ),
                "lead": (
                    "State law as written requires two elections for "
                    "a special reorganization like La Jolla&rsquo;s: "
                    "one in the territory detaching, and one across "
                    "the entire city it detaches from &mdash; and a "
                    "majority in both. Government Code section "
                    "57119 orders both elections; section 57176.1 "
                    "makes approval conditional on majorities in "
                    "each."
                ),
                "body": (
                    "<p>Whether that citywide vote is truly "
                    "required is now the proposal&rsquo;s central "
                    "legal question: the applicant "
                    "association&rsquo;s negotiator has argued "
                    "publicly that it may not be, LAFCO&rsquo;s "
                    "position is that it is, and coverage in June "
                    "2026 described the question as untested "
                    "territory no court has resolved. An owner "
                    "tracking this needs no opinion on the merits "
                    "&mdash; just the awareness that the answer "
                    "changes the odds entirely, since a proposal "
                    "that must win a citywide majority faces a "
                    "different electorate than one decided in La "
                    "Jolla alone.</p>"
                ),
            },
            {
                "anchor": "fiscal-analysis",
                "question": (
                    "What does the La Jolla fiscal analysis "
                    "actually decide?"
                ),
                "lead": (
                    "The comprehensive fiscal analysis now underway "
                    "for La Jolla &mdash; prepared by London Moeder "
                    "Advisors under a $150,000 contract funded by "
                    "the applicant association, not by taxpayers "
                    "&mdash; is the statutory test of whether a "
                    "City of La Jolla works on paper: projected "
                    "revenues and costs over ten years, how "
                    "services would be provided, and what the "
                    "detachment does to the City of San "
                    "Diego&rsquo;s finances."
                ),
                "body": (
                    "<p>Two of its tasks carry the outcome. The "
                    "property-tax exchange determines how the "
                    "existing tax revenue splits between the new "
                    "city and the agencies that serve it today. And "
                    "the revenue-neutrality analysis applies the "
                    "law&rsquo;s hard condition: LAFCO cannot "
                    "approve an incorporation that leaves the "
                    "remaining city substantially worse off unless "
                    "the effect is mitigated &mdash; by tax-sharing "
                    "or payments over time. The applicant&rsquo;s "
                    "own preliminary analysis, as reported by "
                    "lajolla.ca, contemplated payments to San Diego "
                    "on the order of $8 million a year for a "
                    "negotiated period &mdash; a number the CFA "
                    "will now test rather than assume.</p>"
                ),
            },
            {
                "anchor": "taxes",
                "question": (
                    "Would La Jolla cityhood change property "
                    "taxes?"
                ),
                "lead": (
                    "Incorporation would not change the 1 percent "
                    "base property-tax rate in La Jolla &mdash; "
                    "that cap is set by the state constitution and "
                    "applies regardless of which city a parcel sits "
                    "in &mdash; and it is not a reassessment "
                    "event: the law reallocates existing revenue "
                    "between agencies rather than levying anything "
                    "new."
                ),
                "body": (
                    "<p>The moving part is allocation. Per the "
                    "applicant&rsquo;s preliminary fiscal analysis "
                    "on file with LAFCO, about 17 percent of the "
                    "basic 1 percent collected in La Jolla &mdash; "
                    "roughly $44 million &mdash; currently accrues "
                    "to the City of San Diego, and that share is "
                    "what a new city would negotiate over; the "
                    "schools&rsquo; 53 percent share sits outside "
                    "the fight, and existing special taxes and "
                    "assessments above the 1 percent continue "
                    "unchanged. What a new city could add later "
                    "&mdash; its own taxes, its own fees &mdash; is "
                    "a policy question for a city that does not "
                    "yet exist, which is exactly why the CFA&rsquo;s "
                    "ten-year budget is the document to read when "
                    "it publishes.</p>"
                ),
            },
            {
                "anchor": "schools-services",
                "question": (
                    "What happens to schools and city services if "
                    "La Jolla incorporates?"
                ),
                "lead": (
                    "School assignments in La Jolla would not "
                    "change with cityhood: school districts are "
                    "outside this process entirely &mdash; the "
                    "state&rsquo;s reorganization law expressly "
                    "excludes them from LAFCO&rsquo;s jurisdiction, "
                    "and the proposal on file touches no school "
                    "boundary. City services are the open "
                    "question the analysis exists to answer."
                ),
                "body": (
                    "<p>Today the City of San Diego provides "
                    "police, fire-rescue, lifeguards, parks, "
                    "libraries, permitting, sewer and trash in La "
                    "Jolla. A new city would provide each of those "
                    "directly, contract for them &mdash; including "
                    "potentially back to San Diego &mdash; or join "
                    "a regional provider; the applicant&rsquo;s "
                    "preliminary analysis catalogs options from a "
                    "standalone police department to annexation "
                    "into County Fire. Which model each service "
                    "gets, and what it costs, is the substance of "
                    "the analysis running through mid-2027 &mdash; "
                    "and the first document that will state it "
                    "concretely is the draft CFA.</p>"
                ),
            },
            {
                "anchor": "timeline",
                "question": (
                    "When could La Jolla actually vote on "
                    "cityhood?"
                ),
                "lead": (
                    "LAFCO&rsquo;s own published timeline for La "
                    "Jolla runs: analysis fieldwork August 2026 "
                    "through June 2027, a draft report with a "
                    "90-day public review and community workshops "
                    "July through October 2027, a final report by "
                    "early 2028, Commission consideration around "
                    "May 2028, and &mdash; only if the Commission "
                    "approves &mdash; an election in November 2028, "
                    "with a potential effective date of July 2029."
                ),
                "body": (
                    "<p>Every arrow in that chain is conditional "
                    "on the one before it, and the Commission can "
                    "attach terms that reshape the proposal at the "
                    "approval step. The trackable record lives in "
                    "San Diego LAFCO&rsquo;s agendas &mdash; the "
                    "next regular meetings fall August 3 and "
                    "October 5, 2026 &mdash; and this page gets "
                    "revised as those milestones land, the same "
                    "update-in-place treatment as the "
                    "<a href=\"/blog/del-mar-bluff-rail-what-owners-should-know\">"
                    "Del Mar bluff rail tracker</a>. History gives "
                    "the honest odds: press coverage notes no "
                    "California community has voted itself out of "
                    "an existing city in more than a century.</p>"
                ),
            },
        ],
    },
]


def by_slug(slug: str) -> dict | None:
    return next((p for p in POSTS if p["slug"] == slug), None)
