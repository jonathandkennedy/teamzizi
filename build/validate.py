"""Pre-push gate. Run this before every commit that touches site/.

    python3 build/validate.py

Checks, in the order they have historically bitten:

1. Every JSON-LD block parses. A single missing brace made CitedRealty's
   homepage graph unparsable and GSC flagged it within hours.
2. No duplicate `@id` across pages — the named common error in the schema
   skill, and the thing that quietly merges two entities into one.
3. `sitemap.xml` parses as XML and every listed URL resolves to a file.
4. No stale NAP string appears anywhere in the output. These are the exact
   strings currently corrupting the entity across the web; the one place
   they must never appear is the canonical source.
5. Unverified claims are surfaced, not silently shipped.

Exit code is non-zero if anything in 1-4 fails.
"""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from data import site  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

LD_BLOCK = re.compile(
    r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.DOTALL | re.IGNORECASE,
)

errors: list[str] = []
warnings: list[str] = []

# Things that are fine mid-build but must never reach production. Running
# with --prelaunch demotes these to loud warnings so development can proceed;
# the launch build runs WITHOUT the flag, so shipping one requires a
# deliberate act rather than a quiet oversight.
blockers: list[str] = []
PRELAUNCH = "--prelaunch" in sys.argv


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def walk_ids(node, sink: list[str]) -> None:
    """Collect every @id in a parsed graph, at any nesting depth."""
    if isinstance(node, dict):
        if "@id" in node and isinstance(node["@id"], str):
            sink.append(node["@id"])
        for value in node.values():
            walk_ids(value, sink)
    elif isinstance(node, list):
        for item in node:
            walk_ids(item, sink)


def check_jsonld(pages: list[Path]) -> None:
    """Parse every block; flag any @id that describes two different things.

    Repeating the *same* entity definition on every page is correct and
    deliberate — an AI fetcher may only ever see one page, so each page has to
    stand alone as a complete statement of the entity. The error the schema
    skill actually warns about is one `@id` meaning different things in
    different places, which silently merges two entities into one.
    """
    definitions: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))

    for page in pages:
        html = page.read_text(encoding="utf-8")
        blocks = LD_BLOCK.findall(html)
        if not blocks:
            warnings.append(f"{rel(page)}: no JSON-LD block")
            continue

        for i, raw in enumerate(blocks):
            try:
                data = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"{rel(page)}: JSON-LD block {i} is invalid — {exc}")
                continue

            for node in data.get("@graph", [data]):
                if not isinstance(node, dict):
                    continue
                node_id = node.get("@id")
                # A bare {"@id": ...} is a pointer, not a definition, and may
                # legitimately repeat anywhere.
                if isinstance(node_id, str) and len(node) > 2:
                    fingerprint = json.dumps(node, sort_keys=True)
                    definitions[node_id][fingerprint].append(rel(page))

    for node_id, variants in definitions.items():
        if len(variants) > 1:
            where = "; ".join(
                f"{len(pages_)} page(s) incl. {sorted(pages_)[0]}"
                for pages_ in variants.values()
            )
            errors.append(
                f"@id {node_id} has {len(variants)} conflicting definitions — {where}"
            )


def check_stale_strings(pages: list[Path]) -> None:
    for page in pages:
        text = page.read_text(encoding="utf-8")
        for stale in site.STALE_STRINGS:
            if stale.lower() in text.lower():
                errors.append(f"{rel(page)}: contains stale string {stale!r}")


def check_sitemap() -> None:
    sitemap = SITE / "sitemap.xml"
    if not sitemap.exists():
        warnings.append("sitemap.xml not generated yet")
        return

    try:
        tree = ET.parse(sitemap)
    except ET.ParseError as exc:
        errors.append(f"sitemap.xml is not valid XML — {exc}")
        return

    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    for loc in tree.getroot().findall(".//sm:url/sm:loc", ns):
        url = (loc.text or "").strip()
        if not url.startswith(site.DOMAIN):
            errors.append(f"sitemap.xml: {url} is not on {site.DOMAIN}")
            continue
        path = url[len(site.DOMAIN) :].strip("/")
        candidate = SITE / (f"{path}.html" if path else "index.html")
        if not candidate.exists() and not (SITE / path / "index.html").exists():
            errors.append(f"sitemap.xml lists {url} but no file backs it")


ANSWER_BLOCK = re.compile(
    r'<section class="answer" id="(?P<anchor>[^"]+)">.*?'
    r'<p class="answer__lead">(?P<lead>.*?)</p>',
    re.DOTALL,
)
TAGS = re.compile(r"<[^>]+>")


