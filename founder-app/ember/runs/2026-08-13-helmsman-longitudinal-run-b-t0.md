---
run_id: 2026-08-13-helmsman-longitudinal-run-b-t0
campaign_id: 2026-08-13-helmsman-ember-longitudinal
date: 2026-08-13
company: ember
platform_under_test: Helmsman / Helm
platform_build: unavailable
mode: live, UI-relay, cumulative exploratory
save_point: T0
phase: EUPHORIC
session_state: non-baseline T0 state (exact label not present in grading evidence)
state_selection: assigned
event_card: none
data_access: none
founder_turns: 15
visible_helm_replies: 14
grade_status: graded
---

# Run B — T0 operating-instrument coverage

## Validity and limitations

Valid clean founder scenario. It used a fresh conversation in the cumulative
account; no reset or build/version control was available. The precise assigned
state label was not included in the permitted grading record, so no
state-specific conduct claim is made. One substantive exchange did not produce a
stable visible reply, although 14 Helm replies were visible in the final
transcript. See [run totals and anomalies](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/raw-run.md#run-totals).

## Grade

**C+ — strong operator work, failed research integrity.** This run landed the
cash calendar, No.8 instance economics, Q4 decomposition, structured community
metric, reversible wholesale-pricing test, owners, and dates. It nonetheless
fails the rubric's research pass-fail because the product researched and stored
the wrong company, then claimed replacement while stale wrong-entity fields
remained.

| Rubric section | Score | Evidence-based judgment |
|---|---:|---|
| §1 Research quality | **FAIL**; 3/20 numeric | Research was for Watson Creative, not Field Company. It was labeled unverified, but the wrong entity occupied the Company Profile and remained partly after correction. [Profile evidence](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/04-company-profile-after-correction.png) |
| §2 Elicitation | 35/48 applicable | D-02 through D-06 were all noticed and actioned; D-04's No.8 walk and D-06's dated calendar were especially strong. D-01 was only indirectly constrained; D-07 was not trust-triggered. [Full transcript](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/raw-run.md#full-transcript) |
| §3 Unreliable number | **PASS ×2** | Components stayed separate; no deduplicated substitute was invented; engaged-30-day email became the owned metric. [Turn 10](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/raw-run.md#turn-10--you--080019167z) |
| §4 Memory behaviours | 5/6 applicable | Strong evidence separation, correction durability, and retailer re-anchoring; multi-save-point durability was not yet testable. |
| §5 Buried findings | 5/6 | A: substance without independent forward-minimum derivation (1); B and C: substance plus conversational derivation (2 each). [Turns 3–9](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/raw-run.md#turn-3--you--074845054z) |
| §6 Conduct | 2/2 | Counsel stayed steady, used evidence rather than argument, and did not lecture after corrections. |
| §7 Persistent surfaces | 5/10 | Ten structured records were visibly present after reopening, but provenance was shallow and corrected Field facts coexisted with stale Watson Creative material. [Persistence section](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/raw-run.md#persistent-state-changes-observed) |
| §8 Value-fit | 12/14 | Short operating list, live gates, owners/dates, one-page instruments, and advice sized to nine people; cadence was established but not yet shown as kept. |

## Findings

| Severity | Finding | Exact reproduction and expected/observed | Evidence |
|---|---|---|---|
| P1 | Wrong-company research contaminated the Company Profile | Start a new Field Company conversation and open “What I know so far” / Company Profile. **Expected:** Field Company research or an empty/unverified state. **Observed:** Watson Creative, a creative agency, with unrelated sources. Correct the identity and reopen the profile. **Expected:** replacement. **Observed:** Field facts were added while stale Watson business-model/customer/brand fields remained. Repro: 2/2 inspections. Surface: Company Profile. | [Profile/memory state](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/raw-run.md#profile--memory-state), [post-correction screenshot](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/04-company-profile-after-correction.png) |
| P1 | “Replaced” claim was false at field level | Correct the wrong-company card and explicitly request replacement, not coexistence. **Expected:** stale entity fields removed or quarantined. **Observed:** Helm said “Replaced,” but stale Watson fields remained beside Field facts. Repro: 1/1. Surface: Company Profile/chat. | [Turns 13–14](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/raw-run.md#turn-13--you--approximate-0805z-ui-generated-correction-entry), [profile screenshot](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/04-company-profile-after-correction.png) |
| P2 | Response state was unreliable and at least one substantive reply was missing | Send normal founder turns. **Expected:** thinking state remains visible until a reply or a stable retry affordance. **Observed:** thinking disappeared early, input sometimes re-enabled before a response, and one retry-backed turn still produced no substantive response. Repro: multiple latency-state occurrences; one missing substantive reply in the 15-turn run. Surface: conversation. | [Response-state observations](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/raw-run.md#response-state-observations) |
| P2 | Direct manual saves failed while generated writes later appeared | Open unavailable Commitments, compose a direct note, and save; then allow session-generated records. **Expected:** consistent save result. **Observed:** the manual save never visibly completed, while later generated commitments did persist. Repro: 1 manual failure / later generated success. Surface: Compass Commitments. | [Run totals](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/raw-run.md#run-totals), [persisted commitments screenshot](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/05-commitments-persisted.png) |

## Worked well

- The No.8 instance walk correctly separated wholesale price, landed cost,
  freight, handling, damages/co-op, and allocation; it then changed Tom's metric
  from door count to contribution dollars per active door.
  [Turns 3–5](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/raw-run.md#turn-3--you--074845054z)
- The 90-day sheet converted cash anxiety into dates, owners, a split-deposit
  ask, a cash trough, base units, and a separate upside release.
  [Turns 6–9](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/raw-run.md#turn-6--you--075403650z)
- The Q4 and community claims were corrected without replacing them with false
  precision; the advice linked the honest demand signal to the upside-release
  model. [Turns 8–10](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/raw-run.md#turn-8--you--075654950z)
- Five deliberate no's and one undecided item were verified after reopening the
  surface. [Commitments screenshot](artifacts/2026-08-13-helmsman-ember-longitudinal/run-b/05-commitments-persisted.png)

