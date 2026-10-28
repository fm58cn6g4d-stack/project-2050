"""Accounting regressions for the adopted climate consumer, not a new climate score."""
import csv, importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
s=importlib.util.spec_from_file_location('climate',ROOT/'index/tools/climate-integration.py')
C=importlib.util.module_from_spec(s);s.loader.exec_module(C)
class IntegrationTests(unittest.TestCase):
 def test_components_equal_export_without_double_count(self):
  for case in C.DATA['budget']['cases']:
   for y in range(2030,2057):
    a=C.account(y,case)
    self.assertAlmostEqual(sum(C.delta_rows(y,case).values()),a['general_fund_net_cost_bn']+a['d4b_net_cost_bn'],places=8)
    self.assertAlmostEqual(a['added_receipts_bn'],a['process_receipts_bn']+a['combustion_receipts_change_bn'],places=9)
    self.assertAlmostEqual(a['cx_cost_bn'],.25*a['added_receipts_bn'],places=9)
    self.assertAlmostEqual(a['dividend_bn'],.8*a['added_receipts_bn']-a['process_dividend_diversion_bn'],places=9)
    self.assertLessEqual(a['process_dividend_diversion_bn'],.8*a['process_receipts_bn']+1e-8)
 def test_maturity_all_four_cases(self):
  for case in C.DATA['budget']['cases']:
   for y in (2040,2050):self.assertLessEqual(C.account(y,case)['general_fund_net_cost_bn'],1e-8)
 def test_credit_allocation_and_end_dates(self):
  self.assertAlmostEqual(sum(C.CONFIG['credit_split'].values()),1)
  for y in range(2026,2057):
   self.assertAlmostEqual(sum(C.delta_rows(y)[k] for k in ('CLI-1','CLI-5')),C.item('credits',y))
   if y>=2040:self.assertEqual(C.account(y)['d4b_net_cost_bn'],0)
   if y<2031:self.assertEqual(C.item('reinsurance',y),0)
   if y>=2050:self.assertEqual(C.item('credits',y),0)
 def test_ledger_matches_annual_paths(self):
  bills={r['id']:r for r in csv.DictReader((ROOT/'index/data/inputs/ledger-bills.csv').read_text().splitlines())}
  for item,rid in C.CONFIG['item_rows'].items():
   self.assertAlmostEqual(float(bills[rid]['cost_mid'])*1000,sum(C.item(item,y) for y in range(2030,2040)))
  self.assertAlmostEqual(float(bills['CLI-2O']['cost_mid'])*1000,sum(C.delta_rows(y)['CLI-2O'] for y in range(2030,2040)))
 def test_contingency_is_unscored(self):
  self.assertEqual(C.disclosure()['CLI-7C_contingent_liability_bn'],[75,150])
  self.assertFalse(C.disclosure()['contingent_scored'])
 def test_shared_model_consumes_once(self):
  m=json.loads((ROOT/'build/fiscal-model.json').read_text());r={v['id']:v for v in m['rows']}
  # Exact sum of separate new components; the only legacy changes are the two credit shares.
  for y in range(2030,2057):
   new=sum(r[k]['gf'][str(y)] for k in C.delta_rows(y) if k not in ('CLI-1','CLI-5'))
   expected=sum(v for k,v in C.delta_rows(y).items() if k not in ('CLI-1','CLI-5'))
   self.assertAlmostEqual(new,expected,delta=.006) # generated rows rounded to $1M
  for result in m['results'].values():
   if 'tests' in result:self.assertFalse(result['tests']['contingent_scored'])
if __name__=='__main__':unittest.main()
