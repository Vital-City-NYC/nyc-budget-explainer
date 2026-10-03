# Who pays for New York City's government? — handoff

Updated 2026-10-02 (second session). Companion page: `../nyc-where-it-goes/` (where the money goes); the two link to each other by a tile at the bottom.

## What is built (index.html, Vital City card system, no wordmark)
- Movement 1: 100-square waffle of General Fund revenue, slider fiscal 2000-2027, play. Click a source to isolate it, open its 28-year line and, where data exists, split its squares in place by who pays it (pop animation, sub-legend with dollars of the $100, source link): property tax by class (DOF FY2026), personal income tax by income band (IBO, tax year 2023), business taxes by sector (DOF, tax year 2022), state and federal aid by what the grants fund (ACFR, fiscal 2016-2025 only; other years show a caption saying so). "Grey out what Albany controls" checkbox.
- Movement 2: Who pays the property tax (toggle share of tax / share of market value; click a row to isolate). Movement 2b: Who pays the income tax (share of tax / share of filers; table also shows share of income). Both use the same `split()` function.
- Movement 3: the same $100 (fiscal 2027) with Albany/Washington-controlled squares greyed; IBO pull quote; control table full width, stacked on phones.
- Method: table of the eight buckets, audited lines vs budget lines; the PTET break explained; source links.
- Framing note from Josh (Oct 2): the intro will ask whether the rich pay their fair share and whether the safety net is generous. The income-tax sentence states share of filers, share of income and share of tax together so both readings are visible. Keep that balance in any copy edit.

## Data (all with URL + verbatim quote in research/)
- `revenue_per_100.json` (research/05): ACFR fiscal 2000-2025; OMB erc6-26.pdf for 2026-27. Buckets follow the audited report's own groupings (mortgage and cigarette taxes sit in sales; PTET sits in business taxes in the audit but in PIT in the budget).
- `property_tax_by_class.json` (research/01), `pit_by_income.json` (research/04), `business_by_sector.json` (research/04 D), `aid_by_function.json` (research/05 A, by-function rows), `control.json` (research/02, including the verification pass at the bottom).
- Still UNVERIFIED and not on the page: CBC effective rates, hotel tax state enabling statute, UBT credit cut.

## Published
Live since 2026-10-02 at https://vital-city-nyc.github.io/nyc-budget-explainer/nyc-who-pays/ (repo Vital-City-NYC/nyc-budget-explainer, Pages from main, the five part folders at the repo root plus a root redirect and .nojekyll). To redeploy: copy the five folders into a checkout of that repo and push with the vitalcity-nyc token. The nav strip links all five parts by relative path, so folder names must stay the same.

## Open
- Not pushed. Confirm the account (joshgreenman1973 Pages unless Josh says Vital City) before pushing; then reply with the live URL.
- Preview: `experiments-root` launch entry serves /Users/joshgreenman/Experiments on 8977; this session edited in the worktree and mirrored files into the main checkout so that URL showed changes. Keep both in sync or stop mirroring once merged.
- `node --check` the script before every preview (extract between `<script>` tags).

## Design pass, Oct 3 2026
- All four pages now load one shared stylesheet and script: `nyc-who-pays/shared/budget.css` and `budget.js` (other parts reference `../nyc-who-pays/shared/`). Bump the `?v=` stamp on those links in all four index.html files whenever either changes.
- Phone layout: the waffle becomes a 20-by-5 strip pinned to the top of the screen while the key scrolls (`.lay.main` with `.wcol{display:contents}` and `position:sticky`).
- Click-splits use shades of the clicked line's own colour (`B.ramp`), never other lines' colours. Income bands run light to dark.
- Big blocks are labelled on the waffle on desktop (`B.labels`); key rows preview on hover and work from the keyboard.
- Trend lines and bars start at zero (Josh's standing rule), so no zero toggle is needed.
- Long caveats sit in `<details class="more">`; bucket tables are folded in the method.
- Part one has a "Four numbers behind the fair-share argument" strip (two numbers for each side: 37% from 0.9% of filers and 93% of corporate tax from 1,912 firms; the flat 3.876% top rate from $50,000 and homes' 14% of property tax on 50% of value). Part two has "Schools and the safety net, in four numbers" (`data/headline_stats.json`). Keep both strips balanced if editing.
- Part three shades each row: lighter squares are the 2000 level, darker are added since. Part four has a clickable bar chart of capital spending by year in fiscal 2025 dollars.
