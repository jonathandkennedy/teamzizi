# Competitor review-mining brief — Whissel Beer Group (+ the direct set)

For a run from a **local machine on a residential IP**, with a normal browser.
Every source below is public. Nothing here requires an account, a purchase, or
interacting with any listing, reviewer or agent.

**Why this can't run from the build container:** Yelp, Zillow, FastExpert and
whisselbeergroup.com all return **403 to datacenter egress** — the same wall
`research/communityVoice.md` §1 documents for Reddit. The pages load normally
from a residential IP. This is an access problem, not a permissions one.

**Not a `/last30days` job.** That skill covers Reddit/X/YouTube/HN — social
listening, not review platforms. Either read these in a browser and paste the
text back, or run Claude Code locally in this repo and re-issue the same
fetches; from a residential IP they should succeed.

**Return format:** structured rows (table, JSON or CSV), one per review, not
prose summaries.

**Ground rule:** capture verbatim. The value here is the reviewer's own
phrasing — the words people use for their fears are the words they type into
search. A paraphrase destroys exactly the signal we're mining.

**Per review, capture:** star rating · date · buyer or seller · city or
neighborhood · agent named · full body text.

---

## Already established — do not redo

Pulled 2026-08-04 from the sources that *are* reachable. Roughly 16 reviews of
real text, **every one 5-star**, against a corpus of 3,000+.

