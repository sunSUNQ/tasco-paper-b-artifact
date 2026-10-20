# PROVENANCE: exported from the internal TASCO research repository. This script references internal absolute paths and is a provenance record; the runnable reproduction interface is reproduction/verify.py. Source file: pb_step1_overlap.py
"""TASCO-PAPER-B Step 1/3 — sample-overlap verification + evidence-index assembly."""
import hashlib, json, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
R5 = Path(r"D:\tasco-temp\research-semantic-compression\r5")
R4 = Path(r"D:\tasco-temp\research-semantic-compression\r4")
OUT = R5 / "paper-b"


def case_set(path):
    ids = set()
    for l in Path(path).read_text(encoding="utf-8").splitlines():
        if l.strip():
            ids.add(json.loads(l)["case_id"])
    return ids


s100 = case_set(R4 / "100case" / "case-sampling-manifest.jsonl")
s_r1 = case_set(R4 / "refinement" / "refinement-case-manifest.jsonl")
s_next = case_set(R5 / "online" / "next-case-manifest.jsonl")
s_exp = case_set(R5 / "expansion" / "expansion-case-manifest.jsonl")
print("case-set sizes: 100case", len(s100), "| R1", len(s_r1), "| NEXT", len(s_next), "| expansion", len(s_exp))
print("overlaps:", {"100∩R1": len(s100 & s_r1), "100∩NEXT": len(s100 & s_next),
                    "R1∩NEXT": len(s_r1 & s_next), "100∩EXP": len(s100 & s_exp),
                    "R1∩EXP": len(s_r1 & s_exp), "NEXT∩EXP": len(s_next & s_exp),
                    "100∩R1∩NEXT∩EXP": len(s100 & s_r1 & s_next & s_exp)})
# recovery-count consistency across calibers
def _sr(r):
    v = r.get("store_reads")
    if isinstance(v, list):
        return len(v)
    if isinstance(v, int):
        return v
    return 0


r510 = sum(_sr(r) for r in
           [json.loads(l) for l in (R5 / "online" / "paired-results.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
           if r["arm"] == "T")
exp_recs = [json.loads(l) for l in (R5 / "expansion" / "expansion-paired-results.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
exp_rec = sum(len(r.get("store_reads", [])) for r in exp_recs if r["arm"] == "T")
ws = json.loads((R5 / "workload-screening-r1" / "step1-summary.json").read_text(encoding="utf-8"))
print(f"recoveries: R5-10pair T runs = {r510} | expansion T runs = {exp_rec} | R6 census = {ws['recovery_total']} | consistent = {r510 + exp_rec == ws['recovery_total']}")
print(f"stored views: R6 census = {ws['stored_views']} (10pair + expansion T runs = {ws['runs_T']})")
