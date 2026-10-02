# 03. Context facts for the ten spending buckets

Compiled 2026-10-02. Every number below was read in a document or dataset downloaded to the scratchpad (PDF text via PyMuPDF, XLSX via openpyxl), except the three rows marked "via WebFetch extraction." Derived arithmetic is labeled as such and kept out of the JSON unless both inputs are quoted.

Main sources (local copy, MD5 of the live file):
- MMR = Mayor's Management Report, Fiscal 2026 (September 2026, covers July 1, 2025 to June 30, 2026): https://www.nyc.gov/assets/operations/downloads/pdf/mmr2026/2026_mmr.pdf (`mmr2026.pdf`, 2f6d36edf090b361559bf5fbb8e30768). Page numbers are PDF pages.
- ACFR = Comptroller's Annual Comprehensive Financial Report, FY2025: https://comptroller.nyc.gov/wp-content/uploads/documents/ACFR-2025-7-28-2026.pdf (`acfr2025.pdf`, 972e533108e31b2da2be30d59d97264f)
- CPT27 = Comptroller, Comments on NYC's FY2027 Adopted Budget, Aug. 12, 2026: https://comptroller.nyc.gov/wp-content/uploads/documents/Comments-on-New-York-Citys-Fiscal-Year-2027-Adopted-Budget.pdf (`comptroller_fy27_adopted.pdf`, 3589fdd5b8e6880f37a3b804d447f974)
- DEBT = Comptroller, Annual Report on Capital Debt and Obligations, FY2026 (Dec. 1, 2025): https://comptroller.nyc.gov/wp-content/uploads/documents/Annual-Report-on-Capital-Debt-and-Obligations-Fiscal-Year-2026-1.pdf (`debt_fy2026.pdf`)
- CENSUS-ED = Census Bureau, 2024 Annual Survey of School System Finances, summary tables: https://www2.census.gov/programs-surveys/school-finances/tables/2024/secondary-education-finance/elsec24_sumtables.xlsx (`elsec24_sumtables.xlsx`); press release May 7, 2026: https://www.census.gov/newsroom/press-releases/2026/school-system-finances.html
- ASPEP = Census Bureau, 2024 Annual Survey of Public Employment and Payroll, individual unit file: https://www2.census.gov/programs-surveys/apes/datasets/2024/2024_individual_unit_files.zip (`apes/24emp.xlsx`); payroll is for March 2024.

## 1. Education

| Fact | Year | Source | Verbatim |
|---|---|---|---|
| NYC current spending per pupil $35,796, highest of the 100 largest districts; national average $17,619 | FY2024 | Census press release | "public school current spending per pupil rose 6.6% from $16,526 in fiscal year (FY) 2023 to $17,619 in FY 2024" ... "New York City School District in New York ($35,796) had the highest current expenditures per pupil in FY 2024" |
| Peers, Table 18 (rank, system, enrollment, current spending per pupil) | FY2024 | CENSUS-ED Table 18 | NYC: `1, New York City, New York, 845509, 35795.73`; `2, Los Angeles Unified, California, 419929, 25631.25`; `4, Chicago, Illinois, 322809, 24330.40`; `10, Houston, Texas, 184109, 13950.23`; `21, Philadelphia, Pennsylvania, 117907, 19525.17`; `3, Miami-Dade County, Florida, 335500, 13931.50`; `82, District of Columbia, 50839, 31529.36`. Table 8 US row: `United States, 17619.39`; New York State `31917.51` |
| NYCPS serves "nearly one million students"; DOE personnel 152,698 | FY2026 | MMR p281, p296 | "provides primary and secondary education to nearly one million students, from early childhood through grade 12" ... "in approximately 1,600 schools in 32 school districts and District 75"; Agency Resources "Personnel | 141,748 | 141,594 | 143,663 | 147,565 | 152,698" (FY22-FY26 actual); "Expenditures ($000,000) | $31,558.0 | $31,505.5 | $33,367.6 | $34,672.3 | $37,709.6" |
| Education is 27.1% of the FY2027 adopted budget | FY2027 | CPT27 p.44 | "The Adopted Budget for FY 2027 totals $125.84 billion. Just over a quarter of the total budget ($34.11 billion or 27.1 percent) is allocated for education spending, which includes funding the Department of Education (DOE) and the City University of New York (CUNY)" |

