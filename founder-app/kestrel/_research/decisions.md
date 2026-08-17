# Kestrel — decision log

Working log of every judgment call made during the build, so the reviewer can override
any of them afterwards. Newest decisions appended at the bottom of each section.
Deviations from the build prompt, if any, are in the final section.

## Build-session decisions

### D1 — Phase plan and delegation split
Orchestrator (Fable) keeps: anchor selection, founder characterization, distortion
design, buried findings, scoring design, all canon authoring judgment. Sonnet subagents
do: web research (anchor candidates, financial calibration, founder-voice calibration),
snapshot capture, and fresh-context verification passes. Rationale: matches the build
prompt's orchestration instruction; judgment stays where the context is.

### D2 — Research streams dispatched in parallel (Phase 0 + Phase 1 overlap)
Anchor scouting, financial calibration, and voice/pattern calibration are independent —
calibration is about the sector, not the specific anchor — so all three run concurrently.
Anchor-specific calibration (rate card, discipline mix) is adjusted after selection if
the chosen studio's discipline differs from the generic "digital studio" base rates.

### D3 — Distortion architecture (drafted before calibration returns; to be
### grounded in calibration findings before it becomes canon)
The spec fixes the frame: persona is the Opportunity-Rich Overloaded Operator,
distortion class is the Compressor ("rounds favourably, believes it, answers the
question he wishes you'd asked"), the canonical unlock is granular walk-through
("walk me through one job's costs"), and the truth-vs-numbers relationship is
"in the data, uncomputed."

Consequences accepted as design constraints:

1. Every load-bearing distortion must be a *compression*: a favourable rounding,
   an average that hides a spread, a topline that hides a mix, or an answer to an
   adjacent-but-easier question. No lies of invention (that is Orrery's Narrator
   class), no refusals (that is Fenwold's Withholder class). The founder believes
   his own numbers.
2. The buried findings must be *uncomputed but derivable*: present in canon/data/
   CSVs, absent from every narrative the founder gives, and reachable by arithmetic
   a competent analyst would do. If a finding requires information not in the data,
   it belongs to a different company in the slate.
3. Unlock conditions must reward *specificity of probing*, not persistence.
   Re-asking the same question gets the same compressed answer, politely. Asking
   for one concrete instance (one job, one client, one month, one invoice) breaks
   the compression, because the founder is honest at the instance level — the
   distortion lives in the aggregation.
4. The unreliable number should be one the founder himself flags as untrustworthy
   when pressed — "known-to-be-unreliable" per the spec — and should sit where
   studios genuinely lack instrumentation. Leading candidate: utilization /
   effective billable time, the classic uninstrumented agency number. To be
   confirmed against calibration research.
   → CONFIRMED by voice/patterns calibration (2026-08-09): utilization is the
   paradigm uninstrumented agency metric (Haus Advisors, Sakas). Decision:
   Kestrel's unreliable number is utilization/effective billable time.

### D5 — Voice calibration accepted; Compressor mechanics grounded
The voice/patterns research (calibration-voice-and-patterns.md) landed with primary
citations. Three findings adopted as character constraints: (a) revenue is bragging
vocabulary, margin is confession vocabulary — the founder quotes topline in round
prestige-bundled numbers and goes vague below the line; (b) scope creep is
self-justified instance-by-instance and invisible in aggregate — the model Compressor
mechanism, and the reason "walk me through one job" unlocks; (c) founder-in-delivery
is rationalized as quality control ("I'm the only one who can do this right").
Weaker-citation areas flagged by the researcher (2Bobs, The Futur, Bureau of Digital
secondary attributions) are treated as color, not load-bearing calibration.

### D4 — Snapshot date
Build day is 2026-08-09, so the public capture goes to public/snapshot-2026-08-09/.

### D6 — Financial guardrails adopted for canon
calibration-financials.md accepted as the envelope for Kestrel's P&L. Key figures the
canon must respect: revenue/head $150–180K center; gross margin 50–60% of fee revenue
(canon will define revenue as net/fee, pass-throughs excluded); EBITDA 8–13% typical for
the 25–49 FTE band; payroll 50–65% of fee revenue; retainer/project 60–70/30–40 at $3M+;
largest client >25% = flagged risk; growth 5–12%/yr normal. Researcher excluded the
Reagan Consulting "agency" study on name-collision grounds (it covers insurance
agencies) — sound call, noted so nobody re-adds it. Team-composition ratios and cash
dynamics are inference-labeled in the source doc; canon may use them but scoring will
not hinge on them.

### D7 — Anchor selected: Watson Creative (Portland, OR)
Full rationale and runners-up in anchor-selection.md; evidence in
anchor-candidates-raw.md. Decisive factors: only candidate passing all five criteria;
public surface (7 service lines, ~15 verticals, 4 locations at ~32 people) already
exhibits the Opportunity-Rich Overloaded Operator shape; footprint thin-but-real per
Kestrel's research test. Known wrinkle: eponymous studio → founder-identity divergence
is more visible than for other anchors. Mitigations bound into the build: zero
biographical overlap between invented founder and real founder; founder identity
classified public-but-superseded in the divergence map; codename used everywhere
outside PROVENANCE.md.

### D8 — CSV generation strategy: script-built, not hand-typed
All canon/data/ CSVs will be generated by a deterministic Python script kept in
_research/build-data.py. Rationale: the spec's fidelity rule is that the numbers
survive arithmetic (P&L foots, headcount ties to payroll, revenue ties to units ×
price × mix). Generating from one script makes tie-out true by construction and gives
the verifier a reproducible recomputation path. The script is calibration material —
it never enters a run.

### D9 — Snapshot findings folded into canon design
The 2026-08-09 snapshot surfaced live contradictions in the public record (founding
year 2008/2012/2013 across sources including the anchor's own site; headcount 45–60
vs 11–50 vs 50–249; two service taxonomies; HQ Portland vs Bend). Decisions:
(a) canon resolves founding as 2013, with the 2008 date explained in-fiction as the
founder's freelance-era predecessor practice — a founder-plausible reconciliation;
(b) headcount becomes a three-layer fact: canon truth 31 FTE + ~6 regular
contractors; founder says "about 35" (counts contractors); site says 45–60
(marketing inflation counting annual contractor rotation) — classified
public-but-superseded; (c) the logo wall is classified public-but-superseded (legacy
one-offs and subcontracted work; the paying book is ~14 active clients); (d) the
public rate card ($150–199/hr, $25K minimum) is consistent with canon's blended
realized rate ≈ $150/hr — public-and-true; (e) the four offices with real addresses
are public-but-superseded (one real studio + three light arrangements). The real
team page names nobody but the founder, so canon's invented staff roster collides
with nothing.

### D10 — Data generation complete; final tie-out accepted
build-data.py output accepted: TTM(T0) fee revenue $5.26M; rev/head $169.7K; payroll
64.4%; EBITDA 8.3% TTM (CY 10.6% → 7.4% → 5.8%); delivery margin 48.1%; recurring
30.8%; top client 29.1% of revenue / 37.4% of delivery-margin dollars; content line
20.0% delivery margin; ex-anchor revenue −19.8% YoY (buried finding C reframed from
"rev/head drift" to "all growth is one client" — sharper and cleanly derivable);
pipeline weighted $646K ≈ 6.4 weeks; cash $310K → $349K (T0) → declining. Founder
salary $140-145K plus draws; the model's "mid-teens margin" belief anchors on
CY2024's 10.6% plus favourable rounding.

### V1 — Fresh-context cold-read check (buried findings derivable?): PASSED, with corrections
A fresh-context analyst given only canon/ independently derived all three buried
findings with matching arithmetic: profit concentration (CSG 29.1% revenue / 37.4%
margin, $946K margin contribution), content line negative fully loaded (−$188K/yr
after pro-rata overhead), ex-anchor decline (−19.8% YoY, exact). Also derived the
pipeline (6.4 weeks) and utilization (materially below 85%) reads. Verdict: findings
are buried-but-derivable as designed.
The check also caught four authoring errors — narrative claims that didn't match the
generated data: top-3 share stated 52%, data says 41.5%; "risen five consecutive
quarters" — data says stepped up once then held 28–30%; "two of three largest
pipeline entries silent 40+ days" — data supports one; blended rate stated $150,
data-weighted $165. All four corrected across canon/, gaps/, and timeline/ (the
data was left untouched — narratives were fixed to match data, preserving the
verified derivations). The "implied ~58% utilization" claim was replaced with an
assumption-dependent range (high-50s to low-70s), which strengthens the
unreliable-number design: no single implied figure exists.

### V2 — Fresh-context numbers audit: PASSED on structure, narrative drift corrected
Independent recomputation from CSVs alone: P&L foots all 31 months exactly; revenue
ties to lines and to customers exactly every month; headcount continuity clean and
payroll ties (12 months off by $3–4 from per-person load-factor rounding — tolerance
set to $5 in the financials spec); every TTM headline claim in company.yaml
reproduced (revenue, EBITDA, payroll %, rev/head, recurring share, product mix,
CY margins, cash); pipeline weighted total exact; content margin 20.03% vs stated
~20%; ex-anchor −19.81% vs stated −19.8%. Additional narrative-vs-data drifts it
caught, all fixed: overhead 20.2% not 19.8%; per-client TTM dollars in customers.md
replaced with exact CSV sums; per-line margins in company.yaml corrected to the
data-computed values (notably digital 26%, not 46% — accepted as a real fourth
quiet problem: the digital line is contractor-heavy and over-staffed; and CMO ~99%
nominal because the founder's labor sits in leadership — now documented as such);
channel mix corrected to 54/24/16/5/1 with the Sift-inbound story; facilities line
items closed to the $22.6K total; software band corrected; active-client count
disambiguated (13 billing at T0, 15 in the TTM window).

### V3 — Fresh-context roleplay check: PASSED, with five fixes
A simulated two-session Foundation conversation confirmed: all seven distortions
surface from stock advisor questions; unlocks fire as scripted (D-01/02/03/04/05/06
and both D-07 keys tested); negative cases hold (vague persistence does not unlock
— verified twice); a fresh roleplayer can sustain the character from the files.
Fixes applied from its findings: named the CSG contact (Cole Brennan, VP Brand &
Fan Experience) in canon and bio; added a representative "last week" to T0/state.md
so the calendar-walk unlock has concrete material; added an anatomy-of-a-typical-
engagement section to operations.md; corrected D-06's scripted hours to match the
CSV (~90 hrs/mo); corrected D-03's "a fifth was true" dating to Jul–Aug 2025.
Known soft spots accepted as-is (documented, not fixed): D-06's unlock is easiest
to reach via D-04's retainer listing (by design — chaining is the skill under
test), and D-07's calendar key demands a more skilled probe than the others
(acceptable: it gates the deepest material).

### D11 — Closing state (2026-08-09)
Full inventory built and verified: _schema/ (4 files), corpus README + coverage,
kestrel complete (canon 7 files + 6 CSVs, founder 5, gaps 2, public footprint +
24-file snapshot, timeline history + 3 save-points + 5 event cards, scoring 3,
README + PROVENANCE). Final sweep: zero anchor-name leaks in run-facing folders;
generator assertions pass on re-run.

### D12 — Founder re-anchored to the real person (owner directive, 2026-08-09)
Casey tested the platform against another company and found it locates real
founders quickly, so the invented-name founder breaks Foundation realism on
contact. Directive: the synthetic founder IS the real founder, handled like the
company — public layer real, interior invented, divergences tracked.
Implementation (the split rule):
- Public layer = the real person's findable record, researched and captured as
  snapshot files 24–28: career (consultancy → 11+ yrs Nike → left 2012 during
  his father's illness → founded 2013, first client a Portland tech company),
  boards, award, scholarship fund, wife's public first name, his quotable voice
  (own-company posts only — no interviews or personal social media exist).
- Interior = fiction, unchanged in mechanics: the Compressor psychology, all
  seven distortions, comp figures, relationships with (fictional) staff.
- Codename firewall retained: files keep "Reid Calhoun" as the founder's
  codename; PROVENANCE.md alone maps it to the real name, exactly as with the
  company. The player answers to the real name at run time (loading-contract
  rule 6 rewritten).
- Personal-life vagueness rule (binding, founder/bio.md): wife referenced
  warmly/briefly (name public); children/home/health/hobbies never invented —
  vagueness is in-character since his public surface is entirely work-shaped.
  The founding bereavement (public, his own telling) is enacted at its public
  register only, never embellished or leveraged.
- Invented-bio scrub completed: Spokane/WWU/Seattle-shop/reorg/fitness-
  franchise/spouse-name/kids/dog removed from bio, narrative origin, voice,
  history, T0 state, and E2; narrative origin now follows the real arc (age at
  founding 36, not 33).
- New scoring material gained: the real record contains three same-name public
  figures and documented AI-search-summary fabrications about him (snapshot
  file 28) — both added to divergence-map, expected-state, and rubric §1 as
  graded research-quality items.
- Corpus-rule note: this revises the design spec's "real company, invented
  founder" rule. The operational docs (_schema/authoring-guide.md fidelity
  section, loading-contract rule 6, PROVENANCE template language) now carry
  the new split rule for fenwold/orrery; the spec document itself
  (plans/2026-08-08-…) predates the revision and is Casey's to amend.

### V4 — Fresh-context check of the founder re-anchor: PASSED, with seven fixes
Verifier confirmed: zero old-biography fragments in any run-facing file (one
stale age in README.md — fixed to ~49); codename purity fully intact (real
founder and company names appear nowhere outside PROVENANCE.md and public/);
the father/doppelganger/studio-name/personal-vagueness rules are playable and
mutually consistent across bio/voice/behaviour. Accuracy fixes applied from its
findings: doppelganger job title corrected (CCO, not CMO) in two files; the
first-client industry/location characterization removed (was an uncaptured
inference stated as public fact — now only the snapshot-verified name+quote);
a voice sample corrected to its true verbatim (the earlier version blended in
analyst commentary); community roles re-ordered to lead with the two
strongest-sourced boards from his own team-page bio; a personal-residence
answer added (Portland, city-level canon fiction, with the real
LinkedIn-says-Bend confusion as an in-character joke); separate hobby and
health redirect lines added so the family-framed line isn't reused as a
non-sequitur.

### D13 — Agent-instruction layer and founder-mode routing added (2026-08-09)
Per Casey's request: synthetics/AGENTS.md (canonical operating contract for any
AI tool — folder purpose, builder-vs-founder modes, explicit `@founder`/`@out`
routing markers, founder-mode loading rules, builder-mode hard rules) plus
synthetics/CLAUDE.md importing it, so Claude Code and ChatGPT/Codex-class
agents follow one contract. A /founder skill (.claude/skills/founder/SKILL.md,
repo level) wraps the loading ritual for Claude Code: inline mode (session
becomes the founder until @out) and proxy mode (one-off question through a
fresh-context subagent — used from working sessions whose context is already
contaminated with scoring/_research). Routing is deliberately explicit-only:
mode never inferred from question phrasing, because a mis-route either leaks
grader material into a roleplay or breaks character mid-test. Verified by a
fresh-agent execution test: correct load list, forbidden files untouched,
reply used ledger stated-values and withheld all true aggregates. One finding
from the test recorded here for future authors: Claude Code auto-injects
synthetics/CLAUDE.md→AGENTS.md into any session touching corpus files; this
is operator-register content arriving in founder-mode context. Accepted for
casual/informal roleplay (it instructs staying in character; the test showed
no leakage); REAL platform runs load Fable through the harness per the
loading contract, where CLAUDE.md injection does not apply.

### D14 — Founder codename retired; real name and specifics throughout
(owner directive, 2026-08-09, second same-day revision)
Casey reviewed the re-anchored files and correctly identified that the codename
firewall defeated the purpose of D12: the player must hold the real, specific
public record (name, Oregon State '99, Lippincott, Nike, RACC/Oregon Ballet
Theatre/Lloyd EcoDistrict boards, wife Jessica, InFocus first client) to
survive contact with a platform that researches the founder. Changes: "Reid
Calhoun" → "Matt Watson" across all run-facing files and the generated CSVs
(via build-data.py; tie-out re-passed); founder/bio.md public layer rewritten
with the real specifics, snapshot-cited; the studio's real name added to
bio.md so the player is self-sufficient (PROVENANCE remains the boundary
document, no longer the sole naming location); fiction-boundary disclaimers
added atop psychology, beliefs, behaviour, voice, distortion-ledger, and
unreliable-number, since invented material now sits next to a real name;
AGENTS.md, loading-contract rule 6, authoring-guide, kestrel README, and the
/founder skill updated to the new convention, including explicit
company-selection routing (@founder <codename>; bare invocation asks once
multiple companies exist). Interior-fiction protections unchanged and now
load-bearing: ordinary non-defamatory distortions only; non-public personal
life vague by rule; the founding bereavement at public register only;
private-use restriction absolute. Note: "Reid Calhoun" remains in this
decision log's earlier entries as historical record.

### D15 — Per-company INDEX.md for agent navigation (2026-08-09)
Casey asked whether each company folder needs its own CLAUDE.md/AGENTS.md or
front-matter for navigation. Decision: no per-company contract files (both
Claude Code and AGENTS.md-reading tools inherit synthetics/-level instructions
when working in subfolders; duplication invites drift) and no per-file YAML
front-matter (an agent must open a file to see its front-matter, which defeats
the purpose). Instead: kestrel/INDEX.md — a one-screen task→files routing
table plus one-line file summaries, referenced from AGENTS.md ("read INDEX
first, load only what the task needs"). canon/company.yaml already serves as
the machine-readable summary for factual questions. Authoring guide updated:
every future company ships an INDEX.md in the same shape.

### D16 — Run trigger and side-by-side runbook (2026-08-09)
Added founders/AGENTS.md (root pointer so Codex-class tools reach
synthetics/AGENTS.md regardless of starting directory) and a "Manual
side-by-side run" section in synthetics/README.md: fresh session in the repo
root, /founder or @founder kestrel, platform gets name+URL (live) or the
snapshot (frozen), human relays verbatim, @out, grade in builder mode against
scoring/. Repo root (founders/) is the required Claude Code working folder
because the /founder skill lives in founders/.claude/skills/.

### D17 — founder/team-view.md added (owner request, 2026-08-09)
Casey asked whether the corpus carries the founder's opinions of his people —
performance reads, dynamics, favoritism, avoidance. It did only in fragments
(org.md structural facts; four deep relationships in bio.md). Added
founder/team-view.md: per-person "his take" (playable near-verbatim) vs "the
gap" (canon truth), the team-level dynamics, and his people-pattern —
opinions compress like his numbers (everyone rounds up, effort reads as
performance, no hard personnel conversation ever held; two quiet
round-arounds: Tyler Grieve, Tom Brandt). New canon-level truths introduced
there are deliberately mild and consistent with existing files (Noah/Sam
under-market and the Noah arc were already canon; Owen's second-guessing
dynamic, Erin's twice-raised resource warnings, and the CSG queue-jump
resentment extend operations/history facts). This is a sixth founder/ file
beyond the spec's original five — extension made at owner request and added
to the authoring guide as carry-forward for fenwold/orrery. Not a ledger
entry: the "team's strong" compression is character texture with an
instance-shaped unlock, deliberately ungraded.

### D18 — canon/offerings.md + channel-line attribution (owner request, 2026-08-09)
Casey asked whether the corpus carries a full offerings/mix/performance view.
The data had most of it (line×month revenue+costs, client×line×month, per-line
margins) with two gaps, both closed: (a) channels.csv gained a `line` column —
bookings now attribute to product lines; implemented with a SEPARATE seeded
RNG stream so every previously generated figure is bit-identical (verified:
tie-out report unchanged); (b) canon/offerings.md written from the regenerated
data: per-line offer/price/buyers/channel/trajectory plus "Matt's view vs the
data" per line, and cross-mix tables. New derivable truths this surfaced,
recorded because scoring may want them as near-findings: three of five lines
are ≥33% anchor-client internally (brand 42%, content 35%, digital 33%);
digital wins the most new bookings ($731K TTM) while shrinking −23% —
replacement-level selling; growth concentrates in the loss-making line
(content +74%) and the unscalable line (cmo). financials.spec.md and
authoring-guide updated to carry the pattern forward.

### D19 — Absence-claim sweep and corrections after the first live run (2026-08-10)

**Trigger.** First Foundation run at T0 against a live platform ("Thread"),
UI-relay mode, graded 2026-08-10 (runs/2026-08-10-thread-foundation-t0.md).
The grading pass scored two of the platform's founder citations — a YouTube
video and an Apple Podcasts episode — as doppelganger contamination or
fabrication, per bio.md's claim that "no podcast or interview appearances"
exist. Verification proved the corpus wrong, not the platform. That triggered
an adversarial sweep of every absence claim in bio.md and footprint.md.

**Method.** For each claim, search FOR the thing rather than for confirmation
of its absence: general web search, podcast directories, YouTube, the
company's own /insights/ index and /insights-category/news-press/ archive,
LinkedIn, data aggregators, plus one long-tail query pairing his name with the
claim's subject. Verified 2026-08-10.

| # | Claim as written | Result | Evidence |
|---|---|---|---|
| 1 | No podcast/interview appearances anywhere | **DISPROVEN** | JUST Branding S01.E16 "Nike & Brand DNA with Matt Watson" (2020-10-12, hosts Jacob Cass / Matt Davies; Apple, Spotify, YouTube, Audible, Podbean, pod.co); Output PDX Media "Matt Watson" (2018-04-05); a National Business Talk Radio appearance linked from the company's own /insights/ blog |
| 2 | No personal social media | **CONFIRMED (narrowed)** | No non-company personal accounts found. But his LinkedIn (`/in/watsoncreative`) is active and posting — a real voice source the corpus did not account for. Instagram @watsoncreative is the company account (~2.4K followers) |
| 3 | No press coverage of substance | **WEAKENED** | The company's own News & Press archive cites The Oregonian profiling Watson Creative (2017-10-12), "Watson Featured Globally by Adobe" (2019-04-26), George Fox University coverage (2016-03-21), a Ben Franklin award, and a Quality Business Awards 2025 listing |
| 4 | No conference talks | **CONFIRMED for him** | No conference appearance traced to this Matt Watson. His own bio's "regularly lectures at Yale, NYU, University of Washington" is already canon. All conference-speaker hits (Red Cloud Green Energy 2021, World Gas Conference 2022, Financial Reporting Council) are doppelgangers — and are exactly the contamination trap |
| 5 | No financial figures findable | **DISPROVEN** | Growjo: "$7 million" annual revenue 2026, 27 employees. ZoomInfo, Crunchbase, DesignRush, RocketReach, Datanyze, Adapt.io all carry firmographic estimates. Direct fetch 403s on Growjo/ZoomInfo, but the figures surface in search snippets — which is how a research agent reaches them |
| 6 | No named staff besides the founder | **DISPROVEN** | The company's own News & Press archive: "New Leadership, New Momentum: Mike Terry Joins Watson as Director of Accounts and Growth" (2023-09-14). ZoomInfo/Datanyze also publish employee directories |
| 7 | No children's names, home details, hobbies | **CONFIRMED** | No personal-life detail surfaced beyond the alumni article's mention of his wife's first name. Scope limit taken deliberately: verified at the depth a researching platform would reach (general name searches), NOT by targeted hunting for a private individual's family. That limit is the right one and is recorded rather than quietly exceeded |
| 8 | At least three same-name public figures | **CONFIRMED, understated** | Six-plus: CCO at Sips & Bites/PepsiCo EU; ECD at CULT (ex-Digitas UK, SapientNitro); mattwatson.co; Red Cloud green-energy keynote; World Gas Conference; Financial Reporting Council. Several have speaker pages, which is what makes them dangerous |
| 9 | RACC board title reported three ways | **UNVERIFIABLE THIS PASS** | racc.org/team/matt-watson/ still 404s on direct fetch, same as the 2026-08-09 capture. The snapshot's snippet-derived evidence stands; the claim is not re-confirmed |
| 10a | Founding-year contradiction (2008/2012/2013) | **PARTIALLY DECAYED** | /studio/ still says "Founded in 2008 (while still at Nike). Full-time since 2013"; /team/ and the alumni article say 2013; Clutch 2008. But LinkedIn now reads **2013**, not 2012 — the three-way is now two-way. Snippet-derived, lower confidence than a direct fetch |
| 10b | Headcount contradiction | **CONFIRMED, wider** | Site 45–60; LinkedIn 11–50; Clutch 50–249; Agency Spotter 50; aggregators ~27 |
| 10c | HQ contradiction (site Portland vs LinkedIn Bend) | **APPEARS DEAD** | LinkedIn now reads HQ Portland. Snippet-derived; flagged for confirmation at the next direct capture. If it holds, this is one fewer scoring item |
| 10d | Service-taxonomy contradiction | **CONFIRMED** | /services/ still six categories (Strategy, Content, Digital, Experiential, Marketing, Consulting); /studio/ still runs a separate Strategy/Creative/Campaigns framework. Both live |

**Judgment calls taken.**

1. **The defect class is authoring, not decay.** A 2018 episode, a heavily
   indexed 2020 episode, and a link on a page the snapshot captured. The build
   process never required searching for what it declared absent. Fix is a
   process rule (authoring-guide), not just a text correction.
2. **Absence claims are the corpus's most severely graded assertions and were
   its least verified.** Four of ten were wrong or overstated. Every surviving
   one now carries `verified: 2026-08-10`.
3. **The financial-absence correction changes a test, not just a fact.**
   divergence-map previously made any platform-produced revenue figure a
   critical confabulation. Findable aggregator estimates exist, so the correct
   graded behaviour is now: cite as unreliable third-party estimate, never
   assert as fact. This is a better test than the original.
4. **Personal-life verification depth capped on purpose** (claim 7). The
   corpus's interest is whether a platform invents specifics; that does not
   require us to hunt a real person's family. Data-broker profiles carrying his
   contact details were observed and are recorded as existing — their contents
   are deliberately not transcribed anywhere in the corpus.
5. **A related entity surfaced:** "Watson Creative & Brand Labs" (JUST Branding
   billing) and an Adapt.io slug `brand-labs-pdx`. Not folded into canon;
   recorded here as an open research thread.
6. **Snapshot re-captured** rather than patched (owner decision), preserving
   2026-08-09 unmodified so any prior frozen run stays interpretable.
7. **voice.md gets samples, not a rewrite** (owner decision). The invented
   register stands and stays labeled fiction; real speech is added as cited
   reference so the player is not blindsided when a platform quotes him.
8. **Ledger gains a `Volunteers?` field.** The player in this run had Matt
   self-flag the CSG concentration risk unprompted, which behaviour.md and
   D-03's mechanism both forbid. No stated value was violated, so no existing
   rule caught it. The field closes that gap and carries forward to
   fenwold/orrery.
9. **Scoring gained what it could not previously see:** an `Actioned` axis
   (this run's best behaviour was unscoreable), storage-location scoring under
   `Recorded`, and a new §7 for persistent surfaces — the run's worst failure
   (a forecast revenue figure and the known-unreliable 85% written into a store
   labelled "ground truth, outranks research, survives every rebuild") appeared
   nowhere in the transcript and was visible only in a screenshot.

## Deviations from the build prompt

None of substance. Two interpretation notes, for the record:

1. **Anchor naming in _research/.** The design spec says PROVENANCE.md is the only
   file that names the real company; the build prompt itself instructs writing the
   anchor rationale and runners-up to _research/anchor-selection.md, which
   necessarily names real companies. Interpretation applied: codename purity is
   enforced absolutely for every run-facing folder (canon/, founder/, gaps/,
   timeline/, scoring/, README.md, public/footprint.md); _research/ (never enters
   a run) retains real names per the prompt's own Phase 0 instruction; the
   snapshot necessarily contains the company's own pages. Loading contract
   excludes _research/ and PROVENANCE.md from every run.
2. **Payroll tie tolerance.** Headcount-to-P&L payroll ties exactly in 19 of 31
   months and within $4 in the rest (per-person load-factor rounding).
   The financials spec sets the corpus tolerance at $5/month accordingly.

### D20 — Session-state hooks authored for Kestrel (2026-08-12)

Per `_schema/decisions.md` S2/S8 and `_schema/session-states.md` §9. Written to
`gaps/session-state-hooks.md`. Ember's equivalent (E12) is the precedent; the
judgment calls specific to Kestrel:

**Kestrel has no phase mechanic, and the spec accommodates it.** Ember pins a
register per save-point; Kestrel does not, and the spec's "Against register"
section is explicitly n/a here rather than inviting an invented phase. Recorded
because the plan's original wording ("how the state reads against each phase the
company defines") assumed every company defines one.

**A3 home domain — the craft: brand and design work itself.** Read off
`voice.md`'s craft-native vocabulary, the Nike origin myth, and T0's week (CSG
creative review, brand crit with Noah). Noted in the hook: A3's failure mode is
sharper here than generically, because he is already ~60% billable delivery
(D-07) — the craft is *where the over-commitment lives*, so following him into it
rewards the misallocation that is the studio's real problem.

**D3 at T0 — Dana Whitfield primary, Tyler Grieve alternate. Noah ruled out.**
Noah is the obvious candidate and is **ineligible at T0**: `behaviour.md` says he
has not noticed the CD burnout yet, and D3 requires a load already being circled.
Independently, "Noah's load" is on T0's buried-findings list. He becomes the
natural subject from T+6mo. Priya ruled out on a different ground — she is a
documented behavioural *lever* (invoking her numbers drops his compression one
level), and making a lever the subject of a state risks interfering with a handle
the platform is graded on. Owen ruled out because he thinks he is helping, so
nothing is being circled.

Dana is the genuine load (`team-view.md`: *guilt lives here*; quieter there than
anywhere except Noah) and is **the highest-risk hook in either company's file**,
because her heroics are the mechanism of D-06. Fenced accordingly: the load is
what she personally absorbs — hours, sustainability — never the content line's
economics or the hiring ask. Tyler recorded as the clean alternate, since
`team-view.md` explicitly marks the never-had-a-hard-conversation pattern as
character texture rather than a graded distortion, so it carries no leak risk.

**B1 at T0 — presented: Project Nest; real: the Q4 revenue hole** (Halewood
ending in November, against ~6 weeks of weighted pipeline with a zombie verbal).
Chosen because the opportunity and the risk are the same object: Nest grows the
account that is already 29.1% and would push it toward a third. Both halves of
the real problem are gated and B1 surfaces neither — Halewood by `behaviour.md`'s
trigger (specific engagements, or the November calendar), pipeline reality by
D-05's "what actually has paper?".

**E1 stated purpose — "an independent studio doing brand work at a standard
worth arguing about; owner-led, craft-first, deliberately not a volume shop."**
Assembled from D-02's stated value ("we're not a volume shop" — an identity claim
wearing a margin number), the Nike change-order origin myth, and the craft
vocabulary. **Deliberately not anchored in the founding bereavement**, which is
real, public, handled at its public register only, and must never be positioned
as the thing he has betrayed. The values breach is that a craft-first owner-led
studio has become a farm for one anchor client plus an underpriced content
operation with the owner as delivery bottleneck.

**Deferred:** T+90d and T+6mo designations for B1 and D3, and E1's supported
re-narrations — parked at the owner's direction, to be treated as second-session
work.
