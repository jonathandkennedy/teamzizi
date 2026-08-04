"""Site generator.

    python3 build/generate.py

Writes static HTML into site/. Output is committed — there is no build step
on the host, which is the point: the client can open any file in this repo
and read their own website.

Run build/validate.py before every push.
"""

from __future__ import annotations

import re
import sys
from datetime import date
from html import unescape
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

sys.path.insert(0, str(Path(__file__).parent))

import components as c  # noqa: E402
import schema  # noqa: E402
import textures  # noqa: E402
from data import agents, guides, photos, posts, resources, site, taxes, testimonials  # noqa: E402

SITE = Path(__file__).resolve().parent.parent / "site"
TODAY = date.today().isoformat()

# Pages written so far, for the sitemap. (path, changefreq, priority)
PAGES: list[tuple[str, str, str]] = []

# Paths whose rendered HTML is byte-identical to the previous build. Their
# sitemap `lastmod` must not move — see build_sitemap().
UNCHANGED: set[str] = set()


def write(path: str, html: str, *, changefreq="monthly", priority="0.6") -> None:
    target = SITE / (f"{path.strip('/')}.html" if path.strip("/") else "index.html")
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.read_text(encoding="utf-8") == html:
        # Identical output. Skip the write so the file mtime stays put too.
        UNCHANGED.add(path)
    else:
        target.write_text(html, encoding="utf-8")
    PAGES.append((path, changefreq, priority))
    print(f"  {target.relative_to(SITE.parent)}")


def hood(slug: str) -> dict:
    return next(h for h in site.ALL_AREAS if h["slug"] == slug)


# Carmel Valley and 4S Ranch were removed from the recovered asset set: the
# archived images depict Carmel Valley, Monterey County and a mid-century
# suburb respectively. An honest placeholder beats a wrong-place photograph
# on the page whose entire SEO problem is being confused with Monterey.
HOOD_IMAGE_MISSING = ({"carmel-valley", "4s-ranch"} | {
    a["slug"] for a in site.NORTH_COUNTY
} | {
    a["slug"] for a in site.SD_CITY
} | {
    a["slug"] for a in site.EAST_SOUTH
} | {
    a["slug"] for a in site.SW_RIVERSIDE
}) - set(photos.CREDITS)


# --------------------------------------------------------------------------
# Homepage
# --------------------------------------------------------------------------


def hood_card(slug: str) -> str:
    """A neighborhood card leads with the place and names the human who owns
    it. "Del Sur — Nilab Azizi" is a different proposition from "Del Sur"."""
    h = hood(slug)
    agent, confirmed = agents.for_neighborhood(slug)
    if slug in HOOD_IMAGE_MISSING:
        media = '<div class="card__media card__media--pending"></div>'
    else:
        media = (
            '<div class="card__media">'
            + c.picture(
                f"/assets/img/neighborhoods/{slug}.jpg", width=1280, height=800,
                sizes="(min-width: 62rem) 30vw, (min-width: 40rem) 45vw, 92vw",
            )
            + '<span class="card__overlay"><span class="btn btn--light btn--sm">'
            "Explore</span></span>"
            "</div>"
        )
    who = (
        f"{c.esc(agent['name'])} &middot; {h['zip']}"
        if confirmed
        else f"{h['zip']} &middot; {c.esc(h['district'])}"
    )
    return f"""      <a class="card" href="/neighborhoods/{slug}">
        {media}
        <span class="card__title">{c.esc(h['name'])}</span>
        <span class="card__meta">{who}</span>
      </a>"""


def stat(value: str, label: str) -> str:
    return (
        '      <div class="stat">\n'
        f'        <p class="stat__value">{c.esc(value)}</p>\n'
        f'        <p class="stat__label">{c.esc(label)}</p>\n'
        "      </div>"
    )


def build_home() -> None:
    path = "/"
    # Six cards, chosen by the sold record rather than by aspiration. The full
    # set lives on /neighborhoods; the homepage leads with the communities the
    # team can actually evidence, which is why Escondido is first.
    featured = sorted(
        (s for s in SOLD_RECORD if SOLD_RECORD[s]),
        key=lambda s: -SOLD_RECORD[s],
    )[:6]
    cards = "\n".join(hood_card(slug) for slug in featured)
    stats = "\n".join(
        [
            stat(site.PROOF["volume_2025"], "2025 sales volume"),
            stat(site.PROOF["sides_2025"], "2025 transaction sides"),
            # "#1 in Del Mar by sides" pulled 2026-07-25 — likely an
            # artifact of RealTrends' business-city assignment, not market
            # share (six Del Mar sales in the whole Compass record).
            # research/salesRecord.md §2. SDBJ top-10 is specific and safe.
            stat("Top 10", "Team in San Diego County"),
            stat(site.PROOF["list_rank"], "Large team in California"),
        ]
    )

    body = f"""<section class="hero">
  {c.picture("/assets/img/backgrounds/hero-poster.jpg", width=1920, height=2880,
             cls="hero__media", eager=True)}
  <div class="hero__inner">
    <h1>{c.esc(site.NAME)}</h1>
    <p class="hero__sub">Who Represents You Matters</p>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn--light" href="/neighborhoods">Neighborhood guides</a>
      <a class="btn btn--light" href="/home-valuation">What's my home worth?</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container" style="text-align:center">
    <p class="eyebrow">San Diego County &amp; the Temecula Valley</p>
    <h2>From the coast to the corridor</h2>
    <p class="lede" style="margin-inline:auto">
      Team Azizi represents buyers and sellers across {len(site.ALL_AREAS)}
      communities &mdash; the coast from La&nbsp;Jolla to Oceanside, the
      urban core, East County and the South Bay, inland through Escondido
      and the backcountry, and up the I&#8209;15 into the Temecula Valley
      &mdash; from the Compass office at {c.esc(site.STREET)} in
      Carmel&nbsp;Valley.
    </p>

    <div class="stats">
{stats}
    </div>
    <p class="stats__source">
      {site.PROOF['list_rank']} of all California large teams by volume on
      <a href="{site.PROOF['source_url']}" rel="nofollow noopener"
      target="_blank">{c.esc(site.PROOF['list_name'])}</a>, RealTrends
      Verified &mdash; reporting 2025 production. Named one of the top 10
      real estate teams in the county by the San&nbsp;Diego Business
      Journal, October 2025.
      Every figure on this site is third-party verifiable; none of them
      require taking our word for it.
    </p>
  </div>
</section>

<section class="section section--panel">
  <div class="container">
    <p class="eyebrow">Neighborhood guides</p>
    <h2 class="rule-gold">{len(site.ALL_AREAS)} communities, in depth</h2>
    <p>
      Each guide carries the Mello-Roos position for that community traced to
      the County Auditor&rsquo;s active district list, which district assigns
      the schools and where the boundaries actually run, and what we have sold
      there &mdash; not a search widget and a paragraph. The six below are the
      ones where our transaction record runs deepest.
    </p>
    <div class="grid grid--3" style="margin-top:2.5rem">
{cards}
    </div>
    <p style="margin-top:2rem">
      <a class="btn" href="/neighborhoods">All {len(site.ALL_AREAS)} neighborhood guides</a>
    </p>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split__media">
      {c.picture("/assets/img/team/team-group.jpg", alt="The Team Azizi team",
               width=1920, height=1528)}
    </div>
    <div class="split__body">
      <p class="eyebrow">Meet the team</p>
      <h2>A family team, {site.PROOF['closed_sales']} closed sales</h2>
      <p>
        Team Azizi was founded by Sonia Azizi and is led today by
        {c.esc(site.LEAD_AGENT)}. The team works the full price spectrum
        across San Diego County &mdash; first homes through estates &mdash;
        which is why the guides here talk about tax districts and school
        boundaries rather than lifestyle adjectives.
      </p>
      <div class="cta-row">
        <a class="btn btn--dark" href="/team">Meet the team</a>
      </div>
    </div>
  </div>
</section>

<section class="band band--heavy">
  {c.picture("/assets/img/backgrounds/work-with-us.jpg", width=1920, height=1200, cls="band__media")}
  <div class="container">
    <h2 class="rule-center">Work With Us</h2>
    <p style="margin-inline:auto">
      Whether you are selling a Del Mar bluff-top home or buying your first
      place in Del Sur, the work is the same: honest pricing, real
      preparation, and a negotiation run by someone who has done it here
      before.
    </p>
    <div class="cta-row">
      <a class="btn btn--light" href="/contact">Contact us</a>
      <a class="btn btn--light" href="{site.PHONE_HREF}">{site.PHONE_DISPLAY}</a>
    </div>
  </div>
</section>"""

    nodes = c.base_nodes() + [
        schema.breadcrumbs([("Home", f"{site.DOMAIN}/")]),
    ]

    write(
        path,
        c.page(
            title=(
                "North San Diego Real Estate — Carmel Valley, Del Mar & "
                "Rancho Santa Fe | Team Azizi"
            ),
            description=(
                "Team Azizi is a Compass team serving Carmel Valley, Del Mar, "
                "Rancho Santa Fe, Del Sur, 4S Ranch and Scripps Ranch. "
                f"{site.PROOF['volume_2025']} in 2025 sales, "
                f"{site.PROOF['sides_2025']} sides, #1 in Del Mar by sides. "
                f"Call {site.PHONE_DISPLAY}."
            ),
            path=path,
            body=body,
            nodes=nodes,
            hero=True,
            og_image="/assets/img/og/home.jpg",
        ),
        changefreq="weekly",
        priority="1.0",
    )


# --------------------------------------------------------------------------
# Neighborhoods hub
# --------------------------------------------------------------------------


def build_neighborhood_hub() -> None:
    path = "/neighborhoods"
    corridor = "\n".join(hood_card(slug) for slug in site.NAV_ORDER)
    north = "\n".join(hood_card(slug) for slug in site.NORTH_COUNTY_ORDER)
    sd_city = "\n".join(hood_card(slug) for slug in site.SD_CITY_ORDER)
    east_south = "\n".join(hood_card(slug) for slug in site.EAST_SOUTH_ORDER)
    riverside = "\n".join(hood_card(slug) for slug in site.SW_RIVERSIDE_ORDER)
    total = len(site.ALL_AREAS)

    body = f"""<section class="band band--hero" style="padding-top:calc(var(--nav-h) + 4rem)">
  {c.picture("/assets/img/neighborhoods/_hub-hero.jpg", width=1920, height=1440,
             cls="band__media", eager=True)}
  <div class="container">
    <h1>San Diego County &amp; Temecula Valley Neighborhood Guides</h1>
    <p style="margin-inline:auto">
      {total} communities &mdash; from La Jolla and the Chula Vista bayfront
      to the Ramona backcountry, and up the I-15 to Temecula.
    </p>
  </div>
</section>

<section class="section">
  <div class="container">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; Neighborhoods
    </nav>
    <h2 class="rule-gold">Choose a community</h2>
    <p class="lede">
      These guides are maintained, not published once and abandoned. Each one
      carries the Mello-Roos position for that community traced to the County
      Auditor&rsquo;s active district list, which district assigns the schools
      and how the boundaries actually run, and what Team Azizi has actually
      done there &mdash; including where that record is thin.
    </p>

    <h3 id="north-county" class="rule-gold" style="margin-top:3rem">
      North County
    </h3>
    <p>
      Inland and coastal North County &mdash; Escondido out to Ramona, and
      the coast from Oceanside down to Encinitas. This is where the largest
      part of the team&rsquo;s transaction history sits.
    </p>
    <div class="grid grid--3" style="margin-top:2rem">
{north}
    </div>

    <h3 id="i15-corridor" class="rule-gold" style="margin-top:3.5rem">
      The I&#8209;15 corridor and the coast
    </h3>
    <p>
      The 92127 master-planned communities, Scripps Ranch, and the coastal
      stretch from Carmel Valley through Del Mar to Rancho Santa Fe.
    </p>
    <div class="grid grid--3" style="margin-top:2rem">
{corridor}
    </div>

    <h3 id="san-diego-city" class="rule-gold" style="margin-top:3.5rem">
      San Diego &mdash; the city neighborhoods
    </h3>
    <p>
      From La Jolla down the coast to Ocean Beach and through the urban core
      &mdash; communities of the City of San Diego, where the governing facts
      are city rules: the coastal height limit, the STRO rental tiers,
      historic districts, and plan amendments that redraw what a lot can
      hold.
    </p>
    <div class="grid grid--3" style="margin-top:2rem">
{sd_city}
    </div>

    <h3 id="east-county-south-bay" class="rule-gold" style="margin-top:3.5rem">
      East County &amp; South Bay
    </h3>
    <p>
      Santee, El Cajon, Spring Valley, Lemon Grove and Chula Vista &mdash;
      where the team&rsquo;s transaction record actually concentrates, and
      where the honest math (older stock, few or no special taxes, freeway
      position) is the story competitors skip.
    </p>
    <div class="grid grid--3" style="margin-top:2rem">
{east_south}
    </div>

    <h3 id="temecula-valley" class="rule-gold" style="margin-top:3.5rem">
      Over the county line &mdash; the Temecula Valley
    </h3>
    <p>
      Temecula, Murrieta and Menifee, up the I&#8209;15 in southwest
      Riverside County &mdash; where many North County searches end when the
      budget meets the map. A different county, with its own district
      records: each guide states whose list governs and links it.
    </p>
    <div class="grid grid--3" style="margin-top:2rem">
{riverside}
    </div>

    <p class="updated" style="margin-top:2.5rem">Last updated {TODAY}</p>
  </div>
</section>"""

    nodes = c.base_nodes() + [
        schema.breadcrumbs(
            [
                ("Home", f"{site.DOMAIN}/"),
                ("Neighborhoods", f"{site.DOMAIN}/neighborhoods"),
            ]
        ),
    ]

    write(
        path,
        c.page(
            title=(
                "San Diego County Neighborhood Guides — La Jolla to Escondido, "
                "Chula Vista to Temecula | Team Azizi"
            ),
            description=(
                f"Maintained guides to {total} San Diego County and Temecula "
                "Valley communities: which Mello-Roos districts apply, which "
                "district assigns the schools, and Team Azizi's record in "
                "each. From Team Azizi at Compass."
            ),
            path=path,
            body=body,
            nodes=nodes,
            hero=True,
            og_image="/assets/img/og/neighborhoods.jpg",
        ),
        changefreq="weekly",
        priority="0.9",
    )


# --------------------------------------------------------------------------
# The six neighborhood pages — the product
# --------------------------------------------------------------------------

# Team sales per community across the whole 1,009-record Compass history
# (research/salesRecord.md §1). Published honestly: a page claiming expertise
# it cannot evidence is the exact doorway pattern the plan exists to avoid.
SOLD_RECORD = {
    "del-sur": 18, "4s-ranch": 18,   # 92127 — not separable by ZIP
    "carmel-valley": 11, "scripps-ranch": 9, "del-mar": 6, "rancho-santa-fe": 1,
    # North County. Escondido is the one count salesRecord.md documents; the
    # others need the full sales export. None means the page says nothing
    # about volume rather than guessing at it.
    "escondido": 96,
    "oceanside": None, "fallbrook": None, "san-marcos": None,
    "carlsbad": None, "vista": None, "poway": None, "encinitas": None,
    "valley-center": None, "ramona": None,
    # Southwest Riverside — absent from the Compass sales sweep entirely.
    # None means the page says nothing about volume rather than guessing.
    "temecula": None, "murrieta": None, "menifee": None,
    # City neighborhoods + East County/South Bay. salesRecord.md names
    # Spring Valley, South Bay (incl. Chula Vista), Santee and El Cajon as
    # actual top markets, but per-area counts need the full export — None
    # until then, same rule as North County.
    "la-jolla": None, "pacific-beach": None, "ocean-beach": None,
    "hillcrest": None, "north-park": None, "downtown-san-diego": None,
    "college-area": None, "chula-vista": None, "santee": None,
    "el-cajon": None, "spring-valley": None, "lemon-grove": None,
}


def plain(html: str) -> str:
    """Markup and entities out, readable sentence in — for JSON-LD text."""
    text = re.sub(r"<[^>]+>", "", html)
    return re.sub(r"\s+", " ", unescape(text)).strip()


ANSWER_Q = re.compile(
    r'<h[1-6] class="answer__q">(?P<q>.*?)</h[1-6]>\s*'
    r'<p class="answer__lead">(?P<a>.*?)</p>',
    re.DOTALL,
)


