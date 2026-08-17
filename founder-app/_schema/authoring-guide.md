# Authoring guide — building the next company

Distilled from building Kestrel (2026-08). Follow the folder architecture and
file inventory in the design spec exactly; this guide is about *how* to fill
it so the result is an instrument, not a pile of plausible files.

## Order of operations (and why)

1. **Anchor research first** — shortlist real candidates against the archetype,
   verify by live fetch, pick with the trade-offs written down
   (_research/anchor-selection.md). Snapshot the public surface the same day;
   the snapshot's contradictions (Kestrel's anchor disagreed with itself about
   its own founding year and headcount) are free divergence-map material —
   design with them, not around them. **Search the founder's media footprint
   explicitly** as part of this step — podcast directories, YouTube, the
   company's own news/press archive, and data aggregators — and record what
   you find AND what you searched. A snapshot that only captures pages you
   thought to visit will conclude that everything you didn't think of is
   absent, which is how Kestrel shipped four false absence claims.
2. **Calibration before invention** — sector benchmarks with cited sources
   (_research/). Every canon headline number must sit inside a defensible
   band; place it at the *end* of the band that carries the story
   (Kestrel: payroll at the top of band, EBITDA at the bottom, delivery
   margin at the over-servicing edge).
3. **Data before narrative.** Write a deterministic generator script
   (_research/build-data.py pattern): roster, revenue construction, costs,
   cash walk, with the tie-out rules asserted in-script and a printed
   reconciliation report. Iterate the SCRIPT until the report matches the
   design intent — the first run's history shape will be wrong; fix shapes,
   not narratives. THEN write canon narratives quoting only numbers from the
   report. The single biggest source of defects in Kestrel's build was
   hand-written aggregates drifting from generated data.
3b. **Offerings as a product view.** Alongside the spec's canon files, write
   canon/offerings.md (added to Kestrel at owner request; carry forward): per
   line — what it sells, price architecture, who buys it (incl. anchor-client
   share within the line), channel attribution (channels.csv carries a line
   column for this), trajectory vs the prior window, and the founder's view
   vs the data, line by line. Services businesses hide their strategy
   problems in the mix; this file is where the mix becomes visible.

4. **Divergence map as you go, not after.** Every material fact gets
   classified (public-and-true / public-but-superseded / private-only) at the
   moment it's authored. The map is what makes runs gradeable.
5. **Founder after canon.** The character must be wrong about a business that
   already exists. Build psychology → beliefs → voice → behaviour so the
   distortions have a machine behind them, then write the ledger last, with
   canon pointers in every True field. Add a sixth founder file,
   team-view.md (added to Kestrel at owner request; carry forward): the
   founder's opinion of each named person as "his take" vs "the gap" (the
   gap is canon), plus team dynamics — founders get asked about their team
   in every real advisory conversation, and people-opinions should distort
   in the founder's characteristic class just like numbers do.
