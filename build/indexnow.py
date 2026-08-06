"""IndexNow submission.

    python3 build/indexnow.py --check     # is the domain ready? submits nothing
    python3 build/indexnow.py             # submit every URL in sitemap.xml
    python3 build/indexnow.py /sell /buy  # submit specific paths

Why this is worth doing here specifically: ChatGPT's retrieval leans on Bing's
index, and IndexNow is how you tell Bing a URL changed without waiting to be
crawled (research/aiPlaybook.md §1 — "ChatGPT pulls from Bing's index"). It is
supported by Bing, Yandex, Seznam and Naver. **Google does not participate.**

Be honest about what it does: IndexNow accelerates *discovery and crawl*. It
does not cause ranking, and it does not cause citation. It removes a delay; it
does not create demand. On a site relaunching at ~10 still-indexed URLs after
dead DNS, removing that delay is worth the twenty lines.

Run it after every deploy that changes content, and once at launch against the
full sitemap.
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from data import site  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

# Public by design: the key is proof of domain control, not a credential. It is
# verified by fetching https://teamazizi.com/<KEY>.txt, which must contain it.
# That is also why swapping it is a swap and not a rotation — there is no
# secret here to have leaked.
KEY = "a5ac16d870d4480e8de36f49e4b2270d"

# Keys that are no longer submitted under but whose files must still be served.
#
# IndexNow verifies a submission by fetching the key file at the point it
# *processes* the batch, which is not the moment the endpoint returns 200. The
# full 85-URL sitemap went in under ce8555… on 2026-08-04 and may still be in
# that queue; deleting its file now would fail verification for the one
# submission that matters most, the launch one. The protocol explicitly allows
# a host to carry several keys, so both are served and nothing is lost.
#
# Empty this list once the launch batch has visibly landed in Bing Webmaster
# Tools — a week is generous. Nothing breaks if it lingers; it is one 32-byte
# file, and this note is here so a future tidy-up knows it was deliberate
# rather than debris.
PREVIOUS_KEYS = ["ce855552330a448ca1c9fa0f83e35e5a"]
ENDPOINT = "https://api.indexnow.org/indexnow"
HOST = site.DOMAIN.replace("https://", "")


def sitemap_urls() -> list[str]:
    sitemap = SITE / "sitemap.xml"
    if not sitemap.exists():
        raise SystemExit("sitemap.xml not found — run build/generate.py first")
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.parse(sitemap).getroot()
    return [
        (loc.text or "").strip()
        for loc in root.findall(".//sm:url/sm:loc", ns)
        if (loc.text or "").strip()
    ]


def preflight() -> list[str]:
    """Check the domain is actually serving before submitting anything.

    Returns a list of problems; empty means good to go.

    This exists because as of 2026-07-25 `teamazizi.com` had no A record at
    all — the Luxury Presence site was dead and DNS still pointed nowhere.
    Firing IndexNow at a domain that does not resolve earns a 422 every time,
    and repeated failures against the same host are exactly how you get
    rate-limited by the endpoint you most need on launch day.

    So: verify the site answers, verify the key file is served with the exact
    key as its body, verify the sitemap is fetchable. Then submit.
    """
    problems: list[str] = []

    def get(url: str) -> tuple[int, str]:
        try:
            with urllib.request.urlopen(url, timeout=20) as response:
                return response.status, response.read(200).decode("utf-8", "replace")
        except urllib.error.HTTPError as exc:
            return exc.code, ""
        except Exception as exc:  # DNS failure, TLS failure, timeout
            return 0, str(exc)

    status, body = get(f"{site.DOMAIN}/")
    if status != 200:
        problems.append(
            f"{site.DOMAIN}/ returned {status or 'no response'} — the domain "
            "is not serving. Point DNS at Vercel and add the domain to the "
            "project first; nothing below can work until it does."
        )
        return problems  # everything else will fail for the same reason

    status, body = get(f"{site.DOMAIN}/{KEY}.txt")
    if status != 200:
        problems.append(f"key file {site.DOMAIN}/{KEY}.txt returned {status}")
    elif body.strip() != KEY:
        problems.append(
            f"key file body is {body.strip()!r}, expected {KEY!r} — IndexNow "
            "verifies domain control by matching these exactly."
        )

    status, _ = get(f"{site.DOMAIN}/sitemap.xml")
    if status != 200:
        problems.append(f"{site.DOMAIN}/sitemap.xml returned {status}")

    return problems


def submit(urls: list[str], *, force: bool = False) -> int:
    if not urls:
        print("nothing to submit")
        return 0

    print(f"Preflight against {site.DOMAIN} …")
    problems = preflight()
    for problem in problems:
        print(f"  BLOCK  {problem}")
    if problems and not force:
        print("\nNot submitting. Fix the above, or pass --force to try anyway.")
        return 1
    if not problems:
        print("  ok — domain serving, key file matches, sitemap reachable\n")

    payload = json.dumps(
        {
            "host": HOST,
            "key": KEY,
            "keyLocation": f"{site.DOMAIN}/{KEY}.txt",
            "urlList": urls,
        }
    ).encode("utf-8")

    request = urllib.request.Request(
        ENDPOINT,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            status = response.status
    except urllib.error.HTTPError as exc:
        # 422 is the usual one: the key file is not reachable yet, which will
        # be true until DNS points at Vercel.
        print(f"  FAIL  HTTP {exc.code} — {exc.read().decode('utf-8', 'replace')[:300]}")
        return 1

    print(f"  submitted {len(urls)} URL(s) — HTTP {status}")
    for url in urls:
        print(f"    {url}")
    return 0


def main(argv: list[str]) -> int:
    force = "--force" in argv
    check_only = "--check" in argv
    paths = [a for a in argv if not a.startswith("--")]

    if check_only:
        print(f"Preflight against {site.DOMAIN} …")
        problems = preflight()
        for problem in problems:
            print(f"  BLOCK  {problem}")
        if not problems:
            print("  ok — ready to submit")
        return 1 if problems else 0

    if paths:
        urls = [
            f"{site.DOMAIN}{p if p.startswith('/') else '/' + p}" for p in paths
        ]
    else:
        urls = sitemap_urls()
    return submit(urls, force=force)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
