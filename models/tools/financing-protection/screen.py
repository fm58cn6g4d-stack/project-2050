"""Exploratory financing screen using the recovery model; no selected inputs written.
Quintile diagnostics include service values and inherited allocation keys, not D3.
Run the common build first. Outputs JSON to stdout.
"""
import importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('recovery',ROOT/'index/tools/recovery-budget/model.py')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
f,b,old,u=m.load()
components=m.education_components(old)
results=[]
for credit,high,broad in [(1,0,0),(1,4,0),(1,4,2),(5,10,2),(5,10,0),(8,10,2),(5,14,2),(8,14,0)]:
    case=m.build_case('screen',f,b,old,u,credit_multiple=credit,high_rate=high,broad_rate=broad,corridor=True)
    # Diagnostic expects three named cases; supply identical case to each.
    d={'cases':{k:case for k in ('mixed','larger_payroll','mixed_larger_credit')},'education_components':components}
    h=m.household_diagnostic(d,f,b,old,u)['per_household_annual_dollars']['mixed']
    results.append({'credit_2030_dollars_per_adult':300*credit,'high_income_points':high,'broad_income_points':broad,'summary':case['summary'],'households':{y:h[y] for y in (2030,2035,2039)}})
print(json.dumps({'status':'exploratory screen, not adopted; same 2-point SS closer and 1.4-point education illustration retained; no within-quintile or cash-only protection claim','source_commit':'aa8552d plus capacity-integration working changes','cases':results},indent=2))
