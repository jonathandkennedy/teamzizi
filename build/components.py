"""Shared page chrome: <head>, nav, footer, and the page shell.

URL convention: the old Luxury Presence site served paths with **no trailing
slash** (`/neighborhoods/carmel-valley`) and roughly ten of those URLs are
still indexed despite dead DNS. Preserving them exactly is the cheapest SEO
win available, so pages are written as `neighborhoods/carmel-valley.html` and
served extensionless by Vercel's `cleanUrls`. Do not "tidy" this into
trailing slashes — that would 301 away the equity we are rebuilding to keep.
"""

from __future__ import annotations

import hashlib
import html
from functools import lru_cache
from pathlib import Path
from typing import Any

import schema
from data import agents, site

SITE_ROOT = Path(__file__).resolve().parent.parent / "site"


@lru_cache(maxsize=None)
def asset(path: str) -> str:
    """Append a content hash to a CSS/JS URL so changes actually reach people.

    `vercel.json` caches `/assets/(css|js|img)/*` for a week. That is the right
    number for bytes that rarely change, but the filenames never changed with
    them, so a returning visitor kept the stylesheet they already had for up to
    seven days no matter what shipped.

    This is not hypothetical. The /join hero fix went to production and the
    client still saw the broken crop, because their browser was serving the CSS
    it had cached before the fix. The bug was invisible from the server side —
    the file was correct, the deploy was correct, and every check passed.

    Hashing the contents fixes both halves at once: identical bytes produce an
    identical URL and stay cached, changed bytes produce a new URL that no
    cache has ever seen. The week-long lifetime becomes an asset rather than a
    liability.

    Missing files raise rather than silently shipping an unversioned URL — a
    quiet fallback here would reintroduce exactly the failure this exists to
    prevent.
    """
    f = SITE_ROOT / path.lstrip("/")
    if not f.is_file():
        raise SystemExit(f"asset() — no such file: {f}")
    return f"{path}?v={hashlib.sha256(f.read_bytes()).hexdigest()[:8]}"

