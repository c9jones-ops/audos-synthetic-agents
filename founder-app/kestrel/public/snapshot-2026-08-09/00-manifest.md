---
snapshot_target: Watson Creative (Portland, OR creative studio)
snapshot_root_url: https://www.watsoncreative.com/
capture_date: 2026-08-09
purpose: Frozen public-web snapshot for private test corpus (kestrel synthetics). Files in this
  directory substitute for live web access in "frozen mode" research-agent testing.
---

# Manifest — Watson Creative Snapshot (2026-08-09)

> **SUPERSEDED 2026-08-10 — do not use as the frozen-mode baseline.**
> Use `../snapshot-2026-08-10/`. This capture reached three wrong conclusions
> that were written into canon and graded as critical errors: that the founder
> had no podcast or interview appearances, that no financial figures about the
> company were findable, and that no staff besides the founder were named
> anywhere. All three are false — see `../snapshot-2026-08-10/00-manifest.md`
> ("What the 2026-08-09 capture missed, and why") and `_research/decisions.md`
> D19. This directory is retained **unmodified** so that runs already graded
> against it stay interpretable.

## Capture Method Key
- **direct fetch** — WebFetch tool successfully retrieved and returned page content.
- **search snippets** — content derived from WebSearch result snippets, not a full page fetch.
- **blocked-with-evidence** — direct fetch attempted and failed (403/404); the failure itself is recorded, and any available snippet content is included as a clearly labeled substitute.
- **mixed** — a file combining more than one method for related sub-sources; see per-section notes inside the file.

## File Index

| # | File | Source URL | Method | Description |
|---|------|-----------|--------|-------------|
| 00 | 00-manifest.md | (this file) | — | Index of all captures + gaps |
| 01 | 01-homepage.md | https://www.watsoncreative.com/ | direct fetch | Homepage: nav, taglines, service list, industry categories, 4 office addresses, values, phone |
| 02 | 02-team-matt-watson.md | https://www.watsoncreative.com/team/matt-watson/ | direct fetch | Founder/CEO Matt Watson bio page: career history, roles, education, key numbers |
| 03 | 03-team-index.md | https://www.watsoncreative.com/team/ | direct fetch | Team roster page — at capture time featured only Matt Watson, no other named staff |
| 04 | 04-studio-about.md | https://www.watsoncreative.com/studio/ | direct fetch | Functional "About" page (note: /about/ 404s). Company history, headcount, founding-year claim (2008/2013), values, 4 offices |
| 05 | 05-services.md | https://www.watsoncreative.com/services/ | direct fetch | Six service categories (Strategy, Content, Digital, Experiential, Marketing, Consulting) with sub-services |
| 06 | 06-work-index.md | https://www.watsoncreative.com/work/ | direct fetch | Case study/portfolio index — 140+ client/project links captured with titles and slugs |
| 07 | 07-case-study-percipio-group.md | https://www.watsoncreative.com/portfolio/percipio-group-brand-strategy-consulting-firm/ | direct fetch | Case study: Percipio Group (consulting firm rebrand) |
| 08 | 08-case-study-courtesy-lincoln.md | https://www.watsoncreative.com/portfolio/courtesy-lincoln-automotive-advertising/ | direct fetch | Case study: Courtesy Lincoln dealership launch (listed as "Lincoln Motor Company" on index) |
| 09 | 09-case-study-craft3.md | https://www.watsoncreative.com/portfolio/craft3-branding-services/ | direct fetch | Case study: Craft3 financial institution rebrand |
| 10 | 10-case-study-umpqua-bank.md | https://www.watsoncreative.com/portfolio/umpqua-bank-business-marketing/ | direct fetch | Case study: Umpqua Bank business marketing (31%/23% metrics) |
| 11 | 11-case-study-oregon-state-university.md | https://www.watsoncreative.com/portfolio/oregon-state-university-athletics-college-football-marketing/ | direct fetch | Case study: OSU Athletics ($3M raised in first month) |
| 12 | 12-contact-locations.md | https://www.watsoncreative.com/contact/ | direct fetch | Contact page: 4 offices (Bend, Portland, Sausalito, Seattle) with full addresses, phone |
| 13 | 13-insights-index.md | https://www.watsoncreative.com/insights/ | direct fetch | Blog/insights index: macrotrends, "Notes from the Field," "Signals From the Market," "News & Press" sections with post titles, slugs, and dates |
| 14 | 14-blog-post-ats-brand-touchpoint.md | https://www.watsoncreative.com/insights/applicant-tracking-system-brand-touchpoint/ | direct fetch | Most recent blog post found (dated 7.29.26 per index) — full body + FAQ |
| 15 | 15-blog-post-candidate-experience.md | https://www.watsoncreative.com/insights/candidate-experience-employer-brand/ | direct fetch | 2nd most recent post (7.22.26) — full body |
| 16 | 16-blog-post-public-safety-recruiting.md | https://www.watsoncreative.com/insights/public-safety-recruiting-respond-capture/ | direct fetch | 3rd post captured (7.8.26) — full body |
| 17 | 17-linkedin-company.md | https://www.linkedin.com/company/watson-creative | direct fetch (unexpectedly succeeded; see caution note in file) | Company size, founding year (2012), HQ (Bend — conflicts with site), follower count, recent post themes |
| 18 | 18-clutch-profile.md | https://clutch.co/profile/watson-creative | direct fetch (unexpectedly succeeded; see caution note in file) | Rating 5.0/5, 60 reviews, service mix %, notable clients, founded 2008, employees 50-249 |
| 19 | 19-oregon-state-alumni-article.md | https://business.oregonstate.edu/blog/alumni/alum-matt-watson-started-his-own-portland-creative-agency-2013-now-its-thriving | direct fetch | Full alumni profile article: founding story, 2022 Weatherford Award, Design Thinking Scholarship Fund (2019) |
| 20 | 20-racc-matt-watson.md | https://racc.org/team/matt-watson/ | blocked-with-evidence (HTTP 404 x2) + search snippets | Matt Watson's RACC board bio — page unreachable by direct fetch; recovered via search snippet |
| 21 | 21-employer-reviews-indeed-glassdoor.md | indeed.com/cmp/Watson-Creative/reviews; glassdoor.com (2 URLs) | mixed (Indeed = direct fetch; Glassdoor = blocked 403 + snippets) | Employer review headline ratings: Indeed 4.5/5 (4 reviews); Glassdoor 4.1/5 (24 reviews, Portland) |
| 22 | 22-directory-profiles-and-search-snippets.md | Yelp, Agency Spotter, Digital Excellence Awards, + 3 general searches | mixed | Yelp (blocked), Agency Spotter (fetched: founded 2013, 50 employees, different Portland address), awards mentions, "Watson Creative Portland" general search rollup, discrepancy-pattern summary |
| 23 | 23-careers.md | https://www.watsoncreative.com/careers/ | direct fetch | Careers page: benefits, open roles, culture stats |

