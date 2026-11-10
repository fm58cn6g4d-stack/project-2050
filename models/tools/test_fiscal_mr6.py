"""MR6, Moving America's 25% income and payroll tax offset, is booked on the general fund in the base, as CX.

Role: protects the booking of the transportation milestone review's finding F-1. Run by run-all.sh after the
ledger step (it reads build/ledger.json); standard library only. Checks that:
- the year-by-year shape in fiscal-years.csv is the transportation model's own offset, year by year;
- the ledger books MR6 as general-fund base revenue, so the base revenue headline includes it;
- the fiscal model scores MR6 as a base revenue row whose FY2030-39 total is the ledger's MR6 figure;
- the surface transportation trust fund channel carries gross receipts (MR1-MR5), never MR6 a second time.
"""
import csv
import importlib.util
import json
import os
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BUILD = Path(os.environ.get("BUILD", ROOT / "build"))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "transportation"))
import moving_america as MA  # noqa: E402

spec = importlib.util.spec_from_file_location("mr6_fiscal", HERE / "fiscal-model.py")
fiscal = importlib.util.module_from_spec(spec); spec.loader.exec_module(fiscal)


def model_offset(t):
    """The offset in $B for FY t, as Model().cbo_basis(t) adds it on top of allocate(t)."""
    m = MA.Model()
    new = m.P1(t) - MA.legacy(t) - (MA.ev_fee(t) if t <= 2029 else 0)
    return MA.EXCISE_OFFSET * max(new, 0) if t >= 2030 else 0.0


class MR6Booking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = json.load(open(BUILD / "ledger.json"))
        cls.rev = {r["id"]: r for r in cls.ledger["revenue"]}
        cls.base = fiscal.read_baseline(ROOT / "models/data/fiscal-baseline.csv")

    def test_shape_is_the_transportation_models_offset(self):
        shape = fiscal.PR.YEARS["MR6"]
        for i, t in enumerate(range(2030, 2040)):
            self.assertAlmostEqual(-shape[i], model_offset(t), delta=0.005, msg=str(t))
        m = MA.Model()
        self.assertAlmostEqual(model_offset(2040), (m.cbo_basis(2040) - m.allocate(2040)["gf_total"] / MA.gdp(2040)) * MA.gdp(2040), places=6)

    def test_ledger_books_mr6_on_the_general_fund_in_the_base(self):
        r = self.rev["MR6"]
        self.assertEqual((r["channel"], r["in_base"]), ("General fund", "Yes"))
        self.assertLess(r["mid"], 0)
        self.assertEqual((self.rev["CX"]["channel"], self.rev["CX"]["in_base"]), ("General fund", "Yes"))

    def test_fiscal_model_scores_mr6_to_the_ledger_figure(self):
        prof = fiscal.PR.REVENUE["MR6"]
        self.assertEqual((prof["cat"], prof.get("grow", "gdp")), ("rev_individual", "gdp"))
        path = fiscal.row_path(self.base, -self.rev["MR6"]["mid"], prof, "MR6")
        self.assertAlmostEqual(sum(path[y] for y in range(2030, 2040)), -self.rev["MR6"]["mid"] * 1000, places=6)
        self.assertTrue(all(path[y] > 0 for y in range(2030, 2057)))   # a revenue loss, every year
        rows = {r["id"]: r for r in json.load(open(BUILD / "fiscal-model.json"))["rows"]} if (BUILD / "fiscal-model.json").exists() else None
        if rows is not None:
            self.assertEqual(rows["MR6"]["group"], "base revenue")

    def test_trust_fund_channel_is_gross(self):
        ch = {c["channel"]: c for c in self.ledger["summary"]["channels"]}["Surface transportation trust fund"]
        gross = sum(self.rev[k]["mid"] for k in ("MR1", "MR2", "MR3", "MR4", "MR5"))
        self.assertAlmostEqual(ch["rev_mid"], round(gross, 3), places=6)


if __name__ == "__main__":
    unittest.main()
