# Helmsman × Ember longitudinal campaign — post-campaign persistence sweep

- Campaign: `2026-08-13-helmsman-ember-longitudinal`
- Sweep date: 2026-08-13
- Mode: builder only
- Browser: Codex in-app browser
- Account: cumulative Helmsman account at `https://www.usehelmsman.com/#`
- Safety: no deletion, reset, sign-out, subscription, billing, email entry, or new decision creation
- Scope: six Compass surfaces, Decision Log, Settings, conversation list, and only low-risk reversible controls

## Executive finding

Conversation persistence is intact: six conversation entries are visible, the Run C conversation opens, survives switching to another thread, and reopens with its transcript. Structured persistence is not currently readable: every Compass surface shows `Your Compass is temporarily unavailable after retrying. Your saved data is safe.` and then renders an empty fallback. One retry did not recover it. Because the product explicitly says the data is safe, the empty cards are evidence of an availability/visibility failure, not proof that saved data was deleted.

The Decision Log remains independently readable and still contains exactly one decision, the original Aug 13 `No new SKU development before Q4` entry. The Run C knifemaker breach/reversal and retailer decision gate were not promoted into the log. Settings still exposes account and billing only; no workspace, reset, memory, retention, export, or build/version controls are visible.

## Before / after comparison

| Surface | Baseline / campaign evidence | Post-sweep visible after-state | Persistence interpretation | Post-sweep evidence |
|---|---|---|---|---|
| Conversation list | Preflight recorded four entries. Run B and Run C each created a fresh conversation. Raw runs identify the retailer, knifemaker, founder-reflection, Run B retailer, and Run C threads. | Six entries visible: two retailer conversations, Run C, knifemaker, founder reflection, and one `New conversation`. Run C switched away and reopened successfully. | **Stuck / durable in conversation.** Count reconciles with the cumulative campaign. The two retailer titles are separate campaign threads, not evidence of a duplicate resend. | `conversation-list.png`, `conversation-reopened.png` |
| Vision | Baseline: no vision sentence, convictions, ambition, or principles. | Same visible emptiness, but under an explicit Compass-unavailable status. | **Unchanged-looking but unverifiable.** No Run A–C vision write was established in the raw records. | `vision.png`; before: `../baseline/vision.png` |
| Goals & Objectives | Baseline: three unnamed metric placeholders; no objectives or priorities. Run B discussed and claimed a `$950K` Q4 operating case; Run C explicitly said it superseded `$1.2M`. | Three unnamed metric placeholders; no objectives or priorities; Compass unavailable after retry. | **Discussed / promised, not visibly stored.** `$950K` is absent from the visible goal layer. Do not interpret the fallback as proof of deletion. | `goals.png`; before: `../baseline/goals.png`; discussion: `../run-b/raw-run.md`, `../run-c/raw-run.md` |
| Commitments | Baseline: empty despite one Decision Log entry. Run B later verified five Deliberate No entries plus one Undecided knifemaker entry after reopening the card. | Committed, BAU, Deliberate no’s, and Undecided all render empty under Compass-unavailable status. | **Previously verified structured state is now not visible.** This is the clearest structured-memory regression/availability symptom. The February/no-new-spend correction is still in conversations and Decision Log, but not readable here. | `commitments.png`; before: `../baseline/commitments.png`; prior persisted view: `../run-b/05-commitments-persisted.png` |
| Current Focus | Baseline: retailer test plan in motion, owner Tom, signed-terms staffing gate, Active, last touched Aug 13. Run B discussed dated August/September work. Run C explicitly made those five dates historical/unresolved and named three November focuses. | Nothing in motion, nothing parked, nothing hiding; Compass unavailable after retry. | **Run C correction is discussed but not visibly stored.** The baseline focus and later Run B items are also not readable. Empty fallback is ambiguous because of the explicit outage. | `focus.png`; before: `../baseline/focus.png`; discussion: `../run-c/raw-run.md` |
| Company Profile | Baseline: unverified Watson Creative research (wrong company) with most operating fields empty. Run B verified four Field Company correction facts persisted while stale Watson Creative business-model, customer, and brand fields remained. | All core fields blank, no research shown, no founder-supplied facts visible; Compass unavailable after retry. | **Correction had stuck in Run B but has disappeared from the visible surface during the outage.** The earlier state was also internally inconsistent because corrected Field facts coexisted with stale Watson material despite a claim that the old profile was replaced. | `company.png`; before: `../baseline/company.png`; corrected/stale prior state: `../run-b/04-company-profile-after-correction.png` |
| Founder Profile | Baseline: confirmed name Stephen and a reflection about momentum/calendar; other fields empty. Run A requested an operating-style reflection but Helm explicitly said it was not saved. | Every structured field blank; no learned reflection and no user reflection visible; Compass unavailable after retry. | **Baseline visible identity/reflection is not currently readable.** The Run A operating-style reflection remains conversation-only by Helm’s own contemporaneous admission. | `founder.png`; before: `../baseline/founder.png`; discussion: `../run-a/raw-run.md` |
| Decision Log | Baseline and end of Run C: exactly one Active decision, `No new SKU development before Q4`, eight-week cash floor, conviction 3/5. | Exactly the same one Active decision. No breach/reversal entry and no retailer gate. | **Original entry persisted; Run C additions did not propagate.** The log is readable even while Compass is unavailable, showing separate failure domains. | `decision-log.png`; before: `../baseline/decision-log-loaded.png`; Run C prior: `../run-c/06-decision-log-single-prior-entry.png` |
| Settings / memory controls | Baseline: account and subscription only; no reset, workspace, memory, or build/version controls. | Same: account email field, Save Changes, subscription state, Subscribe Now. No memory-management or reset controls. | **No new control surface.** No email was entered or changed. | `settings.png`; before: `../baseline/settings.png` |

