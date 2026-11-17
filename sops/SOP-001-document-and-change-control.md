---
id: SOP-001
title: Document and change control
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead     # a role, see roles.yaml
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-001 Document and change control

Each section has a **Basis** line. *ISO* means the standard requires it (clause given).
*minimalQMS* means it's our choice, which a team using minimalQMS may change.

## 1. Purpose
Make sure everyone works from the current approved version, every change is deliberate
and traceable, and every approval can be proven.
*Basis: ISO §7.5, §8.3.6, §8.5.6*

## 2. Scope
All controlled documents and records in minimalQMS repos. CAD files stay in the CAD tool.
Records in git cite the exact CAD version.
*Basis: ISO §7.5.3. Keeping CAD out of git is a minimalQMS choice.*

## 3. Roles
Procedures name roles. Each repo's `roles.yaml` says who holds each role. One person may
hold several.

| Role | Responsibility |
|---|---|
| **Author** | Drafts or changes a document or design. A human or an agent. |
| **Reviewer** | Checks the content. A human or an independent agent; agent findings are input only. |
| **Approver** | A named human, authorised in `roles.yaml`. |
| **Quality lead** | Owns the QMS. Approves deviations. |

*Basis: ISO §5.3 (assign responsibilities and authorities). Role names and agent roles
are minimalQMS choices.*

## 4. Documents and records
- **Controlled document:** says how to work (SOP, template, requirement, drawing). It's
  changed only through §6.
- **Record:** evidence that something happened. It's never edited after approval.
  Corrections are new records that reference the original.

*Basis: ISO §7.5.3 (records protected from unintended changes)*

## 5. Identification and versions
- Every controlled document's header gives its ID, title, revision (A, B, …) and status
  (draft / released / obsolete).
- **What's on `main` is the released version.** Branches are drafts. Exports are
  uncontrolled unless generated from a tagged release.
- External documents (standards, datasheets, supplier specs) are listed with the version
  used.

*Basis: ISO §7.5.2 (identification, review and approval), §7.5.3 (version control,
external documents)*

## 6. Change procedure
1. **Request.** An ECR says what should change and why. An agent may draft it from a
   conversation, and the author confirms it.
2. **Change.** Made on a branch, scoped to one ECR. Commits use the `AGENTS.md` format.
3. **Check.** CI runs. A failed check blocks the change unless a deviation is approved (§9).
4. **Review.** Small changes: a PR review. Design changes and phase gates: a formal review
   (SOP-003).
5. **Approve.** An explicit approval that meets §7.
6. **Merge.** A human merges. **Agents never merge.** The ECR is closed with a link to the change.
7. **Release.** A human tags product and QMS releases.

Update everything that cites a changed item in the same change.

*Basis: ISO §8.3.6 and §8.5.6 (changes reviewed and authorised, with records of who
authorised them and the actions taken). ECR/ECO terms, git mechanics and "agents never
merge" are minimalQMS choices.*

## 7. What an approval must prove
An approval is valid only if the record shows:

| Element | Example |
|---|---|
| **Who**, a named person authorised in `roles.yaml` | A. Engineer, approver |
| **What** exactly, by ID and revision | PCB-0001 rev B; DR-004 |
| **The decision** | Approved / rejected / approved with actions |
| **When** | Actual date and time. Never backdated. |
| **Evidence**, kept unaltered | A PR approval, or the human's reply in an archived transcript, quoted and located in the minutes |

A reply counts as approval only when it answers a question that names exactly what's
being approved. Casual replies during work are working decisions, not approvals. Agents
never approve. No handwritten or digital signature is needed.

*Basis: ISO §8.5.6 and §8.6 (traceability to the person authorising). ISO doesn't require
signatures; electronic approval is accepted (APG guidance on documented information). The
explicit-question rule is a minimalQMS choice.*

## 8. When one person holds several roles
- **Internal audit** is done by someone other than the person whose work is audited.
  In a one-person organisation, that means an outside person.
  *Basis: ISO §9.2.2 (objectivity and impartiality)*
- When the author also approves, a **fresh agent session** with no memory of the work
  reviews it first, and the human records a decision on each finding. Approving after a
  break (ideally the next day) is recommended.
  *Basis: minimalQMS choice. ISO doesn't require reviewers independent of the author.*

## 9. Deviations
If a procedure can't be followed, write a deviation record (template) with the reason,
scope, affected items and compensating actions. The quality lead approves it **before**
the work is released. Capturing records after the fact is always a deviation.
*Basis: ISO §8.6 (release before planned arrangements are complete needs authorisation),
§8.7. The deviation record itself is a minimalQMS choice.*

## 10. Retention
Records are kept in git for the life of the product plus at least 3 years. They're never
deleted, and `main` is never force-pushed. Formal-review transcripts are archived unaltered
next to their minutes.
*Basis: ISO §7.5.3 requires deciding retention and protecting records. The period is a
minimalQMS choice; customer or legal requirements may need longer.*
