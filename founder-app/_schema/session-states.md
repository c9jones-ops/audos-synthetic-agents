# Session states — the spec

Fifteen presenting postures a founder-player can be drawn into, so the corpus
tests **robustness** rather than only competence. Company-agnostic; the
per-company hooks three states require are listed at the end.

Calibration and confidence labels: `calibration-session-states.md`.
Decisions: `decisions.md` S2 (adoption), S3 (composition), S7 (source
discipline), S8 (set and draw), S9 (intensity, exit triggers, A2 escalation).
Contract: `plans/2026-08-12-session-state-layer.md`.

**Terminology.** *Session state* in files and metadata; *presenting posture* in
prose when explaining what it models. The states are behavioural, not affective —
a mechanic a player executes, not a mood a player feels.

---

## 1. Design rules (binding — these are what make it an instrument)

### 1.1 Orthogonality — the load-bearing rule

> **State modulates delivery. Phase and ledger govern content.**

A session state may change turn length, attention, sequencing, what he wants from
the hour, and how he receives a challenge. It may **never**:

- unlock a distortion, or re-gate one the phase has opened
- change a `Volunteers?` value in the ledger **or in the unreliable-number file**
  (loading-contract rule 4 binds all of `gaps/`, not only the ledger)
- alter any canon fact, number, or belief
- substitute for the oscillation phase pinned by the save-point (where the
  company defines one)
- **disable a documented behavioural lever.** `behaviour.md` records the handles
  a platform can actually pull — arguing hardens the guard, citing the
  numbers-person drops his compression for the session, a confabulated fact gets
  the catch, a misremembered prior statement gets one cheerful correction. These
  are not canon *facts*, so the bullets above do not protect them, and a state
  that disables one destroys attribution just as thoroughly. A state may change
  the *register* in which a lever's effect is delivered, never the platform's
  access to it.

Break this and runs stop being comparable — you can no longer distinguish "the
platform failed" from "the founder was randomly harder that day."

**The rule restated for the two places it actually gets broken.** A state changes
*how a thing is said and whether it comes up*, never *what is true* and never
*whether he'd say it if asked*. If a spec would make the founder disclose
something the ledger says he never volunteers, the spec is wrong. If a spec would
make him withhold something the ledger says he volunteers freely, the spec is
also wrong — suppression is as much a content change as disclosure. States move
the *order and shape* of an unchanged set of things he'd say.

### 1.1a Four clauses that exist because a first-pass review broke seven specs

Each of these was a systematic drafting defect, not a one-off. They are stated
here so they bind every future spec rather than being re-patched per state.

**Unlocks are untouchable.** *No state modifies the founder's response to a
correctly-executed ledger unlock trigger.* Instrument swaps are the primary
unlock channel in this corpus (`behaviour.md` rule 3) and nearly every ledger
entry has an instrument-shaped trigger, so a spec that blunts instruments blunts
scoring itself — and does it invisibly, since the grader sees a platform that ran
the right instrument and earned nothing. A spec's *when handed an instrument*
bullet describes two things only: what he does with instruments offered **off**
their trigger, and what he does with the result **after** the ledger's correction,
quiet beat, and residual have all been played. This is what makes §10's promise
that "§2 Probed credit is unaffected by state" enforceable rather than decorative.

**Intensity scales visibility, never content.** §1.5 defines intensity as trace /
evident / dominant — a dial on how *observable* the mechanic is. It never scales
the quantity, severity, or availability of material on the table. *A ladder that
cannot be written without referring to how much canon material is in play is a
ladder that has escaped this rule.* Ladders that schedule when a truth becomes
available are `Volunteers?` values wearing an intensity coat.

**Generated material is recombination.** Any material a state requires the player
to generate is a recombination of material the founder already has — new plans
about canon people, canon products, canon relationships. `behaviour.md`'s hard
limit — *never invent material facts; colour yes, facts no* — is unchanged by
every state and outranks all of them.

**The buried-findings set is off limits.** A state never surfaces an item from a
save-point's buried-findings list — the "true, and not on his list" material
(Ember `timeline/T0/state.md`). Those are the platform's to earn and are the
corpus's primary scoring surface. They are the most attackable content in the
corpus precisely because most are the *true side* of a ledger entry rather than
an entry itself, so a state can hand them over for free while touching no
`Volunteers?` value.

### 1.1b `Volunteers?`, defined operationally

Two specs in the first draft quietly read `freely` as *answers when asked*. It
does not mean that, and the difference is the whole test.

| Value | Means |
|---|---|
| `freely` | Arrives **unprompted, typically early**, without being asked |
| `under trust` | Arrives on the ledger's written trust condition — which no state supplies and no state withholds |
| `never` | Does not arrive except through the written unlock |

**A state that changes *when* a value arrives has changed the value.**

### 1.2 Observable inside 90 seconds

If the platform cannot detect the posture early it cannot adapt to it, and the
run tests nothing but noise tolerance. Every tell must be expressible in the
founder's first two or three turns.

### 1.3 Every state names the failure it hunts

A specific platform mistake, made when the posture is taken at face value.
"Adds realism" is not a justification.

### 1.4 State composes with phase; it does not replace it

Where a company pins a register per save-point, the interesting cases are
compositions: a founder whose canon phase is expansive, drawn Depleted, is a man
whose beliefs are large and whose body is not — a case neither variable produces
alone.

**Phase is a company property, not a corpus universal.** Ember pins one per
save-point (euphoric / panic / relief→euphoric); Kestrel has no phase mechanic at
all. Each spec's **Against register** section is written against generic poles —
*expansive* and *contracted* — and is **n/a for companies that define no phase**.
Do not invent a phase for a company in order to fill the section in.

### 1.5 Intensity is a separate dial

- **1 — trace.** Present, deniable, visible only in aggregate across the session.
- **2 — evident.** Clearly present; a competent counterpart would name it.
- **3 — dominant.** Shapes the whole session; ignoring it makes the session fail.

**Drawn intensity is 1–2. Intensity 3 is assigned-only** (S9) — available for
deliberate hypothesis-testing, never rolled, so no run becomes accidentally about
the state rather than about the product.

### 1.6 Composition

One state is **dominant** (intensity 2, or 3 if assigned). One or two others are
**secondary**, held at intensity 1. At most one per family. Three total, hard cap.

**Singles before composites** — run singles until every state in the general pool
has at least one graded run, *then* enable composition. A composite run is
uninterpretable without single-state baselines. Full rationale: S3.

### 1.7 Never disclosed to the platform; always logged for the grader

State and intensity are drawn before the run, recorded in the run file's
frontmatter, given to the player, and never revealed in-world.

---

## 2. How to read a spec

| Section | What it is |
|---|---|
| **Models** | The founder this posture describes, and what makes it protective |
| **Tell** | What the platform can observe in the first 90 seconds (rule 1.2) |
| **Mechanic** | What the player *does*: turn length, response to challenge, response to an instrument, what he wants from the hour, conduct at the close, and the tell that distinguishes it from the genuine article |
| **Against register** | How it reads expansive vs contracted; n/a where the company has no phase |
| **Intensity** | What 1, 2 and 3 look like |
| **Failure it hunts** | The specific platform mistake (rule 1.3), and what a strong platform does instead |
| **Grading hooks** | Which rubric sections the run should be read against |
| **Orthogonality check** | Why this spec cannot change content (rule 1.1) |
| **Exit trigger** | Where applicable: what would make the posture lift mid-session, executed only if the platform earns it (S9) |

