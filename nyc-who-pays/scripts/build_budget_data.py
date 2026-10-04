#!/usr/bin/env python3
# Title: Build the derived data files for "New York City's budget in $100"
# Author: Josh Greenman / Vital City, with Claude
# Date: October 2-3, 2026
# Data sources (all public):
#   - NYC Comptroller, Annual Comprehensive Financial Reports (FY2005, FY2015, FY2025 editions),
#     as extracted by the nyc-budget-per-capita repo (data.json, data/out/acfr_raw.csv with page numbers)
#   - NYC OMB, Adopted Budget FY2027: Expense Revenue Contract (erc6-26.pdf), as extracted by the
#     same repo (data/out/omb_agencies.json, budget_years in data.json), and Supporting Schedules
#     (ss6-26.pdf), parsed here
#   - Census population and BLS CPI series carried in the per-capita repo's data.json
# Description: Writes revenue_per_100, aid_by_function (part one); agency_map, spending_per_100,
#   inside, funding_by_bucket (part two); real_per_resident (part three); capital_per_100 (part four).
#   Hand-entered files, each documented with URL and quotation in research/, are NOT built here:
#   property_tax_by_class, pit_by_income, business_by_sector, control (both parts), context_facts,
#   headline_stats, offbudget.
# Dependencies: Python 3.9+, PyMuPDF (fitz) for the PDF step
# Usage: python3 build_budget_data.py [--out DIR]   (default: write in place under the four part folders)
#   BUDGET_REPO=/path/to/nyc-budget-per-capita  SS_PDF=/path/to/ss6-26.pdf (downloaded if absent)
import csv, json, os, re, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))            # folder holding the four part folders
REPO = os.environ.get('BUDGET_REPO', os.path.join(ROOT, 'nyc-budget-per-capita'))
if not os.path.isdir(REPO): REPO = '/Users/joshgreenman/Experiments/nyc-budget-per-capita'
OUT = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else ROOT
SS_URL = 'https://www.nyc.gov/assets/omb/downloads/pdf/adopt26/ss6-26.pdf'
SS_PDF = os.environ.get('SS_PDF', os.path.join(HERE, 'ss6-26.pdf'))

def out(rel):
    p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p), exist_ok=True); return p
def dump(rel, obj, **kw):
    json.dump(obj, open(out(rel), 'w'), ensure_ascii=False, **kw)

D = json.load(open(os.path.join(REPO, 'data.json')))
RAW = list(csv.DictReader(open(os.path.join(REPO, 'data', 'out', 'acfr_raw.csv'))))
OMB = json.load(open(os.path.join(REPO, 'data', 'out', 'omb_agencies.json')))

# ---------------------------------------------------------------- part one: revenue per $100
# Buckets follow the audited report's own groupings (see research/05-revenue-series.md).
REV = {'property_tax': ['property_tax'], 'personal_income_tax': ['personal_income_tax'], 'sales_tax': ['sales_tax'],
       'business_taxes': ['business_taxes'], 'other_taxes': ['other_taxes', 'tax_penalties'], 'state_aid': ['state_aid'],
       'federal_aid': ['federal_aid'],
       'fees_fines_other': ['charges_for_services', 'fines_forfeitures', 'licenses_permits', 'investment_income', 'other_revenues',
                            'other_grants', 'unrestricted_aid', 'other_financing', 'tobacco_settlement', 'disallowances']}
rev = {'source': 'NYC Comptroller ACFR, General Fund Revenues (statistical section), as extracted in nyc-budget-per-capita',
       'unit': 'thousands of dollars, nominal', 'grouping': REV,
       'budget_years_source': 'OMB adopted budget FY2027 (erc6-26.pdf) as parsed in nyc-budget-per-capita/data.json (budget_years). OMB lines are mapped to the audited buckets: PTET sits inside personal income tax; mortgage and cigarette taxes sit inside sales; other_revenues is OMB miscellaneous plus other categorical grants and inter-fund revenue, less intra-city revenue and disallowances.',
       'years': {}}
for y in D['years']:
    r = y['revenue']; groups = {k: float(sum(r.get(x, 0) for x in xs)) for k, xs in REV.items()}; tot = float(y['revenue_total'])
    assert abs(sum(groups.values()) - tot) < 2, (y['fy'], sum(groups.values()), tot)   # buckets must sum to the printed total
    rev['years'][str(y['fy'])] = {'total': tot, 'groups': groups, 'per_100': {k: round(v / tot * 100, 4) for k, v in groups.items()}, 'ungrouped': []}
