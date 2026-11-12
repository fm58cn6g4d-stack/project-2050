"""The four counting inputs Espen decided on November 12, 2026 (board question 0q, DEC-2026-11-12-08),
and Moving America's FY2037-39 draw (DEC-2026-11-12-10).

Role: protects those bookings. Run by run-all.sh after the fiscal model (it reads build/ledger.json and
build/fiscal-model.json); standard library only. Checks that:
- MOV-29 and MOV-30 are booked in the years the acts name, by year from the transportation model, with
  nothing after their last top-up year, and MOV-31's successor line carries the model's general-fund draw
  from FY2037, with no empty year and none counted twice;
- C35 grows at GDP plus the points in its profile (ASM-PROF-ESTATE) and DEM-11 with prices;
- CX, CXP and MR6 take JCT's offset rate from excise-offset.csv (ASM-EXCISE-OFFSET).
"""
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
from inputs import offset_rate, read  # noqa: E402

spec = importlib.util.spec_from_file_location("counting_fiscal", HERE / "fiscal-model.py")
fiscal = importlib.util.module_from_spec(spec); spec.loader.exec_module(fiscal)

W = range(2030, 2040)


def act_shapes():
    """The two acts by fiscal year, $B, from the transportation model: each package on the model's
    FY2029-31 obligation schedule for the two packages (FY2029's share in FY2030, the first window
    year), then the top-ups by year as ledger_rows() splits them between the acts."""
    m = MA.Model()
    tu = m.topups()
    sched = {y: MA.RAIL_RECON[y] + sum(v for n, k, yy, v in MA.TRANSIT_RECON if yy == y) for y in (2029, 2030, 2031)}
    tot = sum(sched.values())
    pk = {"MOV-29": sum(MA.RAIL_RECON_PACKAGE1.values()) + sum(MA.TRANSIT_PACKAGE1.values()),
          "MOV-30": sum(MA.RAIL_RECON_PACKAGE2.values()) + sum(MA.TRANSIT_PACKAGE2.values())}
    out = {i: {y: 0.0 for y in W} for i in pk}
    for i, p in pk.items():
        out[i][2030] += p * (sched[2029] + sched[2030]) / tot
        out[i][2031] += p * sched[2031] / tot
    for y in (2032, 2033, 2034):
        out["MOV-29"][y] += tu[y]["hwy"] + tu[y]["tra"] + tu[y]["rail"]
    out["MOV-29"][2035] += tu[2035]["hwy"] + tu[2035]["tra"]
    out["MOV-30"][2035] += tu[2035]["rail"]
    out["MOV-30"][2036] += tu[2036]["hwy"] + tu[2036]["tra"] + tu[2036]["rail"]
    return out


