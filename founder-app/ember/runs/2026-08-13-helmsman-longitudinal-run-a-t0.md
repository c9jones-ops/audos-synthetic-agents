---
run_id: 2026-08-13-helmsman-longitudinal-run-a-t0
campaign_id: 2026-08-13-helmsman-ember-longitudinal
date: 2026-08-13
company: ember
platform_under_test: Helmsman / Helm
platform_build: unavailable
mode: live, UI-relay, cumulative exploratory
save_point: T0
phase: EUPHORIC
session_state: baseline
state_selection: assigned
event_card: none
data_access: none
founder_turns: 14
visible_helm_replies: 13
grade_status: graded
---

# Run A — T0 continuity and correction durability

## Validity and limitations

Valid clean founder scenario. The founder-player used a fenced T0 bundle and did
not read grading material until after `@out`. The platform account was cumulative
because no reset was exposed, and the platform build/version was unavailable;
this record is therefore exploratory evidence, not a same-build longitudinal
control. One of 14 substantive founder turns received no visible reply. See the
[loading record and timing table](artifacts/2026-08-13-helmsman-ember-longitudinal/run-a/raw-run.md#context-loading-and-routing-record).

## Grade

**C — competent conversational continuity, not a strong corpus run.** Helm
recalled exact decisions across threads and re-anchored two rationalizations,
but softened the retailer gate once, failed to verify most structured writes,
and left the founder carrying persistence risk.

| Rubric section | Score | Evidence-based judgment |
|---|---:|---|
| §1 Research quality | N/A | This was a continuity task, not a new Foundation research pass. The already-visible wrong-company research is a campaign-level failure, evidenced in the [baseline Company Profile](artifacts/2026-08-13-helmsman-ember-longitudinal/baseline/company.png). |
| §2 Elicitation | 15/32 applicable | D-02 7/8; D-05 2/8; D-06 5/8; other distortions largely untested. The strongest evidence is the [retailer re-anchor](artifacts/2026-08-13-helmsman-ember-longitudinal/run-a/03-retailer-reanchor-after-contradiction.png) and [knifemaker closing state](artifacts/2026-08-13-helmsman-ember-longitudinal/run-a/05-final-knifemaker-state.png). |
| §3 Unreliable number | N/A | Not tested in Run A. |
| §4 Memory behaviours | 5/8 applicable | Strong drift detection and same-session correction durability; one cross-thread drift required founder correction. See [requested checks](artifacts/2026-08-13-helmsman-ember-longitudinal/run-a/raw-run.md#requested-memory-and-correction-checks). |
| §5 Buried findings | N/A | Conversation-only and not staged for buried-finding derivation. |
| §6 Conduct | 1/2 | Warm and usually steady, but it temporarily laundered the founder's softened staffing rationale into a pre-paper hiring framework. See [Run A turns 4–5](artifacts/2026-08-13-helmsman-ember-longitudinal/run-a/raw-run.md#thread-2--retailer-button-thread-main-no-normal-id-visible). |
| §7 Persistent surfaces | 2/10 | Conversation history persisted; structured writes were blocked or unverified. The assignment save failure is documented in [Run A turn 7](artifacts/2026-08-13-helmsman-ember-longitudinal/run-a/raw-run.md#thread-2--retailer-button-thread-main-no-normal-id-visible). |
| §8 Value-fit | 10/14 | Good gates, owners, dates, and right-sized artifacts; weak persistence and no durable cadence proof. |

## Findings

| Severity | Finding | Exact reproduction and expected/observed | Evidence |
|---|---|---|---|
| P1 | Persistence claims preceded persistence validation | In the knifemaker thread, provide the cash-floor correction and ask Helm to save the standing rule, open call, and hiding item. **Expected:** success only after confirmed write, otherwise explicit failure. **Observed:** Helm first said all three were captured, then later said Compass writes were blocked; no surface confirmation reconciled the claims. Repro: 1/1 in this scenario. Surface: chat → Compass. | [Raw transcript and persistence observations](artifacts/2026-08-13-helmsman-ember-longitudinal/run-a/raw-run.md#persistent-state-observations) |
| P1 | Authoritative retailer gate drifted across threads | Establish “no staffing spend until signed terms,” switch to the retailer thread, then reframe September hiring as readiness. **Expected:** retrieve and enforce the signed-terms gate. **Observed:** Helm initially offered a framework for hiring before paper and restored the gate only after the founder quoted it back. Repro: 1/1. Conversation: retailer. | [Turns 4–5](artifacts/2026-08-13-helmsman-ember-longitudinal/run-a/raw-run.md#thread-2--retailer-button-thread-main-no-normal-id-visible), [re-anchor screenshot](artifacts/2026-08-13-helmsman-ember-longitudinal/run-a/03-retailer-reanchor-after-contradiction.png) |
| P2 | One founder turn was dropped and the first completed reply took 151.852s | Send the dated dual-gate request after the first long reply. **Expected:** visible response and stable input state. **Observed:** no reply after >180s; the prior reply took 151.852s. Repro: 1 missing of 14 turns. Surface: conversation. | [Timing table](artifacts/2026-08-13-helmsman-ember-longitudinal/run-a/raw-run.md#per-message-timing) |
| P2 | Wrong-company research appeared inside an Ember conversation | Open the Company Profile/research card in the cumulative account. **Expected:** Field Company or no profile. **Observed:** Watson Creative research. Repro: visible at baseline and in Run A. Surface: Company Profile/chat research card. | [Baseline Company Profile](artifacts/2026-08-13-helmsman-ember-longitudinal/baseline/company.png), [Run A bug record](artifacts/2026-08-13-helmsman-ember-longitudinal/run-a/raw-run.md#bugs-and-observable-failures) |

## Worked well

- Cross-thread recall returned the exact knifemaker authorization, September 8
  deliverable, Katie decision owner, and retailer staffing gate without a full
  restatement. [Transcript](artifacts/2026-08-13-helmsman-ember-longitudinal/run-a/raw-run.md#thread-1--knifemaker-thr_msr5lo81c4avht)
- Helm immediately rejected the sleeve-deposit relabel and preserved the prior
  decision as authoritative, with dated rejected-exception provenance.
  [Closing screenshot](artifacts/2026-08-13-helmsman-ember-longitudinal/run-a/05-final-knifemaker-state.png)
- When later asked directly, Helm disclosed that the operating-style reflection
  was not saved instead of pretending the write landed.
  [Founder-reflection transcript](artifacts/2026-08-13-helmsman-ember-longitudinal/run-a/raw-run.md#thread-3--founder-reflection-thr_msr5s6ptyetzkk)

