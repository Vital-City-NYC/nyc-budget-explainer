# 05. The $100 series: audited fiscal 2000-2025 and budgeted 2026-2027

Compiled 2026-10-02. This file covers every number in `data/revenue_per_100.json`, which movement 1 and movement 3 draw. The series is built by the `nyc-budget-per-capita` repo (https://github.com/joshgreenman1973/nyc-budget-per-capita; `scripts/extract_acfr.py`, `scripts/extract_omb.py`, `scripts/build_series.py`), whose build fails if any bucket sum differs from the total the source report prints. Both source PDFs are in that repo's `data/raw/` and were read directly here with PyMuPDF.

## A. Audited years: Comptroller's Annual Comprehensive Financial Report

Source for fiscal 2016-2025: NYC Comptroller, *Annual Comprehensive Financial Report for Fiscal Year 2025*, Part III Statistical Information, "General Fund Revenues and Other Financing Sources, Ten Year Trend", printed pp. 396-402 (PDF pp. 430-436). https://comptroller.nyc.gov/wp-content/uploads/documents/ACFR-2025-7-28-2026.pdf. Earlier years come from the same schedule in the 2020, 2015 and 2005 reports (URLs in that repo's `scripts/fetch_sources.sh`: CAFR2020.pdf, CAFR2015.pdf, cafr2005.pdf on comptroller.nyc.gov).

Fiscal 2025 cells, verbatim labels and values (in thousands), PDF p. 430-436:

| ACFR label | FY2025 ($000) | Page bucket |
|---|---|---|
| "Taxes (Net of Refunds): Real Estate Taxes" | 34,756,900 | property_tax |
| "Sales and Use Taxes (Net of Refunds): General Sales" | 10,364,782 | sales_tax |
| "Cigarette" / "Commercial Motor Vehicle" / "Mortgage" / "Auto Use" / "Other" | 12,802 / 65,886 / 773,174 / 29,555 / 17,999 | sales_tax |
| "Total Sales and Use Taxes" | 11,264,198 | sales_tax |
| "Personal Income Taxes (Net of Refunds)" | 16,102,462 | personal_income_tax |
| "Other Income Taxes (Net of Refunds): General Corporation" | 7,365,442 | business_taxes |
| "Financial Corporation" / "Business Tax Suspense Account" / "Unincorporated Business" / "Pass-through Entity Tax" / "Personal Income— (Non-Resident City Employees)" / "Utility" | 21,724 / 1,215 / 3,641,035 / 2,363,772 / 243,695 / 482,526 | business_taxes |
| "Total Other Income Taxes" | 14,119,409 | business_taxes |
| "Other Taxes: Payments in Lieu of Taxes" | 865,443 | other_taxes |
| "Hotel Room Occupancy" / "Commercial Rents" / "Conveyance of Real Property" / "Beer and Liquor Excise" / others | 791,568 / 1,010,198 / 1,255,560 / 22,582 | other_taxes |
| "Total Other Taxes" | 3,897,773 | other_taxes |
| "Total Penalties and Interest on Delinquent Taxes" | 174,718 | other_taxes |
| "Total Taxes" | 80,315,460 | |
| "Total Federal Grants" | 9,082,951 | federal_aid |
| "Total State Grants" | 20,022,019 | state_aid |
| "Total Non-Governmental Grants" | 796,351 | fees_fines_other |
| "Total Unrestricted Federal and State Aid" | 52,693 | fees_fines_other |
| "Total Charges for Services" | 3,501,088 | fees_fines_other |
| "Investment Income" | 640,780 | fees_fines_other |
| "Total Licenses, Permits, Privileges and Franchises" | 736,942 | fees_fines_other |
| "Total Fines and Forfeitures" | 1,424,628 | fees_fines_other |
| "Miscellaneous" | 641,850 | fees_fines_other |
| "Pollution Remediation— Bond Sales" / "Transfer from General Debt Service Fund" / "Transfer from Nonmajor Debt Service Fund" | 205,907 / 42,039 / 203,542 | fees_fines_other (other_financing 451,488) |
| provision for disallowances | (6,534) | fees_fines_other |
| "Total Revenues" | "$117,659,716" | |

Quote, PDF p. 436: "Total Revenues. . . . . . . . . .  $117,659,716 $112,814,233 $108,237,610 $107,228,653 $99,587,211 $95,058,142" and "Source: Annual Comprehensive Financial Reports of the Comptroller."

Check: 34,756,900 + 11,264,198 + 16,102,462 + 14,119,409 + (3,897,773 + 174,718) + 20,022,019 + 9,082,951 + 8,239,286 = 117,659,716. Per $100: 29.54 / 9.57 / 13.69 / 12.00 / 3.46 / 17.02 / 7.72 / 7.00.

So the audited report itself files mortgage recording, cigarette and auto-use taxes under "Sales and Use Taxes", and files the pass-through entity tax (PTET), utility tax and the non-resident employee tax under "Other Income Taxes". The page's buckets follow the audited report.

## B. Budgeted years: OMB adopted budget, fiscal 2027

Source: NYC Office of Management and Budget, *Adopted Budget Fiscal Year 2027, Expense Revenue Contract*, June 2026, PDF p. 5 (revenue summary, three columns: FY2026 as adopted, FY2026 as modified, FY2027 adopted). https://www.nyc.gov/assets/omb/downloads/pdf/adopt26/erc6-26.pdf

Verbatim lines (FY2026 as modified, FY2027 adopted):
- "General Property . . . $35,386,000,000 ... $37,190,000,000"
- "General Sales . . . 11,016,000,000 ... 11,503,000,000"
- "Personal Income . . . 20,724,000,000 ... 20,688,000,000"
- "General Corp . . . 7,289,000,000 ... 7,586,000,000"
- "Commercial Occupancy . . . 950,000,000 ... 974,000,000"
- "Second Home Surcharge . . . --- ... 500,000,000"
- "Utility . . . 517,000,000 ... 562,000,000"
- "Unincorporated Business . . . 3,735,000,000 ... 3,855,000,000"
- "Real Property Transfer . . . 1,493,000,000 ... 1,514,000,000"
- "Mortgage Recording . . . 984,000,000 ... 1,061,000,000"
- "Tax Audit Revenues . . . 1,148,666,000 ... 928,666,000"
- "Cigarette . . . 11,000,000 ... 12,000,000"
- "Cannabis Tax . . . 25,000,000 ... 32,000,000"
- "Hotel . . . 810,000,000 ... 843,000,000"
- "Other . . . 1,509,831,000 ... 1,357,281,000"
- "City Tax Programs . . . --- ... 68,000,000"
- "Total Taxes . . . $85,598,497,000 ... $88,673,947,000"
- "Water and Sewer Charges . . . 2,310,781,000 ... 2,392,139,000" (inside Miscellaneous Revenues)
- "Fines and Forfeitures . . . 1,472,865,000 ... 1,334,491,000"

Mapping of OMB lines into the page's buckets (done in the repo's `build_series.py`, checked here against the JSON):

