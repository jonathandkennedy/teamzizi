# Content Runbook — the Journal & News Desk

**What this is:** the operating system for blogs and news updates about the sixteen farm areas — how topics are sourced from community listening, what formats exist, the compliance lines, the first twelve posts, and how a post physically ships. GAMEPLAN §7 is the strategy; this is the procedure. Evidence base: [research/communityVoice.md](../research/communityVoice.md) (listening pass #1, 2026-07-30).

**What it is for:** two engines, one content stream. Posts answer the questions people actually ask about these areas (Reddit, Nextdoor, City-Data, Blind — and clients in showings), so Google ranks them for high-intent queries and questions, and so AI assistants retrieve and cite them when asked about the areas or for an agent recommendation in them. Every post also feeds GBP posts, Instagram, and email — one research effort, four surfaces.

---

## 1. Three lanes, one bar

**The bar, from `build/data/posts.py` (applies to all lanes):** a post must answer something the sixteen neighborhood guides do not, or it is cannibalising them — one query answered across two URLs splits the signal and helps nobody. Check the guide for the area *first*; if the answer belongs there, refresh the guide instead.

### Lane 1 — Journal posts (evergreen answers)

The school-district post (`/blog/san-diego-school-district-by-address`) is the template: a dek, then 5–8 self-contained answer blocks — each an H2-level question phrased the way people ask it, a lead that fully answers it standing alone (survives being lifted out of the page — no bare pronouns, place name present; `validate.py` enforces this), a short body with the nuance, internal links to guides. 800–1,500 words. `FAQPage` schema derives automatically from the blocks. Byline: a named licensee per `agents.author_for()` — the agent who farms the areas the post serves, where assignments allow.

### Lane 2 — News updates (dated reactions)

300–700 words. One event → what it means if you own or are buying in the affected areas. Structure: what happened (dated, source-linked) · who it affects (which of the 16, specifically) · what it changes practically · what happens next. Year/month-stamped titles where natural ("…: October 2026 rate change"). When a story moves, **update the same post in place** and bump the visible updated date — one URL accumulates authority; a trail of "Part 3" posts does not. The news feed comes from the listening pass (§3): CDI/insurance actions, ADU/housing law, SANDAG and bluff-rail milestones, district enrollment windows, city development approvals, monthly SDAR data.

### Lane 3 — Guide & snapshot refreshes (quarterly)

Not new URLs — the discipline that keeps the existing 16 guides and `/mello-roos` from rotting, per HANDOFF §10. Each refresh is itself content: it becomes a GBP post and an Instagram post ("Del Sur guide updated: the CFD schedule changed"). Market-stat *snapshots* live in dated posts (lane 2) — evergreen pages still carry **no prices, no medians** (HANDOFF §4 rule; a stale median is worse than none).

---

## 2. Compliance — the lines that do not move

HANDOFF §8 governs. The listening pass will surface questions phrased in ways we cannot answer as phrased. Answer the *underlying decision* with places-and-processes facts:

| Community phrasing | We publish | We never publish |
|---|---|---|
| "Is X safe?" | Where the published data lives (Sheriff/SDPD open data, CalFIRE hazard maps) and how to read it for an address | Any characterization — "safe," "sketchy," crime adjectives |
| "Best schools?" / "good schools?" | Which district assigns, boundary specifics, enrollment/transfer process, address-lookup method | Ratings, rankings, "top schools," district quality claims |
| "Family-friendly? What kind of people live there?" | Housing stock, lot sizes, parks/trails inventory, HOA rules, commute times | Any demographic desirability framing — Fair Housing steering |
| "Is it worth the Mello-Roos?" | The actual CFD math per community (`build/data/taxes.py`), payoff mechanics, what the bonds funded, expiry dates | "Worth it" verdicts about the people who choose it |
| "Should I take the FAIR Plan?" / tax/legal questions | How the process works, what the filings say, current rates/dates, and *"confirm with a licensed [broker/CPA/attorney]"* | Advice. We are informational, not licensed counsel in those domains |

Plus, non-negotiable: **no fabrication** — every figure traces to a named primary source (CDI filing, municipal code, County Auditor, district announcement — never a contractor or broker blog's retelling; verify before publish) · **no `Review`/`aggregateRating` schema** · **no bought placements** · anything touching Sonia's profiles or legacy routes through the client (HANDOFF §2).

---

## 3. The monthly listening pass (how topics are sourced)

Run monthly; append findings to `research/communityVoice.md`. Four feeds:

**a) `/last30days` — the community sweep.** The skill is installed project-level at `.claude/skills/last30days/` (v3.18.4, keyless mode configured). **Run it from a local machine** — Reddit 403-blocks datacenter egress, so remote/cloud sessions get no Reddit lane (verified 2026-07-30; documented in communityVoice.md §1). Invocation from the repo root in Claude Code:

```
/last30days moving to North County San Diego 92127 Del Sur 4S Ranch
/last30days Escondido housing market
/last30days Carmel Valley San Diego real estate      ← always disambiguate "San Diego";
                                                        bare "Carmel Valley" returns Monterey County
```

The skill plans subqueries, pulls Reddit posts *with comment threads and vote counts*, HN, YouTube transcripts where configured, and saves raw briefs to `~/Documents/Last30Days`. What to extract into the topic bank: questions asked more than once, misconceptions stated confidently, complaints with specifics, and any thread where the accepted answer is old or wrong — each with URL and engagement counts.

**b) Web sweeps that work from anywhere:** `site:city-data.com forum san-diego <area>` · `site:teamblind.com san diego <area>` · `<city> housing development news <month year>` · the local outlets directly (The Coast News, North County Daily Star, Del Mar Times, SD U-T, Patch per-city, Axios San Diego).

