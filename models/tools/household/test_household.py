#!/usr/bin/env python3
"""Tests for the household model: accounting identities, hand-checked tax cases, the law's 2029 values, reproduction
of the Census's published SPM figures and of the legacy incidence model, and the typical families.

Role: the household model's test suite (`MODEL-CARD.md`, "Tests"). Status: working. Run from anywhere:
  python3 models/tools/household/test_household.py
The legacy-reproduction test needs the budget model's `ledger.json` and the legacy model's `incidence.json`; it looks
for them in $BUILD (run-all.sh sets it) or `build/`, and is skipped if they are absent. The other tests start from
`build/ledger.json` when it exists and otherwise from the committed snapshot (`snapshot/ledger.json`), so they run from a
fresh clone.
"""
import importlib.util
import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))

from budget import baseline  # noqa: E402
from distribution import assign  # noqa: E402
from families import (FAMILIES, budget as family_budget, care_charge, care_credit_rate, ceiling_check,  # noqa: E402
                      marginal_rates, plan_budget)
from params import law, index_factor  # noqa: E402
from poverty import rates  # noqa: E402
import provisions as P  # noqa: E402
from rules import (afa_child_benefit, cdctc_rate, cdctc_refundable, childless_eitc_2021, guarantee_charge,  # noqa: E402
                   inc1_childless_eitc, ssi_exclusions_indexed)
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


class SecureFloorRules(unittest.TestCase):
    """INC-1 to INC-4's rules (`rules.py`); INC-2 and INC-5 use household fields."""
    L = dict(law(2029), smi4=150000)

    def taxed(self, **kw):
        u = unit(**kw)
        u.update({"t_" + k: v for k, v in unit_tax(u, self.L).items()})
        return u

    def test_childless_credit_2021_design(self):
        from params import econ
        f = econ("cpiu", 2028) / 270.970
        self.assertAlmostEqual(childless_eitc_2021(self.L, 9820 * f, 9820 * f, "single", [30]), 1502.46 * f, delta=1)
        self.assertEqual(childless_eitc_2021(self.L, 8000, 8000, "single", [18]), 0)        # from age 19
        self.assertGreater(childless_eitc_2021(self.L, 8000, 8000, "single", [70]), 0)      # no upper limit
        self.assertEqual(childless_eitc_2021(self.L, 9820 * f, 9820 * f, "single", [30], invest=1e5), 0)

    def test_inc1_gain(self):
        u = self.taxed(age_h=40, wage_h=10000)
        self.assertGreater(inc1_childless_eitc(u, self.L), 0)
        self.assertGreater(u["t_eitc"], 0)                                   # today's credit, netted out
        kid = self.taxed(age_h=40, wage_h=10000, filestat=4, n_dep=1, n_dep_6_16=1)
        self.assertEqual(inc1_childless_eitc(kid, self.L), 0)                # families with children: unchanged

    def test_care_credit_rate(self):
        self.assertEqual(cdctc_rate(15000, "single"), 0.50)
        self.assertEqual(cdctc_rate(15001, "single"), 0.49)                  # each $2,000 or fraction
        self.assertEqual(cdctc_rate(60000, "single"), 0.35)
        self.assertEqual(cdctc_rate(80000, "single"), 0.32)
        self.assertEqual(cdctc_rate(160000, "joint"), 0.32)                  # $4,000 steps on joint returns
        self.assertEqual(cdctc_rate(10 ** 6, "joint"), 0.20)

    def test_guarantee_charge(self):
        self.assertEqual(guarantee_charge(0.85 * 150000, 4, 150000), 0)
        self.assertAlmostEqual(guarantee_charge(1.5 * 150000, 4, 150000), 0.07 * 225000)
        self.assertAlmostEqual(guarantee_charge(3 * 150000, 4, 150000), 0.07 * 450000)

    def test_care_credit_refundable_part(self):
        base = dict(age_h=30, wage_h=20000, filestat=4, n_dep=1, n_dep_6_16=1, n_dep_5_12=1, n_dep_u5=0,
                    n_people=2, childcare=4000)
        u = self.taxed(**base)
        self.assertAlmostEqual(cdctc_refundable(u, self.L), cdctc_rate(u["t_agi"], "hoh") * 3000
                               - u["t_tax_before_credits"], places=6)
        young = self.taxed(**dict(base, n_dep_6_16=0, n_dep_u6=1, n_dep_5_12=0, n_dep_u5=1))
        self.assertEqual(cdctc_refundable(young, self.L), 0)                 # the guarantee pays: free care

    def test_ssi_exclusions(self):
        u = unit(n_ssi=1, n_ssi_unearned=1, n_ssi_earn=0)
        e = unit(n_ssi=1, n_ssi_unearned=0, n_ssi_earn=1)
        self.assertEqual(ssi_exclusions_indexed(unit(n_ssi=1, n_ssi_unearned=0, n_ssi_earn=0), self.L), 0)
        self.assertAlmostEqual(ssi_exclusions_indexed(e, self.L) / ssi_exclusions_indexed(u, self.L), 52.5 / 20)

    def test_snap_cut_is_the_law(self):
        b = baseline(2029)
        cut = sum(h["weight"] * h["snap_cut"] for h in b["households"]) / 1e9
        sl = b["snap_law"]
        self.assertAlmostEqual(cut, sl["snap_prior_law_bn"] - sl["snap_bn"], delta=0.3)


