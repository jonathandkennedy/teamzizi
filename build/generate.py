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
from data import site  # noqa: E402

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
    h = hood(slug)
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
    return f"""      <a class="card" href="/neighborhoods/{slug}">
        {media}
        <span class="card__title">{c.esc(h['name'])}</span>
        <span class="card__meta">{h['zip']} &middot; {c.esc(h['district'])}</span>
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
    txt = f"""User-agent: *
Allow: /

Sitemap: {site.DOMAIN}/sitemap.xml
"""
    (SITE / "robots.txt").write_text(txt, encoding="utf-8")
    print("  site/robots.txt")


def main() -> int:
    print("Generating site/\n")
    build_home()
    build_neighborhood_hub()
    build_sitemap()
    build_robots()
    print(f"\n{len(PAGES)} page(s) written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