Note: Census enrollment (845,509) counts the district's fall enrollment as reported to Census; MMR's "nearly one million" includes 3-K, pre-K and charter students. Do not mix the two.

## 2. Social services

| Fact | Year | Source | Verbatim |
|---|---|---|---|
| 85,066 people in DHS shelters per day on average (86,403 in FY2025; 45,563 in FY2022) | FY2026 | MMR p264 | "« Average number of individuals in shelter per day | 45,563 | 66,195 | 86,321 | 86,403 | 85,066" |
| 566,500 people on cash assistance, June 2026 | June 2026 | MMR p239 | "The number of persons receiving Cash Assistance (CA) was 566,500 in June 2026, six percent lower than in June 2025" ... "« Cash Assistance — Persons receiving Assistance (000) | 425.0 | 481.5 | 557.6 | 601.1 | 566.5" |
| City Medicaid payment $6.763B (FY2026), $6.790B (FY2027) | FY2026-27 | CPT27 Table 13, p.45 | "Table 13. FY 2027 Expenditures vs. FY 2026 Expenditures Adjusted for Prepayments ($ in millions)" ... "Medicaid | $6,763 | $6,790 | $27 | 0.4%" |
| Social service agencies are 18.6% of the FY2027 budget | FY2027 | CPT27 p.44 | "followed by $23.37 billion for the City's social service agencies (18.6 percent)" |

## 3. Public safety (police, fire, courts, jails)

| Fact | Year | Source | Verbatim |
|---|---|---|---|
| Full-time sworn officers (ASPEP "Police Protection - Persons with Power of Arrest"), with the population in the file | March 2024 | ASPEP `24emp.xlsx` | New York `32910` (flag T), pop `8335897`; Chicago `11474` (R), pop `2665039`; Los Angeles `8979` (R), pop `3822238`; Philadelphia `5433` (R), pop `1567258`; Houston `5889` (flag G = imputed, do not use) |
| Derived officers per 1,000 (my arithmetic from the row above) | March 2024 | derived | NYC 3.9, Chicago 4.3, Philadelphia 3.5, Los Angeles 2.3. Flag T = "Respondent reports totals and these data are pro-rated based on the prior year distribution." |
| National benchmark: departments serving 1 million+ residents average 3.0 officers per 1,000 | 2020 | BJS, Local Police Departments Personnel, 2020, https://bjs.ojp.gov/sites/g/files/xyckuh236/files/media/document/lpdp20_emb.pdf p.4 | "Departments serving 1 million or more residents had 3.0 officers per 1,000 residents on average" |
| NYPD uniformed headcount 34,018 (FY2026); 33,614 (FY2025) | FY2026 | MMR p65; ACFR p510 | MMR: "Personnel (uniformed) | 34,825 | 33,797 | 33,812 | 33,614 | 34,018"; ACFR "Number of Full Time Employees—Ten Year Trend": Police "Uniformed . . . 33,614 | 33,812 | 33,797 | 34,825 | 34,858 | 35,910" (FY2025 back to FY2020) |
| Jail average daily population 6,954; DOC spending $1.38B; DOC uniformed staff 5,777 | FY2026; FY2025 | MMR p90, p94; ACFR p510 | "® Average daily population | 5,559 | 5,873 | 6,206 | 6,823 | 6,954"; "Expenditures ($000,000) | $1,391.8 | $1,357.4 | $1,277.6 | $1,356.2 | $1,379.9"; ACFR Correction "Uniformed . . . 5,777 | 5,954 | 6,299 | 7,068 | 8,388 | 9,237" |
| Cost per incarcerated person $556,539 a year, $1,525 a day | FY2021 | Comptroller release Dec. 6, 2021, https://comptroller.nyc.gov/newsroom/comptroller-stringer-cost-of-incarceration-per-person-in-new-york-city-skyrockets-to-all-time-high-2/ (via WebFetch extraction) | "The City now spends $556,539 to incarcerate one person for a full year, or $1,525 per day" ... "Including additional costs outside the DOC budget, such as employee fringe benefits and health care expenses for the incarcerated population" ... "nearly quadrupling since FY 2011" |

