# Save-point founder-context bundles — implementation plan

**Goal:** Make it impossible for a correctly started founder session to load
information after its selected save-point.

**Architecture:** A single standard-library Python command builds a disposable
player bundle from the source corpus. It copies only player-facing prose,
filters every CSV by its observation date, includes timeline files only through
the selected save-point, rejects unsafe output locations, and writes a manifest
that records the fence and every included file. Founder-mode instructions point
only at this bundle; direct source-tree loading is forbidden.

**Tech stack:** Python 3 standard library and `unittest`; Markdown operating
contracts.

## Global constraints

- Source CSVs remain generated artifacts and are never edited by this work.
- `scoring/`, `_research/`, `PROVENANCE.md`, seeds, event cards, and later
  save-points never enter a player bundle.
- T0 player-facing prose contains no knowledge of post-T0 outcomes.
- Bundle creation fails closed for unknown companies, unsupported save-points,
  malformed temporal CSVs, and non-empty output directories.
- The source corpus remains private and no files are published.

## Task 1 — executable bundle contract

**Files:**

- Create `synthetics/tests/test_build_founder_context.py`
- Create `synthetics/tools/build_founder_context.py`

1. Write integration tests that invoke the command against Ember and Kestrel.
2. Observe the tests fail because the command does not exist.
3. Implement `build_bundle(repo_root, company, save_point, output)` and its CLI.
4. Verify T0 and later bundles contain only permitted paths and dated rows.
5. Verify the manifest reports the selected save-point, cutoff, and file hashes.

## Task 2 — remove baseline future knowledge

**Files:**

- Modify Ember player-facing files under `canon/`, `founder/`, and `gaps/`.
- Add save-point-specific hook material under `timeline/T+90d/` where needed.

1. Add a T0 regression assertion for every already-observed future leak.
2. Observe the assertion fail after the new command copies current source prose.
3. Rewrite T0 material as information available at T0; retain actual later
   outcomes only in the appropriate timeline delta.
4. Verify the T0 bundle does not contain those outcomes and T+90d still does.

## Task 3 — make the safe path mandatory

**Files:**

- Modify `synthetics/AGENTS.md`.
- Modify `.claude/skills/founder/SKILL.md`.
- Modify `synthetics/_schema/loading-contract.md`.
- Modify company indexes/readmes where they describe player loading.
- Modify `synthetics/_schema/decisions.md` with the shared S11 decision.

1. Replace direct source-tree loading instructions with the bundle command.
2. Remove language allowing unfenced loading by “discipline.”
3. Document that a session which has read the source company tree is
   contaminated for founder mode.
4. Run the integration suite and manually inspect Ember T0’s manifest and
   latest temporal rows.

## Definition of done

- `python3 -m unittest discover -s synthetics/tests -v` passes.
- An Ember T0 bundle’s latest observation is `2026-08`.
- No forbidden directory/file or known later-outcome prose appears in it.
- Ember T+90d includes T0 and T+90d state, but nothing from T+6mo.
- Both founder entry contracts require bundle-only loading.
