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
                self.assertAlmostEqual(got, o["need"] + o["hi"] + o["hi_tax"] + o["credit_bn"], delta=0.5,
                                       msg=(grp, k))
                # the household rows' collections equal household_collected
                hh_rows = [bn for lb, bn, _ in o["rows"][o["n_fixed_rows"]:]]
                self.assertAlmostEqual(-sum(hh_rows), o["household_collected"], delta=0.5, msg=(grp, k))

    def test_package_paths_close_each_year_and_end_at_fy2040(self):
        for k, path in self.r["package_paths"].items():
            o = self.r["packages"][k]
            for y, d in path.items():
                self.assertAlmostEqual(d["employers"] + d["states"] + d["savings"] + d["households"],
                                       d["need"] + d["hi"] + d["hi_tax"] + d["credit"], delta=0.01)
            self.assertAlmostEqual(path[2040]["first"], o["first"], delta=1e-6)
            self.assertAlmostEqual(path[2040]["vat"], o["vat_rate"], delta=1e-6)

    def test_rates_multiply_out(self):
        """The middle fifth's first-tier charge is the rate times its base (the reader's multiplication)."""
        a, b = self.r["packages"]["A"], self.r["base_2040"]
        q3 = [d for d in a["detail"] if d[0] == "First tier: the statutory charge"][0][2]["Q3"]
        self.assertAlmostEqual(-q3, a["first"] / 100 * b["per_household"]["Q3"], delta=2)
        self.assertLess(abs(b["cps_grown_bn"] / b["statutory_bn"] - 1), 0.05)
        # the employer contribution: former premiums (all employers) plus the repealed HI tax, over its base
        S = self.r["sensitivities"]
        self.assertAlmostEqual(a["employer_rate"] * HF.band_share(), 11.87, delta=0.01)
        self.assertAlmostEqual(S["A_hi_folded"]["employer_rate"] * HF.band_share(), 11.87 + HF.HI_RATE, delta=0.01)
        self.assertAlmostEqual(S["A_employer_uncapped"]["employer_rate"], 11.87, delta=0.01)
        self.assertAlmostEqual(HF.TOP_RATE_BEFORE_HEALTH, 63.0)

    def test_whole_system_sources_add_to_the_gross_cost(self):
        """Every package's sources (federal general revenue already spent, states, employers, households, HX's
        remainder, savings) add to the system's gross cost, in FY2040 and in every year of package A's path."""
        for k, v in self.r["views"].items():
            self.assertAlmostEqual(v["check"], 0.0, delta=0.01, msg=k)
        for y, v in self.r["path_views"].items():
            self.assertAlmostEqual(v["check"], 0.0, delta=0.01, msg=y)
            self.assertGreaterEqual(v["sources"]["federal_general_revenue"], 0.0)
        self.assertAlmostEqual(self.r["views"]["A"]["gross"], 8407, delta=5)

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
                parts = (e["stop_paying"] + e["hx_on_worker_share"] + e["worker_hi_ends"] + e["pay_change"]
                         + e["tax_on_pay_change"]
                         + e["contribution"] + e["self_employed"] + e["vat"] + e["credit"])
                self.assertAlmostEqual(parts, e["net"], delta=4, msg=(k, e["name"]))
                self.assertAlmostEqual(-e["contribution"], e["rate1"] / 100 * e["base"] + e["rate2"] / 100
                                       * e["base2"], delta=1)

    def test_the_fix_cuts_the_losers_and_protects_the_hardest_case(self):
        """Package A with the phase-in and the worker transition credit: fewer bottom-four households lose cash, and
        far fewer lose more than 5%; the $45,000 worker whose employer offered no coverage no longer loses."""
        m, before = self.r["micro"]["A"], self.r["micro"]["A_before_fix"]
        self.assertLess(m["bottom_four_losers_m"], before["bottom_four_losers_m"] - 3)
        self.assertLess(m["bottom_four_lose_5pct_m"], 0.6 * before["bottom_four_lose_5pct_m"])
        self.assertLess(sum(m[q]["lose_5pct_m"] for q in ("Q1", "Q2", "Q3")), 1.0)
        ex = {e["name"]: e for e in self.r["examples"]["A"]}
        u = [e for n, e in ex.items() if "no coverage" in n][0]
        self.assertGreaterEqual(u["net"], 0)
        self.assertLess([e for e in self.r["examples"]["A_before_fix"] if "no coverage" in e["name"]][0]["net"], -3000)
        # the credit is the contribution charged on that worker's pay (phased in at FY2040's share), in full
        self.assertAlmostEqual(u["credit"], u["employer_pays"], delta=1)
        self.assertAlmostEqual(u["employer_pays"], (1 - HF.phase_left(2040)) * u["employer_base"]
                               * self.r["packages"]["A"]["employer_rate"] / 100, delta=1)

    def test_phase_in_and_credit_are_priced_into_the_rate(self):
        a, b = self.r["packages"]["A"], self.r["sensitivities"]["A_before_fix"]
        pp = b["household_collected"] / b["first"]      # a point's yield on the widened base (memo part 2.1, item 3)
        self.assertAlmostEqual(HF.phase_left(2035), 0.9)
        self.assertAlmostEqual(HF.phase_left(2040), 0.425)
        self.assertAlmostEqual(a["phase_in_bn"], 0.425 * a["no_offer_share"] * a["employer_premium_part"], delta=0.01)
        cost = a["phase_in_bn"] * (1 - self.r["tau"]) + a["credit_bn"]
        self.assertAlmostEqual((a["first"] - b["first"]) * pp, cost, delta=0.03 * cost)
        no = self.r["no_offer"]
        self.assertAlmostEqual(no["share"], no["target"], delta=0.1 * no["target"])

    def test_employer_split_and_pay_holds(self):
        """The pass-through rule's pay rises owed less the restraint the wage rule leaves to future raises equals the
        premiums that become pay less the contribution charged; if pay holds, the household rate falls."""
        a, sp = self.r["packages"]["A"], self.r["employer_split"]
        self.assertAlmostEqual(sp["owed_bn"] - sp["restraint_bn"], a["employer_premium_part"] - a["employer_gross"],
                               delta=1.0)
        self.assertLess(self.r["pay_holds"]["first"], a["first"])
        self.assertLess(self.r["pay_holds"]["micro"]["bottom_four_losers_m"], self.r["micro"]["A"]["bottom_four_losers_m"])
        k = self.r["savings_kept"]
        self.assertAlmostEqual(k["kept_bn"], 0.5 * sp["owed_bn"], delta=0.01)
        self.assertGreater(k["first"], a["first"])
        self.assertGreater(k["micro"]["bottom_four_losers_m"], self.r["micro"]["A"]["bottom_four_losers_m"])

    def test_physician_rate_correction(self):
        """Memo part 1.2b: physician and other non-hospital claims at the decided rate lower FY2040's cost."""
        ph = self.r["physician_rate"]
        self.assertAlmostEqual(ph[1.05], -275, delta=5)
        self.assertLess(ph[1.0], ph[1.05])
        self.assertLess(ph[1.05], ph[1.10])
        self.assertLess(ph[1.10], 0)

    def test_keys_sum_to_100(self):
        for k, (sh, _) in self.r["keys"].items():
            self.assertAlmostEqual(sum(sh), 100, delta=1e-6, msg=k)


if __name__ == "__main__":
    unittest.main()