No newer official cost-per-person figure found: the Comptroller's March 2022 release repeats the FY2021 number, and the Council Finance Division's June 2026 DOC report (downloaded) has no per-person cost. A comparison to other jail systems exists only as the 2022 release's unquantified phrase "far exceeding other jail systems in the country." UNVERIFIED beyond that.

## 4. Pensions

| Fact | Year | Source | Verbatim |
|---|---|---|---|
| Pension contributions $9.707B (FY2026), $8.707B (FY2027), on a $125.84B budget | FY2026-27 | CPT27 Table 13, p.45; p.44 | "Pensions | 9,707 | 8,707 | (1,000) | (10.3%)"; "The year-over-year decline in pension costs is largely due to the re-amortization of the pension unfunded accrued liability (UAL) included in the Enacted State FY 2027 budget and approved by four of the five City's pension funds" ... "The New York City Police Pension Fund did not approve the change." Derived share: 8,707 / 125,840 = 6.9%. |
| Pensions + fringe = 19.4% of FY2027 budget | FY2027 | CPT27 p.44 | "Spending on fringe benefits and pensions for City employees and retirees account for another $24.36 billion (19.4 percent of the budget)" |
| Funded ratios ("Plan Fiduciary Net Position as a Percentage of Total Pension Liability") at June 30, 2025: POLICE 92.2%, FIRE 79.4%, NYCERS 87.66%, TRS 90.44%, BERS 102.56% | June 30, 2025 | ACFR pp.196, 198, 200 | POLICE: "92.2% | 89.3% | 85.8% | 84.2% | 96.6%" (2025 to 2021); FIRE: "79.4% | 75.8% | 72.8% | 71.0% | 80.0%"; NYCERS "87.66% | 84.25%"; TRS "90.44% | 85.71%"; BERS "102.56% | 97.43%" (2025, 2024) |
| 361,394 retirees and beneficiaries receiving benefits; 378,991 active members | June 30, 2024 | ACFR p179 | "QPP Membership at June 30, 2024 / Retirees and Beneficiaries Receiving Benefits . . . 173,106 | 94,612 | 21,550 | 55,124 | 17,002 | 361,394" (NYCERS, TRS, BERS, POLICE, FIRE, Total); "Active Members . . . 184,126 | 126,251 | 24,120 | 33,803 | 10,691 | 378,991" |

## 5. Health insurance, claims and other benefits

| Fact | Year | Source | Verbatim |
|---|---|---|---|
| Health insurance $10.581B (FY2026), $10.862B (FY2027) | FY2026-27 | CPT27 Table 13, p.45 | "Health Insurance | 10,581 | 10,862 | 281 | 2.7%" |
| Retiree health (OPEB) participants: 288,479 active, 260,016 receiving benefits; OPEB liability $101.7B, 5.1% funded | June 30, 2024 (count); June 30, 2025 (liability) | ACFR p168, p170 | "Active plan members | 288,479 | 287,342"; "Inactive plan members or beneficiaries currently receiving benefits | 260,016 | 257,331"; "the OPEB Plan's Fiduciary Net Position as a percentage of the Total OPEB liability was 5.1%. The total OPEB liability for benefits was $101.7 billion" |
| Judgments and claims actually spent $1.376B in FY2025 (budgeted $877M) | FY2025 | ACFR p60 | General Fund Expenditures FY2025, Adopted / Modified / Actual: "Judgments and claims (JC) . . . 877 | 1,282 | 1,376" |
| Claims resolved $1.94B on 13,397 claims, the most ever | FY2024 | Comptroller release Apr. 30, 2025, https://comptroller.nyc.gov/newsroom/comptroller-landers-new-dashboard-tracks-city-claims-city-paid-nearly-2b-in-settlements-last-fiscal-year/ (via WebFetch extraction) | "In FY 2024, 13,397 claims against New York City were resolved for $1.94 billion, the most ever for one fiscal year, up from $1.5 billion in FY 2023." ... "NYPD settlements totaled $309.51 million" |
| J&C budget $1.266B (FY2026), $1.148B (FY2027) | FY2026-27 | CPT27 Table 13 | "Judgments and Claims | 1,266 | 1,148 | (118) | (9.3%)" |

The Comptroller's Claims Dashboard replaced the annual Claims Report; its FY2025 totals are inside a Tableau embed I could not read. UNVERIFIED for FY2025 claim counts.

