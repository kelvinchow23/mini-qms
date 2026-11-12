# Why git, and why now

The best-known argument against running a QMS in git is OpenRegulatory's
[*GitHub QMS: We No Longer Recommend It*](https://openregulatory.com/articles/we-no-longer-recommend-github-gitlab-as-qms-software)
(Oliver Eidel, ~2023). It comes from real client experience, and it's right about the
setup it describes. This document explains what miniQMS does differently and what
risks are still open.

Context: OpenRegulatory sells a purpose-built QMS (Formwork) and works mainly with
medical-device companies under ISO 13485. miniQMS targets small, engineering-led
hardware teams under ISO 9001. Those differences matter, but the critique deserves an
answer either way.

## The core shift: git is the database, not the interface

The 2023 critique assumed that people work in git: they edit Markdown, open PRs and
review diffs. In miniQMS, people work through **agents** (Claude Code, Cowork, Codex)
and through **generated documents**:

| Layer | What it is | Who touches it |
|---|---|---|
| Record store | Git: plain text, CSV and YAML. The single source of truth. | Agents and CI, almost never humans |
| Automation | Agents write records and answer questions. CI enforces the rules. | Humans steer them through chat |
| Human interface | Chat, plus rendered PDF/Word documents with number, revision, approval block and history | Everyone, including auditors |

GitHub appears only where an authenticated human approval is needed, and that could
move elsewhere later.

## Problem 1: Markdown tables are impossible to edit

**The critique:** QMS documents end up with large tables (requirements, traceability,
supplier lists). Markdown tables become unusable, and the workarounds (xlsx in git,
Google Sheets, one person who can edit them) are all bad.

**Our answer:**
- **No Markdown tables for records.** Tabular data is stored as CSV or YAML from the start
  (`parts.csv`, `bom.csv`, `requirements.yaml`, `trace_matrix.csv`). CSV opens in any
  spreadsheet program and still produces readable diffs.
- **Agents edit the tables.** "Add REQ-014 with test method T-07" is a sentence, not a
  wide-table editing job. Nobody needs a special editor.
- **Rendered views for reading.** Wide tables are rendered into the PDF or Word output,
  where they're readable, rather than read as source text.

**Still open:** CSV handles long text or line breaks inside cells poorly. Keep long text
in YAML or separate files, and keep tables as data, not prose.

## Problem 2: non-technical people can't use it

**The critique:** this is the main one. When the first non-technical person joins (QA,
regulatory, a consultant), git and Markdown are too much to learn. In practice the
original maintainer becomes their editing assistant, or the company migrates and loses
its history.

**Our answer:** this is what has changed most since 2023. **The editing assistant is now
an agent, and it's available to everyone.** A non-technical person asks in plain
language ("draft an ECR for the new LED supplier", "what changed in rev B and why?",
"give me SOP-003 as a Word document"). The agent does the git work and returns readable
output. Nobody has to learn git.

**Still open:**
- **A new bottleneck:** whoever maintains the agent instructions and CI checks. miniQMS
  aims to package those once so each team doesn't have to rebuild them.
- If the agent interface isn't good enough, a non-technical hire will still struggle.
  This has to be tested with a real non-technical user before claiming it works.
- **Migration:** plain text in git is the *most* portable format, and converting it to
  another system's import format is now cheap agent work. The real lock-in is in
  proprietary eQMS databases.

## Problem 3: review, signing and branch discipline

**The critique:** PR-based approval only works with strict discipline: one document per
PR, merging quickly, no stale branches, and knowing the edit before you discuss it.
Git has no collaborative "suggest" editing like Google Docs, so it ends up as a mess of
branches.

**Our answer:**
- **Agents are good at mechanical discipline.** They keep each PR scoped to one change,
  link it to its ECR and use the right commit format. CI enforces the rest:
  - one ECR per PR
  - flagging PRs open longer than N days
  - no branches without an open PR
- **Discussion happens before editing**, in the ECR issue or in a chat with an agent.
  That chat is minuted (see design review in the README). People discuss in
  conversation, and the agent turns the agreed result into the change.
- **Reviewers comment in plain language.** "Change the torque spec to 0.4 Nm" is enough,
  and the agent applies it to the branch.

**Still open:**
- **Approval must be an authenticated human action.** Today that's a GitHub PR approval.
  Make it one click from a plain-language summary, and define in SOP-001 that this
  approval *is* the document approval.
- **Rubber-stamping risk:** polished agent output is easy to approve without reading.
  The raw transcript is kept next to the minutes, and each item gets a human decision,
  not one blanket approval.

## What this doesn't fix

- **Two places for records.** Design data lives in CAD (Fusion, possibly Onshape later),
  and records live in git. That's the two-headed elephant the article warns about with
  Google Drive. The rule: CAD is a *design source*, not a record store. Every released
  record in git cites the exact CAD version it came from, so an auditor never searches CAD
  for evidence.
- **Agents make confident mistakes.** CI verifies facts mechanically (the BOM line
  exists, the test result file exists, the PO resolves). It never relies on an agent
  saying a check passed.
- **Tool churn.** Agents and models change quickly. Records must make sense without any
  AI: plain files a person could open in 20 years. Agent instructions live in a generic
  `AGENTS.md`, not tied to any one vendor.
- **Regulated medical devices.** ISO 13485 and 21 CFR Part 11 add e-signature and
  software-validation requirements that miniQMS doesn't address. Using it there is out of
  scope until someone does that work.

## How we'll know if this is right

The photoreactor showcase is the test. A git QMS that "works" only for its author has
failed. Before claiming success:
1. An outside person runs a mock audit using only the generated documents and
   chat, without reading the repo directly.
2. A non-technical person completes a real change (ECR → approved ECO) with an agent's
   help, without touching git.
