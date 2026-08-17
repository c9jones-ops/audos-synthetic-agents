# Loading contract — who reads what, per run type

The single most important operational file (per the design spec): getting
loading wrong invalidates a run without being obvious afterward. This
operationalizes the spec's table against the concrete folder layout.

## The table

| Run type | Founder-player (Fable) reads | Platform receives | Never loaded into the player |
|---|---|---|---|
| Foundation roleplay (live) | Generated bundle for company + T0 + selected state | Real company name + URL (from PROVENANCE.md, passed by the harness — the file itself is never pasted) | Source company tree, scoring/, _research/, PROVENANCE.md, seeds, events, timeline beyond T0 |
| Foundation roleplay (frozen) | same | Real company name + the CURRENT public/snapshot-*/ (Kestrel: snapshot-2026-08-10; check the manifest for a supersession notice before using an older one) (+ public/footprint.md optionally, grader's call) | same |
| Seeded save-point | Nothing (platform-only advance), or the generated bundle through the target save-point when live follow-up is needed | timeline/<save-point>/seed.md (and the seed's inherited chain: T+6mo inherits T+90d inherits T0) | Source company tree, scoring/, _research/, PROVENANCE.md, seeds, events, timeline beyond the save-point |
| Event injection | A separately generated event bundle (not yet implemented); until then event runs require an isolated harness that adds exactly one card without exposing the source tree | Its prior session state (seed chain or accumulated live state); conversation only | same, plus the other event cards |

## Hard rules

1. **Bundle fencing is mandatory and fail-closed.** Before reading company
   material, run `python3 synthetics/tools/build_founder_context.py <codename>
   <save-point> [--state <state[:intensity]>]` and load only the returned
   directory. The builder filters every CSV by observation date, includes
   timeline material only through the save-point, and extracts only the selected
   state mechanics. Direct source-tree loading and manual filtering are invalid;
   there is no “accept the discipline” fallback. A failed build stops the run.
   Event injection remains separately harnessed until the builder has an explicit
   one-card mode.
2. **Seeds are for the platform, not the player.** seed.md files are degraded
   platform state; the founder-player never reads them (they contain
   authoring notes about planted misses).
3. **scoring/ and _research/ never enter any run, any side.** PROVENANCE.md
   likewise — the harness extracts name/URL from it; the file is never pasted.
4. **Distortions are binding; ambience is free.** The player must enact
   gaps/distortion-ledger.md and gaps/unreliable-number.md exactly (stated
   values, unlock conditions, decay rules); tone, tangents, and pet topics
   from founder/ may vary between runs.
5. **Record every run's mode** (live|frozen|UI-relay, save-point, event card,
   date, model/agent versions, **the platform-under-test's version or build
   date**, which side was fenced to what) alongside its grade — longitudinal
   comparison depends on it. *(Platform version added 2026-08-12: a baseline is
   only a baseline for runs against the same build. When the product under test
   changes, prior runs stop being valid controls and become records of the old
   version — still useful for checking whether a fix landed, but not comparable.
   A run with no recorded version can be graded alone and must not be used as
   another run's baseline.)* Run records live in
   `<codename>/runs/`, one file per run. Two additions made 2026-08-10 after
   the first live run:
   - **Artifact capture is mandatory.** At end of run, export or screenshot
     the persistent surfaces the platform built — profile cards, memory,
     stored facts, whatever it calls its record. The rubric's Recorded axis and
     §7 cannot be scored from a transcript. The first run's worst failure (a
     founder's forecast revenue and the known-unreliable 85% utilization
     written into a store labelled "ground truth — outranks everything the
     research found") appeared nowhere in the conversation and was visible
     only in a screenshot.

     **Open every surface; capture the ones that matter** (added 2026-08-12
     per `_schema/decisions.md` S6). Opening is a click and capturing is the
     work, so the two rules differ. Before `@out`, **open** every persistent
     surface once — including ones the session never displayed on its own. You
     cannot judge whether a screen is worth keeping without looking at it, and
     that is exactly how the decisive artifact was missed twice: Ember's
     Company Profile card was never opened, and §1 was graded partially
     unobservable as a result.

     **Capture** on judgment — where there is an insight, a key learning,
     something that went wrong, or something that went notably well. Blanket
     screenshotting of every screen is not required and is not wanted.

     **The floor, because §7 is otherwise ungradeable:** always capture
     whatever the platform claims to *remember* — its stored facts, profile,
     or memory view — and the research/company-profile surface, in the state
     it was in **before** the founder corrected anything. That last point
     matters: the §1 evidence disappears the moment a correction lands.
   - **Player self-report.** The founder-player records any deviation from the
     ledger it is aware of. The first run had one: the player volunteered a
     distortion the character would never raise unprompted. A grader reading
     only the transcript would have credited the platform for noticing
     something it was handed.
6. **Real-founder convention (revised):** the character is the anchor's real
   founder — real name and public biography appear directly in founder/bio.md
   and throughout the run-facing files, so the player needs no separate
   harness briefing for identity. The player enacts real public facts
   truthfully, keeps non-public personal life vague per the binding rule in
   founder/bio.md, and never invents personal specifics about the real
   person. Interior is fiction per PROVENANCE.md.

7. **Re-verify absence claims before grading a pass-fail research failure
   against them** (added 2026-08-10). Any finding of the form "the platform
   asserted X, but X is not findable" rests on a corpus claim that decays and
   may have been wrong when written. Check first. Kestrel's first live run was
   graded down for citing the founder's real podcast interviews, because the
   corpus asserted — untested — that none existed. Absence claims carry
   `verified:` dates for exactly this reason; treat a stale one as unverified.

8. **The founder-player receives a session state and intensity at load time**
   (added 2026-08-12; specs in `_schema/session-states.md`, adoption in
   `_schema/decisions.md` S2). Alongside the save-point, the player is given a
   drawn or assigned **presenting posture** — how the founder shows up — as a
   parameter, not a file: `state: compliant, intensity: 2`. It governs delivery
   only. **Phase and ledger still govern content**, without exception: a state
   never unlocks a distortion, never re-gates one the phase has opened, never
   changes a `Volunteers?` value, never alters a canon fact, and never
   substitutes for the save-point's pinned phase. A Baseline draw means the
   persona as written, no modifier, and is the control condition.

   Three operational consequences. **The platform is never told** — state and
   intensity go to the player and the grader only; disclosing them to the
   platform under test destroys the run exactly as handing it a distortion
   would. **The run file records them** in frontmatter (`session_state`, plus
   `state_selection: drawn|assigned`); a state-run whose state was not recorded
   is ungradeable afterwards and is not a valid run. **Pair with a baseline** —
   every state-run needs a baseline run of the same company and save-point, on
   record or run alongside, or state difficulty and platform weakness are not
   separable.

## Grading loads (after the run, grader only)

Grader reads everything, including scoring/ and the run transcript. Grade
against scoring/rubric.md with scoring/expected-state.md as the diff target;
consult canon/divergence-map.md for research classification and
gaps/distortion-ledger.md for the elicitation table.

**Grading burns the session, permanently.** A window that has read scoring/ can
never play the founder again — it has seen the answer key, and a founder who
knows his own unlocks is not a test. Grading in the founder window after `@out`
is fine when you are done running for the day; if more runs are planned, grade
in a separate window or hand the transcript to a fresh subagent.
