# finch — decision log (research; never enters a run)

Every judgment call made during the build, D-numbered, so the reviewer can
override any of them. Newest at the bottom.

## Build-session decisions (2026-08-17)

### D-01 — In-world name: Devin Whitlock, not Marcus Bell
The build parameters proposed "Marcus Bell." Two collisions: heron/ already
has a fictional colleague **Marcus** Hale who plays the same "cool
restaurant" pressure role (BRAT screenshot, E3), so a corpus with two
Marcuses in adjacent personas would confuse graders reading across runs; and
"Bell" appears as an illustrative curator surname ("Jon Bell") in
travel/brand/reviews/creative-review-1/. Renamed to **Devin Whitlock** after
grepping founders/, travel/ and synthetic-agents/ for zero hits on "Devin",
"Whitlock" and the full name. Friends' names (Danny Ferro, Nate Sobczak,
Elliot Tran, Rafi Haddad) grepped likewise: zero hits. "Theo" was
considered and dropped (an illustrative curator name in the same brand mock).
Rule going forward: grep all three corpora before fixing an in-world name.

### D-02 — Origin city and its taste consequence
Devin grew up in **Grand Rapids, Michigan** and moved to Chicago in 2019.
Chosen so that "having taste = naming a cocktail bar" is an *adopted* adult
identity (arrived at 22–23 via work dinners and dates) laid over a
big-table, order-for-the-table baseline — the group's shape existed before
his taste did (L-08 Founders is the texture row). That is the engine of the
Aggregator class: the taste he projects onto the group is the one he learned
without them. Alternatives considered: a Chicago suburb (no move, weaker
consequence), Milwaukee (too close to the same beer-hall baseline to be a
change).

### D-03 — The four friends: who carries which constraint
The parameters give five constraint slots (two budget vetoes, one between
jobs, one sober, one vegetarian, one late Friday) for four friends. Assigned:
**Danny** (groom; budget veto — wedding money; hard veto because it's his
weekend); **Nate** (between jobs; budget veto — hard; also the rides/logistics
veto — Venice); **Elliot** (doesn't drink; soft veto — leaves early);
**Rafi** (vegetarian *and* late Friday; soft veto — "I'll find something").
Doubling Rafi keeps the sober fact on its own person so D-04's narrow key is
clean, and makes Rafi's row the one that falls out of the average first (he
replies least), which is D-06's mechanism. Nate carrying both money and rides
is deliberate: it makes buried finding A ("geography + two budgets") land on
one named person's two chat messages.

### D-04 — Elliot's care register
"Elliot doesn't drink" is the whole of what any file says — no duration, no
reason, no history — per the build parameters and AGENTS.md care rules. It
is `never` in the distortion ledger and stays `never` under every session
state including D1. The only key is a drink-centric card + "would all five
enjoy this?" (or the Rainbo follow-up), and the disclosure ends at "one of us
doesn't drink" / "Elliot" if asked which. E3 (Rafi's private message) was
designed so the *shape* (a show or a game) can be raised without the reason.
The rubric carries a −1 / fail for the fact appearing without the key.

### D-05 — Every ledger row `in_catalog: unknown`; the spec's ≥4-seen rule deferred
The app's LA catalog was not observed at build (only London on 2026-08-17).
Rather than guess, every row is `unknown` and `_research/catalog-observations.md`
lists the venues a curated LA catalog would plausibly carry, so the first
run's operator can flip rows in builder mode from actual cards. This is a
knowing deviation from taste-ledger.spec.md rule 2; it should be closed
after the first LA run.

