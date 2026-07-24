

# ==== design_tokens ====

## Platform
**Luxury Presence** (confirmed by multiple fingerprints: `styles.luxurypresence.com/producer/index.css`, `luxuryPresence.divolte.initialize()` analytics, `media-production.lp-cdn.com` media CDN, Cloudinary account `res.cloudinary.com/luxuryp` for stock videos, `lp-btn`/`lp-container`/`lp-h1` class system, section-UUID architecture, Handlebars `text/x-handlebars-template` blocks, "Luxury Presence Home Value" widget). Brokerage affiliation: **Compass** (Compass Concierge nav item, 150px brokerage logo strip under hero).

## Colors (exact hex)
| Role | Value |
|---|---|
| Global page background | `#FFFFFF` (`--global-background-color: #fff`) |
| Dark band sections (Selling/Buying CTAs, newsletter, Instagram) | `#000000` pure black |
| Body/heading text on light | `#000000` |
| Text on dark sections | `#FFFFFF` |
| Near-black UI (footer icons SVG fill, IG nav-button hover) | `#1A1A1A` |
| Neutral/secondary gray text | `#848484` (`--textNeutralColor`) |
| Sidemenu inactive link | `#7A7A7A` |
| Nav hover underline / muted accents | `#C6C6C6` |
| Light outline buttons (silver) | `#C0C0C0` |
| Hairline dividers | `#E7E7E7` |
| Scrollbar track / light panel | `#F3F3F3` (thumb `#C4C4C4`) |
| **Gold accent (dark)** — neighborhoods carousel title underline, featured-property label tag bg | `#8D7120` |
| **Gold accent (light tan)** — checklist bullets in home-valuation module | `#CCB091` |
| Hero overlay | `rgba(0,0,0,0.30)` |
| CTA video panel overlays | `rgba(0,0,0,0.4)` and `rgba(0,0,0,0.5)` |
| Image-section overlays (Work With Us, page heroes) | `rgba(0,0,0,0.4)` |
| Contact modal backdrop | `rgba(2,5,7,0.7)` |

## Typography
- **Primary / headings font**: `'Reem Kufi Fun', sans-serif` (Google Fonts, weights 400,500,600,700 loaded). Applied to ALL h1–h6, `.lp-h*`, buttons element, and the `.serif` utility class. Headings render at **weight 400**, line-height 1.1–1.3. Note: LP's class is named "serif" but the font is a geometric Kufi-flavored sans.
- **Secondary / body font**: `Lato, sans-serif` (weights 100–900 loaded). Body weight 400, 16px. Used for body copy, buttons, nav, labels.
- **Type scale** (CSS vars): h1 `70px`, h2 `43px`, h3 `30px`, h4 `21px`, h5 `17px`, h6 `16px`, body `16px`. Mobile: `.lp-h1` 40px / letter-spacing .75px, `.lp-h2` 32px / .75px.
- **Nav links**: Lato 13px, weight 700, UPPERCASE, letter-spacing 1.5px, animated 1px underline on hover.
- Sidemenu links: Reem Kufi Fun 21px, letter-spacing .5px.

## Buttons
- Base `.lp-btn` / `.btn`: **square (border-radius: 0)**, `border: 2px solid`, transparent background (ghost style), padding `20px 46px`, Lato 14px weight 700 UPPERCASE letter-spacing 1.5px, transition all .2s. Hover inverts (fills with border color).
- `button-style-1` (on light): black text/border, transparent bg → hover black bg / white text.
- `button-style-2` (on dark/photo): white text/border, transparent bg → hover white bg / black text.
- Filled variant used for form submits: black bg / white text (`.lp-btn--filled.home-val-btn`).
- Property "label" tags: `#8D7120` bg, white text, padding 8px 34px, 14px bold uppercase.
- Border-radius elsewhere: essentially 0 everywhere; exceptions are avatars (50%), mobile contact pill (999px), home-valuation modal (16px).

## Spacing / containers
- Content container: `max-width: 1400px`, 50px side padding. Nav container: 1440px, 15px padding.
- Section vertical rhythm: `--global-section-padding: 96px` (64px compact variant). Hero collection min-height 100vh with 120px top padding.
- Fixed nav height 100px (translateY 24px offset at top).

