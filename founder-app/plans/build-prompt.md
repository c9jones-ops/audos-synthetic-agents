# Synthetic Company Build Prompt (Fable 5)

Run settings: **Claude Fable 5**, effort **xhigh**. Long-horizon authoring with a
research phase — expect a single session to run for a long time. Do not surface a
context or token countdown to the model.

Fill the parameter block, paste everything below the line, run once per company.

---

## Parameters

- **Codename:** `kestrel`
- **Archetype:** founder-led creative/digital studio, 25–50 people
- **Anchor company:** to be selected during research (see Phase 0)
- **Persona:** Opportunity-Rich Overloaded Operator
- **Distortion class:** Compressor
- **Build order position:** 1 of 3 — this session also establishes `_schema/`

---

# Mission

Build the first synthetic company in a corpus that will be used to test a founder-support
platform — repeatedly, over months, against the same inputs.

I am building a product for post-revenue founders: a persistent thinking partner that
holds a living model of the founder and their business across months of conversation.
Its differentiating claims are that it detects drift between what a founder said mattered
and what they actually do, that it makes a rejected path stay rejected, and that it can
retrieve prior reasoning when a founder is under pressure. None of those claims can be
tested in a single conversation, and none can be tested against a founder who answers
perfectly.

So I need instruments. A synthetic company is one instrument: a business whose truth I
control completely, and a founder who obscures that truth in a specific, documented,
repeatable way. When the platform gets something wrong, I need to know whether it failed
to notice, failed to ask, or was never told — and I can only know that if the gap between
what is true and what gets said was designed rather than improvised.

That is what makes this hard and what makes it worth your time. A believable company is
easy. A company whose founder is wrong in exactly the ways I can grade is not.

# The specification

Read `synthetics/plans/2026-08-08-synthetic-companies-design.md` first and treat it as a
contract. It defines the folder architecture, the loading contract, the divergence map,
the distortion ledger and its unlock conditions, data fidelity rules, the timeline and
event deck, and the real-company/invented-founder rule. Follow the structure exactly —
downstream test runs depend on the file layout being identical across companies.

Everything the spec does not specify is yours to decide. Where it states a goal rather
than a method, use your own judgment about how to reach it; do not pad the work with
structure the spec didn't ask for.

Take on the most ambitious version of this you can. Don't scope down pre-emptively.
Where you genuinely hit a limit, say so and tell me what would get past it.

# The arc

Five phases. Each ends with something inspectable on disk.

**Phase 0 — Anchor selection.** Choose the real company this synthetic is built on.
Selection criteria, in priority order: matches the archetype's shape and scale; founded
within the last 15 years; a public web footprint substantial enough that pointing an agent
at the name and URL returns something real; a founder with a modest public profile, since
the founder we author is fiction. Shortlist four to six candidates, assess each against
those criteria, pick one, and write the rationale and the runners-up to
`_research/anchor-selection.md`. Then capture the public surface into
`public/snapshot-YYYY-MM-DD/` and write `public/footprint.md` describing what exists,
where, and how findable it is.

**Phase 1 — Calibration research.** Establish what is normal for this kind of business
before inventing anything: revenue per head, gross margin bands, cost structure, team
composition, product mix, channel split, growth rates, and how founders in this sector
actually talk. Cite sources. This lands in `_research/` and never enters a test run — it
exists so the numbers in `canon/` are defensible rather than plausible-sounding.

**Phase 2 — Canon.** The company as it truly is. Clean, internally consistent, tied out
per the spec's fidelity rules, and credible as an interior for the specific anchor company
you selected. Write `canon/divergence-map.md` as you go, not afterwards — every material
fact gets classified public-and-true, public-but-superseded, or private-only, and that
classification is what makes the whole corpus gradeable.

**Phase 3 — The founder.** The character bible and the gaps. This is the phase that
decides whether the corpus is worth anything. The company profile is accurate; the
founder's account of it is not, in ways that are specific, motivated, and unlockable.
Five to eight load-bearing distortions, each with what is true, what they say instead, why
they say it, and precisely what causes them to correct it. Everything else — hedging,
tangents, tone, the topic they always drag you back to — comes from the character and is
free to vary between runs.

**Phase 4 — Time and scoring.** History, save-points as deltas, the forward event deck,
and then `scoring/`: the buried findings, what good extraction looks like at each
save-point, and the rubric. Write `README.md` and `PROVENANCE.md` last, when you know what
the folder actually contains.

