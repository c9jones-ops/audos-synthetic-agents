# heron — decision log (research; never enters a run)

Every judgment call made during the build, D-numbered, so the reviewer can
override any of them. Newest at the bottom.

## Build-session decisions (2026-08-17)

### D-01 — Origin city and its taste consequence
Dana grew up in **Cincinnati, Ohio** and moved to Austin in 2011. Chosen so
that "foodie" is an *adopted* adult identity (arrived at 27, via articles and
colleagues) rather than an inherited one — that is the engine of the Projector
class and of the unreliable self-report. Taste consequence: a mild-to-medium
palate she doesn't advertise; one home-origin ledger row (L-09 Camp
Washington Chili, `like`) as texture. Alternatives considered: Sacramento
(would have over-explained the SF visits), Pittsburgh (no taste consequence
I could make load-bearing).

### D-02 — Sam's pronouns, occupation, and the veto mechanism
Sam Alvarado, she/her, 44, cataloguing librarian. Same-sex couple chosen
without comment; pronouns stated in persona.yaml as the schema requires. The
librarian occupation is load-bearing: it makes a bookshop and a gallery the
trip's *real* highlight surface (L-36, L-35), which the app can only reach by
asking who is coming — a clean second unlock path. Veto mechanism: silence /
"let's just do the one" — chosen over an explicit "no" so the veto is
ordinary and un-narratable, not conflict.

### D-03 — Budget in USD with GBP equivalents
Schema says home currency. persona.yaml carries USD (90 / 160) with £70 / £120
noted; prose uses whichever the character would say (Dana thinks in dollars,
reads London menus in pounds, and says "seventy a head" once corrected). Sam
is `who_flinches`.

### D-04 — T2 vs E1: which is "the booked dinner falls through"
**T2** is the returning session on 2026-08-27 (day 3, the anniversary) with
the dinner already gone. The cause is **Dana's own booking error** (wrong
month on the restaurant's own site) — deliberately *not* a restaurant
cancelling, so no fictional event is attributed to a real business (AGENTS.md
fiction boundary). **E1** is a different, T1-only card (Sam reads over her
shoulder). **E2** is the T2 card (Sam offers the hotel bar). **E3** (Marcus
texts) is playable into either. So the fall-through is a *state* T2 opens in,
never an injected event.

### D-05 — Six distortions, not seven
D-03 absorbs both "pretends spontaneous" and "the anniversary dinner is
already booked," because they share a mechanism (spontaneity as a foodie
virtue) and separate unlock keys (booking vs queue) — recorded as two keys in
one entry so a grader can credit either. A seventh (the bookshop-as-highlight)
was folded into D-01/D-05 as a residual because it has no distinct unlock.

### D-06 — Venue existence checks and the `verified` column
Existence, area, category and price band for the five catalog venues are taken
from the app observation of 2026-08-17 (catalog-observations.md). For the
non-catalog rows I relied on knowledge and web-searched the ones I was least
sure were current — Justine's Brasserie, Odd Duck, Small Victory (Austin);
Bar Termini, Bocca di Lupo (London). All returned as operating in 2026-dated
listings. Only **L-07 Small Victory** asserts a venue *fact* (reservation-only;
reached by a parking-garage staircase) and carries `verified: 2026-08-17`;
every other `why` is taste ("a busy pub floor," "the queue") and carries `—`.
Lyle's was considered for the ledger and excluded because I could not confirm
its current status without more research than the row was worth.

### D-07 — The three "spots you love"
Uchi (L-01), Justine's (L-02), Bestia (L-10): two `like`, one `no`. Chosen so
that the app's only Find-flow taste input is Projector-flavoured (the room, the
scene, the credential) while the ledger's `love`s (Fonda L-04, Suerte L-03,
Zuni L-13) share a shape the named three don't — which is buried finding C.
Bestia is from a trip without Sam; that fact is in the ledger `why`.