class Counting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = json.load(open(BUILD / "ledger.json"))
        cls.bills = {b["id"]: b for b in cls.ledger["bills"]}
        cls.rev = {r["id"]: r for r in cls.ledger["revenue"]}
        cls.cuts = {c["id"]: c for c in cls.ledger["cuts"]}
        cls.B = fiscal.read_baseline(ROOT / "models/data/fiscal-baseline.csv")

    def path(self, i):
        return fiscal.row_path(self.B, self.bills[i]["gf_mid"], fiscal.PR.BILLS[i], i)

    def test_moving_america_acts_in_the_years_they_pay(self):
        want = act_shapes()
        for i in ("MOV-29", "MOV-30"):
            shape = fiscal.PR.YEARS[i]
            for k, y in enumerate(W):
                self.assertAlmostEqual(shape[k], want[i][y], delta=0.006, msg="%s %d" % (i, y))
            # the shape adds to the act's ledger amount (package plus top-ups), so calibration only rounds
            self.assertAlmostEqual(sum(shape) / 1000, self.bills[i]["gf_mid"], delta=0.0005, msg=i)
            p = self.path(i)
            self.assertTrue(all(p[y] == 0 for y in range(2040, 2057)), i + " continues after 2039")
        self.assertEqual(max(y for y in W if want["MOV-29"][y]), 2035)
        self.assertEqual(max(y for y in W if want["MOV-30"][y]), 2036)

    def test_later_draw_is_the_transportation_models(self):
        m = MA.Model()
        after = fiscal.PR.AFTER["MOV-31"]
        self.assertEqual(sorted(after), list(range(2040, 2047)))
        for y, v in after.items():
            self.assertAlmostEqual(v, m.allocate(y)["gf_total"], delta=0.006, msg=str(y))
        p = self.path("MOV-31")
        self.assertAlmostEqual(sum(p[y] for y in W), self.bills["MOV-31"]["gf_mid"] * 1000, places=6)
        self.assertAlmostEqual(p[2040], 29.0, delta=0.05)
        self.assertAlmostEqual(p[2044], 14.0, delta=0.06)
        g = fiscal.growth_index(self.B, "gdp")
        self.assertAlmostEqual(p[2056], p[2046] * g[2056] / g[2046], places=9)

    def test_successor_line_from_fy2037(self):
        """DEC-2026-11-12-10: FY2037-39 at the model's general-fund draw, joined to the FY2040 draw.
        The ledger rounds MOV-31 to $1B, so the window's years are scaled by that rounding only."""
        m = MA.Model()
        p = self.path("MOV-31")
        shape = dict(zip(W, fiscal.PR.YEARS["MOV-31"]))
        for y in (2037, 2038, 2039):
            self.assertAlmostEqual(shape[y], m.allocate(y)["gf_total"], delta=0.006, msg=str(y))
            self.assertAlmostEqual(p[y], m.allocate(y)["gf_total"], delta=0.1, msg=str(y))
        self.assertAlmostEqual(sum(shape[y] for y in (2037, 2038, 2039)), MA.ledger_rows()["gf_draw_fy37_39"], delta=0.01)
        # the 2031 bill's own FY2032-36 years: its expansion and division E, at the model's amount
        self.assertAlmostEqual(sum(shape[y] for y in range(2032, 2037)), MA.expansion_authority() + 1.0, delta=0.02)
        self.assertTrue(all(shape[y] == 0 for y in (2030, 2031)))
        # no double count: the two acts book nothing once the successor line starts
        for i in ("MOV-29", "MOV-30"):
            q = self.path(i)
            self.assertTrue(all(q[y] == 0 for y in range(2037, 2057)), i)
        # no gap: every year from FY2032 to FY2056 carries Moving America's general-fund money
        tot = {y: sum(self.path(i)[y] for i in ("MOV-29", "MOV-30", "MOV-31")) for y in range(2032, 2057)}
        self.assertTrue(all(v > 0 for v in tot.values()))
        # the ledger amount is the 2031 bill plus the successor years
        f = MA.ledger_rows()
        self.assertAlmostEqual(self.bills["MOV-31"]["cost_mid"],
                               round((round(f["expansion_authority"], 2) + 1.0 + round(f["gf_draw_fy37_39"], 2)) / 1000, 5), places=9)

    def test_estate_tax_grows_faster_than_gdp(self):
        prof = fiscal.PR.CUTS["C35"]
        self.assertTrue(prof["grow"].startswith("gdp+"))
        x = float(prof["grow"][4:])
        self.assertTrue(1.4 <= x <= 4.3, "outside ASM-PROF-ESTATE's range")
        p = fiscal.row_path(self.B, -self.cuts["C35"]["saves_tn"], prof, "C35")
        self.assertAlmostEqual(sum(p[y] for y in W), -self.cuts["C35"]["saves_tn"] * 1000, places=6)
        for y in range(2031, 2057):
            self.assertAlmostEqual(p[y] / p[y - 1], self.B[y]["gdp"] / self.B[y - 1]["gdp"] * (1 + x / 100), places=9)

    def test_election_funding_indexed_to_prices(self):
        self.assertEqual(fiscal.PR.BILLS["DEM-11"]["grow"], "cpi")

    def test_offsets_at_jcts_rate(self):
        rate = offset_rate()
        self.assertEqual(rate, 0.244)
        rv = {r["id"]: r for r in read("ledger-revenue.csv")}
        for k, col in enumerate(("lo", "mid", "hi")):
            fees = sum(float(rv[c][("hi", "mid", "lo")[k]]) for c in ("C1", "C2", "C3"))
            self.assertAlmostEqual(float(rv["CX"][col]), round(-rate * fees, 3), places=9, msg="CX " + col)
        f = MA.ledger_rows()
        gross = round(f["act29_gross"], 1) + round(f["act30_gross"], 1)
        self.assertAlmostEqual(self.rev["MR6"]["mid"], round(-rate * gross / 1000, 4), places=9)
        cl = fiscal.CL
        cxp = sum(cl.delta_rows(y)["CXP"] for y in W)
        self.assertAlmostEqual(cxp, rate * sum(cl.account(y)["added_receipts_bn"] for y in W), places=6)
        self.assertAlmostEqual(-self.rev["CXP"]["mid"] * 1000, cxp, places=6)


if __name__ == "__main__":
    unittest.main()
