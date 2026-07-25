"""IndexNow submission.

    python3 build/indexnow.py            # submit every URL in sitemap.xml
    python3 build/indexnow.py /sell /buy # submit specific paths

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
KEY = "ce855552330a448ca1c9fa0f83e35e5a"
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


def submit(urls: list[str]) -> int:
    if not urls:
        print("nothing to submit")
        return 0

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
    if argv:
        urls = [f"{site.DOMAIN}{path if path.startswith('/') else '/' + path}" for path in argv]
    else:
        urls = sitemap_urls()
    return submit(urls)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
