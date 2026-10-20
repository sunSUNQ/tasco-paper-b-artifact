# PROVENANCE: exported from the internal TASCO research repository. This script references internal absolute paths and is a provenance record; the runnable reproduction interface is reproduction/verify.py. Source file: fp_figures.py
"""FULL-PAPER-EXPANSION-R1 — figures from frozen data (grayscale-safe, vector PDF).

Validates f4 against the frozen grid verdict (max exposure 1.66%) before use.
Outputs -> full-paper-r1/figures/*.pdf
"""
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
plt.rcParams.update({"font.size": 8, "axes.linewidth": 0.6,
                     "pdf.fonttype": 42, "ps.fonttype": 42})
FIG = Path(r"D:\tasco-temp\research-semantic-compression\r5\paper-b\full-paper-r1\figures")
FIG.mkdir(parents=True, exist_ok=True)
R4 = Path(r"D:\tasco-temp\research-semantic-compression\r4")
R5 = Path(r"D:\tasco-temp\research-semantic-compression\r5")

def jload(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))

def jlines(p):
    return [json.loads(l) for l in Path(p).read_text(encoding="utf-8").splitlines() if l.strip()]

# ---------- data ----------
m1_rows = jlines(R4 / "100case" / "paired-execution-results.jsonl")
m2_rows = jlines(R4 / "refinement" / "refinement-paired-results.jsonl")
m3_an = jload(R5 / "expansion" / "expansion-analysis.json")
m1_an = jload(R4 / "100case" / "verification-and-analysis.json")["analysis"]
m2_an = jload(R4 / "refinement" / "verification-and-analysis.json")["analysis"]
grid = jload(R4 / "refinement-r2" / "grid-results.json")
vb = jlines(R5 / "workload-screening-r1" / "view-behavior.jsonl")

def pair_rows(rows):
    by = {}
    for r in rows:
        by.setdefault(r["case_id"], {})[r["arm"]] = r
    out = []
    for cid, d in by.items():
        if "B" in d and "T" in d:
            b, t = d["B"], d["T"]
            out.append({"case_id": cid, "family": b.get("family"),
                        "benefit": (b["tokens"]["input"] - t["tokens"]["input"]) / b["tokens"]["input"]})
    return out

m1p = pair_rows(m1_rows)
m2p = pair_rows(m2_rows)
m3p = [{"case_id": c["case_id"], "family": c["family"], "benefit": c["input_benefit"]}
       for c in m3_an["cases"]]

# ---------- f0 design overview ----------
fig, ax = plt.subplots(figsize=(7.0, 2.6))
ax.axis("off")
boxes = [
    (0.01, 0.55, 0.16, 0.34, "170 disjoint tasks\n2 JS repositories\n1 stack: opencode +\nGLM-5.3-Flash"),
    (0.20, 0.72, 0.20, 0.20, "M1 RDS folding\n100 pairs (high dose)"),
    (0.20, 0.44, 0.20, 0.20, "M2 gated folding\n30 pairs (safe dose)"),
    (0.20, 0.16, 0.20, 0.20, "M3 side-store\n30 cases x 2 reps"),
    (0.44, 0.44, 0.19, 0.48, "Paired B/T arms\nseed-balanced AB/BA\noracle: frozen tests\n+ text oracles"),
    (0.67, 0.60, 0.15, 0.32, "Calibers\ninput / cache / flow\ntokens; chars proxy;\ntool calls; wall"),
    (0.67, 0.16, 0.15, 0.32, "Offline instruments\n64-config grid;\nrecovery screening;\nG5 replay audit"),
    (0.855, 0.38, 0.135, 0.54, "Findings\nF1 compensation\nF2 exposure collapse\nF3 re-injection\nexposure < noise"),
]
for x, y, w, h, t in boxes:
    ax.add_patch(plt.Rectangle((x, y), w, h, fill=False, lw=0.9, edgecolor="black"))
    ax.text(x + w / 2, y + h / 2, t, ha="center", va="center", fontsize=6.4)
arrows = [(0.17, 0.72, 0.20, 0.82), (0.17, 0.62, 0.20, 0.54), (0.17, 0.55, 0.20, 0.26),
          (0.40, 0.82, 0.44, 0.72), (0.40, 0.54, 0.44, 0.66), (0.40, 0.26, 0.44, 0.52),
          (0.63, 0.68, 0.67, 0.76), (0.63, 0.55, 0.67, 0.40), (0.63, 0.26, 0.67, 0.26),
          (0.82, 0.76, 0.855, 0.72), (0.82, 0.32, 0.855, 0.52)]
