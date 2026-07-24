

# ==== playbook ====

# Team Azizi AI-Visibility Playbook
Distilled from: `skills/ai-local-search/SKILL.md` (v1.2.0), `skills/entity-authority/SKILL.md` (v1.0.0), `skills/local-schema/SKILL.md` (v1.1.0), `docs/how-local-search-works.md` (all by Garrett Smith). Evidence tiers per the skill set's evidence-standards scale: **A** = Google-confirmed, **B** = controlled causal test, **C** = correlation study, **D** = expert survey/consensus, **E** = vendor claim/anecdote.

---

## 1. How AI Assistants Pick Which Local Businesses to Mention

### The mechanics (from ai-local-search + how-local-search-works)
- AI models **synthesize from multiple sources rather than rank pages**. Traditional ranking position matters less; **being a cited source matters more**.
- **The 7 data sources AI uses**, in the skill's stated order:
  1. Google Business Profile data (for AI Overviews / AI Mode / Gemini)
  2. Web content — especially well-structured service/location pages
  3. Reviews — aggregated sentiment, specific service mentions, quality signals
  4. Citations and directories — NAP data, category associations
  5. Brand mentions — unstructured mentions across blogs, news, forums
  6. Structured data (schema) — machine-readable business info
  7. Third-party reviews — Yelp, industry platforms, social media
