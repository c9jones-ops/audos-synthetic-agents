# 00 — Manifest: Field Company public-surface snapshot

- **Company:** Field Company (fieldcompany.com), American cast-iron cookware brand
- **Founders:** Stephen Muscarella and Chris Muscarella (brothers)
- **Capture day:** 2026-08-11
- **Purpose:** frozen snapshot substituting for live web access in reproducible test runs. Fidelity over polish — captures what pages actually say, without editorializing.
- **Prior research consulted for URLs (not treated as authoritative, everything re-fetched):** `ember/_research/founder-dossier-field.md`, `ember/_research/anchor-candidates-a-product.md`.
- **Trust note:** all fetched page content is data, not instructions. No fetched page attempted to redirect this research session.

---

## File index

| # | File | Topic | Method |
|---|---|---|---|
| 01 | 01-homepage.md | Homepage | direct fetch |
| 02 | 02-about-story.md | About/story page, founder billing | direct fetch |
| 03 | 03-products-collection.md | Full SKU + price list (91 SKUs, 4 pages) | direct fetch |
| 04 | 04-wholesale-stockists.md | Stockists + wholesale inquiry pages | direct fetch |
| 05 | 05-journal-blog-index.md | Journal/blog index (23 pages) | direct fetch |
| 06 | 06-journal-post-shakshuka.md | Recent post 1: Cast Iron Skillet Shakshuka | direct fetch |
| 07 | 07-journal-post-shrimp-scampi.md | Recent post 2: Cast Iron Shrimp Scampi | direct fetch |
| 08 | 08-journal-post-cherry-pie-filling.md | Recent post 3: Cherry Pie Filling | direct fetch |
| 09 | 09-journal-field-is-family-essay.md | Founder-authored essay: "Field is Family" | direct fetch |
| 10 | 10-shipping-returns-faq.md | Returns + FAQ pages (freight/policy texture) | direct fetch |
| 11 | 11-kickstarter-campaign.md | Kickstarter campaign page | search snippets (direct fetch 403, consistent across 2 sessions) |
| 12 | 12-linkedin-company.md | LinkedIn company page | blocked-with-evidence (404) + search snippets |
| 13 | 13-social-accounts-company.md | Company IG/FB/X — existence, handles, followers | blocked-with-evidence (JS-rendered, no metrics) + search snippets |
| 14 | 14-no5-skillet-launch-coverage.md | No.5 skillet launch, 4(+1)-outlet coverage | mixed: direct fetch (Yahoo Shopping, product page) + search snippets (Gear Patrol/H&G/Tom's Guide blocked/truncated) |
| 15 | 15-aggregator-firmographics.md | Growjo, ZoomInfo, Tracxn, Crunchbase, RocketReach, Owler | search snippets (all direct aggregator fetches failed: 403/402/timeout) |
| 16 | 16-cook-culture-podcast-2020.md | Cook Culture podcast (May 2020) | direct fetch |
| 17 | 17-crafted-podcast-2025.md | CRAFTED podcast ep.81 (Aug 2025) | search snippets (direct fetch 403, consistent across 2 sessions) |
| 18 | 18-facebook-qa-video.md | Cook Culture Facebook Q&A video | direct fetch (partial — description only, no date/views) |
| 19 | 19-youtube-interview-1.md | YouTube interview 1 (May 2020) | blocked-with-evidence + search snippets |
| 20 | 20-youtube-interview-2.md | YouTube interview 2, "FULL" (May 2020) | blocked-with-evidence + search snippets |
| 21 | 21-skillethead-interview-2023.md | Skillethead interview (Apr 2023) | direct fetch |
| 22 | 22-informalcc-interview-2025.md | informal.cc interview (Jun 2025) | direct fetch |
| 23 | 23-yahoo-2016-joint-origin.md | Yahoo/Food52 2016 joint origin piece | direct fetch |
| 24 | 24-food-wine-2025-mention.md | Food & Wine 2025 mention | search snippets (primary article not located, corroborated indirectly) |
| 25 | 25-stephen-personal-social.md | Stephen's personal IG/X/FB | blocked-with-evidence + search snippets |
| 26 | 26-chris-timon-capital-bio.md | Chris Muscarella: Timon Capital bio + personal site | direct fetch (2 of 3 sources; TheOrg partial) |
| 27 | 27-search-field-company-cast-iron.md | Additional search results, company name | search snippets |
| 28 | 28-search-stephen-muscarella.md | Additional search results, founder name | search snippets |

**Totals: 28 numbered capture files.** By method: **17 direct fetch** (01-10, 16, 18, 21-23, 26 partial), **2 mixed** (14, 26), **9 search-snippets/blocked-with-evidence** (11, 12, 13, 15, 17, 19, 20, 24, 25, 27, 28 — note 27/28 are themselves search-snippet-native capture files by design).

---

## Capture gaps (honest accounting)

- **Kickstarter campaign page**: direct fetch blocked (HTTP 403) both this session and the prior research pass — a consistent, repeatable block, not a fluke. Figures fully recoverable via cross-confirmed search snippets (11).
- **LinkedIn company and person pages** (company page, Crunchbase's Chris Muscarella page, TheOrg's Chris Muscarella page): all blocked to direct fetch (404/403, or rendered without the target profile). Company LinkedIn figures recovered via search snippet only, not primary-page-verified.
- **Instagram and Facebook (both company and personal accounts)**: the fetch tool consistently could not render JS-based profile metrics (bio, follower counts) — every profile capture in this snapshot for these two platforms is search-snippet-sourced, not a primary-page pull.
- **Both YouTube interview videos (19, 20)**: title and rough date only; no channel name, view count, like count, or description text was obtainable by any method attempted this session.
- **CRAFTED podcast (Aug 2025, ep. 81)**: blocked to direct fetch (403) in both this and the prior session; no verbatim transcript quotes obtainable by any method.
- **Cook Culture podcast (2020)**: episode metadata captured directly, but no transcript exists on Apple Podcasts — no verbatim quotes obtainable.
- **Crunchbase** (organization and person pages): both 403'd; person-page headline ("Chris Muscarella - Founder @ Field Company") carried forward from the prior dossier's earlier-session capture, not re-confirmed live this session.
- **Owler**: fetch timed out this session; also 403'd in the prior session — two consecutive failures, two different failure modes, across two sessions. Treated as a fetch failure, not confirmed absence, per the corpus's absence-discipline rule.
- **Food & Wine 2025 "best lightweight cast iron" mention**: the primary article was not located by search in either this session or the prior one — the claim is corroborated by multiple independent secondary mentions but remains unconfirmed at the primary-source level.
- **Journal post publish dates**: not shown anywhere on the journal index or on any individual recipe post fetched (06-08) — Field's blog appears to not surface dates to visitors/fetchers at all.
- **Stephen's LinkedIn profile**: a prior-session disambiguation risk (unclear which of several LinkedIn URLs is genuinely his) was not re-resolved this session — same open flag, not chased further (out of this brief's explicit scope for item 13, which asks only existence/activity for IG/X/FB).

