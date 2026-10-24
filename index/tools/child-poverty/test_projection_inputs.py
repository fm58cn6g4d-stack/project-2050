"""Hand-calculated credit boundaries and demographic accounting invariants."""
import copy
import unittest
from current_law_ctc import calculate, parameters
from cps_projection import claimant_record, read_inputs, resource_total, sensitivity, HERE


def case(**changes):
    data = dict(eligibility_review='synthetic reviewed eligibility',
                credit_limit_review='synthetic Worksheet A result', special_case='none',
                filing_status='head', qualifying_children=1, other_dependents=0,
                modified_agi=30000, earned_income=30000, credit_limit=10000)
    data.update(changes)
    return data


class CurrentLawCreditTests(unittest.TestCase):
    def test_official_target_parameters(self):
        self.assertEqual(parameters(2030)['per_child'], 2400)
        self.assertEqual(parameters(2034)['max_refundable'], 2100)

    def test_source_year_maximum(self):
        self.assertEqual(calculate(case(), 2025)['combined_credit'], 2200)

    def test_target_year_maxima(self):
        self.assertEqual(calculate(case(), 2030)['combined_credit'], 2400)
        self.assertEqual(calculate(case(), 2034)['combined_credit'], 2600)

    def test_refund_earned_income_phasein(self):
        self.assertEqual(calculate(case(earned_income=10000, credit_limit=0), 2030)['refundable_actc'], 1125)

    def test_no_earnings_no_refund(self):
        self.assertEqual(calculate(case(earned_income=0, credit_limit=0), 2030)['combined_credit'], 0)

    def test_refundable_cap(self):
        self.assertEqual(calculate(case(credit_limit=0), 2034)['combined_credit'], 2100)

    def test_partial_tax_liability_and_refund(self):
        r = calculate(case(credit_limit=500), 2030)
        self.assertEqual((r['nonrefundable_ctc_and_odc'], r['refundable_actc']), (500, 1900))

    def test_phaseout_uses_next_thousand(self):
        self.assertEqual(calculate(case(modified_agi=200001), 2030)['combined_credit'], 2350)
        self.assertEqual(calculate(case(modified_agi=201001), 2030)['combined_credit'], 2300)

    def test_joint_threshold(self):
        self.assertEqual(calculate(case(filing_status='joint', modified_agi=400001), 2030)['combined_credit'], 2350)

    def test_odc_not_refundable_or_called_ctc(self):
        r = calculate(case(qualifying_children=0, other_dependents=2, credit_limit=800), 2030)
        self.assertEqual(r['combined_credit'], 800)
        self.assertEqual(r['refundable_actc'], 0)
        self.assertIsNone(r['ctc_only_allocation'])

    def test_combined_credit_full_phaseout(self):
        self.assertEqual(calculate(case(modified_agi=300000), 2030)['combined_credit'], 0)

    def test_three_child_payroll_route_requires_inputs(self):
        with self.assertRaises(ValueError):
            calculate(case(qualifying_children=3, credit_limit=0, earned_income=10000), 2030)

    def test_three_child_payroll_route(self):
        r = calculate(case(qualifying_children=3, credit_limit=0, earned_income=10000,
                           payroll_alternative=2000, payroll_alternative_review='synthetic line23-line24'), 2030)
        self.assertEqual(r['refundable_actc'], 2000)

    def test_special_case_rejected(self):
        with self.assertRaises(ValueError):
            calculate(case(special_case='Form2555'), 2030)

    def test_missing_reviews_and_fractional_children_rejected(self):
        for changes in ({'eligibility_review': ''}, {'credit_limit_review': ''}, {'qualifying_children': 1.5}):
            with self.assertRaises(ValueError):
                calculate(case(**changes), 2030)

    def test_unsupported_year_rejected(self):
        with self.assertRaises(ValueError):
            calculate(case(), 2032)


class ProjectionInputTests(unittest.TestCase):
    def test_dependent_filer_keeps_own_return_separate(self):
        child = {'DEP_STAT': '1', 'age': 16, 'tax_id': ('10', '102')}
        adult = {'tax_id': ('10', '101')}
        r = claimant_record(('10', '43'), child, {('10', '1'): adult})
        self.assertEqual(r['own_census_tax_unit_id'], '10:102')
        self.assertEqual(r['census_claimant_tax_unit_id'], '10:101')
        self.assertEqual(child['tax_id'], ('10', '102'))

    def test_no_pointer_does_not_create_claimant(self):
        child = {'DEP_STAT': '0', 'age': 10, 'tax_id': ('10', '101')}
        r = claimant_record(('10', '43'), child, {})
        self.assertIsNone(r['census_claimant_tax_unit_id'])

    def test_source_inputs_complete(self):
        pop, econ, hashes = read_inputs(HERE/'empirical')
        self.assertEqual(len(pop), 108)
        self.assertEqual(len(hashes), 3)
        self.assertGreater(econ[(2034, 'cpiu')], econ[(2025, 'cpiu')])

    def test_relative_growth_not_absolute_population(self):
        pop, _, _ = read_inputs(HERE/'empirical')
        rows = [dict(age=8, sex='male', resources=5000, threshold=10000,
                     person_weight=2, replicate_weights=[1, 3]),
                dict(age=8, sex='male', resources=15000, threshold=10000,
                     person_weight=2, replicate_weights=[1, 3])]
        before = copy.deepcopy(rows)
        r = sensitivity(rows, pop, 2030)
        factor = pop[(2030, 8, 'male')]/pop[(2026, 8, 'male')]
        self.assertAlmostEqual(r['all_children']['weighted_children'], 4*factor)
        self.assertAlmostEqual(r['all_children']['poor_rate'], .5)
        self.assertEqual(r['conditional_sampling_uncertainty']['n_replicates'], 2)
        self.assertEqual(rows, before)
        self.assertNotEqual(r['status'], 'projected')

    def test_resource_formula_includes_refunds_only_once(self):
        u = {k: 0 for k in ('SPM_TOTVAL', 'SPM_SNAPSUB', 'SPM_CAPHOUSESUB', 'SPM_SCHLUNCH',
             'SPM_WICVAL', 'SPM_ENGVAL', 'SPM_FEDTAX', 'SPM_STTAX', 'SPM_FICA',
             'SPM_CAPWKCCXPNS', 'SPM_CHILDSUPPD', 'SPM_MEDXPNS')}
        u.update(SPM_TOTVAL=10000, SPM_FEDTAX=-2000, SPM_ACTC=2000)
        self.assertEqual(resource_total(u), 12000)


if __name__ == '__main__':
    unittest.main()