for x0, y0, x1, y1 in arrows:
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="->", lw=0.7, color="0.25"))
ax.set_xlim(0, 1)
ax.set_ylim(0.08, 1.0)
fig.tight_layout(pad=0.3)
fig.savefig(FIG / "f0_design_overview.pdf")
plt.close(fig)

# ---------- f1 unified benefit (case-equal-weight, with CI) ----------
def boot_ci(vals, n=10000, seed=20261019):
    a = np.asarray(vals, float)
    r = np.random.default_rng(seed)
    idx = r.integers(0, len(a), size=(n, len(a)))
    m = a[idx].mean(axis=1)
    return np.percentile(m, 2.5), np.percentile(m, 97.5)

mechs = [
    ("M1 folding\n(100 pairs)", [p["benefit"] for p in m1p], 0.071),
    ("M2 gated\n(30 pairs)", [p["benefit"] for p in m2p], -0.029),
    ("M3 side-store\n(30 cases x 2)", [p["benefit"] for p in m3p], 0.124),
]
fig, ax = plt.subplots(figsize=(3.4, 2.4))
hatches = ["", "//", "xx"]
for i, (lbl, vals, tot) in enumerate(mechs):
    m = float(np.mean(vals))
    lo, hi = boot_ci(vals)
    ax.bar(i, m * 100, width=0.55, color="0.75", hatch=hatches[i], edgecolor="black", lw=0.6,
           label="case-equal-weight mean")
    ax.errorbar(i, m * 100, yerr=[[abs(lo - m) * 100], [abs(hi - m) * 100]], fmt="none",
                ecolor="black", elinewidth=0.8, capsize=3)
    ax.plot(i, -tot * 100, marker="D", color="black", markersize=4.5,
            label="totals-based input delta" if i == 0 else None)
ax.axhline(0, color="black", lw=0.7)
ax.set_xticks(range(3))
ax.set_xticklabels([m[0] for m in mechs], fontsize=7)
ax.set_ylabel("Input-token benefit (%)")
ax.set_ylim(-90, 30)
ax.legend(fontsize=6, loc="lower left", frameon=False)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout(pad=0.3)
fig.savefig(FIG / "f1_unified_benefit.pdf")
plt.close(fig)

# ---------- f2 paired distributions ----------
fig, axes = plt.subplots(1, 3, figsize=(7.0, 2.0), sharey=True)
for ax, (lbl, vals, _) in zip(axes, mechs):
    v = np.array(vals) * 100
    ax.boxplot(v, widths=0.4, showfliers=False, medianprops=dict(color="black"))
    jit = np.random.default_rng(7).normal(0, 0.05, size=len(v))
    ax.plot(np.ones_like(v) + jit, v, ".", ms=2.2, color="0.35")
    ax.axhline(0, color="black", lw=0.7)
    ax.set_xticks([1])
    ax.set_xticklabels([lbl], fontsize=6.5)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
axes[0].set_ylabel("Per-case input benefit (%)")
fig.tight_layout(pad=0.4)
fig.savefig(FIG / "f2_paired_deltas.pdf")
plt.close(fig)

# ---------- f3 turn amplification ----------
dc = [c["t_calls"] - c["b_calls"] for c in m3_an["cases"]]
df = [(c["t_flow"] - c["b_flow"]) / 1000.0 for c in m3_an["cases"]]
rec = [max(c["recoveries"], 0) for c in m3_an["cases"]]
fig, ax = plt.subplots(figsize=(3.4, 2.4))
sizes = [12 + 14 * r for r in rec]
ax.scatter(dc, df, s=sizes, facecolor="0.7", edgecolor="black", lw=0.5)
ax.axhline(0, color="black", lw=0.7)
ax.set_xlabel("$\\Delta$ tool calls per case (T$-$B)")
ax.set_ylabel("$\\Delta$ flow tokens (K, T$-$B)")
ax.text(0.02, 0.95, "bubble size = recoveries", transform=ax.transAxes, fontsize=6, va="top")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout(pad=0.3)
fig.savefig(FIG / "f3_turn_amplification.pdf")
plt.close(fig)

# ---------- f4 grid pareto (validated against frozen verdict) ----------
deliveries = jlines(R4 / "refinement-r2" / "b-deliveries.jsonl")
split = jload(R4 / "refinement-r2" / "split-70-30.json")
hold_cases = set(split["holdout"]) if isinstance(split.get("holdout"), list) else set(split.get("hold", []))
tot_hold_chars = sum(x["chars"] for d in deliveries if d.get("case_id") in hold_cases
                     for x in d["rows"])
xs, ys, ok = [], [], []
max_exp = 0.0
for k, v in grid["grid"].items():
    h = v["hold"]
    if h.get("chars") is None or not tot_hold_chars:
        continue
    exp = h["chars"] / tot_hold_chars * 100
    cov = h.get("coverage", 0.0) or 0.0
    xs.append(cov)
    ys.append(exp)
    max_exp = max(max_exp, exp)
    ok.append((k, exp, cov))
