"""Historical pre-PR26 spending ceilings, not current package recommendations.
Run after common rebuild. Outputs JSON; compares identical financing across packages.
"""
import importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('recovery',ROOT/'models/tools/recovery-budget/model.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
f,b,old,u=m.load()
gdp={'ramp':4,'grow':'gdp','perm':1}
climate=f.PR.BILLS['CLI-1']
packages={
 'current':{},
 'focused_recovery':{
  'AI transition 120 to 80':{'delta_tn':-.04,'profile':f.PR.BILLS['AI-4']},
  'participation 100 to 70':{'delta_tn':-.03,'profile':gdp},
  'additional housing 135 to 100':{'delta_tn':-.035,'profile':gdp},
  'climate credits 900 to 700':{'delta_tn':-.2,'profile':climate}},
 'infrastructure_rebalance':{
  'climate credits 900 to 600':{'delta_tn':-.3,'profile':climate},
  'grid adaptation workforce replacement':{'delta_tn':.1,'profile':{'start':2032,'ramp':4,'grow':'cpi','perm':1}}}
}
results=[]
for financing,high,broad in [('existing_reforms',0,0),('upper_income_comparator',4,0)]:
 for name,adjustments in packages.items():
  for stress in (False,True):
   c=m.build_case(name,f,b,old,u,high_rate=high,broad_rate=broad,corridor=True,stress=stress,spending_adjustments=adjustments)
   results.append({'package':name,'financing':financing,'stress':stress,'summary':c['summary'],
     'spending_delta_2030_39_bn':sum(r['primary_outlay_change_bn'] for r in c['audit'] if r['line'].startswith('Exploratory:') and r['year'] in m.W),
     'spending_delta_2040_bn':sum(r['primary_outlay_change_bn'] for r in c['audit'] if r['line'].startswith('Exploratory:') and r['year']==2040)})
print(json.dumps({'status':'historical pre-PR26 exploratory ceilings, not adopted; no emissions/access/D3 certification; existing illustrative payroll and social-insurance parameters retained','packages':packages,'results':results},indent=2))
