# 06. Breakdowns by year (compiled November 19, 2026)

The first chart's property, income and business tax squares split by the selected year's own figures. This folder holds those series and the record of where each number came from. `scripts/build_breakdown_years.py` turns them into the `years` blocks in `data/property_tax_by_class.json`, `data/pit_by_income.json` and `data/business_by_sector.json`, and stops if any year's parts do not add to its total.

| File | What it holds | Years |
|---|---|---|
| `property_by_class.json`, `property_by_class_notes.md` | Department of Finance levy by tax class ($ millions) and the share of Class 2 in rental buildings | Fiscal 2000 to 2026; Class 2 split from fiscal 2005 |
| `income_by_band.json`, `income_by_band_notes.md`, `income_by_band_browser_reads.json` | Independent Budget Office, residents' liability before credits and returns by income, sheet 8 rows 19 to 39 of each year's workbook | Tax years 2006 to 2023 |
| `business_by_sector.json`, `business_by_sector_notes.md` | Department of Finance statistical profiles, combined table by industry ($ thousands) | Tax years 1999 to 2022 |
| `check_pdfs.py`, `check_pit.py` | Independent re-reads: every property and business figure is on the PDF page it cites; every saved income workbook regroups to the same bands | |

Each notes file gives, for every year, the URL, the local file name and MD5, the table or sheet and page, and the verbatim row text or cell values used.

How the series were built:
- **Property tax.** Four-class levy from the class-levy history table (Table 19) in the newest annual report that prints the year, so the series is on one basis. The Class 2 split is each year's own "Reconciliation ... by Property Type", gross levy column: rentals are Rentals, Conrentals and 4-10 Family Rentals; owner units are co-ops, condos and condops, large and 2-10 family. Reports before fiscal 2005 have no levy by property type. Before fiscal 2010, condo buildings with rental units were counted as condos (0.35% of the Class 2 levy in fiscal 2010).
- **Income tax.** Six bands summed from IBO's nominal rows. Sheet 8 is used for every year because the Summary sheet's tax column was after credits through 2022. IBO says 2014 and earlier come from samples of returns and "should therefore be considered estimates." IBO's old links for 2006 to 2020 and 2022 now redirect; the files are the Internet Archive's copies of those addresses. The 2021 and 2023 workbooks were read in a browser on the city's publications portal and are not saved; the cells read are in `income_by_band_browser_reads.json`.
- **Business taxes.** Six groups from DOF's combined table: Finance and insurance ("FINANCIAL" through 2008), Services, Trade, Information, Real estate, and Manufacturing plus Other. Through 2014 the table covers the banking corporation, general corporation and unincorporated business taxes; from 2015 the business corporation tax, the general corporation tax (S corporations) and the unincorporated business tax. Tax year 1998 has no combined table and 1997 uses older industry codes, so the series starts in 1999.

On the page, a fiscal year shows the tax year whose returns were due in it (fiscal 2024 shows tax year 2023).
