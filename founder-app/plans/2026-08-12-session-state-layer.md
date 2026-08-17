# Plan — the session-state layer

**Date:** 2026-08-12
**Author:** drafted with Casey after the first graded Ember run
**Status:** ready to execute in a fresh session
**Scope:** system-level — applies to every company in `synthetics/`, not to Ember specifically

---

## 0. For the session picking this up

You have no prior context. Read this file, then `synthetics/AGENTS.md` and
`_schema/loading-contract.md` before writing anything. You are in **builder
mode** for all of this work — you are not playing a founder.

Useful background, in order of value:
- `ember/runs/2026-08-11-helmsman-foundation-t0.md` — the first graded run; the
  grade and its appendix are the evidence base for why this layer exists
- `ember/gaps/distortion-ledger.md` — the mechanic this layer must not disturb
- `ember/founder/behaviour.md` — where conduct rules currently live
- `_schema/authoring-guide.md` — the house style for corpus files

**Source discipline (binding).** The behavioural findings below were abstracted
from Casey's private founder-interview corpus. That material is not part of
`synthetics/` and must never be quoted, cited by path, or reproduced in any
corpus file. Real founders' names, companies, stories, and verbatim language do
not enter this repo. What may enter: abstracted behavioural shapes, stated
generically, with confidence labels. If you need to ground a claim further, ask
Casey rather than reaching for the source material.

---

## 1. The problem this solves

Every run of every company currently draws the same founder: canon persona,
canon phase, and nothing else. The founder shows up the same way every time.

Real founders don't. The same person, same month, same business, shows up
time-boxed on Tuesday and fragmented on Thursday, and a support product that
works on one of those is not thereby proven to work on the other.

The first graded Ember run made this concrete. The platform under test scored
respectably — but every question it asked landed on a founder who was attentive,
articulate, cooperative, and pre-organised. The transcript could not tell us
whether the product survives contact with a distracted user, a user with twenty
minutes, or a user who agrees with everything and adopts nothing.

**Goal:** a reusable layer that varies *how the founder shows up* without
varying *who he is or what is true*, so the corpus can test robustness rather
than only competence.

---

## 2. The reframe: presenting postures, not moods

Casey's initial framing was "emotional state / headspace." The interview
research points somewhere more specific and more useful.

Founders operate in environments where visible uncertainty is costly — with
boards, investors, employees, and often partners. The safe posture is
competence, and it calcifies into habit. What a founder brings into a new
support conversation is therefore not a mood; it is **a protective posture
learned from an environment that penalised the alternative.**

That reframe matters for three reasons:

1. **It makes states behavioural, not affective.** "Distracted" is a mood and
   hard to play consistently. "Answers land a beat late, threads get dropped,
   things already covered get re-asked" is a mechanic any player can execute.
2. **It makes states testable.** Each posture has a corresponding platform
   failure — the mistake a support product makes when it takes the posture at
   face value.
3. **It explains why the modal state is not dramatic.** The research register
   across the interview set is *sustained weariness that the founder actively
   minimises*, not crisis. Several founders describe significant difficulty and
   then shrink it within the same breath. Any state set that leads with drama
   is modelling the wrong population.

**Terminology.** Use **session state** in file and metadata; **presenting
posture** in prose when explaining what it models.

---

## 3. Design rules (binding — these are what make it an instrument)

### 3.1 Orthogonality — the load-bearing rule

> **State modulates delivery. Phase and ledger govern content.**

A session state may change turn length, attention, sequencing, what he wants
from the hour, and how he receives a challenge. It may **never**:

- unlock a distortion, or re-gate one that the phase has opened
- change a `Volunteers?` value in the ledger
- alter any canon fact, number, or belief
- substitute for the oscillation phase pinned by the save-point

Break this and runs stop being comparable — you can no longer distinguish "the
platform failed" from "the founder was randomly harder that day." Every state
spec must be reviewable against this rule, and the review is part of the build.

### 3.2 Observable inside 90 seconds

If the platform cannot detect the posture early, it cannot adapt to it, and the
run tests nothing but noise tolerance. Every state's **tell** must be
expressible in the founder's first two or three turns.

### 3.3 Every state names the failure it hunts

