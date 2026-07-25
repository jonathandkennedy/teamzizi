"""Shared page chrome: <head>, nav, footer, and the page shell.

URL convention: the old Luxury Presence site served paths with **no trailing
slash** (`/neighborhoods/carmel-valley`) and roughly ten of those URLs are
still indexed despite dead DNS. Preserving them exactly is the cheapest SEO
win available, so pages are written as `neighborhoods/carmel-valley.html` and
served extensionless by Vercel's `cleanUrls`. Do not "tidy" this into
trailing slashes — that would 301 away the equity we are rebuilding to keep.
"""

from __future__ import annotations

import html
from typing import Any

import schema
from data import site

NAV_LINKS = [
    ("Neighborhoods", "/neighborhoods"),
    ("Properties", "/properties/sale"),
    ("Sell", "/sell"),
    ("Buy", "/buy"),
    ("Concierge", "/concierge"),
    ("Team", "/team"),
    ("Contact", "/contact"),
]


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def head(
    *,
    title: str,
    description: str,
    path: str,
    nodes: list[dict[str, Any]],
    og_image: str = "/assets/img/logos/og-default.png",
) -> str:
    canonical = f"{site.DOMAIN}{path}"
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">

<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(site.NAME)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{site.DOMAIN}{og_image}">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="/assets/img/logos/monogram.png" type="image/png">
<link rel="preload" href="/assets/fonts/reem-kufi-fun-400.woff2" as="font"
      type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/lato-400.woff2" as="font"
      type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/fonts.css">
<link rel="stylesheet" href="/assets/css/tokens.css">
<link rel="stylesheet" href="/assets/css/base.css">
<link rel="stylesheet" href="/assets/css/site.css">

{schema.render(nodes)}"""


def nav(current: str = "") -> str:
    """Transparent over the hero, solid white on scroll with a logo swap —
    both logo variants ship in the markup and CSS toggles them, so there is
    no flash and no JS dependency for the initial paint.
    """
    rows = []
    for label, href in NAV_LINKS:
        aria = ' aria-current="page"' if href == current else ""
        rows.append(f'      <li><a href="{href}"{aria}>{esc(label)}</a></li>')
    items = "\n".join(rows)
    return f"""<header class="nav" id="nav" data-nav>
  <div class="nav__inner container container--wide">
    <a class="nav__logo" href="/" aria-label="{esc(site.NAME)} — home">
      <img class="nav__logo-light" src="/assets/img/logos/logo-light.png"
           alt="{esc(site.NAME)} | Compass" width="200" height="49">
      <img class="nav__logo-dark" src="/assets/img/logos/logo-dark.png"
           alt="" aria-hidden="true" width="200" height="49">
    </a>

    <nav class="nav__links" aria-label="Primary">
      <ul>
{items}
      </ul>
    </nav>

    <div class="nav__actions">
      <a class="nav__phone" href="{site.PHONE_HREF}">{site.PHONE_DISPLAY}</a>
      <button class="nav__toggle" type="button" data-drawer-open
              aria-expanded="false" aria-controls="drawer">
        <span class="visually-hidden">Open menu</span>
        <span class="nav__bars" aria-hidden="true"></span>
      </button>
    </div>
  </div>
</header>

<div class="drawer" id="drawer" data-drawer hidden>
  <div class="drawer__panel">
    <button class="drawer__close" type="button" data-drawer-close>
      <span class="visually-hidden">Close menu</span>
      <span aria-hidden="true">&times;</span>
    </button>
    <nav aria-label="All pages">
      <ul>
{items}
      </ul>
    </nav>
    <a class="drawer__phone" href="{site.PHONE_HREF}">{site.PHONE_DISPLAY}</a>
  </div>
</div>"""


def footer() -> str:
    """Footer NAP must match the (future) GBP exactly — schema, footer and
    GBP are one entity or they are three. Licence numbers and the Compass
    equal-housing / MLS marks are a California DRE requirement, not decoration.
    """
    hoods = "\n".join(
        f'        <li><a href="/neighborhoods/{slug}">'
        f"{esc(next(h['name'] for h in site.NEIGHBORHOODS if h['slug'] == slug))}"
        f"</a></li>"
        for slug in site.NAV_ORDER
    )
    return f"""<footer class="footer">
  <div class="container footer__grid">

    <div class="footer__brand">
      <img src="/assets/img/logos/logo-dark.png" alt="{esc(site.NAME)} | Compass"
           width="240" height="58" loading="lazy">
      <p class="footer__tagline">Who Represents You Matters</p>
    </div>

    <div class="footer__nap">
      <h2 class="footer__heading">Get In Touch</h2>
      <address>
        <a href="{site.PHONE_HREF}">{site.PHONE_DISPLAY}</a><br>
        <a href="mailto:{site.EMAIL}">{site.EMAIL}</a><br>
        <span>{esc(site.STREET)}<br>{esc(site.CITY)}, {site.REGION} {site.POSTAL}</span>
      </address>
    </div>

    <div class="footer__nav">
      <h2 class="footer__heading">Neighborhoods</h2>
      <ul>
{hoods}
      </ul>
    </div>

    <div class="footer__nav">
      <h2 class="footer__heading">Explore</h2>
      <ul>
        <li><a href="/sell">Sell Your Home</a></li>
        <li><a href="/buy">Buy a Home</a></li>
        <li><a href="/concierge">Compass Concierge</a></li>
        <li><a href="/team">Meet the Team</a></li>
        <li><a href="/testimonials">Testimonials</a></li>
        <li><a href="/blog">Blog</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </div>
  </div>

  <div class="container footer__legal">
    <p class="footer__licence">
      {esc(site.LEAD_AGENT)} &middot; CA DRE# {site.LEAD_DRE}<br>
      {esc(site.BROKERAGE)} &middot; CA DRE# {site.BROKERAGE_DRE}
    </p>
    <p class="footer__disclaimer">{esc(site.DISCLAIMER)}</p>
    <div class="footer__marks">
      <img src="/assets/img/compliance/realtor-eho.png"
           alt="REALTOR and Equal Housing Opportunity" width="178" height="92"
           loading="lazy">
      <img src="/assets/img/compliance/san-diego-mls.png"
           alt="San Diego MLS" width="200" height="22" loading="lazy">
    </div>
    <p class="footer__copyright">
      &copy; <span data-year>2026</span> {esc(site.NAME)}.
      <a href="/terms-and-conditions">Privacy Policy</a>
    </p>
  </div>