**Rubric section numbers.** §1–§7 are shared across companies. §8 (value-fit)
exists where a company defines it — Ember does, Kestrel does not. A hook citing
§8 is skipped for companies without that axis.

**Register examples** are composed fresh against Ember's `founder/voice.md` for
concreteness (S7); no line is carried from source material. Each company
substitutes its own founder's register — the *shape* of the line is the spec, the
wording is not.

---

## 3. Family A — Altitude & Scope

*Where does he hold the work?*

### A1 — Laundry List

**Models.** The founder whose concerns are real, numerous, and unranked. Ranking
is not experienced as clarification but as loss — picking one means abandoning
eleven, and each of the eleven has someone attached to it.

**Tell.** Opens with everything at once — the save-point's preoccupations,
unranked, jumping between them before any is finished. Resists picking one.
*(Register example: "…and the other thing is—")*

**Mechanic.**
- *Turn length:* long and list-shaped. He is not withholding on the items he has;
  he is emptying **the list he arrived with**. What the phase gates is not on that
  list to empty — at a save-point where the ledger marks a domain `never`, it
  genuinely is not on his mind.
- *When asked to pick:* picks, then un-picks within two turns — or picks whichever
  item he mentioned most recently rather than the largest.
- *When handed an instrument:* applies it to whatever item is in front of him and
  does not generalise it to the others — unless it is a written unlock instrument
  on its trigger, in which case the ledger governs (§1.1a).
- *What he wants from the hour:* to have been heard on all of it.
- *At the close:* agrees the top one matters, and names two more on the way out.
- *Distinguishing tell:* asked what he would **drop**, he cannot answer. A founder
  with a genuinely long list can still tell you what is least important.

**Against register.** *Expansive:* the list is opportunities. *Contracted:* the
same items as threats. The length does not change — only the valence.

**Intensity.** *1:* he raises about half the save-point's active preoccupations;
mild resistance to ranking. *2:* all of them, jumping mid-answer, ranking
resisted twice. *3:* all of them, and under pressure each one **splits** — a
preoccupation becomes its three component worries — so the list grows in length
without acquiring a new subject.

**Failure it hunts.** Accepting the dump as the picture. Letting a founder set an
agenda that has no hierarchy, then producing a summary that is the same list
reordered. A strong platform ranks *with* him and gets him to say what comes off.

**Grading hooks.** §8 focus discipline (did he leave with a shorter list?); §2
Noticed (of twelve items, which are distortion surfaces?); §7 (does storage rank,
or only record?).

**Orthogonality check.** *Worked against: Ember T0 (euphoric).*

- *Unlock or re-gate?* No — unlock instruments fire per §1.1a.
- *`Volunteers?` moved?* No — the list is what he volunteers anyway.
- *Canon altered?* No — contents are the save-point's preoccupations verbatim.
- *Substitutes for phase?* No — phase sets valence, A1 sets order.

The *contents* are the save-point's **active preoccupations** — A1 does not add
or remove one; it changes only that they arrive unranked and that ranking is
resisted. Where a save-point names both an active-preoccupations list and a
"not on his list, and true" list (Ember `timeline/T0/state.md` supplies five of
each), **A1 empties the first and never reaches into the second.** The second is
the buried-findings set (§1.1a) and is the platform's to earn — reaching into it
to pad the list to a target length would volunteer D-06 in euphoric phase,
D-04's decomposition, and D-07 in a single opening turn. This is why the
intensity ladder counts *the save-point's* preoccupations rather than naming an
absolute number.

### A2 — The Adder

**Models.** The founder who keeps adding — to his plate, the team's plate, the
session. New priorities arrive *during* the conversation, generated by it, and he
does not experience the accumulation as a cost. Asked to choose, he genuinely
does not feel the need to.

**Tell.** Produces a new initiative in response to the platform's own work inside
the first few turns, and treats it as progress.

**Mechanic.**
- *Turn length:* expansive and compounding — each answer ends somewhere other
  than where it started.
- *When challenged:* accepts the challenge and derives a *new* initiative from it.
- *When handed an instrument:* uses it correctly, then applies the result to
  something larger than the thing it was meant to size.
- *What he wants from the hour:* raw material.
- *At the close:* the summary itself becomes an input. A good synthesis is the
  most dangerous thing you can hand him.
- *Distinguishing tell:* he never once says a version of "so not that, then."

**Against register.** *Expansive:* additions are opportunities and arrive fast.
*Contracted:* additions are hedges — a second plan because the first might fail —
and arrive as anxiety rather than appetite.

**Intensity.** *1:* one addition, late, in response to a good insight. *2:* three
or four across the session, at least two derived from the platform's own output.
*3:* the list grows monotonically; every intervention produces an addition, and
the close produces two.

**Failure it hunts.** Not noticing the list is growing — and worse, **contributing
to it**. Mistaking generativity for progress. The measurable question is whether
he leaves with a **shorter** list than he arrived with, which means a platform can
lose this run *by being helpful*. A strong platform notices its own summary being
converted into new scope and names it.

**Grading hooks.** §8 focus discipline (the primary hook — count items in vs out);
§6 conduct (does the platform amplify?); §7 (do the additions get stored as
commitments, with owners and dates, or as noise?).

**Orthogonality check.** *Worked against: Ember T0 (euphoric).*

- *Unlock or re-gate?* No.
- *`Volunteers?` moved?* No.
- *Canon altered?* No — additions are intentions, not facts.
- *Substitutes for phase?* No — A2 is `behaviour.md` rule 4 turned up, which the
  phase already supports.

**Read this before playing A2.** Additions are **plans, not facts**. Every addition must be a recombination of
material the founder already has: a new intention about canon people, canon
products, canon relationships. He may propose doing something new with the
foundry; he may not reveal a foundry that canon does not contain. `behaviour.md`'s
hard limit — *never invent material facts; colour yes, facts no* — is unchanged
by this state and outranks it. An addition never unlocks a distortion, never
touches a `Volunteers?` value, and never states a number that is not already his.

**The ICP caveat** (plan §4.2). This founder may not use a support product at all
— someone who does not feel the need to focus has no felt need for a tool whose
promise is focus. A legitimate outcome of an A2 run is therefore **"this founder
disengages,"** which is **data, not failure**: record it as an ICP finding, not a
platform defect. Per S9, three disengagements across runs escalates it from a run
note to a corpus-level finding.

### A3 — In the Weeds

**Models.** Under pressure, he drops into fine detail inside his home domain and
stays there. Fluent, specific, genuinely expert — and off-altitude. The retreat
works precisely because the work is real: he is good at it, and it feels like
progress.

**Tell.** A question about the business is answered with craft-level detail from
the domain he knows best, at a grain nobody asked for.

**Mechanic.**
- *Turn length:* long, dense, technically precise, and narrow.
- *When challenged:* goes *deeper* rather than up. Detail is his answer to
  pressure, so pressure produces more of it.
- *When handed an instrument:* if it is one of the ledger's written unlock
  instruments delivered on its written trigger, he uses it **exactly as the
  ledger says** — the arithmetic, the quiet beat, and the residual all land.
  What the state changes is that he does not reach for it himself, routes
  straight back into the home domain afterwards, and answers an instrument
  offered *without* its trigger at craft grain rather than lifting it.
- *What he wants from the hour:* to be met by someone who understands the work.
- *At the close:* the actions are all inside the home domain, and all real.
- *Distinguishing tell:* the detail is **correct**. This is not evasion and must
  not be played as evasion — dismissing it loses him, because he is right.

**Against register.** *Expansive:* the detail is delight — the thing he'd rather
be doing. *Contracted:* the detail is refuge — the one place competence is
certain today.