def check_answer_blocks(pages: list[Path]) -> None:
    """Enforce fan-out discipline on every answer block.

    AI Mode decomposes a query into sub-queries and retrieves passages, not
    pages. A lead answer is therefore always read out of context, so it has to
    survive being lifted: no pronoun opener, and it must name the place it is
    about. See build/data/fanout.py for the reasoning.
    """
    from components import ANAPHORA  # noqa: PLC0415

    # A passage must carry its own geography, because a sub-query result never
    # arrives with the page around it. A community name satisfies that; so does
    # the region, for site-wide passages like "how many homes have you sold"
    # that genuinely belong to no single neighborhood. What is NOT acceptable
    # is a passage with no place in it at all.
    hood_names = {h["name"].lower() for h in site.ALL_AREAS} | {
        "san diego", "north county", "southern california",
    }
    # A subtler failure than an opening pronoun, and one I shipped three times
    # before catching it: the lead answers the heading conversationally and
    # refers back to it. On the page it reads fine. Lifted into a sub-query
    # result, where the heading is gone, "that reason" refers to nothing.
    BACKREF = (
        "that reason", "this reason", "for that", "the above", "said above",
        "the question above", "that question", "this question",
        "as the heading", "the answer is no", "the answer is yes",
        "what you found", "what you searched",
    )
    # Only the *bare* reply counts. "No community facilities district in the
    # active list is named for Vista" opens with "No" as a determiner and is
    # completely self-contained; "No. In Del Sur…" is a reply to a heading that
    # will not be there. The difference is length, so both tests must hold.
    SHORT_ANSWER = {
        "both", "neither", "either", "yes", "no", "not", "depends",
        "sometimes", "correct", "sort", "kind",
    }
    anchors_seen: dict[str, list[str]] = defaultdict(list)

    for page in pages:
        html = page.read_text(encoding="utf-8")
        for match in ANSWER_BLOCK.finditer(html):
            anchor = match.group("anchor")
            lead = TAGS.sub("", match.group("lead")).strip()
            anchors_seen[rel(page)].append(anchor)

            lowered = lead.lower()
            if lowered.startswith(ANAPHORA):
                errors.append(
                    f"{rel(page)}#{anchor}: lead answer opens with an anaphor "
                    f"— useless once extracted: {lead[:70]!r}"
                )
            if not any(name in lowered for name in hood_names):
                errors.append(
                    f"{rel(page)}#{anchor}: lead answer never names the "
                    f"neighborhood, so it loses its geography when lifted: "
                    f"{lead[:70]!r}"
                )
            if (hit := next((b for b in BACKREF if b in lowered[:160]), None)):
                errors.append(
                    f"{rel(page)}#{anchor}: lead answer points back at its own "
                    f"heading ({hit!r}) — the heading does not travel with the "
                    f"passage, so the reference dangles: {lead[:70]!r}"
                )
            # "Both, depending on the parcel." answers the heading and says
            # nothing on its own. Any opening clause this short is answering a
            # question the reader of the extracted passage cannot see.
            opener = re.split(r"[.,;:]", lowered, 1)[0].strip()
            words = opener.split()
            if words and len(words) <= 3 and words[0].strip("&") in SHORT_ANSWER:
                errors.append(
                    f"{rel(page)}#{anchor}: lead answer opens with a bare "
                    f"reply to its own heading ({opener!r}) — meaningless once "
                    f"the heading is gone: {lead[:70]!r}"
                )

        for page_name, anchors in anchors_seen.items():
            duplicates = {a for a in anchors if anchors.count(a) > 1}
            for dupe in duplicates:
                errors.append(f"{page_name}: duplicate anchor id #{dupe}")
        anchors_seen.clear()


def check_lead_forms(pages: list[Path]) -> None:
    """A form that does not deliver is worse than no form.

    Every lead form must post somewhere real, carry TCPA consent, and — on the
    valuation form — capture the address, which is the entire point of it.
    Shipping any of these broken loses listings silently, which is the failure
    mode nobody notices until a quarter has gone by.
    """
    if "PLACEHOLDER" in site.LEAD_ENDPOINT:
        blockers.append(
            "site.LEAD_ENDPOINT is still a placeholder — every lead form on "
            "the site posts into nothing. Set the real Formspree ID (or the "
            "client's CRM webhook) before launch."
        )

    for page in pages:
        html = page.read_text(encoding="utf-8")
        if "data-lead-form" not in html:
            continue
        if 'name="consent"' not in html:
            errors.append(f"{rel(page)}: lead form has no TCPA consent field")
        if "formspree.io" not in html and site.LEAD_ENDPOINT not in html:
            errors.append(f"{rel(page)}: lead form has no delivery endpoint")
        if 'data-lead-kind="valuation"' in html and 'name="address"' not in html:
            errors.append(
                f"{rel(page)}: valuation form does not capture an address"
            )