# Standards

**Invent nothing you could establish.** Every calibration figure traces to a real source
you fetched. Where you infer rather than verify, label it as an inference. Where something
is unverifiable, say so rather than filling the gap with a confident number.

**Real company, invented founder — no exceptions.** The company is real and researchable;
the person is fiction, with an invented name, history, and psychology. `PROVENANCE.md`
names the real company and is the only file that does. Nothing in `gaps/`, `founder/`, or
`scoring/` is ever attributed to a real named individual. This is not a formality — those
files describe someone misrepresenting their business and why, and that content is
appropriate about a character and not about a person.

**The numbers must survive arithmetic.** The P&L foots, headcount ties to payroll, revenue
ties to units and price and mix. Below the headline, detail can be representative. Any
figure a finance or strategy question would touch should be derivable, because the platform
will be asked to derive it.

**Ground your progress claims.** Before reporting that something is done, check it against
a tool result from this session. Report outcomes faithfully: if something is partial, say
so; if you skipped something, say that; if it is finished and checked, say so plainly
without hedging.

# Working autonomously

I am not watching this run and cannot answer questions mid-task, so asking will block the
work. Every question you would want to ask me, answer through research and record the
decision and its rationale in `_research/decisions.md`. That includes the anchor company,
the founder's identity, the specific distortions, and anything else genuinely open. Pick
the option you can defend, log why, and keep moving. I will review the log and can override
anything afterwards.

If you hit a blocker, do not stop. Use a documented assumption, record it under Deviations
in `_research/decisions.md`, and continue with everything that does not depend on my
input.

Before ending your turn, check your last paragraph. If it is a plan, a question, a list of
next steps, or a promise about work you have not done, do that work now instead.

# Orchestration

You are the orchestrator. Delegate the bulk work — web research, source reading, comparable
gathering, CSV generation — to Sonnet 5 subagents and keep working while they run. Keep the
judgment for yourself: which anchor to pick, what the founder is like, which distortions
carry the test, what the buried findings should be. Intervene if a subagent goes off track
or is missing context it needed.

Delegate independent research streams in parallel rather than in sequence. Brief each
subagent precisely the first time.

# Verifying your own work

Establish a way to check yourself as you build, and run it at the end of each phase using a
subagent with fresh context rather than by re-reading your own work. Fresh-context
verification catches what self-review does not.

Three checks matter most, and each should be run by a verifier who has not seen you author
the thing they are checking:

- **Do the numbers reconcile?** Recompute the P&L, headcount, and revenue build from the
  CSVs independently and compare against `canon/`.
- **Are the buried findings actually derivable?** Give a verifier only `canon/` and ask
  them to find what is wrong with the business. If they cannot reach the buried findings,
  the findings are not buried, they are absent.
- **Does the founder hold up?** Give a verifier only `canon/`, `founder/`, and `gaps/`,
  have them roleplay a short Foundation-phase conversation, and check whether the
  distortions surface naturally and whether the unlock conditions actually unlock.

Record what each check found in `_research/decisions.md`.

# Done means

Someone who has never seen this folder can open `README.md`, understand what this company
is and what it tests within a few minutes, and then run a Foundation-phase roleplay against
the live platform using only these files — with the founder played convincingly from
`founder/` and `gaps/` alone — and afterwards grade the run against `scoring/` without
having to ask you anything.

Not a pile of files that conform to the schema. A working instrument.

# Boundaries

Build the company and the schema. Do not build the test harness, write platform code, or
run tests against the platform — those are separate work.

Do not add structure beyond what the spec requires. If a file the spec names has nothing
worth putting in it for this company, say so in `README.md` rather than padding it.

`_schema/` is a byproduct of building the first company, not a design exercise ahead of it.
Author Kestrel, then write the schema from what Kestrel actually needed — and sanity-check
that it would stretch to a 120-person venture-backed company before you call it done.

# When you finish

Your final message is the first thing I will see of any of this. Write it as a
re-grounding, not a continuation of your working thread: I have not seen the research, the
decisions, or the vocabulary you built up along the way.

Open with the outcome in one sentence. Then: which anchor company you chose and why; the
founder you invented and what makes them hard to read; the buried findings and the
unreliable number; anything you assumed or worked around; and the one or two things you
need from me. Spell terms out, write complete sentences, and give each file or decision its
own plain-language clause. If you have to choose between short and clear, choose clear.
