# PROVENANCE: exported from the internal TASCO research repository. This script references internal absolute paths and is a provenance record; the runnable reproduction interface is reproduction/verify.py. Source file: emse_figures.py
"""EMSE submission figures — color, larger fonts, sized for target layout.

Colorblind-safe (Okabe-Ito derived) palette; also distinguishable in grayscale.
All data from frozen artifacts (same sources as full-paper-r1/scripts/fp_figures.py).
Targets: f0/f2/f6 = double-column span (7.0in); f1/f3/f4/f5 = column (3.35in).
"""
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
plt.rcParams.update({
    "font.size": 9.5, "axes.titlesize": 10, "axes.labelsize": 10,
    "xtick.labelsize": 9.5, "ytick.labelsize": 9.5, "legend.fontsize": 9,
    "axes.linewidth": 0.7, "pdf.fonttype": 42, "ps.fonttype": 42,
    "figure.dpi": 150, "savefig.bbox": "tight",
})
C = {"M1": "#0072B2", "M2": "#E69F00", "M3": "#009E73"}   # Okabe-Ito
NEG, POS = "#C1272D", "#1B7837"
FIG = Path(r"D:\tasco-temp\research-semantic-compression\r5\paper-b\emse-submission-pack-r1\figures")
FIG.mkdir(parents=True, exist_ok=True)
R4 = Path(r"D:\tasco-temp\research-semantic-compression\r4")
R5 = Path(r"D:\tasco-temp\research-semantic-compression\r5")

def jload(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))

def jlines(p):
    return [json.loads(l) for l in Path(p).read_text(encoding="utf-8").splitlines() if l.strip()]

m1_rows = jlines(R4 / "100case" / "paired-execution-results.jsonl")
m2_rows = jlines(R4 / "refinement" / "refinement-paired-results.jsonl")
m3_an = jload(R5 / "expansion" / "expansion-analysis.json")
grid = jload(R4 / "refinement-r2" / "grid-results.json")
deliveries = jlines(R4 / "refinement-r2" / "b-deliveries.jsonl")
split = jload(R4 / "refinement-r2" / "split-70-30.json")
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

def boot_ci(vals, n=10000, seed=20261019):
    a = np.asarray(vals, float)
    r = np.random.default_rng(seed)
    idx = r.integers(0, len(a), size=(n, len(a)))
    m = a[idx].mean(axis=1)
    return np.percentile(m, 2.5), np.percentile(m, 97.5)

# ---------- f0 design overview (double-column, color; text auto-fit by measurement) ----------
fig, ax = plt.subplots(figsize=(7.0, 2.5))
ax.axis("off")
boxes = [
    (0.005, 0.50, 0.175, 0.42, "168 disjoint tasks\n2 JS repositories\nopencode +\nGLM-5.3-Flash", "#EAF2F8"),
    (0.205, 0.74, 0.195, 0.20, "M1 RDS folding\n100 pairs (high dose)", "#D6EAF8"),
    (0.205, 0.45, 0.195, 0.20, "M2 gated folding\n30 pairs (safe dose)", "#FDF2E9"),
    (0.205, 0.16, 0.195, 0.20, "M3 side-store\n30 cases × 2 reps", "#E8F8F5"),
    (0.435, 0.40, 0.19, 0.54, "Paired B/T arms\nseed-balanced\nAB/BA order\nfrozen oracles", "#FEF9E7"),
    (0.655, 0.58, 0.16, 0.36, "Calibers\ninput/cache/flow\ntokens · chars proxy\ntool calls · wall", "#F4ECF7"),
    (0.655, 0.10, 0.16, 0.36, "Offline tools\n64-config grid\nrecovery screen\nreplay audit", "#F4ECF7"),
    (0.845, 0.26, 0.15, 0.68, "Findings\nF1 compensation\nF2 exposure\ncollapse\nF3 re-injection\nsafe < noise", "#FADBD8"),
]
texts = []
for x, y, w, h, t, fc in boxes:
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=fc, edgecolor="black", lw=0.9))
    texts.append((ax.text(x + w / 2, y + h / 2, t, ha="center", va="center", fontsize=8.6),
                  x, w, h))
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
ax_bb = ax.get_window_extent(renderer=renderer)
for t, x, w, h in texts:
    # auto-shrink font until the text block fits inside its box (92% padding)
    for _ in range(24):
        bb = t.get_window_extent(renderer=renderer)
        bw = w * ax_bb.width * 0.92
        bh = h * ax_bb.height * 0.92
        fs = t.get_fontsize()
        if bb.width <= bw and bb.height <= bh:
            break
        t.set_fontsize(max(fs - 0.2, 5.5))
        fig.canvas.draw()
