# 01. Real spending per resident, fiscal 2000-2027

Compiled 2026-10-02. Numerator: the ten spending lines in ../nyc-where-it-goes/data/spending_per_100.json (Comptroller ACFR General Fund expenditures and transfers, fiscal 2000-2025; OMB adopted budget for 2026-2027; provenance with page numbers in ../nyc-where-it-goes/research/01-spending-series.md). Denominators and deflator come from the nyc-budget-per-capita repo's data.json (`years[].population`, `years[].cpi`, `years[].deflator`), whose sources are listed in its scripts/fetch_sources.sh:
- Population: Census Bureau county estimates for Bronx, Kings, New York, Queens and Richmond counties: 2000-2010 intercensal (co-est00int-tot.csv), 2010-2020 intercensal (co-est2020int-pop-36.xlsx), 2020-2025 vintage 2025 (co-est2025-alldata.csv), https://www2.census.gov/programs-surveys/popest/. Fiscal 2025 population used: 8,584,629. Budget years reuse 2025 ("population held at the 2025 estimate").
- Prices: BLS CPI-U, New York-Newark-Jersey City, all items (CUURS12ASA0), https://download.bls.gov/pub/time.series/cu/cu.data.1.AllItems, averaged over each fiscal year (July-June) and rebased so fiscal 2025 = 1. Fiscal 2025 average index: 340.4688; fiscal 2000: 179.6167 (deflator 1.89553).
Per-resident real dollars = line amount (thousands) x 1000 x deflator / population. Budget years are not deflated (deflator 1.0) and are flagged on the page.

Checks: fiscal 2025 total $13,709 per resident = $117,690,172 thousand x 1000 / 8,584,629; fiscal 2000 total $8,956 = $37,879,886 thousand x 1000 x 1.89553 / 8,017,608.

Self-audit: HIGH for inputs; derived arithmetic as stated. The Census and BLS files are in the per-capita repo's data/raw (not committed there; re-fetch with its script).

Blind-check note (2026-10-02): the 2020 population value (8,751,188) is the vintage-2025 estimate, not the 2010-2020 intercensal figure (8,804,200); 2010-2019 are intercensal. The method text says so. Fiscal 2000 pension contributions (615,085 thousand) were a trough year (1999: 1,342,415; 2001: 1,127,129), so the +694% figure is sensitive to the base year.

## Oct. 14, 2026 review
- Pension trough: Comptroller, "The $8 Billion Question" (April 2011), PDF p. 6 (https://comptroller.nyc.gov/wp-content/uploads/documents/C__WWW_NYC-site_rsnyc_pdf_NYC_PensionCostIssueBrief.pdf): the funds "implemented a market value reset" that "allowed employer contributions to be reduced by $1.1 billion in FY '00." City contributions, FY2005 CAFR p. 277: $1,342,415 thousand (1999), $615,085 thousand (2000), $1,127,129 thousand (2001).
- Debt service prepayments: ACFR FY2025 PDF p. 62-64 ($3,787 million prepaid toward 2026; $4,397 million of 2025 prepaid in 2024). FY2001 CAFR (Wayback, Part II-A, PDF p. 11): fiscal 2000 prepayments about $3.05 billion. Debt service is excluded from the grew-most and grew-least ranking for this reason.
- Health + Hospitals payments: FY2015 ACFR p. 374, 1,290,016 (2006) and 37,572 (2008), thousands.
- Government price index: BEA, state and local government consumption expenditures and gross investment price index (FRED A829RD3Q086SBEA), fiscal-year averages 59.64 (2000) and 132.00 (2025), up 121%; on it, total spending per resident rose 31.1%, against 53.1% on the New York-area consumer price index. Downloaded from FRED Oct. 14, 2026.
- Pooled costs, fiscal 2025 estimate: police, fire, jails and prosecutors $23.32 billion with pensions and fringe (about $2,700 per resident); schools $38.05 billion (about $4,400). See ../nyc-where-it-goes/research/03 (Oct. 14 section).
- Population revisions: Census challenge program results (https://www.census.gov/programs-surveys/popest/about/challenge-program/results.html).
