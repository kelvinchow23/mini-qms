"""Draw the minimalQMS gate timeline (docs/img/gate-timeline.svg and .png).

Usage: python tools/make_gate_figure.py
Requires: matplotlib
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon

# Phase boundaries on an arbitrary time axis (not to scale)
X = {"start": 0, "G0": 1, "G1": 3, "G2": 7, "buy": 8.6, "G3": 11, "G4": 12.8}
PHASES = [
    ("Scope", "start", "G0"),
    ("Requirements", "G0", "G1"),
    ("Design", "G1", "G2"),
    ("Build & verify", "G2", "G3"),
    ("Release", "G3", "G4"),
]
GATES = [("G0", "Scope\napproved"), ("G1", "Requirements\nreviewed"), ("G2", "Design\nfreeze"),
         ("G3", "Verified"), ("G4", "Released")]

INK = "#1f2937"
MUTED = "#6b7280"
GRID = "#e5e7eb"
SOLID = "#2563eb"   # main activity
LIGHT = "#bfdbfe"   # supporting / continuous activity
ACCENT = "#dc2626"  # gates and approvals

# (label, [(start, end, style, text)], [review points])
LANES = [
    ("SOP-001  Change control", [("start", "G4", "light", "every change: ECR → PR → approval → human merge")], []),
    ("SOP-003  Design review", [("start", "G4", "light", "check-ins in worklog.md", 5.0)], ["G1", "G2", "G3", "G4"]),
    ("SOP-004  Planning", [("start", "G1", "solid", "plan, requirements, risks"),
                           ("G3", "G4", "solid", "lessons")], []),
    ("SOP-002  Parts & revisions", [("G1", "G2", "solid", "part numbers, BOM → released")], []),
    ("SOP-005  Purchasing", [("G2", "buy", "solid", "orders")], []),
    ("SOP-006  Inspection & build", [("G2", "G3", "solid", "inspect · build · trace")], []),
    ("SOP-007  Test & release", [("G1", "G2", "light", "test procedures"),
                                 ("buy", "G3", "solid", "test"), ("G3", "G4", "solid", "release")], []),
    ("SOP-008  Nonconformance", [("G2", "G4", "hatch", "as needed: parts or units not as designed")], []),
]


def main():
    fig, ax = plt.subplots(figsize=(13, 6.4), dpi=100)
    left, right = -4.2, X["G4"] + 0.9
    n = len(LANES)
    top = n + 2.05
    ax.set_xlim(left, right)
    ax.set_ylim(-0.75, top + 0.25)
    ax.axis("off")

    # phase band
    for i, (name, a, b) in enumerate(PHASES):
        x0, x1 = X[a], X[b]
        ax.add_patch(FancyBboxPatch((x0 + 0.04, n - 0.42), x1 - x0 - 0.08, 0.5,
                                    boxstyle="round,pad=0,rounding_size=0.12",
                                    fc="#f3f4f6" if i % 2 else "#e5e7eb", ec="none"))
        ax.text((x0 + x1) / 2, n - 0.17, name, ha="center", va="center", fontsize=9.5, color=INK)

    # gate lines and diamonds
    for g, label in GATES:
        x = X[g]
        ax.plot([x, x], [-0.35, n - 0.45], color=GRID, lw=1.2, zorder=0)
        d = 0.17
        cy = n + 0.38
        ax.add_patch(Polygon([(x, cy - d * 1.6), (x + d, cy), (x, cy + d * 1.6),
                              (x - d, cy)], closed=True, fc=ACCENT, ec="white", lw=1, zorder=3))
        ax.text(x, cy + 0.32, g, ha="center", va="bottom", fontsize=10.5, fontweight="bold", color=ACCENT)
        ax.text(x, -0.45, label, ha="center", va="top", fontsize=8, color=MUTED, linespacing=1.1)

    # lanes
    for row, (label, bars, reviews) in enumerate(LANES):
        y = n - 1 - row
        ax.text(left + 0.05, y, label, ha="left", va="center", fontsize=9.5, color=INK, family="monospace")
        ax.plot([X["start"], X["G4"]], [y, y], color=GRID, lw=0.8, zorder=0)
        for bar in bars:
            a, b, style, text = bar[:4]
            x0, x1 = X[a], X[b]
            tx = bar[4] if len(bar) > 4 else (x0 + x1) / 2
            h = 0.5 if style != "light" else 0.34
            kw = dict(boxstyle="round,pad=0,rounding_size=0.1", zorder=2)
            if style == "solid":
                patch = FancyBboxPatch((x0 + 0.06, y - h / 2), x1 - x0 - 0.12, h, fc=SOLID, ec="none", **kw)
                tc = "white"
            elif style == "light":
                patch = FancyBboxPatch((x0 + 0.06, y - h / 2), x1 - x0 - 0.12, h, fc=LIGHT, ec="none", **kw)
                tc = INK
            else:
                patch = FancyBboxPatch((x0 + 0.06, y - h / 2), x1 - x0 - 0.12, h, fc="white",
                                       ec=SOLID, hatch="////", lw=1, **kw)
                tc = INK
            ax.add_patch(patch)
            ax.text(tx, y, text, ha="center", va="center", fontsize=8.3, color=tc, zorder=4,
                    bbox=dict(fc="white", ec="none", pad=1.5) if style == "hatch" else None)
        for g in reviews:
            ax.scatter([X[g]], [y], s=150, marker="o", fc=ACCENT, ec="white", lw=1.5, zorder=5)
            ax.text(X[g] + 0.18, y + 0.3, "formal\nreview", fontsize=7, color=ACCENT, va="bottom",
                    linespacing=1.0, zorder=5)

    # legend
    ly = n + 1.35
    items = [(SOLID, "main activity"), (LIGHT, "continuous / supporting"), (None, "as needed"),
             (ACCENT, "gate or formal review (human approval)")]
    lx = left + 0.05
    for color, text in items:
        if color is None:
            ax.add_patch(FancyBboxPatch((lx, ly - 0.12), 0.5, 0.24, boxstyle="round,pad=0,rounding_size=0.05",
                                        fc="white", ec=SOLID, hatch="////", lw=1))
        else:
            ax.add_patch(FancyBboxPatch((lx, ly - 0.12), 0.5, 0.24, boxstyle="round,pad=0,rounding_size=0.05",
                                        fc=color, ec="none"))
        ax.text(lx + 0.65, ly, text, va="center", fontsize=8.5, color=MUTED)
        lx += 0.65 + len(text) * 0.105 + 0.6

    ax.text(left + 0.05, top - 0.05, "minimalQMS: one iteration through the SOPs (not to scale)",
            ha="left", va="center", fontsize=12, color=INK, fontweight="bold")

    fig.tight_layout(pad=0.4)
    fig.savefig("docs/img/gate-timeline.svg")
    fig.savefig("docs/img/gate-timeline.png", dpi=200)
    print("wrote docs/img/gate-timeline.svg and .png")


if __name__ == "__main__":
    main()
