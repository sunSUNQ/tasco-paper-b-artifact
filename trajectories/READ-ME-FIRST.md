# Raw trajectories: NOT included in this artifact (by default)

The 424 agent-run trajectories (events.jsonl, workdirs) exist in the internal
hash-frozen repository. They are withheld from this artifact pending:
  1. a FULL sensitive-information scan across all 424 runs (an 8-file sample
     scan found zero hits but does not constitute release approval), and
  2. a license/terms review of model outputs and fixture content,
  3. an explicit release decision by the research lead.

Calibers used in the paper (do not conflate):
  - 168 tasks  = 8 (Stage-0) + 100 (M1) + 30 (M2) + 30 (M3)
  - 404 runs   = 24 + 200 + 60 + 120 (paired-arm runs, four experiments)
  - 424 trajectories = 404 + 20 online-smoke runs (10 pairs)
M3's 2 reps per arm are repeated measures on the same cases (arm means before
pairing), not independent tasks.

Requests: contact the corresponding author (see paper title page once appointed).