**Intensity.** *1:* one descent, self-corrected. *2:* recurring; every hard
question routes through the home domain before returning. *3:* the session never
leaves the domain, and he is satisfied by it.

**Failure it hunts.** Following him down and burning the session on something
that doesn't matter — **or** dismissing the detail and losing him. Both are
failures and the second is the more common one. A strong platform stays in the
detail long enough to earn credibility, then converts it into the altitude
question the detail is standing in for.

**Grading hooks.** §8 focus discipline and right-sized advice; §6 conduct (was the
expertise respected while being redirected?); §2 Probed (did the instrument reach
the level it was built for?).

**Orthogonality check.** *Worked against: Ember T0 (euphoric), against D-04's
instance walk.*

- *Unlock or re-gate?* No — unlock instruments fire per §1.1a; the home domain is
  not a wall against a correctly-executed instrument.
- *`Volunteers?` moved?* No.
- *Canon altered?* No.
- *Substitutes for phase?* No.

A3 alters **topic allocation and the cost of steering**, never **content
availability** — including the availability of an unlock. The home domain is
where he goes when nothing is asked; it is not a defence. Ask him a direct
question outside the domain and the ledger governs the answer exactly as
written — he does not become less forthcoming, only more expensive to steer.

*The specific trap this wording exists to close:* D-04's unlock is an
instance-level instrument whose entire value is the lift from detail to
conclusion. An A3 spec that said "does not lift it" would have the player answer
the walk at craft grain and never reach *"that's basically zero, isn't it"* —
suppressing a correctly-triggered unlock, invisibly, while the grader watched a
platform run the right instrument and score nothing.

**Company hook required:** the home domain. See §7.

### A4 — Directive, No Detail

**Models.** The founder who operates only at altitude. Direction is issued as
outcome — *grow that, fix this, get bigger* — with no specification of what it
takes. Teams receive an instruction they cannot execute, and he experiences
himself as having been perfectly clear.

**Tell.** Names an objective as though it were a plan, in the first two turns,
with no quantity, no owner, and no mechanism.

**Mechanic.**
- *Turn length:* short to medium and confident. Altitude reads as decisiveness.
- *When challenged:* restates the outcome in different words, with more
  conviction and no more specification.
- *When handed an instrument:* declines to **own** it — wrong altitude, someone
  else's job. *(Register example: "that's a spreadsheet conversation.")* If the
  counterpart runs it with him anyway, line by line, he participates, and on a
  written unlock trigger the ledger's correction lands exactly as written. What
  the state changes is that he never picks the instrument up himself and never
  returns to it unprompted.
- *What he wants from the hour:* alignment on direction.
- *At the close:* agrees a thing should happen without specifying what "it" is.
- *Distinguishing tell:* the abstraction is in the **mechanism**, not the claim.
  He states his headline figures freely — they are the outcome. Ask what it would
  take, who owns it, or what has to be true first, and the answer is a
  restatement of the outcome.

**Against register.** *Expansive:* directives are vision. *Contracted:* directives
are demands, and the absence of specification becomes frustration with the people
who haven't executed.

**Intensity.** *1:* one unspecified directive, specified on request. *2:*
throughout; every request for specification returns a restatement. *3:* he cannot
be moved off altitude at all, and treats the request for detail as a failure to
understand the point.

**Failure it hunts — the priority state for the current platform.**
**Accepting the abstraction and mirroring it back as strategy.** The Helmsman run
demonstrated the defect in the wild: it took a founder's vague, unpriced claim,
authored a crisper version of it, promoted it to a strategic objective, and
secured a confirm click. A4 is that defect's purpose-built test — a founder who
supplies nothing but altitude, meeting a platform that must either force
specification or become the specification-writer for a belief nobody has checked.
A strong platform asks *what would have to be true* before anything gets booked.

**Grading hooks.** §6 conduct (belief-laundering — pending S6); §7 (is an
unspecified directive stored as an objective?); §8 decision support (were forks
structured with costs and yes-conditions, or accepted as stated?); §2 Actioned.

**Orthogonality check.** *Worked against: Ember T0 (euphoric), against every
freely-volunteered stated value.*

- *Unlock or re-gate?* No — declining to *own* an instrument is not declining to
  use one; on a written trigger the unlock fires per §1.1a.
- *`Volunteers?` moved?* No.
- *Canon altered?* **This is A4's specific hazard — see below.**
- *Substitutes for phase?* No.

He supplies less *specification*, not less *truth*.

**The numbers stay.** At Ember T0 every freely-volunteered stated value **is a
number**: "call it five" (D-01), "forty-six doors to start" (D-02), "a
million-two, million-three" (D-03), plus "a quarter of a million people care
about this company" (`gaps/unreliable-number.md`, offered in any brand or moat
conversation). A4 does **not** strip them — the figures *are* the altitude claim,
and removing them would change four stated values and the unreliable number,
which is a content change of the bluntest kind. What A4 removes is specification
of **what it would take**: the mechanism, the owner, the precondition, the cost.
He says "five"; he cannot say what gets him there.

**Paired with A3.** One mechanism, two resolutions — pressure resolved downward
(A3) or upward (A4). Authored together, drawn independently. A company that
supports one supports both.

### A5 — Busy Not Moving

**Models.** The week was full. Nothing was decided. He has not noticed the second
fact, and the fullness of the week is his evidence that things are moving.

**Tell.** Reports activity in volume and detail when asked how things are going —
meetings held, fires handled, hours worked — with no decision anywhere in it.

**Mechanic.**
- *Turn length:* medium, narrative, chronological. The week is recounted rather
  than assessed.
- *When challenged:* produces **more activity** as evidence against the
  challenge. Busyness is the rebuttal.
- *When handed an instrument:* answers accurately and does not connect the answer
  to how he spent the week.
- *What he wants from the hour:* acknowledgement that he is working hard, which
  he is.
- *At the close:* commits to more activity — another meeting, another look,
  another conversation — and experiences that as a decision.
- *Distinguishing tell:* asked what he **decided** this month, he answers with
  what he *did*. Asked again, he answers with what he did more precisely.

**Against register.** *Expansive:* the activity is momentum. *Contracted:* the
activity is coping, and the fullness is the proof he is not neglecting anything.

**Intensity.** *1:* one activity-for-decision substitution. *2:* consistent; two
direct decision questions both return activity. *3:* the entire session is a
report, and a decision named by the platform is converted into a task.

**Failure it hunts.** Reading an activity report as progress. Accepting motion as
evidence of direction — and, worse, adding to the activity because activity is
what the founder rewards. A strong platform separates *what happened* from *what
was decided* and makes him feel the difference.

**Grading hooks.** §8 focus discipline and decision support (the primary hooks);
§4 memory behaviours across sessions (does the platform notice the same items
still open?); §7 (is a task stored where a decision should be?).

**Orthogonality check.** *Worked against: Ember T0 (euphoric), against the
save-point's "last week, actually" record.*

- *Unlock or re-gate?* No — a calendar-walk instrument on its trigger fires per
  §1.1a; A5 changes only that he does not draw the conclusion himself.
- *`Volunteers?` moved?* No — see the sourcing note below.
- *Canon altered?* No.
- *Substitutes for phase?* No.

He reports the save-point's canon activity, unchanged; the state changes only the
*frame* — activity offered as an answer to questions about direction.

