"""Tests for `health_cost_review.py`: the rebuild reproduces the model, each correction is what it says, and every
package's sources add up to its gross cost, and the unified health contribution (part 3) is built as specified.

Role: checks the arithmetic of `dossiers/foundations/health-cost-review.md`. Status: exploratory analysis's test,
November 15, 2026. Run: `python3 models/tools/test_health_cost_review.py` (about three minutes).
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))   # the shared readers (step H4 move)
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


class Unified(unittest.TestCase):
    """Part 3: the unified contribution, built in the tool (not monkeypatched)."""
    @classmethod
    def setUpClass(cls):
        cls.ctx = HF.context()
        cls.case = CR.cost_cases(CR._g40())["design"]
        CR._setup_visible(cls.ctx)
        cls.u3 = CR.unified_spec(3.0)
        # the lead's X3 (dossiers/foundations/notes/variants-2026-11-15/outX.json) on its own conventions
        cls.x3 = CR.unified_row(cls.ctx, cls.case, cls.u3, basis="hf", part_b=False, others=False)

    def test_exemption_shape(self):
        u = self.u3
        F = CR.poverty(1)
        self.assertEqual(CR.unified_charge(1.38 * F, "single", 1, u), 0.0)
        self.assertAlmostEqual(CR.unified_charge(2.0 * F, "single", 1, u), 0.03 * 2.0 * F, places=6)   # no cliff
        self.assertAlmostEqual(CR.unified_charge(2.0 * F - 1e-3, "single", 1, u), 0.03 * 2.0 * F, delta=0.01)
        self.assertAlmostEqual(CR.unified_charge(60000, "single", 1, u), 1800.0, places=6)
        top = CR.unified_charge(300000, "single", 1, u)
        self.assertAlmostEqual(top, 9000 + 0.05 * (300000 - 205400), places=6)
        for form in ("quadratic", "linear"):
            v = CR.unified_spec(3.0, form=form)
            lo, hi = CR.exemption_marginal(v)
            d = lambda x: (CR.unified_charge(x * F + 1, "single", 1, v) - CR.unified_charge(x * F, "single", 1, v)) \
                * 100  # noqa: E731
            self.assertAlmostEqual(d(1.3801), lo, delta=0.01)
            self.assertAlmostEqual(d(1.9999), hi, delta=0.01)
        self.assertAlmostEqual(CR.exemption_marginal(u)[0], 6.68, places=2)    # the brief's "about 6.7-12.7%"
        self.assertAlmostEqual(CR.exemption_marginal(u)[1], 12.68, places=2)

    def test_reproduces_x3(self):
        r = self.x3
        self.assertAlmostEqual(r["reassigned"] - r["lost"]["H1b"], 308.06, delta=0.05)   # X3 kept H1b whole
        self.assertAlmostEqual(r["pass_all"], 78.66, delta=0.01)
        self.assertAlmostEqual(r["pass_below_200"], 98.55, delta=0.01)
        self.assertAlmostEqual(r["exemption_cost_bn"], 18.99, delta=0.01)
        self.assertAlmostEqual(r["T"]["plan"], 3514.1, delta=0.5)
        self.assertAlmostEqual(r["T"]["today"], 6692.3, delta=0.5)
        self.assertAlmostEqual(r["lost"]["total"] - r["lost"]["H1b"], 359.36, delta=0.05)

    def test_booked_revenue_adds_up(self):
        o = CR.unified_package(self.ctx, self.case, self.u3, basis="hf")
        self.assertAlmostEqual(o["reassigned"], o["remainder_F"] + o["lost"]["total"] - o["household_collected"],
                               places=6)
        self.assertAlmostEqual(o["household_collected"], o["statutory"] * 0.8, places=6)
        # CBO's payroll raises the lost worker HI and so the booked revenue taken, one for one
        oc = CR.unified_package(self.ctx, self.case, self.u3, basis="cbo")
        self.assertAlmostEqual(oc["reassigned"] - o["reassigned"], oc["lost"]["W"] - o["lost"]["W"], places=6)

    def test_worker_hi_bases(self):
        hf, cbo, mi = (CR.worker_hi_bn(self.ctx, b) for b in ("hf", "cbo", "micro"))
        self.assertAlmostEqual(hf, 289.76, delta=0.05)
        self.assertGreater(cbo, hf)
        self.assertLess(cbo, mi)

    def test_cbo_payroll_matches_the_library(self):
        path = os.path.join(CR.ROOT, "library", "text", "cbo-2026-long-term-social-security-projections-workbook.txt")
        lines = open(path, encoding="utf-8").read().splitlines()
        start = next(i for i, x in enumerate(lines) if x.endswith("= Taxable payroll"))      # table 2's header
        for y, v in CR.CBO_TAXABLE_PAYROLL.items():
            i = next(i for i in range(start, len(lines)) if lines[i].endswith(f"= {y}"))
            self.assertAlmostEqual(float(lines[i + 2].split("= ")[1]), v, places=3)

    def test_take_home_counts_hi_on_both_sides_for_e(self):
        oE = CR.health_package(self.ctx, self.case, CR.PACKAGES2["E"][2])
        T = CR.household_T(self.ctx, oE)
        self.assertAlmostEqual(T["today_hi"], T["plan_hi"], places=6)        # E keeps HI: the same on both sides
        self.assertAlmostEqual(T["plan_without_hi"], 1371, delta=1)          # the README's like-for-like note
        self.assertAlmostEqual(T["today"], 6692.3, delta=0.5)

    def test_lower_rate_more_pass_more_booked_revenue(self):
        a = CR.unified_package(self.ctx, self.case, CR.unified_spec(2.5))
        b = CR.unified_package(self.ctx, self.case, self.u3)
        self.assertGreater(a["reassigned"], b["reassigned"])
        self.assertGreater(CR.take_home_micro(self.ctx, a)["all"], CR.take_home_micro(self.ctx, b)["all"])

    def test_h1b_folded_into_s_wins_back_its_wage_half(self):
        fold = CR.h1b_restated(self.ctx)["fold_into_s_points"]
        a = CR.unified_package(self.ctx, self.case, self.u3)                              # S = 5, H1b lost
        b = CR.unified_package(self.ctx, self.case, CR.unified_spec(3.0, S=5.0 + fold))  # H1b folded into S
        L = a["lost"]
        # the fold-in's total carries H1b's wage half on top of HI, the 0.9% and HI on former premiums
        self.assertAlmostEqual(L["total"] - (L["W"] + L["A"] + L["hxp"]), CR.h1b_restated(self.ctx)["wage_half"],
                               places=6)
        self.assertGreater(L["H1b"], 40.0)
        # with H1b folded into S, booked revenue taken is what S = 5 takes when H1b is kept whole (pinned to the
        # pieces, not to the total, so dropping the wage half from the total fails here)
        self.assertAlmostEqual(b["reassigned"], a["remainder_F"] + L["W"] + L["A"] + L["hxp"]
                               - a["household_collected"], places=6)

    def test_h1b_restatement_keeps_its_yield(self):
        h = CR.h1b_restated(self.ctx)
        self.assertGreater(h["wage_share"], 0.3)
        self.assertLess(h["wage_share"], 0.95)
        one = dict(R=0.0, S=0.0, lo=0.0, hi=1e-9, form="quadratic")
        got = CR.unified_statutory_bn(self.ctx, dict(one, h1b=h["own_step_points"]), "h1b") * 0.8
        self.assertAlmostEqual(got, h["wage_half"], places=6)


if __name__ == "__main__":
    unittest.main()