def check_unverified() -> None:
    if not site.GEO["verified"]:
        warnings.append(
            "GEO coordinates are approximate — re-pin against the GBP "
            "location before launch (schema and GBP must agree exactly)."
        )
    if not site.NAME_CONFIRMED_BY_CLIENT:
        warnings.append(
            f"Canonical name {site.NAME!r} is still awaiting client confirmation."
        )
    for url, reason in site.SAME_AS_PENDING:
        warnings.append(f"sameAs withheld — {url}: {reason}")

    # The "review me on Zillow" CTA only renders where a real profile URL
    # exists, so a missing one is a silently absent call to action rather
    # than a broken page. Surfaced on every build so it does not stay
    # forgotten, and the URL shape is checked so a typo cannot ship a link
    # pointing at a stranger's profile under an agent's name.
    from data import agents as _agents  # noqa: PLC0415

    for person in _agents.ROSTER:
        url = person.get("zillow")
        if url and not url.startswith("https://www.zillow.com/profile/"):
            errors.append(
                f"{person['name']}'s zillow URL is not a Zillow profile URL: "
                f"{url!r}"
            )
    if _agents.ZILLOW_PENDING:
        warnings.append(
            f"{len(_agents.ZILLOW_PENDING)} of {len(_agents.ROSTER)} agents "
            "have no Zillow profile URL, so their pages carry no 'review me' "
            "call to action. Each agent can copy their own profile URL from "
            "the address bar — they cannot be guessed or looked up."
        )


def check_internal_links(pages: list[Path]) -> None:
    """Every internal href must resolve to a file that exists.

    Added after the footer shipped seven dead links on all 43 pages — /sell,
    /buy, /concierge, /testimonials, /blog, /contact, /terms-and-conditions —
    for as long as the footer has existed. Nobody noticed because a footer is
    the part of a page you stop reading.

    Resolution mirrors Vercel's `cleanUrls`: /foo matches foo.html.
    """
    existing = {
        p.relative_to(SITE).as_posix() for p in SITE.rglob("*") if p.is_file()
    }

    def resolves(href: str) -> bool:
        target = href.split("#")[0].split("?")[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "tel:")):
            return True
        target = target.lstrip("/")
        if not target:
            return "index.html" in existing
        return (
            target in existing
            or f"{target}.html" in existing
            or f"{target}/index.html" in existing
        )

    broken: dict[str, set[str]] = defaultdict(set)
    for page in pages:
        html = re.sub(r"(?s)<script.*?</script>", "", page.read_text(encoding="utf-8"))
        for match in re.finditer(r'href="([^"]+)"', html):
            if not resolves(match.group(1)):
                broken[match.group(1)].add(rel(page))

    for href, on_pages in sorted(broken.items(), key=lambda kv: -len(kv[1])):
        errors.append(
            f"dead internal link {href!r} on {len(on_pages)} page(s) "
            f"(e.g. {sorted(on_pages)[0]}) — nothing resolves there."
        )


def check_faq_matches_visible(pages: list[Path]) -> None:
    """Every FAQPage answer must appear in the page's visible text.

    Google requires FAQ structured data to match content visible on the
    page, and the honest reason to care is simpler than the policy: markup
    that says something the page does not say is a claim nobody can check.

    This used to fail. Three FAQ lists were hand-written alongside the
    passages they described and had drifted into paraphrase — the guides'
    Mello-Roos answer used the note from taxes.py while the page displayed a
    different lead sentence. They are derived from the rendered blocks now,
    which makes a mismatch impossible by construction; this check is what
    catches anyone reintroducing a hand-written one.
    """
    import html as html_mod  # noqa: PLC0415

    for page in pages:
        raw = page.read_text(encoding="utf-8")
        stripped = re.sub(r"(?s)<script.*?</script>", "", raw)
        visible = re.sub(
            r"\s+", " ", html_mod.unescape(TAGS.sub(" ", stripped))
        )

        for block in LD_BLOCK.findall(raw):
            try:
                data = json.loads(block)
            except json.JSONDecodeError:
                continue  # check_jsonld already reported this
            for node in data.get("@graph", [data]):
                if not isinstance(node, dict) or node.get("@type") != "FAQPage":
                    continue
                for entry in node.get("mainEntity", []):
                    answer = entry.get("acceptedAnswer", {}).get("text", "")
                    probe = re.sub(r"\s+", " ", answer)[:70]
                    if probe and probe not in visible:
                        errors.append(
                            f"{rel(page)}: FAQ answer is not in the visible "
                            f"text — {probe[:60]!r}"
                        )


