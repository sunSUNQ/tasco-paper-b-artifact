# Code Availability

## Analysis and verification scripts (included in this artifact)

All scripts used to compute the paper's numbers from the frozen data are included
in `analysis/` and `reproduction/`:

- `reproduction/verify.py` — 39 automated R1/R2 checks (the primary reproduction entry point)
- `analysis/fp_phase_a.py` — unified mechanism table, family statistics with bootstrap CIs
- `analysis/fp_figures.py` — all 7 paper figures (color, vector PDF)
- `analysis/fp_supplement_gen.py` — supplement table generation
- `analysis/colorize_tables.py` — table semantic color markup
- `analysis/fig1_integrate.py` — Figure 1 integration build
- `analysis/f0_lanes.py` — Figure 1 lanes variant
- `analysis/emse_figures.py` — EMSE figure set
- `analysis/pb_step1_overlap.py` — sample disjointness verification

All scripts use deterministic computation with fixed seeds. No model calls are
required for any analysis in this artifact.

## Mechanism source code (included in this artifact)

The frozen compression mechanism implementations are in `mechanisms/`:

- `rds-impl/post_tool/repeated_delivery_suppression.js` — M1/M2 RDS primitive (142 lines)
- `rds-impl/guard_core/runtime_paths.js` — session-state helper
- `rds-plugin-template.js` — M1 plugin wrapper
- `rds-v2-plugin-template.js` — M2 gated plugin wrapper
- `view-store-plugin-template.js` — M3 side-store plugin
- `refine_gate_tests.mjs` — M2 gate tests (9 gates)
- `rds-selftest.js` — M1 smoke selftest

These are frozen as deployed in the online experiments. The M3 implementation has
known diagnostic-visibility defects (disclosed in the paper, Section 5.7).

## Provenance note

The `analysis/` scripts reference internal absolute paths from the original research
environment and are included as provenance records. The `reproduction/verify.py` is
the self-contained reproduction entry point that uses only package-relative paths.
