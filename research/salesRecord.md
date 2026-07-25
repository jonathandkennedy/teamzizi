# Sales record — the strategy problem

Source: full sweep of the Compass team page (57 pages × 18 = 1,009 past sales,
8 unparsed) plus all 18 individual Compass agent pages and a 299-post,
24-month Instagram read. Captured 2026-07-25.

**This supersedes the assumption the whole GAMEPLAN rests on.** Read this
before writing a neighborhood page.

---

## 1. The six communities are not the farm

| Metric | Value (n = 1,009) |
|---|---|
| **Median sale price** | **$650,000** |
| Under $1M | 782 (77.5%) |
| $2M and above | 52 (5.2%) |
| Range | $60,000 – $6,100,000 |
| California | 862 |
| **Connecticut** | **136** |
| **Six target communities, combined** | **45 (4.5%)** |

Actual top markets, by volume of transactions: **Escondido** (~96 across four
ZIPs — the single largest), Spring Valley, South Bay (92154, 92114, 92113,
92102, Chula Vista), Fallbrook, Oceanside, Santee, El Cajon.

Per target community:

| Community | Team sales, all time | Best-supported agent | Confidence |
|---|---|---|---|
| Del Sur + 4S Ranch (92127) | 18 | Zohra Azizi (6), then Sofia Azizi (3) | Moderate |
| Carmel Valley (92130) | 11 | Contested — Javier Hernandez 3, Angotta 3, Miele 2 (Miele holds the $4.75M top sale) | Low |
| Scripps Ranch (92131) | 9 | Sofia Azizi (holds both top sales, $3.5M and $3.2M) / Zohra (4 by count) | Moderate |
| Del Mar (92014) | 6 | Michael Angotta (3, plus hosted the Mira Montana launch event) | Moderate |
| **Rancho Santa Fe (92067)** | **1** (5918 Fairway Place, $2.9M) | **None** | **None** |

**Del Sur and 4S Ranch are not separable.** ZIP 92127 covers Del Sur, 4S
Ranch, Rancho Bernardo *and* Santaluz. Any per-community split has to come
from street-level data, not ZIP.

### What this means for the build

The plan's own quality gate (contentPlaybook §1.8) asks: *would you show this
page to Google's webspam team?* A Rancho Santa Fe expert page backed by one
lifetime sale does not survive that question, and RSF is the hardest SERP in
the county — the one place a thin page will be most visibly outclassed by
Barry Estates and Brizolis Janzen.

The honest options, in order of preference:

1. **Re-point the farm at the evidence.** Escondido alone has ~96 sales. An
   Escondido guide would be backed by more first-hand transactions than all
   six current targets combined, and no competitor in the research owns it.
2. **Keep the six, but sequence by record**: Del Sur/4S Ranch (18) →
   Carmel Valley (11) → Scripps Ranch (9) → Del Mar (6), and **drop Rancho
   Santa Fe** until there is a record to stand on.
3. Build all six anyway — but then the "track record in this neighborhood"
   block, which is the moat, is empty on two of them.

This is a client conversation, not a build decision.

---

## 2. ⚠️ "#1 in Del Mar by sides" needs verifying before it ships

It is currently the third stat on the homepage.

RealTrends assigns each team a **business city** and ranks within it. Team
Azizi's assigned city is Del Mar. Their Compass record shows **six Del Mar
sales, ever** — against 92 sides in 2025 alone, almost none of them in Del
Mar.

So the claim is very likely an artifact of *where the team is registered*,
not a statement of Del Mar market share. Published as "#1 in Del Mar," a
reader will reasonably infer the latter.

The safe claim is the one already on the page and independently checkable:
**#58 of all California Large Teams by volume.** Recommend dropping the Del
Mar line until RealTrends' methodology is confirmed. Flagged in `site.py` as
`DEL_MAR_CLAIM_UNVERIFIED`.

---

## 3. "Top 1% in SD County" is now clearly unsupportable

A $650,000 median with 77.5% of sales under $1M does not support a luxury
positioning, and the phrase appears **zero times in ~300 captions** over 24
months — it lives only in the Instagram bio. Their own captions consistently
use the citable RealTrends framing instead ("top 1.5% nationwide").

Dropping it therefore costs nothing and contradicts nothing they have
published. Clean recommendation.

---

## 4. Michael Angotta — highest producer, two cautions

177 sales, the largest book on the team. But:

