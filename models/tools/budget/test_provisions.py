#!/usr/bin/env python3
"""test_provisions.py: checks for the provision scoring library (piece B3).

Role: proves the library and the fiscal model are one model of the program, so B3 moves no
figure. Status: current. run-all.sh runs it right after the fiscal model (step 6a), because it reads
that run's build/ledger.json and build/fiscal-paths.csv. Standard library only.
Run from the repo root, after bash models/tools/run-all.sh:  python3 models/tools/budget/test_provisions.py

  1. The specs are well formed, one per ledger row (bills, revenue, options, dynamic), plus one
     per component of a split bill.
  2. Until B6, each spec's model fields equal the fiscal model's profile for that row
     (fiscal-profiles.csv, fiscal-components.csv), and the specs score exactly the rows the
     fiscal model scores.
  3. Every scored row's FY2030-39 total equals its ledger midpoint on both bases, to 1e-9 billion
     ($1; the only difference is floating-point summation, in practice under 1e-12 billion).
     This includes the climate rows, whose own check in the fiscal model allows $1 million.
  4. Every row's year-by-year path, FY2026-2056, on both bases, is the same floating-point
     number the fiscal model uses: exact equality, not a tolerance. So are the dynamic path,
     each scenario's program total and the composition by category.
  5. models/data/fiscal-paths.csv is the file this run wrote, the ledger headlines follow from
     the library's own totals, and every generated output is unchanged (run-all's drift check).
  6. The budget-concept paths behave: discretionary budget authority leads outlays, is never
     negative and adds up to lifetime outlays; budget authority splits into mandatory and
     discretionary; highway and transit contract authority (MOV-29, MOV-30) is mandatory budget
     authority equal to the transportation model's top-ups, with discretionary outlays, and the
     nondefense spend-out leaves transportation out; budget authority equals outlays where the spec says so; receipts are minus the
     deficit effect; views come from data.py.
  7. provisions.md is what provisions_report.py writes from the specs.
"""
import csv, importlib.util, json, os, sys, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.normpath(os.path.join(HERE, ".."))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
BUILD = os.environ.get("P2050_BUILD", os.path.join(ROOT, "build"))
sys.path.insert(0, HERE)
import data as D          # noqa: E402
import provisions as P    # noqa: E402
import provisions_report as R  # noqa: E402

LEDGER = os.path.join(BUILD, "ledger.json")
INPUTS = os.path.join(ROOT, "models", "data", "inputs")
EXACT = 1e-9


