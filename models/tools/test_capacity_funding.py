"""Regression checks for the availability/cash boundary."""
import importlib.util, unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location("capacity",Path(__file__).with_name("capacity-funding.py"))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class FundingChecks(unittest.TestCase):
 def setUp(self):
  self.f={"available_on_enactment":"yes","multi_year":"yes","target_vehicle":"R1","availability_fy":"2029","fy2029_outlay_bn":"","outlay_status":"unpriced","byrd_status":"pending"}
  self.b={"rail":"R1","cost_mid":0.6}
  self.y={f"y{y}":str(v) for y,v in zip(range(2030,2040),[70,120,130,120,100,60,0,0,0,0])}
 def test_unknown_is_not_zero(self):
  r=m.assess(self.f,self.b,self.y)
  self.assertIsNone(r["fy2029_outlay_bn"])
  self.assertEqual(r["available_bn"],600)
 def test_no_silent_pre_window_addition(self):
  for cash in ["0","20","600"]:
   with self.subTest(cash=cash):
    f=dict(self.f,fy2029_outlay_bn=cash)
    with self.assertRaises(ValueError):m.assess(f,self.b,self.y)
 def test_reject_inconsistent_lifetime_total(self):
  y=dict(self.y,y2030="90")
  with self.assertRaises(ValueError):m.assess(self.f,self.b,y)
 def test_reject_route_drift(self):
  with self.assertRaises(ValueError):m.assess(self.f,dict(self.b,rail="APPROPS"),self.y)
if __name__=="__main__":unittest.main()