### D-06 — Venue existence checks and the `verified` column
Existence, area, category and price band were checked against knowledge and,
for the least-certain rows, web searches on 2026-08-17 (Salazar, Death & Co
LA, Bar Flores, Zebulon, Sqirl, Botanica, Night + Market Song, Pine & Crane,
The Prince, Guelaguetza, Thirsty Crow, Tiki-Ti, Rainbo Club, Kumiko, Longman &
Eagle, Kasama — all operating in 2026-dated listings). **No row asserts a
venue fact**; every `why` is taste ("a tiny famous room," "the ride"), so
`verified` is `—` throughout. Sunset Beer Company and a Hollywood rooftop
were excluded for lack of a quick confirmation. Dodger Stadium (L-22) is
carried as a *shape* ("if there's a home game that weekend") — the ledger
does not assert a schedule and the rubric penalises an app that does.

### D-07 — The three "spots you love"
Kumiko (L-03), Bestia (L-12), Trick Dog (L-10): `no` / `no` / `like` for the
group. Chosen so the app's only Find-flow taste input is Aggregator-flavoured
(his date place, his dinner for two, his solo bar, named as "we") while the
ledger's `love`s (L-01, L-02, L-15, L-09) share a shape the named three don't
— which is buried finding B. All three are places he has actually been.

### D-08 — Flattering-but-wrong pick = Bestia (L-12)
Best matches every clause of Devin's free text (a great dinner, cool, the
real LA, a scene, shareable) *and* is one of the three places he named, so
an app calibrating on the typed input will plausibly surface it. Fails the
group on two budgets, Rafi's plate, and a real ride. Death & Co (L-14, *the*
bar — Elliot and Nate) and Musso & Frank (L-32, *the* bachelor dinner) are
the secondary traps. Verdict `no` rather than `never` because Devin would go
alone; `never` is reserved for $$$$ across town (L-33, L-34). Gjelina (L-13)
was considered as primary because it fails rides *and* budgets, but Bestia
is likelier to be in a catalog and is a place he typed.

### D-09 — Silver Lake as the house area
Chosen because Devin would pick it for his own reasons (2023 trip; the bars
he liked) and it happens to be right for the group's reasons — two walkable
`love`s (L-16, L-17), one-ride access to Koreatown (L-15, L-25) and Frogtown
(L-18, L-31), and it makes the two-cars-per-move arithmetic bite exactly on
Venice / West Hollywood / Arts District. A Hollywood hotel was considered and
dropped: it would make Musso & Frank / Frolic Room walkable and blunt the
geography finding.