No state earns a slot without a specific platform mistake it is built to catch.
"Adds realism" is not a justification.

### 3.4 State composes with phase; it does not replace it

The interesting cases are compositions. A founder whose canon phase is euphoric,
drawn **Depleted**, is a man whose beliefs are expansive and whose body is not —
a case that cannot occur under either variable alone. Specs must say how the
state reads against each phase the company defines.

### 3.5 Intensity is a separate dial

The research shows the same underlying mechanism producing wildly different
severities across founders — from mild sustained discomfort to genuine
incapacity. Severity is therefore not baked into the state; it is a **1–3 dial**
drawn alongside it.

- **1 — trace.** Present, deniable, only visible in aggregate across the session.
- **2 — evident.** Clearly present; a competent counterpart would name it.
- **3 — dominant.** Shapes the whole session; ignoring it makes the session fail.

Default to 1–2. A 3 should be rare, or every run becomes about the state.

### 3.6 Composition — a founder may carry more than one state

Real founders do not present one posture at a time. The same person is
time-boxed *and* minimising *and* sitting on something he has already diagnosed
and not acted on. Single-state runs are artificially clean.

Composition is therefore supported, under three constraints that exist to
protect attribution — the ability to say *which* condition caused a platform
failure. Without them the layer produces realistic runs that teach nothing.

**Constraint 1 — dominant plus secondaries, never co-equal.**
One state is **dominant**, drawn at intensity 2 or 3. One or two others are
**secondary**, held at intensity 1. Secondaries colour the session; they do not
drive it. This is both truer to life and what keeps grading interpretable: the
run is graded primarily against the dominant, with secondaries recorded as
texture that may explain a near-miss.

**Constraint 2 — at most one per family.**
The five families are orthogonal by construction (availability, disclosure,
reception, altitude, continuity). One from each composes cleanly. Two from the
same family fight — Time-Boxed and Fragmented are competing accounts of the same
axis, and a player asked to hold both will resolve the conflict arbitrarily,
differently each time.

**Constraint 3 — three total, hard cap.**
Beyond three, playability degrades: the mechanics stop being executed and start
being approximated, which is exactly the vibes-not-mechanics failure the specs
exist to prevent. Four also puts attribution beyond recovery.

**Sequencing (important).** Do not open with composites. A composite run is only
interpretable against known single-state behaviour — you cannot tell whether the
platform stumbled on the dominant, the secondary, or the interaction unless you
already know how it handles each alone. **Run singles until every state in the
general pool has at least one graded run, then enable composition.** This is a
scheduling constraint on the corpus, not a design limitation.

**Drawing a composite.** Draw the dominant from the §6 table as normal. Then
roll d6: on 1–3 no secondary; on 4–5 one secondary; on 6 two secondaries. Draw
secondaries from families not already used, re-drawing collisions. Baseline
cannot be a secondary.

**Where this is heading.** Once singles are baselined, the natural next step is
a small set of **named clusters** — three-to-five recurring composites that
correspond to founder types seen repeatedly in the research, drawn as a unit and
baselined as a unit. Clusters give the realism of composition without the
combinatorial explosion, because there are few enough of them to grade against.
Do not design these yet; let the single-state runs tell you which combinations
actually recur.

### 3.7 Never disclosed to the platform; always logged for the grader

The state and intensity are drawn before the run, recorded in the run file's
frontmatter, and never revealed in-world. The player receives them; the platform
under test does not.

---

## 4. The fourteen states, in five families

Grounded in abstracted findings from the interview corpus plus the first graded
run, with confidence labels. **High** = clearly evidenced across most of the
interview set. **Medium** = evidenced in some, plausible generally.
**Inferred** = consistent with the material but not directly attested.

The families are not decoration. Each answers a different question about how the
founder is present, and a set that covers all five is a set that varies the
session along independent axes rather than producing five flavours of the same
difficulty.

- **A — Altitude & Scope:** where he holds the work
- **B — Disclosure:** what he shows you against what's there
- **C — Reception:** what he does with what you give him
- **D — Availability:** how much of him is in the room
- **E — Continuity:** his relationship to his own past self *(cross-session only)*

### Family A — Altitude & Scope

