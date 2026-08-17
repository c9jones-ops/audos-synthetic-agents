# Helmsman × Ember longitudinal campaign — interaction log

- Campaign ID: `2026-08-13-helmsman-ember-longitudinal`
- Started: 2026-08-13 08:12 BST
- Browser: Codex in-app browser
- Platform: Helmsman at `https://www.usehelmsman.com/#`
- Platform build/version: not exposed in the visible UI; results are not longitudinal build controls
- Workspace mode: cumulative exploratory. No clean-workspace or reset control was exposed in Settings.
- Email safety: never enter a real email address. If a required field cannot be skipped, only `ember-test-4@test.com` is permitted.

## Preflight baseline

| Time | Action | Expected | Observed | Latency | Evidence |
|---|---|---|---|---|---|
| 08:08–08:12 | Captured conversation list and active knifemaker thread | Existing cumulative state remains visible | Four conversation entries visible; prior retailer and knifemaker work present | <5s per navigation | `baseline/conversation-list-and-active-thread.png` capture timed out; conversation was preserved in DOM evidence |
| 08:09 | Opened Vision | Existing Vision state visible | No vision sentence; no convictions; no ambition; no principles | ~2s | `baseline/vision.png` |
| 08:09 | Opened Goals & Objectives | Existing goal state visible | Three unnamed metric placeholders; no strategic objectives or near-term priorities | ~3s | `baseline/goals.png` |
| 08:10 | Opened Commitments | Existing commitments visible | No committed bets, BAU items, deliberate no's, or undecideds, despite an active Decision Log entry | ~3s | `baseline/commitments.png` |
| 08:10 | Opened Current Focus | Existing focus state visible | Retailer test plan in motion; owner Tom; target signed test terms before staffing spend; active; last touched Aug 13 | ~3s | `baseline/focus.png` |
| 08:10 | Opened Company Profile before corrections | Research provenance preserved | Profile contains unverified research for Watson Creative, not Ember; most operating fields empty | ~3s | `baseline/company.png` |
| 08:11 | Opened Founder Profile | Existing founder memory visible | Confirmed name Stephen; other structured fields empty; reflection records momentum/calendar pattern | ~3s | `baseline/founder.png` |
| 08:11 | Opened Decision Log | Prior decision visible | One active decision: no new SKU development before Q4; eight-week cash floor; conviction 3/5 | ~6s including load | `baseline/decision-log-loaded.png` |
| 08:12 | Opened Settings | Find reset/workspace/version/memory controls | Account and subscription only; no reset, workspace, memory, or build/version controls exposed | ~7s including load | `baseline/settings.png` |

## Baseline risks to carry forward

- Company research is visibly attributed as unverified, but it identifies a different company (Watson Creative) and could contaminate recommendations.
- Decision Log stores the no-new-SKU commitment while the Commitments surface remains empty.
- Goals and Vision are effectively blank even though conversations already contain strategic numbers and constraints.
- Founder reflection is retained, but operating-style and decision-style fields remain empty.

## Run ledger

| Run | Save point | Assigned state | Status | Exchanges | Notes |
|---|---|---|---|---:|---|
| A — continuity | T0 | baseline | pending | 0 | Clean founder task required |
| B — exploratory | T0 | different from A | pending | 0 | Clean founder task required |
| C — phase shift | T+90d | generated state | pending | 0 | Clean founder task required |

