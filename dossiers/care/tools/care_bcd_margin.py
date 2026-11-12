#!/usr/bin/env python3
"""The plan-wide margin with care parts B-D, for `dossiers/care/6bcd-cost.md`, part 5.

Runs the budget model's recovery-budget case `mixed` in memory (nothing is written, no model file changes),
with parts B-D's fiscal-year lines from `care_bcd_path.py` added: long-term care and its workforce on the
general fund, net of HLT-4's booked long-term care component; child care, pre-K and early educators' pay
either inside the EDU-9B fund's care component (whose general-fund grant is 30% of the fund's outlays after
2034) or on the general fund with the fund's care component removed. Not a booking. Needs the build outputs:

    bash models/tools/run-all.sh        # once, to make build/
    python3 dossiers/care/tools/care_bcd_margin.py
"""
import importlib.util, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def load(name,p):
    s=importlib.util.spec_from_file_location(name,p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
P=load('cbp',ROOT/'dossiers/care/tools/care_bcd_path.py')
M=load('rb',ROOT/'models/tools/recovery-budget/model.py')
lines,extra,_=P.fy_lines(1)
yrs=list(P.FY)
part=lambda p:{y:sum(s.get(y,0) for k,s in lines.items() if k[0]==p) for y in yrs}
B,C,D=part('B'),part('C'),part('D'); par=lines['D parity (memo 15)']
ltc={y:(P.HLT4_BOOKED[i]-P.HLT4_YEAR_SHAPED[i])*P.LTC_SHARE for i,y in enumerate(yrs)}
edu=dict(zip(yrs,P.EDU_CARE))
ltc_net={str(y):B[y]+D[y]-par.get(y,0)-ltc[y] for y in yrs}
cpar={y:C[y]+par.get(y,0) for y in yrs}
f,b,m,u=M.load()
def gf(case): r={x['year']:x for x in case['rows']}; return r[2040]['agenda_gf_primary_bn'], r[2040]['education_gf_grant_bn'], r
base=M.build_case('mixed',f,b,m,u)
orig=M.education_components
def patched(mode):
    def ec(*a,**k):
        rows=orig(*a,**k)
        for r in rows:
            if r['component']=='care' and r['year'] in cpar:
                d = (cpar[r['year']]-edu[r['year']]) if mode=='fund' else -r['full_fund_outlays_bn']+r['current_law_transfer_bn']
                for kk in ('full_fund_outlays_bn','increment_over_current_law_bn','change_over_old_agenda_bn'): r[kk]+=d
        return rows
    return ec
out={}
g0,gr0,_=gf(base); out['as booked']=(g0,gr0)
c1=M.build_case('mixed',f,b,m,u,spending_adjustments={'ltc':{'annual_bn':ltc_net}}); out['LTC only']=gf(c1)[:2]
M.education_components=patched('fund')
c2=M.build_case('mixed',f,b,m,u,spending_adjustments={'ltc':{'annual_bn':ltc_net}}); out['C in fund']=gf(c2)[:2]
M.education_components=patched('gf')
adj={'ltc':{'annual_bn':ltc_net},'c':{'annual_bn':{str(y):cpar[y] for y in yrs}}}
c3=M.build_case('mixed',f,b,m,u,spending_adjustments=adj); out['C on GF']=gf(c3)[:2]
M.education_components=orig
for k,(g,gr) in out.items(): print(f"{k:12} FY2040 general-fund primary balance {g:8.1f}B short; education fund grant {gr:6.1f}B; {100*g/b[2040]["gdp"]:.2f}% of GDP")
