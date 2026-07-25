"""Query fan-out map.

Google AI Mode does not answer the query it is given. It decomposes that query
into a batch of synthetic sub-queries, runs them in parallel, and synthesises
one answer from whatever each of them returns. ChatGPT and Perplexity behave
similarly. So the unit that gets retrieved and cited is **not the page** — it
is a passage that happens to fully answer one sub-query.

That changes the page template. A neighborhood page written as one flowing
narrative competes for the head term and loses every sub-query, because no
individual passage stands on its own. The same content, cut into blocks that
each answer one sub-query completely, competes for twenty retrievals instead
of one.

Three rules follow, and validate.py enforces the first two:

1. **No anaphora in a lead answer.** A passage that opens "It's roughly
   $250–300 a month" is worthless out of context, and out of context is the
   only context it will ever be read in.
2. **Name the entity inside the block.** The neighborhood name and ZIP belong
   in the passage, not only in the H1 three screens up.
3. **Lead with the number, then the nuance.** The extractable sentence comes
   first; caveats come after.

`CLASSES` are the sub-queries that fan out for essentially any residential
neighborhood — the reusable spine, which is what makes this repeatable for
CitedRealty customer #2. `EXTRA` holds the ones specific to a community,
drawn from the verified forum/PAA demand in research/keywords.md.
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# The reusable spine. `q` is formatted with the neighborhood dict.
# `block` is the anchor id the answering passage must carry, so the fan-out
# map and the rendered page cannot drift apart.
# --------------------------------------------------------------------------

CLASSES = [
    {
        "block": "market-snapshot",
        "q": "median home price in {name} San Diego",
        "why": "Fans out of every buy/sell/live query. The most-retrieved fact.",
    },
    {
        "block": "market-snapshot",
        "q": "how fast do homes sell in {name}",
        "why": "Days on market. Seller-side decisive; nobody local publishes it.",
    },
    {
        "block": "market-snapshot",
        "q": "are home prices going up or down in {name}",
        "why": "Direction, not just level. Needs a dated YoY figure.",
    },
    {
        "block": "taxes",
        "q": "does {name} have Mello-Roos and how much",
        "why": "THE question in 92127. Not one competitor page answers it.",
    },
    {
        "block": "taxes",
        "q": "what is the effective property tax rate in {name}",
        "why": "Base + CFD + HOA as one number is what buyers actually need.",
    },
    {
        "block": "taxes",
        "q": "what are HOA fees in {name}",
        "why": "Pairs with Mello-Roos; usually quoted wrong or not at all.",
    },
    {
        "block": "schools",
        "q": "what school district is {name} in",
        "why": "Cheap to answer, high retrieval volume, frequently wrong online.",
    },
    {
        "block": "schools",
        "q": "which schools serve {name} and how are they rated",
        "why": "Named schools are entities; they anchor the page's geo-relevance.",
    },
    {
        "block": "schools",
        "q": "which homes in {name} feed into which high school",
        "why": "Attendance-boundary specificity. The documented competitor gap.",
    },
    {
        "block": "housing-stock",
        "q": "what kind of homes are in {name}",
        "why": "Era, builders, price bands. Portals cannot template this.",
    },
    {
        "block": "commute",
        "q": "how long is the commute from {name} to Sorrento Valley",
        "why": "Recurring Blind/Bogleheads question for the biotech corridor.",
    },
    {
        "block": "living-here",
        "q": "is {name} a good place to live",
        "why": "The head query itself — answer it with facts and tradeoffs, "
        "never with who lives there (Fair Housing, HANDOFF §6).",
    },
    {
        "block": "living-here",
        "q": "pros and cons of living in {name}",
        "why": "The format that already ranks in this market.",
    },
    {
        "block": "track-record",
        "q": "best real estate agent in {name}",
        "why": "Agent-selection fan-out. Answered by the sold record, not a claim.",
    },
]

# --------------------------------------------------------------------------
# Community-specific sub-queries. Every one of these traces to a real thread
# or PAA pattern in research/keywords.md — none are invented.
# --------------------------------------------------------------------------

EXTRA = {
    "del-sur": [
        ("taxes", "when does Mello-Roos end in Del Sur"),
        ("comparison", "Del Sur vs 4S Ranch which is better"),
        ("living-here", "how much hotter is Del Sur than the coast"),
        ("living-here", "what amenities does Del Sur have"),
    ],
    "4s-ranch": [
        ("taxes", "is Mello-Roos in 4S Ranch worth it"),
        ("comparison", "4S Ranch vs Del Sur taxes and amenities"),
        ("living-here", "what can you walk to in 4S Ranch"),
        ("risk", "is 4S Ranch in a fire zone and what about insurance"),
    ],
    "scripps-ranch": [
        ("taxes", "does Scripps Ranch have Mello-Roos"),
        ("schools", "is Scripps Ranch in Poway Unified or San Diego Unified"),
        ("risk", "what is the wildfire risk in Scripps Ranch"),
        ("living-here", "is MCAS Miramar jet noise a problem in Scripps Ranch"),
        ("living-here", "what can you do at Lake Miramar"),
    ],
    "carmel-valley": [
        ("schools", "do Carmel Valley homes fall in the Del Mar Union district"),
        ("schools", "which Carmel Valley homes feed Torrey Pines High School"),
        ("living-here", "why is Carmel Valley so expensive"),
        ("living-here", "how bad is the marine layer in Carmel Valley"),
        ("comparison", "is Pacific Highlands Ranch part of Carmel Valley"),
    ],
    "del-mar": [
        ("housing-stock", "how much more does an ocean view cost in Del Mar"),
        ("regulation", "what does the Coastal Zone mean for remodeling in Del Mar"),
        ("market-snapshot", "why do Del Mar homes sit on the market so long"),
        ("comparison", "Del Mar vs Encinitas vs Solana Beach"),
        ("living-here", "does Del Mar have a train station"),
    ],
    "rancho-santa-fe": [
        ("regulation", "what is the Covenant in Rancho Santa Fe"),
        ("regulation", "how strict is the Rancho Santa Fe Art Jury for remodels"),
        ("housing-stock", "do Rancho Santa Fe homes have sewer or septic"),
        ("market-snapshot", "why do Rancho Santa Fe homes take so long to sell"),
        ("comparison", "Covenant vs The Bridges vs Cielo vs Fairbanks Ranch"),
    ],
}


# North County's community-specific sub-queries are derived from the passages
# that answer them rather than listed twice. `build/data/guides.py` holds both
# the question and its answer, so deriving here makes drift between the two
# impossible: a sub-query cannot exist without a passage answering it.
#
# The six entries above are NOT derived, deliberately. Those came out of the
# keyword research in research/keywords.md — they are observed demand, and
# guides.py was written to answer them. Overwriting them with the questions we
# chose to answer would destroy that provenance and turn an evidence list into
# a self-graded one. They stay as the record of what people actually ask.
from . import guides  # noqa: E402

EXTRA.update({
    slug: [(b["anchor"], b["question"]) for b in blocks]
    for slug, blocks in guides.GUIDES.items()
    if slug not in EXTRA
})


def for_neighborhood(hood: dict) -> list[dict]:
    """Every sub-query a page must answer, with the block that owns it."""
    queries = [
        {"block": c["block"], "q": c["q"].format(**hood), "why": c["why"]}
        for c in CLASSES
    ]
    queries += [
        {"block": block, "q": q, "why": "Community-specific verified demand."}
        for block, q in EXTRA.get(hood["slug"], [])
    ]
    return queries


def required_blocks(hood: dict) -> list[str]:
    """Anchor ids the page must define. Order is the page's section order."""
    seen: list[str] = []
    for item in for_neighborhood(hood):
        if item["block"] not in seen:
            seen.append(item["block"])
    return seen