for x0, y0, x1, y1 in [(0.18, 0.71, 0.205, 0.84), (0.18, 0.58, 0.205, 0.55),
                       (0.18, 0.50, 0.205, 0.26), (0.40, 0.84, 0.435, 0.70),
                       (0.40, 0.55, 0.435, 0.67), (0.40, 0.26, 0.435, 0.50),
                       (0.625, 0.67, 0.655, 0.76), (0.625, 0.55, 0.655, 0.36),
                       (0.625, 0.26, 0.655, 0.24), (0.815, 0.76, 0.845, 0.68),
                       (0.815, 0.28, 0.845, 0.46)]:
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="->", lw=1.0, color="#34495E"))
fig.savefig(FIG / "f0_design_overview.pdf")
plt.close(fig)

# ---------- f1 unified benefit (column, color) ----------
mechs = [
    ("M1 folding\n(100 pairs)", [p["benefit"] for p in m1p], 0.071, C["M1"]),
    ("M2 gated\n(30 pairs)", [p["benefit"] for p in m2p], -0.029, C["M2"]),
    ("M3 side-store\n(30 cases × 2)", [p["benefit"] for p in m3p], 0.124, C["M3"]),
]
fig, ax = plt.subplots(figsize=(3.35, 2.7))
for i, (lbl, vals, tot, col) in enumerate(mechs):
    m = float(np.mean(vals))
    lo, hi = boot_ci(vals, seed=20261019 + i)
    ax.bar(i, m * 100, width=0.6, color=col, edgecolor="black", lw=0.6, alpha=0.85,
           label="case-equal-weight mean", zorder=2)
    ax.errorbar(i, m * 100, yerr=[[abs(lo - m) * 100], [abs(hi - m) * 100]], fmt="none",
                ecolor="black", elinewidth=1.0, capsize=3.5, zorder=3)
    ax.plot(i, -tot * 100, marker="D", color=NEG, markersize=6, markeredgecolor="black",
            markeredgewidth=0.6, zorder=4, label="totals-based Δ (favors < 0)" if i == 0 else None)
ax.axhline(0, color="black", lw=0.9, zorder=1)
ax.set_xticks(range(3))
ax.set_xticklabels([m[0] for m in mechs])
ax.set_ylabel("Input-token benefit (%)")
ax.set_ylim(-92, 32)
ax.legend(fontsize=8.2, loc="lower left", frameon=True, framealpha=0.9)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout(pad=0.3)
fig.savefig(FIG / "f1_unified_benefit.pdf")
plt.close(fig)

# ---------- f2 paired distributions (double-column, color) ----------
fig, axes = plt.subplots(1, 3, figsize=(5.2, 2.05), sharey=True)
for ax, (lbl, vals, _, col) in zip(axes, mechs):
    v = np.array(vals) * 100
    bp = ax.boxplot(v, widths=0.42, showfliers=False, patch_artist=True,
                    medianprops=dict(color="black", lw=1.2),
                    boxprops=dict(facecolor=col, alpha=0.45, edgecolor="black", lw=0.7),
                    whiskerprops=dict(color="black", lw=0.7),
                    capprops=dict(color="black", lw=0.7))
    jit = np.random.default_rng(7).normal(0, 0.045, size=len(v))
    ax.plot(np.ones_like(v) + jit, v, ".", ms=3.0, color="#34495E", alpha=0.75)
    ax.axhline(0, color=NEG, lw=0.9, ls="--")
    ax.set_xticks([1])
    ax.set_xticklabels([lbl])
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
axes[0].set_ylabel("Per-case input benefit (%)")
fig.tight_layout(pad=0.4)
fig.savefig(FIG / "f2_paired_deltas.pdf")
plt.close(fig)

# ---------- f3 turn amplification (column, color) ----------
dc = [c["t_calls"] - c["b_calls"] for c in m3_an["cases"]]
df = [(c["t_flow"] - c["b_flow"]) / 1000.0 for c in m3_an["cases"]]
rec = [max(c["recoveries"], 0) for c in m3_an["cases"]]
fig, ax = plt.subplots(figsize=(3.35, 2.8))
sc = ax.scatter(dc, df, s=[16 + 15 * r for r in rec], c=rec, cmap="YlGnBu",
                edgecolor="black", lw=0.5, vmin=0, vmax=8)
cb = fig.colorbar(sc, ax=ax, pad=0.02)
cb.set_label("recoveries", fontsize=8.5)
cb.ax.tick_params(labelsize=8)
ax.axhline(0, color=NEG, lw=0.9, ls="--")
ax.set_xlabel("Δ tool calls per case (T−B)")
ax.set_ylabel("Δ flow tokens (K, T−B)")
ax.text(0.03, 0.95, "bubble size = recoveries", transform=ax.transAxes, fontsize=8, va="top")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout(pad=0.3)
fig.savefig(FIG / "f3_turn_amplification.pdf")
plt.close(fig)

