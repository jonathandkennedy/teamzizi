# Launch runbook — getting teamazizi.com live and indexed

**Status as of 2026-07-25: `teamazizi.com` has no DNS A record at all.** The
domain does not resolve, so nothing is served and nothing can be crawled.

```
$ getent hosts teamazizi.com
  (no A record resolved)
$ curl -sI https://teamazizi.com/
  (no response)
```

This is the single fact that governs everything below. **A sitemap cannot be
resubmitted for a domain that does not resolve** — Google and Bing fetch the
sitemap over HTTP, and there is nothing to fetch. Every indexing step is
blocked on step 2, and doing them out of order wastes the one launch-day
signal that matters.

---

## The order, and why it is this order

### 1. Set `LEAD_ENDPOINT` — before the domain goes live, not after

`build/data/site.py` still has a placeholder. **Every form on the site posts
into nothing**: the valuation flow, the contact form, and the address-capture
step that fires when someone clicks through to their Zestimate. This is the
Instagram link-in-bio destination for 2,055 followers.

Going live without it means traffic arrives, converts, and the leads are
discarded silently. Nobody notices until someone asks why the phone stopped
ringing.

Either a Formspree form ID (free tier caps around 50 submissions/month, which
this will exceed) or the team's CRM webhook. Set it, run
`python3 build/generate.py`, and `build/validate.py` will stop reporting its
one launch blocker.

### 2. Point DNS at Vercel

At the registrar for `teamazizi.com`:

| Record | Name | Value |
|---|---|---|
| `A` | `@` | `76.76.21.21` |
| `CNAME` | `www` | `cname.vercel-dns.com` |

Then Vercel → project → Settings → Domains → add `teamazizi.com` and
`www.teamazizi.com`, and set one as primary so the other 301s to it. Vercel
issues the TLS certificate automatically once DNS resolves; that usually takes
minutes, occasionally an hour.

Confirm the Vercel build settings while you are there — the site is a static
build with no framework:

| Setting | Value |
|---|---|
| Framework Preset | **Other** — not Next.js |
| Root Directory | **blank** |
| Build Command | override ON, empty |
| Output Directory | override ON, `site` |
| Install Command | override ON, empty |

Root Directory must stay blank. Vercel looks for `vercel.json` inside the Root
Directory, and ours is at the repo root — setting it to `site` silently drops
`cleanUrls`, the three 301 redirects and the security headers.

### 3. Verify the domain actually serves

```bash
python3 build/indexnow.py --check
```

This checks three things and submits nothing: the site answers 200, the
IndexNow key file is served with the exact key as its body, and the sitemap is
fetchable. It refuses to go further until all three pass, because firing
IndexNow at a domain that does not resolve earns a 422 every time — and
repeated failures against the same host are how you get rate-limited by the
endpoint you most need on launch day.

### 4. Google Search Console

Google does **not** participate in IndexNow, so this is a separate, manual job
and it is the one that matters most for ordinary search.

1. Add `teamazizi.com` as a **Domain property** (DNS TXT verification) rather
   than a URL-prefix property. A domain property covers `www`, non-`www`,
   `http` and `https` in one place, which is what you want when the old site's
   surviving URLs may be on any of them.
2. Sitemaps → submit `sitemap.xml`.
3. URL Inspection → paste the homepage → **Request Indexing**. Do the same for
   `/neighborhoods` and the two or three guides you most want found first —
   Escondido, then whichever communities the team is farming. Request Indexing
   is rate-limited to a handful per day; spend it on the pages that earn.
4. Check **Page Indexing** after a week for anything reported as excluded.

### 5. Bing Webmaster Tools

Import the Search Console property (Bing offers a one-click import). This
matters more than usual here: **ChatGPT's retrieval leans on Bing's index**, so
Bing coverage is AI-citation coverage.

### 6. Fire IndexNow

```bash
python3 build/indexnow.py
```

Submits all 42 URLs to Bing, Yandex, Seznam and Naver in one call. Re-run it
after any deploy that changes content — it is cheap and it removes crawl delay.

Be honest about what it does: IndexNow accelerates **discovery and crawl**. It
does not cause ranking and it does not cause citation. It removes a delay; it
does not create demand.

### 7. The old URLs

Roughly ten Luxury Presence URLs are still indexed despite the dead DNS. That
residual equity is the cheapest win available and it is already handled in
code — `vercel.json` carries the 301 map, and pages are served extensionless
with no trailing slash to match the old paths exactly.

Check them once live:

```bash
for u in / /neighborhoods /neighborhoods/carmel-valley /home-search/anything /profile; do
  curl -s -o /dev/null -w "%{http_code} %{redirect_url}  $u\n" "https://teamazizi.com$u"
done
```

Do not "tidy" URLs into trailing slashes later. That would 301 away the equity
this was built to keep.

---

## Google Business Profile — do this in parallel

Local pack ranking and the knowledge panel both key off GBP, and two things in
the repo are waiting on it:

- **`site.GEO` is approximate and marked `verified: False`.** Re-pin it to the
  GBP location exactly once the profile exists. Schema and GBP disagreeing is
  the precise failure this data file was built to prevent, and `validate.py`
  warns about it on every run until it is fixed.
- **NAP must match character for character** across GBP, the footer and the
  `LocalBusiness` schema — the same street, suite, city, state, ZIP and phone.
  `validate.py` already fails the build on any of the known-stale strings
  (the Craftsman Way address, the old 619 number, "Upstart Real Estate").

---

## Still outstanding, not blocking DNS

- **Privacy policy.** The footer link was removed rather than pointed at a page
  I would have had to invent. California CCPA applies to a site collecting
  names, emails, phone numbers and property addresses. This needs the client's
  lawyer, not a generator.
- **Google Maps API key** for the Street View photograph on `/home-valuation`
  (`site.GOOGLE_MAPS_KEY`). The page works without it and simply shows no
  photograph. If you add one, restrict it by HTTP referrer to `teamazizi.com`
  in the Google Cloud console — it is necessarily public in an `<img>` src, and
  an unrestricted key on a public page is someone else's free quota on your
  bill.
- **Photography for twelve of sixteen guides** — see
  `docs/photography-brief.md`. The fact plates are a good interim; a real
  photograph of the street beats them.
- `/sell`, `/buy`, `/concierge`, `/testimonials`, `/blog` — removed from the
  nav until they exist, so nothing links at a 404.
