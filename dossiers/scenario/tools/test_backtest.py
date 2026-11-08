#!/usr/bin/env python3
"""Tests for backtest.py: the extracted data matches the model's typed inputs; the rules and back-tests run.

Role: checks the back-test behind dossiers/scenario/model-credibility.md. Status: current.
Run: python3 dossiers/scenario/tools/test_backtest.py
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import backtest as bt  # noqa: E402
import senate_model as sm  # noqa: E402


class Data(unittest.TestCase):
    def test_extract_matches_typed_presidential_inputs(self):
        for s in sm.P20:
            if s == 'NY':
                continue   # the extract counts the Democratic line only, not fusion lines (Working Families)
            self.assertAlmostEqual(bt.PRES[2020][s], sm.P20[s], delta=0.06, msg=s)
            self.assertAlmostEqual(bt.PRES[2024][s], sm.P24[s], delta=0.06, msg=s)

    def test_midterm_swings_match_model(self):
        sw = [round(bt.midterm_swing(y), 1) for y in bt.MIDTERMS]
        self.assertEqual(sw, [round(x, 1) for x in sm.MIDTERM_SWINGS])


class Backtests(unittest.TestCase):
    def test_senate_backtest_runs_and_bias_shift_raises_seats(self):
        a = bt.senate_backtest(2024, bt.NAT_PRES[2024], n=500)
        b = bt.senate_backtest(2024, bt.NAT_PRES[2024], n=500, prm={'bias': 3.0})
        self.assertGreater(a['n_races'], 25)
        self.assertGreater(b['pred'], a['pred'])
        self.assertTrue(0 <= a['brier'] <= 1)

    def test_environment_rule_rmse(self):
        rows, res = bt.env_rules()
        self.assertEqual(len(rows), 9)
        self.assertAlmostEqual(res['Average of the two'][0], 4.5, delta=0.1)
        self.assertAlmostEqual(res['Average of the two'][2], (12.9 - 1.48) / 2, places=6)

    def test_house_backtest_fits_previous_election(self):
        r = bt.house_backtest(2020, bt.NAT_HOUSE[2018], n=2000)
        self.assertAlmostEqual(r['pred'], bt.HOUSE_SEATS_D[2018], delta=3)   # refits 2018 at 2018's vote


if __name__ == '__main__':
    unittest.main(verbosity=1)
