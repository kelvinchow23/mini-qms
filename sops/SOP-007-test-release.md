---
id: SOP-007
title: Test and release
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-007 Test and release

Each section has a **Basis** line: *ISO §x.y* (required) or *minimalQMS choice*.

## 1. Purpose
Prove that each built unit meets its requirements before it's released, using equipment
whose readings can be trusted, and record who released it.
*Basis: ISO §8.6 (release of products), §8.3.4 (verification), §7.1.5 (monitoring and
measuring resources)*

## 2. Scope
Testing and release of every unit built under SOP-006, plus the test equipment used.
Design validation (does the design meet its intended use?) is planned as requirements and
gates in SOP-004.

## 3. Test procedures
Each requirement verified by test (SOP-004) points to a test procedure
`03_release/test_procedures/TP-nnn.md`. A procedure lists the setup, the equipment
needed, the steps, and for each measurement the **limits** and the requirement it checks.
Test procedures are controlled documents (SOP-001) and are released at gate G3.
*Basis: ISO §8.3.4 (verification activities), §8.6 (planned arrangements for release)*

## 4. Test equipment
`equipment.csv` lists each instrument used for an accept/reject decision (`EQ-nnn`):
whether it needs calibration and, if so, when it's next due and a reference to its
certificate. A test can't use equipment that's overdue. If equipment is found faulty or
out of calibration, check whether earlier results it produced are still valid, and raise
an NC if needed.
Instruments used only for rough or indicative checks are marked `cal_required: no`, with a
reason.
*Basis: ISO §7.1.5 (fit for purpose; calibrated or verified where measurement
traceability is required; action if found unfit)*

## 5. Testing
Results go in `test_results.csv`, one row per measurement: serial number, test procedure
and step, date, tester, equipment, measured value, limits and result (`pass` / `fail`).
An agent may run automated tests and record their results. A human checks any result
the agent can't measure directly. A failure leads to an NC (SOP-008), and the unit can't
be released until the NC is dispositioned.
*Basis: ISO §8.6 (evidence of conformity), §8.7 (nonconforming outputs are not
released)*

## 6. Release
A unit is released when every test for its configuration has passed (or failed tests are
covered by an NC dispositioned `use-as-is`), its trace is complete (SOP-006), and no
deviation blocks it. The agent prepares `release.yaml` with this evidence. The release
approver approves it under SOP-001 §7 and merges it. CI checks the evidence before the
merge is allowed.
*Basis: ISO §8.6 (release only when planned arrangements are met, or approved by a
relevant authority; record traceable to the person authorising release)*

## 7. Records
`TP-nnn.md`, `equipment.csv`, `test_results.csv` and `release.yaml`, kept under SOP-001.
Calibration certificates may be kept in the organisation's own systems and referred to
by number.
