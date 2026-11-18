# ISO 9001 requirements map

What ISO 9001 actually requires to be written down, and where minimalQMS covers it. This
is the definition of "minimal": **everything the standard requires, and as little else
as possible.**

> **Basis and limits.** Built from public sources only: ISO/TC 176/SC 2's free guidance on
> documented information (written for the 2015 edition), the ISO 9001 Auditing Practices
> Group papers, and certification bodies' summaries of the 2026 changes (see
> [SOURCES.md](SOURCES.md)). **The clause numbers haven't yet been checked against the
> purchased text of ISO 9001:2026.** That check is needed before the first audit.
> No text from the standard is reproduced here, only clause numbers and plain-language
> summaries.

## Which edition

**ISO 9001:2026** (6th edition) was published on 16 September 2026 and replaces the
2015 edition. Certificates to the 2015 edition are reported to remain valid until about
30 September 2029. minimalQMS targets **2026**. The 10-clause structure is unchanged, and
the clauses minimalQMS relies on most (7.5, 8.3, 8.5.6, 9.2.1) are reported as unchanged
or only reworded.

## The key finding: ISO 9001 requires very few documents

ISO 9001 **doesn't require any written procedures**, a quality manual or forms. It
requires a short list of documents to **maintain**, and evidence (records) to **retain**.
Everything else is optional and is written only if it helps.

minimalQMS's SOPs exist to keep humans and agents consistent, not because the standard
requires SOPs. That's why each SOP is about one page.

## Documents to maintain

| Clause | Requirement | minimalQMS | When |
|---|---|---|---|
| 4.3 | Scope of the QMS | `qms/scope.md` | Management layer, after rev A |
| 4.4 | Information needed to run the processes | SOP-001 to SOP-008, `AGENTS.md`, templates | Rev A |
| 5.2 | Quality policy | `qms/policy.md` (a few lines) | Management layer |
| 6.2 | Quality objectives | `qms/objectives.yaml` (measurable, e.g. admin hours per build) | Management layer |

## Records to retain

| Clause | Evidence of… | minimalQMS record | When |
|---|---|---|---|
| 4.4 | Processes ran as planned | Git history, PRs, CI results | Rev A |
| 7.1.5 | Measuring equipment fit for purpose, and calibration | `equipment/equipment.csv`, plus a CI check for overdue equipment | SOP-007 |
| 7.2 | Competence | `qms/training.csv` (person, skill, evidence) | Management layer |
| 8.2.3 | Review of customer or product requirements | `requirements.yaml`, approved at G1 | SOP-004 |
| 8.3.2–8.3.6 | Design planning, inputs, reviews, outputs, changes | `plan.yaml`, requirements, review minutes and transcripts, released design exports, ECR/ECO | SOP-003, SOP-004 |
| 8.4.1 | Supplier evaluation and monitoring | `suppliers.csv` | SOP-005 |
| 8.5.2 | Unique identification where traceability is needed | Serial numbers, `trace.csv`, purchase lines (Class A/B) | SOP-002, SOP-006 |
| 8.5.3 | Customer or supplier property lost or damaged | An NC record if it happens | SOP-008 |
| 8.5.6 | Changes reviewed: results, who authorised, actions | ECR, ECO PR, approval | **SOP-001** |
| 8.6 | Release, traced to the person who authorised it | `release.yaml`, approved and merged by a named human | SOP-007 |
| 8.7 | Nonconforming outputs, actions, concessions, who decided | `NC-nnn.md` | SOP-008 |
| 9.1.1 | Monitoring and measurement results | Objectives tracking | Management layer |
| 9.2.2 | Internal audit programme and results | Audit plan and report | Management layer (yearly) |
| 9.3.3 | Management review results | Review minutes | Management layer (yearly) |
| 10.2.2 | Nonconformities and corrective actions | Corrective-action section of `NC-nnn.md` | SOP-008 |

## What the standard does *not* require

These are minimalQMS choices, and SOPs mark them as such so others can drop or change them:

- **Independent design reviewers.** ISO 9001 doesn't require the reviewer to be independent
  of the author (unlike US FDA rules for medical devices). minimalQMS requires an
  independent *agent* review as a one-person safeguard.
- **Signatures.** Not required. Approval must be attributable to a person, and electronic
  approval is accepted (APG guidance on electronic documented information).
- **A retention period.** The standard requires you to *decide* retention. The period
  itself is a minimalQMS choice.

The **only** independence requirement is for internal audit: auditors must be objective
and impartial (9.2.2). Auditing your own work isn't acceptable, so a one-person
organisation needs an outside auditor.

## New or expanded in 2026 (from secondary sources, to verify)

These mostly affect the management layer, which comes after rev A:
- **4.1:** climate change considered as part of context.
- **5.1.1:** leadership promotes a culture of quality and ethical behaviour; **7.3** adds
  awareness of it.
- **6.1.2 / 6.1.3:** risks and opportunities are now separate clauses, with actions
  proportionate to impact.
- **6.3:** planning of changes is expanded.
- **7.1.6:** organisational knowledge is retained, applied and shared. The git history,
  review minutes and lessons learned largely cover this.
- **9.2.2:** each audit needs defined objectives.
- **9.3:** new management-review inputs.