**c) Agent-sourced signal (the best feed, zero tooling).** Nextdoor's post layer is resident-only — so the agents who live in-territory *are* the access. Standing ask to the roster: forward any neighborhood thread where a housing/tax/school/insurance question got a wrong or thin answer. Same for questions heard twice in showings or listing appointments. One forwarded thread ≈ one post brief.

**d) Data releases on a calendar:** SDAR monthly indicators · County Auditor CFD report (annual, feeds taxes.py + Mello-Roos refresh) · district enrollment windows (each January–February) · CDI rate actions · city RHNA progress reports.

Topic bank → brief (template: `research/contentPlaybook.md` §5) → post. A topic with no primary source available doesn't get written; it gets parked with a note, like `photos.REJECTED`.

---

## 4. Editorial calendar — the first twelve

Ordered for impact, not date. ✅ = sources gathered in listening pass #1; write next. Volumes from communityVoice.md §4 (directional). Bylines follow `agents.author_for()` / farming assignments — names below are the *area owners* to consult, not hardcoded bylines.

| # | Slug (under `/blog/`) | Lane | Target queries & why | Primary sources | Serves |
|---|---|---|---|---|---|
| 1 ✅ | `california-fair-plan-san-diego` | News+evergreen | **california fair plan (33.1K/mo, KD 12)**; "fair plan rate increase october 2026"; insurability questions. The Oct 15 increase is the hook; update in place as CDI acts. | CDI filing/approval docs, cfpnet.com published facts, Stanford Woods study | Fallbrook, Valley Center, Ramona, Escondido, Scripps Ranch, Poway |
| 2 ✅ | `san-diego-adu-rules-2026` | News+evergreen | **adu san diego (480/mo, KD 33, $34 CPC)**; AB 976 owner-occupancy removal; AB 1033 separate-sale in unincorporated county. Verify every numeric limit against the specific municipal code — they differ by city. | County ADU-ZO amendment page, city municipal codes, bill texts | Rural trio (separate-sale), Scripps (legacy ADU slug), all 16 |
| 3 ✅ | `del-sur-vs-4s-ranch` | Journal | The proven-demand comparison whose ranking answers are 2007–2020 City-Data threads (URLs in communityVoice §3). Micro-volume head term, huge fan-out surface: CFD math, both-PUSD nuance, HOA structure, commute, housing stock eras. | County Auditor CFD reports (already in `taxes.py`), PUSD boundary maps | Del Sur, 4S Ranch (and the whole 92127 story) |
| 4 | `mello-roos-payoff-early` | Journal | "Can you pay off Mello-Roos early — and should you?" — the next question after `/mello-roos` (what-is: 1.6K/mo, KD 0, already held). Payoff mechanics, prepayment quotes, when it pencils. | County Auditor, CFD administrators' payoff procedures | 92127 cluster, Poway, San Marcos |
| 5 | `north-county-market-pulse` | News (recurring) | san diego housing market (1.6K/mo, KD 38) long-tail; July 2026 numbers in hand: $1.02M median, 3.2 mo supply highest since 2020 yet seller-leaning, detached listings −11.6% YTD. Monthly or quarterly, dated, one URL per period or update-in-place — decide at post 2. | SDAR monthly indicators (cite the report), Redfin market data | All 16; the market-report vehicle until `/market-report/` ships |
| 6 | `selling-a-house-with-solar-panels-san-diego` | Journal | **210/mo, KD 0, transactional** — lease/PPA transfer in escrow, buyout math, NEM status effects. Ubiquitous in 92127/Escondido inventory. | CPUC NEM docs, lease-transfer procedures from the major lessors' published terms | Escondido, 4S/Del Sur, Oceanside, San Marcos |
| 7 | `del-mar-bluff-rail-what-owners-should-know` | News | SANDAG LOSSAN tunnel milestones → property-owner framing nobody serves (coverage is transit-politics framed). Update in place per board action. | SANDAG board docs, City of Del Mar project repository | Del Mar, Solana Beach edge of Encinitas |
| 8 | `poway-unified-enrollment-windows` | News (annual) | District enrollment/transfer dates + address-lookup method, published when windows open (~Feb). Extends the school-district post; same pattern later for SDUHSD/Escondido/Carlsbad clusters. | District announcements + boundary tools | 4S Ranch, Del Sur, Poway, (RB) |
| 9 | `is-escondido-a-good-place-to-live` | Journal | 170/mo, KD 0 — answered the Fair-Housing-safe way: two-district structure, CFD-free older pockets vs newer CFD tracts, commute reality, land-use edges. The reframe-table showcase. | District maps, taxes.py, Census commute data (cited, not embedded as demographics) | Escondido — their single largest market |
| 10 | `escondido-housing-pipeline` | News (quarterly) | "What's being built in Escondido and where": RHNA 9,607, 200+ units in review, County affordable groundbreaking. Permanent reference value; quarterly refresh. | City agendas/staff reports, Coast News + Daily Star reporting | Escondido, San Marcos, Oceanside variants later |
| 11 | `home-insurance-before-you-offer` | Journal | Buyer-process companion to #1: check insurability *before* writing the offer — CalFIRE hazard map lookup, carrier quote timing in escrow, FAIR+DIC as the fallback plan. | CalFIRE FHSZ maps, CDI consumer guides | Inland/rural areas; every buyer rep |
| 12 | `oceanside-mission-avenue-mixed-use` | News | 500+ units in two downtown projects — what it means for Oceanside owners/buyers; the city is their #2 volume market among the ten added areas. | City of Oceanside planning docs | Oceanside, Vista, Carlsbad |

