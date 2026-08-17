# finch

A synthetic seeker for testing At Their Word. Third persona in the
`travel/synthetics/` corpus; the group-trip case, mirroring heron's pattern.

## Who and what

**The seeker:** a 29-year-old account manager from Chicago planning a
three-night Los Angeles weekend (2026-09-11 → 14) for five college friends —
a tasteful bachelor-ish weekend for one of them. Distortion class:
**Aggregator**. He reports the group's needs as his own preferences and
averages away the vetoes: "five of us, everyone's pretty easy, we want great
dinners and cool bars, somewhere with a scene, budget's mixed but nobody's
counting, we'll Uber everywhere." The truth is four named people with four
different hard edges — two who can't or won't do $$$ (one is between jobs),
one who doesn't drink, one who is vegetarian and lands late Friday — plus a
groom whose one message *is* the brief, a group that decides by vetoing his
plan after the fact, and a real map (five people, no car, two rides per move)
that rules out half his list. He is the only one who wants "cool," and he
says "we."

**What this persona tests:** whether the app asks **who is coming, by name,
and what each of them would refuse**, and who pays; whether its read
describes five people or one; whether a $$$ Arts District dinner he *named*
as a favourite (Bestia — the flattering-but-wrong pick) becomes the top pick;
whether "bachelor" defaults to a stag-do; whether he can make a list, share
it to a group chat, and — a week later, after two vetoes arrive — re-edit the
same list with the app remembering the vetoes and dropping the vetoed places
without being re-told. A buried finding: the real constraint is geography
plus two budgets, not vibe.

## The design in one paragraph

Canon is a ledger of 38 real venues (27 Los Angeles, 7 Chicago, 3 San
Francisco, 1 Grand Rapids; 8 love · 17 like · 4 fine · 7 no · 2 never; every
row `in_catalog: unknown` because the app's LA catalog was not observed at
build — see _research/catalog-observations.md) plus a spine, a people file
that gives the groom and the between-jobs friend hard vetoes, and a history
whose one prior trip as five is the master unlock. The persona diverges from
canon in six documented, unlockable ways (gaps/distortion-ledger.md), all one
class, all opened by specificity (names, refusals, who pays, one card +
"would all five come?", the last trip) and never by persistence, plus one
self-report with no true value ("the group's easy"). Three findings are
derivable from canon and never voiced (scoring/buried-findings.md). Two
trips: T1 the planning session a month out, ending in a shared list; T2 a
week later, after the chat has replied with two vetoes, to re-edit and
re-share. Three event cards. Everything material is classified volunteered /
when asked / never said / wrong in canon/divergence-map.md.

## How to run a test

See `../README.md` and `../_schema/loading-contract.md` (authoritative).
Summary: fresh app account; from the repo root
`python3 travel/synthetics/tools/build_seeker_context.py finch T1` (add
`--state <state[:n]>` to assign); a fresh player window reads only the bundle;
the operator relays screens; capture every persistent surface — **including
the list and whatever the share produces** — and the read *before* any
correction; `@out`; player self-report; grade in a different window against
scoring/. T2 continues the same account and the same list.

## Map

- canon/ — persona.yaml (spine), taste.md, people.md, history.md,
  divergence-map.md, data/taste-ledger.csv
- persona/ — bio, voice, psychology, beliefs ([T]/[F]/[~]), behaviour,
  companions-view
- gaps/ — distortion-ledger (D-01…D-06), unreliable-self-report,
  session-state-hooks (D1/O1/H1/M1/X1)
- trips/ — T1-la-bachelor-weekend, T2-la-replan-after-vetoes, events/E1–E3
- scoring/ — expected-fit, buried-findings, rubric (grader only)
- runs/ — one file per graded run; _research/ — decisions, calibration,
  catalog-observations (never in runs)

## Caveats a grader should know

- The LA catalog was **not observed** at build; expect off-ledger picks and
  update _research/catalog-observations.md from the run's cards before
  grading §4. The app changes weekly; re-verify surfaces before §1/§5/§6.
- A save is not a hit: Devin saves things "for himself" while thinking [not
  with these four]; grade fit against the *group* verdict and his brackets.
- One friend's fact (he doesn't drink) is `never` and has one narrow key; if
  it appears in a transcript without that key, it is a player breach or an
  app confabulation — either is a finding, never a credit.
- The T2 brief has Devin unable to name Nashville venues or the exact T1
  list — deliberate; the player must not invent them, and takes the T1
  transcript's outcome as given if the operator states it.
- The in-world first name was changed from the build parameters to avoid a
  same-role collision with a heron companion (_research/decisions.md D-01).
