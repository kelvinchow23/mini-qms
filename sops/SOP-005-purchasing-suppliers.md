---
id: SOP-005
title: Purchasing and suppliers
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-005 Purchasing and suppliers

Each section ends with its basis: *ISO §x.y* (required by the standard) or *minimalQMS
choice* (may be changed by teams using minimalQMS).

## 1. Purpose
To buy the correct items from suitable suppliers and to keep a traceable record of each
purchase.
*Basis: ISO §8.4*

## 2. Scope
All items and services bought for a product: parts, PCBs, printing and machining. The
organisation's ordering process is outside this procedure. Requisitions, POs, approvals
and invoices remain in the organisation's own systems; the product repo keeps a list that
refers to them.
*Basis: minimalQMS choice*

## 3. Suppliers
`suppliers.csv` lists each supplier with a status (`approved`, `conditional` or
`removed`), a date, and a one-line basis (e.g. "authorised distributor", "used previously
with good results", "sole source").
- Add a supplier before its first order. A supplier added after the fact requires a
  deviation (SOP-001 section 9).
- Review the supplier's status when the supplier causes a nonconformance (SOP-008).

*Basis: ISO §8.4.1*

## 4. Purchase list
Record each item ordered as one line in `purchases.csv`:
- line ID (`P-nnnn`), PN, description, quantity, supplier and link to the item;
- `order_ref`: the organisation's requisition or PO number;
- order date; on receipt, received date, quantity and supplier lot or job number;
- inspection result for Class A lines (SOP-006).

Order only PNs that are `released` in `parts.csv` (SOP-002). Prototype parts for design
work are the exception; mark them `proto` in `notes`. Prototype parts must not be used in
a released build. Prices are optional.
*Basis: ISO §8.4.3, §8.5.2. Referring to external records instead of copying them is a
minimalQMS choice.*

## 5. Order list for a build
An agent may generate the order list from `bom.csv` and the build quantity, grouped by
supplier and less bulk stock on hand. The buyer places the order in the organisation's
system and records the order reference.
*Basis: minimalQMS choice*

## 6. Records
`purchases.csv` and `suppliers.csv` are controlled under SOP-001. The organisation keeps
the documents behind each `order_ref` for the same retention period, and retrieves them
by reference when required.
*Basis: ISO §7.5.3*