## 6. Debt service

| Fact | Year | Source | Verbatim |
|---|---|---|---|
| Debt service 10.2% of tax revenues (10.6% in FY2024; 15% ceiling); projected 14.2% by FY2033 | FY2025 | DEBT p.9 | "The share of tax revenues dedicated to debt service remains well below the 15.0 percent ceiling used to evaluate affordability as articulated in the City's Debt Policy and fell slightly from 10.6 percent in Fiscal Year 2024 to 10.2 percent in Fiscal Year 2025 due to a significant 8.3 percent year-over-year increase in tax revenues." ... "the share is projected to reach approximately 14.2 percent by Fiscal Year 2033" |
| Net debt $121,031M; total primary government debt $133,639M; $15,763 per capita; 17.95% of personal income | FY2025 | ACFR pp.488-489, "Ratios of Outstanding Debt by Type—Ten Year Trend" | "2025 46,721 63,013 879 42 — — 2,521 258 — 113,434 7,597 121,031 12,134" ... "2025 | 474 | 133,639 | 17.95 | 15,763" (Conduit Debt, Total Primary Government, Percentage of Personal Income, Per Capita). Note (4): "Current Year Total Primary Government is divided by prior years City of New York population" (2024 population 8,478,072, p503) |
| Direct and overlapping debt per capita $12,402, second among 14 peer cities after Washington DC ($21,712); Chicago $6,659, Los Angeles $5,360, Philadelphia $4,869, Houston $4,410 | FY2024 | DEBT Table 19, p.47 | "Washington DC | 687,324 | $14,923,301 | $21,712 | New York City | 8,390,888 | 104,063,000 | 12,402 | San Francisco | 819,151 | 8,159,377 | 9,961" ... "Chicago | 2,699,144 | 17,973,817 | 6,659" ... "Los Angeles | 3,847,428 | 20,621,100 | 5,360 | Philadelphia | 1,563,349 | 7,611,500 | 4,869 | Houston | 2,346,908 | 10,370,010 | 4,410" ... "there is no assurance that the components of the data published in those exhibits are comparable" |
| Debt service $7.37B, 5.9% of the FY2027 budget | FY2027 | CPT27 p.44 | "Debt service costs to pay for the City's capital program account for $7.37 billion (5.9 percent)" |

## 7. Health and hospitals

| Fact | Year | Source | Verbatim |
|---|---|---|---|
| City support to H+H over $2.4B | FY2025 | NYS Comptroller (OSC), "NYC Health + Hospitals: Strategic Initiatives," Dec. 2025, https://www.osc.ny.gov/files/reports/pdf/nyc-health-hospitals-strategic-initiatives.pdf (`osc_hh_2025.pdf`) | "In FY 2025, the City provided H+H with over $2.4 billion. These funds were for collective bargaining costs, unrestricted subsidy, full financial support of Correctional Health Services, financial support for the NYC Care program and debt service on capital projects funded with the City's general obligation bonds for which the City does not expect reimbursement. This amounts to 145 percent growth over FY 2018" |
| H+H saw 1,170,529 unique patients; 215,554 uninsured; spending $13.19B | FY2026 | MMR p229, p231, p234 | "The total number of unique patients seen in the System decreased by less than two percent from 1,191,776 in Fiscal 2025 to 1,170,529 in Fiscal 2026"; "The System served 215,554 uninsured patients in Fiscal 2026"; "Expenditures ($000,000) | $12,742.1 | $10,878.7 | $12,414.4 | $13,027.5 | $13,189.9" |
| DOHMH spending $2.84B | FY2026 | MMR p212 (DOHMH Agency Resources) | "Expenditures ($000,000) | $2,613.2 | $2,335.5 | $2,344.3 | $2,452.2 | $2,840.2" |
| City-funded H+H budget line $1.645B (FY2026), $1.694B (FY2027) | FY2026-27 | CPT27 agency table, p.45 | "Health + Hospitals | 1,645 | 1,694 | 1,696 | 1,698 | 52 | 3.2%" (city funds; column headers are on the preceding page and were not captured, so use the OSC figure instead) |

## 8. General government

