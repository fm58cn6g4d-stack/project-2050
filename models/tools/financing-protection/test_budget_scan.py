"""Tests for the budget scan's screens (stage G step 4b). Run after the common rebuild:
    python3 models/tools/financing-protection/test_budget_scan.py
"""
import hashlib
import unittest

import budget_scan as S
import packages as K


def _hash_inputs():
    h = hashlib.sha256()
    for p in sorted((K.ROOT / 'models/data/inputs').rglob('*')):
        if p.is_file():
            h.update(p.read_bytes())
    return h.hexdigest()


class BudgetScan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = _hash_inputs()
        cls.ctx = K.Context()

    def test_decided_target(self):
        """The decided settlement leaves about $262B in FY2040 and $728B in FY2056 (memo G3's $263B and $731B, moved by
        G7's 1.65 points)."""
        e = S.evaluate(self.ctx, 'decided', [])
        self.assertAlmostEqual(e['left'][2040], 262.1, delta=1.0)
        self.assertAlmostEqual(e['left'][2056], 728.4, delta=2.0)

    def test_flat_real_is_zero_to_2036(self):
        o = S.opt_defense_flat_real(self.ctx)
        path = next(iter(o['adjust'].values()))
        self.assertTrue(all(abs(path[y]) < 1e-9 for y in range(2026, 2037)))
        self.assertLess(path[2040], -30)

    def test_cuts_are_negative_and_additive(self):
        parts = sum(S.evaluate(self.ctx, n, S.SETS[n])['cut'][2040]
                    for n in ('defense_recommended', 'farm', 'tax_recommended', 'housing_c'))
        whole = S.evaluate(self.ctx, 'recommended', S.SETS['recommended'])['cut'][2040]
        self.assertLess(whole, 0)
        self.assertAlmostEqual(parts, whole, delta=0.5)

    def test_package_closes_2040_on(self):
        p = S.package(self.ctx)
        self.assertLessEqual(p['worst'], 0.05)

    def test_inputs_untouched(self):
        self.assertEqual(self.before, _hash_inputs())


if __name__ == '__main__':
    unittest.main()
