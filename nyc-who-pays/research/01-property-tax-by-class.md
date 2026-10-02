# 01. Who pays the property tax? (levy and market value by class)

Compiled 2026-10-02. Primary source for every number in tables A-D is the NYC Department of Finance (DOF) annual report. Local copies were checked against the live URLs by MD5 hash (identical files).

- **FY2026 report (latest published; dated July 2026, Mayor Mamdani / Commissioner Richard Lee):** https://www.nyc.gov/assets/finance/downloads/pdf/reports/Annual%20Report%20FY26%207-8-26%20FINAL.pdf (local copy: scratchpad `fy26.pdf`, MD5 c55874c9ccee61b461e1a4ee0c15b096)
- **FY2025 report (dated July 2025, Mayor Adams / Commissioner Niblack):** https://www.nyc.gov/assets/finance/downloads/pdf/reports/reports-property-tax/nyc_property_fy25.pdf (local copy: `fy25.pdf`, MD5 e8e68c352779e377a9390e36178bb4b5)

No FY2027 DOF annual report has been published yet. The FY2026 report's Table 21 already cites the "Adopted 2027 Financial Plan, Fiscal Years 2026-2030 (June, 2026)".

Class definitions (DOF FY2026, Fast Facts p.1): "Class One is primarily one-, two-, and three-family homes; Class Two is all other residential property; Class Three is certain types of property owned by utility companies subject to government supervision; and Class Four is all other commercial property."

## A. Levy and market value by class, FY2026 ($ millions)

| Class | Levy | Share of levy | Market value | Share of market value | Tax rate per $100 of assessed value | Levy ÷ market value (derived) |
|---|---|---|---|---|---|---|
| Citywide | 37,976.6 | 100.0% | 1,574,378.8 | 100.00% | 12.283 | 2.41% |
| 1: 1-3 family homes | 5,430.3 | 14.3% | 781,307.8 | 49.63% | 19.843 | 0.70% |
| 2: apartment buildings (rentals, co-ops, condos) | 14,869.4 | 39.2% | 395,059.1 | 25.09% | 12.439 | 3.76% |
| 3: utilities | 3,145.0 | 8.3% | 63,196.0 | 4.01% | 11.108 | 4.98% |
| 4: commercial | 14,532.0 | 38.3% | 334,815.9 | 21.27% | 10.848 | 4.34% |

Sources: levy, levy share, and rates are from DOF FY2026 Fast Facts p.1 and Tables 19-20. Market value and market-value share are from Table 1 (Citywide, p.6). The last column is my own arithmetic (levy ÷ market value). DOF does not publish an "effective tax rate" by class. Exact class shares are in Table 19: 14.2990 / 39.1540 / 8.2814 / 38.2656.

Quotes:
- Fast Facts FY2026: "Citywide $37,976.6 100.0% 3.0% / Class 1 $5,430.3 14.3% 3.0% / Class 2 $14,869.4 39.2% 3.1% / Class 3 $3,145.0 8.3% 6.5% / Class 4 $14,532.0 38.3% 2.3%"
- Summary p.3: "The Citywide average tax rate remained at $12.283 per $100 of assessed value. The levy increased 3.0 percent to $37,976.6 million"
- Summary p.3: "The total citywide market value of taxable property approached $1.6 trillion."
- Table 1: "Class 1 698,508 1,096,932 781,307.8 49.63" and "Class 2 310,114 2,034,308 395,059.1 25.09"

## B. Same table for FY2025 ($ millions)

| Class | Levy | Share of levy | Market value | Share of market value (derived) | Rate per $100 assessed value | Levy ÷ market value (derived) |
|---|---|---|---|---|---|---|
| Citywide | 36,862.3 | 100.0% | 1,493,902.8 | 100% | 12.283 | 2.47% |
| 1 | 5,274.0 | 14.3% | 738,510.3 | 49.4% | 20.085 | 0.71% |
| 2 | 14,428.9 | 39.1% | 369,474.2 | 24.7% | 12.500 | 3.91% |
| 3 | 2,952.0 | 8.0% | 58,972.1 | 3.9% | 11.181 | 5.01% |
| 4 | 14,207.4 | 38.5% | 326,946.2 | 21.9% | 10.762 | 4.35% |

Source: DOF FY2025 Fast Facts p.1, quoted: "Class 1 $738,510.3 -3.4%" ... "Class 1 $5,274.0 14.3% 3.5% 20.085" ... "Class 2 $14,428.9 39.1% 3.7% 12.500".

## C. Inside Class 2: rentals vs co-ops and condos, FY2026 ($ millions)

DOF Table 4 (p.34) splits the levy by property type, and Table 1 (p.6) does the same for market value. The groupings below are mine. Rentals = "Rentals" + "Conrentals" + "4-10 Fam Rentals". Owner units = co-ops, condos and condops, both the large buildings and the 2-10 family ones.

