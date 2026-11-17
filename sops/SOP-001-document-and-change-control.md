---
id: SOP-001
title: Document and change control
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead     # a role, see roles.yaml
---

# SOP-001 Document and change control

## 1. Purpose
Make sure everyone works from the current approved version of each document, every
change is deliberate and traceable, and every approval can be proven. (ISO 9001 §7.5, §8.5.6)

## 2. Scope
All controlled documents and records in miniQMS repos: SOPs, templates, requirements,
design data exported to git, BOMs, part masters, plans, review minutes, purchase, build and
test records. CAD files themselves stay in the CAD tool. The git records cite the exact
CAD version.

## 3. Roles
Roles, not people, are named in procedures. Each repo's `roles.yaml` assigns people to
roles. One person may hold several roles (see §8).

| Role | Responsibility |
|---|---|
| **Author** | Drafts or changes a document or design. Can be a human or an agent. |
| **Reviewer** | Checks the content. Can be a human or an independent agent; agent findings are input only. |
| **Approver** | A named human authorised in `roles.yaml` to approve this type of change. |
| **Quality lead** | Owns this SOP and the QMS overall. Approves deviations. |

## 4. Definitions
- **Controlled document:** tells people how to work (SOP, template, requirement,
  drawing). It's changed only through this procedure.
- **Record:** evidence that something happened (minutes, PO, test result). Once
  approved, it's never edited. Corrections are new records that reference the original.
- **ECR (engineering change request):** a request to change something, with the reason.
- **ECO (engineering change order):** the change itself, made on a branch and proposed as a PR.
- **Deviation:** a recorded, approved departure from a procedure, with its reason and scope.

## 5. Identification and versions
- Every controlled document has an **ID**, a **title**, a **revision** (A, B, C …) and a
  **status** (draft / released / obsolete) in its header.
- **The released version is whatever is on `main`.** Branches are drafts. Anything
  printed or exported is uncontrolled unless it was generated from a tagged release and
  says so.
- Documents from outside (standards, datasheets, supplier specs) are listed with the
  version used in the repo's external-documents list.

## 6. Change procedure
1. **Request.** Open an ECR that says what should change and why. During a live
   design session, an agent can draft the ECR from the conversation, and the author
   confirms it.
2. **Change.** The author makes the change on a branch, scoped to that ECR. Commits use
   the format in `AGENTS.md` and reference the ECR.
3. **Check.** CI runs automatically. A failed check blocks the change unless a deviation
   is approved (see §9).
4. **Review.** Small changes: the approver reviews the PR. Design changes and phase gates:
   a formal review under SOP-003.
5. **Approve.** The approver gives an explicit approval meeting §7.
6. **Merge.** A human merges the PR. **Agents never merge.** The merge releases the
   change, and the ECR is closed with a link to it.
7. **Release.** Product or QMS releases are marked with a tag, created by a human.

Bump the revision of every document or part that changes, and update everything that
cites it in the same change.

## 7. What an approval must prove
An approval is valid only if the record shows all of these:

| Element | Example |
|---|---|
| **Who** approved, by name, authorised in `roles.yaml` | A. Engineer, approver |
| **What** exactly, by ID and revision | PCB-0001 rev B; DR-004 |
| **The decision** | Approved / rejected / approved with actions A-12 |
| **When** | The actual date and time. Never backdated. |
| **Evidence**, kept unaltered | The PR approval, or the human's reply in an archived transcript, quoted and located in the minutes |

A reply counts as approval only when it answers a question that names exactly what's
being approved. Casual replies during working sessions ("ok", "sure, do that") are
working decisions, not approvals. Agents never approve.

## 8. One-person safeguards
When the same person is both author and approver:
- an **independent review** is required: a fresh agent session with no memory of the
  design work, and the human records a decision on every finding;
- formal approvals of human-authored work should come **after a break** (ideally the next
  day), not straight after finishing the work;
- the **internal audit** must be done by someone other than the person whose work is
  audited (an outside person if necessary).

## 9. Deviations
If a procedure can't be followed (for example records captured after the fact, or an
override of a failed CI check), write a deviation record using the template. It must give
the reason, the scope, the affected items and any compensating actions, and the quality
lead must approve it **before** the deviating work is released. Retroactive capture is
always a deviation.

## 10. Records
- Records are kept in git for the life of the product plus at least 3 years.
- They're never deleted or rewritten. Git history is never force-pushed on `main`.
- Formal-review transcripts are archived unaltered next to their minutes.
