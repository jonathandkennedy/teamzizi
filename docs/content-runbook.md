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

Ordered for impact, not date. ✔ = shipped (slug is live under `/blog/`) · ✖ = retired with the reason recorded. Volumes from communityVoice.md §4 (directional). Bylines follow the `agents.py` pool (`author_for("/blog/{slug}")` — the three shipped posts landed Nilab/Sofia/Zohra) and get reassigned to area owners when farming assignments are confirmed.

| # | Slug (under `/blog/`) | Lane | Target queries & why | Primary sources | Serves |
|---|---|---|---|---|---|
| 1 ✔ **shipped 2026-07-30** | `california-fair-plan-san-diego` | News+evergreen | **california fair plan (33.1K/mo, KD 12)**; "fair plan rate increase october 2026"; insurability questions. The Oct 15 increase is the hook; update in place as CDI acts. | CDI-approved rate action (29.1%, eff. Oct 15) as reported at approval; cfpnet.com program description; Stanford Woods study | Fallbrook, Valley Center, Ramona, Escondido, Scripps Ranch, 4S Ranch |
| 2 ✔ **shipped 2026-07-30** | `adu-rules-san-diego-county-2026` | News+evergreen | **adu san diego (480/mo, KD 33, $34 CPC)**. The real 2026 story was better than the contractor-blog version: the County adopted AB 1033 separate-sale on **March 4, 2026 (effective April 4)** — verified at the County page; AB 976/1033 verified at leginfo. The "permitted after Jan 1 2026" owner-occupancy claim circulating on contractor blogs was wrong (AB 976 is from Oct 2023) — which is why the verify-first rule exists. | County ADU-ZO amendment page, leginfo bill texts | Rural trio (separate-sale), city-vs-county block touches all 16 |
| 3 ✖ **retired 2026-07-30** | ~~`del-sur-vs-4s-ranch`~~ | — | **Cannibalization check failed**: both guides already carry the head-to-head as answer blocks (`del-sur#vs-4s-ranch`, `4s-ranch#vs-del-sur`, plus `4s-ranch#cfd-worth-it`). A standalone post would split that query across three URLs — the exact failure the posts.py bar exists to prevent. The comparison surface stays in the guides; deepen there if needed. Slot replaced by #4. | — | — |
| 4 ✔ **shipped 2026-07-30** | `mello-roos-payoff-early` | Journal | Payoff mechanics anchored to the Mello-Roos Act + district rate-and-method; administrator-quote process (contacts already in `taxes.py`); bond-vs-services split; the three moments the math is worth running. No amounts published — parcel-specific, per the taxes.py honesty rule. | Mello-Roos Act, district administrators, taxes.py | 92127 cluster, Poway, San Marcos |
| 5 ✔ **shipped 2026-07-30** | `north-county-market-pulse` | News (recurring) | san diego housing market (1.6K/mo, KD 38) long-tail. Shipped on SDAR's June 2026 indicators ($950K combined median +4.4%, 3.2 mo supply, detached listings −11.6% H1), attributed and dated; **update-in-place** — one URL accumulates authority. The weaker July blog-sourced figure was dropped; SDAR-published data only. | SDAR monthly indicators | All 16; the market-report vehicle until `/market-report/` ships |
| 6 ✔ **shipped 2026-07-30** | `selling-a-house-with-solar-panels-san-diego` | Journal | **210/mo, KD 0, transactional** — owned-vs-leased, lease assumption in escrow, UCC-1 release, legacy NEM transfer mechanics (term stated as confirm-with-SDG&E rather than an unverified number), disclosure package. | Process facts framed as process; tariff/term specifics deferred to SDG&E/CPUC by name | Escondido, San Marcos, 92127, all newer-tract areas |
| 7 ✔ **shipped 2026-07-30** | `del-mar-bluff-rail-what-owners-should-know` | News | The property-owner framing nobody serves: 1.7-mile bluff segment, the published route alternatives (I-5 / under-town / coastal), mid-2030s horizon, what bluff vs inland owners watch, comment windows as the influence point. **Update in place per SANDAG milestone** (72-hour SLA). Closes the Del Mar coverage gap. | SANDAG published realignment materials, City of Del Mar project pages | Del Mar, Solana Beach edge of Encinitas |
| 8 | `poway-unified-enrollment-windows` | News (annual) | District enrollment/transfer dates + address-lookup method, published when windows open (~Feb). Extends the school-district post; same pattern later for SDUHSD/Escondido/Carlsbad clusters. **Holding for its January window (client may pull it early).** | District announcements + boundary tools | 4S Ranch, Del Sur, Poway, (RB) |
| 9 ✔ **shipped 2026-07-30** | `is-escondido-a-good-place-to-live` | Journal | 170/mo, KD 0 — answered the Fair-Housing-safe way. Shipped as seven blocks: facts-not-adjectives frame, older-stock/one-CFD reality, two-district check method, the city-sourced open-space inventory (Daley Ranch 3,000+ ac, Lakes Division 4,500+ ac, Kit Carson/Queen Califia), the "is it safe" reframe (EPD beat map + ARJIS + SANDAG CJRD — data locations, no characterization), downtown institutions, honest tradeoffs. Links to the guide rather than restating its schools/commute blocks. | City of Escondido pages (Lakes Division, Daley Ranch, Kit Carson), EPD/ARJIS, taxes.py | Escondido — their single largest market |
| 10 ✔ **shipped 2026-07-30** | `escondido-housing-pipeline` | News (quarterly) | Shipped on the verified mid-2026 record: the Valley Parkway cluster (The Maple 128 approved 1/28/26 · Valley Parkway Townhomes 94 for-sale 6/10/26 · KB Home 70 for-sale 12/10/25 · Quince Street 145 affordable senior under construction · Palomar Heights 510 approved 2021 · county Valley Creek 134 in env. review, construction expected 2028), RHNA scoreboard (~2,300 of 9,607 through 2025 per the city's APR as reported by VOSD), the **HCD letter of inquiry 12/3/25** (eight overdue programs, revocation warning, builder's-remedy stakes) and the 6/24/26 ADU-ordinance response, Prop S as the named constraint, Harvest Hills honestly stalled. Quarterly refresh. | City hearing notices/agendas, HCD letter PDF, Coast News, Voice of San Diego | Escondido, San Marcos variant later |
| 11 ✔ **shipped 2026-07-30** | `home-insurance-before-you-offer` | Journal | Buyer-process companion to #1, shipped with the legal spine verified: C.A.R. RPA makes insurability an **investigation-contingency item (default 17 days), not the loan contingency**; the 2025 FHSZ maps (SD County batch 3/24/25, VH acreage +26%), hazard-vs-insurer-risk-score distinction + the see-and-appeal right, CLUE mechanics (owner orders; seller's 5-yr claims disclosure), AB 38 sale paperwork as underwriting evidence, Safer-from-Wildfires discounts (FAIR Plan: up to 12 discounts since 11/15/25), FAIR+DIC fallback (~19 DIC carriers per CDI), dated 2026 carrier re-entry (Farmers, Mercury/CSAA, Travelers). | Leginfo statute texts, OSFM/CalFIRE, CDI releases + consumer guides, CFPB, C.A.R. RPA sample | Inland/rural areas; every buyer rep |
| 12 ✔ **shipped 2026-07-30** | `oceanside-mission-avenue-mixed-use` | News | Shipped wider than the brief: the Mission Ave pair (901 Mission 273 approved 10/15/25 + 801 Mission 230 approved 5/20/26 = 503), the entitled wave behind it (401 Mission 326 · Blocks 5/20 373 · Modera Neptune 360+62-room hotel · 712 Seagaze 179 under construction), the rules story (43→uncapped→**86 du/ac base certified by CCC 2/2026**, inclusionary 15%/7+/55-yr, SB 79 eff. 7/1/26), the NCTD transit-center 547+hotel awaiting CCC (commission meets **in Oceanside 10/7/26**), Coast Hwy road-diet construction targeted spring 2027. Approved-is-not-built stated throughout. Revised per milestone. | City staff reports/Legistar, CEQAnet, CCC staff reports + calendar, NCTD, Coast News, inewsource | Oceanside, Vista, Carlsbad |