for b in D['budget_years']:
    rc = b['revenue_categories']; groups = {k: rc[k] for k in REV if k != 'fees_fines_other'}; groups['fees_fines_other'] = rc['other_revenues']
    tot = sum(groups.values())                                                            # equals the budget's net total
    rev['years'][str(b['fy'])] = {'total': tot, 'groups': groups, 'per_100': {k: round(v / tot * 100, 4) for k, v in groups.items()},
                                  'ungrouped': [], 'basis': b['basis'], 'budgeted': True}
dump('nyc-who-pays/data/revenue_per_100.json', rev, indent=1)

# ---------------------------------------------------------------- part one: state and federal grants by function
FN = {'general government': 'General government', 'public safety and judicial': 'Police, fire, jails and prosecutors', 'education': 'Schools',
      'social services': 'Social services', 'environmental protection': 'Environment', 'transportation services': 'Transportation',
      'parks, recreation and cultural activities': 'Parks and culture', 'housing': 'Housing', 'health': 'Health', 'libraries': 'Libraries',
      'city university': 'City University'}
aid = {'source': 'NYC Comptroller, annual comprehensive financial reports, General Fund revenues ten-year trend, federal and state grants and contracts (categorical) by function',
       'url': 'https://comptroller.nyc.gov/wp-content/uploads/documents/ACFR-2025-7-28-2026.pdf', 'years': {}}
by = {}
for r in RAW:
    if r['table'] == 'gf_revenues': by.setdefault((r['source'], r['fiscal_year']), []).append(r)
for (src, y), rows in by.items():
    rows.sort(key=lambda r: int(r['row_order'])); cur = None; acc = {'state': {}, 'federal': {}}; tot = {}
    for r in rows:
        lab = r['label'].lower().strip()
        if lab.startswith('federal grants and contracts'): cur = 'federal'; lab = lab.split(':', 1)[1].strip()
        elif lab.startswith('state grants and contracts'): cur = 'state'; lab = lab.split(':', 1)[1].strip()
        if lab.startswith('total federal grants'): tot['federal'] = float(r['value_thousands']); cur = None; continue
        if lab.startswith('total state grants'): tot['state'] = float(r['value_thousands']); cur = None; continue
        if lab.startswith('non-governmental'): cur = None
        if cur and lab in FN: acc[cur][FN[lab]] = float(r['value_thousands'])
    if acc['state'] and acc['federal']:
        prev = aid['years'].get(y)
        if prev and prev['src'] > src: continue
        for k in ('state', 'federal'): assert abs(sum(acc[k].values()) - tot[k]) < 2, (y, k)   # functions must sum to the printed total
        aid['years'][y] = {'src': src, 'state': acc['state'], 'federal': acc['federal'], 'tot': tot}
dump('nyc-who-pays/data/aid_by_function.json', aid)

# ---------------------------------------------------------------- part two: agency -> function map
# Read from the headings of the FY2025 ACFR General Fund expenditure schedule, plus codes the schedule does not carry.
HEADS = {'general government': 'general_government', 'public safety and judicial': 'public_safety', 'education': 'education',
         'city university': 'city_university', 'social services': 'social_services', 'environmental protection': 'environmental',
         'transportation services': 'transportation', 'parks recreation and cultural activities': 'parks', 'housing': 'housing',
         'health': 'health', 'libraries': 'libraries', 'pensions': 'pensions'}
hk = lambda s: re.sub(r'[^a-z ]', '', s.lower()).strip()
amap = {}; cur = None
rows25 = sorted([r for r in RAW if r['source'] == 'acfr2025' and r['table'] == 'gf_expenditures' and r['fiscal_year'] == '2025'], key=lambda r: int(r['row_order']))
for r in rows25:
    lab = r['label']; m = re.match(r'^(.*?):\s*(?:\(cont\.\)\s*)?(.*)$', lab)
    if m and hk(m.group(1).split(' (')[0]) in HEADS: cur = HEADS[hk(m.group(1).split(' (')[0])]; lab = m.group(2)
    c = re.match(r'^(\d{3})\s+(.*)$', lab)
    if c and cur: amap[c.group(1)] = {'name': c.group(2).strip(), 'fn': cur}
