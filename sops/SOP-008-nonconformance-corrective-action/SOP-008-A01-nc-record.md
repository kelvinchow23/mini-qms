---
id: NC-nnn
raised: YYYY-MM-DD           # the day it was found
raised_by: ae                # id from roles.yaml, or agent plus directing human
found_in: incoming-inspection # incoming-inspection / test / use / customer / supplier / process
items:                       # everything affected; use trace to find all units
  - {pn: PRX-A-0003, rev: A, sns: [PRX-A-0003-261125A], lines: [P-0001]}
status: open                 # open / dispositioned / closed
disposition: null            # use-as-is / rework / scrap / return
decided_by: null
corrective_action_needed: null   # yes / no
---

# NC-nnn: <short title>

## What's wrong
<observation and how it was found; photos or data linked>

## Containment
<items labelled or set aside; other affected units found via trace>

## Disposition (SOP-008 §4)
<decision, reason, who decided and when; customer agreement if needed>

## Cause and corrective action (SOP-008 §5)
<needed? if no, one-line reason. If yes: root cause, action (ECR #n / supplier review), owner>

## Effectiveness check and closure
<date, evidence that the action worked>
