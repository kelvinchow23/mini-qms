# Sources

What minimalQMS is based on. Checked 2026-11-17.

## Standards (paid, not reproduced here)

| Standard | Use | Status in this repo |
|---|---|---|
| **ISO 9001:2026** (6th edition) | The target standard | **Not yet purchased.** Clause references come from public guidance and certification-body summaries, and need checking against the text. [ISO catalogue page](https://www.iso.org/standard/88464.html) |
| ISO 9001:2015 | The previous edition. Most public guidance refers to it. | Withdrawn; transition ends about 30 Sept 2029 |
| ISO 19011 | Guidelines for auditing | To use when writing the internal-audit procedure |

minimalQMS never copies text from ISO standards. It cites clause numbers and summarizes
requirements in plain language.

## Free official guidance

- ISO/TC 176/SC 2, [*Guidance on the requirements for documented information of ISO 9001:2015*](https://committee.iso.org/sites/tc176sc2/home/projects/published/iso-9001-2015.html). The basis for [ISO9001-MAP.md](ISO9001-MAP.md).
- [ISO 9001 Auditing Practices Group papers](https://committee.iso.org/home/tc176/iso-9001-auditing-practices-group.html), especially:
  - Documented information (electronic approval)
  - Design and development
  - Internal audits
  - External providers
- 2026 changes and transition dates:
  - [LRQA](https://www.lrqa.com/en/latest-news/iso-9001-2026-live/)
  - [DQS](https://www.dqsglobal.com/en/explore/blog/iso-9001-2026-transition)
  - [Advisera](https://advisera.com/articles/iso-9001-2015-vs-9001-2026-main-differences/)
  - [PJR](https://www.pjr.com/iso-standards-and-technical-updates/iso-90012026-whats-changed)

## Open templates we may build from

minimalQMS is MIT-licensed, so we only reuse content whose licence allows it. Anything
reused gets an entry in `NOTICE` (source, licence, commit) and keeps any required
attribution.

| Source | Licence | What we'd use it for |
|---|---|---|
| [OpenRegulatory templates](https://github.com/openregulatory/templates) at commit `aad8277` (2024-06-04) | **CC BY 4.0** at that commit. Current versions are CC BY-NC-SA 4.0 and **can't be used.** | Structure for nonconformance/CAPA, internal audit, management review and supplier control SOPs, adapted from ISO 13485 down to 9001 |
| [GSTT-CSC QMS-Template](https://github.com/GSTT-CSC/QMS-Template) | Apache-2.0 (many SOPs derive from OpenRegulatory, so credit both) | GitHub-based PR review and change management, as a reference |
| [git-plm/parts](https://github.com/git-plm/parts) and [gitplm](https://github.com/git-plm/gitplm) | MIT and Apache-2.0 | Part numbering, part master, BOM and release conventions (SOP-002) |
| [Open QMS (IridiumSoftware)](https://github.com/IridiumSoftware/OpenQMS) | Apache-2.0 | GitHub issue forms (nonconformance, supplier evaluation) and CI gate ideas |
| [Innolitics RDM](https://github.com/innolitics/rdm) | MIT | Pattern for rendering Markdown to released PDF/Word documents |

## Reference only (don't copy)

- [Tidepool QMS](https://www.tidepool.org/blog/tidepools-open-source-qms-gets-iso-13485-certified):
  the licence for its SOPs is unclear.
- Current OpenRegulatory templates (NonCommercial) and the dearauditor SOPs (ShareAlike):
  their licences aren't compatible with MIT.
- [OpenRegulatory, *GitHub QMS: We No Longer Recommend It*](https://openregulatory.com/articles/we-no-longer-recommend-github-gitlab-as-qms-software):
  the critique answered in [RATIONALE.md](RATIONALE.md).
