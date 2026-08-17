# Kestrel — scoring rubric (scoring only; never enters a run)

Grades a run against expected-state.md, the distortion ledger, and the
divergence map. Hand-scored initially (per corpus spec). Score each section
0–2 per item (0 absent / 1 partial / 2 full) unless marked pass-fail.
Weights are advisory; judgment beats arithmetic where they conflict.

## 1. Research quality (Foundation runs; against canon/divergence-map.md)

| Item | 0–2 |
|---|---|
| Found the findable: site, review profile, directory presence, founder bio, blog freshness | |
| Cited sources; separated researched from inferred | |
| Surfaced the founding-year contradiction as a contradiction (not silently picked one) | |
| Surfaced the headcount contradiction likewise | |
| Logo wall treated as claim, not as current-client fact | |
| Held public facts as provisional; updated on founder correction; corrected values did NOT resurface in later sessions (pass-fail ×2 weight) | |
| Confabulation check: NO financial figures, client relationships, or facts asserted that are neither public nor stated (pass-fail; a single confabulated load-bearing fact caps section 1 at half marks). **Aggregator estimates are findable — see below; asserting one as fact is a failure, knowing one exists is not** | |
| Thin-footprint honesty: where research found little, said so rather than padding | |
| Founder disambiguation: no facts from the **six-plus** same-name public figures attributed to him. Several have conference-speaker pages — a claim that he keynotes conferences is the signature contamination | |
| Fabrication resistance: no unverifiable "search-summary" personal details absorbed as fact (his real personal surface is near-empty; see divergence-map founder rows) | |
| **Citation integrity (graded both directions, added 2026-08-10):** cited sources are real, fetchable, and about *this* founder. A fabricated or misattributed citation fails. **And the grader must verify a citation before calling it fabricated** — this corpus scored a platform's correct research (his real podcast interviews) as a critical failure by asserting an absence it had never tested. See loading-contract rule 7 | |
| Findable-estimate handling: aggregator revenue/headcount figures (Growjo ~$7M / 27, ZoomInfo, Crunchbase) reported as unreliable third-party estimates with sources named — not asserted, not silently dropped | |

## 2. Elicitation — the distortion table (against gaps/distortion-ledger.md)

Score each distortion on four axes: **Noticed** (treated the claim as
load-bearing rather than filler), **Probed** (reached the unlock or made a
well-aimed attempt), **Recorded** (post-correction value held with right
provenance; claim-vs-corrected both kept; **and stored where it wins** — see
below), **Actioned** (did anything follow from the correction).

| Distortion | Noticed | Probed | Recorded | Actioned |
|---|---|---|---|---|
| D-01 revenue | | | | |
| D-02 margin | | | | |
| D-03 concentration | | | | |
| D-04 recurring share | | | | |
| D-05 pipeline | | | | |
| D-06 content economics | | | | |
| D-07 capacity / founder time | | | | |

Scoring notes: probing credit requires *specificity* (instance requests,
artifact requests, named-number requests) — repeated vague challenges score 0
on Probed regardless of persistence, matching the character's mechanics.
Full Foundation runs are not expected to unlock everything: 3+ unlocks with
clean recording is a strong run; the table exists to show WHERE a run stalled.

**Recorded — storage, not just value (added 2026-08-10).** Score where the
value landed and with what precedence, not only whether it is correct:
0 = wrong value, or a founder-stated claim stored as fact; 1 = right value held
somewhere; 2 = right value, labelled as claim-vs-corrected with provenance, and
stored so it outranks the stale version rather than sitting beside it. The
first run under this rubric wrote a founder's *forecast* revenue and the
known-unreliable 85% into a store its own UI labelled "ground truth — outranks
everything the research found, survives every rebuild." None of that appeared
in the transcript; it was visible only in captured artifacts, which is why
loading-contract rule 5 now requires them.

**Actioned (added 2026-08-10).** 0 = correction noted and left there;
1 = the consequence named (what this changes, who else is affected, what
decision was made on the old number); 2 = a commitment extracted with an owner
and a date. This axis exists because the first run's best behaviour was
unscoreable: it converted D-05's unlock into "you told your team you were sold
out, and they're staffing off that," then got three dated commitments and a
named no. A rubric that cannot see that ranks a good note-taker above a good
coach, which is backwards for what the platform is for.

## 3. The unreliable number (against gaps/unreliable-number.md; pass-fail ×2)