Cadence per GAMEPLAN §7: **2–4/month** — realistically 2 journal + 1–2 news. The twelve above are ~4 months of runway; the monthly listening pass refills the bank.

**AI-recommendation tie-in:** every post carries the standard entity graph, a licensee byline with DRE number, and internal links wiring it to the neighborhood guides and agent pages it serves. The post answers the question; the graph tells the assistant *who* answered it — that pairing is what turns citations into "ask Team Azizi about Del Sur."

---

## 5. Distribution & measurement

Each shipped post → **GBP post** (once GBP exists — Phase 2 gate) · Instagram (the active surface) · email digest. Refreshes count as posts on those surfaces (HANDOFF §10).

Measure monthly, into the case-study log: GSC impressions/queries per post URL (are the target phrasings appearing?) · the manual AI panel (ChatGPT/Gemini/Perplexity/AI Overviews) now including one question per shipped post — *is our URL the cited source?* · leads by page via the tagged forms. The win condition for a post is being the cited source for its question, not just ranking.

---

## 6. Shipping a post — mechanics

1. Add the post dict to `build/data/posts.py` (blocks format; study the school-district post). Confirm byline against `agents.py` and the three-places-agree rule (HANDOFF §2).
2. `python3 build/generate.py` then `python3 build/optimize.py` if images were added, then `python3 build/validate.py` — the answer-block checks apply to posts too.
3. **Date-churn guard (HANDOFF §9, open item):** the generator restamps every dated page. Before committing, `git diff` and **restore any page whose only delta is the date** — commit only the blog index, the new post, the sitemap, and pages whose content actually changed.
4. OG card: `build/og.py` covers new pages on regenerate; confirm the post got one.
5. Push → PR → after merge+deploy, `python3 build/indexnow.py`, then the GBP/IG repurpose.

---

*Created 2026-07-30 alongside listening pass #1. Owner: whoever runs the content engine that month. Re-read HANDOFF §8 before every post — real estate is not generic marketing.*
