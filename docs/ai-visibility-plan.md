# AI visibility plan

**Written 2026-08-04, the day DNS pointed.** Every number here was measured that
day against the live site and live SERPs, not estimated. OpenSEO project:
`teamazizi.com` (`af9cee88-201c-4d8b-a27b-fbe939c8a01a`).

The goal this document plans for is the one the client stated: **rank on, and be
named in, high-intent AI answers** — Google's AI Overviews and AI Mode, and
assistant retrieval in ChatGPT, Perplexity and Claude. Not traffic for its own
sake. Being the answer.

---

## 1. Where we actually stand

The site went live today. `teamazizi.com` serves the build from Vercel, 85 URLs
in the sitemap, `robots.txt` explicitly admitting `OAI-SearchBot`,
`PerplexityBot`, `Claude-SearchBot`, `Google-Extended` and `bingbot`, and the
IndexNow key file returning 200 — so IndexNow can finally fire, which it could
not while DNS was dead.

`HANDOFF.md` still said "DNS not pointed" when this was written. That line is
now wrong and has been corrected.

**The site is invisible, and the brand query proves it.** Searching
`team azizi compass san diego` returns twenty results and *the site is not one
of them*. What ranks instead:

| # | What Google returns for their own name | |
|---|---|---|
| 1 | compass.com/agents/team-azizi | Compass-controlled |
| 2 | linkedin.com/in/soniagazizi | |
| 3 | zillow.com/profile/nilabazizi | 4.9★, 9 reviews |
| 4 | instagram.com/teamazizi_realestate | |
| 5 | realtrends.com team profile | "conducting business in Del Mar" |
| 6 | facebook.com/TeamAziziRealEstate | |
| 9 | homes.com — Sonia Azizi | **listed under "Upstart Residential"** |
| 14 | yelp.com — SONIA AZIZI - TEAM AZIZI | |
| 19 | psar.org — Zohra Azizi Legler | |

Ten third-party profiles own the brand. This is exactly the "corrupted brand
answers" problem HANDOFF recorded as the accepted cost of the
foundation-before-DNS sequencing. The bill has now come due, and the fix is
Phase 0 — not more content.

---

## 2. What the SERPs actually do

Six high-intent queries pulled live. The finding is unambiguous:

**An AI Overview fires at rank 1 on 5 of 5 informational queries tested.**

| Query | AI Overview? | Volume | KD | CPC |
|---|---|---|---|---|
| best real estate agent san diego | **yes, rank 1** | 390 | **8** | **$10.13** |
| mello-roos tax | **yes, rank 1** | 2,400 | **1** | $0.94 |
| how to find a real estate agent | **yes, rank 1** | 1,600 | 20 | $23.35 |
| mello roos tax lookup | **yes, rank 1** | 390 | 11 | $1.65 |
| how much is mello-roos tax | **yes, rank 1** | 70 | 0 | — |
| carmel valley san diego realtor | no — local pack | — | — | — |

Two rules fall out of that table, and they drive everything below.

**Rule one: question-shaped queries are answered by an AI, local-shaped queries
are answered by a map.** "How much is Mello-Roos" gets an AI Overview. "Carmel
Valley realtor" gets a three-slot local pack — `carmelvalley.com`, Felicia Lewis
Group, Coldwell Banker — and no AI Overview at all. These are two different
machines and they need two different pieces of work. Content wins the first. A
Google Business Profile wins the second, and nothing else does.

**Rule two: `best real estate agent san diego` is winnable.** KD 8 at $10.13 a
click, with an AI Overview on top. The agents who rank on it — Scott Cheng,
Best Life Home Team, Greg Cummings — share one visible trait: **the review count
is in the title tag.** "295+ Five-Star Reviews." "over 150 Google verified
five-star reviews." That is what this SERP rewards, and it is a Phase 2 asset,
not a content asset.

### Who the AI is reading

