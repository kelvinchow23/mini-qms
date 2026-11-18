# Interfaces: shared names across the SOPs

The SOPs pass records to each other. This file fixes the names they share, so every
SOP, template, CI check and agent uses the same ones. **If a SOP needs a new shared name,
add it here first.**

## Product repo layout

```
roles.yaml                      SOP-001  who holds which role
worklog.md                      SOP-003  check-ins and notable working decisions
00_planning/
  plan.yaml                     SOP-004  phase gates: target and actual dates
  gates.yaml                    SOP-004  what each gate requires
01_requirements/
  requirements.yaml             SOP-004  REQ-nnn with verification method
  risks.csv                     SOP-004  RISK-nnn (lightweight FMEA)
02_design/
  reviews/DR-nnn/               SOP-003  package, minutes, transcript, visuals
03_release/
  parts.csv, bom.csv            SOP-002
  part-categories.csv           SOP-002
  test_procedures/TP-nnn.md     SOP-007
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
equipment/equipment.csv         SOP-007  test equipment and calibration due dates
nonconformance/NC-nnn.md        SOP-008
deviations/DEV-nnn.md           SOP-001
```

## IDs

| ID | Meaning | Defined in | Example |
|---|---|---|---|
| `CCC-NNNN` + rev | Part or assembly | SOP-002 | `PCB-0001` rev `B` |
| `SNnnn` | Unit serial number | SOP-002 | `SN001` |
| ECR `#n` | Change request (an issue) | SOP-001 | `ECR #12` |
| `DEV-nnn` | Deviation | SOP-001 | `DEV-001` |
| `DR-nnn` | Formal design review | SOP-003 | `DR-004` |
| `A-nnn` | Action from a review | SOP-003 | `A-012` |
| `G0`–`G5` | Phase gates | SOP-004 | `G3` |
| `REQ-nnn` | Requirement | SOP-004 | `REQ-007` |
| `RISK-nnn` | Risk (FMEA line) | SOP-004 | `RISK-003` |
| `P-nnnn` | Purchase line | SOP-005 | `P-0042` |
| `B00n` | Build | SOP-006 | `B002` |
| `TP-nnn` | Test procedure | SOP-007 | `TP-001` |
| `EQ-nnn` | Test or measuring equipment | SOP-007 | `EQ-003` |
| `NC-nnn` | Nonconformance | SOP-008 | `NC-005` |

IDs are never reused. Numbers are zero-padded so they sort correctly.

## Phase gates (SOP-004)

| Gate | Name | Passed by |
|---|---|---|
| G0 | Scope | Approval of the plan |
| G1 | Requirements frozen | Formal review (SOP-003) |
| G2 | Design complete | Formal review (SOP-003) |
| G3 | Released for build | Formal review, plus parts and BOM released (SOP-002) |
| G4 | Built and verified | Every unit released or dispositioned (SOP-007, SOP-008) |
| G5 | Close-out | Lessons learned, including where AI was wrong |

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
| `order_ref` | the organisation's own requisition or PO number; the documents stay in its own system | purchases.csv |

## Who produces what for whom

```
SOP-004 plan, requirements, risks ──► SOP-003 reviews check designs against them
SOP-003 review approval ───────────► SOP-004 gate passed
SOP-002 parts.csv (class) ─────────► SOP-005 what to buy · SOP-006 what to inspect and trace
SOP-005 purchases.csv (P-nnnn) ────► SOP-006 inspection and trace.csv
SOP-006 inspection fail ───────────► SOP-008 NC record
SOP-006 built units (SNnnn) ───────► SOP-007 tests and release
SOP-007 test fail ─────────────────► SOP-008 NC record
SOP-008 corrective action ─────────► SOP-001 ECR, if the design must change
```
