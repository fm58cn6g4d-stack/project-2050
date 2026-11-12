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
     discretionary; no ledger row is contract authority (Moving America's top-ups are general-fund
     appropriations); the spend-out shares are B2's CBO-calibrated ones as stored, and with the zero-budget-authority
     accounts carried on their own they rebuild CBO's discretionary outlays within 2%; budget authority equals outlays where the spec says so; receipts are minus the
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


class SharedScenarios(unittest.TestCase):
    """B6's shared scenario file (models/data/inputs/scenarios.json): one home for the decided package and its
    variants, read by the fiscal model and the incidence model."""

    def test_both_models_read_one_decided_package(self):
        sp = importlib.util.spec_from_file_location("scenarios_b6", os.path.join(TOOLS, "scenarios.py"))
        SF = importlib.util.module_from_spec(sp)
        sp.loader.exec_module(SF)
        doc = SF.load()
        self.assertEqual(FM.SCENARIOS, SF.fiscal(doc))
        self.assertEqual(FM.DEC, SF.package("DEC", doc))
        q = next(x for x in doc["incidence"] if x["id"] == "Q")
        self.assertEqual(SF.options(q, doc), FM.DEC)          # incidence scenario Q is the fiscal model's DEC
        dec = next(x for x in doc["fiscal"] if x["id"] == "DEC")
        self.assertEqual(SF.options(dec, doc), SF.options(q, doc))
        cuts = {c["id"] for c in L["cuts"]}
        for sid, _, opts, _ in FM.SCENARIOS:
            self.assertTrue(set(opts or []) <= cuts, sid)    # every fiscal option is a ledger option


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
            # Optional columns: end and fade (blank or absent means none).
            self.assertEqual(s["expiry_year"], P._num(c["end"]) if c.get("end") else None)
            self.assertEqual(s["fade"], P._num(c["fade"]) if c.get("fade") else 0.0)
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
        """Discretionary budget authority by spend-out: never negative where outlays are not, spends
        out to the same lifetime total as the outlays it covers (FY2026-56 plus the extension), and
        comes first."""
        n = 0
        for i, sc in SC.items():
            if S.get(i, {}).get("budget_authority") != "spendout":
                continue
            ba = sc["ba_discretionary"]
            o = sc["outlays"]
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
            tot = sum(sh)
            g = o[P.Y1] / o[P.Y1 - 1] if o[P.Y1 - 1] else 1.0
            tail = sum(sh[k] * o[P.Y1] * g ** j
                       for j in range(1, len(sh)) for k in range(j, len(sh)))
            # spent out at the shares (sum tot), the budget authority gives back lifetime outlays
            self.assertAlmostEqual(sum(ba.values()) * tot ** 2, tot * sum(o.values()) + tail, places=6, msg=i)
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
            self.assertAlmostEqual(back[2040], 10.0 * sum(P._spendout(g)), places=12)

    def test_spendout_shares_are_b2s_as_stored(self):
        """No rescaling: the shares are spendout-discretionary-cbo.csv's, whose sums are within 2%
        of one once ground transportation is out of nondefense."""
        for g in ("defense", "nondefense"):
            rows = sorted((r for r in D.table("spendout-discretionary-cbo") if r["group"] == g),
                          key=lambda r: int(r["year_of_spending"]))
            self.assertEqual(P._spendout(g), [float(r["share"]) for r in rows])
            self.assertAlmostEqual(sum(P._spendout(g)), 1.0, delta=0.02)
            self.assertAlmostEqual(float(rows[0]["scale"]), 1.0, delta=0.01)

    def test_rebuilds_cbo_discretionary_outlays(self):
        """CBO's projected discretionary budget authority, spent out at the library's shares, plus
        the nondefense accounts with no discretionary budget authority, gives CBO's projected
        outlays within 2% in every year FY2029-36 (the gap B4 found at -11% is closed)."""
        for g in ("defense", "nondefense"):
            for y, (got, want) in P.cbo_discretionary_outlays(g).items():
                self.assertLess(abs(got / want - 1), 0.02, "%s FY%d: %.1f vs %.1f" % (g, y, got, want))

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


