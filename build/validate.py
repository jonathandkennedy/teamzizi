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

    hood_names = {h["name"].lower() for h in site.NEIGHBORHOODS}
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


def main() -> int:
    if not SITE.exists():
        print("site/ does not exist yet")
        return 1

    pages = sorted(SITE.rglob("*.html"))
    check_jsonld(pages)
    check_answer_blocks(pages)
    check_lead_forms(pages)
    check_stale_strings(pages)
    check_sitemap()
    check_unverified()

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
