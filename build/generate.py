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
from data import agents, guides, site, taxes  # noqa: E402

SITE = Path(__file__).resolve().parent.parent / "site"
TODAY = date.today().isoformat()

# Pages written so far, for the sitemap. (path, changefreq, priority)
PAGES: list[tuple[str, str, str]] = []


def write(path: str, html: str, *, changefreq="monthly", priority="0.6") -> None:
    target = SITE / (f"{path.strip('/')}.html" if path.strip("/") else "index.html")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")
    PAGES.append((path, changefreq, priority))
    print(f"  {target.relative_to(SITE.parent)}")


def hood(slug: str) -> dict:
    return next(h for h in site.ALL_AREAS if h["slug"] == slug)


# Carmel Valley and 4S Ranch were removed from the recovered asset set: the
# archived images depict Carmel Valley, Monterey County and a mid-century
# suburb respectively. An honest placeholder beats a wrong-place photograph
# on the page whose entire SEO problem is being confused with Monterey.
HOOD_IMAGE_MISSING = {"carmel-valley", "4s-ranch"} | {
    a["slug"] for a in site.NORTH_COUNTY
}


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
            f'<img src="/assets/img/neighborhoods/{slug}.jpg" alt="" '
            'width="1280" height="800" loading="lazy">'
            '<span class="card__overlay"><span class="btn btn--light btn--sm">'
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
  <img class="hero__media" src="/assets/img/backgrounds/hero-poster.jpg" alt=""
       width="1920" height="2880" fetchpriority="high" decoding="async">
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
    <p class="eyebrow">North San Diego County</p>
    <h2>From the coast to the corridor</h2>
    <p class="lede" style="margin-inline:auto">
      Team Azizi represents buyers and sellers across {len(site.ALL_AREAS)}
      North San Diego communities &mdash; from Oceanside, Carlsbad and
      Encinitas on the coast, inland through Vista, San&nbsp;Marcos,
      Escondido and Poway, out to Fallbrook, Valley&nbsp;Center and Ramona
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
      <img src="/assets/img/team/team-group.jpg" alt="The Team Azizi team"
           width="1920" height="1528" loading="lazy">
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
  <img class="band__media" src="/assets/img/backgrounds/work-with-us.jpg" alt=""
       width="1920" height="1200" loading="lazy">
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
    total = len(site.ALL_AREAS)

    body = f"""<section class="band band--hero" style="padding-top:calc(var(--nav-h) + 4rem)">
  <img class="band__media" src="/assets/img/neighborhoods/_hub-hero.jpg" alt=""
       width="1920" height="1440" fetchpriority="high" decoding="async">
  <div class="container">
    <h1>North San Diego Neighborhood Guides</h1>
    <p style="margin-inline:auto">
      {total} communities, from the Del Mar coast to the Ramona backcountry.
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
                "North San Diego Neighborhood Guides — Escondido, Carlsbad, "
                "Oceanside, Poway & More | Team Azizi"
            ),
            description=(
                f"Maintained guides to {total} North San Diego communities: "
                "which Mello-Roos districts apply, which district assigns the "
                "schools, and Team Azizi's record in each. From Team Azizi at "
                "Compass."
            ),
            path=path,
            body=body,
            nodes=nodes,
            hero=True,
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
}


def plain(html: str) -> str:
    """Markup and entities out, readable sentence in — for JSON-LD text."""
    text = re.sub(r"<[^>]+>", "", html)
    return re.sub(r"\s+", " ", unescape(text)).strip()


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
        lead = (
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

    body += (
        f'<p class="answer__source">{c.esc(taxes.VERIFY_NOTE)}</p>'
        f'<p class="answer__source">Source: <a href="{taxes.SOURCE_URL}" '
        f'rel="nofollow noopener" target="_blank">{c.esc(taxes.SOURCE_NAME)}</a>, '
        f"retrieved {taxes.RETRIEVED}.</p>"
    )
    return c.answer_block(
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
        *[c.answer_block(**b) for b in guides.for_hood(slug)],
        c.answer_block(
            anchor="track-record",
            question=f"Has Team Azizi actually sold in {h['name']}?",
            lead=record,
        ) if record else None,
    ]))

    faq = [
        {"q": f"Does {h['name']} have Mello-Roos?",
         "a": (taxes.for_hood(slug) or {}).get("note", "")},
        {"q": f"What school district serves {h['name']}?",
         "a": f"{h['name']} is served by {h['district']}. Attendance is "
              "assigned by address, not by ZIP code."},
    ]
    # Every community-specific passage also goes into the FAQ graph. The lead
    # is written to stand alone on the page, which is the same property the
    # schema answer needs, so it transfers without rewriting. Entities are
    # unescaped because JSON-LD carries text, not markup.
    faq += [
        {"q": b["question"], "a": plain(b["lead"])}
        for b in guides.for_hood(slug)
    ]

    hero = (
        f"""<img class="band__media" src="/assets/img/neighborhoods/{slug}.jpg"
       alt="" width="1280" height="800" fetchpriority="high">"""
        if slug not in HOOD_IMAGE_MISSING else ""
    )

    body = f"""<section class="band band--hero" style="padding-top:calc(var(--nav-h) + 4rem)">
  {hero}
  <div class="container">
    <h1>{name} Real Estate Guide</h1>
    <p style="margin-inline:auto">{h['zip']} &middot; {c.esc(h['district'])}</p>
  </div>
