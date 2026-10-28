"""Check material payment and overlap boundaries, not policy/legal validity."""
import unittest
from decision_analysis import claim_split, hcbs_split, payer_route


class HealthBoundaryTests(unittest.TestCase):
    def test_claim_with_deductible(self):
        r = claim_split(1000, 100)
        self.assertEqual(r['medicare'], 720)
        self.assertEqual(r['patient'], 280)
        self.assertEqual(r['medicare'] + r['non_medicare_share'], 1000)

    def test_deductible_larger_than_claim(self):
        self.assertEqual(claim_split(50, 100)['patient'], 50)
        self.assertEqual(claim_split(50, 100)['medicare'], 0)

    def test_qmb_does_not_shift_everything_to_medicare(self):
        r = claim_split(1000, 100, qmb=True)
        self.assertEqual(r['patient'], 0)
        self.assertEqual(r['medicare'], 720)
        self.assertEqual(r['non_medicare_share'], 280)

    def test_unknown_is_not_zero(self):
        self.assertIsNone(claim_split(None, 100)['medicare'])
        self.assertIsNone(hcbs_split(100, .6, None, 10)['resources'])

    def test_ma_existing_obligation_stays_with_plan(self):
        self.assertEqual(payer_route('MA', existing_obligation=True, significance='significant', overlap_known=True), 'MA')

    def test_partial_overlap_cannot_be_assumed_ffs(self):
        self.assertEqual(payer_route('MA', significance='significant', overlap_known=False), 'unresolved')
        self.assertEqual(payer_route('MA', significance='unknown', overlap_known=True), 'unresolved')

    def test_nonsignificant_and_adjusted_contract(self):
        self.assertEqual(payer_route('MA', significance='nonsignificant'), 'MA')
        self.assertEqual(payer_route('MA', adjusted=True, significance='significant'), 'MA')
        self.assertEqual(payer_route('MA', significance='significant', overlap_known=True), 'FFS')
        self.assertEqual(payer_route('FFS'), 'FFS')

    def test_match_is_share_not_added_resource(self):
        r = hcbs_split(100, .6, .1, 10)
        self.assertAlmostEqual(r['federal'], 80)
        self.assertAlmostEqual(r['state'], 30)
        self.assertEqual(r['resources'], 110)
        self.assertAlmostEqual(r['federal'] + r['state'], r['resources'])

    def test_invalid_values_rejected(self):
        with self.assertRaises(ValueError):
            hcbs_split(100, .9, .2, 10)
        with self.assertRaises(ValueError):
            claim_split(-1, 100)
        with self.assertRaises(ValueError):
            payer_route('unknown')


if __name__ == '__main__':
    unittest.main()
