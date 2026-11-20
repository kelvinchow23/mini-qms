# minimalQMS

A lean, ISO 9001-style quality management system for hardware, run with AI agents and
decided by humans. It works for a team of one.

minimalQMS gives hardware development a backbone: requirements, design reviews, controlled
changes, traceable parts and builds, and lessons learned. Agents do the legwork and the
record-keeping. Humans make every decision.

## Why minimalQMS

### Less bureaucracy, more design intent

Running product development under a quality system brings a lot of supporting work:
document control, approvals, purchasing paperwork, traceability records and audit
preparation. Some of it is necessary. Much of it is inefficient bureaucracy that takes
time away from the design itself.

minimalQMS lets designers spend that time on design intent:
- **Design with agents.** Agents work on the CAD, the PCB and the parts selection alongside
  you. You set the intent, steer the work, review and approve.
- **Agents automate the admin.** Change requests, review packages, minutes, purchase lists
  and build records are drafted for you.
- **Cross-referencing is automatic.** Checks that used to mean comparing documents by hand
  (BOMs against part lists, part numbers, revisions, purchase records, traceability) run on
  every change, and problems are flagged before anything is released.
- **A streamlined process based on ISO 9001.** Eight one-page procedures
  ([how they map to the standard](docs/ISO9001-MAP.md)).

### Formalizing informal design projects

Many projects run without a formal process: personal builds, research prototypes,
open-source hardware, and early prototypes in any organization. They focus on the design
itself: build, try, fix, repeat. That works until a design has to be repeated, handed over,
shared or trusted.

Informal projects also move much faster than a formal process allows, and that speed is
worth keeping. More and more developers design by chatting with an AI agent, and
minimalQMS formalizes those casual chats without slowing them down. Start a project from
this repository and its companions, and it follows the intent of the standards
(controlled, traceable designs) without anyone formally knowing they are doing it. The
agent asks the questions and runs the checks that improve a design, at the moment they
matter, and turns the answers into records:

> **After a change:** "You moved the mounting holes. The lid from the last build won't fit
> any more. Is this a new revision, or a new part?"
>
> **After testing:** "Two of three units ran hotter than the others. Is that a problem
> with those parts, or with the design?"

The result is fewer surprises, designs that others can rebuild, a clear history to share,
and a project that improves from one iteration to the next.

## How it works

### Development is a cycle

![Development cycle](docs/img/development-cycle.png)

Each iteration passes six gates, from scope to close-out, starting from the last released
revision. Lessons learned, problems found and feedback become the change requests for the
next iteration. Small fixes between iterations skip the gates. See the
[SOP overview](sops/README.md).

### Coworkable, not fully agentic
Humans and agents work on the **same** design. Either can change the CAD or the PCB, every
change records who made it, and agents never silently overwrite human work.

### Three kinds of interaction, one kind of approval
- **Check-ins** keep the human up to date. No decision is needed.
- **Working decisions** steer the work ("use the 0805 part"). They are captured, not approved.
- **Formal reviews** at gates work like a real review meeting. The agent prepares a package
  (grouped changes, where to look, before/after visuals, affected risks, findings from an
  independent AI reviewer) and walks the human through it. The human answers **yes or no**
  to a question that names exactly what is being approved.

Minutes are generated from the review, and the transcript is archived as evidence. Agents
never approve. See [docs/REVIEW-MODEL.md](docs/REVIEW-MODEL.md).

### Design source of truth
CAD owns the design; git owns the release record. At release, BOMs are exported from the
CAD tools into git with the CAD version they came from, and checked against the part data.

### Only as much process as needed
- **Risk-based traceability.** Critical parts are traced per unit, bulk hardware per
  purchase, consumables not at all.
- **No SOP before its process.** Each procedure is about one page and is written just
  before it is first needed.

## Why git?

Git has known problems as a QMS, especially for people who don't use it. minimalQMS uses git
as the **database**, not the interface: people work through agents and readable documents.
See [docs/RATIONALE.md](docs/RATIONALE.md), which answers the main critiques.

## The minimalQMS family

| Repo | What it holds | Changes |
|---|---|---|
| **minimal-qms** (this repo) | Process: SOPs and appendices, CI checks, product scaffold | Rarely, by revision |
| [**minimal-qms-ots-library**](https://github.com/kelvinchow23/minimal-qms-ots-library) | Off-the-shelf parts, prefix and project codes, purchasing tools, [searchable catalogue](https://kelvinchow23.github.io/minimal-qms-ots-library/) | With every purchase |
| minimal-qms-playbook *(planned)* | Work instructions and agent skills for engineering practice | As practice improves |
| Product repos | Custom parts, BOMs, reviews, builds and records of one product | Continuously |

Each product lives in its own repo, generated from a Copier template in this repo. Each
product records which QMS revision it was built under, and `copier update` offers later
revisions as a reviewable change.

## Showcases

- **Photoreactor:** [kelvinchow23/photo-reactor](https://github.com/kelvinchow23/photo-reactor)

## Status

Building QMS-rev A. See [docs/ROADMAP.md](docs/ROADMAP.md) for the plan.

Until QMS-rev A is tagged, minimalQMS is developed with lightweight branches and PRs.
After the tag, changes to minimalQMS follow its own change control.

## Open questions

- **Guided mode.** Which questions should the agent ask at each gate, and how does it
  adapt them to the project and the person? This is what gives a project without a formal
  process its backbone.
- **Interface beyond git.** What lets a non-technical team use this without seeing git?
  So far: agents as the main interface, readable generated documents, and the OTS
  library's catalogue site.

## Note on ISO 9001

minimalQMS is based on ISO 9001 but is not certified, and using it does not make a project
or organization ISO 9001 certified. Certification is done by an accredited certification
body. minimalQMS does not reproduce text from the standard.

## Licence

[MIT](LICENSE). Use it, fork it, build products on it.
