# Recovered brand assets

Pulled from the Wayback Machine after teamazizi.com went offline. **These are compressed archive copies — request originals from the client before launch.**

The three videos are Luxury Presence **stock** footage, not Team Azizi footage. Replace with real neighborhood video (see GAMEPLAN §4.3).

## Corrections — 2026-07-25

Every file below was opened and inspected during the Phase 1 build. The table
further down was written from media IDs, not from the images themselves, and it
is wrong in several places. Corrections, most consequential first:

| File | Manifest says | Actually is |
|---|---|---|
| `neighborhoods/carmel-valley.jpg` | Carmel Valley hero | **A vineyard in Carmel Valley, Monterey County** — wine country, not 92130. The old site shipped the exact geographic conflation the SEO strategy exists to fight. **Do not use.** |
| `neighborhoods/4s-ranch.jpg` | 4S Ranch hero | **A mature mid-century suburb** — 1960s ranch homes, old fan palms, grid streets. 4S Ranch is a 2000s master-planned community. **Do not use.** |
| `logos/compass-brokerage.png` | Compass brokerage mark | The **TA monogram**, cropped. We do not have the Compass logo — request it from Compass's brand kit. |
| `backgrounds/newsletter.png` | Newsletter band image | **A blank white image.** Not recovered. |
| `misc/44e07ded-….png` | Unidentified | **REALTOR® + Equal Housing Opportunity marks** — required in the footer (HANDOFF §6). |
| `misc/c572aa1a-….png` | Unidentified | **San Diego MLS logo** — required for the MLS disclaimer. |
| `misc/9c77c8c8-….png` | Unidentified | **The Luxury Presence logo.** Must never ship. |
| `misc/jx9bf4w0yscrocpejgwv.png` | Unidentified | TA │ COMPASS lockup on black — now the default OG share image. |
| `misc/8f4fcc54-….jpg`, `misc/zbz1puja….jpg` | Unidentified | **Mediterranean stock** (olive, cypress, stone walls) — Greece or Spain, not San Diego. |
| 9 × 500×500 `misc/*.png` | 9 unidentified assets | **One image, nine byte-identical copies** — the TA monogram, now `site/assets/img/logos/monogram.png`. |

So "all 34 identified assets recovered" overstates it: one asset is blank, one
is the wrong image entirely, two neighborhood photos show the wrong places, and
nine of the "assets" are the same file. Usable unique assets are closer to 22.

Also worth knowing: the primary logo is not a "Team Azizi" wordmark — it is a
**TA │ COMPASS lockup**, so the brand mark already carries the affiliation.

Assets in active use now live in `site/assets/img/`. The two wrong-place
neighborhood photos were deliberately *not* copied there, so they cannot ship
by accident; those cards render an honest "photography pending" placeholder.

