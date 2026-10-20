# PROVENANCE: exported from the internal TASCO research repository. This script references internal absolute paths and is a provenance record; the runnable reproduction interface is reproduction/verify.py. Source file: fig1_integrate.py
﻿"""Figure 1 final integration build - V2 style + metric semantics + bottom closure strip.

Layout (y budget of the 2.1in canvas):
  banner   y 0.775-0.975  (two lines: stack / scope)
  lanes    chips h 0.19 at cy 0.66 / 0.445 / 0.23
  closure  y 0.02-0.115   (one-line takeaway, mirrors the banner, closes the frame)
Badges (2-line, 10pt bold number / 8.5pt metric label):
  M1  +7.1%          input tokens        (consumption increase)
  M2  2 folds / 30   triggered exposure  (count, not a token rate)
  M3  -23.0%         mean input benefit  (negative benefit = loss)
All strings ASCII by design. Fit ASSERTED per text (no auto-shrink).
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
plt.rcParams.update({"pdf.fonttype": 42, "figure.dpi": 200})
ROOT = Path(r"D:\tasco-temp\research-semantic-compression\r5\paper-b\emse-submission-pack-r1")
OUT = ROOT / "figures"
OUT.mkdir(parents=True, exist_ok=True)
INK, SUB = "#1B2631", "#424949"
HEAD, AUX = 10.0, 8.5
VIOL = []

fig, ax = plt.subplots(figsize=(7.0, 2.1))
ax.axis("off")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

def rbox(x, y, w, h, fc, ec, lw):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.012",
                                facecolor=fc, edgecolor=ec, lw=lw))

def arrow(x0, x1, y):
    ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle="-|>", mutation_scale=12,
                                 lw=1.2, color="#566573", shrinkA=0, shrinkB=0))

# banner (setting layer)
rbox(0.015, 0.775, 0.97, 0.20, "#E8EDF2", "#7F8C8D", 1.0)
tb1 = ax.text(0.5, 0.905, "opencode + GLM-5.3-Flash", fontsize=HEAD, fontweight="bold",
              ha="center", va="center", color=INK)
tb2 = ax.text(0.5, 0.815, "168 tasks overall   |   M1-M3 paired B/T comparisons   |   frozen oracles",
              fontsize=AUX, ha="center", va="center", color=INK)

lanes = [
    ("M1 folding", "100 pairs", "+7.1%", "input tokens", "#2874A6", "#D6EAF8"),
    ("M2 gated", "30 pairs", "2 folds / 30", "triggered exposure", "#B9770E", "#FDF2E9"),
    ("M3 side-store", "30 cases x 2", "-23.0%", "mean input benefit", "#1E8449", "#D5F5E3"),
]
cy_list = [0.66, 0.445, 0.23]
items = []
for (name, dose, num, label, dark, tint), cy in zip(lanes, cy_list):
    # mechanism chip
    rbox(0.015, cy - 0.095, 0.21, 0.19, tint, dark, 1.0)
    t1 = ax.text(0.12, cy + 0.045, name, fontsize=HEAD, fontweight="bold",
                 ha="center", va="center", color=INK)
    t2 = ax.text(0.12, cy - 0.048, dose, fontsize=AUX, ha="center", va="center", color=SUB)
    arrow(0.235, 0.265, cy)
    # exposure (neutral)
    t3 = ax.text(0.345, cy, {"M1 folding": "542 folds", "M2 gated": "2 folds",
                             "M3 side-store": "280 views"}[name],
                 fontsize=AUX, ha="center", va="center", color=SUB)
    arrow(0.425, 0.455, cy)
    # result badge (most prominent; 2-line semantic)
    rbox(0.46, cy - 0.095, 0.22, 0.19, "#F5B7B1", "#922B21", 1.3)
    t4 = ax.text(0.57, cy + 0.045, num, fontsize=HEAD, fontweight="bold",
                 ha="center", va="center", color="#7B241C")
    t5 = ax.text(0.57, cy - 0.048, label, fontsize=AUX, ha="center", va="center", color="#7B241C")
    arrow(0.685, 0.72, cy)
    # failure chip (restrained)
    rbox(0.725, cy - 0.095, 0.265, 0.19, "#D6E2F0", "#5D6D7E", 1.0)
    t6 = ax.text(0.8575, cy, {"M1 folding": "F1 compensation",
                              "M2 gated": "F2 exposure collapse",
                              "M3 side-store": "F3 re-injection"}[name],
                 fontsize=AUX, ha="center", va="center", color=INK)
    items += [(t1, 0.21), (t2, 0.21), (t3, 0.17), (t4, 0.22), (t5, 0.22), (t6, 0.265)]

# closure strip (bottom frame + one-line takeaway, mirrors the banner)
rbox(0.015, 0.02, 0.97, 0.095, "#E8EDF2", "#7F8C8D", 1.0)
tc = ax.text(0.5, 0.0675,
             "Outcome: no mechanism established net input-token savings (Table 2)",
             fontsize=AUX, ha="center", va="center", color=INK)
items += [(tb1, 0.97), (tb2, 0.97), (tc, 0.97)]

fig.canvas.draw()
r = fig.canvas.get_renderer()
axbb = ax.get_window_extent(renderer=r)
for t, wf in items:
    bb = t.get_window_extent(renderer=r)
    if bb.width > wf * axbb.width * 0.97:
        VIOL.append("'{}': {:.0f}px > {:.0f}px".format(t.get_text()[:34], bb.width, wf * axbb.width * 0.97))

if VIOL:
    for v in VIOL:
        print("OVERFLOW:", v)
    sys.exit(1)
fig.savefig(OUT / "fig1-final.pdf")
plt.close(fig)
print("fig1-final.pdf regenerated with bottom closure strip; zero overflow at target sizes")
