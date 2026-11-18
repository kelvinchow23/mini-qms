---
id: SOP-003
title: Design review
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-003 Design review

Each section ends with its basis: *ISO §x.y* (required by the standard) or *minimalQMS
choice* (may be changed by teams using minimalQMS). Background: `docs/REVIEW-MODEL.md`.

## 1. Purpose
To verify that a design meets its requirements and controls its risks, to record the
decisions, and to give the approver an informed yes or no.
*Basis: ISO §8.3.4*

## 2. Scope
Formal reviews at gates G1–G3 (SOP-004) and for design changes that require formal review
(SOP-001), plus check-ins between reviews.

## 3. Types of interaction

| Type | Purpose | Record | Approval |
|---|---|---|---|
| **Check-in** | Report what changed, who changed it and what is next | `worklog.md` | No |
| **Working decision** | Direct the work | `worklog.md` when significant; included in the next review package | No |
| **Formal review** | Approve a set of changes or pass a gate | `02_design/reviews/DR-nnn/` | Yes |

Only a formal review approves.
*Basis: minimalQMS choice*

## 4. Review package
The author, usually an agent, prepares `DR-nnn/package.md` from the template. The package
contains:
- **Scope:** items and revisions reviewed (from → to), CAD versions, ECRs and gate.
- **Change groups:** for each group, what changed and why, who made the change (human,
  agent, or agent directed by a human), links to the files, visuals where useful
  (before/after renders, annotated screenshots, PCB layer images), and the requirements
  and risks affected.
- **Independent findings:** from a fresh agent session with no memory of the design work.
- **Open items:** carried-over actions and known gaps.

*Basis: ISO §8.3.4. The package format and independent agent review are a minimalQMS
choice (SOP-001 section 8).*

## 5. Walkthrough
1. The agent presents each change group in turn. The approver questions and challenges it.
2. The approver gives each group a disposition: accept, reject (with reason), or accept
   with action (`A-nnn`, with an owner).
3. The approver accepts or rejects each independent finding, with a reason for rejection.
4. The agent asks one question that names exactly what is being approved, e.g. *"Approve
   DR-004: PCB-0001 rev B, 5 groups accepted, 1 with action A-012?"*
5. The approver answers yes or no. The answer is the approval (SOP-001 section 7).

Conduct the review in an agent tool that saves the session transcript.
*Basis: ISO §8.3.4, §8.3.6. The walkthrough format is a minimalQMS choice.*

## 6. Records
`DR-nnn/` contains:
- `package.md` as reviewed, with its visuals;
- `minutes.md`, generated from the template, with participants (humans, and agents with
  their models), the disposition of every group and finding, actions, and the decision,
  with the approval quoted and its location in the transcript;
- `transcript.*`, the unaltered session transcript.

The minutes are merged by a human through a PR (SOP-001). An action remains open until it
is closed with evidence or carried forward at the next gate.
*Basis: ISO §8.3.4, §8.3.6. Transcript archiving is a minimalQMS choice.*

## 7. Check-ins
The agent adds a short entry to `worklog.md` after each work session, or more often when
useful: what changed and who changed it, what is next, what is blocked, and items for the
next review. No reply is required.
*Basis: minimalQMS choice. Supports ISO §7.1.6.*