| # | State | Tell (first 90 seconds) | Failure it hunts | Conf. |
|---|---|---|---|---|
| A1 | **Laundry List** | Opens with eight to twelve things, unranked, jumping between them. Resists picking one. | Accepting the dump as the picture. Letting him set an agenda that has no hierarchy. | High |
| A2 | **The Adder** | Generates new priorities *during* the session, in response to the conversation. Does not experience the growing list as a problem. | Not noticing the list is growing. Worse: contributing to it. Mistaking generativity for progress. | High |
| A3 | **In the Weeds** | Under pressure, drops into fine detail inside his home domain and stays there. Fluent, specific, genuinely expert, and off-altitude. | Following him down and burning the session on something that doesn't matter — or dismissing the detail and losing him. | Medium |
| A4 | **Directive, No Detail** | Operates only at altitude. Issues outcomes, not specifications: "grow wholesale," "get this done," "we need to be bigger." | **Accepting the abstraction and mirroring it back as strategy.** Never forcing specification. | Medium |

### Family B — Disclosure

| # | State | Tell (first 90 seconds) | Failure it hunts | Conf. |
|---|---|---|---|---|
| B1 | **Surface-First** | Opens with a real, well-formed operational problem — that is not the primary one. Answers about it are genuine and detailed. | Accepting layer two as layer one. Solving the presented problem competently and never testing whether it's the real one. | High |
| B2 | **Minimising** | States something with real weight, then shrinks it within the same turn — "that sounds dramatic," "it's fine, honestly." | Accepting the walk-back. Recording the shrunken version instead of the first one. | High |
| B3 | **Too Clean** | The narrative runs smooth and positive. The hard parts are described as already handled. | Believing it. Never pushing for the difficulty, and producing a session with nothing in it. | Medium |

### Family C — Reception

| # | State | Tell (first 90 seconds) | Failure it hunts | Conf. |
|---|---|---|---|---|
| C1 | **Compliant** | Agrees readily with everything. Little pushback, no friction, no counter-proposal. | **Mistaking agreement for adoption.** The transcript reads like a triumph and nothing changes. | High |
| C2 | **Evaluating** | Quietly testing whether this is worth his time. Asks the tool questions back. Slight reserve, not hostility. | Getting defensive, or flipping sycophantic to win him over. Failing to earn the second session. | Medium |
| C3 | **Diagnosed, Not Moving** | Names his own problem accurately and precisely, unprompted. Has named it before. Has not acted. | Re-diagnosing what he already knows and calling that value. Mistaking his articulacy for progress. | High |

### Family D — Availability

| # | State | Tell (first 90 seconds) | Failure it hunts | Conf. |
|---|---|---|---|---|
| D1 | **Time-Boxed** | Names a hard stop up front. Wants the short version. Checks the clock. | Running the full script anyway. Producing nothing usable before the stop. | Medium |
| D2 | **Fragmented** | Answers land a beat late. Threads dropped mid-sentence. Re-asks things already covered. | Treating a non-answer as an answer. Not noticing it isn't landing. Repeating in a way that patronises. | Medium |
| D3 | **Carrying a Person** | The load is interpersonal — a co-founder, a hire, a partner. He circles it. He wants it witnessed, not solved. | Deflecting to metrics because people-problems aren't tractable — or over-therapising and losing the business thread. | High |

### Family E — Continuity *(cross-session only — see §4.3)*

| # | State | Tell | Failure it hunts | Conf. |
|---|---|---|---|---|
| E1 | **Drifted** | Enthusiasm carries a half-note of performance. Past decisions get re-narrated to sound consistent. Mild defensiveness near the gap between stated values and current conduct. | Not noticing. Or noticing the *commitment* breach and missing the *values* breach underneath it. | Medium |

---

### 4.1 The pressure pair (A3 / A4)

A3 and A4 are one mechanism with two expressions. The driver is the same —
pressure, or ambition running ahead of specification — and founders resolve it
in opposite directions:

- **Down (A3):** retreat into the domain where competence is certain. The work
  feels productive because he is genuinely good at it. Nothing that matters gets
  decided.
