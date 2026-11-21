---
id: SOP-006
title: Incoming inspection and build records
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-006 Incoming inspection and build records

Each section ends with its basis: *ISO §x.y* (required by the standard) or *minimalQMS
choice* (may be changed by teams using minimalQMS).

## 1. Purpose
To inspect critical parts on receipt and to record what went into each unit, so that any
unit can be traced to its parts and any part to the units that contain it.
*Basis: ISO §8.4.2, §8.5.1, §8.5.2*

## 2. Scope
Every build of a product: receipt of parts, assembly of units and recording of their
contents. Testing and release are covered by SOP-007.

## 3. Incoming inspection

| Class | On receipt |
|---|---|
| **A** | Inspect against the order (correct part and revision, quantity, no visible damage) and against the checks for the PN in `inspection_checks.csv` (SOP-006-A05). Record the result in `inspection.csv`. |
| **B** | Visually confirm the item. No record beyond the received date in `purchases.csv`. |
| **C** | No inspection. |

A purchased assembly receives its serial number at inspection (SOP-002 section 7).
When a Class A item fails, mark it `fail`, segregate it from accepted stock, and raise an
NC (SOP-008). Photos may be stored with the inspection record.
*Basis: ISO §8.4.2, §8.6. Classes are defined in SOP-002.*

## 4. Assembly instructions and inspection checks
Each assembly (`PPP-A-NNNN`) built in-house has an assembly instruction
(`03_build_package/assembly/PPP-A-NNNN.md`, SOP-006-A04) with the same revision as the assembly.
Each Class A part has its incoming checks in `03_build_package/inspection_checks.csv`
(SOP-006-A05). Both are design outputs, approved at G2 with the BOM (SOP-004). The builder
follows the instruction; a step that cannot be followed as written is recorded in the build
record and an ECR is raised.
*Basis: ISO §8.3.5 (design outputs specify production and inspection), §8.5.1 (documented
information for production)*

## 5. Opening a build
Before assembly, record in `builds/B00n/build.yaml`:
- build ID, actual start date and builder;
- assembly PN and revision, and the QMS revision in use;
- configuration: the revision of every made part and the firmware version;
- serial numbers to be built (SOP-002 section 7);
- applicable deviations.

Use only `released` parts and revisions (SOP-002). Any other use requires a deviation.
*Basis: ISO §8.5.1, §8.5.2*

## 6. Trace record
`trace.csv` has one row per unit per traced part: serial number, PN, revision, quantity,
purchase line (`P-nnnn`), and the sub-assembly's own serial number where it has one. Class A parts are traced per unit. Class B parts are traced once
per build (serial number `all`). Class C parts are not traced.

An agent may prepare `trace.csv` from the build plan. The builder confirms or corrects it
during or immediately after assembly. Corrections are never made later from memory.
*Basis: ISO §8.5.2. Traceability by class is a minimalQMS choice.*

## 7. Unit history
After release, record every change to a unit in `builds/unit_history.csv` (SOP-006-A06):
serial number, date, what changed (e.g. software v1.2.0 to v1.3.0, part replaced, rework,
recalibration), the reason (ECR or NC reference) and who made the change. Per-unit settings
such as calibration values are recorded in the unit's build or history records.
Credentials are never stored in the repo.
*Basis: ISO §8.5.2, §8.5.6*

## 8. Records
`build.yaml`, `inspection.csv` and `trace.csv` in `builds/B00n/`, the assembly instructions
and the inspection checks are controlled under SOP-001. CI checks that every Class A and B line in `trace.csv` refers to an existing
purchase line, and that every Class A purchase line used has passed inspection.

## Appendices
Appendices are forms and templates that belong to this SOP. They carry the SOP's revision
and change only through a revision of this SOP.

| ID | Title | File | Used in product repos as |
|---|---|---|---|
| SOP-006-A01 | Build record header | [SOP-006-A01-build.yaml](SOP-006-A01-build.yaml) | `builds/B00n/build.yaml` |
| SOP-006-A02 | Incoming inspection record | [SOP-006-A02-inspection.csv](SOP-006-A02-inspection.csv) | `builds/B00n/inspection.csv` |
| SOP-006-A03 | Trace record | [SOP-006-A03-trace.csv](SOP-006-A03-trace.csv) | `builds/B00n/trace.csv` |
| SOP-006-A04 | Assembly instruction | [SOP-006-A04-assembly-instruction.md](SOP-006-A04-assembly-instruction.md) | `03_build_package/assembly/PPP-A-NNNN.md` |
| SOP-006-A05 | Incoming inspection checks | [SOP-006-A05-inspection-checks.csv](SOP-006-A05-inspection-checks.csv) | `03_build_package/inspection_checks.csv` |
| SOP-006-A06 | Unit history | [SOP-006-A06-unit-history.csv](SOP-006-A06-unit-history.csv) | `builds/unit_history.csv` |
