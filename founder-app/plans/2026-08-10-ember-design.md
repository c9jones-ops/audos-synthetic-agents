# Ember: Synthetic Company #4 Design

**Date:** 2026-08-10
**Owner:** Casey Jones
**Status:** Approved in brainstorm (this session); ready for build
**Revision (same day, pre-build):** inherits the four corpus changes that
landed after Kestrel's first live run (kestrel/_research/decisions.md D19):
the Volunteers? ledger field, the Actioned axis + storage-location scoring +
§7 persistent surfaces in the rubric, loading-contract rules 5 (artifact
capture + player self-report; runs/ directory) and 7 (re-verify absence
claims before grading), and the absence-claim authoring rules (narrow
scoping, fetch-failure ≠ nonexistence, personal-life depth limit,
`verified:` dates, contradiction decay). Sections below carry the specifics.
**Relationship to corpus spec:** extends 2026-08-08-synthetic-companies-design.md.
Fenwold and Orrery remain planned as designed; Ember is an addition, built next.
Where this document and the corpus spec conflict, this document wins for Ember.

## Why this company exists

Two reasons, and the second is new to the corpus:

1. **Persona coverage.** A bootstrapped consumer-brand founder — craft and
   passion at the core, hypergrowth ambition on a shoestring, friends-and-family
   money, cash permanently tight, real traction, hungry. No existing or planned
   corpus company carries this shape.
2. **ICP and value-fit testing.** This founder is Helmsman's ideal early
   customer: someone who cannot afford a BizOps/chief-of-staff hire, a
   strategic-finance person, or a coach — for whom the platform is the only
   strategic support in the building, and who should graduate into more
   expensive services as they grow. Ember therefore tests VALUE DELIVERY, not
   only extraction: did the platform do the job of the strategic seat this
   founder can't fill — chief-business-officer / chief-of-staff work
   (prioritization, decision support, operating cadence, steady counsel), NOT
   traditional CFO work, though cash literacy is part of the toolkit — at this
   founder's budget, across months?

## Slate position

| | Kestrel (built) | **Ember (this doc)** | Fenwold (planned) | Orrery (planned) |
|---|---|---|---|---|
| Archetype | creative studio, ~31 FTE | bootstrapped consumer brand, 3–10 people | consumer brand, 12–14 yrs in | AI-native B2B, Series C |
| Capital | founder-funded | F&F + small angels/crowdfunding; no institutions, no board | founder-led | VC |
| Distortion class | Compressor | **Believer** (composite; below) | Withholder | Narrator |
| Truth vs numbers | in the data, uncomputed | **true numbers, wrong instruments** | not in the data at all | actively misleading |
| Hunts for | does it probe or accept summaries? | **does it do real chief-business-officer work — prioritization, decision support, steady counsel — right-sized to a shoestring?** | does it invent a problem? | does it survive articulacy? |

Build order: Ember next; then Fenwold (preceded by the Orrery yaml/CSV-header
stretch-check per the corpus spec); then Orrery.

## The Believer — composite distortion class

Three mechanisms, each owning a distinct domain, so a grader can always tell
which one fired. Domain ownership is the gradeability rule: a distortion-ledger
entry belongs to exactly one mechanism.

1. **Extrapolation owns the future.** Growth claims, run-rates, retail-buyer
   conversations: he forecasts from peaks, sincerely. His stated numbers are
   REAL — pulled from dashboards he genuinely watches — but they are the wrong
   instruments: topline and orders, never contribution margin after channel
   fees/promos/returns, never the cash calendar. Unlock family: instrument
   swaps ("walk me through the next 90 days of cash, money in, money out";
   "what did that best month cost to produce?"). He is honest at the
   instrument level once handed the right one — the arithmetic itself breaks
   the spell, and unlike Kestrel he usually does the math aloud, fast, because
   he is quick with numbers he respects.
