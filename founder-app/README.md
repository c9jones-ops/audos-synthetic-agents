# Synthetic companies — test corpus

A small corpus of synthetic founder-led companies for testing the
founder-support platform repeatedly, comparably, and over time. Design
contract: plans/2026-08-08-synthetic-companies-design.md. Schema and
operational rules: _schema/. Which company tests what: coverage.md.

Each company is a real, researchable business (named only in its
PROVENANCE.md) with a fictional founder whose account of it diverges from a
clean, tied-out canon in documented, gradeable ways.

## How to run a test

1. **Pick the mode** — Foundation roleplay (live or frozen), seeded
   save-point, or event injection. What each mode tests: the design spec's
   run-model table; per-company specifics: <codename>/README.md.
2. **Build and load exactly per _schema/loading-contract.md.** Before the player
   reads company material, run `python3 synthetics/tools/build_founder_context.py
   <codename> <save-point>`. Fable reads only the returned bundle; it never reads
   the source company tree. The platform gets the company name + URL (live), the
   frozen snapshot (frozen), or the save-point seed (seeded).
3. **Draw a session state** (added 2026-08-12; loading-contract rule 8, specs in
   _schema/session-states.md). The player gets a presenting posture and an
   intensity alongside the save-point — `compliant:2` — drawn on a d20 or
   assigned. It varies HOW the founder shows up, never who he is or what is
   true. **The platform is never told.** Baseline is a valid draw and is the
   control condition. Pair every state-run with a baseline run of the same
   company and save-point.
4. **Run the conversation.** The player enacts the distortion ledger exactly;
   ambient character may vary. Event runs add exactly one card from
   timeline/events/.
5. **Record run metadata** — date, mode, save-point, session state and
   intensity (plus whether it was drawn or assigned), event card, model
   versions, what each side was loaded with.
6. **Grade** against <codename>/scoring/: expected-state.md is the diff
   target, rubric.md the score sheet, buried-findings.md the derivation key;
   canon/divergence-map.md classifies research results. Grading is by hand
   for now (per the design spec's open question on automation).

## Manual side-by-side run (two windows, human relaying)

The simplest real test: your platform in one window, the founder-player in
another, you copying messages between them.

1. **Founder window** — open the `founders` folder (the repo root — in Claude
   Code the /founder skill only loads from there) in a **fresh session**
   (fresh matters: a session that previously read scoring/ plays a founder
   who has seen his own answer key). Type `/founder` (Claude Code) or
   `@founder kestrel` (ChatGPT/Codex or any AGENTS.md-reading tool).
   Optionally add a save-point and a session state:
   `/founder ember T0 compliant:2`. With no state given, the skill draws one
   and reports it out of character. Wait for the "in character" confirmation,
   and **write the state down** — the run file needs it and the grade is not
   interpretable without it.
2. **Platform window** — start your platform's onboarding and give it the
   anchor company name and URL from kestrel/PROVENANCE.md (live mode), or
   attach the contents of kestrel/public/snapshot-2026-08-10/ instead
   (the current baseline; snapshot-2026-08-09/ is superseded — see its manifest)
   (frozen mode — reproducible).
3. **Relay** — paste the platform's messages into the founder window and the
   founder's replies back. Don't editorialize either direction; you are the
   wire. The founder handles everything in character, including bad research
   and awkward personal questions.
4. **End** — type `@out` in the founder window. Save both transcripts.
5. **Grade** — paste or attach the transcript **and the captured artifacts**
   (loading-contract rule 5) and ask for a grading pass against
   `kestrel/scoring/rubric.md` with `scoring/expected-state.md` as the diff
   target. Record the run in `kestrel/runs/` with its metadata: date, mode
   (live/frozen/UI-relay), save-point, event card if any, model versions.

   **Grading burns the window permanently.** Doing it in the founder session
   after `@out` works, but that session has now read the answer key and can
   never play the founder again. If you plan more runs today, grade in a
   separate window or hand the transcript to a fresh subagent.

## UI-relay runs (the platform is a live product)

The most realistic mode, and the only one that tests what the platform
*stores* rather than only what it says. Same relay procedure as above, except
you are pasting screenshots of a real interface rather than text.

- **The player clicks.** Screens and buttons are in-world; the founder decides
  what he'd tap and says so, in character, with no meta-commentary about the
  product. Give operator directions in brackets — `[you've just opened this
  app]`, `[you clicked X and saw this]` — which the player acts on without
  voicing.
- **Capture everything persistent, not just the chat.** Profile cards, memory
  views, saved-fact lists, anything the product claims to remember. This is
  mandatory here: rubric §7 and the Recorded axis are ungradeable without it,
  and the failure modes that live in storage never appear in the transcript.
  Kestrel's first run stored a founder's *forecast* revenue and its
  known-unreliable utilization figure as privileged ground truth; the
  conversation gave no sign of it.
- **Record what the platform's own research card claimed** before the founder
  corrected it — that's the §1 evidence, and it disappears once corrected.

Event runs: same procedure, but after entering founder mode tell the player
which single card from kestrel/timeline/events/ is live ("play E2"). Seeded
save-point runs additionally require loading your platform with the matching
kestrel/timeline/<save-point>/seed.md as its prior memory — that side is
platform-specific and yours to wire.

## Corpus state

| Company | Status | Archetype | Distortion class |
|---|---|---|---|
| kestrel/ | **Built** (2026-08-09) | Founder-led creative studio, ~31 FTE, bootstrapped | Compressor |
| ember/ | **Built** (2026-08-11) | Bootstrapped craft consumer brand, 9 FTE, Kickstarter+F&F, cash-tight | Believer (composite: extrapolation / craft-guard / oscillation, phase-pinned) |
| fenwold/ | Planned | Founder-led consumer brand, founder 12–14 yrs in | Withholder |
| orrery/ | Planned (schema stretch-check before fenwold) | AI-native B2B, Series C hypergrowth | Narrator |

Before building fenwold: draft orrery's company.yaml + CSV headers against
_schema/ to confirm the schema stretches (see the design spec's build
sequence; the schema files carry [scale] notes from a paper stretch-check —
the draft makes it real). Snapshot orrery's anchor early; its funding
coverage is still accumulating.
