# Embedding the budget explainer in a Ghost article

One HTML card carries all four parts. The reader can move between parts inside the frame; the frame resizes itself as lines are opened.
Start it on any part by changing the `src` folder (`nyc-who-pays`, `nyc-where-it-goes`, `nyc-budget-since-2000`, `nyc-what-the-city-builds`).
To open a year or a line on arrival, add a hash, e.g. `...nyc-who-pays/?embed=1#y=2025&k=personal_income_tax`.

```html
<!-- New York City's budget in $100: Vital City embed -->
<div class="vc-embed-nyc-budget" style="margin:1.5em 0;">
  <div style="position:relative;width:100%;border:1px solid #111;overflow:hidden;">
    <iframe class="vc-embed-nyc-budget__iframe"
      src="https://vital-city-nyc.github.io/nyc-budget-explainer/nyc-who-pays/?embed=1"
      title="New York City's budget in $100" loading="lazy" scrolling="no"
      style="display:block;width:100%;height:1400px;border:0;background:transparent;"></iframe>
  </div>
  <p style="font-size:0.8em;color:#666;margin:0.5em 0 0;text-align:center;">
    Click any line to open it.
    <a href="https://vital-city-nyc.github.io/nyc-budget-explainer/nyc-who-pays/" target="_blank" rel="noopener">Open full screen</a>
  </p>
  <script>
    (function () {
      window.addEventListener('message', function (e) {
        var d = e && e.data;
        if (!d || d.type !== 'vc-embed-height' || d.id !== 'nyc-budget-explainer') return;
        var f = document.querySelector('.vc-embed-nyc-budget__iframe');
        if (f && typeof d.height === 'number') f.style.height = d.height + 'px';
      });
    })();
  </script>
</div>
```

Notes
- Every part posts its height under the shared id `nyc-budget-explainer` (and under its own folder name), on load and whenever the card changes size.
- Inside a frame the phone layout's pinned waffle scrolls with the article instead of sticking; everything else behaves the same.
- To embed a single part without the others, use that part's folder and its own id in the listener.
