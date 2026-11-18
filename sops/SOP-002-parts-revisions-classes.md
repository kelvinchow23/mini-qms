---
id: SOP-002
title: Part numbering, revisions and part classes
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead     # a role, see roles.yaml
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-002 Part numbering, revisions and part classes

Each section ends with its basis: *ISO §x.y* (required by the standard) or *minimalQMS
choice* (may be changed by teams using minimalQMS).

## 1. Purpose
To identify every part, assembly and unit, state its current revision, and set the level
of traceability according to risk.
*Basis: ISO §8.5.2, §8.4.2*

## 2. Scope
Everything that appears on a BOM: purchased parts, made parts (PCBs, printed or machined
parts, harnesses), assemblies, firmware and consumables. Also serial numbers of built units.

## 3. Part numbers
Part numbers use the format **`CCC-NNNN`** (e.g. `PCB-0001`, `ASY-0001`, `RES-0002`).
`CCC` is a category code from `part-categories.csv`; `NNNN` is the next free number in
that category. Use capital letters, digits and hyphens only.
- A part number never changes meaning and is never reused.
- Related made items may share `NNNN` (e.g. `PCB-0001` bare board, `PCA-0001` assembled
  board).
- Purchased parts also receive an internal PN, mapped to the manufacturer part number in
  `parts.csv`. A change of supplier is then a one-line change.

*Basis: ISO §8.5.2. The format is a minimalQMS choice adapted from gitplm (see NOTICE).*

## 4. Revisions
The revision is a separate field, not part of the PN: `PCB-0001` rev `B`. Revisions run
A, B, C …, omitting I, O, Q, S, X and Z.
- **Interchangeable change** (same form, fit and function): increment the revision.
- **Non-interchangeable change:** assign a new PN.
- Firmware uses its version tag (e.g. `v1.2.0`) as the revision.
- Purchased parts have no internal revision (`-`); the manufacturer part number defines
  them. A replacement MPN that is not a drop-in substitute receives a new PN.

A revision change follows SOP-001: everything that cites the part (`parts.csv`, BOMs,
drawings) is updated in the same change.
*Basis: ISO §8.3.6, §8.5.6, §7.5.3. The interchangeability rule and letter sequence are a
minimalQMS choice based on common drafting practice.*

## 5. Lifecycle
Each PN in `parts.csv` has one lifecycle state:

| State | Meaning |
|---|---|
| `draft` | In design. Not permitted on a released BOM. |
| `released` | Approved for building or purchasing. |
| `obsolete` | Not permitted in new builds. Retained for traceability of existing units. |

State changes follow SOP-001.
*Basis: ISO §8.5.2. The three states are a minimalQMS choice.*

## 6. Part classes

| Class | Items | Traced to | Incoming inspection |
|---|---|---|---|
| **A** | Made parts and key components: PCBs, LEDs, driver ICs, printed or machined parts, harnesses | The specific purchase or print job, per unit | Yes, recorded |
| **B** | Bulk hardware: screws, standoffs, heat-set inserts, wire, crimps | The bulk purchase | Visual check, not recorded |
| **C** | Consumables: glue, flux, solder, zip ties | Not traced | None |

The class is set per PN in `parts.csv`. When in doubt, assign the higher class.
*Basis: ISO §8.5.2 and §8.4.2 allow traceability and control to be set by risk. The A/B/C
scheme is a minimalQMS choice.*

## 7. Serial numbers
Each built unit receives a serial number unique within its product (`SN001`, `SN002` …).
The build record links each serial number to its assembly PN and revision and to the
Class A purchases it contains (SOP-006).
*Basis: ISO §8.5.2*

## 8. Records
- `parts.csv`: part master, one row per PN.
- `bom.csv`: one row per line item, exported from the CAD tools at release and joined with
  `parts.csv`.
- `part-categories.csv`: category codes in use.

These records are controlled under SOP-001. CI checks that every BOM line has a PN that
exists in `parts.csv`, is `released` and has a class, and that purchased parts have a
supplier.
