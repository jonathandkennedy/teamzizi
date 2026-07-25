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

Research and strategy complete. **Phase 1 in progress** — the design system, global chrome, schema pipeline, homepage and `/neighborhoods` hub are built. Next: the six neighborhood pages.

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

Deploy is Vercel with **Root Directory = `site`**. There is no build step on the host — generated HTML is committed, so the client can open any file in this repo and read their own website.

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
research/                Research pack (9-agent pass, 2026-07-24)
  archive-snapshots/     Saved HTML/CSS of the dead Luxury Presence site
assets/recovered/        Brand assets pulled back from the Wayback Machine
  README.md              Manifest + 2026-07-25 corrections (several were wrong)
```

## Notes

- **Stack:** static HTML/CSS/JS, no framework, no build step. Python generators for repeating page types. Deploys to Vercel.
- **Schema must be server-rendered** into the HTML — AI fetchers and `curl` don't run JavaScript.
- **Validate every JSON-LD block** (`json.loads`) and `sitemap.xml` before each push.
- **Recovered assets are placeholders.** Wayback copies are compressed and incomplete; request originals from the client. The three `.mp4` files are Luxury Presence *stock* footage — replace with real neighborhood footage.
- **Two recovered neighborhood photos show the wrong places** — the Carmel Valley image is Carmel Valley, *Monterey County* (wine country), and the 4S Ranch image is a mid-century suburb. Neither is in `site/`; those cards render a "photography pending" placeholder until real images exist.
- Fair Housing, MLS data-use, DRE display, and TCPA constraints are documented in [HANDOFF.md §6](HANDOFF.md) — read before writing neighborhood content.