For "best agent" queries the organic results *are* the AI's source list:
Reddit (#5), U.S. News, Zillow, RealTrends, Compass, FastExpert, Realtor.com,
Yelp, HomeLight. An assistant asked "who's the best realtor in San Diego"
synthesises from those pages. **You do not get named in that answer by writing a
page on your own site.** You get named by being in those sources, with reviews.

---

## 3. The one thing blocking everything

> **Every form on the live site posts to `https://formspree.io/f/PLACEHOLDER`.**

This was a pre-launch gate. The moment DNS pointed it became live lead loss —
buyers, sellers, agent applicants and visibility-check requests all submitting
into nothing, with a success message. It is a one-line change in `build/site.py`
once the Formspree ID or CRM webhook exists.

Nothing in this plan returns anything until that line is real.

---

## 4. The content architecture is already built

Worth stating plainly, because it changes what the next month should be spent
on: **the fan-out work is done.**

`build/data/fanout.py` already models how AI Mode decomposes a query into
synthetic sub-queries and retrieves passages rather than pages. It carries a
14-class reusable spine — median price, Mello-Roos, effective tax rate, HOA,
school district, attendance boundaries, housing stock, commute, pros and cons,
and `best real estate agent in {name}` — plus **researched community-specific
sub-queries for all 31 guides. Coverage is 31 of 31.** `validate.py` enforces
the passage rules: no anaphora in a lead answer, name the entity inside the
block.

So the honest read is: we are not content-blocked. We are **retrieval-blocked
and entity-blocked.** Phases 0 and 2 are where the next month's value is, and
Phase 1 is the one content lane with a genuinely open door.

---

## 5. Phase 0 — become retrievable (this week)

Nothing can cite a page it has never fetched.

1. **`LEAD_ENDPOINT`.** Above. Blocks everything.
2. **Submit the sitemap in Search Console** and request indexing on the twelve
   highest-intent URLs by hand — homepage, `/mello-roos/`, the six original
   community guides, `/sell/`, `/buy/`, `/join`, `/careers`.
3. **Connect GSC to OpenSEO.** The property exists on Google's side but OpenSEO
   holds no OAuth grant, so first-party query data is unavailable to the tooling:
   https://app.openseo.so/p/af9cee88-201c-4d8b-a27b-fbe939c8a01a/search-performance
4. **Bing Webmaster Tools — separate setup, and not optional.** ChatGPT's
   retrieval leans on Bing's index. A site absent from Bing is absent from
   ChatGPT regardless of how it does in Google. Import from GSC, submit the
   sitemap.
5. **Fire IndexNow.** `build/indexnow.py` will now succeed — the key file
   returns 200. Bing, Yandex, Seznam, Naver. Google does not participate; this
   accelerates discovery and does not cause ranking.
6. **Re-verify the ~10 surviving legacy URLs 301 correctly** now that DNS
   resolves. That index equity is decaying and the window closes.

**Done when:** `site:teamazizi.com` returns the sitemap's URLs, and the brand
query returns the site in the top 3 rather than ten profiles of it.

---

## 6. Phase 1 — the Mello-Roos wedge

This is the one lane where the door is open, and the SERP shows exactly why.

Look at who ranks for `mello-roos tax` and `mello roos tax lookup` beneath
Investopedia, Wikipedia and the county: **individual agents who own one
district each, in someone else's market.**

- `cherielliott.com` — El Dorado, Sacramento, Placer
- `lisamlum.com` — "Mello-Roos District Lookup | San Mateo & Santa Clara"
- `homesbyverso.com` — "Irvine HOA & Mello-Roos Costs (2026)"
- `daftariangroup.com` — Turtle Ridge
- `refinedre.com` — Mountain House
- `valerievicente.com` — San Ramon
- `35oakspropertygroup.com` — Valencia
- `melloroosmap.com` — "enter any **Riverside County** parcel number"

Every one of those is a smaller operation than Team Azizi winning a national
informational SERP by being specific about one place. **Nobody occupies San
Diego County at that granularity.** The county's own page (`sdarcc.gov`) ranks
but is a bare institutional stub, and it is the top non-encyclopedia result —
which means the demand is real and the satisfying answer does not exist.

Team Azizi is unusually well-placed: HANDOFF records that the county CFD list
has already been read in full, `/mello-roos/` exists and names CFD 98, CFD 2000,
CFD 2013, CFD 2015 and CFD No. 2019-1, and two posts already sit underneath it.

Three things to build, in order:

1. **Per-district answer pages.** One extractable passage per CFD: what it
   funds, the annual range, when the bonds retire, which neighborhoods sit
   inside it. This is precisely the passage shape `fanout.py` already
   specifies — lead with the number, name the district in the sentence.
2. **A parcel/address lookup.** `melloroosmap.com` ranks on exactly this for
   Riverside; a Reddit thread asking for a Sacramento version ranks too. It
   needs **no MLS licence and no IDX** — Mello-Roos is public assessor data, so
   it sits entirely outside the no-IDX decision. Highest-effort item here and
   the most defensible.
3. **The expiry question.** "How to find out when Mello-Roos expire" and
   "4s ranch mello roos end date" both have volume at KD 0. Nobody answers them
   per-district. Team Azizi can.

Why this is the right wedge and not a detour: Mello-Roos is a **factual** query
with a **verifiable** answer, which is what assistants cite most readily, and it
is the exact question a $1.5M Carmel Valley buyer asks before writing an offer.
Informational query, transactional audience.

---

## 7. Phase 2 — entity trust (the "few days" work)

The client has this scheduled and it is correctly scheduled — but it is not
secondary. Section 2 showed the local pack and the "best agent" AI answers are
gated on it and on nothing else.

### The NAP is genuinely broken

Not "needs tidying". These are live conflicting records found today:

| Source | Address | Phone |
|---|---|---|
| Compass | — | 858-847-8067 |
| Yelp | 10550 Craftsman Way Ste 184, SD 92127 | (619) 929-9691 |
| Realtor.com (Nilab) | 12860 El Camino Real Ste 100, 92130 | — |
| Instagram bio | 35335 Ponderosa Pl, **Fallbrook** | — |
| PSAR (Zohra) | — | (619) 876-0110 |
| The live site | — | (858) 201-2899 (call tracking) |

**Four addresses across three cities, five phone numbers, and homes.com has
Sonia under the wrong brokerage entirely — "Upstart Residential", not Compass.**
PSAR's web field is mangled to `Zohra.Teamazizigmail.com`.

An assistant asked "is Team Azizi in Carmel Valley or Fallbrook, and what's
their number" cannot answer confidently, so it names a competitor it *can*
resolve. That is the mechanism by which this costs money.

### Order of work

1. **Pick the canonical NAP first** — one address, one phone, one name string.
   Everything else is a rewrite against that record. Do not start corrections
   before this is decided.
2. **Google Business Profile.** The only route into the local pack. Categories,
   service areas covering the 31 guide areas, and the profile linked to the
   matching guide URL rather than all to the homepage.
3. **Fix the wrong records in priority order** — homes.com's brokerage error
   first (it is factually false), then Yelp, PSAR, Realtor.com, Instagram.
4. **Reviews, and put the count in the title tag.** Section 2 showed this is the
   visible differentiator among agent sites ranking for the money query. Zillow
   currently shows 9 reviews on Nilab's profile.
5. **The directories that AI cites** — U.S. News, RealTrends, FastExpert,
   HomeLight, Zillow. Claimed and complete. These are the AI's sources for
   "best agent in San Diego"; a page on our own domain is not.

### Reddit, honestly

Reddit ranks #5 for `best real estate agent san diego`, #2 for `how to find a
real estate agent`, and drives the `discussions_and_forums` and `perspectives`
blocks. Assistants weight it heavily for recommendation queries.

The only version of this worth doing is genuine participation — answering
Mello-Roos and CFD questions in r/sandiego where the team actually knows the
answer, under a real identity. Seeded recommendations violate Reddit's rules,
are detectable, and the downside is a permanent, searchable accusation attached
to the brand name. Recorded here so the tempting version is a decision someone
made, not an oversight.

---

## 8. Phase 3 — knowing whether it worked

Rankings are a lagging and increasingly partial measure; an AI Overview can
answer a query using our passage while sending no click at all.

- **Rank tracking** on the Phase 1 and Phase 2 targets, weekly.
- **GSC impressions on question-shaped queries** — the leading indicator of
  fan-out retrieval, and it moves before positions do.
- **Direct assistant checks**, monthly, logged with dates: ask ChatGPT,
  Perplexity, Claude and Google AI Mode the ten money questions and record
  whether Team Azizi is named and what is cited. This is the actual scoreboard.
  The site already ships an AI visibility check as a lead magnet — run the same
  discipline on ourselves.
- **Baseline is today, and today is zero**, on a brand query that returns ten
  profiles and not the site. That makes the next 90 days unusually easy to read.

---

## 9. Decisions needed

1. **The Formspree ID or CRM webhook.** Blocks every form on a live site.
2. **Canonical NAP** — one address, one phone. Everything in Phase 2 waits on it.
3. **Is the Mello-Roos lookup tool in scope?** Highest effort here, most
   defensible asset, needs no MLS licence. A yes reorders the next month.
4. **Who answers Reddit**, if anyone. A real person with a real account, or we
   skip the channel.
5. **Privacy policy**, still outstanding, still required before the live forms
   collect anything.
