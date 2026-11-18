---
id: SOP-003
title: Design review
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-003 Design review

Each section has a **Basis** line: *ISO §x.y* (required) or *minimalQMS choice*.
The reasoning behind this SOP is in `docs/REVIEW-MODEL.md`.

## 1. Purpose
Check that a design meets its requirements and that its risks are handled, record the
decisions, and give a human a clear, informed yes or no, without making them fill in forms.
*Basis: ISO §8.3.4 (reviews to evaluate whether results meet requirements, and to identify
problems and actions; records retained)*

## 2. Scope
Formal reviews at phase gates G1–G3 (SOP-004), and before any design change that needs a
formal review under SOP-001. The section on check-ins covers the informal contact in
between.

## 3. Three kinds of interaction
| Kind | Purpose | Record | Approval? |
|---|---|---|---|
| **Check-in** | Keep the human informed: what changed, who changed it, what's next | One entry in `worklog.md` | No |
| **Working decision** | Steer the work ("use the 0805 part") | `worklog.md` if notable; it shows up in the next review package | No |
| **Formal review** | Approve a set of changes or pass a gate | `02_design/reviews/DR-nnn/` | **Yes** |

Only a formal review approves anything. This keeps approvals deliberate and avoids
approval fatigue.
*Basis: minimalQMS choice*

## 4. Before the review: the package
The author (usually an agent) prepares `DR-nnn/package.md` from the template. It contains:
- **scope:** the items and revisions reviewed (from → to), CAD versions, ECRs and gate;
- **change groups,** each with what changed and why, who made it (human, agent, or agent
  directed by a human), where to look (links), visuals where useful (before/after renders,
  annotated screenshots, PCB layer images), and the requirements and risks affected;
- **independent findings:** from a fresh agent session with no memory of the design work;
- **open items:** carried-over actions and known gaps.

*Basis: ISO §8.3.4 (the review evaluates results against requirements). The package
format and independent agent review are minimalQMS choices (SOP-001 §8).*

## 5. During the review: the walkthrough
1. The agent presents one change group at a time. The human asks questions and
   challenges.
2. For each group, the human gives a disposition: **accept**, **reject** (with a
   reason), or **accept with action** (`A-nnn`, with an owner).
3. For each independent finding, the human records **accept** or **reject** with a reason.
4. The agent asks the overall question, naming exactly what's being approved, e.g.
   *"Approve DR-004: PCB-0001 rev B, 5 groups accepted, 1 with action A-012?"*
5. The human answers **yes** or **no**. That reply is the approval (SOP-001 §7).

The review is run in an agent tool that saves the session transcript.
*Basis: ISO §8.3.4 (identify problems and actions), §8.3.6. The walkthrough format is a
minimalQMS choice.*

## 6. After the review: records
In `DR-nnn/`:
- `package.md`: as reviewed, with its visuals.
- `minutes.md`: generated from the template, with participants (humans, plus agents and
  their models), the disposition of every group and finding, actions, and the decision.
  The approval is quoted and its location in the transcript is given.
- `transcript.*`: the raw session, unaltered.

The minutes go through a PR, and a human merges it (SOP-001). An action stays open until
it's closed with evidence, or explicitly carried forward at the next gate.
*Basis: ISO §8.3.4 and §8.3.6 (records of reviews and actions). Transcript archiving is a
minimalQMS choice.*

## 7. Check-ins
Whenever useful (for example after a work session), the agent adds a short entry to
`worklog.md`: what changed and who changed it, what's next, anything blocked, and items for
the next review. No reply is needed.
*Basis: minimalQMS choice (also supports ISO §7.1.6, organisational knowledge)*
