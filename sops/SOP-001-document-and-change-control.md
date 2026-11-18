---
id: SOP-001
title: Document and change control
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead     # a role, see roles.yaml
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-001 Document and change control

Each section ends with its basis: *ISO §x.y* (required by the standard) or *minimalQMS
choice* (may be changed by teams using minimalQMS).

## 1. Purpose
To ensure that the current approved version of each document is used, that every change
is deliberate and traceable, and that every approval can be proven.
*Basis: ISO §7.5, §8.3.6, §8.5.6*

## 2. Scope
All controlled documents and records in minimalQMS repos. CAD files remain in the CAD
tool; records in git cite the exact CAD version.
*Basis: ISO §7.5.3. Keeping CAD files out of git is a minimalQMS choice.*

## 3. Roles
Procedures name roles. Each repo's `roles.yaml` assigns people to roles. One person may
hold several roles.

| Role | Responsibility |
|---|---|
| **Author** | Drafts or changes a document or design. A human or an agent. |
| **Reviewer** | Checks content. A human or an independent agent; agent findings are input only. |
| **Approver** | Approves changes. A named human listed in `roles.yaml`. |
| **Quality lead** | Owns the QMS and approves deviations. |

*Basis: ISO §5.3. Role names and agent roles are a minimalQMS choice.*

## 4. Documents and records
A **controlled document** describes how work is done (SOP, template, requirement,
drawing). It changes only through section 6. A **record** is evidence that something
happened. Records are never edited after approval; a correction is a new record that
references the original.
*Basis: ISO §7.5.3*

## 5. Identification and versions
Each controlled document's header states its ID, title, revision (A, B …) and status
(draft, released or obsolete). The version on `main` is the released version; branches
are drafts. Exports are uncontrolled unless generated from a tagged release. External
documents (standards, datasheets, supplier specifications) are listed with the version
used.
*Basis: ISO §7.5.2, §7.5.3*

## 6. Change procedure
1. **Request.** Raise an ECR stating what should change and why. An agent may draft the ECR
   from a conversation; the author confirms it.
2. **Change.** Make the change on a branch, limited to one ECR. Use the commit format in
   `AGENTS.md`.
3. **Check.** CI runs on every change. A failed check blocks the change unless a deviation
   is approved (section 9).
4. **Review.** Small changes: PR review. Design changes and phase gates: formal review
   (SOP-003).
5. **Approve.** The approver gives an explicit approval that meets section 7.
6. **Merge.** A human merges the change. **Agents never merge.** Close the ECR with a link
   to the change.
7. **Release.** A human tags product and QMS releases.

Update everything that cites a changed item in the same change.
*Basis: ISO §8.3.6, §8.5.6. The ECR/ECO terms, git workflow and merge rule are a
minimalQMS choice.*

## 7. Approval evidence
An approval is valid only when the record shows:

| Element | Example |
|---|---|
| **Who:** a named person listed in `roles.yaml` | A. Engineer, approver |
| **What:** the exact items, by ID and revision | PCB-0001 rev B; DR-004 |
| **Decision** | Approved, rejected, or approved with actions |
| **When:** the actual date and time | Never backdated |
| **Evidence**, kept unaltered | A PR approval, or the human's reply quoted from an archived transcript |

A reply counts as approval only when it answers a question that names exactly what is
being approved. Replies during working sessions are working decisions, not approvals.
Agents never approve. Signatures are not required.
*Basis: ISO §8.5.6, §8.6. ISO accepts electronic approval (APG guidance). The
explicit-question rule is a minimalQMS choice.*

## 8. One person in several roles
Internal audit must be done by someone other than the person whose work is audited; in a
one-person organisation, this is an outside person. When the author is also the approver,
a fresh agent session with no memory of the work reviews it first, and the approver
records a decision on each finding. Approval should follow a break, ideally the next day.
*Basis: ISO §9.2.2 for internal audit. The independent agent review is a minimalQMS
choice; ISO does not require reviewers independent of the author.*

## 9. Deviations
When a procedure cannot be followed, record a deviation (`DEV-nnn`) stating the reason,
scope, affected items and compensating actions. The quality lead approves it before the
affected work is released. Records captured after the fact always require a deviation.
*Basis: ISO §8.6, §8.7. The deviation record is a minimalQMS choice.*

## 10. Retention
Records are kept in git for the life of the product plus at least 3 years. Records are
never deleted, and `main` is never force-pushed. Formal-review transcripts are archived
unaltered with their minutes.
*Basis: ISO §7.5.3 requires a defined retention. The period is a minimalQMS choice;
customer or legal requirements may require longer.*