| File | Dimensions | Size | Purpose |
|---|---|---|---|
| `backgrounds/hero-poster.jpg` | 1920×2880 | 396 KB | Hero video poster frame (LCP image — optimize first) |
| `backgrounds/home-valuation.jpg` | 2560×1708 | 765 KB | Home-valuation module image |
| `backgrounds/newsletter.png` | 500×263 | 1 KB | Newsletter band image |
| `backgrounds/testimonials.jpg` | 2560×1706 | 557 KB | Testimonials section fixed background (30% overlay) |
| `backgrounds/work-with-us.jpg` | 1920×1200 | 555 KB | "Work With Us" full-bleed parallax band (40% overlay) |
| `logos/compass-brokerage.png` | 500×263 | 1 KB | Compass brokerage mark — 150px strip under hero (required affiliation) |
| `logos/logo-dark.png` | 2560×622 | 34 KB | Primary logo, dark — scrolled/solid nav + light footers |
| `logos/logo-light.png` | 2560×622 | 46 KB | Primary logo, white — transparent nav over hero + dark-section footers |
| `misc/44e07ded-9c1f-4c27-a916-0ea2d52e4824.png` | 355×184 | 3 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/8f4fcc54-e5d2-4fa1-9f50-6f3a59f3e34b.jpg` | 1920×1200 | 205 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/9c77c8c8-df92-4d39-8391-459a3d58e6e9.png` | 390×140 | 3 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/bekvy9fnc8wnttsmvwqp.jpg` | 2560×1706 | 1,615 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/c572aa1a-209b-451e-ad7d-ab7d72f3402e.png` | 705×79 | 3 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/ddtmsws5gcxjjbkfetix.png` | 500×500 | 1 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/jelatniuw7yen4xfg0oq.png` | 500×500 | 1 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/jx9bf4w0yscrocpejgwv.png` | 1280×800 | 7 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/ljotynfw1mr5gnqt2cg4.png` | 500×500 | 1 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/pljwkfpc8eecnd2xvx5u.png` | 500×500 | 1 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/rp5csehywniiiryuvjmr.png` | 500×500 | 1 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/s5c6dnyggs0zgt7uf0w1.png` | 500×500 | 1 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/ucgttlbgs1spcstjeimm.png` | 500×500 | 1 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/xsgljgvqqm4qezu9kxiw.png` | 500×500 | 1 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/zbz1pujagpko4gdiueud.jpg` | 1920×1200 | 405 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `misc/zkvuq2mm9h6k1cae4rqt.png` | 500×500 | 1 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `neighborhoods/4s-ranch.jpg` | 1280×800 | 227 KB | Neighborhood card + page hero — 4S Ranch |
| `neighborhoods/_hub-hero.jpg` | 1920×1440 | 652 KB | /neighborhoods hub page hero |
| `neighborhoods/carmel-valley.jpg` | 1280×800 | 313 KB | Neighborhood card + page hero — Carmel Valley |
| `neighborhoods/del-mar.jpg` | 1280×800 | 184 KB | Neighborhood card + page hero — Del Mar |
| `neighborhoods/del-sur.jpg` | 1280×800 | 179 KB | Neighborhood card + page hero — Del Sur |
| `neighborhoods/rancho-santa-fe.jpg` | 1280×800 | 391 KB | Neighborhood card + page hero — Rancho Santa Fe |
| `neighborhoods/scripps-ranch.jpg` | 1280×800 | 242 KB | Neighborhood card + page hero — Scripps Ranch |
| `team/headshot-candace-kirk.jpg` | 1280×1280 | 130 KB | Agent headshot — Candace Kirk |
| `team/headshot-candice-casares.jpg` | 1280×1280 | 104 KB | Agent headshot — Candice Casares |
| `team/headshot-coby-herzog.jpg` | 1280×1280 | 89 KB | Agent headshot — Coby Herzog |
| `team/headshot-dari-ahranjani.jpg` | 1280×1280 | 113 KB | Agent headshot — Dari Ahranjani |
| `team/headshot-deanna-colby.png` | 1280×1280 | 448 KB | Agent headshot — Deanna Colby |
| `team/headshot-gabriela-santiago.jpg` | 1280×1280 | 95 KB | Agent headshot — Gabriela Santiago |
| `team/headshot-jared-stransky.jpg` | 1280×1280 | 126 KB | Agent headshot — Jared Stransky |
| `team/headshot-melissa-lopez.jpg` | 1280×1280 | 136 KB | Agent headshot — Melissa Lopez |
| `team/headshot-michael-angotta.jpg` | 1280×1280 | 128 KB | Agent headshot — Michael Angotta |
| `team/headshot-nicholas-miele.jpg` | 1280×1280 | 122 KB | Agent headshot — Nicholas Miele |
| `team/headshot-nilab-azizi.png` | 750×750 | 219 KB | Agent headshot — Nilab Azizi |
| `team/headshot-sara-forgnone.jpg` | 1280×1280 | 106 KB | Agent headshot — Sara Forgnone |
| `team/headshot-sarah-rivas.jpg` | 1280×1280 | 181 KB | Agent headshot — Sarah Rivas |
| `team/headshot-sofia-azizi.jpg` | 1920×2878 | 872 KB | Agent headshot — Sofia Azizi |
| `team/headshot-zohra-azizi.jpg` | 1280×1280 | 143 KB | Agent headshot — Zohra Azizi |
| `team/team-group.jpg` | 1920×1528 | 323 KB | Team group photo — homepage "Meet The Team" section |
| `team/tile-contact.jpg` | 1024×1024 | 139 KB | Homepage gallery tile → /contact |
| `team/tile-meet-the-team.jpg` | 2560×1434 | 676 KB | Homepage gallery tile → /team |
| `team/tile-properties.jpg` | 960×960 | 149 KB | Homepage gallery tile → /properties/sale |
| `video/cta-buying.mp4` |  | 4,910 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `video/cta-selling.mp4` |  | 3,721 KB | Unidentified decorative asset (recovered by id; classify during build) |
| `video/hero-villa.mp4` |  | 3,986 KB | Unidentified decorative asset (recovered by id; classify during build) |

## Not recovered (3)

Three unnamed decorative images had no successful Wayback capture: `2836bb3e-f64f-46ff-9277-ca804dfa774a`, `3be2b7f0-341c-4a9d-af1d-194a63046f01`, `ttyovy8cfudpzb8xzwhj`. Every *identified* asset (all 34) was recovered.

## How these were found

Media IDs and their exact archived URL forms were extracted from the saved page snapshots in `research/archive-snapshots/`, then fetched through Wayback at the timestamp that captured each page. Requesting an unarchived resize width returns nothing — only widths the live site actually served (960/1280/1920/2560) exist in the archive.
