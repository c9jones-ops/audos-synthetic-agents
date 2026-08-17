# System decision log — corpus-wide judgment calls

Working log of every judgment call that changes shared infrastructure, so the
owner can review or override any of them afterwards. The per-company logs
(`<codename>/_research/decisions.md`) cover company content; this file covers
the rules those companies are built and run under.

Newest decisions appended at the bottom. Open decisions stay in place with a
`**Status: OPEN**` line until resolved, then are amended in place rather than
rewritten — the history of what was undecided is part of the audit trail.

## Why this file exists

`AGENTS.md` requires every judgment call to be logged in
`<codename>/_research/decisions.md`. That log is per-company, and some work
isn't: the loading contract, the authoring guide, the schema, the two-mode
contract, run-file conventions. Before this file existed, a decision that
changed the rules governing *every* company had nowhere to live, so it either
went unrecorded or was filed against whichever company happened to surface it
(see S4 and S5, both promoted out of Ember's log).

## Scope

**Qualifies — anything that changes shared infrastructure:**

- any file in `_schema/`
- the two-mode contract (`AGENTS.md`) or the `/founder` skill
- rubric *structure* shared across companies — the section set, what a section
  grades, scoring conventions like N/A-vs-PASS. Individual companies may still
  add their own axes and name their own hunted failure; that stays company-level
- run-file conventions and metadata
- grading methods that apply regardless of which company was run

**Does not qualify — stays in the company's own log:** company content, company
numbers, company-specific canon, character decisions, per-company scoring
content, anchor and calibration choices.

## Conventions

**Prefix.** `S1`, `S2`, … Kestrel uses `D`-numbers and Ember uses `E`-numbers;
`S` for system keeps the three namespaces distinct and makes a bare citation
(`per S4`) unambiguous about which log it points into.

**Cross-referencing, both directions.** When a company decision is downstream of
a system decision, cite it (`per S4`). When a system decision was provoked by
something found in one company, cite the company entry that surfaced it. A
promoted decision is never deleted from the company log — the provenance of
where a system rule was *discovered* is worth keeping, so the company entry is
amended to point here instead.

---

## Decisions

### S1 — This log exists; location, prefix, and scope (2026-08-12)

Stood up per `plans/2026-08-12-session-state-layer.md` §8 step 0, before that
plan's build began generating decisions that had nowhere to go.

**Location: `_schema/`.** That folder is already the cross-company authority —
`loading-contract.md`, `authoring-guide.md`, `company.schema.yaml`,
`financials.spec.md` all live there and bind every company. Decisions that
change those rules belong beside them, not one level up in a root file that
would compete with `README.md` for the reader's attention.

Prefix, scope boundary, and cross-referencing rules as stated above.

**Downstream edit made under this decision.** `AGENTS.md`'s builder-mode rule
"log every judgment call in `<codename>/_research/decisions.md`" was amended the
same day to carve out shared-infrastructure decisions and route them here.
Without that edit the contract still misroutes exactly the decisions this file
was created to hold — a change to the two-mode contract, and therefore itself
system-level, logged here as part of S1 rather than as its own entry.

The boundary case worth naming: **rubric changes split.** Structure is system-level
(the section set, what §6 grades, the N/A convention from S4's neighbourhood);
content is company-level (Ember's §6 hunts energy-chasing, Kestrel's hunts its
own failure). A change that adds a named failure *shape* to §6 is therefore a
system decision with per-company text edits downstream — which is exactly the
situation S6 is currently parked on.

### S2 — The session-state layer is adopted (2026-08-12)

Contract: `plans/2026-08-12-session-state-layer.md`. Provoked by
`ember/runs/2026-08-11-helmsman-foundation-t0.md` — a competent graded run in
which every question landed on a founder who was attentive, articulate,
cooperative and pre-organised, leaving the corpus unable to say whether the
platform survives contact with anyone else.

**Adopted:** a reusable layer that varies *how the founder shows up* without
varying *who he is or what is true*. Fourteen states in five families
(altitude, disclosure, reception, availability, continuity), a 1–3 intensity
dial drawn alongside the state, and a weighted d20 draw that keeps Baseline
control runs in rotation.

**The load-bearing constraint — orthogonality:**

> **State modulates delivery. Phase and ledger govern content.**

A state may change turn length, attention, sequencing, what he wants from the
hour, and how he receives a challenge. It may **never** unlock a distortion or
re-gate one the phase has opened; change a `Volunteers?` value; alter any canon
fact, number, or belief; or substitute for the oscillation phase pinned by the
save-point. Break this and runs stop being comparable — "the platform failed"
becomes indistinguishable from "the founder was randomly harder that day." Every
state spec is reviewable against this rule and the review is a build step, not a
nicety.

**Terminology:** *session state* in files and metadata; *presenting posture* in
prose when explaining what it models. The states are behavioural, not affective
— a mechanic a player can execute, not a mood they must feel.

**Never disclosed to the platform, always logged for the grader.** State and
intensity are drawn before the run, recorded in run-file frontmatter, given to
the player, and never revealed in-world.

**Baseline control rule.** Any state-run should be paired with a baseline run of
the same company and save-point, previously recorded or run alongside. Without
it, a weak counterpart's poor performance is indistinguishable from state
difficulty — states hand any bad run a plausible excuse. Ember has a T0 baseline
on record, so Ember T0 state-runs may proceed immediately.

**Rubric impact is deliberately small.** States are a condition, not a section;
the rubric is not rewritten to score them. Two additions only: conduct (§6) is
graded *against the drawn state* (failing to compress under Time-Boxed is a §6
failure, not a neutral outcome), and §2 Probed credit is unaffected by state —
the right instrument is the right instrument whether or not the founder was easy
that day.

Downstream infrastructure changes this decision authorises: run-file frontmatter
gains a `session_state` block; `loading-contract.md` gains a paragraph putting
state and intensity in the player's load alongside the save-point; the
`/founder` skill accepts an optional state argument and draws one when it isn't
supplied.

### S3 — Composition rules for session states (2026-08-12)

Real founders present more than one posture at once, so composition is
supported — under three constraints that exist to protect **attribution**, the
ability to say which condition caused a platform failure. Without them the layer
produces realistic runs that teach nothing.

1. **Dominant plus secondaries, never co-equal.** One state is dominant at
   intensity 2–3; one or two others are secondary, held at intensity 1.
   Secondaries colour the session, they do not drive it.
2. **At most one per family.** The five families are orthogonal by construction.
   Two states from the same family are competing accounts of the same axis, and
   a player asked to hold both resolves the conflict arbitrarily — differently
   each time.
3. **Three total, hard cap.** Beyond three, mechanics stop being executed and
   start being approximated, which is the vibes-not-mechanics failure the specs
   exist to prevent, and attribution is past recovery.

**Scheduling gate — singles before composites.** A composite run is only
interpretable against known single-state behaviour. Run singles until every
state in the general pool has at least one graded run, *then* enable
composition. This is a constraint on the corpus's run campaign, not on the
design (plan §8 steps 8–9; 8 gates 9).

**Grading a composite.** Score against the dominant. Secondaries are recorded as
texture that may explain a near-miss, not separately scored. A secondary that
appears to have caused a failure outright is a signal that the intensity-1 spec
is too strong and needs tuning down — record it as a follow-up.

**Drawing a composite.** Dominant from the §6 table; then d6 — 1–3 no secondary,
4–5 one, 6 two — drawn from families not already used, collisions re-drawn.
Baseline is never a secondary.

Named clusters (recurring composites drawn and baselined as a unit) are the
intended next step, deliberately **not** designed yet: let the single-state runs
show which combinations actually recur.

### S4 — The proxy-debrief grading method (2026-08-12; promoted from `ember/_research/decisions.md` E11.3)

**Applies to every company.** Recorded originally as an Ember decision because
Ember's first graded run is where it was invented; nothing about it is
Ember-specific.

**The method.** After grading, load a **clean-context founder proxy** at the
run's save-point, give it the session as in-world material, and ask for
artifacts the founder would actually produce — a call he makes, a late-night
message he sends, a conversation he has that week, how he tells the story two
weeks later.

**Why it earns a slot.** The four scoring axes (Noticed / Probed / Recorded /
Actioned) all grade the *platform's* artifacts. A correction that escapes the
session through the founder's own mouth is therefore structurally invisible to
them. In the Ember run the debrief established that the D-02 correction
propagated and held for two weeks — against a ledger that predicts re-inflation
within hours — because the founder socialised it to two named people, while the
underlying conviction never moved. It also surfaced a re-inflation six hours
later that became a pre-loaded counsel-stability test for the next session, and
showed a buried finding about to be requested by the founder unprompted after
the platform scored 0 on probing for it.

**Binding caveat.** It is downstream *simulation*, not observed behaviour. It
never substitutes for artifact evidence, and its findings belong in the run
record (where they change the next save-point) rather than in the score — see
S5.

Loading discipline for the proxy is the ordinary founder-mode load per
`loading-contract.md`, fenced to the run's save-point. The proxy must be
clean-context: a window that has read `scoring/` has seen the answer key.

### S5 — Platform-caused vs. character-caused outcomes (2026-08-12; promoted from `ember/_research/decisions.md` E11.2)

**Applies to every company.** Scoring credits the platform's work, not the
founder's downstream behaviour.

A graduation marker the founder reaches on his own — extracting a date from
someone else, requesting the arithmetic the platform never asked for — is
**recorded in the run file**, because it changes what the next save-point looks
like, and **earns no score**. The provoking case: Ember's first run produced two
such outcomes in the proxy debrief, both graduation markers by `behaviour.md`'s
definition, neither earned by the platform.

The rule generalises past graduation markers to any downstream good outcome the
character produced unaided. If the run record and the score disagree about
whether something happened, both are right: the company changed, the platform
didn't cause it.

### S6 — Two rubric amendments raised by the first graded run — **RESOLVED 2026-08-12: both adopted, (b) narrowed**

Both change infrastructure shared with runs that are **already graded**, which
is why neither has landed. Raised in `ember/_research/decisions.md` E11
follow-ups (a) and (b) and in the run file's follow-ups.

**(a) Add *belief-laundering* to §6 as a named failure shape.** §6 currently
describes energy-chasing as amplification — the platform catching the founder's
euphoria and echoing it. The Helmsman run demonstrated a second mode: the
platform took a founder's vague, unpriced claim ("the doors basically pay for
themselves"), authored a crisper version of it, promoted it to a 2–3 year
strategic objective, and secured a confirm click. No cheerleading, no
amplification — the founder's energy was *formalised* rather than matched, and
the belief was booked without ever being checked. The proposed rule of thumb:
promoting something to a strategic objective should trigger "what would have to
be true?" before the confirm button.

*Builder note for the decision.* Per S1, this is a system decision with
per-company text edits downstream — §6's hunted failure is written separately in
each company's `scoring/rubric.md`. Two files today (Kestrel, Ember), and every
company built after it. The retroactivity question needs answering with it: the
Helmsman run scored §6 = 1 under the current wording and flagged the gap in a
rubric note. If the amendment lands, does that run get re-scored, annotated, or
left as-is with the note standing as its record?

**(b) An artifact capture rule for run operators: open every persistent surface
before `@out`.**

*Builder note for the decision.* `loading-contract.md` rule 5 already makes
capture mandatory — "export or screenshot every persistent surface the platform
built." The proposed addition is a different obligation: rule 5 covers capturing
surfaces the operator *saw*, while this covers actively opening surfaces the
session never displayed. That is the gap the Helmsman run fell into — the
Company Profile card was never opened, and §1 substantively lives there, so that
section was graded partially unobservable off the summary card alone. The same
card was the decisive artifact in Kestrel's first run. If adopted, it is one
clause added to rule 5 rather than a new rule.

---

**RESOLUTION (2026-08-12, owner's call). Both adopted. (b) narrowed in scope.**

**(a) Belief-laundering adopted as a named §6 failure shape.** Written into both
rubrics: `kestrel/scoring/rubric.md` §6 and `ember/scoring/rubric.md` §6, the
latter as one of two named modes of energy-chasing (amplification and
belief-laundering) with the Helmsman run cited as the worked example. Both
rubrics also gained the S2 line that conduct is graded against the drawn session
state.

*Retroactivity: no re-scoring.* The owner has since changed Helmsman, so the
graded run measures a version of the product that no longer exists — re-scoring
it against the amended rubric would produce a number about nothing. The run
file's existing §6 note stands as its record. **This generalises: an amended
rubric applies to runs from its amendment date forward, and prior runs keep
their original grade plus whatever note prompted the change.**

**(b) Capture rule adopted, and deliberately narrowed** to avoid the blanket-
screenshot burden the owner flagged as overkill. Landed as an addition to
loading-contract rule 5, splitting one obligation into two:

- **Open** every persistent surface once before `@out`, including surfaces the
  session never displayed. This is the part that fixes the original defect —
  the Company Profile card was never opened, so nobody could judge whether it
  was worth keeping, and §1 was graded partially unobservable off the summary
  card alone. Opening is a click.
- **Capture** on judgment: an insight, a key learning, something that went
  wrong, something that went notably well. Blanket capture is explicitly not
  required.
- **A floor**, because §7 cannot be scored without it: always capture whatever
  the platform claims to *remember*, and the research/company-profile surface
  **in its pre-correction state** — that evidence is destroyed the moment the
  founder corrects it.

The open/capture split is the substance of the narrowing: the owner's concern
was capture volume, and opening carries almost none of that cost while fixing
the whole of the original problem.

### S7 — Source-discipline standard for the session-state files (2026-08-12)

Resolves `plans/2026-08-12-session-state-layer.md` §10 Q1. Owner's call, taken
before any calibration file was written, because it constrains everything
downstream.

**The risk is phrasing, not shape.** The behavioural mechanics are population-
level and unattributable — "agrees readily, adopts nothing" identifies nobody.
What can carry a real person into this repo is **illustrative language**: a tell
or example line that is a near-verbatim quote from one conversation stays
identifying no matter how generic the mechanic around it is.

**Standard adopted — shape plus fresh-written register.** Mechanics and tells
are stated generically. Every illustrative line in `calibration-session-states.md`
and `session-states.md` is **written fresh against a corpus founder's own voice
files** (Ember: `founder/voice.md`), never carried across from source material.
The register has to be audible for a player to execute a posture consistently —
a state described without any example of how it *sounds* degrades into the
vibes-not-mechanics failure the specs exist to prevent — so the lines stay, and
their provenance is the corpus, not the interviews.

Applies also to D3 Carrying a Person, which gets extra generalisation: the tell
is that the load is interpersonal, stated without a specific relationship
configuration. It is the one state whose tell is a situation rather than a
conversational mechanic, and therefore the one most able to identify a person
through circumstance alone.

**Audit trail — owner-held, outside this repo.** The corpus files carry
behavioural shapes and High/Medium/Inferred confidence labels only. The map from
state to the evidence supporting it is a **private file the owner maintains
outside `synthetics/`**, so the audit trail genuinely exists and is checkable
without any of it crossing the boundary. Corpus files reference it generically
and never by path. Confidence labels are stated as population frequencies
("evidenced across most of the set"); counts small enough to identify a
contributor are not recorded on either side of the boundary.

**Standing rule this generalises to.** Any future corpus file abstracted from
the private interview corpus follows S7: shapes and confidence in-repo,
evidence map outside, illustrative language written fresh against corpus voice
files.

### S8 — State set is fifteen; A5 restored; draw protocol rebuilt (2026-08-12)

Resolves §10 Q2 and §10 Q5 (numbered 3 and 5 in the plan — §10's numbering runs
1, 2, 5, 6, 3, 4, a defect noted here so a later reader isn't hunting for a
missing question).

**A5 Busy Not Moving restored.** Full week, no output, hasn't noticed. Cut in
the plan as possibly foldable into A2 or A3; restored on the argument that it
hunts a failure neither covers — the platform reading an activity report as
progress. A2 grows the list, A3 goes deep on the wrong thing, A5 is unexamined
full utilisation *plus the absence of self-awareness about it*.

**Filed in Family A (Altitude & Scope), deliberately.** He holds the work
entirely at execution altitude and never rises to decision altitude. Family
placement is not cosmetic: under S3 constraint 2 it makes A5 non-composable with
A1/A2/A3/A4, which is correct — they are competing accounts of the same axis and
a player asked to hold two of them resolves the conflict differently every time.

*Ambushed* and *Buoyant* stay cut. Ambushed on the plan's own reasoning
(deferrable, cheap to add after singles are baselined, most likely of the three
to make a run about itself). Buoyant on a design argument rather than an
evidential one: euphoric is already a **phase**, and a state duplicating a phase
violates S2's rule that state must never substitute for the pinned oscillation
phase. Reinstating Buoyant would require accepting an orthogonality exception.

**Set is now fifteen; general pool fourteen** (E1 excluded per plan §4.3).

**Draw table rebuilt.** Fifteen states do not fit the plan §6 d20: 3 Baseline
faces + 8 double-weight faces + 10 single faces = 21. Resolved by dropping
**Baseline from 3 faces to 2**, giving 2 + 8 + 10 = 20 exactly.

Rationale for taking it out of Baseline rather than out of a state's weight or
off the d20: S2's baseline-pairing rule already requires every state-run to have
a same-company, same-save-point baseline run alongside it or on record. Baseline
faces in the draw are rotation, not the mechanism that produces control runs, so
they are the cheapest thing in the table to trim. Double weights are unchanged
(B1, C1, C3, A4) because their justification — deceptively successful
transcripts, highest value, an already-evidenced defect — is untouched by set
size.

| Roll | State | Weight |
|---|---|---|
| 1–2 | Baseline (persona as written, no modifier) | ×2 |
| 3–4 | B1 Surface-First | ×2 |
| 5–6 | C1 Compliant | ×2 |
| 7–8 | C3 Diagnosed, Not Moving | ×2 |
| 9–10 | A4 Directive, No Detail | ×2 |
| 11 | A1 Laundry List | ×1 |
| 12 | A2 The Adder | ×1 |
| 13 | A3 In the Weeds | ×1 |
| 14 | A5 Busy Not Moving | ×1 |
| 15 | B2 Minimising | ×1 |
| 16 | B3 Too Clean | ×1 |
| 17 | C2 Evaluating | ×1 |
| 18 | D1 Time-Boxed | ×1 |
| 19 | D2 Fragmented | ×1 |
| 20 | D3 Carrying a Person | ×1 |

Fourteen general-pool states across twenty faces. E1 Drifted is not in the
table — it is drawn separately and only at eligible save-points (plan §4.3),
substituted for a Baseline face or assigned directly. This table is reproduced
as the authoritative version in `session-states.md`; if the two ever disagree,
the spec file is wrong and gets corrected against this entry.

**Set size — author fifteen, stage the campaign.** All fifteen specs are written
in one pass while the pattern is loaded; the campaign is staged. Correcting the
plan's premise: per-company hooks do **not** scale with set size — there are
exactly three *(amended 2026-08-12 per S10: **four**, D3's eligible-relationship
designation added)* (B1 decoy, A3 home domain, E1 purpose, D3 relationship), each
attached to a specific state, so per-company cost is flat. Set size is an authoring-time
question only, which is what makes writing all fifteen defensible. Step 8's
singles campaign runs C1, C3, B1, A4 and Baseline first; the remaining states
follow once the layer has demonstrably changed grades.

### S9 — Three remaining §10 calls, adopted on the builder's recommendation (2026-08-12)

Walked through with the owner alongside S7 and S8; not separately confirmed.
Recorded here so each is cheap to flip. Any of the three can be reversed with a
single amendment to `session-states.md`.

**1. Intensity 3 is assigned-only, never drawn** (§10 Q, numbered 3). The plan
included it at low draw weight and flagged the risk that it produces runs about
the state rather than about the product. Making it assigned-only keeps the
capability for deliberate hypothesis-testing and removes the risk entirely —
and such runs already carry `state_selection: assigned`, which the plan
correctly says is not evidence about frequency. Intensity is therefore drawn
1–2 (d6: 1–3 → 1; 4–6 → 2) and set to 3 only by operator assignment.

**2. Mid-session transition: deferred, with a cheaper version built now**
(§10 Q, numbered 4). Drawing a transition as a random variable is not adopted —
it roughly doubles grading complexity. Instead, states that plausibly turn carry
a **documented exit trigger** in their spec (D1 Time-Boxed: what would make him
stay). The player executes it only if the platform earns it. This converts the
transition from noise into a **gradeable event** — did the counterpart buy the
extra half-hour? — at a cost of one line per applicable spec.

**3. A2 disengagement escalates rather than reclassifies** (§10 Q, numbered 6).
A2's "this founder disengages" outcome stays an ICP finding rather than a
platform defect. The plan's worry that this is too passive is met with an
escalation rule, not a reclassification: **three A2 runs ending in disengagement
promotes it from a run note to a corpus-level finding.** Dependency recorded —
that has nowhere to land until the cross-run findings ledger (plan §9 item B)
exists, so until then the third occurrence raises it directly with the owner.

### S10 — Orthogonality review: seven violations found and fixed; rule 1.1 hardened (2026-08-12)

Plan §8 step 3, executed as specified — all fifteen specs read against rule 3.1
in one pass, **fresh context**, by a reviewer that had not written them. Result:
**7 VIOLATION / 6 MINOR / 2 CLEAN**. Recorded in full because the failure pattern
is the useful artifact, not the individual fixes.

**What made the review work.** The reviewer grounded every judgment in a real
save-point — `ember/timeline/T0/state.md` — rather than arguing in the abstract.
All seven violations surfaced on first contact with that file, and none was
visible from the spec text alone. The specs' self-authored "orthogonality check"
paragraphs had certified all fifteen clean; in three cases the check asserted the
opposite of the mechanic directly above it. **A self-review by the author would
have found none of this**, which is the case for the step existing.

**Two systematic drafting defects accounted for six of the seven violations.**
Both are now clauses in `session-states.md` §1.1a so they bind future specs
rather than being re-patched per state:

1. **The instrument-blunting bullet.** Seven specs carried a bullet of the form
   *"uses the instrument but does not reach the conclusion."* Fatal in this
   corpus specifically: `behaviour.md` rule 3 makes instrument swaps the primary
   unlock channel and every ledger entry has an instrument-shaped trigger. Such a
   spec suppresses correctly-triggered unlocks **invisibly** — the grader sees a
   platform that ran the right instrument and earned nothing, and §10's promise
   that "§2 Probed credit is unaffected by state" becomes unenforceable. Fixed by
   a general clause: no state modifies the response to a correctly-executed
   unlock trigger; instrument bullets describe off-trigger offers and post-
   correction behaviour only.
2. **Intensity ladders written as content schedules.** Five ladders scaled a
   content quantity rather than visibility — how many items are on the table
   (A1), when the real problem becomes available (B1), how serious the minimised
   thing is (B2), how far the drift has gone (E1). These are `Volunteers?` values
   wearing an intensity coat. Fixed by: *intensity scales how visible the
   mechanic is, never the quantity, severity, or availability of content — a
   ladder that cannot be written without referring to how much canon material is
   in play has escaped rule 1.1.*

**Four further gaps in rule 1.1 itself**, all now closed: the rule bound "the
ledger" but loading-contract rule 4 binds all of `gaps/`, so the unreliable-number
file was unprotected (A4 stripped it by construction, since the community figure
is a quantity); `behaviour.md`'s documented behavioural levers — arguing hardens
the guard, the confabulation catch, the cheerful correction — were protected by
none of the four bullets, and C1 disabled two of them; `Volunteers?` was never
defined operationally, and two specs quietly read `freely` as *answers when
asked* rather than *arrives unprompted and early*; and no spec named the
**buried-findings set**, the corpus's primary scoring surface, which four specs
could have handed over for free because most of its items are the *true side* of
a ledger entry rather than an entry itself.

**The most instructive single finding.** `calibration-session-states.md` §1's
register example — composed carefully, against the right voice file, to
illustrate minimising — was an unprompted cash-domain disclosure at a euphoric
save-point, forbidden by D-06 (`never` in euphoric) and independently by
`voice.md`. The first careful instantiation of the mechanic produced the leak.
Fixed, and the file now carries the near-miss as a worked warning: **when writing
a register example, check the domain as well as the shape.**

**Structural change adopted.** Every spec's orthogonality check is now a
four-line checklist keyed to rule 1.1's bullets, answered against a **named
save-point of a built company**, above the prose. Free prose let an author
gesture; a checklist against Ember T0 would have forced A4's author to write down
"call it five" and see the contradiction.

**Company hooks: three became four.** D3 needs a per-save-point
eligible-relationship designation, because at Ember every plausible candidate
collides with something — the family relations are D-07 (`under trust`), the
co-founder has a canon conduct rule confining competition to the private-doubt
register, and the overdue raise is a buried finding. S8 amended above.

**Build-state consequence.** No company currently has any of the four hooks —
A3's home domain existed only inside the spec file's own example column, not in
`ember/founder/` where the table said it lived. **A3, B1, D3 and E1 are therefore
undrawable everywhere**, which is fortunate: three of them held violations. The
other eleven states are drawable for both built companies today. Step 6 closes
this for Ember.

**Not adopted.** The reviewer's suggestion to re-verify A2's derived-arithmetic
edge (extrapolating instrument output across doors) — judged covered by the
existing "never states a number that is not already his" plus `behaviour.md`'s
established fast-accurate-arithmetic behaviour. Recorded so the judgment is
visible rather than silent.

### S11 — Founder-player context is generated, never loaded from source (2026-08-12)

Two consecutive Ember T0 attempts were invalidated when the player bulk-read
full-window CSVs. Investigation found the same class of future knowledge in T0
canon prose, founder/ and ledger files, and the cross-save-point session-state
hooks. The previous contract contained the right warning in
`loading-contract.md` but the entry instructions still said to read `canon/`,
and even allowed date fencing by discipline. That made the safety boundary a
memory task for the model.

**Adopted:** founder players never read a company's source tree. The standard
library command `synthetics/tools/build_founder_context.py` creates a disposable
bundle for one company, save-point, and session state. It filters CSV rows by
their observation field, copies timeline files only through the fence, excludes
seeds/scoring/research/provenance/events, extracts only player-facing state
mechanics, and writes a hashed manifest. Entry contracts now fail closed if the
bundle cannot be built; manual filtering is not a fallback.

**Content consequence:** baseline player-facing prose must itself remain T0-safe.
Ember's known later outcomes moved out of canon/founder/gaps and remain in the
appropriate timeline deltas. Cross-save-point hook additions now live beside
the delta at which they become knowable. Tests lock the observed leak phrases,
forbidden paths, CSV cutoffs, timeline selection, state extraction, and output
safety.

**Event consequence:** event cards are intentionally not supported by the first
bundle format. Event runs remain isolated-harness-only until the command gains an
explicit exactly-one-card mode; silently reading `timeline/events/` is forbidden.
