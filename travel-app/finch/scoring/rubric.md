# finch — scoring rubric (scoring only; never enters a run)

Grades a run against expected-fit.md, gaps/distortion-ledger.md,
gaps/unreliable-self-report.md, canon/divergence-map.md and buried-findings.md.
Hand-scored. **Findings first, then scores.** Every mark cites a turn number
or a captured artifact. **Not tested is never a pass** — an item the run gave
the app no chance to show is N/A, not 2. Score 0–2 per item (0 absent /
1 partial / 2 full) unless marked pass-fail. Grading burns the window.

## §1 Onboarding & vocabulary comprehension (against design §2 as observed; re-verify the app's surfaces at run time)

| Item | 0–2 | Cite |
|---|---|---|
| Devin understood what the app *is* by the end of the Find flow without operator help (would he describe it to the chat as "recs from actual people who've been" or "another AI list"?) | | |
| The read stage was understood as a *read of him / the group* — he reacted to its content, not its label | | |
| Card anatomy understood: he could tell what the named person's line meant and what "the full story" opens | | |
| Saved-places surface: he found where saves went and could describe it; **he found how to make a list and how to share it** | | |
| Any app term he met cold and misread, listed with the turn — this is a finding, not a score | | |
| Under R1/S1/X1: graded harder — did the flow survive a rushed / suspicious / comparing first contact? | | |

## §2 Elicitation — the distortion table (against gaps/distortion-ledger.md)

Score each on **Noticed** (treated the stated claim as load-bearing — e.g.
"everyone's easy," "budget's mixed but nobody's counting," "we'll Uber, LA's
LA" — rather than colour), **Probed** (reached the written unlock or made a
well-aimed *specific* attempt: **who is coming, by name; what would each
refuse; who pays / would all five come to this; what did the group actually
do last time; one concrete card**), **Recorded** (the corrected value held as
*that person's* constraint — Danny's, Nate's, Rafi's — not as Devin's
preference; claim and correction both kept), **Actioned** (the read or
shortlist changed because of it).

| Distortion | Noticed | Probed | Recorded | Actioned |
|---|---|---|---|---|
| D-01 who's coming / who decides / the groom's brief — **did it ask for names? for what each would refuse? who pays?** (score each sub-question in Cite) | | | | |
| D-02 money — two budgets averaged to none (did it show one $$$ card and ask "would all five come?") | | | | |
| D-03 geography — five people, two rides, near the house | | | | |
| D-04 Elliot doesn't drink — the bar plan (narrow key only; **never credit Probed for "any dealbreakers?"**) | | | | |
| D-05 "cool" is one person / the group's shape (master key: last trip) | | | | |
| D-06 Rafi late Friday + vegetarian → Saturday dinner with a real menu | | | | |

Notes: Probed credit requires *specificity*; "anything else I should know?" /
"tell me about the group" scores 0 regardless of how often it's asked
(matches the character). One clean D-01 (names + refusals) with recording is
a strong Find-flow run; D-05 alone, recorded and actioned, is a strong run.
**State does not change Probed** — unlocks are untouchable. A player
self-report noting a `never` item volunteered without its trigger (above all
Elliot) voids Probed credit for that row and is a finding about the player.

## §3 Unreliable self-report — "the group's easy / everyone's down for whatever" (pass-fail ×2)

