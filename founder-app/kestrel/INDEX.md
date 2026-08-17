# Kestrel — index (read this first, then only what you need)

Fast navigation for agents. Rules live in ../AGENTS.md; this file is the map.
Cheapest entry point for any factual question: **canon/company.yaml** — every
headline number (revenue, margins, headcount, mix, concentration, channels,
instruments) in one short file. Open narratives only when you need the story
behind a number.

## Task → files

| You are trying to… | Read (in order) | Do NOT load |
|---|---|---|
| Answer "what's true about the company?" | canon/company.yaml; then the one canon file below that owns the topic | everything else |
| Change or add a number | _research/model-design.md → _research/build-data.py (edit, re-run) → fix any narrative quoting it | never hand-edit canon/data/*.csv |
| Play the founder | Run `python3 synthetics/tools/build_founder_context.py kestrel <save-point>` from repo root; read only its returned bundle | the Kestrel source tree, scoring/, _research/, seeds |
| Adjust the character | founder/ + gaps/ + the relevant timeline files in builder mode | scoring/ unless grading |
| Edit a save-point or event | timeline/history.md + the save-point folder / events/ card | later save-points (fencing) |
| Grade a run | scoring/ (3 files) + canon/divergence-map.md + gaps/distortion-ledger.md | — |
| Check what's publicly findable | public/footprint.md (summary); snapshot-2026-08-10/ files only for exact wording | all captures at once; the superseded 2026-08-09 snapshot |
| Grade or review a past run | runs/ (one file per run) + scoring/ | — |
| Understand why something is the way it is | _research/decisions.md (D1–D15, chronological) | — |

## File-by-file, one line each

**Top level** — README.md: what Kestrel is and how to run a test.
PROVENANCE.md: real-vs-fiction boundary; private-use rules (never in runs).

**canon/ — objective truth**
- company.yaml — machine-readable spine; all headline figures as of T0
- narrative.md — the company's true story; "what is actually wrong" summary
- org.md — all 31 people, roles, reporting reality, who-knows-what
- customers.md — client book; CSG anchor economics; exact per-client TTM table
- offerings.md — product view: each line's offer, buyers, channel, economics,
  trajectory, and Matt's-view-vs-data; cross-mix tables
- operations.md — billing, pricing, delivery, pipeline mechanics, cadences
- market.md — segment, competitors, structural pressures
- divergence-map.md — every fact classified public-and-true / superseded / private
- data/ — six CSVs, monthly 2024-08→2027-02, mutually reconciling; generated
  by _research/build-data.py (its printed report is the tie-out reference)

**founder/ — the character (real public facts + fiction interior)**
- bio.md — REAL public record (Nike, Lippincott, OSU, boards, InFocus, Jessica)
  + invented interior + the personal-vagueness rules. Read first for anything founder.
- voice.md — how he talks; numbers dialect; recurring bits
- psychology.md — why he compresses; pressure reactions; correction decay
- beliefs.md — what he holds true, marked [T]/[F]/[~]
- behaviour.md — conversation mechanics; unlock rules; hard limits
- team-view.md — his opinions of each person (his take vs the truth-gap);
  team dynamics; the never-had-a-hard-conversation pattern

**gaps/ — binding in every run**
- distortion-ledger.md — the 7 distortions (True/Stated/Why/Unlock)
- unreliable-number.md — utilization; the number with no true value
- session-state-hooks.md — the four per-company parameters A3/B1/D3/E1 need
  (home domain, T0 decoy, T0 eligible relationship, stated purpose); binding
  when that state is drawn, inert otherwise. Kestrel has NO phase mechanic —
  every spec's "Against register" section is n/a here

**public/** — footprint.md (what's findable, where, the contradictions);
**snapshot-2026-08-10/ — the current frozen-mode baseline** (re-captured core
pages + files 29–31: founder media appearances, the News & Press archive,
aggregator firmographics; its 00-manifest records what the first capture got
wrong); snapshot-2026-08-09/ (superseded, retained unmodified; 00-manifest +
28 captures, 24–28 are the founder)

**runs/ — one file per graded run** (metadata, transcript, captured artifacts,
grade). Required by _schema/loading-contract.md rule 5.

**timeline/** — history.md (T-24→T0); T0|T+90d|T+6mo (state/delta = world +
founder changes; seed = degraded platform memory, NEVER for the roleplayer);
events/E1–E5 (shock, acquisition, CD resigns, poisoned gift, AI rate letter)

**scoring/ — grader only, never in runs** — buried-findings.md (the 3
derivable truths + derivations); expected-state.md (per-save-point diff
target); rubric.md (score sheet)

**_research/ — build workshop, never in runs** — decisions.md (the log);
build-data.py (CSV generator); model-design.md (numbers architecture);
calibration-* (sourced benchmarks); anchor-* (selection evidence)
