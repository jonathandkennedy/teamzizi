# Team Azizi — Handoff & Decision Log

**Client:** Team Azizi (Compass) · San Diego · **CitedRealty customer #1**
**Domain:** teamazizi.com (Jon controls registrar; site currently DOWN) · **Planned host:** Vercel
**Project dir:** `/Users/jonkennedy/team-azizi-website/` · **Repo:** [github.com/jonathandkennedy/teamzizi](https://github.com/jonathandkennedy/teamzizi) (public — client-facing docs are visible; note the repo name is missing the "a") · **Brief:** `retainer-reach/briefs/team-azizi/san-diego/location.brief.md`
**Strategy doc:** [GAMEPLAN.md](GAMEPLAN.md) — this file is *state + decisions + why*; GAMEPLAN is *the plan*.
**Last updated:** 2026-07-25

---

## 0. One-paragraph summary

Team Azizi is a RealTrends-verified top San Diego team ($105.59M / 92 sides in 2025, **#1 in Del Mar by sides**, 1,016 closed sales on Compass) whose Luxury Presence website is dead — DNS down, Google's index of it decaying, no Google Business Profile, and AI assistants already repeating corrupted third-party data about them. A 9-agent research pass confirmed they are **absent from all 14 tested AI/search queries**, including their own office neighborhood. The engagement is: rebuild teamazizi.com as an owned static site at the same URLs with the same brand but real editorial depth, repair the entity across the web, stand up GBP + review velocity, and run the market-report/Q&A content engine that research proved earns AI citations *in this exact market*. It doubles as CitedRealty's first documented case study — the zero-visibility "before" is already captured.

---

## 1. Status as of 2026-07-24

| | |
|---|---|
| **Research** | ✅ Complete (9-agent workflow, ~684k tokens) — `research/` |
| **Strategy** | ✅ Complete — `GAMEPLAN.md` |
| **Client brief** | ✅ Filed — `retainer-reach/briefs/team-azizi/` |
| **AI baseline** | ✅ Captured (absent from 14/14 queries) — `research/aiBaseline.md` |
| **Code / site** | 🔨 Phase 1 in progress — design system, chrome, schema pipeline, homepage + `/neighborhoods` hub shipped |
| **Repo** | ✅ [jonathandkennedy/teamzizi](https://github.com/jonathandkennedy/teamzizi) — **being made private** (2026-07-25) |
| **Brand assets** | ⚠️ Recovered, but the manifest was wrong in several places — see the corrections table in `assets/recovered/README.md` |
| **GBP** | ❌ Does not exist — Phase 2 |

**Next action:** the six neighborhood pages. Blocked only on sourcing the market data (see §9).

---

## 2. Decision log — settled, do not re-litigate

| Decision | Why |
|---|---|
| **Static HTML/CSS/JS, no framework, no build step** (Python generators for repeating page types) | CitedRealty house style. Fastest Core Web Vitals; **schema server-rendered in the HTML** because AI fetchers and `curl` don't run JS; trivially portable so the client genuinely owns it; anyone can edit it. |
| **Client owns everything** | Their last site vanished when the Luxury Presence relationship ended. That *is* the pitch — they lived the rented-SaaS failure mode. Never build them onto something they can lose. |
| **Rebuild at the same URLs; 301 the rest** | ~10 old URLs are still indexed despite dead DNS. URL preservation is the cheapest SEO win available and the window is closing. Full map in GAMEPLAN §4.2. |
| **Keep the brand, modernize the bones** | Black/white system, Reem Kufi Fun + Lato, square 2px ghost buttons, gold `#8D7120`/`#CCB091` accents, video hero — this IS the brand and returning clients should recognize it. Modernize *execution* (fluid type, CSS grid, lighter motion), not identity. |
| **NO IDX at launch** | Fails CitedRealty's own published need-test: a listing-focused team's sellers don't hire them for a search widget, and buyers use Zillow regardless. IDX would cost $50–100+/mo plus MLS fees, add another vendor whose URLs die on exit, and risk the broken-widget trust failures seen on competitor sites (Whissel's $0 medians, Kolker's "No results found"). Their **own** listings need no IDX license — generator + weekly refresh. `/home-search/*` → 301. Revisit only if the team commits to a real buyer saved-search nurture pipeline; then noindexed, on their own domain. |
| **Neighborhood pages are the product** | Verified gap: not one competitor page publishes Mello-Roos math, school-boundary specifics, or maintained market stats. That's the moat. Template = CitedRealty's published 7-block post + the skills' 8-section spec (GAMEPLAN §4.5). |
| **Hand-craft 6 pages, don't scale to 30 yet** | May 2026 core update explicitly demotes name-swapped geo templates. 5–20 pages = hand-crafted tier per the skills. Five deep pages beat thirty thin ones — and CitedRealty's own blog says so publicly. |
| **Primary tracking keyword: "carmel valley san diego real estate agent"** | Sits at their physical office (92130) so it's geogrid-trackable and proximity-favored; decisive agent-selection intent; genuinely winnable — unlike portal-locked "homes for sale" or RSF head terms owned by Barry Estates/Brizolis Janzen. |
| **Content priority: Del Sur → 4S Ranch → Scripps → CV → Del Mar → RSF** | Ordered by *winnability*, not by prestige. Del Sur has no market content anywhere (AI admits it has no data); 4S Ranch's incumbents are 2000s forum threads; RSF is the hardest SERP in the county. |
| **Earned mentions only — never bought** | Google's May 2026 AI-search guide makes buying citations/mentions to influence AI results a stated spam risk (Tier A). This is also CitedRealty's compliance line and must survive contact with the Scripps Ranch competitor who *is* using paid press releases. Legit PR announcing real RealTrends results is fine; paid "AI mention" packages are not. |
| **Honest content, evidence tiers in reporting** | The brand's citation strategy. Competitor listicles name competitors fairly; ranking claims carry their confidence tier (entity→AI = Tier D consensus, not measured; open-at-search-time = Tier B; review responses = Tier A). Don't oversell schema — "schema alone rarely moves rankings." |
| **Recommend canonical name "Team Azizi"** (long form "Team Azizi Real Estate \| Compass San Diego") | Matches Compass + RealTrends. Long form disambiguates from **Azizi Developments (Dubai)**, which pollutes generic "Azizi real estate" AI/search results. *Pending client confirm — but everything ships with one string.* |
| **Sonia legacy handled with the family, never silently** | Founder Sonia Azizi died July 6, 2023. Most review equity is stranded on her profiles. Plan: honor her on `/about`; every decision about her Yelp/Zillow/LinkedIn/podcast profiles routes through the client and family. Do not delete or quietly rewrite anything of hers. |

### Added 2026-07-25 (Phase 1 build)

| Decision | Why |
|---|---|
| **URLs carry no trailing slash** — `/neighborhoods/carmel-valley`, served from `neighborhoods/carmel-valley.html` via Vercel `cleanUrls` | That is exactly how the old site served them, and ~10 of those URLs are still indexed. GAMEPLAN §4.4 writes them with a trailing slash; that was a drafting slip. Preserving the path exactly is the whole point — a trailing-slash convention would 301 away the equity we are rebuilding to keep. |
| **No JSON-LD is ever hand-written.** Every block is a Python dict serialised with `json.dumps`; `build/validate.py` re-parses all of it pre-push | Makes the missing-brace failure that broke CitedRealty's homepage graph structurally impossible rather than merely unlikely. |
| **The full entity graph repeats on every page**, rather than being defined once and referenced | An AI fetcher may only ever see one page. Each page has to stand alone as a complete statement of the entity. (The validator flags one `@id` describing *different* things, which is the real error the schema skill warns about.) |
| **`sameAs` only lists profiles that are accurate today.** LinkedIn, Yelp and the YouTube channel are withheld in `SAME_AS_PENDING` with reasons | A `sameAs` pointing at a profile carrying "Upstart Real Estate" or the old (619) number tells the knowledge graph that the wrong data is authoritative. They move up as Phase 2 fixes them. |
| **Fonts self-hosted** (Reem Kufi Fun 400, Lato 400/700 — both SIL OFL, 84 KB total) | Removes a render-blocking third-party request and a dependency the client cannot control, which is the premise of the whole rebuild. |
| **Reem Kufi Fun's colour layer remapped to the brand gold `#8D7120`** | The typeface is a COLRv1 colour font — the tittles on i/j are small **red hearts**, which is the "Fun" in the name and which the old site shipped unremarked. Red appears nowhere else in the brand and fights the gold accent. Remapping the palette keeps the letterforms and the detail while resolving the clash. One CSS block to delete if the client wants the stock red back. |
| **Neighborhood market data comes from public sources**, cited and dated: County Auditor CFD reports for Mello-Roos, district boundary maps for schools, published portal medians with named attribution | No client dependency, fully defensible under "no fabrication," and the Mello-Roos and school-boundary data *is* the moat — no competitor publishes it. Revisit if the client grants MLS access. |
| **No generated imagery on neighborhood pages** | A synthetic photo of a real named community cuts against the no-fabrication doctrine the whole strategy rests on. Generated art is fine for abstract section bands. Wrong-place recovered photos render an honest "photography pending" placeholder instead. |
| **Neighborhood pages are built as fan-out answer blocks, not narrative** | AI Mode decomposes a query into sub-queries and retrieves *passages*. A flowing page competes for one head term; the same content in self-contained blocks competes for ~19 retrievals. Map in `build/data/fanout.py`; `validate.py` rejects any lead answer that opens with a pronoun or omits the place name, because both make a passage useless once lifted. See GAMEPLAN §4.5. |
| **Localized imagery, sourced from their own listing photography first** | Original local imagery is a first-hand signal the May 2026 update rewards, and **no competitor publishes any** — a documented open gap. 1,016 closed sales means they already own true street-level photography of every one of the six communities; that beats a shoot for a first pass. Shot list and technical spec: [docs/photography-brief.md](docs/photography-brief.md). |
| **IndexNow at launch** (key `ce855552…`, `build/indexnow.py`) | ChatGPT retrieval leans on Bing's index, and IndexNow is how you tell Bing a URL changed without waiting to be crawled. Bing/Yandex/Seznam/Naver only — **Google does not participate**. Honest framing for the client: it accelerates discovery, it does not cause ranking or citation. |
| **Neighborhood-first IA: one named licensee owns each of the six areas** | A page authored by "Team Azizi" is a company talking; a page authored by a named licensee with a DRE number, a direct line and a sold record *in that neighborhood* is a person who can be checked — which is what E-E-A-T rewards and what an assistant needs before it will name someone. `/team` groups by area rather than showing one flat grid of nineteen faces, because "who do I call about Del Sur" is the question visitors arrive with. Person schema carries `areaServed` + `knowsAbout`; the neighborhood page's `WebPage.author` points at that agent. |
| **Farming assignments are client data — the system ships with confirmable slots** | Nothing published anywhere says which agent works which community. All six start unassigned in `build/data/agents.py`, and pages fall back to the team lead, who is a real, accountable, verifiable licensee — not a placeholder and not a company byline. Six one-line answers turn the whole system on. Question is pre-written in `agents.PROPOSED_ASSIGNMENTS`. |
| **robots.txt names the AI crawlers explicitly and allows them** | Retrieval bots (OAI-SearchBot, ChatGPT-User, PerplexityBot, Claude-SearchBot, Google-Extended) are what fetch a page in order to cite it — blocking any would forfeit the engagement. Training bots (GPTBot, ClaudeBot, Applebot-Extended) are also allowed: for a business whose problem is that models don't know it exists, being in the training data is upside. That one is a reversible client call. |

---

## 3. Canonical data block (reuse these exact strings everywhere)

```
Name:        Team Azizi
Long form:   Team Azizi Real Estate | Compass San Diego
Address:     12860 El Camino Real, Suite 100, San Diego, CA 92130
Phone:       (858) 847-8067        Schema: +18588478067
Email:       teamazizi@compass.com
Lead:        Nilab Azizi, CA DRE# 02047962
Brokerage:   Compass California III, Inc., CA DRE# 01527365
Website:     https://teamazizi.com
```

**These must match GBP exactly** once GBP exists — schema, footer NAP, and GBP are one entity or they're three. Old strings to purge wherever found: `10550 Craftsman Way`, `11682 El Camino Real`, `(619) 929-9691`, `sonia@teamazizi.com`, `Upstart Residential` / `Upstart Real Estate`, DRE `01426453`, and the "45 Ranch" typo.

**Proof points (all third-party verifiable — use these, not the old site's "$90M+ 2024"):**
$105.59M volume / 92 sides (RealTrends Verified 2025) · #1 Del Mar by sides, #2 by volume · #58 California by volume · #265 nationally · 1,016 closed sales + 43 rentals (Compass) · actives $369K–$5.875M · solds to $6.1M · 7 units at 6710 La Jolla Blvd = whole-building development representation.

---

## 4. What exists, where

```
team-azizi-website/
├── GAMEPLAN.md                    ← the plan (strategy, specs, build order)
├── HANDOFF.md                     ← this file
├── vercel.json                    ← cleanUrls, 301 map, cache + security headers
├── build/                         ← generators. Nothing here is deployed.
│   ├── data/site.py    THE canonical strings — NAP, proof points, services,
│   │                   sameAs, neighborhoods. Never retype these elsewhere.
│   ├── schema.py       JSON-LD builders (dicts → json.dumps, never strings)
│   ├── components.py   <head>, nav, footer, page shell
│   ├── generate.py     writes site/
│   ├── validate.py     PRE-PUSH GATE — run before every commit
│   └── fetch_fonts.py  one-shot: self-hosts the webfonts
├── site/                          ← the deployable site (output is committed)
│   ├── assets/{css,js,fonts,img}
│   └── *.html, sitemap.xml, robots.txt
└── research/
    ├── site.md          Old-site URL inventory, content, SEO observations, preservation notes
    ├── design.md        Exact design tokens + section-by-section layouts + Wayback asset URLs
    ├── compass.md       Roster, DRE numbers, production stats, active/sold listings
    ├── social.md        Full entity footprint + the 11-item NAP cleanup list
    ├── aiBaseline.md    14-query AI/SERP baseline + cited-source patterns + opportunity map
    ├── competitors.md   8 competitor profiles, neighborhood-page teardowns, conversion patterns
    ├── keywords.md      Keyword→page map, question bank by neighborhood, primary keyword
    ├── aiPlaybook.md    ai-local-search + entity-authority + local-schema distilled to this client
    ├── contentPlaybook.md  landing-pages + keyword-research + content-strategy + briefs + GBP
    └── archive-snapshots/  Saved HTML/CSS of the dead site (homepage, neighborhoods, team, CSS)

retainer-reach/briefs/team-azizi/
├── _brand.brief.md
└── san-diego/{location.brief.md, reports/, scans/, drafts/, alerts/}
```

Also relevant, outside this repo:
- **CitedRealty site + generators** (`retainer-reach/citedrealty.com/`) — the code patterns to copy: `gen_blog.py`, `gen_services.py`, `assets/`, and its `HANDOFF.md` for house conventions.
- **Neighborhood page template**, published: `citedrealty.com/blog/how-to-build-a-neighborhood-page.html`
- **IDX position**, published: `citedrealty.com/blog/what-is-idx.html`
- **Local SEO skills:** `~/.claude/skills/localseoskills/`

---

## 5. Build spec quick reference

Full detail in GAMEPLAN §4. The parts most easily got wrong:

- **Schema graph, server-rendered:** `RealEstateAgent` `@id: /#business` with `geo`, `areaServed` (one entry per neighborhood, Wikipedia `sameAs` where the article exists), `hasOfferCatalog` (services **with descriptions**), full `sameAs`. Agent pages get unique `@id`s linked via `Organization`/`department`. Neighborhood pages use `Service` + `areaServed` — **not** fake per-neighborhood business entities with addresses. `FAQPage` for AI parsing only (rich results were dropped in 2026 — say so honestly). `BreadcrumbList` everywhere.
- **Validate every JSON-LD block with `json.loads` before every push.** A single missing brace made CitedRealty's entire homepage graph unparsable and GSC flagged it within hours. Validate `sitemap.xml` as XML too.
- **Every page:** footer NAP matching GBP, author byline (the agent who farms that neighborhood), visible updated date, breadcrumbs, ≤3 clicks from home, zero orphans.
- **Per neighborhood page:** 800–1,500 words hand-written, 5–8 FAQs as H3-question + 2–3-sentence direct answer, a quotable dated market-snapshot opener, the Mello-Roos/school-boundary/commute data nobody else publishes, real solds from that neighborhood, one CTA. Write the semantic brief *before* the page.
- **Quarterly refresh discipline is a feature.** Competitors ship $0 medians, lorem ipsum, and empty school tables. Nothing on this site may rot unattended; each refresh also becomes GBP post + social content.
- **Design tokens & asset recovery URLs:** `research/design.md`. Example recovery:
  ```bash
  curl -o logo-dark.png "https://web.archive.org/web/20260104120026im_/https://media-production.lp-cdn.com/media/w4vgzllyebehwvwgoc4k"
  ```
  Recover now as insurance; request originals from the client for final quality.

---

## 6. Compliance & sensitivities (real estate ≠ generic marketing)

- **Fair Housing.** Neighborhood content must not steer. Describe *verifiable facts* — prices, days on market, tax structure, school **attendance boundaries**, commute times, amenities, HOA rules. Avoid framing that signals protected classes: "good/safe neighborhood," "family-friendly," religious or ethnic character, demographic desirability. Note the old LP pages embedded Census demographic widgets — do not reproduce that pattern as editorial. When answering "is X a good place to live," answer with facts and tradeoffs, not with who lives there.
- **MLS data use.** Aggregate stats (medians, DOM, counts) are generally fine and are what makes pages citable — but confirm SDMLS rules before displaying individual listing data; that's where IDX licensing bites.
- **California DRE.** License numbers on marketing materials — Nilab's DRE and the Compass brokerage DRE go in the sitewide footer, as on the old site. Keep the Compass equal-housing + MLS disclaimers.
- **TCPA.** Consent language on every lead form (the old site had it; don't lose it).
- **No fabrication, ever.** No invented stats, testimonials, or `aggregateRating`. Every claim traces to Compass, RealTrends, MLS, or a named source. Languages spoken stay unclaimed until the client confirms.
- **Sonia.** See §2. Sensitivity over speed on anything touching her profiles.

---

## 7. Open items

**Client-dependent (asked; don't block Phase 1 build):**
- [ ] **Which agent farms each of the six neighborhoods?** Six names. Turns on the byline, the direct contact, the `/team` grouping and the schema author on every neighborhood page. Question text ready in `build/data/agents.py:PROPOSED_ASSIGNMENTS`.
- [ ] **The other three link-in-bio URLs on Instagram.** The visible one is `teamazizi.com/home-valuation` — dead, and taking live traffic from 2,055 followers. The other three are almost certainly dead teamazizi.com paths too. This makes `/home-valuation` launch-critical, not a Phase 3 rebuild.
- [ ] **Substantiate or retire "Top 1% in SD County."** It is live in their Instagram bio today and this build refuses to print it (unverified — it is in `STALE_STRINGS`). The site and the profile cannot disagree about the same business; either they can back it or the bio changes at launch with the site.
- [ ] Headshots for the six agents without one — Masooma, Charisma, Tiffney, Javier, Malcolm, Mahan
- [ ] Deanna Colby and Coby Herzog: departed? Their `/agent/` URLs are indexed and need a deliberate 301 either way
- [ ] Confirm canonical name string
- [ ] Current roster — old site showed 15, Compass shows 18 public (new: Masooma CFO, Tiffney, Javier, Malcolm, Mahan, Charisma; verify Deanna Colby / Coby Herzog status)
- [ ] Sonia legacy decisions (memorialize vs. update her profiles) — with the family
- [ ] Languages spoken per agent (Dari/Farsi/Spanish plausible; strong E-E-A-T + untapped keyword category — never claim unconfirmed)
- [ ] Founding year + lifetime volume claim (Yelp says est. 2010, housing.info says 2014)
- [ ] Original photography/video; any drone footage of the six neighborhoods
- [ ] Testimonial permissions; CRM / lead routing destination
- [ ] Branded listing-prep program name (riding Compass Concierge)
- [ ] GBP verification — client must receive/complete it
- [ ] Scope confirm: this is Local Hero tier ($3,999/mo — site build + neighborhoods)

**Ours:**
- [x] `git init` — done; repo is live
- [ ] Vercel project — set **Root Directory = `site`**; `vercel.json` at repo root already carries `cleanUrls`, the 301 map and cache/security headers
- [ ] Make the repo private (no API for this — GitHub Settings → General → Danger Zone)
- [ ] Optimise images before launch — `site/assets/img/` is 8.3 MB unoptimised; the hero poster alone is 396 KB and is the LCP element
- [ ] Get the real **Compass brokerage logo** from Compass's brand kit (the recovered file is the TA monogram, mislabelled)
- [ ] Replace the Carmel Valley and 4S Ranch neighborhood photos — the archived ones show the wrong places
- [ ] Verify the office **geo coordinates** against the GBP pin once GBP exists (currently approximate; `validate.py` warns)
- [x] Recover all Wayback assets — done 2026-07-24; **manifest corrected 2026-07-25**, see `assets/recovered/README.md`
- [ ] Point DNS to Vercel at launch (Jon controls registrar)
- [ ] Submit to GSC + Bing Webmaster immediately at launch; request re-indexing of preserved URLs
- [ ] Run `python3 build/indexnow.py` at launch (full sitemap) and after every content deploy — will 422 until DNS points at Vercel and the key file is reachable
- [ ] Ask the client for rights to their own listing photography — it is the fastest source of true localized neighborhood imagery and they already own 1,016 sales' worth
- [ ] Lead form endpoint decision (Formspree — watch the ~50/mo free cap — vs. client CRM webhook)
- [ ] Find owner of `greatersandiegohouses.com` staging site (broken `*.testintegration.com` SSL, indexed) → fix or noindex
- [ ] Case-study log: screenshot the corrupted AI answers *now*, before they're fixed

---

## 8. How to do common tasks

- **Add/edit a neighborhood page:** write the semantic brief first (`research/contentPlaybook.md` §5 has the template), then add the data dict to the generator and run it. Never write a second page by copying the first and swapping the name — that's the exact failure mode the plan exists to avoid.
- **Refresh market snapshots (quarterly):** update the stats block per neighborhood from MLS, bump the visible updated date, then recycle each refresh into a GBP post and an Instagram post.
- **Before every push:** `json.loads` every `<script type="application/ld+json">`; validate `sitemap.xml`; Rich Results Test on any page whose schema changed.
- **After publishing pages:** point GBP's website link at the right page, then run a geogrid scan 2–4 weeks later to measure. Log results to `briefs/team-azizi/san-diego/scans/`.
- **Monthly reporting:** manual AI query panel (ChatGPT / Gemini / Perplexity / AI Overviews) per neighborhood — mentioned yes/no, sentiment, **which sources got cited**, competitor grid; plus GBP actions and conversions rather than raw clicks. File to `reports/`.
- **Resuming this project cold:** read `GAMEPLAN.md` → this file → `briefs/team-azizi/san-diego/location.brief.md` (Next Action). The `research/` files are the evidence base; don't re-run the research.
