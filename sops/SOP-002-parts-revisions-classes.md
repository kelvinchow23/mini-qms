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
| Format | Used for | Examples |
|---|---|---|
| **`CCC-NNNN`** | Parts: single items with no sub-parts, made or purchased | `PCB-0001` bare board, `MEC-0003` printed bracket, `RES-0002` resistor |
| **`CCC-A-NNNN`** | Assemblies: items with sub-parts, or that require an assembly or modification instruction | `PCB-A-0001` assembled board, `HRN-A-0002` harness, `SYS-A-0001` complete product |

`CCC` is a category code from `part-categories.csv`. `A` is a fixed letter that marks an
assembly. `NNNN` is the next free number in that category. Use capital letters, digits
and hyphens only.
- A part number never changes meaning and is never reused.
- An assembly built from one main part shares its number (e.g. `PCB-0001` bare board,
  `PCB-A-0001` assembled board).
- A PCB ordered already assembled is an assembly (`PCB-A-NNNN`) with its own revision.
- Purchased parts also receive an internal PN, mapped to the manufacturer part number in
  `parts.csv`. A change of supplier is then a one-line change.

*Basis: ISO §8.5.2. The format is a minimalQMS choice; category codes are adapted from
gitplm (see NOTICE).*

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
Assemblies (`CCC-A-NNNN`) receive a serial number. Parts do not; they are traced by
purchase line or print job.
- **Format:** `<PN>-YYMMDD<letter>`, where the date is the assembly date (or the receipt
  date for purchased assemblies) and the letter counts units of that PN on that date: A,
  B … Z, then AA. Example: `PCB-A-0001-261118A`.
- **Label:** mark the serial number on the unit. Where the PN is already marked on the unit,
  the label may show only `YYMMDD<letter>`.
- **Record:** the serial number is listed in the build record (SOP-006), which links it to
  the assembly revision, its Class A purchase lines and any sub-assembly serial numbers.
  No separate form is required.
- Purchased assemblies receive their serial number at incoming inspection (SOP-006).

*Basis: ISO §8.5.2. The format is a minimalQMS choice.*

## 8. Records
- `parts.csv`: part master, one row per PN.
- `bom.csv`: one row per line item, exported from the CAD tools at release and joined with
  `parts.csv`.
- `part-categories.csv`: category codes in use.

These records are controlled under SOP-001. CI checks that every BOM line has a PN that
exists in `parts.csv`, is `released` and has a class, and that purchased parts have a
supplier.
