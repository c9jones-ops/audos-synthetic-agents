# Calibration: presenting postures in founder conversations

The audit trail for the session-state layer — why these fifteen states and not
others. Companion to `session-states.md` (the specs) and `decisions.md` S2/S7/S8
(the decisions). Contract: `plans/2026-08-12-session-state-layer.md`.

## What this file is calibrating

**Not** how founders feel. How founders *present* — what a support product
actually meets when a founder sits down with it, which is a posture, not an
interior state. The layer exists because every run of every company currently
draws the same founder: canon persona, canon phase, nothing else. The platform
under test is therefore only ever graded against a founder who is attentive,
articulate, cooperative and pre-organised, and a product that works on that
founder is not thereby proven to work on any other.

## Source discipline (binding — `decisions.md` S7)

Two evidence bases, handled differently.

**1. An abstracted reading of a private founder-interview corpus.** That corpus
is not part of `synthetics/` and never enters it. What appears here: behavioural
*shapes*, stated generically, with confidence labels. What never appears: names,
companies, sectors, situations specific enough to identify a person, quoted or
paraphrased language, or counts small enough to single a contributor out. The
map from state to supporting evidence is a private file the owner maintains
outside this repo; it is referenced here and never reproduced.

**2. Graded runs in this corpus**, which are ordinary in-repo evidence and are
cited by path. Currently one: `ember/runs/2026-08-11-helmsman-foundation-t0.md`.
Where a state has run corroboration it is marked **[run-corroborated]** — that
is the strongest evidence in the file, because it is observed platform behaviour
rather than an inference about founders.

**Illustrative lines are written fresh.** Every example of how a posture *sounds*
in this file and in `session-states.md` was composed against a corpus founder's
own voice file — Ember's `founder/voice.md` — and marked *(register example)*.
None is carried across from source material. The lines exist because a posture
described without a register degrades in play into a vibe rather than a mechanic,
which is the exact failure the specs are built to prevent.

## Confidence labels

- **High** — clearly evidenced across most of the interview set.
- **Medium** — evidenced in some; plausible generally.
- **Inferred** — consistent with the material, not directly attested. Present
  because it earns a slot on a design argument, and labelled so nobody later
  mistakes it for an observation.

---

## 1. The central finding: the modal register is minimised weariness, not crisis

**Confidence: High.**

The dominant register across the interview set is **sustained weariness that the
founder actively shrinks in the telling**. Not drama, not crisis, not collapse —
difficulty described and then immediately made smaller within the same breath.

This is the single most important calibration in the file, because it determines
what the *rest* of the set is allowed to look like. A state set that leads with
drama is modelling the wrong population: it would produce vivid runs against a
founder who does not exist in the evidence, and quietly fail to produce runs
against the founder who does.

Two direct consequences, both binding on the spec file:

1. **Default intensity is 1–2.** A posture that dominates the session is the
   exception, not the texture (see §6).
2. **B2 Minimising is not one state among fifteen — it is the population's
   baseline behaviour, isolated and turned up.** Drawing it makes explicit what
   is otherwise ambient.

*Register example, against Ember's voice file:* "We lost the wholesale guy who
set the whole thing up. Which sounds worse than it is — he'd taught Tom most of
it by then, honestly."

**A worked warning about this example.** The first draft of this line used a
near-miss on payroll. It was wrong, and instructively so: cash is a
phase-gated domain for that founder (`never` volunteered in euphoric phase,
`freely` in panic), and `founder/voice.md` independently forbids the cash number
unprompted in euphoric phase. A perfectly good *illustration of minimising* was
simultaneously an unprompted disclosure the ledger forbids — which is exactly how
a state leaks content without anyone noticing they changed a `Volunteers?` value.
**When writing a register example, check the domain as well as the shape.**

Note that Ember's `founder/voice.md` already encodes this shape independently,
under **what he never says**: *never a number that makes the company smaller
without an immediate "but."* The calibration and the existing character work
agree without having been written against each other, which is the closest thing
to a cross-check this file can offer.

## 2. The reframe: a posture is protective, and it was learned

**Confidence: High** for the pattern; **Medium** for the causal account.

