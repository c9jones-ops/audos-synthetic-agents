# Synthetic Companies: Test Infrastructure Design

**Date:** 2026-08-08
**Owner:** Casey Jones
**Status:** Approved design, ready for implementation planning

## Purpose

Build a small corpus of synthetic founder-led companies used to test the founder-support
platform repeatedly, comparably, and over time. Each company is a durable asset that
outlives any particular version of the product: it describes a business and a founder,
not a set of product screens.

The corpus must support three things the platform claims to do and that a single
conversation cannot test:

1. **Drift detection** — behaviour diverging from stated commitments over months.
2. **Durability of no's** — a rejected path quietly reopening later.
3. **Crisis retrieval** — prior decisions and assumptions retrieved under pressure.

## Core principles

**Clean company, messy founder.** The company's data is accurate and internally
consistent. The founder's account of it is not. Every gap between the two is deliberate,
documented, and gradeable. This mirrors the product's own epistemics — fact,
interpretation, assumption, decision, commitment — and makes the corpus useful for
testing extraction quality rather than just conversational feel.

**Product-agnostic structure.** Folders are organised by epistemic role, not by product
surface. Nothing references State panels, Thread Maps, or Gap Check. If the product is
renamed or restructured, the corpus is unaffected.

**Real company, invented founder.** Each synthetic company is anchored to a real,
researchable business so the platform's live research capability can be tested against a
genuine web footprint. The person in the founder's chair is entirely fictional.

**Deltas, not restatements.** The company is authored once. Later save-points record only
what changed.

## Run model

Three test modes, all drawing on the same folder.

| Mode | What happens | Primarily tests |
|---|---|---|
| **Foundation roleplay** | Fable plays the founder in live conversation from `T0`. Platform receives the real company name and URL and researches it. | Research quality, elicitation, extraction, handling of public/private conflict |
| **Seeded save-point** | Platform is loaded with a prior state and advanced to a later save-point. | Drift detection, durability of no's, delta quality |
| **Event injection** | An event card is played into any save-point, with Fable in character. | Crisis retrieval, tripwire reasoning, reactive-vs-evidence separation |

Foundation roleplay runs in either **live mode** (agent researches the live web — realistic,
not perfectly reproducible) or **frozen mode** (agent is given the captured snapshot —
fully reproducible). Every run records which mode was used.

## Folder architecture

```
synthetics/
├── README.md                      # how to run a test
├── coverage.md                    # matrix: which company tests which behaviour
├── _schema/
│   ├── company.schema.yaml        # required fields, shared across all companies
│   ├── financials.spec.md         # CSV columns + tie-out rules
│   ├── loading-contract.md        # who reads what, per run type
│   └── authoring-guide.md         # rules for building the next company
│
└── <codename>/
    ├── README.md                  # one page: who, what, why this one exists
    ├── PROVENANCE.md              # real company named here and nowhere else
    │
    ├── canon/                     # objective reality — clean, tied out
    │   ├── company.yaml
    │   ├── narrative.md
    │   ├── org.md
    │   ├── customers.md
    │   ├── operations.md
    │   ├── market.md
    │   ├── divergence-map.md      # canon vs. public reality, fact by fact
    │   └── data/
    │       ├── pnl-monthly.csv
    │       ├── revenue-by-line.csv
    │       ├── headcount.csv
    │       ├── customers.csv
    │       ├── pipeline.csv
    │       └── channels.csv
    │
    ├── founder/                   # the character bible
    │   ├── bio.md
    │   ├── voice.md
    │   ├── psychology.md
    │   ├── beliefs.md
    │   └── behaviour.md
    │
    ├── public/
    │   ├── footprint.md           # what exists publicly, where, how findable
    │   └── snapshot-YYYY-MM-DD/   # captured copy for frozen mode
    │
    ├── timeline/
    │   ├── history.md             # T-24 → T0
    │   ├── T0/{state.md, seed.md}
    │   ├── T+90d/{delta.md, seed.md}
    │   ├── T+6mo/{delta.md, seed.md}
    │   └── events/                # forward event deck
    │
    ├── gaps/                      # Fable's script for being imperfect
    │   ├── distortion-ledger.md
    │   └── unreliable-number.md
    │
    ├── scoring/                   # Casey only — never enters a run
    │   ├── buried-findings.md
    │   ├── expected-state.md
    │   └── rubric.md
    │
    └── _research/                 # calibration material — never enters a run
```

Five content folders, each answering one question: `canon` is what is true, `founder` is
who is telling you, `timeline` is when, `gaps` is where telling diverges from truth,
`public` is what the world can see. `scoring` and `_research` are excluded from every run.

## The loading contract