def faq_from_blocks(blocks_html: str) -> list[dict[str, str]]:
    """Derive the FAQPage graph from the answer blocks already on the page.

    Hand-maintaining a parallel FAQ list is how the markup and the visible
    text drift apart, and Google is explicit that FAQ structured data must
    match content visible on the page. Reading it back out of the rendered
    blocks makes that impossible by construction: if the passage changes,
    the schema changes with it.

    This closed a real gap. /sell, /buy, /concierge, both /properties pages
    and all 19 agent pages carried question-and-answer content with no
    FAQPage node at all, while the guides had one — roughly 25 pages of
    extractable answers invisible to anything reading the graph.
    """
    return [
        {"q": plain(m.group("q")), "a": plain(m.group("a"))}
        for m in ANSWER_Q.finditer(blocks_html)
    ]


def tax_block(h: dict) -> str:
    """The Mello-Roos answer — the single most-asked question in 92127 and,
    per the competitor teardown, not addressed on one competitor page."""
    t = taxes.for_hood(h["slug"])
    if not t:
        return ""
    name = c.esc(h["name"])

    if t["has_cfd"]:
        rows = "".join(
            f"<li><strong>{c.esc(d[0])}</strong> &mdash; district {d[1]}, "
            f"administered by {c.esc(d[2])}, {d[3]}</li>"
            for d in t["districts"]
        )
        # Riverside entries carry their own lead — the default sentence
        # names the San Diego County Auditor, which would be the wrong
        # source for a Temecula or Menifee parcel.
        lead = t.get("lead") or (
            f"{name} does carry Mello-Roos. The County Auditor's active "
            f"FY&nbsp;2025-26 list shows {len(t['districts'])} community "
            f"facilities district{'s' if len(t['districts']) > 1 else ''} "
            f"covering {name}, and a home there can sit inside more than one."
        )
        body = f"<ul>{rows}</ul><p>{c.esc(t['note'])}</p>"
    else:
        lead = (
            f"No community facilities district in the County Auditor's active "
            f"FY&nbsp;2025-26 list is named for {name}. That is the documented "
            f"basis for saying {name} homes generally do not carry Mello-Roos "
            f"&mdash; though it describes district names, not a guarantee for "
            f"any particular parcel."
        )
        body = f"<p>{c.esc(t['note'])}</p>"

    src_url = t.get("source_url", taxes.SOURCE_URL)
    src_name = t.get("source_name", taxes.SOURCE_NAME)
    retrieved = t.get("retrieved", taxes.RETRIEVED)
    body += (
        f'<p class="answer__source">{c.esc(taxes.VERIFY_NOTE)}</p>'
        f'<p class="answer__source">Source: <a href="{src_url}" '
        f'rel="nofollow noopener" target="_blank">{c.esc(src_name)}</a>, '
        f"retrieved {retrieved}.</p>"
    )
    return c.answer_block(
        heading="h2",
        anchor="mello-roos",
        question=f"Does {h['name']} have Mello-Roos, and how much?",
        lead=lead,
        body=body,
    )


def build_neighborhood(slug: str) -> None:
    h = hood(slug)
    agent, confirmed = agents.for_neighborhood(slug)
    name = c.esc(h["name"])
    path = f"/neighborhoods/{slug}"
    sold = SOLD_RECORD.get(slug)

    video_html = ""
    if h.get("video"):
        v = h["video"]
        video_html = f"""<section class="section section--tight">
  <div class="container container--narrow">
    <h2 class="rule-gold">A tour of {name}</h2>
    <div class="video">
      <iframe src="https://www.youtube.com/embed/{v['id']}"
              title="{c.esc(v['title'])}" loading="lazy"
              allow="accelerometer; encrypted-media; picture-in-picture"
              allowfullscreen></iframe>
    </div>
    <p class="answer__source">
      &ldquo;{c.esc(v['title'])}&rdquo; &mdash; produced for Team Azizi,
      published on <a href="{site.VIDEO_CHANNEL}" rel="nofollow noopener"
      target="_blank">{c.esc(site.VIDEO_CHANNEL_NAME)}</a>.
    </p>
  </div>
</section>"""

    # Track record, stated plainly. One sale is one sale, and an unverified
    # count is silence rather than a guess.
    if sold is None:
        record = None
    elif sold >= 9:
        record = (
            f"Team Azizi has closed {sold} sales in {name} across the team's "
            f"Compass history."
        )
    elif sold > 1:
        record = (
            f"Team Azizi has closed {sold} sales in {name}. That is a modest "
            f"number and stating it plainly is the point &mdash; the guide "
            f"below is built on public records and first-hand local knowledge, "
            f"not on volume we do not have."
        )
    else:
        record = (
            f"Team Azizi has closed one sale in {name}. This guide is built on "
            f"public records and on-the-ground familiarity rather than a deep "
            f"transaction record here, and saying so is more useful to you "
            f"than implying otherwise."
        )

    blocks = "\n\n".join(filter(None, [
        tax_block(h),
        c.answer_block(
            heading="h2",
            anchor="schools",
            question=f"What school district serves {h['name']}?",
            lead=(
                f"{h['name']} is served by {c.esc(h['district'])}. "
                "Attendance is assigned by address rather than by ZIP code, so "
                "two homes a few streets apart can feed different schools "
                "&mdash; confirm the specific address with the district before "
                "relying on it."
            ),
        ),
        # Community-specific depth. Structural facts only — which district,
        # which boundary, which agency. See build/data/guides.py.
        *[c.answer_block(heading="h2", **b) for b in guides.for_hood(slug)],
        c.answer_block(
            heading="h2",
            anchor="track-record",
            question=f"Has Team Azizi actually sold in {h['name']}?",
            lead=record,
        ) if record else None,
    ]))

    # Derived from the rendered blocks, not hand-written alongside them.
    # The previous version paraphrased: the Mello-Roos answer used the note
    # from taxes.py while the page displayed a different lead sentence, which
    # is exactly the visible-content mismatch Google's FAQ guidance forbids.
    faq = faq_from_blocks(blocks)

    # Twelve communities have no photograph and are not getting a fabricated
    # one (docs/photography-brief.md). Instead of an empty band they get a
    # designed hero: the community's own facts set as type, over an abstract
    # texture that depicts nothing. It carries more information than a stock
    # photograph would, and it stops being needed the day a real photograph
    # of that street exists — remove the slug from HOOD_IMAGE_MISSING.
    if slug not in HOOD_IMAGE_MISSING:
        hero_media = c.picture(
            f"/assets/img/neighborhoods/{slug}.jpg", width=1280, height=800,
            cls="band__media", eager=True,
        )
        hero_facts = ""
        hero_class = "band band--hero"
    else:
        texture = textures.ASSIGNMENT.get(slug, "grain")
        hero_media = c.picture(
            f"/assets/img/textures/{texture}.jpg", width=1600, height=1067,
            cls="band__media", eager=True,
        )
        hero_class = "band band--hero band--plate"

        # Facts, not adjectives — and each is already sourced elsewhere on the
        # page, so the hero promises exactly what the page delivers.
        cfd = taxes.for_hood(slug) or {}
        districts = len(cfd.get("districts", []))
        if slug == "san-marcos":
            tax_fact = ("91", "active CFDs &mdash; most in the county")
        elif slug == "poway":
            tax_fact = ("19", "Poway Unified CFDs")
        elif slug == "temecula":
            tax_fact = ("4", "city CFDs &mdash; schools levy more")
        elif slug == "murrieta":
            tax_fact = ("10", "city CFDs formed to date")
        elif slug == "menifee":
            tax_fact = ("34", "zones in the citywide CFD")
        elif slug == "chula-vista":
            tax_fact = ("3", "CFD layers possible on one east-side bill")
        elif slug == "lemon-grove":
            tax_fact = ("1", "CFD &mdash; commercial corridor only")
        elif cfd.get("has_cfd"):
            tax_fact = (str(districts), "Mello-Roos district" + ("s" if districts != 1 else ""))
        else:
            tax_fact = ("None", "named in the county CFD list")

        zips = h["zip"].split(",")
        plate = [
            (str(len(zips)), "ZIP code" + ("s" if len(zips) != 1 else "")),
            tax_fact,
        ]
        if (sold := SOLD_RECORD.get(slug)):
            plate.append((str(sold), "closed sales here"))

        cells = "\n".join(
            f'      <div class="plate__cell">'
            f'<span class="plate__value">{v}</span>'
            f'<span class="plate__label">{lab}</span></div>'
            for v, lab in plate
        )
        hero_facts = f'\n    <div class="plate">\n{cells}\n    </div>'

    # The "check the record" layer: every authority the guide names, linked.
    # Official sources only, each verified before listing — see
    # build/data/resources.py for the rule. Followed links, deliberately:
    # these are citations to the agencies that hold the record.
    res = resources.for_hood(slug)
    resources_html = ""
    if res:
        items = "\n".join(
            f'      <li><a href="{r["url"]}" rel="noopener" target="_blank">'
            f'{c.esc(r["label"])}</a> &mdash; {c.esc(r["note"])}.</li>'
            for r in res
        )
        resources_html = f"""
<section class="section section--tight">
  <div class="container container--narrow">
    <h2 class="rule-gold">Check the record: official {name} sources</h2>
    <p class="sources__intro">
      Every figure above names its source. These are the official pages where
      those records actually live &mdash; verified {resources.VERIFIED}, and
      worth more than any summary of them, ours included.
    </p>
    <ul class="sources">
{items}
    </ul>
  </div>
</section>"""

    credit = photos.for_hood(slug)
    credit_html = ""
    if credit:
        lic = (
            f'<a href="{credit["licence_url"]}" rel="nofollow noopener" '
            f'target="_blank">{c.esc(credit["licence"])}</a>'
            if credit.get("licence_url") else c.esc(credit["licence"])
        )
        # CC BY and CC BY-SA both require indicating that changes were made,
        # not merely naming the author. Cropping to a 16:10 hero is already a
        # change, so this applies to every one of these; where the frame was
        # also graded, the credit says so specifically.
        changed = credit.get("modified") or "Cropped to fit."
        credit_html = (
            '\n<p class="photo-credit">Photograph: '
            f'<a href="{credit["source"]}" rel="nofollow noopener" '
            f'target="_blank">{c.esc(credit["title"])}</a> by '
            f'{c.esc(credit["author"])}, {lic}. {c.esc(credit["depicts"])} '
            f'{c.esc(changed)}</p>'
        )

    body = f"""<section class="{hero_class}" style="padding-top:calc(var(--nav-h) + 4rem)">
  {hero_media}
  <div class="container">
    <h1>{name} Real Estate Guide</h1>
    <p style="margin-inline:auto">{h['zip']} &middot; {c.esc(h['district'])}</p>{hero_facts}
  </div>
</section>

<section class="section">
  <div class="container container--narrow">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; <a href="/neighborhoods">Neighborhoods</a>
      &rsaquo; {name}
    </nav>
    {c.byline(agent, TODAY)}{credit_html}
    <p class="lede">
      What follows is the part of a {name} search that is hard to look up:
      which tax districts apply, which district assigns the schools, and what
      we have actually done here. Every figure names its source.
    </p>

{blocks}
  </div>
</section>
{resources_html}
{video_html}

<section class="section">
  <div class="container container--narrow">
    {c.expert_block(agent, h, confirmed=confirmed)}
  </div>
</section>

<section class="band band--heavy">
  {c.picture("/assets/img/backgrounds/work-with-us.jpg", width=1920, height=1200, cls="band__media")}
  <div class="container">
    <h2 class="rule-center">Thinking about {name}?</h2>
    <div class="cta-row">
      <a class="btn btn--light" href="/home-valuation">What's my home worth?</a>
      <a class="btn btn--light" href="{site.PHONE_HREF}">{site.PHONE_DISPLAY}</a>
    </div>
  </div>
</section>"""

    nodes = c.base_nodes() + [
        schema.neighborhood_service(h),
        schema.web_page(
            url=f"{site.DOMAIN}{path}",
            name=f"{h['name']} Real Estate Guide",
            author_slug=agent["slug"],
            updated=TODAY,
            significant_links=[r["url"] for r in res] or None,
        ),
        schema.agent(agent, hood=h if confirmed else None),
        schema.faq_page(faq),
        schema.breadcrumbs([
            ("Home", f"{site.DOMAIN}/"),
            ("Neighborhoods", f"{site.DOMAIN}/neighborhoods"),
            (h["name"], f"{site.DOMAIN}{path}"),
        ]),
    ]
    if (v := schema.video(h)):
        nodes.append(v)

    write(
        path,
        c.page(
            title=(
                f"{h['name']} Real Estate Guide — Mello-Roos, Schools & "
                f"Market | Team Azizi"
            ),
            description=(
                f"A sourced guide to {h['name']} ({h['zip']}): which "
                "Mello-Roos districts apply, which district assigns the "
                f"schools, and Team Azizi's record there. Call "
                f"{site.PHONE_DISPLAY}."
            ),
            path=path,
            body=body,
            nodes=nodes,
            hero="light" if slug in HOOD_IMAGE_MISSING else True,
            og_image=f"/assets/img/og/hood-{slug}.jpg",
        ),
        changefreq="monthly",
        priority="0.9",
    )


def build_neighborhoods() -> None:
    for slug in (
        site.NAV_ORDER + site.NORTH_COUNTY_ORDER + site.SD_CITY_ORDER
        + site.EAST_SOUTH_ORDER + site.SW_RIVERSIDE_ORDER
    ):
        build_neighborhood(slug)


# --------------------------------------------------------------------------
# /home-valuation — the highest-traffic page they own
# --------------------------------------------------------------------------


