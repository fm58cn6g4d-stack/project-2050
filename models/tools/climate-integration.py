"""Consume decided Package A/O5 annual accounts, nominal $B; no aggregate double count.
The research export remains a delta against the pre-Package-A $150 baseline.
"""
import hashlib, json
from pathlib import Path
from inputs import path
CONFIG=json.loads(Path(path('climate-adoption.json')).read_text())
ROOT=Path(path('climate-adoption.json')).resolve().parents[3]
SOURCE=ROOT/CONFIG['source']
if hashlib.sha256(SOURCE.read_bytes()).hexdigest()!=CONFIG['source_sha256']:
    raise ValueError('Climate pricing export changed: explicitly reconcile climate-adoption.json before consumption')
DATA=json.loads(SOURCE.read_text()); CASE=CONFIG['case']
ITEMS={r['id']:r for r in DATA['budget']['items']}

def item(i,y,case=CASE):
    if y<2030:return 0.
    return ITEMS[i]['path_bn'][case][str(min(y,2050))]*1.022**max(0,y-2050)

def account(y,case=CASE):
    annual=DATA['budget']['payment']['O5']['cases'][case]['annual']
    if y<2030:return {k:0. for k in annual['2030']}
    # Explicit constant-real-flow extension, not a new emissions projection.
    return {k:v*1.022**max(0,y-2050) for k,v in annual[str(min(y,2050))].items()}

def delta_rows(y,case=CASE):
    a=account(y,case)
    rows={rid:item(i,y,case) for i,rid in CONFIG['item_rows'].items()}
    rows.update({rid:share*item('credits',y,case) for rid,share in CONFIG['credit_split'].items()})
    rows['CXP']=a['cx_cost_bn']
    rows['CLI-2O']=a['dividend_bn']-a['added_receipts_bn']
    return rows

def capital_tn(case=CASE):return sum(account(y,case)['d4b_net_cost_bn'] for y in range(2030,2040))/1000

def apply(rows,B,row_path,profiles):
    """Replace changed row paths once; retain the baseline profile before adding exact deltas."""
    for r in rows:
        rid=r['id']
        if rid not in delta_rows(2030):continue
        baseline=(row_path(B,CONFIG['legacy_gf_tn'][rid],profiles[rid],rid)
                  if rid in CONFIG['legacy_gf_tn'] else {y:0 for y in B})
        expected=sum(r['gf'][y] for y in range(2030,2040))
        for key in ('gf','uni'):
            r[key]={y:baseline[y]+delta_rows(y)[rid] for y in r[key]}
        if abs(sum(r['gf'][y] for y in range(2030,2040))-expected)>0.001:
            raise ValueError('Climate annual/ledger calibration mismatch: '+rid)
    return rows

def disclosure():
    return {'CLI-7C_contingent_liability_bn':CONFIG['contingent_liability_bn'],
            'contingent_scored':False,'climate_case':CASE,
            'climate_post2050_assumption':CONFIG['post2050']}
