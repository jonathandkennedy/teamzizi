# Instagram extraction brief — @teamazizi_realestate

For an agent with a logged-in browser session. Everything below is public to a
logged-in viewer; none of it requires interacting with the account.

**Return format:** structured data (table, JSON or CSV), not prose summaries.
Where something isn't found, say "not found" rather than omitting the row —
absence is itself an answer for several of these.

**Ground rule:** capture verbatim. Do not paraphrase captions, awards wording,
or claims. This site refuses to publish any figure it cannot trace to a named
source, so a paraphrase is unusable.

---

## Tier 1 — blocking work right now

### 1. The four link-in-bio URLs ★ highest value

The bio shows `teamazizi.com/home-valuation` **and 3 more**. Open the link
aggregator and capture **all four destination URLs**, plus their labels and
the order they appear in.

Also note **which platform** hosts the aggregator (Linktree, Beacons, Later,
Compass-provided, or a self-hosted page).

*Why:* every one of these is a live destination taking traffic from 2,055
followers, and at least one is a dead teamazizi.com URL. This decides which
pages are launch-critical and what 301s are needed on day one. If the
aggregator is a third-party service, that is another rented dependency worth
naming.

### 2. Agent → neighborhood evidence ★ unblocks the redesign

The site is being rebuilt so one named licensee owns each of the six
communities (Carmel Valley, Del Mar, Rancho Santa Fe, Del Sur, 4S Ranch,
Scripps Ranch). Nothing published anywhere states who farms what. Instagram is
the most likely public source.

**a. Story highlights.** Visible covers: Sonia Azizi · Nilab Azizi · Sara
Forgnone · Gaby Santiago · Sofia Azizi · OPEN HOUSE · Zohra Azizi, and more
behind the arrow. For **each** highlight: the full list of covers, and for the
per-agent ones, what the highlight actually contains — which neighborhoods,
which listings, which addresses.

**b. Listing posts.** For every just-listed / just-sold / open-house post,
record the **agent named or tagged** alongside the **neighborhood or city**.
A repeated pairing is the evidence we need.

**c. Tagged accounts** on listing posts — the presenting agent is often tagged
rather than named in the caption.

*Why:* six confirmed assignments turn on the byline, direct contact, `/team`
grouping and schema author of every neighborhood page. Evidence beats asking
the client to recall it.

---

## Tier 2 — feeds the neighborhood pages

### 3. Just-listed and just-sold posts (last 24 months)

Per post: **address · list and/or sold price · beds/baths/sqft · neighborhood
or city · agent · post date · status (listed / pending / sold) · whether the
caption states an outcome** ("sold in 6 days", "over asking", "8 offers").

*Why:* this becomes the "Recently sold by Team Azizi in [neighborhood]" block
on each guide — the passage that answers the "best real estate agent in X"
fan-out sub-query with a record rather than a claim. Compass exposes only 18
of their 1,016 sales, and those land in the wrong neighborhoods.

### 4. Testimonial and client-outcome posts

Verbatim client quotes, the agent involved, the neighborhood, and any outcome
numbers. Note whether the client is named or initialled.

*Why:* `/testimonials` is unbuilt. The seven archived from the old site are
truncated mid-sentence and unusable. Outcome-stat testimonials
("8 offers in 3 days, over asking") are the best-converting pattern found in
the competitor research.

---

## Tier 3 — proof points and open questions

### 5. Award, ranking and recognition posts
Verbatim wording, awarding body, year, and post date. Already known: San Diego
Business Journal "$100M+ in sales in 2025", and RealTrends Verified. Looking
for anything further — Compass internal awards, local recognition, press.

### 6. Founding year
An anniversary post ("celebrating X years") would settle a live conflict:
Yelp says established 2010, housing.info says 2014. Either resolves an open
client question.

### 7. Languages spoken
Any post, story or caption in Dari, Farsi or Spanish, or any explicit mention
of languages served. **Do not infer from surnames.** This is a strong E-E-A-T
signal and an untapped keyword category, but it will not be published unless
confirmed.

### 8. Sonia Azizi legacy content — handle with care
The pinned "IN LOVING MEMORY" post and her story highlight. Capture the
verbatim wording and date, nothing more. Do not engage, do not collect
comments. This informs the tone of an "Our Founder" section; every decision
about it routes through the family.

### 9. Related accounts
Any Team Azizi agent's individual business account beyond the three known
(@nilab.azizi_realtor, @soniasellssd, @paulinasellssandiego). Handle and
follower count for each.

*Why:* each is a `sameAs` candidate for the entity graph — but only once
confirmed accurate.

### 10. Original neighborhood photography
Do their posts contain real photography of the six communities — streets,
landmarks, drone footage — as opposed to listing interiors and graphics?
Note which neighborhoods are covered and roughly how much.

*Why:* two of the recovered "neighborhood" photos show the wrong places
entirely (the Carmel Valley one is Monterey County wine country). If the team
already owns true local imagery, that is the cheapest fix available.

### 11. Market-data and educational posts
Do they publish market reports, price data or neighborhood explainers? If so,
which neighborhoods and how often.

### 12. Profile contact details
Whatever the profile exposes — email, phone, address, category, action
buttons. Needed for a NAP consistency check against the canonical record.

---

## Also worth a note

- Engagement: typical likes/comments per post, and whether reels outperform
  feed posts. Informs the repurposing cadence.
- Posting frequency over the last 6 months.
- Whether "Top 1% in SD County" appears in captions as well as the bio — it is
  an unciteable claim the site declines to print, and we need to know how
  widely it is deployed before recommending it be dropped.
