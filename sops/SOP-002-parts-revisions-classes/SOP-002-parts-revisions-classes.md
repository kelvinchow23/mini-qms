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

| Type | Format | Kept in | Example |
|---|---|---|---|
| **OTS part** (off the shelf) | `CCC-NNNN` | Part library (`parts-library` repo) | `FST-0001` M3x8 screws |
| **Custom part** | `PPP-NNNN` | Product repo, `03_release/parts.csv` | `PRX-0004` printed lid |
| **Custom assembly** | `PPP-A-NNNN` | Product repo, `03_release/parts.csv` | `PRX-A-0003` assembled PCB |

- `CCC` is an OTS category code; `PPP` is the project code. Both are 3 capital letters,
  registered in the part library, and never the same. `A` is a fixed letter that marks an
  assembly.
- An assembly has sub-parts or requires an assembly or modification instruction. A PCB
  ordered already assembled is an assembly.
- Custom parts and assemblies share one number sequence per project.
- Allocate numbers with the part library's `new_pn.py`. A part number never changes meaning
  and is never reused.
- OTS records hold where to buy: manufacturer, MPN, supplier, supplier part number, link,
  and unit price with its date. Custom records hold revision, lifecycle, make method and
  source (CAD reference), plus the same purchasing columns when the part is bought from a
  fabricator.

*Basis: ISO §8.5.2. The format is a minimalQMS choice; OTS category codes are adapted from
gitplm (see NOTICE).*

## 4. Revisions
The revision is a separate field, not part of the PN: `PRX-0002` rev `B`. Revisions run
A, B, C …, omitting I, O, Q, S, X and Z.
- **Interchangeable change** (same form, fit and function): increment the revision.
- **Non-interchangeable change:** assign a new PN.
- Firmware uses its version tag (e.g. `v1.2.0`) as the revision.
- OTS parts have no internal revision; the manufacturer part number defines them. A
  replacement MPN that is not a drop-in substitute receives a new PN.

A revision change follows SOP-001: everything that cites the part (`parts.csv`, BOMs,
drawings) is updated in the same change.
*Basis: ISO §8.3.6, §8.5.6, §7.5.3. The interchangeability rule and letter sequence are a
minimalQMS choice based on common drafting practice.*

## 5. Lifecycle
Each PN (OTS and custom) has one lifecycle state:

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

The class is set per PN. When in doubt, assign the higher class.
*Basis: ISO §8.5.2 and §8.4.2 allow traceability and control to be set by risk. The A/B/C
scheme is a minimalQMS choice.*

## 7. Serial numbers
Assemblies (`PPP-A-NNNN`) receive a serial number. Parts do not; they are traced by
purchase line or print job.
- **Format:** `<PN>-YYMMDD<letter>`, where the date is the assembly date (or the receipt
  date for purchased assemblies) and the letter counts units of that PN on that date: A,
  B … Z, then AA. Example: `PRX-A-0003-261118A`.
- **Label:** mark the serial number on the unit. Where the PN is already marked on the unit,
  the label may show only `YYMMDD<letter>`.
- **Record:** the serial number is listed in the build record (SOP-006), which links it to
  the assembly revision, its Class A purchase lines and any sub-assembly serial numbers.
  No separate form is required.
- Purchased assemblies receive their serial number at incoming inspection (SOP-006).

*Basis: ISO §8.5.2. The format is a minimalQMS choice.*

## 8. Records
- Product repo `03_release/parts.csv`: custom parts and assemblies.
- Product repo `03_release/bom.csv`: master BOM, one block of lines per assembly (top level
  and each sub-assembly), referring to OTS and custom PNs alike. Exported from the CAD tools
  at release.
- Part library: OTS `parts.csv`, `categories.csv` and `projects.csv`.

These records are controlled under SOP-001. CI checks that every BOM line refers to an
existing, `released` PN with a class, and that bought items have a supplier.

## Appendices
Appendices are forms and templates that belong to this SOP. They carry the SOP's revision
and change only through a revision of this SOP.

| ID | Title | File | Used in product repos as |
|---|---|---|---|
| SOP-002-A01 | Custom parts list | [SOP-002-A01-custom-parts.csv](SOP-002-A01-custom-parts.csv) | `03_release/parts.csv` |
| SOP-002-A02 | Master BOM | [SOP-002-A02-bom.csv](SOP-002-A02-bom.csv) | `03_release/bom.csv` |
