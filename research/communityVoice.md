# ==== community_voice ====

## Team Azizi — Community Listening Pass #1 (2026-07-30)

What people in the sixteen farm areas are asking, complaining about, and reacting to right now — mined from community forums, public Q&A surfaces, and the local news cycle — plus keyword validation on the resulting topics. This file is the evidence base for the journal/news content engine; the operating system that consumes it is [docs/content-runbook.md](../docs/content-runbook.md).

**Why listening comes first:** the guides answer the durable questions (districts, CFDs, land use). The journal and news desk answer the *live* ones. The only way to know the live questions is to read where people actually ask them — Reddit, Nextdoor, City-Data, Blind — and to watch the local news that generates them. Writing to that signal is also what earns AI citations: assistants synthesize from the pages that answer the questions people phrase, in the words they phrase them in.

---

### 1. Source access — what works from where

Tested 2026-07-30 from the remote build container. This matters because the listening pass is repeatable and the tooling differs by environment.

| Source | Access | Notes |
|---|---|---|
| **Reddit** (r/sandiego etc.) | ❌ from remote containers · ✅ from a local machine | reddit.com returns 403 to datacenter egress regardless of user agent; the archive mirror (pullpush.io) is rate-limited to uselessness; search engines no longer index Reddit deeply (licensing). **Run the Reddit pass locally via the `/last30days` skill** — installed at `.claude/skills/last30days/`, keyless Reddit works from residential IPs. |
| **Nextdoor** | ⚠️ posts walled · ✅ public pages indexed | Post content requires resident accounts. But Nextdoor's *public* per-neighborhood pages ("Everything You Need to Know", city hubs, "Best places to live in Escondido 2025" rankings) are indexed and AI-readable — they are a citation surface competitors already benefit from. Post-level signal must come from **agents who live in the farm areas** reading their own feeds. |
| **City-Data forum** | ✅ fully open | Deeply indexed. The incumbent answer surface for 4S Ranch / Del Sur questions (see §3). |
| **Blind** (teamblind.com) | ✅ indexed | Tech-worker relocation threads — the exact buyer demographic for Carmel Valley / Del Sur / 4S Ranch. |
| **Local news** | ✅ fully open | The Coast News, North County Daily Star, Del Mar Times, SD Union-Tribune, Patch, Axios San Diego, Voice of San Diego. This is the news-desk feed. |
| **YouTube** | ✅ | Searchable; transcripts via the skill's yt-dlp lane (local runs). |

---

### 2. The news cycle, last 30 days (July 2026) — what a news desk would have covered

#### Market: the numbers moved