| Fact | Year | Source | Verbatim |
|---|---|---|---|
| 287,422 full-time city employees | FY2025 | ACFR p510 | "Number of Full Time Employees—Ten Year Trend" ... "Total . . . 287,422 | 283,971 | 281,917 | 282,498 | 291,101 | 300,446" (FY2025 to FY2020); "General Government . . . 15,073" |
| Authorized full-time headcount 307,199 | FY2027 | CPT27 p.46 | "Full-time authorized headcount for FY 2027 totals 307,199 in the Adopted Budget" |

## 9. Sanitation, water and sewers

| Fact | Year | Source | Verbatim |
|---|---|---|---|
| 3.13 million tons of refuse disposed; 719,000 tons recycled by DSNY; 19.7% diversion | FY2026 | MMR p153 | "DSNY disposed of 3.13 million tons of refuse in Fiscal 2026, a decrease of one percent from Fiscal 2025" ... "DSNY-collected recycled tons increased by seven percent, to 719,000 tons, and the DSNY-collected diversion rate rose one percentage point, to 19.7 percent"; "« Tons of refuse disposed (000) | 3,351.1 | 3,162.5 | 3,202.5 | 3,153.6 | 3,131.3" |
| Water and sewer are run off budget: the Water Board sets rates, pays Water Authority debt, and reimburses the city about $1.5B a year; DEP collected over $4.8B | FY2026 | ACFR p119; MMR p353 note 4, p350 | ACFR: "The Water Board leases the System from the City and sets and collects rates, fees, rents, and other charges for the use of, or for services furnished, rendered, or made available by the System to produce revenue sufficient to pay debt service on the Water Authority's bonds and to put the System on a self-sustaining basis." MMR: "DEP revenues shown here do not include any of the approximately $1.5 billion the City receives annually from the NYC Water Board in reimbursement for operations & maintenance and in rent." ... "In Fiscal 2026, the Department collected over $4.8 billion" |
| DSNY spending $2.36B; 8,170 uniformed sanitation workers | FY2026; FY2025 | MMR p155; ACFR p510 | "Expenditures ($000,000) | $2,040.3 | $1,919.3 | $1,977.8 | $2,057.9 | $2,361.1"; ACFR Sanitation "Uniformed . . . 8,170" |

## 10. Everything else (housing, transportation, CUNY, parks, libraries)

| Fact | Year | Source | Verbatim |
|---|---|---|---|
| NYCHA: 497,649 authorized residents, 177,565 apartments, 335 developments | FY2026 | MMR p423 | "provides affordable housing to 497,649 authorized residents in 177,565 apartments within 335 housing developments and units leased through the Section 8 program. NYCHA serves 275,546 authorized residents in 145,347 apartments within 216 housing developments through the conventional public housing program (Section 9)" |
| DOT: 6,300 miles of streets, 809 bridges, 4 tunnels, 11 ferries; 1,169 lane miles resurfaced | FY2026 | MMR p355, p358 | "responsible for the condition and operation of 6,300 miles of streets, highways, and public plazas, 809 bridges and four vehicular tunnels, and 11 Staten Island Ferry vessels"; "DOT's in-house crews resurfaced 1,169 lane miles of roadway" |
| CUNY: 246,503 students; 81,883 at community colleges; community college tuition $4,800 | FY2026 | MMR p325, p326 | "Total headcount enrollment increased four percent, from 237,671 in Fiscal 2025 to 246,503 in Fiscal 2026. At the community colleges, total enrollment increased seven percent, from 76,432 to 81,883."; "tuition remained the same at $4,800 for the community colleges and $6,930 for the senior colleges" |
| Parks: 2,000 parks, 1,000 playgrounds, 12,000 acres of natural areas, 5.6 million trees; $724M spending | FY2026 | MMR p159, p167 | "manages and cares for New York City's 2,000 parks, 1,000 playgrounds, 37 recreation centers, 66 pools, 800 basketball courts, 700 public restrooms, 12,000 acres of natural areas, 5.6 million trees, and 160 miles of shoreline"; "Expenditures ($000,000) | $588.2 | $614.3 | $639.0 | $650.8 | $724.2" |
| Libraries: 220 locations in three systems | FY2026 | MMR p317 | "The Libraries oversee 220 local library locations across the five boroughs of New York City, including five research library centers." |

Total parkland acreage (the familiar ~30,000 acres) is not in the MMR; UNVERIFIED, left out.