amap.update({'126': {'name': 'Department of Cultural Affairs', 'fn': 'parks'}, '058': {'name': 'Office of Community Safety', 'fn': 'public_safety'},
             '094': {'name': 'Department of Employment', 'fn': 'social_services'}, '130': {'name': 'Department of Juvenile Justice', 'fn': 'public_safety'},
             '817': {'name': 'Department of Mental Health, Mental Retardation and Alcoholism Services', 'fn': 'health'},
             '264': {'name': 'Educational Aid', 'fn': 'education'}})
dump('nyc-where-it-goes/data/agency_map.json', amap, indent=1)

# ---------------------------------------------------------------- part two: spending per $100
BUCKETS = [('education', 'Schools', ['education']), ('social_services', 'Social services', ['social_services']),
           ('public_safety', 'Police, fire, jails and prosecutors', ['public_safety']), ('pensions', 'Pensions', ['pensions']),
           ('benefits', 'Health insurance, claims and other benefits', ['fringe_benefits', 'judgments', 'lease_payments', 'other_misc']),
           ('debt_service', 'Debt service', ['debt_service']), ('health', 'Health and hospitals', ['health']),
           ('general_government', 'General government', ['general_government']), ('environmental', 'Sanitation, water and sewers', ['environmental']),
           ('everything_else', 'Housing, transportation, CUNY, parks, libraries', ['housing', 'transportation', 'city_university', 'parks', 'libraries'])]
FN2B = {f: k for k, _, fs in BUCKETS for f in fs}
EXTRA = {'040': 'education', '042': 'city_university', '095': 'pensions', '098': 'fringe_benefits', '099': 'debt_service', '058': 'public_safety'}
# OMB erc6-26.pdf, Miscellaneous (098) OTPS detail, printed p. 119E: (FY2026 modified, FY2027 adopted), dollars.
M098 = {'transit': {'Payments to Transit Authority': (910147482, 983812579), 'MTA Bus Company': (563854489, 594825790), 'MTA Payroll Tax': (137562799, 138599499)},
        'debt': {'HYIC TEP': (206276893, 217782360), 'TFA - Retained State Building Aid': (1192413432, 1311838995)}}
def nice(n):
    n = n.replace('—', ' ').replace('’', "'"); n = re.sub(r'\s+', ' ', n).strip(); n = re.sub(r'^Miscellaneous\s*', '', n).strip()
    for a, b in [('Health and Hospitals Corporation', 'Health + Hospitals subsidy'), ('Department of Information Technology and Telecommunications', 'Office of Technology and Innovation'),
                 ('City University of New York Community Colleges', 'CUNY community colleges'), ('Payments to the Transit Authority', 'Transit Authority subsidy'),
                 ('Payments to Private Bus Companies', 'Private bus companies'), ('Payments to the Housing Authority', 'Housing Authority subsidy'),
                 ('Administration for Children', "Administration for Children's Services"), ('Department of Mental Health, Mental Retardation', 'Department of Mental Health')]:
        if n.startswith(a): return b
    return n
def fixcase(n):
    n = re.sub(r"\b(And|Of|For|The)\b", lambda m: m.group(1).lower(), n).replace("'S", "'s")
    return n.replace("Admin for Children's Services", "Administration for Children's Services").replace('Dept ', 'Department ')
# uncoded "Miscellaneous" rows of the audited schedule (transit payments, Legal Aid and so on), by year and function
misc = {}; byy = {}
for r in RAW:
    if r['table'] == 'gf_expenditures': byy.setdefault(r['fiscal_year'], []).append(r)
for y, rows in byy.items():
    if not (2000 <= int(y) <= 2025): continue
    rows.sort(key=lambda r: (r['source'], int(r['row_order']))); cur = None; m = {}
    for r in rows:
        lab = r['label'].strip(); v = float(r['value_thousands']); mm = re.match(r'^(.*?):\s*(?:\(cont\.\)\s*)?(.*)$', lab)
        if mm and hk(mm.group(1).split(' (')[0]) in HEADS and HEADS[hk(mm.group(1).split(' (')[0])] != 'pensions': cur = HEADS[hk(mm.group(1).split(' (')[0])]; lab = mm.group(2).strip()
        elif mm and hk(mm.group(1)) not in HEADS and not re.match(r'^\d{3}', lab): cur = None
        if lab.lower().startswith(('pensions', 'judgments', 'lease', 'fringe', 'other:', 'transfers', 'total')):
            if not lab.lower().startswith('total'): cur = None
            continue
        if cur and not re.match(r'^\d{3}\s', lab) and v and 'community board' not in lab.lower(): m[(cur, nice(lab))] = v
    misc[y] = m
