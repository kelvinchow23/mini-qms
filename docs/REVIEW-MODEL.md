# Review and coworking model

How humans and agents work on a design together, and how decisions get made and recorded.
This is the design intent behind SOP-001 (approvals), SOP-003 (design review) and
SOP-004 (planning). The SOPs state the requirements; this document explains the thinking.

## Principle: coworkable, not fully agentic

miniQMS is built for **humans and agents working on the same design**, not for agents
working alone while a human rubber-stamps the output.

- **Both can change the design.** A human might move a mounting hole in Fusion or reroute
  a trace in KiCad. An agent might do the same through its tools. Neither is the "real"
  designer; both are contributors.
- **Every change has a known author.** Records show whether a change was made by a human,
  an agent, or an agent directed by a human. Review packages show this too.
- **Agents never silently overwrite human work.** If an agent finds a human edit it
  didn't expect (a changed file, a new CAD version), it stops and asks instead of
  reverting or building over it.
- **Say who's working where.** Before an agent starts on an area (for example "housing
  lid"), it says so. Humans do the same in chat. That avoids two people editing the same
  CAD file without knowing it.
- **The human stays informed without being buried.** Short, regular check-ins keep the
  human up to date. Formal reviews happen at a few deliberate points. Routine questions
  don't pile up.

## Three kinds of interaction

Asking for approval on every step causes approval fatigue: the human ends up typing
"yes" without reading. miniQMS separates three kinds of interaction, and only one of
them is an approval.

| | **Check-in** | **Working decision** | **Formal review** |
|---|---|---|---|
| Purpose | Stay informed | Steer the work | Approve a group of changes or pass a gate |
| How often | Whenever useful, e.g. daily or after a work session | As needed while working | At phase gates and before releasing a change (ECO) |
| Who starts it | Agent or human | Either | Agent prepares it; the human runs it |
| Human's answer | None needed, but questions welcome | A direction ("use the 0805 part") | **Yes / no / yes with actions**, for each item and overall |
| Record | One line in the project log | Captured in the work log and the next review package | Review minutes, archived transcript, approval |
| Is it an approval? | No | No | **Yes** |

## Check-ins

A check-in is a short status update, like a colleague stopping by your desk:

- What changed since the last check-in, and who changed it (human or agent).
- What's next.
- Anything blocked or uncertain.
- Anything the agent thinks should come up at the next formal review.

No decision is required. The human can just read it, ask questions or redirect. Check-ins
are logged in one line each so the project history stays readable, but they aren't
review records.

## Formal design review

A formal review should feel like a real review meeting run by a well-prepared colleague,
not like scrolling through a diff.

### 1. The agent prepares a review package

Before the review, the agent puts together a package (generated, not hand-written):

- **Scope:** what's under review, from which revision to which (for example
  `PCB-0001 rev A → rev B`, Fusion version 47 → 52), and which ECRs it covers.
- **Agenda:** the changes grouped the way a person would present them (for example
  "LED thermal path", "connector moved", "BOM substitutions"), not one entry per file.
- **For each change group:**
  - what changed and why, linked to the ECR or requirement
  - who made it: human, agent, or agent directed by a human
  - **where to look:** links to the exact files, drawing sheets or CAD versions
  - **visuals where they help:** before/after renders, annotated screenshots, PCB layer
    comparisons, BOM differences. Physical changes should be *seen*, not just described.
  - affected requirements and risks (requirement IDs, FMEA lines)
  - verification done or planned
- **Independent findings:** a review by a fresh agent session with no memory of the
  design chat, so it hasn't been talked into the design. Its findings are input for the
  human, not decisions.
- **Open items:** carried-forward actions, known gaps, questions for the approver.

### 2. The review is run as a walkthrough

The agent presents the package one group at a time, like a presenter. The human looks,
asks questions, challenges choices and may ask for changes. That discussion is the
review.

For each change group, the human gives a **disposition**:
- **Accept.**
- **Reject**, with a reason.
- **Accept with action:** an action item with an owner. It must be closed or explicitly
  carried forward before the next gate.

For each independent finding: accept it, or reject it with a reason.

### 3. Explicit overall decision

At the end, the agent repeats back exactly what's being decided, for example:

> *Approve DR-004: PCB-0001 rev B and HSG-0002 rev C, 5 change groups accepted,
> 1 accepted with action (A-12, owner: KC), 1 finding rejected?*

The human answers **yes or no**. That reply is the approval. A vague "ok" doesn't count:
the answer must respond to a question that names exactly what's being approved.

### 4. Records are generated, not filled in

- **Review minutes:** scope, attendees (human and agents, with which model), each
  group's disposition, findings and their dispositions, actions, the overall decision.
- **Archived transcript,** unchanged, next to the minutes.
- **Each approval in the minutes quotes the human's reply** and points to where it is in
  the transcript. CI checks that the quote really exists in the transcript, so an agent
  can't invent an approval.
- **The package and its visuals** are archived with the minutes, so a reader later sees
  what the approver saw.

Nobody fills in a form. The records come from how the review was actually run.

## Where this lives

| What | Where |
|---|---|
| What an approval must prove (who, what, decision, when, evidence) | SOP-001 |
| When formal reviews happen; package and minutes requirements | SOP-003 |
| Which reviews gate which phases | SOP-004 and the product's `gates.yaml` |
| How agents prepare packages, run walkthroughs and log check-ins | `AGENTS.md` |
| Package and minutes formats | Templates in the product repo |
| Checking that cited approvals exist in transcripts | CI |

## Tools to look at (not decided)

- **PCB visual comparisons:** KiCad's command-line export (layer images), and KiBot's
  KiDiff for before/after comparisons.
- **MCAD visuals:** renders and screenshots through the CAD tool's API (the Fusion API
  today; Onshape's API offers version comparisons).
- **Transcripts:** controlled work should be done in agent tools that save sessions
  locally (Claude Code, Codex). Chat apps without a reliable export aren't suitable for
  formal reviews.
