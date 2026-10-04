# New York City's budget in $100

Four linked visual explainers. Each is a static page; every number on a page has a URL and a verbatim quotation in that part's `research/` folder, and every number was re-derived from the primary documents in a blind check (October 2026).

1. `nyc-who-pays/` Who pays. Revenue by source, fiscal 2000-2027; who pays the property, income and business taxes; what the mayor can change without Albany.
2. `nyc-where-it-goes/` Where it goes. Spending by line, with agency and unit-of-appropriation splits, who pays for each line, context facts, what the mayor can change, and what sits off the budget.
3. `nyc-budget-since-2000/` Since 2000. Each line in real dollars per resident.
4. `nyc-what-the-city-builds/` The capital budget. Capital spending by function, fiscal 2000-2025.

Live: https://vital-city-nyc.github.io/nyc-budget-explainer/nyc-who-pays/

## Sources

- New York City Comptroller, Annual Comprehensive Financial Reports (fiscal 2005, 2015 and 2025 editions): General Fund revenues and expenditures, Capital Projects Fund expenditures, debt tables.
- Office of Management and Budget, Adopted Budget Fiscal Year 2027 (June 2026): Expense Revenue Contract (`erc6-26.pdf`) and Supporting Schedules (`ss6-26.pdf`).
- Department of Finance: Annual Report on the NYC Real Property Tax, fiscal 2026; Statistical Profiles of NYC Business Income Taxes, tax year 2022.
- Independent Budget Office: tables on residents' income and income tax liability, tax year 2023; analysis of the fiscal 2027 preliminary budget.
- Comptroller, Comments on the Fiscal Year 2027 Adopted Budget; Mayor's Management Report, fiscal 2026; Census Bureau school finance, population and public employment files; Bureau of Labor Statistics consumer price index, New York area.

Documents were downloaded and read on October 2 and 3, 2026. Exact URLs, page numbers and quotations are in each part's `research/` folder.

## How the numbers are built

`nyc-who-pays/scripts/build_budget_data.py` rebuilds every derived data file (revenue and spending per $100, aid by purpose, agency lists, units of appropriation, funding by line, real dollars per resident, capital by function). It reads the extraction outputs of the companion repo [nyc-budget-per-capita](https://github.com/joshgreenman1973/nyc-budget-per-capita) (which parses the Comptroller's and OMB's PDFs and fails if any sum misses the total the report prints) and parses the 4,716-page supporting schedules itself. The script asserts that buckets sum to printed totals, that agency rows tie to their line, and that every agency's units of appropriation match OMB's agency total net of intra-city sales.

    BUDGET_REPO=/path/to/nyc-budget-per-capita python3 nyc-who-pays/scripts/build_budget_data.py

Hand-entered files (each documented in `research/`): `property_tax_by_class`, `pit_by_income`, `business_by_sector`, both `control` files, `context_facts`, `headline_stats`, `offbudget`.

`nyc-who-pays/shared/budget.css` and `budget.js` are shared by all four pages; bump the `?v=` stamp on those links when either changes. `nyc-who-pays/EMBED.md` has the article embed snippet.

## Known limits

- Fiscal 2026 and 2027 are budget figures, not audited. The budget's Miscellaneous line is split by what it holds so those years line up with the audited classification.
- The audited report counts the pass-through entity tax as a business tax; the budget counts it as income tax.
- Shares inside a tax (property by class, income by band, business by sector) are the latest published year and are applied to whichever year the slider shows.
- Part three's budget years are in nominal dollars. Part four's bars use a general consumer price index, not a construction cost index.
