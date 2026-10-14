# 01. Capital spending by function, fiscal 2000-2025

Compiled 2026-10-02. Source: NYC Comptroller, Annual Comprehensive Financial Reports, Capital Projects Fund "Expenditures by Agency" / by function schedules, as extracted with page numbers in the nyc-budget-per-capita repo (data/out/acfr_raw.csv, table `capital_expenditures`; sources acfr2005 for 1996-2005, acfr2015 for 2006-2015, acfr2025 for 2016-2025). Fiscal 2025 report: https://comptroller.nyc.gov/wp-content/uploads/documents/ACFR-2025-7-28-2026.pdf, Schedule CP2, PDF p. 462 on, e.g. "General Government: Department of Small Business Services 387,167", "Department of Citywide Administrative Services 980,482", "Total General Government 1,446,293", "Public Safety and Judicial: Police Department 143,498", "Fire Department 129,737" (thousands). Function totals for fiscal 2025 (thousands): education 3,858,377; environmental 2,382,483; general government 1,446,293; health 590,502; housing 2,875,769; libraries 103,519; parks 795,473; public safety 1,281,529; social services 199,545; transportation 2,044,516; total 15,578,006. The repo's build asserts each year's functions sum to the printed total.

Bonds issued: ACFR governmental funds statement, fiscal 2025 PDF p. 426, "Principal amount of bonds issued 15,518,392" and "Bond premium 1,562,536"; refunding debt issued 6,970,750 is excluded from the "bonds issued" figure shown. Debt service and operating totals as in part two (research/01 there).

Caveat on the page: these are cash expenditures in the year, not commitments; the capital commitment plan the city announces ($117.1 billion for fiscal 2026-2030 per the Comptroller's June 2026 report, see ../nyc-where-it-goes/research/02) is a different measure. Figures nominal.

Self-audit: HIGH for every number (extracted cells with page numbers, sums asserted). Editorial: labels (schools and CUNY; housing and buildings; water, sewers and sanitation; streets, bridges and transit).

Blind-check note (2026-10-02): the per-capita repo records refunding debt issued as 0 for 2024 and 2025; the ACFR shows 1,697,190 and 6,970,750 (thousands). The page does not display refunding debt. The FY2005 CAFR labels the fiscal 2000 bonds line "Proceeds from sale of bonds" (3,125,230).

Year bars (added Oct 3 2026): capital_total x that year's deflator from the same BLS New York-area CPI series as part three (fiscal 2000 deflator 1.89553): fiscal 2000 $4,809,483 thousand = $9.1 billion in fiscal 2025 dollars; fiscal 2025 $15.6 billion; ratio 1.7. CPI is a general price index, not a construction-cost index; the heading says "after general inflation."

## Oct. 14, 2026 review
- Construction prices: BEA NIPA table 3.9.4 line 36, price index for state and local government investment in structures (FRED B842RG3Q086SBEA), fiscal-year averages 50.993 (2000) and 144.722 (2025), 2.84 times; consumer prices 1.90 times. On the construction index, fiscal 2000 = $13.6 billion in 2025 prices, ratio 1.14; fiscal 2025 is below 2002, 2008, 2009 and 2010. Rechecked from FRED Oct. 14, 2026.
- Housing capital is HPD alone: ACFR FY2025 p. 464, 2,875,769; FY2005 CAFR p. 298, "HOUSING: Department of Housing Preservation and Development."
- Water and sewer: ACFR FY2025 p. 462, Environmental Protection 2,025,988 (thousands); p. 119, "The Water Authority issues debt to finance the cost of capital improvements to the System"; p. 121, Capital Projects Fund resources include "payments from the Water Authority."
- General government capital: ACFR FY2025 p. 462, Citywide Administrative Services 980,482; Small Business Services 387,167; Information Technology and Telecommunications 78,644; total 1,446,293.
- Debt service share: 8,080,015 / 117,690,172 = 6.87%.
