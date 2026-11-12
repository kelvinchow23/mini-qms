# AGENTS.md

Instructions for any AI agent (Claude Code, Codex, Cowork, …) working in this repo.
`CLAUDE.md` just imports this file. Keep all agent instructions here, not in
vendor-specific files.

## What this repo is

miniQMS is a lean, ISO 9001-style QMS for small hardware teams. This repo is the
**org-level QMS**: SOPs, templates, reusable CI checks and the Copier template that
generates product repos. Read [README.md](README.md) for the thesis and
[docs/RATIONALE.md](docs/RATIONALE.md) for the design reasoning.

Layout (planned items are created as their PRs land):

```
AGENTS.md / CLAUDE.md   agent instructions (this file)
docs/                   rationale, original brief, design notes
sops/                   SOP-001, SOP-002, ...           (planned)
templates/              ECR, PR/ECO, review minutes      (planned)
.github/                issue/PR templates, reusable CI  (planned)
product-template/       Copier template for product repos (planned)
```

## Current mode: bootstrap (before QMS-rev A)

miniQMS hasn't been released yet, so it doesn't control its own changes yet.
- Work on a branch, one chunk of work per PR. No ECR issues needed.
- Branch names: `docs/...`, `sop/...`, `ci/...`, `template/...`, `chore/...`.
- Commit format: `[DOC-ID] summary` (for example `[SOP-001] add approval rules`), or
  `[QMS] summary` for repo-wide changes.

After `QMS-rev-A` is tagged, this repo follows its own SOP-001: every change needs an
ECR issue, and every commit references it (`(ECR #n)`).

## Hard rules (apply in every miniQMS repo)

1. **Never commit to `main`.** Always use a branch and a PR.
2. **Never approve, merge or sign off anything.** Never mark a record approved,
   released or signed. Approval is a human action. You may *prepare* a PR for approval.
3. **Never backdate a record.** Use the real date. When capturing something after the
   fact, say so and add a deviation note.
4. **Never bump a part or document revision without updating everything that cites it**
   (`parts.csv`, BOMs, trace records, document headers).
5. **Every commit names what it changes**, using the commit format above. In product repos:
   `[PN] revX: summary (ECR #n)`.
6. **Run the checks before finishing** (CI checks, once they exist), and report failures
   honestly. Never claim a check passed if you didn't run it.
7. **No secrets in the repo:** no API keys, tokens, passwords or personal data.
8. **AI output is input, not a decision.** When you review a design or summarize a
   discussion, list each finding so a human can accept or reject it. Don't resolve them
   yourself.

## Writing conventions

- **SOPs are short:** about one page each. Write an SOP only for a process that's about to
  be run. Plain language. Each SOP has a document ID, a revision and a "Purpose / Scope /
  Procedure / Records" structure.
- **Tables are data, not Markdown.** Store anything tabular as CSV or YAML, never as a
  Markdown table in a controlled record. (Markdown tables in explanatory docs like the
  README are fine.)
- **Records must make sense without AI:** plain text that a person can read in 20
  years. Don't depend on any tool-specific format.
- **Tool-agnostic.** Don't hard-code one AI vendor, CAD tool or the GitHub UI into
  procedures. Name the role ("the approver", "the MCAD tool") and give the current tool
  as an example.
- **Line endings are LF** (enforced by `.gitattributes`).
