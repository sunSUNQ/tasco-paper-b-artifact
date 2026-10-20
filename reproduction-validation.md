# 复现验证报告 — Paper B GitHub Candidate (2026-10-20)

## 结果: 39 PASS / 0 FAIL / 4 UNAVAILABLE

### R1(完整性+独立性) — 12 PASS

| 检查 | 结果 |
|---|---|
| python_version ≥ 3.8 | ✓ |
| no_internal_paths | ✓(verify.py 不引用内部研究树路径) |
| manifest_hashes(123 条) | ✓ 0 mismatch |
| layout: paper/prereg/data/mechanisms/analysis/audit/trajectories | ✓ 7 目录齐全 |
| M1/M2/M3 case counts 100/30/30 | ✓ |
| runs 200+60+120 | ✓ |
| pairwise_disjoint | ✓ 零交集 |
| task_count 168(含 Stage-0 8)| ✓ |
| run_count 404(含 Stage-0 24)| ✓ |
| trajectory_count 424(含 smoke 20)| ✓ |

### R2(核心数字重算) — 27 PASS

| 数字 | 重算值 | 冻结值 | 一致 |
|---|---|---|---|
| M1 totals | +7.08% | +7.08% | ✓ |
| M1 case mean | −41.76% | −41.76% | ✓ |
| M1 CI | [−67.66,−20.31] | [−66.69,−20.19] | ✓(bootstrap 容差) |
| M1 W/L | 42/58 | 42/58 | ✓ |
| M2 totals | −2.89% | −2.89% | ✓ |
| M2 case mean | −21.28% | −21.28% | ✓ |
| M2 median | +4.88% | +4.88% | ✓ |
| M2 cache | −17.6% | −17.6% | ✓ |
| M3 totals | +12.44% | +12.44% | ✓ |
| M3 mean | −23.00% | −23.00% | ✓ |
| M3 CI | [−41.09,−7.69] | [−40.76,−7.63] | ✓(bootstrap 容差) |
| grid exposure | 1.6586% | 1.66% | ✓ |
| grid configs | 64 | 64 | ✓ |
| R6 views | 311 | 311 | ✓ |
| R6 recovered | 135 | 135 | ✓ |
| R6 rate | 43.41% | 43.4% | ✓ |
| R6 median dist | 4 | 4 | ✓ |
| R6 chars | 352,804 | 352,804 | ✓ |
| σ̂_w | 0.155 [0.093,0.197] | 0.155 [0.093,0.197] | ✓ |
| σ̂_w arms | 0.258/0.244 | 0.258/0.244 | ✓ |
| D3 triggers | 52,719 | 52,719 | ✓ |
| D3 fraction | 29.52% | 29.5% | ✓ |
| G4 S/R/M | 650,693/158,880/40,600 | 650,693/158,880/40,600 | ✓ |

### R3(UNAVAILABLE) — 4 项

| 项 | 原因 |
|---|---|
| online_LLM_re-execution | 需 live model API |
| raw_trajectory_replay | 424 轨迹待全量扫描+许可审查 |
| tokenizer_exact_attribution | harness 遥测不可观测 |
| G5_model_re-review | 模型辅助审计已记录;人工审核 PENDING |