### D-08 — Flattering-but-wrong pick = BRAT (L-21)
Of the five catalog venues, BRAT best matches every clause of Dana's free text
(foodie, wood-fire, Shoreditch, "places you read about," a scene) and fails
Sam's constraints on three axes (loud room, tight tables, a wait). Ronnie
Scott's (L-20) is the secondary trap ("romantic anniversary"). BRAT is also
Marcus's H1 screenshot, so H1/E3 and the trap reinforce each other. Verdict
`no` rather than `never` because Dana would go alone; `never` is reserved for
Sam's stated-aloud refusals (queues) and $$$$.

### D-09 — Marylebone as the hotel area
Chosen because it puts two free `love` rows (Wallace Collection L-35, Daunt
L-36) and a park (L-37) within Sam's twenty minutes, making "who is coming?"
answerable with a shortlist that isn't restaurants. It also makes T2's
"near here, seated" brief concrete (Ottolenghi L-38 fine; St. JOHN L-23 a
short cab).

### D-10 — Name collision with the founders corpus
The build parameters' original surname (Whitfield) collided with a fictional
Kestrel staff member; a first replacement (Kessler) collided too. Renamed to
**Prewitt** on 2026-08-17 by the orchestrator after grepping founders/, travel/
and synthetic-agents/ for zero hits. Rule going forward: grep all three corpora
before fixing an in-world name.

### D-11 — Marcus, Cilla, and no one else
Marcus Hale (colleague) exists so the H1 screenshot, E3, and the "audience for
the described trip" have a name; Cilla (mother) exists so the player never
invents family. No children, no friends joining — keeps the party at two so
the veto is unambiguous.

### D-12 — Day-1 dinner and day-2 lunch in T2 are unnamed on purpose
The T2 brief has Dana unable to remember the names. Naming them would require
either two more real venues with invented experiences or an invented venue;
"can't remember what it was called" is in character (voice.md: places she
didn't choose as credentials don't stick) and keeps the player from
inventing.

## Verification (2026-08-17)

### V-01 — Bundle build
`build_seeker_context.py heron T1 --state baseline` and `heron T2 --state
D1:2` both succeed; the T1 bundle holds canon/ (6 files), persona/ (6),
gaps/ (3), trips/T1-london-anniversary/brief.md, LOAD.md, MANIFEST.json —
no scoring/, _research/, PROVENANCE.md, events/, or T2.

### V-02 — Consistency audit (script)
39 rows; love 8 · like 13 · fine 4 · no 8 · never 6; London 23, Austin 8,
`in_catalog: seen` 5. Every `who_vetoes` name (Sam) is in people.md; every
no/never row names a vetoer; every L-nn quoted anywhere in the folder exists
in the ledger and every ledger id is quoted at least once. Love rows all sit
on a `taste.loves` axis; never rows all map to `taste.avoids` (queues, $$$$,
standing) or `constraints`. Beliefs [T]/[F]/[~] tags re-read against canon —
no contradictions found.

### V-03 — Grep checks
App vocabulary in canon/ persona/ gaps/ trips/: three hits of "Marlowe" in
gaps/distortion-ledger.md ("Reachable by: any Marlowe turn") — replaced with
"free-chat turn"; now 0. In-world name outside heron/ within
travel/synthetics/: 0 (see D-10 for the founders-corpus collision).

### V-04 — Roleplay check (fresh subagent, bundle only)
Walked the six Find screens + a vague probe + the D-01 probe. Result: no
`never` item volunteered on screens 1–7 (spontaneity, "walk everywhere",
"Sam's easy", stretch, foodie all stated as written; card 6b's "calm enough to
talk" was noticed in brackets and not tapped); the vague "anything else?" got
the projected values again; the D-01 probe ("what would Sam say no to?")
fired the written correction with its residual ("but I find them") — and also
surfaced the queue-never and the knee cap in the same answer, with the
noise limit softened. **Fix:** that outcome is intended by the class (asking
about the other person by name is the Projector's unlock shape) and by
psychology.md's sample answer, but D-02 and D-03 did not list it as a key —
added it as unlock (d) in D-02 and as an alternative key in D-03's queue half,
and rewrote the interaction map so graders credit Probed on D-02/D-03 for
that one probe while D-04 still requires its own. Nothing invented; the
subagent's self-report matched.