def build_home_valuation() -> None:
    """Lead magnet, built around the Zestimate rather than reproducing it.

    Two things drove the design:

    **It is the Instagram link-in-bio destination** — dead, and taking traffic
    from 2,055 followers. Highest-traffic single page on the site.

    **We cannot legally show a Zestimate.** Zillow retired the public Zestimate
    API in September 2021; Bridge Interactive, its replacement, is enterprise-
    only, MLS-gated, and does not generally expose the Zestimate at all.
    Everything else on the market is a scraper, and Zillow's terms prohibit
    automated access. Building the client's main lead magnet on a scraper is
    the exact rented-vendor failure mode that killed their last website.

    So the page makes the Zestimate the antagonist instead of the centrepiece.
    That is the stronger play regardless of the legal question: reproducing a
    competitor's number makes Zillow the authority on your client's home, on
    your client's own site, and Zillow monetises by selling that homeowner back
    to an agent. The differentiated page explains why the algorithm is wrong
    *in these specific ZIP codes* — Mello-Roos districts, school attendance
    boundaries, view premiums, Coastal Zone rules — which is precisely the
    data no competitor publishes and precisely what an AVM handles worst.

    One compliance note on the framing: "we'll get you more than Zillow says"
    is a price promise a licensee cannot make. "Zillow has never seen your
    house and does not know which school your street feeds" is a factual
    differentiator that lands the same way.
    """
    path = "/home-valuation"
    updated = TODAY
    author = agents.author_for("/home-valuation")

    blocks = "\n\n".join([
        c.answer_block(
            anchor="why-avms-miss",
            question="Why is my Zestimate wrong?",
            lead=(
                "An automated valuation has never been inside the house. In "
                "Carmel Valley and Del Mar it is working from public records "
                "and recent nearby sales, so it cannot see a remodel, a view, "
                "a canyon-rim lot versus an interior one, or which side of a "
                "school boundary the address falls on &mdash; and those are "
                "the variables that move price most here."
            ),
            body=(
                "<p>Zillow publishes its own median error rate and is candid "
                "that off-market homes are estimated far less accurately than "
                "listed ones. That is not a criticism of the tool; it is what "
                "an algorithm working from public data can do.</p>"
            ),
        ),
        c.answer_block(
            anchor="mello-roos",
            question="Does an online estimate account for Mello-Roos?",
            lead=(
                "An automated estimate does not account for Mello-Roos. In "
                "Del Sur and 4S Ranch, two homes on the same street "
                "with the same square footage can carry materially different "
                "Mello-Roos obligations depending on the community facilities "
                "district and the phase they were built in &mdash; which "
                "changes the monthly payment a buyer can afford, and therefore "
                "changes what the home actually sells for."
            ),
        ),
        c.answer_block(
            anchor="school-boundaries",
            question="Do school boundaries change what my home is worth?",
            lead=(
                "In Carmel Valley they can change it by a great deal. Homes "
                "carrying San Diego addresses can feed Del Mar Union schools "
                "or San Dieguito Union depending on the street, and buyers pay "
                "for the assignment &mdash; an automated estimate that treats "
                "the ZIP code as uniform will miss that difference entirely."
            ),
        ),
        c.answer_block(
            anchor="coastal-zone",
            question="How does the Coastal Zone affect value in Del Mar?",
            lead=(
                "Del Mar properties inside the Coastal Zone carry permitting "
                "constraints on remodels and rebuilds that properties outside "
                "it do not. Two otherwise comparable homes can be worth "
                "meaningfully different amounts because of what a buyer is "
                "allowed to do with them, and no automated model reads the "
                "permit history."
            ),
        ),
        c.answer_block(
            anchor="what-you-get",
            question="What do I get instead of an instant number?",
            lead=(
                "A comparative market analysis prepared by the Team Azizi "
                "agent who works your neighborhood &mdash; Del Mar, Carmel "
                "Valley, Rancho Santa Fe, Del Sur, 4S Ranch or Scripps Ranch "
                "&mdash; built from MLS sales, current competing inventory and "
                "the local factors above, with the reasoning shown rather than "
                "a single figure asserted."
            ),
        ),
    ])

    # Grouped rather than a flat list of thirty-one: a homeowner scanning for
    # their own city finds it faster, and the group label tells the agent
    # reading the lead email roughly where the property is before they open it.
    def _optgroup(label: str, slugs: list[str]) -> str:
        opts = "\n".join(
            f'            <option value="{h["slug"]}">{c.esc(h["name"])}</option>'
            for h in [hood(s) for s in slugs]
        )
        return f'          <optgroup label="{c.esc(label)}">\n{opts}\n          </optgroup>'

    hood_options = "\n".join([
        _optgroup("North County", site.NORTH_COUNTY_ORDER),
        _optgroup("I-15 corridor & coast", site.NAV_ORDER),
    ])

    body = f"""<section class="section" style="padding-top:calc(var(--nav-h) + 3rem)">
  <div class="container">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; Home Valuation
    </nav>
    <p class="eyebrow">Home valuation</p>
    <h1>What's your home worth?</h1>
    <p class="lede">
      Put in your address and we'll pull up your house and open your Zestimate
      in a new tab, so you can see what the algorithm thinks. Then, if you want
      a number that accounts for what you've actually done to the place, an
      agent who sells on your street will come out and work it properly.
    </p>

    <!-- Step 1. Address only. Deliberately one field: this is the step that
         has to convert, and every extra box costs completions. The address is
         sent as a lead the moment it is submitted (see site.js) — before the
         Zillow tab opens — because that is the point of highest intent and
         highest abandonment. -->
    <form class="valuation valuation--step1" data-address-step
          data-zillow="{site.ZILLOW_SEARCH}"
          data-endpoint="{site.LEAD_ENDPOINT}"
          data-streetview-key="{site.GOOGLE_MAPS_KEY}">
      <div class="field">
        <label for="address-lookup">Your property address</label>
        <input id="address-lookup" name="address" type="text" required
               autocomplete="street-address"
               placeholder="1234 Example St, Escondido CA 92025">
      </div>
      <button class="btn btn--filled" type="submit">See my home &amp; Zestimate</button>
      <p class="updated" style="margin-top:1rem">
        Opens Zillow in a new tab. Nothing is posted publicly and your address
        is not sold on &mdash; it goes to a Team Azizi agent and nobody else.
      </p>
    </form>

    <!-- Revealed after step 1, populated by site.js. -->
    <div class="valuation__result" data-address-result hidden>
      <figure class="valuation__shot">
        <img data-streetview alt="" width="800" height="500" loading="lazy" hidden>
        <figcaption data-address-echo class="updated"></figcaption>
      </figure>
      <div class="valuation__pitch">
        <h2 class="rule-gold">Zillow has never been inside</h2>
        <p>
          Your Zestimate is open in the other tab. It was built from public
          records and nearby sales &mdash; which means it has not seen your
          kitchen, your addition, your lot, or which side of a school boundary
          you sit on. Those are the things that move the number most in North
          San Diego County.
        </p>
        <p>
          For an accurate figure, a Team Azizi agent comes out, walks the
          property, pulls real comparables from the MLS, and prices in the
          upgrades and additions you have actually made &mdash; with the
          reasoning shown rather than a single number asserted.
        </p>
        <p><a class="btn btn--filled" href="#full-valuation">Book that walkthrough</a></p>
      </div>
    </div>

    <form class="valuation" id="full-valuation" method="POST"
          action="{site.LEAD_ENDPOINT}"
          data-lead-form data-lead-kind="valuation">
      <!-- Formspree control fields. _subject is rewritten on submit to carry
           the address, so the notification email is scannable in an inbox
           without opening it. _gotcha is a honeypot: bots fill it, humans
           never see it. -->
      <input type="hidden" name="_subject" value="Home valuation request"
             data-subject-prefix="Valuation request">
      <input type="hidden" name="_next"
             value="{site.DOMAIN}/thank-you">
      <input type="text" name="_gotcha" tabindex="-1" autocomplete="off"
             aria-hidden="true"
             style="position:absolute;left:-9999px;width:1px;height:1px">
      <div class="field">
        <label for="address">Property address</label>
        <input id="address" name="address" type="text" autocomplete="street-address"
               placeholder="12860 El Camino Real, San Diego CA 92130" required>
      </div>
      <div class="grid grid--2">
        <div class="field">
          <label for="hood">Neighborhood</label>
          <select id="hood" name="neighborhood">
            <option value="">Select&hellip;</option>
{hood_options}
            <option value="other">Somewhere else in San Diego County</option>
          </select>
        </div>
        <div class="field">
          <label for="timing">Timing</label>
          <select id="timing" name="timing">
            <option value="">Select&hellip;</option>
            <option>Just curious what it is worth</option>
            <option>Thinking about selling this year</option>
            <option>Ready to list now</option>
            <option>Refinancing or estate planning</option>
          </select>
        </div>
      </div>
      <div class="grid grid--2">
        <div class="field">
          <label for="name">Name</label>
          <input id="name" name="name" type="text" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="email">Email</label>
          <input id="email" name="email" type="email" autocomplete="email" required>
        </div>
      </div>
      <div class="field">
        <label for="phone">Phone</label>
        <input id="phone" name="phone" type="tel" autocomplete="tel">
      </div>
      <div class="consent">
        <input id="consent" name="consent" type="checkbox" required>
        <p><label for="consent" style="display:inline;font-size:inherit;
           font-weight:400;letter-spacing:0;text-transform:none">
           {c.esc(site.TCPA_CONSENT)}</label></p>
      </div>
      <button class="btn btn--filled" type="submit">Book my walkthrough</button>
      <p class="updated" style="margin-top:1rem">
        A real person reads every one of these. No automated estimate, no drip
        sequence, no selling your details on.
      </p>
    </form>
  </div>
</section>

<section class="section section--panel">
  <div class="container container--narrow">
    <h2 class="rule-gold">What an algorithm cannot see</h2>
{blocks}
    {c.byline(author, updated)}
  </div>
</section>

<section class="band band--heavy">
  {c.picture("/assets/img/backgrounds/home-valuation.jpg", width=1920, height=1281,
             cls="band__media")}
  <div class="container">
    <h2 class="rule-center">Rather just talk it through?</h2>
    <div class="cta-row">
      <a class="btn btn--light" href="{site.PHONE_HREF}">{site.PHONE_DISPLAY}</a>
      <a class="btn btn--light" href="/contact">Send a message</a>
    </div>
  </div>
</section>"""

    faq = faq_from_blocks(blocks)

    nodes = c.base_nodes() + [
        schema.web_page(
            url=f"{site.DOMAIN}{path}",
            name="Home Valuation",
            author_slug=author["slug"],
            updated=updated,
        ),
        schema.agent(author),
        schema.faq_page(faq),
        schema.breadcrumbs([
            ("Home", f"{site.DOMAIN}/"),
            ("Home Valuation", f"{site.DOMAIN}{path}"),
        ]),
    ]

    write(
        path,
        c.page(
            title=(
                "What Is My Home Worth? North San Diego Home Valuation | Team Azizi"
            ),
            description=(
                "Zillow has never seen your house. Get a comparative market "
                "analysis from the Team Azizi agent who works Carmel Valley, "
                "Del Mar, Rancho Santa Fe, Del Sur, 4S Ranch or Scripps Ranch. "
                f"Call {site.PHONE_DISPLAY}."
            ),
            path=path,
            body=body,
            nodes=nodes,
        ),
        changefreq="monthly",
        priority="0.9",
    )



def build_thank_you() -> None:
    """Where lead forms land after posting. noindex — it is a confirmation,
    not a destination, and it exists so a submitter gets a real acknowledgement
    instead of Formspree's own branded page."""
    path = "/thank-you"
    body = f"""<section class="section" style="padding-top:calc(var(--nav-h) + 5rem);min-height:60vh">
  <div class="container container--narrow">
    <p class="eyebrow">Received</p>
    <h1>Thank you &mdash; that came through</h1>
    <p class="lede">
      A member of the team will read it and come back to you personally,
      usually the same day. Nothing automated is going to happen in the
      meantime: no instant estimate, no drip sequence.
    </p>
    <p>
      If it is urgent, call {site.PHONE_DISPLAY} and you will get a person.
    </p>
    <div class="cta-row">
      <a class="btn btn--dark" href="{site.PHONE_HREF}">{site.PHONE_DISPLAY}</a>
      <a class="btn btn--dark" href="/neighborhoods">Neighborhood guides</a>
    </div>
  </div>
</section>"""
    html = c.page(
        title="Thank You | Team Azizi",
        description="Your request has been received.",
        path=path,
        body=body,
        nodes=c.base_nodes(),
    )
    html = html.replace(
        "<title>", '<meta name="robots" content="noindex,follow">\n<title>', 1
    )
    target = SITE / "thank-you.html"
    target.write_text(html, encoding="utf-8")
    print(f"  {target.relative_to(SITE.parent)}  (noindex, not in sitemap)")


# --------------------------------------------------------------------------
# /properties/* — the two redirect targets, and a 404
#
# These exist because `vercel.json` already 301s two families of dead Luxury
# Presence URLs at them: /home-search/* and every old individual listing page.
# A permanent redirect into a 404 is worse for those still-indexed URLs than
# no redirect at all, so the targets have to exist before the domain moves.
#
# Neither page carries live inventory. The MLS question in HANDOFF §6 is
# unresolved — aggregate statistics are fine, individual listing display needs
# SDMLS rules confirmed first — so these say what is true today and route the
# visitor somewhere useful instead of faking a search widget.
# --------------------------------------------------------------------------