# ---------- f4 grid pareto (column, color; validated vs frozen 1.66%) ----------
hold_cases = set(split["holdout"]) if isinstance(split.get("holdout"), list) else set(split.get("hold", []))
tot_hold_chars = sum(x["chars"] for d in deliveries if d.get("case_id") in hold_cases for x in d["rows"])
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
print(f"f4 validation: max_exposure={max_exp:.4f}% (frozen 1.66%)")
assert abs(max_exp - 1.66) < 0.15, "grid figure must match frozen verdict"
fig, ax = plt.subplots(figsize=(3.35, 2.7))
ax.scatter(xs, ys, s=22, c="#0072B2", edgecolor="black", lw=0.4, alpha=0.8, zorder=3)
ax.axhspan(2.0, 12, color=POS, alpha=0.07, zorder=1)
ax.axvspan(1.0 / 3, 1.05, ymin=0, ymax=1, color=POS, alpha=0.05, zorder=1)
ax.axhline(2.0, color=NEG, lw=1.1, ls="--", zorder=2)
ax.axvline(1.0 / 3, color=NEG, lw=1.1, ls=":", zorder=2)
ax.set_xlabel("Case coverage (holdout)")
ax.set_ylabel("Safe exposure (% of context chars)")
ax.set_xlim(-0.03, 1.05)
ax.set_ylim(-0.3, 3.6)
ax.text(0.36, 3.25, "acceptance gates:\n≥2% exposure, ≥1/3 coverage", fontsize=7.6, color=NEG)
ax.text(0.62, 0.9, "0 / 64 pass", fontsize=10, fontweight="bold", color="#34495E")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout(pad=0.3)
fig.savefig(FIG / "f4_grid_pareto.pdf")
plt.close(fig)

# ---------- f5 recovery CDF (column, color) ----------
dists = sorted(r["first_recovery_distance"] for r in vb
               if r.get("recovery_count", 0) > 0 and r.get("first_recovery_distance") is not None)
n = len(dists)
cdf = np.arange(1, n + 1) / n
fig, ax = plt.subplots(figsize=(3.35, 2.5))
ax.step(dists, cdf, where="post", color="#0072B2", lw=1.4)
ax.fill_between(dists, 0, cdf, step="post", color="#0072B2", alpha=0.12)
med = dists[n // 2]
ax.axvline(med, color="#E69F00", lw=1.3, ls="--")
ax.annotate(f"median {med}", xy=(med, 0.52), xytext=(med + 1.2, 0.38), fontsize=8.5,
            arrowprops=dict(arrowstyle="->", lw=0.8, color="#E69F00"), color="#B9770E")
ax.set_xlabel("Tool events from fold to first recovery")
ax.set_ylabel("CDF (recovered views)")
ax.set_ylim(0, 1.02)
ax.set_xlim(left=0)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout(pad=0.3)
fig.savefig(FIG / "f5_recovery_cdf.pdf")
plt.close(fig)
print("f5 recovered views:", n)

# ---------- f6 family x mechanism (double-column, color) ----------
common = ["file-review", "module-analysis", "mutation-testfix", "cross-spec"]
data = {"M1": {}, "M2": {}, "M3": {}}
for p in m1p:
    data["M1"].setdefault(p["family"], []).append(p["benefit"])
for p in m2p:
    data["M2"].setdefault(p["family"], []).append(p["benefit"])
for p in m3p:
    data["M3"].setdefault(p["family"], []).append(p["benefit"])
fig, ax = plt.subplots(figsize=(5.5, 2.45))
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
    ax.bar(xs_, ys_, width=wid, color=C[mech], edgecolor="black", lw=0.6, alpha=0.85,
           label={"M1": "M1 folding", "M2": "M2 gated", "M3": "M3 side-store"}[mech], zorder=2)
    for x, y, l, h, e in zip(xs_, ys_, lo_, hi_, explor):
        ax.errorbar(x, y, yerr=[[l], [h]], fmt="none", ecolor="black", elinewidth=0.8,
                    capsize=2.5, zorder=3)
        if e:
            ax.text(x, -86, "explor.", ha="center", fontsize=7.2, rotation=90, color="#7B241C")
ax.axhline(0, color="black", lw=0.9, zorder=1)
ax.set_xticks(range(len(common)))
ax.set_xticklabels(common)
ax.set_ylabel("Input-token benefit (%)")
ax.set_ylim(-92, 42)
ax.legend(fontsize=9, frameon=True, framealpha=0.9, loc="lower right", ncols=3)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout(pad=0.3)
fig.savefig(FIG / "f6_family_benefits.pdf")
plt.close(fig)
print("figures done:", sorted(p.name for p in FIG.glob("*.pdf")))
