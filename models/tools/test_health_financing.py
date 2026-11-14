"""Tests for `health_financing.py`: its figures reconcile with the booked model and the care dossier.

Role: checks the settlement checkpoint memo's health-financing arithmetic. Status: exploratory analysis's test.
Run: `python3 models/tools/test_health_financing.py`.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import health_financing as HF  # noqa: E402


class HealthFinancing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = HF.run()

    def test_need_is_the_booked_health_rows(self):
        n = self.r["need"]
        self.assertAlmostEqual(n["net"], n["spending"] + n["hx"], places=6)
        self.assertAlmostEqual(n["net"], 4093.7, delta=1.0)            # care 6-cost.md, part 5

    def test_gap_is_the_budget_models(self):
        self.assertAlmostEqual(self.r["gap"]["gap_2040"], 4164.0, delta=1.0)

    def test_full_scale_flows_match_the_dossier(self):
        fl = self.r["flows"]
        self.assertAlmostEqual(fl["plan_2032"]["net_model"], 2712, delta=1)
        self.assertAlmostEqual(fl["nhe_2032"]["change"], -491, delta=1)
        self.assertAlmostEqual(fl["stop_paying_2032"]["states"], 225, delta=1)
        self.assertAlmostEqual(fl["plan_2032"]["net_spending"], 3391, delta=2)

    def test_employer_contribution_net_matches_the_dossier(self):
        self.assertAlmostEqual(self.r["f1"]["employer_net"], 1061, delta=2)   # care 6-cost.md, part 4

    def test_each_option_closes_health_exactly(self):
        """Every F1 option's revenue rows, with the employer side and the states' extra, add to health's need."""
        need = self.r["need"]["net"]
        for k, o in self.r["f1"]["options"].items():
            rev = -sum(bn for label, bn, key in o["rows"][3:])
            self.assertAlmostEqual(rev + self.r["state_extra"], need, delta=1.0, msg=k)

    def test_keys_sum_to_100(self):
        for k, (sh, t1) in self.r["keys"].items():
            self.assertAlmostEqual(sum(sh), 100, delta=1e-6, msg=k)

    def test_relief_before_financing_adds_up(self):
        f = self.r["flows"]["fy2040"]
        total = sum(self.r["before_financing"][g] for g in HF.GROUPS) * 0.2 * self.r["households_2040"] / 1e9
        self.assertAlmostEqual(total, f["households"] + f["employers"] - f["hx_gross"], delta=2.0)


if __name__ == "__main__":
    unittest.main()
