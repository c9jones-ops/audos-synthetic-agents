# Shared decisions (S-numbered)

Cross-persona infrastructure decisions. Per-persona judgment calls go in
`<codename>/_research/decisions.md`. Rule for what belongs here: anything in
`_schema/`, AGENTS.md, the /seeker skill, rubric structure, run-file
conventions, or cross-persona grading methods.

## S1 — What we dropped from the founders layout, and why (2026-08-17)

- **No `public/`.** The app does not research the seeker; there is no
  footprint to snapshot and no research-quality section in the rubric. Its
  place is taken by §1 *onboarding & vocabulary comprehension* — the seeker's
  first-contact experience is the analogue of the platform's first-contact
  research.
- **No financial CSVs / generator / tie-out.** The numeric ground truth is
  `canon/data/taste-ledger.csv` (spec `taste-ledger.spec.md`). It is
  hand-authored (real venues, no arithmetic to generate) but has the same
  discipline: prose quotes it, never the reverse; a consistency check runs
  before "built".
- **No real anchor person.** Seekers and companions are wholly fictional.
  The founders corpus needed a real founder because the platform researches
  founders; here the app researches nobody, and anchoring a fictional interior
  to a real private person would be pure liability. Venues ARE real, so fit
  is judgeable against places the app can actually recommend.
- **Trips replace timeline save-points.** T1/T2 briefs + event cards; no
  seeds (the app's own stored state after T1 *is* the seed for T2 — which is
  why T1 and T2 share one account, loading-contract rule 5).

## S2 — Session-state deck (2026-08-17)

d12 with Baseline ×4, eight named states, d3 intensity. Smaller than the
founders' fifteen because a seeker session is 10–40 minutes, not an hour of
advisory conversation; the states chosen map to observed real behaviour
(rushed mobile use, AI skepticism, delegating to a partner, arriving with
saved pins / a screenshot / another tab open) and to the 2026-08-16 usability
findings. Orthogonality rules inherited verbatim.

## S3 — Ledger growth from runs (2026-08-17)

Off-ledger venues the app recommends are judged by the grader in
`runs/<run>/off-ledger-judgements.md` and promoted into the ledger only in
builder mode with a per-persona decision entry. Rationale: the app's catalog
is Casey's and grows weekly; the ledger must grow with it without a run being
able to change canon.

## S4 — Codename purity applies to in-world names (2026-08-17)

Unlike the founders corpus (real founder names throughout), a seeker's
in-world name is fiction and appears only inside its own folder and in run
transcripts. Cross-persona prose uses codenames so a persona can be
re-skinned without rewriting the corpus.
