#!/usr/bin/env python3
"""Check new experiments against stored baselines and independent boundary identities."""
import json
import unittest

from redesign import run, ROOT


class RedesignChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = run()
        cls.climate = {c['name']: c for c in cls.r['climate']}

    def case(self, architecture, stress, scope='Existing agenda'):
        return next(c for c in self.r['fiscal'] if (c['architecture'], c['stress'], c['scope']) == (architecture, stress, scope))

    def test_selected_climate_reproduces_stored_output(self):
        old = json.loads((ROOT/'build/carbon.json').read_text())['emissions']['full']
        rows = {r['year']: r for r in self.climate['selected']['years']}
        for year, values in old.items():
            self.assertAlmostEqual(rows[int(year)]['energy'], values['energy'], delta=.51)
            self.assertAlmostEqual(rows[int(year)]['cleanShare'], values['clean_share'], delta=.00051)

    def test_selected_fiscal_requirement_matches_stored_gap(self):
        old = json.loads((ROOT/'build/fiscal-model.json').read_text())['results']['DEC']['tests']
        case = self.case('Retain existing taxes', 'Central')
        self.assertAlmostEqual(case['minimum_net_gdp_percent'], old['gf_worst_2040_56_pct'])

    def test_replacement_removes_existing_money(self):
        keep = self.case('Retain existing taxes', 'Central')
        replace = self.case('Replace C19b and C20', 'Central')
        removed = sum((replace['gf_path_bn'][y] + replace['new_receipts_path_bn'][y]) -
                      (keep['gf_path_bn'][y] + keep['new_receipts_path_bn'][y]) for y in range(2030,2040))
        self.assertAlmostEqual(removed, 1330)
        self.assertGreater(replace['minimum_net_gdp_percent'], keep['minimum_net_gdp_percent'])

    def test_deeper_window_loss_excludes_later_g11_haircut(self):
        joint = self.case('Retain existing taxes', 'Joint low cases')
        deeper = self.case('Retain existing taxes', 'Deeper sensitivity')
        loss = sum((deeper['gf_path_bn'][y] + deeper['new_receipts_path_bn'][y]) -
                   (joint['gf_path_bn'][y] + joint['new_receipts_path_bn'][y]) for y in range(2030,2040))
        self.assertAlmostEqual(loss, 540)

    def test_funding_ramp_and_maturity_margin(self):
        for c in self.r['fiscal']:
            self.assertEqual(c['new_receipts_path_bn'][2029], 0)
            self.assertTrue(c['maturity_pass'])
            self.assertAlmostEqual(c['target_net_gdp_percent']-c['minimum_net_gdp_percent'], .1)

    def test_grid_cost_only_change_has_no_emissions_effect(self):
        grid, expensive = self.climate['grid'], self.climate['grid_double_cost']
        self.assertEqual(grid['extra_avoided_energy_co2_2030_50_gt'], expensive['extra_avoided_energy_co2_2030_50_gt'])
        self.assertAlmostEqual(expensive['extra_model_spend_2030_50_bn_2025'] - grid['extra_model_spend_2030_50_bn_2025'], 120)

    def test_climate_bundle_is_not_sum_of_independent_effects(self):
        total = self.climate['grid']['extra_avoided_energy_co2_2030_50_gt'] + self.climate['nuclear']['extra_avoided_energy_co2_2030_50_gt']
        self.assertLess(self.climate['grid_and_nuclear']['extra_avoided_energy_co2_2030_50_gt'], total)
        self.assertLess(self.climate['grid_without_credits']['extra_avoided_energy_co2_2030_50_gt'], 0)


if __name__ == '__main__':
    unittest.main()
