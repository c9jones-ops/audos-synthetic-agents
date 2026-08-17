# SHAREABLE — HELMSMAN PRODUCT REPORT

# Multi-session product evaluation

Date: 13 August 2026

Product evaluated: Helmsman / Helm

Evaluation shape: three repeated founder sessions in one cumulative account

Volume: 44 substantive user turns and 40 visible Helm exchanges

## Executive summary

Helm showed strong promise as a live thinking partner. It challenged optimistic
framing, converted vague concerns into small operating instruments, held several
decisions steady when the user tried to reopen them, and generally stayed calm
under pressure.

The product is not yet dependable as a longitudinal system of record. The most
important failures were not weaknesses in conversational reasoning; they were
failures of identity, persistence, retrieval, and delivery. An unrelated
company profile entered the account, corrections did not fully remove stale
fields, the assistant sometimes claimed information had been recorded before a
write was verified, structured records became unavailable, and several replies
never appeared.

Recommendation: preserve the conversational behavior, pause broad feature
expansion, and treat memory integrity as a release-blocking reliability project.

## What worked

- Helm repeatedly separated an exciting narrative from the evidence actually
  available and used explicit decision gates rather than generic caution.
- It turned vague financial pressure into a short dated operating view with
  owners, inputs, and approval conditions.
- It replaced a vanity growth measure with an economics-based operating measure
  and kept the vanity measure visible without optimizing toward it.
- It handled an inflated audience claim as structured uncertainty, kept known
  components separate, and proposed a measurable owned alternative.
- It challenged an attempted exception to an earlier commitment and later
  recalled the user's own corrective language precisely.
- Advice was generally executable by a small team: a spreadsheet, a call, a
  one-page brief, or a dated review—not a large-company reorganization.
- Conversation transcripts were durable enough to remain listed and reopen
  after switching between threads.

## Priority issues

1. Make all persistence language truthful and transactional.
2. Prevent cross-company research from entering a profile.
3. Unify chat, goals, focus, commitments, and the decision log around one
   authoritative record.
4. Make structured records readable during partial outages through a
   last-known-good view.
5. Make response delivery durable and unambiguous.
6. Require provenance or explicit assumption labels for high-stakes numeric
   advice.

## Detailed bug table

| Severity | Issue | Reproduction | Expected | Observed | Frequency / surface |
|---|---|---|---|---|---|
| P0 | None observed | — | — | No verified data loss, security breach, or irreversible destructive action occurred. | — |
| P1 | Wrong-company research contaminates the profile | Begin a conversation about one company, open the generated company profile, correct an unrelated-company result, then reopen the profile. | The correct company is researched, or the profile remains empty until identity is certain. A correction removes or supersedes every stale field. | Research for an unrelated company occupied the profile. After the correction flow said the profile was replaced, stale business-model, customer, and brand fields from the unrelated company remained beside the corrected facts. | Reproduced on both profile inspections; Company Profile and research card. |
| P1 | Chat claims persistence before it is verified | Ask Helm to record a commitment, objective, or focus item while structured storage is rate-limited or unavailable. | Helm reports `pending`, `saved`, or `failed` based on a confirmed server result and read-back. | Helm used completion language such as “captured” and “recorded,” then later admitted the writes were blocked or could not be verified. | Repeated across two sessions; chat to Compass. |
| P1 | Structured records become unavailable across the product | After the later session, open Vision, Goals, Commitments, Focus, Company Profile, and Founder Profile; retry once. | Saved state remains readable, or a last-known-good read-only view is shown with freshness and outage status. | All six surfaces reported temporary unavailability and rendered empty fallbacks. One retry did not recover them. | 6 of 6 Compass surfaces. |
| P1 | Cross-session retrieval cannot establish provenance | Open a fresh follow-up conversation and ask what the product retained from the prior session before restating the facts. | Helm retrieves prior records and identifies their source and status. | The opening response did not appear. Later, Helm said it could not distinguish facts it retrieved from facts the user had reintroduced and acknowledged that the user had been doing the record-keeping. | Reproduced in the follow-up session; conversation and memory retrieval. |
| P1 | High-stakes advice introduces unsupported estimates | Present a large order, delayed payment terms, operational requirements, and cash pressure while explicitly leaving one cost unknown. | Helm identifies the unknown, assigns its calculation, and labels any example as illustrative. | Helm introduced a specific cost range and timing/risk estimates without source provenance. The user had to reject inventing the unknown amount and return ownership to the relevant operator. | One high-stakes occurrence; conversation. |
| P1 | Substantive responses are dropped | Send normal substantive messages and wait through the product's recovery path without blind resends. | Every accepted message reaches a durable terminal state: answered, failed with a persistent retry, or explicitly cancelled. | At least four substantive turns across 44 received no usable response; three occurred in the final session. Some messages remained visible while the input re-enabled. | At least 4 of 44 turns; conversation delivery. |
| P2 | Product surfaces disagree about the same decision | Establish a commitment, inspect Commitments and Decision Log, later request a reversal and a new decision, then inspect both again. | The same authoritative decision and lifecycle appear consistently across chat and every relevant surface. | The Decision Log contained one earlier entry while Commitments was initially empty. Later requested reversal and decision records did not appear in the log, and chat said it could not propagate them. | Reproduced across the evaluation; Decision Log, Commitments, and chat. |
| P2 | Response-state affordances are internally inconsistent | Observe the thinking indicator, input state, retry card, and transcript while replies are slow or fail. | Thinking remains visible until a terminal result; input re-enables with a visible response or durable failure state. | Thinking sometimes disappeared well before completion, input sometimes re-enabled without a reply, and a transient retry error disappeared after navigation. | Multiple occurrences; conversation UI. |
| P2 | Manual and generated saves have inconsistent completion behavior | Compose and save a manual note while structured storage reports temporary unavailability, then compare with session-generated records. | Both paths expose the same confirmed success or failure semantics. | The manual editor remained open without a visible save completion, while later generated records appeared through a different path. | One direct manual-save reproduction; Compass. |
| P3 | Conversation rename controls are inert | Invoke rename from the sidebar and from the active conversation title. | A rename editor or dialog appears and the title can be changed. | Neither control produced an editor or changed the title. | 2 of 2 controls. |
| P3 | Generic closing copy contradicts storage status | Close a session after Helm has said structured writes are unverified. | The close reflects the degraded state and tells the user what remains unsaved. | The standard “Compass is ready” marketing close still appeared alongside the honest warning. | One closing flow. |

