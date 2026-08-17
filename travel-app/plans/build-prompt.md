# Synthetic Seeker Build Prompt

Fill the parameter block, paste everything below the line into a fresh
context, run once per persona. Long-horizon authoring; do not surface a
token countdown.

---

## Parameters

- **Codename:** `<heron|lark|finch|magpie|…>`
- **Slate entry:** the row for this codename in
  `travel/synthetics/plans/2026-08-17-synthetic-seekers-design.md` §4 and the
  README corpus-state table (who, class, primary test, T1/T2 sketch)
- **Distortion class:** as in the slate
- **T1 city:** London | Los Angeles | San Francisco
- **Pattern persona (if any):** `heron/` — mirror its file shapes exactly

---

# Mission

Build one synthetic seeker for the `travel/synthetics/` corpus: a fully
specified fictional person used to test At Their Word (attheirword.com), a
human-grounded place-discovery app. The seeker will be played by a fresh
model window against the live app while an operator relays screens; a grader
will afterwards judge, against files you write, whether the app was never
told, failed to notice, failed to probe, failed to record, or failed to act —
and whether the places it recommended are ones this person would actually
have loved.

Read first, in order: `travel/synthetics/AGENTS.md`, the design contract,
`_schema/authoring-guide.md`, `_schema/persona.schema.yaml`,
`_schema/taste-ledger.spec.md`, `_schema/session-states.md` (§3 hooks). Then
the grounding: `travel/brand/01-brand-foundation.md`, the WHO→PAIN statements
in `travel/brainstorms/`, `travel/260816-at-their-word-user-interview-feedback.md`,
and `synthetic-agents/example-otto-files/*.md`. If a pattern persona exists,
read its INDEX.md and then each of its files as you write the equivalent.

# Hard rules (from AGENTS.md — binding)

1. Wholly fictional person and companions; no real private person as model
   (not Casey's friends/family, not the app's real curators Casey / Priya /
   Jon). Real venues only in the ledger; taste-only claims about them; any
   venue *fact* verified and dated or moved to gaps/ as a belief.
2. In-world name only inside the persona folder. Codename everywhere else.
3. No app vocabulary in persona/ or canon/ ("Your Word", "Marlowe", "Adjust
   the read", "why them?", "Open your word") — the seeker has never seen it.
4. Ledger is ground truth; prose quotes `L-nn` ids; every ledger `True:`
   field, every [T]/[F] tag, every expected-fit class points at canon.
5. Distortions: 5–7, one class, each with True / Stated / Volunteers? / Why /
   Unlock(+correction+residual); unlocks reachable by the app's actual
   question set or a plausible Marlowe turn; vague persistence never unlocks.
6. One unreliable self-report (no true value). One flattering-but-wrong pick
   per T1, `in_catalog: seen` where possible.
7. No first-person minors. Care register = what a stranger types into an app.
8. Every judgment call → `_research/decisions.md` (D-numbered).

# Deliverables (the persona folder, exactly)

```
<codename>/
├── README.md  INDEX.md  PROVENANCE.md
├── canon/  persona.yaml  taste.md  people.md  history.md  divergence-map.md
│           data/taste-ledger.csv
├── persona/ bio.md voice.md psychology.md beliefs.md behaviour.md companions-view.md
├── gaps/    distortion-ledger.md unreliable-self-report.md session-state-hooks.md
├── trips/   T1-<slug>/brief.md  T2-<slug>/brief.md  events/E1.md E2.md E3.md
│            (magpie also: T1-<slug>/paste/<doc>.md — the document he brings)
├── scoring/ expected-fit.md buried-findings.md rubric.md
├── runs/    .gitkeep
└── _research/ decisions.md calibration.md catalog-observations.md
```

File shapes (mirror `founders/synthetics/kestrel/` conventions, adapted):

- Every persona/ and gaps/ file opens with an H1 `# <Name> — <aspect>` and a
  blockquote: `> Character file: wholly fictional person for roleplay. Venues
  named are real; everything said about them is this character's taste, not
  a claim about the business. See PROVENANCE.md.`
- `bio.md`: **Convention (read first)** paragraph → identity & texture (low-
  specificity personal life by rule) → money, personally → relationships that
  matter to runs → what they'd never type into an app.
- `voice.md`: Register → Vocabulary → Numbers-and-places dialect (how they
  name budgets, distances, venues — the class's fingerprint) → Recurring bits
  → What they never say.
- `psychology.md`: the core mechanism (why this class) → the fears, ranked →
  reactions when a rec misses / when asked about the veto-holder → what
  correction feels like (post-unlock behaviour, one-notch decay across
  sessions).
- `beliefs.md`: About this trip / About the people coming / About places and
  taste / About themselves / The private doubts — bullets tagged [T]/[F]/[~]
  with ledger/canon pointers.
- `behaviour.md`: Session shape (what they do on each Find screen; how they
  use free chat) → Answer mechanics (the class rules, numbered, binding) →
  Topic-specific behaviours → What makes them save / leave / share → Hard
  limits (do not vary).
- `companions-view.md`: The pattern → per person: **Their take:** / **The
  gap:** (canon pointer) → party dynamics.
- `distortion-ledger.md`: header explaining fields + `Volunteers?` note; D-01…
  entries; closing `## Interaction map (for graders)`.
- `unreliable-self-report.md`: The claim → Where it comes from → What can
  actually be known → Who knows it's unreliable → What this tests
  (good-run / weak-run).
- `session-state-hooks.md`: values for D1 / O1 / H1 / M1 / X1 as the state
  spec requires (or "n/a — treat as Baseline" with reason).
- `trips/T1-*/brief.md`: dates (absolute), city, party present, what's
  booked, where they're staying (area only), what they'd type in the first
  free-text box (verbatim), the two–three "spots you love" they'd name
  (ledger ids), what a good evening looks like, what they'll do at the end.
  T2 likewise, plus "what happened last time (as I remember it)".
- `events/E*.md`: trigger (one sentence, operator-injectable mid-run) → true
  reaction → what the seeker says → what a good app response looks like.
- `expected-fit.md`: per trip: hit / acceptable / miss / flattering-but-wrong
  with ledger ids; the read the app *should* produce vs the read it will
  produce if it only hears the stated need; off-ledger judging axes.
- `buried-findings.md`: 2–3 findings + derivations from canon files.
- `rubric.md`: §1–§8 per design §8, rows specific to this persona, 0–2 per
  item, pass-fail where marked, "not tested is never a pass".
- `divergence-map.md`: table — fact | canon pointer | volunteered / when
  asked / never said / wrong (→ D-nn).
- `INDEX.md`: task→files table + one-line-per-file summaries (one screen).
- `README.md`: who/what, the design in one paragraph, how to run, map,
  grader caveats. `PROVENANCE.md`: fiction boundary; venues real; private use.

# Method

Phase 0 grounding → Phase 1 spine + ledger (≥25 rows; consistency rules in
the spec) → Phase 2 canon narratives → Phase 3 persona files → Phase 4 gaps
→ Phase 5 trips + events → Phase 6 scoring → Phase 7 README/INDEX/PROVENANCE
→ Phase 8 verification: run the three fresh-context checks in
`_schema/authoring-guide.md` (consistency audit, cold read via
`tools/build_seeker_context.py <codename> T1`, roleplay check) as subagents
where possible, fix findings, log them. Finish by grepping the folder for the
app vocabulary and for the in-world name outside the folder.

Return: a short build report — files written, ledger row count and verdict
distribution, the distortion list (ids + one line each), the
flattering-but-wrong pick, verification results and fixes.
