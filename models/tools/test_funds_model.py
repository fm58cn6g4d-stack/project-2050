"""Unit tests for funds-model.py's `direct` provision kind (E-Verify's Social Security funds line, IMM-EV-SS; PR #405).

Role: guards the `direct` kind in provision_path and its input, models/data/inputs/funds-ss-offbudget.csv, against
silent edits. Run by run-all.sh after the dedicated-funds step (it needs build/ledger.json, build/fiscal-model.json and
build/moving-america.json from the same run). Standard library only. The funds model runs at import, so the test loads
it in a scratch folder holding copies of those three files; its funds.json and dedicated-funds.md stay there.
Checks that:
- a `direct` provision returns (-x, 0) in % of payroll, x read from the per-year input: revenue only, no benefit change;
- it is zero before its start year and before the input series begins, and holds the series' last share after it ends;
- IMM-EV-SS, as booked in funds-ss-provisions.csv, follows the input year by year from its 2031 start.
"""
import csv
import importlib.util
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BUILD = Path(os.environ.get("BUILD", ROOT / "build"))
INPUTS = ROOT / "models" / "data" / "inputs"
NEEDS = ("ledger.json", "fiscal-model.json", "moving-america.json")


def load_funds():
    missing = [n for n in NEEDS if not (BUILD / n).exists()]
    if missing:
        raise unittest.SkipTest(f"no {', '.join('build/' + m for m in missing)}: run bash models/tools/run-all.sh first")
    tmp = tempfile.mkdtemp(prefix="funds-test-")
    for n in NEEDS:
        shutil.copy(BUILD / n, tmp)
    cwd = os.getcwd()
    sys.path.insert(0, str(HERE))
    try:
        os.chdir(tmp)
        spec = importlib.util.spec_from_file_location("funds_model_under_test", HERE / "funds-model.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    finally:
        os.chdir(cwd)
        sys.path.remove(str(HERE))
        shutil.rmtree(tmp, ignore_errors=True)
    return mod


def direct(start):
    return dict(kind="direct", rate=0.0, threshold=0.0, start=start, credit_factor=0.0, extra_haircut=0.0, cola_bump=0.0)


class DirectKind(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.F = load_funds()
        with open(INPUTS / "funds-ss-offbudget.csv", newline="", encoding="utf-8") as f:
            cls.series = {int(r["year"]): float(r["loss_pct_payroll"]) for r in csv.DictReader(f)}
        cls.first, cls.last = min(cls.series), max(cls.series)

    def test_returns_minus_input_and_no_cost(self):
        f = self.F.provision_path(direct(self.first))
        for t, x in self.series.items():
            self.assertEqual(f(t), (-x, 0.0), t)

    def test_zero_before_start_year(self):
        f = self.F.provision_path(direct(2035))
        for t in range(2026, 2035):
            self.assertEqual(f(t), (0.0, 0.0), t)
        self.assertEqual(f(2035), (-self.series[2035], 0.0))

    def test_zero_before_series_begins(self):
        f = self.F.provision_path(direct(2026))
        for t in range(2026, self.first):
            self.assertEqual(f(t), (0.0, 0.0), t)

    def test_holds_last_share_after_series(self):
        f = self.F.provision_path(direct(self.first))
        for t in (self.last + 1, 2060, 2100):
            self.assertEqual(f(t), (-self.series[self.last], 0.0), t)

    def test_imm_ev_ss_follows_input(self):
        p = self.F.SSP["IMM-EV-SS"]
        self.assertEqual((p["kind"], p["start"]), ("direct", 2031))
        f = self.F.SSF["IMM-EV-SS"]
        self.assertEqual(f(2030), (0.0, 0.0))
        for t in range(2031, self.last + 1):
            self.assertEqual(f(t), (-self.series[t], 0.0), t)
        self.assertEqual(f(2100), (-self.series[self.last], 0.0))

    def test_in_plan_scenarios_only(self):
        S = self.F.SS_SCEN
        self.assertNotIn("IMM-EV-SS", S["Current law"])
        self.assertIn("IMM-EV-SS", S["D8 baseline"])
        self.assertIn("IMM-EV-SS", S["D8 + SS-5"])


if __name__ == "__main__":
    unittest.main(verbosity=1)
