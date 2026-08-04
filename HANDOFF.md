# Team Azizi — Handoff & Decision Log

**Client:** Team Azizi (Compass) · San Diego · **CitedRealty customer #1**
**Domain:** teamazizi.com — registrar controlled by Jon; **DNS not yet pointed** · **Host:** Vercel
**Repo:** [github.com/jonathandkennedy/teamzizi](https://github.com/jonathandkennedy/teamzizi) — note the missing "a" in the repo name; the domain is team**a**zizi.com
**Live preview:** https://teamazizi.vercel.app
**Strategy doc:** [GAMEPLAN.md](GAMEPLAN.md) — that file is *the plan*; this file is *state, decisions, and why*.
**Last updated:** 2026-07-30

---

## 0. Read this first

Two things will waste your time if you don't know them.

**One: the farm in the plan is not the farm in the record.** GAMEPLAN is built on six affluent north-coastal communities. A full sweep of all 1,009 Compass sales found only 45 of them (4.5%) in those six, a median sale price of $650,000, and exactly one lifetime sale in Rancho Santa Fe. The real book is Escondido (~96 sales, the single largest market), South Bay, Spring Valley, Fallbrook, Oceanside, Santee, El Cajon. See [research/salesRecord.md](research/salesRecord.md). The site now covers **thirty-one** areas rather than six, which is the resolution: the original six are kept because the client asked for them; ten North County communities were added because that is where the transactions are; twelve more — seven City of San Diego neighborhoods plus Santee, El Cajon, Spring Valley, Lemon Grove and Chula Vista — went in 2026-07-30 at client request, finally covering the East County/South Bay markets the record names; and three Southwest Riverside cities (Temecula, Murrieta, Menifee) extend up the I-15 (§2 records how a second county is handled honestly). The unanswered client question is which set gets the marketing spend.

**Two: there is exactly one launch blocker.** `site.LEAD_ENDPOINT` is still `https://formspree.io/f/PLACEHOLDER`. Every lead form on the site posts into nothing. `build/validate.py` fails the build on it deliberately, and that single failure is the "1 error" you will see on every validate run. Nothing else is blocking DNS.

---

## 1. Status as of 2026-07-26

| | |
|---|---|
| **Research** | ✅ Complete (9-agent workflow, ~684k tokens) — `research/` |
| **Strategy** | ✅ Complete — `GAMEPLAN.md` |
| **AI baseline** | ✅ Captured — absent from 14/14 tested queries — `research/aiBaseline.md` |
| **Site** | ✅ **71 pages** built and deployed to the Vercel preview |
| **Neighborhood guides** | ✅ **31 areas** — the 16 San Diego originals (16,107 words, measured 2026-07-26), plus 2026-07-30: seven city neighborhoods, five East County/South Bay communities, three Riverside corridor cities |
| **Agent pages** | ✅ 19, all with headshots; 18 of 19 carry a review CTA |
| **Photography** | ✅ **16 of 31** areas have a real photograph; 12 are third-party with rendered credits. The fifteen 2026-07-30 additions ship on designed plate heroes — photography pass pending |
| **Validation** | ✅ 0 errors other than the deliberate `LEAD_ENDPOINT` blocker |
| **DNS** | ❌ Not pointed. This is the last step, not the first — see [docs/launch-runbook.md](docs/launch-runbook.md) |
| **GBP** | ❌ Does not exist. Phase 2, and it needs the client to receive the postcard |
| **Repo visibility** | ⚠️ Still public. No API for this — GitHub Settings → General → Danger Zone |

### The 71 pages

```
/                                  home
/neighborhoods                     hub
/neighborhoods/{31}                the product — see §4
/team                              grouped by area, not a flat grid of 19 faces
/agent/{19}                        one per licensee
/home-valuation                    two-step lead magnet
/mello-roos                        2,671 words — the deepest single asset on the site
/blog  +  /blog/{7}                journal — calendar in docs/content-runbook.md §4
/sell  /buy  /concierge            service pages
/join                              careers — see §2, and what it refuses to publish
/contact  /thank-you  /404
/properties/sale  /properties/sold 301 targets for ~10 indexed legacy listing URLs
```

---

## 2. Decision log — settled, do not re-litigate

### Foundational

| Decision | Why |
|---|---|
| **Static HTML/CSS/JS. No framework, no build step at deploy time.** Python generators for repeating page types; output committed to the repo | CitedRealty house style. Fastest Core Web Vitals; **schema server-rendered into the HTML** because AI fetchers and `curl` do not run JS; trivially portable so the client genuinely owns it; anyone can edit it with a text editor. |
| **Client owns everything** | Their last site vanished when the Luxury Presence relationship ended. That *is* the pitch — they lived the rented-SaaS failure mode. Never build them onto something they can lose again. |
| **Rebuild at the same URLs; 301 the rest** | ~10 old URLs are still indexed despite dead DNS. URL preservation is the cheapest SEO win available and the window closes as the index decays. |
| **Content foundation completes before DNS points** (client, 2026-07-30) | The client's sequencing call: crawlers meet a finished, deep site on first fetch rather than a thin one assembling in public. The accepted cost — recorded, not hidden — is that the old index decays and the corrupted brand answers stand while we build, which is why the foundation gate is a finishable checklist (docs/content-runbook.md §6.1), not an open-ended standard. GBP, reviews and entity cleanup run in parallel, not after. |
| **Twelve southern areas added: La Jolla, Pacific Beach, Ocean Beach, Hillcrest, North Park, Downtown, College Area + Santee, El Cajon, Spring Valley, Lemon Grove, Chula Vista** (client, 2026-07-30) | Southward to where the record lives — salesRecord.md names Spring Valley, South Bay, Santee and El Cajon as actual top markets the original farm ignored. The county CFD list was re-read in full: Chula Vista's east side is the densest CFD concentration in it (city + elementary + high-school layers on one bill), Santee and Lemon Grove appear once each (Lemon Grove's is commercial-corridor — the custom lead says so), and the seven city neighborhoods plus El Cajon and Spring Valley are verified absences. Live regulatory facts (STRO tiers, the 2024 Hillcrest plan amendment, La Jolla's LAFCO cityhood timeline, Fanita Ranch) verified before writing. Counts stay unpublished pending the export. Homepage/hub coverage copy updated to countywide; the homepage *title* (North San Diego / Carmel Valley positioning) deliberately untouched — repositioning the brand keyword is a client decision, flagged. |
| **Three Southwest Riverside cities added: Temecula, Murrieta, Menifee** (client, 2026-07-30) | Client-directed expansion up the I-15 — where many North County searches end when budget meets map, with Fallbrook as the geographic hinge. A different county, handled honestly: taxes.py entries carry their own city-published sources (the SD Auditor's list says nothing about Riverside), `areaServed` names them "{City}, California" rather than folding them into San Diego, and the Compass record has no sales there so the pages publish structural facts and no volume claims. Photography pass pending — designed plate heroes until then. |
| **URLs carry no trailing slash** — `/neighborhoods/carmel-valley` served from `neighborhoods/carmel-valley.html` via Vercel `cleanUrls` | Exactly how the old site served them. GAMEPLAN §4.4 writes them with a trailing slash; that was a drafting slip. A trailing-slash convention would 301 away the very equity we are rebuilding to keep. |
| **Keep the brand, modernize the bones** | Black/white system, Reem Kufi Fun + Lato, square 2px ghost buttons, gold `#8D7120`/`#CCB091`, video hero. This IS the brand and returning clients should recognise it. Modernize *execution* — fluid type, CSS grid, lighter motion — not identity. |
| **Fonts self-hosted** (Reem Kufi Fun 400, Lato 400/700, both SIL OFL, 84 KB) | Removes a render-blocking third-party request and a dependency the client cannot control, which is the premise of the whole rebuild. |
| **Reem Kufi Fun's colour layer remapped to brand gold** | It is a COLRv1 colour font: the tittles on i/j are small **red hearts**. Red appears nowhere else in the brand and fights the gold. Remapping the `@font-palette-values` keeps the letterforms and the detail while resolving the clash. One CSS block to delete if the client wants stock red back. |
| **NO IDX at launch.** `/home-search/*` → 301 | Fails CitedRealty's own published need-test: a listing-focused team's sellers don't hire them for a search widget, and buyers use Zillow regardless. Costs $50–100+/mo plus MLS fees, adds a vendor whose URLs die on exit, and risks the broken-widget trust failures visible on competitor sites (Whissel's $0 medians, Kolker's "No results found"). Their **own** listings need no IDX licence — generator plus weekly refresh. Revisit only if the team commits to a real buyer nurture pipeline; then noindexed, on their own domain. |
| **robots.txt names the AI crawlers explicitly and allows all of them** | Retrieval bots (OAI-SearchBot, ChatGPT-User, PerplexityBot, Claude-SearchBot, Google-Extended) are what fetch a page in order to cite it — blocking any forfeits the engagement. Training bots (GPTBot, ClaudeBot, Applebot-Extended) are also allowed: for a business whose problem is that models do not know it exists, being in the training data is upside. Reversible client call. |
| **IndexNow at launch** (key `ce855552…`, `build/indexnow.py`) | ChatGPT retrieval leans on Bing's index. Bing/Yandex/Seznam/Naver only — **Google does not participate**. Honest framing for the client: it accelerates discovery; it does not cause ranking or citation. Will 422 until DNS points at Vercel and the key file is reachable. |

### Schema and content architecture

| Decision | Why |
|---|---|
| **No JSON-LD is ever hand-written.** Every block is a Python dict serialised with `json.dumps`; `validate.py` re-parses all of it pre-push | Makes the missing-brace failure that broke CitedRealty's homepage graph structurally impossible rather than merely unlikely. |
| **The full entity graph repeats on every page** rather than being defined once and referenced | An AI fetcher may only ever see one page. Each page has to stand alone as a complete statement of the entity. The validator flags one `@id` describing *different* things, which is the real error the schema skill warns about. |
| **`sameAs` lists only profiles that are accurate today.** LinkedIn, Yelp and the YouTube channel sit in `SAME_AS_PENDING` with per-item reasons | A `sameAs` pointing at a profile carrying "Upstart Real Estate" or the old (619) number tells the knowledge graph that the wrong data is authoritative. They get promoted as Phase 2 fixes them. |
| **Neighborhood pages are built as fan-out answer blocks, not narrative** | AI Mode decomposes a query into sub-queries and retrieves *passages*, not pages. A flowing page competes for one head term; the same content in self-contained blocks competes for ~19 retrievals. Map in `build/data/fanout.py`. |
| **Every lead answer must survive being lifted out of the page.** `validate.py` rejects any answer opening with a bare pronoun or omitting the place name | A passage that reads "It has no Mello-Roos" is useless once separated from its heading, which is exactly what retrieval does to it. |
| **`FAQPage` schema is derived from the visible passages, never authored separately** | Two sources of truth drift, and a mismatch between schema and rendered text is a structured-data violation. `faq_from_blocks()` extracts from the built HTML, so they cannot disagree. Rich results for FAQ were dropped in 2026 — this is for AI parsing, and the client should be told that plainly rather than sold a rich-result promise. |
| **Neighborhood market data comes from public primary sources**, cited and dated: County Auditor CFD reports for Mello-Roos, district boundary maps for schools | No client dependency, fully defensible under no-fabrication, and the Mello-Roos and school-boundary data *is* the moat — not one competitor page publishes it. Revisit if the client grants MLS access. |
| **Hand-craft, don't scale by template** | The May 2026 core update explicitly demotes name-swapped geo templates. Sixteen pages sharing a generator but not sharing prose; each carries community-specific district, CFD and boundary facts that had to be looked up individually. |
| **Primary tracking keyword: "carmel valley san diego real estate agent"** | Sits at their physical office (92130) so it is geogrid-trackable and proximity-favoured; decisive agent-selection intent; genuinely winnable, unlike portal-locked "homes for sale" or RSF head terms owned by Barry Estates and Brizolis Janzen. |
| **`/join` publishes only checkable recruiting claims, and says out loud what it withholds** | Added 2026-08-04 at client request, modelled on a supplied mockup. The genre runs on unfalsifiable promises ("we invest in your future"), and the reader is a licensee deciding where to move a licence. So the four value columns carry the RealTrends and SDBJ placements, the published production figures, the brokerage and its DRE number, and the marketing surface that can be read on this domain before anyone applies. **Splits, caps, desk fees, lead volume, training and benefits are not published** — none are in the record this site was built from, and inventing them to fill the template is the exact failure `check_unverified` exists to prevent. The `#terms` block states that and tells the applicant to get all of it in writing from any team, this one included. If the client wants those terms published, they supply them and they become facts like any other. |
| **`/join` names the three real openings; `JobPosting` schema still waits on details** | Client confirmed 2026-08-04 that the roles are real: **licensed agents, social media marketing, paid advertising.** All three are named on the page. The schema is a separate question: `JobPosting` expects employment type, location and — under California SB 1162 — a pay scale in the posting itself once an employer crosses 15 employees. Agent roles are typically independent-contractor, which changes that analysis and is not something to guess at. Marking up a posting with invented terms feeds Google Jobs directly, which makes it worse than the same invention in prose. Details in §9; the page ships as `WebPage` + `FAQPage` until they arrive. |
| **Earned mentions only — never bought** | Google's May 2026 AI-search guide makes buying citations to influence AI results a stated spam risk. Also CitedRealty's compliance line, and it has to survive contact with the Scripps Ranch competitor who *is* using paid press releases. Legit PR announcing real RealTrends results is fine; paid "AI mention" packages are not. |

### People, authorship and attribution

| Decision | Why |
|---|---|
| **Neighborhood-first IA: one named licensee owns each area** | A page authored by "Team Azizi" is a company talking. A page authored by a named licensee with a DRE number, a direct line and a sold record in that neighborhood is a person who can be checked — which is what E-E-A-T rewards and what an assistant needs before it will name someone. `/team` groups by area because "who do I call about Del Sur" is the question visitors arrive with. |
| **Farming assignments are client data; the system ships with confirmable slots** | Nothing published anywhere says which agent works which community. Proposals in `agents.PROPOSED_ASSIGNMENTS` are now evidence-based (drawn from the sales sweep), but only **Del Mar → Michael Angotta** is marked confirmed. Everything else falls back to a real, accountable licensee rather than a company byline. |
| **Bylines rotate across the three Azizi licensees, weighted to Sofia** | `agents.BYLINE_POOL` is 6 Sofia / 2 Nilab / 2 Zohra, selected by a SHA-256 hash of the page slug so it is deterministic and stable across builds. Client instruction was "most should default to Sofia but do a mix." Nineteen pages all bylined to one person reads as a single-author site pretending to be a team. |
| **The byline rotation forced two corrections.** `expert_block` used to say "Team lead · covering X" — factually wrong for Sofia and Zohra, i.e. on two-thirds of guides. `/team` separately disagreed with the guides about who covers what | Both fixed. Worth knowing because it is the failure mode of any change that touches authorship: the byline is asserted in three places and they must agree. |
| **Every agent page carries "Review me on Zillow" with that agent's own profile link** | Client instruction. 15 of 19 have Zillow URLs, 1 has realtor.com (Tiffney), 1 is explicitly marked `no_review_profile` (Candice — Compass profile only), and the remainder fall back to team-level. Review velocity is the single highest-leverage local ranking factor available and it costs nothing to ask. |
| **No `Review` or `aggregateRating` schema anywhere on the site** | Verified against Google's structured-data policy rather than recalled: *"Don't aggregate reviews or ratings from other websites."* Zillow reviews are Zillow's. Self-collected reviews are also ineligible for the star feature. Testimonials will render as plain text with attribution, carrying no review markup. `build/data/testimonials.py` is deliberately empty pending client-supplied, permissioned quotes. |
| **Sonia Azizi's profiles are not used** | Founder, died July 6, 2023. Most review equity is stranded on her profiles and the temptation to use it is real. Client decided against; recorded in `site.NOT_USING`. **Do not delete or quietly rewrite anything of hers.** Honour her on `/about` when that page exists. Any future decision here routes through the client and the family. |
| **Nilab's "0 sales" is an attribution gap, not a real zero** | 779 of 1,009 sales are attributed to a named agent; the rest are not. The team lead showing zero would be worse than showing nothing. `agent_record_block()` handles three cases explicitly and publishes no number rather than a false one. |

### Photography — the longest-running thread in this project

| Decision | Why |
|---|---|
| **No generated imagery of real named places** | A synthetic photo of a real community cuts against the no-fabrication doctrine the whole strategy rests on. Generated art is fine for abstract section bands (`build/textures.py` generates four, with explicit prompt bans on buildings, landscapes and photorealism) and for typographic OG cards (`build/og.py`, 20 of them). |
| **Compass listing photography was rejected as a source** | Three independent reasons, checked rather than assumed: the images carry a "SAN DIEGO \| MLS" watermark and are MLS-licensed rather than the team's own; the agent pages expose no reliable image-to-city mapping, so picking one per neighborhood would be guesswork; and they are interiors. An empty bedroom is not a picture of Escondido. |
| **Wikimedia Commons and Openverse, with every image verified by a human before install** | Commons gives a licence, an author, a description and often coordinates — everything needed to publish a photograph honestly. Openverse adds Flickr, where people who actually live somewhere post pictures of it, plus US government accounts whose work is public domain. |
| **Non-commercial and no-derivatives licences excluded at the query, not filtered afterwards** | This is a commercial site and a hero has to be cropped. A crop of a share-alike image is an adaptation and inherits the licence. |
| **Every borrowed photo renders its attribution on the page, and now also states what was changed** | CC BY and CC BY-SA both require indicating that modifications were made, not merely naming the author. Eleven credits read "Cropped to fit" — cropping to a 16:10 hero is itself a change — and Valley Center reads "Cropped to fit; colour and contrast adjusted." |
| **Search the DISAMBIGUATED name, and trust the Commons category over the description** | This is the method that actually worked, and it should have been step one. See §5 for the full sequence and the three wrong-place near-misses it caught. |
| **Tonal grading yes, generative "enhancement" no** | Levels, contrast, saturation and unsharp mask apply a response curve to pixels already in the frame, which is what a darkroom print does. Re-rendering pixels invents detail that is not in a neighborhood a buyer may move to — the same category of error as the Monterey County vineyard, just harder to spot — and it would make a "Photograph by ‹author›" credit false. |
| **A third-party real estate site's photo was declined** | The client offered a Valley Center image hosted on a competing San Diego agent's site: uncredited, unlicensed, and served behind a captcha wall on direct fetch. Copying it would be infringement with the shortest possible path to a complaint, because the injured party is a competitor who would notice. Options given instead: trace and licence the original, commission a shoot, or keep the CC image. |

---

## 3. Canonical data block — reuse these exact strings everywhere

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

Single source of truth: `build/data/site.py`. Never retype these anywhere else.

**These must match GBP exactly** once GBP exists — schema, footer NAP and GBP are one entity or they are three.

**Phone is now a call-tracking number: (858) 201-2899** (client-supplied 2026-08-03). It replaced the main line *and* all nineteen agent direct lines, so every inbound call from the site is measurable. Two consequences that are the client's to close:
1. **Set this same number on GBP at creation**, and on Compass/Zillow/social profiles as the cleanup sweep reaches them. A tracking number on the site while GBP shows the old (858) 847-8067 is precisely the split-entity failure this section exists to prevent — worse than not tracking at all, because it splits the signal *and* measures nothing.
2. **Routing:** nineteen licensees' "call me" links now resolve to one line. If "call this agent" is still meant to reach that agent, the tracking provider has to route or forward per destination. The agents' original direct numbers are not recoverable from the repo — they were replaced, deliberately, and would have to be re-supplied.

**Strings to purge wherever found** (`validate.check_stale_strings` enforces this): `10550 Craftsman Way`, `11682 El Camino Real`, `(619) 929-9691`, `sonia@teamazizi.com`, `Upstart Residential`, `Upstart Real Estate`, DRE `01426453`, and the "45 Ranch" typo.

**Recommended canonical name: "Team Azizi"**, long form "Team Azizi Real Estate | Compass San Diego". Matches Compass and RealTrends; the long form disambiguates from **Azizi Developments (Dubai)**, which pollutes generic "Azizi real estate" results. Still pending client confirmation — the validator warns — but everything ships with one string so a change is one edit.

**Proof points, all third-party verifiable.** Use these, not the old site's "$90M+ 2024":
$105.59M volume / 92 sides (RealTrends Verified, 2026 program reporting 2025 production) · **#58 of all California large teams by volume** · #265 nationally · 1,016 closed sales + 43 rentals (Compass) · actives $369K–$5.875M · solds to $6.1M · 7 units at 6710 La Jolla Blvd = whole-building development representation.

Cite both years or a reader who clicks through thinks the number is stale.

**Two claims were pulled from the site** because the record does not support them:
- "#1 in Del Mar by sides" — RealTrends ranks within an assigned business city; theirs is Del Mar; they have six Del Mar sales in the entire Compass record. Almost certainly an artifact of registration rather than market share, and a reader will infer market share.
- "Top 1% in San Diego County" — no published denominator, no source, and it is the identical string their most direct competitor already uses. The RealTrends line is stronger precisely because a reader can click it.

---

## 4. The neighborhood guides — the product

Thirty-one areas. The sixteen San Diego originals measured 16,107 words (2026-07-26), 867–1,204 words each, 10–13 answer blocks each; the fifteen 2026-07-30 additions — seven city neighborhoods, five East County/South Bay communities, three Riverside corridor cities — follow the same template, with the county CFD list re-read in full and city-published sources where Riverside governs.

**The original six** (from GAMEPLAN, ordered by winnability rather than prestige): Del Sur, 4S Ranch, Scripps Ranch, Carmel Valley, Del Mar, Rancho Santa Fe.

**Ten North County communities** added at client request, ordered by transaction volume in the actual record: Escondido, Oceanside, Fallbrook, San Marcos, Carlsbad, Vista, Poway, Encinitas, Valley Center, Ramona.

Every guide answers, per community, the things that are genuinely hard to look up:

- **Which Community Facilities District applies, and what it costs** — from County Auditor CFD reports, the primary source. `build/data/taxes.py`.
- **Which school district assigns, and how to check a specific address** — districts, not ratings. `/blog/san-diego-school-district-by-address` carries the method in 1,212 words because it did not belong inside a single guide.
- **Which county land-use rules bite** — septic, wells, minimum lot size, agricultural zoning. This is what separates Ramona and Valley Center from Carmel Valley in practice.

**Governing content rules**, documented in the `build/data/guides.py` docstring:

- Structural facts only. Which district, which boundary, which agency.
- **No prices, no medians, no school ratings.** They rot, and a stale median on a real estate site is worse than no median.
- **Fair Housing: places and processes, never people.** Describe verifiable facts — tax structure, attendance boundaries, commute times, HOA rules. Never "good neighborhood," "safe," "family-friendly," or demographic desirability. The old Luxury Presence pages embedded Census demographic widgets; do not reproduce that pattern as editorial. When answering "is X a good place to live," answer with facts and tradeoffs.

---

## 5. Photography — what was tried, in order, and what it cost

This took four passes and is written down because the failure mode is expensive and non-obvious.

**The failure being guarded against is specific and already happened:** the old Luxury Presence site published a photograph of Carmel Valley, **Monterey County** on the Carmel Valley, San Diego page — four hundred miles from the neighborhood it was selling.

| Pass | Method | Result |
|---|---|---|
| 1 | Commons text search on `"<Name>, California"` | 6 areas. Would have shipped **three wrong places** if the captions had not been read: "Vista, California" returns the State Capitol in Sacramento; "Carmel Valley, California" returns Monterey County; "Valley Center, California" returns Fountain Valley and Napa. |
| 2 | Commons **geosearch** by community centroid (`commons.near()`) | 3 more. Structurally immune to the same-name trap — a file 400 miles away is not within a 6 km radius — but only as good as the geotags, and **Fallbrook's are wrong**: every hit is San Luis Rey Mission Church, which is in Oceanside. |
| 3 | **Openverse** (`build/openverse.py`) | 1 more (Encinitas). Indexes Flickr and US government accounts. |
| 4 | Commons text search on the **disambiguated** name | The last 5. `"Carmel Valley San Diego"`, not `"Carmel Valley, California"`. `"4S Ranch"`, not `"4S Ranch, California"`. |

**The lesson, now in `photos.py`:** Commons keeps a **category per community** — `Carmel Valley, San Diego`, `4S Ranch, California`, `Geography of Fallbrook, California`. A file carrying that category was filed by a human who knew which place they meant. **The category is the strongest signal available and the cheapest to check.** Prefer it over description text, which is often just the filename again. This should have been pass one.

**Valley Center needed a different question entirely.** Its one plausible file carries **both** `Valley Center, California` and `Laguna Mountains (California)` — two places fifty kilometres apart, with no coordinates to break the tie. I rejected it on that basis, and that was over-cautious. What settled it was asking not *what does the file claim* but *who relies on it*: it is the lead image on the Valley Center, California article across **27 Wikipedias**, bound to **Wikidata Q2861838**, and in 2020 an editor deliberately recategorised it *to* Valley Center, removing the broader county and CDP categories by hand. **Usage is a stronger signal than metadata, because metadata is one uploader and usage is many editors with something to lose.**

**Rejected during review**, so you know the bar: an upside-down Carmel Valley file; a USDA Fallbrook frame that is a portrait of a named farmer rather than a picture of the place; a Fallbrook crop that landed on bare ground instead of the grove.

**Held 2026-08-04 — the two images supplied with the careers-page request, and a misidentification worth recording.** The client sent a finished "Join Our Team" landing-page mockup and a cut-out group shot of four women in cream suits as the reference for `/join`. The layout was used; the images are **held pending one answer from the client**, and the reasoning got corrected mid-task:

- **What I got wrong.** I compared the four faces against the nineteen recovered headshots and concluded none was on the roster. **The client says they are Masooma, Nilab, Zohra and Sofia** — and the client knows their own family. Recorded bluntly because the lesson generalises: *do not identify people from photographs.* It is a judgement this project has no business making unilaterally when the client can answer it in one line. The same instinct that is correct for a landscape — "verify before you publish" — becomes recognition, which is a different and much less reliable act.
- **What is still unresolved, and is the actual question.** The mockup carries the branding **"TEAM AZIZI INJURY LAWYERS"** — wrong business entirely for a Compass real estate team — and the cut-out has the surface qualities of a generated or heavily processed image. The most likely explanation is that the mockup was produced with an AI design tool that hallucinated the tagline, in which case the underlying photograph may be perfectly real. **Ask the client which it is before publishing either image:** a real shoot of the four of them (usable, and better than what is on the page now), a real photo run through generative editing (judgement call), or generated imagery (not usable, per this section).
- **Why the branding still matters even if the photo is real.** Nothing carrying "Injury Lawyers" can ship as-is. If the client wants that mockup's exact composition, it needs regenerating without the wrong-industry text.

`/join` ships in the meantime on `team-group.jpg` — the real thirteen-person photograph already used on the homepage — which is defensible under every branch of the question above. A portrait-format recruiting hero remains a shot-list item for the commissioned pass in [docs/photography-brief.md](docs/photography-brief.md).

**Current state: 16 of 16.**

- **4 from the recovered Luxury Presence asset set** — Del Mar, Del Sur, Rancho Santa Fe, Scripps Ranch. No credit needed; these came with the brand.
- **12 third-party, all credited on the page** — 10 under CC BY or CC BY-SA, 2 public domain (4S Ranch, San Marcos).

`photos.REJECTED` is now empty but stays in the file, with a note explaining what it is for: when a search returns nothing verifiable, record the reason rather than leaving the slot silently blank. The risk in a repeat search is not finding nothing again — it is someone less careful installing the wrong place.

**The upgrade path is commissioned photography.** Twelve credit lines are a visible tell that the photography is not the team's, and the ten share-alike ones carry an obligation that follows every future crop. A commissioned pass removes all of it at once. Shot lists are in [docs/photography-brief.md](docs/photography-brief.md).

---

## 6. Build system

```
build/
├── data/                  ← all content and facts live here, nowhere else
│   ├── site.py            THE canonical strings: NAP, proof points, services,
│   │                      sameAs, the 16 areas, footer link sets
│   ├── agents.py          19-agent roster, DRE numbers, review profiles,
│   │                      farming assignments, BYLINE_POOL, author_for()
│   ├── guides.py          per-community answer blocks for all 16 areas
│   ├── taxes.py           CFD / Mello-Roos data from County Auditor reports
│   ├── fanout.py          the query-decomposition map the guides are built against
│   ├── photos.py          third-party photo provenance + the REJECTED record
│   ├── posts.py           journal entries
│   └── testimonials.py    deliberately empty — see §2
├── schema.py              JSON-LD builders (dicts → json.dumps, never strings)
├── components.py          <head>, nav, footer, page shell, picture()
├── generate.py            writes site/ — one build_* function per page type
├── validate.py            PRE-PUSH GATE — 11 checks, see below
├── optimize.py            image caps, WebP, narrow renditions, hash manifest
├── og.py                  20 typographic Open Graph cards
├── textures.py            4 abstract section-band textures (gpt-image-2)
├── commons.py             Wikimedia candidate finder — installs nothing
├── openverse.py           Openverse candidate finder — installs nothing
├── indexnow.py            ping Bing/Yandex/Seznam/Naver at launch
└── fetch_fonts.py         one-shot: self-hosts the webfonts
```

### The workflow

```bash
python3 build/generate.py     # writes all 50 HTML pages + sitemap, robots, IndexNow key
python3 build/optimize.py     # idempotent; safe to run every time
python3 build/validate.py     # MUST pass before every commit
```

`generate.py` prints "48 page(s) written". That counter is the sitemap list, and `/404` and `/thank-you` are deliberately kept out of the sitemap — a 404 page and a form-confirmation page have no business being submitted for indexing. All 50 HTML files are generated; nothing in `site/` is hand-maintained.

Expect `1 error` from `validate.py` until `LEAD_ENDPOINT` is set. That is by design — see §0.

### `validate.py` — the 11 checks, and what each one is preventing

| Check | Prevents |
|---|---|
| `check_jsonld` | The missing brace that made CitedRealty's entire homepage graph unparsable and got flagged in GSC within hours |
| `check_answer_blocks` | Passages that die when lifted out of the page — bare-pronoun openers, missing place names, backreferences, over-short answers |
| `check_lead_forms` | A form with no TCPA consent language, or one pointing at the placeholder endpoint |
| `check_stale_strings` | The old address, the old phone, "Upstart", the wrong DRE, the "45 Ranch" typo |
| `check_internal_links` | Orphans and dead internal links |
| `check_sitemap` | Malformed XML, and URLs in the sitemap that do not exist on disk |
| `check_unverified` | Publishing a claim the record does not support; emits warnings for the pending canonical name and the withheld `sameAs` entries |
| `check_faq_matches_visible` | `FAQPage` schema drifting from the rendered text — a structured-data violation |
| `check_headings` | Skipped heading levels (this caught 17 pages) |
| `check_testimonials` | Any `Review` or `aggregateRating` markup sneaking in |
| `check_footer_licensees` | The footer licence block losing a named licensee |

### `optimize.py` — read this before touching an image

Caps by role, doubled for retina: backgrounds 1920, neighborhoods 1280, textures 1600, team 800. Logos and compliance marks are left alone. WebP is written *alongside* the JPEG, and `components.picture()` emits the WebP first with the JPEG as fallback.

**Idempotency is enforced by a content-hash manifest** at `site/assets/img/.optimized.json`, committed alongside the images. Two mechanisms were tried first and both were worse than the bug they fixed:

- **mtime comparison** — git writes files at checkout time in arbitrary order, so on a fresh clone half the derivatives look older than their sources and the whole tree re-encodes. Caught when it dirtied 30 unrelated headshots.
- **Requiring the `-800` rendition unconditionally** — the team headshots cap at exactly 800, and the narrow rendition is only written when a source is *wider* than 800. Demanding a file that correctly never exists made all twenty headshots re-encode on every run, forever. That condition now lives in `derived_for()` alone so the two checks cannot drift.

**The bug the manifest exists to catch:** replacing a source JPEG in place used to leave the old `.webp` beside it. Because `picture()` emits WebP first, **every browser that can read WebP got the stale frame** while the JPEG fallback nobody looks at was correct. Silent, and invisible in the markup.

`seed_manifest()` adopts already-correct files without re-encoding them, so introducing the manifest cost no lossy generation and no binary diff.

---

## 7. Vercel

**These settings are the answer to "it's not pulling for the teamzizi repo."**

| Setting | Value |
|---|---|
| Framework Preset | **Other** — not Next.js. There is no framework and no build step. |
| Root Directory | **blank** |
| Output Directory | **`site`** |
| Build Command | **empty** |
| Install Command | **empty** |

`vercel.json` at the repo root carries `cleanUrls: true`, `trailingSlash: false`, the 301 map, and cache plus security headers (HSTS with preload, nosniff, SAMEORIGIN, strict-origin-when-cross-origin). Fonts get a one-year immutable cache; css/js/img get a week with `stale-while-revalidate`.

**The preview URL sits behind Vercel deployment protection.** `curl -L` against it returns the login page with HTTP 200, which looks exactly like success. I claimed "all 200, preview is fine" once on that basis and it was wrong. Check for `Authentication Required` or `vercel.com/sso` in the body before believing any preview measurement.

---

## 8. Compliance and sensitivities — real estate is not generic marketing

- **Fair Housing.** Content must not steer. Describe verifiable facts: prices, days on market, tax structure, school **attendance boundaries**, commute times, amenities, HOA rules. Avoid framing that signals protected classes — "good/safe neighborhood," "family-friendly," religious or ethnic character, demographic desirability. The old LP pages embedded Census demographic widgets; do not reproduce that as editorial.
- **No fabrication, ever.** No invented stats, testimonials or `aggregateRating`. Every claim traces to Compass, RealTrends, MLS, or a named source. Languages spoken stay unclaimed until the client confirms.
- **Reviews.** Google's structured-data policy: *"Don't aggregate reviews or ratings from other websites."* No review markup anywhere. See §2.
- **TCPA.** Consent language on every lead form. The old site had it; `check_lead_forms` makes losing it a build failure.
- **California DRE.** Nilab's licence number and the Compass brokerage DRE in the sitewide footer, as on the old site. Keep the Compass equal-housing and MLS disclaimers.
- **MLS data use.** Aggregate stats (medians, DOM, counts) are generally fine and are what makes pages citable. Confirm SDMLS rules before displaying individual listing data — that is where IDX licensing bites.
- **Sonia.** Sensitivity over speed on anything touching her profiles. See §2.

---

## 9. Open items

### Blocking launch

- [ ] **`site.LEAD_ENDPOINT`** — Formspree ID (watch the ~50/mo free cap) or the client's CRM webhook. This is the only true blocker.

### Client-dependent

- [ ] **⚠️ Which farm gets the spend?** 45 of 1,009 sales are in the original six. The real book is Escondido, South Bay, Spring Valley, Fallbrook, Oceanside. The site now covers both sets; the marketing decision is still open. [research/salesRecord.md](research/salesRecord.md) §1.
- [ ] **Rancho Santa Fe: keep or drop?** One lifetime sale, hardest SERP in the county. An expert page there fails the plan's own webspam test.
- [ ] **Confirm 15 of the 16 farming assignments.** Only Del Mar → Angotta is confirmed. Pre-written in `agents.PROPOSED_ASSIGNMENTS`. Also: can Del Sur be split from 4S Ranch? ZIP 92127 covers both plus Rancho Bernardo and Santaluz, so any split needs street-level data.
- [ ] **Per-area sales counts for the nine North County communities** — needed to publish a record block on those guides.
- [ ] **Testimonials** — permissioned quotes with attribution. Pipeline is built and empty.
- [ ] **Coby Herzog roster status.** Deanna Colby resolved; Coby still open. Their `/agent/` URLs are indexed and need a deliberate 301 either way.
- [ ] **Confirm the canonical name string** — validator warns until then.
- [ ] **Nicholas Miele's YouTube channel** (@lifeinsandiego, 12.4K subs, 205 videos, ~weekly). The only real on-location neighborhood video in the estate, in the team's link-in-bio, but owned personally. Highest-reach asset they have and it is not theirs. Licensing arrangement?
- [ ] **@soniasellssd — 9,412 followers**, still live, bio "Founder of Team Azizi". Four and a half times the team account. Family decision, not an SEO one. A team-level Zillow profile under her name also surfaced and conflicts with `site.NOT_USING`.
- [ ] **The other three Instagram link-in-bio URLs.** The visible one is `teamazizi.com/home-valuation` — which is why that page was launch-critical rather than a Phase 3 rebuild. The other three are almost certainly dead teamazizi.com paths.
- [ ] **Replace "Top 1% in SD County" in the Instagram bio** with the RealTrends line, so profile and site assert the same checkable thing.
- [ ] **`/join` — the terms the page deliberately does not publish.** Splits, caps, desk fees, lead flow, training and any benefits. Supply them and they can be published like any other fact; leave them unsupplied and the page keeps saying so, which is defensible but converts worse than a straight answer.
- [ ] **`/join` — the careers form's consent language needs counsel's eye.** It reuses `site.TCPA_CONSENT` verbatim, which authorises contact "about real estate services" — correct for buyer and seller enquiries, arguably not the right description for a recruiting conversation. It was not rewritten unilaterally because it is an approved legal string. Either counsel confirms it covers recruiting contact, or they supply a careers variant.
- [ ] **`/join` — details to turn the three confirmed roles into `JobPosting` markup.** Roles confirmed 2026-08-04 (agents · social media marketing · paid ads) and named on the page. Still needed per role: employment type (W-2 or independent contractor), on-site/hybrid/remote, and a **pay scale — which California SB 1162 requires in the posting itself for employers at 15+ employees.** Whether the team crosses that threshold depends on how the contractor licensees count, which is a question for the client's counsel, not for this repo. Get the answer before publishing comp either way.
- [ ] **`/join` — image provenance (blocking for the supplied photo).** Is the four-person cream-suit shot a real photograph of Masooma, Nilab, Zohra and Sofia, a real photo run through generative editing, or generated? See §5. The answer decides whether it can replace `team-group.jpg` on the page. The "Injury Lawyers" mockup cannot ship in any case.
- [ ] **Google Maps API key** (`site.GOOGLE_MAPS_KEY` is empty) — for the contact-page map.
- [ ] **Malcolm Schick's higher-resolution headshot** — current one is soft.
- [ ] **Privacy policy** — needed before launch for the forms.
- [ ] **GBP verification** — client must receive and complete the postcard. Nothing else in Phase 2 starts without it. **Use the tracking number (858) 201-2899 as the GBP phone** so site and profile assert one number (see the NAP block above).
- [ ] **Call-tracking routing** — confirm with the provider how the single tracked line reaches individual agents, since all nineteen agent pages now point at it.
- [ ] **Compass brokerage logo** from Compass's brand kit. The recovered file is the TA monogram, mislabelled.
- [ ] Founding year and lifetime volume (Yelp says 2010, housing.info says 2014).
- [ ] Languages spoken per agent — Dari/Farsi/Spanish plausible; strong E-E-A-T signal and an untapped keyword category. Never claim unconfirmed.
- [ ] Branded listing-prep program name, riding Compass Concierge.

### Ours

- [ ] **⚠️ `generate.py` restamps every page's date on every build.** `TODAY = date.today().isoformat()` at line 29 feeds the visible "Last updated" line, `dateModified` in the schema, and `<lastmod>` in the sitemap — at ~18 call sites. Running the generator with no content change therefore bumps the date on all 27 dated pages, which is a **false freshness signal**: it tells Google and any reader that a page was revised when it was not, on a site whose entire premise is that its claims can be checked. It also destroys the one thing the visible date is for, which is letting a buyer see that the Mello-Roos figure is current.

  Caught while committing a docs-only change that arrived with 27 pages of date churn attached. The churn was stripped from that commit; the generator was not fixed, because doing it properly is not a one-line change.

  **The fix, when it is done:** a page's date should change exactly when its content changes. Compare each freshly rendered page against the committed version with all date occurrences normalised to a placeholder; if the bodies are otherwise identical, keep the stored date, and if they differ, stamp today. Same shape as the `optimize.py` hash manifest in §6, and the sitemap `lastmod` should then read each page's own date rather than today's. Until this lands, **do not commit rebuilt HTML unless the content actually changed** — check `git diff` for pages whose only delta is the date, and restore them.

- [ ] **Make the repo private** — no API for this; GitHub Settings → General → Danger Zone.
- [ ] **Rotate the OpenAI API key.** It lives in a gitignored `.env` at mode 600 and is absent from every staged diff — verified — but it was exposed in a session transcript. Rotate it.
- [ ] **Point DNS at Vercel:** `A @ → 76.76.21.21`, `CNAME www → cname.vercel-dns.com`. Full sequence in [docs/launch-runbook.md](docs/launch-runbook.md).
- [ ] **Verify office geo coordinates** against the GBP pin once GBP exists. Currently approximate; `validate.py` warns. Schema and GBP must agree exactly.
- [ ] Submit to GSC and Bing Webmaster at launch; request re-indexing of the preserved URLs.
- [ ] Run `python3 build/indexnow.py` at launch and after every content deploy.
- [ ] Ask the client for rights to their own listing photography — 1,016 sales' worth, and the fastest route to owned imagery even after the Compass-photos rejection in §2, because *permissioned* use is a different question from scraping.
- [ ] Find the owner of `greatersandiegohouses.com` staging site (broken `*.testintegration.com` SSL, indexed) → fix or noindex.
- [ ] **Case-study log: screenshot the corrupted AI answers now**, before they are fixed. The zero-visibility "before" is the entire value of customer #1.

---

## 10. How to do common tasks

**Add or edit a neighborhood guide.** Write the semantic brief first (`research/contentPlaybook.md` §5 has the template), add the answer blocks to `build/data/guides.py`, then run the three-command workflow in §6. Never write a second page by copying the first and swapping the name — that is the exact failure mode the plan exists to avoid, and the May 2026 core update targets it specifically.

**Add a neighborhood photograph.** Search Commons on the **disambiguated** name and check the **category** before anything else. Read the description. Look at the image. Add a `photos.CREDITS` entry with the licence URL and a `modified` note, drop the cropped file into `site/assets/img/neighborhoods/`, then run optimize and generate. If nothing verifiable turns up, add a `photos.REJECTED` entry saying why.

**Replace an existing image.** Just overwrite the JPEG. The hash manifest will notice and regenerate every derivative. This did not use to work — see §6.

**Write a journal post or news update.** [docs/content-runbook.md](docs/content-runbook.md) is the whole procedure — three lanes, the Fair-Housing reframe table, the briefed calendar, and the shipping mechanics (including the date-churn guard from §9). Topic sourcing runs on the monthly listening pass: the `/last30days` skill (installed at `.claude/skills/last30days/`; **run it locally — Reddit blocks datacenter egress**, verified 2026-07-30) plus the web sweeps and agent-sourced Nextdoor signal documented in [research/communityVoice.md](research/communityVoice.md).

**Refresh market snapshots.** Update the stats per community, bump the visible updated date, and recycle each refresh into a GBP post and an Instagram post. Quarterly refresh discipline is a feature, not overhead: competitors ship $0 medians, lorem ipsum and empty school tables. Nothing here may rot unattended.

**Before every push.** `python3 build/validate.py`. Rich Results Test on any page whose schema changed.

**After publishing pages.** Point GBP's website link at the right page, then run a geogrid scan 2–4 weeks later. Log to `briefs/team-azizi/san-diego/scans/`.

**Monthly reporting.** Manual AI query panel — ChatGPT, Gemini, Perplexity, AI Overviews — per neighborhood: mentioned yes/no, sentiment, **which sources got cited**, competitor grid. Plus GBP actions and conversions rather than raw clicks.

**Resuming cold.** `GAMEPLAN.md` → this file → `research/salesRecord.md`. The `research/` files are the evidence base; do not re-run the research.

---

## 11. Mistakes made on this project, and what they cost

Kept because every one of them is a trap the next person can fall into, and three of them were only caught by luck.

| What happened | How it was caught | The lesson |
|---|---|---|
| Claimed the Vercel preview was healthy — "all 200" | It was not. Deployment protection returns the login page with HTTP 200, so `curl -L` was measuring a login form | A 200 is not a success. Check the body. |
| A Zillow URL regex attached the wrong agent's profile to Masooma Azizi | Printing **every** pairing individually before committing | A non-greedy match will happily cross record boundaries. Verify pairings one by one, not in aggregate. |
| `optimize.py` re-encoded every JPEG on every run | Noticed ~40 binary files dirty in git for no reason | Idempotency in a generator is a correctness property, not a nicety. |
| Then the fix for *that* left stale WebP files after an image was replaced | Only found because a graded image was replaced in place and the WebP was checked by hash | The cache-invalidation fix needs its own invalidation test. |
| The mtime-based fix reintroduced the churn, dirtying 30 unrelated headshots | git status, immediately | mtime is not a content signal. git rewrites it at checkout. |
| The byline rotation made `expert_block` say "Team lead" about two people who are not the team lead | Reading the rendered output rather than trusting the diff | Authorship is asserted in three places; changing one means checking all three. |
| A validator rule for bare-pronoun openers flagged 9 false positives | The failures were obviously fine on inspection | A crude heuristic that fires on good content trains people to ignore the validator. Requiring both conditions fixed it. |
| San Marcos's licence was recorded as CC BY-SA when it is public domain | Checked against the API before commit | Do not transcribe a licence from memory or from a sibling entry. |
| A test corrupted `contact.html` and a second test then treated the damaged file as the original | Regenerating from source rather than from a backup | A test that mutates a real file must restore it in a `finally`, and never trust a backup taken after the damage. |
| Rejected Valley Center's photo as unverifiable | Asking a different question — who *uses* the file | Contradictory metadata is a reason to look harder, not always a reason to stop. |
| A documentation-only commit arrived with 27 pages of date churn attached, every one claiming an update that never happened | Reading `git show --stat` before pushing, and asking why a docs change touched 29 files | A generator that stamps `date.today()` unconditionally manufactures freshness. **Read the file list on every commit** — if the count surprises you, find out why before pushing. Open item in §9. |

---

*This file is state, decisions and why. `GAMEPLAN.md` is the plan. `docs/launch-runbook.md` is the ordered launch sequence. `research/` is the evidence base.*
