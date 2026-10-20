# PROVENANCE: exported from the internal TASCO research repository. This script references internal absolute paths and is a provenance record; the runnable reproduction interface is reproduction/verify.py. Source file: f0_lanes.py
"""Figure 1 (final v2): D-lanes hybrid — geometry budgeted for uniform 9pt.

Column budget (x fractions; 1 char ~ 12.5px at 9pt/200dpi on a 1080px axes):
  chip 0.24 (20 ch) | arrow | exposure 0.205 (17 ch) | arrow | badge 0.18 (14 ch) |
  arrow | failure 0.25 (20 ch). Banner 0.99 (83 ch). Fit is ASSERTED per text.
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
plt.rcParams.update({"pdf.fonttype": 42, "figure.dpi": 200})
OUT = Path(r"D:\tasco-temp\research-semantic-compression\r5\paper-b\emse-submission-pack-r1\figures")
OUT.mkdir(parents=True, exist_ok=True)
INK = "#1B2631"
RED = "#C1272D"
FILL = {"blue": "#D6EAF8", "orange": "#FDF2E9", "green": "#D5F5E3",
        "gray": "#EBEDEF", "red": "#FADBD8"}
BODY = 9.0
VIOL = []

fig, ax = plt.subplots(figsize=(7.0, 2.5))
ax.axis("off")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

def rbox(x, y, w, h, fc, lw=0.9):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.012",
                                facecolor=fc, edgecolor=INK, lw=lw))

def arrow(x0, x1, y):
    ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle="-|>", mutation_scale=11,
                                 lw=1.1, color="#34495E", shrinkA=0, shrinkB=0))

rbox(0.005, 0.79, 0.99, 0.19, FILL["gray"])
tb = ax.text(0.5, 0.885,
             "Stack: opencode + GLM-5.3-Flash  |  168 tasks  |  paired B/T arms  |  frozen oracles",
             fontsize=BODY, ha="center", va="center", color=INK)

lanes = [
    (0.615, "M1 folding", "100 pairs", "542 folds online", "+7.1%", "F1 compensation", FILL["blue"]),
    (0.375, "M2 gated", "30 pairs", "2 folds online", "2 folds / 30", "F2 exposure\ncollapse", FILL["orange"]),
    (0.135, "M3 side-store", "30 cases x 2", "280 views online", "-23.0%", "F3 re-injection", FILL["green"]),
]
fit_items = [(tb, 0.99)]
for y, name, dose, expo, badge, fail, fc in lanes:
    cy = y + 0.115
    rbox(0.015, cy - 0.10, 0.24, 0.20, fc)
    t1 = ax.text(0.135, cy + 0.048, name, fontsize=BODY, fontweight="bold", ha="center", va="center", color=INK)
    t2 = ax.text(0.135, cy - 0.052, dose, fontsize=BODY - 0.5, ha="center", va="center", color=INK)
    arrow(0.26, 0.29, cy)
    t3 = ax.text(0.3975, cy, expo, fontsize=BODY, ha="center", va="center", color=INK)
    arrow(0.50, 0.53, cy)
    rbox(0.545, cy - 0.10, 0.18, 0.20, FILL["red"], lw=1.2)
    t4 = ax.text(0.635, cy + 0.048, badge, fontsize=BODY, fontweight="bold", ha="center", va="center", color=RED)
    arrow(0.73, 0.76, cy)
    t5 = ax.text(0.76, cy, fail, fontsize=BODY, ha="left", va="center", color=INK)
    fit_items += [(t1, 0.24), (t2, 0.24), (t3, 0.205), (t4, 0.18), (t5, 0.24)]

fig.canvas.draw()
r = fig.canvas.get_renderer()
axbb = ax.get_window_extent(renderer=r)
for t, wf in fit_items:
    bb = t.get_window_extent(renderer=r)
    if bb.width > wf * axbb.width * 0.97:
        VIOL.append("'{}': {:.0f}px > {:.0f}px".format(t.get_text()[:30].replace("\n", "/"),
                                                       bb.width, wf * axbb.width * 0.97))

if VIOL:
    for v in VIOL:
        print("OVERFLOW:", v)
    sys.exit(1)
fig.savefig(OUT / "f0_lanes.pdf")
plt.close(fig)
print("Figure 1 (D-lanes v2): uniform 9pt, 1 headline badge per lane, zero overflow")
