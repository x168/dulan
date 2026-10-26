# Taiwan Public Funds Intelligence: business plan

Direction decision: 2026-10-25.
Approved scope update: 2026-10-27, Asia/Taipei.

This plan records business decisions, price hypotheses, market comparisons, and evidence limits.
The [product requirements](PRODUCT_REQUIREMENTS.md) define behavior, data meanings, interfaces, and architecture.
[AGENTS.md](../AGENTS.md) defines agent rules and engineering workflows.

## Position and approved categories

The product is business-to-business intelligence, abbreviated B2B, for organizations that research government markets.
It joins traceable procurement and enterprise-grant records to reduce collection, comparison, and preparation work.
Likely paying groups include small businesses, sales teams, accountants, investors, and research organizations.
Journalists and general readers use public-topic pages.
Government is a research subject, not an assumed paying customer.

The approved first priorities are organization and agency references, procurement intelligence, and central enterprise grants.
Central and local procurement belong within verified source coverage.
Central enterprise research, transformation, equipment, and related business programmes are the first grant priorities.
An explicitly selected local enterprise-grant pilot follows central ingestion.
Other organization grants remain incidental records from the same approved inputs.
Loan and credit-guarantee work retains incidental public programme metadata only.
Government investment and tax-benefit ingestion are outside the first release.

The commercial hypothesis is that useful public topics demonstrate research depth and attract some buyers of deeper research or prepared exports.
This is a hypothesis, not demonstrated conversion, revenue, or profitability.
Source completeness and maintenance costs also remain unverified.

## Approved first customer and purchase task