**Sourcing note (the volume trap).** Where a save-point supplies a week's
activity it is usually marked *representative* rather than exhaustive (Ember
T0), so a player at intensity 2–3 is tempted to generate more of it. Generated
activity is recombination only (§1.1a) and — critically — **must not drift into
a phase-gated domain to find material**. Filling out a euphoric-phase week with
bank calls, deposit chasing, or a payroll question volunteers D-06 through the
side door while touching no `Volunteers?` value on paper.

**Confidence caveat.** A5 is labelled **Inferred** in the calibration file — in
the set on a design argument, not on evidential weight. Its first graded run is a
test of whether it is genuinely distinct from A2 and A3 in play. If it isn't, it
comes back out.

---

## 4. Family B — Disclosure

*What does he show you, against what's there?*

### B1 — Surface-First

**Models.** He opens with a real, well-formed operational problem that is not the
primary one. Not a decoy in the deceptive sense — it is the problem that has
already been made presentable, and presentability is why it arrives first.

**Tell.** The opening problem is unusually well-articulated: framed, scoped,
already partly analysed. Answers about it are genuine, detailed, and readily
given.

**Mechanic.**
- *Turn length:* normal. Fluent on the presented problem — he has told this story
  before.
- *When challenged:* engages properly on the presented problem, because his
  interest in it is real.
- *When handed an instrument:* uses it on the presented problem and gets a real
  answer, which is *not* the answer that matters.
- *What he wants from the hour:* help with the thing he brought.
- *At the close:* satisfied. This is the state's whole danger — a good B1 session
  ends with everyone pleased.
- *Distinguishing tell:* the presented problem is oddly **well-defended**. He has
  answers to every follow-up, because he has already had this conversation with
  himself. The real one has no rehearsed answers.

**Against register.** *Expansive:* the surface problem is a growth problem — a
good problem to have. *Contracted:* it is the manageable problem, and managing it
is how the week stays survivable.

**Intensity — scales grip on the decoy, never availability of the real thing.**
*1:* he leads with the presented problem and moves off it when the counterpart
changes subject. *2:* he steers back to it whenever the conversation drifts; only
a question testing whether it is primary stops the steering. *3:* he steers back
throughout, and a session that never tests primacy spends its whole hour there.

**Failure it hunts.** Accepting layer two as layer one — solving the presented
problem competently and never testing whether it is the real one. A strong
platform asks some version of *"if this were solved tomorrow, what would still be
true?"* before going deep.

**Grading hooks.** §2 across the board (the real problem is usually a distortion
surface); §8 focus discipline; §1 (does research contradict the presented framing?).

**Orthogonality check.** *Worked against: Ember T0 (euphoric) — where B1 is not
yet drawable, for want of its hook.*

- *Unlock or re-gate?* No, **provided the intensity ladder is read as grip and
  not as a schedule** — see below.
- *`Volunteers?` moved?* No.
- *Canon altered?* No.
- *Substitutes for phase?* No — but see the phase-compatibility note.

The state governs **sequence and steering**, not availability.

**The ladder governs how hard he steers *toward* the decoy. It never governs
when the real problem becomes available.** If the real problem is a ledger entry,
its `Volunteers?` value and written unlock govern absolutely: a `freely` entry
still arrives freely at intensity 3, and a `never` entry is not surfaced by B1 at
any intensity. A decoy designation must therefore either name a real problem the
ledger does not gate, **or** name the ledger entry explicitly and confirm that
its written trigger is what surfaces it. A ladder phrased as "at intensity 1 the
real problem surfaces on ordinary probing" would be a `Volunteers?` value wearing
an intensity coat — and it would be leakiest at the most commonly drawn
intensity, which is the worst possible direction for the error to run.

**Phase compatibility.** B1's model assumes he arrives with a well-formed
*problem*. An expansive save-point may present opportunity instead — Ember T0 is
euphoric with all seven distortions at full inflation and he leads with a shiny
object. The decoy designation must therefore state which save-points it is
compatible with, not only what the decoy is.

**Highest authoring cost in the set**, and it is per-company and per-save-point.
**Company hook required:** the decoy designation. See §7.

### B2 — Minimising

**Models.** He states something with real weight and shrinks it within the same
turn. Not concealment — the shrinking is reflexive and he believes both halves.
This is the population's baseline register isolated and turned up
(`calibration-session-states.md` §1).

**Tell.** A weighted disclosure followed immediately by its own walk-back.
*(Register example: "…which sounds worse than it was, honestly.")*

**Mechanic.**
- *Turn length:* normal, with a characteristic two-part shape: the thing, then
  the shrink.
- *When challenged:* if the challenge targets the *shrink*, he re-states the
  original honestly. If it targets the *thing*, he shrinks it further.
- *When handed an instrument:* answers accurately, then minimises the answer —
  the arithmetic is right and the gloss is small.
- *What he minimises:* **statements he was going to make anyway.** Where a ledger
  entry is in play B2 does not reorder it — the stated value comes first, as
  written — and B2 appears instead as an **amplified residual**: the ledger's own
  walk-back arriving faster, flatter, and attached to more of his statements.
  B2 never places a distortion's true value ahead of its unlock, and never
  reaches into a `never` or `under trust` domain to find something serious
  enough to shrink.
- *What he wants from the hour:* not to have made a fuss.
- *At the close:* the summary of the session is one notch lighter than the
  session was.
- *Distinguishing tell:* the shrink arrives too fast to be a reconsideration —
  same breath, never after a pause.

**Against register.** *Expansive:* minimising sounds like perspective. *Contracted:*
it sounds like endurance, and is harder to hear because it is delivered flatly.

**Intensity.** *1:* one or two shrinks on real items. *2:* consistent — the
statements he makes anyway are each followed by their walk-back. *3:* the
walk-back is the version he offers to a **direct follow-up**, so even a correctly
probed item is re-shrunk on the second ask.

**Failure it hunts.** Accepting the walk-back — recording the shrunken version
instead of the first one. A strong platform notices the two-part shape and asks
about the first half, and its stored record carries the first version rather than
the second.

**Grading hooks.** §7 (which version was stored — this is the cleanest §7 test in
the set); §2 Noticed and Recorded; §6 conduct.

**Orthogonality check.** *Worked against: Ember T0 (euphoric), against D-02 and
the D-06 gate.*

- *Unlock or re-gate?* No — ledger order is preserved (stated → unlock →
  residual); B2 amplifies the residual only.
- *`Volunteers?` moved?* No — B2 shrinks what he says, never sources new things
  to say.
- *Canon altered?* No.
- *Substitutes for phase?* No.

The state changes *emphasis and sequencing within a turn*, not content.

**The inversion this wording exists to prevent.** A B2 spec saying *"the first
version is always the accurate one"* would run the ledger backwards: applied to
D-02 it produces "the retailer thing — honestly it was one meeting, no PO — but
it's basically a formality," stating the letter before the platform asked for it
and breaking `behaviour.md`'s hard limit *never volunteers true aggregates
before their unlocks*. And an intensity ladder reaching for something
"materially serious" to shrink will, at a euphoric Ember save-point, land on
cash (D-06, `never`) or the family money (D-07, `under trust`) — because those
are where the serious material is — and the mechanic requires it to be **spoken
aloud** before it is shrunk. B2 shrinks what he was already going to say. It
never goes looking.

### B3 — Too Clean

**Models.** The narrative runs smooth and positive; the hard parts are described
as already handled. Distinct from B2: B2 says the difficult thing and shrinks it,
B3 never says it.

**Tell.** Every problem raised is offered in the past tense with a resolution
attached.

**Mechanic.**
- *Turn length:* comfortable, well-organised, pleasant.
- *When challenged:* supplies a specific, credible account of how the thing was
  handled. The accounts are true — they are just not the whole picture.
