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

Cadence per GAMEPLAN §7: **2–4/month** — realistically 2 journal + 1–2 news. The twelve above are ~4 months of runway; the monthly listening pass refills the bank.

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
- **La Jolla CFA timeline concrete** — LAFCO approved the London Moeder contract 5/4/26; fieldwork starts August 2026, draft June 2027, final by Jan 2028, Nov 2028 ballot target; next LAFCO date 8/3/26. Guide lead refined; full detail feeds the cityhood-tracker post (bank).
- **Escondido adopted ADU separate-sale** — 6/24/26 ordinance overhaul (ministerial approval + AB 1033 opt-in). ADU post `#city-vs-county` body updated.
- No movement: SANDAG Del Mar (technical-studies notice 7/23/26 only), SDAR (July data ~mid-August). Banked from the sweep: record $845B county tax roll (Assessor, 7/13/26) for the tax batch; PB Chalcifica redesign + Nov 13 hearing; Hillcrest promenade end-of-2026 + post-office relocation (feeds the Hillcrest explainer brief); Midway Rising "delayed indefinitely" (KPBS).
- **Mechanics added:** posts now support an `"updated"` key — renders "Published X · Revised Y" and drives schema `dateModified` — so lane-2 update-in-place revisions carry a visible date without a new URL.

**Batch production is the multiplier.** One verification pass feeds several posts: today's single research pass shipped three (insurance, solar, ADU). Future themed batches: the schools batch (one enrollment post per district cluster, each January), the development batch (one pipeline post per city, quarterly), the tax batch (payoff + assessment appeals + Prop 19, off one Auditor/Assessor reading).

### 6.3 Per-area coverage matrix

Every area gets touched at least quarterly by a post that serves it, a guide refresh, or a fast-lane news item. State as of 2026-07-30 (end of day), eleven posts live; the market pulse serves all sixteen, so rows list area-specific coverage beyond it:

| Area | Guide | Served by posts today | Next planned touch |
|---|---|---|---|
| Fallbrook | ✅ | FAIR Plan · ADU separate-sale · school-district · **insurance-before-offer ✔** | quarterly refresh pass |
| Valley Center | ✅ | FAIR Plan · ADU separate-sale · **insurance-before-offer ✔** | water-district explainer (bank) |
| Ramona | ✅ | FAIR Plan · ADU separate-sale · **insurance-before-offer ✔** | quarterly refresh pass |
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
| Rancho Santa Fe | ✅ | — deliberate gap | Guide already carries Covenant/Art-Jury/septic blocks; a post would cannibalize. Holds pending the client's keep-or-drop call (HANDOFF §9) |
| **Temecula** *(added 2026-07-30)* | ✅ new | pulse (county-level context) | Wine Country jurisdiction post (bank); Riverside listening added to the monthly pass; photography |
| **Murrieta** *(added 2026-07-30)* | ✅ new | pulse · **Gierson Ranch CFD formation reflected in guide (formed June 2026, $8M authorized)** | track first bond issuance (fast lane); photography |
| **Menifee** *(added 2026-07-30)* | ✅ new | pulse | EMWD/CFD new-construction explainer variant (bank); photography |

**Riverside note:** the three corridor guides cite city-published district records (the SD Auditor's list doesn't reach Riverside County), publish no volume claims (no Compass record there), and ship on designed plate heroes until a photography pass — same §5-of-HANDOFF verification method when it runs. Add `Temecula Murrieta Menifee` phrasings to the monthly listening sweeps and the AI query panel.

**Southern expansion (2026-07-30, twelve areas):** La Jolla, Pacific Beach, Ocean Beach, Hillcrest, North Park, Downtown, College Area + Chula Vista, Santee, El Cajon, Spring Valley, Lemon Grove — all guides live, all served today by the market pulse plus their own live-fact blocks. Post bank seeded by the guides themselves: **STRO license explainer** (PB/OB/Mission Beach tiers — high-intent, no local competitor answers it with the actual caps), **La Jolla cityhood tracker** (update-in-place per LAFCO milestone, same pattern as Del Mar bluff/rail), **Hillcrest plan amendment owner explainer**, **Chula Vista east/west total-monthly comparison**, **Fanita Ranch tracker**. Add all twelve to listening sweeps and the AI panel; photography pass covers all fifteen new areas together.

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
