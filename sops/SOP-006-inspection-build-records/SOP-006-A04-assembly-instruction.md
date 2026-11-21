---
# SOP-006-A04 Assembly instruction (appendix to SOP-006; revised with it)
assembly: PPP-A-NNNN      # the assembly this instruction builds
rev: A                    # same revision as the assembly
status: draft             # approved at G2 (design freeze) with the BOM
time_estimate: 30 min     # per unit, hands-on
---

# Assembly instruction: PPP-A-NNNN <assembly name>

## Overview
<!-- One or two sentences: what is built, and a render or photo of the finished unit. -->
![Finished unit](images/finished.png)

## Before you start
- **Parts:** as listed for this assembly in `bom.csv`. Check quantities before starting.
- **Tools:** <!-- e.g. soldering is not used; hex key 2.5 mm; heat-set insert tool at 230 °C -->
- **Consumables:** <!-- e.g. thread locker, isopropyl alcohol -->
- **Safety:** <!-- e.g. hot tool, ESD strap for the PCB -->

## Steps
<!-- One action per step. Each step names its parts and has a check where a mistake is likely. -->

### 1. <Action>
- **Parts:** PPP-0004 (1), HWS-0001 (4)
- **Do:** <what to do, in the imperative>
- **Setting:** <!-- torque, temperature, orientation; delete if none -->
- **Check:** <!-- what must be true before moving on; delete if none -->

![Step 1](images/step-01.png)

### 2. <Action>
- **Parts:**
- **Do:**
- **Check:**

## Final checks
- [ ] All screws fitted and tight
- [ ] <!-- functional or visual check before testing -->
- [ ] Serial number label applied (SOP-002 section 7)

## Record
Record the build in `builds/B00n/` (SOP-006). Note any step that could not be followed as
written, and raise an ECR if the instruction needs to change.
