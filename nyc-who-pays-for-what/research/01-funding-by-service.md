# 01. Who pays for what: funding source by service, fiscal 2027

Compiled 2026-10-02. Source: NYC Office of Management and Budget, *Adopted Budget Fiscal Year 2027, Supporting Schedules* (June 2026), https://www.nyc.gov/assets/omb/downloads/pdf/adopt26/ss6-26.pdf (4,716 pages; downloaded and parsed with PyMuPDF). Every unit of appropriation has a "UNIT OF APPROPRIATION SUMMARY" page with a "FUNDING SUMMARY" block: CITY, OTHER CATEGORICAL, CAPITAL FUNDS - I.F.A., STATE, FEDERAL - C.D., FEDERAL - OTHER, INTRA-CITY SALES, in two columns (current modified fiscal 2026, adopted fiscal 2027). This page uses the adopted column.

Sample, verbatim, PDF p. 693 (Police Department, U/A 001 Special Operations & Support Services): "APPROPRIATION | 2,556 | 314,245,261 | 2,555 | 317,376,826 | 3,131,565" and "CITY 280,409,749 305,468,040 25,058,291 / OTHER CATEGORICAL 2,958,633 2,958,633- / STATE 1,279,782 644,464 635,318- / FEDERAL - OTHER 29,362,673 11,264,322 18,098,351- / INTRA-CITY SALES 234,424 234,424- / TOTAL 314,245,261 317,376,826 3,131,565".

Method: 716 unit pages across 141 agencies parsed; each agency's units sum, net of intra-city sales, matches OMB's agency total in the Expense Revenue Contract document to within $1 million for every agency (checked in this session; the gross-minus-intra-city identity is exact for all but rounding). Intra-city sales are dropped (an agency paying another agency, counted once already); Capital IFA is counted with city funds; "other categorical" is shown as other grants. Agencies map to the ten lines of part two using the audited report's classification (`../nyc-where-it-goes/data/agency_map.json`, plus 095 pensions, 098 Miscellaneous = benefits, 099 debt service, 126 Cultural Affairs = parks).

Result, fiscal 2027 adopted ($ millions): city 96,917; state 20,813; federal 7,374; other 1,138; total 126,242, which equals the budget's net total expense (research/01 in part two). State and federal totals match the Comptroller's Table A1 ("Total State Grants $20,813"; "Total Federal Grants $7,374", research/03 in part one).

By line ($ millions, city / state / federal / other):
- general_government: 5,240 / 120 / 181 / 175
- public_safety: 11,598 / 127 / 60 / 344
- everything_else: 5,339 / 480 / 983 / 44
- education: 21,353 / 15,123 / 2,029 / 68
- social_services: 17,579 / 2,334 / 3,462 / 0
- pensions: 8,574 / 133 / 0 / 0
- benefits: 12,957 / 1,752 / 273 / 182
- debt_service: 7,030 / 4 / 83 / 251
- health: 3,289 / 738 / 302 / 74
- environmental: 3,958 / 0 / 1 / 1

Self-audit: HIGH for every number (read from the PDF text, reconciled to agency totals and to the Comptroller's state and federal totals). Editorial: the bucket mapping and the treatment of IFA and intra-city.