class Families(unittest.TestCase):
    def test_single_parent_snap_and_eitc_band(self):
        r = {x["pct_poverty"]: x for x in marginal_rates(FAMILIES["single_parent_2"])}
        self.assertAlmostEqual(r[100]["snap"], 24.0, places=1)
        self.assertAlmostEqual(r[150]["income_tax"], 21.1 + 12 - 0.6, delta=1.0)
        self.assertAlmostEqual(r[300]["total"], 7.65 + 12, delta=0.1)

    def test_net_is_budget(self):
        b = family_budget(FAMILIES["single_adult"], 20000)
        self.assertAlmostEqual(b["net"], 20000 - b["payroll"] - b["income_tax"] + b["snap"], places=6)


class Ceiling(unittest.TestCase):
    """The 65-cent ceiling check (INC-5.02), every plan layer (`families.py`, `plan_budget`)."""

    def test_layers_add_up(self):
        f = FAMILIES["single_parent_2"]
        b = plan_budget(f, 70000, period="2030-34", marketplace=True, smi4=98693)
        self.assertAlmostEqual(b["net"], 70000 - b["payroll"] - b["income_tax"] + b["snap"] - b["ptc_contribution"]
                               - b["care"], places=6)
        self.assertAlmostEqual(b["payroll"], 0.0765 * 70000 + 0.003 * 70000, places=6)
        self.assertEqual(plan_budget(f, 70000, period="2035", marketplace=True)["ptc_contribution"], 0)

    def test_care_charge_and_credit(self):
        self.assertEqual(care_charge(0.85 * 0.84 * 100000, 3, 100000), 0)
        self.assertAlmostEqual(care_charge(1.5 * 100000, 4, 100000), 0.07 * 150000)
        self.assertEqual(care_credit_rate(80000, "hoh"), 0.32)

    def test_verdicts(self):
        rent = "2035 on, with a $1,400 rent in SNAP's shelter deduction | lowest-income state"
        # the decided set before INC-2.02 (SNAP's earned income deduction at 20%): the shelter case fails at 100%
        R = ceiling_check(98693, 160852, snap_earn_ded=0.20)
        sp = R["single_parent_2"]
        self.assertTrue(sp["2035 on, no shelter deduction | lowest-income state"]["pass"])
        self.assertFalse(sp[rent]["pass"])
        self.assertEqual((sp[rent]["at"], sp[rent]["max"]), (100, 75.0))
        self.assertTrue(R["single_adult"]["2035 on, no shelter deduction | lowest-income state"]["pass"])
        # with INC-2.02 at 45% (DEC-2026-11-13-03): every case meets the ceiling but one, the married couple on the
        # marketplace in 2030-34 with the rent (65.9 at 125%), which INC-5.02's monitoring rule covers
        R = ceiling_check(98693, 160852)
        fails = sorted((k, c.split(" | ")[0]) for k, v in R.items() for c, r in v.items()
                       if c.endswith("lowest-income state") and not r["pass"])
        self.assertEqual(fails, [("married_2", "2030-34 on the marketplace, with the rent")])
        m = R["married_2"]["2030-34 on the marketplace, with the rent | lowest-income state"]
        self.assertEqual((m["max"], m["at"]), (65.9, 125))
        self.assertEqual(R["single_parent_2"][rent]["max"], 55.5)
        self.assertEqual(R["married_2"][rent]["max"], 63.8)