sp = {'source': 'NYC Comptroller ACFR, General Fund expenditures and transfers by function and agency, fiscal 2000-2025; OMB Adopted Budget FY2027 Expense Revenue Contract (erc6-26.pdf), fiscal 2026 as modified and 2027 adopted',
      'unit': 'thousands of dollars, nominal', 'buckets': {k: {'label': l, 'lines': fs} for k, l, fs in BUCKETS}, 'years': {}}
for yr in D['years']:
    y = str(yr['fy']); op = dict(yr['operating']); op['debt_service'] = yr['debt_service']; tot = sum(op.values())
    groups = {k: sum(op.get(f, 0) for f in fs) for k, _, fs in BUCKETS}
    assert abs(sum(groups.values()) - tot) < 2
    ag = {}; cb = 0
    for code, a in D['agencies'].items():
        v = a['v'].get(y); mp = amap.get(code)
        if not v or not mp or mp['fn'] == 'pensions': continue
        name = nice(a['name'])
        if 'community board' in name.lower(): cb += v; continue
        ag.setdefault(FN2B[mp['fn']], []).append([name, v])
    if cb: ag.setdefault('general_government', []).append(['59 community boards', cb])
    for (fn, name), v in misc.get(y, {}).items(): ag.setdefault(FN2B[fn], []).append([name, v])
    for b, lst in ag.items(): assert abs(sum(x[1] for x in lst) - groups[b]) <= groups[b] * 0.004, (y, b)   # agency rows tie to the bucket
    sp['years'][y] = {'total': tot, 'groups': groups, 'per_100': {k: round(v / tot * 100, 4) for k, v in groups.items()},
                      'agencies': {k: sorted(v, key=lambda x: -x[1]) for k, v in ag.items()}}
for i, by_ in enumerate(D['budget_years']):
    y = str(by_['fy']); cat = by_['categories']; tot = by_['total_expense'] / 1000
    groups = {k: sum(cat.get(f, 0) for f in fs) for k, _, fs in BUCKETS}; s = sum(groups.values()); groups = {k: v * tot / s for k, v in groups.items()}
    tr = sum(v[i] for v in M098['transit'].values()) / 1000; db = sum(v[i] for v in M098['debt'].values()) / 1000
    groups['benefits'] -= tr + db; groups['everything_else'] += tr; groups['debt_service'] += db      # file 098's transit and bond lines where the audit files them
    col = 'fy2026_modified' if by_['fy'] == 2026 else 'fy2027_adopted'; ag = {}
    for code, a in OMB.items():
        fn = EXTRA.get(code) or (amap.get(code) or {}).get('fn')
        if not fn or fn in ('pensions', 'fringe_benefits', 'debt_service'): continue
        v = a.get(col, 0) / 1000
        if v > 0: ag.setdefault(FN2B[fn], []).append([fixcase(nice(a['name'].title())), round(v)])
    ag.setdefault('everything_else', []).append(['Transit subsidies (Miscellaneous budget)', round(tr)])
    sp['years'][y] = {'total': round(tot), 'groups': groups, 'per_100': {k: round(v / tot * 100, 4) for k, v in groups.items()},
                      'agencies': {k: sorted(v, key=lambda x: -x[1]) for k, v in ag.items()}, 'budgeted': True, 'basis': by_['basis'],
                      'realloc_note': 'Miscellaneous (098) OTPS reallocated by line: transit subsidies to everything else, HYIC and TFA retained building aid to debt service (OMB erc6-26.pdf printed p. 119E)'}
dump('nyc-where-it-goes/data/spending_per_100.json', sp)

# ---------------------------------------------------------------- part two: units of appropriation and funding (OMB supporting schedules)
if not os.path.exists(SS_PDF):
    subprocess.run(['curl', '-s', '-A', 'Mozilla/5.0', '-o', SS_PDF, SS_URL], check=True)
