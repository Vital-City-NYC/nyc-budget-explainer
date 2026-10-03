# Where New York City's money goes — handoff

Started 2026-10-02 as the companion to `../nyc-who-pays/`. Same card system, same mechanism: 100 squares of General Fund spending, fiscal 2000-2027.

## Built
- Movement 1: waffle by ten buckets (schools, social services, police/fire/courts/jails, pensions, benefits+claims, debt service, health and hospitals, general government, sanitation/water, everything else). Click a line: sparkline, in-place split by agency for that year (top five plus everything else, audited schedule rows for 2000-2025, OMB agency tables for 2026-27), and a "facts" list under the waffle from `data/context_facts.json` (per-pupil spending, officers per capita and the like; research/03, in progress when this was written).
- "What the squares leave out": capital borrowing, debt outstanding, out-year gaps (`data/offbudget.json`, research/01 C).
- Method table; tile to the companion.
- Movement 3 (what the mayor can change without Albany on the spending side) renders only if `data/control.json` exists: keys = bucket keys, each {fixed:bool, setter, who, alone, limits}, plus optional sub, quote, quote_cite, finding ("{city}" is replaced), note. Research for it: research/02 (agent, in progress).

## Added Oct 2 (later)
- Click state now shows three lists in the key: agency split (or unit-of-appropriation split for single-agency lines), inside the biggest agency (OMB ss6-26 units, data/inside.json, research/04), and who pays for it (city/state/federal/other from the same schedules, data/funding_by_bucket.json, research/05). A separate "who pays for what" page was built and then cut at Josh's request; this is where it lives now.
- Four parts total now: who pays, where it goes, since 2000, what it builds.

## Data
- `spending_per_100.json` built by the script in this session from `nyc-budget-per-capita/data.json`, `data/out/omb_agencies.json` and `data/out/acfr_raw.csv` (agency-to-function map derived from the FY2025 ACFR schedule headings, saved as `data/agency_map.json`). Provenance with page numbers: research/01.
- Caveat on the page: the budget's Miscellaneous line (098) inflates the benefits bucket in 2026-27 relative to the audited years.

## Published
Live since 2026-10-02 at https://vital-city-nyc.github.io/nyc-budget-explainer/nyc-where-it-goes/ (repo Vital-City-NYC/nyc-budget-explainer, Pages from main, the five part folders at the repo root plus a root redirect and .nojekyll). To redeploy: copy the five folders into a checkout of that repo and push with the vitalcity-nyc token. The nav strip links all five parts by relative path, so folder names must stay the same.

## Open
- Fill `data/control.json` and `data/context_facts.json` from research/02 and 03 once verified; every fact needs URL + quote.
- Not pushed; same account rule as the companion.

## Design pass, Oct 3 2026
- All four pages now load one shared stylesheet and script: `nyc-who-pays/shared/budget.css` and `budget.js` (other parts reference `../nyc-who-pays/shared/`). Bump the `?v=` stamp on those links in all four index.html files whenever either changes.
- Phone layout: the waffle becomes a 20-by-5 strip pinned to the top of the screen while the key scrolls (`.lay.main` with `.wcol{display:contents}` and `position:sticky`).
- Click-splits use shades of the clicked line's own colour (`B.ramp`), never other lines' colours. Income bands run light to dark.
- Big blocks are labelled on the waffle on desktop (`B.labels`); key rows preview on hover and work from the keyboard.
- Trend lines and bars start at zero (Josh's standing rule), so no zero toggle is needed.
- Long caveats sit in `<details class="more">`; bucket tables are folded in the method.
- Part one has a "Four numbers behind the fair-share argument" strip (two numbers for each side: 37% from 0.9% of filers and 93% of corporate tax from 1,912 firms; the flat 3.876% top rate from $50,000 and homes' 14% of property tax on 50% of value). Part two has "Schools and the safety net, in four numbers" (`data/headline_stats.json`). Keep both strips balanced if editing.
- Part three shades each row: lighter squares are the 2000 level, darker are added since. Part four has a clickable bar chart of capital spending by year in fiscal 2025 dollars.