**Batch 2 — the southern-expansion five (all shipped 2026-07-30).** Research method: five parallel primary-source passes, each returning dated findings with URLs and an explicit could-not-verify list; load-bearing claims re-verified directly before writing. Where a figure survived only in press coverage, the post attributes it inline; where it couldn't be verified at all, it stayed out (e.g. Hillcrest's circulating "20-story towers" — the du/ac figures from the CEQA NOD ran instead).

| # | Slug (under `/blog/`) | Lane | What it answers & the facts that anchor it | Primary sources | Serves |
|---|---|---|---|---|---|
| 13 ✔ **shipped 2026-07-30** | `san-diego-short-term-rental-license` | Journal | The STRO system for buyers/sellers: four tiers, live cap state (Tier 3 open, 821 remaining of the 1% cap; Tier 4 Mission Beach closed to a lottery waitlist — Treasurer table 7/17/26, re-verified on the live page), **licenses die at close of escrow** (SDMC §510.0106(e)), 90-day minimum use, fees eff. 3/1/25, Measure C TOT zones eff. 5/1/25, the Jan 1 2030 coastal sunset (§510.0112). Counts move — revisit quarterly. | City Treasurer STRO pages, SDMC ch. 5 art. 10, CCC staff report W14f | PB, La Jolla, OB, North Park, Hillcrest, Downtown |
| 14 ✔ **shipped 2026-07-30** | `whats-changing-in-hillcrest` | News | The three clocks with dates: FPA mechanics (380 ac, 109→218/290 du/ac per CEQA NOD, CPIOZ corridors, ordinances eff. 12/1/24, 17,200 capacity per the city's release); the rezone's actual first filings (post-office block ~270 units applied since 7/25; Hillcrest Hall 97 affordable, SDHC 4/16/26; AT&T site a watch item); promenade open-by-end-2026/full 2027; **USPS moving onto Normal St** (proposal 12/30/25, no date yet); UCSD: McGrath opened 7/28/25, demolition late summer 2026, construction summer 2027, operational 2033 (Regents $150M 3/19/25). Revise per milestone. | City planning pages, R-315731, CEQAnet NOD, USPS notice, UCSD capital pages, Regents item F2 | Hillcrest, North Park, Downtown edge |
| 15 ✔ **shipped 2026-07-30** | `la-jolla-cityhood-what-owners-should-know` | News (tracker) | LAFCO-primary record: petition certified 6,772 vs 6,750 (4/29/25, amended 8/5/25); city's challenge stricken 10/24/25; CFA = London Moeder, $150k NTE, applicant-funded, **authorized 6/15/26** (⚠ LAFCO's project page misfiles this under 5/4/26 — meeting documents control; our earlier fast-lane note had the wrong date, corrected below); dual-vote law (Gov C 57119/57176.1) + the live dispute over it (VOSD 6/15/26); no-change facts (1% cap, no reassessment, school districts outside LAFCO jurisdiction per 56036(b)); LAFCO timeline → conditional Nov 2028 election, effective 7/2029. Next dates: LAFCO 8/3/26, 10/5/26. | sdlafco.org staff reports/agendas/executed contract, leginfo, applicant PCFA (labeled) | La Jolla |
| 16 ✔ **shipped 2026-07-30** | `fanita-ranch-where-it-stands` | News (tracker) | Court-verified chronology: approved 9/23/20 · 9/14/22 · 6/11/25, blocked after each — 3/2022 wildfire-evacuation CEQA ruling; 10/1/24 judgment/writ (GP consistency; wildfire ch. 4.18 spared); **6/4/26 dual rulings**: D085121 affirmed the set-aside but *reversed* the Elections Code finding (no court has ordered a vote — precision point), Bacal ruled against the 2025 density-bonus path same day. Status: unentitled, ungraded, no vote scheduled, HomeFed "looking at all our options" (ECM 6/20/26). ~2,949/3,008 units ≈ an eighth of Santee's 22,614-unit stock (DOF E-5 2026). | D085121 opinion (loaded PDF), city-posted judgment+writ, CEQAnet NOD 6/12/25, DOF E-5 | Santee |
| 17 ✔ **shipped 2026-07-30** | `chula-vista-mello-roos-east-vs-west` | Journal | The method post the guide's #east-west block promises: the ≤5-CFD stack (SUHSD's own explainer), inventories (33 city levy lines FY25-26; CVESD 17; SUHSD 20), the parcel lookup chain (county special-assessments → Auditor CFD list → Spicer/CVESD/SUHSD), Notice of Special Tax rights (CC 1102.6b + GC 53340.2), end-date split (school CFDs 25–30 yrs, some ended; city maintenance districts perpetual), 8/2025 refunding trimmed four eastern districts, west-side exceptions (Citrus Bay $2,702–2,812 assigned + 2%/yr per the city's 2024 staff report; bayfront project district; DIF CFD 17-I; opt-in clean energy). **No current-year city rates published anywhere loadable — the post teaches the lookup instead of printing numbers.** | County Auditor FY25-26 CFD list, city staff reports/RFP, CVESD/SUHSD special-tax reports + portals, leginfo | Chula Vista |

**Batch 3 — August cycle opener (client-fed).** Listening pass #2 opened 2026-08-02 with three client-supplied sources (communityVoice.md pass #2 has full dispositions + the Quora answer draft for Jon).

| # | Slug (under `/blog/`) | Lane | What it answers & why | Primary sources | Serves |
|---|---|---|---|---|---|
| 18 ✔ **shipped 2026-08-02** | `san-diego-neighborhoods-close-to-downtown` | Journal | The Quora/Reddit perennial ("close to the city, not beach prices") answered as the router post: the southeast-of-Balboa-Park pattern (North Park · Hillcrest · College Area · Lemon Grove · Spring Valley · El Cajon · west Chula Vista · downtown condos), cost structure not medians, "best"-free per §2. All facts reused from verified guide blocks; the post adds the cross-area pattern the guides individually can't. | The guides' own sourced blocks (no new external claims) | Eight areas at once — the southern expansion's router |

**Batch 4 — the tax batch and the router pair (2026-08-04).** Four posts off one verification pass, which is the batch-production thesis in §6.2 tested properly: a single Assessor/Clerk-of-the-Board/BOE reading produced #19 and #20, and #21/#22 recombine facts the guides already carry with no new external claims (the #18 method). Selection logic: the tax pair serves all 31 areas at once — including College Area, El Cajon, Spring Valley and Lemon Grove, which had nothing beyond the router — while #21 closes the Riverside corridor's post gap and #22 serves the rural trio plus RSF, the deliberate guide-only area.

| # | Slug (under `/blog/`) | Lane | What it answers & the facts that anchor it | Primary sources | Serves |
|---|---|---|---|---|---|
| 19 ✔ **shipped 2026-08-04** | `san-diego-property-tax-assessment-appeal` | Journal | The two routes to a lower assessed value and the fact that they are *not* sequential: the Assessor's free decline-in-value Review of Assessment (form available **Dec 1–Apr 30**, (858) 505-6262) versus the formal Assessment Appeals Board application (**July 2–Nov 30**; Sept 15 in counties whose assessor doesn't mail notices by Aug 1; supplemental/escape **60 days**; calamity **6 months**). Hook is the 2026 roll: record **$845B** gross assessed value, +4.86% (+$39B), ~$8.1B revenue (+$366M), and a record **$34.6B in reductions** = $346M saved. Plus **R&TC §167** — rebuttable presumption for the burden of proof favors the taxpayer on an owner-occupied SFR that is the principal residence and carries the homeowners' exemption (not for escapes from a failure to file or permit). Closes with the block that prevents confusion: appeals reach the 1% ad valorem value, **not** Mello-Roos or fixed charges. | SD County Assessor release (7/2/26), Clerk of the Board AAB pages + filing guide, leginfo R&TC §167 | All 31 |
| 20 ✔ **shipped 2026-08-04** | `prop-19-san-diego-inherited-property` | Journal | Prop 19 as two separate machines: the intergenerational exclusion (eff. **2/16/21** — family home must be principal residence of parent *and* child; excluded amount = factored base year value + $1M, adjusted to **$1,044,586** for 2/16/25–2/15/27; family farms qualify, other real property no longer does; **continuing** occupancy condition) and base-year transfers (eff. **4/1/21** — 55+/severely disabled, **3 times**, anywhere in CA, replacement within **2 years**, equal-or-lesser thresholds **100/105/110%** with the excess *added*, BOE-19-B/-D/-DC/-V). The deadline pair families miss: exclusion claim within 3 years or before transfer to a third party, **homeowners' exemption within 1 year**. | BOE Prop 19 pages (rules, forms, adjusted amount) | All 31; heaviest where tenure is longest |
| 21 ✔ **shipped 2026-08-04** | `temecula-murrieta-menifee-vs-san-diego-county` | Journal (router) | What actually changes crossing the county line: Riverside holds the records, and **the SD Auditor's CFD list does not reach Riverside** — so the lookup is the Assessor's parcel records plus the bill's own itemized lines. Formal appeal windows match (July 2–Nov 30, BOE-305-AH, 60-day supplementals) but the informal route does **not**: Riverside's decline-in-value deadline is **Nov 1, 2026** against San Diego's Dec 1–Apr 30 form window — the post's sharpest fact. Plus Gierson Ranch CFD 2026-1 (formed 6/26, $8M authorized, before any home sold), Wine Country/La Cresta as unincorporated county, TVUSD reaching French Valley, Menifee's three school systems, EMWD, the I-15/I-215 split. | Riverside County Assessor + Clerk of the Board, Murrieta legislative record, the three corridor guides | **Temecula, Murrieta, Menifee — their first area-specific post** |
| 22 ✔ **shipped 2026-08-04** | `buying-a-home-with-well-and-septic-san-diego` | Journal (router) | The semi-rural purchase as a *sequence* rather than a checklist — insurance quote first (it can make the property unaffordable and no lender funds without bound coverage), well yield + water quality and septic function/leach field second (five figures, no post-closing remedy), easement and district paperwork third. Adds one fact the guides don't carry: **Civil Code §845** — easement holders maintain a private right-of-way in repair, cost apportioned to use where there's no agreement, enforceable by contribution or specific performance. Plus County PDS jurisdiction, Williamson Act contracts, SDCE's association, and VC's fire-protection CFD as the district worth having. | Civil Code §845 (leginfo); the Fallbrook, Valley Center, Ramona and RSF guides | Fallbrook, Valley Center, Ramona + **Rancho Santa Fe**, served without cannibalizing its guide |