</footer>"""


def page(
    *,
    title: str,
    description: str,
    path: str,
    body: str,
    nodes: list[dict[str, Any]],
    hero: bool = False,
) -> str:
    """`hero=True` tells the nav to start transparent over a full-bleed hero."""
    return f"""<!doctype html>
<html lang="en-US">
<head>
{head(title=title, description=description, path=path, nodes=nodes)}
</head>
<body{' class="has-hero"' if hero else ""}>
<a class="skip-link" href="#main">Skip to content</a>
{nav(current=path)}
<main id="main">
{body}
</main>
{footer()}
<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""


def base_nodes() -> list[dict[str, Any]]:
    """Entity nodes that belong on every page."""
    return [schema.business(), schema.organization(), schema.website()]


# --------------------------------------------------------------------------
# Fan-out primitives
# --------------------------------------------------------------------------

# Openers that make a passage useless once it is lifted out of the page.
# validate.py rejects a lead answer starting with any of these.
ANAPHORA = (
    "it ", "it's", "its ", "they ", "they're", "this ", "that ", "these ",
    "those ", "there ", "there's", "here ", "he ", "she ", "as mentioned",
    "as noted", "as above", "additionally", "however,", "also,",
)


def expert_block(agent: dict[str, Any], hood: dict[str, Any], *, confirmed: bool) -> str:
    """The named licensee who owns a neighborhood.

    This is the single strongest E-E-A-T element on a neighborhood page: a real
    person, a licence number anyone can look up on the DRE site, a direct line,
    and a stated area. A company byline cannot do that work.

    When the assignment is unconfirmed the page falls back to the team lead and
    says so plainly rather than implying a specialism nobody has claimed.
    """
    photo = (
        f'<img class="expert__photo" src="{agent["photo"]}" '
        f'alt="{esc(agent["name"])}" width="200" height="200" loading="lazy">'
        if agent.get("photo")
        else '<div class="expert__photo expert__photo--pending"></div>'
    )
    dre = (
        f'<span class="expert__dre">CA DRE# {agent["dre"]}</span>'
        if agent.get("dre")
        else ""
    )
    role = (
        f"Your {esc(hood['name'])} specialist"
        if confirmed
        else f"Team lead &middot; covering {esc(hood['name'])}"
    )
    tel = "tel:+1" + agent["phone"].replace(".", "")
    return f"""<aside class="expert">
  {photo}
  <div class="expert__body">
    <p class="expert__role">{role}</p>
    <p class="expert__name">{esc(agent['name'])}</p>
    <p class="expert__meta">{esc(agent['title'])}<br>{dre}</p>
    <div class="cta-row">
      <a class="btn btn--dark btn--sm" href="{tel}">{esc(agent['phone'])}</a>
      <a class="btn btn--dark btn--sm" href="/agent/{agent['slug']}">Profile</a>
    </div>
  </div>
</aside>"""


def byline(agent: dict[str, Any], updated: str) -> str:
    """Visible author + updated date. The date must match `dateModified` in
    the schema — a schema date contradicting the visible one is worse than
    shipping no date."""
    licence = f", CA DRE# {agent['dre']}" if agent.get("dre") else ""
    return (
        '<p class="updated">Written by '
        f'<a href="/agent/{agent["slug"]}">{esc(agent["name"])}</a>'
        f"{licence} &middot; Updated {updated}</p>"
    )


def answer_block(
    *,
    anchor: str,
    question: str,
    lead: str,
    body: str = "",
    heading: str = "h3",
) -> str:
    """One passage that fully answers one fan-out sub-query.

    `question` is the sub-query in the words a person would use — it becomes
    the heading, because the heading is what tells a retriever what the
    passage is for.

    `lead` must stand completely alone: no pronoun opener, and it has to name
    the place. It will be read out of context, because out of context is the
    only way an AI Mode sub-query ever reads it.

    `anchor` gives the passage a stable fragment URL, so it can be linked and
    cited as a passage rather than as "somewhere on this page".
    """
    extra = f"\n  {body}" if body else ""
    return f"""<section class="answer" id="{anchor}">
  <{heading} class="answer__q">{esc(question)}</{heading}>
  <p class="answer__lead">{lead}</p>{extra}
</section>"""