import fitz
SRC = [('CITY', 'city'), ('OTHER CATEGORICAL', 'other_cat'), ('CAPITAL FUNDS - I.F.A.', 'ifa'), ('STATE', 'state'), ('FEDERAL - C.D.', 'fed_cd'), ('FEDERAL - OTHER', 'fed_other'), ('INTRA-CITY SALES', 'intra')]
nums = lambda s: [(-int(x[:-1].replace(',', '')) if x.endswith('-') else int(x.replace(',', ''))) for x in re.findall(r'[\d,]+-?', s) if re.search(r'\d', x)]
ua = {}
for i, page in enumerate(fitz.open(SS_PDF)):
    t = page.get_text()
    if 'UNIT OF APPROPRIATION SUMMARY' not in t[:300]: continue
    m = re.search(r'AGENCY:\s+(\d{3})\s+(.+)', t); u = re.search(r'UNIT OF APPROPRIATION:\s+(\d{3})\s+(.+)', t)
    if not m or not u: continue
    lines = t.split('\n'); appr = None; fund = {}
    for l in lines:
        if l.startswith('|APPROPRIATION'):
            cells = [c.strip() for c in l.strip('|').split('|')]; appr = nums(cells[4])[0] if nums(cells[4]) else 0; break     # adopted column
    hdr = next((l for l in lines if 'FUNDING SUMMARY' in l and 'ADOPTED BUDGET' in l), None)
    if hdr:
        ad = hdr.index('ADOPTED BUDGET'); inc = hdr.index('INC/DEC')
        for l in lines:
            for lab, key in SRC:
                st = l.strip()
                if st.startswith(lab) and (len(st) == len(lab) or st[len(lab)] == ' '):
                    v = nums(l[ad - 6:inc - 2] if len(l) > ad - 6 else ''); fund[key] = v[0] if v else 0
    ua.setdefault(m.group(1), {'name': m.group(2).strip().title(), 'uas': []})['uas'].append({'code': u.group(1), 'name': u.group(2).strip().title(), 'amount': appr, 'funding': fund, 'page': i + 1})
for c, a in ua.items():                                                       # every agency: units net of intra-city sales must equal OMB's agency total
    t = (OMB.get(c) or {}).get('fy2027_adopted')
    if t is not None: assert abs(sum(x['amount'] or 0 for x in a['uas']) - sum(x['funding'].get('intra', 0) for x in a['uas']) - t) < 5e6, c
fb = {}
for c, a in ua.items():
    fn = EXTRA.get(c) or (amap.get(c) or {}).get('fn'); d = fb.setdefault(FN2B[fn], {'city': 0, 'state': 0, 'federal': 0, 'other': 0})
    for x in a['uas']:
        f = x['funding']; d['city'] += f.get('city', 0) + f.get('ifa', 0); d['state'] += f.get('state', 0); d['federal'] += f.get('fed_cd', 0) + f.get('fed_other', 0); d['other'] += f.get('other_cat', 0)
u2 = next(x for x in ua['098']['uas'] if x['code'] == '002'); f = u2['funding']                 # apportion 098's OTPS unit like the spending lines
for b, key in (('everything_else', 'transit'), ('debt_service', 'debt')):
    sh = sum(v[1] for v in M098[key].values()) / u2['amount']
    for k, val in (('city', f.get('city', 0) + f.get('ifa', 0)), ('state', f.get('state', 0)), ('federal', f.get('fed_cd', 0) + f.get('fed_other', 0)), ('other', f.get('other_cat', 0))):
        fb[b][k] += val * sh; fb['benefits'][k] -= val * sh
tot = {k: sum(v[k] for v in fb.values()) for k in ('city', 'state', 'federal', 'other')}
dump('nyc-where-it-goes/data/funding_by_bucket.json', {'source': "OMB, Adopted Budget Fiscal Year 2027, Supporting Schedules (ss6-26.pdf), Unit of Appropriation Summary pages, Funding Summary, adopted column. Intra-city sales excluded; Capital IFA counted with city funds; other categorical grants shown as other. The Miscellaneous budget's OTPS unit is apportioned to everything else (transit subsidies) and debt service (HYIC, TFA retained building aid) in proportion to those lines, with its funding mix.",
                                                    'url': SS_URL, 'fiscal_year': 2027, 'buckets': fb, 'total': tot}, indent=1)