| Bucket | OMB lines | FY2027 ($M) |
|---|---|---|
| property_tax | General Property | 37,190 |
| personal_income_tax | Personal Income (OMB includes PTET here) | 20,688 |
| sales_tax | General Sales + Mortgage Recording + Cigarette | 11,503 + 1,061 + 12 = 12,576 |
| business_taxes | General Corp + Unincorporated Business + Utility | 7,586 + 3,855 + 562 = 12,003 |
| other_taxes | Commercial Occupancy, Second Home Surcharge, Real Property Transfer, Tax Audit Revenues, Cannabis, Hotel, Other, City Tax Programs | 6,217 |
| state_aid | State categorical grants | 20,813 |
| federal_aid | Federal categorical grants | 7,374 |
| fees_fines_other | Miscellaneous revenues, unrestricted aid, other categorical grants, inter-fund agreements, less intra-city revenue and disallowances | 9,381 |
| total | | 126,242 (= budget total expense; the budget balances) |

The one known break between the audited and budgeted years: the audited report counts the PTET (fiscal 2025: $2,363,772 thousand) as a business tax; OMB counts it inside personal income tax. That alone moves about $2 of every $100 from business taxes to the income tax between fiscal 2025 and 2026. Tax audit revenue is a separate OMB line (filed under other taxes here) but is folded into each tax in the audited report.

Cross-check with the Comptroller's reproduction of the same plan (research/03, Table A1): Real Property $37,300 (OMB table shows 37,190; the Comptroller's figure includes the STAR reimbursement per its footnote 7), PIT and PTET 20,688, GCT 7,586, UBT 3,855, Sales and Use 11,503, Total Taxes $88,674, Total Federal Grants $7,374, Total State Grants $20,813. All match except the property tax presentation.

## C. Self-audit
- HIGH: every FY2025 cell above (read from the ACFR PDF, page numbers given) and every OMB line (read from erc6-26.pdf p.5).
- Derived: per-$100 shares, bucket sums.
- Editorial: the eight buckets and the decision to file PTET where each source files it rather than restate either.
