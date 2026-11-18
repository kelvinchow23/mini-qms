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
organization's ordering process is outside this procedure. Requisitions, POs, approvals
and invoices remain in the organization's own systems; the product repo keeps a list that
refers to them.
*Basis: minimalQMS choice*

## 3. Suppliers
`suppliers.csv` lists each supplier with a status (`approved`, `conditional` or
`removed`), a date, and a basis chosen from:

| Basis | Meaning |
|---|---|
| `authorized-distributor` | Authorized distributor for the manufacturer (e.g. Mouser, Digi-Key) |
| `manufacturer-direct` | Bought from the manufacturer or its own store |
| `established-supplier` | Widely used industrial supplier with published specifications (e.g. McMaster-Carr) |
| `prior-good-results` | Used before without nonconformances |
| `sole-source` | Only available source for the item |
| `trial` | First order; status `conditional` until incoming inspection passes |

- Add a supplier before its first order. A supplier added after the fact requires a
  deviation (SOP-001 section 9).
- Review the supplier's status when the supplier causes a nonconformance (SOP-008).

*Basis: ISO §8.4.1*

## 4. Purchase list
Record each item ordered as one line in `purchases.csv`:
- line ID (`P-nnnn`), PN, description, quantity, supplier and link to the item;
- `order_ref`: the organization's requisition or PO number;
- order date; on receipt, received date, quantity and supplier lot or job number;
- inspection result for Class A lines (SOP-006).

Order only PNs that are `released` in `parts.csv` (SOP-002). Prototype parts for design
work are the exception; mark them `proto` in `notes`. Prototype parts must not be used in
a released build.
*Basis: ISO §8.4.3, §8.5.2. Referring to external records instead of copying them is a
minimalQMS choice.*

## 5. Ordering for a build
1. Generate the purchasing upload files with the part library's `requisition.py`, from
   `bom.csv` and the build quantity. It produces one file per supplier in the purchasing
   system's upload format, less stock on hand.
2. Check the files, then upload them to the organization's purchasing system.
3. Record each placed order with the part library's `record_order.py`. It adds the
   `purchases.csv` lines and stores the uploaded file in `purchasing/requisitions/`.

*Basis: minimalQMS choice*

## 6. Records
`purchases.csv`, `suppliers.csv` and the uploaded files in `purchasing/requisitions/` are
controlled under SOP-001. The organization keeps
the documents behind each `order_ref` for the same retention period, and retrieves them
by reference when required.
*Basis: ISO §7.5.3*

## Appendices
Appendices are forms and templates that belong to this SOP. They carry the SOP's revision
and change only through a revision of this SOP.

| ID | Title | File | Used in product repos as |
|---|---|---|---|
| SOP-005-A01 | Purchase list | [SOP-005-A01-purchases.csv](SOP-005-A01-purchases.csv) | `purchasing/purchases.csv` |
| SOP-005-A02 | Supplier list | [SOP-005-A02-suppliers.csv](SOP-005-A02-suppliers.csv) | `purchasing/suppliers.csv` |
