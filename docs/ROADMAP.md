# Roadmap to QMS-rev A

QMS-rev A is the first release of miniQMS: enough to run photoreactor iteration 2 under
control from its first design review. **Deadline: before iteration 2's first design review.**

Until it's tagged, miniQMS is built with lightweight branches and PRs (see AGENTS.md).

## Planned PRs

Status: ✅ merged · 🔄 open · ⬜ not started

| # | Contents | Status |
|---|---|---|
| 1 | README thesis, rationale, original brief | ✅ |
| 2 | MIT license, `AGENTS.md` hard rules, `CLAUDE.md` pointer, line endings | 🔄 |
| 3 | Showcase origin story, retroactive capture of iteration 1, this roadmap | 🔄 |
| 4 | **SOP-001 Document and change control**, plus ECR issue template and PR/ECO template. Defines what counts as an approval. | ⬜ |
| 5 | **SOP-002 Part numbering, revisions and part classes**, plus `parts.csv` / `bom.csv` schema and lifecycle states | ⬜ |
| 6 | **SOP-003 Design review**, plus review-minutes template (risks, decisions, actions, human disposition per item) and transcript archiving | ⬜ |
| 7 | **SOP-004 Design and development planning**, plus `plan.yaml` (phase gates 0–5 with target date, actual date and approver; date changes go through a PR with a reason) | ⬜ |
| 8 | **CI checks:** BOM/parts lint, commit-message lint, `plan.yaml` validation | ⬜ |
| 9 | **Copier product template:** product repo structure wired to the CI checks and `AGENTS.md`, recording which QMS rev it's built under | ⬜ |
| 10 | **Dry run and release:** generate a throwaway product, fix what breaks, write a CHANGELOG, tag `QMS-rev-A` | ⬜ |

**If iteration 2 starts early:** ship the SOPs and templates (PRs 4–7) first, tag them as
QMS-rev A, and add the CI checks and Copier template (PRs 8–9) as QMS-rev B during
iteration 2. Iteration 2's repo can be set up by hand from the templates in the meantime.

## After rev A (each written just before it's needed)

- **Document rendering:** PDF/Word output of controlled documents with approval blocks.
  Needed before a non-technical user or an auditor gets involved.
- **Purchasing and supplier control:** approved supplier list. Needed before iteration 2
  orders parts.
- **Incoming inspection and build records.**
- **Test and release.**
- **Nonconformance and corrective action.**
- **Management layer:** scope, quality policy, objectives, risk register, calibration,
  training, internal audit, management review. Written once real data exists.
