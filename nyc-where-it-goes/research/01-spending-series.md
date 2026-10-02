# 01. The $100 of spending: audited fiscal 2000-2025 and budgeted 2026-2027

Compiled 2026-10-02. Covers every number in `data/spending_per_100.json` (movement 1 and the in-place agency splits) and the off-budget strip. Built from the same `nyc-budget-per-capita` pipeline as the revenue page (see ../nyc-who-pays/research/05-revenue-series.md), whose build fails if a function sum differs from the total the report prints.

## A. Audited years: Comptroller's ACFR, General Fund expenditures

Source for fiscal 2016-2025: NYC Comptroller, *Annual Comprehensive Financial Report for Fiscal Year 2025*, Part III Statistical Information, "General Fund Expenditures and Other Financing Uses by Function, Ten Year Trend" (totals) and the General Fund expenditure schedule by agency (PDF pp. 438-456). https://comptroller.nyc.gov/wp-content/uploads/documents/ACFR-2025-7-28-2026.pdf. Earlier years from the 2020, 2015 and 2005 reports.

Fiscal 2025 subtotals, verbatim labels and values (in thousands), with PDF page:

| ACFR line | FY2025 ($000) | PDF p. | Page bucket |
|---|---|---|---|
| "Total General Government" | 5,111,504 | 448 | general_government |
| "Total Public Safety and Judicial" | 12,838,701 | 450 | public_safety |
| Department of Education (040) | 34,051,680 | 450 | education |
| "Total City University" | 1,261,522 | 452 | everything_else |
| "Total Social Services" | 20,642,060 | 452 | social_services |
| "Total Environmental Protection" | 3,632,911 | 452 | environmental |
| Total Transportation Services | 2,754,999 | 452 | everything_else |
| "Total Parks, Recreation, and Cultural Activities" | 848,435 | 454 | everything_else |
| "Total Housing" | 2,092,768 | 454 | everything_else |
| "Total Health" | 5,476,794 | 454 | health |
| "Total Libraries" | 500,156 | 454 | everything_else |
| "Pensions: 095 Pension Contributions" | 9,915,575 | 456 | pensions |
| "Judgments and Claims" | 1,376,184 | 456 | benefits |
| Fringe Benefits and Other Benefit Payments | 8,688,731 | 456 | benefits |
| "Lease Payments" | 85,865 | 456 | benefits |
| "Other: 098 Miscellaneous" | 332,272 | 456 | benefits |
| "Total Expenditures" | 109,610,157 | 456 | |
| "Transfers : General Debt Service Fund: 099 Debt Service" | 3,801,162 | 456 | debt_service |
| "Miscellaneous—Building Aid Revenue Bonds" / "Miscellaneous—Future Tax Secured" | 3,504,206 / 774,647 | 456 | debt_service |
| "Total Transfers" | 8,080,015 | 456 | debt_service |
| "Total Expenditures and Other Financing Uses" | 117,690,172 | 456 | total |

Check: the ten buckets sum to 117,690,172 in every audited year (the build asserts it). The Comptroller's release on the fiscal 2025 report, quoted in the per-capita repo's README, gives "expenditures of $117.690 billion".

Agency rows inside each bucket are the schedule's own lines, e.g. PDF p. 450: "056 Police Department 6,610,389", "057 Fire Department 2,836,440", "072 Department of Correction 1,303,643", "128 Office of Criminal Justice 960,198"; p. 452: "069 Department of Social Services 13,136,965", "071 Department of Homeless Services 3,595,168", "068 Administration for Children's Services 3,356,362"; p. 454: "819 Health and Hospitals Corporation 3,094,557", "816 Department of Health and Mental Hygiene 2,382,237". The agency-to-function map (`data/agency_map.json`) is read from the headings of that schedule.

## B. Budgeted years: OMB adopted budget, fiscal 2027

Source: OMB, *Adopted Budget Fiscal Year 2027, Expense Revenue Contract*, June 2026, https://www.nyc.gov/assets/omb/downloads/pdf/adopt26/erc6-26.pdf: the citywide summary (PDF p. 5, "Total Expenditures" by agency groups) and the 141 agency tables that follow. Fiscal 2026 is the "As Modified" column, fiscal 2027 the adopted column. Each agency is assigned to a function with the ACFR's own classification of agency codes; pseudo-agencies 095 (pension contributions), 098 (Miscellaneous, mostly fringe benefits) and 099 (debt service) map to pensions, benefits and debt service. Totals: fiscal 2026 as modified $126,810,081,450; fiscal 2027 adopted $126,241,596,044 (the budget's printed net total expense, which equals its revenue: the budget balances by law).

