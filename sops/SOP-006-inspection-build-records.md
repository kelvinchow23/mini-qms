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
| **A** | Inspect against the order: correct part and revision, quantity, no visible damage, and any checks listed for the PN in `parts.csv`. Record the result in `inspection.csv`. |
| **B** | Visually confirm the item. No record beyond the received date in `purchases.csv`. |
| **C** | No inspection. |

When a Class A item fails, mark it `fail`, segregate it from accepted stock, and raise an
NC (SOP-008). Photos may be stored with the inspection record.
*Basis: ISO §8.4.2, §8.6. Classes are defined in SOP-002.*

## 4. Opening a build
Before assembly, record in `builds/B00n/build.yaml`:
- build ID, actual start date and builder;
- assembly PN and revision, and the QMS revision in use;
- configuration: the revision of every made part and the firmware version;
- serial numbers to be built (SOP-002 section 7);
- applicable deviations.

Use only `released` parts and revisions (SOP-002). Any other use requires a deviation.
*Basis: ISO §8.5.1, §8.5.2*

## 5. Trace record
`trace.csv` has one row per unit per traced part: serial number, PN, revision, quantity and
purchase line (`P-nnnn`). Class A parts are traced per unit. Class B parts are traced once
per build (serial number `all`). Class C parts are not traced.

An agent may prepare `trace.csv` from the build plan. The builder confirms or corrects it
during or immediately after assembly. Corrections are never made later from memory.
*Basis: ISO §8.5.2. Traceability by class is a minimalQMS choice.*

## 6. Records
`build.yaml`, `inspection.csv` and `trace.csv` in `builds/B00n/` are controlled under
SOP-001. CI checks that every Class A and B line in `trace.csv` refers to an existing
purchase line, and that every Class A purchase line used has passed inspection.