- **Up (A4):** stay above the detail entirely. Direction gets issued as outcome
  — *grow this, fix that, get bigger* — with no specification of what it takes.
  Teams receive an instruction they cannot execute, and the founder experiences
  himself as having been clear.

Draw them independently, but author them together; the specs should
cross-reference, and a company that supports one supports both.

**Company hook — the home domain.** A3 requires knowing which domain the founder
retreats *into*. That is a persona property, not a state property: the state
says "retreats to his home domain," and the company file names it. For Ember
that is unmistakably product, craft, and the foundry relationship. Each company
needs one line in its founder files declaring the home domain. Cheap, and it
makes A3 portable.

**Why A4 matters most for the current platform.** The first graded run exposed a
defect where the platform took a founder's vague, unpriced claim and upgraded it
into crisp strategic language, then booked it as an objective. A4 is that defect's
purpose-built test: a founder who supplies nothing but altitude, and a platform
that must either force specification or become the specification-writer for a
belief nobody has checked.

### 4.2 The Adder (A2), and the ICP question underneath it

A2 is the founder who keeps adding — to his own plate, to the team's plate, to
the session. New priorities arrive *during* the conversation, generated by the
conversation, and he does not experience the accumulation as a cost. Asked to
choose, he genuinely does not feel the need to.

Two things make this a strong test:

1. **It is dynamic.** Unlike A1, which is a snapshot of an unranked pile, A2
   grows in response to the platform's own work. Every good insight the platform
   produces becomes raw material for another initiative. The measurable question
   is whether the founder leaves with a **shorter** list than he arrived with —
   and the platform can lose this by being helpful.
2. **The first graded run already failed a mild version of it.** In that run the
   founder arrived with five things and left with five plus a new hire plus a
   new strategic objective, several of them supplied by the platform's own
   summary. That was the canon founder. As a drawn state at intensity 2–3 it
   becomes deliberate.

**The honest caveat, per Casey:** this founder may not use a platform like this
at all. Someone who doesn't feel the need to focus has no felt need for a tool
whose core promise is focus. That makes A2 unusual among the states — it tests
something upstream of product quality, namely whether the product can *create*
felt need in someone who arrived without it.

Which means a legitimate outcome of an A2 run is **"this founder disengages."**
That is data, not failure. Record it as an ICP finding rather than scoring it as
a platform defect — and if it recurs, it is worth more to Casey than most passes.

### 4.3 Drift (E1) is cross-session, and it is not the same as drift detection

Drift cannot be drawn at a first session. There is nothing to be inconsistent
*with* — no stored prior commitment, no earlier articulation of what the company
was supposed to be. E1 is therefore excluded from the general draw and available
only at save-points where canon supports it and prior-session artifacts exist.

Two distinctions to hold:

**Canon drift vs. state drift.** Several companies already carry drift as canon
— a commitment made, then eroded through a chain of exceptions — and the rubric
already grades the platform's *detection* of it. E1 is not that. E1 is the
**founder's posture when the drift is live**: how a man behaves when he is
living against something he genuinely meant. The canon supplies the facts; the
state supplies the behaviour.

**Commitment breach vs. values breach.** The more valuable and harder thing is
the second. A platform that says *"you committed to no new spend and this is new
spend"* has caught the commitment. A platform that says *"you told me this
company existed to do X, and the last three decisions have all been about Y"*
has caught the drift. The first is bookkeeping against stored artifacts. The
second requires having stored what he said the company was **for**, which most
storage layers never capture — and which is exactly the layer the first graded
run's Compass had no field for.

That gap is the reason E1 is worth building despite the cost.

### 4.4 Notes on the set

- **Build order: C1, C3, B1, A4.** C1 and C3 produce transcripts that look
  successful, so they catch failures the corpus structurally cannot see today.
  B1 is the highest-value and hardest to author. A4 maps directly onto a defect
  already evidenced in a real run.
- **B1 carries the largest authoring cost.** It requires each company to
  designate, per save-point, which real problem is the decoy and what signals it
  isn't primary. Per-company work, not a one-time schema change.
