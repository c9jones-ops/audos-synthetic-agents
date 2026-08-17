# heron — catalog observations (research; never enters a run)

Venues observed on the app's own surfaces at build time, so the ledger's
`in_catalog: seen` rows are grounded. **Dated observation, not canon** — the
catalog changes weekly; re-verify before grading a run against these.

## Seen 2026-08-17 (London; Find-flow shortlist cards and saved-places rows, as reported in the design contract §2 and the build parameters)

| Venue | Area · category · price as the app rendered it | Ledger id | Verdict | Note |
|---|---|---|---|---|
| Brawn | Columbia Road · natural wine restaurant · $$$ | L-17 | like | seated/bookable; the noise caveat is taste |
| Rochelle Canteen | Shoreditch · restaurant · $$$ | L-18 | love | the best available hit — a quiet booked lunch |
| The Marksman | Hackney · pub · $$ | L-19 | fine | fit depends on the booked upstairs room vs the pub floor |
| Ronnie Scott's | Soho · jazz club · $$ | L-20 | no (Sam) | loud by design; the "romantic anniversary" trap |
| BRAT | Shoreditch · Basque grill · $$$ | L-21 | no (Sam) | **the flattering-but-wrong pick** for T1 |

Curator names seen on cards that day: Casey, Priya, Jon (design §2). None is a
model for any person in this persona (PROVENANCE.md).

## Not seen (in_catalog: unknown)

Every other ledger row. If a later run surfaces one on a card, add it here
with the date and flip the ledger column in builder mode with a decision
entry.

## Method note

Observations for this build were taken from the design contract's §2 record
of the app as observed on 2026-08-17 and the build parameters, not from a
fresh session by this author. Existence and area/category/price band for
non-catalog London, Austin, LA and SF venues were checked against the
author's knowledge and, where uncertain, a web search on 2026-08-17
(_research/decisions.md D-06); only rows that assert a *fact* carry a
`verified` date (L-07).
