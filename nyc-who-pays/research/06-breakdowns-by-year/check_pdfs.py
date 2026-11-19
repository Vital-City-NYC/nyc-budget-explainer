"""Independent check: every figure in the property and business series appears on the PDF page it cites."""
import json, re, sys, hashlib, fitz
R = sys.argv[1]
def page_text(path, pno):
    d = fitz.open(path); return d[pno - 1].get_text()
fmt1 = lambda x: f'{x:,.1f}'
fmt0 = lambda x: f'{round(x):,}'
bad = 0
# ---- property
notes = open(f'{R}/prop/notes.md').read()
loc = {u: f for u, f in re.findall(r'\|\s*(https?://\S+?)\s*\|\s*(src/\S+?)\s*\|', notes)}
P = json.load(open(f'{R}/prop/prop_by_class.json'))['years']
n = 0
for y, v in sorted(P.items()):
    s = v['levy_src']; f = loc.get(s['url'])
    if not f: print('prop', y, 'no local file for', s['url']); bad += 1; continue
    pno = int(re.search(r'PDF p\. (\d+)', s['page']).group(1))
    t = page_text(f'{R}/prop/{f}', pno).replace(' ', ' ')
    for k in ['total_m', 'c1_m', 'c2_m', 'c3_m', 'c4_m']:
        n += 1
        if fmt1(v[k]) not in t and f'{v[k]:.1f}' not in t:
            print('prop', y, k, v[k], 'NOT on', f, 'p', pno); bad += 1
    if abs(v['c1_m'] + v['c2_m'] + v['c3_m'] + v['c4_m'] - v['total_m']) > 0.15: print('prop', y, 'classes do not add'); bad += 1
print('property figures checked', n)
# ---- business
B = json.load(open(f'{R}/biz/biz_by_sector.json'))['years']
n = 0
for y, v in sorted(B.items()):
    s = v['src']; t = page_text(f'{R}/biz/{s["file"]}', int(s['pdf_page'])).replace(' ', ' ')
    if hashlib.md5(open(f'{R}/biz/{s["file"]}', 'rb').read()).hexdigest() != s['md5']: print('biz', y, 'md5 differs'); bad += 1
    nums = set(re.findall(r'\d{1,3}(?:,\d{3})+|\d+', t))
    for k in ['s1', 's2', 's3', 's4', 's5']:
        n += 1
        if fmt0(v['sectors'][k]) not in nums: print('biz', y, k, v['sectors'][k], 'NOT on page'); bad += 1
    n += 1
    if fmt0(v['total_liab_k']) not in nums: print('biz', y, 'total NOT on page'); bad += 1
    if abs(sum(v['sectors'].values()) - v['total_liab_k']) > 3: print('biz', y, 'sectors do not add'); bad += 1
print('business figures checked', n)
print('problems', bad)
