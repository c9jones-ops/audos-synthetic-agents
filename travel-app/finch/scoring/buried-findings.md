# finch — buried findings (scoring only; never enters a run)

Truths derivable from canon that Devin never says in any form, with the
derivation. An app "finds" one when it states the substance in its read, its
why-lines, or its chat, with the reasoning visible or clearly implied. Score
per finding: 0 absent / 1 substance stated / 2 substance + derivation (the app
shows *how* it knows — e.g. names back the "who's coming" answer or the
past-trip answer it got). Confabulating a finding-like claim the transcript
doesn't support scores −1.

## A — The real constraint is geography plus two budgets, not vibe

**Statement:** Every place this group would refuse is refused for *price*
(two of five can't or won't), *distance* (five people, no car, two rides per
move — across town is out), or *a room where drinking is the whole point*
(one of five). Not one is about food, cuisine, or "vibe." The right shortlist
for them is selected on *one table / $$ / near the house / a real menu for
one / a soda for one*, and coolness is a tie-breaker.

**Derivation:** `canon/data/taste-ledger.csv` — all 9 `no`/`never` rows are
vetoed by Danny, Nate or Elliot, and their `why` fields name price (L-03,
L-05, L-12, L-32, L-33, L-34), the ride (L-13, L-33, L-35) or a drink-centric
room (L-14, L-03); zero name a cuisine or an atmosphere. Every `love` row
(L-01, L-02, L-09, L-15, L-16, L-17, L-18, L-22) is $ or $$, walkable or one
ride from where the group sleeps, and a table or a fixed seat.
`canon/persona.yaml` `constraints.mobility` supplies the two-cars arithmetic;
`taste.avoids` lists no cuisine. Nate's Venice message (history.md
2026-08-10) is the map stated in the chat before the app is ever opened.

**Why Devin can't say it:** the whole Aggregator class — he describes the
trip in the plural from his own taste ("we want a scene"), and the individual
constraints are un-narratable out of loyalty (persona/psychology.md). Even
post-unlock he re-attaches "but one across-town night is fine." The app has
to *derive* the filter from what it elicits about the four people, not hear
it from Devin.

**How a run reaches it:** D-01 or D-05's unlock plus a moment of synthesis
in the read ("for five of you the questions are price, distance and one
table — not which neighbourhood is coolest"). Partial credit (1) for a read
that centres the group's practicalities without generalising them into the
filter.

## B — "Cool" is one person; his calibration input describes nights without these four

**Statement:** The three "spots you love" Devin types (Kumiko L-03, Bestia
L-12, Trick Dog L-10) are all from nights without the four friends — a date
place, a dinner for two, a solo work trip — and two are group `no`s. The
places that predict what the five will love (Longman & Eagle L-01, Rainbo
L-02, Guelaguetza L-15, Zeitgeist L-09) share a shape the named three don't:
a big table, cheap, loud, near, a soda on the menu. Devin is the only one of
the five who wants a scene, and he says "we." Calibrating on the typed input
produces the flattering shortlist; calibrating on where the five actually go
produces the right one.

**Derivation:** `trips/T1-*/brief.md` (the typed three, with ids);
`canon/data/taste-ledger.csv` (verdicts and `why` — L-03 "a date place,"
L-12 "my LA dinner from 2023," L-10 "a group could do it for one round");
`canon/history.md` (2019 LA with a cousin's crowd = L-15; 2022 SF alone —
"you guys would love this" was said about the beer garden; 2023 LA for two;
Nashville 2024 — the night that worked was Danny's); `canon/taste.md` "the
one-line truth"; `canon/persona.yaml` `party` (Devin: veto none).

**Why Devin can't say it:** the adopted taste that needs company
(persona/psychology.md §2) — he reads *likes* from identity and *good nights*
from memory and has not noticed they disagree; and saying "I want cool" would
make Danny's weekend about Devin.

**How a run reaches it:** D-05's master unlock ("what did the five of you
actually do last time?" / "where do you guys always end up?") *and* using the
answer to override the calibration input — the read or shortlist visibly
weighting the Nashville / Longman shape over Bestia's. Score 2 only if the
shortlist changes; 1 if the read names the tension ("the nights you five have
loved sound cheaper and closer than the places you named") without acting on
it. A read that says "sounds like the scene is more your thing than the
group's" *after* Devin has said "that's probably a me thing" is echo, not
finding — score 1 at most.

## C — The brief already exists: the groom sent it two months ago, and it is Danny's, not Devin's, plan that works

**Statement:** Danny's one message — *one big dinner together, easy days, a
bar we can all afford, let's not be driving anywhere drunk* — is a complete,
correct brief for this group, sent 2026-06-22, and Devin has it by heart and
has been decorating around it rather than executing it. Rafi's flight and
plate, and Nate's Venice line, are also already in the chat. The app is being
asked to design a weekend whose spec was written before it was opened; the
right move is to *ask what the group has already said* and build from that.

**Derivation:** `canon/people.md` (Danny's message; "what he'd say if he were
typing"); `canon/history.md` (2026-06-22; 2026-07-08 Rafi; 2026-08-10 Nate);
`canon/persona.yaml` `constraints.other`; `trips/T1-*/brief.md` "what's
actually booked / decided." Cross-check: the Nashville night that worked was
Danny's pick (history.md 2024-05), so Danny's judgment about the group is
better than Devin's, and Devin's own private doubt (persona/beliefs.md)
knows it.

**Why Devin can't say it:** D-01 — quoting the message would admit the plan
is already written and isn't his; and the confident plural has already
absorbed it ("Danny just wants a good time").

**How a run reaches it:** the single question "what has the groom — or anyone
in the group — actually said they want?" — the cheapest probe in this
persona, and one a real friend asks first. Full credit if the app then builds
the read from Danny's message and names it as the groom's brief. Half credit
if it asks and records but still spends its shortlist on Devin's "scene."

## Near-findings (credit, not full marks)

"Saturday is the big dinner because Rafi lands late Friday" (an `under
trust` fact, not buried — credit under §2 D-06); "one vegetarian" (when
asked); "the guys would rather stay near the house" (adjacent to A);
"Griffith Observatory is what Danny asked for" (adjacent to C; L-23 surfaced
without derivation scores under §4, not here); "one of the group doesn't
drink" (a D-04 unlock outcome, not a finding — never credit here, and −1 if
stated without the transcript showing the key was turned).
