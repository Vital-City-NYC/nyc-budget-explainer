# 04. Who pays the city personal income tax? (by income band)

Compiled 2026-10-02. Latest full tax year available: **2023** (returns filed in 2024; IBO released the tables Feb 10, 2026, from the state's 2023 annual PIT file). Every number in tables A-C comes from one workbook published by the NYC Independent Budget Office (IBO). No NYS Tax Department NYC-specific statistical report for a recent year turned up: tax.ny.gov's "Analysis of ... Personal Income Tax Returns" series is statewide and stops at 2011, and the IBO file is itself a cut of the state's return file, so IBO is the primary source here.

- **IBO workbook, "2023-pit-data.xlsx" (Feb 10, 2026):** record page https://a860-gpp.nyc.gov/concern/nyc_government_publications/pv63g542d ; file https://a860-gpp.nyc.gov/downloads/2227mv671 (local copy: scratchpad `2023-pit-data.xlsx`, MD5 4db3713423d59a5627224ca038929f08, 180,968 bytes). a860-gpp.nyc.gov returns Akamai 403s to curl and WebFetch; the file was pulled through the browser pane's own session, so the hash is of what the server actually sent.
- **IBO highlights PDF, "Highlights from IBO's Updated Tables on New York City Residents' Income & Income Tax Liability in 2023" (Feb 2026, 8 pp., Director Louisa Chafee, prepared by Benjamin Ferri):** https://a860-gpp.nyc.gov/downloads/3t945w93g (local: `ibo_2026_feb_pit_highlights.pdf`, MD5 e13fb45a75a036ae86f612bd38dbaea8)
- **IBO press release, Feb 10, 2026:** https://www.ibo.nyc.gov/assets/ibo/downloads/pdf/press-releases/2026/2026-pit-2023-tables-press-release.pdf (local: `ibo_pit2023_pr.pdf`, MD5 a66f40f037a2d5e8fd230ce233b658ed)
- **NYC Comptroller, "Spotlight: NYC Personal Income Tax 2019-2021" (April 2023):** https://comptroller.nyc.gov/wp-content/uploads/documents/Spotlight_PIT_Taxpayers.pdf (local: `comptroller_spotlight_pit.pdf`, MD5 a82e7517811a4e6d8468b3277cc023e3)
- **NYC DOF, "Statistical Profiles of New York City Business Income Taxes, Tax Year 2022" (August 2026, Mayor Mamdani / Commissioner Lee):** https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2022.pdf (local: `bit_report_2022.pdf`, MD5 284019ad8f82cce40159782e6f2609fb; nyc.gov needs a browser user-agent string or it 403s)

Definitions that matter. Income = New York adjusted gross income (NYAGI). "Filers" = all 3,905,234 returns; "taxpayers" = the 3,233,191 with positive liability. **Liability = "NYC Personal Income Tax Liability Before Credits"** unless stated otherwise; this is the measure IBO itself uses for "share of city PIT liability" (highlights p.8: "Liability is calculated before credits are applied."). Net liability after refundable credits is also given, because the gap at the top is large and is almost all the pass-through entity tax (PTET) credit, which refunds tax already paid at the entity level: of the $1,658.6M PTET credit in 2023, $1,583.6M (95.5%) went to the top 1 percent (sheet "9. Tax Credits", rows "100th Percentile" and "All Filers").

## A. Tax year 2023, IBO's nominal income bands exactly (sheet "2. Summary", rows 19-39; $ millions)

| NYAGI band | Returns | Share of returns | NYAGI | Share of NYAGI | PIT liability before credits | Share of liability | Avg liability ($) |
|---|---|---|---|---|---|---|---|
| Under $0 | 51,536 | 1.3% | -3,712.9 | -0.9% | 0.0 | 0.0% | 0 |
| $0 - $9,999 | 578,044 | 14.8% | 2,009.0 | 0.5% | 1.8 | 0.0% | 3 |
| $10,000 - $19,999 | 464,107 | 11.9% | 6,891.7 | 1.6% | 64.9 | 0.4% | 140 |
| $20,000 - $29,999 | 385,637 | 9.9% | 9,591.4 | 2.2% | 164.1 | 1.1% | 426 |
| $30,000 - $39,999 | 348,707 | 8.9% | 12,156.3 | 2.8% | 271.6 | 1.9% | 779 |
| $40,000 - $49,999 | 293,592 | 7.5% | 13,174.2 | 3.1% | 339.5 | 2.3% | 1,156 |
| $50,000 - $59,999 | 253,334 | 6.5% | 13,900.5 | 3.2% | 389.5 | 2.7% | 1,537 |
| $60,000 - $74,999 | 313,794 | 8.0% | 21,063.0 | 4.9% | 627.0 | 4.3% | 1,998 |
| $75,000 - $99,999 | 348,851 | 8.9% | 30,167.4 | 7.0% | 947.7 | 6.5% | 2,717 |
| $100,000 - $124,999 | 220,456 | 5.6% | 24,608.2 | 5.7% | 802.4 | 5.5% | 3,640 |
| $125,000 - $149,999 | 142,984 | 3.7% | 19,533.0 | 4.5% | 651.6 | 4.5% | 4,557 |
| $150,000 - $199,999 | 169,984 | 4.4% | 29,295.7 | 6.8% | 998.6 | 6.8% | 5,875 |
| $200,000 - $349,999 | 186,452 | 4.8% | 48,033.5 | 11.1% | 1,691.9 | 11.6% | 9,074 |
| $350,000 - $499,999 | 59,045 | 1.5% | 24,465.0 | 5.7% | 881.0 | 6.0% | 14,922 |
| $500,000 - $749,999 | 38,128 | 1.0% | 23,027.2 | 5.3% | 848.1 | 5.8% | 22,242 |
| $750,000 - $999,999 | 16,276 | 0.4% | 13,997.3 | 3.2% | 518.7 | 3.5% | 31,871 |
| $1,000,000 - $1,999,999 | 19,897 | 0.5% | 27,236.3 | 6.3% | 1,029.8 | 7.0% | 51,754 |
| $2,000,000 - $4,999,999 | 9,660 | 0.2% | 29,324.6 | 6.8% | 1,112.4 | 7.6% | 115,159 |
| $5,000,000 - $9,999,999 | 2,814 | 0.1% | 19,441.8 | 4.5% | 739.4 | 5.1% | 262,766 |
| $10,000,000 and Over | 1,936 | 0.0% | 67,607.9 | 15.7% | 2,550.4 | 17.4% | 1,317,356 |
| All Filers | 3,905,234 | 100.0% | 431,811.0 | 100.0% | 14,630.6 | 100.0% | 3,746 |

Shares are my division of the IBO cell values; IBO's own share columns agree to the decimal (e.g. $10,000,000 and Over: 0.000496 of filers, 0.156568 of NYAGI, 0.17432 of liability).

## B. Grouped for a 100-square waffle (sums of the rows above; IBO's cut points force $200k and $500k rather than $250k)

| Band | Returns | Share of returns | NYAGI ($M) | Share of NYAGI | Liability before credits ($M) | Share of liability | Net liability after refundable credits ($M) | Share of net |
|---|---|---|---|---|---|---|---|---|
| Under $50,000 | 2,121,623 | 54.3% | 40,109.8 | 9.3% | 842.0 | 5.8% | 475.0 | 3.8% |
| $50,000 - $99,999 | 915,979 | 23.5% | 65,130.8 | 15.1% | 1,964.2 | 13.4% | 1,960.5 | 15.7% |
| $100,000 - $199,999 | 533,424 | 13.7% | 73,436.9 | 17.0% | 2,452.7 | 16.8% | 2,443.1 | 19.6% |
| $200,000 - $499,999 | 245,497 | 6.3% | 72,498.5 | 16.8% | 2,573.0 | 17.6% | 2,539.2 | 20.4% |
| $500,000 - $999,999 | 54,404 | 1.4% | 37,024.5 | 8.6% | 1,366.8 | 9.3% | 1,306.2 | 10.5% |
| $1,000,000 and over | 34,307 | 0.9% | 143,610.6 | 33.3% | 5,432.0 | 37.1% | 3,733.5 | 30.0% |
| All filers | 3,905,234 | 100.0% | 431,811.0 | 100.0% | 14,630.6 | 100.0% | 12,457.4 | 100.0% |

Whole-square rounding (largest remainder) that sums to 100: returns 54 / 24 / 14 / 6 / 1 / 1; NYAGI 9 / 15 / 17 / 17 / 9 / 33; liability 6 / 13 / 17 / 18 / 9 / 37. Net liability column: columns J-K of sheet "8. Tax Liability".

```json
[
{"band": "Under $50,000", "returns": 2121623, "share_returns": 54.3, "nyagi_millions": 40109.8, "share_nyagi": 9.3, "liability_before_credits_millions": 842.0, "share_liability": 5.8, "net_liability_after_refundable_credits_millions": 475.0, "share_net_liability": 3.8},
{"band": "$50,000 - $99,999", "returns": 915979, "share_returns": 23.5, "nyagi_millions": 65130.8, "share_nyagi": 15.1, "liability_before_credits_millions": 1964.2, "share_liability": 13.4, "net_liability_after_refundable_credits_millions": 1960.5, "share_net_liability": 15.7},
{"band": "$100,000 - $199,999", "returns": 533424, "share_returns": 13.7, "nyagi_millions": 73436.9, "share_nyagi": 17.0, "liability_before_credits_millions": 2452.7, "share_liability": 16.8, "net_liability_after_refundable_credits_millions": 2443.1, "share_net_liability": 19.6},
{"band": "$200,000 - $499,999", "returns": 245497, "share_returns": 6.3, "nyagi_millions": 72498.5, "share_nyagi": 16.8, "liability_before_credits_millions": 2573.0, "share_liability": 17.6, "net_liability_after_refundable_credits_millions": 2539.2, "share_net_liability": 20.4},
{"band": "$500,000 - $999,999", "returns": 54404, "share_returns": 1.4, "nyagi_millions": 37024.5, "share_nyagi": 8.6, "liability_before_credits_millions": 1366.8, "share_liability": 9.3, "net_liability_after_refundable_credits_millions": 1306.2, "share_net_liability": 10.5},
{"band": "$1,000,000 and over", "returns": 34307, "share_returns": 0.9, "nyagi_millions": 143610.6, "share_nyagi": 33.3, "liability_before_credits_millions": 5432.0, "share_liability": 37.1, "net_liability_after_refundable_credits_millions": 3733.5, "share_net_liability": 30.0}
]
```

## C. Top of the distribution, 2023 (sheets "2. Summary" and "8. Tax Liability", percentile rows)

| Group | Returns | Share of returns | Share of NYAGI | Liability before credits ($M) | Share | Net after refundable credits ($M) | Share of net |
|---|---|---|---|---|---|---|---|
| 91st - 95th Percentiles | 195,262 | 5.0% | 10.1% | 1,521.9 | 10.4% | 1,511.9 | 12.1% |
| 96th - 99th Percentiles | 156,209 | 4.0% | 16.7% | 2,616.5 | 17.9% | 2,540.5 | 20.4% |
| 100th Percentile (top 1%) | 39,052 | 1.0% | 34.3% | 5,599.8 | 38.3% | 3,891.3 | 31.2% |

Top 1 percent starts at NYAGI $906,514 in the workbook (sheet "1. Income Categories": "100th Percentile | Over $906,513") and $906,677 in the press release text; the two IBO documents differ by $163, so quote whichever you cite. Headline: in 2023 the top 1 percent of filers earned 34.3% of income and owed 38.3% of city PIT before credits; filers over $1 million (0.9% of returns) earned 33.3% and owed 37.1%. The bottom 54% of returns (under $50,000) owed 5.8%.

Prior years for context (top 1 percent share of liability): 2019 40%, 2021 48% (Comptroller); millionaire filers' share 2021 48%, 2022 39%, 2023 37% (IBO). The 2021 peak was capital gains, not a rate change.

Quotes:
- IBO workbook, sheet "2. Summary", header rows: "Comparison of Percentile and Decile Categories with Nominal Income Categories Tax Year 2023" / "Dollars in millions, except Average Personal Income Tax" / "Income Groups | Number of Filers | Number of Taxpayers | New York Adjusted Gross Income | New York Taxable Income | NYC Personal Income Tax Liability Before Credits | Average NYC PIT Liability Before Credits"
- Same sheet, row 38 cell values: "$10,000,000 and Over | 1936 | 0.000496 | 1934 | 0.000598 | 67607.874757 | 0.156568 | 66060.4692 | 0.16998 | 2550.400872 | 0.17432 | 1317356"; row 16: "100th Percentile | 39052 | 0.01 | 39007 | 0.012065 | 148127.488581 | 0.343038 | 145014.947621 | 0.373138 | 5599.800902 | 0.382746 | 143393"; row 39: "All Filers | 3905234 | 1 | 3233191 | 1 | 431811.038189 | 1 | 388635.841641 | 1 | 14630.593316 | 1 | 3746"
- Sheet "8. Tax Liability", row 16: "100th Percentile ... NYC Net PIT Liability After Refundable Credits 3891.252268 | 0.312364"; row 17 "All Filers ... 12457.419878"
- IBO highlights p.6: "IBO defines millionaire filers as filers with an AGI of at least $1 million. The shares of overall income (measured through AGI) and overall Personal Income Tax liability attributable to millionaire filers hit a high in 2021 at 43% and 48%, respectively, driven largely by realized capital gains income from the strong stock market in that year. These shares declined to 35% and 39% in 2022, and 33% and 37% in 2023."
- IBO highlights p.4: "Effective PIT rates decline slightly at the top of the income distribution, however. This in part reflects very high-income filers' ability to decrease their liability through tax reduction strategies such as deductions and credits, including the Pass-Through Entity Tax (PTET)."
- IBO press release: "In 2023, 3.91 million tax returns were filled by New York City residents, 69% of income being in the form of wages and salaries, with income from realized capital gains making up 9%." ... "the median adjusted gross income (AGI) for New York City filers was $42,749 and more than 90% of filers had an AGI of less than $170,000. The top 1% of the New York City income distribution begins at $906,677 and tops out at more than $5 billion in 2023."
- IBO press release: "New York City's PIT currently has four marginal tax rates that range from 3.078% to 3.876%. Rate increases peak at $50,000 if filing individually, $60,000 if filing as head of household or $90,000 if filing a joint return."
- Comptroller Spotlight p.5: "In 2021, the top 1 percent of tax filers accounted for 48 percent of NYC PIT liability, a share that has grown from 40 percent in 2019. While a small number of people pay a large share of personal income tax, the same top 1 percent of tax filers also earned 43 percent of all the income in 2021."

## D. Who pays the business income taxes, by sector (DOF, tax year 2022, latest published)

| Tax | Total liability | Taxpayers | Finance & insurance share of liability | Finance & insurance share of taxpayers | Next largest sectors |
|---|---|---|---|---|---|
| All three combined (COR + GCT + UBT) | $8,587.1M | 391,778 | 38.7% ($3,319.3M) | 5.4% (21,308) | Services 28.7%, Trade 9.2%, Information 8.6%, Real estate 6.0% |
| Business Corporation Tax (COR) | $4,568.0M | 191,171 | 49.1% ($2,242.5M), of which commercial banking 22.6%, securities & commodities 17.8% | 6.9% (13,150) | Information 13.0%, Trade 11.3%, Prof/tech/managerial 8.5% |
| General Corporation Tax (GCT, S-corps) | $1,463.5M | 168,883 | 5.5% ($80.5M) | 2.4% (4,121) | Real estate 17.6%, Prof/tech/managerial 16.5% |
| UBT partnerships | $2.38B | n/a in highlights | 41% | n/a | Legal, prof/tech, arts/food and other services 46% |

Concentration: in the COR, "The top 1 percent of taxpayers, or 1,912 firms, accounted for $4.24 billion, or 93 percent of total liability." Of that top 1 percent's $4,236.9M, finance & insurance firms (528 of them) owed $2,192.0M (Table 5). "Fifty-five percent of NYC business income taxpayers reported liability of $300 or less."

Quotes:
- DOF highlights p.1: "The COR, GCT, and UBT generated $8.59 billion in tax year 2022 liability, an increase of 9 percent from tax year 2021. The number of taxpayers increased by 1 percent, to 391,778." ... "The finance & insurance sector accounted for 39 percent of all tax liability, followed by the services sector, which generated 29 percent."
- p.1: "In 2022, the Business Corporation Tax generated $4.57 billion from 191,171 taxpayers." ... "The finance & insurance sector generated 49 percent of total liability. The professional/ technical/managerial and other services sectors accounted for 14 percent, while the information sector generated 13 percent and the trade sector contributed an additional 11 percent."
- Table 3 (p.9): "Finance & Insurance 13,150 6.9 % $2,242,478 49.1 %" / "Commercial Banking 273 0.1 1,033,682 22.6" / "Securities & Commodities 7,173 3.8 814,699 17.8"
- p.1: "The General Corporation Tax generated $1.46 billion from 168,883 taxpayers in 2022." Table 13 (p.23): "Finance & Insurance 4,121 2.4 % $80,532 5.5 %" / "Real Estate 24,630 14.6 257,902 17.6"
- p.1: "Among partnerships, the legal, professional/technical/managerial, arts/entertainment/ accommodation/food, and other services sectors accounted for 46 percent of total liability, while finance & insurance sector generated 41 percent."

## E. Sales tax by payer

No primary source breaks the city sales tax down by who pays it. DOF, IBO and the Comptroller publish collections, not incidence; the state Comptroller's local sales tax reports are by county. The only distributional estimates are model-based (ITEP's "Who Pays?" as summarized by the Fiscal Policy Institute, statewide, not city-specific). Those were not downloaded or read and should not be cited as city data. Say in the explainer that sales tax is paid at the register by residents, commuters and visitors, with no filer-level record.