The single most important operational file. Getting it wrong invalidates a run without
being obvious afterward.

| Run type | Fable reads | Platform receives | Never loaded |
|---|---|---|---|
| Foundation roleplay (live) | `canon/`, `founder/`, `gaps/`, `timeline/` up to `T0` | Company name + live URL; conversation only | `scoring/`, `_research/`, timeline beyond `T0` |
| Foundation roleplay (frozen) | Same | Company name + `public/snapshot-*/` | Same |
| Seeded save-point | Absent, or the same set as roleplay fenced to the save-point if follow-up questions are needed | `timeline/<save-point>/seed.md` | `scoring/`, `_research/`, canon, timeline beyond save-point |
| Event injection | Above, plus the event card | Prior session state; conversation | `scoring/`, `_research/`, timeline beyond save-point |

**Timeline fencing is mandatory.** Fable must never read past the current save-point. A
founder who has seen `T+6mo` will foreshadow, and every drift test is silently ruined.

**Seeds are degraded, not perfect.** `seed.md` represents what the platform would
plausibly hold at that point — the output of a decent prior run, not a copy of canon.
Seeding canon directly would grant perfect knowledge and invalidate the test.

## The divergence map

Because the anchor company is real, the platform will find real facts that our canon
contradicts. `canon/divergence-map.md` classifies every material fact so scoring stays
unambiguous.

| Class | Meaning | What it tests |
|---|---|---|
| **Public-and-true** | Canon agrees with what is findable | Research quality — found, correct, cited |
| **Public-but-superseded** | Findable, but canon says otherwise | Whether researched facts are held as provisional and updated when the founder corrects them |
| **Private-only** | Not findable at all | Elicitation |

The middle class is the most valuable and the main reason to anchor to real companies:
the agent arrives with confident, specific, wrong beliefs, and the founder corrects them.
That is what happens in every real onboarding. The behaviour under test is whether a
corrected fact receives the right provenance, stays corrected, and does not resurface
from the stale public version three sessions later.

## Distortion ledger

Five to eight load-bearing distortions per founder, each with four fields:

- **True** — what canon says
- **Stated** — what the founder says instead
- **Why** — the psychological or social reason
- **Unlock condition** — what specifically causes them to correct it

The unlock condition is what turns a distortion from a static fact into a test of the
platform's questioning. It lets a run be scored three ways: did the platform notice, did
it probe well enough to break through, and did it record the corrected fact with the
right provenance.

Ambient messiness — hedging, tangents, tone, pet topics — is not enumerated. It comes
from `founder/` and is free to vary between runs.

## Data fidelity

**Tied-out headline, illustrative detail.** The P&L foots. Headcount ties to payroll.
Revenue ties to units, price, and mix. Below that — named customers, pipeline entries,
individual projects — is representative rather than exhaustive.

**Canon must be plausible behind the real anchor's facade.** Numbers are not invented
freely. They sit in a credible relationship to whatever the real company publicly
discloses, diverging on the things public sources never show: mix, concentration, channel
economics, and what the founder actually knows.

**Two deliberate imperfections per company:**

1. **Buried findings (2–3).** Fully derivable from clean data, never mentioned by the
   founder, listed in `scoring/`. Not errors — the drift the product exists to surface.
2. **One unreliable number.** The single figure nobody owns, flagged in `gaps/` as
   unreliable-and-known-to-be. Supports the real founder question: which of these numbers
   can I actually trust?

**Formats.** Markdown for narrative. CSV for anything with a time series, so it diffs in
git and needs no tooling to read. One `company.yaml` per company as the machine-readable
spine, conforming to `_schema/company.schema.yaml`.

**Required schema fields:** team size and composition, revenue, gross margin, cost
structure, channels, functions, capabilities, product mix, customer concentration,
capital model, governance, growth posture, geography. Enough for a finance, strategy, or
CEO question to be answerable; not so much that authoring collapses.

## Timeline and events

History runs T-24 to T0. Save-points at `T0`, `T+90d`, `T+6mo`. CSVs run continuously
across the whole span so numbers are never restated. Delta files carry only what changed
in the world and in the founder's head, pointing at date ranges in the data.

The **event deck** holds pre-written forward events — an anchor customer churns, inbound
acquisition interest, a key departure, a competitor move — playable into any save-point.
Events are described in business terms, never product terms, so they survive product
change. The deck is also where **consequential-fork** tests live: a fork played against a
founder with two years of accumulated context is a better test than a company that exists
only at its decision point.

## Real company, invented founder

Each company is anchored to a real business. `PROVENANCE.md` names it — and is the only
file that does, alongside wherever the harness passes the URL. Codenames are used
everywhere else so the anchor can be swapped without rewriting the corpus.

