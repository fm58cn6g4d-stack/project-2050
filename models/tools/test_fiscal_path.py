#!/usr/bin/env python3
"""Tests for stage G step 8's fiscal path tools: `fiscal_path.py` (the debt goals on the conventional score) and
`fiscal_dynamic.py` (the contained dynamic layer). Run after the common rebuild (run-all.sh step 8d).

Checks: the central reading is the budget model's booked path; the r - g readings hit their targets; each goal's
solved share meets the goal and a slightly smaller one doesn't; the debt identity holds for added deficit reduction;
the dynamic layer is symmetric (reading B leaves the baseline unchanged, and with no channels and no feedback the plan
is the conventional path); the registration is unchanged since it was committed; WAD-H1 never enters a net, a path or a
goal; the pessimistic goal shares are each goal's own worst feedback end; DY4 stays
zero (the double count with LAB-1); and the two committed results notes equal what the code writes.
"""
import hashlib
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'models/tools'))
import fiscal_path as FP      # noqa: E402
import fiscal_dynamic as FD   # noqa: E402

BK = FP.Booked()
# the registration as committed in 87125a0 (stage G step 8a); a change is a new registration (the note says how)
REGISTERED_SHA256 = 'e861f380213528c64d29e5c296fc61fa83c74859846c59a64eeb1ccf3a8a0093'


class FiscalPath(unittest.TestCase):
    def test_central_is_the_booked_path(self):
        sim = FP.simulate(BK)
        self.assertAlmostEqual(sim[2040]['debt_gdp'], BK.rows[2040]['debt_gdp'], places=9)
        self.assertAlmostEqual(sim[2056]['debt_gdp'], BK.rows[2056]['debt_gdp'], places=9)
        self.assertEqual(round(sim[2040]['debt_gdp'], 1), 117.8)
        self.assertEqual(round(sim[2056]['debt_gdp'], 1), 133.1)

    def test_r_minus_g_readings(self):
        for t in (-0.5, 1.5):
            sh = FP.shift_for(BK, t)
            self.assertAlmostEqual(FP.r_minus_g(BK, FP.simulate(BK, shift_points=sh)), t, places=3)
        self.assertTrue(0.3 < FP.r_minus_g(BK, FP.simulate(BK)) < 0.6)

    def test_goals_solved_minimally(self):
        for g, _ in FP.GOALS:
            s = FP.solve_share(BK, g, 0.0)
            self.assertTrue(FP.met(g, FP.simulate(BK, FP.shape(BK, s))), g)
            self.assertFalse(FP.met(g, FP.simulate(BK, FP.shape(BK, s - 0.01))), g)

    def test_debt_identity(self):
        X = FP.shape(BK, 1.0)
        sim = FP.simulate(BK, X)
        cut = sum(X[y] for y in FP.YEARS) + sum(sim[y]['interest_saved'] for y in FP.YEARS)
        self.assertAlmostEqual(BK.debt[2056] - sim[2056]['debt'], cut, places=6)
        self.assertTrue(all(sim[y]['interest_saved'] >= 0 for y in FP.YEARS))

    def test_shape_respects_the_populist_start(self):
        X = FP.shape(BK, 1.0)
        self.assertTrue(all(X[y] == 0 for y in range(2026, 2032)))

    def test_year_by_year_goal1_holds_flat(self):
        sim = FP.simulate(BK, FP.year_by_year(BK, 0.0))
        for y in FP.WINDOW:
            self.assertLessEqual(sim[y]['debt_gdp'], sim[y - 1]['debt_gdp'] + 1e-6)


