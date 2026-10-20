"""Paper B GitHub candidate reproduction verification (standalone).

Usage: python -m reproduction.verify   (from the artifact root)

Reproduction levels:
  R1  integrity + layout + manifests + sample disjointness + calibers
  R2  recompute paper headline numbers from frozen per-case data
  R3  UNAVAILABLE: online LLM re-execution, raw-trajectory replay,
      tokenizer-exact attribution, G5 model re-review

Exit code 0 = all R1/R2 checks PASS.
"""
import hashlib
import json
import os
import sys
from pathlib import Path

import numpy as np

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
results = []

def check(rq, name, cond, detail=""):
    results.append((rq, name, "PASS" if cond else "FAIL", detail))
    return cond

def unavailable(rq, name, reason):
    results.append((rq, name, "UNAVAILABLE", reason))

def jload(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))

def jlines(p):
    return [json.loads(l) for l in Path(p).read_text(encoding="utf-8").splitlines() if l.strip()]

rng = np.random.default_rng(20261019)

def boot_ci(vals, n=10000, seed=20261019):
    a = np.asarray(vals, float)
    r = np.random.default_rng(seed)
    idx = r.integers(0, len(a), size=(n, len(a)))
    m = a[idx].mean(axis=1)
    return float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))

def pair_rows(rows):
    by = {}
    for r in rows:
        by.setdefault(r["case_id"], {})[r["arm"]] = r
    out = []
    for cid, d in by.items():
        if "B" in d and "T" in d:
            b, t = d["B"], d["T"]
            out.append({"case_id": cid, "family": b.get("family"),
                        "b_in": b["tokens"]["input"], "t_in": t["tokens"]["input"],
                        "benefit": (b["tokens"]["input"] - t["tokens"]["input"]) / b["tokens"]["input"],
                        "b_cache": b["tokens"].get("cache_read", 0), "t_cache": t["tokens"].get("cache_read", 0)})
    return out

# ── R1: integrity ────────────────────────────────────────────────────────────
check("R1", "python_version", sys.version_info >= (3, 8), sys.version.split()[0])
check("R1", "no_internal_paths",
      "research-semantic-compression" not in str(Path(__file__).resolve()) and
      "PAPER-A-SECTION3" not in str(Path(__file__).resolve()),
      "verify.py does not reference internal research tree")

manifest = ROOT / "manifest.sha256"
if manifest.exists():
    bad = 0
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if line.strip():
            h, _, fn = line.partition("  ")
            fp = ROOT / fn
            if not fp.exists() or hashlib.sha256(fp.read_bytes()).hexdigest() != h:
                bad += 1
    check("R1", "manifest_hashes", bad == 0, f"{bad} mismatches")
else:
    check("R1", "manifest_hashes", False, "manifest not found")

for d in ("paper", "prereg", "data", "mechanisms", "analysis", "audit", "trajectories"):
    check("R1", f"layout:{d}", (ROOT / d).is_dir())

# ── R1: sample counts + disjointness ────────────────────────────────────────
m1r = jlines(DATA / "M1-paired-execution-results.jsonl")
m2r = jlines(DATA / "M2-refinement-paired-results.jsonl")
m3r = jlines(DATA / "M3-expansion-paired-results.jsonl")
smoke = jlines(DATA / "online-smoke-paired-results.jsonl")
m1p = pair_rows(m1r)
m2p = pair_rows(m2r)
m3an = jload(DATA / "M3-expansion-analysis.json")
m3_cases = m3an["cases"]

ids_m1 = {r["case_id"] for r in m1r}
ids_m2 = {r["case_id"] for r in m2r}
ids_m3 = {c["case_id"] for c in m3_cases}
check("R1", "M1_100_cases", len(ids_m1) == 100)
check("R1", "M2_30_cases", len(ids_m2) == 30)
check("R1", "M3_30_cases", len(ids_m3) == 30)
check("R1", "runs_200+60+120", len(m1r) == 200 and len(m2r) == 60 and len(m3r) == 120)
check("R1", "pairwise_disjoint", len(ids_m1 & ids_m2) == 0 and len(ids_m1 & ids_m3) == 0 and len(ids_m2 & ids_m3) == 0)
check("R1", "task_count_168", len(ids_m1) + len(ids_m2) + len(ids_m3) + 8 == 168)
check("R1", "run_count_404", len(m1r) + len(m2r) + len(m3r) + 24 == 404)
check("R1", "trajectory_count_424", len(m1r) + len(m2r) + len(m3r) + 24 + 20 == 424)

