# miniQMS

A lean, ISO 9001-style quality management system that a very small team — even one
person — can actually run, with AI agents doing the clerical work and humans making
every decision.

## Why this exists

Developing physical products under a quality system is usually assumed to need a
quality team, document controllers, a purchasing department and a PLM system:
easily 10× the people who do the engineering. Most of that headcount goes to
paperwork: keeping documents in sync, chasing approvals, tracing parts and assembling
records for an auditor.

miniQMS tests a different claim:

> A one- or two-person team can develop hardware with **auditable, ISO 9001-level
> control** — full traceability, change control and design review — without red tape,
> by using git as the PLM and AI agents as the clerks.

The point is **controlled, traceable, AI-assisted development**, not "AI built a
product". Agents draft, check and keep records. Humans approve everything.

## How it stays lean

- **Git is the PLM.** An issue is a change request (ECR); a PR is the change order (ECO);
  a human merge is the approval. Releases are tags.
- **CI does the policing.** BOM lint, commit-message lint and traceability checks run on
  every PR, so nobody has to check them by hand.
- **Risk-based traceability.** Critical parts (Class A) are traced to a specific order
  and inspected. Bulk hardware (Class B) is traced to its batch PO. Consumables (Class C)
  aren't traced.
- **No SOP before its process.** Each procedure is about one page and is written just
  before it's first needed. A minimum viable 9001 QMS is about 6–8 short SOPs plus records.
- **Agents never sign off.** AI reviews are inputs. A human dispositions every finding.

## Structure

This repo is the **org-level QMS**: SOPs, templates, reusable CI checks and the base
agent instructions. It's versioned by revision (`QMS-rev A`, …).

Each product lives in its own repo, generated from a **Copier** template here. Running
`copier update` brings SOP and template changes into existing products as a reviewable PR,
and each product records which QMS revision it was built under.

## First showcase: the photoreactor

The first product run through miniQMS is the photoreactor
([`kelvinchow23/photo-reactor`](https://github.com/kelvinchow23/photo-reactor)):
planning → requirements → design → purchasing → build → test → sign-off.

It's done when:
- SN001 is released.
- `trace SN001` resolves every part to its vendor, order, date, cost and inspection result.
- An outside person runs a mock audit with no major findings.
- There's an honest write-up of what the agents did well and badly.

## Status

QMS-rev A skeleton: not started. See [docs/HANDOFF.md](docs/HANDOFF.md) for the full brief.
