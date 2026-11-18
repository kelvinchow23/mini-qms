---
id: SOP-004
title: Design and development planning
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-004 Design and development planning

Each section has a **Basis** line: *ISO §x.y* (required) or *minimalQMS choice*.

## 1. Purpose
Plan each product's development in stages with clear gates, so it's known what must be
true before moving on. Planning shouldn't turn into project-management overhead.
*Basis: ISO §8.3.2 (plan stages, reviews, verification and validation, responsibilities,
interfaces, and involvement of relevant parties)*

## 2. Scope
Every product repo, from the start of a project or iteration to close-out. How the
schedule is managed day to day isn't covered; use any tool.

## 3. Phase gates
| Gate | Name | What must be true |
|---|---|---|
| **G0** | Scope | `plan.yaml` approved: goal, scope, make/buy, roles, target dates |
| **G1** | Requirements frozen | `requirements.yaml` and `risks.csv` approved in a formal review |
| **G2** | Design complete | Design reviewed against requirements and risks; actions closed or carried forward |
| **G3** | Released for build | Parts and BOM released (SOP-002); test procedures written (SOP-007) |
| **G4** | Built and verified | Every unit tested and released or dispositioned (SOP-007, SOP-008) |
| **G5** | Close-out | Lessons learned written, including where AI was wrong |

`gates.yaml` lists the records each gate needs. CI blocks a gate whose records are
missing. A product may drop a gate that doesn't apply, with a reason in `plan.yaml`.
*Basis: ISO §8.3.2 (stages and controls). The six gates are a minimalQMS choice.*

## 4. The plan
`plan.yaml` gives the goal, scope, responsibilities (from `roles.yaml`), and for each gate
the **target date**, the **actual date** and the approval reference. When a target date
moves, it's changed through a PR with a one-line reason. Old targets stay in the git history.
*Basis: ISO §8.3.2. Recording planned vs. actual dates is a minimalQMS choice; it also
measures how lean the process really is.*

## 5. Requirements and risks
- `requirements.yaml`: each requirement has an ID (`REQ-nnn`), a statement, its source
  (customer, standard, internal) and a **verification method** (test, inspection,
  analysis or review).
- `risks.csv`: a lightweight FMEA. Each line has an ID (`RISK-nnn`), the hazard or failure,
  its effect, severity and likelihood (1–5 each), the controls, and the requirement or
  test that verifies them.
- Both are frozen at G1. Later changes go through SOP-001.

*Basis: ISO §8.3.3 (design inputs, including standards and the consequences of failure),
§6.1.2 (actions on risks proportionate to their impact). The FMEA format is a minimalQMS
choice.*

## 6. Gate approval
Gates G1–G3 are passed by a formal review (SOP-003). G0, G4 and G5 are passed by an
explicit approval under SOP-001 §7. The actual date and approval reference are then
recorded in `plan.yaml`.
*Basis: ISO §8.3.4, §8.3.5 (design outputs meet input requirements)*