The user approved this decision on 2026-10-27, Asia/Taipei.
[Issue #40](https://github.com/x168/dulan/issues/40) records the approval and document delivery.

The first paying audience is small and medium-sized suppliers with experience in government contracts.
The first validation segment is information technology services and systems integration.
Primary users are sales leads and bid managers.
Purchase decision-makers are business owners or managers.
The other customer groups remain candidates for later validation.
This approval selects a starting segment; it does not prove local demand.

The first purchase task supports business development in government markets.
The customer researches peer suppliers' government contracts, relevant buying agencies, and comparable award amounts.
The customer exports a traceable case list for a business development meeting.

The minimum pilot covers one industry with these outputs:

- Organization, agency, and case searches.
- Historical award comparisons within verified coverage.
- Distributions by peer supplier and buying agency with clear metrics.
- Excel case exports with source links and data versions.

The acceptance task uses three peer suppliers.
It covers their government cases and relevant buying agencies.
It ends with a case export that includes source links.
This task tests usable research and traceability, not winning probability or personal contact discovery.

Actual historical years follow verified source coverage.
No fixed year range, row count, launch date, or commercial success threshold is approved by this decision.
Central enterprise grants retain their approved priority.
The selected local grant pilot still follows central ingestion.
Procurement and grant amounts remain separate.

## Free public topics and paid research

| Visitor context | Free content | Paid content |
| --- | --- | --- |
| A selected public-topic organization | Complete publishable analysis within verified coverage, without login | Prepared organization or industry exports |
| Other organizations | Current-year basic records, sources, coverage, and data cutoff date | Available historical analysis, comparisons, agency distributions, and separately purchased exports |
| Missing data or uncertain identity | Clear missing-data or identity status | No sale based on nonexistent analysis |

Complete analysis means complete within the verified, publishable scope.
It does not mean complete government spending.
No current-year record does not establish that an organization never received public funding.
Older records cannot silently replace missing current-year records.

Public-topic selection uses shared public-interest rules, not personal browsing histories.
The user approved the following trial policy on 2026-10-27, Asia/Taipei.
[Issue #42](https://github.com/x168/dulan/issues/42) records this decision.

Collect Taiwan Google Trends candidates daily using the previous 24 hours of trending searches.
Select topics related to government procurement or enterprise grants.
Verify the organization or agency identity before publication.
Review source evidence and data quality before opening a topic.
Do not open a company's analysis solely because a related person's name is trending.

Provide the topic's publishable analysis without login for seven days from topic publication.
Show its publication time, free-period end, source scope, and policy version.
Give all visitors the same free-topic access.
Keep published historical snapshots free after that period.
Apply normal access rules to new deep research added after the free period.
Prepared exports retain their existing separate purchase rules.

Keep fixed demonstration topics free for industries that rarely appear in trending searches.
These topics provide a stable introduction to the product's research.
Record the selection reasons, identity review, source references, data versions, and policy version for each topic.
A topic label or funding record does not imply misconduct.

Google Trends supplies a candidate signal, not automatic proof of public interest or company identity.
Google Trends Explore displays relative search interest on a scale from 0 to 100.
Its scale depends on the selected geography and period.
Do not set an unverified automatic traffic threshold.
Do not use an Explore score above 80 as an automatic free-access condition.
A zero score can reflect insufficient search volume rather than no searches.

An RSS feed is a machine-readable stream of updates.
An application programming interface, or API, permits software access to a service.

Official Google documentation was retrieved on 2026-10-27:

- [Trending now](https://support.google.com/trends/answer/3076011?hl=en) describes location and time filters, downloadable files, and an RSS feed.
- [Data definitions](https://support.google.com/trends/answer/4365533?hl=en) explain relative Explore scores and low-volume data limits.
- [API access](https://developers.google.com/search/apis/trends) describes an alpha application process with limited access.

Assess the official RSS feed first for automated collection.
Verify actual source access and usage conditions during implementation.
Do not assume that API access has been granted.
This record approves policy and does not start collection or publication.

Dated public snapshots retain source references and correction history.
Already published information can be copied.
The paid value is cleaning, cross-source comparison, reproducibility, traceability, and convenient exports.

## Shared product behavior

The first release provides shared searches, organization pages, public topics, and agency, industry, and year filters.
A filter changes the current query without creating a personal profile.
Equal data versions and access rights produce equal results.

Saved searches, favorites, watchlists, recommendations, personal notifications, private proposal uploads, and customer-management connections are excluded.
Personal evaluator profiles and automated proposal diagnosis are excluded.
The earlier NT$299 monthly five-organization monitoring offer is excluded.

Paid retrieval can retain the minimum necessary transaction and access records.
Those records do not authorize behavioral recommendations.
Public reading requires no login.
Paid access uses the minimum verification necessary for the transaction.
Necessary receipts and delivery notices serve transaction purposes only.

## Customer work and research outputs

| Customer group | Work supported | Source-supported output |
| --- | --- | --- |
| Business owners and sales leads | Assess an agency or government market | Competitor awards, agency distributions, comparable amounts, and dated trends |
| Business sales and research teams | Prepare organization research lists | Organization identifiers, identity status, sources, dates, and amount types |
| Accountants, investors, and researchers | Check public-sector business leads | Historical records, corrections, repeatable statistics, and coverage limits |
| Journalists and general readers | Understand public procurement and grants | Open topics, citable charts, source records, and methods |

An award is not cash received or recognized revenue.
Research cannot guarantee an investment result, a winning bid, or a future grant.

| View or metric | Necessary definition and inputs | Interpretation limit |
| --- | --- | --- |
| Annual announced amounts and counts | Declared award or approval date; separate procurement and grant series | Show partial years and cutoff dates; do not invent annual revenue from contract totals |
| Agency distribution | Same amount type, period, and deduplication rules | Show sample and coverage; do not infer private relationships |
| Award-to-budget ratio | Same case, scope, and currency with positive amounts | Not a losing bid, profit margin, or recommended winning price |
| Comparable-case distribution | Compatible procurement category, method, period, and scope | Show samples; do not mix incompatible cases |
| Announcement relationship chart | Source-supported agency, programme, and organization links | Keep award, approval, and payment meanings separate |
| Contract terms and public opportunities | Published performance dates, procurement notices, and grant announcements | Expiry does not guarantee renewal, new procurement, or future funds |

Winning rates require a verified denominator that includes valid unsuccessful bids.
With award announcements alone, the product shows award counts.
Agency and case evidence cannot establish personal evaluator preferences or political relationships.
Network and Sankey charts require source-supported relationship labels and table alternatives.

## Price hypotheses and purchase scope

The currency symbol NT$ means New Taiwan dollars.
These prices come from the user's proposal and remain test hypotheses.
Charging is not enabled by this plan.

| Offer | Proposed price | Proposed rights |
| --- | --- | --- |
| Public reading | Free | Publishable public-topic analysis and current-year basics for other organizations |
| Professional subscription | NT$999 monthly or NT$7,990 yearly | Available historical web analysis and comparisons, without separate per-query charges |
| Standalone export | NT$499 per purchase | One confirmed organization or industry query, data version, date range, and Excel detail file |

Prepared exports are sold separately from subscriptions.
A subscription does not imply unlimited bulk downloads or API access.
The first release has no undefined premium-membership tier.
Future bundled export allowances require commercial evidence.

Before checkout, show available years, fields, row counts, missing data, and a nonrestricted format sample.
Deliver the purchased data version with its source information.
Checkout terms must define download expiry, retries, refunds, and tax presentation before live use.
Do not begin live charging from a static demonstration.

Ten-year history is a coverage target, not a verified capability.
The original 2020–2026 range contains seven calendar years.
The 2026 year was incomplete at the direction decision.
Published coverage must come from the actual data version, not a permanent hardcoded promise.

## International comparisons and their limits

The retained source notes were reviewed on 2026-10-25.
They describe provider statements, not independent commercial audits.
A further source review on 2026-10-27 confirmed the limited statements below.

| Comparator | Primary evidence | Useful design direction | Limit |
| --- | --- | --- | --- |
| OpenTheBooks | [Official introduction](https://www.openthebooks.com/about-us/) describes American Transparency and public-spending research | Citable public topics and traceable records | Nonprofit reach does not prove subscription conversion or low maintenance cost |
| Deltek GovWin IQ | [Product page](https://www.deltek.com/products/govwin/) and [early-intelligence article](https://www.deltek.com/resources/articles/deltek-business-development-growth-ai/) describe procurement research and analyst contacts | Dated contract, budget, and announcement research | Historical public data alone does not reproduce analyst intelligence |
| GovDash | [Funding announcement](https://www.govdash.com/blog/press-govdash-raises-30m-series-b-to-help-companies-win-and-manage-government-contracts-with-ai) describes opportunity, bid, and contract workflows | Deliver directly useful structured records and source packages | Funding does not prove profit, Taiwan demand, or this product's access model |

The following references informed the approved first customer decision.
Their official pages were retrieved on 2026-10-27.

| Comparator | Primary evidence | Design used for the approved decision | Limit |
| --- | --- | --- | --- |
| Tussell | [Official supplier FAQ](https://www.tussell.com/faqs) describes sales, business development, and account research for government suppliers | Start with experienced government suppliers and a clear business user | Its audience does not prove demand in the selected Taiwan segment |
| Stotles | [Big Blue Door customer case](https://www.stotles.com/customer/big-blue-door), published 2024-10-14, describes paid adoption and market research from contract records | Support research on peer contracts and buying agencies | The reported results are claims from a provider case, not independent causal evidence |
| HigherGov | [Market intelligence page](https://www.highergov.com/market-intelligence/) describes agency and award analysis with Excel downloads; [pricing](https://www.highergov.com/pricing/) lists commercial plans | Connect case research, comparison, and traceable exports | Published features and prices do not establish profitability or our minimum viable scope |

The Taiwan pilot is an approved local design derived from these references.
The pilot requires local source and customer validation.

OpenTheBooks reports an annual budget of approximately US$2.7 million.
That figure is organizational context, not this product's cost estimate.
Its [2023 annual report](https://www.openthebooks.com/assets/1/6/AR_otb.com_final2.pdf) remains a historical source reference.
No tool-launch date from that report is necessary to this plan.

Deltek advertises intelligence up to five years before a request for proposal.
Its account includes analysts obtaining information from government contacts.
It does not establish certain predictions from public files alone.
The reviewed pages do not establish an average annual price of US$29,000.

GovDash announced US$30 million in Series B funding in January 2026.
It reported sixteenfold revenue growth since its Series A.
These are provider statements about that company, not proof of this product's demand or profitability.
They do not establish a universal delivery-time guarantee.

The reviewed primary sources do not establish the same free-public-topic and paid-other-organization strategy.
This product must validate that access model independently.

## Taiwan source candidates and trust

Official procurement notices, government open data, and formal agency disclosures are candidate sources.
A discovery link does not prove licensed bulk access, complete years, usable raw files, or accurate organization matching.
Central and local enterprise-grant sources require separate audits.

Two retained examples show why coverage needs individual verification.
The [major procurement supplier dataset](https://data.gov.tw/dataset/7264) covers recent-week major announcements still in performance.
It is not complete historical procurement.
The [Workforce Development Agency grant dataset](https://data.gov.tw/dataset/143623) covers a specific agency and reporting periods.
Its cumulative amount fields cannot simply be added across quarters.

These examples were metadata inspections, not ingested product datasets.
Raw files, licences, actual years, gaps, and updates remain subject to source validation.
Personal recipients in mixed source files remain outside the product recipient directory.

Preserve source versions, original fields, identifiers, aliases, corrections, cancellations, multiple awards, and uncertain matches.
Show currency, units, date basis, coverage, and missing-data status with results.
Keep procurement budgets, awards, grant approvals, cumulative disbursements, and verified payments separate.
Until duplicate funding is resolved, omit unsupported combined totals.
Use neutral descriptions and a correction channel for disputed public topics.

## Growth and operating-cost hypotheses

Candidate growth channels include public data topics, industry analysis, and citable charts.
Current events can suggest a topic but do not guarantee reliable reporting within one hour.
Social attention is not sales evidence.
A shared weekly report can be an open webpage rather than a personal notification.
Outreach, campaigns, social-account use, and publication require their applicable authorization.

Research separates topic readership, business queries, payment intent, actual purchases, refunds, and renewals.
It uses anonymous aggregate results without cross-site personal tracking.
The protocol must define the sample, period, and adopt-or-revise thresholds before testing.
Actual conversion tests require the verified product.

Costs include source access, licences, format changes, identity matching, manual checks, corrections, payment fees, cloud services, support, and editing.
Static output can reduce some computation but does not prove low total maintenance cost.
Revenue analysis must include these costs, yearly discounts, and refunds.
There is no supported revenue forecast yet.

## Architecture and delivery boundary

Public introductions, topics, and publishable records use static outputs with precomputed preparation and summaries.
Cloudflare static hosting is the target.
Actual products, build commands, output directories, payment services, and destinations require selection and verification.

Real paid access requires server-side payment verification, current access rights, and private exports.
Public data files or visual masking cannot protect restricted records.
Public caches must not mix responses between purchase rights.
Expiry and refunds must remove future access where the purchase terms require it.

The intended flow supports organization search, source interpretation, access decisions, and authorized analysis or export retrieval.
Mobile use, keyboard use, table alternatives, partial years, and missing data remain part of acceptance.
The [delivery stages](DELIVERY_STAGES.md) define separate data, product, and commercial gates.
Epics [#14](https://github.com/x168/dulan/issues/14), [#15](https://github.com/x168/dulan/issues/15), [#16](https://github.com/x168/dulan/issues/16), [#17](https://github.com/x168/dulan/issues/17), and [#18](https://github.com/x168/dulan/issues/18) own the remaining product delivery.