Known break between audited and budgeted years: OMB's Miscellaneous budget (098) carries fringe benefits plus judgments, reserves and other citywide costs, so the "benefits" bucket runs higher in budget years (about $12 of every $100) than in the audited books (about $9), where some of those costs are booked to agencies once spent.

## C. Off-budget strip

- Bonds issued, fiscal 2025: ACFR PDF p. 426 (governmental funds, other financing sources), "Principal amount of bonds issued 15,518,392" and "Bond premium 1,562,536" (thousands); "Other financing sources - refunding debt issued: 6,970,750".
- Capital Projects Fund expenditures, fiscal 2025: ACFR Schedule CP2, PDF p. 462 on; total capital expenditures 15,578,006 (thousands) per the per-capita series (`capital_total`), e.g. "Total General Government 1,446,293".
- Debt outstanding: ACFR PDF p. 488, "Ratios of Outstanding Debt by Type—Ten Year Trend", fiscal 2025 row: "2025 46,721 63,013 879 42 — — 2,521 258 — 113,434 7,597 121,031 12,134" (dollars in millions: general obligation bonds 46,721; TFA 63,013; gross debt 113,434; net of premiums 121,031; lease obligations 12,134).
- Out-year gaps: NYC Comptroller, *Comments on New York City's Fiscal Year 2027 Adopted Budget*, Aug 12, 2026, p. 46: "While the FY 2027 budget is, as required by law, balanced, the June 2026 Plan presents budget gaps of $6.44 billion in FY 2028, $8.21 billion in FY 2029, and $8.52 billion in FY 2030." https://comptroller.nyc.gov/wp-content/uploads/documents/Comments-on-New-York-Citys-Fiscal-Year-2027-Adopted-Budget.pdf
- Water and sewer: the Water Board's payment to the city appears as revenue in the operating budget, OMB erc6-26.pdf p. 5, "Water and Sewer Charges ... 2,392,139,000" (fiscal 2027). More in 02-what-the-mayor-controls.md.

## D. Self-audit
- HIGH: every ACFR line above (labels and values read from the extraction with page numbers, cross-checked against the PDF); OMB totals; Comptroller gap sentence.
- Derived: per-$100 shares; "top five agencies plus everything else" within a bucket; debt per resident (121,031 million over the Census 2025 estimate of 8,584,629 used in the per-capita repo).
- Editorial: the ten buckets. Judgments, lease payments and the Miscellaneous line are folded into "health insurance, claims and other benefits" because fringe benefits dominate that group.


## E. Cross-check against IBO, "NYC's Budget in $100" (October 2025)

IBO published the same device for the fiscal 2026 adopted budget ($115.9 billion, June 2025), using the Comptroller's budget categories. Local copy read: /Users/joshgreenman/Downloads/100-city-budget.pdf. Its figures: "Education $29.71", "Human Services $16.37", "Miscellaneous $13.18", "City Employee Pensions $8.90", "Public Safety & Judicial $10.11", "General Government $5.48", "Debt Service $4.14", "Environmental Protection $3.18", "Health $3.49", "Housing $1.56", "City University $1.32". IBO notes "City funds account for the largest share of revenue in the City's general fund (over 80%)".

This page's fiscal 2026 row is the June 2026 modified budget ($126.8 billion), not the June 2025 adopted one, and folds judgments and lease payments into benefits, so the two are not identical. Same order of magnitude throughout: schools 29.65 vs 29.71; social services 19.07 vs 16.37 (federal and state aid for asylum seekers and shelter recognized during the year); pensions 7.65 vs 8.90 and benefits 11.38 vs 13.18 (the Miscellaneous budget shrinks as reserves are spent); public safety 10.23 vs 10.11; debt service 5.11 vs 4.14 (prepayments move it between years); general government 4.48 vs 5.48; environmental 3.36 vs 3.18; health 3.66 vs 3.49. No successor IBO "$100" document for fiscal 2027 was found as of October 2, 2026.
