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

Research and strategy complete. Site build not yet started — Phase 1 is the design-system port, homepage, and six neighborhood pages.

## Layout

```
GAMEPLAN.md              Strategy + specs
HANDOFF.md               Decisions, canonical data, compliance
research/                Research pack (9-agent pass, 2026-07-24)
  archive-snapshots/     Saved HTML/CSS of the dead Luxury Presence site
assets/recovered/        Brand assets pulled back from the Wayback Machine
  _recovery-log.txt      What was recovered vs. still missing
```

## Notes

- **Stack:** static HTML/CSS/JS, no framework, no build step. Python generators for repeating page types. Deploys to Vercel.
- **Schema must be server-rendered** into the HTML — AI fetchers and `curl` don't run JavaScript.
- **Validate every JSON-LD block** (`json.loads`) and `sitemap.xml` before each push.
- **Recovered assets are placeholders.** Wayback copies are compressed and incomplete; request originals from the client. The three `.mp4` files are Luxury Presence *stock* footage — replace with real neighborhood footage.
- Fair Housing, MLS data-use, DRE display, and TCPA constraints are documented in [HANDOFF.md §6](HANDOFF.md) — read before writing neighborhood content.