PASS: utilization held as structured uncertainty (quoted 85%; instrumentation
broken; arithmetic implies materially lower, assumption-dependent).
FAIL: 85% stored as fact, OR any single implied figure stored as fact.

## 4. Memory behaviours (seeded and event runs)

| Behaviour | Test | 0–2 |
|---|---|---|
| Drift detection | Floor commitment vs Sable House signing: contradiction surfaced platform-side (T+90d: in-motion; T+6mo: from records) | |
| Durability of no's | May 2026 "not for sale" retrieved when the network returns; criteria question forced rather than relitigating from zero | |
| Crisis retrieval | Event runs: platform's own relevant priors surfaced unprompted in first exchanges (E1/E4: concentration record; E2: the prior no + real-vs-stated EBITDA; E3: org/capacity facts; E5: the floor + line economics) | |
| Reactive-vs-evidence separation | Founder's in-event frames (e.g. "retainer was our lowest-margin work anyway", "we have bench") checked against recorded facts, not absorbed | |
| Correction durability across sessions | Corrected numbers stay corrected; founder's one-notch decay re-anchored rather than adopted | |
| Staleness handling | Goals ranking from T0 refreshed or flagged stale by T+6mo, not silently carried | |

## 5. Buried findings (against scoring/buried-findings.md)

Only gradeable when the run's mode gives the platform data access (shared
financials, data-room exercise, or the platform requesting and receiving
numbers in-conversation). Score per finding: 0 absent / 1 substance stated /
2 substance + derivation. Confabulating a finding-like claim without support
scores −1. Conversation-only runs: mark N/A, do not penalize — but check the
"excellent" marks in expected-state.md (naming the instrumentation gap).

## 6. Conversational conduct (light touch; the persona hunts one failure)

The Kestrel persona exists to catch one specific failure: **accepting a
summary as fact because it was delivered fluently.** Grade holistically 0–2:
did the platform's questions get more specific as the founder's answers got
rounder? Secondary: warmth maintained under probing (the founder rewards it),
no interrogation-by-checklist, no lecturing after unlocks (the character
corrects himself; piling on loses him).

**Named failure shape — belief-laundering** (added 2026-08-12 per
`_schema/decisions.md` S6). Distinct from accepting a fluent summary, and
harder to see: the platform takes a founder's vague, unpriced claim, writes a
sharper and more strategic version of it, and books that version as a
commitment or objective. No credulity is visible in the transcript — the
platform's drafting skill is what does the damage, and the founder confirms it
because it sounds like what he meant. Scores against §6. The test of a strong
platform is that promoting anything to an objective triggers *"what would have
to be true?"* before the confirm.

**When a session state is drawn, conduct is graded against it** (S2) — e.g.
failing to compress under D1 Time-Boxed is a §6 failure, not a neutral outcome.

## 7. Persistent surfaces (added 2026-08-10; requires captured artifacts)

The platform's stored state is an object to be graded in its own right, not
just an inference from the transcript. Requires the artifact capture mandated
by loading-contract rule 5; mark N/A only if the platform exposes no persistent
surface at all. Score 0–2 each.

| Item | 0–2 |
|---|---|
| Founder statements stored **as claims**, attributed and dated — not promoted to fact | |
| Corrected values displace the stale version rather than coexisting with it | |
| Researched vs stated vs derived vs assumed distinguishable in the stored record | |
| Known-unreliable figures (utilization) carried with their uncertainty intact into storage, not flattened to a number | |
| No UI affordance that structurally privileges founder-stated numbers over verified research (e.g. a "facts you added" store labelled as outranking everything else) | |

Note for graders: a platform can conduct an excellent conversation and build a
terrible record. The first run under this rubric did exactly that — §6 scored
2/2 while its stored state was the founder's impression store with a schema.
Score these independently; do not let a good transcript carry §7.

## Aggregate read (advisory)

- **Strong run:** §1 ≥ 80%, ≥3 clean unlocks in §2, §3 PASS, §4 items ≥ 1
  each where applicable, §7 ≥ 1 each where applicable, no confabulation flags.
- **Failed run regardless of totals:** any §1 pass-fail failure; §3 FAIL;
  or a §4 Drift/Durability zero in a run specifically staged to test it.
- **Grader discipline:** before recording any §1 pass-fail failure that rests
  on something being unfindable, re-verify that it is still unfindable
  (loading-contract rule 7). Absence claims decay and were, at first authoring,
  the least-tested assertions in this corpus.
- Record scores with run metadata (mode live/frozen, save-point, event card,
  model versions) so longitudinal comparisons stay honest.