## What Could NOT Be Captured (and why)

1. **https://www.watsoncreative.com/about/** — HTTP 404. This path does not exist on the live site; the functional equivalent is `/studio/` (captured as file 04).
2. **https://www.watsoncreative.com/blog/** — HTTP 404. This path does not exist; the functional equivalent is `/insights/` (captured as file 13).
3. **https://racc.org/team/matt-watson/** — HTTP 404 on two separate direct-fetch attempts, despite being a valid indexed URL per search results. Full page content NOT captured; only a search-snippet-derived partial bio was recovered (file 20). This is a capture gap relative to the task brief's expectation that this page was capturable.
4. **Yelp business page** (yelp.com/biz/watson-creative-portland-2) — HTTP 403 Forbidden. Only the search-result title/snippet was recovered (file 22); no star rating or review text captured.
5. **Glassdoor company overview page** (glassdoor.com/Overview/...) — HTTP 403 Forbidden. Portland-specific rating/review-count figures were recovered only via search snippet (file 21), not a full page fetch.
6. **DesignRush, SelectedFirms, ReportGarden agency-directory profiles** — surfaced in search results but not individually fetched in full; only titles/URLs recorded in file 22 for completeness. Time/scope tradeoff — these are lower-priority directory duplicates of information already captured from Clutch and Agency Spotter.
7. **Instagram (@watsoncreative) and Pinterest (@watsoncreative)** — social links confirmed to exist (referenced in nav on every site page and in search results) but not fetched for post content; out of scope per task brief, which named LinkedIn and Clutch specifically as the social/review targets.
8. **Full FAQ text on file 15** (candidate-experience-employer-brand post) — the fetch tool returned only a summary of the FAQ section rather than verbatim Q&A text (unlike file 14, where full FAQ text was returned). Noted inline in that file.
9. **Quote truncation on Craft3 case study (file 09)** — two client/CEO quotes were returned truncated by the fetch tool ("...") rather than in full; verbatim complete text was not recoverable from this fetch method.