def check_headings(pages: list[Path]) -> None:
    """Exactly one h1 per page, and no skipped heading level.

    Screen reader users navigate by heading, and a jump from h1 straight to
    h3 tells them a level exists that they cannot find. Seventeen pages did
    exactly that — every neighborhood guide plus /mello-roos — because
    `answer_block` defaults to h3 and those blocks are the page's top-level
    sections, so there was no h2 anywhere between the title and them.

    Cheap to check, invisible to catch by eye, and it silently regresses the
    moment someone adds a section without thinking about level.
    """
    heading = re.compile(r"<h([1-6])[ >]")
    for page in pages:
        html = re.sub(
            r"(?s)<(script|style).*?</\1>", "", page.read_text(encoding="utf-8")
        )
        levels = [int(m) for m in heading.findall(html)]

        h1s = levels.count(1)
        if h1s != 1:
            errors.append(
                f"{rel(page)}: {h1s} <h1> elements — a page needs exactly one."
            )

        previous = 0
        for level in levels:
            if previous and level > previous + 1:
                errors.append(
                    f"{rel(page)}: heading level jumps h{previous} to h{level} "
                    f"— skipped level breaks heading navigation."
                )
                break
            previous = level


def check_testimonials() -> None:
    """Testimonials must be attributable, and must never be marked up.

    Two failure modes this guards against. First, an entry with no source
    URL is unverifiable, which on a site whose entire pitch is "check us"
    is worse than no testimonial. Second, someone later adding Review or
    aggregateRating schema to them — Google prohibits aggregating reviews
    from other sites, and a business marking up reviews of itself is
    ineligible for the star feature regardless, so the markup would be a
    policy violation bought for nothing.
    """
    from data import agents, testimonials  # noqa: PLC0415

    roster = {a["slug"] for a in agents.ROSTER}
    areas = {a["slug"] for a in site.ALL_AREAS}

    for i, entry in enumerate(testimonials.ENTRIES):
        label = entry.get("name") or f"entry {i}"
        for field in ("quote", "name", "source_url"):
            if not entry.get(field):
                errors.append(
                    f"testimonial {label!r} has no {field} — an unattributable "
                    "testimonial cannot ship on this site."
                )
        if entry.get("agent") and entry["agent"] not in roster:
            errors.append(
                f"testimonial {label!r} names agent {entry['agent']!r}, who is "
                "not on the roster."
            )
        if entry.get("hood") and entry["hood"] not in areas:
            errors.append(
                f"testimonial {label!r} names area {entry['hood']!r}, which is "
                "not a community we cover."
            )

    page = SITE / "testimonials.html"
    if page.exists():
        html = page.read_text(encoding="utf-8")
        if '"Review"' in html or "aggregateRating" in html:
            errors.append(
                "testimonials.html carries Review or aggregateRating schema. "
                "Google prohibits aggregating reviews from other sites and "
                "makes self-controlled reviews ineligible for the star "
                "feature — remove it."
            )


def check_footer_licensees() -> None:
    """The DRE line in the footer is a legal display, not decoration.

    It renders on all 43 pages, so a wrong or missing number is wrong 43
    times. These are hard errors rather than warnings: publishing a licence
    number that does not belong to the named person is worse than publishing
    no footer at all.
    """
    from data import agents  # noqa: PLC0415

    roster = {a["slug"] for a in agents.ROSTER}
    for slug in site.FOOTER_LICENSEES:
        if slug not in roster:
            errors.append(
                f"site.FOOTER_LICENSEES names {slug!r}, who is not on the "
                "roster — the footer would render a broken /agent link and a "
                "licence number for nobody."
            )
            continue
        person = agents.by_slug(slug)
        if not person.get("dre"):
            errors.append(
                f"Footer licensee {person['name']} has no DRE number on the "
                "roster. California requires it wherever the licensee is "
                "named in advertising."
            )


def main() -> int:
    if not SITE.exists():
        print("site/ does not exist yet")
        return 1

    pages = sorted(SITE.rglob("*.html"))
    check_jsonld(pages)
    check_answer_blocks(pages)
    check_lead_forms(pages)
    check_stale_strings(pages)
    check_internal_links(pages)
    check_sitemap()
    check_unverified()
    check_faq_matches_visible(pages)
    check_headings(pages)
    check_testimonials()
    check_footer_licensees()

    for warning in warnings:
        print(f"  warn   {warning}")
    for blocker in blockers:
        print(f"  {'BLOCK ' if PRELAUNCH else 'FAIL  '} {blocker}")
    for error in errors:
        print(f"  FAIL   {error}")

    failed = errors if PRELAUNCH else errors + blockers
    print(
        f"\n{len(pages)} page(s) checked · {len(failed)} error(s) · "
        f"{len(blockers)} launch blocker(s) · {len(warnings)} warning(s)"
    )
    if PRELAUNCH and blockers:
        print("running --prelaunch: launch blockers shown but not failing")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