- County median dipped to **$1.02M in July 2026** from June's $1.05M peak ([SD Cash Buyer analysis](https://www.sd-cash-buyer.com/blog/san-diego-median-home-price-102-million-july-2026-market-analysis/)); June-over-June the combined median is **up 4.4%** ($910K → $950K), detached $1,125,000 (+5.1%), attached $670,000 (+1.1%) — from [SDAR's monthly indicators](https://sdar.stats.10kresearch.com/docs/mmi/x/report).
- **Inventory is the highest since 2020 — ~3.2 months of supply — yet still seller-leaning** (balanced ≈ 6 months). New listings fell 13.9% in June; H1 2026 new listings down 6.6% YoY, with the decline concentrated in detached (−11.6%). ([Redfin market page](https://www.redfin.com/city/16904/CA/San-Diego/housing-market), SDAR.)
- North County detached homes still sell in ~2 weeks ([a competitor's monthly North County report](https://mylenemerlo.com/blog/north-county-san-diego-real-estate-market-report-july-2026/) — note that solo agents are already running the exact monthly-report play GAMEPLAN §7 prescribes, and getting indexed for it).

*Content implication:* the "more inventory but still tight" tension is the story buyers and sellers are both confused by. A dated market-pulse post that states both facts plainly, with the SDAR numbers cited, answers the question AI currently answers with generic national commentary.

#### Insurance: the biggest homeowner story in the county

- The CDI approved a **FAIR Plan average rate increase of 29.1%, effective October 15, 2026**; wildfire-exposed parcels can see far more ([Oakview Insurance summary](https://www.oakviewins.com/ca-fair-plan-rate-increase-2026/)). **Verify against the CDI filing itself before publishing.**
- The FAIR Plan now covers **~5% of California single-family homes (March 2026), up from 1.5% in December 2020** ([Stanford Woods Institute](https://woods.stanford.edu/news/californias-home-insurance-crisis-spreading-beyond-wildfire-country)); San Diego County FAIR policies **tripled 2018→2022 (5,385 → 16,679)**, concentrated in the eastern backcountry ([Jump Insurance](https://jumpins.com/san-diego-home-insurance-wildfire-neighborhoods/)).
- The FAIR Plan is fire coverage, not homeowners insurance — it needs a **Difference in Conditions** companion policy for liability/theft/water/loss-of-use ([TSM](https://www.tsminsurance.com/resources/wildfire-insurance-california-homeowners), [Old Harbor](https://oldharbor.com/2026/07/01/fire-insurance-san-diego/)).

*Content implication:* this lands hardest exactly where the team's real book is — Fallbrook, Valley Center, Ramona, Escondido's edges — plus Scripps Ranch, which carries 2003 Cedar Fire memory. Keyword validation (§4) shows **"california fair plan" at 33,100 searches/month with keyword difficulty 12**. No neighborhood competitor is writing this. It is also a buyer-process story: insurability checks belong in every inland offer timeline now.

#### ADU law: 2026 changed the rules

- **AB 976** permanently removed owner-occupancy requirements for ADUs permitted after Jan 1, 2026; **AB 1033** enables selling an ADU separately via condo conversion, which the **County adopted for unincorporated communities** ([County ADU ordinance amendment](https://www.sandiegocounty.gov/content/sdc/pds/longrangeplanning/ADU-ZO.html) — primary source) — i.e., Fallbrook, Valley Center, Ramona parcels. City of San Diego permitting has compressed to ~3–5 months. Contractor blogs claim lot-coverage/height loosening (25%→30%, 35 ft) — **those specifics vary by jurisdiction; verify against the municipal code before publishing any number.**
- Context: [Axios San Diego on sellable backyard units](https://www.axios.com/local/san-diego/2025/07/14/san-diego-adu-rules-sell-granny-flats).

*Content implication:* the old site's highest-signal legacy blog slug was an ADU post (Scripps Ranch). The 2026 law changes give the refresh a news hook, and the separate-sale angle is genuinely new information for the rural areas nobody else covers. "adu san diego" carries a **$34 CPC** — this is commercial-value content.

#### Schools: a recurring calendar, not a one-off

- PUSD opened 2026–27 enrollment Feb 2, 2026, with defined intra-district transfer windows ([district announcement](https://www.powayusd.com/apps/news/article/2142414)) and publishes an [address lookup + boundary maps](https://www.powayusd.com/apps/pages/boundaries-and-district-maps). Every district in the farm has an equivalent annual cycle.

*Content implication:* an annual "enrollment windows and how transfers actually work" news post per district cluster, published when the windows open, is evergreen-by-repetition, feeds the school-district journal post that already exists, and is the kind of dated, source-linked page assistants cite for "when can I enroll / can we transfer" questions.

#### Coastal infrastructure: the Del Mar bluff story is active

- SANDAG's LOSSAN realignment — moving the rail line off the Del Mar bluffs into a tunnel — continues to generate milestones ([Fortune's overview of the tunnel fight](https://fortune.com/2024/02/14/del-mar-san-diego-railroad-sandag-bluffs-tunnels-project-residents), [Del Mar's project repository](https://www.delmar.ca.us/)); Encinitas cleared a 27-home Ocean Bluff project after geotechnical review ([The Coast News](https://thecoastnews.com/encinitas-clears-way-for-27-home-ocean-bluff-project/)).

*Content implication:* every SANDAG board action on the tunnel is a news post for Del Mar owners ("what was decided, what changes, which properties are affected, what happens next"). Nobody serves this to *property owners* — coverage is transit-politics framed.

#### Development pipeline: the inland cities are building

- **Escondido** holds North County's largest RHNA (9,607 units; 2,309 permitted) and just moved 200+ units into preliminary review ([The Coast News](https://thecoastnews.com/escondido-reviews-housing-proposals-totaling-more-than-200-units/)); the County broke ground on an affordable complex there ([North County Daily Star](https://northcountydailystar.com/county-breaks-ground-on-affordable-housing-complex-in-escondido/)).
- **San Marcos** leads North County on housing goals — 330 units permitted in 2026, 74 deed-restricted ([The Coast News](https://thecoastnews.com/san-marcos-leads-north-county-in-meeting-housing-goals/)).
- **Oceanside**: two Mission Avenue mixed-use projects totaling 500+ units.

*Content implication:* "what's being built in [city] and where" is a quarterly news roundup with permanent reference value, for the cities that are the team's actual transaction book (Escondido is their single largest market — research/salesRecord.md).

---

### 3. The community question surface — where the answers AI cites live today

**City-Data is the stale incumbent, and that is the opening.** The threads that still rank (and that AI answers appear to draw on, per research/aiBaseline.md) for the 92127 comparisons date from 2007–2020:

- [Scripps Ranch or 4S?](https://www.city-data.com/forum/san-diego/1485737-scripps-ranch-4s.html) (2012) · [poway vs scripps ranch vs 4s ranch](https://www.city-data.com/forum/san-diego/1923803-poway-vs-scripps-ranch-vs-4s.html) (2013) · [4S Ranch Pros & Cons](https://www.city-data.com/forum/san-diego/51170-4s-ranch-pros-cons.html) (2007) · [Del Sur and 4S — current market conditions](https://www.city-data.com/forum/san-diego/2003114-del-sur-4s-current-market-conditions-2.html) (2020) · [La Jolla vs Del Mar vs 4S Ranch](https://www.city-data.com/forum/san-diego/2865477-la-jolla-vs-del-mar-vs.html) · [Carlsbad/Encinitas/Del Mar/Rancho Bernardo/4S Ranch](https://www.city-data.com/forum/san-diego/3342853-carlsbad-encinitas-del-mar-rancho-bernardo-2.html)

The recurring question *shapes* in those threads, which the calendar answers with current facts: which of the two/three is "worth" the tax load; what Mello-Roos actually costs and when it ends; which side of a boundary a specific address falls on; commute reality to Sorrento Valley/UTC; what young-family budgets actually buy in each.

**Blind carries the tech-relocation version of the same questions** — [moving to San Diego, best schools](https://www.teamblind.com/post/moving-to-san-diego-best-schools-neighbourhood-8g0ewf2s), [where to live in San Diego](https://www.teamblind.com/post/where-to-live-in-san-diego-ewxggbn8), [places to be](https://www.teamblind.com/post/places-to-be-in-san-diego-kkfy8nes) — and the named set is always the same: Carmel Valley, Del Mar Heights, 4S Ranch, Del Sur, Scripps Ranch, Rancho Bernardo, South Carlsbad, San Marcos ("good schools, affordable"), with commute-to-Sorrento-Valley as the deciding constraint. These are the team's buyers.

**Nextdoor's public layer** — per-neighborhood profile pages and city hubs like [Escondido](https://nextdoor.com/city/escondido--ca/) and its ["best places to live" rankings](https://nextdoor.com/rankings/best-places-to-live/escondido--ca/) — is indexed and quotable-by-AI today. The post layer is resident-only: the runbook assigns it to agents who live in-territory.

**Fair Housing note for everything in this section:** the community phrases questions as "safe," "good," "family-friendly," "what kind of people." We answer the *underlying decision* with places-and-processes facts — tax structure, boundaries, commute times, land-use rules, published data sources — never demographic characterization. HANDOFF §8 governs; the reframe table is in the runbook.

---

### 4. Keyword validation (OpenSEO / DataForSEO, 2026-07-30)

US national volumes; directional for local (local tools undercount, and question long-tail underreports systematically). KD = keyword difficulty.

| Keyword | Vol/mo | KD | Intent | Signal |
|---|---|---|---|---|
| california fair plan | 33,100 | 12 | info | **The outlier.** Huge demand, low difficulty, $9.54 CPC. Statewide term — win the San Diego-specific slice of it. |
| san diego housing market | 1,600 | 38 | commercial | Market-pulse series target. |
| what is mello roos | 1,600 | 0 | info | `/mello-roos` already targets it; journal follow-ups compound it. |
| adu san diego | 480 | 33 | info | **$34.39 CPC** — highest commercial value on the board. |
| selling a house with solar panels | 210 | 0 | transactional | Unclaimed, KD 0, and a real North County escrow pain point. |
| is escondido a good place to live | 170 | 0 | info | Fan-out answer-block post, Fair-Housing-safe framing. |
| escondido real estate agent | 110 | 0 | navigational | Agent-intent, zero difficulty, in their #1 volume market. |
| rancho santa fe real estate agent | 110 | 8 | navigational | Low KD but entrenched incumbents (aiBaseline). |
| mello roos san diego | 110 | 0 | navigational | Held by `/mello-roos`. |
| del mar real estate agent | 90 | 7 | navigational | |
| carmel valley realtor | 50 | 14 | navigational | Primary-keyword cluster member. |
| living in escondido | 50 | 0 | info | |
| moving to oceanside ca | 40 | 0 | info | |
| living in carmel valley san diego | 10 | 42 | info | Head phrase is competitive; the long tail is not. |
| del sur vs 4s ranch · living in 4s ranch · living in del sur · living in scripps ranch · mello roos 4s ranch · torrey pines high school boundaries · poway unified boundary map | *below reporting threshold* | — | — | **This is not absence of demand** — it is demand fragmented across hundreds of phrasings, which is precisely what AI-mode query fan-out retrieves passage-by-passage. Write these as answer blocks inside posts/guides, not as head-term pages. |

Read on the nulls: volume tools see Google Ads groupings; conversational and question queries (the ones assistants answer) mostly never register. The City-Data/Blind evidence in §3 is the demand proof for those topics; the keyword table is the demand proof for the head terms.

---

### 5. What this feeds

Twelve briefed posts, cadence, compliance reframes, and the monthly re-run procedure live in **[docs/content-runbook.md](../docs/content-runbook.md)**. The three highest-conviction first moves from this pass:

1. **FAIR Plan / insurance explainer** — 33K/mo, KD 12, Oct 15 rate-increase deadline gives it a news hook and an update cadence. *(Shipped 2026-07-30: `/blog/california-fair-plan-san-diego`.)*
2. **ADU rules 2026** — the County adopted AB 1033 separate-sale March 4, 2026; $34 CPC; legacy ADU slug precedent. *(Shipped 2026-07-30: `/blog/adu-rules-san-diego-county-2026` — and the solar-sale post shipped alongside it.)*
3. **Del Sur vs 4S Ranch** — the 20-year-old-thread vacuum, provable with the §3 URLs. *(Retired as a standalone post 2026-07-30: both guides already carry the head-to-head as answer blocks, so a post would cannibalize — runbook §4 records the reasoning. The vacuum is served by deepening the guide blocks, not by a new URL.)*

**Verification discipline:** several §2 figures come from insurance-broker and contractor blogs. Before any of them appears on teamazizi.com, trace to the primary source — CDI filing, FAIR Plan published facts, municipal code, County ordinance, district announcements. No secondary-source number ships. (HANDOFF §8: no fabrication; every claim traces to a named source.)

---

*Method: WebSearch sweeps (site-scoped and news-cycle queries) + OpenSEO keyword metrics, from the remote session of 2026-07-30. Reddit pass deferred to the first local `/last30days` run — see runbook §3 for the exact invocation. This file is a snapshot; re-run monthly and append, do not overwrite.*

---

## Team Azizi — Community Listening Pass #2 (opened 2026-08-02, August cycle)

Client-initiated: three sources supplied directly. Dispositions below; the pass stays open for the local Reddit run.

### Items and dispositions

**1. Reddit — r/Moving2SanDiego thread (share link `AjtJ3ut1pD`), supplied 2026-08-02.**
Status: **unreadable from cloud** — Reddit's datacenter block re-confirmed today (both share links 403). Pending either (a) the client pastes the thread text, or (b) the local `/last30days moving to San Diego` run per runbook §3a. Parked, not dropped — the share link is recorded here so the local pass can resolve it.

**2. Quora — "What are the best neighborhoods to live in San Diego if you want to be close to the city but avoid crazy beach prices?"** (question text supplied by client; Quora page itself login-walls fetchers.)
Disposition: **cross-area query → post.** Shipped same day as `/blog/san-diego-neighborhoods-close-to-downtown` (calendar #18) — answers the underlying decision with the guides' verified structural facts (corridors, stock eras, tax structure, transit), no medians, no "best" verdicts. This is the router post for the whole southeast-of-Balboa-Park value pattern; the guides carry the depth.

**Quora answer draft — for Jon to post under his own name, disclosure included (per HANDOFF §2 no profile is operated by the site team; posting is a human act):**

> Full disclosure: I run a real-estate team here, so read accordingly. The honest pattern: the "close to the city, not beach-priced" neighborhoods run east and southeast of Balboa Park — North Park and Hillcrest if you want walkable-urban (pre-war houses and conversion condos; the condo lane is the realistic entry), the College Area if a trolley stop under the neighborhood matters, Lemon Grove/Spring Valley at the 94/125 junction (closer than most people's mental map — Lemon Grove has an Orange Line stop), and El Cajon or western Chula Vista for the full-city version. The reason they cost less is structural, not a bargain: older stock that predates Mello-Roos and HOA-financed development, so a given price carries fewer monthly lines. The mistake to avoid is crossing I-805 eastward in Chula Vista without checking the tax bill — same list price, very different monthly. We keep sourced, no-medians guides for each of these (with the official district/county links to verify everything yourself): [link to /blog/san-diego-neighborhoods-close-to-downtown]

**3. Nextdoor — "friendliest places to live" rankings page (nextdoor.com/rankings/...), supplied 2026-08-02.**
Disposition: **no response possible, and none appropriate.** Fetched and inspected: it is a static SEO/marketing rankings page (twenty neighborhoods, opaque "friendliness scores," no comment surface). Two rules apply: (a) there is nothing to respond *to* — it is not a neighbor post; (b) ranking communities by friendliness is characterization-of-people territory our Fair Housing line bars us from echoing or citing (runbook §2 table — same family as "what kind of people live there"). The Nextdoor lane remains §3c as designed: resident agents sharing factual guide content in their own neighborhoods, disclosed, human. Logged so the next person who finds the rankings page knows why we didn't engage it.

### Pass #2 additions (2026-08-04) — the data-release feed, not the community feed

Four posts shipped this pass off feed **(d)**, the data-release calendar, with no community input at all: `san-diego-property-tax-assessment-appeal` and `prop-19-san-diego-inherited-property` from one Assessor/Clerk-of-the-Board/BOE reading, plus two router posts (`temecula-murrieta-menifee-vs-san-diego-county`, `buying-a-home-with-well-and-septic-san-diego`) recombining facts the guides already carry. Worth stating plainly: **feed (d) is the only one of the four that works from a cloud session.** Feeds (a) and (b) are throttled by the datacenter-egress wall, feed (c) needs the roster to forward threads. Until the local Reddit run happens, the calendar is doing the work the community listening is supposed to do — which is a reason to close the local-run gap, not a substitute for it.

New question-bank entries these posts target, for the AI panel: "how to lower property taxes san diego", "prop 19 inherited house california", "do I have to pay taxes while appealing assessment", "buying a house with a well and septic san diego", "temecula vs san diego county property tax".

### Pass #2 open items
- Local `/last30days` Reddit run (resolves item 1 + the monthly sweep proper).
- AI query panel re-run scheduled with the pass close (~early Sept).
- Topic bank additions this pass: the Quora phrasing joins the panel question list ("close to downtown san diego without beach prices").

*Method note: items supplied by client 2026-08-02; dispositions same day from the remote session. Reddit remains local-only.*
