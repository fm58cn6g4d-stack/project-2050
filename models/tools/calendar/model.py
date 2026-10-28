"""Scenario calendar. Dates/hours are uncalibrated experiments, not forecasts.
Independent chamber capacity; no automatic scope trims or probability averaging.
"""
import calendar,copy,csv,json
from datetime import date,timedelta
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
K=('favorable','central','difficult')
def D(s):return date.fromisoformat(s)
def days(a,b):
 while a<=b:yield a;a+=timedelta(days=1)
def window(s):
 """Preserve seasonal/month targets as windows; never silently choose day 28."""
 y=int(s[:4])
 if s.endswith('spring'):return f'{y}-03-01',f'{y}-05-31'
 if s.endswith('summer'):return f'{y}-06-01',f'{y}-08-31'
 m=int(s[5:7]);return f'{y}-{m:02}-01',f'{y}-{m:02}-{calendar.monthrange(y,m)[1]}'
def load(root=ROOT):
 c=json.loads((root/'models/data/inputs/calendar-scenarios.json').read_text())
 with (root/'models/data/inputs/ledger-bills.csv').open() as f:rows=list(csv.DictReader(f))
 fast={'INT-1','CAP-8','LAB-9D'};items=[]
 for r in rows:
  if r['rail']!='FLOOR' or float(r['floor_days'])<=0 or r['id']=='D2-RULES':continue
  i=r['id'];a,b=window(r['target']);rd=c['readiness'].get(i)
  if rd is None:raise ValueError('Missing readiness scenario for '+i)
  items.append(dict(id=i,scope=[i],profile='fast' if i in fast else 'heavy' if float(r['floor_days'])>=8 else 'standard',ready=rd,target_window=[a,b],target_kind='floor_start' if i=='DEM-1' else 'planning_completion',source=r['source']))
 items.append(dict(id='D2',scope=[],profile='rules',ready=c['readiness']['D2'],target_window=['2029-01-03','2029-01-09'],target_kind='completion'))
 for i,y in [('R1',2029),('R2',2029),('R3',2030)]:
  items.append(dict(id=i+'-BR',scope=[],profile='resolution',ready=c['readiness'][i+'-BR'],target_window=[f'{y}-01-03',f'{y}-02-01'] if i=='R1' else [f'{y}-04-01',f'{y}-06-01'],target_kind='preparation_convention'))
  items.append(dict(id=i,scope=[i],profile=i,ready=c['readiness'][i],target_window=['2029-02-03','2029-02-16'] if i=='R1' else [f'{y}-06-01',f'{y}-08-31'],target_kind='completion'))
 c['items']=items
 for cap in c['capacity'].values():
  if cap['other_share']+cap['reserve_share']>1:raise ValueError('Capacity shares exceed 100%')
 if len({i['id'] for i in items})!=len(items):raise ValueError('Duplicate vehicle')
 return c,rows