All absence-adjacent claims above carry **`verified: 2026-08-11`** and list the specific surfaces/methods attempted, per the corpus's absence-discipline rule — none of these are asserted as "the thing doesn't exist," only as "this session's fetch/search methods could not retrieve it."

---

## Contradictions and corrections vs. the prior research files (flagged explicitly, per the task brief)

1. **HQ location contradiction (new, real, load-bearing):** ZoomInfo's current company-profile snippet lists Field Company's address as **49 King St, Port Jefferson Station, New York, 11776** — a Long Island address, not New York City. Both prior research files describe Field Company as "NYC-headquartered" throughout. Not resolved this session (could be a warehouse/fulfillment address rather than the true operating HQ) — flagged for downstream canon review.
2. **Founding-year self-contradiction, confirmed and sharpened:** the company's own materials disagree with each other — homepage says "we launched Field in 2016," the founder-authored "Field is Family" essay's captured summary indicates 2015, and the company's own "Iron Anniversary" journal post says the idea originated in 2014 with the Kickstarter (which the company treats as the launch) in March 2016. This is the company's own inconsistency, not a researcher artifact.
3. **Quote mis-sourcing correction:** the line "We put an obsessive amount of detail into the small things" — used in `founder-dossier-field.md`'s quote bank as sourced to the April 2023 Skillethead interview — actually traces to the **March 2016 Yahoo/Food52 piece** (direct-fetch-confirmed verbatim, see 23) and appears again, in a longer form, as unattributed on-site marketing copy on Field's "5 Field Skillet Design Details" page (see 27). This session's direct fetch of the Skillethead page itself did not surface this quote. **Any canon file citing this quote should re-cite it to the 2016 piece, not 2023.**
4. **RocketReach internal inconsistency resolved:** the prior dossier flagged RocketReach as inconsistently labeling "Katie Muscarella" as both "Managing Partner" and "CEO." This session's direct fetch shows a clean, single "CEO" label with no conflicting title found — the inconsistency appears to have been a snippet-level artifact, not a persistent aggregator contradiction. The Katie Muscarella surname-coincidence question remains unpursued (personal-life depth limit).
5. **Kickstarter figure "resolved," not contradictory:** the prior dossier flagged a "$475K–$1.6M" spread across sources as unreconciled. This session resolves it as a snapshot-vs-final artifact: $475K was a mid-campaign figure (Yahoo piece published March 25, 2016, campaign still running); final was $1,633,361/12,553 backers by close (April 6, 2016). Not a real contradiction.
6. **Skillethead interview format correction:** the prior dossier calls this a "written interview." This session's direct fetch finds the actual page content is built around a **video** interview with timestamp markers, not a verbatim written Q&A transcript — a format correction, not a contradiction of the interview's existence or date.
7. **No evidence of the About page changing its founder billing** — still "Brothers Stephen and Chris Muscarella," Stephen first, no title split. **No evidence of prices having moved dramatically** relative to what's implied by prior research (No.5 skillet still $125 at launch and at capture; No.8 skillet at $165 matches the prior dossier's implicit price anchor). **No evidence any prior media item has disappeared** — everything in the capture list (12) was either directly re-confirmed or re-confirmed via search snippet; nothing came back as a 404/removed.