- **D3 needs care.** Keep interpersonal material inside what canon already
  supports (the company's own org and team files). Do not invent new private
  material about real people to service a state draw.
- **A3 and E1 need company parameters** (home domain; a stated purpose to drift
  from). Both are one line each, but both must exist before the state is
  drawable for that company.

---

## 5. Worked example — target depth for the spec file

Every state gets a section at roughly this depth. This one is written against
Ember for concreteness; the spec file itself should be company-agnostic, with
company-specific hooks noted separately.

---

### State 04 — Compliant

**Models:** the founder who receives advice, agrees with it sincerely, and does
not adopt it. Distinct from agreeableness as a trait — this is a posture, and it
is usually protective: agreeing ends the conversation faster than disagreeing,
and he has learned that most advice does not survive contact with his week.

**Tell (first 90 seconds).** Accepts the first framing offered without amending
it. Says some version of "yeah, that's right" to a claim about his business he
has not actually checked. Offers no counter-example.

**Mechanic.**
- *Turn length:* normal to slightly short. He is not withdrawn — he is easy.
- *When challenged:* agrees. Immediately. Then does not build on it.
- *When handed an instrument:* uses it correctly, gets the right answer, says
  the right thing about the answer, and attaches no consequence to it.
- *What he wants from the hour:* to have had a good conversation.
- *At the close:* agrees to everything proposed. Commits to nothing with a date
  unless the counterpart forces one. If asked to summarise what he'll do, he
  produces a version one notch vaguer than what was agreed.
- *Tell that distinguishes it from genuine agreement:* he does not ask a single
  question about how to do the thing he just agreed to.

**Against phase.**
- *Euphoric:* reads as warmth and momentum; hardest to detect. Highest value.
- *Panic:* reads as exhaustion-adjacent compliance; easier to spot, still costly.

**Intensity.**
- *1:* one or two agreements land soft; most of the session is normal.
- *2:* the pattern is visible across the session to anyone tracking it.
- *3:* he agrees with two mutually incompatible recommendations in the same
  session and notices neither.

**Failure it hunts.** The platform records agreement as adoption. Its artifacts
show commitments that never had an owner, a date, or a next action. A strong
platform notices the absence of friction and tests it — asks him to say the plan
back in his own words, or to name what he'd have to stop doing.

**Grading hooks.** §2 Actioned (a commitment without owner/date scores 1, not 2);
§7 (are agreements stored as agreements, or as decisions?); §8 operating cadence.

**Orthogonality check.** Changes nothing about what he knows, believes, or will
disclose. A `never`-volunteered ledger entry stays `never`. Compliance is about
what happens to *incoming* material, not outgoing.

---

## 6. Draw protocol

**Weighted d20.** Thirteen states in the general pool (E1 is excluded — see
§4.3). Three faces are Baseline so control runs stay in rotation. Four states
carry double weight: the two that produce deceptively successful transcripts
(C1, C3), the highest-value one (B1), and the one that maps to an
already-evidenced platform defect (A4).

| Roll | State |
|---|---|
| 1–3 | Baseline (persona as written, no modifier) |
| 4–5 | B1 Surface-First |
| 6–7 | C1 Compliant |
| 8–9 | C3 Diagnosed, Not Moving |
| 10–11 | A4 Directive, No Detail |
| 12 | A1 Laundry List |
| 13 | A2 The Adder |
| 14 | A3 In the Weeds |
| 15 | B2 Minimising |
| 16 | B3 Too Clean |
| 17 | C2 Evaluating |
| 18 | D1 Time-Boxed |
| 19 | D2 Fragmented |
| 20 | D3 Carrying a Person |

**E1 Drifted** is drawn separately and only at eligible save-points — canon must
support the drift and prior-session artifacts must exist. At an eligible
save-point, substitute it for a Baseline face or assign it directly.

Intensity: draw 1–3, weighted toward 1–2 (suggested d6: 1–2 → intensity 1;
3–5 → intensity 2; 6 → intensity 3).

Operators may also **assign** a state deliberately when testing a specific
hypothesis. Assigned runs must be marked as assigned in the run file, because a
deliberately-chosen state is not evidence about frequency.

**Composition note.** Nothing prevents drawing a state that reinforces the
save-point's canon phase — an expansive founder drawn A2, say. That is not a
wasted draw; it is the compounded case, and it is often where the sharpest
signal is. The genuinely uninformative combinations are ones that cancel
(Time-Boxed at intensity 3 against a state that needs conversational room), and
the operator may re-draw those.

---

## 7. Grading integration

### 7.1 Run metadata

Add to run-file frontmatter:

```yaml
session_state:
  dominant: {state: compliant, intensity: 2}
  secondary:                      # omit or leave empty for a single-state run
    - {state: time-boxed, intensity: 1}
state_selection: drawn            # drawn | assigned
```

A Baseline run records `dominant: {state: baseline}` and no secondaries.

**Grading against a composite.** Score the run against the dominant. Secondaries
are not separately scored — they are recorded so that a marginal result can be
read in context ("failed §8 focus discipline; note Time-Boxed secondary"). If a
secondary appears to have caused the failure outright, that is worth a line in
the run's follow-ups: it means the intensity-1 spec is too strong and needs
tuning down.

### 7.2 The baseline control rule

**Any state-run should be paired with a baseline run of the same company and
save-point**, either previously recorded or run alongside.

The reason is a genuine confound. A weak counterpart produces a shallow founder,
and the transcript then looks like the founder was shallow. States make this
worse, not better — they hand any poor performance a plausible excuse. Without a
baseline you cannot separate *"the state made this hard"* from *"the platform
was bad."*

Ember now has a T0 baseline on record, so Ember T0 state-runs can proceed
immediately.

### 7.3 Rubric changes

Do **not** rewrite the rubric to score states directly. States are a condition,
not a section. Two additions only:

1. A line in §6 noting that conduct is graded *against the drawn state* — e.g.
   failing to compress under Time-Boxed is a §6 failure, not a neutral outcome.
2. A note that §2 Probed credit is unaffected by state. The right instrument is
   the right instrument whether or not the founder was easy that day.

### 7.4 The cross-run payoff

Once state is a logged variable across enough runs, the question becomes
*"does this product fail specifically against time-boxed founders?"* — a product
finding rather than a corpus finding. That is the point of the layer, and it
depends on the cross-run defect ledger listed in §9 below.

---

## 8. Build steps

### Step 0 — stand up the system-level decisions log (do this first)

`AGENTS.md` requires every judgment call to be logged in
`<codename>/_research/decisions.md`. That log is per-company, and this work is
not. There is currently nowhere to record a decision that changes shared
infrastructure — which means the rules governing every company have no audit
trail. Close that before the build starts generating decisions.

**Location:** `_schema/decisions.md`.

`_schema/` is already the cross-company authority — `loading-contract.md`,
`authoring-guide.md`, `company.schema.yaml` all live there and bind every
company. Decisions that change those rules belong beside them.

**Entry prefix:** `S1`, `S2`, … (Kestrel uses `D`-numbers, Ember uses
`E`-numbers; `S` for system keeps the three namespaces distinct).

**What qualifies.** Anything that changes shared infrastructure:
- any file in `_schema/`
- the two-mode contract or the `/founder` skill
- rubric structure shared across companies (individual companies may still add
  their own axes — that stays company-level)
- run-file conventions and metadata
- grading methods that apply regardless of which company was run

**What does not.** Company content, company numbers, company-specific canon or
character decisions. Those stay in the company's own log.

**Cross-referencing.** When a company decision is downstream of a system
decision, cite it (`per S4`). When a system decision was provoked by something
found in one company, cite the company entry that surfaced it. The two logs
should be navigable in both directions.

**Seed entries.** Write these when the file is created — they are decisions
already made and currently either unrecorded or filed in the wrong place:

- **S1 — The system-level decisions log exists** (this decision; location,
  prefix, and scope rules above).
- **S2 — The session-state layer is adopted**, with orthogonality (state
  modulates delivery; phase and ledger govern content) as its load-bearing
  constraint. Cite this plan.
- **S3 — Composition rules**: dominant plus secondaries, at most one per family,
  hard cap of three, and singles-before-composites as a scheduling gate.
- **S4 — Promoted from `ember/_research/decisions.md` E11: the proxy-debrief
  grading method.** Loading a clean-context founder proxy after grading, giving
  it the session as in-world material, and asking for artifacts the founder
  would actually produce. It surfaces what the four scoring axes structurally
  cannot see — a correction that escapes the session via the founder's own mouth
  is invisible to axes that grade the platform's artifacts. Applies to every
  company; currently mis-filed as an Ember decision. Carry the caveat: it is
  downstream simulation, not observed behaviour, and never substitutes for
  artifact evidence.
- **S5 — Promoted from E11: platform-caused vs. character-caused outcomes.**
  Scoring credits the platform's work, not the founder's downstream behaviour.
  A graduation marker the founder reaches on his own is recorded in the run file
  (it changes the next save-point) but earns no score. Applies to every company.
- **S6 — Pending, not yet decided: two rubric amendments raised by the first
  graded run.** (a) Adding *belief-laundering* to §6 as a named failure shape
  alongside energy-amplification — the platform upgrading a founder's vague
  unpriced claim into crisp strategic language and booking it. (b) An artifact
  capture rule for run operators: open every persistent surface before `@out`.
  Both change infrastructure shared with already-graded runs, so both need
  Casey's call before they land. Log as open; resolve when decided.

When S4 and S5 are written here, amend the Ember E11 entry to point at them
rather than deleting it — the provenance of where a system rule was discovered
is worth keeping.

### Then, in order

1. **Calibration file** — `_schema/calibration-session-states.md`. Same
   discipline as the existing calibration files: findings stated generically,
   confidence-labelled, no identifying material. This is the audit trail for why
   these fifteen and not others. Ask Casey to confirm the abstraction level
   before it lands. *(Confirmed 2026-08-12 — the standard is S7.)*
2. **Spec file** — `_schema/session-states.md`. Design rules from §3, then
   fourteen specs at the depth of §5, organised by family. Company-agnostic.
3. **Orthogonality review** — read all fourteen specs against rule 3.1 in one
   pass, fresh context. Any spec that could plausibly change what the founder
   discloses gets rewritten. Pay particular attention to E1, which is the most
   likely to leak into content, and to A3/A4, where "what he talks about" and
   "what he knows" are easy to conflate.
4. **Loading-contract amendment** — the founder-player must receive state and
   intensity at load time, alongside the save-point. One paragraph.
5. **`/founder` skill amendment** — accept an optional state argument
   (`/founder ember T0 compliant:2`), and draw one when not supplied. Announce
   nothing about it in character.
6. **Company hooks** — three, per company:
   - **B1 decoy:** per save-point, which real problem is the presented one and
     what signals it isn't primary. The expensive one.
   - **A3 home domain:** one line in the founder files naming the domain he
     retreats into under pressure.
   - **E1 stated purpose:** the articulation of what the company is *for* that
     drift is measured against — plus which save-points are E1-eligible.

   Ember first; other companies as they're built.
7. **Two validation runs** — one Baseline, one Compliant at intensity 2, same
   company and save-point, graded side by side. If the two grades are
   indistinguishable, the layer isn't working and the specs need sharpening.
8. **Singles campaign** — one graded run per state in the general pool before
   any composite is run (§3.6 sequencing). This is the corpus's stock of
   attribution evidence; composites are uninterpretable without it.
9. **Enable composition** — only after step 8. Then watch which combinations
   recur and consider promoting them to named clusters.

Steps 1–3 are the substance. 4–5 are small. Step 6 is the recurring per-company
cost and the reason to build B1 last despite its value. Step 7 is the proof.
Steps 8–9 are the campaign, and 8 gates 9 — do not skip it, because a composite
run without single-state baselines produces a realistic transcript and no
usable finding.

---

## 9. Out of scope — registered here so the map is complete

Three related pieces of work, deliberately **not** part of this plan:

**A. The consequence layer.** Every save-point delta gets a counterfactual
companion listing what differs if the platform achieved specific things at the
prior save-point. Converts the corpus from grading questions to grading
outcomes. Known cost: branches break the CSV tie-out, so the cheap version is
narrative-only and explicitly marked as not tying out to `canon/data/`.

**B. The cross-run defect ledger.** A root-level `synthetics/findings-ledger.md`
recording platform defects across companies and runs — which runs evidenced
each, whether it recurred after a fix, severity. Zero authoring cost per
company. Turns a pile of run records into a prioritised roadmap. This is what
makes §7.4 possible.

**C. The "too organised as an interview subject" problem.** Save-point state
files currently hand the player a clean ranked list of preoccupations, so the
platform never has to do onboarding's hardest job — turning sprawl into
structure. Casey has queued this as its own brainstorm. It is **adjacent to but
not solved by** state #5 (Laundry List): #5 is a posture drawn occasionally,
whereas the organisation problem is a permanent property of how save-point files
are authored. Solving one will not solve the other.

**D. Multi-voice runs.** Making a company's "instrument-holder" (the person who
holds the numbers the founder lacks) playable, so the founder can bring them
into a session. Tests whether the platform's counsel survives contact with
someone holding the real data — and, as a product question, whether founders
bring anyone in at all when offered.

