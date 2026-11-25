#!/usr/bin/env python3
"""Tests for `fiscal_revision.py` (stage G step 9: G23's debt goals and G24's financing mixes). Run after the common
rebuild (run-all.sh step 8c4).

Checks: the base carries CLI-1's correction once (and PH-3); goal A holds FY2039's level, which G19 B's FY2037-39
steps put below step 8b's 116.9%; each solved share meets its goal and a slightly smaller one doesn't; each mix's plug
closes its goal; the VAT's rebate is what the header says; the take-home base reproduces the booked 69.0%; and the
committed note equals what the code writes.
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'models/tools'))
import fiscal_revision as R   # noqa: E402
import fiscal_path as FP      # noqa: E402

D = R.build()


class Revision(unittest.TestCase):
    def test_base(self):
        B = D['B']
        self.assertLess(D['base_sim'][2056]['debt_gdp'], B['booked'].rows[2056]['debt_gdp'])
        self.assertAlmostEqual(sum(B['ph3'].values()), 52, delta=1)

    def test_goal_a_level(self):
        s = D['G']['A']['sim']
        self.assertLess(s[2039]['debt_gdp'], 116.9)
        for y in range(2041, 2057):
            self.assertLessEqual(s[y]['debt_gdp'], s[2040]['debt_gdp'] + 1e-6)

    def test_shares_minimal(self):
        bk, ph3 = D['bk'], D['B']['ph3']
        for gid in ('B', 'C', 'D'):
            g = D['G'][gid]
            ok = lambda s: R.met(g['goal'], FP.simulate(bk, R.add(ph3, FP.shape(bk, s, g['start']))))
            self.assertTrue(ok(g['share']))
            self.assertFalse(ok(g['share'] - 0.01))

    def test_plugs_close(self):
        for (gid, mid), mx in D['M'].items():
            if mx is not None:
                self.assertTrue(R.met(D['G'][gid]['goal'], mx['sim']), (gid, mid))

    def test_rebate(self):
        net, reb = R.vat_point(D['bk'], 2040)
        self.assertAlmostEqual(reb, 150 * R.adults(2040) / 1000, places=6)
        self.assertAlmostEqual(net + reb, R.K.VAT_POINT_2040, places=6)

    def test_take_home_base(self):
        self.assertAlmostEqual(D['th']['base']['workers'], 69.0, delta=0.05)

    def test_note_current(self):
        self.assertEqual(R.OUT.read_text(), R.markdown(D))


if __name__ == '__main__':
    unittest.main()
