#!/usr/bin/env python3
"""Boundary checks against independent stored results and hand-computable units."""
import json
from pathlib import Path
import unittest
from analyze import analyze, ROOT


class ReviewChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = analyze()

    def test_zero_case_matches_rebuilt_baseline(self):
        baseline=json.loads((ROOT/'build/fiscal-model.json').read_text())['results']['DEC']['years']
        for year, value in self.r['cases'][0]['gap_path_bn'].items():
            self.assertEqual(value,baseline[year]['gf_primary'])

    def test_corporate_reproduces_previous_independent_report(self):
        prior=json.loads((ROOT/'sources/family-financing-comparison.json').read_text())['cases'][0]
        new=self.r['cases'][2]
        self.assertAlmostEqual(new['fy2040_gap_bn'],prior['fy2040_primary_gap_bn'])
        self.assertAlmostEqual(new['revenue_2030_39_tn'],prior['revenue_2030_39_tn'])

    def test_joint_loss_calibration_and_monotonicity(self):
        cases=self.r['cases']
        self.assertAlmostEqual(cases[1]['added_cost_or_lost_receipts_2030_39_tn'],.7)
        for y in range(2030,2057):
            self.assertGreater(cases[1]['gap_path_bn'][str(y)],cases[0]['gap_path_bn'][str(y)])
            self.assertGreater(cases[3]['gap_path_bn'][str(y)],cases[2]['gap_path_bn'][str(y)])

    def test_housing_is_incremental_and_persistent(self):
        h=self.r['housing'][0]['path_bn']
        self.assertEqual(h[2033],0)
        self.assertAlmostEqual(h[2034],(2000000/6/2)*15200*1.03**8*1.05/1e9)
        self.assertAlmostEqual(h[2040],2000000*15200*1.03**14*1.05/1e9)
        self.assertAlmostEqual(h[2050]/h[2040],1.03**10)

    def test_housing_price_sensitivity(self):
        low,high=self.r['housing']
        self.assertAlmostEqual(high['cost_2030_39_tn']/low['cost_2030_39_tn'],1.25)
        self.assertGreater(high['case']['fy2040_gap_bn'],low['case']['fy2040_gap_bn'])

    def test_care_examples_are_not_nominal_fiscal_costs(self):
        self.assertEqual(self.r['care'][0]['gross_annual_bn_2026_dollars'],62.4)
        self.assertEqual(self.r['care'][1]['gross_annual_bn_2026_dollars'],182)
        self.assertEqual(self.r['cases'][-1]['added_cost_or_lost_receipts_2030_39_tn'],self.r['cases'][1]['added_cost_or_lost_receipts_2030_39_tn'])


if __name__=='__main__': unittest.main()