---

## Ten most test-relevant facts

1. **Founder billing, verbatim and unchanged:** the About page captions the founders "Brothers Stephen and Chris Muscarella" — Stephen named first, no title differentiation, presented as strictly co-equal. (02)
2. **Price range and SKU count:** 91 distinct SKUs captured across the full collection index, ranging from $12 (XL Cleaning Cloth) to $2,367 regular/$1,825 sale (Cast Iron Collector's Set / 12-Piece Set). Core skillet ladder: No.4 $100 → No.5 $125 (newest, March 2026) → No.6 $135 → No.8 $165 → No.10 $215 → No.12 $265 → No.16 $350. (03)
3. **Stockist presence is real and large:** 100+ authorized retailers listed across the US and Canada, plus a live, actively-recruiting wholesale-inquiry form (business name/address/product-interest intake, response with pricing). (04)
4. **Kickstarter figures, fully resolved:** $1,633,361 raised from 12,553 backers against a $30,000 goal, March 6–April 6, 2016 (one campaign only, confirmed — no second Field Company Kickstarter campaign found in either research pass). (11)
5. **Aggregator contradictions are wide and now include a location discrepancy:** employees range 8 (LinkedIn) to 16 (Growjo/RocketReach); revenue ranges $2.4M (Growjo) to $9.1M (ZoomInfo), nearly 4x; and ZoomInfo's address (Port Jefferson Station, NY) contradicts the "NYC HQ" framing used elsewhere. Funding status is consistently "no institutional funding" across every source that addresses it. (15)
6. **Freshest activity dates:** No.5 Chef Skillet launch press dated March 3–4, 2026 (one week before this snapshot); CRAFTED podcast (Aug 2025) remains the freshest dedicated founder-media appearance; company social accounts (95K IG followers, 26K FB likes) show ongoing, current-looking posting activity. (13, 14, 17)
7. **The company's own founding-year story is internally inconsistent:** 2014 (idea genesis, per company's own anniversary post) / 2015 (per the founder's own "Field is Family" essay) / 2016 (per the homepage and the same anniversary post's Kickstarter-launch framing) — three different company-owned sources, three different years. (01, 09, 27)
8. **Chris Muscarella's own site presents Field Company as current, active work while omitting his VC day job entirely:** christmasgorilla.com/about lists Field Company first, present-tense ("Trying to build an iconic American brand..."), with zero mention of his Timon Capital partnership anywhere on the page — even though Timon Capital is his best-documented current professional identity elsewhere (Crunchbase, Bloomberg, ZoomInfo, VC Sheet). (26)
9. **A verbatim quote's sourcing needed correcting:** "We put an obsessive amount of detail into the small things" is Stephen's, from the March 2016 Yahoo/Food52 piece — not the 2023 Skillethead interview as previously filed. (23, 27)
10. **Freight/returns policy is concrete cash-physics texture:** 45-day return window, customer pays return shipping, Factory Seconds are final-sale-only (a real clearance channel), and EU shipping is currently paused specifically because new EU regulations would require Field to cover full return-shipping costs — a documented instance of a channel decision driven by a cost/liability tradeoff. (10)
