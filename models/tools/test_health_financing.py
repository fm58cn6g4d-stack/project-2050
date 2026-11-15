"""Tests for `health_financing.py`: its figures reconcile with the booked model, the care dossier and themselves.

Role: checks the arithmetic of `dossiers/foundations/health-financing.md`. Status: exploratory analysis's test,
November 15, 2026 (the fresh start: the Medicare seam, the payer accounting, the packages year by year).
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

    def test_need_is_the_booked_health_rows_less_the_seam(self):
        n = self.r["need_path"]
        self.assertAlmostEqual(n[2040]["booked"], 4093.7, delta=1.0)            # care 6-cost.md, part 5
        for y, d in n.items():
            self.assertAlmostEqual(d["net"], d["booked"] + d["seam"], places=6)
            self.assertAlmostEqual(d["booked"], d["spending"] + d["hx"], places=6)
            self.assertLessEqual(d["seam"], 0.0)
        self.assertAlmostEqual(n[2040]["seam"], -300, delta=5)
        self.assertAlmostEqual(sum(n[y]["seam"] for y in range(2030, 2040)), -1281, delta=10)

    def test_seam_is_medicares_and_vanishes_when_rebased(self):
        self.assertAlmostEqual(self.r["payers_booked"]["seam_2032"], 172, delta=1)
        self.assertAlmostEqual(self.r["payers"]["seam_2032"], 0.0, delta=1e-6)
        g = self.r["seam"]["by_group_2032"]
        self.assertAlmostEqual(g["medicare"], -181, delta=1)
        for k in ("medicaid", "employer", "individual"):
            self.assertAlmostEqual(g[k], 0.0, delta=1e-6)

    def test_payers_add_to_national_spending_both_ways(self):
        for name in ("payers", "payers_booked"):
            rc = self.r[name]
            n = rc["nhe_2032"]
            self.assertAlmostEqual(n["today"], n["model_today"], delta=0.01, msg=name)
            self.assertAlmostEqual(n["plan"], n["model_plan"], delta=0.01, msg=name)
            i = rc["identity_2032"]
            self.assertAlmostEqual(i["new_federal"], i["others_stop_paying"] - i["national_saving"], delta=0.01)
            self.assertAlmostEqual(sum(rc["lines_2032"].values()), rc["unassigned_2032"], delta=0.01)
            self.assertAlmostEqual(sum(rc["named_split_2032"].values()) + rc["seam_2032"], rc["unassigned_2032"],
                                   delta=0.01)
        # the rebased country saves more than the booked reading; new public money is below what others stop paying
        self.assertLess(self.r["payers"]["identity_2032"]["new_federal"],
                        self.r["payers"]["identity_2032"]["others_stop_paying"])

    def test_year_path_reaches_the_fy2040_table(self):
        p, rc = self.r["payer_path"][2040], self.r["payers"]
        nat = sum(rc["plan_2040"].values()) - sum(rc["today_2040"].values())
        self.assertAlmostEqual(p["national"], nat, delta=0.02 * abs(nat))
        for y, d in self.r["payer_path"].items():
            parts = sum(v for k, v in d.items() if k != "national")
            self.assertAlmostEqual(parts, d["national"], delta=0.01, msg=y)

    def test_every_package_closes_the_need(self):
        for grp in ("packages", "sensitivities"):
            for k, o in self.r[grp].items():
                got = o["employer_net"] + o["state_extra"] + o["household_collected"] + o["savings"]
                self.assertAlmostEqual(got, o["need"], delta=0.5, msg=(grp, k))
                # the household rows' collections equal household_collected
                hh_rows = [bn for lb, bn, _ in o["rows"][5:]]
                self.assertAlmostEqual(-sum(hh_rows), o["household_collected"], delta=0.5, msg=(grp, k))

    def test_package_paths_close_each_year_and_end_at_fy2040(self):
        for k, path in self.r["package_paths"].items():
            o = self.r["packages"][k]
            for y, d in path.items():
                self.assertAlmostEqual(d["employers"] + d["states"] + d["savings"] + d["households"], d["need"],
                                       delta=0.01)
            self.assertAlmostEqual(path[2040]["first"], o["first"], delta=1e-6)
            self.assertAlmostEqual(path[2040]["vat"], o["vat_rate"], delta=1e-6)

    def test_rates_multiply_out(self):
        """The middle fifth's first-tier charge is the rate times its base (the reader's multiplication)."""
        a, b = self.r["packages"]["A"], self.r["base_2040"]
        q3 = [d for d in a["detail"] if d[0] == "First tier: the statutory charge"][0][2]["Q3"]
        self.assertAlmostEqual(-q3, a["first"] / 100 * b["per_household"]["Q3"], delta=2)
        self.assertLess(abs(b["cps_grown_bn"] / b["statutory_bn"] - 1), 0.05)
        self.assertAlmostEqual(a["employer_rate"], 11.87, delta=0.01)
        self.assertAlmostEqual(a["employer_rate_with_hi"], a["employer_rate"] + 1.45, places=9)
        self.assertAlmostEqual(HF.TOP_RATE_BEFORE_HEALTH, 63.0)

    def test_hx_left_at_full_employer_share_is_the_workers_share(self):
        """At 100%, employers' premiums never become pay, so what HX keeps is the tax on the pay workers used to put
        into premiums before tax."""
        a, f = self.r["packages"]["A"], self.r["flows_path"][2040]
        self.assertAlmostEqual(a["hx_kept"], f["hx"] - self.r["tau"] * f["employers"], delta=0.01)
        self.assertGreater(a["hx_kept"], 0)

    def test_recommended_package_leaves_the_bottom_four_ahead(self):
        self.assertTrue(self.r["packages"]["A"]["bottom_four_ahead"])
        self.assertAlmostEqual(self.r["packages"]["B"]["first"], HF.FIRST_TIER_TARGET)

    def test_micro_spread_keeps_the_fifths_averages(self):
        for k in self.r["packages"]:
            m, h = self.r["micro"][k], self.r["packages"][k]["households"]
            for g in HF.GROUPS:
                self.assertAlmostEqual(m[g]["avg"], h[g], delta=5, msg=(k, g))   # h is rounded row by row

    def test_examples_add_up(self):
        for k, ex in self.r["examples"].items():
            for e in ex:
                parts = (e["stop_paying"] + e["hx_on_worker_share"] + e["pay_change"] + e["tax_on_pay_change"]
                         + e["contribution"] + e["self_employed"] + e["vat"])
                self.assertAlmostEqual(parts, e["net"], delta=4, msg=(k, e["name"]))
                self.assertAlmostEqual(-e["contribution"], e["rate1"] / 100 * e["base"] + e["rate2"] / 100
                                       * e["base2"], delta=1)

    def test_keys_sum_to_100(self):
        for k, (sh, _) in self.r["keys"].items():
            self.assertAlmostEqual(sum(sh), 100, delta=1e-6, msg=k)


if __name__ == "__main__":
    unittest.main()
