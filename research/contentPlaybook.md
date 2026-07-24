

# ==== playbook ====

# Team Azizi Local SEO Playbook — Neighborhood-Expert Pages as the Centerpiece

Distilled from: `local-landing-pages`, `local-keyword-research`, `local-content-strategy`, `local-content-briefs`, `gbp-optimization` (each skill directory contains only SKILL.md; no supplementary reference files exist).

Workflow the skills prescribe (follow this order):
```
local-keyword-research → local-content-strategy → local-content-briefs → local-landing-pages (build) → GBP alignment → geogrid measurement
```

---

## 1. The Neighborhood Page Blueprint

### 1.1 Core principle: unique value per page
Google's doorway-page penalty targets pages that swap city/neighborhood names into identical content, exist only to funnel to a single conversion, and provide no unique value. **Every page must earn its existence.**

**May 2026 core update (explicitly called out in the skill):** it devalued commodity/templated content and rewarded first-hand, point-of-view pages with original local detail and experience. "Templated geo-pages with the city name swapped are exactly what's being demoted." Every neighborhood page needs genuine local substance — real transactions, real streets/blocks, original photos, area facts, lived expertise — **not just unique sentences.** For Team Azizi this is the single biggest strategic requirement AND the biggest opportunity: an agent who actually farms a neighborhood can produce exactly the first-hand POV content the update rewards.

### 1.2 Page-type mapping for Team Azizi
The skill defines three page types:
- **Type 1 — Physical Location Page** (`/locations/[city]/`): full NAP, embedded map, hours, team members, LocalBusiness schema with unique `@id`, unique photos/reviews. → Team Azizi: the Compass office page (one page).
- **Type 2 — Service-Area Page** (`/service-area/[area]/`): area served without a storefront there; service + area in title/H1/meta; local context; CTA with click-to-call; Service schema with `areaServed`. → Team Azizi: **this is the neighborhood-expert page model.**
- **Type 3 — Service × Location Page** (`/[service]/[area]/`): highest intent — intersection of a specific service and location; local regulations, pricing, case studies; location-specific FAQ. → Team Azizi: "Sell your home in [Neighborhood]" or "[Neighborhood] home valuation" pages layered on top of the flagship neighborhood pages for the highest-value neighborhoods.

### 1.3 On-page template (exact formulas from the skill)
- **Title:** `[Primary Service] in [City, ST] | [Brand Name]` → e.g. `[Neighborhood] Real Estate Agents & Homes | Team Azizi | Compass`
- **Meta:** `[Service benefit] in [City]. [Differentiator]. [CTA]. Call [phone].`
- **H1:** `[Primary Service] in [City/Area]` → e.g. `[Neighborhood] Real Estate Experts`
- **No duplicate meta tags across neighborhood pages** (named as a common mistake).

### 1.4 Required page structure (8 sections, in order)
1. **Hero** — service + location, primary CTA (home valuation / buyer consult), trust signals (sales volume, years, Compass)
2. **Service overview** — what the team does in this neighborhood, 2–3 paragraphs
3. **Why choose us** — differentiators for local clients (homes sold in this neighborhood, avg. days on market vs. area, list-to-sale ratio)
4. **Service details** — specific offerings with descriptions (listing/marketing, buyer representation, valuation, Compass Concierge, relocation)
5. **Local context** — the uniqueness engine (see 1.5)
6. **Social proof** — reviews from clients IN this neighborhood, sold case studies with addresses/streets
7. **FAQ** — neighborhood-specific questions
8. **CTA** — phone, form, or scheduling (valuation widget / consult booking)

The briefs skill adds: CTA at the end **and optionally mid-page for long content**; highest-value content early, never buried.

### 1.5 Uniqueness strategies (what separates ranking pages from penalty-worthy doorway pages)
- **Local context:** micro-neighborhoods/blocks, local building/architecture types (Craftsman vs. mid-century vs. new construction), climate-specific considerations, local regulations/HOA/permit quirks, schools, commute, proximity notes.
- **Local social proof:** reviews from that neighborhood, case studies with location details, before/after (staging, sold) photos from actual local transactions.
- **Local data:** market statistics (median sale price, price/sq ft, days on market, inventory, YoY change), common area-specific issues, pricing ranges, response/turnaround expectations. *This is Team Azizi's programmatic-data advantage — MLS data is a legitimate per-page unique-data source.*
- **Local partnerships:** relationships with local businesses, community involvement, org memberships (neighborhood associations, sponsorships).

