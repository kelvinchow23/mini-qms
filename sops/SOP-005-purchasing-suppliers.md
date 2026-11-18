---
id: SOP-005
title: Purchasing and suppliers
rev: A
status: draft          # draft until released with QMS-rev A
owner: Quality lead
standard: ISO 9001:2026 # clause refs not yet checked against the purchased text
---

# SOP-005 Purchasing and suppliers

Each section has a **Basis** line: *ISO §x.y* (required) or *minimalQMS choice*.

## 1. Purpose
Buy the right parts from suitable suppliers, and be able to trace what was bought, with
as little paperwork as possible.
*Basis: ISO §8.4 (control of externally provided products and services)*

## 2. Scope
Everything bought for a product: parts, PCBs, printing or machining services. **How the
organisation places orders isn't covered.** Requisitions, POs, approvals and invoices stay
in the organisation's own systems. The product repo only keeps a list that refers to
them.
*Basis: minimalQMS choice. Keeps private commercial records out of public repos.*

## 3. Suppliers
`suppliers.csv` lists each supplier with a status (`approved`, `conditional`,
`removed`), the date and a **one-line basis**, for example "authorised distributor",
"used before with good results" or "only source for this part".
- Add a supplier before its first order. If that wasn't done, record it after the fact
  under a deviation (SOP-001 §9).
- If a supplier causes a nonconformance (SOP-008), review its status and note why.

*Basis: ISO §8.4.1 (criteria for evaluating, selecting, monitoring and re-evaluating
suppliers; records retained). The one-line basis is the minimum that meets it.*

## 4. Purchase list
Each item ordered gets a line in `purchases.csv`:
- a line ID (`P-nnnn`), PN, description, quantity, supplier and **link to the item**;
- **`order_ref`:** the organisation's own requisition or PO number. That's the pointer to
  the real paper trail;
- order date and, on arrival, received date, quantity and supplier lot or job number;
- the inspection result for Class A lines (SOP-006).

Order only PNs that are `released` in `parts.csv` (SOP-002). Prototype parts for design
work are the exception: mark them `proto` in `notes`; they can't go into a released build.
Prices are optional and not included by default.
*Basis: ISO §8.4.3 (communicate requirements to suppliers: the PN, MPN and link fix
what's bought), §8.5.2 (traceability for Class A and B). Referencing external records
instead of copying them is a minimalQMS choice.*

## 5. Making the cart
For a build, an agent can create the shopping list from `bom.csv` × quantity, grouped by
supplier, minus bulk stock on hand. The human places the order in the organisation's
system and gives the agent the order reference.
*Basis: minimalQMS choice*

## 6. Records
`purchases.csv` and `suppliers.csv` in the product repo, kept under SOP-001.
The documents behind each `order_ref` are kept by the organisation for the same retention
period. An auditor asks for them by reference.
*Basis: ISO §7.5.3 (records can be held in any system, as long as they can be retrieved)*