## Self-audit

Confirmed (document downloaded, text read, numbers copied from cells or text): all of A, B, C from the IBO workbook, with the $1M+ totals (33.3% of NYAGI, 37.1% of liability) matching IBO's own narrative "33% and 37% in 2023"; the PTET credit split (sheet 9); Comptroller 2019 and 2021 top-1% shares; all of D from the DOF PDF text.
Medium: the top-1% cutoff ($906,513 vs $906,677, two IBO documents); the UBT partnership row in D, which is from the DOF highlights text only (Table 22 was not transcribed). Band grouping in B is mine, built from IBO's rows; IBO does not publish a $250k break.
UNVERIFIED / superseded: NYC Open Data "Tax Liability By AGI Range" (https://data.cityofnewyork.us/d/3vvi-fwjs, attributed to IBO, published 2014-03-06, deciles only, total liability $6,044.3M on 2,282,001 taxpayers). Downloaded and read, but the metadata does not state the tax year, so it is unusable for a dated chart. Empire Center and Politifact figures for 2011-2020 appeared only in search snippets and were not read; not used. No NYS Tax Department NYC-specific report was found for any year after 2011.


## F. Rate basics shown on the page (sources already cited above)
- Four rates, 3.078 to 3.876 percent; top rate from $50,000 single / $60,000 head of household / $90,000 joint: IBO press release Feb 10 2026, "New York City's PIT currently has four marginal tax rates that range from 3.078% to 3.876%. Rate increases peak at $50,000 if filing individually, $60,000 if filing as head of household or $90,000 if filing a joint return." https://www.ibo.nyc.gov/assets/ibo/downloads/pdf/press-releases/2026/2026-pit-2023-tables-press-release.pdf
- Flat above that: IBO, Analysis of the 2027 Preliminary Budget, Mar 24 2026, p.9, "City residents with AGIs ranging from $60,000 to $5 billion ... pay at the rate of 3.876%." (research/02)
- Residents only: the IBO tables and press release cover "tax returns ... filled by New York City residents"; the tax is imposed on "every city resident individual" (Admin Code 11-1701, quoted in research/02 verification item 3).
- The 2026 ask: IBO Mar 2026 p.9, "which would raise the topmarginal rate from 3.876% to 5.876%"; declined per NY Focus May 29 2026 (research/02).
- The sentence that the state's rates are "higher and more graduated" rests on the state's published schedule (top rate above the city's 3.876), which this session did not download; verify against tax.ny.gov before publishing or soften to "the state income tax, which is separate".

Blind-check note (2026-10-02): the state schedule has nine rates from 4 to 10.9 percent (top bracket at $25 million), per Form IT-201 instructions read by the checker; the page now says so. Of the $1,699 million drop in the top band's liability after refundable credits, $1,575 million is the PTET credit and $125 million the UBT credit (IBO workbook), so "mostly," not "almost entirely."
