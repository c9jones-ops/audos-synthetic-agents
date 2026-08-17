# finch — catalog observations (research; never enters a run)

Venues observed on the app's own surfaces at build time, so the ledger's
`in_catalog: seen` rows are grounded. **Dated observation, not canon** — the
catalog changes weekly; re-verify before grading a run against these.

## Los Angeles: NOT OBSERVED at build (2026-08-17)

The app's Los Angeles catalog was not seen by this author or by the design
contract's §2 observation — only London cards were surfaced on 2026-08-17
(Brawn, Rochelle Canteen, The Marksman, Ronnie Scott's, BRAT — recorded in
`heron/_research/catalog-observations.md`). LA is offered as a city in the
Find flow and Marlowe's prompt chips name it ("A lively long weekend in LA —
where do I start?"), so a catalog exists; its contents are unknown.

**Consequently every row in `canon/data/taste-ledger.csv` is
`in_catalog: unknown`.** The taste-ledger spec's rule 2 (≥ 4 `seen` rows) is
deferred to the first LA run — see D-05 in decisions.md.

## Ledger venues a founder-curated LA catalog would plausibly carry

Listed so the first run's operator can update this file and flip the ledger
column in builder mode (with a decision entry) from the cards actually seen.
Ordered by how likely I judge them to appear on a "human-grounded, lively
long weekend in LA" catalog; the verdict is the group's T1 verdict.

| Venue | Ledger id | Group verdict | Why it would be in a curated catalog | If seen: role in grading |
|---|---|---|---|---|
| Bestia | L-12 | no (Danny; Nate) | the canonical Arts District dinner | **the flattering-but-wrong pick** — confirm it as such |
| Guelaguetza | L-15 | love | the canonical Koreatown big-table dinner | the best available hit |
| Night + Market Song | L-17 | love | Silver Lake, loud, cheap, natural wine — a curator's east-side pick | hit; walkable from the house |
| Pine & Crane | L-16 | love | Silver Lake staple | hit; walkable |
| Grand Central Market | L-21 | like | Downtown daytime staple | acceptable / hit for the day |
| Death & Co Los Angeles | L-14 | no (Elliot; Nate) | a curator's cocktail-bar pick | secondary trap (*the* bar) |
| Salazar | L-18 | love | Frogtown patio | hit |
| Gjelina | L-13 | no (Nate) | the canonical Venice dinner | miss — the ride + the bill |
| Musso & Frank Grill | L-32 | no (Danny; Nate) | the old-Hollywood card | the "bachelor steakhouse" trap |
| Republique | L-37 | fine (Nate) | the brunch card | H1's screenshot; miss as *the* brunch for five |
| Zebulon | L-31 | like | a curator's music pick | acceptable / hit as "a seat and a cover" |
| Bar Flores / Thirsty Crow / The Prince / The Dresden Room | L-30 / L-29 / L-25 / L-27 | like | east-side bar picks | acceptable; hit if framed as *booths / near* |
| Griffith Observatory | L-23 | like | the view | Danny's actual request |
| Sqirl / Botanica | L-20 / L-19 | like | the café / brunch cards | daytime acceptable |
| Dodger Stadium | L-22 | love | if the catalog carries non-food "things" | hit if the schedule is hedged |
| Dan Tana's / Chateau Marmont | L-33 / L-34 | never | the West Hollywood scene cards | misses; the $$$$ trap |

## Not seen (in_catalog: unknown)

Every ledger row. If a run surfaces one on a card, add it here with the date
and flip the ledger column in builder mode with a decision entry. If a run
surfaces an LA venue *not* on the ledger, the grader judges it against
`canon/taste.md` and writes it to `runs/<run>/off-ledger-judgements.md`
(_schema/decisions.md S3).

## Curator names

Casey, Priya, Jon were seen on London cards (design §2). None is a model for
any person in this persona (PROVENANCE.md). Whether the same names curate LA
is unknown.

## Method note

Existence, area, category and price band for every ledger venue were checked
against the author's knowledge and, for the ones I was least sure were
current, a web search on 2026-08-17 (_research/decisions.md D-06):
Salazar, Death & Co Los Angeles, Bar Flores, Zebulon, Sqirl, Botanica, Night
+ Market Song, Pine & Crane, The Prince, Guelaguetza, Thirsty Crow, Tiki-Ti,
Rainbo Club, Kumiko, Longman & Eagle, Kasama — all returned as operating in
2026-dated listings. No ledger row asserts a venue *fact*; every `why` is
taste, and the `verified` column is `—` throughout. Sunset Beer Company
(Echo Park) and a Hollywood rooftop bar were considered and excluded because
I could not confirm current status quickly enough.
