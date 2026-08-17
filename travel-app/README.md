# travel/synthetics — synthetic seekers for testing At Their Word

Private test infrastructure. A corpus of fully specified fictional people —
each with a real trip, a ledger of real venues they actually like or don't,
companions with real veto power, and a documented gap between what they say
and what is true — used to test **attheirword.com** end to end: the Find
flow's read and shortlist, Marlowe's elicitation, trust legibility (place /
person / fit), and Your Word (save, list, share, return).

Design contract: `plans/2026-08-17-synthetic-seekers-design.md`.
Operating contract for agents: `AGENTS.md`. Loading rules that invalidate a
run when broken: `_schema/loading-contract.md`. Sibling corpus and ancestor:
`../../founders/synthetics/`.

## Corpus state

| Codename | Who (codename-safe) | Class | Primary test | Status |
|---|---|---|---|---|
| heron | US couple, 4 nights London, anniversary; partner holds the veto | Projector | shortlist fit vs actual need; veto-holder elicitation; trust legibility to a stranger | built 2026-08-17 |
| lark | London local, weeknight, knows the obvious spots | Under-stater | beats-what-a-local-knows; hard filters under "surprise me"; recall on return | built 2026-08-17 |
| finch | organiser of a 5-friend LA weekend, mixed budgets | Aggregator | group constraints never volunteered; sharing / lists | built 2026-08-17 |
| magpie | London list-keeper hosting visitors; arrives to give recs | Over-confident curator | curator side: paste-a-doc, People/Lists, staleness and taste-mismatch | built 2026-08-17 |

## How to run a test (UI-relay, the primary mode)

1. **Fresh app account** for the persona (T2 reuses T1's account). Note the
   app build date if visible; otherwise "seen on <date>".
2. **Fresh player window.** From the repo root:
   `python3 travel/synthetics/tools/build_seeker_context.py <codename> T1`
   (add `--state <state[:n]>` to assign; otherwise it draws). Paste/load only
   the returned bundle. In Claude Code, `/seeker <codename> T1` does this.
3. **Relay.** Drive the app; tell the player exactly what the screen shows
   (question, options, cards, Marlowe's reply). The player answers as the
   seeker: what to tap, what to type (quoted), what they think but don't
   type (`[bracketed]` — never relayed). Never tell the app it's a test.
4. **Before `@out`:** open every Your Word surface (Places, Lists, People,
   Profile, Map) and the read/shortlist intro; capture the read *before* any
   correction and whatever the app claims to remember; screenshots to
   `<codename>/runs/<run>/artifacts/`.
5. **`@out`**, then the player's self-report (any ledger deviation).
6. **Grade in a different window** against `<codename>/scoring/`. Record the
   run in `<codename>/runs/<run>.md` with the frontmatter in
   loading-contract rule 6. Off-ledger venues → `off-ledger-judgements.md`.

Conversation (Marlowe-only), returning (T2), event and paste-in modes: see
`_schema/loading-contract.md`.

## Map

- `_schema/` — persona.schema.yaml, taste-ledger.spec.md, loading-contract.md,
  session-states.md, authoring-guide.md, decisions.md (S-numbered)
- `plans/` — the design contract; `build-prompt.md` (author the next seeker)
- `tools/build_seeker_context.py` — the mandatory bundle builder; `tests/`
- `<codename>/` — README, INDEX, PROVENANCE, canon/, persona/, gaps/, trips/,
  scoring/ (grader only), runs/, _research/ (never in runs)
- `coverage.md` — behaviour × persona matrix and known gaps
- `../.claude/skills/seeker/` — the Claude Code loading ritual