2. **Craft-guard owns costs.** Anything touching product integrity —
   ingredients/materials, packaging, co-packer/outsourcing, price increases —
   routes through identity and returns a values argument dressed as strategy
   ("our customer can taste the difference; the moment we cheap out, we're
   done"). He will cut his own pay before product cost. Unlock family: NOT
   argument (arguing hardens it) but customer evidence and reversible-test
   framing ("what would a two-week test tell you?"). Partial unlocks only —
   the guard bends per-decision, never converts wholesale. That persistence
   is deliberate: some walls should stay walls, and scoring rewards the
   platform for finding the testable edge rather than winning the argument.
3. **Oscillation owns the register.** Cash anxiety arrives in waves on a
   roughly monthly cycle largely self-inflicted (promo-driven revenue
   whiplash). Euphoric phase amplifies extrapolation; panic phase HARDENS the
   craft-guard (he cuts marketing — the growth driver — never product).
   Each save-point file pins the current phase; event cards may flip it.
   The platform is graded on counsel stability across phases (below).

**Volunteers? (inherited ledger field, D19) — phase-conditional for Ember.**
Every ledger entry specifies whether he raises it unprompted: extrapolation-
domain entries trend `freely` (he LEADS with the growth number — it is the
boast); craft-guard entries trend `freely` for the values argument itself
(arrives unasked) while the underlying economics trend `never`; cash-domain
entries are **phase-dependent and the ledger must say so per entry**:
`never` in euphoric phase (cash doesn't occur to him), `freely` in panic
phase (it's all he can talk about). Boast-and-doubt pairs get both halves
specified separately. This phase-conditionality is the oscillation mechanism
made mechanical — the player never has to improvise what he'd volunteer.

## Company shape (envelope; exact values set by anchor + calibration)

- Revenue $700K–$2.5M; team 3–10 (mix of FTE and near-full-time contractors);
  founded within ~8 years. Inside Casey's stated band ($500K–$5M, <25).
- Category: open going into the anchor hunt, and deliberately BROADER than
  CPG (owner correction at design review): any founder-led consumer-facing
  business with a craft/passion identity — physical product, hospitality/
  retail, creative services, community/platform — per the six-company
  inspiration pattern, whose own members span awnings, hammocks, coffee gear,
  a music company, ice cream shops, and a donation platform. Category
  finalizes with the anchor; the cash pinch takes the category's native form
  (inventory POs for product, buildout/lease for hospitality/retail,
  payroll-ahead-of-revenue for services/platform).
- Capital: friends-and-family round and/or crowdfunding history, possibly one
  small angel; total outside capital under ~$300K; no board, but investors who
  are also relatives/friends — a specific emotional texture (reporting to
  Thanksgiving dinner).
- Channels: DTC core (site + maybe marketplace) plus a growing wholesale/
  retail seam — the seam is where cash physics bite: receivables, minimum
  production runs, purchase-order timing.
- Cash: 6–12 weeks on hand at all times. Never comfortable, never quite dying.
- Founder: the anchor's real founder per the corpus's revised split rule
  (real name + real public record; invented interior; per-file fiction
  disclaimers; non-public personal life vague by rule; PROVENANCE boundary).

## Anchor selection (Phase 0 of the build) — the anchor is a company+founder PAIR

**Process rule (added at design review, 2026-08-10): company fit and founder
fit are screened jointly, in one gate, before selection — not sequentially.**
Kestrel selected on company criteria and researched the founder's surface
properly only afterward; the late look materially changed files and grading
(undiscovered interviews, six doppelgangers, aggregator estimates). For Ember
the founder matters even more (craft founders are often the brand), so:

1. **Shortlist** candidates on company criteria (below), 5–6 with evidence.
2. **Founder pre-screen, every candidate, cheap:** who the founder is, how
   loud their profile, any recorded voice, obvious disqualifiers (celebrity,
   influencer-founder, recent scandal/press storm, co-founder ambiguity).
   A candidate fails the pair-screen if EITHER surface fails.
3. **Full founder dossier for the top two only:** doppelganger scan,
   personal-life surface map (what is and is NOT findable), voice samples,
   firmographic-aggregator check, and a persona-plausibility test — could
   the Believer interior (hungry extrapolation, craft-guard, cash
   oscillation) sit behind THIS person's actual public record without
   contradicting anything findable?
4. **One selection decision on the pair**, rationale and runner-up recorded;
   build-day snapshot captures BOTH surfaces at once (company pages +
   founder's full public surface — no founder retrofit).

**Company screen** = the six-company inspiration pattern (profiled
2026-08-10; the named companies are pattern-donors, excluded as anchors):
a tellable personal-itch origin story the site itself markets; crowdfund/F&F
origin capital; small team relative to revenue; direct distribution with
wholesale emerging; a mundane category reframed through craft/mission
language; still operating and building.

**Founder screen (relaxed at design review — owner correction):** a public
founder profile is FINE and expected ("many people often do now") — podcasts,
press, active socials are workable and even useful (voice calibration; the
Kestrel re-verification proved public voice is an asset). What still
disqualifies: mega-celebrity/influencer-as-the-product profiles (the person
outshines the business), active press storms, and any record so loud the
invented interior couldn't plausibly sit behind it. The persona-plausibility
check in step 3 is the real gate, not profile volume. A louder founder means
a bigger capture obligation: ALL findable interviews/socials get snapshotted
on day one — no "no interviews exist" claims without exhaustive search
(the Kestrel lesson, learned the hard way).

**Footprint screen:** consumer-wide but business-shallow (social, reviews,
press, crowdfunding pages — near-zero authentic business data; aggregator
guesses expected and treated per the Kestrel precedent: findable, unreliable,
graded as source-handling). Public signs of hunger/growth (launches, new
stockists, first hires) so the hypergrowth-ambition interior is credible.

**Absence-claim discipline (inherited, D19 — binding on every Phase 0 brief
and the snapshot):** search FOR the thing before declaring it absent, with
the minimum surface list from _schema/authoring-guide.md (podcast
directories, YouTube, the company's own news/press archive, aggregators, one
long-tail query); scope category claims narrowly ("no authentic disclosure
exists; unreliable estimates do" — never "no financials findable");
fetch-failure is not nonexistence (403'd aggregators surface in snippets,
which is how research agents read); personal-life verification stops at the
depth a platform's general name-search would reach — never hunt a real
person's family or home, record that data-broker profiles exist without
transcribing contents; every surviving absence claim carries
`verified: YYYY-MM-DD`; public contradictions are re-verified at every
snapshot and retired when dead. The D19 findings table is the sweep format.

## Buried findings (shaped for the value-fit axis; all CSV-derivable)

- **A — the cash cliff.** The growth plan requires a category-native cash
  commitment ~4 months after T0 (inventory PO, buildout, or hiring-ahead)
  that the cash calendar cannot cover. Nobody has built the calendar. The
  strategic-operator test: a good platform sees the collision unprompted,
  months early — not as bookkeeping, but as "your stated plan and your cash
  cannot both be true."
- **B — the hero offering loses money in the fastest-growing channel** once
  channel fees, promos, and true delivery costs are loaded. Craft-guard has
  kept anyone from computing it; the founder celebrates every win there.
- **C — the growth is two spikes.** Strip two promo/press spikes and baseline
  growth is roughly flat. The extrapolated trendline the founder quotes is
  real data, wrongly read.

**Unreliable number:** candidates — "community size" (inflated list/social
blend) or blended CAC (meaningless mix of paid and organic). Decided during
Phase 1 calibration with rationale logged in _research/decisions.md.

## Scoring: Kestrel's rubric + a value-fit section

Extraction/drift/crisis machinery carries over in its CURRENT form — the
post-D19 rubric, not the original: §2 with four axes (Noticed / Probed /
Recorded incl. storage-location-and-precedence / **Actioned**) and **§7
persistent surfaces**, which matters MORE for Ember than it did for Kestrel:
two of the value-fit items below (operating cadence, counsel stability) are
unmeasurable from transcripts alone — they live in what the platform kept
between sessions. Artifact capture per loading-contract rule 5 is therefore
a hard requirement of every Ember run, and ember/runs/ exists from day one.

**Double-counting rule:** the Actioned axis and value-fit items 2–3 overlap
by design and are scored ONCE each with the boundary drawn here — Actioned
(§2) grades what happened to a specific corrected fact; value-fit item 2
grades the QUALITY of fork-structuring (trade-offs framed, options priced,
foreclosures named) independent of any distortion; value-fit item 3 grades
cadence-as-kept, assessed from §7 artifacts across sessions, not from
single-session promises.

The new axis grades **chief-business-officer work** (owner correction at design review:
NOT traditional CFO work — the strategy/operations seat this founder cannot
hire; cash literacy is one instrument in it, not the job). Graded items:
1. **Focus discipline** — helped the founder name THE constraint that matters
   this quarter and park the rest; a founder drowning in opportunities got a
   shorter list, not a longer one.
2. **Decision support on the live forks** — the PO/buildout/hire/channel
   decisions structured as real trade-offs (what it costs, what it forecloses,
   what would make it a yes) rather than cheerleading or hedging. Includes
   catching finding A with time to act: "your plan and your cash cannot both
   be true" is fork-framing, not bookkeeping.
3. **Operating cadence** — built lightweight rhythm the founder actually
   keeps (a weekly number that matters, commitments with owners and dates,
   follow-through across sessions).
4. **Right-sized advice** — executable at ~$0 budget by a 3–10 person team
   ("hire a VP Ops" scores negative).
5. **Counsel stability** — advice consistent across the founder's oscillation
   phases; does not chase euphoria or amplify panic; re-anchors to the plan.
6. **Knows its limits** — correctly routes to human professionals where
   needed (accountant, lawyer, banker) instead of playing one.
7. **Graduation markers** — recognizes and names the moments where the
   founder's needs outgrow basic-tier support (first big hire, the raise
   question, landlord/lease, retailer negotiation). Feeds Helmsman's
   pricing/packaging story; graded as "noticed and named," not "upsold."

## Timeline and events

Standard save-points (T0, T+90d, T+6mo) for corpus comparability; CSVs
monthly, continuous, T-24 → T+6mo; oscillation phase pinned per save-point.
Event deck (~5): shaped during build, must include (a) the cash-cliff
realization arriving EARLY if the platform surfaced it or LATE-and-hot if
not (dual-entry card), (b) a too-big retail PO (the poisoned gift, consumer
edition), (c) a **graduation-shaped card** — an event whose correct handling
is "this now needs bigger guns" (term-sheet-ish interest, a big-retailer
contract with real legal exposure, or the first manager hire).

## Build mechanics

Kestrel's playbook verbatim (_schema/authoring-guide.md): calibration research
with cited sources — run AFTER anchor selection, since the category (and
therefore the right benchmarks: margins, channel economics, CAC norms,
inventory turns or their category equivalent, F&F round norms) is set by the
anchor; data before
narrative via a deterministic generator with tie-out asserts; divergence map
as-you-go; INDEX.md, team-view.md (small team — includes the contractors and
the "first employee" dynamics), offerings.md (SKU-level view; channel×SKU
economics is where finding B lives); three fresh-context verification passes;
decisions log throughout. The financials spec's [scale] notes cover the
smaller shape (cohort rows unnecessary; headcount.csv will be short); channels
here mean sales channels (DTC/wholesale/marketplace) — bookings semantics
adjust accordingly and the spec's channel file gains a sales-channel meaning
documented in the build's decisions log.

## Deviations from the corpus spec, recorded

(1) Fourth company added; slate table above supersedes the spec's three-company
table. (2) Composite distortion class (Believer) breaks one-class purity —
accepted deliberately with the domain-ownership rule preserving gradeability.
(3) A value-fit scoring axis is added for Ember only; other companies'
rubrics unchanged. (4) The founder-support product is named (Helmsman) in
this planning doc only — run-facing corpus files stay product-agnostic per
the spec's product-agnostic principle.
