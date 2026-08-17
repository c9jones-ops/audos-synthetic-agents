---
snapshot_target: Watson Creative (Portland, OR creative studio)
snapshot_root_url: https://www.watsoncreative.com/
capture_date: 2026-08-10
supersedes: snapshot-2026-08-09/ (retained unmodified; see "Relationship to the
  previous capture" below)
purpose: Frozen public-web snapshot for private test corpus (kestrel synthetics).
  This directory is the frozen-mode baseline going forward.
---

# Manifest — Watson Creative snapshot (2026-08-10)

## Why this capture exists

The 2026-08-09 capture concluded that the founder had no podcast or interview
appearances, that no financial figures about the company were findable, and
that no staff member besides the founder was named anywhere. All three were
written into canon and graded as critical research errors when violated.

On 2026-08-10, a platform under test cited two of the founder's real podcast
appearances. The grader scored them as doppelganger contamination — because the
corpus said they could not exist. Verification proved the platform right. An
adversarial sweep of every absence claim followed, and four of ten were wrong
or overstated (_research/decisions.md D19).

**This capture is the corrected baseline.** It is also the reason the authoring
guide now requires absence claims to be verified by searching FOR the thing.

## Capture method key

Same as the previous manifest: **direct fetch** · **search snippets** ·
**blocked-with-evidence** · **mixed** · and new here, **carried forward** —
the 2026-08-09 file is still accurate and was not re-fetched this pass.

## File index

| # | File | Source | Method | Note |
|---|---|---|---|---|
| 00 | this file | — | — | Index, gaps, and the correction record |
| 01 | 01-homepage.md | watsoncreative.com | direct fetch | **RE-CAPTURED — drifted.** New three-segment industry taxonomy; homepage no longer states headcount or founding year |
| 02 | 02-team-matt-watson.md | /team/matt-watson/ | direct fetch | **RE-CAPTURED — two new facts.** George Fox MBA (earned while at Nike); declined RISD President's Scholarship. Neither was previously recorded |
| 03 | 03-team-index.md | /team/ | direct fetch | **RE-CAPTURED.** Still names only the founder — but the previous over-generalisation from this page is corrected in-file |
| 04 | 04-studio-about.md | /studio/ | direct fetch | **RE-CAPTURED.** Founding-year, headcount and taxonomy contradictions all confirmed live |
| 05 | 05-services.md | /services/ | direct fetch | **RE-CAPTURED.** Six categories, unchanged |
| 12 | 12-contact-locations.md | /contact/ | direct fetch | **RE-CAPTURED.** Addresses unchanged; Bend now described as an offsite venue |
| 13 | 13-insights-index.md | /insights/ | direct fetch | **RE-CAPTURED.** Blog active; cadence now bursty rather than weekly |
| 29 | 29-founder-media-appearances.md | Apple Podcasts, pod.co, justcreative.com, watsoncreative.com | direct fetch | **NEW.** Two podcasts + a radio segment, with verbatim quotes. The correction that triggered this capture |
| 30 | 30-news-press-archive.md | /insights-category/news-press/ | direct fetch | **NEW.** Real press mentions and one publicly named staff hire |
| 31 | 31-aggregator-firmographics.md | Growjo, ZoomInfo, Crunchbase et al. | blocked-with-evidence + snippets | **NEW.** Findable revenue/headcount estimates (~$7M, 27 employees) |
| 06–11, 14–28 | (in snapshot-2026-08-09/) | — | **carried forward** | Case studies, blog post bodies, LinkedIn, Clutch, alumni article, RACC, employer reviews, directories, careers, founder LinkedIn/voice/community/social/personal-details. Not re-fetched this pass; see gaps below |

## What could NOT be captured (2026-08-10)

1. **racc.org/team/matt-watson/** — still HTTP 404 on direct fetch, exactly as
   on 2026-08-09. The three-way board-title contradiction (Secretary / Board of
   Directors / Finance Chair) therefore **could not be re-confirmed at source**.
   File 02 confirms "Secretary" from the studio's own page; the other two
   variants rest on the previous capture's snippet evidence. Treat that
   contradiction as unverified, not confirmed.
2. **Growjo and ZoomInfo** — HTTP 403. Figures recovered from search snippets
   only (file 31). This is materially the same route a research agent takes.
3. **LinkedIn company page** — not re-fetched directly this pass. The founding
   year (now 2013, previously 2012) and HQ (now Portland, previously Bend) are
   **snippet-derived and lower confidence**. Both changes matter: they shrink
   one scoring contradiction and appear to kill another. Confirm by direct
   fetch at the next capture before retiring the HQ row for good.
4. **Files 06–11 and 14–28 were not re-fetched.** They are carried forward. Any
   of them may have drifted; the four that matter most for scoring (01, 02, 04,
   05) were re-captured deliberately.

## Relationship to the previous capture

`snapshot-2026-08-09/` is **retained unmodified**. Any run graded against it
stays interpretable, and its errors are part of the corpus's history rather
than something quietly overwritten. Frozen-mode runs from 2026-08-10 onward
should be given **this** directory.

## What the 2026-08-09 capture missed, and why

A record of the defect class, for the next company's build:

1. **It searched for pages it expected, not for facts it doubted.** The founder
   media search was never run as its own query. Two podcasts, both indexed on
   Apple and Spotify, one with 43 minutes of audio and published show notes.
2. **It indexed a page without opening it.** The News & Press archive was
   listed in file 13 and never fetched. Inside it: a named staff hire and the
   real press mentions — the exact two things the corpus then declared absent.
3. **It followed a link outward but not the link back.** The radio appearance
   was published on the studio's own blog, which had been captured.
4. **It treated fetch failure as nonexistence.** Growjo and ZoomInfo 403, so
   their figures were recorded as unfindable. They are visible in search
   snippets to anyone who looks — which is how research agents actually read.
5. **It generalised one page into a category claim.** The team page names only
   the founder; that became "no named staff findable anywhere."

Common root: **absence was inferred from the shape of the search, not tested.**
The fix now lives in _schema/authoring-guide.md and _schema/loading-contract.md
rule 7.

## Contradictions status at this capture

| Contradiction | Status |
|---|---|
| Founding year 2008 vs 2013 | **LIVE** — on the company's own site. Formerly three-way; LinkedIn's 2012 is now 2013 |
| Headcount | **LIVE and wider** — 45–60 / 11–50 / 50–249 / 50 / ~27. Five sources, ~9× spread |
| HQ Portland vs Bend | **APPEARS DEAD** — LinkedIn now reads Portland. Snippet-derived; confirm before retiring |
| Service taxonomy | **LIVE** — six flat categories vs a three-stage framework, both under "Systems of Meaning" |

Three of the four moved within a year of authoring. Re-verify before grading a
run against any of them.