## Cross-city total spending per capita

Not done. The Lincoln Institute's Fiscally Standardized Cities database (data through 2022) is only available through an interactive query tool (https://apps.lincolninst.edu/data/fiscally-standardized-cities/access-fisc-database), and I found no Pew or Census table comparing NYC per-capita total spending with other big cities that I could read. The DEBT report's Table 19 (debt per capita, 14 peer cities) is the only readable cross-city table found. Caveat for any such comparison, in the Comptroller's words (DEBT p.5): "NYC's debt burden is relatively high compared to U.S. peer cities, but not unreasonably so when viewed in context."

## JSON

```json
{
  "education": [
    {"fact": "New York City schools spent $35,796 per pupil in fiscal 2024, the most of the 100 largest districts and about double the national average of $17,619.", "source": "Census Bureau, 2024 Annual Survey of School System Finances", "url": "https://www.census.gov/newsroom/press-releases/2026/school-system-finances.html"},
    {"fact": "Per-pupil current spending in fiscal 2024: New York City $35,796, Los Angeles $25,631, Chicago $24,330, Philadelphia $19,525, Houston $13,950.", "source": "Census Bureau, school finance Table 18", "url": "https://www2.census.gov/programs-surveys/school-finances/tables/2024/secondary-education-finance/elsec24_sumtables.xlsx"},
    {"fact": "The Department of Education spent $37.7 billion in fiscal 2026 and had 152,698 staff; it serves nearly one million students in about 1,600 schools.", "source": "Mayor's Management Report, Fiscal 2026", "url": "https://www.nyc.gov/assets/operations/downloads/pdf/mmr2026/2026_mmr.pdf"}
  ],
  "social_services": [
    {"fact": "An average of 85,066 people slept in Department of Homeless Services shelters each night in fiscal 2026, up from 45,563 in fiscal 2022.", "source": "Mayor's Management Report, Fiscal 2026", "url": "https://www.nyc.gov/assets/operations/downloads/pdf/mmr2026/2026_mmr.pdf"},
    {"fact": "566,500 New Yorkers were receiving cash assistance in June 2026, 6 percent fewer than a year earlier.", "source": "Mayor's Management Report, Fiscal 2026", "url": "https://www.nyc.gov/assets/operations/downloads/pdf/mmr2026/2026_mmr.pdf"},
    {"fact": "The city's own share of Medicaid is budgeted at $6.79 billion in fiscal 2027.", "source": "NYC Comptroller, Comments on the FY2027 Adopted Budget", "url": "https://comptroller.nyc.gov/wp-content/uploads/documents/Comments-on-New-York-Citys-Fiscal-Year-2027-Adopted-Budget.pdf"}
  ],
  "public_safety": [
    {"fact": "In March 2024 New York City had 32,910 full-time sworn police officers, Chicago 11,474, Los Angeles 8,979 and Philadelphia 5,433; against the populations in the same Census file that is about 3.9 officers per 1,000 residents in New York, 4.3 in Chicago, 3.5 in Philadelphia and 2.3 in Los Angeles.", "source": "Census Bureau, 2024 Annual Survey of Public Employment and Payroll", "url": "https://www2.census.gov/programs-surveys/apes/datasets/2024/2024_individual_unit_files.zip"},
    {"fact": "The city's jails held an average of 6,954 people a day in fiscal 2026; the Comptroller's last full costing, for fiscal 2021, put the cost at $556,539 per incarcerated person per year.", "source": "Mayor's Management Report, Fiscal 2026; NYC Comptroller, Dec. 2021", "url": "https://comptroller.nyc.gov/newsroom/comptroller-stringer-cost-of-incarceration-per-person-in-new-york-city-skyrockets-to-all-time-high-2/"},
    {"fact": "NYPD uniformed headcount was 34,018 in fiscal 2026, down from 35,910 in fiscal 2020.", "source": "Mayor's Management Report, Fiscal 2026; Comptroller's ACFR FY2025", "url": "https://www.nyc.gov/assets/operations/downloads/pdf/mmr2026/2026_mmr.pdf"}
  ],
  "pensions": [
    {"fact": "City pension contributions are $8.7 billion in the $125.8 billion fiscal 2027 budget, down $1 billion from fiscal 2026 after the state let four of the five funds stretch out their unfunded liability.", "source": "NYC Comptroller, Comments on the FY2027 Adopted Budget", "url": "https://comptroller.nyc.gov/wp-content/uploads/documents/Comments-on-New-York-Citys-Fiscal-Year-2027-Adopted-Budget.pdf"},
    {"fact": "As of June 30, 2025 the five funds held assets covering 92.2 percent of liabilities for Police, 79.4 percent for Fire, 87.7 percent for NYCERS, 90.4 percent for Teachers and 102.6 percent for the Board of Education system.", "source": "Comptroller's ACFR FY2025", "url": "https://comptroller.nyc.gov/wp-content/uploads/documents/ACFR-2025-7-28-2026.pdf"},
    {"fact": "361,394 retirees and beneficiaries were drawing city pensions as of June 30, 2024, against 378,991 active members.", "source": "Comptroller's ACFR FY2025", "url": "https://comptroller.nyc.gov/wp-content/uploads/documents/ACFR-2025-7-28-2026.pdf"}
  ],
  "benefits": [
    {"fact": "Employee and retiree health insurance is budgeted at $10.9 billion for fiscal 2027, up from $10.6 billion in fiscal 2026.", "source": "NYC Comptroller, Comments on the FY2027 Adopted Budget", "url": "https://comptroller.nyc.gov/wp-content/uploads/documents/Comments-on-New-York-Citys-Fiscal-Year-2027-Adopted-Budget.pdf"},
    {"fact": "The retiree health plan covered 288,479 active workers and 260,016 retirees and beneficiaries as of June 30, 2024; its $101.7 billion liability was 5.1 percent funded at June 30, 2025.", "source": "Comptroller's ACFR FY2025", "url": "https://comptroller.nyc.gov/wp-content/uploads/documents/ACFR-2025-7-28-2026.pdf"},
    {"fact": "The city paid $1.38 billion in judgments and claims in fiscal 2025, against an adopted budget of $877 million; in fiscal 2024 it resolved 13,397 claims for $1.94 billion, the most ever.", "source": "Comptroller's ACFR FY2025; NYC Comptroller claims release, April 2025", "url": "https://comptroller.nyc.gov/newsroom/comptroller-landers-new-dashboard-tracks-city-claims-city-paid-nearly-2b-in-settlements-last-fiscal-year/"}
  ],
  "debt_service": [
    {"fact": "Debt service took 10.2 percent of city tax revenues in fiscal 2025, under the city's 15 percent affordability ceiling, but is projected to reach about 14.2 percent by fiscal 2033.", "source": "NYC Comptroller, Annual Report on Capital Debt and Obligations FY2026", "url": "https://comptroller.nyc.gov/wp-content/uploads/documents/Annual-Report-on-Capital-Debt-and-Obligations-Fiscal-Year-2026-1.pdf"},
    {"fact": "Net debt was $121.0 billion at the end of fiscal 2025, and total primary-government debt worked out to $15,763 per resident.", "source": "Comptroller's ACFR FY2025, Ratios of Outstanding Debt", "url": "https://comptroller.nyc.gov/wp-content/uploads/documents/ACFR-2025-7-28-2026.pdf"},
    {"fact": "Direct and overlapping debt per capita in fiscal 2024 was $12,402 in New York City, second among 14 peer cities after Washington ($21,712); Chicago was $6,659, Los Angeles $5,360, Philadelphia $4,869 and Houston $4,410.", "source": "NYC Comptroller, Annual Report on Capital Debt and Obligations FY2026, Table 19", "url": "https://comptroller.nyc.gov/wp-content/uploads/documents/Annual-Report-on-Capital-Debt-and-Obligations-Fiscal-Year-2026-1.pdf"}
  ],
  "health": [
    {"fact": "The city gave NYC Health + Hospitals more than $2.4 billion in fiscal 2025, 145 percent more than in fiscal 2018.", "source": "New York State Comptroller, Dec. 2025", "url": "https://www.osc.ny.gov/files/reports/pdf/nyc-health-hospitals-strategic-initiatives.pdf"},
    {"fact": "Health + Hospitals treated 1,170,529 unique patients in fiscal 2026, 215,554 of them uninsured, on spending of $13.2 billion.", "source": "Mayor's Management Report, Fiscal 2026", "url": "https://www.nyc.gov/assets/operations/downloads/pdf/mmr2026/2026_mmr.pdf"},
    {"fact": "The Department of Health and Mental Hygiene spent $2.84 billion in fiscal 2026.", "source": "Mayor's Management Report, Fiscal 2026", "url": "https://www.nyc.gov/assets/operations/downloads/pdf/mmr2026/2026_mmr.pdf"}
  ],
  "general_government": [
    {"fact": "The city had 287,422 full-time employees in fiscal 2025, of whom 15,073 were in general government; the fiscal 2027 budget authorizes 307,199 full-time positions.", "source": "Comptroller's ACFR FY2025; Comptroller, Comments on the FY2027 Adopted Budget", "url": "https://comptroller.nyc.gov/wp-content/uploads/documents/ACFR-2025-7-28-2026.pdf"}
  ],
  "environmental": [
    {"fact": "Sanitation disposed of 3.13 million tons of refuse in fiscal 2026 and collected 719,000 tons of recycling, a 19.7 percent diversion rate.", "source": "Mayor's Management Report, Fiscal 2026", "url": "https://www.nyc.gov/assets/operations/downloads/pdf/mmr2026/2026_mmr.pdf"},
    {"fact": "Water and sewer service is paid for off budget: the Water Board sets rates to cover the Water Authority's debt and collected over $4.8 billion in fiscal 2026, reimbursing the city about $1.5 billion a year for operations and rent.", "source": "Comptroller's ACFR FY2025; Mayor's Management Report, Fiscal 2026", "url": "https://www.nyc.gov/assets/operations/downloads/pdf/mmr2026/2026_mmr.pdf"}
  ],
  "everything_else": [
    {"fact": "NYCHA houses 497,649 authorized residents in 177,565 apartments across 335 developments as of fiscal 2026.", "source": "Mayor's Management Report, Fiscal 2026", "url": "https://www.nyc.gov/assets/operations/downloads/pdf/mmr2026/2026_mmr.pdf"},
    {"fact": "The Department of Transportation maintains 6,300 miles of streets, 809 bridges and four tunnels, and resurfaced 1,169 lane miles in fiscal 2026.", "source": "Mayor's Management Report, Fiscal 2026", "url": "https://www.nyc.gov/assets/operations/downloads/pdf/mmr2026/2026_mmr.pdf"},
    {"fact": "CUNY enrolled 246,503 students in fiscal 2026, 81,883 of them at its seven community colleges, where tuition is $4,800; Parks cares for 2,000 parks and 12,000 acres of natural areas, and the three library systems run 220 branches.", "source": "Mayor's Management Report, Fiscal 2026", "url": "https://www.nyc.gov/assets/operations/downloads/pdf/mmr2026/2026_mmr.pdf"}
  ]
}
```

