#!/usr/bin/env python3
"""test_data.py: checks for the budget data layer (models/data/budget/, piece B2).

Role: proves the data layer and the adopted baseline are one baseline. Status: current.
Run from the repo root: python3 models/tools/budget/test_data.py   (standard library only)

  1. The layer's CSVs follow from their cached sources (build_data.py writes the same bytes).
  2. Rebuilt from the layer alone, the adopted baseline equals models/data/fiscal-baseline.csv
     in every cell, FY1962-2056 (the brief asks for FY2026-2056; the history matches too).
     The file stores billions to three decimals (nearest $1 million); that is its only
     rounding. Before rounding, every value also equals fiscal-data.py's own unrounded build
     exactly (the same floating-point number), so the match holds to the cent and beyond.
  3. post-february.csv carries the same FY2026 actuals and adjustments as fiscal-data.py.
  4. The category list is complete and well formed.
  5. The two conversions behave, and CBO's and OMB's actuals agree where they should.
"""
import csv, importlib.util, os, sys, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
import build_data  # noqa: E402
import data as D   # noqa: E402

BASELINE = os.path.join(ROOT, "models", "data", "fiscal-baseline.csv")
KINDS = {"receipts", "mandatory", "discretionary", "interest"}


def fiscal_data_module():
    spec = importlib.util.spec_from_file_location("fiscal_data", os.path.join(ROOT, "models", "tools", "fiscal-data.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


class Layer(unittest.TestCase):
    def test_files_follow_from_sources(self):
        for name, text in build_data.build().items():
            with open(os.path.join(D.DATA, name)) as f:
                self.assertEqual(f.read(), text, name + " differs from build_data.py output; rerun it")


class Reproduction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(BASELINE, newline="") as f:
            rd = csv.reader(f)
            cls.header = next(rd)
            cls.want = list(rd)
        cls.rows = D.adopted_baseline()

    def test_same_columns_and_years(self):
        self.assertEqual(self.header, D.BASELINE_COLUMNS)
        self.assertEqual([int(r[0]) for r in self.want], sorted(self.rows))
        self.assertEqual(sorted(self.rows)[0], 1962)
        self.assertEqual(sorted(self.rows)[-1], 2056)

    def test_every_cell_equal(self):
        got = D.baseline_csv_rows(self.rows)
        diffs = [(w[0], c, a, b) for g, w in zip(got, self.want)
                 for c, a, b in zip(self.header, g, w) if a != b]
        self.assertEqual(diffs, [], "cells that differ (year, column, rebuilt, adopted)")

    def test_unrounded_values_identical_to_fiscal_data(self):
        F = fiscal_data_module()
        ref = F.build(os.path.join(ROOT, "models", "data", "cbo"))
        self.assertEqual(sorted(ref), sorted(self.rows))
        for y in ref:
            for c in D.BASELINE_COLUMNS:
                a, b = ref[y].get(c), self.rows[y].get(c)
                self.assertEqual(a, b, "FY%d %s: fiscal-data %r, layer %r" % (y, c, a, b))


class PostFebruary(unittest.TestCase):
    def test_matches_fiscal_data_constants(self):
        F = fiscal_data_module()
        pf = D.post_february()
        act = {a["category"]: float(a["base"]) + float(a["change"]) if a["change"] else float(a["base"])
               for a in pf if a["kind"] == "fy2026_actual"}
        self.assertEqual(act, F.FY2026_ACTUAL)
        adj = {a["id"]: a for a in pf if a["kind"] == "adjustment"}
        self.assertEqual(sorted(adj), sorted(a["id"] for a in F.ADJUSTMENTS))
        for a in F.ADJUSTMENTS:
            r = adj[a["id"]]
            self.assertEqual(r["category"], a["kind"])
            self.assertEqual(r["label"], a["label"])
            self.assertEqual(r["basis"], a["basis"])
            if "one_time" in a:
                self.assertEqual(r["rule"], "one_time")
                self.assertEqual({int(r["year"]): float(r["base"])}, a["one_time"])
            else:
                self.assertEqual((r["rule"], float(r["base"])), ("gdp_spread", a["ten_year_total"]))
                self.assertEqual((int(r["year"]), int(r["year_end"])), a["years"])
                self.assertEqual(r["after"], a["after"])


class Categories(unittest.TestCase):
    def test_well_formed(self):
        cats = D.categories()
        names = [c["category"] for c in cats]
        self.assertEqual(len(names), len(set(names)))
        for c in cats:
            self.assertIn(c["kind"], KINDS, c["category"])
            self.assertIn(c["level"], ("baseline", "detail"))
            self.assertIn(c["measure"], ("receipts", "outlays", "budget_authority"))
        base = [c["category"] for c in D.categories("baseline")]
        self.assertEqual(base, D.CATS_REV + D.CATS_OUT)

    def test_named_variables_exist(self):
        cols = {}
        for f, period in (("cbo-historical", "cbo_historical"), ("cbo-ten-year", "cbo_ten_year"),
                          ("cbo-long-term", "cbo_long_term")):
            cols[period] = set(D.table(f)[0])
        names = {c["category"] for c in D.categories()}
        for c in D.categories():
            for period in cols:
                for tok in c[period].replace(":", " ").split():
                    if tok in "+-" or tok in names or tok in ("gdp_share", "gdp_share_split", "defense", "nondefense"):
                        continue
                    self.assertIn(tok, cols[period], "%s %s" % (c["category"], period))
            if c["omb_discretionary"]:
                self.assertIn(c["omb_discretionary"], {r["program"] for r in D.table("omb-discretionary")})

    def test_categories_add_to_totals(self):
        for y, r in D.adopted_baseline().items():
            self.assertAlmostEqual(r["rev_total"] - r["out_total"], -r["deficit"], places=9)
        T = D.by_year("cbo-ten-year")
        for y, t in T.items():   # CBO's own totals, before the FY2026 actuals
            rev = sum(D.cbo_series(c)[y] for c in D.CATS_REV)
            out = sum(D.cbo_series(c)[y] for c in D.CATS_OUT)
            self.assertAlmostEqual(rev, t["proj_rev_total"], delta=0.01, msg=y)
            self.assertAlmostEqual(out, t["proj_outlays_total"], delta=0.01, msg=y)

    def test_budget_authority_detail(self):
        ba = D.cbo_series("ba_disc_defense")
        parts = [D.cbo_series("ba_disc_defense_base"), D.cbo_series("ba_disc_defense_emergency")]
        self.assertEqual(sorted(ba), list(range(2025, 2037)))
        for y in ba:
            self.assertAlmostEqual(ba[y], parts[0][y] + parts[1][y], delta=0.002)


class Conversions(unittest.TestCase):
    def test_real_dollars(self):
        nominal = {y: 100.0 for y in range(2000, 2057)}
        for idx in ("cpiu", "gdp_price_index"):
            real = D.to_real(nominal, base_year=2026, index=idx)
            self.assertAlmostEqual(real[2026], 100.0, places=9)
            self.assertLess(real[2056], real[2026])      # later dollars are worth less
            self.assertGreater(real[2000], real[2026])
        with self.assertRaises(ValueError):
            D.deflator("pce")

    def test_deflators_cover_and_match_sources(self):
        d = {int(r["year"]): r for r in D.table("deflators")}
        self.assertEqual(sorted(d), list(range(1950, 2057)))
        E, H = D.by_year("cbo-economic"), D.by_year("cbo-economic-historical")
        for y in range(2026, 2037):
            self.assertAlmostEqual(float(d[y]["cpiu"]), E[y]["cpiu"], places=3)
        for y in range(1950, 2026):
            self.assertAlmostEqual(float(d[y]["gdp_price_index"]), H[y]["gdp_price_index"], places=3)

    def test_pct_gdp(self):
        g = D.gdp()
        self.assertEqual(sorted(g), list(range(1962, 2057)))
        pct = D.to_pct_gdp(g)
        self.assertTrue(all(abs(v - 100) < 1e-9 for v in pct.values()))
        B = D.adopted_baseline()
        # CBO's long-term debt share comes back out
        L = D.by_year("cbo-long-term")
        debt = D.to_pct_gdp({y: B[y]["debt_public"] for y in range(2037, 2057)})
        for y in debt:
            self.assertAlmostEqual(debt[y], L[y]["lt_debt_held_by_public_gdp_share"], places=9)


class CBOAgainstOMB(unittest.TestCase):
    def test_total_outlays(self):
        """CBO's and OMB's historical outlays are identical through FY2019. FY2020-2025 differ
        by at most 0.6% (CBO's historical file differs from OMB's tables in those years)."""
        O, H = D.omb_function("outlays", "total"), D.by_year("cbo-historical")
        for y in range(1962, 2026):
            o, c = O[(y, "000")], H[y]["outlays_total"]
            if y <= 2019:
                self.assertAlmostEqual(o, c, delta=0.0015, msg=y)
            else:
                self.assertLess(abs(o - c) / c, 0.006, y)

    def test_discretionary_outlays(self):
        disc = {(int(r["year"]), r["program"]): r for r in D.table("omb-discretionary")}
        H = D.by_year("cbo-historical")
        for y in range(1962, 2026):
            for p, c in (("defense_total", "disc_defense"), ("nondefense_total", "disc_nondefense")):
                self.assertLess(abs(float(disc[(y, p)]["outlays"]) - H[y][c]) / H[y][c], 0.002, (y, p))

    def test_spendout_shares(self):
        s = D.table("spendout-discretionary")
        for grp in ("defense", "nondefense"):
            rows = [r for r in s if r["group"] == grp]
            self.assertEqual([int(r["year_of_spending"]) for r in rows], list(range(build_data.LAGS)))
            self.assertLess(float(rows[0]["rmse_pct_of_mean_outlays"]), 5.0)


if __name__ == "__main__":
    unittest.main(verbosity=1)
