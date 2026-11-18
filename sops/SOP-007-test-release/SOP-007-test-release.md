---
id: SOP-007
title: Test and release
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-007 Test and release

Each section ends with its basis: *ISO §x.y* (required by the standard) or *minimalQMS
choice* (may be changed by teams using minimalQMS).

## 1. Purpose
To verify that each built unit meets its requirements before release, using suitable
equipment, and to record who released it.
*Basis: ISO §8.6, §8.3.4, §7.1.5*

## 2. Scope
Testing and release of every unit built under SOP-006, and the test equipment used.
Design validation is planned through requirements and gates (SOP-004).

## 3. Test procedures
Each requirement verified by test (SOP-004) refers to a test procedure
`03_release/test_procedures/TP-nnn.md`. A test procedure states the setup, the equipment,
the steps, and for each measurement the limits and the requirement checked. Test
procedures are controlled documents (SOP-001) and are released at gate G3.
*Basis: ISO §8.3.4, §8.6*

## 4. Test equipment
`equipment.csv` lists each instrument used for an accept or reject decision (`EQ-nnn`),
whether it requires calibration, the calibration due date and the certificate reference.
- Equipment past its calibration due date must not be used.
- When equipment is found faulty or out of calibration, assess earlier results made with
  it and raise an NC where required.
- Instruments used only for indicative checks are marked `cal_required: no`, with a reason.

*Basis: ISO §7.1.5*

## 5. Testing
Record results in `test_results.csv`, one row per measurement: serial number, test
procedure and step, date, tester, equipment, measured value, limits and result (`pass` or
`fail`). An agent may run automated tests and record their results. A human performs or
confirms any measurement the agent cannot take directly. A failure requires an NC
(SOP-008); the unit is not released until the NC is dispositioned.
*Basis: ISO §8.6, §8.7*

## 6. Release
A unit may be released when all tests for its configuration have passed, or failures are
covered by an NC dispositioned `use-as-is`; its trace record is complete (SOP-006); and no
deviation prevents release. The agent prepares `release.yaml` with this evidence. The
release approver approves it (SOP-001 section 7) and merges it. CI checks the evidence
before merge.
*Basis: ISO §8.6*

## 7. Records
`TP-nnn.md`, `equipment.csv`, `test_results.csv` and `release.yaml` are controlled under
SOP-001. Calibration certificates may be kept in the organisation's own systems and
referred to by number.

## Appendices
Appendices are forms and templates that belong to this SOP. They carry the SOP's revision
and change only through a revision of this SOP.

| ID | Title | File | Used in product repos as |
|---|---|---|---|
| SOP-007-A01 | Test procedure | [SOP-007-A01-test-procedure.md](SOP-007-A01-test-procedure.md) | `03_release/test_procedures/TP-nnn.md` |
| SOP-007-A02 | Test results | [SOP-007-A02-test-results.csv](SOP-007-A02-test-results.csv) | `builds/B00n/test_results.csv` |
| SOP-007-A03 | Equipment and calibration list | [SOP-007-A03-equipment.csv](SOP-007-A03-equipment.csv) | `equipment/equipment.csv` |
| SOP-007-A04 | Release record | [SOP-007-A04-release.yaml](SOP-007-A04-release.yaml) | `builds/B00n/release.yaml` |