## Self-audit

- Read directly from downloaded files: MMR 2026, ACFR 2025, CPT27, DEBT, CENSUS-ED xlsx, ASPEP xlsx, OSC H+H PDF, BJS 2020 PDF. Live-URL hashes were checked for MMR, ACFR and CPT27.
- Via WebFetch extraction only (not downloaded, treat as one notch weaker): the Census press release sentences, the Comptroller Dec. 2021 jail-cost release, the Comptroller Apr. 2025 claims release. The Table 18 and Table 8 xlsx values independently confirm the press-release per-pupil numbers.
- Derived by me, labeled as such: officers per 1,000 (ASPEP counts divided by the population field in the same file; the file's population year code is "20"), and pensions as 6.9% of the FY2027 budget. The JSON states the inputs alongside the ratio.
- Mixed years inside single JSON sentences are stated explicitly (e.g., ADP FY2026 with the FY2021 cost figure).
- Not found or not readable, left out of the JSON: a post-FY2021 official cost per incarcerated person; FY2025 claims-dashboard totals; total parkland acreage; any NYC-vs-cities total spending per capita table (Lincoln FiSC is interactive only); DOE enrollment as a single MMR indicator (Census gives 845,509 for FY2024 in Table 18, which is in the table above but not the JSON because the MMR's "nearly one million" counts a different population).
- ASPEP Houston officer count is flagged G (imputed) and was excluded. NYC's count is flag T (totals reported, function split pro-rated from the prior year).
