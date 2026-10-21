#!/usr/bin/env python3
# Title: Audit-trail check for part one of "New York City's budget in $100"
# Author: Josh Greenman / Vital City, with Claude
# Date: October 19, 2026
# Description: Fails loudly unless
#   1. the upstream nyc-budget-per-capita checkout is at the pinned commit, with the files we read unedited;
#   2. every source PDF matches the checksum in sources.lock.json (upstream copies always; the rest with --fetch);
#   3. the four payer breakdowns carry period, basis and coverage fields;
#   4. every breakdown the first chart draws as a split of its squares partitions its parent total each year
#      (aid by function must add to state and federal aid), the snapshot breakdowns add to 100, the $100
#      buckets add to each year's total, and the line-by-line control sort adds to its two groups.
# Usage: python3 check_audit_trail.py [--fetch]    BUDGET_REPO=/path/to/nyc-budget-per-capita
# Dependencies: Python 3.9+ standard library; curl for --fetch
import hashlib, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PART = os.path.abspath(os.path.join(HERE, '..'))
ROOT = os.path.abspath(os.path.join(PART, '..'))
REPO = os.environ.get('BUDGET_REPO', os.path.join(ROOT, 'nyc-budget-per-capita'))
FETCH = '--fetch' in sys.argv
LOCK = json.load(open(os.path.join(HERE, 'sources.lock.json')))
J = lambda rel: json.load(open(os.path.join(PART, rel)))
fails, notes = [], []

def check(ok, msg):
    print(('PASS  ' if ok else 'FAIL  ') + msg)
    if not ok: fails.append(msg)

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()

# ---------------------------------------------------------------- 1. upstream pin
print('== upstream pin')
git = lambda *a: subprocess.run(['git', '-C', REPO] + list(a), capture_output=True, text=True).stdout.strip()
check(os.path.isdir(REPO), f'upstream checkout found at {REPO}')
head = git('rev-parse', 'HEAD')
check(head == LOCK['upstream']['commit'], f"upstream HEAD {head[:12] or '?'} is the pinned {LOCK['upstream']['commit'][:12]}")
for rel, want in LOCK['upstream']['files'].items():
    p = os.path.join(REPO, rel)
    check(os.path.exists(p) and sha256(p) == want, f'upstream {rel} matches its pinned checksum')

# ---------------------------------------------------------------- 2. source PDFs
print('== source PDFs')
tmp = tempfile.mkdtemp(prefix='budget-src-')
for s in LOCK['pdfs']:
    if s.get('browser_only'):
        notes.append(f"not checked: {s['name']} (server refuses scripts; MD5 {s['md5']} recorded from a browser download)"); continue
    path = os.path.join(REPO, s['upstream_path']) if s.get('upstream_path') else os.path.join(PART, s['local_path']) if s.get('local_path') else None
    if not (path and os.path.exists(path)):
        if not FETCH:
            notes.append(f"not checked: {s['name']} (no local copy; run with --fetch)"); continue
        path = os.path.join(tmp, re.sub(r'[^A-Za-z0-9.]+', '_', s['url'].rsplit('/', 1)[-1]))
        r = subprocess.run(['curl', '-sSL', '-A', 'Mozilla/5.0', '-o', path, s['url']])
        if r.returncode or not os.path.exists(path):
            check(False, f"{s['name']} downloads from {s['url']}"); continue
    check(sha256(path) == s['sha256'], f"{s['name']} matches sha256 {s['sha256'][:12]}")

# ---------------------------------------------------------------- 3. period, basis, coverage
print('== breakdown metadata')
for f in ('property_tax_by_class', 'pit_by_income', 'business_by_sector', 'aid_by_function'):
    d = J(f'data/{f}.json')
    check(all(isinstance(d.get(k), str) and d[k].strip() for k in ('period', 'basis', 'coverage')), f'{f}.json has period, basis and coverage')

# ---------------------------------------------------------------- 4. partitions
print('== partitions')
rev = J('data/revenue_per_100.json')['years']
for y, v in sorted(rev.items()):
    check(abs(sum(v['groups'].values()) - v['total']) < 2, f'revenue_per_100 {y}: eight buckets add to the total ({v["total"]:,.0f} thousand)')

