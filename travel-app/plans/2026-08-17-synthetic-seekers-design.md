# Synthetic seekers — design contract

Date: 2026-08-17. Owner: Casey. Status: approved (plan session 2026-08-17).
Ancestor: `founders/synthetics/plans/2026-08-08-synthetic-companies-design.md`.

## 1. Purpose

At Their Word promises *three to five places fitted to you, with a human source
and a reason you can understand*. That promise fails in specific ways: the app
was **never told** the constraint that mattered, or it **failed to notice** a
load-bearing claim, **failed to probe** to what was really meant, **failed to
record** it, or **failed to act** on it — or it produced a fluent, flattering
shortlist that a real person with that taste would not have enjoyed. None of
those can be told apart with a real user, whose truth we don't hold, or with an
improvised persona, whose truth is invented mid-run.

So: instruments. A synthetic seeker is a person whose truth we control
completely — what they actually like (a ledger of real venues with verdicts),
who is coming and who holds the veto, what they can spend and walk and eat,
what they've done before — and a character who obscures that truth in one
documented, repeatable way. When the app gets something wrong, the corpus can
say which of the five failures it was.

## 2. What is under test (the app, as observed 2026-08-17)

Observation, not canon; re-verify at each run. Three tabs.

- **Find** — a guided flow: choose city (London / Los Angeles / San Francisco;
  "More cities coming soon", "Request a city") → *Where are you from?* (city
  autocomplete + optional "other cities you know well enough to vouch for") →
  *Name a couple of spots you love — bar, restaurant, café, anywhere*
  ("Anywhere in the world. This is just to calibrate your vibe") → *What's the
  occasion?* (Solo trip / Couple's trip / Trip with friends / Family trip /
  A long weekend / Date night / Night out with friends / Finding great
  restaurants / Exploring a neighbourhood / Something else) → free-text
  *What are you hoping this trip feels like?* ("say it the way you'd text a
  friend"; "I'll know it when I see it" skip) → five three-option calibration
  cards, adaptively chosen ("No repeats — only the gaps you haven't covered"),
  e.g. *What should this trip make room for?* / *What kind of room pulls you
  in?* / *Where does food sit on this trip?* / *How much should each place
  carry?* / *What do you want more of?* → **HERE'S WHAT I THINK YOU'RE REALLY
  ASKING FOR** — a paragraph "read" with *Give me another read*, then *How
  adventurous are you feeling?* (Safe bets / Balanced mix / Stretch me) →
  *That feels right — show me my shortlist* → **YOUR LONDON SHORTLIST**: an
  intro paragraph and 3–5 place cards. Card = icon, name, area · category ·
  $/$$/$$$, one-line why, "**Casey**'s been there · why them?" (named curator
  — Casey / Priya / Jon seen), TOP PICK badge, Saved / Unsave, *The full
  story* expander (Open in Google Maps, address, a longer paragraph).
- **Marlowe** — "the friend who actually knows London, LA and San Francisco";
  free-text chat with attach button and prompt chips ("A lively long weekend
  in LA — where do I start?", "Plan a date night in San Francisco that isn't
  too polished", "Friends in London, one big night, no tourist traps",
  "Somewhere near Shoreditch tonight, nothing touristy").
- **Your Word** — tabs Places / Lists / People / Profile; a "Paste a doc,
  link, or place name…" bar with a Screenshots button; "SAVED WITH MARLOWE"
  recap; "Distance from…" filter, List / Map toggle; grouped by city with
  curator + tags per row (e.g. `Priya · wood-fire · foodie`); "Make a list out
  of it — your lists →".

Known vocabulary a new user meets cold: *Your Word*, *Marlowe*, *Open your
word*, *Adjust the read*, *Got one*, *That's it*, *The full story*, *why
them?*. The 2026-08-16 usability session found the vocabulary was not
understood without explanation, cards lacked photos, and Your Word was
"way too overwhelming" — those are live hypotheses the corpus can test.

## 3. What a seeker is

**A person plus a designed gap.** Concretely:

- **canon/** — objective truth: `persona.yaml` (spine), `taste.md`,
  `people.md` (companions and their real power), `history.md`,
  `divergence-map.md`, `data/taste-ledger.csv`.
- **persona/** — the character: `bio.md`, `voice.md`, `psychology.md`,
  `beliefs.md` (marked [T]/[F]/[~] against canon), `behaviour.md`,
  `companions-view.md` (their take on each companion vs the truth-gap).
- **gaps/** — the script for being imperfect: `distortion-ledger.md` (5–7
  entries, one class), `unreliable-self-report.md` (a claim with no true
  value), `session-state-hooks.md`.
- **trips/** — the scenario layer (analogue of the founders' timeline):
  `T1-<slug>/brief.md`, `T2-<slug>/brief.md`, `events/E1–E3.md`.
- **scoring/** — grader only: `expected-fit.md`, `buried-findings.md`,
  `rubric.md`.
- **runs/**, **_research/**, `README.md`, `INDEX.md`, `PROVENANCE.md`.

Deliberately absent vs the founders layout (see `_schema/decisions.md` S1):
no `public/` (the app does not research the user), no financial CSVs and
tie-out (the taste ledger is the numeric ground truth), no real anchor person
(seekers are wholly fictional; venues are real).

## 4. Distortion classes (one per persona; class purity is what makes the
slate comparable)

| Codename | Class | Mechanism in one line | Unlock shape |
|---|---|---|---|
| heron | **Projector** | describes the trip they want to be the kind of person who takes; the partner's limits and the real pace never make it into the first answer | ask about the *other* person, or ask for a specific past evening that went well |
| lark | **Under-stater** | "anything, surprise me" — genuine openness on top of hard, unspoken filters (price, format, last train, done-that-already) | ask for a specific no ("what would make you leave?"), or offer one concrete option and read the flinch |
| finch | **Aggregator** | reports the group's needs as his own preferences and averages away the vetoes; hides that he's the only one who wants "cool" | ask who is coming *by name* and what each would refuse; ask who pays / who decides |
| magpie | **Over-confident curator** | speaks for the visitors' taste from his own; his list is stale in places and he doesn't know which | ask when he was last at a place; ask what the visitors themselves said they wanted |

Every ledger entry: **True** (canon pointer) → **Stated** (their words) →
**Volunteers?** (`freely` / `under trust` / `never`) → **Why** (from
psychology.md) → **Unlock** (a SPECIFIC probe; what the correction sounds
like; the residual) . Vague persistence NEVER unlocks; specificity does.

## 5. Fit is gradeable because the ledger exists

`canon/data/taste-ledger.csv` (spec: `_schema/taste-ledger.spec.md`) lists
≥25 real venues per persona with a verdict in {love, like, fine, no, never},
a why, and whether the venue was seen in the app's catalog at build time.
Rows span the app's three cities where the persona plausibly knows them, plus
home-city rows (the app asks for "spots you love — anywhere in the world").
`scoring/expected-fit.md` turns the ledger into hit / acceptable / miss classes
per trip and names the *flattering-but-wrong* pick — the rec that matches the
stated need and misses the actual one. Off-ledger recommendations are graded
against `taste.md`'s axes, and the grader writes the venue into
`runs/<run>/off-ledger-judgements.md` so the ledger can grow.

## 6. Run types (`_schema/loading-contract.md` is authoritative)

- **UI-relay** (primary): Casey drives attheirword.com in a fresh test
  account; a fresh window holding only the seeker bundle answers each screen.
- **Conversation** (Marlowe): same, free text.
- **Returning** (T2): a second session against the same account, bundle
  fenced to T2 (which includes T1's brief and what happened, as the persona
  remembers it).
- **Event injection**: one card, isolated harness, mid-run.
- **Paste-in** (magpie): the seeker brings a document; the doc lives in
  `trips/T1-*/paste/` and is player-visible.

Artifact capture before `@out`: open every Your Word surface (Places, Lists,
People, Profile, Map) and the app's read/summary of the seeker in the state
it was in **before** any correction; capture on judgment; always capture
whatever the app claims to remember.

## 7. Session states (`_schema/session-states.md`)

d12 deck; baseline ×4 is the control. Rushed · Skeptic · Delegating ·
Overloaded · Screenshot-in-hand · Too-Clean · Minimising ·
Comparison-shopping. Intensity d3. State modulates delivery only — never what
is true, never a `Volunteers?` value, never an unlock.

## 8. Grading (`<codename>/scoring/rubric.md`)

§1 onboarding & vocabulary comprehension · §2 elicitation per distortion on
Noticed / Probed / Recorded / Actioned · §3 unreliable self-report (pass-fail
×2) · §4 fit vs ledger (per pick: hit / acceptable / miss / flattering-wrong;
plus "did the read describe the actual need or the stated one") · §5 trust
legibility (could the seeker name back place / person / fit; did "why them?"
land) · §6 Your Word / retention (save, list, share, return, recall) · §7
conduct (invented venue facts, sycophancy, extraction before value,
compression failure) · §8 buried findings. Findings first; every mark cites a
turn or capture; not tested is never a pass. Grading burns the window.

## 9. Fidelity boundaries

Fictional people, real venues. Nothing about a venue beyond the persona's
taste unless verified and dated. Companions never voiced when minors. Casey's
real friends and the app's real named curators are off-limits as models.
Distortions ordinary and non-defamatory. Vocabulary in the persona files is
the persona's, never the app's (a seeker who says "Your Word" before seeing
it has been contaminated).

## 10. Build order and verification

Schema and tools first; heron establishes the per-persona pattern; lark,
finch, magpie authored from `plans/build-prompt.md` in fresh contexts. Each
persona passes a consistency audit (yaml ↔ ledger ↔ people ↔ ledger `True`),
a cold read (bundle only), and a roleplay check (Find flow's six screens
against the bundle; `never` items stay unvolunteered; unlocks fire as
written) before it is marked built in `coverage.md`.