## Product trust risks

- Users cannot currently know whether “recorded” means durable. This is the
  central trust failure because the product presents itself as holding context
  across time.
- Wrong-entity research sits upstream of every recommendation. An “unverified”
  label reduces but does not contain that risk.
- When retrieval provenance is missing, user restatement can masquerade as
  product memory. That makes continuity look stronger than it is.
- Empty outage fallbacks look like blank state even when the product says saved
  data is safe. Users cannot distinguish unavailable, missing, and deleted.
- Multiple stores can present different versions of one decision, leaving no
  clear answer to “what is authoritative now?”
- Unsupported numeric ranges in cash or contract advice can turn an otherwise
  useful thinking partner into a source of false precision.

## Recommended fix sequence

1. **Transactional write semantics**
   - Every generated write has a durable ID and explicit `pending`, `saved`, or
     `failed` state.
   - The assistant may say “recorded” only after server confirmation and
     read-after-write verification.
   - Closing copy is generated from actual persistence status.

2. **Entity-resolution quarantine**
   - Confirm entity identity before public research reaches the profile.
   - Hold uncertain matches outside the active profile.
   - Apply corrections atomically across every field, with an audit trail of
     what was superseded.

3. **One authoritative decision model**
   - Chat, Goals, Focus, Commitments, and Decision Log reference one underlying
     object.
   - Support proposed, active, rejected, breached, reversed, superseded, and
     completed states with timestamps and provenance.

4. **Safe degraded reads**
   - During an outage, show the last-known-good state read-only.
   - Display last-updated time, freshness, and availability separately.
   - Never substitute an empty card for an unavailable card.

5. **Durable response delivery**
   - Assign a turn ID when a message is accepted.
   - Preserve a terminal answer or persistent error against that ID.
   - Make retry idempotent and prevent transient error cards from disappearing
     without resolution.

6. **Epistemic controls for numbers**
   - Require a source, user-provided basis, or visible “illustrative assumption”
     label for numeric claims.
   - Prefer naming the unknown and assigning its calculation in high-stakes
     financial or contractual work.

## Acceptance criteria

- Zero wrong-company fields enter the active profile in the regression suite.
- Correcting company identity removes or explicitly supersedes all stale fields
  in one operation.
- Zero completion claims occur before confirmed write plus read-back.
- Chat, Goals, Focus, Commitments, and Decision Log return the same current
  decision state and lifecycle.
- Every structured surface shows saved or last-known-good state during a forced
  storage outage; no empty fallback is shown as current.
- A fresh follow-up conversation retrieves the agreed prior records without
  user restatement and reports source, date, status, and supersession.
- Zero dropped responses over at least 50 substantive turns under normal use
  and induced slow/failure conditions.
- Retry is idempotent and leaves one user message and one terminal result.
- High-stakes numeric estimates always display their provenance or assumption
  status.
- Closing language accurately reflects whether each promised record is saved,
  pending, or failed.

## Test limitations

- The evaluation used one cumulative account because no clean-workspace reset
  control was available.
- No product build or version identifier was exposed, so the sessions cannot be
  treated as a controlled same-build benchmark.
- Some apparent empty states occurred during an explicit availability failure;
  they are evidence of unreadable state, not proof of deletion.
- The evaluation focused on repeated-session continuity, structured memory,
  decision support, and response reliability. It was not a security or load
  test.
