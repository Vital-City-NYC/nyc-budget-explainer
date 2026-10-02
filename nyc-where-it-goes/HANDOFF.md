# Where New York City's money goes — handoff

Started 2026-10-02 as the companion to `../nyc-who-pays/`. Same card system, same mechanism: 100 squares of General Fund spending, fiscal 2000-2027.

## Built
- Movement 1: waffle by ten buckets (schools, social services, police/fire/courts/jails, pensions, benefits+claims, debt service, health and hospitals, general government, sanitation/water, everything else). Click a line: sparkline, in-place split by agency for that year (top five plus everything else, audited schedule rows for 2000-2025, OMB agency tables for 2026-27), and a "facts" list under the waffle from `data/context_facts.json` (per-pupil spending, officers per capita and the like; research/03, in progress when this was written).
- "What the squares leave out": capital borrowing, debt outstanding, out-year gaps (`data/offbudget.json`, research/01 C).
- Method table; tile to the companion.
- Movement 3 (what the mayor can change without Albany on the spending side) renders only if `data/control.json` exists: keys = bucket keys, each {fixed:bool, setter, who, alone, limits}, plus optional sub, quote, quote_cite, finding ("{city}" is replaced), note. Research for it: research/02 (agent, in progress).

## Data
- `spending_per_100.json` built by the script in this session from `nyc-budget-per-capita/data.json`, `data/out/omb_agencies.json` and `data/out/acfr_raw.csv` (agency-to-function map derived from the FY2025 ACFR schedule headings, saved as `data/agency_map.json`). Provenance with page numbers: research/01.
- Caveat on the page: the budget's Miscellaneous line (098) inflates the benefits bucket in 2026-27 relative to the audited years.

## Open
- Fill `data/control.json` and `data/context_facts.json` from research/02 and 03 once verified; every fact needs URL + quote.
- Not pushed; same account rule as the companion.
