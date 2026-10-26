# Taiwan Public Funds Intelligence: product requirements

This document defines product behavior, data meanings, interfaces, and architecture.
The [business plan](BUSINESS_PLAN.md) defines the business model and price hypotheses.
[AGENTS.md](../AGENTS.md) defines agent rules and engineering workflows.
These requirements describe a target product, not delivered features or verified data coverage.

## Terms

- An organization is a company, business, association, foundation, or another registered body.
- An organization identifier is an official registration number, such as a Taiwan Unified Business Number.
- A source record is a published record before product transformations.
- A derived record is an output from versioned matching, correction, or calculation rules.
- A grant approval is an approved award, not evidence that money was paid.
- A programme is a public funding scheme with published rules.
- An application programming interface, or API, permits software access to a service.
- A Sankey chart uses connected bands to show quantities between categories.

## Approved scope and priority

The approved planning baseline is recorded in [Issue #6](https://github.com/x168/dulan/issues/6) on 2026-10-27, Asia/Taipei.
First priority includes organization and agency references, procurement intelligence, and central enterprise grants.
Second priority is one explicitly selected local enterprise-grant pilot after central ingestion.
Other organization grants are incidental records from the same approved inputs.
Loan and credit-guarantee coverage is limited to incidental public programme metadata.
Government investment and tax-benefit ingestion are outside the first release.

Prioritize enterprise research, transformation, equipment, and related business programmes.
Keep company, association, foundation, and unresolved organization identities distinct.
Retain grant, donation, award, interest-support, and payment classifications from the source.
Do not expand the first release into nationwide welfare or activity-grant collection.
Do not collect personal recipient directories.

The product supports businesses that research government markets.
Journalists and general readers can use public-topic pages.
Government is a research subject, not an assumed paying customer.
Source access, licences, actual years, organization matching, and metrics require verification before publication or sale.
Nationwide coverage, ten complete years, customer demand, and low operating costs remain unverified.

## Approved first research pilot

The user approved the first customer and purchase task recorded in [Issue #40](https://github.com/x168/dulan/issues/40).
The first paying audience is small and medium-sized suppliers with experience in government contracts.
The first validation segment is information technology services and systems integration.
Primary users are sales leads and bid managers.
Purchase decision-makers are owners or managers.

The first purchase task supports business development through research on peer contracts, buying agencies, comparable awards, and traceable exports.
The pilot covers one industry.
The broader source and grant priorities in this document remain applicable.

Provide organization, agency, and case searches for the pilot.
Provide historical award comparisons within verified coverage.
Provide distributions by peer supplier and buying agency with declared metrics.
Provide Excel case exports with source links and data versions.
Apply the existing subscription and standalone-export access rules.

Verify the following task with three peer suppliers:

1. Find their government cases within the verified source scope.
2. Inspect relevant buying agencies and comparable award amounts.
3. Export a case list with traceable source records and data versions.

Show actual years and unavailable data during this task.
Do not substitute missing records with invented cases or zero amounts.
If verified inputs cannot support the task, record the source limitation before claiming pilot acceptance.
The task does not establish customer demand or commercial success.
The approval sets no fixed historical period, minimum row count, launch date, or conversion threshold.
Central enterprise grants retain first grant priority and remain separate from procurement amounts.

## Search and shared behavior

Provide searches by organization identifier, organization name, or keyword.
Provide organization pages and agency, industry, and year filters.
Provide shared public topics, historical analysis, comparisons, and structured exports.
Give visitors with the same data version and access rights the same results.
Use the same topic rules and ordering rules for those visitors.

Exclude saved searches, favorites, watchlists, personal recommendations, personal notifications, customer-system connections, and private proposal uploads.
Exclude the earlier five-organization monitoring add-on.
Keep necessary transaction and access records for purchases and retrieval.
Do not turn transaction records into behavioral profiles.
Use necessary receipts and delivery notices only for their transaction purpose.

## Public topics and paid access

Select public topics through shared public-interest rules and aggregate signals.
Record each topic's basis, sources, selection time, review, policy version, and expiry rules.
Verify organization identity before opening a topic.
Do not set an unverified automatic traffic threshold.
Do not choose free content from individual browsing histories.

Provide complete publishable topic analysis without login within verified coverage.
For other organizations, provide free current-year basic records, source references, coverage, and the data cutoff date.
Unlock available historical analysis and comparisons through a subscription.
Sell prepared bulk exports separately, including to visitors without a subscription.
Apply the same source, privacy, and quality requirements to free and paid content.
Keep dated public-topic snapshots, source references, and correction history available under the published topic policy.

Before checkout, show available years, fields, row counts, missing data, data versions, and delivery scope.
When identity or data is uncertain, show that condition clearly.
Do not imply that missing records mean no public funding ever existed.
Do not sell nonexistent analysis.
Do not imply wrongdoing from a public-topic label or a public funding record.
Public information can be copied; payment buys preparation, comparison, traceability, and convenient exports.

Enforce paid access on the server.
Keep restricted records out of public data files, pages, scripts, source maps, static outputs, and public caches.
Treat a blurred chart only as a preview.
Keep export storage private.
Before each restricted response or download, verify the transaction and current access rights.
Isolate cached responses between access rights.
After expiry or refund removes access, reject further restricted retrieval.

## Sources and reproducibility

Prefer official announcements, official grant disclosures, and other primary sources.
For each dataset, record its URL, publisher, publication date or version, retrieval date, licence, format, and update frequency.
Record its geography, actual years, currency, units, field definitions, and known gaps.
Keep raw inputs, normalized records, and derived analysis separate.
Version inputs, transformations, identity rules, corrections, and outputs.
Preserve correction history and make preparation reproducible.

## Amounts, dates, and corrections

Keep procurement budgets, bid prices, award amounts, grant approvals, cumulative disbursements, and verified payments separate.
Do not treat an award or approval as cash received.
Do not treat a contract total as annual or recognized revenue.
Keep announcement, award, approval, payment, and performance dates separate.
Explain the date basis of each annual view.
Show partial years, observed coverage, and missing years.
Do not fill missing years with zero.
Retain supported negative adjustments with their source meaning.

Keep announcements, contracts, lots, suppliers, amendments, and cancellations distinct.
Handle multiple awards, withdrawals, refunds, and cumulative grant amounts without double counting.
Until meanings and duplicate funding are resolved, do not add procurement and grant amounts into one cash-received total.

## Organization identity

Prefer official organization identifiers for matching.
Retain source names and aliases.
Handle missing identifiers, name changes, and ambiguous matches explicitly.
Do not merge organizations only because their names are similar.
Keep uncertain matches visible.
Do not publish private contact details or personal recipient lists.

## Analysis and public descriptions

Distinguish source facts, calculated statistics, and forecasts.
For each metric, explain its formula, denominator, comparison group, sample size, and missing-value handling.
Use award-to-budget ratios only for compatible scope and currency with positive amounts.
Do not interpret that ratio as a losing bid, profit, or a guaranteed winning price.
Show winning rates only with a verified denominator that includes valid unsuccessful bids.
When only award announcements exist, show award counts and omit unsupported winning rates.

Group comparable cases by procurement category, method, period, and scope.
Show the distribution and sample size.
Do not draw strategy conclusions from sparse or incompatible cases.
Show material uncertainty and coverage limits without unsupported precision.
Use confidence-interval labels only with a stated statistical basis.

Use source-supported agency distributions and award patterns for competitor research.
Do not infer evaluator preferences, political ties, corruption, or private relationships from co-occurrence or amounts.
Exclude personal evaluator profiles.
Treat published contract expiry as a dated opportunity hypothesis, not a promised renewal or future budget.
Keep official announcements separate from estimated cycles.
Explain the supported relationship and amount type for every network or Sankey-chart link.
Do not describe an award relationship as a completed payment.

Use neutral topic titles and verifiable evidence.
Distinguish allegations, official findings, and corrections.
Provide a correction channel.

## Interface and accessibility

Use Traditional Chinese interface text.
Explain metrics, units, controls, assumptions, and data cutoff dates.
Support keyboard use, mobile devices, and responsive layouts.
Do not use color alone to distinguish amounts or categories.
Provide table alternatives for all charts, including network and Sankey charts.
Keep missing values visibly different from zero.
Place sources, coverage, exclusions, definitions, limitations, and corrections near the results.
Show access and export terms before payment.

## Architecture and delivery

Use static pages, styles, scripts, and versioned public data for public content.
Precompute expensive joins and summaries when practical.
Keep browser downloads and dependencies proportional to the product.
Cloudflare static hosting is the target, not an existing verified deployment.
Use only the server services necessary for payment verification, access rights, restricted queries, and authorized downloads.
Select and verify actual Cloudflare products and payment services during implementation.
Do not assume that accounts, services, or destinations already exist.

When choices are made, record build commands, output locations, deployment settings, and public/private data boundaries.
Keep credentials, tokens, transaction records, private material, and restricted business records out of public assets.
Identify preview and production destinations and source revisions.
Verify the exact delivery artifact and access behavior before publication.
Keep a known working revision for recovery.
Show input versions, analysis versions, and update dates.
Preserve material historical changes and uncertainty when data changes.

## Product acceptance coverage

| Area | Required evidence |
| --- | --- |
| Source quality | Identifiers, dates, actual years, units, missing values, duplicates, amount constraints, source totals, and explained discrepancies |
| Reproducibility | Identity rules, corrections, deduplication, denominators, input versions, rule versions, known cases, and repeatable outputs |
| Access | Free, subscription, and export rights; restricted-data isolation; private storage; cache separation; expiry and refund behavior |
| Usability | Affected pages, mobile use, keyboard use, chart controls, table alternatives, data loading, source references, and metric definitions |
| Publication | Matching preview and delivery artifacts, exact revision, input and analysis versions, update dates, visible corrections, and limitations |

Engineering execution locations and release gates remain defined in AGENTS.md.
The [delivery stages](DELIVERY_STAGES.md) define stage outcomes and exit evidence.
These requirements do not establish that any product acceptance check has passed.
