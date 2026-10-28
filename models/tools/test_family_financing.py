"""Bounded financing arithmetic, replacement and uncertainty boundaries."""
import importlib.util
from pathlib import Path
import unittest

HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('family_finance',HERE/'family-financing.py')
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)

class FinancingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=m.analyze()

    def test_revenue_reduces_a_deficit_not_increases_it(self):
        years={str(y):dict(gf_primary=50) for y in range(2040,2057)}
        r=m.assessed_gap(years,{y:60 for y in range(2040,2057)})
        self.assertEqual(r['fy2040_primary_gap_bn'],-10)
        self.assertTrue(r['maturity_screen_pass'])
        years['2050']['gf_primary']=70
        self.assertFalse(m.assessed_gap(years,{y:60 for y in range(2040,2057)})['maturity_screen_pass'])

    def test_replacement_is_increment_not_double_counted_total(self):
        c=self.result['cases'][2]
        self.assertAlmostEqual(c['revenue_2030_39_tn'],.59)
        self.assertAlmostEqual(sum(c['revenue_path_bn'][str(y)] for y in range(2030,2040)),590)

    def test_each_path_calibrates_to_its_stated_receipts(self):
        for c in self.result['cases']:
            self.assertAlmostEqual(sum(c['revenue_path_bn'][str(y)] for y in range(2030,2040)),1000*c['revenue_2030_39_tn'])
            self.assertAlmostEqual(c['fy2040_primary_gap_bn'],self.result['base_fy2040_gap_bn']-c['fy2040_receipts_bn'])

    def test_further_receipt_losses_do_not_improve_fiscal_result(self):
        for name in {r['name'] for r in self.result['stress']}:
            rows=[r for r in self.result['stress'] if r['name']==name]
            gaps=[r['worst_maturity_gap_bn'] for r in rows]
            self.assertEqual(gaps,sorted(gaps))

    def test_corporate_gross_and_payroll_scale_remain_explicit(self):
        self.assertAlmostEqual(self.result['cases'][0]['revenue_2030_39_tn'],self.result['corporate_gross_linear_tn']*.8)
        self.assertAlmostEqual(self.result['cases'][1]['revenue_2030_39_tn'],.35*self.result['payroll_point_option_tn'])
        self.assertTrue(self.result['unpriced_high_income_guardrails'])

if __name__=='__main__':unittest.main()
