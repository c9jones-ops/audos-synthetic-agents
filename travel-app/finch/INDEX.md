# finch — index (read this first, then only what you need)

Rules live in ../AGENTS.md; this file is the map. Cheapest entry point for any
factual question: **canon/persona.yaml**. Fit questions: **canon/data/taste-
ledger.csv** (search the venue). Never bulk-read this folder in builder mode.

## Task → files

| You are trying to… | Read (in order) | Do NOT load |
|---|---|---|
| Answer "what's true about this seeker?" | canon/persona.yaml; then the one canon file that owns the topic | everything else |
| Check whether a venue is a hit | canon/data/taste-ledger.csv (row — the verdict is the *group's*) → canon/taste.md (axis) | scoring/ unless grading |
| Change a verdict or add a venue | ledger row → re-check canon/taste.md, scoring/expected-fit.md, gaps/distortion-ledger.md `True:` fields, persona/beliefs.md tags → _research/decisions.md entry | — |
| Play the seeker | run `python3 travel/synthetics/tools/build_seeker_context.py finch <T1|T2>` from repo root; read only the returned bundle | this source tree, scoring/, _research/, PROVENANCE.md, events/ |
| Adjust the character | persona/ + gaps/ in builder mode | scoring/ unless grading |
| Edit a trip or event | trips/T1-*/brief.md, trips/T2-*/brief.md, trips/events/E*.md | — |
| Grade a run | scoring/ (3 files) + canon/divergence-map.md + gaps/ + the transcript + artifacts | — |
| Understand why something is the way it is | _research/decisions.md (D-01…) | — |

## File-by-file, one line each

**Top level** — README.md: who/what, design, how to run, caveats.
PROVENANCE.md: fiction boundary; venues real; private use (never in runs).

**canon/ — objective truth**
- persona.yaml — spine: identity, party of five (Danny + Nate = hard vetoes),
  constraints ($45/$70; five people = two rides; Rafi veg + late Fri; Elliot
  doesn't drink), taste axes, tools, trips
- taste.md — the two-tastes truth (the group's big cheap table vs Devin's
  scene) and the axes, quoting ledger ids; likely-catalog verdicts
- people.md — Danny (the brief, the veto), Nate (money + rides), Elliot,
  Rafi; the group as a unit; nobody else
- history.md — Grand Rapids → UIUC → Chicago → LA ×2 → SF → Nashville 2024
  (the master-unlock night) → how the weekend came together (absolute dates;
  the chat messages verbatim)
- divergence-map.md — every fact: volunteered / when asked / never said / wrong
- data/taste-ledger.csv — 38 real venues; group verdict, why, who_vetoes,
  in_catalog (all unknown — LA catalog not observed at build)

**persona/ — the character (all fiction)**
- bio.md — convention, identity, money, relationships, what he'd never type
- voice.md — register, vocabulary, the Aggregator's "we"-for-"I" dialect
- psychology.md — aggregation not deception; fears; reactions; correction decay
- beliefs.md — [T]/[F]/[~] against canon and ledger ids; the private doubts
- behaviour.md — screen-by-screen session shape; the seven binding answer
  rules; list-and-share at the end
- companions-view.md — his take vs the gap for Danny, Nate, Elliot, Rafi;
  party dynamics

**gaps/ — binding in every run**
- distortion-ledger.md — D-01 who's coming / decides / the groom's brief
  (master) · D-02 two budgets · D-03 rides / near the house · D-04 Elliot
  (narrow key) · D-05 "cool" is one person (last trip) · D-06 Rafi late +
  veg; map
- unreliable-self-report.md — "the group's easy"; pass/fail
- session-state-hooks.md — D1 Danny · O1 eight pins · H1 Republique from
  Rafi · M1 the budgets softened · X1 the five-venue tab

**trips/** — T1-la-bachelor-weekend/brief.md (2026-08-17 session; the
verbatim free text; the three "spots you love" with ids; ends by sharing a
list); T2-la-replan-after-vetoes/brief.md (2026-08-24; Nate's number and
Danny's radius in the chat verbatim; re-edit and re-share); events/E1 Danny
replies (T1) · E2 Nate "just pick a taco place" (T2) · E3 Rafi's private
message about a show (either)

**scoring/ — grader only** — expected-fit.md (hit/acceptable/miss per trip;
Bestia = flattering-but-wrong; the two reads; the share/re-edit test);
buried-findings.md (A geography + two budgets, not vibe · B "cool" is one
person · C the brief already exists); rubric.md (§1–§8; §2 grades names /
refusals / who pays; §6 grades list, share, T2 re-edit recall)

**runs/** — one file per graded run. **_research/** — decisions.md,
calibration.md, catalog-observations.md (never in runs)
