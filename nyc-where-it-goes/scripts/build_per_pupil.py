#!/usr/bin/env python3
# Title: Build data/per_pupil.json, the per-pupil layer in the schools click-state of "Where it goes"
# Author: Josh Greenman / Vital City, with Claude
# Date: October 30, 2026
# Data sources (all public; raw files stay outside the repo, paths passed as arguments):
#   1. Census Bureau, 2024 Annual Survey of School System Finances, summary tables (Table 18 NYC row, Table 8 U.S. row)
#      https://www2.census.gov/programs-surveys/school-finances/tables/2024/secondary-education-finance/elsec24_sumtables.xlsx
#   2. Same survey, 2016 summary tables (Table 18 NYC row)
#      https://www2.census.gov/programs-surveys/school-finances/tables/2016/secondary-education-finance/elsec16_sumtables.xls
#   3. NYSED report card database 2024-25, table "Expenditures per Pupil" exported to CSV
#      https://data.nysed.gov/files/essa/24-25/SRC2025.zip
#   4. Census district-level files, fiscal 2024 and 2016, for payments to charter (V92) and private (V91) schools
#      https://www2.census.gov/programs-surveys/school-finances/tables/2024/secondary-education-finance/elsec24.xlsx
#      https://www2.census.gov/programs-surveys/school-finances/tables/2016/secondary-education-finance/elsec16.txt
#   5. BLS CPI-U, New York-Newark-Jersey City, all items (CUURS12ASA0), fetched from the BLS public API
# Description: Writes the NYC-vs-U.S. per-pupil comparison by object, the fiscal 2016-2024 trend and the
#   school-by-school spread, then checks that the hand-written schools facts in data/context_facts.json
#   quote these numbers exactly. Method and judgment calls: research/03-context-facts.md, "Oct. 30, 2026".
# Usage: python3 scripts/build_per_pupil.py elsec24_sumtables.xlsx elsec16_sumtables.xls Expenditures_per_Pupil_2025.csv elsec24.xlsx elsec16.txt
# Dependencies: Python 3.9+, pandas, openpyxl, xlrd
import json, os, statistics, sys, urllib.request
import pandas as pd

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s24, s16, src, u24, u16 = sys.argv[1:6]

def t18_nyc(path):
    t = pd.read_excel(path, sheet_name=[k for k in pd.ExcelFile(path).sheet_names if k.strip() == '18'][0], header=None)
    r = t[t[2].astype(str).str.strip() == 'New York City'].iloc[0]
    # columns: 4 enrollment, 5 total, 6 salaries and wages, 7 employee benefits
    return {'enrollment': int(r[4]), 'total': float(r[5]), 'salaries': float(r[6]), 'benefits': float(r[7])}

nyc, nyc16 = t18_nyc(s24), t18_nyc(s16)
t8 = pd.read_excel(s24, sheet_name='8', header=None)
u = t8[t8[0].astype(str).str.contains('United States')].iloc[0]
us = {'total': float(u[2]), 'salaries': float(u[3]), 'benefits': float(u[4])}
assert round(nyc['total']) == 35796 and round(us['total']) == 17619, 'Census figures differ from the press release'

def objects(x):
    s, b, t = round(x['salaries']), round(x['benefits']), round(x['total'])
    return [s, b, t - s - b, t]          # third row is the rounded total minus the first two, so rows add to the total
N, U = objects(nyc), objects(us)

# CPI: fiscal-year averages, July through June
req = urllib.request.Request('https://api.bls.gov/publicAPI/v2/timeseries/data/', method='POST',
    data=json.dumps({'seriesid': ['CUURS12ASA0'], 'startyear': '2015', 'endyear': '2024'}).encode(),
    headers={'Content-Type': 'application/json'})
j = json.load(urllib.request.urlopen(req))
assert j['status'] == 'REQUEST_SUCCEEDED', j
m = {(int(x['year']), int(x['period'][1:])): float(x['value']) for x in j['Results']['series'][0]['data'] if x['period'] != 'M13'}
fy = lambda y: sum([m[(y - 1, k)] for k in range(7, 13)] + [m[(y, k)] for k in range(1, 7)]) / 12
c16, c24 = fy(2016), fy(2024)
p16, p24 = nyc16['total'], nyc['total']
real16 = p16 * c24 / c16
tot16, tot24 = p16 * nyc16['enrollment'], p24 * nyc['enrollment']
# Charter-school payments sit outside Table 18 (thousands of dollars, NYC = NCESID 3620580)
def unit(path):
    t = pd.read_excel(path, dtype={'NCESID': str}) if path.endswith('xlsx') else pd.read_csv(path, dtype={'NCESID': str}, index_col=False, low_memory=False)  # header ends in a comma
    r = t[t.NCESID == '3620580'].iloc[0]
    assert int(r.V33) in (nyc['enrollment'], nyc16['enrollment'])
    assert abs((r.TCURELSC - r.V91 - r.V92) * 1000 / r.V33 - (p24 if int(r.V33) == nyc['enrollment'] else p16)) < 0.01, 'unit file does not reproduce Table 18'
    return float(r.V92) * 1000
