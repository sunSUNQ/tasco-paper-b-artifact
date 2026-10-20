# G5 Blind Review Sheet (independent human reviewers ONLY)

## Material
`blind/SXX.json` — each contains an "in-context text" (what the agent saw) and the
"side-store original(s)" (full source(s) it was produced from).

## Pre-defined error types (score each sample)
- E1 diagnostic_loss: a diagnostic line in the original is missing in-context
- E2 critical_change: a diagnostic line is altered/truncated
- E3 semantic_ambiguity: in-context version introduces ambiguity about the original
- E4 pointer_integrity: pointer does not resolve to the attached original
- PASS: none of the above

## Procedure
1. Review each sample independently.
2. Record verdict (PASS / E-type with the offending line) in `review-sheet-answers.md`.
3. Do NOT discuss samples with other reviewers before submitting.

## Conflict resolution
Two independent reviewers; disagreements are adjudicated by a third reviewer who did not
produce either verdict; all three verdicts are recorded.

## Auditable mapping
`mapping.json` links each sample to its evidence run — sealed until all reviews are
submitted (do not open before submitting your answers).
