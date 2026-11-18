---
id: SOP-006
title: Incoming inspection and build records
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-006 Incoming inspection and build records

Each section has a **Basis** line: *ISO §x.y* (required) or *minimalQMS choice*.

## 1. Purpose
Check critical parts when they arrive, and record what went into each unit, so that
`trace SNnnn` works and a bad part can be traced to every unit that contains it.
*Basis: ISO §8.4.2 (verify purchased items), §8.5.1 (controlled production), §8.5.2
(identification and traceability)*

## 2. Scope
Every build of a product: receiving its parts, assembling the units and recording what
went into them. Testing and release are covered by SOP-007.

## 3. Incoming inspection
| Class | On arrival |
|---|---|
| **A** | Inspect against the order: right part and revision, quantity, visible damage, plus any checks listed for that PN in `parts.csv` notes (e.g. PCB dimensions, LED wavelength marking). Record the result in `inspection.csv`. |
| **B** | Visual check that it's the right item. No record needed beyond the received date in `purchases.csv`. |
| **C** | None. |

If a Class A item fails, mark it `fail`, keep it apart from good stock, and raise an NC
(SOP-008). Where photos help, the agent stores them next to the inspection record.
*Basis: ISO §8.4.2 (type and extent of control by risk), §8.6 (verification before use).
The A/B/C split comes from SOP-002.*

## 4. Opening a build
Before assembly starts, `builds/B00n/build.yaml` records:
- the build ID, actual start date and builder;
- the assembly PN and revision, and the QMS revision used;
- the **configuration**: the revision of every made part and the firmware version used;
- the serial numbers to be built (SOP-002 §7);
- any deviations that apply.

Only `released` parts and revisions may be used (SOP-002). Using anything else needs a
deviation.
*Basis: ISO §8.5.1 (documented information on the product and the results to achieve;
controlled conditions), §8.5.2*

## 5. Recording what went into each unit
`trace.csv` has one row per unit per traced part: serial number, PN, revision, quantity
and the purchase line (`P-nnnn`) it came from. Class A parts are traced to the line
**per unit**. Class B parts are traced to the line once per build (serial number `all`).
Class C parts aren't traced.

An agent fills `trace.csv` from the build plan, and the builder confirms or corrects it
during or right after assembly. Corrections are made at the time, never later from
memory.
*Basis: ISO §8.5.2 (unique identification and records where traceability is required).
Traceability by class is a minimalQMS choice.*

## 6. Records
`build.yaml`, `inspection.csv` and `trace.csv` in `builds/B00n/`, kept under SOP-001. CI
checks that every A and B line in `trace.csv` points to a real purchase line, and that
every Class A purchase line used has passed inspection.
