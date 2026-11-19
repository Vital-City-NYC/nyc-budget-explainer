"""Independent check of the income tax series: re-read sheet 8 of each saved IBO workbook, group the rows into the six bands, compare."""
import json, re, sys, os, hashlib
R = sys.argv[1]
d = json.load(open(f'{R}/pit/pit_by_band.json'))['years']
def rows_xlsx(p):
    import openpyxl
    wb = openpyxl.load_workbook(p, data_only=True, read_only=True); ws = wb[[n for n in wb.sheetnames if n.strip().startswith('8')][0]]
    return [(r[0], r[1], r[5]) for r in ws.iter_rows(min_row=19, max_row=39, values_only=True)]
def rows_xls(p):
    import xlrd
    wb = xlrd.open_workbook(p); ws = wb.sheet_by_name([n for n in wb.sheet_names() if n.strip().startswith('8')][0])
    return [(ws.cell_value(i, 0), ws.cell_value(i, 1), ws.cell_value(i, 5)) for i in range(18, 39)]
def band(label):
    l = str(label).lower().replace(',', '')
    if 'all' in l: return 'all'
    if 'under' in l or l.startswith('$0') or l.startswith('0'): return 'i1'
    lo = float(re.findall(r'\d+', l)[0])
    for cut, k in [(1_000_000, 'i6'), (500_000, 'i5'), (200_000, 'i4'), (100_000, 'i3'), (50_000, 'i2')]:
        if lo >= cut: return k
    return 'i1'
bad = 0
for y, v in sorted(d.items()):
    f = v['src'].get('local_file')
    if not f or not os.path.exists(f'{R}/pit/{f}'): print(y, 'no local workbook (read in the browser):', v['src'].get('file')); continue
    p = f'{R}/pit/{f}'
    if v['src'].get('md5') and hashlib.md5(open(p, 'rb').read()).hexdigest() != v['src']['md5']: print(y, 'md5 differs'); bad += 1
    rows = rows_xls(p) if p.endswith('.xls') else rows_xlsx(p)
    agg = {}
    for lab, n, liab in rows:
        if lab is None or liab in (None, ''): continue
        k = band(lab); a = agg.setdefault(k, [0, 0]); a[0] += float(n); a[1] += float(liab)
    scale = 1e-6 if agg['all'][1] > 1e6 else 1   # some workbooks are in dollars, some in millions
    for k in ['i1', 'i2', 'i3', 'i4', 'i5', 'i6']:
        mine = agg[k][1] * scale; theirs = v['bands'][k]['liab_m']
        if abs(mine - theirs) > 0.06: print(y, k, 'liability mine', round(mine, 2), 'json', theirs); bad += 1
    if abs(agg['all'][1] * scale - v['total_liab_m']) > 0.06: print(y, 'total differs'); bad += 1
print('problems', bad)
