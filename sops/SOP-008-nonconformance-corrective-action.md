---
id: SOP-008
title: Nonconformance and corrective action
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-008 Nonconformance and corrective action

Each section has a **Basis** line: *ISO §x.y* (required) or *minimalQMS choice*.

## 1. Purpose
When something isn't right (a part, a unit, a supplier or our own process), stop it
from being used by mistake, decide what to do with it, and fix the cause when it's worth
fixing.
*Basis: ISO §8.7 (control of nonconforming outputs), §10.2 (nonconformity and corrective
action)*

## 2. Scope
Failed incoming inspections (SOP-006), failed tests (SOP-007), problems found in use or
reported by a customer, supplier problems, and procedures that weren't followed.

## 3. Raise it
Anyone (a human or an agent) who finds a problem opens `nonconformance/NC-nnn.md` from
the template, on the day it's found: what's wrong, which items are affected (PN,
revision, serial numbers, purchase lines), and how it was found. Affected items are
labelled or set aside so they can't be used by mistake.
*Basis: ISO §8.7.1 (identify and control nonconforming outputs; segregate or contain)*

## 4. Decide what to do with the items (disposition)
A human with the authority in `roles.yaml` decides one of:
- **`use-as-is`:** the item is accepted despite the problem, with a reason. If a customer
  is involved, their agreement is recorded.
- **`rework`:** fix it, then re-inspect or re-test.
- **`scrap`:** throw it away.
- **`return`:** send it back to the supplier.

For problems found in units already built, use `trace` to find **every unit containing
the same purchase line** and include them in the NC.
*Basis: ISO §8.7.1 (correction, segregation, return, concession), §8.7.2 (record the
nonconformity, actions, concessions and who decided)*

## 5. Fix the cause (when worth it)
The decider records whether corrective action is needed. Use **one rule of thumb:** it's
needed if the problem could happen again and matter (safety, function, repeated cost).
If it is needed:
1. find the root cause (a few "why?" questions are usually enough),
2. act on the cause. A design or document change goes through an ECR (SOP-001); a
   supplier problem goes through SOP-005 §3,
3. later, check that the action worked, and record it.

If it isn't needed, record the reason in one line. Agents may draft the root-cause analysis;
the human decides whether it's right.
*Basis: ISO §10.2.1 (react, evaluate the need for action, act, review effectiveness),
§10.2.2 (records). The rule of thumb is a minimalQMS choice that keeps small problems
small.*

## 6. Close
An NC is closed when the disposition is done and any corrective action has been checked
as effective. CI blocks gate G4 while any NC affecting the build is open without a
disposition.
*Basis: ISO §8.7.2, §10.2.2*