- **AI search signals are now a distinct ranking-factor category**: entity clarity, web presence breadth, content structure, brand authority across diverse sources.
- **Key data points (as stated in the skills, mid-2026):**
  - AI Overviews appear for **over half of local search queries**; AI Overview prominence is **rooted to industry, not city** (if AIOs show for a vertical in Houston, they show for it in Denver — so test whether real-estate queries trigger AIOs once, and it generalizes across Team Azizi's neighborhoods).
  - Google AI Mode passed **1 billion monthly users** at I/O 2026; follow-up queries up **40%+ month-over-month**.
  - **Top-3 local pack businesses have only ~26% likelihood of appearing in Gemini responses** (restaurant-query analysis) — i.e., **~74% of pack winners don't show in AI**. Map pack ranking alone does not guarantee AI visibility. (Tier C — correlation analysis.)
  - **Zero-click is the norm**: industry estimates put organic-click reduction near **~58%** for AI-affected queries. Measure GBP actions and on-site conversions, not raw clicks.
  - AI traffic to local business sites grew from **~0.1% to ~2%** of Google traffic in one year (large multi-location businesses) — directional, not dominant. Don't abandon Google optimization for AI optimization.
  - **ChatGPT pulls from Bing's index** — Bing Places is newly relevant.
- **What AI search signals reward** (how-local-search-works): entity clarity (consistent, structured info everywhere — where citations regain importance), review sentiment (AI synthesizes review *text*, not just stars), authoritative comprehensive service/location pages, and **web presence breadth** — mentions in diverse authoritative sources AI pulls from: **Reddit, Quora, niche blogs, news articles, not just directories**.
- **Key insight (verbatim intent):** the fundamentals of local SEO (strong GBP, website, reviews, consistent citations) are exactly what AI models need to confidently recommend a business. **The businesses most at risk in AI search are those with thin web presence** — if AI can't find diverse, consistent information about you, it won't recommend you.

### Query types that trigger AI local results — mapped to Team Azizi
- "Best [service] in [city]" → "best realtor in [neighborhood]," "best real estate agent in [city]"
- "Find me a [service] near [area]" → "find me a listing agent near [neighborhood]"
- Conversational → "I need to sell my house fast," "we're relocating to [city], who should we work with"
- Comparison → "Who's better, Team Azizi or [competitor team]?"
- Recommendation → "What realtor do you recommend in [neighborhood]?"
- **"Should I buy in X neighborhood?"** is informational/mixed intent — per how-local-search-works, informational queries don't trigger the map pack, but AI assistants answer them and **cite sources**. Neighborhood pages are the asset built to be that citation (see §5).

### Platform-by-platform source notes
| Platform | Primary sources | Implication for Team Azizi |
|---|---|---|
| Google AI Overviews / AI Mode | GBP data + website content + reviews; map pack may appear alongside | GBP optimization remains foundational; geogrid tools (Local Falcon) now scan AI results |
| ChatGPT / SearchGPT | Web search (Bing index) + training data; **cites sources** — well-structured pages with clear facts get cited; review aggregation across platforms; **less dependent on GBP, more on web content and authority** | The rebuilt website + Bing Places + multi-platform reviews are the ChatGPT levers |
| Gemini | **GBP is the primary data source**; deep Maps/Search integration; conversational local queries are a primary use case | Same optimization as AI Overviews — GBP completeness |
| Perplexity | AI search engine with **cited local results** | Same citable-content play as ChatGPT |
| Apple Intelligence / Siri | Maps integration | Covered by separate apple-business-connect skill (not read here) |

### The three classic factors still underneath it all (how-local-search-works)
- **Relevance** — GBP primary category is the strongest single signal; **relevance is binary before it's a spectrum**: category selection is the highest-impact single change in local SEO. Also: additional categories (3–5 usually sufficient), services/products, website content, review text mentioning services, schema.
- **Proximity** — can't be optimized; strengthen relevance + prominence to widen the ranking radius. Weighting varies by keyword ("coffee shop" extreme, "brain surgeon" minimal — realtor selection sits toward the low-proximity/high-trust end, which favors prominence work).
- **Prominence** — review count/rating, **review recency & velocity (top-tier signal as of 2025: a business with 200 reviews but none in 3 months loses to one with 80 getting 5–10/month)**, citation volume/consistency, backlinks (local/relevant), **brand search volume**, listing age, engagement signals, website authority, linked active social.
- **Business hours**: being open at search time is now considered the **5th most influential local pack factor** (Tier B — controlled test per evidence-standards); rankings degrade in the final hour before closing. Don't fake 24/7; do evaluate legitimate extended hours (a team answering 8am–8pm has a structural advantage).
- Behavioral feedback loop: CTR, click-to-call, direction requests, website clicks, dwell, pogo-sticking — engagement compounds.

---

## 2. Entity Consistency & Authority (entity-authority skill)

Entity signals are "disproportionately important for AI visibility, where citation- and entity-based signals make up several of the top factors." **Honesty note from the skill: "branded search as a trust signal" and "entity clarity helps AI" are Tier D (strong consensus) plus partial Google statements — not a measured weight.** Build it because it's coherent and compounding; label confidence honestly to the client.

### 2.1 One canonical identity, everywhere
- Lock a **single canonical business name, address format, and phone** — the real-world brand, never keyword-stuffed (suspension risk).
- Enforce across GBP, website, social, directories, data aggregators. **Inconsistency is the #1 way an entity fragments.**
- **Team Azizi decision to make first**: exactly one canonical string (e.g., "Team Azizi – Compass" vs "Team Azizi") — then it's identical on GBP, the new site footer (footer NAP on every page is standard), Compass profile, Zillow, Realtor.com, social, everywhere.
- **Entity-resolution mechanics** (how-local-search-works): Google connects GBP + website + citations + social + reviews + schema into one entity. When sources agree, confidence is high and rankings benefit; when they disagree, signals split across "versions" of the business. **Duplicate listings are the worst version** — two GBPs = two entities; reviews on one don't help the other. Real-estate-specific risk: individual agents' GBP listings vs. the team listing — audit and either differentiate cleanly or consolidate.

### 2.2 Organization schema + sameAs
- Implement `Organization` (or `LocalBusiness` subtype) schema with a **complete `sameAs` array linking every official profile** — social, major directories, Wikipedia/Wikidata if present. "`sameAs` is how you tell search engines 'all of these are the same entity.'"
- Keep schema's name/logo/contact **identical to GBP**.
- Team Azizi `sameAs` targets: Compass team profile, Zillow team + agent profiles, Realtor.com, Facebook, Instagram, LinkedIn, YouTube, Yelp.

### 2.3 Authoritative reference nodes
- **Wikidata**: a well-formed item (where genuinely notable/eligible) is a strong entity anchor knowledge systems read. **Don't fabricate notability.**
- **Wikipedia**: only if genuinely notable — otherwise it gets removed and can backfire. **Most local businesses won't qualify; that's fine.** (Set this expectation with the client up front.)
- **Crunchbase, industry bodies, official registries**: legitimate structured nodes. Real-estate mapping: state real-estate license registries, local Realtor association / MLS member pages, Chamber of Commerce.

### 2.4 Knowledge panel
- A branded search should surface a knowledge panel. **Claim it (verification) when available**, keep data accurate, feed it via consistent schema + authoritative references. The panel both reflects and reinforces entity strength.

### 2.5 Branded search demand
- Branded search volume is the **demand-side prominence signal**. Grow it legitimately: local PR, community presence, content, social, offline marketing; earn genuine media and "best of [city]" brand mentions. Never fake queries (manipulation).
- **Track branded query volume over time in Search Console** as a leading indicator of prominence — a clean agency KPI.
- Skill's expectation-setting line: "Entity work is slow-compounding infrastructure, not a quick ranking lever — set expectations accordingly."

### 2.6 Earned, not bought — the AI-era constraint (Tier A)
- **Google's first official AI-search guide (May 2026)** states its spam policies apply to AI features and warns against **manipulating or buying citations/mentions to influence AI results**.
- **Do:** earn mentions via genuine newsworthiness, partnerships, expertise, community involvement. **Don't:** buy citation/mention placements engineered for AI visibility or run mention/link networks. "Earned compounds; bought is a stated spam risk."
- This is the compliance line for the agency's repeatable offering — no paid "AI mention" packages.

---

## 3. Schema Blueprint (local-schema skill)

**Core principle: schema on the website must match GBP data exactly. Mismatches create conflicting signals. Schema is the website confirming what GBP says.**

**2026 schema notes (all effectively Tier A / Google-confirmed changes):**
1. **FAQ rich results were dropped in 2026** (with the Search Console report). FAQPage no longer produces SERP rich results — **keep it for AI parsing, not rich-result display**.
2. **Self-serving `aggregateRating`/`Review` markup on your own LocalBusiness will not render star rich results**; only independent/third-party review markup is eligible. (Can still include it as machine-readable data, but promise no stars.)
3. **Schema's biggest payoff now is helping AI Overviews, AI Mode, and assistants understand your entity — completeness matters more than ever.**

### 3.1 @type selection
The skill's subtype table explicitly prescribes: **Real estate agent → `RealEstateAgent`**. Rule: use the most specific LocalBusiness subtype (full list: https://schema.org/LocalBusiness). So the Team Azizi main entity is `@type: "RealEstateAgent"`. (Note: the skills prescribe `RealEstateAgent` and the `Organization` linking pattern below; **`Person` schema for individual agents is not covered in these skill files** — if the agency adds Person markup for agent bios, flag it as an extension beyond the skills' prescription.)

