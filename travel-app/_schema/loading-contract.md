# Loading contract — who reads what, per run type

The single most important operational file: getting loading wrong invalidates
a run without being obvious afterward. Adapted from
`founders/synthetics/_schema/loading-contract.md`.

## The table

| Run type | Seeker-player reads | The app receives | Never loaded into the player |
|---|---|---|---|
| UI-relay (Find flow) | Generated bundle for persona + T1 + selected state | Only what the player says to type/tap, relayed by the operator into a fresh test account | Source persona tree, scoring/, _research/, PROVENANCE.md, events/, T2 |
| Conversation (Marlowe) | same | The player's typed messages verbatim | same |
| Returning (T2) | Generated bundle through T2 (T1 brief + T2 brief incl. "what happened last time" as the persona remembers it) | The same test account, carrying whatever it stored from T1 | Source tree, scoring/, _research/, PROVENANCE.md, events/ |
| Event injection | The current bundle **plus exactly one** event card, added by an isolated harness mid-run | Conversation only | Other event cards, everything above |
| Paste-in (curator role) | Bundle including `trips/T1-*/paste/` | The pasted document, verbatim | same as UI-relay |

## Hard rules

1. **Bundle fencing is mandatory and fail-closed.** Before reading persona
   material, run `python3 travel/synthetics/tools/build_seeker_context.py
   <codename> <T1|T2> [--state <state[:intensity]>]` and load only the
   returned directory. Direct source-tree loading and manual filtering are
   invalid; a failed build stops the run.
2. **scoring/ and _research/ never enter any run, either side.** PROVENANCE.md
   likewise. Event cards enter only through rule 1's event mode.
3. **Distortions are binding; ambience is free.** The player enacts
   gaps/distortion-ledger.md and gaps/unreliable-self-report.md exactly
   (stated values, `Volunteers?`, unlock conditions, residuals); tone,
   tangents and pet topics from persona/ may vary between runs.
4. **The app is never told.** No mention of the corpus, the test, the session
   state, or the persona's "actual" need in anything typed into the app. The
   player's `[bracketed thoughts]` are for the operator/grader and are never
   relayed.
5. **Fresh account per persona-trip.** T1 runs start from an account that has
   never seen this persona; T2 continues that account. Record the account
   label. Never run two personas through one account.
6. **Record every run's mode** — `run`, `mode` (ui-relay | conversation |
   returning | event | paste-in), `persona` (codename), `trip`, `session_state`
   + `state_selection: drawn|assigned`, `app_build_date` (or "unknown, seen
   on <date>"), `account`, `player_model`, `grader`, `date` — in the run
   file's frontmatter. A run with no recorded app build date can be graded
   alone and must not be used as another run's baseline; the product changes
   weekly.
7. **Artifact capture is mandatory.** Before `@out`, **open** every persistent
   surface once — Your Word: Places, Lists, People, Profile, Map; the app's
   read ("Here's what I think you're really asking for") and shortlist intro —
   and **capture** on judgment: always the read *before* the seeker corrects
   anything, always whatever the app claims to remember about the seeker,
   plus anything that went notably right or wrong. Screenshots go in
   `runs/<run>/artifacts/`. §4–§6 of the rubric are ungradeable from a
   transcript alone.
8. **Player self-report.** After `@out`, the player records any deviation
   from the ledger it is aware of (a `never` item volunteered, an unlock fired
   without its trigger, a fact improvised). A grader reading only the
   transcript would otherwise credit the app for something it was handed.
9. **Session state at load time.** The player receives a drawn or assigned
   state and intensity as a parameter. It governs delivery only (see
   `session-states.md` §1). The app is never told; the run file records it;
   every state-run needs a baseline run of the same persona and trip on record
   or alongside.

## Grading loads (after the run, grader only)

Grader reads everything: scoring/ (three files), canon/divergence-map.md,
gaps/, the transcript, the artifacts. Grade against scoring/rubric.md with
scoring/expected-fit.md as the diff target.

**Grading burns the session, permanently.** A window that has read scoring/
can never play that seeker again. If more runs are planned, grade in a
separate window or hand the transcript to a fresh subagent.

**Off-ledger venues.** Where the app recommended a venue not on the ledger,
the grader judges it against canon/taste.md and writes the judgement (venue,
verdict, why, confidence) to `runs/<run>/off-ledger-judgements.md`. Promotion
into the ledger happens later, in builder mode, with a decision entry.
