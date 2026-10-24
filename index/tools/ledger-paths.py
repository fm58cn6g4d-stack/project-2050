import json, math
d=json.load(open('ledger.json')); s=d['summary']
bills=[b for b in d['bills'] if b['rail'] not in ('LATER','T2')]
recon=s['recon_days']; approps=sum(b['floor_days'] for b in bills if b['rail']=='APPROPS')
fl=[b for b in bills if b['rail']=='FLOOR']
contested=[b for b in fl if b['floor_days']>0 and b['id']!='D2-RULES']
carve={'DEM-1','DEM-5','DEM-6'}            # electoral and civil-rights package (with its riders), DC, PR
topfights=['DEM-1','DEM-5','LAB-1','RTS-1','HLT-3','SS-1']  # assumed minority priority fights under C
fast={'INT-1','CAP-8','LAB-9D'}  # bipartisan, on the fast track (C27; LAB-9D's authorization)
def total(fn):
    days=recon+approps+4  # D2 rules vote
    passed=0
    for b in contested:
        x=fn(b)
        if x is None: continue
        days+=x; passed+=1
    return days,passed
paths={
 'E (bound): majority cloture after normal debate': lambda b: b['floor_days'],
 'F (decided Oct 20): graduated cloture, ~4.5 session days minimum per contested bill': lambda b: b['floor_days'] if b['id'] in fast else max(b['floor_days'],4.5),
 'C (opening offer to holdouts): talking filibuster with a speech budget; minority picks 6 top fights at ~15 days each': lambda b: max(b['floor_days'],15) if b['id'] in topfights else b['floor_days'],
 'G (written fallback): carve-out only; other contested bills need 60 and are counted as not passing': lambda b: b['floor_days'] if b['id'] in carve else None,
}
rows=[]
for k,fn in paths.items():
    days,passed=total(fn)
    rows.append(dict(status='legacy_assumption_crosswalk', current_model='calendar-scenarios.json', path=k,days=math.ceil(days),bills=passed,of=len(contested),over_first=math.ceil(days)-s['floor_budget']))
json.dump(rows,open('paths.json','w'),indent=1)
for r in rows: print(r)
print([b['id'] for b in contested])
# Sensitivity (Oct 20, Talarico stress test): path C at the scenario's observed pace (~24 days per top fight),
# with the minority's "proud to block" bills (IMM-1, RTS-3) in place of HLT-3 and SS-1. Printed only; not in paths.json.
alt=['DEM-1','DEM-5','LAB-1','RTS-1','IMM-1','RTS-3']
for per in (15,20,25):
    a,_=total(lambda b: max(b['floor_days'],per) if b['id'] in topfights else b['floor_days'])
    c,_=total(lambda b: max(b['floor_days'],per) if b['id'] in alt else b['floor_days'])
    print(f"C sensitivity: {per} days per fight -> base list {math.ceil(a)}, re-ordered list {math.ceil(c)}")