Founders operate in environments where visible uncertainty is expensive — with
boards, investors, employees, lenders, and often domestic partners. The reliably
safe presentation is competence. Presented often enough, under enough pressure,
it stops being a choice and becomes the resting posture: what gets brought into
*every* conversation, including ones where it is actively counterproductive.

So what a support product meets in session one is not a mood the founder happens
to be in. It is **a protective posture learned from an environment that penalised
the alternative** — which is why it does not yield to rapport alone, why it is
stable enough to model as a mechanic, and why it is the founder's *default* rather
than his reaction to the counterpart in front of him.

The causal account is labelled Medium deliberately: the pattern is well evidenced,
the explanation is a reading. Nothing downstream depends on the explanation being
right — the specs describe behaviour, not motive.

## 3. Why the states are behavioural, not affective

**Confidence: High** — this is a playability finding from corpus work, not a
claim about founders.

"Distracted" is a mood. A player asked to be distracted will produce a different
session every time, and two runs of the same state stop being comparable — which
destroys the layer's entire purpose.

"Answers land a beat late, threads get dropped mid-sentence, things already
covered get re-asked" is a mechanic. Any player executes it the same way twice,
and a grader can check whether it was executed.

Every state in the set is therefore specified as **observable conduct with an
in-session tell**, never as an internal condition. Three rules follow, and they
are the acceptance criteria for a spec:

- **Observable inside 90 seconds.** If the platform cannot detect the posture
  early, it cannot adapt, and the run tests nothing but noise tolerance. Every
  tell must be expressible in the founder's first two or three turns.
- **Every state names the failure it hunts.** A specific platform mistake, made
  when the posture is taken at face value. "Adds realism" is not a justification
  and does not earn a slot.
- **Orthogonality.** State modulates delivery; phase and ledger govern content
  (`decisions.md` S2). This is the load-bearing rule, reviewed separately.

## 4. Why five families

**Confidence: Medium** — the axes are a construct imposed on the material, not a
structure the material announced.

The families are not decoration and not a filing convenience. Each answers a
different question about how the founder is present:

| Family | The question it answers |
|---|---|
| **A — Altitude & Scope** | Where does he hold the work? |
| **B — Disclosure** | What does he show you, against what's there? |
| **C — Reception** | What does he do with what you give him? |
| **D — Availability** | How much of him is in the room? |
| **E — Continuity** | What is his relationship to his own past self? |

A set covering all five varies the session along **independent** axes. A set
that didn't would produce five flavours of the same difficulty and read as five
tests while being one.

The family structure also does load-bearing work in composition: at most one
state per family (`decisions.md` S3), because two from the same family are
competing accounts of the same axis and a player asked to hold both resolves the
conflict arbitrarily, differently each time.

## 5. The states, and what each rests on

Confidence labels apply to the *behavioural pattern*, not to the spec's mechanics
— the mechanics are authored, and their justification is the failure they hunt.

### Family A — Altitude & Scope

| # | State | Rests on | Conf. |
|---|---|---|---|
| A1 | Laundry List | Founders arriving with eight-to-twelve unranked concerns and resisting ranking is one of the most consistent shapes in the set. Ranking is experienced as loss, not clarification. | High |
| A2 | The Adder | Generativity presenting as progress: new priorities produced *during* a conversation, in response to it, with no felt cost to accumulation. **[run-corroborated]** — the Helmsman run's founder arrived with five things and left with five plus a hire plus a strategic objective, several supplied by the platform's own summary. | High |
| A3 | In the Weeds | Retreat under pressure into the domain where competence is certain. Fluent, specific, genuinely expert, and off-altitude — the work *feels* productive because he is actually good at it. | Medium |
| A4 | Directive, No Detail | Direction issued as outcome with no specification of what it takes. Teams receive an instruction they cannot execute; the founder experiences himself as having been clear. **[run-corroborated]** — the Helmsman run's §6 defect, where a vague unpriced claim was upgraded into crisp strategic language and booked as an objective. | Medium |
| A5 | Busy Not Moving | Full week, no decisions, and no awareness of the gap. Restored to the set on a design argument, not an evidential one — see §8. | **Inferred** |