class LegacyReproduction(unittest.TestCase):
    """`d3.py` replaced the legacy incidence model (M3 part 2). Its legacy version must give the legacy model's last
    results (frozen in `test-data/`) while the rows, keys, scenarios and ledger amounts are those it ran on."""

    def test_legacy_figures(self):
        import hashlib
        import d3
        build = os.environ.get("BUILD", os.path.join(ROOT, "build"))
        led = os.path.join(build, "ledger.json")
        if not os.path.exists(led):
            self.skipTest("no ledger.json in BUILD; run models/tools/run-all.sh")
        fx = json.load(open(os.path.join(HERE, "test-data", "legacy-incidence-2026-11-13.json")))
        inputs = os.path.join(ROOT, "models", "data", "inputs")
        same = all(hashlib.sha256(open(os.path.join(inputs, f), "rb").read()).hexdigest() == v
                   for f, v in fx["inputs_sha256"].items())
        same &= hashlib.sha256(json.dumps(P.ledger_values(led), sort_keys=True).encode()).hexdigest() == fx["ledger_sha256"]
        if not same:
            self.skipTest("the D3 inputs changed since the legacy model's last run; the frozen figures no longer apply")
        D = d3.D3.load(led)
        for name, (o, drop) in D.SCEN.items():
            res = D.run(o, drop)[0]
            self.assertEqual({g: v["net"] for g, v in res.items()}, fx["results"][name]["net"], msg=name)
            self.assertEqual(list(D.gf_test(o)), fx["results"][name]["gf"], msg=name)

    def test_year_profiles_sum_to_the_total(self):
        import d3
        led = P.default_ledger()      # build/ledger.json if there is one, else the committed snapshot
        D = d3.D3.load(led)
        for rid, label, side, amt, parts, basis in D.ROWS:
            if rid in ("C1P", "CB1", "CLIW", "CLIL", "E2d", "E1h") or not amt:
                continue                                              # the climate account's own paths
            self.assertAlmostEqual(sum(D.annual_fraction(rid, amt, y) for y in d3.YRS), amt, places=9, msg=rid)