### 3.2 Full property checklist (from the LocalBusiness template — populate every field)
- `@context`: "https://schema.org"
- `@type`: `RealEstateAgent`
- `@id`: `https://[domain]/#business` (stable, unique)
- `name` (identical to GBP), `image` (logo URL), `url`, `email`
- `telephone` — **with country code** (e.g., `+1...`); local number preferred over toll-free (per GBP ecosystem notes)
- `address` → `PostalAddress`: `streetAddress`, `addressLocality`, `addressRegion`, `postalCode`, `addressCountry` — **format must match GBP exactly** (Compass office address)
- `geo` → `GeoCoordinates`: `latitude`, `longitude`
- `openingHoursSpecification` → `dayOfWeek` array, `opens`, `closes` — must match actual/GBP hours
- `areaServed` — array of `{ "@type": "City", "name": "...", "sameAs": "https://en.wikipedia.org/wiki/..." }` entries. **This is the neighborhood-targeting property**: one entry per neighborhood/city served, with Wikipedia `sameAs` URLs where they exist (the template shows this pattern for the primary city)
- `priceRange` (e.g., "$$")
- `sameAs` — the entity array from §2.2
- `aggregateRating` → `ratingValue`, `reviewCount` (with the no-stars caveat above)
- `hasOfferCatalog` → `OfferCatalog` with `name` + `itemListElement` of `Offer` → `itemOffered` → `Service` with `name` AND `description` (not just names). Team Azizi catalog: Buyer Representation, Seller/Listing Representation, Relocation Services, Investment Property, Home Valuation — each with a real description sentence.

### 3.3 Multi-entity pattern (prescribed for multi-location; adapt for team + agents + neighborhoods)
- Each sub-entity page gets its own schema with a **unique `@id`**: e.g., `https://[domain]/agents/[name]/#business` — the skill's exact pattern is `"@id": "https://example.com/locations/buffalo-ny/#business"` with its own `name` and `url`.
- Homepage carries `Organization` with `"@id": "https://[domain]/#organization"` and a **`department` array of `@id` references** to each sub-entity — this is the skills' prescribed linking mechanism, adaptable to team → agents.
- **Common error to avoid: duplicate `@id` across pages.**
- Neighborhood pages: neighborhoods are service areas, not offices — represent them via the `areaServed` array on the main entity (SAB pattern: emphasize `areaServed` with `City`/`State` entries) rather than fake per-neighborhood business entities with addresses.
- Multi-location content rule that applies directly to agent and neighborhood pages: **unique, substantial content per page — Google devalues pages identical except the swapped name/city**. Subfolder structure (`domain.com/neighborhoods/x`) beats subdomains.