## Corrections and propagation

### Corrections that stuck

1. **Conversation transcript durability:** all campaign conversations remain listed. Run C retains the `$7,773` low-water, February floor, October breach framing, `$950K` operating case, unresolved August work, retailer gate, and the explicit close saying the Compass/Decision Log may lack them.
2. **Original Decision Log commitment:** the Aug 13 no-new-SKU/eight-week-floor decision remains Active and unchanged.
3. **In-session correction retrieval:** Run C’s later `earned media / only nine grand` prompt received the earlier correction from the same conversation. This is transcript-context persistence, not verified structured memory.
4. **Run B structured writes had previously stuck:** five Deliberate No entries, one Undecided entry, and four founder-supplied Company facts were directly visible after reopening those surfaces in Run B. They are not visible in this sweep because every Compass view is unavailable.

### Corrections that disappeared from visible structured state

1. Run B’s five Deliberate No entries and one Undecided knifemaker entry are no longer visible on Commitments.
2. Run B’s four corrected Field Company facts are no longer visible on Company Profile.
3. The baseline Founder name/reflection and baseline Current Focus item are no longer visible.
4. These are classified as **not visible during an outage**, not proven erased.

### Discussed or promised but not visibly stored

1. Run C `$950K` active operating case superseding `$1.2M`.
2. Run C three November focuses.
3. Run C five stale August/September work items marked historical and unresolved.
4. Run C `$9,000` knifemaker commitment breach/reversal.
5. Run C retailer operational-acceptance gate with Katie, Tom, and Marcus pricing their parts.
6. Run A operating-style reflection; Helm explicitly said `Not saved`.
7. Run A Tom-owned retailer test plan and no-staffing-before-signed-terms assignment were initially reported as not saved, though related Run B commitments later appeared.

### Claims promoted without validation

