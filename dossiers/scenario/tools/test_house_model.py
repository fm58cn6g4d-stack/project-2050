#!/usr/bin/env python3
"""Tests for house_model.py: the curve's calibration, monotonicity and the trifecta bookkeeping.

Role: checks the 2028 House model behind dossiers/scenario/house-model-2028.md. Status: current.
Run: python3 dossiers/scenario/tools/test_house_model.py
"""
import os
import random
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import house_model as hm  # noqa: E402


class Curve(unittest.TestCase):
    def test_calibration_reproduces_the_2024_district_count(self):
        sp = hm.fit_spread()
        seats = hm.SEATS * hm.phi((hm.NAT_PRES_2024 - hm.PARAMS['median']) / sp)
        self.assertAlmostEqual(seats, 201, delta=0.5)        # Trump carried 234 of 435 [SRC-0817]

    def test_median_is_the_break_even(self):
        sp = hm.fit_spread()
        self.assertAlmostEqual(hm.SEATS * hm.phi(0) , 217.5)
        self.assertAlmostEqual(hm.SEATS * hm.phi((3.0 - hm.PARAMS['median']) / sp), 217.5, delta=0.01)

    def test_curve_near_2026_result(self):
        sp = hm.fit_spread()
        seats = hm.SEATS * hm.phi((12.9 - hm.PARAMS['median']) / sp)
        self.assertTrue(245 <= seats <= 265, seats)          # about 259 won in 2026

    def test_inv_phi(self):
        for p in (0.1, 0.46, 0.5, 0.9):
            self.assertAlmostEqual(hm.phi(hm.inv_phi(p)), p, places=6)


class Simulation(unittest.TestCase):
    def test_monotone_in_environment(self):
        means = [hm.summary(hm.simulate(e, n=1500, seed=3))['mean'] for e in (-3, 0, 3, 6)]
        self.assertEqual(means, sorted(means))

    def test_trifecta_needs_all_three(self):
        runs = hm.simulate(3.0, n=1500, seed=4)
        s = hm.summary(runs)
        self.assertLessEqual(s['trifecta'], s['house_and_senate'])
        self.assertLessEqual(s['house_and_senate'], s['house'])
        self.assertEqual(hm.summary(runs, 'R')['trifecta'], 0.0)

    def test_deterministic(self):
        self.assertEqual(hm.simulate(0.0, n=300, seed=8), hm.simulate(0.0, n=300, seed=8))

    def test_map_shift_bounds(self):
        rng = random.Random(2)
        lo = sum(d for p, d in hm.MAP_CHANGES.values() if d < 0)
        hi = sum(d for p, d in hm.MAP_CHANGES.values() if d > 0)
        for _ in range(500):
            self.assertTrue(lo <= hm.map_shift(rng) <= hi)


if __name__ == '__main__':
    unittest.main(verbosity=1)
