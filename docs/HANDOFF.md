# Handoff: Lean Agentic QMS + Photoreactor Showcase

## Goal
Build a lean, ISO 9001-style, agent-operated QMS as a git/GitHub repo, then run the
photoreactor (repo: `kelvinchow23/photo-reactor`) through it as the first showcase
build: planning → requirements → design → purchasing → build → test → sign-off,
with full traceability down to when each part was bought.

The showcase is about **controlled, traceable AI-assisted hardware development**,
not "AI made a product". Humans approve everything.

## Context
- Small team, build-to-order lab hardware. No inventory system needed.
- ISO 9001-level rigor is the target, not ISO 13485. Make it auditable, but don't
  pursue certification unless needed.
- Certification applies to an org's QMS scope, not to a build. Frame builds as "made under the QMS".
- QMS name: undecided (candidates: Keel, MVQ, Floor). Must not include a person's name.

## Architecture
Two levels:
1. **Org QMS repo**: SOPs, templates, reusable CI checks (GitHub Actions), base `AGENTS.md`.
   Versioned and tagged (e.g. `QMS-rev A`).
2. **Product repo scaffold**, generated with **Copier** (not a GitHub template repo) so
   `copier update` pulls SOP and template changes into existing products as a reviewable PR.
   Each product records which QMS rev it was built under.

Codex reads `AGENTS.md`. Claude Code reads `CLAUDE.md`, which should just point to `AGENTS.md`.

## Git as lightweight PLM
- ECR = GitHub Issue. ECO = PR referencing the ECR. Merge = approval (human only).
- Protect `main`: PRs required, CI must pass, human approval required.
- Commit format: `[PN] revX: change summary (ECR #n)`. Small commits, squash-merge PRs.
- Releases = tags (e.g. `ASM-0001-revA`) with a GitHub Release attaching STEP, PDF drawings,
  Gerbers, BOM, and firmware binary.
- Use Git LFS for large binaries. Prefer text exports (CSV BOM, KiCad, YAML).
- Fusion files stay in Fusion cloud. Record the Fusion version number in commits.
- AI design reviews are posted as PR comments. They are an **input** to review; a human
  dispositions every item (accept / reject + rationale / action). AI never signs off.

## Part classes (traceability, risk-based)
- **A (traced):** custom parts and key components (PCB, LEDs, driver ICs, printed/machined
  parts, harness). Each traced to a specific PO or print job, with incoming inspection.
- **B (bulk):** screws, standoffs, heat-sets, wire, crimps. Internal PN, traced to the bulk PO only.
  `/stock/bulk.yaml` maps PN → current batch PO. No counts.
- **C (consumable):** glue, flux, zip ties, solder. On the BOM as consumable, untraced.

## Product repo structure (starting point)
```
/00_planning      charter, schedule, project risk register
/01_requirements  requirements.yaml (REQ-xxx + verification method), fmea.csv
/02_design        /mech /pcb /harness /firmware /reviews
/03_release       parts.csv, bom.csv (PN, rev, class, qty, supplier, cost_cad, lead_time),
                  /drawings /work_instructions /test_procedures
/builds/B00x/     build.yaml (units, config revs, date, builder), cart.csv,
                  purchases/PO-*.yaml (+ invoice PDF), trace.csv, inspection/, test/, signoff.md
/stock/bulk.yaml
/equipment/       calibration records (later)
trace_matrix.csv  REQ → design → test → result
ai_log.md         what each agent produced / what was changed / what was rejected
```

## Build flow
1. Open build → script generates `cart.csv` from BOM × qty (grouped by vendor), minus bulk stock.
2. Order → PO yaml + order confirmation (may integrate with the existing Airtable purchase-req flow).
3. Receive → incoming inspection for Class A.
4. Build → test results recorded per serial number.
5. Release PR → CI verifies every A/B line in `trace.csv` resolves to a PO and all tests passed → human merges.
6. Demo target: `trace SN001` prints config revs → each part → vendor, order #, date, cost (CAD), inspection result, plus a cost rollup.

## Phase gates
0 Scope (charter, WBS, make/buy, project risks) → 1 Requirements (frozen rev A, FMEA-lite:
LED optical hazard, thermal, electrical, solvent) → 2 Design (reviews closed) → 3 Release for
build → 4 Build & verify (trace matrix complete) → 5 Close-out (handoff docs, lessons learned
including where AI was wrong).

## Task now: QMS-rev A skeleton (keep it minimal)
- Repo structure + Copier template for product repos.
- Base `AGENTS.md` (structure, hard rules: no commits to main, PN + ECR in every commit,
  never bump a rev without updating parts.csv/BOM, never mark anything approved,
  run checks before finishing) + `CLAUDE.md` pointer.
- SOP-001 Document & change control
- SOP-002 Part numbering, revisions & part classes
- SOP-003 Design review
- Templates: ECR issue, PR/ECO, design review log.
- CI check: BOM/parts lint (every line has PN, rev, class, supplier, cost_cad; no orphan PNs).
- Commit message lint.
- Each SOP is about one page. **Do not write SOPs for processes not yet run.**

## Later (write just before each is needed)
SOPs for purchasing & supplier control (approved supplier list), incoming inspection & build
records, test & release, nonconformance/corrective action. Management layer comes after real
data exists: scope, quality policy, measurable objectives, org risk register, calibration
register (+ CI check for expired tools), training records, customer feedback, yearly internal
audit (must be someone other than the person whose work is audited) and management review.
Minimum viable 9001 QMS ≈ 6–8 short SOPs plus records.

## Photoreactor specifics
- Existing repo was for sharing designs. **First, tag the current state as `baseline-pre-QMS`**
  without rewriting history.
- PCB is being designed with Codex (replacing breadboarded Pico electronics).
- **B001 parts were already purchased before the QMS existed.** Capture them retroactively
  from real order confirmations/invoices, with a deviation note. Supplier approval is retroactive.
  Do incoming inspection now. **Never backdate records.**
- Check with the employer before publishing purchase records/pricing publicly; plan a redacted mirror if needed.

## Working setup
- GitHub is the source of truth. Work on branches, push often, open PRs when done
  (supports remote steering from the mobile app; review and merge later).
- Keep secrets out of the repo.
- Keep `ai_log.md` updated as you go. It's the core showcase artifact.

## Definition of done (showcase)
SN001 released, `trace SN001` resolves fully, mock audit by an outside person with no major
findings, and an honest write-up of what agents did well and badly.