# Built pages only. Sell / Buy / Concierge were here linking at nothing, so
# the primary navigation on all 43 pages offered three 404s. They come back
# the moment those pages exist — validate.py now fails the build on a dead
# internal link, which is what should have caught this the first time.
NAV_LINKS = [
    ("Neighborhoods", "/neighborhoods"),
    ("Buy", "/buy"),
    ("Sell", "/sell"),
    ("Mello-Roos", "/mello-roos"),
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
    # Bing reads its verification tag at the root and nowhere else, so it ships
    # on the homepage alone rather than on all 87 pages. See site.py.
    bing = (
        f'\n<meta name="msvalidate.01" content="{site.BING_VERIFICATION}">'
        if path == "/" else ""
    )
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">{bing}

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
<link rel="stylesheet" href="{asset('/assets/css/fonts.css')}">
<link rel="stylesheet" href="{asset('/assets/css/tokens.css')}">
<link rel="stylesheet" href="{asset('/assets/css/base.css')}">
<link rel="stylesheet" href="{asset('/assets/css/site.css')}">

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


def picture(
    src: str,
    *,
    alt: str = "",
    width: int,
    height: int,
    cls: str = "",
    eager: bool = False,
    sizes: str = "",
) -> str:
    """<picture> with WebP first and the JPEG as fallback.

    build/optimize.py writes a .webp alongside every photograph. WebP is
    roughly 40-60% smaller than the equivalent JPEG here, and a browser that
    cannot read it silently takes the <img>. Nothing is lost and nobody needs
    a script.

    `eager` marks the LCP candidate: fetchpriority high, no lazy attribute.
    Everything else is lazy and async-decoded, because on a neighborhood page
    the hero is the only image above the fold.
    """
    stem = src.rsplit(".", 1)[0]
    klass = f' class="{cls}"' if cls else ""
    loading = (
        ' fetchpriority="high" decoding="async"'
        if eager
        else ' loading="lazy" decoding="async"'
    )

    # `sizes` is what stops the browser downloading a 1280px file for a 400px
    # card. It is only correct when a narrow rendition exists, which
    # build/optimize.py writes for the directories that need one.
    narrow = Path(SITE_ROOT / f"{stem.lstrip('/')}-800.webp")
    if sizes and narrow.exists():
        webp_set = f"{stem}-800.webp 800w, {stem}.webp {width}w"
        jpeg_set = f"{stem}-800.jpg 800w, {stem}.jpg {width}w"
        return (
            "<picture>"
            f'<source srcset="{webp_set}" sizes="{sizes}" type="image/webp">'
            f'<source srcset="{jpeg_set}" sizes="{sizes}" type="image/jpeg">'
            f'<img{klass} src="{src}" alt="{esc(alt)}" '
            f'width="{width}" height="{height}"{loading}>'
            "</picture>"
        )

    return (
        "<picture>"
        f'<source srcset="{stem}.webp" type="image/webp">'
        f'<img{klass} src="{src}" alt="{esc(alt)}" '
        f'width="{width}" height="{height}"{loading}>'
        "</picture>"
    )


def action_bar(variant: str = "client") -> str:
    """Persistent two-action bar, mobile only.

    The nav phone number is `display: none` below 62rem — so on a phone,
    which is where most of this traffic arrives, there was no persistent way
    to reach anyone. The tel: links existed but were buried mid-page and in
    the footer.

    Two actions, no more. Calling is the high-intent one and goes first; the
    second is the low-commitment one for someone not ready to talk.

    `variant="agent"` swaps that second action on the recruiting pages. A
    home valuation is a *client* offer, and on a page addressed to licensed
    agents it is worse than a wasted slot — it tells the reader the page was
    not written for them. The agent equivalent has to be something they want
    for their own business, which is what the AI visibility check is.
    """
    second = (
        '<a class="actionbar__btn" href="/join#visibility-check">'
        "AI visibility check</a>"
        if variant == "agent"
        else '<a class="actionbar__btn" href="/home-valuation">Home value</a>'
    )
    return f"""<div class="actionbar" role="group" aria-label="Contact Team Azizi">
  <a class="actionbar__btn actionbar__btn--call" href="{site.PHONE_HREF}">
    <span aria-hidden="true">&#9742;</span> Call {site.PHONE_DISPLAY}
  </a>
  {second}
</div>"""


def footer() -> str:
    """Footer NAP must match the (future) GBP exactly — schema, footer and
    GBP are one entity or they are three. Licence numbers and the Compass
    equal-housing / MLS marks are a California DRE requirement, not decoration.
    """
    # Resolved against ALL_AREAS, not NEIGHBORHOODS — the latter is only the
    # original six, which is exactly how the North County guides ended up
    # unreachable from the footer. See site.FOOTER_HOODS.
    hoods = "\n".join(
        [
            f'        <li><a href="/neighborhoods/{slug}">'
            f"{esc(next(a['name'] for a in site.ALL_AREAS if a['slug'] == slug))}"
            f"</a></li>"
            for slug in site.FOOTER_HOODS
        ]
        + [
            f'        <li><a href="/neighborhoods">All {len(site.ALL_AREAS)}'
            f" guides</a></li>"
        ]
    )
    # Only pages that exist. This block previously linked seven — /sell, /buy,
    # /concierge, /testimonials, /blog, /contact, /terms-and-conditions — none
    # of which had been built, so every page on the site shipped seven 404s in
    # its footer. site.FOOTER_EXPLORE is the built set; the rest come back as
    # each page lands.
    explore = "\n".join(
        f'        <li><a href="{href}">{esc(label)}</a></li>'
        for label, href in site.FOOTER_EXPLORE
    )
    # Each named licensee links to their own page, so the DRE number and the
    # person it belongs to are one click apart rather than an orphan string.
    licensees = "<br>\n      ".join(
        f'<a href="/agent/{a["slug"]}">{esc(a["name"])}</a> '
        f"&middot; CA DRE# {a['dre']}"
        for a in (agents.by_slug(s) for s in site.FOOTER_LICENSEES)
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
{explore}
      </ul>
    </div>
  </div>

  <div class="container footer__legal">
    <p class="footer__licence">
      {licensees}<br>
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
    </p>
{powered_by()}
  </div>
</footer>"""


def powered_by() -> str:
    """The CitedRealty build credit, from the badge kit at
    citedrealty.com/powered-by.html.

    Option 2 (inline SVG) of the three offered, for the reason the kit gives —
    it is the one meant for custom builds, and nothing loads from another
    origin, so the badge cannot slow this page down or break when an asset
    moves. That also keeps it consistent with the rule the rest of this site
    is built on: the client owns every byte, with no dependency they can lose.

    Rendered in the kit's light-footer variant, because this footer sits on
    #ffffff — the two text fills are swapped per its instructions
    (#8E8EA8 -> #6B6B85, #F5F5FA -> #14142B). The gradient reads on both.

    Anchor text stays branded, and the placement is once, in the footer,
    which is what the kit asks for and what keeps a build credit reading as
    attribution rather than link building.
    """
    return """    <p class="footer__powered">
      <a href="https://citedrealty.com/" aria-label="Powered by CitedRealty">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 190 44" width="190" height="44"
             role="img" aria-label="Powered by CitedRealty"
             font-family="Inter,'Avenir Next',-apple-system,'Segoe UI',Helvetica,Arial,sans-serif">
          <defs><linearGradient id="cr-pb" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" stop-color="#4F46E5"/><stop offset=".6" stop-color="#8B5CF6"/>
            <stop offset="1" stop-color="#C084FC"/></linearGradient></defs>
          <g transform="translate(4,5) scale(0.303) translate(-46,-48)">
            <path d="M 66 48 h 72 a 20 20 0 0 1 20 20 v 52 a 20 20 0 0 1 -20 20 h -50 l -22 20 v -20 h 0 a 20 20 0 0 1 -20 -20 v -52 a 20 20 0 0 1 20 -20 z" fill="url(#cr-pb)"/>
            <path d="M 102 72 L 128 92 L 128 122 L 76 122 L 76 92 Z" fill="none" stroke="#fff" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
            <path d="M 134 56 q 2 8 10 10 q -8 2 -10 10 q -2 -8 -10 -10 q 8 -2 10 -10 z" fill="#fff"/>
          </g>
          <text x="47" y="18" font-size="8.5" font-weight="600" fill="#6B6B85" letter-spacing="1.3">POWERED BY</text>
          <text x="47" y="36" font-size="18" font-weight="700" fill="#14142B" letter-spacing="-.4">Cited<tspan fill="url(#cr-pb)">Realty</tspan><tspan dx="2" dy="-7" font-size="9" letter-spacing="0" fill="url(#cr-pb)">[1]</tspan></text>
        </svg>
      </a>
    </p>"""


def page(
    *,
    title: str,
    description: str,
    path: str,
    body: str,
    nodes: list[dict[str, Any]],
    hero: bool | str = False,
    og_image: str = "/assets/img/logos/og-default.png",
    audience: str = "client",
) -> str:
    """`hero=True` tells the nav to start transparent over a full-bleed hero.

    `hero="light"` is the same full-bleed treatment over a *light* hero — the
    fact plates on communities with no photograph. Without it the nav renders
    white-on-cream and is effectively invisible, which is an accessibility
    failure rather than a cosmetic one.
    """
    body_class = ""
    if hero == "light":
        body_class = ' class="has-hero has-hero--light"'
    elif hero:
        body_class = ' class="has-hero"'
    return f"""<!doctype html>
<html lang="en-US">
<head>
{head(title=title, description=description, path=path, nodes=nodes, og_image=og_image)}
</head>
<body{body_class}>
<a class="skip-link" href="#main">Skip to content</a>
{nav(current=path)}
<main id="main">
{body}
</main>
{footer()}
{action_bar(variant=audience)}
<script src="{asset('/assets/js/site.js')}" defer></script>
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
        picture(agent["photo"], alt=agent["name"], width=200, height=200,
                cls="expert__photo")
        if agent.get("photo")
        else '<div class="expert__photo expert__photo--pending"></div>'
    )
    dre = (
        f'<span class="expert__dre">CA DRE# {agent["dre"]}</span>'
        if agent.get("dre")
        else ""
    )
    # Not "team lead" any more: the fallback rotates across the three Azizi
    # licensees, and Sofia and Zohra are not the team lead. Saying so would
    # be a plain factual error on two thirds of the guides.
    role = (
        f"Your {esc(hood['name'])} specialist"
        if confirmed
        else f"Team Azizi &middot; covering {esc(hood['name'])}"
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
