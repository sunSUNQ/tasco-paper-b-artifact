# Data Availability

## Frozen per-case and per-run results (included in this artifact)

All quantitative results in the paper are derived from the following frozen data files,
included in `data/`:

- `M1-paired-execution-results.jsonl` — 200 runs (100 B/T pairs), M1 repeated-delivery folding
- `M2-refinement-paired-results.jsonl` — 60 runs (30 B/T pairs), M2 eligibility-gated folding
- `M3-expansion-paired-results.jsonl` — 120 runs (30 cases × 2 reps × 2 arms), M3 side-store externalization
- `M3-expansion-analysis.json` — per-case arm means, bootstrap CIs, per-family/stratum results
- `grid-results.json` — 64-configuration offline eligibility grid
- `r6-view-behavior.jsonl` — 311 per-view behavior records (70 treatment runs)
- `step2-strengthening.json` — S1 (σ̂_w), S2 (arm noise), S3 (recovery attribution), S4 (D3 census), S5 (diagnostic audit)

These files contain aggregate and per-case token counts, oracle results, and mechanism
telemetry. No API credentials, personal information, or restricted third-party data
are included.

## Raw agent trajectories (NOT included)

The full 424 agent-run trajectories (events, workdirs, model outputs) exist in the
internal hash-frozen repository. They are withheld from this artifact pending:
1. A full sensitive-information scan across all 424 runs
2. A license/terms review of model outputs and fixture content
3. An explicit release decision by the research lead

See `trajectories/READ-ME-FIRST.md` for the release policy.

## Second-corpus census (D3)

The D3 census (15,000 sessions) was performed on a public HuggingFace corpus.
Only aggregate counts are reported (52,719 triggers, 366M chars saved). The raw
trajectories belong to the respective dataset publishers and are not redistributed.
