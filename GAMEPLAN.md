# Team Azizi — Website Rebuild + AI Citation Game Plan

**Client:** Team Azizi (Compass) · San Diego, CA · CitedRealty customer #1
**Prepared:** 2026-07-24 · Research basis: 9-agent workflow (archived site, Compass, entity footprint, AI baseline, competitors, keywords) — full findings in [research/](research/)
**Working brief:** `retainer-reach/briefs/team-azizi/san-diego/location.brief.md` · **Decisions & state:** [HANDOFF.md](HANDOFF.md)

---

## 0. TL;DR

Team Azizi is a RealTrends-verified top team (**$105.59M volume / 92 sides in 2025, #1 in Del Mar by sides, 1,016 closed sales on Compass**) that is currently **invisible to AI in all 14 tested queries across their own six neighborhoods** — including "best agent in Carmel Valley," where their office sits. Their old Luxury Presence site is dead (DNS down), Google's index of it is decaying, they have **no Google Business Profile**, and AI already repeats corrupted third-party data about them (an old address, "45 Ranch" typo). Meanwhile the competitive research shows the citation bar in this market is **low**: solo agents with basic blogs are getting cited, Del Sur has literally **no market content anywhere**, and 4S Ranch's top answers are 20-year-old forum threads.

The plan: rebuild teamazizi.com fast on an owned static stack (same URLs, same brand, modernized), make the six neighborhood pages the deepest fact pages in the corridor (Mello-Roos, school boundaries, real MLS stats — the things **no competitor** publishes), ship a complete schema/entity graph, stand up GBP + directory presence + review velocity, and run the market-report/Q&A content engine that is already proven to earn AI citations in this exact market. Everything is measured: AI-visibility baseline is captured (it's zero), geogrid + SAIV tracking after launch. This is CitedRealty's case study #1 — document before/after from day one.

---

## 1. Client Snapshot (verified facts)

| Fact | Value | Source |
|---|---|---|
| Team | Team Azizi, Compass (Compass California III, Inc., DRE# 01527365) | Compass |
| Lead | Nilab Azizi, DRE# 02047962 | Compass |
| Founder | Sonia Azizi (DRE 01889023) — **passed away July 6, 2023**; team continues in her legacy | multiple |
| Office | 12860 El Camino Real Ste 100, San Diego CA 92130 (Carmel Valley) | Compass |
| Phone / email | (858) 847-8067 · teamazizi@compass.com | Compass |
| Production | **$105.59M / 92 sides (2025, RealTrends Verified)** · 1,016 closed sales + 43 rentals on Compass profile · active listings $369K–$5.875M · solds to $6.1M | RealTrends, Compass |
| Rankings | **#1 Del Mar team by sides, #2 by volume · #58 in CA by volume · #265 nationally** · 4 RealTrends badges | RealTrends 2025 |
| Team size | 17–18 licensed agents + ops (CFO, assistant); 33 roster entries | Compass, RealTrends |
| Six claimed neighborhoods | Carmel Valley, Del Mar, Rancho Santa Fe, Del Sur, 4S Ranch, Scripps Ranch | old site |
| Special asset | 7 active units at 6710 La Jolla Blvd — whole-building development representation | Compass |
| Old platform | Luxury Presence (2022 build) — site now down; **the "rented site" cautionary tale in the flesh** | archive |

Update the old site's stat tiles ("$90M+ 2024") to the stronger, third-party-verifiable 2025 RealTrends numbers, with links. AI loves verifiable specifics.

---

## 2. The Emergency Layer (why speed matters)

1. **Index decay.** Google still indexes ~10 teamazizi.com URLs with dead DNS. Every week down increases the chance those rankings are lost for good and the brand answer gets rewritten by junk directories.
2. **AI is already wrong about them.** The AI-synthesized branded answer serves the **old 10550 Craftsman Way address** (via cityof.com) and calls their service area "**45 Ranch**" (a directory typo). Their entity is being defined by third parties.
3. **No GBP.** The single largest gap. Gemini's primary data source is GBP; AI Overviews pull heavily from it. Without it they cannot appear in the map pack, near-me results, or most Google AI local answers.
4. **Review equity is stranded** on deceased founder Sonia's profiles (Yelp, Zillow, HomeLight, realtor.com, homes.com — several with the old address/phone/brokerage "Upstart Residential"). Nothing accrues to "Team Azizi" or Nilab.
5. **Entity collision:** Azizi Developments (Dubai) dominates generic "Azizi real estate" surfaces. Canonical naming + schema disambiguation is required.
6. **Leaking staging site:** greatersandiegouses.com / greatersandiegohouses.com serves an "About Team Azizi" page with a broken `*.testintegration.com` SSL cert — indexed. Find owner, fix or noindex.

**Implication: Phase 1 site launch is the urgent deliverable — every entity/citation fix downstream needs a live canonical home to point at.**

---

## 3. Strategy — One Story, Two Engines

**The story:** *the North San Diego corridor experts.* Research finding: every competitor owns a slice (Felicia Lewis/Sezer → Carmel Valley, Barry/Jackson Arnett → RSF prestige, Kolker/Grannis → Del Sur/4S, Whissel → countywide volume) but **nobody owns the coastal-luxury-to-inland-family corridor as one story**. Team Azizi's actual sales footprint spans it, with RealTrends proof at the Del Mar end.

**Engine 1 — Rank (classic local SEO):** GBP + reviews + citations + neighborhood pages + geogrid measurement. Primary tracking keyword: **"carmel valley san diego real estate agent"** (office proximity, winnable, decisive intent).

**Engine 2 — Cited (GEO):** fact-dense neighborhood pages, year-stamped market reports, direct-answer FAQs, schema graph, multi-platform entity breadth — the exact formats the AI baseline proved get cited in this market. Priority order comes from the opportunity map (§7).

Per the skills' honesty layer: traditional fundamentals feed AI visibility; entity work is slow-compounding; we report evidence tiers and never buy mentions (Google's May 2026 AI-search guide makes bought citations a stated spam risk).

---

## 4. Website Rebuild Spec

### 4.1 Stack & ownership
- **Static HTML/CSS/JS, no framework** — the CitedRealty house style: fastest possible Core Web Vitals, schema server-rendered in the HTML (AI fetchers don't run JS), trivially portable. **The client owns everything** — the pitch writes itself: their last site vanished when the Luxury Presence relationship ended.
- Python generators (à la citedrealty.com) for repeating page types: neighborhood pages, agent pages, blog posts. Hand-authored homepage.
- Host: Vercel (auto-deploy from repo). Forms: Formspree (or client CRM webhook — ask). All forms carry TCPA consent language like the old site.

### 4.2 URL preservation (SEO non-negotiable)
Rebuild at the **same paths**; 301 anything not rebuilt. From the old sitemaps (~140 URLs):

| Old path | Plan |
|---|---|
| `/`, `/team`, `/contact`, `/blog`, `/neighborhoods`, `/neighborhoods/{6 slugs}` | Rebuild, same URLs |
| `/agent/{15 slugs}` | Rebuild (roster refresh with client — Compass shows 18 public incl. new members) |
| `/blog/{4 slugs}` | Rebuild — bodies were never archived; rewrite better under identical slugs (titles known: Compass Concierge Del Mar, ADUs Scripps Ranch, Closing costs Del Sur, Mello-Roos vs HOA 4S Ranch — all perfectly on-strategy) |
| `/buyers-guide`, `/sellers-guide`, `/concierge`, `/home-valuation`, `/testimonials`, `/renovation-case-studies` | Rebuild (content lost — write new) |
| `/properties/sale`, `/properties/sold`, `/properties/{addr-mls}` (~100) | Rebuild indexes; property pages 301 → `/properties/sold` (or per-neighborhood sold sections) unless IDX vendor recreates them |
| `/home-search/*` (LP-proprietary IDX) | 301 → new IDX search page |
| `/terms-and-conditions` | New privacy/terms (old was LP boilerplate; fix the URL/title mismatch) |
| `/404` in sitemap, robots 500 | Hygiene fixes; new split sitemaps kept |

### 4.3 Design — "same brand, better bones"
Keep (it IS the brand): black/white high-contrast system · **Reem Kufi Fun** headings + **Lato** body/uppercase-tracked UI · square 2px ghost buttons that invert on hover · gold micro-accents `#8D7120` / `#CCB091` · full-bleed video hero with 30% overlay + "Who Represents You Matters" · transparent→white sticky nav with logo swap · alternating white/black section rhythm · family-team photography.

Modernize: fluid type (`clamp()` from the 70/43/30px scale) · CSS grid instead of slick-carousel · lightweight scroll-reveal, `prefers-reduced-motion` respected · real `<video>` with posters (the three Cloudinary stock videos are still live; consider replacing with **actual drone footage of their neighborhoods** — instant differentiation from every LP template site) · LCP/CLS budget enforced · light/dark handled deliberately (old site was light-only; keep light-first).

All archived assets (logos, 15 headshots, 6 neighborhood images, section backgrounds, hero videos) are mapped with recovery URLs in [research/design.md](research/design.md). Recover now; request originals from client for quality.

### 4.4 Sitemap (new information architecture)
```
/                              Homepage (hand-authored)
/neighborhoods/                PILLAR HUB — "North San Diego Neighborhood Guide" (2,500–4,000 words)
/neighborhoods/carmel-valley/          ┐
/neighborhoods/del-mar/                │  6 flagship pages (hand-crafted)
/neighborhoods/rancho-santa-fe/        │  + /homes-for-sale/ IDX sub-pages (Phase 3)
/neighborhoods/del-sur/                │
/neighborhoods/4s-ranch/               │
/neighborhoods/scripps-ranch/          ┘
/neighborhoods/pacific-highlands-ranch/   Phase 3 — proven demand, CV spillover
/sell/                         Seller hub: valuation tool + process ("Equity Assessment" framing)
/buy/                          Buyer hub (absorbs /buyers-guide)
/concierge/                    Compass Concierge (branded-procedure keyword — high intent, low competition)
/team/  + /agent/{slug}/       Roster + agent pages (each agent tagged to neighborhoods they farm)
/testimonials/                 Outcome-stat testimonials
/properties/sale|sold          Listings indexes (IDX-fed)
/market-report/{neighborhood}/ Monthly/quarterly report series (the proven AI-citation vehicle)
/blog/ + posts                 Content engine (4 legacy slugs preserved)
/about/  (+ Sonia legacy section — see §9 open questions)
/contact/
```
Hub-and-spoke internal linking: every neighborhood page ↔ hub, spoke-to-spoke "nearby neighborhoods," service pages ↔ neighborhood pages, breadcrumbs + BreadcrumbList everywhere, everything ≤3 clicks, zero orphans.

### 4.5 The neighborhood page template (the product)
Merges CitedRealty's published 7-block template, the skills' 8-section spec, and the competitor-gap findings. Per page (800–1,500 words hand-crafted, unique substance — May 2026 core update demotes name-swap templates):

1. **H1 + quotable market snapshot** — "[Neighborhood] Real Estate Guide — [Month Year]": median sale, DOM, inventory trend, one plain-language takeaway. *The block an AI lifts.* Refresh quarterly (refresh = GBP post + social content).
2. **Housing stock & character** — eras, builders (Pardee/Shea tracts), price bands, micro-areas. Specifics portals can't template.
3. **Buying here** — competition level, inspection gotchas for this stock, what moves vs. sits.
4. **Selling here** — prep that pays, realistic timelines, pricing vs. adjacent areas.
5. **The data no competitor publishes** *(the moat — verified gaps: not one competitor page has these)*:
   - **Mello-Roos / HOA / effective tax rate** per sub-community (THE #1 forum question for 92127; Scripps' "mostly no Mello-Roos" is its differentiator)
   - **School boundary specificity** (which CV homes feed Torrey Pines HS / DMUSD vs SDUSD; Scripps = San Diego Unified NOT Poway — common misconception; 4S/Del Sur = Poway Unified)
   - Commute reality (Sorrento Valley biotech, UTC, downtown drive times)
6. **Track record in THIS neighborhood** — "Recently sold by Team Azizi in [X]" with real solds (they have 1,016 to draw from), outcome stats ("sold in N days at X% of list"), review excerpts from that neighborhood.
7. **FAQ (5–8 real questions)** from the question bank in [research/keywords.md](research/keywords.md) — H3 question + 2–3 sentence direct answer + FAQPage schema (AI parsing; rich results are gone and we say so honestly).
8. **One CTA** — valuation (sellers) or consult (buyers), intent-dropdown form.

Byline: the actual agent who farms that neighborhood + visible updated date. Every page passes the 4-question doorway check before publish. A semantic content brief (per the briefs skill: core concept, 10–15 related concepts, required entities, depth tiers, 8–10 mapped questions) is produced per page **before** writing — this is what makes the system repeatable for CitedRealty customer #2.

**Per-neighborhood angle (from AI baseline):**

| Neighborhood | Situation | Play |
|---|---|---|
| Carmel Valley | Home turf; crowded (Felicia Lewis, carmelvalley.com) | Flagship depth + GBP proximity + primary geogrid keyword |
| Del Mar | **#1 by sides — provable**; entrenched luxury SERP | Lead with RealTrends proof; market-report series; don't chase "best agent" head term yet |
| Rancho Santa Fe | Hardest (Barry, Brizolis Janzen, Cabral) | Covenant/ARB/septic explainer content; long game |
| **Del Sur** | **Vacant lane — no market content exists anywhere** | Monthly market report + full guide; fastest possible AI win |
| **4S Ranch** | Incumbents are 2000s forum threads | Year-stamped pros/cons + Mello-Roos math; second-fastest win |
| Scripps Ranch | AI answer held by two ~$300 press releases | Full guide + reviews + (legit) RealTrends announcement PR |

### 4.6 Schema graph (server-rendered, day one)
- **`RealEstateAgent`** main entity, `@id: https://teamazizi.com/#business`: exact-match GBP NAP, `+1` phone, `geo`, `areaServed` array — one `City`/`Place` entry per neighborhood **with Wikipedia sameAs where pages exist** (Carmel Valley, Del Mar, Rancho Santa Fe, 4S Ranch, Scripps Ranch have Wikipedia articles), `hasOfferCatalog` (Buyer Representation, Listing Representation, Home Valuation, Compass Concierge, Relocation, Investment/Development, Leasing — each with a description), complete `sameAs` (Compass, RealTrends profile, Zillow, Facebook, Instagram, LinkedIn, YouTube, Yelp).
- Agent pages: unique `@id` per agent, linked from an `Organization` `department`/`member` pattern (Person markup = flagged extension beyond the skills' prescription).
- Neighborhood pages: `Service` schema with `areaServed` per page (service-area pattern — no fake per-neighborhood addresses).
- `FAQPage` on neighborhoods/guides, `BlogPosting` + `BreadcrumbList` sitewide, `Article` on market reports.
- **Validate every JSON-LD block with `json.loads` pre-push** (the CitedRealty missing-brace lesson) + Rich Results Test; watch GSC structured-data errors 2 weeks post-launch.

### 4.7 Conversion system (competitor-proven patterns)
- **Two poles on every page:** seller pole = "What's your [Neighborhood] home worth?" (consider Felicia-style luxury framing: *Equity Assessment*) · buyer pole = gated neighborhood guide/market report PDF.
- **Intent dropdown** on all forms (Buying / Selling / Both / Relocating / Investing / Renting) — pre-qualified leads, per Whissel's best-in-class pattern.
- **Outcome-stat testimonials** ("8 offers in 3 days, over asking") — mine their 7 archived testimonials + new ones; numbers not adjectives.
- Sticky click-to-call, footer form on every page (LP default that works — keep).
- **Branded program**: a Team Azizi listing-prep/concierge name riding Compass Concierge (cf. "Show Perfect™") — cheap, ownable differentiation. Draft options for client.
- **Maintenance as advantage:** Whissel shows $0 medians and lorem ipsum; Felicia's school table is empty. Our quarterly refresh discipline is itself a conversion and trust win.
- IDX: **skipped at launch** (§9 decision). Neighborhood pages show market stats + Team Azizi's own actives/solds, not MLS search widgets. Don't rebuild a mini-Zillow — the page's job is the expert, not the inventory.

---

## 5. Entity & Citation Repair (runs parallel to build)

1. **Canonical identity decision (client, week 1):** exactly one string — recommend **"Team Azizi"** (matching Compass/RealTrends) with "Team Azizi Real Estate | Compass San Diego" as the descriptive long form for disambiguation vs. Azizi Developments. One address (12860 El Camino Real Ste 100), one phone ((858) 847-8067), everywhere.
2. **NAP cleanup list** (full detail in [research/social.md](research/social.md)): cityof.com (drives the wrong-address AI answer — fix first) · housing.info (dead site link) · Yelp listing (Sonia's name, old address/phone — see legacy decision §9) · homes.com ("Upstart Residential") · LinkedIn company page ("Team Azizi Upstart Real Estate", 40 followers — rename) · ChamberOfCommerce.com · Experience.com (claim; old phone) · RealEstateAgents.com (wrong DRE) · RocketReach dead email.
3. **Directory enrollment** (the frames AI draws "best realtor" names from): FastExpert, HomeLight, U.S. News agents, Agent Pronto, proper team Yelp, realtor.com/homes.com team profiles, Zillow **team** profile consolidation.
4. **Aggregators:** Data Axle, Neustar/Localeze, Foursquare, Yelp — one accurate submission cascades downstream.
5. **Bing Places** (ChatGPT reads Bing's index) + **Apple Business Connect** (Siri/Apple Maps).
6. **Knowledge panel:** claim once brand search surfaces it; track branded query volume in GSC as the entity KPI.
7. **Earned mentions only:** RealTrends result announcements, community sponsorships, local news — legitimate PR is fine (a placed release with *real verifiable rankings* contests the Scripps Ranch press-release answer); **no bought "AI mention" placements** (Google May 2026 spam guidance — also CitedRealty's compliance line).
8. Fix/noindex the leaking `greatersandiegohouses.com` staging site.

---

## 6. Google Business Profile (needs client verification)

- Create GBP: "Team Azizi" at the Compass office (storefront w/ suite, or hybrid SAB — decide during setup; verify no duplicate/individual-agent listings to consolidate).
- Primary category: **Real Estate Agency** (verify against map-pack competitors' categories); secondaries: Real Estate Consultant, Real Estate Agents, Property Management (only if leasing line is real — they have 43 closed rentals).
- Full services menu mirroring `hasOfferCatalog`; 750-char description from the concept map; real hours (not the directory's fake "24/7"); 10–15 photos at launch, 2–3/month after; UTM'd website link.
- **Cadence:** 1–2 posts/week (recycled from neighborhood page refreshes, just-solds, market reports); respond to every review; review AI-suggested Q&A answers before they publish (2026 AI-Q&A rollout).
- **Review velocity engine:** steady 5–10/month across **Google + Zillow + Yelp** beats a stale pile; ask clients to name neighborhood + service + outcome. All new equity accrues to the team listing + Nilab.

---

## 7. Content Engine (the citation flywheel)

Priority from the opportunity map (most-winnable first — [research/aiBaseline.md](research/aiBaseline.md)):

1. **Branded-answer repair** — site relaunch + §5 cleanup (urgent, zero competition).
2. **Del Sur Market Report** (monthly) + "Living in Del Sur (2026)" — vacant lane, AI currently admits it has no data.
3. **"Living in 4S Ranch: Pros & Cons (2026)"** + Mello-Roos math — beats 20-year-old City-Data threads.
4. **Market-report series for all six** (Del Sur, 4S → Scripps → CV → Del Mar → RSF) — solo agents' monthly reports already get cited for CV; the team has 92 sides/yr of first-party data to write better ones.
5. **"Top Real Estate Agents in [Neighborhood] (2026)"** honest listicles — the established play competitors use to feed AI answers; include competitors fairly (CitedRealty honesty doctrine — it's also *why* this content earns citations).
6. **Scripps Ranch contest** — guide + reviews + legitimate RealTrends PR vs. the paid-PR incumbent.
7. **Comparison posts:** Del Sur vs 4S Ranch (proven demand), Carmel Valley vs Del Mar, Del Mar vs Encinitas vs Solana Beach, Scripps vs Poway vs RB.
8. **Evergreen money guides:** "Mello-Roos in 92127: the real math" · "Which Carmel Valley homes feed Torrey Pines HS" (the DMUSD boundary-confusion explainer) · "RSF Covenant, Art Jury & septic explained" · ADU/renovation content (they already blogged ADUs + have a renovation-case-studies page precedent).

Anatomy per post: question-first title, **TL;DR block**, H2s, FAQ + schema, byline + dated, year-stamped where it fits, internal links to neighborhood/service pages. Cadence: 2–4/month. Every piece repurposes into GBP posts + Instagram (their IG is active — listings, market education, milestones) + email newsletter.

---

## 8. Measurement & the Case Study

**Baseline (captured today, pre-launch):** 14 AI/SERP queries — Team Azizi absent from all; corrupted brand answer documented; competitor mention grid recorded. This is the "before."

Ongoing:
- **Monthly AI visibility report:** manual query panel (ChatGPT / Gemini / Perplexity / AI Overviews) per neighborhood — mentioned yes/no, sentiment, cited sources, competitor grid; Local Falcon GAIO/AI Mode scans (SAIV) when budget allows.
- **Geogrid** (7×7, centered 92130): primary "carmel valley san diego real estate agent" + "realtor near me" proxy + 2–3 revenue keywords; scan 2–4 weeks after each page ships.
- **GSC:** branded-query volume (entity KPI), neighborhood page queries/impressions; **report GBP actions (calls, directions, site clicks) + conversions, not raw clicks** (zero-click era; ~58% click reduction on AI-affected queries — Tier C, labeled honestly).
- **Formspree/CRM lead log** tagged by page + intent dropdown.
- Evidence tiers on every claim in client reports (evidence-standards discipline).
- **Case study doc from day one** — screenshots of the corrupted AI answers, absent-everywhere baseline, then the recovery. This is CitedRealty's "proof gap" closer (per HANDOFF.md §11).

---

## 9. Open Questions for the Client (intake — none block Phase 1 build start)

1. ~~**Domain/DNS access to teamazizi.com**~~ — **RESOLVED 2026-07-24: Jon controls the domain.** Point DNS to Vercel at Phase 1 launch.
2. ~~**IDX vendor**~~ — **DECIDED 2026-07-24: launch without IDX** (fails CitedRealty's own need-test for a listing-focused team). Site shows their OWN listings (generator-maintained — no IDX license needed for own inventory) + per-neighborhood solds + market stats; buyers link out to Compass search; `/home-search/*` 301 → `/properties/sale`. Revisit only if the team commits to a buyer saved-search nurture pipeline — then noindexed, own-domain implementation.
3. **Canonical name** confirm: "Team Azizi" everywhere?
4. **Sonia legacy** (sensitive): propose an "Our Founder" section honoring her on /about; decide handling of her Yelp/Zillow/LinkedIn profiles (memorialize vs. update) with the family — never silently delete. Her podcast/YouTube ("The Sonia Azizi Show") is real entity equity; link it as legacy.
5. **GBP verification** — needs client to receive/complete verification; confirm no existing/duplicate listings we didn't find.
6. **Roster** — 15 old-site agents vs 18 public on Compass (new: Masooma CFO, Tiffney, Javier, Malcolm, Mahan, Charisma; departed?: Deanna Colby, Coby Herzog). Confirm current list for /team.
7. **Languages spoken** (Dari/Farsi/Spanish plausible — strong E-E-A-T + an untapped keyword category, but never claim unconfirmed).
8. **Founding year & lifetime volume claim** ("est. 2010" Yelp vs "2014" housing.info; RealTrends $105.59M is 2025-only).
9. **Original photography/video** — headshots, team photo, any drone footage; Wayback recovery works but originals are better.
10. **Testimonial permissions** + CRM/lead routing destination; branded program name preference (§4.7).
11. **CitedRealty scope confirm** — this plan = Local Hero tier ($3,999/mo, site build + 15 neighborhoods; 6 now, expansion room for PHR, Torrey Hills, Del Mar Mesa, Santaluz, RSF sub-communities, La Jolla — the 6710 La Jolla Blvd project justifies a La Jolla page).

---

## 10. Build Order

**Phase 0 — now:** asset recovery from Wayback; intake questions to client; brief + baseline filed. ✅ research done
**Phase 1 — Site core (target: ~2 weeks):** design system port → homepage → 6 neighborhood pages (briefs first) → /team + agent pages → /sell, /buy, /contact, /concierge → schema graph → 301 map → sitemaps/robots → launch on teamazizi.com → GSC + Bing Webmaster submission, re-index requests.
**Phase 2 — Entity (weeks 2–4, parallel):** GBP creation + verification → NAP cleanup sweep → aggregators → Bing Places + Apple Business Connect → directory enrollment → Zillow team consolidation → review engine start.
**Phase 3 — Content ramp (months 2–3):** market-report series (Del Sur/4S first) → comparison + Mello-Roos/school-boundary guides → listicles → Scripps PR → PHR page → IDX sub-pages → /testimonials + /renovation-case-studies rebuilds.
**Ongoing:** quarterly page refreshes, 2–4 posts/month, 1–2 GBP posts/week, monthly AI-visibility + geogrid reporting, case-study log.

---

*Research appendix: [site.md](research/site.md) (old-site inventory/SEO) · [design.md](research/design.md) (tokens + asset URLs) · [compass.md](research/compass.md) (production proof) · [social.md](research/social.md) (entity footprint + cleanup list) · [aiBaseline.md](research/aiBaseline.md) (14-query baseline + opportunity map) · [competitors.md](research/competitors.md) (teardowns + conversion patterns) · [keywords.md](research/keywords.md) (keyword map + question bank) · [aiPlaybook.md](research/aiPlaybook.md) + [contentPlaybook.md](research/contentPlaybook.md) (skill distillations) · [archive-snapshots/](research/archive-snapshots/) (saved HTML/CSS of the old site)*
