#!/usr/bin/env python3
"""Tests for the household model: accounting identities, hand-checked tax cases, the law's 2029 values, reproduction
of the Census's published SPM figures and of the legacy incidence model, and the typical families.

Role: the household model's test suite (`MODEL-CARD.md`, "Tests"). Status: working. Run from anywhere:
  python3 models/tools/household/test_household.py
The legacy-reproduction test needs the budget model's `ledger.json` and the legacy model's `incidence.json`; it looks
for them in $BUILD (run-all.sh sets it) or `build/`, and is skipped if they are absent.
"""
import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))

from budget import baseline  # noqa: E402
from distribution import assign  # noqa: E402
from families import FAMILIES, budget as family_budget, marginal_rates  # noqa: E402
from params import law, index_factor  # noqa: E402
from poverty import rates  # noqa: E402
import provisions as P  # noqa: E402
from rules import afa_child_benefit  # noqa: E402
from tax import unit_tax  # noqa: E402

ZERO = {k: 0 for k in ("age_s", "wage_s", "se_h", "se_s", "interest", "dividends", "rent", "capgain", "pension", "ss",
                       "ssi", "tanf", "uc", "vet", "disab_surv", "other", "child_support_rcvd", "dep_wages",
                       "dep_other_income", "n_dep", "n_dep_u6", "n_dep_6_16", "n_dep_17", "n_dep_18",
                       "n_dep_19_23_student", "n_dep_other")}


def unit(**kw):
    u = dict(ZERO, age_s=-1, filestat=5, age_h=30, wage_h=0)
    u.update(kw)
    return u


class TaxCases(unittest.TestCase):
    L = law(2025)

    def test_single_50k(self):
        t = unit_tax(unit(wage_h=50000), self.L)
        self.assertAlmostEqual(t["tax_before_credits"], 1192.5 + (50000 - 15750 - 11925) * 0.12, places=2)
        self.assertEqual(t["eitc"], 0)
        self.assertAlmostEqual(t["fica_ee"], 0.0765 * 50000, places=2)
        self.assertAlmostEqual(t["fica_er"], t["fica_ee"], places=2)

    def test_married_two_kids_30k(self):
        t = unit_tax(unit(filestat=1, age_s=30, wage_h=30000, n_dep=2, n_dep_6_16=2), self.L)
        self.assertEqual(t["fs"], "joint")
        self.assertAlmostEqual(t["eitc"], 7152, places=2)               # below the joint phase-out start, $30,470
        self.assertAlmostEqual(t["actc"], 3400, places=2)               # $1,700 a child binds
        self.assertAlmostEqual(t["income_tax"], -(7152 + 3400), places=2)

    def test_senior_social_security(self):
        t = unit_tax(unit(age_h=70, ss=30000, pension=20000), self.L)
        self.assertAlmostEqual(t["agi"], 20000 + 850 + 4500, places=2)  # sec. 86: 85% band starts at $34,000
        self.assertAlmostEqual(t["taxable_income"], 25350 - 15750 - 2000 - 6000, places=2)

    def test_ctc_phaseout_rounds_up(self):
        t = unit_tax(unit(wage_h=200001, n_dep=1, n_dep_6_16=1), self.L)
        self.assertAlmostEqual(t["ctc_nonref"], 2200 - 50, places=2)   # $1 over counts as a full $1,000

    def test_payroll_wage_base(self):
        t = unit_tax(unit(wage_h=300000), self.L)
        self.assertAlmostEqual(t["fica_er"], 0.062 * 176100 + 0.0145 * 300000, places=2)
        self.assertAlmostEqual(t["fica_ee"] - t["fica_er"], 0.009 * 100000, places=2)


