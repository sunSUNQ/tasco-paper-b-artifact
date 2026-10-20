# EVIDENCE-MAP.md — Paper B Claim → Artifact File

Every number in the paper traces to a specific frozen data file in this artifact.

## Main Results (Table 2)

| Metric | Frozen source | Verification |
|---|---|---|
| M1 input +7.1% (totals) | M1-verification-and-analysis.json → primary_input_reduction = −0.0708 | reproduction/verify.py: R2.M1_totals |
| M1 case mean −41.8% [−66.7,−20.2] | M1-paired-execution-results.jsonl (200 rows) → recomputed | reproduction/verify.py: R2.M1_case_mean, R2.M1_CI |
| M1 542 folds / 561K chars | M1-verification-and-analysis.json → rds_telemetry_T | reproduction/verify.py |
| M1 cache 10.27M→10.74M | M1-paired-execution-results.jsonl (per-run cache_read) | reproduction/verify.py: R2.M1_cache |
| M2 totals −2.9% | M2-verification-and-analysis.json → primary_input_reduction = +0.0289 | reproduction/verify.py: R2.M2_totals |
| M2 2 fold events / 2/30 cases | M2-verification-and-analysis.json → rds_T | reproduction/verify.py |
| M2 cache 5.36M→4.42M | M2-refinement-paired-results.jsonl (per-run cache_read) | reproduction/verify.py: R2.M2_cache |
| M3 totals +12.4% | M3-expansion-analysis.json → totals | reproduction/verify.py: R2.M3_totals |
| M3 mean −23.0% CI [−40.8,−7.6] | M3-expansion-analysis.json → primary_input_benefit + bootstrap95_mean | reproduction/verify.py: R2.M3_mean, R2.M3_CI |
| M3 280 views / 2.81M chars / 123 rec | M3-expansion-analysis.json → totals | reproduction/verify.py |
| M3 cache 2.20M→3.58M (+63.2%) | M3-expansion-analysis.json → totals | reproduction/verify.py: R2.M3_cache |
| M3 +4.7 calls / +2.4 turns / +48% wall | M3-expansion-analysis.json → totals + per-case | reproduction/verify.py |
| M3 task 18→20 | M3-expansion-analysis.json → oracle_B/T_pass_cases | reproduction/verify.py |

## Supplementary Analyses

| Metric | Frozen source | Verification |
|---|---|---|
| σ̂_w = 0.155 [0.093,0.197] | step2-strengthening.json → S1_sigma_w | reproduction/verify.py: R2.sigma_w |
| σ̂_w arms 0.258/0.244 | step2-strengthening.json → S2_sigma_w_arms | reproduction/verify.py: R2.sigma_w_arms |
| Grid max exposure 1.66% (0/64 pass) | grid-results.json + b-deliveries.jsonl + split-70-30.json | reproduction/verify.py: R2.grid_max_exposure |
| R6 311 views / 135 rec / 43.4% / dist 4 | workload-screening-r1/step1-summary.json + view-behavior.jsonl | reproduction/verify.py: R2.R6_* |
| R6 recovered chars 352,804 | r6-view-behavior.jsonl (sum of recovered_chars) | reproduction/verify.py: R2.R6_recovered_chars |
| D3 52,719 triggers / 29.5% | step2-strengthening.json → S4_d3_census | reproduction/verify.py: R2.D3_* |
| G4 S/R/M = 650,693/158,880/40,600 | g4-cost-decomposition.json + g4-final-metrology.json | reproduction/verify.py: R2.G4_* |

## G5 Diagnostic Audit

| File | Content |
|---|---|
| audit/g5-blind-package/blind/S01–S30.json | 30 blind views |
| audit/g5-dual-model-audit-r1/reviewer-a-results.jsonl | Reviewer A results (25 FAIL / 5 PASS) |
| audit/g5-dual-model-audit-r1/reviewer-b-results.jsonl | Reviewer B results (1 FAIL / 29 PASS) |
| audit/g5-dual-model-audit-r1/execution-ledger.jsonl | 92 API calls, all attempts logged |
| audit/g5-diagnostic-risk-rootcause-r1/rc-step1-reconstruction.json | V1/V2/V4 three-layer verification (30/30) |

## Key Metric Calibers (never mixed)

| Caliber | Unit | Files |
|---|---|---|
| Input tokens | non-cached, api-reported | M1/M2/M3 paired results |
| Cache-read tokens | cached re-send | same |
| Flow tokens | in+out+reasoning+cache | same |
| Chars | opportunity proxy | grid-results, view-behavior |