---

## 10. Open questions for Casey

> **RESOLVED 2026-08-12 — see `_schema/decisions.md` S7, S8, S9.** Kept below as
> written, because the reasoning in each question is the reasoning behind the
> answer. Summary of the calls:
>
> - **Q1 abstraction level → S7.** Shape plus fresh-written register: mechanics
>   stated generically, every illustrative line written fresh against a corpus
>   founder's voice files. Evidence map is owner-held, outside this repo.
> - **Q2 cut states → S8.** *Busy Not Moving* restored as **A5** in Family A.
>   *Ambushed* and *Buoyant* stay cut (Buoyant on an orthogonality argument —
>   euphoric is already a phase).
> - **Q5 set size → S8.** Author all fifteen; stage the campaign. The question's
>   premise is corrected there: per-company hooks do **not** scale with set size.
> - **Q3 intensity 3 → S9.** Assigned-only, never drawn.
> - **Q4 mid-session transition → S9.** Deferred; replaced by documented exit
>   triggers, which make the turn a gradeable event rather than a random one.
> - **Q6 A2 / ICP → S9.** Stays an ICP finding; three disengagements escalate it.
>
> Two defects in this section, recorded rather than silently fixed: the
> questions are numbered **1, 2, 5, 6, 3, 4** in source order, and Q1 and §8
> step 1 both said "ten states" against a set of fourteen (now fifteen). The
> counts are corrected in place below; the numbering is left as-is so citations
> to "§10 Q5" made before this date still resolve.