def rows(name):
    with open(os.path.join(INPUTS, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fiscal_model():
    if TOOLS not in sys.path:
        sys.path.insert(0, TOOLS)
    sp = importlib.util.spec_from_file_location("fiscal_model_b3", os.path.join(TOOLS, "fiscal-model.py"))
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


def setUpModule():
    if not os.path.exists(LEDGER):
        raise unittest.SkipTest("no build/ledger.json: run bash models/tools/run-all.sh first")
    global FM, M, S, SC, L
    FM = fiscal_model()
    M = FM.build(LEDGER, os.path.join(ROOT, "models", "data", "fiscal-baseline.csv"))
    S = P.specs()
    SC = P.score_all(LEDGER)
    L = json.load(open(LEDGER))


class Specs(unittest.TestCase):
    def test_well_formed(self):
        self.assertEqual(P.problems(S), [])

    def test_one_spec_per_ledger_row(self):
        want = ([("bill", b["id"]) for b in L["bills"]] +
                [("revenue", r["id"]) for r in L["revenue"]] +
                [("option", c["id"]) for c in L["cuts"]] +
                [("dynamic", d["id"]) for d in L["dynamic"]])
        table = {"bill": "bill", "base_revenue": "revenue", "revenue_option": "revenue",
                 "option": "option", "dynamic": "dynamic"}
        got = [(table[s["table"]], i) for i, s in S.items() if s["table"] != "component"]
        self.assertEqual(sorted(got), sorted(want))
        comps = [(r["owner"], r["component"]) for r in rows("fiscal-components.csv")]
        self.assertEqual(sorted((s["parent"], i.split("/", 1)[1]) for i, s in S.items() if s["table"] == "component"), sorted(comps))

    def test_model_fields_equal_the_profiles(self):
        """Until B6 the profiles stay canonical for the fiscal model; the specs must not drift."""
        defaults = dict(start=2030, ramp=1, grow="gdp", end=None, perm=1.0, fade=0.0)
        tbl = {"bill": "bill", "base_revenue": "base revenue", "option": "option"}
        prof = {(r["table"], r["id"]): r for r in rows("fiscal-profiles.csv")}
        n = 0
        for i, s in S.items():
            if s["table"] not in tbl or s["in_model"] != "yes":
                continue
            p = prof[(tbl[s["table"]], i)]
            self.assertEqual(s["category"], p["cat"], i)
            for k, sk in (("start", "start"), ("ramp", "ramp"), ("perm", "continues_after_2039"), ("fade", "fade")):
                want = P._num(p[k]) if p[k] else defaults[k]
                self.assertEqual(s[sk], want, "%s %s" % (i, k))
                self.assertEqual(type(s[sk]), type(want), "%s %s typed differently" % (i, k))
            self.assertEqual(s["indexation"], p["grow"] or "gdp", i)
            self.assertEqual(s["expiry_year"], P._num(p["end"]) if p["end"] else None, i)
            want_uni = "net_of_own_revenue" if i == "SS-1" else ("zero" if p["unified_zero"] == "yes" else "same")
            self.assertEqual(s["unified"], want_uni, i)
            n += 1
        self.assertGreater(n, 90)
        for c in rows("fiscal-components.csv"):
            s = S["%s/%s" % (c["owner"], c["component"])]
            for k, sk in (("start", "start"), ("ramp", "ramp"), ("perm", "continues_after_2039")):
                self.assertEqual(s[sk], P._num(c[k]))
            self.assertEqual((s["indexation"], s["category"]), (c["grow"], c["cat"]))

    def test_scores_exactly_the_rows_the_model_scores(self):
        model = {r["id"] for r in M["rows"]} | set(M["opt_rows"])
        lib = set(SC) - {"DYN"}
        self.assertEqual(lib, model)


class Calibration(unittest.TestCase):
    def test_window_totals_equal_ledger_midpoints(self):
        amounts = P.ledger_amounts(LEDGER)
        worst = 0.0
        for i, sc in SC.items():
            if i == "DYN":
                continue
            gf, uni = amounts[i]
            for basis, want in (("gf", gf), ("unified", uni)):
                err = abs(sum(sc[basis][y] for y in range(P.W0, P.W1 + 1)) - want * 1000)
                self.assertLessEqual(err, EXACT, "%s %s off by %g billion" % (i, basis, err))
                worst = max(worst, err)
        self.assertLess(worst, EXACT)

    def test_ledger_headlines_follow(self):
        claims = sum(P.window_total(SC[b["id"]]["gf"]) for b in L["bills"] if b["rail"] not in ("LATER", "T2"))
        self.assertEqual(round(claims, 2), L["summary"]["gf_claims"]["mid"])
        base = -sum(P.window_total(SC[r["id"]]["gf"]) for r in L["revenue"] if r["id"] in SC)
        self.assertEqual(round(base, 2), L["summary"]["base_revenue"]["mid"])


class SamePaths(unittest.TestCase):
    def test_every_row_path_is_the_models(self):
        model = {r["id"]: r for r in M["rows"]}
        model.update(M["opt_rows"])
        for i, r in model.items():
            for mb, lb in (("gf", "gf"), ("uni", "unified")):
                got = SC[i][lb]
                self.assertEqual(sorted(got), sorted(r[mb]), i)
                diff = [y for y in r[mb] if got[y] != r[mb][y]]
                self.assertEqual(diff, [], "%s %s differs in %s" % (i, mb, diff[:3]))
            self.assertEqual(SC[i]["category"], r["cat"], i)

    def test_dynamic_path_is_the_models(self):
        self.assertEqual(SC["DYN"]["unified"], M["dyn"])

    def test_scenario_program_totals(self):
        """Each scenario's program total, summed in the model's order, is the model's own."""
        order = [r["id"] for r in M["rows"]]
        for sid, label, opts, cfg in FM.SCENARIOS:
            if opts is None or cfg.get("envelope"):
                continue
            use = order + [o for o in opts if o in M["opt_rows"]]
            tot = {y: sum(SC[i]["unified"][y] for i in use) for y in range(P.Y0, P.Y1 + 1)}
            if cfg.get("dynamic"):
                for y in tot:
                    tot[y] += SC["DYN"]["unified"][y]
            self.assertEqual(tot, {y: M["results"][sid]["years"][y]["prog_primary"] for y in tot}, sid)

    def test_composition_by_category(self):
        """The model's all-of-government picture (DEC, % of GDP) from the library's paths."""
        B = M["B"]
        order = [r["id"] for r in M["rows"]] + [o for o in M["results"]["DEC"]["options"] if o in M["opt_rows"]]
        for y, comp in M["composition"]["DEC"].items():
            for k, want in comp.items():
                add = sum(SC[i]["unified"][y] for i in order if SC[i]["category"] == k)
                v = B[y][k] - add if k.startswith("rev_") else B[y][k] + add
                self.assertEqual(100 * v / B[y]["gdp"], want, "%s %d" % (k, y))

    def test_baseline_is_the_models(self):
        B = P.baseline()
        for y, r in M["B"].items():
            for k, v in r.items():
                if isinstance(v, float):
                    self.assertEqual(B[y][k], v, "%d %s" % (y, k))


class NoSilentMoves(unittest.TestCase):
    def test_fiscal_paths_unchanged(self):
        with open(os.path.join(BUILD, "fiscal-paths.csv")) as a, open(os.path.join(ROOT, "models", "data", "fiscal-paths.csv")) as b:
            self.assertEqual(a.read(), b.read(), "fiscal-paths.csv moved: a figure changed (tier 3, needs Espen)")

    def test_cpi_growth_is_the_models(self):
        self.assertEqual(P.CPI_RATE, FM.CPI)
        self.assertEqual((P.Y0, P.Y1, P.W0, P.W1), (FM.Y0, FM.Y1, FM.W0, FM.W1))


class BudgetConcepts(unittest.TestCase):
    def test_spendout_budget_authority(self):
        """Discretionary budget authority by spend-out: never negative where outlays are not, adds
        up to the same lifetime total as the outlays it covers (FY2026-56 plus the extension), and
        comes first. For contract-authority rows the outlays it covers are the non-contract share."""
        n = 0
        for i, sc in SC.items():
            if S.get(i, {}).get("budget_authority") not in ("spendout", "contract_authority"):
                continue
            ba = sc["ba_discretionary"]
            share = sc.get("contract_authority_share", 0.0)
            o = {y: (1 - share) * v for y, v in sc["outlays"].items()}
            self.assertTrue(sc["budget_authority_rough"])
            if all(v >= 0 for v in o.values()):
                self.assertTrue(all(v >= 0 for v in ba.values()), i)
            first_o = next((y for y in sorted(o) if o[y] != 0), None)
            if first_o is None:
                self.assertTrue(all(v == 0 for v in ba.values()), i)
                continue
            first_ba = next(y for y in sorted(ba) if ba[y] != 0)
            self.assertLess(first_ba, first_o, i)
            sh = P._spendout(S[i]["spendout_group"])
            g = o[P.Y1] / o[P.Y1 - 1] if o[P.Y1 - 1] else 1.0
            tail = sum(sh[k] * o[P.Y1] * g ** j
                       for j in range(1, len(sh)) for k in range(j, len(sh)))
            self.assertAlmostEqual(sum(ba.values()), sum(o.values()) + tail, places=6, msg=i)
            n += 1
        self.assertGreater(n, 20)

    def test_budget_authority_by_type_adds_up(self):
        for i, sc in SC.items():
            if sc["budget_authority"] is None:
                continue
            parts = [p for p in (sc["ba_mandatory"], sc["ba_discretionary"]) if p is not None]
            for y in range(P.Y0, P.Y1 + 1):
                self.assertEqual(sc["budget_authority"][y], sum(p[y] for p in parts), i)
            if sc["kind"] == "discretionary":
                self.assertIsNone(sc["ba_mandatory"], i)
            if sc["kind"] in ("mandatory", "transfer"):
                self.assertIsNone(sc["ba_discretionary"], i)

    def test_spendout_apply_inverts_a_flat_stream(self):
        flat = {y: 10.0 for y in range(P.Y0, P.Y1 + 1)}
        for g in ("defense", "nondefense"):
            back = P.spendout_apply(flat, g)
            self.assertAlmostEqual(back[2040], 10.0, places=12)

    def test_spendout_shares(self):
        for g in ("defense", "nondefense"):
            s = P._spendout(g)
            self.assertAlmostEqual(sum(s), 1.0, places=12)
            self.assertTrue(all(v >= 0 for v in s))

    def test_other_kinds(self):
        for i, sc in SC.items():
            k = sc["kind"]
            if k == "revenue":
                self.assertIsNone(sc["budget_authority"])
                self.assertEqual(sc["receipts"], {y: -v for y, v in sc["unified"].items()})
            elif i in S and S[i]["budget_authority"] == "outlays":
                self.assertEqual(sc["budget_authority"], sc["outlays"])
            elif i in S and S[i]["budget_authority"] in ("unknown", "on_enactment", "none"):
                self.assertIsNone(sc["budget_authority"], i)

    def test_views_use_data_layer(self):
        v = P.views(SC["CAP-7"]["unified"])
        self.assertEqual(v["real"], D.to_real(SC["CAP-7"]["unified"]))
        self.assertEqual(v["pct_gdp"], D.to_pct_gdp(SC["CAP-7"]["unified"]))

    def test_by_category_adds_up(self):
        cats = P.by_category(SC)
        for y in (2030, 2039, 2056):
            self.assertAlmostEqual(sum(c[y] for c in cats.values()),
                                   sum(sc["unified"][y] for i, sc in SC.items() if i != "DYN"), places=6)


class ContractAuthority(unittest.TestCase):
    """Highway and transit contract authority: mandatory budget authority, discretionary outlays."""

    def test_rows_and_amounts(self):
        ca = [i for i, s in S.items() if s["kind"] == "contract_authority"]
        self.assertEqual(sorted(ca), ["MOV-29", "MOV-30"])
        tu = P.transportation().Model().topups()
        want = {"MOV-29": {y: tu[y]["hwy"] + tu[y]["tra"] for y in (2032, 2033, 2034, 2035)},
                "MOV-30": {2036: tu[2036]["hwy"] + tu[2036]["tra"]}}
        for i in ca:
            sc = SC[i]
            self.assertEqual({y: v for y, v in sc["ba_mandatory"].items() if v}, want[i], i)
            self.assertEqual(sc["category"], "out_disc_nondefense", i)   # outlays stay discretionary
            self.assertAlmostEqual(sc["contract_authority_share"],
                                   sum(want[i].values()) / sum(sc["outlays"][y] for y in range(P.W0, P.W1 + 1)), places=12)
            self.assertTrue(0 < sc["contract_authority_share"] < 1, i)
        self.assertNotEqual(S["MOV-31"]["kind"], "contract_authority")

    def test_nondefense_spendout_leaves_out_transportation(self):
        groups = {s["spendout_group"] for s in S.values() if s["budget_authority"] in ("spendout", "contract_authority")}
        self.assertEqual(groups, {"defense", "nondefense_ex_transportation"})
        rows = [r for r in D.table("spendout-discretionary") if r["group"] == "nondefense_ex_transportation"]
        self.assertEqual(len(rows), 4)
        self.assertAlmostEqual(float(rows[0]["sum_of_shares"]), 1.0, places=2)

    def test_cbo_records_contract_authority_as_mandatory(self):
        """CBO's account file: the Highway Trust Fund accounts carry mandatory contract authority
        and discretionary outlays, with no discretionary budget authority, in every year."""
        rows = [r for r in D.table("cbo-contract-authority") if r["group"] == "highway_transit"]
        self.assertEqual(sorted(int(r["year"]) for r in rows), list(range(2026, 2037)))
        for r in rows:
            self.assertGreater(float(r["contract_authority"]), 70)
            self.assertGreater(float(r["outlays"]), 70)


class Report(unittest.TestCase):
    def test_report_is_current(self):
        with open(os.path.join(HERE, "provisions.md")) as f:
            self.assertEqual(f.read(), R.render(LEDGER), "provisions.md is stale: run provisions_report.py")


if __name__ == "__main__":
    unittest.main(verbosity=1)