class Intervals(unittest.TestCase):
    """The replicate-weight step (`intervals.py`) and its committed output, `intervals.json`."""

    @classmethod
    def setUpClass(cls):
        import intervals as IV
        cls.IV = IV
        cls.I = json.load(open(os.path.join(HERE, "intervals.json")))
        cls.b = baseline(2029)

    def test_sdr_formula(self):
        # every replicate 3 away from the base estimate: SE = sqrt(4/160 x 160 x 9) = 6
        self.assertAlmostEqual(self.IV.sdr(10.0, [13.0] * 80 + [7.0] * 80), 6.0)
        s = self.IV.summarize(10.0, 10.0, [13.0] * 160)
        self.assertAlmostEqual(s["hi90"] - s["value"], 1.645 * 6.0)

    @unittest.skipIf(importlib.util.find_spec("numpy") is None, "numpy is not installed")
    def test_groups_match_assign(self):
        import numpy as np
        hs = self.b["households"]
        assign(hs, "size_adjusted")
        W = np.array([[h["weight"]] for h in hs])
        G, T = self.IV.groups(np.array([h["size_adjusted"] for h in hs]), W)
        self.assertEqual(list(G[:, 0]), [h["g5"] for h in hs])
        self.assertEqual(list(T[:, 0]), [h["top1"] for h in hs])

    @unittest.skipIf(importlib.util.find_spec("numpy") is None, "numpy is not installed")
    def test_poverty_estimator_is_rates(self):
        import numpy as np
        spm = self.b["spm"]
        S = np.array([[s["weight"]] for s in spm])
        G = np.array([[[s[k]] for k in ("w_people", "w_children", "w_18_64", "w_65")] for s in spm])
        m = self.IV.poverty_metrics(self.b, S, G, "resources_model")
        r = rates(spm)
        for k in ("all", "children", "18_64", "65_plus"):
            self.assertAlmostEqual(float(m[f"rate_{k}"][0]), r[k]["rate"], places=9)

    def test_committed_intervals_are_complete_and_current(self):
        I = self.I
        self.assertEqual(I["persons_joined"], 134729)
        self.assertLess(I["max_base_weight_difference"], 0.01)
        for b in ("poverty_2025_census", "poverty_2025_model", "poverty_2029_model", "tax_rates_2029_d3",
                  "d3_net_per_household", "take_home"):
            self.assertIn(b, I["metrics"], b)
        for ms in I["metrics"].values():
            for m, v in ms.items():
                self.assertLessEqual(v["lo90"], v["value"], m)
                self.assertGreaterEqual(v["hi90"], v["value"], m)
        # the method's check: the Census's published 2025 margins are about 0.3 points (all) and 0.6 (children)
        p = I["metrics"]["poverty_2025_census"]
        self.assertTrue(0.2 < p["rate_all"]["half90"] < 0.4)
        self.assertTrue(0.4 < p["rate_children"]["half90"] < 0.8)
        # the household model's own outputs at the interval run are this model's (rerun intervals.py if this fails)
        r = rates(self.b["spm"])
        for k in ("all", "children", "18_64", "65_plus"):
            self.assertAlmostEqual(I["metrics"]["poverty_2029_model"][f"rate_{k}"]["value"], r[k]["rate"], places=2)
        from distribution import average_rates
        assign(self.b["households"], "size_adjusted")
        d = average_rates(self.b["households"])
        for g, lab in ((1, "Q1"), (4, "Q4"), ("T1", "T1")):
            self.assertAlmostEqual(I["metrics"]["tax_rates_2029_d3"][f"federal_rate_{lab}"]["value"],
                                   d[g]["federal_rate"], places=2)


class CBOConventions(unittest.TestCase):
    def test_steps(self):
        import conventions as C
        led = P.default_ledger()
        b = baseline(2029)
        hs = b["households"]
        assign(hs, "size_adjusted")
        out = C.steps(b, led)
        s0, s1 = out["steps"][0], out["steps"][1]
        self.assertEqual(s0["moved_from_d3_pct"], 0.0)
        # step 0 is D3 itself: its scenario Q equals the provision interface's (to rounding)
        KM, _ = P.model_keys(b)
        pkg, opts = P.rows(P.ledger_values(led))
        o, drop = P.scenarios()[out["scenario"]]
        ref = P.run(pkg, opts, o, drop, KM, P.mid_window_households(b), P.model_incomes(b))[0]
        for g in ("Q1", "Q4", "Q5"):
            # (each group's own household count against a fifth of all: they differ by a few households)
            self.assertLessEqual(abs(s0["net_q"][g] - ref[g]["net"]), max(2, 2e-4 * abs(ref[g]["net"])), g)
        # equal-people groups: each quintile about a fifth of people
        people = [s1["rates"][f"Q{q}"]["people_m"] for q in range(1, 6)]
        for p in people:
            self.assertAlmostEqual(p / sum(people), 0.2, delta=0.002)
        # the model's own groups are left as they were
        self.assertTrue(all("cg" not in h for h in hs))