### 1.6 Word counts and quality standards
- **800–1,500 words** standard pages; **1,500–2,500** for guides (neighborhood-guide-style pages should sit in this band).
- **Pillar pages: 2,500–4,000 words, 20+ distinct concepts** (from the briefs skill).
- Original local insights, not rewritten generic content.
- **Author byline and visible updated date on every page** (E-E-A-T + AI citation credibility — name the actual agent who farms that neighborhood).
- Internal links to service and neighborhood pages.

### 1.7 Scale rules
- **5–20 pages:** hand-craft each, full unique content. ← Team Azizi's flagship neighborhoods belong here.
- **20–100 pages:** template + required unique sections, **300+ unique words per page minimum**.
- **100+ pages:** programmatic only with a reliable per-page data source (MLS feed qualifies), and only if genuine search demand exists.

### 1.8 The four-question quality check (run on every page before publish)
1. Would this help a real person in this neighborhood?
2. Is there unique content beyond the neighborhood-name swap?
3. Does search demand exist?
4. Would you show this page to Google's webspam team?

### 1.9 Thin/doorway traps (verbatim mistake list)
- City/neighborhood name swapping with identical content
- Creating pages for areas with no search volume
- Orphan pages with no internal links
- Missing schema markup
- Duplicate meta tags across location pages
- Thin content ("100 words and a map" — or, for realtors: an IDX widget and a paragraph)

---

## 2. Schema Requirements

### 2.1 Office/location page (Physical Location pattern — swap type for real estate)
```json
{
  "@context": "https://schema.org",
  "@type": "RealEstateAgent",
  "@id": "https://teamazizi.com/#business",
  "name": "Team Azizi | Compass",
  "address": { ... },
  "geo": { "latitude": "…", "longitude": "…" },
  "areaServed": { "@type": "City", "name": "[City, ST]" }
}
```
Unique `@id` per location entity; NAP in schema must match GBP exactly.

### 2.2 Neighborhood pages (Service-Area pattern)
```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Real Estate Services",
  "provider": { "@type": "RealEstateAgent", "@id": "https://teamazizi.com/#business" },
  "areaServed": { "@type": "Place", "name": "[Neighborhood], [City], ST" }
}
```

### 2.3 Additional schema by section (from the briefs skill)
- **LocalBusiness/RealEstateAgent** — required for location pages.
- **FAQPage** — for Q&A sections. **2026 note (exact):** Google dropped FAQ rich results, so FAQPage schema no longer yields SERP rich results — keep it as an **AI-parsing aid**, not a rich-result play. Direct-answer formatting matters more than the markup.
- **HowTo** — process content (e.g., "How to sell your home in [Neighborhood]").
- **Review** — where testimonials appear.
- **BreadcrumbList** — on every page: `Home > Neighborhoods > [City] > [Neighborhood]`.

---

## 3. Local Keyword Research Method

### 3.1 Why local research is different (core dynamics)
- **Implicit vs. explicit local intent** — "realtor" carries local intent with no geo modifier; Google localizes it automatically. Different keywords trigger map pack vs. organic layouts.
- **Near-me queries** are determined by the searcher's device location, not your content — **you cannot optimize for near-me with on-page content.** You win them via GBP presence, reviews, and proximity. (Critical expectation-setting for the client.)
- **Combinatorics:** services × areas explodes (10 services × 30 neighborhoods = 300 combinations). The matrix identifies demand; it does NOT mean 300 pages.
- **Micro-intent variations** attract different clients ("sell my house fast" ≠ "listing agent" ≠ "home valuation").
- **Low volume ≠ low value** — a 10-search/month neighborhood term can convert at extreme rates. Never discard on volume alone.