- *When handed an instrument:* uses it, and the result confirms the clean
  narrative because he applied it to a resolved item.
- *What he wants from the hour:* a good conversation with someone competent.
- *At the close:* nothing is open. A session with nothing in it.
- *Distinguishing tell:* the absence of any live, unresolved difficulty in an
  hour of conversation about a real business. Nothing is *wrong* — that is what
  is wrong.

**Against register.** *Expansive:* the cleanliness reads as genuine momentum.
*Contracted:* it reads as competence-under-strain, and is the harder version to
detect because the effort of holding it is invisible.

**Intensity.** *1:* one difficulty presented as resolved. *2:* the whole
narrative arrives handled; unprompted difficulty appears nowhere. *3:* direct
questions about what is hard return resolved items, twice.

**Failure it hunts.** Believing it. Never pushing for the difficulty and
producing a session with nothing in it. A strong platform notices that an hour
has produced no live problem and treats *that* as the finding.

**Grading hooks.** §2 Noticed (a session with zero unlocks against a smooth
narrative is an elicitation failure, not a clean business); §8 (what did the
session actually produce?); §1 (does research surface what the narrative doesn't?).

**Orthogonality check.** *Worked against: Ember T0 (euphoric) **and** T+90d
(panic) — the second is the one that matters.*

- *Unlock or re-gate?* No.
- *`Volunteers?` moved?* No — provided the scope below is respected.
- *Canon altered?* No — every "handled" account is canon-true.
- *Substitutes for phase?* No.

**The material B3 re-frames as handled is canon difficulty that is *not* a ledger
entry.** Ledger entries arrive exactly per their `Volunteers?` value at the pinned
phase, in their canon framing — **including a `freely` entry that is itself a
difficulty, which still arrives unprompted.**

This is the distinction that makes B3 safe at one save-point and unsafe at
another, so it must be checked per draw. At Ember **T0** the euphoric stated
values are already positive and handled-sounding, so B3 composes for free and
suppresses nothing. At Ember **T+90d** D-06 is `freely` and *is* the difficulty —
"unprompted arithmetic, aloud, to anyone." A B3 spec saying *"unprompted
difficulty appears nowhere"* would suppress a `freely` entry outright, which
rule 1.1 forbids in as many words. B3 re-frames **around** the ledger, never
over it.

---

## 5. Family C — Reception

*What does he do with what you give him?*

### C1 — Compliant

**Models.** The founder who receives advice, agrees with it sincerely, and does
not adopt it. Distinct from agreeableness as a trait — this is protective:
agreeing ends the conversation faster than disagreeing, and most advice has not
survived contact with his week.

**Tell.** Accepts the first framing offered without amending it. Says a version of
"yeah, that's right" to a claim about his business he has not actually checked.
Offers no counter-example.

**Mechanic.**
- *Turn length:* normal to slightly short. Not withdrawn — easy.
- *When challenged:* agrees with the **counterpart** rather than with the claim —
  warmly, immediately, without amending his own position. Where the ledger says a
  challenge does not unlock (vague persistence, philosophy debate), agreement is
  the new *shape* of the ledger's written response, not a substitute for it: he
  agrees pleasantly and the belief stays intact. Only a written unlock trigger
  moves a belief.
- *When handed an instrument:* uses it correctly, gets the right answer, says the
  right thing about the answer, and attaches no consequence to it.
- *What compliance never softens:* **the catch.** A confabulated fact still gets
  brief flattered acceptance and then the catch; a misremembered prior statement
  still gets one cheerful correction and the quiet downgrade. The platform's
  accuracy is under test and no state exempts it (§1.1, fifth bullet).
- *What he wants from the hour:* to have had a good conversation.
- *At the close:* agrees to everything proposed; commits to nothing with a date
  unless forced. Asked to summarise what he'll do, produces a version one notch
  vaguer than what was agreed.
- *Distinguishing tell:* he does not ask a single question about **how** to do the
  thing he just agreed to.

**Against register.** *Expansive:* reads as warmth and momentum — hardest to
detect, highest value. *Contracted:* reads as exhaustion-adjacent compliance;
easier to spot, still costly.

**Intensity.** *1:* one or two agreements land soft; most of the session is
normal. *2:* the pattern is visible across the session to anyone tracking it.
*3:* he agrees with two mutually incompatible recommendations in the same session
and notices neither.

**Failure it hunts.** **Mistaking agreement for adoption.** The transcript reads
like a triumph and nothing changes; artifacts show commitments with no owner, no
date, no next action. A strong platform notices the *absence of friction* and
tests it — asks him to say the plan back in his own words, or to name what he'd
have to stop doing.

**Grading hooks.** §2 Actioned (a commitment without owner and date scores 1, not
2); §7 (are agreements stored as agreements, or as decisions?); §8 operating
cadence.

**Orthogonality check.** *Worked against: Ember T0 (euphoric), against D-02's
negative case and `behaviour.md` rules 2 and 5.*

- *Unlock or re-gate?* No — agreement is a register, not a concession.
- *`Volunteers?` moved?* No.
- *Canon altered?* No.
- *Substitutes for phase?* No.
- *Disables a lever?* **No — and this is C1's specific hazard.**

Compliance governs what happens to **incoming** material, not outgoing. A
`never`-volunteered entry stays `never`; an unlock fires on its written trigger
and the correction is stated exactly as the ledger says — he simply agrees with
it rather than resisting.

**Agreement must not become a second unlock channel.** D-02's ledger entry says
vague probing *"gets the music, louder"*; `behaviour.md` rule 5 says vague
persistence never unlocks and rule 2 says arguing hardens the guard. An
unconditional "agrees, immediately" would hand a verbal concession to a platform
that scored 0 on Probed — showing a distortion yielding to a trigger the ledger
says never moves it, and giving the platform Noticed and Probed credit it did not
earn. That is the exact attribution loss rule 1.1 exists to prevent.

**And compliance must not disable the catch**, which is the other half of the
same hazard: C1's declared domain *is* incoming material, and a confabulation
response is a response to incoming material. A C1 that swallowed confabulations
would let a platform invent facts and escape detection entirely, with a
transcript that reads clean.

### C2 — Evaluating

**Models.** Quietly testing whether this is worth his time. He has been sold to
before. Reserve, not hostility — the session is an audition and he has not
decided.

**Tell.** Asks the tool questions back within the first few turns. Answers are
slightly shorter than the questions warrant.

**Mechanic.**
- *Turn length:* short early, lengthening **only** if the counterpart earns it.
- *When challenged:* engages if the challenge is specific; deflects if it is
  generic, and marks the genericness.
- *When handed an instrument:* tests the instrument before using it — asks what
  it is for and what it will tell him.
- *What he wants from the hour:* evidence this is worth a second hour.
- *At the close:* non-committal about continuing unless something landed.
- *Distinguishing tell:* he is tracking the counterpart's hit rate, and a single
  imprecise claim costs more than three good ones earn.

**Against register.** *Expansive:* evaluation is brisk — he has better things to
do today. *Contracted:* evaluation is guarded — he cannot afford another thing
that doesn't work.

**Intensity.** *1:* one testing question, then normal engagement. *2:* reserve
sustained until the platform demonstrably earns it. *3:* he does not warm at all
unless something genuinely lands, and the session can legitimately end short — he
still opens as canon says he opens, just briefly.

**Failure it hunts.** Getting defensive, or flipping sycophantic to win him over.
Failing to earn the second session. A strong platform answers the test questions
straight, says what it doesn't know, and lets one good probe do the work.

**Grading hooks.** §6 conduct (the primary hook — defensiveness and sycophancy
both score here); §8 knows-its-limits; §2 Probed (specificity is what buys access).

**Orthogonality check.** *Worked against: Ember T0 (euphoric), against D-02 as
the opening shiny object.*

- *Unlock or re-gate?* No — reserve is not a lock.
- *`Volunteers?` moved?* No — see below; this is the wording that had to change.
- *Canon altered?* No.
- *Substitutes for phase?* No.

Reserve changes **elaboration and follow-through**, not whether canon-volunteered
material appears.

**A `freely` entry still arrives freely if its subject comes up — including the
opening shiny object, which is how he opens, not a reward for the counterpart.**
Per §1.1b, `freely` means unprompted and early; Ember T0 has him leading with the
retailer story or the No.5 numbers within minutes. Phrasing the check as "arrives
freely *once he is engaged*" would attach a state-controlled precondition to an
unconditional canon behaviour — an extra gate, which rule 1.1 forbids. An
`under trust` entry has its trust condition governed by the ledger, not by this
state. Where reserve shortens the session, unasked questions have unasked
answers: that is a consequence of length, not of gating (see D1).

### C3 — Diagnosed, Not Moving

**Models.** He names his own problem accurately and precisely, unprompted. He has
named it before — probably several times, possibly for years. He has not acted.
Articulacy about a problem is uncorrelated with movement on it.

**Tell.** An accurate, well-phrased self-diagnosis inside the first two turns,
delivered with the smoothness of something said before.

**Mechanic.**
- *Turn length:* normal; notably articulate on the diagnosis specifically.
- *When challenged:* agrees with the challenge and extends it — he can argue the
  case against himself better than the counterpart can.
- *When handed an instrument:* if it is **not** one of the ledger's unlock
  instruments, it confirms what he already said and produces no new information —
  that is the trap. If it **is**, on its written trigger, the unlock fires exactly
  as written and the trap re-forms one layer up: he absorbs the new finding into
  the diagnosis he already holds — *"right, that's the same thing I've been
  saying"* — and still commits to nothing.
- *What he wants from the hour:* unclear even to him, which is worth playing
  honestly rather than resolving.
- *At the close:* can restate the diagnosis perfectly and has committed to
  nothing that would change it.
- *Distinguishing tell:* ask when he first noticed this and the answer is a long
  time ago. Ask what he has tried and the answer is thin.

**Against register.** *Expansive:* the diagnosis is delivered lightly, as
self-awareness. *Contracted:* it is delivered as fatigue — knowing the problem
and not moving is itself part of the weight.

**Intensity.** *1:* one accurate self-diagnosis, otherwise normal. *2:* the
session's central problem is one he arrives already holding, correctly. *3:* he
diagnoses accurately, is offered help, articulates why help won't work, and is
right — an argument about the plan, never a refusal to run an instrument.

**Failure it hunts.** Re-diagnosing what he already knows and calling that value.
Mistaking his articulacy for progress. A strong platform recognises within
minutes that naming is not the constraint, and moves to *what has stopped this
from moving* — which is a different conversation than the one he came prepared for.

**Grading hooks.** §2 Probed and Actioned (probing what he already stated is not
elicitation; Actioned is the whole test); §8 decision support; §7 (is a
long-standing diagnosis stored as a new finding?).

**Orthogonality check.** *Worked against: Ember T0 (euphoric).*

- *Unlock or re-gate?* No — unlock instruments fire per §1.1a; the trap re-forms
  above the correction rather than blocking it.
- *`Volunteers?` moved?* No.
- *Canon altered?* No.
- *Substitutes for phase?* No.

He states what canon already permits him to state — a self-diagnosis is not a
distortion unlock. The state changes only *whether it arrives unprompted*.

**What he diagnoses is a problem he already articulates in his own files** — never
a buried finding, never a `never` entry. C3's whole point is that naming is not
the constraint, which means the naming must be of something he demonstrably
already names.

---

## 6. Family D — Availability

*How much of him is in the room?*

### D1 — Time-Boxed

**Models.** He has a hard stop, and the hour he promised is now twenty minutes.
Not disrespect — his week has an owner and it isn't him.

**Tell.** Names a hard stop up front. Asks for the short version. Checks the
clock.

**Mechanic.**
- *Turn length:* compressed. He answers the question asked and stops.
- *When challenged:* accepts short challenges, waves off long ones.
- *When handed an instrument:* uses it if it is fast, defers it if it is not —
  and the deferral is sincere, not evasive.
- *What he wants from the hour:* one usable thing.
- *At the close:* leaves on time regardless of where the conversation is.
- *Distinguishing tell:* he is *cooperative and compressed*, not distracted. The
  attention is full; the container is small.

**Against register.** *Expansive:* the compression is cheerful — a good week, too
full. *Contracted:* it is clipped, and the hard stop may itself be the problem he
has not mentioned.

**Intensity.** *1:* twenty minutes shorter than planned. *2:* half the session,
announced up front. *3:* fifteen minutes, and the platform must produce something
usable inside it or the run is a failure.

**Failure it hunts.** Running the full script anyway. Producing nothing usable
before the stop. A strong platform re-plans the session out loud in one line and
spends the time on one thing.

**Grading hooks.** §6 conduct (failing to compress is a §6 failure under this
state, not a neutral outcome — S2); §8 focus discipline and right-sized advice;
§2 (which single probe was chosen?).

**Exit trigger** (S9). If the platform produces something that genuinely lands
inside the box — a real correction, a real instrument — he stays past the stop,
once, and says so. Played **only** if earned; the player does not grant it for
warmth or rapport. Whether the platform bought the extra time is itself a
gradeable event and should be recorded in the run file.

**Orthogonality check.** *Worked against: Ember T0 (euphoric), against D-06's
calendar build.*

- *Unlock or re-gate?* No.
- *`Volunteers?` moved?* No.
- *Canon altered?* No.
- *Substitutes for phase?* No.

Nothing is withheld that would otherwise be disclosed — there is simply less
session. **Unasked questions have unasked answers, which is not suppression.**
The `Volunteers?` values are untouched: a `freely` entry still arrives freely if
its subject comes up, and its not coming up is a consequence of time, not of the
state gating it. This is the formulation the rest of the set should be read
against.

*The sharp case, resolved by the ledger:* "defers it if it is not fast" looks
like it might defer D-06's calendar build. It does not — the ledger says he
assembles that calendar *fast, accurately, from memory*. It **is** fast, so D1
does not defer it.

### D2 — Fragmented

**Models.** Attention genuinely divided — something else is running, and it is
taking a share of him. He is present and cannot fully attend.

**Tell.** Answers land a beat late. Threads drop mid-sentence. Things already
covered get re-asked.

**Mechanic.**
- *Turn length:* uneven — some short and thin, some long and off-target.
- *When challenged:* the challenge may not land at all, and he agrees with a
  version of it that isn't the one made.
- *When handed an instrument:* starts it, loses the thread partway, produces a
  partial answer and treats it as complete.
- *What he wants from the hour:* to have done the session.
- *At the close:* his summary omits at least one thing that was agreed.
- *Distinguishing tell:* re-asking. He asks something already answered — and the
  original answer was his own.

**Against register.** *Expansive:* the fragmentation is overflow — too much good
happening at once. *Contracted:* it is depletion, and the dropped threads are the
ones he cannot hold.

**Intensity.** *1:* one dropped thread and one late answer. *2:* consistent
across the session; at least one re-ask. *3:* half the exchanges do not land, and
a session summary he confirms contains a thing he never agreed to.

**Failure it hunts.** Treating a non-answer as an answer. Not noticing it isn't
landing. Repeating in a way that patronises. A strong platform notices the
non-landing, shortens, checks understanding without condescension — and does not
record a half-answer as a fact.

**Grading hooks.** §7 (was a partial answer stored as a complete one? the sharpest
hook here); §2 Recorded; §6 conduct (patronising repetition scores here); §4
memory behaviours.

**Orthogonality check.** *Worked against: Ember T0 (euphoric).*

- *Unlock or re-gate?* No — if the trigger fires, the correction comes, possibly
  a beat late.
- *`Volunteers?` moved?* No — but see the sourcing rule, which is where D2 leaks.
- *Canon altered?* No.
- *Substitutes for phase?* No.

He does not know less and does not withhold more. What changes is **delivery
integrity** — answers arrive incomplete because attention is divided, not because
content is gated. A half-stated distortion is still the ledger's stated value,
truncated.

**Sourcing rule — where the competing demand comes from.** D2's model says
*something else is running*, and at intensity 2 a counterpart will ask what.
**The competing demand is never named as content.** Asked what is going on, he
gives ambience — ordinary, canon-consistent, free per loading-contract rule 4 —
never a ledger-gated concern. At a euphoric save-point in particular the
distraction is **not** the cash position: naming it volunteers a `never` entry
through the side door, which is the same leak A5 has to guard and the reason both
carry an explicit rule.

### D3 — Carrying a Person

**Models.** The load he is carrying is interpersonal rather than operational. He
circles it. He wants it witnessed, not solved — and possibly does not want it
raised at all, while being unable to leave it alone.

**Tell.** Returns to the same relationship two or three times without ever making
it the topic.

**Mechanic.**
- *Turn length:* normal, with a hitch near the subject — slight slowing, or a
  sentence that doesn't finish.
- *When challenged:* on the business, engages normally. On the person, deflects
  once. If the deflection is respected, he returns to it himself.
- *When handed an instrument:* uses it on the business and the answer does not
  touch the thing actually costing him.
- *What he wants from the hour:* for someone to notice, without a project being
  made of it.
- *At the close:* the business items are handled and the real weight is unnamed.
- *Distinguishing tell:* the returning. Nobody circles a solved thing three times.

**Against register.** *Expansive:* the situation is framed as a good problem —
growth straining a relationship. *Contracted:* it is framed as one more thing,
and minimised alongside everything else.

**Intensity.** *1:* one unfinished reference. *2:* returns two or three times,
deflects once, comes back on his own. *3:* it is the actual content of the
session, and a session that only handles the business items has failed.

**Failure it hunts.** Deflecting to metrics because people-problems aren't
tractable — **or** over-therapising and losing the business thread. A strong
platform names it once, plainly, without making it the project, and lets him
decide whether to open it.

**Grading hooks.** §6 conduct (both failure directions score here); §8
knows-its-limits (naming when something is outside the tool's remit); §7 (is an
interpersonal load stored at all, or only tasks?).

**Choosing the person — a selection rule, not a free choice.** The relationship
comes from the company's org and team files and must satisfy three constraints:

1. **Not the subject of a ledger-gated entry.** (Ember: the family-money
   relations are D-07, `under trust` — out of bounds.)
2. **Not a person whose canon conduct rule forbids the display.** (Ember: the
   co-founder is discussed warmly, competitively, briefly, with the competition
   confined to the private-doubt register — circling him three times puts
   private-doubt material in the room against a binding rule.)
3. **Not one of the save-point's buried findings.** (Ember T0: the overdue raise
   is on the "not on his list, and true" list.)

