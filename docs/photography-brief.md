# Photography brief — localized imagery

**Short answer to "shouldn't pictures be localized to street or neighborhood?": yes, and it matters more than it looks.**

Generic stock is not a neutral choice here, it is a negative signal. The May 2026 core update explicitly rewards first-hand, point-of-view pages with original local detail and demotes commodity content ([contentPlaybook §1.1](../research/contentPlaybook.md)). A photograph of an identifiable local place is the cheapest first-hand signal there is — and the competitor teardown found that **not one competitor embeds real neighborhood imagery or video on their neighborhood pages** ([competitors.md](../research/competitors.md)). It is an open gap, not a nice-to-have.

It also compounds: original geo-relevant images earn image-search and Lens surfaces of their own, and they feed the GBP photo cadence the plan already commits to (2–3/month, [aiPlaybook §4](../research/aiPlaybook.md)).

---

## The source we already own

Before commissioning anything: **Team Azizi has 1,016 closed sales.** Their own listing photography is street-level imagery of the exact neighborhoods, already licensed to them, already geographically true. That is the fastest path to localized imagery and it needs no shoot — only a rights check on the listing photographers.

Priority order:

1. **Their own listing/sold photography** from each neighborhood — owned, true, and doubles as the "recently sold here" proof block.
2. **Original shoot** against the list below — best quality, fills the public-realm gaps listings can't cover.
3. **Correctly-identified licensed stock of named landmarks** — acceptable interim, only where the location is genuinely what it claims.
4. **Generated imagery — not on neighborhood pages.** A synthetic photograph of a real named community is a fabricated depiction of a real place, on a site whose entire pitch is that its facts are checkable. Fine for abstract section textures; never for "this is Del Sur."

---

## Shot list by community

Public-realm subjects only — no private homes without permission, no identifiable people without a release. Each list leads with the single most recognisable subject.

### Carmel Valley (92130)
Del Mar Highlands Town Center · One Paseo · Torrey Pines High School · Canyon Crest Academy · Carmel Valley Recreation Center · residential streetscapes in Ashley Falls and Sage Canyon · the Pacific Highlands Ranch village core · Torrey Pines State Reserve at the western edge

### Del Mar (92014)
Powerhouse Park · Seagrove Park · the 15th Street village · Camino Del Mar streetscape · Del Mar Plaza · the bluffs · Del Mar Fairgrounds and racetrack

### Rancho Santa Fe (92067)
The Covenant village at Paseo Delicias · Roger Rowe School · Rancho Santa Fe Golf Club · the eucalyptus-lined lanes (the signature RSF image) · Rancho Santa Fe Library · gates at The Bridges and Fairbanks Ranch

### Del Sur (92127)
Del Sur Town Center · the pools and parks the community is built around · Del Sur Elementary · the trail network · Sundance and Solterra streetscapes

### 4S Ranch (92127)
4S Commons Town Center (its stated edge over Del Sur) · 4S Ranch Sports Park · Design 39 Campus · Del Norte High School · 4S Ranch Library

### Scripps Ranch (92131)
**Lake Miramar** — the hook every ranking page leads with · the eucalyptus groves · Scripps Ranch Library · Scripps Ranch High School · Hoyt Park · the village centre

### Also worth capturing
Drone footage of each community for the neighborhood-page video slot — no competitor has one. The office exterior and interior at 12860 El Camino Real, for GBP. Team-at-work frames: open houses, closings, listing prep.

---

## Technical requirements

Every image that ships:

- **Descriptive filename** — `del-sur-town-center.jpg`, never `IMG_4821.jpg`.
- **Alt text names the actual place**, not the neighborhood generically: "Del Sur Town Center on Camino Del Sur" beats "Del Sur neighborhood".
- **Caption where the subject is a named landmark.** Captions are indexed and read; they are also where an honest "licensed stock" note goes if the image is not original.
- **≥1600px on the long edge**, then compressed. Current `site/assets/img/` is 8.3 MB unoptimised and the hero is the LCP element — optimisation is a launch blocker, tracked in HANDOFF §7.
- **`ImageObject` schema with `contentLocation`** on neighborhood-page imagery, so the image asserts its own geography rather than inheriting it from page context. `build/schema.py:image()` emits this.
- **No geo-tagging effort.** EXIF is stripped on upload and has no ranking effect ([aiPlaybook §4](../research/aiPlaybook.md)) — do not let anyone sell you on it.
- **No Fair Housing signalling.** Imagery is subject to the same rule as copy: depict places, not the demographics of who lives in them (HANDOFF §6).

## Currently blocked

Two recovered images show the wrong places and are held out of `site/` — the Carmel Valley one is Monterey County wine country, the 4S Ranch one is a mid-century suburb. Those two cards render a "photography pending" placeholder until replaced. See [assets/recovered/README.md](../assets/recovered/README.md).
