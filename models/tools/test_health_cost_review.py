"""Tests for `health_cost_review.py`: the rebuild reproduces the model, each correction is what it says, and every
package's sources add up to its gross cost.

Role: checks the arithmetic of `dossiers/foundations/health-cost-review.md`. Status: exploratory analysis's test,
November 15, 2026. Run: `python3 models/tools/test_health_cost_review.py` (about two minutes).
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import health_cost_review as CR  # noqa: E402
import health_financing as HF  # noqa: E402


class CostBridge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.g40 = CR._g40()
        cls.rows, cls.opts, _ = CR.bridge(cls.g40)

    def test_default_reproduces_groups_exactly(self):
        for g, d in CR.check_reproduces().items():
            self.assertAlmostEqual(d, 0.0, places=6, msg=g)

    def test_physician_step_matches_the_memo(self):
        c = HF.coverage(True)
        ref = HF.physician_rate(c, self.g40, rates=(1.05,))[1.05]
        self.assertAlmostEqual(self.rows[1]["d_cost_2040"], ref, places=6)       # about -275

    def test_newly_covered_priced_off_people_under_65(self):
        self.assertGreater(self.rows[1]["new_pp"], 12000)       # all-ages average, Medicare included
        self.assertLess(self.rows[2]["new_pp"], 7500)           # people under 65

    def test_bridge_adds_up(self):
        total = sum(r["d_cost_2040"] for r in self.rows[1:])
        last = CR.rebuild(self.opts)["cost_total"]
        first = CR.rebuild()["cost_total"]
        self.assertAlmostEqual(total, (last - first) * self.g40, places=6)
        self.assertLess(total, -500)                            # the corrected FY2040 gross is about $7.8T
        self.assertGreater(total, -750)

    def test_medicaid_seam_lowers_the_states_share(self):
        r = self.rows[-1]
        self.assertLess(r["d_state_2040"], -150)
        self.assertGreater(r["d_fed_2040"], 100)


class Packages(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx = HF.context()
        cls.cases = CR.cost_cases(CR._g40())

    def test_sources_add_up_and_take_home(self):
        for k in ("A1", "E"):
            label, case, spec = CR.PACKAGES2[k]
            o = CR.health_package(self.ctx, self.cases[case], spec)
            src = CR._sources(self.ctx, o, self.cases[case])
            self.assertAlmostEqual(src["check"], 0.0, delta=0.01, msg=k)
            T = CR.household_T(self.ctx, o)
            if k == "E":
                self.assertEqual(o["first"], 0.0)
                self.assertLess(T["plan"], T["today"])          # passes the take-home test
                self.assertAlmostEqual(o["second"], 4.0, places=9)
            else:
                self.assertGreater(o["first"], 7.0)
                self.assertLess(o["first"], 8.5)


if __name__ == "__main__":
    unittest.main()
