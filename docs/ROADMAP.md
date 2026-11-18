# Roadmap to QMS-rev A

QMS-rev A is the first release of minimalQMS: enough to run photoreactor iteration 2 under
control from its first design review. **Deadline: before iteration 2's first design review.**

Until it's tagged, minimalQMS is built with lightweight branches and PRs (see AGENTS.md).

## Planned steps

One SOP per PR. Status: ✅ merged · 🔄 open · ⬜ not started

| Step | Contents | GitHub PR | Status |
|---|---|---|---|
| 1 | README thesis, rationale, original brief | #1 | ✅ |
| 2 | MIT license, `AGENTS.md` hard rules, `CLAUDE.md` pointer, line endings | #2 | ✅ |
| 3 | Showcase origin story, retroactive capture of iteration 1, this roadmap, review and coworking model | #3 | ✅ |
| – | Rename to minimalQMS | #5 | 🔄 |
| 4 | **SOP-001 Document and change control:** approval by outcome (who, what, decision, when, evidence), roles (`roles.yaml`), one-person safeguards, deviations. ECR, ECO, deviation and roles templates. ISO 9001 requirements map and sources. Agents never merge. | #4 | 🔄 |
| 5 | **SOP-002 Part numbering, revisions and part classes:** `CCC-NNNN` parts and `CCC-A-NNNN` assemblies, separate revision letters, interchangeability rule, lifecycle states, A/B/C classes, serial numbers. `parts.csv`, `bom.csv` and `part-categories.csv` templates. | #6 | 🔄 |
| – | Interfaces: shared names, IDs, product repo layout, data flow ([INTERFACES.md](INTERFACES.md)) and this index | #13 | 🔄 |
| 6 | **SOP-003 Design review:** check-ins vs. working decisions vs. formal reviews; package, minutes and work log templates | #7 | 🔄 |
| 7 | **SOP-004 Design and development planning:** gates G0–G5, `plan.yaml`, `gates.yaml`, `requirements.yaml`, `risks.csv` | #8 | 🔄 |
| 8 | **SOP-005 Purchasing and suppliers:** barebones `purchases.csv` referring to the organisation's own requisitions and POs; `suppliers.csv` with a one-line basis | #9 | 🔄 |
| 8a | **SOP-006 Incoming inspection and build records:** inspection by class, `build.yaml`, `trace.csv` | #10 | 🔄 |
| 8b | **SOP-007 Test and release:** test procedures, equipment and calibration, results, `release.yaml` | #11 | 🔄 |
| 8c | **SOP-008 Nonconformance and corrective action** | #12 | 🔄 |
| ⏸ | **SOP-009 Management layer** (scope, policy, objectives, internal audit, management review, training): held until real data exists | | ⬜ |
| 9 | **CI checks:** BOM/parts lint, commit-message lint, `plan.yaml` / `gates.yaml` validation, approval-quote check, the `trace` script | | ⬜ |
| 10 | **Copier product template:** product repo structure wired to the CI checks and `AGENTS.md`, recording which QMS rev it's built under | | ⬜ |
| 11 | **Dry run and release:** generate a throwaway product, fix what breaks, write a CHANGELOG, tag `QMS-rev-A` | | ⬜ |

**If iteration 2 starts early:** ship the SOPs and templates (steps 4–8c) first, tag them as
QMS-rev A, and add the CI checks and Copier template (steps 9–10) as QMS-rev B during
iteration 2. Iteration 2's repo can be set up by hand from the templates in the meantime.

## After rev A (each written just before it's needed)

- **Document rendering:** PDF/Word output of controlled documents with approval blocks.
  Needed before a non-technical user or an auditor gets involved.
- **Management layer:** scope, quality policy, objectives, risk register, calibration,
  training, internal audit, management review. Written once real data exists.
