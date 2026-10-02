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

## Open
- Not pushed. Confirm the account (joshgreenman1973 Pages unless Josh says Vital City) before pushing; then reply with the live URL.
- Preview: `experiments-root` launch entry serves /Users/joshgreenman/Experiments on 8977; this session edited in the worktree and mirrored files into the main checkout so that URL showed changes. Keep both in sync or stop mirroring once merged.
- `node --check` the script before every preview (extract between `<script>` tags).