| Group | Levy | Share of Class 2 levy | Share of citywide levy | Net levy billed (after STAR and abatements) | Share of Class 2 net billed | DOF market value |
|---|---|---|---|---|---|---|
| Rental buildings | 7,628.1 | 51.3% | 20.1% | 7,428.6 | 53.5% | 234,126.0 |
| Co-ops, condos, condops | 7,241.2 | 48.7% | 19.1% | 6,451.8 | 46.5% | 160,933.1 |

Rows from Table 4, quoted:
- "Rentals 46,893.0 0.1 46,893.1 5,833.0 0.0 -183.7 5,649.3"
- "Cooperatives 27,300.1 192.4 27,492.4 3,419.8 -20.8 -488.3 2,910.7"
- "Condominiums 24,793.2 32.5 24,825.7 3,088.1 -3.5 -207.3 2,877.3"
- "Conrentals 3,064.8 0.0 3,064.8 381.2 0.0 -1.9 379.4"
- "4-10 Fam Rentals 11,359.6 7.3 11,366.9 1,413.9 -0.8 -13.3 1,399.9"

Large "Rentals" alone carry a $5,833.0M levy, 15.4% of the citywide levy, on 8.72% of citywide market value. In FY2025 the same split was rentals $7,401.6M (51.3% of Class 2) and owner units $7,027.3M (48.7%), from FY2025 Table 4.

**Caveat (load-bearing): do not compute co-op or condo "effective rates" from DOF market value.** DOF values co-ops and condos as if they were rental buildings, so their DOF "market value" sits far below sale prices. On DOF values, co-ops show a higher levy-to-value ratio (5.0%) than rentals (4.25%). That reverses the real-world gap. DOF FY2026 Appendix A, p.66: "Unless specifically excluded, Section 581 of the Real Property Tax Law prohibits the use of sales data that reflect actual or potential cooperative or condominium ownership in the assessment of multiple-family housing." The co-op/condo abatement is also large: it accounts for the -$488.3M and -$207.3M in the abatement column above.

## D. Renters' indirect burden (secondary sources)

| Claim | Year of data | Source | Quote |
|---|---|---|---|
| Class 2 pays 39.3% of the levy on 24.7% of market value. Class 1 levy-to-value is about 0.7%, Class 2 about 3.7% | FY2025 | NYU Furman Center, State of the City 2025, https://www.furmancenter.org/soc-report/state-of-the-city-2025/nycs-property-tax-system/ | (via WebFetch extraction) Class 2 contributes "39.3%" of the levy on "24.7%" of market value. "In a market with limited rental supply and high demand, owners may pass at least some of the cost of taxes through to their tenants, potentially increasing housing costs for renters." |
| How much of the tax passes through to rent is not settled | 2018-2019 testimony, report Dec 2021 | NYC Advisory Commission on Property Tax Reform, final report, https://www.nyc.gov/assets/propertytaxreform/downloads/pdf/final-report.pdf (downloaded and read, p.8) | "Commission members felt it was important to understand the degree to which landlords pass on the property tax, a cost of operating a building, through their rents." ... "Unfortunately, the testimony did not reveal conclusive evidence regarding the degree of the property tax borne by renters." ... "Importantly, renters do not pay the property tax directly, so there is no mechanism through the property tax to provide them relief." |
| Large rentals' effective rate of about 4.12%, "more than five times" small homes | year not confirmed | CBC, https://cbcny.org/nyc-effective-tax-rates | **UNVERIFIED.** This appeared only in a search-engine summary. The page sits behind a Cloudflare bot check, so I could not read it. Do not use until someone checks it in a browser. |

The Furman figures (39.3% / 24.7%) differ slightly from DOF FY2025 (39.1% levy share, 24.7% market value). Use the DOF numbers and cite Furman only for the pass-through point.

## E. Other levers inside the property tax (useful for file 02)

- Class shares are set by a state formula with a cap. DOF FY2026 p.32: "The class shares are determined each year according to a formula in State law." Table 23 note: "Article 18 of Real Property Tax Law requires that the adjusted base proportions of the four real property tax classes ... be revised each year to reflect relative changes in market values, subject to a 5 percent cap on the increase in any class's share of the levy. In some years, special State legislation has resulted in a class share cap that is lower than the 5 percent default cap." Cap used: FY2025 0.90%, FY2026 1.00%.
- Assessment caps (Appendix A). Class 1: "Assessment increases cannot exceed 6 percent annually and 20 percent over any five-year period." Class 2 buildings under 11 units: "cannot exceed 8 percent annually and 30 percent over any five-year period." Larger Class 2 and Class 4: no cap, but increases "must be phased-in over a five-year period."
- Levy versus revenue, FY2026 (Table 21): levy $37,976.6M, estimated revenue $35,491.0M, "93.5" percent of levy.
- The 2.5% constitutional operating limit (Table 22, FY2026): operating limit $34,989.2M, expenses subject to the limit $32,746.1M, unused margin $2,243.2M (6.4%). Note 2: "Computed by taking 2.5% of NYS ORPTS full market valuations for the last completed assessment roll and the four preceding assessment rolls."
