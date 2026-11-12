# miniQMS

A lean, ISO 9001-style quality management system for hardware that a very small
team, even one person, can actually run. AI agents do the design legwork and the
clerical work. Humans make every decision.

## Why this exists

Developing physical products under a quality system usually involves a lot of red
tape: document control, approval chases, purchasing paperwork, traceability records
and audit preparation. In a traditional organisation, much of the headcount around a
product exists only to keep that machinery running.

miniQMS tests a different claim:

> A small team can develop hardware with **controlled, traceable, auditable**
> engineering, without the admin overhead, by treating hardware a bit more like
> software and letting agents assist with both the design and the record-keeping.

This isn't about "AI built a product". It's about showing that agent-assisted
hardware development can stay under real control: every change is traceable, every
review is minuted, and humans sign off every step.

It's meant to be reused. The structure is generic, so other people can build their
own products on it.

## Design principles

### Hardware treated like software
- **Git is the PLM.** An issue is a change request (ECR), a PR is the change order (ECO),
  and a human merge is the approval. Releases are tags.
- **Part lifecycle lives in git.** `parts.csv` is the part master. Each part has a part
  number, revision and lifecycle state (draft → released → obsolete). A state or revision
  changes only through a reviewed PR.
- **CI does the policing.** BOM lint, commit-message lint and traceability checks run on
  every PR, so nobody checks them by hand.
- **Nobody has to learn git.** Engineers work by talking to an agent and reviewing on
  GitHub. The agent runs the git commands.

### Design source of truth
- **CAD owns the design. Git owns the release record.** The MCAD tool (Fusion 360 today,
  Onshape possibly later) is the source of truth for the mechanical BOM structure. KiCad is
  the source of truth for the PCB BOM.
- On release, the BOMs are **exported** from CAD into git, together with the CAD version
  identifiers they came from. They're joined with the part master (class, supplier, cost),
  and the snapshot is frozen by a tag.
- CI checks that the exported BOM and the part master agree, so CAD and git can't silently
  drift apart.
- CAD tools are connected through small adapters, so switching from Fusion to Onshape
  doesn't change the process.

### Design review by conversation
Design work, including PCB layout and MCAD, is largely done by agents, steered by a
human through chat. That chat is the design review, so it needs to produce proper records:

1. The review happens as a conversation with the agent: design intent, changes, checks
   and the **risks discussed**.
2. The agent produces **review minutes** from it: scope, design revision reviewed, items
   checked, risks raised and how each was handled, decisions, and open actions. The raw
   transcript is archived next to the minutes as evidence.
3. A human checks the minutes against the transcript and **signs them off** by approving
   the PR.
4. **Gate:** the next phase can't start until the review minutes are signed off and every
   action is closed or explicitly carried forward.

Agents never sign off. An AI finding is input to the review, and a human records a
decision on every item.

### Only as much process as needed
- **Risk-based traceability.** Critical parts (Class A) are traced to a specific order
  and inspected. Bulk hardware (Class B) is traced to its batch PO. Consumables (Class C)
  aren't traced.
- **No SOP before its process.** Each procedure is about one page and is written just
  before it's first needed. A minimum viable 9001 QMS is about 6–8 short SOPs plus records.

## Why git?

Git has known problems as a QMS, especially for non-technical people. miniQMS uses git
as the **database**, not the interface: people work through agents and readable
generated documents. See [docs/RATIONALE.md](docs/RATIONALE.md), which answers the main
critiques point by point.

## Structure

This repo is the **org-level QMS**: SOPs, templates, reusable CI checks and the base
agent instructions. It's versioned by revision (`QMS-rev A`, …).

Each product lives in its own repo, generated from a **Copier** template here. Running
`copier update` brings SOP and template changes into existing products as a reviewable PR,
and each product records which QMS revision it was built under.

## First showcase: the photoreactor

The first product run through miniQMS is the photoreactor
([`kelvinchow23/photo-reactor`](https://github.com/kelvinchow23/photo-reactor)).

### How it started

The photoreactor wasn't planned as a QMS showcase. It started as a design-sharing repo,
and the first iteration was built almost entirely by agents:

- **The PCB and the housing were designed by agents.** No human worked in KiCad or did
  the CAD modelling directly. The human coached the agents through chat: stating intent,
  questioning choices, asking for changes and checking the results.
- **That coaching worked like a live design review:** intent, risks, changes and checks,
  discussed in conversation. That's where miniQMS's "design review by conversation" comes from.
- **Then the agents picked the parts.** At that point, the obvious question was: if agents
  can design it and source it, why not run the *whole* process with agents, under real
  control? miniQMS is the answer to that question.

### Iteration 1: captured after the fact, not backdated

Iteration 1 (build B001) was designed and its parts were bought **before miniQMS
existed**. Real projects often look like this: the prototype comes first and the quality
system arrives later. miniQMS handles it openly instead of rewriting history:

- **The pre-QMS state is frozen as it was.** The photoreactor repo is tagged
  `baseline-pre-QMS` without rewriting any git history.
- **Every record shows the date it was actually created.** Purchases are captured from the
  real order confirmations and invoices, with a deviation note explaining they're
  retroactive. Supplier approval is recorded as retroactive too. Incoming inspection is
  done now, on the parts as they are.
- **Missing reviews aren't presented as if they happened.** The design chats that exist
  are archived as evidence. A formal design review of the iteration 1 baseline is held
  under SOP-003 and dated when it actually happens.
- **ISO 9001 doesn't require history from before the QMS existed.** What it requires is
  that work is controlled from adoption onward, and that a design is verified before
  release. The retroactive capture is recorded as a deviation, so an auditor can see
  exactly where control began.

### Iteration 2: the first fully controlled run

The second iteration is the first one run under miniQMS from the start. Its design-review
chats are minuted and signed off as they happen, its parts are bought under the purchasing
process, and every unit is traced from order to sign-off.

Comparing the two iterations is part of the showcase: the same product and the same small
team, first without control, then with it.

### It's done when

- An iteration 2 unit is released, and `trace <serial>` resolves every part to its vendor,
  order, date, cost and inspection result.
- Iteration 1 is fully captured, with its deviation notes, and no backdated records.
- An outside person runs a mock audit with no major findings.
- There's an honest write-up of what the agents did well and badly, including where they
  were wrong.

## Status

QMS-rev A skeleton: not started. See [docs/HANDOFF.md](docs/HANDOFF.md) for the original brief.

Until QMS-rev A is tagged, miniQMS is developed with lightweight branches and PRs (no ECRs).
After the tag, changes to miniQMS itself follow miniQMS's own change control.

## Open questions

- **Interface for non-technical engineering teams.** What app or GUI lets a typical
  engineering team use this without seeing git? Options to explore: a simple web front
  end over the repo, GitHub Projects, or Cowork or another agent as the main interface.
