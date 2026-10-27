#!/usr/bin/env python3
import hashlib, unittest
from pathlib import Path
import model

class RecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (model.ROOT/'index/data/inputs').glob('*.csv')}
        cls.r=model.run(); cls.rows={r['year']:r for r in cls.r['education_bridge']}
    def test_comparison_guard_accepts_only_recorded_rebases(self):
        h=lambda b:hashlib.sha256(b).hexdigest()
        path='index/data/inputs/x.csv'
        prov,rebased={path:h(b'old')},{path:h(b'new')}
        for ok in (b'old',b'new'):
            model.check_comparison_inputs(prov,rebased,lambda p,ok=ok:ok)
        with self.assertRaises(ValueError):
            model.check_comparison_inputs(prov,rebased,lambda p:b'unlisted change')
        with self.assertRaises(ValueError):
            model.check_comparison_inputs(prov,{},lambda p:b'new')
    def test_full_scope_reconciles_without_duplicate_old_benefits(self):
        t=self.r['totals_2030_39_tn']
        self.assertAlmostEqual(t['old_agenda_transfer_bn'],1.23,places=5)
        self.assertAlmostEqual(t['current_law_absorbed_bn'],.77)
        self.assertAlmostEqual(t['new_benefits_bn'],t['fund_outlays_bn']-2,places=5)
        self.assertGreater(t['new_benefits_bn'],.59)
        self.assertLess(t['new_benefits_bn'],.62)
    def test_transfers_cancel_in_consolidated_government(self):
        for r in self.rows.values():
            self.assertAlmostEqual(r['unified_delta_bn']-r['gf_delta_bn'],r['fund_primary_deficit_bn'])
            self.assertAlmostEqual(r['fund_outlays_bn'],r['new_benefits_bn']+r['old_agenda_transfer_bn']+r['current_law_absorbed_bn'])
    def test_transition_not_a_free_payfor(self):
        self.assertAlmostEqual(self.rows[2030]['payroll_bn'],0)
        self.assertAlmostEqual(self.rows[2030]['gf_bridge_bn'],142)
        self.assertGreater(self.rows[2030]['unified_delta_bn'],28)
        self.assertEqual(self.r['education_cases']['phased_2.0_no_bridge']['first_negative_reserve'],2030)
    def test_no_double_counted_estates_and_no_existing_tax_removal(self):
        self.assertEqual(model.E['estate_receipts'],0)
        m=self.r['fiscal_scenarios'][0]; d=self.r['fiscal_scenarios'][1]
        self.assertAlmostEqual(d['gf_2030_39_primary_tn']-m['gf_2030_39_primary_tn'],self.r['delayed_middle_receipts_2030_39_tn'])
        self.assertGreater(self.r['delayed_middle_receipts_2030_39_tn'],.39)
    def test_old_rate_fails_but_central_funded_cases_do_not(self):
        c=self.r['education_cases']
        self.assertEqual(c['source_1.4_immediate_no_estate']['first_negative_reserve'],2034)
        self.assertIsNone(c['mixed_1.4_GF30']['first_negative_reserve'])
        self.assertFalse(c['mixed_1.4_GF30_low_payroll_high_cost']['nondeclining_terminal_ratio'])
    def test_care_state_cost_is_not_free(self):
        rows={r['year']:r for r in self.r['education_cases']['mixed_1.4_GF30_care_floor80']['rows']}
        self.assertAlmostEqual(rows[2049]['extra_care_bn'],143*(.8/.6-1))
        self.assertAlmostEqual(rows[2030]['extra_care_bn'],0)
    def test_no_quintile_pass_invented(self):
        self.assertLess(self.r['incidence_diagnostic'][2039]['Q4']['new_net_before_unallocated_protection'],0)
    def test_ss_later_start_and_leave_high_take_up_matter(self):
        ss=self.r['funds']['ss']
        self.assertFalse(ss['plus_1_point']['sustainable'])
        self.assertTrue(ss['rounded_case']['sustainable'])
        self.assertFalse(ss['later_2040_case']['sustainable'])
        self.assertGreater(self.r['funds']['leave']['0.85']['loan_2050'],800)
        self.assertEqual(self.r['funds']['leave']['1.1']['loan_2050'],0)
    def test_whole_government_requirement_exceeds_agenda_gap(self):
        for c in self.r['fiscal_scenarios']:
            self.assertGreater(c['stabilizing_net_gdp_percent'],c['net_new_gdp_requirement_with_margin'])
            p=c['stabilized_debt_gdp']
            self.assertTrue(all(p[y]<=p[y-1]+2e-9 for y in range(2045,2057)))
    def test_comparison_inputs_unchanged(self):
        for p,h in self.before.items():self.assertEqual(hashlib.sha256(Path(p).read_bytes()).hexdigest(),h)

if __name__=='__main__':unittest.main()