class FrameAndFreshClone(unittest.TestCase):
    """Step H3: the parameter file, the ledger snapshot, the fetch script, the data boundary and the results header."""

    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, os.path.join(ROOT, "models", "schema"))
        sys.path.insert(0, os.path.join(ROOT, "models"))
        import parameters as PS
        cls.PS = PS
        cls.rows = PS.read(os.path.join(HERE, "parameters.csv"))

    def test_parameter_file_meets_the_schema(self):
        self.assertEqual(self.PS.validate(self.rows), [])

    def test_law_comes_from_the_parameter_file(self):
        import params
        n = sum(1 for r in self.rows if r["group"] == "law")
        flat = []
        def walk(v):
            if isinstance(v, dict):
                for x in v.values():
                    walk(x)
            elif isinstance(v, (list, tuple)):
                for x in v:
                    walk(x)
            else:
                flat.append(v)
        walk({k: v for k, v in params.LAW_2025.items() if k != "year"})
        self.assertEqual(len(flat), n)
        self.assertEqual(params.LAW_2025["std"]["joint"], 31500)
        self.assertEqual(params.LAW_2025["brackets"]["single"][0], 11925)
        self.assertEqual(params.LAW_2025["fpl"], (15650, 5500))
        self.assertEqual(params.constant("snap.usda_participants"), 42145499)

    def test_card_evidence_table_is_the_generated_one(self):
        card = open(os.path.join(HERE, "MODEL-CARD.md"), encoding="utf-8").read()
        a, b = card.index(self.PS.START) + len(self.PS.START), card.index(self.PS.END)
        self.assertEqual(card[a:b].strip(), self.PS.table(self.rows).strip(),
                         "the card's evidence table is stale: python3 models/schema/parameters.py "
                         "models/tools/household/parameters.csv --card models/tools/household/MODEL-CARD.md")

    def test_snapshot_matches_the_built_ledger(self):
        led = os.path.join(ROOT, "build", "ledger.json")
        if not os.path.exists(led):
            self.skipTest("no build/ledger.json")
        self.assertEqual(P.ledger_values(led), P.ledger_values(P.SNAPSHOT),
                         "the ledger changed: python3 models/tools/household/run.py --update-snapshot, then regenerate the results")

    def test_runs_from_the_snapshot_without_build(self):
        v = P.ledger_values(P.SNAPSHOT)
        self.assertGreater(len(v), 100)
        D = __import__("d3").D3.load(P.SNAPSHOT)
        self.assertTrue(D.SCEN)

    def test_no_import_of_the_health_cost_or_financing_scripts(self):
        import ast
        for f in sorted(os.listdir(HERE)):
            if not f.endswith(".py") or f.startswith("test_"):
                continue
            tree = ast.parse(open(os.path.join(HERE, f), encoding="utf-8").read())
            for node in ast.walk(tree):
                names = ([a.name for a in node.names] if isinstance(node, ast.Import)
                         else [node.module or ""] if isinstance(node, ast.ImportFrom) else [])
                for n in names:
                    self.assertFalse(n.split(".")[0].startswith("health_"), f"{f} imports {n}")

    def test_no_random_numbers(self):
        # the intervals are successive difference replication (deterministic); nothing here draws at random
        import re
        for f in sorted(os.listdir(HERE)):
            if f.endswith(".py") and not f.startswith("test_"):
                src = open(os.path.join(HERE, f), encoding="utf-8").read()
                self.assertIsNone(re.search(r"^\s*(import random|from random|import numpy\.random|np\.random)", src, re.M), f)

    def test_take_home_flags_match_the_extract(self):
        import csv
        import gzip
        with gzip.open(os.path.join(HERE, "take-home-flags.csv.gz"), "rt", newline="") as f:
            rows = list(csv.DictReader(f))
        units = baseline(2029)["units"]
        self.assertEqual(len(rows), len(units))
        for r in rows[:2000]:
            self.assertTrue(all(v in ("0", "1") for v in r.values()))

    def test_fetch_checks_the_hash(self):
        import hashlib
        import tempfile
        import fetch_cps
        with tempfile.TemporaryDirectory() as d:
            src = os.path.join(d, "a.zip")
            with open(src, "wb") as f:
                f.write(b"not the archive")
            good = hashlib.sha256(b"not the archive").hexdigest()
            out = fetch_cps.fetch(os.path.join(d, "ok"), "file://" + src, good)
            self.assertEqual(open(out, "rb").read(), b"not the archive")
            with self.assertRaises(SystemExit):
                fetch_cps.fetch(os.path.join(d, "bad"), "file://" + src, "0" * 64)
            self.assertEqual(os.listdir(os.path.join(d, "bad")), [])      # nothing kept from a bad download

    def test_committed_results_carry_the_header_and_current_code(self):
        import results as RS
        import runlog
        for f in ("results.json", "results.md"):
            self.assertEqual(RS.check_file(os.path.join(HERE, f)), [], f)
        h = json.load(open(os.path.join(HERE, "results.json")))["header"]
        self.assertEqual(h["model_id"], "MOD-household")
        for path, sha in {**h["code"], **h["inputs"]}.items():
            self.assertEqual(runlog.sha256_file(os.path.join(ROOT, path)), sha,
                             f"{path} changed since the results were written: rerun run.py and update the changelog")


