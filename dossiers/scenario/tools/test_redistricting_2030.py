#!/usr/bin/env python3
"""Tests for redistricting_2030.py: pen rules, the Title II arithmetic and monotonicity.

Role: checks the 2031-pens model behind dossiers/scenario/redistricting-2030-model.md. Status: current.
Run: python3 dossiers/scenario/tools/test_redistricting_2030.py
"""
import os
import random
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import redistricting_2030 as rd  # noqa: E402


class Pens(unittest.TestCase):
    def test_commission_states_are_neutral(self):
        rng = random.Random(1)
        for e in (-20, 0, 20):
            self.assertEqual(rd.pen('MI', e, 0, rng), 'N')
            self.assertEqual(rd.pen('AZ', e, 0, rng), 'N')

    def test_sweeps_give_the_pen(self):
        rng = random.Random(2)
        self.assertEqual(rd.pen('TX', 60, 0, rng), 'D')
        self.assertEqual(rd.pen('TX', -60, 0, rng), 'R')
        self.assertEqual(rd.pen('NC', 60, 0, rng), 'D')

    def test_split_control_is_neutral(self):
        # Georgia at an environment that elects a Democratic governor but a Republican Senate
        rng = random.Random(3)
        old = rd.SD_GOV, rd.SD_CHAMBER
        rd.SD_GOV = rd.SD_CHAMBER = 1e-9
        try:
            self.assertEqual(rd.pen('GA', 5.0, 0, rng), 'N')
        finally:
            rd.SD_GOV, rd.SD_CHAMBER = old


class Values(unittest.TestCase):
    def test_title2_shrinks_partisan_effect(self):
        runs = rd.simulate(n=1500, seed=5)
        for r in runs[:200]:
            self.assertAlmostEqual(r['with_t2'] - r['without'], -rd.F_TITLE2 * r['eff'], places=6)

    def test_value_rises_with_f(self):
        lo = rd.summarize(rd.simulate(n=1500, seed=6, f=0.4), 'D')['value']
        hi = rd.summarize(rd.simulate(n=1500, seed=6, f=0.85), 'D')['value']
        self.assertGreater(hi, lo)

    def test_democratic_president_means_more_republican_pens(self):
        runs = rd.simulate(n=3000, seed=7)
        d = rd.summarize(runs, 'D')
        r = rd.summarize(runs, 'R')
        self.assertLess(d['eff12'], r['eff12'])          # the 2030 midterm penalty
        self.assertGreater(d['value'], r['value'])

    def test_deterministic(self):
        a = rd.summarize(rd.simulate(n=800, seed=8), 'D')['value']
        b = rd.summarize(rd.simulate(n=800, seed=8), 'D')['value']
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main(verbosity=1)
