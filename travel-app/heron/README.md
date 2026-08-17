# heron

A synthetic seeker for testing At Their Word. First persona in the
`travel/synthetics/` corpus; establishes the per-persona pattern.

## Who and what

**The seeker:** a 41-year-old product marketer from Austin planning four nights
in London (2026-08-25 → 29) for her tenth anniversary with her wife — first
time in London for both. Distortion class: **Projector**. She describes the
trip she wants to be the kind of person who takes ("we're foodies, we'll walk
everywhere, somewhere with a scene"), and her partner's limits — a knee that
caps walking at about twenty minutes, a flat refusal to queue, an exit from any
loud room, a quiet veto over where they actually go, and a real budget ceiling
— never make the first answer. She books everything weeks ahead and calls it
spontaneous. The anniversary dinner is already booked; she doesn't say so.

**What this persona tests:** whether the app's read describes the *actual*
need (seated, booked, quiet, near, over by ten) or transcribes the stated one;
whether it elicits the veto-holder's constraints by asking about her by name,
asking for a specific past evening, or showing one concrete option; whether it
holds "we're foodies" as colour rather than as four constraints; whether the
flattering-but-wrong pick (a hot, loud, walk-in grill that matches every typed
clause) becomes the top pick; and whether a stranger's name on a card carries
trust when the reason is legible.

## The design in one paragraph

Canon is a ledger of 39 real venues (23 London, 8 Austin, 1 Cincinnati, 3 LA,
4 SF; 8 love · 13 like · 4 fine · 8 no · 6 never; 5 seen in the app's catalog on
2026-08-17) plus a spine, a people file that gives the partner a hard veto,
and a history whose one "evening that went right" is the master unlock. The
persona diverges from canon in six documented, unlockable ways
(gaps/distortion-ledger.md), all one class, all opened by specificity and
never by persistence, plus one self-report with no true value ("we're
foodies"). Three findings are derivable from canon and never voiced
(scoring/buried-findings.md). Two trips: T1 the planning session a week out;
T2 day 3, the anniversary, with the booked dinner gone by her own error. Three
event cards. Everything material is classified volunteered / when asked /
never said / wrong in canon/divergence-map.md.

## How to run a test

See `../README.md` and `../_schema/loading-contract.md` (authoritative).
Summary: fresh app account; from the repo root
`python3 travel/synthetics/tools/build_seeker_context.py heron T1` (add
`--state <state[:n]>` to assign); a fresh player window reads only the bundle;
the operator relays screens; capture every persistent surface and the read
*before* any correction; `@out`; player self-report; grade in a different
window against scoring/. T2 continues the same account.

## Map

- canon/ — persona.yaml (spine), taste.md, people.md, history.md,
  divergence-map.md, data/taste-ledger.csv
- persona/ — bio, voice, psychology, beliefs ([T]/[F]/[~]), behaviour,
  companions-view
- gaps/ — distortion-ledger (D-01…D-06), unreliable-self-report,
  session-state-hooks (D1/O1/H1/M1/X1)
- trips/ — T1-london-anniversary, T2-london-day3-replan, events/E1–E3
- scoring/ — expected-fit, buried-findings, rubric (grader only)
- runs/ — one file per graded run; _research/ — decisions, calibration,
  catalog-observations (never in runs)

## Caveats a grader should know

- The catalog observations are dated 2026-08-17; the app changes weekly.
  Re-verify surfaces and card presence before grading §1/§4/§5.
- A save is not a hit: Dana saves things "for Marcus" while thinking [not
  happening]; grade fit against the ledger and her brackets, not the save.
- The T2 brief has Dana unable to name her day-1 dinner and day-2 lunch —
  deliberate; the player must not invent them.
- The persona shares an in-world name with a fictional staff member in the
  founders corpus (_research/decisions.md D-10); the two never meet.