Cadence per GAMEPLAN §7: **2–4/month** — realistically 2 journal + 1–2 news. The twenty-two above front-load that; the monthly listening pass refills the bank. Still banked from the southern seed list: **STRO and the tax roll are now shipped**; remaining: Chula Vista bayfront explainer angle (folded partially into #17), PB Chalcifica redesign (Nov 13 hearing), Midway Rising "delayed indefinitely" (KPBS). Tax-batch remainder: Prop 8 timing as its own January post when the Dec 1 review window opens.

**AI-recommendation tie-in:** every post carries the standard entity graph, a licensee byline with DRE number, and internal links wiring it to the neighborhood guides and agent pages it serves. The post answers the question; the graph tells the assistant *who* answered it — that pairing is what turns citations into "ask Team Azizi about Del Sur."

---

## 5. Distribution & measurement

Each shipped post → **GBP post** (once GBP exists — Phase 2 gate) · Instagram (the active surface) · email digest. Refreshes count as posts on those surfaces (HANDOFF §10).

Measure monthly, into the case-study log: GSC impressions/queries per post URL (are the target phrasings appearing?) · the manual AI panel (ChatGPT/Gemini/Perplexity/AI Overviews) now including one question per shipped post — *is our URL the cited source?* · leads by page via the tagged forms. The win condition for a post is being the cited source for its question, not just ranking.

---

## 6. The acceleration plan (added 2026-07-30)

The client asked for faster needle movement. Honesty first, then the plan.

### 6.1 Sequencing — foundation before DNS (client decision, 2026-07-30)

**The client's call: build the neighborhood foundation out fully, then point DNS.** The site cuts over once, complete — Google and the AI crawlers meet a deep site on first fetch rather than watching a thin one assemble itself. The trade being accepted, recorded honestly: every week before cutover, the old index decays further and the corrupted brand answers stand uncorrected (GAMEPLAN §2). That makes the foundation sprint a *sprint* — the gate below is a finishable checklist, not an open-ended standard.

**The foundation-complete gate (DNS points when every box is checked):**

- [x] 16 neighborhood guides, photograph on every page *(done pre-sprint)*
- [x] Temecula / Murrieta / Menifee corridor guides *(added 2026-07-30 at client request — photography pass still open)*
- [x] Money-page layer: `/mello-roos`, `/home-valuation`, sell/buy/concierge *(done pre-sprint)*
- [x] Paperwork trio that kills escrows: insurance (FAIR Plan), solar-sale, Mello-Roos payoff *(shipped 2026-07-30)*
- [x] Market pulse live with current, attributed data *(shipped 2026-07-30 — refresh if >1 month stale at cutover)*
- [x] Del Mar coverage gap closed *(bluff/rail post shipped 2026-07-30)*
- [x] Remaining calendar foundation posts *(#9, #10, #11, #12 all shipped 2026-07-30; #8 enrollment-windows deliberately holds for its January news window per its row)*
- [ ] Quarterly guide-refresh pass #1 — every guide's facts re-verified, dated current
- [ ] **`LEAD_ENDPOINT` set** — forms must deliver from minute one (client)
- [ ] Privacy policy page (client-dependent item in HANDOFF §9 — forms require it)
- [ ] RSF keep-or-drop decided (client) — the one area allowed to stay a gap

**What runs in parallel, not after:** GBP creation and postcard verification (the profile can exist and collect reviews before cutover; its website field updates at cutover), review velocity, and the entity cleanup list. These are client-gated and slow-compounding — starting them now means the site launches *into* an entity that already has signals, which serves the same complete-on-arrival logic as the content gate.

**The needle ranking still holds underneath the sequencing** — launch, GBP, reviews, then content velocity, then entity cleanup. The decision above changes *when* DNS happens, not what matters most once it does.

### 6.2 The weekly rhythm (replaces "2–4/month" pacing)

**One post per week, every week**, plus fast-lane news. Sustainable because the system batches:

- **Monday (30–60 min):** listening scan — the §3b web sweeps, agent-forwarded threads, the data-release calendar. Pick or confirm the week's post from the calendar.
- **Midweek:** verify sources (primary only), write in `posts.py` block format, byline per the pool.
- **Friday:** build → validate → date-churn guard → push → PR. After merge: IndexNow ping.
- **Within 48h of deploy:** repurpose to Instagram now; queue as a GBP post for the day GBP exists.
- **Monthly (first week):** full listening pass — local `/last30days` Reddit sweep + append to communityVoice.md; re-run the AI query panel; refill the calendar to ≥8 briefed posts.

**Fast-lane SLA:** a CDI action, SANDAG board decision, district boundary/enrollment change, or council approval affecting a farm area gets its post — or an update-in-place to the existing one — within **72 hours**. Being the first fact-dense page on a local change is how a small site beats portals to a citation.

**Fast-lane log (movement sweep 2026-07-30, all revisions applied same day):**
- **Gierson Ranch CFD 2026-1 formed** — Murrieta took it through hearings June 2 and passed the special-tax ordinance's second reading June 16 (Legistar record), bonds authorized to $8M. Murrieta guide `#new-districts` + taxes.py revised from "noticed" to "formed."
- **FAIR Plan assessment pass-through upheld** — LA Superior Court 6/30/26, CDI release 7/1/26 (~$28 median temporary fee, ≤2-yr recovery; challenger weighing appeal; AB 1680 in Senate committee). New `#assessment-surcharge` block added to the FAIR post.
- **La Jolla CFA timeline concrete** — ~~LAFCO approved the London Moeder contract 5/4/26~~ **CORRECTED 2026-07-30 (evening pass):** the Commission authorized the contract at its **June 15, 2026 special meeting** (Item 7a); executed 7/8–9/26. LAFCO's own project page misfiles the item under a "May 4, 2026" heading — that mislabel is where the 5/4 date came from; the agenda, slide deck, staff report and executed contract all say June 15. LAFCO's published timeline is also wider than the news account we first logged: draft + 90-day review + workshops July–Oct 2027, final Nov 2027–Mar 2028, Commission ~May 2028, election Nov 2028, effective 7/2029. Fieldwork start Aug 2026 and next LAFCO date 8/3/26 stand. The cityhood-tracker post (#15) is now shipped and carries the corrected record.
- **Escondido adopted ADU separate-sale** — 6/24/26 ordinance overhaul (ministerial approval + AB 1033 opt-in). ADU post `#city-vs-county` body updated.
- No movement: SANDAG Del Mar (technical-studies notice 7/23/26 only), SDAR (July data ~mid-August). Banked from the sweep: record $845B county tax roll (Assessor, 7/13/26) for the tax batch; PB Chalcifica redesign + Nov 13 hearing; Hillcrest promenade end-of-2026 + post-office relocation (feeds the Hillcrest explainer brief); Midway Rising "delayed indefinitely" (KPBS).
- **Mechanics added:** posts now support an `"updated"` key — renders "Published X · Revised Y" and drives schema `dateModified` — so lane-2 update-in-place revisions carry a visible date without a new URL.
- **Official-resources layer shipped (2026-08-02):** every neighborhood page now ends with "Check the record" — verified links to the agencies each guide names (157 links, 74 official domains, all loaded before listing; rule and the domain-rot catches recorded in `build/data/resources.py`). Trigger: the page ranking for "4S Ranch" links zero community resources; ours now links them all. **Maintenance: re-verify the URL set annually with the quarterly guide-refresh pass** — the pass caught five dead/moved "official" domains on day one (helixwater.org → hwd.com among them), which is the decay rate to expect.

**Batch production is the multiplier.** One verification pass feeds several posts: today's single research pass shipped three (insurance, solar, ADU). Future themed batches: the schools batch (one enrollment post per district cluster, each January), the development batch (one pipeline post per city, quarterly), the tax batch (payoff + assessment appeals + Prop 19, off one Auditor/Assessor reading).

**Tax batch shipped 2026-08-04 — what the pass actually cost, and two corrections it produced.** One reading of the Assessor, the Clerk of the Board, the BOE and two leginfo sections produced #19 and #20; #21 and #22 needed no external sourcing beyond one statute, because the guides already carried their facts. Recorded for the next person:

- **Correction to the 7/30 sweep:** the record roll was banked here as "Assessor, 7/13/26." The release is dated **July 2, 2026**. The figure ($845B) was right, the date was not — banked items get re-verified at write time, not copied forward.
- **Riverside County Auditor-Controller 403s datacenter egress** (`auditorcontroller.org/property-tax-fixed-chargespecial-assessments`), so the corridor's fixed-charge list could not be read from the container. Post #21 routes readers to the Riverside Assessor's parcel records and the bill's own itemized lines instead — both verified — rather than describing a page we couldn't load. Add it to the residential-IP list alongside Reddit and the review platforms.
- **Neither county publishes an appeal filing fee** on any page checked. Both posts say so and tell the reader to confirm with the Clerk of the Board, rather than printing a number that isn't sourced.
- **The validator earned its keep again:** four leads shipped without a place name and `check_answer_blocks` failed the build on all four — the failure mode where a passage lifted into an AI answer loses its geography. Fixed at the source, not by relaxing the check.

### 6.3 Per-area coverage matrix

Every area gets touched at least quarterly by a post that serves it, a guide refresh, or a fast-lane news item. State as of **2026-08-04 (twenty-one posts live)**. Two posts now serve every row and are not repeated in the table: the market pulse, and the tax pair (#19 assessment appeals, #20 Prop 19) — property tax reaches all 31 areas equally, which is exactly why the batch was chosen. Rows list area-specific coverage beyond those three:

| Area | Guide | Served by posts today | Next planned touch |
|---|---|---|---|
| Fallbrook | ✅ | FAIR Plan · ADU separate-sale · school-district · insurance-before-offer · **well-and-septic sequence ✔** | quarterly refresh pass |
| Valley Center | ✅ | FAIR Plan · ADU separate-sale · insurance-before-offer · **well-and-septic sequence ✔ (carries the fire-CFD trade)** | water-district explainer (bank) |
| Ramona | ✅ | FAIR Plan · ADU separate-sale · insurance-before-offer · **well-and-septic sequence ✔** | quarterly refresh pass |
| Escondido | ✅ | FAIR Plan · solar · school-district · **is-escondido ✔ · pipeline ✔ (quarterly)** | pipeline refresh ~Oct 2026 |
| San Marcos | ✅ | solar · payoff (91-CFD city) | #10 variant: San Marcos leads RHNA |
| Oceanside | ✅ | ADU (jurisdiction block) · **Mission Ave build-out ✔ (revised per milestone; CCC in Oceanside 10/7/26)** | transit-center CCC decision (fast lane) |
| Vista | ✅ | ADU (jurisdiction block) · pulse | "no Vista CFD" fact worth a payoff-post block on refresh |
| Carlsbad | ✅ | school-district (boundary block) · ADU (jurisdiction) | enrollment-windows batch (Jan) |
| Encinitas | ✅ | school-district (Cardiff block) · bluff/rail (Solana edge) | enrollment batch |
| Poway | ✅ | school-district (PUSD reach) · payoff (CFD contrast) | guide refresh pass |
| 4S Ranch | ✅ | FAIR Plan · school-district · payoff | guide refresh pass |
| Del Sur | ✅ | school-district · payoff (bond-vs-services link) | guide refresh pass |
| Scripps Ranch | ✅ | FAIR Plan · school-district | ADU-on-canyon-lots angle (bank) |
| Carmel Valley | ✅ | school-district (DMUSD/SDUHSD block) · pulse | SDUHSD enrollment batch |
| Del Mar | ✅ | **bluff/rail ✔ (gap closed 2026-07-30)** | update-in-place per SANDAG milestone |
| Rancho Santa Fe | ✅ | **well-and-septic sequence ✔ (sewer-vs-septic block)** | Gap closed the only way it could be without cannibalizing: a cross-area post that cites the guide rather than restating it. Keep-or-drop call still the client's (HANDOFF §9) |
| **Temecula** *(added 2026-07-30)* | ✅ new | pulse (county-level context) · **county-line router ✔** | Wine Country jurisdiction post (bank); Riverside listening added to the monthly pass; photography |
| **Murrieta** *(added 2026-07-30)* | ✅ new | pulse · **Gierson Ranch CFD formation reflected in guide (formed June 2026, $8M authorized)** · **county-line router ✔** | track first bond issuance (fast lane); photography |
| **Menifee** *(added 2026-07-30)* | ✅ new | pulse · **county-line router ✔** | EMWD/CFD new-construction explainer variant (bank); photography |

**Riverside note:** the three corridor guides cite city-published district records (the SD Auditor's list doesn't reach Riverside County), publish no volume claims (no Compass record there), and ship on designed plate heroes until a photography pass — same §5-of-HANDOFF verification method when it runs. Add `Temecula Murrieta Menifee` phrasings to the monthly listening sweeps and the AI query panel.

**Southern expansion (2026-07-30, twelve areas):** La Jolla, Pacific Beach, Ocean Beach, Hillcrest, North Park, Downtown, College Area + Chula Vista, Santee, El Cajon, Spring Valley, Lemon Grove — all guides live, all served by the market pulse plus their own live-fact blocks. **The five-post seed bank shipped same day (calendar #13–#17):** STRO license explainer (serves PB · OB · La Jolla · North Park · Hillcrest · Downtown), La Jolla cityhood tracker, Hillcrest three-clocks explainer, Chula Vista east/west Mello-Roos method, Fanita Ranch tracker. Area-specific coverage now: La Jolla ×2 (cityhood, STRO) · PB/OB ×1 each (STRO; PB guide #str-license deepened by it) · Hillcrest ×2 (explainer, STRO) · North Park/Downtown ×1 (STRO) · Chula Vista ×1 (east/west) · Santee ×1 (Fanita). Still post-less beyond the pulse: College Area, El Cajon, Spring Valley, Lemon Grove — candidate briefs: College Area mini-dorm/STRO angle, El Cajon Gillespie Field tracker, the tax batch touching all four. Trackers #14/#15/#16 carry standing revision triggers (promenade opening · LAFCO milestones · court docket). Add all twelve to listening sweeps and the AI panel; photography pass ✔ done (all fifteen new areas, 2026-07-30).

### 6.4 30 / 60 / 90 (re-baselined 2026-07-30 after the foundation sprint)

- **By day 30:** ~~posts #9, #10, #11, #12 shipped~~ **done day one (2026-07-30)** — the calendar's foundation set is complete (#8 enrollment-windows holds for its January news window unless the client wants it early). Remaining day-30 items: guide-refresh pass #1; first local `/last30days` Reddit pass appended to communityVoice.md; client actions requested in writing: `LEAD_ENDPOINT`, privacy policy, GBP postcard, RSF call.
- **By day 60:** foundation gate fully checked → **DNS cutover** (launch-runbook sequence), GSC/Bing submission, IndexNow, re-index requests; GBP website field pointed at the live domain; every post backfilled as GBP posts.
- **By day 90:** AI panel re-run against the 14-query zero baseline with the site live — the case study's first "after" measurement; market pulse on its third monthly revision; listening pass #4; double down on whatever earned citations.

---

## 7. Shipping a post — mechanics

1. Add the post dict to `build/data/posts.py` (blocks format; study the school-district post). Confirm byline against `agents.py` and the three-places-agree rule (HANDOFF §2).
2. `python3 build/generate.py` then `python3 build/optimize.py` if images were added, then `python3 build/validate.py` — the answer-block checks apply to posts too.
3. **Date-churn guard (HANDOFF §9, open item):** the generator restamps every dated page. Before committing, `git diff` and **restore any page whose only delta is the date** — commit only the blog index, the new post, the sitemap, and pages whose content actually changed.
4. OG card: `build/og.py` covers new pages on regenerate; confirm the post got one.
5. Push → PR → after merge+deploy, `python3 build/indexnow.py`, then the GBP/IG repurpose.

---

*Created 2026-07-30 alongside listening pass #1. Owner: whoever runs the content engine that month. Re-read HANDOFF §8 before every post — real estate is not generic marketing.*
