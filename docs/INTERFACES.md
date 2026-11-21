# Interfaces: shared names across the SOPs

The SOPs pass records to each other. This file fixes the names they share, so every
SOP, template, CI check and agent uses the same ones. **If a SOP needs a new shared name,
add it here first.**

## Product repo layout

```
roles.yaml                      SOP-001  who holds which role
worklog.md                      SOP-003  check-ins and notable working decisions
00_planning/
  plan.yaml                     SOP-004  gates: target and actual dates
  scorecard.csv                 SOP-004  agent and human time per activity, per iteration
  gates.yaml                    SOP-004  what each gate requires
01_requirements/
  requirements.yaml             SOP-004  REQ-nnn with verification method
  risks.csv                     SOP-004  RISK-nnn (lightweight FMEA)
02_design/
  reviews/DR-nnn/               SOP-003  package, minutes, transcript, visuals
03_build_package/               SOP-004  everything needed to buy, make, build and test
  parts.csv, bom.csv            SOP-002
  mechanical/                   SOP-004  STEP, PDF drawings, STL/3MF (with MCAD version)
  electronics/                  SOP-004  PCB fabrication and assembly files (with ECAD version)
  software/                     SOP-004  released binaries or images
  test_procedures/TP-nnn.md     SOP-007
  assembly/PPP-A-NNNN.md        SOP-006  assembly instruction per in-house assembly
  inspection_checks.csv         SOP-006  incoming checks for Class A parts
purchasing/
  purchases.csv                 SOP-005
  suppliers.csv                 SOP-005
  requisitions/<order_ref>.csv  SOP-005  purchasing upload files as submitted
builds/B00n/
  build.yaml                    SOP-006  build header and unit list
  inspection.csv                SOP-006  incoming inspection of Class A lines
  trace.csv                     SOP-006  which purchases went into which unit
  test_results.csv              SOP-007
  release.yaml                  SOP-007  release decision per unit
builds/unit_history.csv         SOP-006  changes to units after release
equipment/equipment.csv         SOP-007  test equipment and calibration due dates
nonconformance/NC-nnn.md        SOP-008
deviations/DEV-nnn.md           SOP-001
```

## IDs

| ID | Meaning | Defined in | Example |
|---|---|---|---|
| `<top assembly>-rev<X>` | Baseline tag of a released configuration | SOP-002 | `PRX-A-0001-revB` |
| `CCC-NNNN` | OTS part (OTS library) | SOP-002 | `HWS-0001` |
| `PPP-NNNN` + rev | Custom part (product repo) | SOP-002 | `PRX-0004` rev `B` |
| `PPP-A-NNNN` + rev | Custom assembly (product repo) | SOP-002 | `PRX-A-0003` rev `A` |
| `<PN>-YYMMDD<letter>` | Serial number (assemblies only) | SOP-002 | `PRX-A-0003-261118A` |
| ECR `#n` | Change request (an issue) | SOP-001 | `ECR #12` |
| `SOP-nnn-Ann` | SOP appendix (form or template) | SOP-001 | `SOP-003-A01` review package |
| `DEV-nnn` | Deviation | SOP-001 | `DEV-001` |
| `DR-nnn` | Formal design review | SOP-003 | `DR-004` |
| `A-nnn` | Action from a review | SOP-003 | `A-012` |
| `G0`–`G4` | Gates | SOP-004 | `G2` |
| `REQ-nnn` | Requirement | SOP-004 | `REQ-007` |
| `RISK-nnn` | Risk (FMEA line) | SOP-004 | `RISK-003` |
| `P-nnnn` | Purchase line | SOP-005 | `P-0042` |
| `B00n` | Build | SOP-006 | `B002` |
| `TP-nnn` | Test procedure | SOP-007 | `TP-001` |
| `EQ-nnn` | Test or measuring equipment | SOP-007 | `EQ-003` |
| `NC-nnn` | Nonconformance | SOP-008 | `NC-005` |

IDs are never reused. Numbers are zero-padded so they sort correctly.

## Gates (SOP-004)

| Gate | Name | Passed by |
|---|---|---|
| G0 | Scope approved | Approval of the plan |
| G1 | Requirements reviewed | Formal review (SOP-003) |
| G2 | Design freeze | Formal review; parts, BOM and test procedures released (SOP-002, SOP-007) |
| G3 | Verified | Formal review of build and test results (SOP-006, SOP-007) |
| G4 | Released | Formal review: units released, lessons learned (SOP-007) |

## Scorecard activities (SOP-004 section 8)

`planning`, `requirements`, `design`, `part_selection`, `purchasing`, `documentation`,
`review`, `build`, `test`, `release`. Time entries in `worklog.md` and rows in
`scorecard.csv` use these names.

## Shared columns

| Column | Values | Used in |
|---|---|---|
| `class` | `A` / `B` / `C` | parts.csv, and checks in purchasing and builds |
| `lifecycle` | `draft` / `released` / `obsolete` | parts.csv |
| `result` | `pass` / `fail` / `na` | inspection.csv, test_results.csv |
| `disposition` | `use-as-is` / `rework` / `scrap` / `return` | NC records |
| `status` (supplier) | `approved` / `conditional` / `removed` | suppliers.csv |
| dates | ISO format `YYYY-MM-DD`, the actual date, never backdated | everywhere |
| people | the `id` from `roles.yaml` | everywhere |
| `order_ref` | the organization's own requisition or PO number; the documents stay in its own system | purchases.csv |

## Who produces what for whom

```
SOP-004 plan, requirements, risks ──► SOP-003 reviews check designs against them
SOP-003 review approval ───────────► SOP-004 gate passed
SOP-002 parts.csv (class) ─────────► SOP-005 what to buy · SOP-006 what to inspect and trace
SOP-005 purchases.csv (P-nnnn) ────► SOP-006 inspection and trace.csv
SOP-006 inspection fail ───────────► SOP-008 NC record
SOP-006 built units (serials) ─────► SOP-007 tests and release
SOP-007 unit built wrong ──────────► SOP-008 NC record
SOP-007 design fails test ─────────► SOP-001 design change, retest
SOP-008 corrective action ─────────► SOP-001 ECR, if the design must change
```