# ---------------------------------------------------------------- the validation table (models/schema/validation.py)
CARD = os.path.join(HERE, "MODEL-CARD.md")
VSTART, VEND = "<!-- generated:validation:start -->", "<!-- generated:validation:end -->"
TPC_NOTE = ("TPC's expanded cash income adds what the CPS lacks (employer health and retirement contributions, retirement-account "
            "earnings, imputed corporate tax, SNAP): TPC's income is $29.0T against the model's $21.9T, so the same dollars sit over a "
            "larger denominator. In dollars the model's income tax is lower ($2.68T against $3.15T: the CPS top-codes and misses top "
            "incomes and gains) and its payroll tax higher ($2.16T against $1.89T: CPS earnings run above the national accounts' wages). "
            "The ordering and the progressivity match")


def validation_rows(results=None):
    """Every benchmark with the model's figure, from the committed results; targets and tolerances are fixed here."""
    import validation as V
    R = results or json.load(open(os.path.join(HERE, "results.json")))
    iv = json.load(open(os.path.join(HERE, "intervals.json")))["metrics"]["poverty_2025_model"]
    ag, pv = R["baseline_2025"]["aggregates"], R["baseline_2025"]["poverty"]["model"]
    tpc = R["baseline_2029"]["distribution_tpc"]
    out = []
    ev = lambda b, m: out.append(V.evaluate(b, m))
    pov_basis = "the 90% sampling half-interval of the model's own rate (intervals.json), which matches the Census's published margin (about 0.3 points for all people, 0.6 for children)"
    for key, name, target in (("all", "all people", 13.1), ("children", "children", 13.4), ("18_64", "adults 18-64", 12.3), ("65_plus", "people 65 and over", 15.4)):
        ev(V.Benchmark(f"HH-P-{key}", f"SPM poverty rate, 2025, the model's own taxes: {name}", target, "SRC-3602",
                       "Census P60-290, table 8 (2025)", "percent", tolerance=round(iv[f"rate_{key}"]["half90"], 2), tolerance_kind="absolute",
                       tolerance_basis=pov_basis,
                       explanation="The model rebuilds the Census's resources from its elements exactly with Census taxes (tested); with its own taxes the difference is its slightly higher income tax (no itemized deductions, A-7)."),
           pv[key]["rate"])
    same = "the model applies the Census tax model's rules to the same records, so it should land within a few percent; 5%, a round band"
    ev(V.Benchmark("HH-T-eitc", "Earned income credit, 2025 law", ag["census_eitc_bn"], "SRC-3600", "Census tax model on the same CPS records", "$ billion",
                   0.05, "relative", same, explanation="Follows the Census on the same records."), ag["eitc_bn"])
    ev(V.Benchmark("HH-T-ctc", "Child and other-dependent credits, refundable and not, 2025 law", ag["census_ctc_bn"] + 0.0, "SRC-3600", "Census tax model on the same CPS records", "$ billion",
                   0.05, "relative", same, explanation="Follows the Census on the same records."), ag["ctc_bn"])
    ev(V.Benchmark("HH-T-agi", "Adjusted gross income, 2025", ag["census_agi_bn"], "SRC-3600", "Census tax model on the same CPS records", "$ billion",
                   0.05, "relative", same, explanation="About 1 percent below."), ag["agi_bn"])
    ev(V.Benchmark("HH-T-tax", "Income tax after credits, 2025 law", ag["census_income_tax_bn"], "SRC-3600", "Census tax model on the same CPS records", "$ billion",
                   0.05, "relative", same,
                   explanation="The model's income tax is about 9% above the Census's, most of it in the top quintile: the CPS microdata has no itemized deductions, AMT or the dependent care, education, saver's and premium credits (A-7), which the Census's own model imputes."),
       ag["income_tax_bn"])
    soi = "https://www.irs.gov/pub/irs-soi/23in25ic.xls; https://www.irs.gov/pub/irs-soi/23in33ar.xls"
    ev(V.Benchmark("HH-S-eitc", "Earned income credit, 2025 law, against IRS returns", 66.27, soi, "IRS SOI, tax year 2023, all returns (2023 law)", "$ billion",
                   0.10, "relative", "10%: a different tax year and law, and a survey against administrative records",
                   explanation="The CPS under-reports low and self-employment earnings and family links, and the IRS total includes claims its own compliance studies find improper; the model follows the Census on the same records. Cited, not run: fetch_public.py cannot read the legacy .xls."),
       ag["eitc_bn"])
    ev(V.Benchmark("HH-S-ctc", "Child and other-dependent credits, total, 2025 law, against IRS returns", 84.42 + 34.53, soi, "IRS SOI, tax year 2023 ($2,000 credit)", "$ billion",
                   0.10, "relative", "10%: a different tax year and credit amount ($2,000 against 2025's $2,200)",
                   explanation="About 1% above SOI on a credit that is 10% larger per child; the refundable part is $11B lower (the low-earnings under-reporting again)."),
       ag["ctc_bn"])
    ev(V.Benchmark("HH-S-actc", "Refundable child credit, 2025 law, against IRS returns", 34.53, soi, "IRS SOI, tax year 2023", "$ billion",
                   0.10, "relative", "10%: a different tax year and credit amount",
                   explanation="The CPS under-reports the low earnings that drive the refundable part."), ag["actc_bn"])
    for g, lab in (("1", "Q1"), ("2", "Q2"), ("3", "Q3"), ("4", "Q4"), ("5", "Q5"), ("T1", "top 1%")):
        t_inc, t_pay = {1: (-3.66, 6.08), 2: (-0.07, 7.70), 3: (4.52, 7.69), 4: (7.71, 7.90), 5: (16.16, 5.52), "T1": (23.33, 2.13)}[int(g) if g.isdigit() else g]
        for kind, target, field in (("income tax", t_inc, "income_tax_rate"), ("payroll tax", t_pay, "payroll_rate")):
            ev(V.Benchmark(f"HH-TPC-{g}-{'i' if kind[0] == 'i' else 'p'}", f"Average federal {kind} rate, 2029, {lab} (tax units, quintiles of equal numbers of people)", target, "SRC-4801",
                           "TPC T26-0045 (June 2026), current law with P.L. 119-21, percent of expanded cash income", "percent", 1.0, "absolute",
                           "one percentage point, a round band set before the comparison; TPC publishes no error band",
                           explanation=TPC_NOTE), tpc[g][field])
    return out


def validation_block(results=None):
    import validation as V
    return VSTART + "\n" + V.render(validation_rows(results)) + "\n" + VEND


def write_validation():
    s = open(CARD, encoding="utf-8").read()
    a, b = s.index(VSTART), s.index(VEND) + len(VEND)
    open(CARD, "w", encoding="utf-8").write(s[:a] + validation_block() + s[b:])


class ValidationTable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, os.path.join(ROOT, "models", "schema"))

    def test_no_problems(self):
        import validation as V
        self.assertEqual(V.problems(validation_rows()), [])

    def test_card_table_is_the_one_the_code_renders(self):
        self.assertIn(validation_block(), open(CARD, encoding="utf-8").read(),
                      "the card's validation table is stale: python3 models/tools/household/test_household.py --write-validation")


if __name__ == "__main__":
    if "--write-validation" in sys.argv:
        sys.path.insert(0, os.path.join(ROOT, "models", "schema"))
        write_validation()
        print("wrote the validation table into MODEL-CARD.md")
    else:
        unittest.main(verbosity=1)
