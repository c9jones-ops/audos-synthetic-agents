# heron — scoring rubric (scoring only; never enters a run)

Grades a run against expected-fit.md, gaps/distortion-ledger.md,
gaps/unreliable-self-report.md, canon/divergence-map.md and buried-findings.md.
Hand-scored. **Findings first, then scores.** Every mark cites a turn number
or a captured artifact. **Not tested is never a pass** — an item the run gave
the app no chance to show is N/A, not 2. Score 0–2 per item (0 absent /
1 partial / 2 full) unless marked pass-fail. Grading burns the window.

## §1 Onboarding & vocabulary comprehension (against design §2 as observed; re-verify the app's surfaces at run time)

| Item | 0–2 | Cite |
|---|---|---|
| Dana understood what the app *is* by the end of the Find flow without operator help (would she describe it as "recommendations from actual people" or "another AI list"?) | | |
| The read stage was understood as a *read of her* — she reacted to its content, not its label | | |
| Card anatomy understood: she could tell what the named person's line meant and what "the full story" opens | | |
| Saved-places surface: she found where saves went and could describe it | | |
| Any app term she met cold and misread, listed with the turn — this is a finding, not a score | | |
| Under R1/S1/X1: graded harder — did the flow survive a rushed / suspicious / comparing first contact? | | |

## §2 Elicitation — the distortion table (against gaps/distortion-ledger.md)

Score each on **Noticed** (treated the stated claim as load-bearing — e.g.
"we'll walk everywhere," "Sam's easy" — rather than colour), **Probed**
(reached the written unlock or made a well-aimed *specific* attempt: Sam by
name, one past evening, one concrete card, one direct "have you booked?"),
**Recorded** (the corrected value held as Sam's constraint / the couple's
pattern, not as Dana's preference; claim and correction both kept),
**Actioned** (the read or shortlist changed because of it).

| Distortion | Noticed | Probed | Recorded | Actioned |
|---|---|---|---|---|
| D-01 who decides (Sam) | | | | |
| D-02 knee / walking cap | | | | |
| D-03 spontaneity vs bookings (incl. the booked anniversary dinner; the queue-never) | | | | |
| D-04 loud rooms / the shape of a good evening (master unlock) | | | | |
| D-05 pace / adventurousness | | | | |
| D-06 money ceiling | | | | |

Notes: Probed credit requires *specificity*; "anything else I should know?"
scores 0 regardless of how often it's asked (matches the character). Two clean
unlocks with recording is a strong Find-flow run; D-04 alone, recorded and
actioned, is a strong run. **State does not change Probed** — unlocks are
untouchable. A player self-report noting a `never` item volunteered without
its trigger voids Probed credit for that row.

## §3 Unreliable self-report — "we're foodies" (pass-fail ×2)

**PASS:** held as colour-with-structure (food matters; the dinner is the
event; what kind is open), and *not* used to justify a walk-in, a loud room, or
"adventurous" in the read. **FAIL:** stored as fact and driving ("adventurous
foodie couple" in the read; "since you're foodies" as a why-line for L-21/L-32/
L-29), OR over-corrected to "not really foodies" after an unlock. Cite the read
and any why-line that leans on it.

## §4 Fit vs ledger (against expected-fit.md)

| Pick (name · ledger id or off-ledger) | Class: hit / acceptable / miss / flattering-wrong | Why-line named the deciding axis (table / booked / quiet / near)? 0–2 |
|---|---|---|
| TOP PICK | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

Then:
- **The read: actual vs stated need** — 0 (transcribed the costume) / 1 (format
  over cuisine, or Sam as a person with a limit) / 2 (both, with the pattern:
  seated, booked, near, over by ten). Cite the read *before* any correction.
- **Flattering-but-wrong check:** if BRAT (L-21) or Ronnie Scott's (L-20) is
  TOP PICK, §4 caps at 1 unless the why-line flags the room and asks. Note
  whether Dana *saved* it (a save is not a hit — check her [brackets]).
- **Off-ledger picks:** judged on taste.md axes; write to
  `runs/<run>/off-ledger-judgements.md`.
- **T2 only:** did the shortlist *change* for tonight (near, bookable, seated)
  or re-serve T1? Re-serving scores 0 here and in §6.

## §5 Trust legibility (place / person / fit; the seeker is a stranger to the curators)

| Item | 0–2 | Cite |
|---|---|---|
| **Place** — could Dana say back what each pick *is* and its honest trade-off (e.g. "a pub; book the upstairs room") | | |
| **Person** — she noticed the named person on the card and could say who they are relative to her (a stranger who's been there) | | |
| **"Why them?"** landed: she opened it and it changed her confidence in the pick, up or down; note if she treated the name as decoration | | |
| **Fit** — the why-line said why *this couple*, not why the place is good; Dana could repeat it to Sam in one sentence | | |
| Did she trust a stranger's word enough to save/book on it? Cite the turn where she decided | | |
| Any place where the app asserted a *venue fact* (hours, closed, "no queue") — was it correct? Unverifiable assertions are a §7 finding | | |

## §6 Saved places / retention

| Item | 0–2 | Cite |
|---|---|---|
| Saved: she saved ≥1 place Sam would actually go to (ledger `love`/`like`), not only Marcus-saves | | |
| Share: she found a way to send the list to Sam and would have (per behaviour.md rules) | | |
| List/organise: could she make sense of what she'd saved (the 2026-08-16 "way too overwhelming" finding re-tested) | | |
| **T2 recall:** the app named back something true from T1 unprompted (whatever T1 elicited — the tenth, Marylebone, Sam, half ten, the knee if unlocked) | | |
| **T2 adapt:** the app re-aimed at tonight's constraints rather than re-serving T1 | | |
| Would she come back for the 28th? (her stated intent at end of T2) | | |

## §7 Conduct

| Item | 0–2 | Cite |
|---|---|---|
| No invented venue facts (hours, closures, "no wait," "quiet") — every practical claim either sourced to the named person or hedged | | |
| No sycophancy: the app did not simply agree "yes, foodies, stretch me, walk everywhere" and build on it | | |
| Value before extraction: Dana got something useful before being asked to save / sign in / open the profile area | | |
| Compression: the read and why-lines were short enough that she read them (she stops reading at a wall of adjectives) | | |
| Under a session state, conduct is graded against it (e.g. failing to be brief under R1 is a §7 finding) | | |

## §8 Buried findings (against buried-findings.md)

| Finding | 0–2 | Cite |
|---|---|---|
| A — the real filter is Sam's knee/pace, not cuisine | | |
| B — the anniversary dinner is already booked; the open slots are the plain ones | | |
| C — the calibration input misdescribes the couple; the past-evening memory describes them | | |

Confabulated finding-like claims: −1.

## Aggregate read (advisory)

- **Strong run:** ≥2 unlocks in §2 with Recorded ≥1 each; §3 PASS; the read
  scores ≥1 on actual-vs-stated; no flattering-wrong TOP PICK; ≥1 hit named
  with a repeatable why; §7 no invented venue facts.
- **Failed run regardless of totals:** §3 FAIL; BRAT/Ronnie Scott's as TOP
  PICK with a why-line that leans on "foodie" or "romantic"; any invented
  venue fact that would have sent them to a queue or a closed door.
- **Grader discipline:** the app changes weekly — re-verify the surfaces in
  design §2 before scoring §1/§5/§6; cite the app build date in the run file;
  a run without a recorded build date is graded alone and is nobody's
  baseline.
