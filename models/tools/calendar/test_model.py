"""Resource, scope and semantic regression checks for the integrated calendar."""
import copy,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from model import load,run,window,dominates
from build import delivery
class CalendarModelTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.c,cls.rows=load();cls.r,cls.u=run(cls.c,frontload=True)
 def test_windows(self):
  self.assertEqual(window('2030-spring'),('2030-03-01','2030-05-31'))
  self.assertEqual(window('2029-summer'),('2029-06-01','2029-08-31'))
  self.assertEqual(window('2030-02'),('2030-02-01','2030-02-28'))
 def test_full_scope_and_merger(self):
  m,_=run(self.c,merged=True)
  self.assertEqual(set(self.r['scope_completion']),set(m['scope_completion']))
  self.assertEqual(len(m['scope_completion']),24);self.assertIn('CLI-7',m['scope_completion']);self.assertNotIn('MOV-31',m['scope_completion'])
 def test_capacity_conservation_and_repayment(self):
  for x in self.u:self.assertAlmostEqual(x['net'],x['active']+x['span_blocked']+x['unused'])
  for ch in ('S','H'):
   self.assertAlmostEqual(self.r['usage'][ch]['deferred_other'],self.r['usage'][ch]['rebooked_other'])
   self.assertAlmostEqual(self.r['unrebooked_other_hours'][ch],0)
 def test_dependencies_and_dem_target_semantics(self):
  d=self.r['vehicles']['D2']['done']
  for i,s in self.r['vehicles'].items():
   if i not in ('D2','R1','R2','R3','R1-BR','R2-BR','R3-BR') and s['S_start']:self.assertGreaterEqual(s['S_start'],d)
  self.assertGreaterEqual(self.r['vehicles']['R1']['done'],'2029-01-20')
  self.assertEqual(next(i for i in self.c['items'] if i['id']=='DEM-1')['target_kind'],'floor_start')
 def test_zero_capacity_and_span_blockage(self):
  z=copy.deepcopy(self.c)
  z['capacity']['working']['S_hours']=z['capacity']['working']['H_hours']=0
  r,_=run(z);self.assertEqual(r['scope_completed'],0)
  z=copy.deepcopy(self.c);z['profiles']['standard']['min_sittings']['favorable']=20
  r,_=run(z,'favorable');self.assertGreater(r['usage']['S']['span_blocked'],0)
 def test_statutory_debate_bounds_and_dominance(self):
  for k in self.c['conditions']:
   self.assertLessEqual(self.c['profiles']['resolution']['debate'][k],50)
   for i in ('R1','R2','R3'):self.assertLessEqual(self.c['profiles'][i]['debate'][k],20)
  self.assertFalse(dominates(self.r,self.r))
  worse=copy.deepcopy(self.r);worse['checks'][next(i for i,v in worse['checks'].items() if v)]=False
  self.assertTrue(dominates(self.r,worse));self.assertFalse(dominates(worse,self.r))
 def test_fixed_delivery_dates_cannot_be_accelerated(self):
  rows=[dict(id='HLT-3',rail='FLOOR',felt_months='0',source='canonical')]
  r=dict(run_id=0,scope_completion={'HLT-3':'2029-01-20'})
  e=delivery(rows,[r],[dict(policy='HLT-3',package='HLT-3',not_before='2031-01-01')],'2030-11-05')[0]
  self.assertEqual(e['candidate_dates']['0'],'2031-01-01')
  self.assertEqual(e['statuses']['0'],'governed_after_midterm')
if __name__=='__main__':unittest.main()