class Law2029(unittest.TestCase):
    def test_values(self):
        L = law(2029)
        self.assertEqual((L["ctc"], L["ctc_refundable"]), (2400, 1800))   # CBO's own path: $2,400 and $1,900 in 2030
        self.assertEqual(L["senior_deduction"], 0)                         # expired after 2028
        self.assertEqual(L["std"]["single"], int(15750 * index_factor(2029) // 50) * 50)
        self.assertGreater(L["ss_wage_base"], 176100)


class Baseline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b25 = baseline(2025)
        cls.b29 = baseline(2029)

    def test_spm_identity_and_published_rates(self):
        for s in self.b25["spm"]:
            self.assertAlmostEqual(s["resources_census"], s["resources"], places=6)
        r = rates(self.b25["spm"], "resources")
        self.assertEqual(round(r["all"]["rate"], 1), 13.1)                 # P60-290, table 4
        self.assertEqual(round(r["children"]["rate"], 1), 13.4)
        self.assertEqual(round(r["65_plus"]["rate"], 1), 15.4)

    def test_model_taxes_close_to_census(self):
        us = self.b25["units"]
        e = sum(u["weight"] * u["t_eitc"] for u in us)
        c = sum(u["weight"] * u["c_eitc"] for u in us)
        self.assertLess(abs(e / c - 1), 0.05)
        m = rates(self.b25["spm"], "resources_model")["all"]["rate"]
        self.assertLess(abs(m - 13.11), 0.2)

    def test_household_accounting(self):
        for h in self.b29["households"][:2000]:
            nc = h["snap"] + h["housing"] + h["school_lunch"] + h["wic"] + h["energy"]
            self.assertAlmostEqual(h["net"], h["cash"] + nc - h["income_tax"] - (h["payroll"] - h["payroll_er"])
                                   - h["state_tax"], places=4)
        us = sum(u["weight"] * u["t_income_tax"] for u in self.b29["units"])
        hs = sum(h["weight"] * h["income_tax"] for h in self.b29["households"])
        self.assertLess(abs(us / hs - 1), 0.01)                             # unit and household weights agree

    def test_groups_equal_households(self):
        H = self.b29["households"]
        assign(H, "size_adjusted")
        tot = sum(h["weight"] for h in H)
        for g in range(1, 6):
            self.assertAlmostEqual(sum(h["weight"] for h in H if h["g5"] == g) / tot, 0.2, places=2)

    def test_micro_keys_sum_to_100(self):
        K, src = P.model_keys(self.b29)
        for k, (sh, t1) in K.items():
            self.assertAlmostEqual(sum(sh), 100, places=6, msg=k)
            if src[k] == "micro" and min(sh) >= 0:
                self.assertLessEqual(t1, sh[4] + 1e-9, msg=k)              # the top 1% sits inside Q5


class SnapLaw(unittest.TestCase):
    """P.L. 119-21's SNAP changes (snap2025.py, A-8)."""

    def test_source_year_untouched_and_2029_calibrated(self):
        import snap2025
        b25 = baseline(2025)
        self.assertFalse(b25["snap_law"]["applied"])
        self.assertTrue(all(s["snap"] == s["snap_prior_law"] for s in b25["spm"]))
        b = baseline(2029)
        sl = b["snap_law"]
        self.assertTrue(sl["applied"])
        for k, v in sl["probabilities"].items():
            self.assertTrue(0 < v <= 1, k)
        # the people losing benefits are CBO's 2.4 million as a share of USDA's participants, on the CPS's base
        cps_people = sum(s["w_people"] for s in b["spm"] if s["snap_prior_law"] > 0)
        share = sl["people_losing_m"] * 1e6 / cps_people
        self.assertAlmostEqual(share, 2.4e6 / snap2025.USDA_PARTICIPANTS_FY2025, delta=0.002)
        # CBO's sections imply about 7% (work rule) plus about 2.6% (energy, internet) of benefits
        self.assertTrue(8 <= sl["cut_pct"] <= 12, sl["cut_pct"])
        self.assertTrue(all(s["snap"] <= s["snap_prior_law"] + 1e-9 for s in b["spm"]))
        self.assertGreaterEqual(rates(b["spm"])["all"]["rate"],
                                rates(baseline(2029, snap_law=False)["spm"])["all"]["rate"])


class Rules(unittest.TestCase):
    def test_afa_no_earnings(self):
        L = law(2029)
        u = unit(filestat=4, n_dep=2, n_dep_u6=1, n_dep_6_16=1)
        u.update({"t_" + k: v for k, v in unit_tax(u, L).items()})
        gain = afa_child_benefit(u, L)
        self.assertEqual(u["t_ctc_total"], 0)                               # no earnings: no credit today
        self.assertGreater(gain, 12 * 300 * 2.2)                            # at least the 2024 amounts


class Families(unittest.TestCase):
    def test_single_parent_snap_and_eitc_band(self):
        r = {x["pct_poverty"]: x for x in marginal_rates(FAMILIES["single_parent_2"])}
        self.assertAlmostEqual(r[100]["snap"], 24.0, places=1)
        self.assertAlmostEqual(r[150]["income_tax"], 21.1 + 12 - 0.6, delta=1.0)
        self.assertAlmostEqual(r[300]["total"], 7.65 + 12, delta=0.1)

    def test_net_is_budget(self):
        b = family_budget(FAMILIES["single_adult"], 20000)
        self.assertAlmostEqual(b["net"], 20000 - b["payroll"] - b["income_tax"] + b["snap"], places=6)


class LegacyReproduction(unittest.TestCase):
    def test_legacy_figures(self):
        build = os.environ.get("BUILD", os.path.join(ROOT, "build"))
        led, inc = os.path.join(build, "ledger.json"), os.path.join(build, "incidence.json")
        if not (os.path.exists(led) and os.path.exists(inc)):
            self.skipTest("no ledger.json/incidence.json in BUILD; run models/tools/run-all.sh")
        legacy = json.load(open(inc))
        pkg, opts = P.rows(P.ledger_values(led))
        K = P.legacy_keys()
        for name, (o, drop) in P.scenarios().items():
            res = P.run(pkg, opts, o, drop, K)[0]
            for g in P.GROUPS + ["Q5x", "T1"]:
                self.assertEqual(res[g]["net"], legacy[name]["res"][g]["net"], msg=(name, g))


if __name__ == "__main__":
    unittest.main(verbosity=1)
