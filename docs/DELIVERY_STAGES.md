# Delivery stages

## Decision

The user requested numbered milestones on 2026-10-27, Asia/Taipei.
The six stages divide the approved public-funds scope recorded in [Issue #6](https://github.com/x168/dulan/issues/6).
[Issue #33](https://github.com/x168/dulan/issues/33) records this planning change.

Stage numbers identify delivery outcomes.
Native Issue dependencies determine which work must finish first.
Independent preparation can proceed when its own blocker is cleared.
The numbers do not impose a new dependency between every adjacent stage.

## Stage definitions

The [GitHub milestone list](https://github.com/x168/dulan/milestones) contains the numbered stages and their assigned Issues.

| Stage | Outcome | Required exit evidence |
| --- | --- | --- |
| 1 | Product scope and delivery rules | Merged product and business documents define the approved scope, data meanings, access rules, and delivery requirements. |
| 2 | Source data and organization identity | Versioned source records and identity rules pass applicable self-hosted checks. Missing data, uncertain matches, units, and actual coverage remain visible. |
| 3 | Procurement data and comparisons | Verified source access and versioned procurement records support traceable comparisons. Checks cover lots, suppliers, corrections, and metric definitions. |
| 4 | Enterprise grants and local pilot | Central enterprise grants pass source and data checks before local ingestion. The selected local pilot records its actual coverage. |
| 5 | Research website and paid exports | The exact self-hosted artifact works in the verified preview. Evidence covers accessibility, private access, payment tests, exports, and recovery. |
| 6 | Demand, pricing, and cost validation | A recorded protocol and observed results support an adopt, revise, or stop decision. Evidence separates readership, purchases, refunds, renewals, and costs. |

Central enterprise grants remain the first grant priority.
The selected local pilot remains the second grant priority.
The stage split preserves their existing order.
Research preparation for stage 6 can precede the preview.
Actual conversion tests require the verified product and their applicable authorization.

## Stage decisions and evidence

A milestone records a delivery target.
Its existence does not open or complete a stage.
Closing its Issues alone does not prove that its exit requirements passed.

The accepting Issue records the reviewed revision and links the required source, artifact, service, or commercial evidence.
GitHub checks remain the sole authority for continuous integration results.
Each stage decision records the evidence, limits, and acceptance outcome on its accepting Issue.
Missing evidence keeps the applicable gate open.

This planning decision establishes no product-stage completion.
It sets no deadline and authorizes no production publication or live charging.
The historical-review milestone remains separate from these public-funds stages.

## Record ownership

GitHub Issues own scope, blockers, priorities, dependencies, milestones, and lifecycle state.
This document defines stage outcomes and required exit evidence.
The existing product documents remain owned by Issue #6.
