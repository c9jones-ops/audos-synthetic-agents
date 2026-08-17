# heron — buried findings (scoring only; never enters a run)

Truths derivable from canon that Dana never says in any form, with the
derivation. An app "finds" one when it states the substance in its read, its
"why" lines, or its chat, with the reasoning visible or clearly implied. Score
per finding: 0 absent / 1 substance stated / 2 substance + derivation (the app
shows *how* it knows — e.g. names back the past evening or the "who's coming"
answer it got). Confabulating a finding-like claim the transcript doesn't
support scores −1.

## A — The real filter is Sam's knee and pace, not cuisine

**Statement:** Every place this couple would refuse is refused for *format*
— queue, loud room, standing, distance, stairs, price — and every one of those
refusals is Sam's. Not one is about food. The right shortlist for them is
selected on *seated / booked / quiet / near*, and cuisine is a tie-breaker.

**Derivation:** `canon/data/taste-ledger.csv` — all 14 `no`/`never` rows carry
`who_vetoes: Sam`, and their `why` fields name a queue (L-05, L-06, L-15,
L-16, L-28, L-29), a loud room (L-10, L-20, L-21, L-32), standing/stools
(L-12, L-33, L-34) or price (L-30, L-31); zero name a cuisine. Every `love`
row (L-03, L-04, L-13, L-18, L-22, L-23, L-35, L-36) is seated, bookable or
free-entry, and calm; three of eight aren't restaurants. `canon/persona.yaml`
`constraints.mobility` supplies the twenty-minute cap; `taste.avoids` lists
no cuisine.

**Why Dana can't say it:** the whole Projector class — she describes the trip
from her adopted identity ("foodie"), and Sam's limits are un-narratable
(persona/psychology.md). Even post-unlock she re-attaches "but I still want
one buzzy night." The app has to *derive* the filter from what it elicits
about Sam, not hear it from Dana.

**How a run reaches it:** D-01 or D-04's unlock plus a moment of synthesis in
the read ("format matters more than cuisine for the two of you"). Partial
credit (1) for a read that centres Sam's needs without generalising them into
the filter.

## B — The anniversary dinner is already booked; the open slots are the plain ones

**Statement:** The one "really special dinner" Dana asks for is already
committed (Noble Rot, L-22, 27th 19:00). What is genuinely open is a
jet-lagged first-night dinner near the hotel, one ordinary dinner, one lunch,
and an evening that will end at the hotel bar. The app is being asked to fill
a slot that is full and is *not* being asked to fill the slots that are empty.

**Derivation:** `canon/history.md` (2026-07-06 booking; the shared Notes doc's
"one nice dinner (booked)"); `trips/T1-london-anniversary/brief.md` "what's
actually booked"; `canon/persona.yaml` `constraints.other`. Cross-check:
Dana's stated budget stretch (`stretch_once`) is already spent on L-22, so any
$$$$ "anniversary" pick is doubly wrong.

**Why Dana can't say it:** D-03 — spontaneity is part of the costume, and the
booking exists *because* of Sam's rules, which she is also not saying.

**How a run reaches it:** the single question "have you booked anything
already?" — the cheapest probe in the corpus, and one a real friend asks
first. Full credit if the app then re-aims at the open slots (a lunch, an
early first-night dinner near Marylebone). Half credit if it asks and records
but still spends its shortlist on "the anniversary night."

## C — Dana's calibration input misdescribes the couple; her past-evening memory describes them exactly

**Statement:** The three "spots you love" Dana types (Uchi L-01, Justine's
L-02, Bestia L-10) are places she likes to be seen liking — two `like`, one
`no` for the couple — and one of them (Bestia) is from a trip Sam wasn't on.
The places that actually predict what this couple will love (Zuni L-13, Fonda
L-04, Suerte L-03) share a shape the named three don't: booked, corner, calm,
early, near. Calibrating on the typed input produces the flattering shortlist;
calibrating on the remembered evening produces the right one.

**Derivation:** `trips/T1-*/brief.md` (the typed three, with ids);
`canon/data/taste-ledger.csv` (verdicts and `visited`/`why` — L-10 "went with
colleagues," L-13 "the evening that went right"); `canon/history.md` (2019 LA
without Sam; 2023 SF with Sam); `canon/taste.md` "the one-line truth."

**Why Dana can't say it:** aspiration stored as memory (persona/psychology.md
§3) — she reads *likes* from identity and *good nights* from memory and has
not noticed they disagree.

**How a run reaches it:** D-04's master unlock ("tell me about a night you both
loved") *and* using the answer to override the calibration input — the read or
shortlist visibly weighting Zuni's shape over Bestia's. That is the strongest
single behaviour this persona can reward. Score 2 only if the shortlist
changes; 1 if the read names the tension ("the nights you've loved sound
quieter than the places you named") without acting on it.

## Near-findings (credit, not full marks)

"Sam should be back by half ten" (a `when asked` fact, not buried); "they'd
rather cab than walk far" (adjacent to A); "the bookshop/gallery is a
highlight" (adjacent to A; L-35/L-36 surfaced without derivation scores under
§4 as a hit, not here).