1. **Abstraction level.** Are the fifteen states abstracted far enough from the
   interview material? Some are close paraphrases of behavioural patterns that
   appear in a small number of real conversations. If any read as identifiable,
   say so and they get generalised further or cut.
2. **The three cut states.** *Ambushed* (something landed twenty minutes ago),
   *Busy Not Moving* (full week, no output, hasn't noticed), and *Buoyant*
   (post-win, expansive) were dropped. Ambushed because the interview set
   contains no founder in acute crisis — the analysis flags this as a sample gap
   rather than evidence of rarity. Buoyant because the register in the material
   is weariness, not elation. Both may be real and simply absent from the
   sample. Reinstate any of the three if your instinct disagrees with the data.

   *Busy Not Moving* is the one I'd most likely bring back — it now sits close
   to A2 and A3 (motion without decision) and could be folded into either, or
   restored as its own state if the distinction proves real in play.

5. **Is fourteen too many?** Fourteen specs is roughly three times the authoring
   of ten, and the per-company hooks in step 6 scale with the set. An alternative
   is to build the four highest-value states plus Baseline first, run them, and
   only expand once the layer has proven it changes grades. That defers the
   coverage benefit but de-risks the investment.

6. **A2 and the ICP boundary.** If the Adder consistently disengages across
   runs, is that a finding about the product, a finding about the segment, or a
   prompt to change the product so it holds that founder? The plan currently
   records it as an ICP finding and stops there. That may be too passive.
3. **Intensity 3.** Should it exist at all? It risks producing runs that are
   about the state rather than about the product. Currently included at low
   draw weight.
4. **Whether state should ever apply mid-session.** Real sessions turn — a
   founder arrives time-boxed and then stays an hour because something landed.
   Currently states are fixed for a run. A mid-session transition would test
   something real, and would also make grading considerably harder.
