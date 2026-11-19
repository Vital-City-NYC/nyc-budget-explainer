"""Adds each year's breakdown to the property, income and business tax data files, so the $100 chart can split those squares by the year shown.

Reads the verified series in research/06-breakdowns-by-year/ (every figure there carries its URL, page and quoted row in the notes files)
and writes a "years" block into data/property_tax_by_class.json, data/pit_by_income.json and data/business_by_sector.json.
The one-year fields the lower charts use are left as they are. Fails loudly if a year's parts do not add to its total.
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RES = os.path.join(ROOT, 'research', '06-breakdowns-by-year')
DATA = os.path.join(ROOT, 'data')
r2 = lambda x: round(x, 2)

def load(name):
    p = os.path.join(RES, name)
    return json.load(open(p)) if os.path.exists(p) else None

def save(name, d):
    p = os.path.join(DATA, name)
    with open(p, 'w') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    print('wrote', name)

def check(label, parts, total, tol):
    s = sum(parts)
    if abs(s - total) > tol:
        sys.exit(f'FAIL {label}: parts {s} vs total {total}')

# ---- property tax: fiscal year levy by class
P = load('property_by_class.json')
if P:
    d = json.load(open(os.path.join(DATA, 'property_tax_by_class.json')))
    out = {}
    for y, v in sorted(P['years'].items()):
        t = v['total_m']
        check('property ' + y, [v['c1_m'], v['c2_m'], v['c3_m'], v['c4_m']], t, 0.15)
        e = {'levy_total_m': t, 'c1': r2(v['c1_m'] / t * 100), 'c3': r2(v['c3_m'] / t * 100), 'c4': r2(v['c4_m'] / t * 100),
             'src': v['levy_src']['url'], 'table': v['levy_src']['table'] + ', ' + v['levy_src']['page'],
             'edition': 2000 + int(re.search(r'fy\s*(\d\d)', v['levy_src']['url'], re.I).group(1))}   # the report whose class-levy table gives this year
        sh = v['c2_rental_share']
        if sh is None:
            e['c2'] = r2(v['c2_m'] / t * 100)
        else:
            e['c2r'] = r2(v['c2_m'] * sh / t * 100); e['c2o'] = r2(v['c2_m'] * (1 - sh) / t * 100)
            e['split_src'] = v['split_src']['url']; e['split_table'] = v['split_src']['table'] + ', ' + v['split_src']['page']
        out[y] = e
    d['years'] = out
    d['years_note'] = ('Each fiscal year\'s levy by class from the Department of Finance\'s class-levy history table (the newest annual report that prints the year). '
                       'Class 2 is divided between rental buildings and co-ops and condos by that year\'s own reconciliation by property type, gross levy, from fiscal 2005; '
                       'earlier reports have no levy by property type, so fiscal 2000 to 2004 show Class 2 whole. Before fiscal 2010 condo buildings with rental units are counted with condos.')
    save('property_tax_by_class.json', d)

# ---- business taxes: tax year liability by sector
Bz = load('business_by_sector.json')
if Bz:
    d = json.load(open(os.path.join(DATA, 'business_by_sector.json')))
    out = {}
    for y, v in sorted(Bz['years'].items()):
        t = v['total_liab_k']; s = v['sectors']
        check('business ' + y, s.values(), t, 3)
        e = {k: r2(s[k] / t * 100) for k in ['s1', 's2', 's3', 's4', 's5', 's6']}
        e.update({'total_m': round(t / 1000, 1), 'taxes': v['taxes'], 'src': v['src']['url'], 'table': f"{v['src']['table']}, PDF p. {v['src']['pdf_page']}"})
        out[y] = e
    d['years'] = out
    d['years_note'] = ('Each tax year\'s liability by industry from that year\'s Statistical Profiles of New York City Business Income Taxes, combined table. '
                       'Through tax year 2014 the table covers the banking corporation, general corporation and unincorporated business taxes; '
                       'from 2015 the business corporation tax replaced the first and most of the second.')
    save('business_by_sector.json', d)

# ---- income tax: tax year liability before credits by income band
I = load('income_by_band.json')
if I:
    d = json.load(open(os.path.join(DATA, 'pit_by_income.json')))
    out = {}
    for y, v in sorted(I['years'].items()):
        t = v['total_liab_m']; b = v['bands']
        check('income ' + y, [b[k]['liab_m'] for k in b], t, 0.6)
        e = {k: r2(b[k]['liab_m'] / t * 100) for k in ['i1', 'i2', 'i3', 'i4', 'i5', 'i6']}
        # IBO's old links for 2006-2020 and 2022 now redirect; the archived copy of the same address is the working link
        e.update({'total_m': round(t, 1), 'returns': v['total_returns'], 'src': v['src'].get('archive_url') or v['src']['url'], 'table': f"{v['src'].get('file', '')}, sheet {v['src'].get('sheet', '')}, rows {v['src'].get('rows', '')}"})
        out[y] = e
    d['years'] = out
    d['years_note'] = 'Each tax year\'s city residents\' income tax liability before credits by income, from the Independent Budget Office\'s tables for that year.'
    save('pit_by_income.json', d)