def build_properties() -> None:
    lead = agents.author_for("/properties")

    # ---- /properties/sale — where /home-search/* lands -------------------
    path = "/properties/sale"
    sale_blocks = "\n\n".join([
        c.answer_block(
            anchor="why-no-search",
            question="Why is there no property search on this site?",
            lead=(
                "Team Azizi does not run a property search widget on this site "
                "because every portal already has one and none of them tell you "
                "what decides a purchase in North San Diego County &mdash; which "
                "Mello-Roos district a parcel sits in, which school boundary the "
                "street falls on, or whether a view is protected."
            ),
            body=(
                '<p>Those are the questions the '
                '<a href="/neighborhoods">neighborhood guides</a> answer, from '
                'the County Auditor&rsquo;s district list and the school '
                'districts themselves. Search is a commodity; that is not.</p>'
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="how-to-see-listings",
            question="How do I see what Team Azizi has for sale?",
            lead=(
                f"Call {site.PHONE_DISPLAY} and a Team Azizi agent will send "
                "current North San Diego County listings for the specific area "
                "and price range you are looking in, including properties that "
                "have not reached the portals yet."
            ),
            heading="h2",
        ),
    ])

    body = f"""<section class="section" style="padding-top:calc(var(--nav-h) + 4rem)">
  <div class="container container--narrow">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; Properties &rsaquo; For sale
    </nav>
    <p class="eyebrow">For sale</p>
    <h1>Current listings</h1>
    <p class="lede">
      If you followed a link to a property search here, that search tool is
      gone. What replaced it is better for most people: a named agent who
      works one area and can send you what is coming before it is public.
    </p>

{sale_blocks}

    <p style="margin-top:2.5rem">
      <a class="btn btn--dark" href="{site.PHONE_HREF}">{site.PHONE_DISPLAY}</a>
      <a class="btn" href="/neighborhoods">Neighborhood guides</a>
    </p>
    <p class="updated" style="margin-top:2rem">Last updated {TODAY}</p>
  </div>
</section>"""

    write(
        path,
        c.page(
            title="Homes for Sale in North San Diego County | Team Azizi",
            description=(
                "Current listings from Team Azizi at Compass across North San "
                f"Diego County. Call {site.PHONE_DISPLAY} for what is "
                "available in your area and price range."
            ),
            path=path,
            body=body,
            nodes=c.base_nodes() + [
                schema.web_page(
                    url=f"{site.DOMAIN}{path}",
                    name="Homes for Sale in North San Diego County",
                    author_slug=lead["slug"],
                    updated=TODAY,
                ),
                schema.faq_page(faq_from_blocks(sale_blocks)),
                schema.breadcrumbs([
                    ("Home", f"{site.DOMAIN}/"),
                    ("For sale", f"{site.DOMAIN}{path}"),
                ]),
            ],
        ),
        changefreq="weekly",
        priority="0.7",
    )

    # ---- /properties/sold — where old listing URLs land ------------------
    # Someone hitting this bookmarked one specific house years ago. Say that
    # plainly rather than dropping them on a generic page with no explanation.
    path = "/properties/sold"
    proof_link = (
        f'<a href="{site.PROOF["source_url"]}" rel="nofollow noopener" '
        f'target="_blank">{c.esc(site.PROOF["list_name"])}</a>'
    )
    sold_blocks = "\n\n".join([
        c.answer_block(
            anchor="track-record",
            question="How many homes has Team Azizi sold?",
            lead=(
                f"Team Azizi, based in San Diego, has "
                f"{site.PROOF['closed_sales']} closed sales and "
                f"{site.PROOF['closed_rentals']} closed rentals recorded on its "
                "Compass profile, with 2025 production of "
                f"{site.PROOF['volume_2025']} across "
                f"{site.PROOF['sides_2025']} transaction sides."
            ),
            body=(
                "<p>That 2025 figure is third-party verifiable: it ranks the "
                f"team {site.PROOF['ca_rank']} on the {proof_link} from "
                "RealTrends Verified, reporting 2025 production. The San Diego "
                "Business Journal named the team one of the top 10 in the county "
                "in October 2025.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="where",
            question="Where does Team Azizi actually sell?",
            lead=(
                "Team Azizi&rsquo;s largest markets by transaction count are in "
                "inland and coastal North County &mdash; Escondido above all, "
                "then Oceanside, Fallbrook and San Marcos &mdash; alongside the "
                "I-15 corridor communities of Del Sur, 4S Ranch and Scripps "
                "Ranch and the coast at Carmel Valley and Del Mar."
            ),
            body=(
                '<p>Each <a href="/neighborhoods">neighborhood guide</a> states '
                "the team&rsquo;s record in that specific community, including "
                "where it is thin. Rancho Santa Fe says one sale, because that is "
                "the number.</p>"
            ),
            heading="h2",
        ),
    ])

    body = f"""<section class="section" style="padding-top:calc(var(--nav-h) + 4rem)">
  <div class="container container--narrow">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; Properties &rsaquo; Sold
    </nav>
    <p class="eyebrow">Sold</p>
    <h1>That listing has closed</h1>
    <p class="lede">
      If a link brought you to a specific property, that listing is no longer
      active and its page is gone. Rather than show you nothing, here is what
      the record actually looks like.
    </p>

{sold_blocks}

    <p style="margin-top:2.5rem">
      <a class="btn btn--dark" href="{site.PHONE_HREF}">{site.PHONE_DISPLAY}</a>
      <a class="btn" href="/properties/sale">Current listings</a>
    </p>
    <p class="updated" style="margin-top:2rem">Last updated {TODAY}</p>
  </div>
</section>"""

    write(
        path,
        c.page(
            title="Recently Sold — Team Azizi's Record | Team Azizi",
            description=(
                f"Team Azizi at Compass has {site.PROOF['closed_sales']} "
                "closed sales across North San Diego County. 2025 production: "
                f"{site.PROOF['volume_2025']} across "
                f"{site.PROOF['sides_2025']} sides, verified by RealTrends."
            ),
            path=path,
            body=body,
            nodes=c.base_nodes() + [
                schema.web_page(
                    url=f"{site.DOMAIN}{path}",
                    name="Recently Sold — Team Azizi's Record",
                    author_slug=lead["slug"],
                    updated=TODAY,
                ),
                schema.faq_page(faq_from_blocks(sold_blocks)),
                schema.breadcrumbs([
                    ("Home", f"{site.DOMAIN}/"),
                    ("Sold", f"{site.DOMAIN}{path}"),
                ]),
            ],
        ),
        changefreq="monthly",
        priority="0.7",
    )


def lead_form(*, kind: str, subject: str, cta: str, address: bool = True,
              extra: str = "") -> str:
    """The standard lead form. One implementation, so the TCPA consent, the
    honeypot and the thank-you redirect cannot drift between pages.

    `extra` takes page-specific fields (the careers form asks for a DRE number
    and the communities an applicant knows) and renders them *above* the
    consent block, so the consent stays the last thing before the button on
    every form regardless of what a page adds.
    """
    addr = f"""      <div class="field">
        <label for="{kind}-address">Property address</label>
        <input id="{kind}-address" name="address" type="text" required
               autocomplete="street-address">
      </div>
""" if address else ""
    return f"""<form class="valuation" method="POST" action="{site.LEAD_ENDPOINT}"
          data-lead-form data-lead-kind="{kind}">
      <input type="hidden" name="_subject" value="{c.esc(subject)}"
             data-subject-prefix="{c.esc(subject)}">
      <input type="hidden" name="_next" value="{site.DOMAIN}/thank-you">
      <input type="text" name="_gotcha" tabindex="-1" autocomplete="off"
             aria-hidden="true"
             style="position:absolute;left:-9999px;width:1px;height:1px">
{addr}      <div class="grid grid--2">
        <div class="field">
          <label for="{kind}-name">Name</label>
          <input id="{kind}-name" name="name" type="text" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="{kind}-email">Email</label>
          <input id="{kind}-email" name="email" type="email" autocomplete="email" required>
        </div>
      </div>
      <div class="field">
        <label for="{kind}-phone">Phone</label>
        <input id="{kind}-phone" name="phone" type="tel" autocomplete="tel">
      </div>
{extra}      <div class="consent">
        <input id="{kind}-consent" name="consent" type="checkbox" required>
        <p><label for="{kind}-consent" style="display:inline;font-size:inherit;
           font-weight:400;letter-spacing:0;text-transform:none">
           {c.esc(site.TCPA_CONSENT)}</label></p>
      </div>
      <button class="btn btn--filled" type="submit">{c.esc(cta)}</button>
    </form>"""


def simple_page(
    *,
    path: str,
    eyebrow: str,
    h1: str,
    lede: str,
    blocks: str,
    tail: str,
    title: str,
    description: str,
    crumb: str,
) -> None:
    # Keyed on the page's own path so /sell, /buy and /concierge each get
    # their own byline rather than sharing the helper's.
    lead = agents.author_for(path)
    body = f"""<section class="section" style="padding-top:calc(var(--nav-h) + 3rem)">
  <div class="container container--narrow">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; {c.esc(crumb)}
    </nav>
    <p class="eyebrow">{c.esc(eyebrow)}</p>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>

{blocks}

{tail}
    <p class="updated" style="margin-top:2.5rem">Last updated {TODAY}</p>
  </div>
</section>"""
    write(
        path,
        c.page(
            title=title,
            description=description,
            path=path,
            body=body,
            nodes=c.base_nodes() + [
                schema.web_page(
                    url=f"{site.DOMAIN}{path}", name=h1,
                    author_slug=lead["slug"], updated=TODAY,
                ),
                schema.faq_page(faq_from_blocks(blocks)),
                schema.breadcrumbs([
                    ("Home", f"{site.DOMAIN}/"),
                    (crumb, f"{site.DOMAIN}{path}"),
                ]),
            ],
        ),
        changefreq="monthly",
        priority="0.8",
    )


def build_sell() -> None:
    blocks = "\n\n".join([
        c.answer_block(
            anchor="what-you-net",
            question="What will I actually net selling my home in San Diego County?",
            lead=(
                "A San Diego County seller's net is the sale price minus the "
                "mortgage payoff, commissions, county and city transfer tax, "
                "escrow and title fees, any Mello-Roos or HOA owed through "
                "close, and whatever the buyer negotiates after inspection. "
                "The gap between the headline price and the wire that lands "
                "is routinely six figures, and it is knowable in advance."
            ),
            body=(
                "<p>City transfer tax is worth flagging early because it is "
                "not uniform across the county, and inspection credits are the "
                "line most sellers forget to plan for. A net sheet built "
                "before listing &mdash; not after an offer &mdash; is what "
                "turns those from surprises into decisions.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="pricing",
            question="How should I price my home in North San Diego County?",
            lead=(
                "Pricing a North San Diego County home starts with the "
                "specifics an automated estimate cannot see: which Mello-Roos "
                "district the parcel sits in, which school boundary the street "
                "falls on, whether a view is protected by topography or by "
                "nothing, and what the Coastal Zone permits on that lot."
            ),
            body=(
                "<p>Those four factors move price more than square footage "
                "does in the communities we work, and they are why two "
                "apparently identical homes trade at different numbers. See "
                "the <a href=\"/mello-roos\">Mello-Roos lookup</a> for the "
                "tax half of it.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="repairs",
            question="Should I renovate before selling in San Diego County?",
            lead=(
                "Some San Diego County pre-sale work returns more than it "
                "costs and some does not, and the split is local rather than "
                "general. Compass Concierge exists to fund the work that does "
                "&mdash; the brokerage fronts the cost and is repaid at "
                "closing, so a seller is not choosing between their savings "
                "and their sale price."
            ),
            body=(
                "<p>The judgement is which work qualifies. Paint, flooring, "
                "landscaping and staging usually earn their cost back; "
                "structural and mechanical work usually does not, and is "
                "better disclosed and priced in. Terms change, so ask for the "
                "current ones. <a href=\"/concierge\">More on Concierge</a>.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="timing",
            question="When is the best time to sell in San Diego County?",
            lead=(
                "San Diego County has a genuine spring selling season, but "
                "the more useful answer for any individual seller is that "
                "competing inventory in their own price band matters more "
                "than the month. Six similar homes listed on the same street "
                "is a harder market than February ever was."
            ),
            body=(
                "<p>Current active and pending counts for a specific "
                "neighborhood and price band come from the MLS on request. "
                "No figure is published here because it would be stale within "
                "weeks, and a stale number is worse than none.</p>"
            ),
            heading="h2",
        ),
    ])
    tail = f"""    <h2 class="rule-gold" style="margin-top:3.5rem">Get a net sheet</h2>
    <p>
      Send the address and we will put together what the sale would actually
      net you &mdash; price supported by real comparables, every cost line
      itemised, and the local factors above priced in rather than assumed.
      No obligation and no automated estimate.
    </p>
    {lead_form(kind="sell", subject="Net sheet request",
               cta="Send me a net sheet")}"""
    simple_page(
        path="/sell",
        eyebrow="Selling",
        h1="Selling your home in North San Diego County",
        lede=(
            "What a sale actually nets, what pricing turns on here, and which "
            "pre-sale work earns its cost back &mdash; before you commit to "
            "anything."
        ),
        blocks=blocks,
        tail=tail,
        title="Sell Your Home in North San Diego County | Team Azizi",
        description=(
            "What you net, how to price against Mello-Roos and school "
            "boundaries, and which pre-sale work pays for itself. Net sheets "
            "from Team Azizi at Compass."
        ),
        crumb="Sell",
    )


def build_buy() -> None:
    blocks = "\n\n".join([
        c.answer_block(
            anchor="true-cost",
            question="What does a home in North San Diego County really cost per month?",
            lead=(
                "A North San Diego County monthly payment is principal and "
                "interest, plus base property tax of roughly 1.1% of assessed "
                "value, plus any Mello-Roos levy, plus HOA, plus insurance "
                "&mdash; and the last three are where two similar homes "
                "diverge by hundreds of dollars a month."
            ),
            body=(
                "<p>Mello-Roos is the one buyers most often miss, because it "
                "is invisible in a listing price and varies parcel by parcel. "
                "The <a href=\"/mello-roos\">Mello-Roos lookup</a> gives the "
                "active districts for all thirty-one communities we cover, "
                "including the sixteen where the answer is none.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="schools",
            question="How do I check which school a San Diego County address feeds?",
            lead=(
                "School assignment is confirmed with the district office for "
                "the exact address, never from the city name or the ZIP "
                "code. In San Diego County "
                "the boundaries routinely cross both: much of Carmel Valley "
                "carries San Diego addresses but feeds Del Mar Union and San "
                "Dieguito Union, and southern Carlsbad homes can be assigned "
                "to Encinitas Union rather than Carlsbad Unified."
            ),
            body=(
                "<p>Buyers pay for school assignment, so getting this wrong "
                "is expensive in both directions. Each "
                "<a href=\"/neighborhoods\">neighborhood guide</a> states "
                "which districts serve that community and where the "
                "boundaries are known to cross.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="insurance",
            question="Can I get fire insurance in inland San Diego County?",
            lead=(
                "Quote it on the specific address before making an offer on "
                "any inland San Diego County property. Much of Fallbrook, "
                "Valley Center, Ramona and the canyon edges of Scripps Ranch "
                "and 92127 sit in state-designated high or very high fire "
                "hazard severity zones, where admitted carriers have narrowed "
                "what they will write."
            ),
            body=(
                "<p>The common outcome there is the California FAIR Plan plus "
                "a difference-in-conditions policy, which costs materially "
                "more than a standard homeowner's policy. A lender will not "
                "fund without bound coverage, so this is a condition of the "
                "purchase being affordable at all &mdash; not a formality for "
                "the end of escrow.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="where-to-look",
            question="Which North San Diego County community should I look in?",
            lead=(
                "The North San Diego County trade-offs are consistent enough "
                "to name: coastal cities like Oceanside, Carlsbad and "
                "Encinitas cost more per foot and add Coastal Zone permitting "
                "on remodels; inland cities like Escondido, San Marcos and "
                "Vista buy more house; and the unincorporated backcountry "
                "&mdash; Fallbrook, Valley Center, Ramona &mdash; buys land "
                "but brings well, septic and fire insurance into the "
                "decision."
            ),
            body=(
                "<p>All thirty-one guides state the tax position, the school "
                "districts and our actual record in that community, including "
                "where it is thin. <a href=\"/neighborhoods\">Start "
                "there</a>.</p>"
            ),
            heading="h2",
        ),
    ])
    tail = f"""    <h2 class="rule-gold" style="margin-top:3.5rem">Tell us what you are looking for</h2>
    <p>
      Area, price range and timing is enough to start. You will hear from the
      Team Azizi agent who works that area &mdash; with a DRE number and a
      direct line, not a call centre.
    </p>
    {lead_form(kind="buy", subject="Buyer enquiry",
               cta="Start the search", address=False)}"""
    simple_page(
        path="/buy",
        eyebrow="Buying",
        h1="Buying in North San Diego County",
        lede=(
            "What a home here actually costs per month, how to check the "
            "school boundary properly, and why fire insurance belongs before "
            "the offer rather than after it."
        ),
        blocks=blocks,
        tail=tail,
        title="Buying a Home in North San Diego County | Team Azizi",
        description=(
            "True monthly cost including Mello-Roos, how to verify school "
            "boundaries, fire insurance before you offer, and which community "
            "fits. From Team Azizi at Compass."
        ),
        crumb="Buy",
    )


def build_concierge() -> None:
    blocks = "\n\n".join([
        c.answer_block(
            anchor="what-is-it",
            question="What is Compass Concierge?",
            lead=(
                "Compass Concierge is a Compass programme that fronts the "
                "cost of pre-sale home improvement work &mdash; the brokerage "
                "pays the vendors up front and is repaid from the proceeds "
                "when the home sells. For a San Diego County seller it means "
                "the work that makes a house show well does not have to come "
                "out of savings first."
            ),
            body=(
                "<p>Eligibility, limits and repayment terms are set by "
                "Compass and change from time to time, so treat anything you "
                "read online &mdash; including this page &mdash; as the shape "
                "of the programme rather than the current terms. Ask for "
                "those in writing before committing to work.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="what-work",
            question="What work is worth doing before selling?",
            lead=(
                "The San Diego County pre-sale work that reliably returns "
                "more than it costs is cosmetic and presentational: paint, "
                "flooring, landscaping, decluttering and staging. Structural, "
                "mechanical and roofing work generally does not return its "
                "cost and is usually better disclosed and priced in than "
                "fixed."
            ),
            body=(
                "<p>That split is the whole judgement, and it is the reason "
                "to have someone walk the property before any money is "
                "committed. Spending on the wrong category is worse than "
                "spending nothing.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="risk",
            question="What is the catch with fronting renovation costs?",
            lead=(
                "The honest risk in any pre-sale improvement programme is "
                "that the work is an obligation regardless of what the San "
                "Diego County home eventually sells for. It is repaid from "
                "proceeds at closing, so a seller with thin equity, or one "
                "who later decides not to sell, needs to understand that "
                "commitment before the first vendor is booked."
            ),
            body=(
                "<p>Which is a reason to scope the work narrowly and to the "
                "categories above, not a reason to avoid it. Read the "
                "agreement, and ask what happens if the home does not "
                "sell.</p>"
            ),
            heading="h2",
        ),
    ])
    tail = f"""    <h2 class="rule-gold" style="margin-top:3.5rem">Find out what your home needs</h2>
    <p>
      Send the address and a Team Azizi agent will walk it and tell you which
      work would actually earn its cost back here &mdash; and which would
      not. That conversation costs nothing and commits you to nothing.
    </p>
    {lead_form(kind="concierge", subject="Concierge enquiry",
               cta="Book a walkthrough")}"""
    simple_page(
        path="/concierge",
        eyebrow="Compass Concierge",
        h1="Compass Concierge",
        lede=(
            "Pre-sale improvement work, funded up front by Compass and repaid "
            "at closing &mdash; and an honest account of which work is worth "
            "doing and what the commitment actually is."
        ),
        blocks=blocks,
        tail=tail,
        title="Compass Concierge — Pre-Sale Home Improvement | Team Azizi",
        description=(
            "How Compass Concierge fronts pre-sale improvement costs, which "
            "work returns its cost in San Diego County, and the commitment "
            "involved. From Team Azizi at Compass."
        ),
        crumb="Concierge",
    )


def value_column(heading: str, body: str) -> str:
    return f"""      <div>
        <h3 class="rule-gold">{heading}</h3>
        <p>{body}</p>
      </div>"""


ICONS = {
    # Simple line marks, drawn rather than downloaded: no icon-font
    # dependency, no licence to track, and they inherit currentColor so the
    # gold comes from the stylesheet instead of being baked into a file.
    "territory": (
        '<path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11Z"/>'
        '<circle cx="12" cy="10" r="2.5"/>'
    ),
    "megaphone": (
        '<path d="M3 11v2a1 1 0 0 0 1 1h2l4 4V6L6 10H4a1 1 0 0 0-1 1Z"/>'
        '<path d="M14 8.5a4 4 0 0 1 0 7"/><path d="M17 6a7.5 7.5 0 0 1 0 12"/>'
    ),
    "chart": (
        '<path d="M4 20V10"/><path d="M10 20V4"/><path d="M16 20v-7"/>'
        '<path d="M3 20h18"/>'
    ),
    "badge": (
        '<circle cx="12" cy="9" r="5.5"/><path d="m8.5 13.5-1 7 4.5-2.5 4.5 2.5-1-7"/>'
    ),
}


def icon(name: str) -> str:
    return (
        '<svg viewBox="0 0 24 24" width="34" height="34" fill="none" '
        'stroke="currentColor" stroke-width="1.25" stroke-linecap="round" '
        'stroke-linejoin="round" aria-hidden="true" '
        'style="color:var(--c-gold-tan);margin-bottom:1rem">'
        f'{ICONS[name]}</svg>'
    )


def build_join() -> None:
    """The agent recruiting landing page.

    Two jobs at once, and they pull in opposite directions. It has to
    *persuade* — the client asked for a conversion page and they are right to,
    because a licensee choosing a team is making a decision no amount of
    sourced prose closes on its own. And it has to stay inside the rule the
    rest of this site is built on: nothing asserted that a reader cannot
    check.

    The resolution is sequencing rather than compromise. Persuasion runs
    first, in the shapes that persuade — a poster hero, verified numbers as
    social proof, four benefit marks, the team's own faces, a CTA repeated at
    every natural decision point. The evidence runs second, as answer blocks,
    where a serious candidate and a retrieval system both go looking. Nobody
    is asked to read a tax explainer before being told what the job is.

    What is NOT here, deliberately: income claims, lead-volume promises, and
    any number that is not already published with a source on this site.
    Recruiting copy is exactly where those get invented, and an agent who
    moves a licence on the strength of an invented figure is a lawsuit with a
    grievance attached.
    """
    proof_stats = "\n".join([
        stat(site.PROOF["volume_2025"], "2025 sales volume"),
        stat(site.PROOF["sides_2025"], "2025 transaction sides"),
        stat("Top 10", "Team in San Diego County"),
        stat(site.PROOF["list_rank"], "Large team in California"),
    ])

    why = [
        ("territory", "A territory of your own",
         "Guides name the licensee who covers the community, with their DRE "
         "number and direct line. You are building your name, not feeding a "
         "queue under someone else&rsquo;s."),
        ("megaphone", "Marketing that runs while you sell",
         f"{len(site.ALL_AREAS)} neighborhood guides and a journal of sourced "
         "posts already exist &mdash; and the team is hiring social and paid "
         "ads so distribution is not your second job."),
        ("chart", "A record you can check",
         f"{site.PROOF['list_rank']} of all California large teams by volume "
         "on RealTrends Verified, and one of the top 10 teams in the county "
         "per the San&nbsp;Diego Business Journal."),
        ("badge", "The Compass platform",
         f"Your licence hangs with {c.esc(site.BROKERAGE)}, CA DRE# "
         f"{site.BROKERAGE_DRE} &mdash; the brokerage tools, and Concierge "
         "for the listings that need work before market."),
    ]
    why_cards = "\n".join(
        f"""      <div>
        {icon(key)}
        <h3>{title}</h3>
        <p>{copy}</p>
      </div>"""
        for key, title, copy in why
    )

    gets = [
        ("Discovery that includes AI assistants",
         "Every page is built the way retrieval actually works &mdash; "
         "self-contained answers, and an entity graph naming the licensee who "
         "wrote them. The page answers the question; the graph says who "
         "answered it. Measured monthly against a fixed query panel."),
        ("Leads that arrive with their context",
         "Enquiries come through the pages themselves &mdash; the "
         "<a href=\"/home-valuation\">valuation tool</a>, the guides, the "
         "<a href=\"/mello-roos\">Mello-Roos lookup</a> &mdash; so you get "
         "the question that produced the lead, not just a name."),
        ("Depth you would spend years building alone",
         "Each guide carries its community&rsquo;s CFD position traced to the "
         "County Auditor, which district assigns the schools and where the "
         "boundaries run. Walking into a listing appointment with that is a "
         "different conversation."),
        ("Straight answers on the terms",
         "Split, cap, fees, who owns the lead and who owns the client "
         "&mdash; in writing, in the first conversation. See "
         "<a href=\"#terms\">the terms section</a> for why we will not print "
         "averages here."),
    ]
    gets_cards = "\n".join(
        f"""      <div>
        <h3 class="rule-gold">{title}</h3>
        <p>{copy}</p>
      </div>"""
        for title, copy in gets
    )

    regions = [
        ("The original six", site.NEIGHBORHOODS),
        ("North County", site.NORTH_COUNTY),
        ("San Diego city", site.SD_CITY),
        ("East County &amp; South Bay", site.EAST_SOUTH),
        ("Southwest Riverside", site.SW_RIVERSIDE),
    ]
    region_cards = "\n".join(
        f"""      <div>
        <h3 class="rule-gold">{label}</h3>
        <p>{len(areas)} communities, including
        {", ".join(f'<a href="/neighborhoods/{a["slug"]}">{c.esc(a["name"])}</a>'
                   for a in areas[:3])}.</p>
      </div>"""
        for label, areas in regions
    )

    blocks = "\n\n".join([
        c.answer_block(
            anchor="who-fits",
            question="What kind of agent fits an area-farming team?",
            lead=(
                f"Team Azizi covers {len(site.ALL_AREAS)} San Diego County "
                f"and Temecula Valley communities with {len(agents.ROSTER)} "
                f"licensees, and each neighborhood guide names the licensee "
                f"who covers that area &mdash; so the agent this model suits "
                f"is one who wants to own a place rather than work a queue of "
                f"leads from anywhere."
            ),
            body=(
                "<p>Depth is the whole method. Every "
                "<a href=\"/neighborhoods\">neighborhood guide</a> carries "
                "that community&rsquo;s Mello-Roos position traced to the "
                "County Auditor&rsquo;s active district list, which district "
                "assigns the schools and where the boundaries actually run, "
                "and what the team has sold there. An agent joining inherits "
                "that surface for their area &mdash; and inherits the "
                "obligation to keep it accurate, because a guide that rots is "
                "worse than no guide.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="record",
            question="What is Team Azizi's track record?",
            lead=(
                f"Team Azizi closed {site.PROOF['volume_2025']} across "
                f"{site.PROOF['sides_2025']} transaction sides in 2025 in San "
                f"Diego County, against {site.PROOF['closed_sales']} closed "
                f"sales in the team&rsquo;s Compass record, and ranks "
                f"{site.PROOF['list_rank']} of all California large teams by "
                f"volume on RealTrends Verified&rsquo;s 2026 list."
            ),
            body=(
                f"<p>The San&nbsp;Diego Business Journal named the team one "
                f"of the top 10 real estate teams in the county in October "
                f"2025. Both placements are third-party published rather than "
                f"self-reported, which is the point: the "
                f"<a href=\"{site.PROOF['source_url']}\" rel=\"nofollow "
                f"noopener\" target=\"_blank\">RealTrends ranking</a> can be "
                f"opened and read before you talk to anyone here. No figure "
                f"on this site requires taking the team&rsquo;s word for it, "
                f"and that standard applies to recruiting as much as to the "
                f"<a href=\"/properties/sold\">sold record</a>.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="brokerage",
            question="Which brokerage would I hang my licence with?",
            lead=(
                f"Licensees on Team Azizi are affiliated with Compass &mdash; "
                f"{c.esc(site.BROKERAGE)}, CA DRE# {site.BROKERAGE_DRE} "
                f"&mdash; working from the Compass office at "
                f"{c.esc(site.STREET)} in Carmel&nbsp;Valley, "
                f"{c.esc(site.CITY)}."
            ),
            body=(
                "<p>Team Azizi is a team within that brokerage rather than an "
                "independent brokerage, so the licence, the transaction file "
                "and the errors-and-omissions cover sit with Compass, and "
                "Compass programmes are available to the team&rsquo;s clients "
                "&mdash; <a href=\"/concierge\">Concierge</a> being the one "
                "that most often decides whether a listing goes to market "
                "ready. Terms of any brokerage programme are set by Compass "
                "and change; ask for the current ones in writing.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="terms",
            question="What about splits, caps, fees and lead flow?",
            lead=(
                "Splits, caps, desk fees and lead flow are not published on "
                "this page, and any San Diego County team that publishes them "
                "on a recruiting page is describing an average rather than "
                "the deal you would actually sign."
            ),
            body=(
                "<p>Those terms depend on the role, the licensee&rsquo;s "
                "experience and the territory, so they are a conversation "
                "rather than a web page &mdash; and the honest advice to any "
                "agent evaluating any team, this one included, is the same: "
                "get the split, the cap, every recurring fee, who owns the "
                "leads and who owns the client relationship in writing before "
                "a licence moves. A team unwilling to put those in writing "
                "has told you the answer.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="apply",
            question="What happens after you send the form?",
            lead=(
                "A first conversation with Team Azizi in San Diego County is "
                "a conversation, not an interview loop: what you are working "
                "on now, which communities you know, what you would want your "
                "territory to be, and the terms in writing."
            ),
            body=(
                "<p>Licence status is worth stating plainly at the start. "
                "California requires a salesperson to be licensed and "
                "affiliated with a broker, and every team member is named on "
                "this site with their DRE number for that reason. If you are "
                "still in the exam process, say so &mdash; it is a timing "
                "question, not a disqualification. Nothing about a first "
                "conversation commits you to anything, and we are not going "
                "to ask you to sign before you have the terms.</p>"
            ),
            heading="h2",
        ),
    ])

    # Deliberately short. Every additional field costs completions, and the
    # only thing this form has to do is start a conversation — the DRE number
    # is the one extra worth asking for, and it stays optional.
    extra = """      <div class="field">
        <label for="join-dre">California DRE licence number (optional)</label>
        <input id="join-dre" name="dre" type="text">
      </div>
"""

    # The visibility check asks for one thing the careers form does not, and
    # it is the one field the report cannot be produced without: which market
    # to run the panel against. Everything else stays minimal, because this
    # is the low-commitment offer on the page and friction defeats its whole
    # purpose.
    vis_extra = """      <div class="field">
        <label for="visibility-market">Which communities do you work?</label>
        <input id="visibility-market" name="market" type="text" required
               placeholder="e.g. Carmel Valley, Del Mar, 92130">
      </div>
      <div class="field">
        <label for="visibility-brokerage">Your brokerage (optional)</label>
        <input id="visibility-brokerage" name="brokerage" type="text">
      </div>
"""

    lead_agent = agents.author_for("/join")
    body = f"""<section class="hero hero--bottom">
  {c.picture("/assets/img/backgrounds/join-hero.jpg",
             alt="Masooma, Nilab, Zohra and Sofia Azizi of Team Azizi",
             width=1537, height=1023, cls="hero__media", eager=True)}
  <div class="hero__inner">
    <h1>Build your career and brand with Team Azizi</h1>
    <p class="hero__sub">The support, experience and expertise to reach your next level</p>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn--light" href="#apply">Find out how we can support you</a>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container" style="text-align:center">
    <p class="eyebrow">Careers at Team Azizi &mdash; licensed agents</p>
    <h2>Build a business, not a job</h2>
    <p class="lede" style="margin-inline:auto">
      The licensees who do best here stop counting transactions and start
      thinking in territory &mdash; a place they own, a name buyers search
      for, and a pipeline that does not reset every January. Everything below
      exists so you are building that instead of building a marketing
      department. And every claim on this page is published with its source,
      because you are deciding where to move a licence, not clicking an ad.
    </p>
    <div class="stats">
{proof_stats}
    </div>
    <p class="stats__source">
      {site.PROOF['list_rank']} of all California large teams by volume on
      <a href="{site.PROOF['source_url']}" rel="nofollow noopener"
      target="_blank">{c.esc(site.PROOF['list_name'])}</a>, RealTrends
      Verified, reporting 2025 production &mdash; and one of the top 10 teams
      in the county, San&nbsp;Diego Business Journal, October 2025.
    </p>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <h2 class="rule-center" style="text-align:center">Why join Team Azizi?</h2>
    <div class="grid grid--4" style="margin-top:3.5rem;text-align:center">
{why_cards}
    </div>
    <div class="cta-row" style="justify-content:center;margin-top:3.5rem">
      <a class="btn btn--light" href="#apply">Find out how we can support you</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split__body">
      <p class="eyebrow">Who you would be joining</p>
      <h2>A family team, {site.PROOF['closed_sales']} closed sales</h2>
      <p>
        Team Azizi was founded by Sonia Azizi and is led today by
        {c.esc(site.LEAD_AGENT)}. It is a family team that grew into one of
        the county&rsquo;s largest, and it works the full price spectrum
        &mdash; first homes through estates &mdash; which is why the guides
        here talk about tax districts and school boundaries rather than
        lifestyle adjectives.
      </p>
      <p>
        The agents who do best here are the ones who wanted a place to own
        and the room to become the person who answers for it.
      </p>
      <div class="cta-row" style="margin-top:2rem">
        <a class="btn btn--dark" href="#apply">Find out how we can support you</a>
        <a class="btn" href="/team">Meet the team</a>
      </div>
    </div>
    <div class="split__media">
      {c.picture("/assets/img/team/team-azizi-four-terrace.jpg",
                 alt="Masooma, Nilab, Zohra and Sofia Azizi of Team Azizi",
                 width=1130, height=1392,
                 sizes="(min-width: 62rem) 45vw, 92vw")}
    </div>
  </div>
</section>

<section class="section section--panel">
  <div class="container container--narrow">
    <p class="eyebrow">What you get</p>
    <h2 class="rule-gold">The support behind a licensee</h2>
    <p>
      An agent joining a team is buying back time and borrowing a platform.
      Specifically, here:
    </p>
    <div class="grid grid--2" style="margin-top:2.5rem">
{gets_cards}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <p class="eyebrow">Territory</p>
    <h2 class="rule-gold">Where the team works</h2>
    <p style="max-width:46rem">
      An agent evaluating a team is really asking which part of the county
      would be theirs. Team Azizi covers {len(site.ALL_AREAS)} communities in
      five clusters, each with a published guide you would inherit and keep
      current. Which one is yours is among the first things to settle.
    </p>
    <div class="grid grid--4" style="margin-top:2.5rem">
{region_cards}
    </div>
    <p style="margin-top:2rem">
      <a class="btn" href="/neighborhoods">All {len(site.ALL_AREAS)} guides</a>
    </p>
  </div>
</section>

<section class="section section--panel" id="visibility-check">
  <div class="container container--narrow">
    <p class="eyebrow">Free, and yours whether we ever speak</p>
    <h2 class="rule-gold">Are you there when a seller asks an AI who to hire?</h2>
    <p>
      Buyers and sellers increasingly open ChatGPT, Gemini or Perplexity
      before they open Zillow, and ask it plainly: who should I hire to sell
      my house in Carmel&nbsp;Valley. The assistant answers with names, and
      cites the sources it drew them from. Most agents have never checked
      whether they are in that answer &mdash; or who is.
    </p>
    <p>
      Send the form and a member of the team runs the same query panel we run
      on ourselves every month, for your market, and sends you what comes
      back:
    </p>
    <ul>
      <li>Whether you are named in the answers to the questions sellers and
      buyers actually ask about your areas, across
      <strong>ChatGPT, Gemini, Perplexity and Google&rsquo;s AI
      Overviews</strong>.</li>
      <li><strong>Which agents and teams do get named</strong> for those same
      questions in your market.</li>
      <li><strong>Which sources the assistants cite</strong> when they answer
      &mdash; the part almost nobody looks at, and the part you can act
      on.</li>
    </ul>
    <p>
      Two honest notes. A person runs this, so it is not an instant score and
      it will not land in your inbox in ten seconds. And we know exactly what
      the report feels like to read, because our own first one came back
      <strong>absent from fourteen of fourteen queries</strong> &mdash; which
      is why this site exists in the shape it does.
    </p>
    {lead_form(kind="visibility", subject="AI visibility check request",
               cta="Send me my visibility check", address=False,
               extra=vis_extra)}
    <p class="updated" style="margin-top:1.5rem">
      No obligation to talk about joining anything. If the result is that you
      are already everywhere, we will tell you that too.
    </p>
  </div>
</section>

<section class="band band--heavy">
  {c.picture("/assets/img/backgrounds/work-with-us.jpg", width=1920,
             height=1200, cls="band__media")}
  <div class="container">
    <h2 class="rule-center">Your next chapter starts here</h2>
    <p style="margin-inline:auto">
      One conversation, no commitment, and the terms in writing before
      anything else. If you are weighing two or three teams at once, ask all
      of them the questions in the terms section below &mdash; the answers
      separate them faster than any careers page can.
    </p>
    <div class="cta-row">
      <a class="btn btn--light" href="#apply">Find out how we can support you</a>
      <a class="btn btn--light" href="{site.PHONE_HREF}">{site.PHONE_DISPLAY}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container container--narrow">
    <p class="eyebrow">The detail</p>
    <h2 class="rule-gold">Questions agents actually ask</h2>

{blocks}

    <h2 class="rule-gold" style="margin-top:3.5rem" id="apply">Find out how we can support you</h2>
    <p>
      Send this and a member of the team replies directly. Salaried marketing
      roles are on the <a href="/careers">careers page</a>.
    </p>
    {lead_form(kind="join", subject="Agent careers enquiry",
               cta="Find out how we can support you", address=False, extra=extra)}
    <p class="updated" style="margin-top:2.5rem">Last updated {TODAY}</p>
  </div>
</section>"""

    write(
        "/join",
        c.page(
            title="Join Our Team — Real Estate Agent Careers | Team Azizi at Compass",
            description=(
                "Join Team Azizi, a 19-licensee Compass team covering 31 San "
                "Diego County and Temecula Valley communities. A territory of "
                "your own, marketing already built, and the terms in writing "
                "before you move your licence."
            ),
            path="/join",
            body=body,
            nodes=c.base_nodes() + [
                schema.web_page(
                    url=f"{site.DOMAIN}/join", name="Join Our Team",
                    author_slug=lead_agent["slug"], updated=TODAY,
                ),
                schema.faq_page(faq_from_blocks(blocks)),
                schema.breadcrumbs([
                    ("Home", f"{site.DOMAIN}/"),
                    ("Join Our Team", f"{site.DOMAIN}/join"),
                ]),
            ],
            hero=True,
            audience="agent",
        ),
        changefreq="monthly",
        priority="0.7",
    )


# The two salaried roles. Range and rendered text come from here and nowhere
# else, so the page copy and the JobPosting markup cannot drift — which
# matters more than usual because California SB 1162 requires the pay scale
# to appear in the posting itself, not merely in the structured data.
W2_ROLES = [
    {
        "id": "paid-advertising",
        "title": "Paid Advertising",
        "min": 150_000,
        "max": 175_000,
        "blurb": (
            "Paid search and paid social pointed at pages that already "
            "answer the query &mdash; the "
            "<a href=\"/home-valuation\">valuation tool</a> and the "
            "<a href=\"/mello-roos\">Mello-Roos lookup</a> are the two "
            "proven destinations, and the neighborhood guides give every "
            "campaign a landing page that is not a search widget."
        ),
        "schema_description": (
            "Run paid search and paid social for a 19-licensee Compass real "
            "estate team covering 31 San Diego County and Temecula Valley "
            "communities, pointing spend at an existing library of "
            "neighborhood guides, a home-valuation tool and a Mello-Roos "
            "lookup rather than at generic landing pages."
        ),
    },
    {
        "id": "social-media-management",
        "title": "Social Media Management",
        "min": 80_000,
        "max": 115_000,
        "blurb": (
            "The team&rsquo;s Instagram is its largest owned audience, and "
            "every <a href=\"/blog\">journal post</a> and guide refresh is "
            "written to become a post there. This role runs that pipeline "
            "rather than starting a feed from nothing."
        ),
        "schema_description": (
            "Own social media for a 19-licensee Compass real estate team in "
            "San Diego County: turn an existing pipeline of neighborhood "
            "guides and sourced journal posts into Instagram and social "
            "content, and support 19 licensees across 31 communities."
        ),
    },
]


def build_careers() -> None:
    """Salaried roles, split off `/join` at the client's call — correctly.

    Two audiences that share nothing but an employer. A licensed agent is
    weighing a 1099 territory against the team they are already on; a
    marketing candidate is comparing a salary band against other salaried
    jobs and will never read a word about Mello-Roos. One page trying to
    serve both buries each of them in the other's material, and splits the
    query too: "join a real estate team san diego" and "paid ads manager san
    diego" want different pages.

    This is also where the `JobPosting` markup lives, because this is where
    the salaried openings are. `/join` carries none — see schema.job_posting.
    """
    def money(n: int) -> str:
        return f"${n:,}"

    role_cards = "\n".join(
        f"""      <div>
        <h3 class="rule-gold">{r['title']}</h3>
        <p class="eyebrow" style="margin-bottom:0.5rem">Full-time employee
        &middot; {money(r['min'])}&ndash;{money(r['max'])}</p>
        <p>{r['blurb']}</p>
      </div>"""
        for r in W2_ROLES
    )
    options = "\n".join(
        f'          <option value="{r["id"]}">{r["title"]}</option>'
        for r in W2_ROLES
    )

    blocks = "\n\n".join([
        c.answer_block(
            anchor="open-roles",
            question="What salaried roles is Team Azizi hiring for?",
            lead=(
                f"Team Azizi is hiring two full-time employee roles in San "
                f"Diego County &mdash; Paid Advertising at "
                f"{money(W2_ROLES[0]['min'])}&ndash;{money(W2_ROLES[0]['max'])} "
                f"and Social Media Management at "
                f"{money(W2_ROLES[1]['min'])}&ndash;{money(W2_ROLES[1]['max'])} "
                f"&mdash; both working from the Compass office at "
                f"{c.esc(site.STREET)} in Carmel&nbsp;Valley."
            ),
            body=(
                f"<p>Both roles support {len(agents.ROSTER)} licensees across "
                f"{len(site.ALL_AREAS)} communities rather than carrying a "
                f"book of clients, which is the practical difference between "
                f"these and the agent roles on "
                f"<a href=\"/join\">the join-our-team page</a>. The licensed "
                f"agent positions are independent-contractor and "
                f"commission-based; these two are salaried employment.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="what-exists",
            question="What would I be working with on day one?",
            lead=(
                f"The marketing infrastructure at Team Azizi already exists "
                f"and is public: {len(site.ALL_AREAS)} San Diego County and "
                f"Temecula Valley neighborhood guides, a journal of sourced "
                f"posts, a home-valuation tool and a Mello-Roos lookup that "
                f"answers the county&rsquo;s most-repeated buyer question."
            ),
            body=(
                "<p>Neither role starts from nothing, which is the unusual "
                "part of both. The social pipeline has a standing supply of "
                "material &mdash; every <a href=\"/blog\">journal post</a> "
                "and guide refresh is written to be recycled &mdash; and "
                "paid campaigns have destinations that answer the query "
                "rather than a generic landing page. What is missing in both "
                "cases is the person to run it consistently.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="pay-and-terms",
            question="Are these employee roles, and is the pay range real?",
            lead=(
                "Both San Diego County roles are full-time W-2 employment "
                "rather than contract, and the ranges published above are "
                "the ranges &mdash; printed on the page rather than held "
                "back for a screening call."
            ),
            body=(
                "<p>California requires pay scales in job postings for "
                "covered employers, and publishing them is the right "
                "practice regardless of whether a given employer is covered: "
                "a candidate should not have to spend two interviews finding "
                "out the job pays less than their current one. Benefits, "
                "start date and reporting line are settled per role and "
                "belong in writing before anyone accepts.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="apply",
            question="How do you apply for a salaried role at Team Azizi?",
            lead=(
                "Applications for the Team Azizi salaried roles in San Diego "
                "County go through the form below &mdash; name, contact "
                "details, which of the two roles, and anything you want to "
                "point at: campaigns you have run, accounts you have grown, "
                "a portfolio link."
            ),
            body=(
                "<p>A link to work beats a description of it for both of "
                "these roles. If you hold a California real estate licence "
                "as well, say so &mdash; it is not required for either "
                "position, and the licensed agent path is a separate "
                "conversation on <a href=\"/join\">the join-our-team "
                "page</a>.</p>"
            ),
            heading="h2",
        ),
    ])

    extra = f"""      <div class="field">
        <label for="careers-role">Which role</label>
        <select id="careers-role" name="role" required>
{options}
        </select>
      </div>
      <div class="field">
        <label for="careers-work">Portfolio, campaigns or accounts to point at</label>
        <textarea id="careers-work" name="work" rows="4"></textarea>
      </div>
"""

    lead_agent = agents.author_for("/careers")
    body = f"""<section class="section" style="padding-top:calc(var(--nav-h) + 3rem)">
  <div class="container container--narrow">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; Careers
    </nav>
    <p class="eyebrow">Careers at Team Azizi</p>
    <h1>Salaried roles</h1>
    <p class="lede">
      Two full-time employee positions at a {len(agents.ROSTER)}-licensee
      Compass team covering {len(site.ALL_AREAS)} communities across San
      Diego County and the Temecula Valley &mdash; both supporting the whole
      team rather than carrying clients, and both with the pay range printed
      below rather than saved for the interview.
    </p>
    <p class="updated">
      Looking for a licensed agent role instead? Those are
      independent-contractor positions working a territory, and they live on
      the <a href="/join">join-our-team page</a>.
    </p>
  </div>
</section>

<section class="section section--panel">
  <div class="container">
    <p class="eyebrow">Open positions</p>
    <h2 class="rule-gold">What the team is hiring for</h2>
    <div class="grid grid--2" style="margin-top:2.5rem">
{role_cards}
    </div>
  </div>
</section>

<section class="section">
  <div class="container container--narrow">

{blocks}

    <h2 class="rule-gold" style="margin-top:3.5rem" id="apply">Apply</h2>
    <p>
      Send the form and a member of the team replies directly. Applications
      for both San Diego County roles arrive in the same place.
    </p>
    {lead_form(kind="careers", subject="Careers application",
               cta="Send application", address=False, extra=extra)}
    <p class="updated" style="margin-top:2.5rem">Last updated {TODAY}</p>
  </div>
</section>"""

    write(
        "/careers",
        c.page(
            title="Careers — Salaried Marketing Roles | Team Azizi at Compass",
            description=(
                "Full-time salaried openings at Team Azizi, a 19-licensee "
                "Compass real estate team in San Diego County: Paid "
                "Advertising ($150,000-$175,000) and Social Media Management "
                "($80,000-$115,000), based in Carmel Valley."
            ),
            path="/careers",
            body=body,
            nodes=c.base_nodes() + [
                schema.web_page(
                    url=f"{site.DOMAIN}/careers", name="Careers",
                    author_slug=lead_agent["slug"], updated=TODAY,
                ),
                schema.faq_page(faq_from_blocks(blocks)),
                schema.breadcrumbs([
                    ("Home", f"{site.DOMAIN}/"),
                    ("Careers", f"{site.DOMAIN}/careers"),
                ]),
            ] + [
                schema.job_posting(
                    url=f"{site.DOMAIN}/careers",
                    identifier=r["id"],
                    title=r["title"],
                    description=r["schema_description"],
                    posted=TODAY,
                    salary_min=r["min"],
                    salary_max=r["max"],
                )
                for r in W2_ROLES
            ],
            audience="agent",
        ),
        changefreq="monthly",
        priority="0.7",
    )


def build_mello_roos() -> None:
    """The lead magnet, and the site's single strongest differentiator.

    `research/competitors.md` found that **not one competitor page mentions
    Mello-Roos at all**, despite it being the most-repeated buyer question in
    92127. Everyone writes around it because getting it right means reading a
    county PDF. `build/data/taxes.py` is that PDF, parsed.

    Every one of the thirty-one panels is server-rendered and present in the
    HTML, hidden with CSS rather than built on demand. An AI fetcher does not
    run JavaScript, and a lookup tool whose answers only exist after a click
    is a lookup tool no model can ever cite. The <select> is a convenience
    for people; the data is there for everyone.
    """
    path = "/mello-roos"
    lead = agents.author_for("/mello-roos")

    panels = []
    options = []
    for area in site.ALL_AREAS:
        slug, name = area["slug"], area["name"]
        cfd = taxes.for_hood(slug) or {}
        options.append(
            f'          <option value="{slug}">{c.esc(name)}</option>'
        )

        if cfd.get("districts"):
            # A "(xxx) ..." value is a phone and gets a tel: link; the
            # Riverside entries carry a website string instead, which a
            # tel: link would mangle.
            rows = "\n".join(
                "        <tr><td>{}</td><td>{}</td><td>{}<br>{}</td></tr>".format(
                    c.esc(d[0]), c.esc(d[1]), c.esc(d[2]),
                    (
                        f"<a href=\"tel:{d[3].replace(' ', '').replace('(', '').replace(')', '').replace('-', '')}\">{c.esc(d[3])}</a>"
                        if d[3].startswith("(")
                        else c.esc(d[3])
                    ),
                )
                for d in cfd["districts"]
            )
            table = f"""      <table class="cfd">
        <caption class="visually-hidden">Active community facilities
          districts named for {c.esc(name)}</caption>
        <thead><tr><th>District</th><th>Fund</th><th>Administrator</th></tr></thead>
        <tbody>
{rows}
        </tbody>
      </table>"""
            verdict = f"{c.esc(name)} does carry Mello-Roos."
        else:
            table = ""
            verdict = (
                f"No active district in the county list is named for "
                f"{c.esc(name)}."
            )

        panels.append(f"""    <div class="cfd-panel" data-cfd="{slug}" hidden>
      <h3 class="rule-gold">{c.esc(name)}</h3>
      <p class="lede">{verdict}</p>
      <p>{cfd.get('note', '')}</p>
{table}
      <p class="answer__source">{taxes.VERIFY_NOTE}</p>
      <p><a class="btn" href="/neighborhoods/{slug}">Full {c.esc(name)} guide</a></p>
    </div>""")

    blocks = "\n\n".join([
        c.answer_block(
            anchor="what-is-mello-roos",
            question="What is Mello-Roos?",
            lead=(
                "Mello-Roos is an additional property tax levied inside a "
                "community facilities district (CFD), used in San Diego "
                "County and across California to pay for the schools, roads "
                "and parks that a new development required. It is charged on "
                "top of the ordinary property tax, it is set per parcel "
                "rather than per neighborhood, and it appears as a separate "
                "line item on the tax bill."
            ),
            body=(
                "<p>The name comes from the Mello-Roos Community Facilities "
                "Act of 1982, passed after Proposition&nbsp;13 limited what "
                "cities could raise through ordinary property tax. The "
                "practical effect for a buyer today: two similar homes on the "
                "same street can carry materially different monthly costs, "
                "and the difference is invisible in a listing price.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="how-much",
            question="How much is Mello-Roos in San Diego County?",
            lead=(
                "No single San Diego County figure exists, and any source "
                "quoting one for a whole city has not read the county's "
                "list. A Mello-Roos "
                "amount is specific to the parcel: it varies by district, by "
                "improvement area within that district, and by the phase a "
                "home was built in. The authoritative number is the line item "
                "on that property's tax bill, which names the district and "
                "gives a contact number."
            ),
            body=(
                "<p>That is why this page gives you district names and "
                "administrator phone numbers rather than a dollar figure. The "
                "administrator can tell you the current levy and the "
                "remaining term for a specific address; a website cannot.</p>"
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="san-marcos-91",
            question="Which San Diego city has the most Mello-Roos?",
            lead=(
                "San Marcos, by a wide margin. The County Auditor's active "
                "FY&nbsp;2025-26 list carries 91 community facilities "
                "districts for San Marcos &mdash; more than any other city in "
                "San Diego County. Most are separately numbered improvement "
                "areas within a small number of parent districts, which is "
                "precisely why no single San Marcos figure exists."
            ),
            heading="h2",
        ),
        c.answer_block(
            anchor="pusd-vs-poway",
            question="Can I get Poway Unified schools without a big Mello-Roos bill?",
            lead=(
                "The city of Poway is where to look. Poway Unified "
                "administers 19 active districts, but the bulk of that load "
                "sits in the newer 92127 communities the district also serves "
                "&mdash; Del Sur, 4S Ranch, the Black Mountain Ranch villages "
                "&mdash; rather than in the older city of Poway itself, which "
                "was largely built before those districts were formed."
            ),
            body=(
                "<p>Same school district, materially different total monthly "
                "cost, older housing stock and larger lots in exchange. It is "
                "a parcel-level question rather than a guarantee &mdash; the "
                "tax bill confirms it &mdash; but it is real, checkable, and "
                "almost nobody spells it out. See the "
                "<a href=\"/neighborhoods/poway\">Poway guide</a>.</p>"
            ),
            heading="h2",
        ),
    ])

    body = f"""<section class="section" style="padding-top:calc(var(--nav-h) + 3rem)">
  <div class="container container--narrow">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; Mello-Roos
    </nav>
    <p class="eyebrow">Property tax</p>
    <h1>Mello-Roos in North San Diego County</h1>
    <p class="lede">
      The most-asked question in 92127, and the one almost no agent site
      answers &mdash; because answering it means reading the County
      Auditor&rsquo;s own district list rather than guessing. Below is that
      list, for all {len(site.ALL_AREAS)} communities we cover, including the
      seven where the honest answer is &ldquo;none.&rdquo;
    </p>

    <h2 class="rule-gold" style="margin-top:2.5rem">
      Look up a community
    </h2>
    <div class="cfd-tool">
      <div class="field">
        <label for="cfd-select">Choose a community</label>
        <select id="cfd-select" data-cfd-select>
          <option value="">Select&hellip;</option>
{chr(10).join(options)}
        </select>
      </div>
{chr(10).join(panels)}
    </div>

{blocks}

    <h2 class="rule-gold" style="margin-top:3.5rem">
      Want the number for a specific address?
    </h2>
    <p>
      The district administrator can give you the current levy and remaining
      term once you know which district applies. If you would rather we just
      pulled it together &mdash; the districts, the schools, and what
      comparable homes on that street actually sold for &mdash; send the
      address.
    </p>

    <form class="valuation" method="POST" action="{site.LEAD_ENDPOINT}"
          data-lead-form data-lead-kind="mello-roos">
      <input type="hidden" name="_subject" value="Mello-Roos lookup request"
             data-subject-prefix="Mello-Roos lookup">
      <input type="hidden" name="_next" value="{site.DOMAIN}/thank-you">
      <input type="text" name="_gotcha" tabindex="-1" autocomplete="off"
             aria-hidden="true"
             style="position:absolute;left:-9999px;width:1px;height:1px">
      <div class="field">
        <label for="mr-address">Property address</label>
        <input id="mr-address" name="address" type="text" required
               autocomplete="street-address"
               placeholder="1234 Example St, San Marcos CA 92078">
      </div>
      <div class="grid grid--2">
        <div class="field">
          <label for="mr-name">Name</label>
          <input id="mr-name" name="name" type="text" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="mr-email">Email</label>
          <input id="mr-email" name="email" type="email" autocomplete="email" required>
        </div>
      </div>
      <div class="field">
        <label for="mr-phone">Phone</label>
        <input id="mr-phone" name="phone" type="tel" autocomplete="tel">
      </div>
      <div class="consent">
        <input id="mr-consent" name="consent" type="checkbox" required>
        <p><label for="mr-consent" style="display:inline;font-size:inherit;
           font-weight:400;letter-spacing:0;text-transform:none">
           {c.esc(site.TCPA_CONSENT)}</label></p>
      </div>
      <button class="btn btn--filled" type="submit">Send me the tax picture</button>
    </form>

    <p class="answer__source" style="margin-top:2.5rem">
      Source: <a href="{taxes.SOURCE_URL}" rel="nofollow noopener"
      target="_blank">{c.esc(taxes.SOURCE_NAME)}</a>, retrieved
      {taxes.RETRIEVED}. The Auditor&rsquo;s list names <em>districts</em>; it
      does not map <em>parcels</em>. &ldquo;No district is named for X&rdquo;
      is a fact about that list, not a parcel-level guarantee &mdash; a
      homeowner can sit inside a differently-named district. The tax bill is
      where the truth for a given parcel lives.
    </p>
    <p class="updated">Last updated {TODAY}</p>
  </div>
</section>"""

    faq = faq_from_blocks(blocks)

    write(
        path,
        c.page(
            title=(
                "Mello-Roos in North San Diego County — Every Active District "
                "by Community | Team Azizi"
            ),
            description=(
                "Which Mello-Roos districts apply in Escondido, San Marcos, "
                "Carlsbad, Poway, Del Sur, 4S Ranch and 10 more communities — "
                "from the County Auditor's active FY 2025-26 list, with "
                "administrator contacts. Including the seven with none."
            ),
            path=path,
            body=body,
            nodes=c.base_nodes() + [
                schema.web_page(
                    url=f"{site.DOMAIN}{path}",
                    name="Mello-Roos in North San Diego County",
                    author_slug=lead["slug"],
                    updated=TODAY,
                ),
                schema.faq_page(faq),
                schema.breadcrumbs([
                    ("Home", f"{site.DOMAIN}/"),
                    ("Mello-Roos", f"{site.DOMAIN}{path}"),
                ]),
            ],
            og_image="/assets/img/og/mello-roos.jpg",
        ),
        changefreq="monthly",
        priority="0.9",
    )


def build_blog() -> None:
    """The blog index and one page per post.

    Not generated when there are no posts, for the same reason /testimonials
    is not: an empty index advertises an abandoned blog, which is a worse
    signal than having none. The old Luxury Presence site shipped a
    copyright notice reading 2022 for four years; nothing here should
    telegraph neglect the same way.
    """
    if not posts.POSTS:
        print("  (no posts yet — /blog not generated)")
        return

    ordered = sorted(posts.POSTS, key=lambda p: p["date"], reverse=True)

    # ---- index ----------------------------------------------------------
    cards = "\n".join(
        f"""      <article class="postcard">
        <h2><a href="/blog/{p['slug']}">{c.esc(p['title'])}</a></h2>
        <p class="updated">{p['date']} &middot; {c.esc(agents.by_slug(p['author'])['name'])}</p>
        <p>{p['dek']}</p>
      </article>"""
        for p in ordered
    )
    body = f"""<section class="section" style="padding-top:calc(var(--nav-h) + 3rem)">
  <div class="container container--narrow">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; Journal
    </nav>
    <p class="eyebrow">Journal</p>
    <h1>Notes on North San Diego County</h1>
    <p class="lede">
      Questions that come up often enough to be worth writing down properly,
      answered from primary sources rather than from what everyone else says.
    </p>
    <div class="postcards">
{cards}
    </div>
    <p class="updated" style="margin-top:2.5rem">Last updated {TODAY}</p>
  </div>
</section>"""
    write(
        "/blog",
        c.page(
            title="Journal — Notes on North San Diego County | Team Azizi",
            description=(
                "Questions about buying and selling in North San Diego "
                "County, answered from primary sources. From Team Azizi at "
                "Compass."
            ),
            path="/blog",
            body=body,
            nodes=c.base_nodes() + [
                schema.breadcrumbs([
                    ("Home", f"{site.DOMAIN}/"),
                    ("Journal", f"{site.DOMAIN}/blog"),
                ]),
            ],
        ),
        changefreq="weekly",
        priority="0.7",
    )

    # ---- posts ----------------------------------------------------------
    for post in ordered:
        author = agents.by_slug(post["author"])
        path = f"/blog/{post['slug']}"
        blocks = "\n\n".join(
            c.answer_block(heading="h2", **b) for b in post["blocks"]
        )
        # Per-post caution line. Each topic needs its own ("confirm with the
        # district" is wrong under an insurance post), so the text lives in
        # the post dict, pre-wrapped to the page's indentation.
        footnote_html = (
            '\n    <p class="answer__source" style="margin-top:2.5rem">\n'
            f"{post['footnote']}\n    </p>"
            if post.get("footnote")
            else ""
        )
        body = f"""<section class="section" style="padding-top:calc(var(--nav-h) + 3rem)">
  <div class="container container--narrow">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; <a href="/blog">Journal</a> &rsaquo;
      {c.esc(post['title'])}
    </nav>
    <p class="eyebrow">Journal</p>
    <h1>{c.esc(post['title'])}</h1>
    {c.byline(author, post['date'])}
    <p class="lede">{post['dek']}</p>

{blocks}
{footnote_html}
    <p class="updated">Published {post['date']}{f" &middot; Revised {post['updated']}" if post.get('updated') else ""}</p>
  </div>
</section>"""
        write(
            path,
            c.page(
                title=f"{post['title']} | Team Azizi",
                description=post["description"],
                path=path,
                body=body,
                nodes=c.base_nodes() + [
                    schema.article(post, author),
                    schema.faq_page(faq_from_blocks(blocks)),
                    schema.breadcrumbs([
                        ("Home", f"{site.DOMAIN}/"),
                        ("Journal", f"{site.DOMAIN}/blog"),
                        (post["title"], f"{site.DOMAIN}{path}"),
                    ]),
                ],
                og_image=f"/assets/img/og/post-{post['slug']}.jpg",
            ),
            changefreq="yearly",
            priority="0.8",
        )


def build_testimonials() -> None:
    """Only generated when there are real testimonials to show.

    An empty testimonials page is worse than no testimonials page — it
    advertises that nobody said anything. So if `testimonials.ENTRIES` is
    empty this writes nothing, and the nav and footer entries stay absent
    because validate.py's link audit would fail the build otherwise.

    Note what is deliberately NOT here: no `Review` nodes, no
    `aggregateRating`. Google prohibits aggregating reviews from other sites
    and makes self-controlled reviews ineligible for the star feature
    regardless. See build/data/testimonials.py for the citation.
    """
    if not testimonials.ENTRIES:
        print("  (no testimonials yet — /testimonials not generated)")
        return

    lead = agents.author_for("/testimonials")
    cards = []
    for t in testimonials.ENTRIES:
        who = agents.by_slug(t["agent"]) if t.get("agent") else None
        attrib = [c.esc(t["name"])]
        if t.get("hood"):
            attrib.append(c.esc(hood(t["hood"])["name"]))
        if t.get("date"):
            attrib.append(c.esc(t["date"]))
        src = (
            f' &middot; <a href="{t["source_url"]}" rel="nofollow noopener" '
            f'target="_blank">{c.esc(t.get("source", "source"))}</a>'
            if t.get("source_url") else ""
        )
        agent_line = (
            f'<p class="updated">Worked with '
            f'<a href="/agent/{who["slug"]}">{c.esc(who["name"])}</a></p>'
            if who else ""
        )
        cards.append(f"""      <figure class="quote">
        <blockquote><p>{c.esc(t["quote"])}</p></blockquote>
        <figcaption>{" &middot; ".join(attrib)}{src}</figcaption>
        {agent_line}
      </figure>""")

    body = f"""<section class="section" style="padding-top:calc(var(--nav-h) + 3rem)">
  <div class="container container--narrow">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; Testimonials
    </nav>
    <p class="eyebrow">Testimonials</p>
    <h1>What clients have said</h1>
    <p class="lede">
      Every one of these was written by a client on a third-party profile,
      and every one links back to it. Nothing here was written by us, and
      nothing has been edited for tone.
    </p>

    <div class="quotes">
{chr(10).join(cards)}
    </div>

    <p class="answer__source" style="margin-top:2.5rem">
      These are reproduced from the agents&rsquo; own third-party profiles
      with a link to each source. They deliberately carry no review
      structured data: Google prohibits aggregating reviews from other sites,
      and makes a business marking up reviews of itself ineligible for the
      star feature regardless. Verify them at the source rather than taking
      our word for it.
    </p>
    <p class="updated">Last updated {TODAY}</p>
  </div>
</section>"""

    write(
        "/testimonials",
        c.page(
            title="Client Testimonials | Team Azizi",
            description=(
                "What Team Azizi clients have said, reproduced from "
                "third-party agent profiles with a link to each source."
            ),
            path="/testimonials",
            body=body,
            nodes=c.base_nodes() + [
                schema.web_page(
                    url=f"{site.DOMAIN}/testimonials",
                    name="Client Testimonials",
                    author_slug=lead["slug"],
                    updated=TODAY,
                ),
                schema.breadcrumbs([
                    ("Home", f"{site.DOMAIN}/"),
                    ("Testimonials", f"{site.DOMAIN}/testimonials"),
                ]),
            ],
        ),
        changefreq="monthly",
        priority="0.7",
    )


def build_contact() -> None:
    """/contact was in the primary nav on all 43 pages, linking at nothing."""
    path = "/contact"
    lead = agents.author_for("/contact")
    body = f"""<section class="section" style="padding-top:calc(var(--nav-h) + 4rem)">
  <div class="container container--narrow">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; Contact
    </nav>
    <p class="eyebrow">Contact</p>
    <h1>Talk to a person</h1>
    <p class="lede">
      Team Azizi works out of the Compass office at {c.esc(site.STREET)} in
      Carmel Valley, across North San Diego County from Oceanside to Ramona.
      Call and you will get a licensee, not a call centre.
    </p>

    <div class="grid grid--2" style="margin-top:2.5rem">
      <div>
        <h2 class="rule-gold">Direct</h2>
        <address style="font-style:normal">
          <a href="{site.PHONE_HREF}">{site.PHONE_DISPLAY}</a><br>
          <a href="mailto:{site.EMAIL}">{site.EMAIL}</a><br><br>
          {c.esc(site.STREET)}<br>
          {c.esc(site.CITY)}, {site.REGION} {site.POSTAL}
        </address>
        <p style="margin-top:1.5rem">
          Looking for a specific area? Each
          <a href="/neighborhoods">neighborhood guide</a> names the agent who
          works it, with their own direct line and DRE number.
        </p>
      </div>

      <form class="valuation" method="POST" action="{site.LEAD_ENDPOINT}"
            data-lead-form data-lead-kind="contact">
        <input type="hidden" name="_subject" value="Website enquiry"
               data-subject-prefix="Enquiry">
        <input type="hidden" name="_next" value="{site.DOMAIN}/thank-you">
        <input type="text" name="_gotcha" tabindex="-1" autocomplete="off"
               aria-hidden="true"
               style="position:absolute;left:-9999px;width:1px;height:1px">
        <div class="field">
          <label for="c-name">Name</label>
          <input id="c-name" name="name" type="text" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="c-email">Email</label>
          <input id="c-email" name="email" type="email" autocomplete="email" required>
        </div>
        <div class="field">
          <label for="c-phone">Phone</label>
          <input id="c-phone" name="phone" type="tel" autocomplete="tel">
        </div>
        <div class="field">
          <label for="c-message">How can we help?</label>
          <textarea id="c-message" name="message" rows="4"></textarea>
        </div>
        <div class="consent">
          <input id="c-consent" name="consent" type="checkbox" required>
          <p><label for="c-consent" style="display:inline;font-size:inherit;
             font-weight:400;letter-spacing:0;text-transform:none">
             {c.esc(site.TCPA_CONSENT)}</label></p>
        </div>
        <button class="btn btn--filled" type="submit">Send</button>
      </form>
    </div>
  </div>
</section>"""
    write(
        path,
        c.page(
            title="Contact Team Azizi — North San Diego County | Team Azizi",
            description=(
                f"Reach Team Azizi at Compass: {site.PHONE_DISPLAY}, "
                f"{site.STREET}, {site.CITY}. Serving North San Diego County "
                "from Oceanside to Ramona."
            ),
            path=path,
            body=body,
            nodes=c.base_nodes() + [
                schema.web_page(
                    url=f"{site.DOMAIN}{path}",
                    name="Contact Team Azizi",
                    author_slug=lead["slug"],
                    updated=TODAY,
                ),
                schema.breadcrumbs([
                    ("Home", f"{site.DOMAIN}/"),
                    ("Contact", f"{site.DOMAIN}{path}"),
                ]),
            ],
        ),
        changefreq="yearly",
        priority="0.8",
    )


def build_404() -> None:
    """Vercel serves site/404.html automatically for a static project.

    Written to `404.html` directly rather than through write(): a 404 must not
    appear in the sitemap, and it is noindex because an indexed error page is
    the one thing worse than no error page.
    """
    body = f"""<section class="section" style="padding-top:calc(var(--nav-h) + 5rem);min-height:60vh">
  <div class="container container--narrow">
    <p class="eyebrow">404</p>
    <h1>That page has moved or no longer exists</h1>
    <p class="lede">
      This site was rebuilt in 2026 and some older links did not survive the
      move. The parts people were usually looking for are below.
    </p>
    <div class="cta-row" style="margin-top:2rem">
      <a class="btn btn--dark" href="/neighborhoods">Neighborhood guides</a>
      <a class="btn btn--dark" href="/properties/sale">Current listings</a>
      <a class="btn btn--dark" href="/team">The team</a>
    </div>
    <p style="margin-top:2.5rem">
      If you were looking for a specific property, call
      {site.PHONE_DISPLAY} and someone will tell you where it ended up.
    </p>
  </div>
</section>"""
    html = c.page(
        title="Page Not Found | Team Azizi",
        description="That page has moved or no longer exists.",
        path="/404",
        body=body,
        nodes=c.base_nodes(),
    )
    html = html.replace(
        "<title>", '<meta name="robots" content="noindex,follow">\n<title>', 1
    )
    (SITE / "404.html").write_text(html, encoding="utf-8")
    print("  site/404.html  (noindex, not in sitemap)")


# --------------------------------------------------------------------------
# Team, grouped by the area each agent farms
# --------------------------------------------------------------------------


def roster_card(agent: dict) -> str:
    photo = (
        c.picture(agent["photo"], alt=agent["name"], width=400, height=400,
                  cls="roster__photo",
                  sizes="(min-width: 62rem) 22vw, (min-width: 40rem) 30vw, 45vw")
        if agent.get("photo")
        else '<div class="roster__photo roster__photo--pending"></div>'
    )
    return f"""      <a class="roster__card" href="/agent/{agent['slug']}">
        {photo}
        <span class="roster__name">{c.esc(agent['name'])}</span>
        <span class="roster__title">{c.esc(agent['title'])}</span>
      </a>"""


def build_team() -> None:
    """Roster organised by neighborhood, not as one undifferentiated grid.

    A flat grid of nineteen faces answers "how big is this team". Grouping by
    area answers "who do I call about Del Sur", which is the question a visitor
    actually arrived with.
    """
    path = "/team"
    groups = []

    for slug in site.NAV_ORDER:
        h = hood(slug)
        members = [a for a in agents.ROSTER if a.get("farms") == slug]
        if members:
            cards = "\n".join(roster_card(a) for a in members)
            body = f'<div class="roster">\n{cards}\n    </div>'
        else:
            body = (
                '<p class="updated">Specialist assignment pending client '
                "confirmation. "
                f"{c.esc(agents.for_neighborhood(slug)[0]['name'])} covers "
                f"{c.esc(h['name'])} enquiries in the meantime.</p>"
            )
        groups.append(f"""    <div class="area-group">
      <div class="area-group__head">
        <h2>{c.esc(h['name'])}</h2>
        <a href="/neighborhoods/{slug}">{h['zip']} guide &rsaquo;</a>
      </div>
      {body}
    </div>""")

    unassigned = [a for a in agents.agents_only() if not a.get("farms")]
    ops = [a for a in agents.ROSTER if a.get("operations")]
    groups.append(f"""    <div class="area-group">
      <div class="area-group__head"><h2>The full team</h2></div>
      <div class="roster">
{chr(10).join(roster_card(a) for a in unassigned)}
      </div>
    </div>""")
    groups.append(f"""    <div class="area-group">
      <div class="area-group__head"><h2>Operations</h2></div>
      <div class="roster">
{chr(10).join(roster_card(a) for a in ops)}
      </div>
    </div>""")

    body = f"""<section class="section" style="padding-top:calc(var(--nav-h) + 3rem)">
  <div class="container">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; Team
    </nav>
    <p class="eyebrow">Meet the team</p>
    <h1>Who covers your neighborhood</h1>
    <p class="lede">
      Team Azizi is {len(agents.agents_only())} licensed agents and
      {len(ops)} operations staff working the North San Diego corridor from the
      Compass office in Carmel&nbsp;Valley. Every neighborhood guide on this
      site is written and kept current by the agent who works there.
    </p>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
{chr(10).join(groups)}
  </div>
</section>

<section class="section section--panel">
  <div class="container container--narrow" style="text-align:center">
    <p class="eyebrow">Careers</p>
    <h2 class="rule-center">Thinking about joining?</h2>
    <p style="margin-top:1.5rem">
      Two different routes in. Licensed agents, and people working toward the
      licence, take a territory as independent contractors &mdash;
      <a href="/join">the join-our-team page</a> sets out the production
      record with its sources, the brokerage, how area farming works, and the
      terms we deliberately do not publish with the questions to ask instead.
      The team is separately hiring two salaried marketing roles, with ranges
      printed on <a href="/careers">the careers page</a>.
    </p>
    <p style="margin-top:2rem">
      <a class="btn btn--filled" href="/join">Agent roles</a>
      <a class="btn" href="/careers">Salaried roles</a>
    </p>
  </div>
</section>"""

    nodes = c.base_nodes() + [
        schema.breadcrumbs(
            [("Home", f"{site.DOMAIN}/"), ("Team", f"{site.DOMAIN}/team")]
        )
    ]
    nodes += [
        schema.agent(
            a,
            hood=next(
                (h for h in site.NEIGHBORHOODS if h['slug'] == a.get('farms')),
                None,
            ),
        )
        for a in agents.ROSTER
    ]

    write(
        path,
        c.page(
            title="Meet the Team — North San Diego Real Estate Agents | Team Azizi",
            description=(
                f"{len(agents.agents_only())} licensed Compass agents covering "
                "Carmel Valley, Del Mar, Rancho Santa Fe, Del Sur, 4S Ranch and "
                f"Scripps Ranch. Find the agent who works your neighborhood. "
                f"Call {site.PHONE_DISPLAY}."
            ),
            path=path,
            body=body,
            nodes=nodes,
        ),
        priority="0.8",
    )


def agent_record_block(agent: dict) -> str | None:
    """What this person has actually closed — including when we cannot say.

    A zero in `sales` does NOT mean "has never sold anything". Only 779 of
    the team's 1,009 records carry an individual attribution
    (research/salesRecord.md), and a team lead's production is routinely
    recorded against the team rather than the person. Printing "0 sales" for
    Nilab Azizi would be both false and damaging, so a zero on a licensee
    gets the team's record instead, and a zero on operations staff gets no
    volume claim at all.
    """
    name = c.esc(agent["name"])
    sales = agent.get("sales") or 0

    if agent.get("operations"):
        return c.answer_block(
            anchor="role",
            question=f"What does {agent['name']} do at Team Azizi?",
            lead=(
                f"{name} works in operations for Team Azizi in San Diego "
                f"rather than as a licensed agent &mdash; the reason there is "
                f"no DRE number on this page. {name} does not represent "
                f"buyers or sellers."
            ),
            heading="h2",
        )

    if sales >= 1:
        plural = "s" if sales != 1 else ""
        return c.answer_block(
            anchor="record",
            question=f"How many homes has {agent['name']} sold?",
            lead=(
                f"{name} has {sales} closed sale{plural} recorded against "
                f"their name in Team Azizi's San Diego County transaction "
                f"history. That is an individual figure, not a share of the "
                f"team total."
            ),
            body=(
                "<p>Team-wide, Team Azizi has "
                f"{site.PROOF['closed_sales']} closed sales and 2025 "
                f"production of {site.PROOF['volume_2025']} across "
                f"{site.PROOF['sides_2025']} sides &mdash; "
                f"{site.PROOF['ca_rank']} on RealTrends Verified&rsquo;s "
                f"{c.esc(site.PROOF['list_name'])}.</p>"
            ),
            heading="h2",
        )

    # A licensee with no attributed count. Say what is true rather than zero.
    return c.answer_block(
        anchor="record",
        question=f"What is {agent['name']}'s track record?",
        lead=(
            f"{name} is a licensed agent with Team Azizi in San Diego "
            f"County. Individual transaction counts are not published here "
            f"for every member of the team, because only part of the "
            f"team&rsquo;s history carries a per-agent attribution and a "
            f"partial number would understate the person rather than "
            f"inform you."
        ),
        body=(
            "<p>The team&rsquo;s own record is "
            f"{site.PROOF['closed_sales']} closed sales, with 2025 "
            f"production of {site.PROOF['volume_2025']} across "
            f"{site.PROOF['sides_2025']} sides &mdash; "
            f"{site.PROOF['ca_rank']} on RealTrends "
            f"Verified&rsquo;s {c.esc(site.PROOF['list_name'])}. Ask "
            f"{name} directly for their own closings in your area; it is a "
            "fair question and there is a real answer.</p>"
        ),
        heading="h2",
    )


def agent_language_block(agent: dict) -> str | None:
    """Only for agents who speak something beyond English.

    "Does anyone at Team Azizi speak Spanish?" is a real query with a real
    answer, and it is the kind of thing a buyer needs and cannot easily find.
    """
    other = [
        lang for lang in (agent.get("languages") or []) if lang != "English"
    ]
    if not other:
        return None
    spoken = " and ".join(other)
    return c.answer_block(
        anchor="languages",
        question=f"Does {agent['name']} speak {other[0]}?",
        lead=(
            f"{c.esc(agent['name'])} works with clients in {c.esc(spoken)} as "
            f"well as English, across Team Azizi&rsquo;s San Diego County "
            f"markets."
        ),
        heading="h2",
    )


def agent_zillow_block(agent: dict) -> str | None:
    """"Review me on Zillow" — only when a real profile URL exists.

    Soliciting reviews to Zillow rather than collecting them on-site is the
    right pattern on two counts. The site cannot carry review schema for
    third-party reviews anyway (Google prohibits aggregating them, see
    data/testimonials.py), and a populated Zillow profile is a `sameAs`
    signal that helps consolidate the entity — which is the problem this
    rebuild exists to fix.

    Eighteen of nineteen agents have no URL yet. Zillow handles do not follow
    from names or Compass handles, and Zillow 403s automated lookups, so
    guessing one means publishing a link to a stranger's profile under our
    client's name. Those pages simply omit the block.
    """
    profile = agents.review_profile(agent)
    if not profile:
        return None
    platform, url = profile
    name = c.esc(agent["name"])
    return f"""<section class="answer" id="review">
  <h2 class="answer__q">Worked with {name}? Leave a review</h2>
  <p class="answer__lead">
    Reviews for {name} live on {c.esc(platform)} rather than on this site,
    where they can be read next to every other agent in San Diego County and
    where nobody at Team Azizi can edit them. If {name} handled your sale or
    purchase, that is the place to say so.
  </p>
  <p style="margin-top:1.25rem">
    <a class="btn btn--filled" href="{url}" rel="nofollow noopener"
       target="_blank">Review {name} on {c.esc(platform)}</a>
    <a class="btn" href="{url}" rel="nofollow noopener"
       target="_blank">Read existing reviews</a>
  </p>
</section>"""


def agent_reach_block(agent: dict, hood_obj: dict | None) -> str:
    name = c.esc(agent["name"])
    dre = (
        f"Their California DRE licence number is {agent['dre']}, which can be "
        "checked against the state register."
        if agent.get("dre")
        else ""
    )
    where = (
        f' They write the <a href="/neighborhoods/{hood_obj["slug"]}">'
        f'{c.esc(hood_obj["name"])} guide</a>.'
        if hood_obj else ""
    )
    return c.answer_block(
        anchor="contact",
        question=f"How do I contact {agent['name']} directly?",
        lead=(
            f"{name} of Team Azizi in San Diego County can be reached on "
            f"{c.esc(agent['phone'])} &mdash; a direct line to the person, "
            f"not a call centre or a shared team inbox. {dre}"
        ),
        body=(
            f"<p>Team Azizi works out of the Compass office at "
            f"{c.esc(site.STREET)}, {c.esc(site.CITY)}, across "
            f"{len(site.ALL_AREAS)} North San Diego County communities.{where} "
            f"Every <a href=\"/neighborhoods\">neighborhood guide</a> names "
            f"the agent who covers that area.</p>"
        ),
        heading="h2",
    )


def build_agents() -> None:
    """One page per agent, at the old /agent/{slug} paths, which are indexed."""
    for agent in agents.ROSTER:
        path = f"/agent/{agent['slug']}"
        farmed = [h for h in site.NEIGHBORHOODS if h["slug"] == agent.get("farms")]
        hood_obj = farmed[0] if farmed else None

        photo = (
            c.picture(agent["photo"], alt=agent["name"], width=320, height=320,
                      cls="expert__photo", eager=True)
            if agent.get("photo")
            else '<div class="expert__photo expert__photo--pending"></div>'
        )
        dre = f"CA DRE# {agent['dre']}" if agent.get("dre") else "Operations"
        tel = "tel:+1" + agent["phone"].replace(".", "")
        area = (
            f"""<p class="lede">{c.esc(agent['name'])} works
      <a href="/neighborhoods/{hood_obj['slug']}">{c.esc(hood_obj['name'])}</a>
      ({hood_obj['zip']}) and writes the neighborhood guide for it.</p>"""
            if hood_obj
            else '<p class="updated">Neighborhood specialism pending client '
            "confirmation.</p>"
        )

        blocks = "\n\n".join(filter(None, [
            agent_record_block(agent),
            agent_language_block(agent),
            agent_reach_block(agent, hood_obj),
            agent_zillow_block(agent),
        ]))

        body = f"""<section class="section" style="padding-top:calc(var(--nav-h) + 3rem)">
  <div class="container">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; <a href="/team">Team</a> &rsaquo;
      {c.esc(agent['name'])}
    </nav>
    <div class="split">
      <div>{photo}</div>
      <div>
        <h1>{c.esc(agent['name'])}</h1>
        <p class="eyebrow">{c.esc(agent['title'])} &middot; {dre}</p>
        {area}
        <div class="cta-row">
          <a class="btn btn--dark" href="{tel}">{c.esc(agent['phone'])}</a>
          <a class="btn btn--dark" href="/contact">Get in touch</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container container--narrow">
{blocks}
  </div>
</section>"""

        nodes = c.base_nodes() + [
            schema.agent(agent, hood=hood_obj),
            schema.faq_page(faq_from_blocks(blocks)),
            schema.breadcrumbs(
                [
                    ("Home", f"{site.DOMAIN}/"),
                    ("Team", f"{site.DOMAIN}/team"),
                    (agent["name"], f"{site.DOMAIN}{path}"),
                ]
            ),
        ]

        where = f" — {hood_obj['name']} Specialist" if hood_obj else ""
        write(
            path,
            c.page(
                title=f"{agent['name']}{where} | Team Azizi at Compass",
                description=(
                    f"{agent['name']}, {agent['title']}, Team Azizi at Compass "
                    f"in San Diego. {dre}. Call {agent['phone']}."
                ),
                path=path,
                body=body,
                nodes=nodes,
            ),
            priority="0.5",
        )


# --------------------------------------------------------------------------
# Sitemap + robots
# --------------------------------------------------------------------------


def build_sitemap() -> None:
    """`lastmod` is a claim about the page, not about the build.

    Stamping TODAY on all 85 URLs every run tells every crawler the whole site
    changed when a single word moved — or when nothing did. That is noise at
    the best of times, and actively harmful in the weeks after DNS points,
    when the initial crawl budget is being allocated and a sitemap that cries
    wolf on every URL is the last thing we want to hand Google and Bing.

    The previous sitemap is its own state file: parse the `lastmod` it already
    carries, and keep it for any page whose rendered HTML came out
    byte-identical this run. New pages and genuinely changed pages get TODAY,
    which is the only thing `lastmod` is supposed to mean.
    """
    previous: dict[str, str] = dict(
        re.findall(
            r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>",
            (SITE / "sitemap.xml").read_text(encoding="utf-8")
            if (SITE / "sitemap.xml").exists()
            else "",
        )
    )

    def lastmod(path: str) -> str:
        loc = xml_escape(site.DOMAIN + path)
        if path in UNCHANGED and loc in previous:
            return previous[loc]
        return TODAY

    urls = "\n".join(
        f"""  <url>
    <loc>{xml_escape(site.DOMAIN + path)}</loc>
    <lastmod>{lastmod(path)}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>"""
        for path, freq, priority in sorted(PAGES)
    )
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
"""
    (SITE / "sitemap.xml").write_text(xml, encoding="utf-8")
    print("  site/sitemap.xml")


def build_robots() -> None:
    """Explicit about AI crawlers rather than relying on a blanket Allow.

    The retrieval bots (OAI-SearchBot, ChatGPT-User, PerplexityBot,
    Claude-SearchBot, Google-Extended) are the ones that fetch a page in order
    to answer and cite. Blocking any of them would forfeit the entire premise
    of this engagement, so they are named and allowed deliberately — a future
    editor changing robots.txt should have to read that sentence first.

    The training crawlers (GPTBot, ClaudeBot, Applebot-Extended) are also
    allowed. For a business whose problem is that models do not know it exists,
    being in the training data is upside, not leakage. That one is genuinely a
    client call and is reversible at any time.

    The old site served a 500 on robots.txt for a stretch, which is worth not
    repeating.
    """
    agents = [
        ("*", "Everything else."),
        ("bingbot", "Bing — also the index ChatGPT retrieval leans on."),
        ("OAI-SearchBot", "ChatGPT search retrieval. Required for citation."),
        ("ChatGPT-User", "User-initiated fetch from a ChatGPT session."),
        ("PerplexityBot", "Perplexity retrieval. Required for citation."),
        ("Claude-SearchBot", "Claude search retrieval."),
        ("Google-Extended", "Gemini / AI Overviews grounding."),
        ("GPTBot", "OpenAI training. Allowed deliberately — see build/generate.py."),
        ("ClaudeBot", "Anthropic training. Same reasoning."),
        ("Applebot-Extended", "Apple Intelligence training. Same reasoning."),
    ]
    blocks = "\n\n".join(
        f"# {note}\nUser-agent: {agent}\nAllow: /" for agent, note in agents
    )
    txt = f"""{blocks}

Sitemap: {site.DOMAIN}/sitemap.xml
"""
    (SITE / "robots.txt").write_text(txt, encoding="utf-8")
    print("  site/robots.txt")


def build_indexnow_key() -> None:
    """IndexNow verifies domain control by fetching this file. Public by
    design — it is a proof of control, not a credential."""
    import indexnow

    (SITE / f"{indexnow.KEY}.txt").write_text(indexnow.KEY, encoding="utf-8")
    print(f"  site/{indexnow.KEY}.txt")


def main() -> int:
    print("Generating site/\n")
    build_home()
    build_neighborhood_hub()
    build_neighborhoods()
    build_home_valuation()
    build_properties()
    build_mello_roos()
    build_sell()
    build_buy()
    build_concierge()
    build_blog()
    build_testimonials()
    build_contact()
    build_thank_you()
    build_404()
    build_team()
    build_join()
    build_careers()
    build_agents()
    build_sitemap()
    build_robots()
    build_indexnow_key()
    print(f"\n{len(PAGES)} page(s) written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