ALIAS = {'Executive Admin': 'Executive administration', 'Executive Administrative': 'Executive administration', 'Exec & Administrative': 'Executive administration',
         'Emergency Medical Serv': 'Emergency medical services', 'Emergency Medical Services': 'Emergency medical services',
         'Fire Exting And Emerg Resp': 'Fire extinguishing and emergency response', 'Fire Exting & Resp': 'Fire extinguishing and emergency response',
         'Bureau Of Motor Equip': 'Motor equipment', 'Cleaning & Collection': 'Cleaning and collection',
         'Alcohol&Drug Use Prevent, Care Treatment': 'Alcohol and drug use prevention and treatment', 'Shelter Intake And Program': 'Shelter intake and programs',
         'Street Programs': 'Street programs', 'Medical Assistance': 'Medicaid (medical assistance)', 'Public Assistance': 'Public assistance',
         'Chief Of Department': 'Chief of Department', 'Special Operations & Support Services': 'Special operations and support', 'Transit Police': 'Transit police',
         'Housing Police': 'Housing police', 'School Safety': 'School safety', 'Early Intervention': 'Early intervention', 'Disease Control': 'Disease control',
         'Family & Child Health': 'Family and child health', 'Mental Health': 'Mental health', 'Health Administration': 'Administration', 'Legal Services': 'Legal services',
         'Adult Services': 'Adult services', 'Domestic Violence Services': 'Domestic violence services', 'Waste Disposal': 'Waste disposal', 'Snow Budget': 'Snow budget',
         'Fire Prevention': 'Fire prevention', 'Nyc Doc Jail Operations': 'Jail operations', 'Nyc Doc Health And Programs': 'Health and programs',
         'Nyc Doc Transportation': 'Transportation', 'Headstart/Daycare': 'Head Start and child care', 'Personal Services': 'Agency-wide personal services',
         'Other Than Personal Services': 'Agency-wide other than personal services', 'Child Welfare': 'Child welfare', 'Juvenile Justice': 'Juvenile justice',
         'Adoption Subsidy': 'Adoption subsidy', 'Building Management': 'Building management', 'Fire Investigation': 'Fire investigation', 'Executive Management': 'Executive management'}
def base(n):
    n = re.sub(r'\s*-\s*(P\.?S\.?|O\.?T\.?P\.?S\.?)\s*$', '', n, flags=re.I); n = re.sub(r'\s*\((PS|OTPS)\)\s*$', '', n, flags=re.I)
    n = re.sub(r'\s+(Ps|Otps|P\.S\.|O\.T\.P\.S\.)$', '', n).strip(' -').strip(); return ALIAS.get(n, n)
def merge(rows):                                                              # personal-services and OTPS units with truncated names
    res = {}
    for k in sorted(rows, key=len):
        a = re.sub(r'[^a-z]', '', k.lower()); hit = next((o for o in res if len(a) >= 8 and (a.startswith(re.sub(r'[^a-z]', '', o.lower())) or re.sub(r'[^a-z]', '', o.lower()).startswith(a))), None)
        if hit: res[hit] += rows[k]
        else: res[k] = rows[k]
    return res
DOE = {'General education instruction and school leadership': ['401', '402'], 'Special education': ['403', '404', '421', '422', '423', '424', '470', '476'],
       'Charter school payments': ['406'], 'Pre-K and early childhood': ['407', '408', '409', '410'], 'Fringe benefits for school staff': ['461'],
       'Pupil transportation': ['437', '438'], 'Buildings, energy and leases': ['435', '436', '444'], 'Contract schools and foster care payments': ['472'],
       'Categorical programs': ['481', '482'], 'Food, safety, technology, support and central offices': ['415', '416', '433', '434', '439', '440', '441', '442', '453', '454', '474', '473', '475']}
inside = {}
for c, a in ua.items():
    rows = {}
    if c == '040':
        have = set()
        for lab, codes in DOE.items():
            amt = sum(x['amount'] or 0 for x in a['uas'] if x['code'] in codes); have |= set(codes)
            if amt: rows[lab] = amt
        assert not [x for x in a['uas'] if x['code'] not in have], 'unbinned DOE units'
    else:
        for x in a['uas']: rows[base(x['name'])] = rows.get(base(x['name']), 0) + (x['amount'] or 0)
        rows = merge(rows)
    r = sorted(rows.items(), key=lambda kv: -kv[1]); top = r[:6]; rest = sum(v for _, v in r[6:])
    m = {}
    for k, v in [[k, v] for k, v in top] + ([['Everything else in the agency', rest]] if rest > 0 else []):
        k = ALIAS.get(k, k); m[k] = m.get(k, 0) + v
    pg = sorted(set(x['page'] for x in a['uas']))
    inside[c] = {'name': a['name'], 'total': sum(rows.values()), 'pages': [pg[0], pg[-1]], 'rows': [list(kv) for kv in sorted(m.items(), key=lambda kv: (kv[0].startswith('Everything else'), -kv[1]))]}
