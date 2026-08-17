# finch — provenance

**Private test infrastructure. Not for publication or external sharing.**
This file never enters a run.

## Fiction boundary

**Every person in this folder is wholly fictional.** Devin Whitlock, Danny
Ferro, Nate Sobczak, Elliot Tran and Rafi Haddad are invented for roleplay.
They are not modelled on, and borrow no identifying detail from, any real
private person — not the corpus owner's friends or family, and not the real
named curators who appear in the app under test (Casey, Priya, Jon at build
time). Any resemblance to a real person is coincidental and carries no
content.

The in-world name was changed from the build parameters' original after a
same-role collision with a fictional companion in the sibling heron persona
and a surname collision with an illustrative curator name in a brand mock
(_research/decisions.md D-01); "Devin Whitlock" and all four friends' names
are verified unused across all corpora.

## Venues are real; everything said about them is taste

The places in `canon/data/taste-ledger.csv` and throughout the prose are real
businesses and places, named so that fit can be graded against venues the app
can actually recommend. **Nothing said about any venue here is a claim about
the business.** Verdicts, "why" fields, and every remark in persona/ or gaps/
("a low dark room," "a tiny famous room," "the ride," "$100+ a head with
drinks") are this fictional character's taste, memory, estimate, or belief.
No row asserts a checkable fact about a venue; the `verified` column is `—`
throughout, by design. No closures, incidents, staff, service events, group
policies, or schedules are asserted about any venue — the ballpark row is
carried as "if there's a home game," never as a claim that there is one. The
Nashville trip in canon/history.md names no venue.

## Handling rules

1. In-world names appear only inside this folder and in run transcripts;
   every cross-persona file uses `finch`.
2. scoring/ and _research/ and this file never enter a player context; event
   cards enter only via an explicit event run (`_schema/loading-contract.md`).
3. If a venue's circumstances change (closes, moves), fix the ledger row in
   builder mode with a `verified` date and a decision entry; never let a run
   change canon.
4. Distress, health and money detail is kept at the register a stranger types
   into an app: "one of the guys is watching money right now," "he's between
   things," "one of us doesn't drink." Nothing more is to be invented — the
   non-drinking friend in particular carries no reason, duration, or history
   anywhere in this folder, and none may be added.