# ==== layout_patterns ====

## Global chrome
- **Nav**: `position: fixed` top, z-index 101, **transparent over the hero** with white logo + white uppercase links; on scroll (`.scroll` class) it swaps to **solid #fff background, black links, and a dark logo variant** (two logo imgs toggled). Right side: phone number link `(858) 847-8067` and a hamburger that opens a 400px white side-drawer (full site map incl. Renovation Case Studies, Buyers/Seller's Guides, Compass Concierge, Blog, Testimonials, My Search Portal). Desktop nav items: Properties (dropdown: Featured Properties / Past Transactions), Neighborhoods, Home Search, Home Valuation, CONTACT US, phone.
- **Footer**: light — white bg, #1A1A1A text and thin line-art SVG icons (email, phone, address). h3 "Team Azizi", "Get In Touch" contact cells, dark logo, 3 social icons, "Team Azizi | CA DRE# 02047962", disclaimer, plus a "Submit a Message" contact-form modal (backdrop rgba(2,5,7,0.7)).

## Homepage, section by section
1. **Hero — full-bleed video slider**: 100vh, slick carousel of looping muted Cloudinary videos (poster fallbacks), `rgba(0,0,0,0.30)` overlay, centered white text: h1 "Team Azizi" (Reem Kufi 70px), subtitle "Who Represents You Matters", one ghost button "BROWSE PROPERTIES" (white outline, style-2). Slide-in animation (translateX) + line-style slick dots.
2. **Brokerage logo strip**: tiny white section, centered 150px Compass logo image.
3. **Stats band** (white): h2 "California Real Estate Experts" + 3 stat cards — "Top 1% / in SD County", "$90M+ / 2024 Volume", "82 / 2024 Units Sold" (values are h3s in Reem Kufi with count-up JS).
4. **Split dual CTA (dark)**: two side-by-side full-bleed **video** panels — "Selling A Home?" (modern-home render, 40% overlay, "GET HOME VALUE" white ghost btn) and "Buying A Home?" (San Diego coastline video, 50% overlay, "VIEW PROPERTIES").
5. **Meet The Team** (white): "hoverable-image" two-column — large team photo left, h2 "Meet The Team" + copy + black-outline "LEARN MORE" button right.
6. **Testimonials**: full-bleed fixed photo background (30% overlay), "Our Testimonials" carousel; circular 104px avatar cards (photo or initial-letter on black circle), name h4, quote.
7. **Gallery trio** (white): three linked image tiles — Properties / Meet The Team / Contact Us (h3 captions).
8. **Newsletter band (black)**: "Receive Exclusive Listings In Your Inbox", email input + white ghost SUBMIT.
9. **Neighborhoods carousel** (white): "Browse Our Neighborhoods Guides" heading section, then a slick carousel of 6 neighborhood photo cards; carousel title carries a **#8D7120 gold underline accent**; prev/next text arrows.
10. **Home Valuation module** (light): "How Much is Your Home Worth?" — address search input + black filled "GET A FREE HOME VALUATION" button, image + gold-bullet (#CCB091) checklist modal flow ("Get Your Instant Home Valuation" / "Schedule a Consultation").
11. **Featured Properties** (white): heading + 3-card listing carousel (8337 Summit Way $1,525,000; 4495 Montalvo St $1,250,000; 3252 Via Marin #9 $985,000) — photo, gold `#8D7120` status label, address h4, price h5.
12. **Work With Us**: full-bleed parallax photo band, 40% overlay, centered white `.serif` h2 with a thin 110px × 1px centered underline, paragraph, "CONTACT US" white ghost button.
13. **Instagram band (black)**: "Follow Us on Instagram" + handle, "FOLLOW US" outline button, horizontally scrolling IG feed (48px square arrow buttons, 1px border, hover #1A1A1A fill).

## /neighborhoods page, section by section
1. **Hero — image-section**: full-bleed photo (`media/rdszydbnfr7blac6fidx`) with `rgba(0,0,0,0.4)` linear-gradient overlay, white h1 "Neighborhoods". Title tag: "Best Places to Live in California | Team Azizi".
2. **Neighborhood grid** (white, class `neighborhood-list three-grid`): **3-column card grid**, 6 cards — Carmel Valley, Del Mar, Rancho Santa Fe, Del Sur, 4S Ranch, Scripps Ranch. Each card: photo with a centered "EXPLORE" ghost button overlay (black style-1, appears on hover), neighborhood name below in the uppercase "feature" label style. Links to `/neighborhoods/{slug}`.
3. **CTA band (black)**: right-aligned "Start Your Property Search" h2 + white ghost "BROWSE HOMES" button.
4. **Work With Us**: same parallax photo band as homepage (photo `iewsuie9vnwodddwjt4l`, 40% overlay, serif h2 with hairline underline, Contact Us button).
5. **Instagram band (black)** + light footer (same global chrome).

# ==== brand_personality ====

Team Azizi's site is modern-luxury minimalism in the classic Luxury Presence mold: a stark, high-contrast black-and-white system where imagery does the talking — full-viewport looping drone/lifestyle video in the hero, full-bleed parallax photo bands, and 30–50% black overlays that keep white type legible. It is luxury-leaning but not old-money: there are no serifs anywhere (despite a `.serif` class name, headings are 'Reem Kufi Fun', a geometric, slightly rounded Kufi-influenced sans at weight 400 that gives the brand a distinctive, softer, almost boutique feel), paired with workhorse Lato for body and uppercase, letter-spaced UI. Buttons are strictly square 2px-border ghosts that invert on hover — crisp and architectural. Warmth comes from restrained gold accents (#8D7120 labels/underline, #CCB091 checklist bullets), family-team photography, avatar-driven testimonials, and stat proof points (Top 1%, $90M+), landing the brand at "approachable luxury" — a family team selling San Diego coastal suburbs, not a Beverly Hills estate broker. For the rebuild: keep the black/white palette, video hero with dark overlay, square ghost buttons, uppercase tracked Lato UI, gold micro-accents, alternating white/black section rhythm, and the transparent-to-white sticky nav with logo swap — these ARE the brand. Modernize by replacing slick-carousel and WOW.js fade-ins with lighter scroll-reveal, making the 70px/43px type scale fluid (clamp()), tightening the neighborhood cards into a responsive CSS grid, and deciding consciously on Reem Kufi Fun: it is the most recognizable brand asset, so keep it for continuity (or, if a more premium read is desired, only swap it deliberately — the rest of the system is font-agnostic).

# ==== assets_found ====

All verified retrievable through Wayback (logo returned `image/png` 200). Pattern: prefix original URL with `https://web.archive.org/web/20260104120026im_/`. For originals, the LP CDN resize wrapper (`cdn-cgi/image/...width=1280/`) can be varied (`width=1920`, or `quality=85` only) — those variants are also archived. Captures used: homepage `20260104120026`, /team `20260104120019`, /neighborhoods `20251206192739`.

**Logos**
- Light/white logo (transparent nav + footer of dark pages): https://web.archive.org/web/20260104120026im_/https://media-production.lp-cdn.com/cdn-cgi/image/format=auto,quality=85,fit=scale-down,width=1280/https://media-production.lp-cdn.com/media/etv3v3yzlbwwqhwsdz0i
- Dark logo (scrolled nav + footer): https://web.archive.org/web/20260104120026im_/https://media-production.lp-cdn.com/cdn-cgi/image/format=auto,quality=85,fit=scale-down,width=1280/https://media-production.lp-cdn.com/media/w4vgzllyebehwvwgoc4k
- Compass/brokerage logo strip (150px, under hero): https://web.archive.org/web/20260104120026im_/https://media-production.lp-cdn.com/media/fcba9879-5e39-46c1-ab34-e4a6bf45c388
- Social icons (footer): https://web.archive.org/web/20260104120026im_/https://media-production.lp-cdn.com/media/44e07ded-9c1f-4c27-a916-0ea2d52e4824 , .../media/c572aa1a-209b-451e-ad7d-ab7d72f3402e , .../media/9c77c8c8-df92-4d39-8391-459a3d58e6e9

**Team photography** (base: `https://web.archive.org/web/20260104120019im_/https://media-production.lp-cdn.com/cdn-cgi/image/format=auto,quality=85,fit=scale-down,width=1280/https://media-production.lp-cdn.com/media/` + id)
- Team group photo (homepage "Meet The Team"): id `wmr3ejnctveq0ixlgfh4` (use `20260104120026im_`)
- Gallery tile "Meet The Team": id `m0ejus3pdlki36fdxjdp`; "Properties" tile: `xtyl0pem1cb3o2cz3mnf`; "Contact Us" tile: `wgj3qjm8xjya8t0cnocc`
- Headshots: Nilab Azizi `wwfc7vxuub6er74fisn2` — Zohra Azizi `phq58lzybiqs5y4cjlnt` — Sofia Azizi `e5498e29-30b1-4ee3-a48b-06e79...` (truncated in listing; re-scrape /team) — Deanna Colby `g87qgdxq9o5npu7terol` — Candace Kirk `etutpeqvziv80uxv18rd` — Candice Casares `o1d30ziunqlrpu08lkk4` — Coby Herzog `hz4ltvz8qfjwwddbmhd8` — Dari Ahranjani `sthlklav0dmjcq8w3gi1` — Gabriela Santiago `obd0zoqjilrpz6tcrk4l` — Jared Stransky `dzgzirpb06m1jzj0pbuq` — Melissa Lopez `wdwwuxe1oacmqzpwbtwp` — Michael Angotta `pc7k1exietlu5a6rxv6a` — Nicholas Miele `s1lnvgmggdgctoyw27q0` — Sara Forgnone `yjkxsfkhm6psjhemekgw` — Sarah Rivas `l5qxumilzsrfydqdfapk`

**Neighborhood imagery** (base: `https://web.archive.org/web/20251206192739im_/https://media-production.lp-cdn.com/cdn-cgi/image/format=auto,quality=85,fit=scale-down,width=1280/https://media-production.lp-cdn.com/media/` + id)
- Carmel Valley `rbc85wswwe17cwnirgrb` — Del Mar `yizgdl9x4k1pqaz3rrlf` — Rancho Santa Fe `qwhya1dvopos70tfwrwz` — Del Sur `bhtwndktup59xhdycvb3` — 4S Ranch `bsjlyen2bxapxag0mmsc` — Scripps Ranch `qmbnozmfx7eolbfgvpgq`
- /neighborhoods page hero: `rdszydbnfr7blac6fidx`

**Section backgrounds & misc**
- "Work With Us" parallax bg (both pages): https://web.archive.org/web/20260104120026im_/https://media-production.lp-cdn.com/cdn-cgi/image/format=auto,quality=85,fit=scale-down,width=1920/https://media-production.lp-cdn.com/media/iewsuie9vnwodddwjt4l
- Testimonials fixed bg: .../width=1920/https://media-production.lp-cdn.com/media/cnhdl45tbr2mi8xiyzkz
- Newsletter section image: https://web.archive.org/web/20260104120026im_/https://media-production.lp-cdn.com/media/40dbb598-d983-41c6-90f0-d1e38801d06e
- Home-valuation section image: .../width=1280/https://media-production.lp-cdn.com/media/axrehxplbquil9mccrlv
- Hero video poster: https://web.archive.org/web/20260104120026im_/https://media-production.lp-cdn.com/media/5d3c2471-7430-46c9-a5d3-3c1d0ecd7565

**Hero videos** (Luxury Presence STOCK footage on Cloudinary — still live, no Wayback needed; also archived):
- Hero: https://res.cloudinary.com/luxuryp/videos/f_mp4,vc_h264,q_auto/fse1r1fgkpjyjpqw0jpn/hov-villa-with-pool-and-garden.mp4
- Selling CTA: https://res.cloudinary.com/luxuryp/videos/f_mp4,vc_h264,q_auto/oplddfmbe6b3z7moaqme/contemporary-modern-florida-exterior-rendering.mp4
- Buying CTA: https://res.cloudinary.com/luxuryp/videos/f_mp4,vc_h264,q_auto/cwj1ku1mokhu22ygniid/san-diego-coastline.mp4

Local working copies saved at /private/tmp/claude-501/-Users-jonkennedy-retainer-reach/f5ca62f0-8ef2-47cd-a0f9-01e21346550e/scratchpad/ (homepage.html, neighborhoods.html, team.html, producer.css, inline.css).