### 3.2 The 9 keyword categories, translated to Team Azizi
1. **Core service** (implicit local intent): realtor, real estate agent, sell my house, listing agent, buyers agent, home valuation.
2. **Geo-modified** — the exact modifier formats: `[service] [city]`, `[service] in [city]`, `[service] [city] [state]`, **`[service] [neighborhood]`** (the money pattern here), `[service] [county]`, `[service] [zip]`. E.g. "homes for sale [neighborhood]", "[neighborhood] realtor", "real estate agent [zip]".
3. **Near-me:** "realtor near me", "best real estate agent near me" — GBP-won, no pages.
4. **Problem/symptom** (customer language, not industry language — high urgency/conversion): "how much is my house worth", "should I sell my house now", "house not selling", "how to price my home", "moving to [city]".
5. **Qualifiers:** urgency (sell fast, this month), cost (commission, fees, free home valuation), quality (best, top rated, #1, luxury), comparison (vs, reviews, "[competitor team] alternative").
6. **Question keywords** (PAA/autocomplete — content/FAQ fuel, rarely direct converters): "is [neighborhood] a good place to live", "what are closing costs in [state]", "how long do homes take to sell in [neighborhood]".
7. **Branded procedure/product** — very high intent, low competition, and the brand's own "find a provider" directory is a listing opportunity: **Compass Concierge**, **Compass Private Exclusives**, "Compass agent [city]". Ensure Team Azizi's Compass directory profile is complete and links to the site.
8. **Insurance/qualification** — searcher already decided, checking access: "first time home buyer programs [city]", "down payment assistance [county]", "VA loan realtor", "FHA homes [city]", "new construction agent".
9. **Cross-border/bilingual** — if the market has a significant non-English-searching buyer pool (e.g., Spanish, Farsi — plausibly relevant given the team name), those keywords deserve their own category and potentially their own pages. Check: do clients search in another language? If yes, build for it; competitors almost certainly haven't.

### 3.3 Research process (5 steps + 2.5)
- **Step 1 — Seed from business intelligence (before any tool):** full service list; every city/neighborhood served; **top-revenue services** (listings vs. buyers — weight accordingly); competitor team names; customer language. Ask the team: **"When someone calls you, what do they say they need?"** — that phrasing is the keyword seed.
- **Step 2 — Expand with tools.** Per seed pull: monthly volume, keyword difficulty, SERP features (local pack? ads? AI Overview?), CPC (commercial-value proxy), related suggestions. Tools: Semrush Keyword Magic, Ahrefs, DataForSEO API, Google Keyword Planner (free, imprecise), Google Autocomplete (free, real-time), People Also Ask, SERP API. (Skill default: LocalSEOData tool — `keyword_opportunities`, `keyword_suggestions`, `search_volume`, `keyword_trends`, `keywords_for_site`.)
- **Step 2.5 — Mine competitor keywords from live SERPs** (free, highest-quality additions, usually skipped): (1) which competitors rank organically — scrape their neighborhood/service pages for terms you don't target; (2) Google's "Related searches" / "People also search for"; (3) each PAA question = FAQ or post topic; (4) map-pack competitors' GBP categories and services (different category = keyword opportunity); (5) who's paying for ads on which keywords = confirmed commercial value.
- **Step 3 — Build the combinatoric matrix** (services × neighborhoods × modifiers). Use it to find which combinations have real volume, which deserve dedicated pages vs. coverage on a broader page, and where competitors have pages you don't. **Do not build a page per combination.**
- **Step 4 — Classify intent.** Every keyword gets a tag:

| Intent | Real-estate example | Content type |
|---|---|---|
| Urgent | "sell my house fast [city]" | GBP + dedicated fast-sale page |
| Transactional | "realtor [neighborhood]" | Neighborhood page |
| Commercial investigation | "best real estate agent [city] reviews" | Reviews/comparison content |
| Informational | "is [neighborhood] a good place to live" | Blog/FAQ/guide |
| Navigational | "team azizi compass" | Homepage, GBP |

Priority order: Urgent > Transactional > Commercial > Informational.
- **Step 5 — Map keywords to pages.** Rules: **one primary keyword per page**; group keywords with SERP overlap onto the same page; **no thin pages for <10 monthly-search terms unless conversion value is high**; every service page targets its service keyword **plus 2–3 geo-modified variants**.

### 3.4 Volume realities (set expectations)
- Tools significantly undercount local volume; "near me" volume is aggregated nationally; long-tail showing 0–10 still drives real traffic; Keyword Planner groups terms misleadingly.
- **Search Console is the only ground truth** for actual clicks/impressions on existing pages. Treat tool volume as directional; **CPC is often a better value signal than volume**; never ignore a 0-volume keyword whose intent is real.
- Benchmarks by market size: major metro service keywords 5,000–50,000/mo (geo-modified 500–5,000); mid-size city 1,000–10,000 (100–1,000); small city/suburb 100–1,000 (10–100); rural 10–100 (0–10). Individual neighborhood terms will typically sit at the low end — that is normal and still worth winning.

### 3.5 SERP layout analysis (run for the top 20 keywords)
| SERP feature | Meaning for Team Azizi |
|---|---|
| Local pack | Implicit local intent — GBP optimization critical ("realtor [city]") |
| Ads / LSAs | High commercial intent; paid opportunity |
| AI Overview | Content must be AI-parseable — direct-answer format |
| People Also Ask | FAQ content opportunity |
| Organic only, portal-dominated (Zillow/Redfin/Realtor.com) | "homes for sale" clusters — decide deliberately whether to fight portals or reframe the page around agent-expertise terms |

A keyword that triggers a local pack requires different optimization than one showing only organic results.

### 3.6 Competitive gap analysis
- Pull organic keywords for the **top 3 local competitor teams** (Semrush/Ahrefs); filter for service terms + city/neighborhood names; find keywords where they rank top 20 and you rank nowhere; cross-reference against services offered; prioritize by **volume × relevance × difficulty**.
- Also hunt "nobody ranks well" keywords: top results are homepages (weak), thin/outdated pages (opportunity), or newer phrasings not yet targeted.

### 3.7 Deliverable: the Keyword Map
| Keyword | Volume | KD | Intent | Target Page | Status | Priority |
|---|---|---|---|---|---|---|
| realtor [neighborhood] | 90 | 25 | Transactional | /neighborhoods/[slug]/ | Needs creation | High |

Status values: **Exists (optimized) / Exists (needs update) / Needs creation / Low priority.** "Keyword research without page creation is wasted effort. Map keywords → pages → publish → scan rankings."

---

## 4. Content Strategy — From Keyword List to Architecture

### 4.1 Core principle
**Keywords are the input; concepts are what you build.** The two most common mistakes: (1) targeting each keyword individually instead of grouping into concept clusters; (2) defaulting to "write a page" when many keywords are won through GBP signals and need no page at all.

### 4.2 Step 1 — Concept clustering rules
- Geographic variants of one term = one cluster ("realtor [city]" + "realtor [neighborhood]" + "realtor near me" = same concept at different geographic specificity).
- Service variants belong together ("home valuation" + "what's my house worth" + "CMA" = one cluster).
- Each cluster gets a **plain-language concept label**, not a keyword string.
- Clusters are mutually exclusive — assign ambiguous keywords to the cluster of their core intent.
- Output per cluster: name, primary keyword (highest volume/most representative), supporting keywords, volume range, intent type, competitive level (H/M/L).

### 4.3 Step 2 — Content vehicle assignment (the most consequential decision)
- **Location/neighborhood page** when: clear transactional local intent; primary keyword carries city/neighborhood modifier; **generally 50+ monthly searches**; concept is specific enough for genuinely unique per-location content.
- **GBP service entry** when: a real service with local intent but **under ~50 MSV**; a service variant (e.g., "probate sale", "1031 exchange help", "relocation assistance") where a dedicated page would be thin — better as a GBP service expanding category coverage.
- **GBP category** when: cluster maps to a claimable secondary category; claiming it expands query eligibility for the whole cluster. (GBP action, not content.)
- **Blog/FAQ** when: informational intent (how-to, what-is, cost, comparison); research phase before a decision; AI Overview / PAA citation potential. **2026: first-hand, point-of-view content with original local insight is favored and is what AI search tends to cite.**
- **Near-me / GBP-signal-only** when: near-me variants that page content cannot target — won via GBP prominence, proximity, completeness. **Document this explicitly so the client understands why no page exists for those terms.**
- **Pillar page** when: a broad primary topic the business should own completely with multiple supporting clusters linking in — for Team Azizi: "[City] Real Estate / Neighborhood Guide" hub, "Selling a Home in [City]", "Buying a Home in [City]".
- **No action** when: under 10 MSV with low competition for a reason; a service not offered; navigational for a competitor.

### 4.4 Step 3 — Coverage gap analysis (against current site/sitemap)
Identify: **missing** coverage (clusters with no vehicle), **thin** coverage (page doesn't fully cover the concept), **duplicate** coverage (cannibalization — e.g., a neighborhood page AND a blog post both chasing "homes for sale in X"), **misassigned** coverage (a full page for a GBP-only term, or vice versa).

### 4.5 Step 4 — Geogrid tracking keyword selection (3–5 keywords)
Criteria: (1) clear local-pack intent; (2) one keyword per distinct concept cluster; (3) competitive enough that position matters (top-3 vs. #8 changes lead volume); (4) representative of primary revenue services (track what makes money — for Team Azizi, listing-side terms like "realtor [city]" / "sell my house [city]"); (5) distinct geographic coverage across the service area. Output: ranked list with reasoning per keyword.

### 4.6 Step 5 — GBP confirmation from the concept map
Secondary categories to add (each corresponds to a cluster) · services to add to the GBP menu · attributes to claim · which concepts appear naturally in the 750-char description.

### 4.7 Step 6 — Internal linking architecture
- **Hub** — pillar page (or primary location page) that all supporting pages link to.
- **Spokes** — neighborhood pages and blog posts link to the hub and to each other where topically relevant.
- **GBP-to-website links** — decide which page receives the GBP website link (primary location page or homepage, matched to query).
- **Anchor text guidance** — concept-based anchors specified per link.

### 4.8 Strategy output document (exact skeleton)
Concept Clusters (each: primary keyword | MSV, supporting keywords, intent, competition, vehicle, 1–2-sentence reasoning) → Content Vehicle Summary (pages table with P1/P2/P3 priority; GBP categories/services/attributes; blog/FAQ table; near-me clusters listed as no-content) → Geogrid tracking keywords with reasoning → Coverage gaps in priority order with visibility impact → Internal linking architecture (hub/spokes/cross-links) → **Production Priority Order**:
- **Phase 1 (immediate):** GBP actions — no content needed, can ship today.
- **Phase 2 (first 30 days):** high-impact content — primary neighborhood pages + GBP services.
- **Phase 3 (30–90 days):** supporting content — blog/FAQ, secondary neighborhood pages.
- **Phase 4 (ongoing):** long-tail, refreshes, gap filling.

---

## 5. Content Brief System — Systematizing Page Production

### 5.1 Core principle
**Concepts over keywords, completeness over length.** "Target 'realtor [neighborhood]' 12 times" produces thin content. A brief that demands complete coverage of the concept — with specific local entities in context — produces content that earns rankings by demonstrating genuine expertise. **Word count is a byproduct of complete concept coverage, not a target.**

### 5.2 Step 1 — Concept decomposition (per page)
- **Core concept** — the actual topic, not the keyword. For a neighborhood page: "how a buyer or homeowner in [Neighborhood] evaluates the market, chooses an agent, and buys or sells a home there."
- **Related concepts (10–15)** — genuinely distinct topics an expert covers, NOT synonyms. Neighborhood-page examples: current market conditions and pricing trends; housing stock and architectural styles; micro-areas/blocks and how they differ; schools and districts; commute/transit; pricing strategy for this inventory; what sells fast here vs. sits; buyer competition dynamics; HOA/permit/local-regulation quirks; recent representative sales; lifestyle/amenities; who's moving in and why.
- **Local-specific concepts** — what distinguishes this page from generic coverage: market micro-data, climate/terrain factors, local ordinances, landmark and street-level references.
- **Required entities (10–15)** — named things authoritative coverage contains: the business (with address/phone as natural mentions), city + key neighborhoods, schools, landmarks, licensing/credential bodies (state DRE license #, REALTOR®, MLS), data sources lending credibility (MLS, county records), differentiating concepts, schema entity types appearing naturally in text.

### 5.3 Step 2 — Depth tiers (exact word counts)
| Tier | Words | Count per piece | Use |
|---|---|---|---|
| Comprehensive | 400–600 | 2–3 | The reason someone reads the page: market conditions, why this team for this neighborhood, primary user question |
| Standard | 200–300 | 4–6 | Supporting context: housing stock, schools, process, buyer/seller dynamics |
| Brief | 75–150 | 4–6 | Authority breadth: amenities, history, adjacent areas |
| Entity mention | 1–2 sentences | as needed | Landmarks, credentials, tools, related services in context |

### 5.4 Step 3 — Local-specific brief requirements (every brief)
- **GBP consistency check** — concepts covered on the page must exist as GBP services/categories; flag misalignments (if the page sells "home valuation," GBP must list it as a service).
- **NAP natural mention** — brief specifies the sections where name/address/phone fit naturally (not forced); checklist requires NAP in **at least 2 places**.
- **Local entity integration** — which neighborhoods, landmarks, nearby areas appear naturally (geo-relevance without stuffing).
- **Schema per section** — LocalBusiness/RealEstateAgent (required, location pages), FAQPage (AI-parsing aid only — no rich results anymore), HowTo, Review; brief maps each type to sections.
- **AI visibility** — identify **3–5 questions per page** that warrant direct-answer formatting: **question as H3 heading, 2–3 sentence direct answer immediately below.** This is the AI Overview / AI Mode / assistant-citation mechanism.
- **Internal linking targets** — which pages this links to, with anchor text and placement, per the hub-and-spoke architecture.

### 5.5 Step 4 — Question mapping (8–10 per page)
For each: the question in natural user language; which section answers it; whether it warrants direct-answer formatting for AI eligibility; PAA-type (short answer) vs. deep question (full section). Neighborhood examples: "Is [Neighborhood] a good place to live?" · "How much do homes cost in [Neighborhood]?" · "How fast do homes sell in [Neighborhood]?" · "What is my [Neighborhood] home worth?"

### 5.6 Step 5 — Structure rules
Open with the core concept before any framing; sequence sections in decision order; group concepts under logical H2s (not one H2 per concept); highest-value content early; end with a conversion section; write actual heading text, not descriptions of headings.

### 5.7 Brief output format (the production template)
`Core Concept → Content Vehicle → Target Word Count (range calculated from depth tiers) → Primary Keyword (MSV, competition) → Supporting Keywords (woven naturally — entities, not density targets) → Concept Coverage Plan (Comprehensive/Standard/Brief/Entity-mention lists, each with key sub-points + local specificity) → Required Local Entities table (Entity | Type | Context for mention) → Questions table (Question | Section | Format | AI Overview candidate?) → Local SEO Technical Requirements (GBP consistency, NAP placement, schema list, internal links table [Link to | Anchor | Placement], 3–5 AI direct-answer questions) → Recommended H1/H2/H3 outline with opening-100-words guidance and FAQ H3s marked for FAQPage schema → Quality Checklist`

### 5.8 Quality checklist (verbatim, per page)
- [ ] 15+ distinct concepts covered
- [ ] All required local entities mentioned in context
- [ ] All 8–10 reader questions answerable from the content
- [ ] NAP appears naturally in at least 2 locations
- [ ] At least 3 sections formatted for AI Overview direct-answer eligibility
- [ ] Internal links placed naturally with concept-based anchor text
- [ ] No keyword stuffing — concepts appear because relevant, not for density
- [ ] Opening 100 words establish core concept and local context
- [ ] CTA at end, and optionally mid-page for long content

### 5.9 Brief emphasis by vehicle
- **Location/neighborhood page brief:** local entity density, GBP consistency, LocalBusiness schema, NAP placement, service-area specificity, "why this location specifically" — genuinely unique, never template-with-name-swapped.
- **Blog/FAQ brief:** informational intent, direct-answer formatting, FAQPage schema, full depth on the research question, internal links to transactional pages.
- **Pillar brief:** comprehensive domain coverage, hub-and-spoke linking, E-E-A-T signals, multiple schema types, **2,500–4,000 words, 20+ concepts**.
- **Service page brief** (valuation, sell-with-us, buy-with-us): transactional intent, scope, differentiators, trust signals, conversion-oriented structure — converts a visitor who has already decided.

### 5.10 Bulk production order (for the site rebuild)
1. **Pillar page brief first** — establishes the concept framework all other briefs reference.
2. **Primary neighborhood page briefs second** — highest traffic impact.
3. **Supporting neighborhood page briefs third** — geographic expansion.
4. **Blog/FAQ briefs last** — informational content supports but doesn't lead.

For CLI generation loops (relevant to this rebuild): each brief is self-contained and independently executable; label each brief file with vehicle type + primary keyword. Fully executed, the brief set produces **semantic saturation** — comprehensive coverage of the topic domain across all local search surfaces with no significant gaps.

---

## 6. Internal Linking Architecture (combined rules)

Hub-and-spoke:
```
/neighborhoods/                    or  /[city]-real-estate/   (pillar hub)
├── /neighborhoods/[neighborhood-a]/   (spoke)
├── /neighborhoods/[neighborhood-b]/   (spoke)
├── /neighborhoods/[neighborhood-c]/   (spoke)
```
- Every neighborhood page links up to the hub/pillar.
- Neighborhood pages link to **nearby neighborhoods** ("Also serving…" / "Nearby neighborhoods") — spoke-to-spoke cross-links where topically relevant.
- Service pages (sell, buy, valuation) link down to neighborhood pages; neighborhood pages link to service pages.
- Homepage links to **priority** neighborhoods.
- **Everything within 3 clicks of the homepage.**
- Breadcrumbs on every page (`Home > Neighborhoods > [Neighborhood]`) with BreadcrumbList schema.
- No orphan pages (named as a common mistake).
- Anchor text is concept-based, specified per link in each brief.
- GBP website link points at the page matched to the query intent (office page or homepage).

---

## 7. Supporting Content Engine (beyond neighborhood pages)

Content types (from local-landing-pages): **service education** ("How much does it cost to sell a home in [city]?", "How to choose a listing agent in [area]"), **local guides**, **case studies** (before/after with location details, problem → solution — e.g., "How we sold a [Neighborhood] Craftsman 12% over list"), **FAQ/knowledge base** (questions clients actually ask, with local variations), **community content** (local events, sponsorship recaps, partnerships).

Content planning inputs: core service keywords + location modifiers; People Also Ask; Google Autocomplete for `[service] + [city]`; **GBP Q&A and reviews for real customer questions**; competitor content gaps.

**Cadence: 2–4 pieces/month.** Mix education, case studies, local guides; align with seasonal demand (spring listing season, year-end market recaps). **Repurpose every piece into GBP posts, social, and email.**

---

## 8. AI-Citation Requirements (threaded through all skills)

- Direct-answer formatting is the mechanism: **question as heading (H3), 2–3 sentence direct answer** — at least 3 sections per page, 3–5 flagged questions per brief.
- FAQPage schema retained as an AI-parsing aid (not for rich results — those are gone).
- First-hand, point-of-view content with original local insight is what AI search tends to cite (May 2026 update alignment).
- Content structure, entity clarity, and web-presence breadth are a named "AI Search Signals" category in the GBP skill; the same engagement signals that drive map-pack rank feed AI-generated local answers.
- Citations/NAP consistency are "regaining importance because AI models pull from diverse web sources."
- Author bylines + visible updated dates support citation credibility.
- GBP data quality matters for AI: Google's new Maps Q&A is AI-generated from your profile, reviews, and website — complete, accurate underlying data is what makes AI answers correct; review AI-suggested answers before they publish.

---

## 9. GBP Checklist for Team Azizi (highest-level, as requested)

### Ranking model
Three pillars: **Proximity** (can't control) · **Relevance** (primary category = strongest signal) · **Prominence**. **2026 shift — prominence → popularity:** weighting has moved toward engagement (CTR, calls, direction requests, review velocity, post/photo activity) and away from static prominence (raw counts, tenure). **Active profiles outrank established-but-inactive ones**; being open at search time is roughly a top-5 factor (confirmed 2023; rankings degrade in the final hour before closing). The same engagement signals feed AI local answers. Frame everything as ongoing activity, not one-time setup.

### Categories (single most important controllable factor)
- **Primary:** what the business IS, most specific available — `Real Estate Agency` or `Real Estate Agent` (check what the top map-pack competitors use via Maps searches / GMB Spy / Pleper).
- **Additional:** up to 9 — add every legitimately applicable one (e.g., Real Estate Consultant; others only if genuinely active services — never aspirational). Each secondary category should correspond to a concept cluster from the strategy; more categories = more query eligibility.

### Business information
- **Name:** exact real-world name — "Team Azizi" (or the exact registered variant). No "Team Azizi | Best [City] Realtors" — keyword stuffing is the #1 spam tactic and a suspension risk; report competitors who do it.
- **Address/phone:** USPS-formatted, consistent everywhere; **local number** (not toll-free) as primary, same number across all citations. Note: GBP chat/messaging retires July 2026 — keep call + website CTAs strong.
- **Hours:** accurate, holiday special hours set in advance; consider legitimate extended hours (every open hour is a ranking-visible hour).
- **Website URL:** with UTM — `?utm_source=google&utm_medium=organic&utm_campaign=gbp`.
- **Description (750 chars):** what the team does + primary service area → key services/specialties → differentiators (years, volume, Compass, credentials) → CTA. No stuffing, URLs, phone numbers, promo language, or all-caps. Description keywords come from the concept clusters.

### Services & attributes
- Every service listed with descriptions, grouped logically, natural keyword variations — mirror the concept map: home valuation, listing/seller representation, buyer representation, relocation, investment property, Compass Concierge, plus every sub-50-MSV cluster assigned as "GBP service."
- Complete **ALL** applicable attributes (identity/ownership, online appointments, service-specific).

### Photos
Cover (16:9) → logo → interior 3+ → exterior → team → service/at-work (listings, open houses, closings). **10–15 minimum, add 2–3/month.** Descriptive filenames, no stock, 720px+ wide, JPG/PNG. Don't bother geo-tagging (EXIF stripped, no ranking effect). Video: 30s–3min, under 75MB, uploaded directly.

### Reviews
Recency and **velocity** are top-tier (recent reviews matter more than total count); rating, keywords in reviews, and response rate all matter. Respond to everything. Seed review requests that naturally elicit neighborhood mentions ("worked with us in [Neighborhood]").

### Posts cadence
**1–2 posts/week** (from the Month-1 playbook), sourced by repurposing neighborhood pages, market updates, just-sold case studies, and community content.

### Q&A
Answer everything (owner answers show first); monitor weekly for spam. 2026: user-facing Q&A is being replaced by AI-generated Q&A drawn from profile/reviews/website — seeding matters less; complete, accurate underlying data + reviewing AI-suggested answers before publish matters more.

### Rollout timeline (from the Map Pack Playbook)
- **Week 1–2 (quick wins):** fix primary category; complete all fields; 10+ photos; respond to all unanswered reviews; fix NAP on website; add/fix RealEstateAgent (LocalBusiness) schema.
- **Month 1:** posting 1–2/week; review generation campaign; top-tier citations (Apple Business Connect, Bing Places, Yelp, Facebook); create/optimize the location page; fix citation inconsistencies.
- **Month 2–3:** industry-specific citations (Zillow/Realtor.com/Homes.com agent profiles, Compass directory); service-area content; local link opportunities; seed Q&A; add video.
- **Ongoing:** weekly — reviews, Q&A, posts, edit monitoring; monthly — photos, insights, hours check; quarterly — competitor audit, category review.

### Common GBP mistakes to avoid
Keyword-stuffed name (suspension risk) · wrong primary category (biggest lever) · stale profile (no posts/photos in months) · inconsistent NAP · ignored Q&A · stock photos · incomplete services section.

---

## 10. Measurement Loop

- **Default next step after publishing pages (verbatim):** link them from GBP (website URL to the right page) and **run a geogrid scan 2–4 weeks later** to measure impact.
- Track the 3–5 geogrid keywords selected in strategy Step 4 (revenue-representative, local-pack-intent, one per concept, geographically spread).
- Search Console = ground truth for organic queries/clicks on the new neighborhood pages; feed real query data back into the keyword map (Status column: Exists-optimized / Exists-needs-update / Needs creation / Low priority).
- Evidence discipline (as flagged in the skills themselves): hours/openness = Google-confirmed ranking factor (2023); engagement-weighting shift = current industry consensus; linked-social = indexing/engagement play, NOT a confirmed ranking factor — don't oversell it to the client. Signal percentages shift yearly; relative weights are what matter.

# ==== top_10 ====

# Top 10 Highest-Leverage Moves for Team Azizi

1. **Build every neighborhood page as a first-hand expert page on the 8-section template (hero → overview → why-us → services → local context → neighborhood social proof → FAQ → CTA), 800–1,500 words, hand-crafted** — the May 2026 core update explicitly demotes name-swapped geo templates and rewards exactly the original, lived-in local detail a farming agent can produce; this is the whole thesis of the site.

2. **Run concept clustering + content-vehicle assignment BEFORE building any pages** — only neighborhoods/terms with real transactional demand (~50+ MSV guideline) get pages; sub-50-MSV service variants become GBP services and near-me terms get no page at all, which prevents the thin/doorway inventory that would sink the rebuild.

3. **Load each page with unique local DATA — median price, price/sq-ft, days-on-market, housing-stock and micro-area detail, plus real sold case studies from that neighborhood** — MLS data is the per-page unique-content source the skills demand, and it's the substance Google ranks and AI assistants cite.

4. **Format 3–5 questions per page as direct answers (H3 question + 2–3 sentence answer) and mark them up with FAQPage schema as an AI-parsing aid** — this direct-answer structure is the prescribed mechanism for AI Overview / assistant citation ("Is [Neighborhood] a good place to live?", "What's my [Neighborhood] home worth?").

5. **Wire the hub-and-spoke internal-link architecture: a [City] real-estate pillar (2,500–4,000 words, 20+ concepts) as hub, neighborhood spokes linking up, 'nearby neighborhoods' cross-links, breadcrumbs with BreadcrumbList schema, everything within 3 clicks, zero orphans** — orphan location pages are a named killer, and the hub concentrates authority on the exact "neighborhood expert" claim.

6. **Ship RealEstateAgent/LocalBusiness schema (unique @id, geo, NAP matching GBP exactly) on the office page and Service schema with `areaServed` per neighborhood page** — missing schema is on the common-mistakes list, and entity clarity is a named AI-search signal.

7. **Produce a semantic content brief for every page before writing (core concept, 10–15 related concepts, 10–15 required local entities, depth tiers of 400–600/200–300/75–150 words, 8–10 mapped questions, quality checklist)** — this is the system that makes 15–30 neighborhood pages producible at consistent authority level, including via a Claude generation loop.

8. **Rebuild GBP around the concept map: exact-match name, most-specific primary category, all legitimate secondary categories, full services menu mirroring the page concepts, 750-char description, all attributes, complete photos** — primary category is the strongest controllable local ranking signal and GBP↔page consistency is a required check in every brief.

9. **Run the engagement cadence: 1–2 GBP posts/week (repurposed from neighborhood pages and just-solds), 2–3 photos/month, review-velocity campaign with responses to everything and neighborhood mentions in reviews** — 2026 weighting moved to popularity/activity signals, so an active profile now outranks an established-but-idle one, and the same signals feed AI local answers.

10. **Close the loop with a keyword map deliverable and measurement: mine problem/symptom and question keywords ("how much is my house worth", "is [Neighborhood] a good place to live") into valuation/consult CTAs, pick 3–5 revenue-representative geogrid tracking keywords, link new pages from GBP, and scan rankings 2–4 weeks post-publish** — "keyword research without page creation is wasted effort," and page creation without ranking measurement is guesswork.