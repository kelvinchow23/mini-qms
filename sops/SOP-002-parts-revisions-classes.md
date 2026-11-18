---
id: SOP-002
title: Part numbering, revisions and part classes
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead     # a role, see roles.yaml
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-002 Part numbering, revisions and part classes

Each section has a **Basis** line: *ISO §x.y* (required) or *minimalQMS choice*.

## 1. Purpose
Every part, assembly and unit can be identified, its current revision is known, and the
level of traceability matches the risk.
*Basis: ISO §8.5.2 (identify outputs and their status; unique identification where
traceability is required), §8.4.2 (control of purchased items proportionate to risk)*

## 2. Scope
Everything that appears on a BOM: purchased parts, made parts (PCBs, printed or machined
parts, harnesses), assemblies, firmware and consumables. It also covers serial numbers
for built units.

## 3. Part numbers
**Format: `CCC-NNNN`**, for example `PCB-0001`, `ASY-0001`, `RES-0002`.
- `CCC` is a category code from `part-categories.csv`. Keep the list short.
- `NNNN` is the next free number in that category.
- Use only capital letters, digits and hyphens. Every PN has the same length.
- **A part number never changes meaning.** It's never reused, even after the part is
  obsolete.
- Related made items can share `NNNN` (e.g. `PCB-0001` bare board, `PCA-0001` assembled
  board), so one number finds the whole set.
- Purchased parts get an internal PN too, mapped to the manufacturer part number(s) in
  `parts.csv`. That makes changing supplier or adding a second source a one-line change.

*Basis: ISO §8.5.2 (identification). The format is a minimalQMS choice, adapted from
gitplm's part-numbering guide (see NOTICE).*

## 4. Revisions
- The revision is a **separate field**, not part of the PN: `PCB-0001` rev `B`.
- Revisions go A, B, C … skipping I, O, Q, S, X and Z (they're easily confused with digits).
- **Interchangeable change** (same form, fit and function; old and new can be used in
  each other's place): bump the revision.
- **Not interchangeable:** give it a **new PN**.
- Firmware uses its version tag (e.g. `v1.2.0`) as the revision.
- Purchased parts have no internal revision (`-`). The manufacturer part number
  defines them. A different MPN that isn't a drop-in replacement gets a new PN.
- A revision change follows SOP-001: everything that cites the part is updated in the
  same change (`parts.csv`, BOMs, drawings).

*Basis: ISO §8.3.6, §8.5.6 (controlled changes), §7.5.3 (version control). The
interchangeability rule and letter scheme are minimalQMS choices, following common
drafting practice.*

## 5. Lifecycle
Each PN in `parts.csv` has a lifecycle state:

| State | Meaning |
|---|---|
| `draft` | Being designed. Can't go on a released BOM. |
| `released` | Approved for building or buying. |
| `obsolete` | Not for new builds. Kept for traceability of units already built. |

State changes go through SOP-001: a PR, plus an approval.

*Basis: ISO §8.5.2 (status of outputs). The three states are a minimalQMS choice.*

## 6. Part classes (traceability by risk)

| Class | What | Traced to | Inspection on arrival |
|---|---|---|---|
| **A** | Made parts and key components: PCBs, LEDs, driver ICs, printed or machined parts, harnesses | The specific purchase or print job, per unit | Yes, recorded |
| **B** | Bulk hardware: screws, standoffs, heat-set inserts, wire, crimps | The bulk purchase it came from | Visual check, not recorded |
| **C** | Consumables: glue, flux, solder, zip ties | Not traced | None |

The class is set per PN in `parts.csv`. If in doubt, choose the higher class.

*Basis: ISO §8.5.2 requires traceability only where you decide it's needed, and §8.4.2
lets control match the risk. The A/B/C scheme is a minimalQMS choice.*

## 7. Serial numbers
Each built unit gets a serial number, unique within its product: `SN001`, `SN002` …
The build record links each serial number to its assembly PN and revision, and to the
Class A purchases it used.
*Basis: ISO §8.5.2 (unique identification where traceability is required)*

## 8. Records
- **`parts.csv`:** the part master, one row per PN.
- **`bom.csv`:** one row per line item, exported from the CAD tools at release and joined
  with `parts.csv` (see the README's "Design source of truth").
- **`part-categories.csv`:** the category codes in use.

These are kept under SOP-001. CI checks that every BOM line's PN exists in `parts.csv`,
is `released`, and has a class. Purchased parts must also have a supplier.