class Dynamic(unittest.TestCase):
    def test_registration_unchanged(self):
        h = hashlib.sha256((ROOT / 'models/tools/fiscal_dynamic_params.json').read_bytes()).hexdigest()
        self.assertEqual(h, REGISTERED_SHA256, 'fiscal_dynamic_params.json changed after registration: record it '
                         'in dynamic-preregistration.md ("Changes after registration") and update this hash')

    def _recursion(self, out, ref, fb='central'):
        """Rebuild the rate path from the engine's own debt ratios, independently of run()'s loop."""
        sym = FD.PARAMS['symmetric']
        beta, adj = sym['rate_bp_per_point'][fb] / 10000, sym['rate_bp_per_point']['adjust_years']
        dr, prev, rates = 0.0, out[FD.REF_YEAR]['debt_gdp'], {}
        for y in range(FD.START, 2057):
            dr += (beta * (prev - ref(y - 1)) - dr) / adj
            rates[y] = 100 * dr
            prev = out[y]['debt_gdp']
        return rates

    def test_reading_b_feedback_is_the_plans_difference(self):
        """Reading B charges the plan beta x (plan - baseline): its rate change is negative and matches the recursion."""
        base = {y: BK.rows[y]['baseline_debt_bn'] for y in FP.YEARS}
        ratio = {y: 100 * base[y] / BK.gdp[y] for y in FP.YEARS}
        out = FD.run(BK, BK.debt, BK.gdp, None, reference='B', ref_path=ratio)
        rates = self._recursion(out, lambda y: ratio[y])
        for y in range(FD.START, 2057):
            self.assertAlmostEqual(out[y]['rate_pts'], rates[y], places=9)
        self.assertLess(out[2056]['rate_pts'], -0.5)        # 47 points below the baseline: rates well down
        base_b = FD.run(BK, base, BK.gdp, None, reference='B', ref_path=ratio)
        self.assertEqual(max(abs(base_b[y]['rate_pts']) for y in FP.YEARS), 0.0)

    def test_symmetry_reading_a(self):
        """The same engine and coefficients run on both paths: each path's rate change follows beta x (its own debt -
        the FY2029 ratio), and the baseline's rises more because its debt is higher."""
        base = {y: BK.rows[y]['baseline_debt_bn'] for y in FP.YEARS}
        outs = {k: FD.run(BK, d, BK.gdp, None, reference='A') for k, d in (('base', base), ('plan', BK.debt))}
        for k, d in (('base', base), ('plan', BK.debt)):
            ref = 100 * d[FD.REF_YEAR] / BK.gdp[FD.REF_YEAR]
            rates = self._recursion(outs[k], lambda y: ref)
            for y in range(FD.START, 2057):
                self.assertAlmostEqual(outs[k][y]['rate_pts'], rates[y], places=9)
        self.assertGreater(outs['base'][2056]['rate_pts'], outs['plan'][2056]['rate_pts'] + 0.5)
        self.assertGreater(outs['base'][2056]['debt_gdp'], 100 * base[2056] / BK.gdp[2056])

    def test_pessimistic_is_the_worst(self):
        """On each feedback reading, the pessimistic case's FY2056 debt is the highest of the low-channel pairings."""
        base_ratio = {y: 100 * BK.rows[y]['baseline_debt_bn'] / BK.gdp[y] for y in FP.YEARS}
        net = FD.net_of(FD.channels(BK.gdp, 'low'))
        for reading in ('A', 'B'):
            path, _ = FD.case_run(BK, BK.debt, net, reading, 'pessimistic', base_ratio)
            for e in ('low', 'central', 'high'):
                alt = FD.run(BK, BK.debt, BK.gdp, net, fb_end=e, reference=reading, ref_path=base_ratio)
                self.assertGreaterEqual(path[2056]['debt_gdp'], alt[2056]['debt_gdp'] - 1e-9)

    def test_amendments_leave_the_registration(self):
        self.assertEqual(FD.REGISTERED['channels']['N-TOP']['low'], -0.25)
        self.assertEqual(FD.PARAMS['channels']['N-TOP']['low'], -0.51)
        self.assertIn('N-CTC', FD.PARAMS['channels'])
        self.assertNotIn('N-CTC', FD.REGISTERED['channels'])

    def test_no_channels_no_feedback_is_conventional(self):
        out = FD.run(BK, BK.debt, BK.gdp, None, reference='C')
        for y in FP.YEARS:
            self.assertAlmostEqual(out[y]['debt_gdp'], BK.rows[y]['debt_gdp'], places=9)

    def test_wad_never_enters(self):
        """Inflating WAD-H1 tenfold changes no net, no dynamic path and no goal share (the reviewer's leak test)."""
        ref = FD.build()
        w = FD.PARAMS['works_as_designed']['WAD-H1']['points_below_cap']
        saved = dict(w)
        try:
            for k in w:
                w[k] = 10 * w[k] + 1.0
            alt = FD.build()
        finally:
            w.update(saved)
        self.assertNotEqual(alt['wad']['central'][2056], ref['wad']['central'][2056])
        for name, _ in FD.CASES:
            self.assertEqual(alt['cases'][name]['net'], ref['cases'][name]['net'])
            for rd in FD.READINGS:
                self.assertEqual(alt['cases'][name][rd]['plan'][2056]['debt_gdp'], ref['cases'][name][rd]['plan'][2056]['debt_gdp'])
        for g in ref['goals']:
            self.assertEqual(alt['goals'][g], ref['goals'][g])

    def test_pessimistic_goal_is_each_goals_worst(self):
        base_ratio = {y: 100 * BK.rows[y]['baseline_debt_bn'] / BK.gdp[y] for y in FP.YEARS}
        net = FD.net_of(FD.channels(BK.gdp, 'low'))
        for g, _ in FP.GOALS:
            for rd in ('A', 'B'):
                pess = FD.solve_dynamic(BK, g, net, rd, 'pessimistic', base_ratio)
                for e in ('low', 'high'):
                    one = FD._solve(lambda s: FP.met(g, FD.dynamic_with_x(BK, s, net, rd, e, base_ratio)))
                    self.assertGreaterEqual(pess, one)

    def test_negatives_counted(self):
        ch = FD.channels(BK.gdp, 'central')
        neg = [k for k, p in ch.items() if p[2040] < 0]
        for k in ('N-CONTRIB', 'N-TOP', 'N-WEALTH', 'N-HEALTHCOV'):
            self.assertIn(k, neg)

    def test_wad_measured_below_d2(self):
        w = FD.PARAMS['works_as_designed']['WAD-H1']
        self.assertEqual(w['points_below_cap']['low'], 0.0)
        self.assertEqual(w['start'], 2037)
        self.assertTrue(all(v == 0 for v in FD.wad_h1(BK.gdp, 'low').values()))

    def test_dy4_zero(self):
        import csv
        rows = {r['id']: r for r in csv.DictReader((ROOT / 'models/data/inputs/ledger-dynamic.csv').open())}
        self.assertEqual([float(rows['DY4'][k]) for k in ('lo', 'mid', 'hi', 'optimistic_mid')], [0, 0, 0, 0])


class Notes(unittest.TestCase):
    def test_notes_current(self):
        self.assertEqual(FP.OUT.read_text(), FP.markdown(FP.build()), 'run fiscal_path.py --write')
        self.assertEqual(FD.OUT.read_text(), FD.markdown(FD.build()), 'run fiscal_dynamic.py --write')


if __name__ == '__main__':
    unittest.main(verbosity=1)
