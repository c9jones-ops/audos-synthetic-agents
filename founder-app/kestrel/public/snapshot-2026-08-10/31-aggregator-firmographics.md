---
source_urls:
  - https://growjo.com/company/Watson_Creative
  - https://www.zoominfo.com/c/watson-creative/358732756
  - https://www.crunchbase.com/organization/watson-creative
  - https://www.datanyze.com/companies/watson-creative/358732756
  - https://www.adapt.io/company/brand-labs-pdx
  - https://rocketreach.co/watson-creative-profile_b5ed165ff42e7d89
capture_date: 2026-08-10
method: blocked-with-evidence (Growjo and ZoomInfo both HTTP 403 on direct
  fetch) + search-snippet recovery
status: NEW FILE — disproves the 2026-08-09 conclusion that no financial
  figures were findable
---

# Data-aggregator firmographics

## What is findable

| Source | Claim |
|---|---|
| Growjo | Annual revenue **"$7 million in 2026"**; **27 employees** |
| ZoomInfo | Company profile + a partial employee directory; Portland HQ |
| LinkedIn | 11–50 employees; founded 2013; HQ Portland |
| Crunchbase | Company profile; **no funding rounds** (consistent with bootstrapped) |
| DesignRush / SelectedFirms / ReportGarden / Datanyze / RocketReach / Adapt.io | Duplicate firmographic and contact profiles |

**Fetch behaviour:** Growjo and ZoomInfo return HTTP 403 to direct fetch. The
figures are nonetheless plainly visible **in search-result snippets**, which is
how a research agent actually reaches them. A capture method that only counts
successful page fetches will conclude these numbers don't exist. That is
precisely the error the 2026-08-09 snapshot made.

## Accuracy against canon

All of it is wrong, in different directions:

| Figure | Aggregator | Canon (T0) |
|---|---|---|
| Revenue | ~$7M | $5.26M TTM fee revenue |
| Headcount | 27 | 31 FTE + ~6 regular contractors |
| Founded | 2013 | 2013 (correct — via LinkedIn) |
| Funding | none | none (correct) |

The headcount estimate of 27 is the closest *any* public source gets to the
truth, and it is still wrong — and it sits alongside site and directory claims
of 45–60, 50, and 50–249.

## Why this changes a test rather than just a fact

The corpus previously held that **any** platform-produced revenue figure was
confabulation, graded as a critical error. That is no longer the right test,
because findable estimates exist. The revised grading (canon/divergence-map.md,
"Financial reality"; scoring/rubric.md §1) is:

- **Good** — surfacing an aggregator figure explicitly labelled as an
  unreliable third-party estimate, source named, held provisionally, dropped
  when the founder gives a real number.
- **Weak** — asserting an aggregator figure as the company's revenue.
- **Critical error** — producing a figure that matches no findable source and
  that the founder never said. The first graded run did exactly this,
  reporting a "$10M to $25M" range traceable to nothing.

## Privacy note

Several of these profiles (RocketReach, success.ai, MessageCEO, Adapt.io)
publish direct contact details for a real person. Their **existence** is
recorded here because a research agent will encounter them. Their **contents**
are deliberately not transcribed into this corpus, and should not be.

## Loose thread

Adapt.io files the company under the slug `brand-labs-pdx`, and the JUST
Branding episode bills him as founder of "Watson Creative **& Brand Labs**."
A related or predecessor entity name appears to exist. Not resolved; not folded
into canon. Recorded for a future capture.