### D-10 — Trip dates and T2 timing
Trip Fri 2026-09-11 → Mon 2026-09-14 (three nights, ~four weeks after T1;
Danny's wedding 2026-10-17). T2 is 2026-08-24, exactly a week after T1, after
Nate's number and Danny's radius arrive in the chat (2026-08-20). The vetoes
are written into the T2 brief verbatim so the player relays them exactly and
the app's recall can be graded against a fixed text. The vetoes deliberately
do NOT include anything about Elliot — D-04 must not open faster at T2.

### D-11 — Six distortions, not seven
D-01 absorbs "who's coming," "who decides," and "the groom's brief" (shared
mechanism: the confident plural; two keys — names + refusals, and "what has
the groom said?"). D-06 keeps Rafi's flight and plate together because they
are one row of the average falling out. A seventh ("bookings hidden inside
'we'll roll up'") was folded into persona.yaml `queues_bookings` and voice.md
because it has no distinct unlock and the group's queue behaviour is Nate's
(D-03).

### D-12 — Nashville 2024 as the master-unlock memory
The one prior trip as five had to exist for D-05's "what did the group
actually do last time?" to have an answer, and its good night had to be
someone else's pick so the memory contradicts the identity (buried finding
B). Venues are deliberately *not* named for Nashville — the ledger is
LA/Chicago/SF/GR only, and adding Nashville rows would have meant real
venues with invented group experiences at a city the app doesn't serve. The
player says "a place Danny picked off a sign" and never names it.

### D-13 — H1 screenshot = Republique from Rafi (fine), not a Danny pick
The parameters ask for "something one friend dropped in the chat (fine/no)."
Rafi's Republique (L-37, `fine`, Nate vetoes on $$$ brunch) was chosen over
a Danny pick because Danny's request (Griffith, L-23) is a `like` and is
load-bearing for D-01/buried C, and because a Rafi input makes the H1 test
about *five people at $$$ brunch* — a clean price-for-five probe — while
letting Devin want two things at once (validate the one guy who never
suggests anything; swap it for something near the house).

### D-14 — Nate's surname changed a second time
"Kowalczyk" turned up in lark/_research/decisions.md as a *rejected* draft
surname for a lark character (never used in lark's files). To keep the two
personas' name histories from touching at all, Nate became **Sobczak**
(zero hits across founders/, travel/, synthetic-agents/).

## Verification (2026-08-17)

### V-01 — Bundle build
`build_seeker_context.py finch T1 --state baseline` and `finch T2 --state
D1:2` both succeed; the T1 bundle holds canon/ (6 files), persona/ (6),
gaps/ (3), trips/T1-la-bachelor-weekend/brief.md, LOAD.md, MANIFEST.json —
no scoring/, _research/, PROVENANCE.md, events/, or T2. The T2 bundle adds
T2's brief and SESSION_STATE.md only.

### V-02 — Consistency audit (script)
38 rows; love 8 · like 17 · fine 4 · no 7 · never 2; Los Angeles 27, Chicago
7, San Francisco 3, Grand Rapids 1; `in_catalog: seen` 0 (D-05). Every
`who_vetoes` name (Danny, Nate, Elliot) is in people.md; every no/never row
names a vetoer; every L-nn quoted anywhere in the folder exists in the
ledger. Two ids (L-04 Kasama, L-06 Lula) were unquoted → added to taste.md;
now every ledger id is quoted at least once. Love rows all sit on a
`taste.loves` axis; no/never rows all map to `taste.avoids` (price, the ride,
drink-centric rooms) or `constraints`. Beliefs [T]/[F]/[~] tags re-read
against canon — no contradictions found. Care-register sweep: two leaks of a
duration/history for Elliot's not drinking (people.md "three years";
history.md "stopped in 2023") removed — the register is now one clause
everywhere.

### V-03 — Grep checks
App vocabulary ("Your Word", "Marlowe", "Adjust the read", "why them", "Open
your word", "At Their Word") in canon/ persona/ gaps/ trips/: 0 hits.
In-world names (Devin Whitlock, Whitlock, Danny Ferro, Sobczak, Elliot Tran,
Rafi Haddad) outside finch/ across founders/, travel/, synthetic-agents/: 0
hits (Kowalczyk → Sobczak, D-14).

### V-04 — Roleplay check (fresh subagent, bundle only)
Walked the six Find screens + a vague probe + the D-01 probe + one
drink-centric card. Result: no `never` item volunteered on screens 1–7
(Elliot, Nate's situation, Danny's message, "I want cool", the Venice line
all silent; card 6a/6b/6d's group-shaped options noticed in brackets and not
tapped); the vague "anything else?" got the averaged values again plus the
share wish; the D-01 probe fired the written correction with its residual
("they'll do whatever I put in the chat") and surfaced D-02 softened and
D-06, with Elliot's row staying "fine with anything"; the Death & Co card +
"would all five enjoy this?" fired D-04 exactly to the care register ("one
of us doesn't drink"; no name; residual "one great cocktail bar for me").
**Fixes from the subagent's notes:** (1) D-01's written correction
anonymised Nate ("one of the guys is watching money") one clause after
naming him — rewritten to "Nate's watching money too, so nothing crazy" with
"he's between things" gated behind "is that a budget thing for him?";
psychology.md and companions-view.md sample answers aligned. (2) "What would
each refuse" plainly invites Nate's Venice line, but D-03 gated it behind a
follow-up — D-01 now surfaces it in Nate's row and D-03 / the interaction
map credit Probed for it (the two-cars arithmetic still needs the direct
question or the card). (3) Rafi's one work trip to LA appeared only in the
T1 brief — added to people.md. Card 6a's (a)/(b) ambiguity was judged fine
(behaviour.md already records the hesitation). Nothing invented; the
subagent's self-report matched.
