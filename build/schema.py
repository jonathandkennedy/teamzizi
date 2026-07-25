"""JSON-LD graph builders.

Design rule: **no JSON-LD is ever hand-written as a string.** Every block is
built as a Python dict and serialised with `json.dumps`, which makes the
missing-brace failure that took out CitedRealty's homepage graph structurally
impossible rather than merely unlikely. validate.py re-parses every emitted
block anyway, because a rule you don't test is a wish.

Everything here is server-rendered into the HTML: AI fetchers and `curl` do
not run JavaScript, so JS-injected schema is invisible to exactly the
consumers this site is built for (research/aiPlaybook.md §3.4).
"""

from __future__ import annotations

import json
from typing import Any

from data import site

BUSINESS_ID = f"{site.DOMAIN}/#business"
ORG_ID = f"{site.DOMAIN}/#organization"
WEBSITE_ID = f"{site.DOMAIN}/#website"


def _postal_address() -> dict[str, Any]:
    return {
        "@type": "PostalAddress",
        "streetAddress": site.STREET,
        "addressLocality": site.CITY,
        "addressRegion": site.REGION,
        "postalCode": site.POSTAL,
        "addressCountry": site.COUNTRY,
    }


def _area_served() -> list[dict[str, Any]]:
    """One entry per neighborhood, with a Wikipedia sameAs where an article
    genuinely exists. Del Sur has none; we leave it off rather than invent one.
    """
    areas: list[dict[str, Any]] = []
    for hood in site.NEIGHBORHOODS:
        entry: dict[str, Any] = {
            "@type": "Place",
            "name": f"{hood['name']}, {site.CITY}, {site.REGION}",
        }
        if hood["wikipedia"]:
            entry["sameAs"] = hood["wikipedia"]
        areas.append(entry)
    return areas


def _offer_catalog() -> dict[str, Any]:
    return {
        "@type": "OfferCatalog",
        "name": "Real Estate Services",
        "itemListElement": [
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": svc["name"],
                    "description": svc["description"],
                },
            }
            for svc in site.SERVICES
        ],
    }


def business() -> dict[str, Any]:
    """The main entity. `RealEstateAgent` is the most specific LocalBusiness
    subtype for this vertical, which is what the schema skill prescribes.

    Deliberately absent: `aggregateRating`. Self-serving review markup earns
    no stars and we have no verified count — HANDOFF §6, no fabrication.
    """
    return {
        "@type": "RealEstateAgent",
        "@id": BUSINESS_ID,
        "name": site.NAME,
        "alternateName": site.NAME_LONG,
        "url": f"{site.DOMAIN}/",
        "email": site.EMAIL,
        "telephone": site.PHONE_SCHEMA,
        "image": f"{site.DOMAIN}/assets/img/logos/logo-dark.png",
        "logo": f"{site.DOMAIN}/assets/img/logos/logo-dark.png",
        "address": _postal_address(),
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": site.GEO["lat"],
            "longitude": site.GEO["lon"],
        },
        "areaServed": _area_served(),
        "hasOfferCatalog": _offer_catalog(),
        "priceRange": "$$$$",
        "sameAs": list(site.SAME_AS),
        "parentOrganization": {
            "@type": "Organization",
            "name": site.BROKERAGE,
        },
    }


def organization() -> dict[str, Any]:
    """Wraps the team so individual agent pages can hang off it via
    `department`, which is the linking pattern the schema skill prescribes for
    multi-entity sites.
    """
    return {
        "@type": "Organization",
        "@id": ORG_ID,
        "name": site.NAME,
        "url": f"{site.DOMAIN}/",
        "logo": f"{site.DOMAIN}/assets/img/logos/logo-dark.png",
        "sameAs": list(site.SAME_AS),
    }


def website() -> dict[str, Any]:
    return {
        "@type": "WebSite",
        "@id": WEBSITE_ID,
        "url": f"{site.DOMAIN}/",
        "name": site.NAME,
        "publisher": {"@id": ORG_ID},
        "inLanguage": "en-US",
    }


def breadcrumbs(trail: list[tuple[str, str]]) -> dict[str, Any]:
    """`trail` is [(label, absolute_url), ...] from Home to the current page."""
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i,
                "name": label,
                "item": url,
            }
            for i, (label, url) in enumerate(trail, start=1)
        ],
    }


def faq_page(questions: list[dict[str, str]]) -> dict[str, Any]:
    """FAQ rich results were dropped in 2026 — this is kept purely as an
    AI-parsing aid, and we say so honestly to the client rather than selling
    it as a rich-result play.
    """
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q["q"],
                "acceptedAnswer": {"@type": "Answer", "text": q["a"]},
            }
            for q in questions
        ],
    }


