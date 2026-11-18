---
id: SOP-008
title: Nonconformance and corrective action
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-008 Nonconformance and corrective action

Each section ends with its basis: *ISO §x.y* (required by the standard) or *minimalQMS
choice* (may be changed by teams using minimalQMS).

## 1. Purpose
To prevent unintended use of nonconforming items, to decide what to do with them, and to
remove the cause where this is justified.
*Basis: ISO §8.7, §10.2*

## 2. Scope
Failed incoming inspections (SOP-006), failed tests (SOP-007), problems found in use or
reported by customers, supplier problems, and procedures not followed.

## 3. Raising an NC
Anyone, human or agent, who finds a nonconformity opens `nonconformance/NC-nnn.md` from the
template on the day it is found. The NC states what is wrong, how it was found, and the
affected items (PN, revision, serial numbers, purchase lines). Label or segregate the
affected items to prevent their use.
*Basis: ISO §8.7.1*

## 4. Disposition
The NC approver (`roles.yaml`) decides one disposition:
- **`use-as-is`:** accepted with a stated reason. Customer agreement is recorded where
  the customer is affected.
- **`rework`:** corrected, then re-inspected or re-tested.
- **`scrap`:** discarded.
- **`return`:** returned to the supplier.

For built units, use the trace records to find every unit containing the same purchase
line, and add them to the NC.
*Basis: ISO §8.7.1, §8.7.2*

## 5. Corrective action
The NC approver decides whether corrective action is required and records the reason. It
is required when the nonconformity could recur and affect safety, function or cost. When
required:
1. Determine the root cause. An agent may draft it; the NC approver accepts or rejects it.
2. Act on the cause: an ECR for design or document changes (SOP-001), or a supplier review
   for supplier causes (SOP-005 section 3).
3. Verify that the action was effective and record the evidence.

*Basis: ISO §10.2.1, §10.2.2*

## 6. Closure
Close the NC when the disposition is complete and any corrective action is verified as
effective. CI blocks gate G4 while any NC affecting the build has no disposition.
*Basis: ISO §8.7.2, §10.2.2*
