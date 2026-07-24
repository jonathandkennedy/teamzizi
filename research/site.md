

# ==== market_summary ====

Team Azizi is a 15-agent Compass-affiliated real estate team (Principal: Nilab Azizi, CA DRE# 02047962; brokerage: Compass California III, Inc., CA DRE# 01527365) serving San Diego County, California, positioned as luxury specialists ("Top 1% in SD County, $90M+ 2024 volume, 82 units sold in 2024"). Office: 12860 El Camino Real Ste 100, San Diego CA 92130 (Carmel Valley/Del Mar area). Their site claimed neighborhood expertise in exactly six North San Diego communities: Carmel Valley, Del Mar, Rancho Santa Fe, Del Sur, 4S Ranch, and Scripps Ranch — though their listing/sold inventory spans all of San Diego County (Oceanside, Escondido, Chula Vista, Carlsbad, La Jolla, etc.). The old site was built on Luxury Presence (footer credit "Real Estate Website Design by Luxury Presence"; lp-cdn.com media; built-in Luxury Presence home-search/IDX portal fed by San Diego MLS).

# ==== neighborhoods ====

[
  "Carmel Valley",
  "Del Mar",
  "Rancho Santa Fe",
  "Del Sur",
  "4S Ranch",
  "Scripps Ranch"
]

# ==== sitemap ====

## Full URL inventory (from 5 sitemap XMLs + CDX; ✓ = real Wayback capture exists, ✗ = never archived)

### Static pages (sitemap-static.xml)
- `/` ✓ — Homepage: hero, stats, buy/sell CTAs, team intro, testimonials carousel, newsletter, neighborhood guides, valuation widget, featured properties, Instagram feed
- `/404` — custom 404 page (in sitemap)
- `/blog` ✓ — Blog index listing 4 posts
- `/buyers-guide` ✗ — Buyer's guide (nav label "Buyers Guide")
- `/concierge` ✗ — Compass Concierge page (nav label "Compass Concierge")
- `/contact` ✓ — Contact page ("Let's Connect") with lead form + NAP
- `/home-valuation` ✗ — Home valuation landing page (instant-valuation widget)
- `/neighborhoods` ✓ — Neighborhood guide hub with 6 "EXPLORE [name]" cards
- `/properties/sale` ✗ — "Featured Properties" (active listings index)
- `/properties/sold` ✗ — "Past Transactions" (sold listings index)
- `/renovation-case-studies` ✗ — Renovation case studies page
- `/sellers-guide` ✗ — "Seller's Guide"
- `/team` ✓ — "Meet the Team" agent roster (15 cards) + testimonials + featured properties
- `/terms-and-conditions` ✓ — Privacy Policy (Luxury Presence boilerplate, ~4,000 words)
- `/testimonials` ✗ — Testimonials page
- `/home-search/listings` ✗ — IDX search (Luxury Presence home search)
- `/home-search/account` — "My Search Portal" login (CDX shows 307); `/home-search/auth/sign_in` ✓ captured
- `/profile` — profile/account page (linked in nav)

### Neighborhood pages (sitemap-neighborhoods-dpages.xml)
- `/neighborhoods/carmel-valley` ✗
- `/neighborhoods/del-mar` ✗
- `/neighborhoods/rancho-santa-fe` ✗
- `/neighborhoods/del-sur` ✗
- `/neighborhoods/4s-ranch` ✗
- `/neighborhoods/scripps-ranch` ✓ — only neighborhood page archived (template reference for the other 5)

### Blog posts (sitemap-blog-dpages.xml) — all ✗ (titles/dates from /blog index)
- `/blog/compass-concierge-for-del-mar-listings-what-to-expect` — "Compass Concierge For Del Mar Listings: What To Expect" (01/1/26)
- `/blog/adus-in-scripps-ranch-what-homeowners-should-know` — "ADUs In Scripps Ranch: What Homeowners Should Know" (12/18/25)
- `/blog/closing-costs-explained-for-del-sur-buyers` — "Closing Costs Explained For Del Sur Buyers" (12/4/25)
- `/blog/mello-roos-vs-hoa-in-4s-ranch` — "Mello-Roos vs HOA In 4S Ranch" (11/21/25)

### Agent pages (sitemap-agent-dpages.xml) — all ✗ (names/DRE from /team)
- `/agent/nilab-azizi`, `/agent/zohra-azizi`, `/agent/sofia-azizi`, `/agent/candace-kirk`, `/agent/candice-casares`, `/agent/coby-herzog`, `/agent/dari-ahranjani`, `/agent/deanna-colby`, `/agent/gabriela-santiago`, `/agent/jared-stransky`, `/agent/melissa-lopez`, `/agent/michael-angotta`, `/agent/nicholas-miele`, `/agent/sara-forgnone`, `/agent/sarah-rivas`

### Property pages (sitemap-properties-dpages.xml) — ~100 URLs, all ✗
Pattern: `/properties/[street-address]-[city]-ca-[zip]-[mls-id]` (e.g. `/properties/8337-summit-way-san-diego-ca-92108-250046401`). Mix of active (3 at capture: 8337 Summit Way $1,525,000; 4495 Montalvo St $1,250,000; 3252 Via Marin #9 La Jolla $985k) and ~97 past-transaction pages across San Diego County.

### Legacy
- 2020 capture of `http://teamazizi.com/` was a placeholder (424 bytes); current LP site dates from ~2022 (footer "Copyright © 2022").

# ==== content_inventory ====

## Content by page (captured pages; word counts = visible text incl. nav/footer)

### Homepage (~2,000 words)
- H1 "Team Azizi"; hero nav CTAs: Featured Properties, Past Transactions, Neighborhoods, Home Search, Home Valuation, "CONTACT US (858) 847-8067"
- H2 "California Real Estate Experts" + stat tiles: "Top 1% in SD County", "$90M+ 2024 Volume – Sales & Referrals", "82 2024 Units Sold"
- Dual CTA cards: "Selling A Home? Find out what your home is really worth → Get Home Value" / "Buying A Home? Browse our exclusive properties → View Properties"
- "Meet The Team" blurb (negotiation skills, tailor-made marketing plans, buyer strategy, network) → learn more
- Testimonials carousel (7 reviews): Neva (Nilab), Tiffany V. (Sofia), Yohanna G. (Nilab), Edgar V. (Melissa), Troy T. (Sofia), Yuri P. (Nilab), Damjmtc (Melissa)
- Newsletter signup: "Receive Exclusive Listings In Your Inbox"
- "Browse Our Neighborhoods Guides" — 6 neighborhood cards
- "How Much is Your Home Worth?" instant-valuation widget (Luxury Presence AVM: "Instant property valuation / Expert advice / Sell for more")
- "Featured Properties" carousel (3 active listings with BD/BA/SqFt/price)
- "Work With Us" CTA block + Instagram feed section
- Footer lead form + full NAP + Compass/MLS disclaimers

### /neighborhoods (~800 words, thin)
- H1 "Neighborhoods"; 6 image cards ("EXPLORE Carmel Valley" etc.); "Start Your Property Search" CTA; standard footer form

### /neighborhoods/scripps-ranch (~1,600 words) — the neighborhood template (Luxury Presence)
- H1 "Discover Scripps Ranch Real Estate – Your Luxury Home Awaits" + geo coords "32.8932° N, 117.0676° W"
- Embedded IDX "Property Listings" module with filters (property type, beds, baths, price, living area) showing live San Diego MLS inventory for 92131
- "Overview for Scripps Ranch, CA" — US Census demographics (pop 20,326, median age 47, avg income $73,172)
- "Around Scripps Ranch, CA" — Walk Score/Bike Score + Yelp points of interest
- "Demographics and Employment Data" and "Schools in Scripps Ranch, CA" data modules
- "Similar Neighborhoods" carousel linking the other 5 → good interlinking
- NOTE: almost all content is third-party data widgets; little unique editorial copy

### /team (~1,700 words)
- H1 "Meet the Team"; 15 agent cards (photo, name, title, license, LEARN MORE → /agent/ page):
  Nilab Azizi (Principal, CA DRE 02047962), Zohra Azizi (01992847), Sofia Azizi (02108624), Deanna Colby (02182003), Candace Kirk (02059754), Candice Casares (#02160651), Coby Herzog (02011079), Dari Ahranjani (02130344), Gabriela Santiago (01955750), Jared Stransky (02081146), Melissa Lopez (01329108), Michael Angotta (02177007), Nicholas Miele (02089615), Sara Forgnone (02045480), Sarah Rivas (02112696)
- Agent emails (in page data): all @compass.com (nilab.azizi, zohra.legler, sofia.azizi, deanna.colby, candace.kirk, candice.casares, coby.herzog, dari.ahranjani, gabriela.santiago, jared.stransky, melissa.lopez, michael.angotta, nick.miele, saraforgnone, sarah.rivas)
- Testimonials + Featured Properties repeated

### /blog (~850 words, thin)
- H1 "Blog"; 4 post cards with dates; newsletter CTA

### /contact (~890 words)
- H1 "Let's Connect"; lead form: Name, Email, Phone, Message, "Interested in..." dropdown (Selling & Buying / Selling / Buying / Renting / Other), TCPA consent checkbox ("...automated calls, texts, and emails... artificial or prerecorded voices...")
- "Submit a Message — Fill out the form below to learn more about buying or selling a house in your area. Nilab Azizi | CA DRE# 02047962"
- Quick links: Properties, Meet The Team, Home Search

### /terms-and-conditions (~4,050 words)
- H1 "Privacy Policy" — stock "PRIVACY POLICY FOR INDIVIDUALS INTERACTING WITH LUXURY PRESENCE CLIENTS"

## Site-wide elements
- Global nav: Home, Home Valuation, Home Search, Meet the Team, Featured Properties, Past Transactions, Neighborhoods, Renovation Case Studies, Buyers Guide, Seller's Guide, Compass Concierge, Testimonials, Blog, Contact Us, My Search Portal
- Footer NAP block: "Team Azizi | CA DRE# 02047962 / Phone (858) 847-8067 / Email nilab.azizi@compass.com (Cloudflare-obfuscated) / Address 12860 El Camino Real Ste 100, San Diego CA 92130"; secondary block "Nilab Azizi | CA DRE# 02047962 / Compass California III, Inc. | CA DRE# 01527365 / O: (858) 345-4514"
- Footer lead form on every page (two-step: message → interest qualifier) + newsletter form
- Compass equal-housing + San Diego MLS disclaimer; "Real Estate Website Design by Luxury Presence"; "Copyright © 2022"
- Socials: facebook.com/TeamAziziRealEstate, instagram.com/teamazizi_realestate (YouTube channel @soniaazizi9469 appears in page data)
- IDX: Luxury Presence native home search (/home-search/listings + /home-search/account portal), San Diego MLS feed; neighborhood pages embed filtered IDX modules

## NAP summary
- Team: Team Azizi (team license #02160651 also appears); Principal: Nilab Azizi, CA DRE# 02047962
- Brokerage: Compass California III, Inc., CA DRE# 01527365
- Phones: (858) 847-8067 (primary), (858) 345-4514 (office)
- Email: nilab.azizi@compass.com; Address: 12860 El Camino Real Ste 100, San Diego CA 92130

## Not recoverable from archive
Buyers/Sellers guides, Concierge, Home Valuation page, Testimonials page, Renovation Case Studies, all 15 agent bio pages, all 4 blog post bodies, 5 of 6 neighborhood pages, all property pages — never captured. Only titles/URLs/template structure are known.

# ==== seo_observations ====

## Title tags (captured pages)
- `/` — "San Diego Real Estate – Discover Luxury Homes with Team Azizi"
- `/blog` — "San Diego, CA Real Estate Tips & More | Team Azizi"
- `/contact` — "Get In Touch | Team Azizi Serving San Diego, CA."
- `/neighborhoods` — "Best Places to Live in California | Team Azizi" (weak: targets state-level, not San Diego)
- `/team` — "Meet The Team | Real Estate Experts Serving California" (same issue)
- `/terms-and-conditions` — "Privacy Policy | Team Azizi Serving San Diego, California" (URL/title mismatch: privacy policy lives at a terms URL)
- `/neighborhoods/scripps-ranch` — "Explore Scripps Ranch Real Estate – Luxury Living Awaits"; H1 "Discover Scripps Ranch Real Estate – Your Luxury Home Awaits"

## Meta descriptions
Present and keyword-written on /, /contact, /neighborhoods, /team, scripps-ranch. MISSING on /blog. Contact page description written in first-person singular ("I look forward...") — inconsistent with team branding.

## Schema markup
NONE anywhere — zero JSON-LD, zero microdata across every captured page. Only OG tags + twitter:card (summary_large_image) + self-referencing canonicals. Rebuild opportunity: RealEstateAgent/LocalBusiness (NAP + DRE), Person schema per agent, BlogPosting, BreadcrumbList, FAQPage on guides, Residence/Offer on listings.

## Sitemaps / crawl
- Five split sitemaps: sitemap-static.xml, sitemap-neighborhoods-dpages.xml, sitemap-blog-dpages.xml, sitemap-agent-dpages.xml, sitemap-properties-dpages.xml (no captured sitemap index; /sitemap.xml on www 404'd in 2024)
- ~140 total URLs: 16 static + 6 neighborhoods + 4 blog + 15 agents + ~100 properties
- /404 page included in sitemap (minor hygiene issue); robots.txt returned 500 in old captures

## Internal linking
- Strong global nav to all money pages; neighborhoods hub → 6 child pages; each neighborhood page cross-links all siblings via "Similar Neighborhoods" carousel (good silo)
- Blog posts are keyword-aligned to the 6 farm neighborhoods (Del Mar, Scripps Ranch, Del Sur, 4S Ranch) — hub-and-spoke already in place; preserve slugs exactly
- Homepage links 3 property detail pages + neighborhoods + team

## Preservation notes for rebuild
1. Preserve exact URL paths: /neighborhoods/[slug], /blog/[slug], /agent/[slug], /properties/[addr-mls], /buyers-guide, /sellers-guide, /concierge, /home-valuation, /renovation-case-studies, /testimonials, /properties/sale, /properties/sold, /contact, /team, /terms-and-conditions — or 301 all of them
2. Neighborhood pages were data-widget-heavy (Census/WalkScore/Yelp/schools/IDX) with thin unique copy — biggest content-upgrade opportunity while keeping URL equity
3. Footer NAP + DRE + Compass disclaimer appears sitewide — must be reproduced exactly for E-E-A-T and compliance (Nilab DRE 02047962, Compass California III DRE 01527365, both phones, El Camino Real address)
4. Stale "Copyright © 2022"; title-tag geo inconsistency (California vs San Diego) worth normalizing to San Diego / North County terms
5. Old platform: Luxury Presence — IDX portal URLs (/home-search/*) are platform-specific and will break unless the new stack replicates or redirects them