def neighborhood_service(hood: dict[str, Any]) -> dict[str, Any]:
    """Neighborhoods are service areas, not offices. Modelling them as
    `Service` + `areaServed` avoids inventing per-neighborhood business
    entities with addresses that do not exist.
    """
    area: dict[str, Any] = {
        "@type": "Place",
        "name": f"{hood['name']}, {site.CITY}, {site.REGION}",
    }
    if hood["wikipedia"]:
        area["sameAs"] = hood["wikipedia"]

    return {
        "@type": "Service",
        "@id": f"{site.DOMAIN}/neighborhoods/{hood['slug']}#service",
        "serviceType": "Real Estate Services",
        "name": f"{hood['name']} Real Estate Services",
        "provider": {"@id": BUSINESS_ID},
        "areaServed": area,
    }


def agent_id(slug: str) -> str:
    return f"{site.DOMAIN}/agent/{slug}#person"


def agent(person: dict[str, Any], *, hood: dict[str, Any] | None = None) -> dict[str, Any]:
    """Per-agent `Person` markup, tied to the neighborhood they farm.

    `areaServed` on the Person is what turns a roster entry into a local
    specialist as far as the graph is concerned: the licence number makes them
    checkable, and the area makes them checkable *about somewhere*. That pair
    is the authorship signal an assistant needs before it will name a person.

    Note for the client report: the local-schema skill does not prescribe
    Person markup for individual agents — this is a deliberate extension, and
    it is labelled as such rather than presented as best practice.
    """
    node: dict[str, Any] = {
        "@type": "Person",
        "@id": agent_id(person["slug"]),
        "name": person["name"],
        "url": f"{site.DOMAIN}/agent/{person['slug']}",
        "jobTitle": person["title"],
        "worksFor": {"@id": ORG_ID},
        "memberOf": {"@id": BUSINESS_ID},
    }
    if person.get("dre"):
        node["identifier"] = {
            "@type": "PropertyValue",
            "propertyID": "CA DRE License",
            "value": person["dre"],
        }
    if person.get("photo"):
        node["image"] = f"{site.DOMAIN}{person['photo']}"
    if person.get("phone"):
        node["telephone"] = person["phone"]
    if person.get("compass"):
        node["sameAs"] = [f"https://www.compass.com/agents/{person['compass']}/"]
    if hood:
        area: dict[str, Any] = {
            "@type": "Place",
            "name": f"{hood['name']}, {site.CITY}, {site.REGION}",
        }
        if hood.get("wikipedia"):
            area["sameAs"] = hood["wikipedia"]
        node["areaServed"] = area
        node["knowsAbout"] = f"{hood['name']} real estate"
    return node


def web_page(
    *,
    url: str,
    name: str,
    author_slug: str,
    updated: str,
    about: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """`WebPage` carrying explicit authorship and a visible-matching date.

    Author bylines and dated content are named citation-credibility signals
    (research/contentPlaybook.md §8). `dateModified` must match the updated
    date rendered on the page — a schema date that disagrees with the visible
    one is worse than no date at all.
    """
    node: dict[str, Any] = {
        "@type": "WebPage",
        "@id": f"{url}#webpage",
        "url": url,
        "name": name,
        "isPartOf": {"@id": WEBSITE_ID},
        "author": {"@id": agent_id(author_slug)},
        "publisher": {"@id": ORG_ID},
        "dateModified": updated,
    }
    if about:
        node["about"] = about
    return node


def image(
    *,
    url: str,
    caption: str,
    hood: dict[str, Any] | None = None,
    credit: str | None = None,
) -> dict[str, Any]:
    """`ImageObject` with `contentLocation`.

    Localized imagery is a first-hand signal the May 2026 core update rewards,
    and no competitor publishes real neighborhood imagery at all. This makes
    the image assert its own geography rather than inheriting it from whatever
    page happens to embed it — which is what lets it surface independently in
    image search and Lens.

    `credit` is for licensed stock. Stating it costs nothing and keeps the
    site's one real asset — being checkable — intact.
    """
    node: dict[str, Any] = {
        "@type": "ImageObject",
        "@id": f"{url}#image",
        "contentUrl": url,
        "caption": caption,
    }
    if hood:
        location: dict[str, Any] = {
            "@type": "Place",
            "name": f"{hood['name']}, {site.CITY}, {site.REGION}",
        }
        if hood.get("wikipedia"):
            location["sameAs"] = hood["wikipedia"]
        node["contentLocation"] = location
    if credit:
        node["creditText"] = credit
    else:
        node["copyrightHolder"] = {"@id": ORG_ID}
    return node


def render(nodes: list[dict[str, Any]]) -> str:
    """Serialise a list of nodes as one `@graph` block.

    One block per page keeps `@id` references resolvable and makes the
    pre-push validation a single parse rather than a hunt.
    """
    payload = {"@context": "https://schema.org", "@graph": nodes}
    body = json.dumps(payload, indent=2, ensure_ascii=False)
    return f'<script type="application/ld+json">\n{body}\n</script>'
