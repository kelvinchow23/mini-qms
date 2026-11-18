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
| 5 | **SOP-002 Part numbering, revisions and part classes:** `CCC-NNNN` part numbers (adapted from gitplm), separate revision letters, interchangeability rule, lifecycle states, A/B/C classes, serial numbers. `parts.csv`, `bom.csv` and `part-categories.csv` templates. | #6 | 🔄 |
| 6 | **SOP-003 Design review**, following [REVIEW-MODEL.md](REVIEW-MODEL.md): check-ins vs. working decisions vs. formal reviews; review-package and minutes templates; transcript archiving | | ⬜ |
| 7 | **SOP-004 Design and development planning:** `plan.yaml` and `gates.yaml` (phase gates 0–5, target and actual dates, approver) | | ⬜ |
| 8 | **SOP-005 Purchasing and suppliers:** a barebones `purchases.csv` (links, plus references to the real requisitions and POs, which stay in the organisation's own systems) and `suppliers.csv` (one-line approval basis). Needed for iteration 2 orders and to capture iteration 1. | | ⬜ |
| 9 | **CI checks:** BOM/parts lint, commit-message lint, `plan.yaml` / `gates.yaml` validation, approval-quote check, the `trace` script | | ⬜ |
| 10 | **Copier product template:** product repo structure wired to the CI checks and `AGENTS.md`, recording which QMS rev it's built under | | ⬜ |
| 11 | **Dry run and release:** generate a throwaway product, fix what breaks, write a CHANGELOG, tag `QMS-rev-A` | | ⬜ |

**If iteration 2 starts early:** ship the SOPs and templates (steps 4–8) first, tag them as
QMS-rev A, and add the CI checks and Copier template (steps 9–10) as QMS-rev B during
iteration 2. Iteration 2's repo can be set up by hand from the templates in the meantime.

## After rev A (each written just before it's needed)

- **Document rendering:** PDF/Word output of controlled documents with approval blocks.
  Needed before a non-technical user or an auditor gets involved.
- **Incoming inspection and build records.**
- **Test and release.**
- **Nonconformance and corrective action.**
- **Management layer:** scope, quality policy, objectives, risk register, calibration,
  training, internal audit, management review. Written once real data exists.
