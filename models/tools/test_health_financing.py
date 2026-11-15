"""Tests for `health_financing.py`: its figures reconcile with the booked model, the care dossier and themselves.

Role: checks the settlement checkpoint memo's health-financing arithmetic. Status: exploratory analysis's test,
revised November 15, 2026 with the corrected household method, the packages and the payer reconciliation.
Run: `python3 models/tools/test_health_financing.py`.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import health_financing as HF  # noqa: E402

FIRST_ROWS = 5   # relief_rows (3) and employer_rows (2) come before the household side's rows


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

    def test_every_package_closes_health_exactly(self):
        """Each package's and each memo option's revenue (employer net, households' collected contribution, states'
        extra share and any savings) adds to health's FY2040 need."""
        need = self.r["need"]["net"]
        groups = [self.r["packages"], self.r["package_sensitivities"], self.r["f1"], self.r["f2"], self.r["f3"]]
        for g in groups:
            for k, o in g.items():
                rev = -sum(bn for _, bn, _ in o["rows"][FIRST_ROWS:])
                self.assertAlmostEqual(rev + o["employer_net"] + o["state_extra"] + o["savings"], need, delta=1.0,
                                       msg=(o["label"], k))

    def test_statutory_charge_less_avoidance_is_what_is_collected(self):
        """The broad tier: the charge is the rate times the base the budget model's yield implies; the allowance is
        20% of it; what is left is what the package collects."""
        a, b, pp = self.r["packages"]["A"], self.r["base_2040"], self.r["per_point"]
        self.assertAlmostEqual(b["statutory_charge_bn"] * (1 - pp["haircut"]), a["rest"], delta=0.5)
        self.assertAlmostEqual(b["statutory_bn"] * a["rates"][0] / 100, b["statutory_charge_bn"], delta=0.5)
        # the CPS-grown base is within 5% of the base the budget model's yield implies
        self.assertLess(abs(b["cps_grown_bn"] / b["statutory_bn"] - 1), 0.05)
        # per household, the middle fifth's charge is the rate times its base (the reader's multiplication)
        q3 = [d for d in a["detail"] if d[0].endswith("statutory charge")][0][2]["Q3"]
        self.assertAlmostEqual(-q3, a["rates"][0] / 100 * b["per_household"]["Q3"], delta=2)

    def test_central_avoidance_falls_on_the_top_fifth(self):
        q, t1 = self.r["keys"]["avoid_central"]
        self.assertEqual(q[:4], [0.0, 0.0, 0.0, 0.0])
        self.assertAlmostEqual(q[4], 100.0)
        sh, t1_base = self.r["keys"]["income_line"]
        self.assertAlmostEqual(t1, 100 * t1_base / sh[4], places=6)

    def test_corrected_method_matches_the_leads_trace(self):
        """The lead's re-estimate of the first draft's package: middle fifth about +$8,700, fourth about break-even."""
        h = self.r["packages"]["A"]["households"]
        self.assertAlmostEqual(h["Q3"], 8700, delta=300)
        self.assertAlmostEqual(h["Q4"], 0, delta=500)
        self.assertEqual(self.r["packages"]["A"]["avoidance_range"]["even"]["Q3"], 11077)   # the first draft's figure

    def test_recommended_package_leaves_the_bottom_four_ahead(self):
        c = self.r["packages"]["C"]
        self.assertTrue(c["bottom_four_ahead"])
        self.assertLess(c["top_rate_on_wages"], self.r["packages"]["A"]["top_rate_on_wages"])
        self.assertAlmostEqual(c["rates"][0], 10.0, delta=0.1)

    def test_keys_sum_to_100(self):
        for k, (sh, t1) in self.r["keys"].items():
            self.assertAlmostEqual(sum(sh), 100, delta=1e-6, msg=k)

    def test_relief_before_financing_adds_up(self):
        f = self.r["flows"]["fy2040"]
        total = sum(self.r["before_financing"][g] for g in HF.GROUPS) * 0.2 * self.r["households_2040"] / 1e9
        self.assertAlmostEqual(total, f["households"] + f["employers"] - f["hx_gross"], delta=2.0)

    def test_reconciliation_adds_to_national_spending_both_ways(self):
        rc = self.r["reconciliation"]
        n = rc["nhe_2032"]
        self.assertAlmostEqual(n["today"], n["model_today"], delta=0.01)
        self.assertAlmostEqual(n["plan"], n["model_plan"], delta=0.01)
        self.assertAlmostEqual(sum(rc["change_2032"].values()), -491, delta=1)
        self.assertAlmostEqual(sum(rc["seam_2032"].values()), rc["unassigned_2032"], delta=0.01)
        i = rc["identity_2032"]
        self.assertAlmostEqual(i["new_federal"], i["households"] + i["employers"] + i["states"] + i["unassigned"]
                               + i["others_uncompensated_care"] - i["national_saving"], delta=0.01)
        # the plan's federal spending net of what it replaces and the states' payment is the dossier's $3,391B
        self.assertAlmostEqual(rc["change_2032"]["federal"], self.r["flows"]["plan_2032"]["net_spending"], delta=1)
        # the first draft's "missing term" (about $565B) is the unassigned part plus others' uncompensated care
        self.assertAlmostEqual(rc["unassigned_2032"] + rc["displaced_2032"], 565, delta=5)


if __name__ == "__main__":
    unittest.main()