- **136 of them are in Connecticut** (Norwalk 24, Fairfield 10, Bridgeport,
  Westport, Stamford, Stratford). He is not primarily a San Diego agent by
  volume.
- A second Instagram account, `@realestatebuyangotta`, **links to YB Realty,
  not Compass** — a possible brokerage change in progress.
- His Compass bio claims "over $100,000,000 in real estate transactions"
  *individually*, which sits awkwardly beside the SDBJ recognition crediting
  the **team** with $100M+ in 2025. Same figure, two different subjects.
- The bio positions him as serving luxury clients exclusively; his own list
  includes a long tail of $60K–$250K Connecticut condos.

He is the best-supported Del Mar candidate on transaction evidence and
simultaneously the riskiest to build a page around. Resolve with the client
before publishing him as a neighborhood specialist.

---

## 5. Attribution gap

Per-agent sales attributed: **779**. Team page total: **1,009**. The ~230
difference belongs to departed agents or is unattributed. Worth knowing before
any "our agents have closed X" claim.

---

## 6. Languages — answered, from a named source

Compass agent profiles carry an explicit Languages field. Only three are
populated:

| Agent | Field value |
|---|---|
| Gabriela Santiago | English, Spanish |
| Melissa Lopez | English, Spanish |
| Mahan Taleshpour | English, Farsi |

All other 15: no Languages field. **Dari is not found anywhere** — it is a
team member's first name, not a stated language.

Caveat before building a Farsi keyword cluster: Taleshpour's entire record is
Los Angeles and the San Fernando Valley, with essentially no San Diego
presence. **The Spanish capability is the real one** — it is San Diego-based
and it maps precisely onto the team's strongest actual markets (South Bay,
Escondido, Chula Vista). That is an untapped keyword category sitting on top
of their genuine book.

---

## 7. Link-in-bio — all four, and one surprise

Instagram's native multi-link, not a third-party aggregator — one less rented
dependency.

| # | Label | Destination | Status |
|---|---|---|---|
| 1 | What Is Your Home Worth? | `teamazizi.com/home-valuation` | **Dead — the whole domain is NXDOMAIN** |
| 2 | Team Azizi - Compass | compass.com/agents/team-azizi | Live |
| 3 | Living in San Diego - YouTube | youtube.com/@lifeinsandiego | Live — **but it is Nicholas Miele's personal channel** |
| 4 | GOLDEN HOUR SOIRÈE, Del Mar | partiful.com/e/WhuTRq7yaJDIAnxrGq4G | Live, ~4 months stale |

Links 1, 2 and 4 carry `utm_source=ig&utm_medium=social&utm_content=link_in_bio`.
Someone set that up deliberately, so the traffic loss is being measured
somewhere — which makes the `/home-valuation` redirect the single most urgent
day-one item.

**The highest-reach asset in the entire estate is not owned by the team:**
@lifeinsandiego has **12.4K subscribers and 205 videos** against the team
account's 2,055 followers, publishes roughly weekly, and belongs to Nicholas
Miele personally. It also holds the only real on-location neighborhood video
that exists — dedicated tours of Carmel Valley (×2), Rancho Santa Fe (×2),
4S Ranch & Del Sur, Del Mar, and Santaluz. Scripps Ranch is missing.

---

## 8. Engagement — reels only

Feed posts run 1–43 likes against 2,055 followers (~0.2–0.3%, very low).
Reels run 548–6,853 views. Reels outperform feed by orders of magnitude.

Two consequences: repurposing cadence should be reels-first, and **any social
proof widget pulling like counts onto the site would actively hurt.**

Posting frequency is not the constraint — 99 posts in ~6 months, ~3.4/week.

---

## 9. Testimonials — usable, but not from Instagram

Only five Instagram posts are framed as client reviews and none quote the
client; the review text sits inside carousel images, not captions.

**Compass agent pages are the better source** — six agents carry star-rated
testimonials with first names: Angotta (3), Santiago (6), Lopez (6), Schick
(6), Taleshpour (4), Miele (2). Outcome numbers largely absent.

The strongest single narrative is on Nilab's personal account (2025-10-08):
a relist story — prior agent, two months, zero showings, zero offers;
repositioned, multiple offers, $20K over asking, two buyers fell through,
third closed. That is the best-converting pattern in the competitor research,
and it is verbatim-capturable.

---

## 10. Awards — one new, and the best of the three

