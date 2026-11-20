"""Draw the minimalQMS development cycle (docs/img/development-cycle.svg and .png).

Usage: python tools/make_cycle_figure.py
Requires: matplotlib
"""
import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

INK = "#1f2937"
MUTED = "#6b7280"
BLUE = "#2563eb"
LIGHT = "#dbeafe"
RED = "#dc2626"
GREEN = "#059669"

# Gates around the circle, clockwise from the top. Angles in degrees.
GATES = [
    ("G0", "Scope", "plan.yaml: goal, scope,\nECRs for this iteration", 90),
    ("G1", "Requirements", "requirements, risks\n(only what changes)", 30),
    ("G2", "Design", "formal review of\nchanges since last release", -30),
    ("G3", "Release", "new revisions released;\nparts ordered (SOP-005)", -90),
    ("G4", "Verified", "units built, inspected,\ntested, released", -150),
    ("G5", "Close-out", "lessons learned,\nincl. where AI was wrong", -210),
]
R = 3.0        # gate ring radius
NODE = 0.78    # gate circle radius


def pos(angle, r=R):
    a = math.radians(angle)
    return r * math.cos(a), r * math.sin(a)


def arc(ax, a0, a1, color, lw, r=R, text=None, text_r=None, fontsize=8.5, weight="normal"):
    # trim the arc so it starts/ends at the node edges
    trim = math.degrees(NODE / r) + 3
    a0t, a1t = a0 - trim, a1 + trim  # clockwise: angles decrease
    p0, p1 = pos(a0t, r), pos(a1t, r)
    span = math.radians(a0t - a1t)
    rad = -math.tan(span / 4) * 1.0  # arc3 curvature that follows the circle (clockwise)
    ax.add_patch(FancyArrowPatch(p0, p1, connectionstyle=f"arc3,rad={rad}", arrowstyle="-|>",
                                 mutation_scale=16, lw=lw, color=color, zorder=2))
    if text:
        mid = (a0 + a1) / 2
        x, y = pos(mid, text_r or r)
        ax.text(x, y, text, ha="center", va="center", fontsize=fontsize, color=color,
                fontweight=weight, zorder=4)


def main():
    fig, ax = plt.subplots(figsize=(8, 8), dpi=100)
    ax.set_aspect("equal")
    ax.set_xlim(-4.35, 4.35)
    ax.set_ylim(-4.25, 4.45)
    ax.axis("off")

    # iteration arcs between consecutive gates
    for i in range(len(GATES) - 1):
        g0, g1 = GATES[i], GATES[i + 1]
        label = "build" if (g0[0], g1[0]) == ("G3", "G4") else None
        arc(ax, g0[3], g1[3], BLUE, 2.4, text=label, text_r=R - 0.55, fontsize=12)

    # closing arc G5 -> G0: the next iteration
    arc(ax, GATES[-1][3], GATES[0][3] - 360, RED, 3.4)
    lx, ly = pos(122, R + 0.75)
    ax.text(lx, ly, "next\niteration", ha="center", va="center", fontsize=13, color=RED,
            fontweight="bold", linespacing=1.05)

    # gates
    for g, name, _desc, ang in GATES:
        x, y = pos(ang)
        ax.add_patch(Circle((x, y), NODE, fc="white", ec=RED, lw=2.4, zorder=5))
        ax.text(x, y + 0.24, g, ha="center", va="center", fontsize=11, color=RED,
                fontweight="bold", zorder=6)
        ax.text(x, y - 0.14, name, ha="center", va="center", fontsize=12.5 if len(name) < 10 else 10.5,
                color=INK, fontweight="bold", zorder=6)

    # small fixes between iterations
    ax.add_patch(Circle((0, 0), 1.3, fc=LIGHT, ec="none", zorder=1))
    small = 0.95
    for a0, a1 in [(80, -40), (-40, -160), (-160, -280)]:
        p0 = (small * math.cos(math.radians(a0 - 8)), small * math.sin(math.radians(a0 - 8)))
        p1 = (small * math.cos(math.radians(a1 + 8)), small * math.sin(math.radians(a1 + 8)))
        ax.add_patch(FancyArrowPatch(p0, p1, connectionstyle="arc3,rad=-0.55", arrowstyle="-|>",
                                     mutation_scale=11, lw=1.5, color=GREEN, zorder=3))
    ax.text(0, 0, "small fixes\nbetween\niterations", ha="center", va="center", fontsize=11,
            color=GREEN, fontweight="bold", zorder=4, linespacing=1.1)

    fig.tight_layout(pad=0.2)
    fig.savefig("docs/img/development-cycle.svg")
    fig.savefig("docs/img/development-cycle.png", dpi=200)
    print("wrote docs/img/development-cycle.svg and .png")


if __name__ == "__main__":
    main()