dump('nyc-where-it-goes/data/inside.json', {'source': 'OMB, Adopted Budget Fiscal Year 2027, Supporting Schedules, Unit of Appropriation Summary (appropriation, adopted column, gross of intra-city sales)', 'url': SS_URL, 'fiscal_year': 2027, 'agencies': inside}, indent=0)

# ---------------------------------------------------------------- part three: real dollars per resident
rp = {'source': 'Spending buckets from spending_per_100.json. Population: Census Bureau county estimates, five boroughs. Prices: BLS CPI-U, New York-Newark-Jersey City (CUURS12ASA0), fiscal-year average, rebased to fiscal 2025 dollars.', 'years': {}}
for y in D['years']:
    fy = str(y['fy']); s = sp['years'][fy]
    rp['years'][fy] = {'population': y['population'], 'cpi': y['cpi'], 'deflator': y['deflator'], 'total': s['total'], 'groups': s['groups'],
                       'real_per_resident': {k: round(v * 1000 * y['deflator'] / y['population'], 2) for k, v in s['groups'].items()},
                       'real_total_per_resident': round(s['total'] * 1000 * y['deflator'] / y['population'], 2)}
for b in D['budget_years']:
    fy = str(b['fy']); s = sp['years'][fy]
    rp['years'][fy] = {'population': b['population'], 'population_note': b['population_note'], 'cpi': None, 'deflator': 1.0, 'deflator_note': 'budget years in nominal dollars, not deflated',
                       'total': s['total'], 'groups': s['groups'], 'real_per_resident': {k: round(v * 1000 / b['population'], 2) for k, v in s['groups'].items()},
                       'real_total_per_resident': round(s['total'] * 1000 / b['population'], 2), 'budgeted': True}
dump('nyc-budget-since-2000/data/real_per_resident.json', rp)

# ---------------------------------------------------------------- part four: capital spending by function
cap = {'source': 'NYC Comptroller ACFR, Capital Projects Fund expenditures by function, fiscal 2000-2025; bonds issued from the governmental funds statement.', 'labels': D['labels']['capital'], 'years': {}}
for y in D['years']:
    assert abs(sum(y['capital'].values()) - y['capital_total']) < 2
    cap['years'][str(y['fy'])] = {'total': y['capital_total'], 'groups': y['capital'], 'per_100': {k: round(v / y['capital_total'] * 100, 2) for k, v in y['capital'].items()},
                                  'borrowing': y.get('borrowing'), 'debt_service': y['debt_service'], 'operating_total': y['operating_total'] + y['debt_service'],
                                  'population': y['population'], 'deflator': y['deflator']}
dump('nyc-what-the-city-builds/data/capital_per_100.json', cap)

# ---------------------------------------------------------------- summary of the numbers the pages lead with
r25 = rev['years']['2025']['per_100']; s25 = sp['years']['2025']['per_100']; s27 = sp['years']['2027']['per_100']
print('revenue 2025 per $100:', {k: round(v, 2) for k, v in r25.items()}, 'total $bn', round(rev['years']['2025']['total'] / 1e6, 1))
print('spending 2025 per $100:', {k: round(v, 2) for k, v in s25.items()}, 'total $bn', round(sp['years']['2025']['total'] / 1e6, 1))
print('spending 2027 per $100:', {k: round(v, 2) for k, v in s27.items()})
print('funding 2027 $bn:', {k: round(v / 1e9, 1) for k, v in tot.items()})
print('per resident, real: 2000', rp['years']['2000']['real_total_per_resident'], '2025', rp['years']['2025']['real_total_per_resident'])
print('capital 2025 $bn', round(cap['years']['2025']['total'] / 1e6, 1), 'units parsed', sum(len(a['uas']) for a in ua.values()), 'agencies', len(ua))