| Date | Body | Wording |
|---|---|---|
| 2025-10-29 | San Diego Business Journal | "one of the top 10 real estate teams in the county" |
| 2026-02-10 | San Diego Business Journal | "recognized among San Diego's top-producing teams", $100M+ in 2025 |
| 2026-06-08 | RealTrends Verified | "2026 RealTrends Verified team and among the top 1.5% of real estate professionals nationwide" |

The **October 2025 SDBJ top-10-in-the-county** line is new and is the
cleanest, most specific of the three. Self-reported volume, if a stats block
needs it: 2024 = $90M / 80 units; Q1 2025 = $25M / 26 closings; 2025 = $100M+.

---

## 11. Still not found

- **Founding year.** No anniversary post in 563 posts; the Compass team page
  has no About section at all. Oldest grid post ~Oct 2018; a "2ND ANNUAL"
  event dated Oct 2018 implies a first in 2017. Neither Yelp's 2010 nor
  housing.info's 2014 is corroborated. Still a client question.
- **Original neighborhood photography on the team account.** Content is
  listing interiors and text-over-image graphics. Local content exists but is
  *events*, not places. The one real asset is listing photography for the Del
  Mar and Scripps Ranch/Stonebridge properties.
- **NAP on Instagram.** Not a Business profile — no category, no address, no
  action buttons. It cannot corroborate the canonical record at all. The only
  contact strings are in caption sign-offs.

---

## 12. Sonia Azizi

Captured minimally; the memorial highlight was **not opened**, on the ground
rule that viewing registers in the account's viewer list.

- Pinned memorial post: `/p/CuX5SLTOxMm/`, "IN LOVING MEMORY"
- 2026-01-11 "Happy Heavenly Birthday" — 32 likes, 12 comments
- 2025-01-11 "Happy Heavenly Birthday" — 43 likes
- 2026-03-04 "Sonia is always on our minds…" — 22 likes

**January 11 is her birthday, and those anniversary posts are the highest-
engagement posts on the entire account.** The team's own captions already
frame the RealTrends recognition as continuing "a legacy that began with
Sonia" — so an "Our Founder" section introduces nothing the team has not
already said publicly.

**@soniasellssd is still live: 9,412 followers**, bio "Founder of Team Azizi",
"TOP 1.5% In the country." That is by far the largest audience in the entity
graph — four and a half times the team account. It is a family decision, not
an SEO one.

---

## 13. Neighborhood video — the asset that was hiding (added 2026-07-25)

The client confirms **the team paid for the video** on @lifeinsandiego, so it
is usable. Channel-searched and resolved to specific videos:

| Community | Video | ID |
|---|---|---|
| Carmel Valley | "EVERYTHING You NEED to Know About Living in Carmel Valley in San Diego" (plus 2 more) | `IGpVk4vTGjg` |
| Rancho Santa Fe | "Living in Rancho Santa Fe California" (**5 videos total** — the most of any community) | `LXO2cS7l36Q` |
| Del Sur + 4S Ranch | "INSANE Community in San Diego You HAVE to See \| 4S Ranch & Del Sur" (one video covers both) | `6nrzXgXyngA` |
| Del Mar | "Living in Solana Beach & Del Mar California" (shared with Solana Beach) | `G-12EJiUSsw` |
| **Scripps Ranch** | **None** | — commission one |

This matters more than it looks. `research/competitors.md` found that **not one
competitor embeds neighborhood video on a neighborhood page** — not O'Byrne
with an HGTV show, not Whissel with a YouTube machine. It is a documented open
gap and the team already owns the content for four of six.

`schema.video()` emits `VideoObject` with `contentLocation`, so the video is
eligible to surface on its own rather than being a decorative iframe.

**The Rancho Santa Fe irony is worth sitting with.** RSF has one lifetime sale
(§1) and the *most* video content of any community — five dedicated videos.
That complicates the earlier "drop RSF" recommendation: they have genuine
content authority there without transaction authority. A guide built on the
video, honest about the team's record, is defensible in a way a fabricated
track-record block is not.

Not added to `sameAs`: paying for production is a licence to use, not a claim
that the channel is a Team Azizi entity. It is embedded with credit instead.

The most recent 30 uploads are county-level market commentary published
roughly weekly — "Ranking San Diego's WORST to BEST Master-Planned
Communities", "Where To Live In San Diego For The HIGHEST ROI In 2026". That
is the content engine GAMEPLAN §7 wants, already running. It is not on the
team's domain, where it would compound.
