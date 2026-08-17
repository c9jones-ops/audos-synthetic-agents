# heron — index (read this first, then only what you need)

Rules live in ../AGENTS.md; this file is the map. Cheapest entry point for any
factual question: **canon/persona.yaml**. Fit questions: **canon/data/taste-
ledger.csv** (search the venue). Never bulk-read this folder in builder mode.

## Task → files

| You are trying to… | Read (in order) | Do NOT load |
|---|---|---|
| Answer "what's true about this seeker?" | canon/persona.yaml; then the one canon file that owns the topic | everything else |
| Check whether a venue is a hit | canon/data/taste-ledger.csv (row) → canon/taste.md (axis) | scoring/ unless grading |
| Change a verdict or add a venue | ledger row → re-check canon/taste.md, scoring/expected-fit.md, gaps/distortion-ledger.md `True:` fields, persona/beliefs.md tags → _research/decisions.md entry | — |
| Play the seeker | run `python3 travel/synthetics/tools/build_seeker_context.py heron <T1|T2>` from repo root; read only the returned bundle | this source tree, scoring/, _research/, PROVENANCE.md, events/ |
| Adjust the character | persona/ + gaps/ in builder mode | scoring/ unless grading |
| Edit a trip or event | trips/T1-*/brief.md, trips/T2-*/brief.md, trips/events/E*.md | — |
| Grade a run | scoring/ (3 files) + canon/divergence-map.md + gaps/ + the transcript + artifacts | — |
| Understand why something is the way it is | _research/decisions.md (D-01…) | — |

## File-by-file, one line each

**Top level** — README.md: who/what, design, how to run, caveats.
PROVENANCE.md: fiction boundary; venues real; private use (never in runs).

**canon/ — objective truth**
- persona.yaml — spine: identity, party (Sam = hard veto, decision-maker),
  constraints (knee 20 min, no queues, noise, £70/£120), taste axes, tools, trips
- taste.md — the one-line truth (booked, seated, quiet corner, near, one great
  dish) and the axes, quoting ledger ids; catalog venues' verdicts
- people.md — Sam (true filters and how she decides), Marcus (pressure), Cilla
- history.md — Cincinnati → Austin → the SF/LA trips → the Zuni evening → the
  knee → how the London trip came together (absolute dates; the booking)
- divergence-map.md — every fact: volunteered / when asked / never said / wrong
- data/taste-ledger.csv — 39 real venues; verdict, why, who_vetoes, in_catalog

**persona/ — the character (all fiction)**
- bio.md — convention, identity, money, relationships, what she'd never type
- voice.md — register, vocabulary, the Projector's places-and-numbers dialect
- psychology.md — projection not deception; fears; reactions; correction decay
- beliefs.md — [T]/[F]/[~] against canon and ledger ids; the private doubts
- behaviour.md — screen-by-screen session shape; the seven binding answer rules
- companions-view.md — her take vs the gap for Sam, Marcus, Cilla; party dynamics

**gaps/ — binding in every run**
- distortion-ledger.md — D-01 who decides · D-02 knee · D-03 spontaneity/bookings
  · D-04 loud rooms / the good evening (master) · D-05 pace · D-06 money; map
- unreliable-self-report.md — "we're foodies"; pass/fail
- session-state-hooks.md — D1 Sam · O1 eight pins · H1 BRAT from Marcus ·
  M1 the knee softened · X1 the five-venue tab

**trips/** — T1-london-anniversary/brief.md (2026-08-17 session; the verbatim
free text; the three "spots you love" with ids); T2-london-day3-replan/brief.md
(2026-08-27 16:30; the booking gone by her error; what she remembers of T1);
events/E1 Sam over the shoulder (T1) · E2 "hotel bar is fine" (T2) · E3 Marcus
texts (either)

**scoring/ — grader only** — expected-fit.md (hit/acceptable/miss per trip;
BRAT = flattering-but-wrong; the two reads); buried-findings.md (A filter is
Sam not cuisine · B dinner already booked · C calibration input vs memory);
rubric.md (§1–§8)

**runs/** — one file per graded run. **_research/** — decisions.md,
calibration.md, catalog-observations.md (never in runs)
