"""Tests for the settlement screens (`packages.py`, `screen.py`). Run after the common rebuild (build/ must exist):
    python3 models/tools/financing-protection/test_packages.py
They check that the screens reproduce the booked gap and D3, that each option is the size its source states, that
the recommended package closes FY2040 and every later year, and that no screen changes an adopted input."""
import copy
import csv
import unittest

import packages as K
import screen as S

CTX = K.Context()


class Booked(unittest.TestCase):
    def test_booked_reproduces_the_committed_gap(self):
        f = K.price(CTX, [])
        rows = [r for r in csv.DictReader(open(K.ROOT / 'models/data/recovery-budget-paths.csv')) if r['case'] == 'mixed']
        gap = {int(r['year']): float(r['agenda_gf_primary_bn']) for r in rows}
        for y in K.SHOW:
            self.assertAlmostEqual(f['gap'][y], gap[y], delta=0.06)
        self.assertAlmostEqual(f['gap_2030_39'], sum(gap[y] for y in range(2030, 2040)), delta=0.1)

    def test_d3_reproduces_q_h7_as_committed(self):
        q = K.Household().run([], convention=False)['net']
        # The committed Q-H7 (models/tools/household/results.md section 5, #467)
        self.assertEqual((q['Q1'], q['Q2'], q['Q3'], q['Q4']), (14840, 13209, 12070, 6837))


class OptionSizes(unittest.TestCase):
    def gap_change(self, name, year=2040, **params):
        b = K.price(CTX, [])
        f = K.price(CTX, [K.OPTIONS[name](CTX, **params)])
        return f['gap'][year] - b['gap'][year]

    def test_gx_is_15_percent_of_hch(self):
        self.assertAlmostEqual(self.gap_change('gx_narrowed'), -0.15 * CTX.line('HCH')[2040], delta=0.1)

    def test_hca_rederived_reaches_70(self):
        self.assertAlmostEqual(self.gap_change('hca_rederived'), 70.0 - CTX.line('HCA')[2040], delta=0.1)

    def test_avoidance_allowance_at_20_percent_is_the_booking(self):
        self.assertAlmostEqual(self.gap_change('avoidance_by_tier', base_allowance=0.20), 0.0, delta=0.05)

    def test_cap_costs_match_the_stack_menu(self):
        for d, (_, central, _, _) in K.CAP_MENU.items():
            self.assertAlmostEqual(self.gap_change('stack_cap', design=d), central, delta=0.1)

    def test_dropping_the_two_points_is_their_booked_yield(self):
        self.assertAlmostEqual(self.gap_change('drop_broad_points'), 216.3, delta=0.2)

    def test_credit_ended_is_the_credit(self):
        self.assertAlmostEqual(self.gap_change('end_adult_credit'), -K.m.credit(2040), delta=0.1)

    def test_ltc_at_100_doubles_the_states_payment(self):
        sp = CTX.component('HLT-9', 'states-payment')
        self.assertAlmostEqual(self.gap_change('ltc_state_share', share=1.0), sp[2040], delta=0.1)

    def test_hi_grant_is_intragovernmental(self):
        b = K.price(CTX, [])
        f = K.price(CTX, [K.OPTIONS['hi_grant_ended'](CTX)])
        self.assertAlmostEqual(f['gap'][2040] - b['gap'][2040], -CTX.rows[2040]['hi_gf_grant_bn'], delta=0.1)
        self.assertAlmostEqual(f['unified_primary_2030_39'], b['unified_primary_2030_39'], delta=0.01)
        self.assertEqual(f['debt_gdp'], b['debt_gdp'])

    def test_education_rates(self):
        self.assertEqual(K.price(CTX, [])['education_depletion'], 2035)
        self.assertIsNone(K.price(CTX, [K.OPTIONS['education_rate'](CTX, rate=1.7)])['education_depletion'])

    def test_vat_point_is_the_menu_yield(self):
        self.assertAlmostEqual(self.gap_change('vat', rate=1.0), -K.VAT_POINT_2040, delta=0.1)

    def test_without_d2_is_the_component(self):
        self.assertAlmostEqual(self.gap_change('without_d2'), -CTX.component('HLT-7', 'national-budget')[2040], delta=0.1)


class Packages(unittest.TestCase):
    def test_recommended_closes_2040_and_every_later_year(self):
        f = K.price(CTX, K.resolve(CTX, K.PACKAGES['recommended']))
        self.assertTrue(f['closes_2040_on'], f['gap'])

    def test_each_option_is_counted_once(self):
        for name, spec in K.PACKAGES.items():
            K.price(CTX, K.resolve(CTX, spec), name)   # raises on a label or argument counted twice

    def test_inputs_untouched(self):
        before = (copy.deepcopy(K.m.ADOPTION), copy.deepcopy(K.m.A), K.m.edu_fund)
        for spec in K.PACKAGES.values():
            K.price(CTX, K.resolve(CTX, spec))
        S.build()
        self.assertEqual((K.m.ADOPTION, K.m.A, K.m.edu_fund), before)

    def test_take_home_follows_the_two_points(self):
        self.assertEqual(K.take_home(K.PACKAGES['booked'])[0], 70.1)
        self.assertEqual(K.take_home(K.PACKAGES['recommended'])[0], 88.7)


if __name__ == '__main__':
    unittest.main()