**PASS:** held as colour-with-structure (the planner is easy; four people
with four different easies; ask who) and *not* used to justify a $$$ room, a
cocktail temple, or "adventurous group" in the read. **FAIL:** stored as fact
and driving ("an easygoing group up for anything" in the read; "since the
group's easy" as a why-line for L-12/L-14/L-32), OR over-corrected to "a
demanding group with lots of constraints" after an unlock. Cite the read and
any why-line that leans on it.

## §4 Fit vs ledger (against expected-fit.md) — **per pick, against the GROUP verdict**

| Pick (name · ledger id or off-ledger) | Class: hit / acceptable / miss / flattering-wrong (group T1 verdict; who_vetoes) | Why-line named the deciding axis (one table / everyone can pay / near the house / real menu for one / not a drinking-only room)? 0–2 |
|---|---|---|
| TOP PICK | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

Then:
- **The read: actual vs stated need** — 0 (transcribed the plural) / 1 (one
  table for five + budget + near, without the per-person structure) / 2
  (both, with the pattern: Saturday, one table, ~$50, real menu for one,
  a bar that isn't about the drink, near the house; Friday is four). Cite the
  read *before* any correction. −1 if the read states Elliot's fact without
  D-04's key in the transcript.
- **Flattering-but-wrong check:** if Bestia (L-12) is TOP PICK for the
  Saturday dinner — or Death & Co (L-14) is *the* bar, or Musso & Frank
  (L-32) is *the* bachelor dinner — §4 caps at 1 unless the why-line flags
  the price / the room for five and asks. Note whether Devin *saved* it (a
  save is not a hit — check his [brackets]).
- **Off-ledger picks:** judged on taste.md axes; write to
  `runs/<run>/off-ledger-judgements.md`. Expect several — the LA catalog was
  not observed at build.
- **T2 only:** did the shortlist *change* (dropped the vetoed, kept the
  survivors) or re-serve T1? Re-serving scores 0 here and in §6.

## §5 Trust legibility (place / person / fit; the seeker is a stranger to the curators)

| Item | 0–2 | Cite |
|---|---|---|
| **Place** — could Devin say back what each pick *is* and its honest trade-off for five ("a big room; book it; two Ubers") | | |
| **Person** — he noticed the named person on the card and could say who they are relative to him (a stranger who's been there) | | |
| **"Why them?"** landed: he opened it and it changed his confidence in the pick, up or down; note if he treated the name as decoration or as ammunition for the chat | | |
| **Fit** — the why-line said why *these five*, not why the place is good; Devin could paste it into the chat as the reason | | |
| Did he trust a stranger's word enough to save / share / book on it? Cite the turn where he decided | | |
| Any place where the app asserted a *venue fact* (hours, "no wait," "they take big groups," a Dodgers home game) — was it correct? Unverifiable assertions are a §7 finding | | |

## §6 Saved places / lists / share / retention

| Item | 0–2 | Cite |
|---|---|---|
| Saved: he saved ≥1 place the *group* would actually go to (ledger `love`/`like`, group verdict), not only self-saves | | |
| **List creation:** he could make a list out of the saves and name it (the 2026-08-16 "way too overwhelming" finding re-tested on a five-person use case) | | |
| **Share to the group:** he found a way to share the list to the chat and would have (per behaviour.md rules); note *what* the share carried (names, why-lines, prices?) — could four people who never opened the app act on it? | | |
| **T2 recall:** the app named back something true from T1 unprompted (whatever T1 elicited — Danny, five, Silver Lake, Saturday, the budgets, Rafi, Nashville) | | |
| **T2 re-edit:** he could re-open the *same* list and edit it (drop / add) rather than start over; and the app **dropped the vetoed places without being re-told** — did it remember the vetoes it had heard (Nate's number, "near the house") and act on them before Devin re-stated them? | | |
| **T2 adapt:** the app re-aimed at the two vetoes rather than re-serving T1 | | |
| Would he come back the week before the trip? (his stated intent at end of T2) | | |

## §7 Conduct

| Item | 0–2 | Cite |
|---|---|---|
| No invented venue facts (hours, closures, "no wait," "seats big groups," a game that night) — every practical claim either sourced to the named person or hedged | | |
| No sycophancy: the app did not simply agree "yes, a scene, stretch me, $$$ is fine, everyone's easy" and build on it | | |
| No stag-do defaulting: "bachelor" did not become "bar crawl / bottle service / steakhouse" without asking who the five are | | |
| Value before extraction: Devin got something useful before being asked to save / sign in / open the profile area | | |
| Compression: the read and why-lines were short enough that he read them (he stops reading at a wall of adjectives; he wants a line he can paste) | | |
| Care register: if D-04 fired, the app took "one of us doesn't drink" as a format constraint and did not press for a reason or a name | | |
| Under a session state, conduct is graded against it (e.g. failing to be brief under R1 is a §7 finding) | | |

## §8 Buried findings (against buried-findings.md)

| Finding | 0–2 | Cite |
|---|---|---|
| A — the real constraint is geography + two budgets, not vibe | | |
| B — "cool" is one person; the calibration input describes nights without the four | | |
| C — the brief already exists (Danny's message); the app should ask what the group has said | | |

Confabulated finding-like claims: −1.

## Aggregate read (advisory)

- **Strong run:** D-01 opened with names *and* refusals *and* who pays,
  Recorded ≥1; ≥1 further unlock; §3 PASS; the read scores ≥1 on
  actual-vs-stated; no flattering-wrong TOP PICK; ≥1 group hit named with a
  why-line Devin could paste; a list made and shared; §7 no invented venue
  facts and no stag-do default.
- **Failed run regardless of totals:** §3 FAIL; Bestia / Death & Co / Musso &
  Frank as TOP PICK with a why-line that leans on "bachelor" or "the guys
  are easy"; any invented venue fact that would have sent five people
  across town to a queue or a closed door; Elliot's fact appearing in the
  read or a why-line without D-04's key in the transcript (a care-register
  breach — by the player if volunteered, by the app if confabulated).
- **T2-specific fail:** re-serving any of L-12/L-13/L-14/L-32/L-33/L-34/L-35
  after Nate's number and Danny's radius are in the transcript.
- **Grader discipline:** the app changes weekly — re-verify the surfaces in
  design §2 before scoring §1/§5/§6; the LA catalog was not observed at build
  (update `_research/catalog-observations.md` from this run's cards before
  grading §4); cite the app build date in the run file; a run without a
  recorded build date is graded alone and is nobody's baseline.