ch24, ch16 = unit(u24), unit(u16)
# Share of the real per-pupil rise explained by fewer students, both orderings (FY2024 dollars)
rise = p24 - real16
fewer_a = (tot24 / nyc16['enrollment'] - real16) / rise   # fiscal 2024 money over fiscal 2016 enrollment
fewer_b = (p24 - tot16 * c24 / c16 / nyc['enrollment']) / rise
trend = {'per_pupil_2016': round(p16), 'per_pupil_2024': round(p24),
         'enrollment_2016': nyc16['enrollment'], 'enrollment_2024': nyc['enrollment'],
         'per_pupil_change_pct': round((p24 / p16 - 1) * 100, 1), 'enrollment_change_pct': round((nyc['enrollment'] / nyc16['enrollment'] - 1) * 100, 1),
         'per_pupil_real_change_pct': round((p24 / real16 - 1) * 100, 1), 'total_real_change_pct': round((tot24 / (tot16 * c24 / c16) - 1) * 100, 1),
         'share_of_real_rise_from_fewer_students': [round(1 - fewer_a, 3), round(1 - fewer_b, 3)],
         'charter_payments_2016': round(ch16), 'charter_payments_2024': round(ch24),
         'charter_payments_real_change_pct': round((ch24 / (ch16 * c24 / c16) - 1) * 100),
         'total_with_charter_payments_real_change_pct': round(((tot24 + ch24) / ((tot16 + ch16) * c24 / c16) - 1) * 100, 1),
         'cpi_fy2016': round(c16, 3), 'cpi_fy2024': round(c24, 3)}
assert min(trend['share_of_real_rise_from_fewer_students']) > 0.5   # the fact says "most of"

# School-by-school spread, 2024-25. Entity codes: CC DD SS TT NNNN (county, district, 01 = district school, 86 = charter).
d = pd.read_csv(src, dtype={'ENTITY_CD': str})
d = d[(d.YEAR == 2025) & d.PER_FED_STATE_LOCAL_EXP.notna()]
e = d.ENTITY_CD
school = e.str[-4:] != '0000'
geo = d[school & e.str[:2].isin(['31', '32', '33', '34', '35']) & (e.str[4:8] == '0001')]
charter = d[school & e.str[:2].isin(['31', '32', '33', '34', '35']) & (e.str[4:8] == '0086')]
d75 = d[school & e.str.startswith('3075')]
v = sorted(geo.PER_FED_STATE_LOCAL_EXP)
q = statistics.quantiles(v, n=4, method='inclusive')
low3 = geo.nsmallest(3, 'PER_FED_STATE_LOCAL_EXP')
spread = {'school_year': '2024-25', 'district_schools': len(v), 'median': statistics.median(v), 'q1': q[0], 'q3': q[2],
          'lowest': [[n, int(x)] for n, x in zip(low3.ENTITY_NAME, low3.PER_FED_STATE_LOCAL_EXP)],
          'charter_schools_left_out': len(charter), 'd75_schools': len(d75), 'd75_median': statistics.median(d75.PER_FED_STATE_LOCAL_EXP)}

out = {'source_census': 'https://www2.census.gov/programs-surveys/school-finances/tables/2024/secondary-education-finance/elsec24_sumtables.xlsx',
       'source_nysed': 'https://data.nysed.gov/files/essa/24-25/SRC2025.zip',
       'fiscal_year': 2024,
       'rows': [['Salaries and wages', N[0], U[0]], ['Employee benefits', N[1], U[1]],
                ['Services, supplies and everything else', N[2], U[2]]],
       'total': [N[3], U[3]], 'ratio': [round(N[i] / U[i], 1) for i in range(4)],
       'trend': trend, 'spread': spread}
json.dump(out, open(os.path.join(HERE, 'data', 'per_pupil.json'), 'w'), indent=1)

# The facts list is hand-written; make sure it quotes the numbers above.
f = ' '.join(x['fact'] for x in json.load(open(os.path.join(HERE, 'data', 'context_facts.json')))['education'])
fmt = lambda x: f'{x:,.0f}'
need = [fmt(p16), fmt(p24), f"{trend['per_pupil_change_pct']} percent", f"{abs(trend['enrollment_change_pct'])} percent",
        f"{trend['per_pupil_real_change_pct']} percent", f"{trend['total_real_change_pct']} percent", f"{trend['charter_payments_real_change_pct']} percent",
        f"{trend['total_with_charter_payments_real_change_pct']} percent",
        fmt(nyc16['enrollment']), fmt(nyc['enrollment']), fmt(len(v)), fmt(spread['median']), fmt(len(d75)), fmt(spread['d75_median']),
        fmt(round(q[0], -2)), fmt(round(q[2], -2))]
missing = [n for n in need if n not in f]
print(json.dumps(out, indent=1))
sys.exit(f'context_facts.json is missing {missing}') if missing else print('PASS  schools facts quote the computed figures')