print(f"grid check: total_hold_chars={tot_hold_chars}, max_exposure={max_exp:.4f}% "
      f"(frozen verdict: 1.66%)")
if abs(max_exp - 1.66) < 0.15:
    fig, ax = plt.subplots(figsize=(3.4, 2.4))
    ax.scatter(xs, ys, s=14, facecolor="0.7", edgecolor="black", lw=0.4)
    ax.axhline(2.0, color="black", lw=0.7, ls="--")
    ax.axvline(1.0 / 3, color="black", lw=0.7, ls=":")
    ax.set_xlabel("Case coverage (holdout)")
    ax.set_ylabel("Safe exposure (% of context chars)")
    ax.text(0.35, max_exp * 0.92, "gates: $\\geq$2% exposure,\n$\\geq$1/3 coverage", fontsize=6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout(pad=0.3)
    fig.savefig(FIG / "f4_grid_pareto.pdf")
    print("f4 regenerated from grid-results.json (validated)")
else:
    import shutil
    shutil.copy(Path(r"D:\tasco-temp\research-semantic-compression\r5\paper-b\latex\fig4_grid_pareto.png"),
                FIG / "f4_grid_pareto.png")
    print("f4 validation FAILED -> reused frozen figure PNG")
plt.close("all")

# ---------- f5 recovery CDF ----------
dists = sorted(r["first_recovery_distance"] for r in vb
               if r.get("recovery_count", 0) > 0 and r.get("first_recovery_distance") is not None)
n = len(dists)
cdf = np.arange(1, n + 1) / n
fig, ax = plt.subplots(figsize=(3.4, 2.2))
ax.step(dists, cdf, where="post", color="black", lw=0.9)
med = dists[n // 2]
ax.axvline(med, color="0.4", lw=0.7, ls="--")
ax.text(med + 0.5, 0.15, f"median {med}", fontsize=6)
ax.set_xlabel("Tool events from fold to first recovery")
ax.set_ylabel("CDF (recovered views)")
ax.set_ylim(0, 1.02)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout(pad=0.3)
fig.savefig(FIG / "f5_recovery_cdf.pdf")
plt.close(fig)
print("f5 recovered views:", n)

# ---------- f6 family x mechanism ----------
common = ["file-review", "module-analysis", "mutation-testfix", "cross-spec"]
data = {"M1": {}, "M2": {}, "M3": {}}
for p in m1p:
    data["M1"].setdefault(p["family"], []).append(p["benefit"])
for p in m2p:
    data["M2"].setdefault(p["family"], []).append(p["benefit"])
for p in m3p:
    data["M3"].setdefault(p["family"], []).append(p["benefit"])
fig, ax = plt.subplots(figsize=(7.0, 2.3))
wid = 0.26
for i, mech in enumerate(["M1", "M2", "M3"]):
    xs_, ys_, lo_, hi_, explor = [], [], [], [], []
    for j, fam in enumerate(common):
        vals = data[mech].get(fam, [])
        if not vals:
            continue
        m = float(np.mean(vals))
        lo, hi = boot_ci(vals, seed=20261019 + i)
        xs_.append(j + (i - 1) * wid)
        ys_.append(m * 100)
        lo_.append(abs(lo - m) * 100)
        hi_.append(abs(hi - m) * 100)
        explor.append(len(vals) < 10)
    bars = ax.bar(xs_, ys_, width=wid, color=["0.8", "0.6", "0.4"][i],
                  edgecolor="black", lw=0.5,
                  hatch=["", "//", "xx"][i],
                  label={"M1": "M1 folding", "M2": "M2 gated", "M3": "M3 side-store"}[mech])
    for x, y, l, h, e in zip(xs_, ys_, lo_, hi_, explor):
        ax.errorbar(x, y, yerr=[[l], [h]], fmt="none", ecolor="black", elinewidth=0.6, capsize=2)
        if e:
            ax.text(x, -84, "n<10", ha="center", fontsize=5, rotation=90, color="0.35")
ax.axhline(0, color="black", lw=0.7)
ax.set_xticks(range(len(common)))
ax.set_xticklabels(common, fontsize=7)
ax.set_ylabel("Input-token benefit (%)")
ax.set_ylim(-92, 40)
ax.legend(fontsize=6.5, frameon=False, loc="lower right")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout(pad=0.3)
fig.savefig(FIG / "f6_family_benefits.pdf")
plt.close(fig)
print("figures done:", sorted(p.name for p in FIG.glob('*.pdf')))
