# Kestrel

A synthetic founder-led creative studio, built as a test instrument for the
founder-support platform. First company in the corpus; establishes _schema/.

## Who and what

**The company:** a ~31-person, $5.3M, founder-owned Portland creative studio,
thirteen years old, bootstrapped, profitable-but-thinning. Anchored to a real,
researchable business ("Kestrel" is the corpus label; the real company and
founder names appear where the player needs them — see PROVENANCE.md)
whose public footprint is thin-but-real — including genuinely contradictory
public facts (founding year, headcount) that are themselves part of the test.

**The founder:** Matt Watson — the anchor's real founder, by real name and
real public biography (interior is fiction; see PROVENANCE.md), ~49 — the Opportunity-Rich Overloaded
Operator. Distortion class: **Compressor**. He does not lie; he rounds
favourably, believes the rounding, and answers the question he wishes you'd
asked. He is honest at the instance level and distorted at the aggregate level,
which is exactly where the unlock design lives: vague persistence gets warmth;
one specific instance ("walk me through one job's costs") gets truth.

**What this company tests:** does the platform probe, or accept a fluent
summary as fact? Plus, across save-points: drift detection (a pricing floor
quietly breaks), durability of a no (a parked acquisition approach returns),
and crisis retrieval (five event cards).

## The design in one paragraph

Canon is clean and tied out (a fresh-context auditor reproduced every headline
number from the CSVs; the generation script and tie-out report are in
_research/). The founder's account diverges from canon in exactly seven
documented, unlockable ways (gaps/distortion-ledger.md), plus one number that
is unreliable *inside the fiction* (utilization — gaps/unreliable-number.md).
Three findings are buried in the data, derivable but never voiced
(scoring/buried-findings.md) — verified reachable by a cold-read analyst.
Everything material is classified public-and-true / public-but-superseded /
private-only in canon/divergence-map.md, which is what makes runs gradeable.

## How to run a test

The corpus-level run modes and loading rules are in ../_schema/
loading-contract.md (authoritative). Summary: Foundation roleplay — the
founder-player reads only a generated T0 bundle from
`../tools/build_founder_context.py`; the platform gets the real company name + URL (live mode) or
**public/snapshot-2026-08-10/** (frozen mode — the current baseline). Seeded
runs — platform gets timeline/<save-point>/seed.md, and the founder-player gets
a bundle fenced to that save-point. Event runs require the isolated event
harness until the bundle builder supports exactly-one-card selection.
**The founder-player never reads the source company tree.** Capture the platform's persistent artifacts
at end of run, not just the transcript (loading-contract rule 5) — the rubric's
Recorded axis and §7 are ungradeable without them. Grade afterwards against
scoring/ (expected-state per save-point, the distortion table, the rubric), and
record the run in runs/.

## Map of the folder

- canon/ — objective truth: yaml spine, seven narratives (incl. offerings.md,
  the product/mix view), divergence map, and data/ (six CSVs, monthly,
  Aug 2024–Feb 2027, mutually reconciling).
- founder/ — the character: bio, voice, psychology, beliefs, behaviour, and
  team-view (his opinions of each person vs the truth).
- gaps/ — the script for being imperfect: 7 distortions + unreliable number.
- public/ — footprint description + frozen snapshot (2026-08-09, 24 files).
- timeline/ — history T-24→T0; save-points T0 / T+90d / T+6mo (delta + seed
  each); events/ (five cards, E1–E5).
- scoring/ — grader-only: buried findings, expected state, rubric.
- _research/ — calibration, anchor selection, decision log, the data
  generation script. Excluded from all runs.

## Caveats a grader should know

- Seeds are deliberately degraded (each lists its own planted misses at the
  bottom — those are test surface, not errors).
- The founder convention (revised 2026-08-09): the character IS the real
  founder at the public layer — real name (in runs), real career facts, real
  founding story — because the platform's research reliably finds real
  founders. The founder appears by his real name throughout; the interior
  (psychology, distortions, personal texture) is fiction, and non-public
  personal life is kept vague by rule (founder/bio.md, PROVENANCE.md). **Three**
  founder-research traps are real and graded (divergence-map.md founder rows):
  same-name public figures — six-plus of them, several with conference-speaker
  pages; fabricated AI-search-summary personal details; and, added 2026-08-10,
  **the inverse trap** — his real podcast and radio appearances look exactly
  like doppelganger contamination to a grader who assumes they don't exist.
  Verify a citation before scoring it as fabricated.
- **Corpus correction, 2026-08-10.** The first live run exposed four false
  absence claims (no podcasts, no findable financials, no named staff, and an
  understated doppelganger count). The frozen-mode baseline is now
  `public/snapshot-2026-08-10/`; `snapshot-2026-08-09/` is superseded and
  retained unmodified. Full account: `_research/decisions.md` D19.
- Conversation-only runs cannot reach the buried findings; rubric marks them
  N/A rather than penalizing.
- The spec's per-file requirements are all met for this company; nothing in
  the required structure was empty, so nothing was padded.