## Ten Most Test-Relevant Facts Captured

1. **Founding year is contested across sources**: site's own /team/matt-watson/ and the Oregon State alumni article both say **2013**; the site's own /studio/ page says **"Founded 2008"** (with "full-time launch 2013"); LinkedIn says **2012**; Clutch and Agency Spotter both say **2008** and **2013** respectively (Clutch: 2008; Agency Spotter: 2013). No single authoritative figure — treat as an open contradiction.
2. **Headcount is also contested**: site's /studio/ page says "45-60 employees annually"; LinkedIn says "11-50 employees" (~35 discoverable); Clutch says "50-249 employees"; Agency Spotter says "50 employees" flat.
3. **Founder/CEO**: Matt Watson, Founder & CEO (also styled "Executive Creative Director" in some sources). Prior career: Lippincott, then 11+ years at Nike (43 retail seasons, 5 Olympic Games, 52 pro athletes, led NIKEiD).
4. **Locations as the site itself presents them**: exactly four offices — **Portland, OR** (1001 SE Water Ave., 97214), **Bend, OR** (2900 NW Clearwater Dr., 97703), **Seattle, WA** (408 North 35th St., 98103), **Sausalito, CA** (480 Gate 5 Rd., 94965) — consistent across homepage, /studio/, and /contact/. This confirms the brief's expected four-city footprint.
5. **Service lines as named on site**: two overlapping namings exist — /services/ names six categories (Strategy, Content, Digital, Experiential, Marketing, Consulting); /studio/ separately names a four-stage "Systems of Meaning" framework (Strategy, Creative, Development, Campaigns). Both are live simultaneously.
6. **Client roster on site**: 140+ named clients/projects at /work/, spanning Nike, Apple (per bio text, not seen as a direct portfolio link), EA Sports, PlayStation, Disney Marvel, LEGO (per bio), plus directly-linked portfolio clients including Kaiser Permanente, Capital One, Eddie Bauer, Budweiser, Halo/Microsoft, Boston Bruins, New York Yankees, Denver Broncos, Las Vegas Raiders, Portland Trail Blazers, Portland Timbers, Seattle Sounders FC, California Highway Patrol, and dozens of Pacific Northwest banks, architecture firms, and nonprofits.
7. **Blog freshness**: most recent post at capture time was dated **7.29.26** ("The ATS Is a Brand Touchpoint"), 11 days before the 8/9/26 capture date — indicating an active, roughly weekly-cadence blog as of capture day.
8. **Clutch**: **60 reviews, 5.0/5 overall rating** (quality 5.0, schedule 4.9, cost 5.0, referral 5.0), min. project size $25,000+, hourly rate $150-199.
9. **Employer reviews**: Indeed 4.5/5 (4 reviews); Glassdoor ~4.1/5 (24 reviews, Portland-specific), 76% would recommend — with some negative outlier snippets also surfaced ("felt like a facade").
10. **Awards/recognition**: Matt Watson individually received the **2022 Weatherford Award** from OSU College of Business; company references a **2021 Clutch "Leader Award for Top B2B Companies in Oregon"** in its own news archive; LinkedIn snippet also referenced "Top 100 fastest-growing Portland agency, 2nd consecutive year" (unverified against a primary award-issuing source).

## Flags Relative to the Original Task Brief

- **Founder team page** (https://www.watsoncreative.com/team/matt-watson/) — confirmed still live and fetchable at capture time, matching the brief's expectation.
- **Four office locations** (Portland, Bend, Seattle, Sausalito) — confirmed exactly as the brief described; no discrepancy here.
- **RACC page** — brief implied this would be capturable; it was NOT (HTTP 404 on repeated direct-fetch attempts). This is the one target explicitly named in the brief that could not be directly captured, despite being confirmed as a real/indexed URL via search.
- **LinkedIn and Clutch** — brief said these "usually block fetches" / "403'd earlier today." On this capture attempt, both returned content via the WebFetch tool rather than blocking. This is noted with an explicit caution flag in files 17 and 18, since it contradicts the brief's stated expectation and the underlying render/verification method differs from a browser-confirmed capture.
- **Biggest new finding not flagged in the brief**: the company's own site is internally inconsistent about its founding year (2008 vs. 2013) and uses two different service-taxonomy namings on different pages (/services/ vs. /studio/). Third-party sources compound this with a third figure (2012, LinkedIn). This numeric instability across founding-year and headcount claims is the most significant data-quality issue in the snapshot and is flagged for the research agent's awareness.
