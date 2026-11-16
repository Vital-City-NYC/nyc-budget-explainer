# nyc-what-the-city-builds handoff

Built 2026-10-02 as one of four linked parts (nav strip at the top of each; parts one and two are nyc-who-pays and nyc-where-it-goes). Part four: capital spending by function, fiscal 2000-2025, with bonds issued and debt service. Data: data/capital_per_100.json. Research with URL + quote in research/. Same rules as part one: Vital City card system, no wordmark; node --check before preview; no number without a source. Publish destination: Vital-City-NYC/nyc-budget-explainer (GitHub Pages), folders at the repo root.

Design pass Oct 3 2026: see ../nyc-who-pays/HANDOFF.md ("Design pass") for the shared stylesheet and script and the layout rules.


## Expert comments, Nov. 16 2026
- The yearly bars default to construction prices (BEA structures index, data/construction_prices.json), with a switch to consumer prices. Headline ratio is 1.1 times on construction prices, 1.7 times on consumer prices. Derivation in research/01, same date.
- "Schools and colleges" is now "Public schools and CUNY."
