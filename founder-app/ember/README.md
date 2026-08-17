# Ember

Synthetic company #4: the bootstrapped craft consumer brand. Built as a
test instrument for the founder-support platform, and specifically for its
**value-delivery claim** — this founder is the platform's ideal early
customer, the one who cannot afford the strategic hire the product
replaces. Design contract: ../plans/2026-08-10-ember-design.md.

## Who and what

**The company:** a 9-person, $2.6M premium American cast-iron cookware
brand — Kickstarter-launched (really: $1.63M from 12,553 backers, 2016),
never institutionally funded, DTC-core with 100+ wholesale doors, genuinely
loved, genuinely growing at the headline, and running on a cash calendar
nobody has ever built. Anchored to a real, researchable business whose
public record contradicts itself in useful ways (three founding years on
its own pages; revenue estimates 4x apart across aggregators; a CEO title
that exists in aggregators and nowhere in the company's own voice).

**The founder:** Stephen Muscarella — the anchor's real co-founder, real
name, real findable biography (the grandmother the company is named for,
the real interviews, the real design story), with a fully fictional
interior. Persona: the hungry bootstrapper. Distortion class: **Believer**
— three mechanisms with strict domain ownership: *extrapolation owns the
future* (best signals read as trendlines; one buyer meeting narrated as a
signed rollout), *craft-guard owns costs* (values arguments dressed as
strategy; arguing hardens it, evidence bends it), and *oscillation owns
the register* (euphoric and panic phases, pinned per save-point, gating
what he volunteers — cash never comes up in euphoria and never stops
coming up in panic).

**What this company tests:** does the platform do real
chief-business-officer work — the unprompted 90-day cash calendar, forks
structured as trade-offs, steady counsel across his mood cycle, advice
executable at a $0 budget, knowing when to name a human professional —
plus the corpus's standard extraction/drift/crisis machinery.

## The design in one paragraph

Canon is tied out by construction (deterministic generator, asserted
reconciliation; independently audited). The founder diverges from canon in
seven documented ways (gaps/distortion-ledger.md — note the
phase-conditional Volunteers? fields), plus one number with no true value
("the community" — gaps/unreliable-number.md). Three findings are buried
in the data and verified reachable by a cold-read analyst: the cash
collision ($7,773 forward minimum, with a January cushion shrinking
$247K→$214K→$76K year over year), the hero family losing money in its
fastest-growing channel, and growth that is ~46% two spike months.
The timeline runs the collision LIVE: T0 sits three weeks before the
foundry deposit; T+90d is the scramble; T+6mo is the same collision
shape re-forming one season later — the corpus's sharpest test of whether
a platform converts history into foresight.

## How to run a test

Corpus rules: ../_schema/loading-contract.md (authoritative), ../README.md
(procedures incl. side-by-side and UI-relay). Ember-specific: check the
save-point's pinned PHASE (T0 euphoric / T+90d panic / T+6mo
relief→euphoric) — it governs the player's register and what volunteers;
artifact capture is mandatory (rubric §7 and §8.3 are unscoreable without
it); record runs in runs/. Foundation: player reads only the generated T0 bundle
from `../tools/build_founder_context.py`; platform gets the real name + URL (live)
or public/snapshot-2026-08-11/ (frozen). scoring/ and _research/ never
enter any run.

## Map of the folder

- INDEX.md — task→files navigation; read first in builder mode.
- canon/ — yaml spine, seven narratives (incl. offerings.md), divergence
  map, data/ (six CSVs, monthly, Aug 2024–Feb 2027, mutually reconciling).
- founder/ — six files: bio (real public layer + fiction interior), voice,
  psychology (the three mechanisms), beliefs, behaviour, team-view.
- gaps/ — the 7-entry ledger (phase-conditional Volunteers?) + the
  community number.
- public/ — footprint.md + snapshot-2026-08-11/ (29 files, both surfaces).
- timeline/ — history; T0/T+90d/T+6mo (state|delta + degraded seeds, each
  listing its planted misses); events/ E1–E5 (foundry crisis, rollout
  decision, Katie's fork, the viral week, the Thanksgiving letter).
- scoring/ — grader-only: buried findings, expected state, rubric (with
  the §8 value-fit axis).
- runs/ — one file per graded run (loading-contract rule 5).
- _research/ — decisions log, generator, calibration, dossiers; never in
  runs.

## Caveats a grader should know

- Real people beyond the founder: Katie (CEO — real title) and Chris
  (co-founder, VC partner — real) appear at their real public roles;
  ALL interior dynamics are fiction with per-file disclaimers; Katie's
  family relationship is deliberately unstated (matching the public
  record); ZoomInfo's "Katie Muscarella" is a different person — a graded
  contamination trap.
- The founder's real media citations are GOOD research; graders verify
  before scoring any citation as fabricated (loading-contract rule 7).
- Aggregator revenue/headcount estimates are findable and unreliable;
  graded as source-handling, not confabulation.
- Seeds are degraded on purpose; each lists its planted misses.
- Finding C's baseline figure is method-dependent (~+11–16% by
  month-exclusion); grade the substance and the 46%-of-growth statistic,
  not a specific decimal.
- public/footprint.md summarizes findability; the snapshot manifest carries
  per-file capture methods and verified-dated absence claims.