| Source | Count | Rating | Status |
|---|---|---|---|
| [experience.com](https://www.experience.com/reviews/kyle-17093498) | 427 (page also says 447 — reconcile on the run) | **4.97** | ✅ read, 10 reviews |
| [Birdeye](https://reviews.birdeye.com/whissel-realty-group-169588162309532) (Google mirror) | 125–146 (both figures appear) | 5.0 | ✅ read, 6 reviews |
| [BBB](https://www.bbb.org/us/ca/san-diego/profile/real-estate-agent/whissel-realty-1126-172000460) | 1 review | A+, **not accredited** | ✅ read |
| [Yelp — San Diego](https://www.yelp.com/biz/whissel-beer-group-san-diego) | 92 | — | ❌ 403 |
| [Zillow — Kyle Whissel](https://www.zillow.com/profile/KyleWhissel) | 1,968 | claimed all 5-star | ❌ 403 |
| [FastExpert](https://www.fastexpert.com/agents/whissel-realty-group-with-kyle-whissel-8432/) | — | — | ❌ 403 |

**What the 4.97 tells us before anyone reads a word.** 427 reviews at a
perfect 5.0 would total 2,135 star-points; 4.97 totals ≈2,122. That is a
**deficit of ~13 star-points** — somewhere between ~3 one-star reviews and ~13
four-star ones. Small, finite, and findable in a single sort. That handful is
the most valuable text in the entire corpus and it is the whole point of
Tier 1.

**Corpus is fragmented across multiple Yelp entities** — worth capturing all
of them, because the negative tail may sit on a listing that isn't the main
one:

- [Whissel Beer Group — San Diego](https://www.yelp.com/biz/whissel-beer-group-san-diego) (92 reviews)
- [Whissel Realty Group at eXp — Santee](https://www.yelp.com/biz/whissel-realty-group-at-exp-realty-santee) (89 reviews)
- [Whissel Realty Group — Temecula](https://www.yelp.com/biz/whissel-realty-group-temecula/)
- [Kimo Quance with Whissel — La Mesa](https://www.yelp.com/biz/kimo-quance-with-whissel-realty-group-la-mesa) (41 reviews)
- [Warren Hill — Whissel](https://www.yelp.com/biz/warren-hill-whissel-realty-group-san-diego)

---

## Tier 1 — the negative tail ★ highest value, do this first

### 1. Every sub-5-star review, all platforms

**Yelp:** sort by **"Lowest Rated"** on each of the five listings above. Also
open **"Reviews that are not currently recommended"** at the page foot — Yelp
filters a large share of reviews out of the main feed, and for a business with
a near-perfect public rating that hidden set is often where the substance is.

**Zillow:** the profile carries 1,968 reviews and is claimed to be 100%
five-star. **Verify that claim** — if true it is itself a finding (a corpus
that clean is curated, and worth knowing about a competitor). If false,
capture every exception.

**Google:** sort reviews by **Lowest** on the Maps listing.

*Why:* everything reachable from here is 5-star, so the analysis so far can
describe what clients *praise* but cannot honestly describe what goes wrong.
This tier is the half of the picture that is currently missing. Complaints
also name the specific failure — a missed disclosure deadline, a rushed
inspection, an unreturned call during escrow — and specifics are what content
can actually answer.

### 2. Owner responses to negative reviews

Capture the response text alongside each complaint, and whether a complaint
went unanswered.

*Why:* how a competitor handles a public complaint is a positioning tell, and
an unanswered one-star review on a team this large is a real gap.

---

## Tier 2 — the anxiety signature at volume

### 3. Mine the 5-star reviews for the fear they name

In a curated corpus the thing a reviewer praises is the thing they walked in
afraid of. That inversion holds and it is well-evidenced even in the 16
reviews already read. Recurring so far — **confirm or overturn these at
volume**, and count frequency:

- **Search fatigue / attrition.** *"Finding a home can feel extremely
  stressful in today's market, taking several months. We had given up"*
- **Fear of being pressured.** *"she never pressured us into anything, but was
  really patient with us on our search"* — named unprompted
- **Paperwork opacity.** *"a very stressful process... endless questions and
  paper work"*
- **First-timer exposure.** *"our first time selling a house... made it so
  much easier than we expected"*
- **Deals blowing up mid-escrow.** *"smoothly navigated tricky problems each
  time they popped up"*
- **Responsiveness.** *"communication was exceptional; always timely, clear"*
  — the single most repeated praise, therefore the most common failure
  elsewhere

For each theme, return a **count and the three most vivid verbatim quotes**.
Frequency is what separates a real pattern from one memorable review.

### 4. Agent-attribution pattern

Every review read so far names an individual agent — twelve different ones
across sixteen reviews. Capture the named agent on each review and check
whether that holds at volume.

*Why:* on a 160-agent team, review text that always names one person is a
deliberate answer to *"will I be handed to a junior?"* Confirming it at scale
tells us whether it is orchestrated or incidental — and it is the objection
Team Azizi answers structurally, with one named licensee per community.

### 5. Neighborhood and price-band distribution

Tag each review with the city/neighborhood named. Note especially anything in
the six-community footprint (Carmel Valley, Del Mar, Rancho Santa Fe, Del Sur,
4S Ranch, Scripps Ranch).

*Why:* `research/competitors.md` records Whissel as the countywide-scale
player with a Scripps Ranch page aimed at one of the six. Whether their review
book actually reaches into the corridor — or stops at El Cajon, La Mesa,
Santee, Murrieta, San Marcos, as the sample so far suggests — decides whether
they are a genuine threat in the footprint or a volume brand adjacent to it.

---

## Tier 3 — the objection map

### 6. Confirm and extend the productized objections

A competitor's objection-handling content is a map of the objections their
market raises. Four are already documented — **verify the wording on-page and
look for others**:

1. **"I'll be locked in with an agent who underperforms."** → their **Easy
   Exit / Cancellation Guarantee**. They state the objection themselves:
   *"most listing agreements in California bind a seller to a specific agent
   for a set period, typically 90 to 180 days, regardless of the agent's
   performance."*
2. **"Why pay full commission when discount brokers exist?"** →
   [their commission breakdown](https://whisselrealty.com/blog-page/2021/7/22/the-breakdown-of-real-estate-commissions):
   *"when you pay a discounted commission, you tend to get a discounted
   service."*
3. **"Do I have to sign something just to tour a home?"** → a client
   references signing a representation agreement before touring. This is the
   live post-NAR-settlement objection.
4. **"When does my home actually hit the market?"** → branded
   [Seven Day Listing Launch™](https://whisselbeergroup.com/blog/seven-day-listing-launch-explained/).

Also capture **Home Match™** and any other branded program, verbatim.

### 7. Google Business Profile Q&A — the actual questions

Reviews record outcomes, not questions. GBP Q&A records questions, in the
asker's own words.

Two routes. In a browser: the **Questions & answers** panel on the Maps
listing, expanded fully. Or via OpenSEO `get_google_business_questions` —
**blocked today** because there is no `teamazizi` project in the org (only
justiceondemand, planatek, citedrealty, mmbonding, retainerreach), so the call
would bill credits against an unrelated project. Creating the project unblocks
it and is worth doing anyway.

### 8. Extend to the two direct competitors

Whissel is countywide scale. The teams fighting for the *same six
neighborhoods* matter more per review:

- **Felicia Lewis Group** — most direct competitor per `competitors.md`;
  claims 150+ five-star reviews (Google/Zillow linked in their footer)
- **O'Byrne Team** — same Compass office as Team Azizi; ~131 Yelp reviews

Same capture rules, Tier 1 first. A hundred reviews from a Carmel Valley
specialist outweigh two thousand countywide.

---

## What this feeds

- **Two gaps `competitors.md` already flags as unclaimed** get evidence: the
  on-page FAQ/Q&A layer (nobody in the set has one) and the buyer-question
  surface AI assistants cite.
- **The pressure/representation-agreement objection** is answered by no one in
  the competitive set. Post-settlement, in plain English, it is an unclaimed
  high-intent page.
- **Search fatigue** is the emotional spine of the buyer journey and nothing
  across the 31 guides currently speaks to it.
- **The lock-in objection** is a positioning decision for the client, not a
  content one — Whissel has neutralized it with a guarantee. Flag it; don't
  answer it unilaterally.

Return the raw rows rather than conclusions. The synthesis belongs in
`research/`, written against the full corpus once the negative tail is in
hand — not against the curated half.