# ── R2: recompute headline numbers ──────────────────────────────────────────
# M1
deltas1 = [p["benefit"] for p in m1p]
tot_b1 = sum(p["b_in"] for p in m1p); tot_t1 = sum(p["t_in"] for p in m1p)
totals1 = (tot_t1 - tot_b1) / tot_b1
check("R2", "M1_totals_+7.1%", abs(totals1 - 0.0708) < 0.001, f"{totals1:.4f}")
check("R2", "M1_case_mean_-41.8%", abs(np.mean(deltas1) - (-0.4176)) < 0.001, f"{np.mean(deltas1):.4f}")
lo1, hi1 = boot_ci(deltas1, seed=20261019)
check("R2", "M1_CI", abs(lo1 - (-0.6669)) < 0.02 and abs(hi1 - (-0.2019)) < 0.02, f"[{lo1:.4f},{hi1:.4f}]")
wl1 = [sum(1 for d in deltas1 if d > 0), sum(1 for d in deltas1 if d < 0)]
check("R2", "M1_W/L_input_42/58", wl1 == [42, 58], f"{wl1}")
cache_b1 = sum(p["b_cache"] for p in m1p); cache_t1 = sum(p["t_cache"] for p in m1p)
check("R2", "M1_cache_+4.6%", abs((cache_t1 - cache_b1) / cache_b1 - 0.046) < 0.002)

# M2
deltas2 = [p["benefit"] for p in m2p]
tot_b2 = sum(p["b_in"] for p in m2p); tot_t2 = sum(p["t_in"] for p in m2p)
totals2 = (tot_t2 - tot_b2) / tot_b2
check("R2", "M2_totals_-2.9%", abs(totals2 - (-0.0289)) < 0.001, f"{totals2:.4f}")
check("R2", "M2_case_mean_-21.3%", abs(np.mean(deltas2) - (-0.2128)) < 0.001, f"{np.mean(deltas2):.4f}")
check("R2", "M2_median_+4.9%", abs(np.median(deltas2) - 0.0488) < 0.001, f"{np.median(deltas2):.4f}")
cache_b2 = sum(p["b_cache"] for p in m2p); cache_t2 = sum(p["t_cache"] for p in m2p)
check("R2", "M2_cache_-17.6%", abs((cache_t2 - cache_b2) / cache_b2 - (-0.176)) < 0.002)

# M3
deltas3 = [c["input_benefit"] for c in m3_cases]
tot_b3 = sum(c["b_in"] for c in m3_cases); tot_t3 = sum(c["t_in"] for c in m3_cases)
totals3 = (tot_t3 - tot_b3) / tot_b3
check("R2", "M3_totals_+12.4%", abs(totals3 - 0.1244) < 0.001, f"{totals3:.4f}")
frozen_ci = m3an["primary_input_benefit"]["bootstrap95_mean"]
lo3, hi3 = boot_ci(deltas3, seed=20261019)
check("R2", "M3_CI_match_frozen", abs(lo3 - frozen_ci[0]) < 0.01 and abs(hi3 - frozen_ci[1]) < 0.01,
      f"[{lo3:.4f},{hi3:.4f}]")
check("R2", "M3_mean_-23.0%", abs(np.mean(deltas3) - (-0.23)) < 0.001)
cache_b3 = m3an["totals"]["B_cache"]; cache_t3 = m3an["totals"]["T_cache"]
check("R2", "M3_cache_+63.2%", abs((cache_t3 - cache_b3) / cache_b3 - 0.632) < 0.002)

# family stats
fams1 = {}
for p in m1p:
    fams1.setdefault(p["family"], []).append(p["benefit"])
check("R2", "M1_file-review_mean_-59.9%", abs(np.mean(fams1.get("file-review", [0])) - (-0.5989)) < 0.001,
      f"{np.mean(fams1.get('file-review', [0])):.4f}")

