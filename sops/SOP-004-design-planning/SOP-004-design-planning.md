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

## 3. Stages and gates
Development runs in five stages. Each stage ends at a gate, where the work is approved
before the next stage starts. Gates are the stage reviews ISO 9001 refers to.

| Stage | Gate | Name | Required to pass |
|---|---|---|---|
| Scope | **G0** | Scope approved | `plan.yaml`: goal, scope, make/buy, roles, target dates |
| Requirements | **G1** | Requirements reviewed | `requirements.yaml` with a verification method for each requirement, and `risks.csv` |
| Design | **G2** | Design freeze | Design reviewed against requirements and risks; parts and BOM released (SOP-002); test procedures (SOP-007), assembly instructions and inspection checks (SOP-006) written |
| Build and verify | **G3** | Verified | Units built and tested; results show the requirements are met (SOP-006, SOP-007) |
| Release and close-out | **G4** | Released | Units released (SOP-007); lessons learned recorded, including errors made by agents; scorecard compiled (section 8) |

`gates.yaml` lists the records each gate requires. CI blocks a gate with missing records.
The gate checklists (SOP-004-A06) list the records and the questions answered at each gate.
A gate that does not apply may be skipped, with the reason stated in `plan.yaml`.
*Basis: ISO §8.3.2, §8.3.4, §8.6. The five gates are a minimalQMS choice.*

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
G0 is passed by an explicit approval (SOP-001 section 7). G1 to G4 are passed by a formal
review (SOP-003). Record the actual date and the approval reference
in `plan.yaml`.

Gates are passed in order. Several gates may be passed in quick succession, including in
one session, provided each gate's records and approval exist before work for the next gate
starts. Ideas for later gates are recorded in `worklog.md` until that gate is reached.
When verification fails, the iteration stays in the build-and-verify stage. A design
problem is corrected by a design change (SOP-001) with a review of that change, followed by
a rebuild or retest. G3 is passed only when the results meet the requirements.
*Basis: ISO §8.3.4, §8.3.5. Passing gates in quick succession is a minimalQMS choice.*

## 7. Iterations
Development repeats in iterations. Each iteration starts at G0 from the last released
revisions and passes the gates again.
- **Inputs:** lessons learned (G4), nonconformances (SOP-008), feedback from use, and open
  ECRs. G0 records which ECRs the iteration covers.
- **Scope of each gate:** only what the iteration changes. A gate the iteration does not
  affect is skipped, with the reason in `plan.yaml`. Review packages cover the changes since
  the last release.
- **Plan:** each iteration has its own `plan.yaml` entry (`iteration: n`).
- **Between iterations:** a change to a released design that does not justify an iteration
  follows SOP-001 alone (ECR, review, new revision) without gates.

*Basis: ISO §8.3.2, §8.3.6. The iteration model is a minimalQMS choice.*

## 8. Scorecard
Each iteration has a scorecard (`00_planning/scorecard.csv`, SOP-004-A05), compiled by the
agent at G4 from the time entries in `worklog.md`. For each activity it shows the agent's
time, the human's hands-on time, and the human's estimate of the time the activity would
have taken without agents. The scorecard is reviewed with the lessons learned at G4.
*Basis: minimalQMS choice. Supports ISO §9.1 (monitoring and measurement).*

## 9. Build package
The build package (`03_build_package/`) holds the design outputs needed to buy, make,
build and test the product:
- `parts.csv` and `bom.csv` (SOP-002);
- mechanical: STEP files and PDF drawings, and STL or 3MF files for printed parts, each
  exported from the MCAD tool with the version it came from;
- electronics: PCB fabrication and assembly files (e.g. Gerbers, PCB BOM, placement file),
  exported from the ECAD tool;
- software: released binaries or images, with their version;
- assembly instructions and inspection checks (SOP-006), and test procedures (SOP-007).

Design sources remain in `02_design/`. Large binary files are stored with Git LFS. The
package is complete when the product can be bought, made, built and tested from it alone.
It is approved at G2.
*Basis: ISO §8.3.5, §8.5.1. The folder and its contents are a minimalQMS choice.*

## Appendices
Appendices are forms and templates that belong to this SOP. They carry the SOP's revision
and change only through a revision of this SOP.

| ID | Title | File | Used in product repos as |
|---|---|---|---|
| SOP-004-A01 | Development plan | [SOP-004-A01-plan.yaml](SOP-004-A01-plan.yaml) | `00_planning/plan.yaml` |
| SOP-004-A02 | Gate requirements | [SOP-004-A02-gates.yaml](SOP-004-A02-gates.yaml) | `00_planning/gates.yaml` |
| SOP-004-A03 | Requirements | [SOP-004-A03-requirements.yaml](SOP-004-A03-requirements.yaml) | `01_requirements/requirements.yaml` |
| SOP-004-A04 | Risk list (simplified FMEA) | [SOP-004-A04-risks.csv](SOP-004-A04-risks.csv) | `01_requirements/risks.csv` |
| SOP-004-A05 | Iteration scorecard | [SOP-004-A05-scorecard.csv](SOP-004-A05-scorecard.csv) | `00_planning/scorecard.csv` |
| SOP-004-A06 | Gate checklists | [SOP-004-A06-gate-checklists.md](SOP-004-A06-gate-checklists.md) | Used by agents and reviewers; not copied |