class Splits(unittest.TestCase):
    """Board 0d (Espen, November 8, 2026): a program may carry a mandatory or advance-appropriation
    part in reconciliation and a regular-appropriations part. The split method scores each part
    in its own category. No ledger row is split yet; this checks the format on a made-up row."""

    def setUp(self):
        import tempfile
        base = dict(S["EDU-4"])
        self.S = dict(S)
        self.S["X-1"] = dict(base, id="X-1", method="split", kind="mandatory", vehicle="reconciliation")
        self.S["X-1/a"] = dict(base, id="X-1/a", table="part", parent="X-1", method="profile", kind="mandatory",
                               category="out_other_mandatory", vehicle="reconciliation", budget_authority="outlays")
        self.S["X-1/b"] = dict(base, id="X-1/b", table="part", parent="X-1", method="profile", kind="discretionary",
                               category="out_disc_nondefense", vehicle="regular_appropriations",
                               budget_authority="spendout", spendout_group="nondefense")
        self.tmp = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False)
        self.tmp.write("parent,part,share,source\nX-1,X-1/a,0.7,test\nX-1,X-1/b,0.3,test\n")
        self.tmp.close()
        self.saved, P.SPLITS = P.SPLITS, self.tmp.name

    def tearDown(self):
        P.SPLITS = self.saved
        os.unlink(self.tmp.name)

    def test_parts_add_to_the_whole_and_land_in_their_own_categories(self):
        sc = P.score(self.S["X-1"], {"X-1": (0.10, 0.10)}, self.S)
        self.assertAlmostEqual(P.window_total(sc["unified"]), 0.10, places=12)
        a, b = sc["parts"]
        self.assertAlmostEqual(P.window_total(a["unified"]), 0.07, places=12)
        self.assertAlmostEqual(P.window_total(b["unified"]), 0.03, places=12)
        cats = P.by_category({"X-1": sc})
        self.assertEqual(set(cats), {"out_other_mandatory", "out_disc_nondefense"})
        self.assertEqual(cats["out_disc_nondefense"], b["unified"])
        self.assertIsNone(a["ba_discretionary"])          # the mandatory part: budget authority equals outlays
        self.assertEqual(a["ba_mandatory"], a["outlays"])
        self.assertIsNotNone(b["ba_discretionary"])       # the appropriated part spends out
        self.assertTrue(sc["budget_authority_rough"])
        self.assertEqual(P.deficit_path(self.S["X-1"], 0.10, self.S), sc["unified"])

    def test_format_errors(self):
        self.assertEqual(P.split_problems(self.S), [])
        bad = dict(self.S)
        bad["X-1/b"] = dict(bad["X-1/b"], vehicle="reconciliation")
        self.assertTrue(any("must each fit their vehicle" in e for e in P.split_problems(bad)))
        self.assertTrue(any("add to" in e for e in P.split_problems(self.S, {"X-1": [("X-1/a", 0.7), ("X-1/b", 0.2)]})))
        self.assertTrue(any("no parts" in e for e in P.split_problems(self.S, {})))

    def test_vehicle_flags_are_the_known_rows(self):
        """The rows whose vehicle and kind disagree are flagged as design choices, not rebooked."""
        flagged = {i for i, _ in P.vehicle_flags(S)}
        self.assertEqual(flagged, {"EDU-4", "LAB-8", "NSC-10", "MOV-29", "DEM-17", "SAF-10", "MOV-30"})


class ContractAuthority(unittest.TestCase):
    """Highway, transit and airport contract authority: in CBO's baseline, not in the ledger."""

    def test_no_ledger_row_is_contract_authority(self):
        """Moving America's top-ups are general-fund appropriations in addition to the trust
        fund's contract authority (Draft 2 sec. 110; decision A-14), so they stay discretionary."""
        for i in ("MOV-29", "MOV-30", "MOV-31"):
            self.assertEqual(S[i]["kind"], "discretionary", i)
            self.assertEqual(S[i]["budget_authority"], "spendout", i)
        self.assertNotIn("contract_authority", P.KINDS)

    def test_spendout_reads_the_cbo_calibrated_file(self):
        groups = {s["spendout_group"] for s in S.values() if s["budget_authority"] == "spendout"}
        self.assertEqual(groups, {"defense", "nondefense"})
        self.assertEqual(P.SPENDOUT_GROUPS, ("defense", "nondefense"))

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