**A3 and A4 are one mechanism with two expressions** (High confidence on the
pairing). The driver is the same — pressure, or ambition running ahead of
specification — and founders resolve it in opposite directions: down into
certain competence, or up above the detail entirely. Drawn independently,
authored together.

### Family B — Disclosure

| # | State | Rests on | Conf. |
|---|---|---|---|
| B1 | Surface-First | The presented problem is real, well-formed, genuinely answerable — and is not the primary one. Layer two arrives first because it is the layer that has already been made presentable. | High |
| B2 | Minimising | §1's population baseline, isolated: real weight stated, then shrunk within the same turn. | High |
| B3 | Too Clean | The narrative runs smooth and positive; the hard parts are described as already handled. Distinct from B2 — B2 says the difficult thing and shrinks it, B3 never says it. | Medium |

**B1 carries the largest authoring cost in the set** and it is per-company, not
schema-level: each company must designate, per save-point, which real problem is
the decoy and what signals it isn't primary. This is why B1 is built last despite
being the highest-value state.

### Family C — Reception

| # | State | Rests on | Conf. |
|---|---|---|---|
| C1 | Compliant | Sincere agreement with no adoption. Usually protective rather than agreeable-as-trait: agreeing ends a conversation faster than disagreeing, and most advice has not survived contact with his week. | High |
| C2 | Evaluating | Quiet assessment of whether this is worth his time; questions asked back at the tool; reserve without hostility. | Medium |
| C3 | Diagnosed, Not Moving | Accurate, precise, unprompted self-diagnosis — named before, more than once, and not acted on. Articulacy about a problem is uncorrelated with movement on it. | High |

**C1 and C3 are the two states that produce transcripts which look successful.**
That is precisely their value: they catch failures the corpus structurally cannot
see today, because a grader reading a cooperative, articulate transcript has no
signal that anything went wrong. Both carry double draw weight for this reason.

### Family D — Availability

| # | State | Rests on | Conf. |
|---|---|---|---|
| D1 | Time-Boxed | A hard stop named up front; wants the short version; visibly tracking the clock. | Medium |
| D2 | Fragmented | Attention genuinely divided. Answers land a beat late, threads drop mid-sentence, covered ground gets re-asked. | Medium |
| D3 | Carrying a Person | The load is interpersonal rather than operational. He circles it, and he wants it witnessed rather than solved. | High |

**D3 is the state most able to identify a real person through circumstance
alone**, which is why its tell is specified at the level of *the load is
interpersonal* and no further (S7). Two authoring constraints follow: keep
interpersonal material inside what a company's canon already supports — its own
org and team files — and never invent new private material about a real person to
service a state draw.

### Family E — Continuity

| # | State | Rests on | Conf. |
|---|---|---|---|
| E1 | Drifted | The posture of a founder living against something he genuinely meant: enthusiasm carrying a half-note of performance, past decisions re-narrated to sound consistent, mild defensiveness near the gap between stated values and current conduct. | Medium |

**E1 cannot be drawn at a first session** — there is nothing to be inconsistent
*with*. It is excluded from the general pool and available only at save-points
where canon supports it and prior-session artifacts exist.

**E1 is not drift detection.** Several companies already carry drift as canon and
the rubric already grades the platform's detection of it. Canon supplies the
facts; E1 supplies the founder's *behaviour* while the drift is live.

The distinction that makes E1 worth its cost: **commitment breach vs. values
breach.** Catching *"you committed to no new spend and this is new spend"* is
bookkeeping against stored artifacts. Catching *"you told me this company existed
to do X, and the last three decisions have all been about Y"* requires having
stored what he said the company was **for** — a field most storage layers never
capture, and one the Helmsman run's Compass had no slot for. **[run-corroborated]**

## 6. Intensity is a separate dial

**Confidence: High.**

The same underlying mechanism produces wildly different severities across
founders — from mild sustained discomfort to genuine incapacity. Severity is
therefore not baked into a state; it is drawn alongside it.

