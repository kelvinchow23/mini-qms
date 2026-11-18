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
NODE = 0.52    # gate circle radius


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
    fig, ax = plt.subplots(figsize=(10.5, 9.2), dpi=100)
    ax.set_aspect("equal")
    ax.set_xlim(-6.3, 6.3)
    ax.set_ylim(-4.4, 5.6)
    ax.axis("off")

    # main iteration arcs between consecutive gates
    phase_labels = {("G3", "G4"): "build"}
    for i in range(len(GATES) - 1):
        g0, g1 = GATES[i], GATES[i + 1]
        arc(ax, g0[3], g1[3], BLUE, 2.2, text=phase_labels.get((g0[0], g1[0])),
            text_r=R - 0.45, fontsize=8.5)

    # closing arc G5 -> G0: the loop back to the next iteration
    arc(ax, GATES[-1][3], GATES[0][3] - 360, RED, 3.2)
    lx, ly = pos(120, R + 0.95)
    ax.text(lx - 0.35, ly + 0.25, "next iteration", ha="center", va="center", fontsize=11,
            color=RED, fontweight="bold")
    ax.text(lx - 0.35, ly - 0.25, "lessons learned · NCs · field feedback\n→ ECRs for iteration n+1",
            ha="center", va="center", fontsize=8.5, color=RED)

    # gate nodes and labels
    for g, name, desc, ang in GATES:
        x, y = pos(ang)
        ax.add_patch(Circle((x, y), NODE, fc="white", ec=RED, lw=2.2, zorder=5))
        ax.text(x, y + 0.08, g, ha="center", va="center", fontsize=13, fontweight="bold",
                color=RED, zorder=6)
        ax.text(x, y - 0.24, name, ha="center", va="center", fontsize=7, color=INK, zorder=6)
        c = math.cos(math.radians(ang))
        if abs(c) < 0.3:   # top and bottom gates: text above / below the node
            above = y > 0
            ax.text(x, y + (NODE + 0.15) * (1 if above else -1), desc, ha="center",
                    va="bottom" if above else "top", fontsize=8.5, color=MUTED, linespacing=1.15)
        else:
            ox, oy = pos(ang, R + 0.85)
            ax.text(ox, oy, desc, ha="left" if c > 0 else "right", va="center", fontsize=8.5,
                    color=MUTED, linespacing=1.15)

    # inner change loop
    ax.add_patch(Circle((0, 0), 1.45, fc=LIGHT, ec="none", zorder=1))
    small = 1.05
    for a0, a1 in [(80, -40), (-40, -160), (-160, -280)]:
        p0 = (small * math.cos(math.radians(a0 - 8)), small * math.sin(math.radians(a0 - 8)))
        p1 = (small * math.cos(math.radians(a1 + 8)), small * math.sin(math.radians(a1 + 8)))
        ax.add_patch(FancyArrowPatch(p0, p1, connectionstyle="arc3,rad=-0.55", arrowstyle="-|>",
                                     mutation_scale=11, lw=1.4, color=GREEN, zorder=3))
    ax.text(0, 0.28, "between iterations", ha="center", va="center", fontsize=8.5, color=GREEN,
            fontweight="bold", zorder=4)
    ax.text(0, -0.12, "ECR → review →\nnew revision", ha="center", va="center", fontsize=8.5,
            color=INK, zorder=4, linespacing=1.15)
    ax.text(0, -0.58, "(SOP-001, no gates)", ha="center", va="center", fontsize=7.5, color=MUTED,
            zorder=4)

    ax.text(-6.2, 5.35, "minimalQMS: development is a cycle", ha="left", va="center", fontsize=14,
            fontweight="bold", color=INK)
    ax.text(-6.2, 4.85, "Each iteration passes the gates again, starting from the last released revision.\n"
                        "Gates that a change does not affect are skipped, with the reason in plan.yaml.",
            ha="left", va="center", fontsize=9, color=MUTED, linespacing=1.3)
    ax.text(6.2, -4.25, "Red: gate (human approval)   Blue: iteration   Green: small change between iterations",
            ha="right", va="center", fontsize=8, color=MUTED)

    fig.tight_layout(pad=0.3)
    fig.savefig("docs/img/development-cycle.svg")
    fig.savefig("docs/img/development-cycle.png", dpi=200)
    print("wrote docs/img/development-cycle.svg and .png")


if __name__ == "__main__":
    main()