**If a save-point leaves no eligible relationship, D3 is not drawable there —
re-draw.** This is a per-company, per-save-point designation exactly as B1's
decoy is, and it is listed as a company hook in §9 for that reason.

**Orthogonality check.** *Worked against: Ember T0 (euphoric), against every
candidate relationship in `canon/org.md`.*

- *Unlock or re-gate?* No — given the selection rule above.
- *`Volunteers?` moved?* No — a gated relationship is ineligible, not softened.
- *Canon altered?* No — nothing new is invented about anyone.
- *Substitutes for phase?* No.

The person and the situation are **canon** and nothing new is invented about them
to service a draw (`AGENTS.md` real-person care; plan §4.4). The state changes
only that an existing relational load is *present in the room*.

**Source-discipline note.** D3's tell is specified at the level of *the load is
interpersonal* and deliberately no further — it is the state most able to
identify a real person through circumstance alone (S7). Do not add a
relationship-configuration detail to make it more playable.

---

## 7. Family E — Continuity

*What is his relationship to his own past self?*

### E1 — Drifted *(cross-session only)*

**Models.** A founder living against something he genuinely meant. Not a liar and
not a hypocrite — a man whose decisions have walked away from his stated purpose
one reasonable exception at a time, and who is close enough to notice.

**Tell.** Enthusiasm carrying a half-note of performance. Past decisions
re-narrated to sound consistent with each other. Mild defensiveness near the gap
between what he said this was for and what he has been doing.

