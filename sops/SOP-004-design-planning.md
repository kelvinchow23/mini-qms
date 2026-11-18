---
id: SOP-004
title: Design and development planning
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-004 Design and development planning

Each section ends with its basis: *ISO §x.y* (required by the standard) or *minimalQMS
choice* (may be changed by teams using minimalQMS).

## 1. Purpose
To plan each product's development in stages, with gates that state what must be complete
before work proceeds.
*Basis: ISO §8.3.2*

## 2. Scope
Every product repo, from the start of a project or iteration to close-out. Day-to-day
scheduling is outside this procedure; any tool may be used.

## 3. Phase gates

| Gate | Name | Required to pass |
|---|---|---|
| **G0** | Scope | `plan.yaml` approved: goal, scope, make/buy, roles, target dates |
| **G1** | Requirements frozen | `requirements.yaml` and `risks.csv` approved in a formal review |
| **G2** | Design complete | Design reviewed against requirements and risks; actions closed or carried forward |
| **G3** | Released for build | Parts and BOM released (SOP-002); test procedures released (SOP-007) |
| **G4** | Built and verified | Every unit released or dispositioned (SOP-007, SOP-008) |
| **G5** | Close-out | Lessons learned recorded, including errors made by agents |

`gates.yaml` lists the records each gate requires. CI blocks a gate with missing records.
A gate that does not apply may be skipped, with the reason stated in `plan.yaml`.
*Basis: ISO §8.3.2. The six gates are a minimalQMS choice.*

## 4. Plan
`plan.yaml` states the goal, scope, responsibilities (from `roles.yaml`), and for each
gate the target date, actual date and approval reference. Change a target date through a
PR with a one-line reason; earlier targets remain in the git history.
*Basis: ISO §8.3.2. Recording planned and actual dates is a minimalQMS choice.*

## 5. Requirements and risks
- `requirements.yaml`: each requirement has an ID (`REQ-nnn`), a statement, a source
  (customer, standard or internal) and a verification method (test, inspection, analysis
  or review).
- `risks.csv`: a simplified FMEA. Each line has an ID (`RISK-nnn`), the hazard or failure,
  its effect, severity and likelihood (1–5), the controls, and the requirement or test that
  verifies the controls.

Both are frozen at G1. Later changes follow SOP-001.
*Basis: ISO §8.3.3, §6.1.2. The FMEA format is a minimalQMS choice.*

## 6. Passing a gate
Gates G1–G3 are passed by a formal review (SOP-003). Gates G0, G4 and G5 are passed by an
explicit approval (SOP-001 section 7). Record the actual date and the approval reference
in `plan.yaml`.
*Basis: ISO §8.3.4, §8.3.5*