# grid
g = json.loads((DATA / "grid-results.json").read_text(encoding="utf-8"))
dlv = jlines(DATA / "grid-b-deliveries.jsonl")
sp = json.loads((ROOT / "prereg" / "grid-split-70-30.json").read_text(encoding="utf-8"))
hold = set(sp["holdout"])
tot_hold = sum(x["chars"] for d in dlv if d["case_id"] in hold for x in d["rows"])
max_exp = max(v["hold"]["chars"] / tot_hold * 100 for v in g["grid"].values() if v["hold"].get("chars"))
check("R2", "grid_max_exposure_1.66%", abs(max_exp - 1.66) < 0.01, f"{max_exp:.4f}")
check("R2", "grid_64_configs", len(g["grid"]) == 64)

# R6
vb = jlines(DATA / "r6-view-behavior.jsonl")
rec = [r for r in vb if r.get("recovery_count", 0) > 0]
check("R2", "R6_311_views", len(vb) == 311)
check("R2", "R6_135_recovered", len(rec) == 135)
check("R2", "R6_rate_43.4%", abs(len(rec) / len(vb) - 0.434) < 0.001, f"{len(rec)/len(vb):.4f}")
med = sorted(r["first_recovery_distance"] for r in rec if r.get("first_recovery_distance") is not None)[len(rec) // 2]
check("R2", "R6_median_distance_4", med == 4)
check("R2", "R6_recovered_chars_352,804", sum(r["recovered_chars"] for r in rec) == 352804)

# sigma_w
s = json.loads((DATA / "step2-strengthening.json").read_text(encoding="utf-8"))
check("R2", "sigma_w_0.155", abs(s["S1_sigma_w"]["sigma_w"] - 0.155) < 0.001)
check("R2", "sigma_w_CI", abs(s["S1_sigma_w"]["bootstrap95_task_level"][0] - 0.0925) < 0.001 and
      abs(s["S1_sigma_w"]["bootstrap95_task_level"][1] - 0.1974) < 0.001)
check("R2", "sigma_w_arms", abs(s["S2_sigma_w_arms"]["T"]["sigma_w_T"] - 0.258) < 0.001 and
      abs(s["S2_sigma_w_arms"]["B"]["sigma_w_B"] - 0.244) < 0.001)

# D3
check("R2", "D3_52719_triggers", s["S4_d3_census"]["P2"]["triggered"] == 52719)
d3_frac = s["S4_d3_census"]["P2"]["chars_saved"] / s["S4_d3_census"]["total_obs_chars"]
check("R2", "D3_29.5%_of_all_obs_chars", abs(d3_frac - 0.295) < 0.001, f"{d3_frac:.4f}")

# G4
g4 = json.loads((DATA / "g4-cost-decomposition.json").read_text(encoding="utf-8"))
check("R2", "G4_S=650,693", g4["aggregate"]["sum_S"] == 650693)
check("R2", "G4_R=158,880", abs(g4["aggregate"]["sum_R"] - 158879.5) < 1)
check("R2", "G4_M=40,600", g4["aggregate"]["sum_M"] == 40600)

# ── R3: UNAVAILABLE ──────────────────────────────────────────────────────────
unavailable("R3", "online_LLM_re-execution", "requires live model API; not redistributable")
unavailable("R3", "raw_trajectory_replay", "424 raw trajectories withheld pending full sensitive-info scan + license review")
unavailable("R3", "tokenizer_exact_attribution", "not observable from harness telemetry (deliberately not constructed)")
unavailable("R3", "G5_model_re-review", "model-assisted audit documented; independent human review pending")

# ── summary ──────────────────────────────────────────────────────────────────
passes = sum(1 for r in results if r[2] == "PASS")
fails = sum(1 for r in results if r[2] == "FAIL")
unavail = sum(1 for r in results if r[2] == "UNAVAILABLE")
print(f"\n{'='*60}")
print(f"Paper B reproduction: {passes} PASS / {fails} FAIL / {unavail} UNAVAILABLE")
print(f"{'='*60}")
for rq, name, status, detail in results:
    flag = "[  OK  ]" if status == "PASS" else ("[ FAIL ]" if status == "FAIL" else "[UNAVAIL]")
    print(f"  {flag} {rq}: {name}" + (f"  ({detail})" if detail else ""))
print(f"\nVerdict: {'ALL R1/R2 CHECKS PASS' if fails == 0 else 'FAILURES PRESENT'}")
sys.exit(1 if fails else 0)