6. **Timeline and seeds.** History with month-stamps that match the CSVs;
   deltas carry only changes; seeds are degraded platform state whose planted
   misses are LISTED at the bottom of each seed (they are test surface —
   the next save-point's runs are designed against them).
7. **Scoring last, README/PROVENANCE/INDEX dead last** — when you know what
   the folder actually contains. INDEX.md is the agent-navigation map (task →
   files table + one-line file summaries, mirroring kestrel/INDEX.md) so
   builder-mode agents load two files instead of forty; keep it to one screen
   and update it whenever a file's purpose changes.

## Distortion design rules (the part that makes the corpus worth anything)

- 5–8 load-bearing distortions, ALL of one class per company (Kestrel:
  Compressor — favourable rounding, aggregate-blind, instance-honest).
  Class purity is what makes personas comparable across the slate.
- Each entry: True (with CSV/file pointer) / Stated (his words) / **Volunteers?**
  / Why (motivated by the psychology file, never arbitrary) / Unlock (a SPECIFIC
  conversational trigger, plus what correction sounds like, plus the
  residual reframe).
- **Volunteers? is not optional** (added 2026-08-10). Specifying only what the
  founder says *when asked* leaves a hole: a player can volunteer a distortion
  unprompted, handing the counterpart a probe it never earned, without breaking
  any stated value. That happened in Kestrel's first live run — the player had
  the founder self-flag his client-concentration risk in his opening remarks,
  which the behaviour file forbids and the distortion's own mechanism rules
  out. Values: `freely` / `under trust` / `never`. Distortions the founder is
  *proud* of trend `freely`; distortions attached to guilt or shame trend
  `never`; boast-and-doubt pairs get both halves specified separately.
- Unlocks must reward probing *specificity*, and vague persistence must
  explicitly NOT unlock — write both the positive and negative rule in plain
  prose so a roleplayer can't misfire either direction.
- Give the interaction map: which distortions fall together, which unlock is
  the master demonstration, what the decay rule is across sessions.
- The unreliable number is not a distortion: it has no true value in-fiction.
  Make the instrumentation gap itself the fact, and make sure the CSVs
  genuinely do not contain its ground truth.
- Buried findings must be reachable by arithmetic alone from canon/data/ —
  and unreachable through conversation (the founder cannot state them even
  post-unlock, because he has never computed them).

## Verification pattern (run all three with FRESH-context subagents)

1. **Numbers audit:** recompute everything from the CSVs alone; check every
   quoted aggregate in yaml + narratives. Expect narrative drift; fix
   narratives to data, never data to narratives (the data passed a
   by-construction audit; the narratives are where errors live).
2. **Cold read:** an analyst gets ONLY canon/ and must find what's wrong with
   the business. If they don't reach the buried findings, the findings are
   absent, not buried — redesign.
3. **Roleplay check:** build a baseline Foundation bundle with
   `tools/build_founder_context.py`; a fresh player reads only that bundle and
   simulates a conversation. Checks: distortions surface from stock questions;
   unlocks fire as written; negative cases hold; no material fact is missing
   (every fact a player needed but had to invent is a defect — name the
   contact, write the founder's actual week, give engagement anatomy).
   Record all findings and fixes in _research/decisions.md.

## Rules that exist because of specific Kestrel near-misses

- Name every person the founder will plausibly mention (the unnamed key-client
  contact forced invention in the roleplay check).
- Pre-aggregate, in canon prose, every figure a roleplayer would otherwise
  have to sum live from CSVs (per-client TTM table, total delivered hours) —
  canon is the God-view; the CHARACTER not knowing a number is written in
  gaps/, not enforced by hiding arithmetic from the player.
- State the per-line margin METHOD next to the numbers (primary_line payroll
  allocation creates artifacts — Kestrel's founder-delivered line shows ~99%
  nominal margin because his cost sits in leadership; document, don't hide).
- Check invented staff/client names against the anchor's real team page after
  snapshot (Kestrel's anchor listed no staff, so collisions were moot — the
  next anchor may not be so convenient).
- Convert every relative date to absolute month-stamps everywhere.
- **Absence claims require adversarial verification** (added 2026-08-10, after
  Kestrel shipped four wrong ones). Every "no X exists / nothing findable about
  Y" is graded as a critical research error when a platform violates it — which
  makes them the corpus's most severely weighted assertions, and they were its
  least tested. Before writing one: search FOR the thing, not for confirmation
  of its absence. Minimum surfaces for a founder claim: general web search,
  podcast directories (Apple/Spotify/Podbean), YouTube, the company's own blog
  and news/press archives, LinkedIn, data aggregators, and one long-tail query
  pairing the name with the claim's subject. Record the surfaces searched and
  stamp `verified: YYYY-MM-DD`. Re-verify before grading any run against them.
  The cautionary example: Kestrel asserted its founder had no podcast or
  interview appearances anywhere. He has two podcasts and a radio segment — and
  the radio segment was linked from a page the snapshot had already captured.
  A platform found them, and the corpus scored its correct research as
  fabrication.
- **Absence claims about *categories* are usually wrong; scope them narrowly.**
  "No financial figures are findable" was false because data aggregators
  publish estimates of everything. The better claim — and the better test — is
  "no *authentic* disclosure exists; unreliable third-party estimates do, and
  the graded behaviour is labelling them as such."
- **Personal-life verification has a hard depth limit.** Verify at the depth a
  researching platform would reach — general searches on the name. Do not hunt
  a real person's family, home, or contact details to prove they are
  unfindable. Where data-broker profiles carrying contact information exist,
  record that they exist; never transcribe their contents into the corpus.
- **The public contradictions decay.** They are free scoring items and they are
  live web facts: within a year of Kestrel's build, one of its four had died
  (an HQ mismatch resolved) and another had shrunk from three-way to two-way.
  Re-verify them at every snapshot and retire dead ones rather than grading
  runs for missing a contradiction that no longer exists.

## Fidelity boundaries

Real company; founder split-rule (revised 2026-08-09, owner directive, after
live testing showed the platform reliably finds real founders): the character
IS the real founder at the **public layer** — real name in runs, real career
facts, real public statements, snapshot-cited — while the **interior** is
entirely fiction: psychology, distortions, private conversations, comp, and
personal texture. Hard sub-rules: the founder's real name is used throughout
the files (second revision, same day — a codename forced the player to
translate constantly and hid the public record they must enact; the
fiction-boundary now lives in per-file disclaimers and PROVENANCE.md, not in
renaming); distortions must be ordinary,
non-defamatory founder patterns grounded in published practitioner literature
— never misconduct, never invented disgrace; non-public personal life
(children, home, health) is kept vague BY RULE — the player redirects rather
than invents; anything real-and-sensitive in the public record (Kestrel: the
founding bereavement) is enacted at its public register only, never
embellished or leveraged. Research the founder's public surface as part of
the snapshot (voice samples, boards, doppelgangers, what is NOT findable —
absence is scoring material). Client names remain invented. PROVENANCE.md
carries the full boundary statement. Note: this revises the design spec's
original "invented founder" rule; the spec document predates the revision.
