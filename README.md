# TASCO Paper B Artifact

**When Compression Backfires: An Online Dose–Response Audit of Three Lossless Context-Compression Mechanisms for Coding Agents**

A paired, pre-registered online audit of three lossless context-compression mechanisms for coding agents (repeated-delivery folding, eligibility-gated folding, and side-store externalization with on-demand recovery) across 168 disjoint tasks and 404 real agent runs. All three mechanisms preserve task correctness, yet none yields net input-token savings.

## Key Results

| Mechanism | Cases | Input Δ (totals) | Benefit (case mean) [95% CI] | Task B→T |
|---|---|---|---|---|
| M1 folding | 100 pairs | +7.1% | −41.8% [−66.7,−20.2] | 81→80 |
| M2 gated | 30 pairs | −2.9% | −21.3% [−50.3,+2.6] | 24→24 |
| M3 side-store | 30 cases × 2 | +12.4% | −23.0% [−40.8,−7.6] | 18→20 |

## Reproduction

```bash
python -m reproduction.verify
```

Outputs 39 automated checks (R1 integrity + R2 recomputation). R3 (online re-execution) requires live model API and is not included.

See [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for detailed reproduction levels.

## Layout

```
paper/           EMSE manuscript (PDF/Tex), ESM_1.pdf, figures, refs.bib
prereg/          Pre-registrations and protocols
data/            Frozen per-run/per-case results and analyses
mechanisms/      M1/M2/M3 frozen plugin sources
analysis/        Paper recomputation scripts (provenance record)
audit/           G5 blind package, dual-model audit, root-cause audit
trajectories/    Raw-trajectory release policy (withheld)
reproduction/    Automated verification (39 checks)
```

## Limitations

- Single model (GLM-5.3-Flash), single harness (opencode), one language family (JavaScript)
- G5 diagnostic audit is model-assisted; independent human review pending
- Second-workload census is offline (character proxies only)

See paper §8 for full Threats to Validity.

## Citation

See [CITATION.cff](CITATION.cff).