### 3.4 Validation workflow
1. **Google Rich Results Test** (https://search.google.com/test/rich-results — renders JavaScript)
2. **Schema Markup Validator** (https://validator.schema.org/)
3. Browser DevTools: `document.querySelectorAll('script[type="application/ld+json"]')`
- **Common errors checklist:** address format ≠ GBP; missing `geo`; `@type` too generic; `telephone` missing country code; `openingHoursSpecification` ≠ actual hours; duplicate `@id` across pages.
- **Detection limitation (the skills' one explicit crawler consideration):** `web_fetch` and `curl` strip `<script>` tags; many CMS plugins inject JSON-LD via JavaScript — always verify with Rich Results Test or browser tools. **Implication for the rebuild (inference from this warning): server-render JSON-LD statically in the HTML** so non-JS fetchers (including AI retrieval) see it.
- **llms.txt: not mentioned anywhere in these skill files.** The only AI-crawler considerations the skills state are: ChatGPT reads Bing's index, Google AI reads GBP, schema completeness aids AI parsing, and the JS-injection detection caveat above. Don't present llms.txt as part of this skill set's prescription.
- Post-launch: validate, then **monitor Search Console for structured-data errors over the next 2 weeks** (skill's stated default next step).
- Expectation-setting: **"Schema alone rarely moves rankings — it reinforces other signals."**

---

## 4. GBP as AI Feedstock (ai-local-search §5 + how-local-search-works)

Google's AI products pull heavily from GBP, and Gemini's primary source is GBP. Checklist:
- **Every GBP field filled completely.**
- **Primary category** = single most impactful ranking signal; most specific match for target queries (real-estate category set). Additional categories: 3–5 usually sufficient.
- **Services section with detailed descriptions** (mirror the `hasOfferCatalog` — GBP and schema must agree); Products with accurate info.
- **Regular posts** (weekly cadence signals an active listing; keywords naturally).
- **Q&A**: Google is moving to **AI-generated Q&A** (answers drawn from profile/reviews/website, gated behind owner review) — keep underlying data accurate so AI answers are right, and **review AI-suggested answers before they publish**.
- **Messaging is being retired** (new conversations end July 15, 2026; fully ends July 31, 2026; WhatsApp replacement) — don't build process on it.
- **Hours**: accurate; set holiday hours BEFORE the holiday; open-at-search-time boost (§1).
- **Photos**: businesses with 100+ photos get more engagement; recency matters.
- **Description**: 750 characters; minimal ranking impact, affects conversion.
- **Website URL in GBP** must point to a page displaying the same NAP as the listing (the new homepage with footer NAP).

---

## 5. Content AI Prefers to Cite (ai-local-search §3) — Neighborhood & Team Pages

**The checklist, verbatim intent:**
- Clear, **factual statements** about services and capabilities
- **Lists of services with descriptions** (not just names)
- **Explicit geographic coverage statements** ("Team Azizi represents buyers and sellers in [Neighborhood A], [B], [C]...")
- **Pricing information where possible — "AI loves specifics"** (real-estate mapping: commission structure if shareable, median sale prices, price-per-sqft by neighborhood)
- **Credentials, certifications, years of experience — stated clearly** (licenses, designations, Compass affiliation, transaction counts, $ volume)
- **FAQ pages with direct question-and-answer format**
- **Avoid fluffy marketing copy — "AI extracts facts, not sizzle"**

**Neighborhood page spec (assembled from the skills):**
- One page per neighborhood, **unique substantial content** (no city-swap templates — Google devalues those)
- Fact-dense: market stats, price data, days-on-market, school/commute facts — the "specifics" AI cites
- Direct Q&A section answering "Should I buy in [neighborhood]?"-class questions, marked up with `FAQPage` (AI parsing, not rich results)
- `areaServed` entry for the neighborhood in the site schema; Wikipedia `sameAs` for the locality where one exists
- City/region in title tags and H1s; internal links between neighborhood pages ↔ service pages (skills: service pages linking to location pages and vice versa)
- These pages are the **ChatGPT/Perplexity citation targets** for informational "should I buy in X" queries and the relevance backbone for "best realtor in X"

**Website technical signals** (how-local-search-works): NAP footer on every page matching GBP exactly; local schema; mobile-responsive, fast, HTTPS, properly indexed; topical authority via comprehensive coverage of the domain.

---

## 6. Reviews as AI Input (ai-local-search §2 + how-local-search-works)

AI **reads and synthesizes review text** to form recommendations — sentiment and specifics, not just stars.
- **Volume** — more reviews = more data for AI; measured **relative to competitors** in the same market/category
- **Recency & velocity** — top-tier signal (2025–2026): reviews THIS MONTH matter more than lifetime total; rankings slip within weeks when reviews stop and recover when they resume; target a steady cadence (the skill's example: 80 reviews at 5–10/month beats 200 stale)
- **Diversity** — reviews mentioning different services and areas; **multi-platform** (Google + Yelp + industry sites > same count all-Google). Real-estate mapping: Google + Zillow + Yelp + Realtor.com
- **Specificity** — ask clients to name the service, neighborhood, and outcome ("sold our home in [neighborhood] over asking in 9 days") — review keywords reinforce relevance and feed AI summaries
- **Sentiment** — consistently positive across platforms; negative sentiment can surface in AI-generated characterizations (skill routes this to review-management)
- **Response rate** — Google confirms responding to reviews is a ranking factor (Tier A)
- Rating nuance: 4.5 vs 4.8 difference is minimal vs 3.5 vs 4.5; 50 reviews at 4.7 beats 3 at 5.0 for trust; photo reviews increase engagement; Local Guides reviews may carry more weight (unconfirmed/observed)

---

## 7. Citations, Directories, and Web Presence Breadth

- **"AI is bringing citations back."** AI models pull from diverse web sources to build entity understanding; citations give AI confidence to recommend. Citations/entity signals **weigh far more for AI than for the traditional pack** (entity-authority, Tier D).
- **Four data aggregators** cascade NAP downstream: **Data Axle (formerly Infogroup), Neustar/Localeze, Foursquare, Yelp** (Yelp is both directory and aggregator). Submit accurate data once, correct hundreds of directories.
- **Diminishing returns:** 0→50 quality citations = dramatic effect; 200→250 ≈ none. **Quality and consistency over count.**
- Structured (Yelp, BBB, Yellow Pages, industry directories) + **unstructured** (blog posts, news, event listings) both count; AI also reads **Reddit, Quora, niche blogs, news** — breadth of source types matters more for AI than directory count.
- **Bing Places** — ChatGPT pulls from Bing's index (separate bing-places skill exists for the full optimization).
- Brand-mention tactics (ai-local-search §4): local blogs/news/industry publications, consistent info everywhere, **local business roundups and "best of" lists**, authoritative industry directories, PR naming the business — all **earned** (§2.6 constraint).

---

## 8. Measuring AI Visibility (ai-local-search §Measuring)

**Tools:**
- **Local Falcon AI scans** — scan types for Google AI Overviews (GAIO) and AI Mode; platforms covered per the tools note: GAIO, ChatGPT, Gemini, Grok ("only option for geographic AI coverage")
- **SAIV metric — Share of AI Voice**: percentage of AI results mentioning the business
- **Manual testing** — run target queries in ChatGPT, Gemini, Perplexity on a schedule
- **Search Console** — AI Overview impressions/clicks (limited data); also branded-query volume as the entity KPI (§2.5)
- Live SERP tools for AI Overview detection (does an AIO trigger for a given query)

**What to track (the skill's exact list):**
1. Mentioned in AI results for target keywords? — **yes/no per platform**
2. **Sentiment** of AI-generated mentions
3. **Which sources AI cites** when recommending the business (this tells you which pages/profiles to strengthen — the agency's diagnostic loop)
4. **Competitor mentions** in the same AI results
5. **Changes over time** as you optimize

**Because zero-click is the norm (~58% click reduction on affected queries): report GBP actions (calls, direction requests, website clicks) and on-site conversions, not raw organic clicks.**

**Task-specific intake questions (skill's list, use verbatim in the agency's onboarding template):** Which AI platforms are priority? Target queries customers actually use? Current traditional local SEO state (GBP, reviews, citations)? Any existing AI scan data? Are competitors showing up in AI results?

---

## 9. Honesty Layer & Client Expectations (state these to Team Azizi)

- AI ranking factors are **less established** than traditional local SEO; platforms change data sources frequently; measurement tools are immature; **ROI attribution is difficult**; today's best practices may shift.
- **The skills' stated safest strategy:** optimize traditional fundamentals (GBP, reviews, citations, content, links) AND layer AI tactics (structured data, clear factual content, multi-platform presence). "What works for traditional local SEO mostly helps AI visibility too."
- Tier-label claims when reporting: entity clarity → AI visibility is **Tier D** (consensus, not measured); Google's earned-not-bought spam warning is **Tier A**; the 26%-Gemini and >50%-AIO figures are correlational/industry data (**Tier C**); open-at-search-time is **Tier B**; review responses as ranking factor is **Tier A**.
- Entity work is **slow-compounding infrastructure** — do not promise a fast AI-visibility jump from schema + sameAs alone.

## 10. Repeatable Agency Runbook (sequencing for customer #2 onward)

1. Intake with the 5 task-specific questions (§8) + canonical-identity decision (§2.1)
2. Baseline: manual AI query panel + Local Falcon GAIO/AI Mode scan + AIO-trigger check for the vertical (industry-rooted, so one check generalizes) + branded-query GSC baseline
3. GBP completeness pass (§4) — category, services w/ descriptions, hours, photos, posts cadence
4. Site build/retrofit: schema graph (§3) server-rendered, footer NAP, neighborhood + service pages to the citable-content spec (§5), FAQPage everywhere
5. Entity pass: sameAs array, aggregator submissions, Bing Places, knowledge-panel claim, Wikidata only if genuinely eligible
6. Ongoing engine: review velocity system + earned local mentions + monthly AI visibility report (SAIV, per-platform yes/no grid, cited-source analysis, competitor grid)
7. Validate schema at scale on releases (Screaming Frog custom extraction per the tools note); watch Search Console structured-data errors 2 weeks post-launch

# ==== top_10 ====

# Top 10 Highest-Leverage Moves for Team Azizi

1. **Lock one canonical identity before anything ships** — a single exact name/address/phone string ("Team Azizi – Compass" or "Team Azizi," pick once) enforced on GBP, site footer, Compass, Zillow, and every profile; inconsistency is the #1 way an entity fragments, and a fragmented entity is "invisible or wrong" to AI (Tier D).

2. **Baseline AI visibility now, before the rebuild launches** — run the manual query panel (ChatGPT/Gemini/Perplexity/AIO) for "best realtor in [each neighborhood]" + record SAIV, cited sources, and competitor mentions; as the agency's first customer, the before/after is the product.

3. **GBP completeness with the most specific real-estate primary category** — Gemini's primary data source is GBP and AI Overviews pull heavily from it; category is the single most impactful relevance signal and "relevance is binary before it's a spectrum."

4. **Ship the full schema graph server-rendered from day one** — `RealEstateAgent` with every template property (`@id`, `geo`, `areaServed` per neighborhood with Wikipedia `sameAs`, `hasOfferCatalog` with described services, complete `sameAs` array), unique `@id` per agent page linked via the `Organization`/`department` pattern; a greenfield rebuild is the one chance to get "completeness matters more than ever" for free.

5. **Build neighborhood pages as fact-dense citation targets** — unique substantial content (no city-swaps) with market stats, prices, and explicit coverage statements, because ChatGPT and Perplexity cite well-structured factual pages and "AI loves specifics"; these are the assets that win "should I buy in X neighborhood."

6. **Put direct Q&A + FAQPage markup on every neighborhood and service page** — FAQ rich results are dead (2026, Tier A) but FAQPage still aids AI parsing, and the direct question-answer format is exactly what AI extracts.

7. **Stand up a review velocity + specificity engine across Google, Zillow, and Yelp** — recency/velocity is a top-5 signal (5–10/month beats a big stale total), AI synthesizes review *text*, and multi-platform diversity beats same-count-all-Google; coach clients to name the neighborhood, service, and outcome.

8. **Claim and optimize Bing Places** — ChatGPT pulls from Bing's index, making this the cheapest single move for the highest-profile non-Google assistant.

9. **Earn (never buy) local brand mentions** — "best realtor in [city]" roundups, local news, community sponsorship coverage; brand mentions build AI's "knowledge" of the business, and Google's May 2026 AI-search guide makes bought mentions a stated spam risk (Tier A) — this is also the agency's compliance line.

10. **Submit to the four data aggregators (Data Axle, Neustar/Localeze, Foursquare, Yelp) + real-estate directories** — 0→50 quality citations has a dramatic effect with steep diminishing returns after, and AI's entity confidence is rebuilding the value of consistent citations.