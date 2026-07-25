"""Site generator.

    python3 build/generate.py

Writes static HTML into site/. Output is committed — there is no build step
on the host, which is the point: the client can open any file in this repo
and read their own website.

Run build/validate.py before every push.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

sys.path.insert(0, str(Path(__file__).parent))

import components as c  # noqa: E402
import schema  # noqa: E402
from data import agents, site  # noqa: E402

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
    return next(h for h in site.NEIGHBORHOODS if h["slug"] == slug)


# Carmel Valley and 4S Ranch were removed from the recovered asset set: the
# archived images depict Carmel Valley, Monterey County and a mid-century
# suburb respectively. An honest placeholder beats a wrong-place photograph
# on the page whose entire SEO problem is being confused with Monterey.
HOOD_IMAGE_MISSING = {"carmel-valley", "4s-ranch"}


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
    cards = "\n".join(hood_card(slug) for slug in site.NAV_ORDER)
    stats = "\n".join(
        [
            stat(site.PROOF["volume_2025"], "2025 sales volume"),
            stat(site.PROOF["sides_2025"], "2025 transaction sides"),
            stat("#1", "In Del Mar by sides"),
            stat(site.PROOF["closed_sales"], "Closed sales on Compass"),
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
      <a class="btn btn--light" href="/sell">What's my home worth?</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container" style="text-align:center">
    <p class="eyebrow">North San Diego County</p>
    <h2>From the coast to the corridor</h2>
    <p class="lede" style="margin-inline:auto">
      Team Azizi represents buyers and sellers across six North San Diego
      communities &mdash; Carmel Valley, Del Mar, Rancho Santa Fe, Del Sur,
      4S&nbsp;Ranch and Scripps Ranch &mdash; from the Compass office at
      {c.esc(site.STREET)} in Carmel&nbsp;Valley.
    </p>

    <div class="stats">
{stats}
    </div>
    <p class="stats__source">
      Source: <a href="{site.PROOF['source_url']}" rel="nofollow noopener"
      target="_blank">RealTrends Verified 2025</a> and the team's Compass
      profile. Every figure on this site is third-party verifiable.
    </p>
  </div>
</section>

<section class="section section--panel">
  <div class="container">
    <p class="eyebrow">Neighborhood guides</p>
    <h2 class="rule-gold">The six communities we actually work in</h2>
    <p>
      Each guide carries current market conditions, the Mello-Roos and
      property-tax math for that community, which streets feed which schools,
      and what we have sold there &mdash; not a search widget and a paragraph.
    </p>
    <div class="grid grid--3" style="margin-top:2.5rem">
{cards}
    </div>
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
        {c.esc(site.LEAD_AGENT)}. The team spans the coastal luxury market at
        the Del Mar end and the inland family communities along the
        I&#8209;15 corridor &mdash; a footprint no other team in the county
        covers as one practice.
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
    cards = "\n".join(hood_card(slug) for slug in site.NAV_ORDER)

    body = f"""<section class="band band--hero" style="padding-top:calc(var(--nav-h) + 4rem)">
  <img class="band__media" src="/assets/img/neighborhoods/_hub-hero.jpg" alt=""
       width="1920" height="1440" fetchpriority="high" decoding="async">
  <div class="container">
    <h1>North San Diego Neighborhood Guides</h1>
    <p style="margin-inline:auto">
      Six communities, from the Del Mar coast to the I&#8209;15 corridor.
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
      carries a dated market snapshot, the Mello-Roos and effective
      property-tax math for that community, school attendance-boundary
      specifics, and the homes Team Azizi has actually sold there.
    </p>
    <div class="grid grid--3" style="margin-top:2.5rem">
{cards}
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
                "North San Diego Neighborhood Guides — Carmel Valley, Del Mar, "
                "Del Sur & More | Team Azizi"
            ),
            description=(
                "Maintained guides to six North San Diego communities: market "
                "conditions, Mello-Roos and property-tax math, school "
                "attendance boundaries and recent sales. From Team Azizi at "
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
    nodes += [schema.agent(a) for a in agents.ROSTER]

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
    build_team()
    build_agents()
    build_sitemap()
    build_robots()
    build_indexnow_key()
    print(f"\n{len(PAGES)} page(s) written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