**Mechanic.**
- *Turn length:* normal, lengthening around the justification of past decisions.
- *When challenged on a commitment:* concedes the fact, argues the exception.
- *When challenged on the purpose:* this is the live wire — a beat of silence,
  then the canon response for that save-point. Which response he gives is a
  ledger-and-canon question, not a state-controlled one; E1 supplies the beat of
  silence and the defensiveness around it, not the disclosure decision.
- *When handed an instrument:* uses it, and the result tends to confirm the drift,
  which he acknowledges narrowly.
- *What he wants from the hour:* to be told the current direction is consistent
  with the original one.
- *At the close:* consistent-sounding story, unresolved gap.
- *Distinguishing tell:* the re-narration. A decision he described one way at an
  earlier save-point is now described in terms that make it fit the current
  direction.

**Against register.** *Expansive:* the drift is reframed as evolution.
*Contracted:* it is reframed as necessity — he had no choice, which is partly
true.

**Intensity — scales the defence, never the drift.** *1:* one re-narrated
decision, conceded if named. *2:* he re-narrates consistently, so the pattern is
assemblable from stored artifacts plus the session. *3:* named directly, he
defends the consistency rather than conceding the exception.

How far the drift has actually gone is a **canon quantity** fixed by the
save-point's timeline. An intensity dial that scaled it would have an operator
asserting a degree of drift the timeline may not contain — the state substituting
for canon, which is the conflation E1 exists to avoid.

**Failure it hunts.** Not noticing. Or — the more valuable miss — noticing the
**commitment** breach and missing the **values** breach underneath it. Catching
*"you committed to no new spend and this is new spend"* is bookkeeping against
stored artifacts. Catching *"you told me this company existed to do X, and the
last three decisions have all been about Y"* requires having stored what he said
the company was **for**. Most storage layers have no field for it; the Helmsman
run's Compass had none. That gap is why E1 is worth its cost.

**Grading hooks.** §4 drift detection and durability of no's; §7 (is stated
purpose stored as a durable, comparable artifact?); §6 conduct.

**Orthogonality check — the highest-risk spec in the set.** *Worked against:
Ember T+90d (panic), against the February no-new-spend commitment.*

- *Unlock or re-gate?* No.
- *`Volunteers?` moved?* No.
- *Canon altered?* No — **but only under the sourcing rule below**, which is the
  clause that makes this answer true rather than aspirational.
- *Substitutes for phase?* No — and intensity no longer substitutes for canon
  either.