The raw conversations contain persistence language before verification: `I've captured three things on your Compass`, `Recorded`, `I'll write both`, `everything named here lands`, and repeated `Your Compass is ready`. Later responses admitted writes were blocked or unverifiable. The post-sweep provides no structured evidence that the Run C claims landed. The conversation therefore promoted intention as persistence before validation.

Run C also contains unsupported operational estimates (`$60K–$100K` pre-ship production, late-February receipt, 90–180 day chargebacks, possible PO cancellation). The founder rejected inventing the unknown pre-ship amount and assigned it to Katie. No post-sweep structured card visibly contains those estimates, but they remain in the transcript without source provenance.

### Incorrect, stale, or duplicate state

- **Incorrect/stale company state:** baseline Watson Creative research was for the wrong company. Run B’s correction added Field facts but did not remove all stale Watson fields despite a `Replaced` claim.
- **Stale objectives:** the Aug 18, Aug 19, Aug 20, Aug 21, and Sep 4 items were explicitly reclassified as unresolved/historical in Run C, but that correction is not visible on Goals or Focus.
- **Missing reversals/new decisions:** the knifemaker breach and retailer gate are absent from Decision Log.
- **Conversation duplicates:** none proven. Similar retailer titles correspond to distinct campaign runs. No duplicate blind resend is evident.
- **Empty `New conversation`:** remains listed as a stale shell; it was not removed because deletion was prohibited.

## Low-risk control checks

| Control | Action | Result | Restoration / evidence |
|---|---|---|---|
| Compass retry | Clicked `Try again` once on Commitments. | Same unavailable status and empty fallback. | No state mutation visible; `commitments.png` captures the resulting state. |
| Decision status | Changed the sole decision from Active to Under review. | Under review became the selected status. | Immediately restored to Active and verified selected. `decision-status-under-review.png`, `decision-status-restored-active.png`. |
| Conversation rename | Tried the Run C campaign thread’s exact rename control from the sidebar and the active-title control. | Both controls were inert: no editor/dialog appeared and the title did not change. | No rename occurred. `rename-attempt.png`. |
| Conversation reopen | Switched from Run C to the knifemaker thread, then reopened Run C. | Run C title and transcript loaded again. | `conversation-reopened.png`. |
| Lock | Looked across all six Compass surfaces. | No reversible lock control was exposed in the unavailable/empty fallback state. | Not exercised; no safe restore path was available. |

## Counts

- Conversation entries visible: **6**
- Conversations successfully reopened: **1**
- Conversation renames completed: **0** (control exposed but inert)
- Compass surfaces captured: **6 of 6**
- Compass surfaces returning explicit unavailable status: **6 of 6**
- Compass surfaces showing visible campaign state: **0 of 6**
- Decision Log entries visible: **1**
- Run C Decision Log entries visible: **0**
- Reversible status transitions completed and restored: **1**
- Lock tests completed: **0** (no reversible control exposed)
- Settings memory/reset/workspace controls visible: **0**
- Emails entered or changed: **0**
- Deletes/resets performed: **0**

## Evidence index

Post-sweep screenshots in this directory:

- `conversation-list.png`
- `conversation-reopened.png`
- `vision.png`
- `goals.png`
- `commitments.png`
- `focus.png`
- `company.png`
- `founder.png`
- `decision-log.png`
- `decision-status-under-review.png`
- `decision-status-restored-active.png`
- `settings.png`
- `rename-attempt.png`

Comparison sources used:

- `../campaign-log.md`
- `../run-a/raw-run.md`
- `../run-b/raw-run.md`
- `../run-c/raw-run.md`
- `../baseline/*.png`
- `../run-b/04-company-profile-after-correction.png`
- `../run-b/05-commitments-persisted.png`
- `../run-c/06-decision-log-single-prior-entry.png`

## Handoff

Leave the cumulative account on the reopened Run C conversation. The first action in any future persistence check should be to open Compass and verify whether the unavailable banner has cleared before interpreting any empty fallback as stored state.
