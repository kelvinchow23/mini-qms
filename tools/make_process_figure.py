"""Draw the minimalQMS process (docs/img/minimalqms-process.svg and .png).

Usage: python tools/make_process_figure.py
Requires: matplotlib
"""
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon

INK = "#1f2937"
MUTED = "#6b7280"
STAGE = "#e8eef9"
STAGE_EDGE = "#2563eb"
RED = "#dc2626"
BACK = "#d97706"

STAGES = ["Scope", "Requirements", "Design", "Build &\nverify", "Release &\nclose-out"]
GATES = [("G0", "approved"), ("G1", "reviewed"), ("G2", "design\nfreeze"), ("G3", "verified"),
         ("G4", "released")]

W, GAP, H = 2.7, 1.05, 1.15     # stage width, gap holding the gate, stage height
Y = 0.0


def main(out):
    fig, ax = plt.subplots(figsize=(14, 5.0), dpi=100)
    ax.set_xlim(-0.4, len(STAGES) * (W + GAP) + 0.1)
    ax.set_ylim(-2.6, 2.3)
    ax.axis("off")

    xs = []
    for i, name in enumerate(STAGES):
        x0 = i * (W + GAP)
        xs.append(x0)
        ax.add_patch(FancyBboxPatch((x0, Y - H / 2), W, H, boxstyle="round,pad=0,rounding_size=0.18",
                                    fc=STAGE, ec=STAGE_EDGE, lw=2))
        ax.text(x0 + W / 2, Y, name, ha="center", va="center", fontsize=16, color=INK,
                fontweight="bold", linespacing=1.05)
        # gate diamond in the gap after the stage
        gx = x0 + W + GAP / 2
        d = 0.27
        ax.add_patch(Polygon([(gx, Y - d * 1.5), (gx + d, Y), (gx, Y + d * 1.5), (gx - d, Y)],
                             closed=True, fc=RED, ec="white", lw=1.5, zorder=3))
        g, label = GATES[i]
        ax.text(gx, Y + 0.62, g, ha="center", va="bottom", fontsize=15, color=RED, fontweight="bold")
        ax.text(gx, Y - 0.6, label, ha="center", va="top", fontsize=11.5, color=RED, linespacing=1.0)
        # forward arrow from stage into gate
        ax.add_patch(FancyArrowPatch((x0 + W + 0.02, Y), (gx - d - 0.02, Y), arrowstyle="-|>",
                                     mutation_scale=14, lw=2, color=STAGE_EDGE))
        if i < len(STAGES) - 1:
            ax.add_patch(FancyArrowPatch((gx + d + 0.02, Y), (x0 + W + GAP + 0.0, Y), arrowstyle="-|>",
                                         mutation_scale=14, lw=2, color=STAGE_EDGE))

    # back arrow: fails verification -> design (within the iteration)
    design_x = xs[2] + W / 2
    build_x = xs[3] + W / 2
    ax.add_patch(FancyArrowPatch((build_x, Y + H / 2 + 0.05), (design_x, Y + H / 2 + 0.05),
                                 connectionstyle="arc3,rad=0.45", arrowstyle="-|>", mutation_scale=16,
                                 lw=2.4, color=BACK))
    ax.text((design_x + build_x) / 2, Y + 1.55, "fails verification: change the design",
            ha="center", va="center", fontsize=12.5, color=BACK, fontweight="bold")

    # next iteration: from the end back to scope
    end_x = xs[-1] + W + GAP / 2
    start_x = xs[0] + W / 2
    yb = Y - 1.75
    ax.plot([end_x, end_x], [Y - 1.05, yb], color=RED, lw=2.6)
    ax.plot([end_x, start_x], [yb, yb], color=RED, lw=2.6)
    ax.add_patch(FancyArrowPatch((start_x, yb), (start_x, Y - H / 2 - 0.05), arrowstyle="-|>",
                                 mutation_scale=18, lw=2.6, color=RED))
    ax.text((start_x + end_x) / 2, yb - 0.32, "next iteration: lessons learned become change requests",
            ha="center", va="center", fontsize=12.5, color=RED, fontweight="bold")

    ax.text(-0.35, 2.15, "minimalQMS process", ha="left", va="center", fontsize=20,
            fontweight="bold", color=INK)

    fig.tight_layout(pad=0.2)
    fig.savefig(out + ".svg")
    fig.savefig(out + ".png", dpi=200)
    print("wrote", out + ".png")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "docs/img/minimalqms-process")
