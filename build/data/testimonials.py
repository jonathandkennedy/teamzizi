"""Client testimonials — empty until real ones are supplied.

HOW TO FILL THIS IN
-------------------
Each agent can see their own reviews at zillow.com/profile/<their-handle>
while logged in. Copy them across verbatim — wording, first name, month and
year. Do not tidy the prose: a testimonial that reads like marketing copy is
worth less than one that reads like a person.

    ENTRIES = [
        {
            "quote": "…exactly as the client wrote it…",
            "name": "Sarah M.",              # first name + initial is fine
            "agent": "nilab-azizi",          # must be a roster slug
            "hood": "escondido",             # optional; must be an area slug
            "date": "2025-08",               # YYYY-MM, as shown on the source
            "source": "Zillow",
            "source_url": "https://www.zillow.com/profile/nilabazizi",
        },
    ]

WHY THERE IS NO REVIEW SCHEMA ON THIS
-------------------------------------
Two Google policies apply, and both are explicit:

  "Don't aggregate reviews or ratings from other websites."

  "If the entity that's being reviewed controls the reviews about itself,
   their pages that use LocalBusiness or any other type of Organization
   structured data are ineligible for star review feature."

    https://developers.google.com/search/docs/appearance/structured-data/review-snippet

So testimonials copied from Zillow get **no** `Review` node and **no**
`aggregateRating` — not as an oversight, as compliance. Marking them up
would be a policy violation that risks structured-data action against the
whole domain, in exchange for stars that would not be granted anyway.

They still earn their place: they convert human readers, and each one links
to the source profile so a reader can verify it rather than trust us. That
is the same standard every other number on this site is held to.

WHAT MUST NOT HAPPEN HERE
-------------------------
No invented testimonials. No composite "typical client" quotes. No lightly
reworded versions of someone else's words. If this list is empty, the
/testimonials page is not generated at all — an empty testimonials page is
worse than none, and a fabricated one ends the engagement.
"""

from __future__ import annotations

# Nothing yet. See the docstring above before adding anything.
ENTRIES: list[dict[str, str]] = []

# Zillow blocks automated access (HTTP 403) and its terms prohibit scraping,
# so these cannot be collected programmatically. They come from the agents'
# own logged-in profiles, by hand. That is the only route, and it is also the
# one that keeps the client on the right side of Zillow's terms.
COLLECTION_NOTE = (
    "Collected by hand from each agent's own Zillow profile. Zillow returns "
    "403 to automated requests and its terms prohibit scraping."
)


def for_agent(slug: str) -> list[dict[str, str]]:
    return [t for t in ENTRIES if t.get("agent") == slug]


def for_hood(slug: str) -> list[dict[str, str]]:
    return [t for t in ENTRIES if t.get("hood") == slug]
