# heron — provenance

**Private test infrastructure. Not for publication or external sharing.**
This file never enters a run.

## Fiction boundary

**Every person in this folder is wholly fictional.** Dana Prewitt, Sam
Alvarado, Marcus Hale and Cilla Prewitt are invented for roleplay. They are
not modelled on, and borrow no identifying detail from, any real private
person — not the corpus owner's friends or family, and not the real named
curators who appear in the app under test (Casey, Priya, Jon at build time).
Any resemblance to a real person is coincidental and carries no content.

The in-world surname was changed from the build parameters' original
after a collision with a fictional staff name in the sibling founders corpus
(_research/decisions.md D-10); "Prewitt" is verified unused across all corpora.

## Venues are real; everything said about them is taste

The places in `canon/data/taste-ledger.csv` and throughout the prose are real
businesses and places, named so that fit can be graded against venues the app
can actually recommend. **Nothing said about any venue here is a claim about
the business.** Verdicts, "why" fields, and every remark in persona/ or gaps/
("a busy pub floor," "the queue," "a hot loud room," "the benches") are this
fictional character's taste, memory, or belief. Where a row asserts a checkable
fact about a venue it carries a `verified: YYYY-MM-DD` stamp (only L-07 at
build); everything else is opinion by design. No closures, incidents, staff, or
service events are asserted about any venue. The T2 scenario's failed booking
is the character's own error, attributed to no business.

## Handling rules

1. In-world names appear only inside this folder and in run transcripts;
   every cross-persona file uses `heron`.
2. scoring/ and _research/ and this file never enter a player context; event
   cards enter only via an explicit event run (`_schema/loading-contract.md`).
3. If a venue's circumstances change (closes, moves), fix the ledger row in
   builder mode with a `verified` date and a decision entry; never let a run
   change canon.
4. Distress, health and money detail is kept at the register a stranger types
   into an app: "knee surgery, twenty minutes then a sit," "seventy a head."
   Nothing more is to be invented.
