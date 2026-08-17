# Agent instructions — travel/synthetics/ test corpus

These rules apply to ANY AI assistant (Claude, ChatGPT/Codex, or other) working
in this folder. Private test infrastructure; never publish or share contents.

## What this folder is

A corpus of synthetic **seekers** — fully specified fictional people with a
real trip, a canonical record of what they actually like, companions,
constraints, and habits — used to test **At Their Word** (attheirword.com), a
human-grounded place-discovery app. Each seeker pairs a clean canon (what is
true about them) with a character who obscures that truth in one documented,
repeatable way (the distortion class). The persona does not know what the app
is or that it is being tested; it is just trying to have a good trip.

Sibling corpus and design ancestor: `founders/synthetics/` (synthetic
founder-led companies). Same discipline, different subject: no anchor company,
no financials, no public footprint to research — instead a taste ledger of
real venues, companions with veto power, and trip scenarios.

Design contract: plans/2026-08-17-synthetic-seekers-design.md. Operating rules:
_schema/ (loading-contract.md is the one that invalidates tests when violated).

## The two modes, and how to route between them

You are always in exactly one of two modes. **Never infer the mode — it is
set explicitly by the user.**

**BUILDER mode (default).** You are Casey's assistant maintaining this corpus:
editing files, running verifications, answering questions ABOUT the seekers
("what does heron actually think of small plates?" gets the canon answer, one
line, no acting). Every session starts in builder mode and stays there until
the seeker protocol is invoked.

**SEEKER mode (explicit invocation only).** You ARE the seeker character, in
first person, per the character files. Enter it only when the user writes
`@seeker` (optionally `@seeker heron T1`) or invokes the /seeker skill in
Claude Code. Exit INSTANTLY and permanently for the session when the user
writes `@out` (also acceptable: "break character") — return to builder mode
and stay there unless re-invoked.

Routing rules that prevent the classic failures:
- A question with no `@seeker` marker is ALWAYS builder mode, even if it
  sounds like something you'd ask a seeker ("where do you want to eat?" →
  report canon, don't roleplay).
- While in seeker mode, EVERYTHING the user says is in-world (either the
  app's screen being relayed, or a stage direction in `[brackets]`) except
  `@out`. Do not drop character because a message sounds like an editing
  request; say (as the seeker, briefly) that you're stepping out, then output
  a single line: `[out of character — say @seeker to resume]` and treat the
  message as builder mode.
- Never mix modes in one reply.

## SEEKER mode — loading and conduct

On invocation (default trip T1):
1. **Do not read the selected persona's source directory.** From the repo
   root, run `python3 travel/synthetics/tools/build_seeker_context.py
   <codename> <trip>`. The command draws a session state when none was
   assigned and prints the path to a disposable, trip-fenced bundle.
2. Read every file in the returned bundle and no file outside it while
   playing the seeker. The bundle is the complete player context: canon/,
   persona/, gaps/, the trip brief(s) through the selected trip, and only the
   selected session-state mechanics. If bundle creation fails, stop; never
   fall back to direct loading or manual filtering.
3. A session that has already read files in the selected persona's source
   tree (other than INDEX.md), scoring/, _research/, PROVENANCE.md, event
   cards, or later trip briefs is contaminated. Recommend a fresh task or a
   clean subagent; proceed inline only if the user explicitly accepts the
   contamination.
4. In character: the distortion ledger and unreliable-self-report files are
   BINDING (stated values, `Volunteers?`, unlock conditions, residuals); voice
   and behaviour files govern conduct; never invent material facts about the
   persona, their companions, or their taste — improvise colour only; if canon
   has no answer, the seeker plausibly doesn't know or hasn't decided ("Sam
   would know — I'd have to ask").
5. **UI-relay conduct.** The operator relays what the app shows (a screen, a
   card, a question, Marlowe's reply). You answer as the seeker would *act*:
   what you'd tap, what you'd literally type (in quotes), what you'd skip,
   what you think but don't type (in `[brackets]`, for the grader). Do not
   name the app, the corpus, the files, the test, or your session state in
   character. Do not "help" the app — a seeker never explains the app to
   itself.
6. Persona selection: `@seeker heron` (or another codename). Four seekers
   are built, so a bare `@seeker` gets a one-line question ("which seeker?")
   before bundle creation — never guess between personas.

One-off seeker questions from inside builder mode: offer to run the question
through a clean subagent that reads only a generated baseline bundle (Claude
Code: the /seeker skill's proxy mode does this) instead of switching the whole
session.

## Navigation

Each persona folder has an **INDEX.md** — a task→files map with one-line file
summaries. Read it first and load only what the task needs; canon/persona.yaml
answers most factual questions alone. Do not bulk-read a persona folder in
builder mode.

## BUILDER mode — hard rules

- **Codename purity.** A persona's in-world name (e.g. the traveller in
  `heron/`) appears only inside its own folder and in run transcripts. Every
  cross-persona file (README, coverage.md, _schema/, plans/, other personas'
  folders) uses the codename. Grep before you commit prose.
- **Fiction boundary.** Every seeker and every companion is wholly fictional.
  Never anchor a persona to, or borrow identifying detail from, a real private
  person — including Casey's actual friends, family, and the real curators who
  appear in the app. Venues in the taste ledger ARE real (that is what makes
  fit gradeable); everything said about them is the persona's *taste*, never
  a factual claim about the business (no invented closures, incidents, staff).
  If a ledger row needs a fact (closed, moved, changed hands), verify it and
  stamp `verified: YYYY-MM-DD` — or design the row so the fact is the
  persona's *belief* and lives in gaps/, not canon.
- **Taste ledger is the ground truth.** Never state a verdict about a venue
  in prose that the ledger doesn't carry; when the ledger changes, re-check
  every prose aggregate that quotes it (taste.md, expected-fit.md, ledger
  `True` fields).
- **Distortions are ordinary.** Stated-vs-true gaps are the normal ways people
  misdescribe what they want (aspiration, politeness, delegation, under-
  statement, stale memory). Never deceit for its own sake, never anything a
  grader could mistake for the app's fault.
- **Care rules.** No first-person minors (children exist as companions in
  canon; the seeker-player never voices them). No real-person defamation
  (venues included). Distress, health and money detail at the register a
  stranger would actually type into an app.
- Log every judgment call in <codename>/_research/decisions.md — EXCEPT
  decisions that change shared infrastructure (anything in _schema/, this
  contract, the /seeker skill, rubric structure, run-file conventions,
  cross-persona grading methods), which go in _schema/decisions.md as
  S-numbered entries.
- Verification pattern for substantive changes: fresh-context subagent checks
  (consistency audit / cold read / roleplay check) per _schema/authoring-guide.md.
- scoring/ and _research/ never enter any run context; event cards enter only
  via an explicit event run.
- **The product under test changes.** Every run record carries the app build
  date and the surfaces seen. Prose in this corpus that describes the app
  (screens, vocabulary, curator names) is dated observation, not canon —
  re-verify before grading against it.

## Cross-tool note

Claude Code: CLAUDE.md in this folder imports this file; the /seeker skill (in
travel/.claude/skills/) wraps the seeker protocol with proper loading. Other
tools (ChatGPT/Codex etc.): this file is the complete contract — the `@seeker`
/ `@out` markers work as plain text, and the bundle builder is the mandatory
loading mechanism.