# Which breakdowns does the first chart draw as a split of its squares? Those registered in BREAK without snap:1.
html = open(os.path.join(PART, 'index.html'), encoding='utf-8').read()
script = html[html.index('<script>') + 8: html.rindex('</script>')]
split_keys, snap_keys = set(), set()
for m in re.finditer(r'BREAK\.(\w+)\s*=\s*\{', script):
    depth, i = 0, m.end() - 1                                 # walk to the matching brace of this object literal
    while True:
        depth += {'{': 1, '}': -1}.get(script[i], 0); i += 1
        if depth == 0: break
    (snap_keys if re.search(r'\bsnap\s*:\s*1\b', script[m.end() - 1:i]) else split_keys).add(m.group(1))
check(bool(split_keys | snap_keys), f'found the breakdowns on the page (split: {sorted(split_keys)}; snapshot: {sorted(snap_keys)})')
TESTED = {'state_aid', 'federal_aid'}
check(split_keys <= TESTED, f'every split drawn in the first chart has a partition test (untested: {sorted(split_keys - TESTED) or "none"})')

aid = J('data/aid_by_function.json')['years']
check(len(aid) == 10, f'aid_by_function covers {len(aid)} fiscal years ({min(aid)}-{max(aid)})')
for y, v in sorted(aid.items()):
    for kind, bucket in (('state', 'state_aid'), ('federal', 'federal_aid')):
        fn = sum(v[kind].values()); printed = v['tot'][kind]; chart = rev[y]['groups'][bucket]
        check(abs(fn - printed) < 2 and abs(printed - chart) < 2,
              f'{y} {kind} aid: functions {fn:,.0f} = printed total {printed:,.0f} = chart {bucket} {chart:,.0f} (thousands)')

pt = J('data/property_tax_by_class.json')
check(abs(sum(c['levy_m'] for c in pt['classes']) - pt['levy_total_m']) < 0.25, f"property classes add to the levy ({sum(c['levy_m'] for c in pt['classes']):,.1f} of {pt['levy_total_m']:,.1f} million)")
for key in ('levy_share', 'mv_share'):
    t = sum(c[key] for c in pt['classes']); check(abs(t - 100) < 0.2, f'property {key} adds to 100 ({t:.2f})')
it = J('data/pit_by_income.json')
for key in ('filer_share', 'income_share', 'tax_share', 'net_share'):
    t = sum(b[key] for b in it['bands']); check(abs(t - 100) < 0.3, f'income tax {key} adds to 100 ({t:.1f})')
bz = J('data/business_by_sector.json')
t = sum(s['tax_share'] for s in bz['sectors']); check(abs(t - 100) < 0.3, f'business tax_share adds to 100 ({t:.1f})')

ctl = J('research/02-control-lines-fy2027.json')
cls = {}
for g, v in ctl['groups'].items():
    t = sum(l['amount'] for l in v['lines']); chart = rev['2027']['groups'][g] * 1000
    check(abs(t - v['total']) < 1 and abs(v['total'] - chart) < 1000, f'control sort {g}: {len(v["lines"])} lines add to ${t:,.0f} = chart FY2027 {g}')
    check(all(l['class'] in ctl['classes'] and l.get('quote') and l['src'] in ctl['sources'] for l in v['lines']), f'control sort {g}: every line has a class, source and quote')
    for l in v['lines']: cls[l['class']] = cls.get(l['class'], 0) + l['amount']
check(abs(cls.get('intra', 0)) < 1, 'intra-city revenue nets to zero')

# ---------------------------------------------------------------- the city-set share this sort would support (not on the page)
tot = rev['2027']['total'] * 1000
water = sum(l['amount'] for g in ctl['groups'].values() for l in g['lines'] if l.get('flag') == 'cost_reimbursement')
city = rev['2027']['groups']['property_tax'] * 1000 + cls['city']
print('== FY2027 city-set share (proposal only)')
print(f"   property tax plus city-set lines: ${city / 1e6:,.1f} million = {city / tot * 100:.2f} per $100")
print(f"   without water and sewer charges (a cost reimbursement): {(city - water) / tot * 100:.2f} per $100")
print(f"   unsorted lines: ${cls.get('unsorted', 0) / 1e6:,.1f} million = {cls.get('unsorted', 0) / tot * 100:.2f} per $100")

for n in notes: print('NOTE  ' + n)
print(f"\n{'FAILED: ' + str(len(fails)) + ' check(s)' if fails else 'All checks passed.'}")
sys.exit(1 if fails else 0)