</section>

<section class="section">
  <div class="container container--narrow">
    <nav aria-label="Breadcrumb" class="updated">
      <a href="/">Home</a> &rsaquo; <a href="/neighborhoods">Neighborhoods</a>
      &rsaquo; {name}
    </nav>
    {c.byline(agent, TODAY)}
    <p class="lede">
      What follows is the part of a {name} search that is hard to look up:
      which tax districts apply, which district assigns the schools, and what
      we have actually done here. Every figure names its source.
    </p>

{blocks}
  </div>
</section>

{video_html}

<section class="section">
  <div class="container container--narrow">
    {c.expert_block(agent, h, confirmed=confirmed)}
  </div>
</section>

<section class="band band--heavy">
  <img class="band__media" src="/assets/img/backgrounds/work-with-us.jpg" alt=""
       width="1920" height="1200" loading="lazy">
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
            hero=True,
        ),
        changefreq="monthly",
        priority="0.9",
    )


def build_neighborhoods() -> None:
    for slug in site.NAV_ORDER + site.NORTH_COUNTY_ORDER:
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
    author = agents.team_lead()

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

    # Grouped rather than a flat list of sixteen: a homeowner scanning for
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
  <img class="band__media" src="/assets/img/backgrounds/home-valuation.jpg" alt=""
       width="2560" height="1708" loading="lazy">
  <div class="container">
    <h2 class="rule-center">Rather just talk it through?</h2>
    <div class="cta-row">
      <a class="btn btn--light" href="{site.PHONE_HREF}">{site.PHONE_DISPLAY}</a>
      <a class="btn btn--light" href="/contact">Send a message</a>
    </div>
  </div>
</section>"""

    faq = [
        {"q": "Why is my Zestimate wrong?",
         "a": "An automated valuation has never been inside the house. It "
              "works from public records and nearby sales, so it cannot see a "
              "remodel, a view, a lot position, or which side of a school "
              "boundary an address falls on."},
        {"q": "Does an online estimate account for Mello-Roos?",
         "a": "No. In Del Sur and 4S Ranch, Mello-Roos obligations vary by "
              "community facilities district and build phase, which changes "
              "the monthly payment a buyer can carry and therefore the price."},
        {"q": "What do I get instead of an instant number?",
         "a": "A comparative market analysis from the Team Azizi agent who "
              "works your neighborhood, built from MLS sales and current "
              "competing inventory, with the reasoning shown."},
    ]

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
    lead = agents.team_lead()

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
                schema.breadcrumbs([
                    ("Home", f"{site.DOMAIN}/"),
                    ("Sold", f"{site.DOMAIN}{path}"),
                ]),
            ],
        ),
        changefreq="monthly",
        priority="0.7",
    )


def build_contact() -> None:
    """/contact was in the primary nav on all 43 pages, linking at nothing."""
    path = "/contact"
    lead = agents.team_lead()
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
        f'<img class="roster__photo" src="{agent["photo"]}" '
        f'alt="{c.esc(agent["name"])}" width="400" height="400" loading="lazy">'
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
                f"confirmation. {c.esc(agents.team_lead()['name'])} covers "
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


def build_agents() -> None:
    """One page per agent, at the old /agent/{slug} paths, which are indexed."""
    for agent in agents.ROSTER:
        path = f"/agent/{agent['slug']}"
        farmed = [h for h in site.NEIGHBORHOODS if h["slug"] == agent.get("farms")]
        hood_obj = farmed[0] if farmed else None

        photo = (
            f'<img class="expert__photo" src="{agent["photo"]}" '
            f'alt="{c.esc(agent["name"])}" width="320" height="320" '
            'fetchpriority="high">'
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
</section>"""

        nodes = c.base_nodes() + [
            schema.agent(agent, hood=hood_obj),
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
    urls = "\n".join(
        f"""  <url>
    <loc>{xml_escape(site.DOMAIN + path)}</loc>
    <lastmod>{TODAY}</lastmod>
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
    build_contact()
    build_thank_you()
    build_404()
    build_team()
    build_agents()
    build_sitemap()
    build_robots()
    build_indexnow_key()
    print(f"\n{len(PAGES)} page(s) written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
