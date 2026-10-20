# TASCO-R4 — 100-Case Paired RDS Rapid Iteration Protocol (EXPLORATORY, FROZEN at write)

Status: EXPLORATORY EXPERIMENT — explicitly NOT the Formal A/B; results carry no final
statistical-validation claims. Frozen before any model call (sha256 in execution ledger).

## 1. Scope and authorization

Per user directive 2026-10-15: 100 independent cases, each executed once as Baseline (B) and
once as RDS Treatment (T) — 200 planned model calls (plus bounded retries, individually
logged). Model: OpenCode + 火山AI网关/glm-5.3-flash (Stage-0 verified). Budget: user waiver
(R4-EXECUTION-ADDENDUM-V1) continues; token observability = api_reported; cost = NOT
observable (gateway reports none) — no synthetic prices.

## 2. Arms

- **B (Baseline)**: identical workdir, NO plugin. RDS absent.
- **T (Treatment)**: identical workdir + project plugin `.opencode/plugins/rds-plugin.js`
  wrapping the FROZEN v0.11-D3-E5 RDS primitive (`repeated_delivery_suppression.js`,
  verbatim vendored copy; sha recorded). Per-session state under `<workdir>/.rds-state/`.
  Everything else (model, prompt, tools, oracle, timeouts) identical across arms.

## 3. Case sampling (frozen; seed 20261015)

- Universe built from real repo material only: 15 mutation/test-fix (F2P testCommand oracles:
  enterprise 3 + test_repo integration 12), 10 spec-contract analyses (test_repo), 3
  enterprise analyses, 24 module deep-dives (9 test_repo + 14 enterprise src modules, symbol
  oracles pre-extracted at freeze), 48 file reviews (seeded from 114 candidates ≥40 lines).
  **Exactly 100 cases**; families: 15/10/3/24/48.
- **Exclusion (recorded)**: enterprise case 06 (config-rename; oracle `test_channel_config.js`
  exit 0 pre-state — E-M3 type, no discrimination).
- **High-noise representation kept**: mutation/debug family (E-M4-type) retained at 15 cases
  (13 test_repo integration fixes + order_bug + cache_policy + order_client).
- Selection by seeded shuffle within strata; **no case chosen or dropped for expected gain**.
- B/T execution order balanced by seeded coin: 47 B-first / 53 T-first; case execution order
  seeded shuffle (exec_position in manifest).
- Manifest: `case-sampling-manifest.jsonl` (100 records, self-contained prompts + oracles;
  manifest sha256 `f7027226…`).

## 4. Metrics (frozen)

- **Primary**: total input-token reduction `(ΣB − ΣT)/ΣB` (non-cached input, api_reported).
- Secondary: flow-total delta (input+output+reasoning+cache), per-case paired deltas &
  distribution, per-family splits (ALL strata reported — no cherry-picking), success parity
  (oracle pass rate B vs T), RDS trigger telemetry (compressed events, matched chars —
  expected in T only), latency, cache_read, failure/retry rates.
- Correctness gates: T-arm success rate must not degrade >10 percentage points vs B in ANY
  family; any reference/answer leakage, state pollution, or ledger inconsistency ⇒ HOLD.
- Stop rules: per-run timeout 20 min (kill tree; retry ≤2 on infra failure only, logged);
  >20% infra-failure rate across the batch ⇒ HALT; no mid-batch RDS implementation changes
  (a changed implementation = a new batch, per task rule).

## 5. Telemetry & verification

Per run: `events.jsonl` (sha256), stderr log (model identity check), tokens per step
(api_reported), oracle output, workdir retained. T arm additionally: `.rds-state/<session>/
rds_ledger.ndjson` (per-call RDS rows from the frozen primitive). Independent verifier
checks: 1:1 case↔records, arm equivalence (same prompt sha per case), isolation, leakage,
no silent sample deletion, token provenance, marker presence only in T.

## 6. Prohibited

Formal A/B, sample-size expansion, RDS implementation changes mid-batch, product/version/tag
changes, result fabrication, mixing implementations across analysis.
