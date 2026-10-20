# TASCO-R4 Execution Addendum (R4-EXEC-ADDENDUM-V1)

Status: FROZEN at write time (sha256 recorded in execution-ledger before any model call) ·
Supersedes ONLY the budget-gate clause of the R3 stage-0 prereg; every other frozen clause
remains in force unchanged.

## 1. User authorization (recorded verbatim from the 2026-10-15 directive)

- 执行 24 个 Baseline 单元(8 任务 × 3 重复),**不启动 100-Case 实验,不启动正式 A/B**。
- 模型:**当前 OpenCode + GLM-5.3-Flash**(已验证:`providerID=火山AI网关 modelID=glm-5.3-flash`,
  opencode DEBUG 日志,run `ec513eed`;opencode.exe 1.19.0)。
- **项目级 USD / Token 总预算上限:按照用户授权,不额外设置** —— 即用户明示豁免 cap_usd /
  max_total_tokens;本附录即该授权的落盘记录。
- 重试:必须有明确上限(本执行取 ≤2 次/单元)并保留失败记录。
- 不修改默认产品行为,不创建版本、Tag 或 Release。

## 2. Relationship to frozen artifacts

- `r3/rds-stage0-runner/stage0_protocol.json` (sha16 `7a6d089f30e12d4a`): **UNCHANGED** —
  `budget.cap_usd` remains null in the frozen file; the live gate is satisfied via THIS
  addendum (user waiver) rather than by editing frozen history.
- `r3/rds-stage0-prereg.md` (sha16 `38d7993763d69143`): clauses retained except budget cap
  (waived above). Retry limit used: 2 (≤ prereg allowance). Stop conditions retained:
  leakage / isolation failure / ledger inconsistency / executor anomaly ⇒ HOLD.
- Baseline-only: no RDS arm; no benefit inference from these 24 units.

## 3. Frozen task manifest (8 tasks × 3 reps; embedded prompts; hash-frozen at build)

Source: `hook_ab_test/enterprise_test_cases/` (7 cases) + `hook_ab_test/spec_test_cases_v2/01`
(1 case, runs in `test_repo`). Built by `code/r4_freeze_manifest.py` →
`r4/stage0-task-manifest.json` (sha recorded in ledger). Selection rule: all real cases with
deterministic oracles; **no task was chosen or dropped for expected ease**; case 09 was
excluded because its referenced spec file does not exist (defect, documented).

| task_id | source | repo | family | oracle |
|---|---|---|---|---|
| E-M1 | enterprise case 03 (spec-to-code) | enterprise_test_repo | mutation | `node --test tests/unit/test_cache_policy.js` exit 0 |
| E-M2 | enterprise case 05 (api migration) | enterprise_test_repo | mutation | `node --test tests/unit/test_order_client.js` exit 0 |
| E-M3 | enterprise case 06 (config rename) | enterprise_test_repo | mutation | `node --test tests/unit/test_channel_config.js` exit 0 |
| E-M4 | enterprise case 07 (order bug fix) | enterprise_test_repo | mutation | `node --test tests/unit/test_order_bug.js` exit 0 |
| E-A1 | enterprise case 01 (traceability) | enterprise_test_repo | analysis | final text contains requiredAll tokens |
| E-A2 | enterprise case 02 (gap analysis) | enterprise_test_repo | analysis | final text ≥2 of requiredAny tokens |
| E-A3 | enterprise case 04 (bug analysis) | enterprise_test_repo | analysis | final text ≥1 of requiredAny tokens |
| T-A4 | spec_v2 case 01 (contract analysis) | test_repo | analysis | final text ≥3 of section-structure tokens |

## 4. Execution parameters

- Per-unit timeout: 20 min (opencode run killed on breach; unit marked infra_failure).
- Retry: ≤2 per unit on infra failure only (`-r1`/`-r2` suffix); task failures (oracle fail)
  are valid units and are never retried.
- Telemetry: opencode `--format json` step events; tokens from `step_finish.tokens`
  (source=api_reported, granularity = per step; session total = Σ steps = flow total).
  **Cost**: the gateway does not report per-token cost for this setup (smoke `cost: 0`) ⇒
  `cost_usd = null` for all units; tokens are the billing-relevant observable. No synthetic
  price is applied.
- Isolation: fresh copy of the pinned repo per unit (`units/<iid>/workdir`); no state
  carries across units; baseline = RDS disabled (no env, no hooks).
- Model identity re-verification: every unit's DEBUG log must contain
  `modelID=glm-5.3-flash` (spot-checked per unit via `--print-logs`).

## 5. Prohibited

Formal A/B, 100-Case, RDS arm, post-hoc task swaps, threshold tuning, product/version/tag
changes, result fabrication. On severe anomaly: HOLD + preserve evidence.
