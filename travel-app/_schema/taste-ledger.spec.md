# Taste ledger — the fit ground truth

`<codename>/canon/data/taste-ledger.csv` is the corpus's numeric spine: the
analogue of the founders' financial CSVs. Every fit judgement in a run is made
against it, so it is written first (after persona.yaml) and never hand-drifted
away from prose.

## Columns (exact order; header row required)

| column | values | notes |
|---|---|---|
| `id` | `L-01`… | stable; never renumber |
| `place` | text | the venue's actual name as Google Maps has it |
| `city` | `London` / `Los Angeles` / `San Francisco` / home city / other | app cities spelled exactly like this |
| `area` | text | neighbourhood as the app would show it |
| `category` | text | short: `natural wine restaurant`, `pub`, `jazz club`, `bakery`, `gallery`, `walk` |
| `price` | `$` / `$$` / `$$$` / `$$$$` / `free` | as the app renders it |
| `verdict` | `love` / `like` / `fine` / `no` / `never` | the persona's TRUE reaction if taken there on the trip in question |
| `visited` | `yes` / `no` | has the persona actually been |
| `why` | ≤ 25 words | in the persona's terms; the taste axis it evidences |
| `who_vetoes` | member name / `—` | which party member's reaction drives a `no`/`never` |
| `in_catalog` | `seen` / `unknown` | `seen` only if observed on an app card at build time (record where in `_research/`) |
| `verified` | date / `—` | required if the row asserts a venue fact (closed, moved, changed hands) |

## Rules

1. **≥ 25 rows** per persona; ≥ 12 in the T1 city; ≥ 5 `love`, ≥ 5 `no`/`never`;
   ≥ 3 home-city rows (the app asks for "spots you love — anywhere").
2. **Include known-catalog venues.** At build the app surfaced (London) Brawn,
   Rochelle Canteen, The Marksman, Ronnie Scott's, BRAT among others; each
   persona's ledger carries ≥ 4 `in_catalog: seen` rows across the verdict
   range so a run can be graded on venues the app *can* recommend, and the
   `no`/`never` catalog rows are the flattering-but-wrong traps.
3. **Verdict is per trip context.** A venue the persona loves alone but which
   fails the T1 party gets the T1 verdict and `who_vetoes` names the member;
   put the solo verdict in `why` ("love solo; Sam won't do the queue").
4. **No venue facts without verification.** `why` carries taste, not claims.
   "Feels touristy" is taste. "Closed in 2025" is a fact — verify, date it, or
   move it into gaps/ as a belief the persona holds.
5. **Real venues only.** Never invent a venue. If a story needs a place the
   persona misremembers, the *misremembering* is the fiction; the venue is real.
6. **Prose quotes the ledger.** `canon/taste.md`, `scoring/expected-fit.md`,
   every ledger `True:` field, and `persona/beliefs.md` [T]/[F] tags cite `L-nn`
   ids. When a row changes, grep for its id and re-check every quote.
7. **Consistency check** (run before marking a persona built): every
   `who_vetoes` name exists in `people.md`; every `love` row is consistent
   with `taste.loves`; every `never` row is explained by a `taste.avoids` axis
   or a constraint in persona.yaml; `in_catalog: seen` rows are listed in
   `_research/catalog-observations.md` with the date seen.
8. **Growth.** Off-ledger venues the app recommends are judged by the grader
   against `taste.md` and appended to `runs/<run>/off-ledger-judgements.md`;
   promote to the ledger in builder mode with a decision entry — never mid-run.
