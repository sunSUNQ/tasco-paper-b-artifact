# Reproducibility

## Levels

| Level | Description | Status |
|---|---|---|
| R1 | Artifact integrity, layout, manifest hashes, sample disjointness, caliber arithmetic | ✅ Supported |
| R2 | Recompute paper headline numbers from frozen per-case data (bootstrap CIs, family stats, grid exposure, R6 rates, G4 decomposition) | ✅ Supported |
| R3 | Online LLM re-execution, raw-trajectory replay, tokenizer-exact attribution, G5 model re-review | ❌ Not available in this artifact |

## Quick start

```bash
python -m reproduction.verify
```

This runs 39 automated checks (R1 + R2). Exit code 0 = all checks pass.

## What R2 verifies

Every number in the paper's Table 2 (Unified mechanism table) is recomputed from
the frozen per-case/per-run JSONL files and compared against the frozen analysis
JSONs. The bootstrap uses a fixed seed (20261019) and is deterministic.

## What R3 would require

- Live model API access (GLM-5.3-Flash via a Volcano-Engine-compatible gateway)
- The 424 raw agent-run trajectories (withheld pending sensitive-info scan)
- Tokenizer-exact token accounting (not observable from harness telemetry)

These are documented as limitations in the paper (Section 8) and cannot be
reproduced from this artifact alone.

## Data files

All frozen data files are in `data/`. Key files:

| File | Role |
|---|---|
| M1-paired-execution-results.jsonl | M1 per-run paired results (200 runs) |
| M2-refinement-paired-results.jsonl | M2 per-run paired results (60 runs) |
| M3-expansion-paired-results.jsonl | M3 per-run paired results (120 runs) |
| M3-expansion-analysis.json | M3 per-case arm means + frozen analysis |
| grid-results.json | 64-config eligibility grid |
| r6-view-behavior.jsonl | R6 per-view behavior (311 views) |
| step2-strengthening.json | S1–S5 strengthening analyses |