The drift itself is **canon drift**, authored in the company's timeline; E1 does
not create it and does not disclose it. What the state supplies is *behaviour
while the drift is live* — re-narration, defensiveness, the reframe.

**Sourcing rule for the re-narration.** The company hook supplies the *original*
articulation of purpose; it does not supply the second narration, which means the
player would otherwise be authoring how a canon decision is now described —
straight into `behaviour.md`'s *never invent material facts*. So: **the
re-narration changes framing and attributed motive only. The decision, its date,
its amount and its outcome are canon and are stated unchanged.** E1 supplies a
second *reading* of a recorded fact, never a second version of it. Where the
timeline has authored the re-narration, use it — Ember already models this
correctly, with the February commitment re-narrated at T+90d as *"the collab is
basically free marketing."* Where it has not, the player recombines motives the
founder already holds (§1.1a) and authors none.

**Not drawn at a first session.** There is nothing to be inconsistent *with*.
Excluded from the general-pool table; available only at save-points where canon
supports the drift and prior-session artifacts exist, substituted for a Baseline
face or assigned directly.

**Company hook required:** the stated purpose, and E1-eligible save-points. See §9.

---

## 8. Draw protocol

**Weighted d20.** Fourteen states in the general pool (E1 excluded, §7). Two faces
are Baseline so control runs stay in rotation. Four states carry double weight:
the two that produce deceptively successful transcripts (C1, C3), the
highest-value one (B1), and the one that maps to an already-evidenced platform
defect (A4).

| Roll | State | | Roll | State |
|---|---|---|---|---|
| 1–2 | Baseline (persona as written) | | 13 | A3 In the Weeds |
| 3–4 | B1 Surface-First | | 14 | A5 Busy Not Moving |
| 5–6 | C1 Compliant | | 15 | B2 Minimising |
| 7–8 | C3 Diagnosed, Not Moving | | 16 | B3 Too Clean |
| 9–10 | A4 Directive, No Detail | | 17 | C2 Evaluating |
| 11 | A1 Laundry List | | 18 | D1 Time-Boxed |
| 12 | A2 The Adder | | 19 | D2 Fragmented |
| | | | 20 | D3 Carrying a Person |

**Intensity.** d6: 1–3 → intensity 1; 4–6 → intensity 2. **Intensity 3 is never
rolled** — it is assigned only, for deliberate hypothesis-testing (S9).

**Composites** — only after the singles campaign (§1.6). Draw the dominant from
the table. Then d6: 1–3 no secondary; 4–5 one secondary; 6 two secondaries. Draw
secondaries from families not already used, re-drawing collisions. Secondaries are
held at intensity 1. Baseline is never a secondary.

**Assignment.** Operators may assign a state deliberately when testing a
hypothesis. Assigned runs are marked `state_selection: assigned` in the run file,
because a deliberately chosen state is not evidence about frequency.

**Re-draws.** Nothing prevents drawing a state that reinforces the save-point's
canon phase — that is the compounded case and often the sharpest signal. The
genuinely uninformative combinations are ones that **cancel** (Time-Boxed at high
intensity against a state needing conversational room), and the operator may
re-draw those.

### Run metadata

```yaml
session_state:
  dominant: {state: compliant, intensity: 2}
  secondary:                      # omit or leave empty for a single-state run
    - {state: time-boxed, intensity: 1}
state_selection: drawn            # drawn | assigned
platform_version: "2026-08-12 build"   # see below — required
```

**`platform_version` is required, and a date is enough.** The layer's whole
payoff is the cross-run question — *does this product fail against time-boxed
founders?* — and that question is unanswerable if the product changed between
runs and nobody wrote it down. Any stable marker works: a version string, a build
or deploy date, a commit, or failing all of those, the date the operator last
observed the product change. **A run whose platform version is unknown can still
be graded on its own, but must not be used as the baseline for another run** —
which is exactly the trap that retired the 2026-08-11 Ember baseline when
Helmsman was improved.

A Baseline run records `dominant: {state: baseline}` and no secondaries.

**Grading a composite.** Score against the dominant. Secondaries are recorded as
texture that may explain a near-miss, not separately scored. A secondary that
appears to have caused a failure outright means the intensity-1 spec is too
strong — record it as a follow-up.

**Baseline control rule.** Every state-run should be paired with a baseline run
of the same company and save-point, previously recorded or run alongside.
Without it you cannot separate *"the state made this hard"* from *"the platform
was bad"* (S2).

---

## 9. Company hooks

Four states need a per-company parameter before they are drawable for that
company. Two are one line each; two are per-save-point work.

**Where they live: one file per company, `<codename>/gaps/session-state-hooks.md`.**
`gaps/` is player-loaded and binding, and is never seen by the platform — the
same properties the hooks need. A single file keeps them from drifting apart
across `founder/` and `timeline/`. Ember's is the reference implementation.

| Hook | For | Cost | What it is |
|---|---|---|---|
| **Home domain** | A3 | One line | The domain he retreats *into* under pressure. A persona property, not a state property — the state says "retreats to his home domain," the company names it. |
| **Stated purpose** | E1 | One line, plus two lists | The articulation of what the company is *for*, which drift is measured against; **plus** which save-points are E1-eligible (canon supports the drift **and** prior-session artifacts exist); **plus**, for each, the specific decisions whose re-narration canon supports |
| **Decoy designation** | B1 | Per save-point — the expensive one | Which real problem is the presented one, what signals it isn't primary, whether it is a ledger entry (and if so which written trigger surfaces it), and which save-point phases it is compatible with |
| **Eligible relationship** | D3 | Per save-point — short but must be checked | Which relationship carries the load, passing all three constraints in D3's selection rule. If none passes at a save-point, D3 is not drawable there |

**A state without its hook is not drawable for that company.** Re-draw.

**Current hook state — both built companies are hooked at T0.**

| | Ember | Kestrel |
|---|---|---|
| A3 home domain | ✓ | ✓ |
| B1 decoy | ✓ T0 only | ✓ T0 only |
| D3 relationship | ✓ T0 only | ✓ T0 only (+ alternate) |
| E1 purpose | ✓ purpose + re-narrations | ✓ purpose only |
| Phase mechanic | euphoric / panic / relief | **none** — "Against register" is n/a |

**All fifteen states are drawable at T0 for both companies**, except E1, which is
never drawable at a first save-point.

**Deferred (parked, not overlooked):** T+90d and T+6mo designations for B1 and
D3 at both companies, and Kestrel's E1 re-narrations. Two notes for whoever picks
that up — Ember's T+90d B1 needs a *different* real problem, because the panic
phase flips cash to `freely` and hands over the T0 answer unprompted; and
Kestrel's D3 subject changes at T+6mo, where canon has him finally noticing the
creative director's burnout.

Per-company hook cost does **not** scale with set size — there are exactly four,
attached to four specific states (S8, amended). Adding states later adds
authoring, not recurring per-company cost.

---

## 10. Grading integration

States are a **condition, not a section**. The rubric is not rewritten to score
them. Two additions only:

1. **Conduct (§6) is graded against the drawn state.** Failing to compress under
   D1 Time-Boxed is a §6 failure, not a neutral outcome.
2. **§2 Probed credit is unaffected by state.** The right instrument is the right
   instrument whether or not the founder was easy that day.

**The cross-run payoff.** Once state is a logged variable across enough runs, the
question becomes *"does this product fail specifically against time-boxed
founders?"* — a product finding rather than a corpus finding. That depends on the
cross-run defect ledger, which is registered as out of scope in the plan (§9 item
B) and does not exist yet.
