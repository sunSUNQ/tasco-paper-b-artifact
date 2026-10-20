# PROVENANCE: exported from the internal TASCO research repository. This script references internal absolute paths and is a provenance record; the runnable reproduction interface is reproduction/verify.py. Source file: fp_supplement_gen.py
"""Generate supplement content (grid table, win/loss tables) + compile support files."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
FP = Path(r"D:\tasco-temp\research-semantic-compression\r5\paper-b\full-paper-r1")
R4 = Path(r"D:\tasco-temp\research-semantic-compression\r4")
R5 = Path(r"D:\tasco-temp\research-semantic-compression\r5")

def jload(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))

def jlines(p):
    return [json.loads(l) for l in Path(p).read_text(encoding="utf-8").splitlines() if l.strip()]

grid = jload(R4 / "refinement-r2" / "grid-results.json")
deliveries = jlines(R4 / "refinement-r2" / "b-deliveries.jsonl")
split = jload(R4 / "refinement-r2" / "split-70-30.json")
hold = set(split["holdout"])
tot = sum(x["chars"] for d in deliveries if d["case_id"] in hold for x in d["rows"])

lines = ["% auto-generated from frozen grid-results.json; exposure = hold chars / " + str(tot),
         "\\begin{longtable}{@{}lrrrr@{}}", "\\toprule",
         "Config & Hold cov. & Hold chars & Exposure\\% & Blocked risk \\\\",
         "\\midrule"]
max_exp, best = 0.0, None
for k in sorted(grid["grid"].keys()):
    v = grid["grid"][k]["hold"]
    exp = v["chars"] / tot * 100
    cov = v.get("coverage") or 0.0
    risk = v.get("risk", 0)
    if exp > max_exp:
        max_exp, best = exp, k
    lines.append(f"{k.replace('_','/')} & {cov:.3f} & {v['chars']:,} & {exp:.2f} & {risk} \\\\")
lines += ["\\bottomrule",
          f"\\caption{{Full 64-configuration eligibility grid (holdout replay). "
          f"Max exposure {max_exp:.2f}\\% ({best.replace('_', '/')}); no configuration reaches the "
          f"$\\geq$2\\% exposure $\\wedge$ $\\geq$1/3 coverage gates. Risk = blocked "
          f"target/specification/diagnostic folds. All volumes are opportunity proxies.}}",
          "\\end{longtable}"]
(FP / "supplement" / "supplement-grid.tex").write_text("\n".join(lines), encoding="utf-8")
print("grid table rows:", len(grid["grid"]), "max exposure:", round(max_exp, 4), best)

# win/loss + leave-one-out from phaseA family stats
a2 = jload(FP / "analysis" / "phaseA-family-stats.json")
out = {"M1": {"loo_range": a2["M1_RDS"]["leave_one_out_mean_range"],
              "median": a2["M1_RDS"]["median_benefit"],
              "wlt": a2["M1_RDS"]["win_loss_tie"]},
       "M2": {"loo_range": a2["M2_gated"]["leave_one_out_mean_range"],
              "median": a2["M2_gated"]["median_benefit"],
              "wlt": a2["M2_gated"]["win_loss_tie"]}}
(FP / "supplement" / "supplement-robustness.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("robustness json written")
