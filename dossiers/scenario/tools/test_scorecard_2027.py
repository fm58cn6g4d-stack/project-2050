#!/usr/bin/env python3
"""Tests for scorecard_2027.py: the on-track benchmarks, the update rule and its calibration.

Role: checks the pre-registered rule behind dossiers/scenario/2027-scorecard.md. Status: current.
Run: python3 dossiers/scenario/tools/test_scorecard_2027.py
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scorecard_2027 as sc  # noqa: E402
import senate_model as sm  # noqa: E402

KEYS = [c[0] for c in sc.CONTESTS]


class Rule(unittest.TestCase):
    def test_on_track_leaves_the_prior_centred(self):
        m, sd, g, sig = sc.update({k: 0.0 for k in KEYS})
        self.assertAlmostEqual(m, sc.PRIOR_MEAN)
        self.assertAlmostEqual(g, sc.K_FULL, places=6)
        self.assertLess(sd, sc.PRIOR_SD)

    def test_no_results_no_change(self):
        self.assertEqual(sc.update({})[:2], (sc.PRIOR_MEAN, sc.PRIOR_SD))

    def test_monotone_and_symmetric(self):
        up = sc.update({k: 5.0 for k in KEYS})[0]
        down = sc.update({k: -5.0 for k in KEYS})[0]
        self.assertAlmostEqual(up - sc.PRIOR_MEAN, sc.PRIOR_MEAN - down)
        self.assertAlmostEqual(up - sc.PRIOR_MEAN, 5.0 * sc.K_FULL)

    def test_one_contest_alone_moves_less_than_the_slate(self):
        for k in KEYS:
            self.assertLess(sc.move_per_point(k, alone=True), sc.K_FULL)
            self.assertGreater(sc.move_per_point(k, alone=True), sc.move_per_point(k))

    def test_full_slate_weights_sum_to_the_gain(self):
        self.assertAlmostEqual(sum(sc.move_per_point(k) for k in KEYS), sc.K_FULL)

    def test_benchmark_shifts_one_for_one_with_the_environment(self):
        for k in KEYS:
            self.assertAlmostEqual(sc.on_track(k, 6.0) - sc.on_track(k, 3.0), 3.0)

    def test_minnesota_on_track_is_a_comfortable_hold(self):
        self.assertGreater(sc.on_track('MN'), 8.0)

    def test_kentucky_and_mississippi_on_track_are_republican(self):
        self.assertLess(sc.on_track('KY'), 0)
        self.assertLess(sc.on_track('MS'), 0)


class Calibration(unittest.TestCase):
    def test_midterm_slope_near_one(self):
        mid, pres = sc.calibration()
        b, a = sc.ols([r[1] for r in mid], [r[3] for r in mid])
        self.assertAlmostEqual(b, 1.0, delta=0.1)

    def test_presidential_years_show_no_relation(self):
        mid, pres = sc.calibration()
        b, a = sc.ols([r[1] for r in pres], [r[3] for r in pres])
        self.assertLess(abs(b), 0.2)

    def test_court_excess(self):
        self.assertAlmostEqual(sc.G, 6.2, delta=0.1)


class Specials(unittest.TestCase):
    def test_series_matches_the_trackers_own_averages(self):
        by = sc.specials_by_year()
        for y, (n, avg) in {2017: (67, 11.2), 2019: (48, 4.7), 2021: (49, -4.4), 2023: (38, 5.2),
                            2025: (67, 13.9), 2026: (43, 10.4)}.items():
            self.assertEqual(by[y][0], n)
            self.assertAlmostEqual(by[y][1], avg, delta=0.05)

    def test_2025_26_cycle(self):
        n, avg = sc.specials_cycle('2025-26')
        self.assertEqual(n, 110)
        self.assertAlmostEqual(avg, 12.5, delta=0.05)

    def test_federal_tagging(self):
        import specials_extract as se
        self.assertTrue(se.is_federal('NJ-11', 'NJ'))
        self.assertTrue(se.is_federal('MT-AL', 'MT'))
        for d, st_ in (('SD-45', 'MS'), ('HD-85', 'PA'), ('AD-09', 'CA'), ('SD-10', 'SD')):
            self.assertFalse(se.is_federal(d, st_))

    def test_counted_never_exceeds_races(self):
        for r in sc.load_specials():
            self.assertLessEqual(int(r['races_counted']), int(r['races']))
            self.assertLessEqual(int(r['federal_counted']), int(r['races_counted']))

    def test_benchmark(self):
        self.assertAlmostEqual(sc.on_track('SP'), 4.48 + sc.SPECIALS_EXCESS, delta=0.01)
        self.assertAlmostEqual(sc.on_track('SP'), 11.2, delta=0.05)


class Fixing(unittest.TestCase):
    def test_fixed_restores_globals(self):
        before = dict(sm.UNCERTAIN_NOT_UP)
        with sc.fixed(mn=False, ny=True, va_senate=False):
            self.assertEqual(sm.UNCERTAIN_NOT_UP['MN-2027'], 0.0)
        self.assertEqual(sm.UNCERTAIN_NOT_UP, before)

    def test_losing_minnesota_costs_senate_odds(self):
        held = sc.metrics(3.0, 3.5, n=3000, mn=True)['p55']
        lost = sc.metrics(3.0, 3.5, n=3000, mn=False)['p55']
        self.assertGreater(held, lost)

    def test_deterministic(self):
        self.assertEqual(sc.metrics(3.0, 3.5, n=1500), sc.metrics(3.0, 3.5, n=1500))


if __name__ == '__main__':
    unittest.main(verbosity=1)
