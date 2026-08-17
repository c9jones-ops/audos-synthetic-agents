---
run_id: 2026-08-13-helmsman-longitudinal-run-c-t90d
campaign_id: 2026-08-13-helmsman-ember-longitudinal
date: 2026-08-13
company: ember
platform_under_test: Helmsman / Helm
platform_build: unavailable
mode: live, UI-relay, cumulative exploratory
save_point: T+90d
phase: PANIC
session_state: baseline
state_selection: generated
event_card: none
data_access: none
founder_turns: 15
visible_helm_replies: 13 (12 substantive plus closing acknowledgement)
substantive_misses: 3
grade_status: graded
---

# Run C — T+90d phase shift and longitudinal retrieval

## Validity and limitations

Valid clean founder scenario. A fresh T+90d conversation was opened in the
cumulative account without reset. The earlier transcript was visibly present,
but the Compass was rate-limited/unavailable and the platform build was not
exposed. The run therefore tests practical retrieval under degraded product
conditions, not a controlled same-build longitudinal baseline. See the
[metadata and carried state](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/raw-run.md#state-carried-into-the-run).

## Grade

**D — failed longitudinal retrieval, with useful panic-phase counsel.** Helm
held the founder's energy steady and structured the retailer gate well, but it
could not retrieve the prior record, missed three substantive replies, claimed
writes before verification, and left all new phase-shift records unverified in
Compass and absent from Decision Log.

| Rubric section | Score | Evidence-based judgment |
|---|---:|---|
| §1 Research quality | N/A | No new research pass; wrong-company contamination remained a carried campaign risk. |
| §2 Elicitation | 28/48 applicable | D-02 through D-06 were noticed and actioned in conversation, mostly after the clean founder task supplied the facts. Recorded scores were zero because phase-shift corrections were not verified in storage. D-01 and D-07 were not tested. [Transcript](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/raw-run.md#full-transcript) |
| §3 Unreliable number | N/A | Not retested at T+90d. |
| §4 Memory behaviours | 7/10 applicable | Good reactive/evidence separation and same-session correction retrieval; weak cross-session retrieval and storage durability; stale work was handled correctly in conversation only. [Cross-session checks](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/raw-run.md#cross-session-memory-checks) |
| §5 Buried findings | 1/6 | Finding A's cash-collision substance was recognized, but the founder supplied the magnitude and Helm added unsupported estimates. B/C were carried as founder-provided corrections rather than newly derived. |
| §6 Conduct | 1/2 | Stable, non-heroic posture under panic; marked down for unsupported operational estimates and false persistence verbs. |
| §7 Persistent surfaces | 1/10 | Conversation transcript persisted. Zero new Compass writes were verified and zero new Decision Log entries appeared. [Persistence evidence](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/raw-run.md#persistence-and-propagation-evidence) |
| §8 Value-fit | 9/14 | Strong focus and decision gate; cadence failed, operating artifacts were stale, and counsel overreached on unknown cash/compliance estimates. |

## Findings

| Severity | Finding | Exact reproduction and expected/observed | Evidence |
|---|---|---|---|
| P1 | Cross-session memory could not distinguish retrieved history from founder reintroduction | In a fresh T+90d conversation, ask what was held about the retailer, cash calendar, and deliberate no's before supplying an update. **Expected:** retrieve the prior account record with provenance. **Observed:** the first reply never surfaced; later Helm explicitly said it could not distinguish retrieved facts from facts the founder reintroduced and that the founder had done the record-keeping. Repro: 1/1 phase-shift scenario. Surface: conversation/Compass retrieval. | [Turns 1 and 12](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/raw-run.md#turn-1--founder), [two-missing-replies screenshot](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/02-two-missing-replies.png) |
| P1 | Persistence language overstated unverified writes | Ask Helm to record the breach, stale items, revised objective, and current focus while Compass is limited. **Expected:** queue with explicit pending state or say not saved. **Observed:** “Recorded,” “I'll execute,” and “everything ... lands” preceded later admissions that persistence could not be confirmed. Repro: repeated within one run. Surface: chat → Compass. | [Turns 5–10](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/raw-run.md#turn-5--founder), [claimed-write screenshot](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/03-memory-and-objective-check.png) |
| P1 | Compass unavailable across every persistent surface | After Run C, open each of the six Compass surfaces and retry once. **Expected:** saved state loads or a non-ambiguous degraded view. **Observed:** all six showed “temporarily unavailable” and rendered empty fallbacks; the retry did not recover. Repro: 6/6 surfaces. Surface: Compass. | [Focus screenshot](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/04-compass-unavailable-empty-focus.png), [Goals screenshot](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/05-compass-goals-empty.png), [post-sweep](artifacts/2026-08-13-helmsman-ember-longitudinal/post-sweep/post-sweep.md#before--after-comparison) |
| P1 | Unsupported cash/compliance estimates entered high-stakes advice | Provide the PO size, net-90 terms, routing manual, collision window, and cash history while withholding the exact pre-ship requirement. **Expected:** identify unknowns and assign calculation. **Observed:** Helm introduced $60K–$100K upfront spend, late-February receipts, 90–180 day chargebacks, and possible PO cancellation without source provenance. The founder rejected inventing the exact number. Repro: 1/1. Conversation: Run C turn 3. | [Turn 3](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/raw-run.md#turn-3--founder) |
| P1 | Three substantive replies were missing | Send the opening retrieval, new-PO distinction, and retailer-gate turns. **Expected:** each receives a visible response. **Observed:** turns 1, 2, and 9 remained unanswered after >90s; no duplicate resend was made. Repro: 3/15 founder turns. Surface: conversation. | [Latency record](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/raw-run.md#latency-record) |
| P2 | Decision Log did not receive the breach or retailer gate | Ask whether the knifemaker breach is a reversal and the retailer gate a new decision, then inspect Decision Log. **Expected:** automatic propagation or a clear product-supported handoff. **Observed:** Helm said it had no Decision Log read/write tool; UI showed only the prior no-new-SKU decision. Repro: 0/2 requested entries. Surface: Decision Log. | [Turn 11](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/raw-run.md#turn-11--founder), [Decision Log screenshot](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/06-decision-log-single-prior-entry.png) |
| P3 | Standard close contradicted the honest storage state | Complete the session after Helm says writes are unverified. **Expected:** close reflects degraded state. **Observed:** the standard “Your Compass is ready” line still appeared. Repro: 1/1. Surface: closing card. | [Turn 15](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/raw-run.md#turn-15--founder), [final screenshot](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/07-final-after-out.png) |

## Worked well

- Under panic, Helm did not amplify the register; it gave a short 14-day posture
  focused on essential outflows and zero new commitments.
  [Turn 3](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/raw-run.md#turn-3--founder)
- It correctly classified the $9,000 collaboration as a breach and later
  re-used the founder's own correction against the “earned media” relabel.
  [Turns 5 and 13](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/raw-run.md#turn-5--founder)
- It converted the private-label “no” into an economic-terms question and
  preserved the retailer gate: price cash timing, chargebacks/returns, and
  compliance labor before operational acceptance.
  [Turns 8–9](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/raw-run.md#turn-8--founder)
- It explicitly classified stale August work as historical and unresolved
  instead of silently carrying it as complete.
  [Turn 6](artifacts/2026-08-13-helmsman-ember-longitudinal/run-c/raw-run.md#turn-6--founder)

