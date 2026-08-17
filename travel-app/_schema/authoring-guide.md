# Authoring guide — building the next seeker

Distilled from `founders/synthetics/_schema/authoring-guide.md` and adapted
for people-not-companies. Follow the folder architecture in the design
contract exactly; this guide is about *how* to fill it so the result is an
instrument, not a pile of plausible files.

## Order of operations (and why)

1. **Grounding before invention.** Read (in this order) the design contract,
   `travel/brand/01-brand-foundation.md`, the WHO→PAIN→SOLUTION→BENEFIT
   statements in `travel/brainstorms/`, the 2026-08-16 usability feedback,
   and the Otto/north-star notes in `synthetic-agents/example-otto-files/`.
   Write `_research/calibration.md`: which audience statement(s) the persona
   instantiates, which real-user finding it is designed to re-test, and what
   real workarounds it carries (Google Maps saves, a friend's Doc, Instagram
   saves). A persona that no brand hypothesis needs is a costume.
2. **Spine, then ledger, then narrative.** Fill `canon/persona.yaml` against
   `_schema/persona.schema.yaml`. Then write `canon/data/taste-ledger.csv`
   per `taste-ledger.spec.md` — ≥25 real venues, verdict range, catalog rows,
   home-city rows. Only THEN write `taste.md`, `people.md`, `history.md`,
   quoting ledger ids. The dominant defect class in the founders corpus was
   prose aggregates drifting from generated data; here it will be prose
   verdicts drifting from the ledger.
3. **People before persona.** `canon/people.md` names every companion the
   seeker will plausibly mention, with their TRUE preferences and their real
   power over the decision (veto: none/soft/hard; payer; decision-maker). The
   distortion classes for heron/finch/magpie live in the gap between the
   seeker's account of these people and this file.
4. **Divergence map as you go.** Every material fact is classified at
   authoring time: `volunteered` (says it unasked) / `when asked` / `never
   said` (must be inferred or asked specifically) / `wrong` (says something
   false; ledger entry). The map is what makes runs gradeable.
5. **Persona after canon.** The character must be wrong about a person who
   already exists. psychology → beliefs ([T]/[F]/[~] against canon and ledger
   ids) → voice → behaviour → companions-view, then the ledger LAST with a
   canon pointer in every `True` field.
6. **Trips.** T1 brief = the trip in the persona's own head: dates, party,
   what's booked, what they'd literally type in the first free-text box, what
   a good evening looks like to them, what they'll do at the end (save? send
   to Sam?). T2 = a second session, written *from the persona's memory of
   T1* (which may be imperfect — that is content, in gaps/, not a state).
   Events = one card each, mid-run, one sentence of trigger and the
   persona's true reaction.
7. **Scoring last, README/PROVENANCE/INDEX dead last.** `expected-fit.md`
   is written from the ledger: hit / acceptable / miss classes per trip and
   the named *flattering-but-wrong* pick. `buried-findings.md` holds 2–3
   truths derivable from canon that the persona never says (and the
   derivation). `rubric.md` follows the shared section structure (design §8)
   with persona-specific rows.

## Distortion design rules

- 5–7 load-bearing distortions, ALL of one class per persona. Class purity is
  what makes the slate comparable.
- Each entry: **True** (canon/ledger pointer) / **Stated** (their words) /
  **Volunteers?** (`freely` / `under trust` / `never`) / **Why** (motivated by
  psychology.md, never arbitrary) / **Unlock** (a SPECIFIC trigger the app
  could plausibly produce — a calibration option, a Marlowe question, a rec
  that lands — plus what the correction sounds like, plus the residual).
- **Volunteers? is not optional.** A player who hands the app a `never` item
  unprompted has given it a probe it never earned; the self-report catches
  it, the grader discounts it.
- **The unlock must be reachable by the app.** The app has a fixed question
  set plus free chat. If the only unlock is a question no product would ask,
  the distortion is untestable — redesign it. Good unlocks: "who's coming?",
  "what would make you leave a place?", "when were you last there?", showing
  one concrete option and reading the reaction, asking about a specific past
  evening.
- **One unreliable self-report per persona**: a claim with no true value
  ("we're adventurous eaters", "I know London really well", "the group's
  easy") — the test is whether the app holds it as structured uncertainty or
  stores it as fact.
- **The flattering-but-wrong pick** must exist for every T1: a venue in the
  ledger (ideally `in_catalog: seen`) that matches the *stated* need and fails
  the *actual* one, with `who_vetoes` filled.

## Verification pattern (fresh-context subagents, before "built")

1. **Consistency audit** — a subagent reads persona.yaml, the ledger,
   people.md, taste.md, beliefs.md, distortion-ledger.md and lists every
   contradiction (verdict vs prose, `who_vetoes` vs people.md, [T]/[F] tag vs
   canon, `True:` vs ledger). Fix all; log in `_research/decisions.md`.
2. **Cold read** — a subagent reads ONLY a generated bundle and answers: who
   is this, what do they want from this trip, who else matters, what would
   they type first, what would they never say. Every fact it had to invent is
   a defect.
3. **Roleplay check** — a subagent plays the seeker from a bundle through the
   six Find screens (city, home, spots you love, occasion, feel, five cards),
   then two Marlowe turns: one vague ("anything else?"), one specific unlock.
   Confirm `never` items stayed silent, the vague probe got the stated value,
   the specific probe fired the written unlock with the residual.

## Rules that exist because of specific near-misses

- Name every companion the seeker will mention (an unnamed "my friend"
  forces invention).
- Pre-write, in canon, the two or three "spots you love" the persona would
  actually type at the app's calibration step — those are the app's only taste
  input in Find, so they are the most consequential rows in the ledger.
- Convert relative dates to absolute (`as_of` + N days).
- Never let the persona know app vocabulary before seeing it. Grep persona/
  and canon/ for "Your Word", "Marlowe", "Adjust the read", "why them" —
  zero hits.
- Real venues, taste-only claims. If you catch yourself writing that a place
  "closed" or "went downhill after the chef left", stop: verify and date it,
  or make it the persona's belief in gaps/.
- Casey's real friends, family and the app's real named curators (Casey,
  Priya, Jon at build time) are not models for any persona or companion.
