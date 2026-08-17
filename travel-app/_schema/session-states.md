# Session states — presenting postures for seekers

Nine postures (plus Baseline) a seeker-player can be drawn into, so the corpus
tests **robustness** rather than only competence. Persona-agnostic; the
per-persona hooks some states need live in `<codename>/gaps/session-state-hooks.md`.
Adapted from `founders/synthetics/_schema/session-states.md` (whose §1 design
rules apply verbatim and are summarised here).

**Terminology.** *Session state* in files and metadata; *presenting posture* in
prose. States are behavioural, not affective — a mechanic the player executes.

## 1. Design rules (binding)

> **State modulates delivery. Canon and ledger govern content.**

A state may change turn length, attention, sequencing, what the seeker wants
from the session, and how they receive a suggestion. It may **never**: unlock
a distortion or re-gate one; change a `Volunteers?` value (ledger *or*
unreliable-self-report); alter any canon fact, ledger verdict, or belief;
disable a documented behavioural lever in `behaviour.md`; make the seeker
disclose what the ledger says they never volunteer, or withhold what they
volunteer freely. Unlocks are untouchable: no state modifies the response to a
correctly executed unlock trigger. Intensity scales *visibility* of the
mechanic (1 trace / 2 evident / 3 dominant), never how much canon material is
in play. Generated material is recombination of what the persona already has.
`behaviour.md`'s hard limit — colour yes, facts no — outranks every state.

## 2. The deck (d12) and intensity (d3)

| Roll | State | Code |
|---|---|---|
| 1–4 | Baseline (persona as written; the control) | — |
| 5 | Rushed | R1 |
| 6 | Skeptic | S1 |
| 7 | Delegating | D1 |
| 8 | Overloaded | O1 |
| 9 | Screenshot-in-hand | H1 |
| 10 | Too-Clean | C1 |
| 11 | Minimising | M1 |
| 12 | Comparison-shopping | X1 |

Intensity: d3 for any non-Baseline draw; bare state names default to 2.
Draw is recorded in MANIFEST.json (`state_selection: drawn|assigned`).

## 3. The specs

Each spec: *what it models* · *how it shows* (by intensity) · *what it never
does* · *when handed a good recommendation* · *hooks needed*.

### R1 — Rushed
Models: on a phone with three minutes — at a gate, between meetings, partner
waiting. Shows: 1 = short answers, skips one optional field; 2 = skips
free-text ("I'll know it when I see it"), taps first plausible calibration
option, asks for the shortlist early; 3 = abandons any screen that asks a
second open question, types "just show me" into Marlowe. Never: changes what
they'd say if asked directly; a direct probe still gets the ledger answer,
just shorter. Given a good rec: saves it and leaves — does not read the full
story. Hooks: none.

### S1 — Skeptic
Models: assumes this is another AI list wearing a person's name. Shows:
1 = tests the read ("Give me another read"), reads the "why them?" line with
suspicion; 2 = asks Marlowe who Casey/Priya actually is, whether they've
really been; 3 = calls out any generic phrasing, refuses to save until a rec
lands on something they already know is right. Never: refuses to answer a
concrete question; if the app names a ledger `love` venue with a legible
reason, the skepticism drops one notch for the session (that's the lever;
the state may not remove it). Hooks: none.

### D1 — Delegating
Models: the seeker is relaying for the real decision-maker (partner, group,
visitor). Shows: 1 = "let me check with —" once; 2 = answers calibration
cards from the *other* person's view, hedged; 3 = the seeker's own taste
nearly disappears from the transcript; asks whether the list can be sent to
someone. Never: changes the ledger's `Volunteers?` — a `never` item about the
decision-maker still isn't volunteered; the seeker just says the
decision-maker's *name* more. Hooks: `D1 eligible delegate` (which companion,
per persona; personas with no eligible delegate treat D1 as Baseline).

### O1 — Overloaded
Models: arrives with 30 saved pins, two Docs, and a screenshot folder; wants
triage not discovery. Shows: 1 = mentions "I've already got a list"; 2 = pastes
or names several venues from history.md unprompted, asks "which of these?";
3 = resists anything new; frames every rec as "instead of X?". Never: names a
venue that isn't in canon/history.md or the ledger. Hooks: `O1 pin sample`
(6–10 ledger ids the persona would bring).

### H1 — Screenshot-in-hand
Models: someone else sent them one place; they want it checked or extended.
Shows: 1 = mentions the rec; 2 = opens with it in Marlowe / pastes it into
Your Word; 3 = evaluates the whole shortlist relative to that one place. Never:
the screenshot's venue is fixed per persona (a real venue; its ledger verdict
may be `fine` or `no` — the test is whether the app builds on or corrects
it). Hooks: `H1 screenshot venue` (ledger id + who sent it, per persona).

### C1 — Too-Clean
Models: the ideal user — answers every question fully and honestly *at the
stated level*. Shows: 1–3 = progressively more complete, articulate answers.
Never: volunteers `never` items — cleanliness is about **stated** truths; the
gap between stated and actual is exactly what stays. Control condition for
"is the app failing on delivery or on elicitation?" Hooks: none.

### M1 — Minimising
Models: understates constraints out of politeness or self-image ("we're
easy"). Shows: 1 = softens one hard constraint into a preference; 2 = answers
"Balanced mix" when canon is `safe`; 3 = says yes to a rec that violates a
constraint and only flinches when asked to save it. Never: moves a `never` to
`freely` in reverse (M1 cannot make a `freely` item silent — that is a content
change); the direct probe still unlocks. Hooks: `M1 softened constraint`
(which persona.yaml constraint gets minimised).

### X1 — Comparison-shopping
Models: has ChatGPT / a Top-10 list open in another tab. Shows: 1 = mentions
"ChatGPT said —"; 2 = pastes an alternative list and asks why these instead;
3 = grades every rec against the other tab out loud. Never: the other tab's
list is fixed per persona (5 real venues, in `session-state-hooks.md`, drawn
from history.md; verdicts already in the ledger). Hooks: `X1 other-tab list`.

## 4. Grading integration

State and intensity are recorded in the run file and announced to the
operator once at load, out of character. Rubric §2 Probed credit is
unaffected by state (unlocks are untouchable). §1 onboarding and §7 conduct
may be graded *harder* under R1/S1/X1 — say so in the grade. Every state-run
pairs with a Baseline of the same persona and trip.
