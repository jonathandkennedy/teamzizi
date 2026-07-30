# Team Azizi — Website Rebuild

Rebuild of **teamazizi.com** for Team Azizi (Compass, San Diego) — a URL-preserving, schema-first static site replacing a dead Luxury Presence build, paired with an AI-citation (GEO) and local SEO program.

Built and maintained by [CitedRealty](https://citedrealty.com).

## Start here

| Doc | What it is |
|---|---|
| **[GAMEPLAN.md](GAMEPLAN.md)** | The plan — strategy, rebuild spec, neighborhood-page template, build order |
| **[HANDOFF.md](HANDOFF.md)** | State + every settled decision and *why*, canonical NAP data, compliance notes |
| [research/](research/) | Evidence base — old-site inventory, design tokens, competitor teardowns, AI-visibility baseline, keyword map |

## Status

Research and strategy complete. **The site is built** — 50 pages, including 16 neighborhood guides (16,107 words), 19 agent pages, the `/mello-roos` and `/home-valuation` lead magnets, and a photograph on every neighborhood page.

**One thing blocks launch:** `site.LEAD_ENDPOINT` is a placeholder, so every lead form posts into nothing. `validate.py` fails the build on it deliberately. Full state and the open-items list: [HANDOFF.md](HANDOFF.md).

## Build

```bash
python3 build/generate.py                # write site/
python3 build/validate.py --prelaunch    # pre-push gate during the build
python3 build/validate.py                # LAUNCH gate — no escape hatch
```

`--prelaunch` demotes *launch blockers* (things fine mid-build but fatal in
production, like a lead form posting at a placeholder endpoint) to loud
warnings. The launch build runs without the flag, so shipping one takes a
deliberate act rather than a quiet oversight.

`validate.py` parses every JSON-LD block, rejects one `@id` describing two different things, checks `sitemap.xml` as XML against real files, and fails the build if any stale NAP string (old address, old phone, "Upstart", the "45 Ranch" typo) reaches the output.

Deploy is Vercel with **Framework Preset = Other**, **Root Directory blank**, **Output Directory = `site`**, and no build or install command. Getting this wrong is why the project first appeared not to pull from the repo — Vercel's Next.js autodetection finds nothing to build. There is no build step on the host: generated HTML is committed, so the client can open any file in this repo and read their own website.

## Layout

```
GAMEPLAN.md              Strategy + specs
HANDOFF.md               Decisions, canonical data, compliance
vercel.json              cleanUrls, 301 map, cache + security headers
build/                   Generators (not deployed)
  data/site.py           THE canonical strings — never retype them elsewhere
  schema.py              JSON-LD builders — dicts, never hand-written strings
  validate.py            Pre-push gate
site/                    The deployable site (output committed)
docs/                    Operational runbooks (launch, photography, content)
research/                Research pack (9-agent pass, 2026-07-24)
  archive-snapshots/     Saved HTML/CSS of the dead Luxury Presence site
assets/recovered/        Brand assets pulled back from the Wayback Machine
  README.md              Manifest + 2026-07-25 corrections (several were wrong)
.claude/skills/          last30days — community-listening skill for the
                         content engine (docs/content-runbook.md §3)
```

## Notes

- **Stack:** static HTML/CSS/JS, no framework, no build step. Python generators for repeating page types. Deploys to Vercel.
- **Schema must be server-rendered** into the HTML — AI fetchers and `curl` don't run JavaScript.
- **Validate every JSON-LD block** (`json.loads`) and `sitemap.xml` before each push.
- **Recovered assets are placeholders.** Wayback copies are compressed and incomplete; request originals from the client. The three `.mp4` files are Luxury Presence *stock* footage — replace with real neighborhood footage.
- **The old site published a photo of Carmel Valley, _Monterey County_ on the Carmel Valley, San Diego page** — four hundred miles wrong. Both that image and the mislabelled 4S Ranch one were discarded. All 16 areas now carry verified photography: 4 from the recovered set, 12 third-party with credits rendered on the page. The verification method, and the three further wrong-place near-misses it caught, are in [HANDOFF.md §5](HANDOFF.md).
- **Never install a photograph of a named place without checking its Commons category and reading its description.** `build/commons.py` and `build/openverse.py` find candidates and install nothing, on purpose.
- Fair Housing, MLS data-use, DRE display, TCPA and the no-review-schema rule are documented in [HANDOFF.md §8](HANDOFF.md) — read before writing neighborhood content.