def run(cfg,condition='central',capacity='working',strategy='deadline',merged=False,frontload=False,shock=False):
 c=copy.deepcopy(cfg);items=c['items'];cap=c['capacity'][capacity];k=condition
 if merged:
  old=[x for x in items if x['id'] in ('CLI-3','CLI-6')]
  assert len(old)==2
  items=[x for x in items if x not in old]+[dict(id='CLI-M',scope=['CLI-3','CLI-6'],profile='climate_merged',ready={s:max(x['ready'][s] for x in old) for s in K},target_window=min(x['target_window'] for x in old),target_kind='planning_completion')]
 by={x['id']:x for x in items};tasks={};state={};current={'S':None,'H':None};debt={'S':0.,'H':0.};usage=[]
 for x in items:
  i=x['id'];p=c['profiles'][x['profile']];state[i]=dict(scope=x['scope'],S_start=None,done=None)
  deps=['D2:done'] if x['scope'] and i not in ('R1','R2','R3') else []
  if i in ('R1','R2','R3'):deps=[i+'-BR:done']
  if i in ('R2-BR','R3-BR'):deps=[{'R2-BR':'R1','R3-BR':'R2'}[i]+':done']
  ready=D(x['ready'][k])
  if i=='SS-1':ready=max(ready,D('2030-03-01')) # spring-month convention, not a new adopted date
  if shock and i in ('R1','DEM-1'):ready+=timedelta(days=21)
  def add(stage,ch,h,dependencies,span=1,lag=0):
   if h<0:raise ValueError('Negative work')
   tasks[i+':'+stage]=dict(id=i+':'+stage,bill=i,ch=ch,h=h,left=h,deps=dependencies,ready=ready,span=span,lag=lag,start=None,done=None,sittings=0,used=0,last=None)
  add('S','S',p['debate'][k]+p['votes'][k],deps,p['min_sittings'][k])
  if i=='D2':add('done',None,0,[i+':S'])
  else:
   add('H','H',p['house'][k],[i+'-BR:done'] if i in ('R1','R2','R3') else [])
   add('return','S',p['return'][k],[i+':S',i+':H'],lag=p['lag_days'][k])
   add('concur','H',{'favorable':0,'central':2,'difficult':6}[k],[i+':return'])
   add('done',None,0,[i+':concur'])
 def enabled(t,day):
  if day<t['ready'] or any(tasks[d]['done'] is None for d in t['deps']):return False
  if t['deps'] and day<max(tasks[d]['done'] for d in t['deps'])+timedelta(days=t['lag']):return False
  if t['id']=='DEM-1:S' and tasks['R1:done']['done'] is None and day<D('2029-03-01'):return False
  if t['id'] in ('R1:done','R2:done','R3:done') and day<D('2029-01-20'):return False
  return True
 def settle(day):
  changed=True
  while changed:
   changed=False
   for t in tasks.values():
    if t['done'] is None and t['h']==0 and t['span']<=1 and enabled(t,day):
     t['start']=t['done']=day;changed=True
     if t['id'].endswith(':done'):state[t['bill']]['done']=day.isoformat()
 def priority(t,day):
  i=t['bill'];target=D(by[i]['target_window'][1]).toordinal()
  protect=0 if i=='D2' else 1 if i in ('R1','R1-BR') else 2 if i=='DEM-1' else 3 if i=='SS-1' else 4
  if strategy=='dependency' and i in ('CAP-8','EXE-1','INT-1'):second=D('2029-03-01').toordinal()
  elif strategy=='quick':second=t['h']*100
  elif strategy=='large':second=-t['h']
  else:second=target
  return protect,second,target,t['id']
 for day in days(D(c['horizon'][0]),D(c['horizon'][1])):
  settle(day)
  for ch in ('S','H'):
   opened=frontload and day<=D(c['frontload']['through'])
   blackout=any(D(a)<=day<=D(b) for a,b in c['blackouts'])
   gross=cap[ch+'_hours'] if day.weekday() in cap['weekdays'] and not blackout else 0
   if gross and opened:gross+=c['frontload'][ch+'_extra']
   factor=c['condition_capacity'][k]*(.7 if shock and D('2029-02-01')<=day<=D('2029-03-31') else 1)
   other=min(cap['other_share'],c['frontload']['opening_other_share']) if opened else cap['other_share']
   deferred=gross*(cap['other_share']-other)*factor;debt[ch]+=deferred
   net=gross*(1-other-cap['reserve_share'])*factor;rebooked=0
   if frontload and not opened:rebooked=min(net,debt[ch]);net-=rebooked;debt[ch]-=rebooked
   remaining=net;active=blocked=0
   while remaining>1e-8:
    settle(day);t=tasks.get(current[ch])
    if t is None or t['done'] is not None:
     eligible=[a for a in tasks.values() if a['ch']==ch and a['done'] is None and enabled(a,day)]
     if not eligible:break
     t=min(eligible,key=lambda a:priority(a,day));current[ch]=t['id']
    if t['start'] is None:t['start']=day
    if t['id'].endswith(':S') and state[t['bill']]['S_start'] is None:state[t['bill']]['S_start']=day.isoformat()
    if t['last']!=day:t['sittings']+=1;t['last']=day
    h=min(remaining,t['left']);t['left']-=h;t['used']+=h;active+=h;remaining-=h
    if t['left']<=1e-8 and t['sittings']>=t['span']:t['done']=day;current[ch]=None
    elif remaining>0:blocked+=remaining;remaining=0
   usage.append(dict(date=str(day),chamber=ch,gross=gross,net=net,active=active,span_blocked=blocked,unused=remaining,deferred_other=deferred,rebooked_other=rebooked))
  settle(day)
 def check(i,end,start=False):
  x=state[i]['S_start' if start else 'done'];return bool(x and x<=end)
 checks=dict(rules_first_week=check('D2','2029-01-09'),R1_preferred=check('R1','2029-02-16'),R1_latest=check('R1','2029-03-31'),DEM_start=check('DEM-1','2029-03-31',True),DEM_spring=check('DEM-1','2030-05-31'),DEM_outer=check('DEM-1','2030-06-30'),SS_spring=check('SS-1','2030-05-31'),R2_summer=check('R2','2029-08-31'),R3_summer=check('R3','2030-08-31'))
 scope={i:s['done'] for s in state.values() for i in s['scope']}
 totals={ch:{f:round(sum(u[f] for u in usage if u['chamber']==ch),3) for f in ('gross','net','active','span_blocked','unused','deferred_other','rebooked_other')} for ch in ('S','H')}
 for ch in totals:totals[ch]['agenda_sitting_dates']=sum(u['active']+u['span_blocked']>0 for u in usage if u['chamber']==ch)
 slips={}
 for i,s in state.items():
  if not s['scope']:continue
  kind=by[i]['target_kind'];value=s['S_start' if kind=='floor_start' else 'done']
  if value is None or value>by[i]['target_window'][1]:slips[i]=dict(kind=kind,window=by[i]['target_window'],observed=value)
 for t in tasks.values():
  if t['done']:assert all(tasks[d]['done']<=t['start'] for d in t['deps'])
 result=dict(condition=k,capacity=capacity,strategy=strategy,merged=merged,frontload=frontload,shock=shock,checks=checks,deadline_misses=[i for i,b in checks.items() if not b],scope_total=len(scope),scope_completed=sum(bool(d) for d in scope.values()),unfinished=[i for i,d in scope.items() if d is None],scope_completion=scope,vehicles=state,planning_target_slips=slips,demand_hours={ch:sum(t['h'] for t in tasks.values() if t['ch']==ch) for ch in ('S','H')},usage=totals,unrebooked_other_hours=debt,DEM_recovery_decision_required=bool(state['DEM-1']['S_start'] and (state['R1']['done'] is None or state['DEM-1']['S_start']<state['R1']['done'])),status='Illustrative conditional procedure completion; not enactment or benefit forecast')
 return result,usage

def dominates(a,b):
 if a['condition']!=b['condition'] or a['shock']!=b['shock']:return False
 values=[(a['checks'][i],b['checks'][i]) for i in a['checks']]
 values += [(-(D(a['scope_completion'][i]).toordinal() if a['scope_completion'][i] else 999999),-(D(b['scope_completion'][i]).toordinal() if b['scope_completion'][i] else 999999)) for i in a['scope_completion']]
 values += [(-a['usage'][ch]['gross'],-b['usage'][ch]['gross']) for ch in ('S','H')]
 return all(x>=y for x,y in values) and any(x>y for x,y in values)

def experiments(c):
 results=[]
 for k in K:
  for cap in c['capacity']:
   for strategy in ('deadline','dependency','quick','large'):
    for merged in (False,True):
     for frontload in (False,True):results.append(run(c,k,cap,strategy,merged,frontload)[0])
 for merged in (False,True):results.append(run(c,'difficult','working','deadline',merged,True,True)[0])
 for n,a in enumerate(results):a['run_id']=n
 for a in results:
  a['dominated_by']=[b['run_id'] for b in results if b is not a and dominates(b,a)];a['on_frontier']=not a['dominated_by']
 return results