The founder is fiction: invented name, history, and psychology. This is a hard rule.
`gaps/` and `founder/psychology.md` contain material that is appropriate about a
character and inappropriate about an identifiable living person, and these files are
routinely pasted into prompts and rendered into outputs.

`PROVENANCE.md` states plainly: company real, founder and all internal data fiction,
private test infrastructure, not for publication. Anchors are preferred where the founder
has a low public profile.

**Snapshot on build day.** Capture website, LinkedIn, press, and filings into
`public/snapshot-YYYY-MM-DD/`. Re-snapshot periodically and diff; the diff shows when a
baseline moved and why an old test now reads differently.

## The persona slate

Three companies, chosen so they differ in the relationship between truth and numbers —
not merely in industry.

| | **Kestrel** | **Fenwold** | **Orrery** |
|---|---|---|---|
| **Anchor** | TBD at build time | Janji (Boston, founded May 2012) | HappyRobot (San Francisco; founding year to confirm in the research pack, comfortably inside the 15-year rule) |
| **Archetype** | Founder-led creative/digital studio, 25–50 people | Founder-led consumer brand, founder 12–14 years in | AI-native B2B, Series C hypergrowth |
| **Persona** | Opportunity-Rich Overloaded Operator | Post-Inflection Identity Drifter | Signal-Saturated Scaling Founder |
| **Capital** | Founder-funded | Founder-led, largely self-funded | VC, Series C |
| **Distortion** | **Compressor** — rounds favourably, believes it, answers the question he wishes you'd asked | **Withholder** — short answers, deflects personal questions back to the business | **Narrator** — speaks in the version he has been pitching; the board account became the internal account |
| **Unlock** | Walk me through one job's costs | Sustained non-business attention | A specific recent week — what happened Tuesday |
| **Truth vs. numbers** | In the data, **uncomputed** | **Not in the data at all** — the business is fine | **Actively misleading** — reported numbers are constructed |
| **Hunts for** | Does it probe, or accept a summary as fact? | Does it invent a business problem to solve? | Does it survive a founder more articulate than it is? |
| **Public footprint** | Thin | Moderate | Heavy and contradictory |

**Footprint diversity is deliberate.** Orrery's anchor has heavy, very fresh funding
coverage and genuinely conflicting headcount figures across sources — a free test of
whether the platform notices contradiction. Kestrel's anchor will have a thin,
badly-indexed footprint, testing what happens when research returns almost nothing: does
the platform say so, or confabulate?

**Fenwold is the inverse test and the reason the slate is not three flavours of one
thing.** The correct output is that the business is healthy and the problem is the
founder. A platform built to find business problems will manufacture one. Reaching the
right answer requires noticing deflection, and nothing else in the corpus tests that.

### Deferred

**Mission-Burdened Builder** — church plant or small charity, where winning is not
commercial. The only remaining candidate that adds a genuine axis rather than a flavour.
Recorded in `coverage.md` as a known gap; build when the first three have earned it and
the brand strategy treats the segment as more than an adjacency.

**Consequential-Fork Founder** — not a company. Built as event cards, per above.

## Build sequence

1. **Kestrel** — establishes `_schema/` on the simplest shape. Anchor selection is step
   one of this session, via a dedicated research pass.
2. **Fenwold** — cheap to author (the numbers are simply good) and surfaces the
   "answer isn't in the data" case while the schema is still soft.
3. **Orrery** — most authoring effort; schema should be settled first.

**Before building Fenwold**, draft Orrery's `company.yaml` and CSV headers only, to
confirm the schema stretches from a 25-person studio to a venture-backed company at
scale. Cheap de-risk; avoids retrofitting two finished folders.

**Snapshot Orrery's anchor early** — its Series C landed 4 August 2026 and coverage is
still accumulating.

Each company is built in its own session. Session one of each begins with the research
pack: comparables, calibration benchmarks, public-surface patterns, founder voice in that
sector, sources cited — landing in `_research/`, excluded from all runs.

## Open questions

- **Scoring automation.** Runs are graded by hand initially. Whether the diff between
  extracted state and `scoring/expected-state.md` can be partially automated is unresolved
  and should not be designed for until several runs have been graded manually.
- **Event deck size.** Start with three or four cards per company and grow from use.
- **Save-point count.** Three may prove too few for drift work; adding a `T+12mo` is
  cheap under the delta model if needed.
- **Kestrel anchor.** Resolved at build time. The name-collision case — a company sharing
  a name with a far more prominent one — is a legitimate hard-mode option but should not
  be the default, since it risks contaminating every other signal from that persona.