- **1 — trace.** Present, deniable, visible only in aggregate across the session.
- **2 — evident.** Clearly present; a competent counterpart would name it.
- **3 — dominant.** Shapes the whole session; ignoring it makes the session fail.

Per `decisions.md` S9, **intensity 3 is assigned-only, never drawn** — it stays
available for deliberate hypothesis-testing without risking a run that is about
the state rather than about the product. Drawn intensity is 1–2, consistent with
§1's finding that the modal register is minimised rather than acute.

## 7. Composition

**Confidence: High** for the observation; the constraints are design.

Real founders do not present one posture at a time. The same person is
time-boxed *and* minimising *and* sitting on something he diagnosed a year ago
and never acted on. Single-state runs are artificially clean, and the layer
would be less true without composition.

But composition trades against **attribution** — the ability to say which
condition caused a platform failure — and a layer that produces realistic runs
teaching nothing is worse than a layer that produces clean runs teaching
something. The three constraints in `decisions.md` S3 (dominant plus secondaries;
at most one per family; hard cap of three) exist entirely to protect attribution,
as does the scheduling gate: **singles before composites**, because a composite
run cannot be read without knowing how the platform handles each state alone.

## 8. What was cut, and why

Recorded so that reinstating any of these is an amendment rather than a
rediscovery.

**Busy Not Moving — cut, then restored as A5** (`decisions.md` S8). Cut on the
grounds that it sits close to A2 and A3 and could fold into either. Restored on
the argument that it hunts a failure neither covers: A2 grows the list, A3 goes
deep on the wrong thing, and A5 is unexamined full utilisation *plus the absence
of self-awareness about it* — meeting a platform that reads an activity report as
progress. Labelled **Inferred** and it should stay that way until play says
otherwise: it is in the set on a design argument, and the first graded A5 run is
the test of whether the distinction from A2/A3 survives contact.

**Ambushed — cut, deferred rather than rejected.** Something landed twenty
minutes before the session. Cut because the interview set contains **no founder
in acute crisis** — which is a sample gap (§9), not evidence of rarity. Also the
state most likely to make a run about itself rather than about the product.
Cheap to add once singles are baselined.

**Buoyant — cut, and the reason is structural rather than evidential.** Post-win,
expansive. Two arguments: the register in the material is weariness rather than
elation (§1), and — decisively — **euphoric is already a phase**. A state
duplicating a phase violates the orthogonality rule that state must never
substitute for the pinned oscillation phase (`decisions.md` S2). Reinstating
Buoyant means accepting an orthogonality exception, which is a much larger
decision than adding a state.

## 9. Limits of this calibration

Stated plainly, because a calibration file that reads as more certain than its
evidence is worse than none.

1. **No acute crisis in the sample.** The set contains no founder mid-catastrophe.
   This is the clearest known gap and it is the direct cause of one cut state.
   Absence here is not evidence of rarity — it is evidence about who agrees to be
   interviewed and when.
2. **Interview presentation is itself a posture.** Every observation is of a
   founder talking to an interviewer, which is not the same as a founder talking
   to a support product with a stake in the answer. The postures are real; their
   *frequencies* in this file should not be treated as frequencies in production.
3. **The draw weights are judgment, not measurement.** Double weight on B1, C1,
   C3 and A4 reflects test value — deceptively successful transcripts, highest
   value, an already-evidenced defect — not observed prevalence.
4. **One graded run.** All **[run-corroborated]** marks currently trace to a
   single run of a single company against a single platform. That is real
   evidence and it is thin evidence.
5. **The causal account in §2 is a reading**, and nothing in the specs depends
   on it.

## 10. Re-checking this file

The state-to-evidence map is **owner-held, outside this repo** (S7). Anything in
this file that needs grounding beyond its confidence label is a question for the
owner, not a reason to reach for the source material — no agent working in
`synthetics/` should read the interview corpus, and none needs to in order to
build, run, or grade against this layer.

The file that will most cheaply improve this one is the run record. Each graded
state-run either corroborates a shape, moves a confidence label, or exposes a
state that does not survive play. **Inferred** labels in particular are
promissory: A5 either earns Medium through play or comes back out of the set.
