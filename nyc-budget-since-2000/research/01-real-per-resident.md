# 01. Real spending per resident, fiscal 2000-2027

Compiled 2026-10-02. Numerator: the ten spending lines in ../nyc-where-it-goes/data/spending_per_100.json (Comptroller ACFR General Fund expenditures and transfers, fiscal 2000-2025; OMB adopted budget for 2026-2027; provenance with page numbers in ../nyc-where-it-goes/research/01-spending-series.md). Denominators and deflator come from the nyc-budget-per-capita repo's data.json (`years[].population`, `years[].cpi`, `years[].deflator`), whose sources are listed in its scripts/fetch_sources.sh:
- Population: Census Bureau county estimates for Bronx, Kings, New York, Queens and Richmond counties: 2000-2010 intercensal (co-est00int-tot.csv), 2010-2020 intercensal (co-est2020int-pop-36.xlsx), 2020-2025 vintage 2025 (co-est2025-alldata.csv), https://www2.census.gov/programs-surveys/popest/. Fiscal 2025 population used: 8,584,629. Budget years reuse 2025 ("population held at the 2025 estimate").
- Prices: BLS CPI-U, New York-Newark-Jersey City, all items (CUURS12ASA0), https://download.bls.gov/pub/time.series/cu/cu.data.1.AllItems, averaged over each fiscal year (July-June) and rebased so fiscal 2025 = 1. Fiscal 2025 average index: 340.4688; fiscal 2000: 179.6167 (deflator 1.89553).
Per-resident real dollars = line amount (thousands) x 1000 x deflator / population. Budget years are not deflated (deflator 1.0) and are flagged on the page.

Checks: fiscal 2025 total $13,709 per resident = $117,690,172 thousand x 1000 / 8,584,629; fiscal 2000 total $8,956 = $37,879,886 thousand x 1000 x 1.89553 / 8,017,608.

Self-audit: HIGH for inputs; derived arithmetic as stated. The Census and BLS files are in the per-capita repo's data/raw (not committed there; re-fetch with its script).

Blind-check note (2026-10-02): the 2020 population value (8,751,188) is the vintage-2025 estimate, not the 2010-2020 intercensal figure (8,804,200); 2010-2019 are intercensal. The method text says so. Fiscal 2000 pension contributions (615,085 thousand) were a trough year (1999: 1,342,415; 2001: 1,127,129), so the +694% figure is sensitive to the base year.
