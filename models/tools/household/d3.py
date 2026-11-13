"""The D3 household net test: the household model's engine for it, with the interface the legacy incidence model had.

Role: the one home of the D3 test's arithmetic (`MODEL-CARD.md`, "Provision interface"), replacing
`models/tools/incidence-model.py` and `incidence-years.py` (retired in M3 part 2). Status: working.

Two versions of every result:
  * `legacy`: the typed keys (`incidence-keys.csv`) over 140 million households and the typed 2034 group incomes, the
    legacy model's figures exactly. The budget-model consumers (`fiscal-recovery/model.py`, `family-financing.py`,
    `climate-integration-report.py`, `check-project.py`) read this version, so their committed outputs do not move
    when the legacy scripts are retired; moving them to the measured keys is a separate, visible change;
  * `model`: the keys `keys.csv` measures on the 2029 CPS households, the model's household count and incomes
    (`provisions.model_keys`, `mid_window_households`, `model_incomes`), as `results.md` reports.

The year-by-year paths (`series`) spread each row's ten-year total over 2030-39 with the profiles in
`models/data/inputs/incidence-phase-in.csv` (adopted input, read only), as `incidence-years.py` did: "ramp" levels grow
4% a year and are normalised, "norm" levels are normalised as typed, `same_as` borrows another row's profile, and the
climate rows follow the climate account's own annual path (`climate-integration.py`).

Reads `ledger.json` from the path given to `load`, or from the working directory.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(HERE, "..")
sys.path.insert(0, HERE)
sys.path.insert(0, TOOLS)
import provisions as P  # noqa: E402
from inputs import read, num  # noqa: E402

GROUPS = P.GROUPS
HH = P.LEGACY_HH
INC = P.LEGACY_INC
YRS = list(range(2030, 2040))
GF_IDS = ["G1", "G5", "G7", "G3", "G9", "G11", "G6", "H1b", "GX", "G8", "G10"]
CORPORATE = ("G1", "G5", "G7")
NOT_GF = ("SAFR2", "EDUP")   # EDUP is a dedicated fund, not general-fund revenue; SAF-R2 is a trim, not a raiser


class D3:
    """The test on one ledger and one set of keys. `D3.load()` gives the legacy version; `D3.load(model=B)` the
    household model's, from a `budget.baseline(2029)`."""

    def __init__(self, ledger, K, hh, inc):
        self.ledger, self.K, self.HH, self.INC, self.GROUPS = ledger, K, hh, inc, GROUPS
        self.ROWS, self.OPTIONS = P.rows(ledger)
        S = P.scenarios()
        self.SCEN = S
        sd = P.SF.load()
        self.QO = P.SF.package("DEC", sd)
        self.QEDU = S[next(s["label"] for s in sd["incidence"] if s["id"] == "Q-EDU")][0]
        self._profiles = None

    @classmethod
    def load(cls, ledger_path="ledger.json", model=None):
        led = P.ledger_values(ledger_path)
        if model is None:
            return cls(led, P.legacy_keys(), P.LEGACY_HH, P.LEGACY_INC)
        K, _ = P.model_keys(model)
        return cls(led, K, P.mid_window_households(model), P.model_incomes(model))

    # ---- the ten-year test ----
    def amount(self, formula):
        """A row's amount: a number, or a formula over ledger IDs in brackets ([G1], [O2]+[OX])."""
        return P.amount(formula, self.ledger)

    def dist(self, parts):
        return P.dist(parts, self.K)

    def per_hh(self, tn, g):
        n = self.HH * (0.01 if g == "T1" else (0.19 if g == "Q5x" else 0.2))
        return tn * 1e12 / 10 / n

    def run(self, opts, drop=()):
        return P.run(self.ROWS, self.OPTIONS, opts, drop, self.K, self.HH, self.INC)

    def gf_test(self, opts):
        """D3's revenue-mix test: the share of new general-fund revenue from the top 1% (by incidence) and
        corporations (statutory). Returns (total, top 1%, corporate, percent)."""
        total = top1 = corp = 0.0
        for rid, label, side, amt, parts, basis in self.ROWS:
            if rid in GF_IDS:
                total += amt
                if rid in CORPORATE:
                    corp += amt
                else:
                    top1 += self.dist(parts)["T1"]
        for o in opts:
            side, amt, parts, label = self.OPTIONS[o]
            if side == "cost" and o not in NOT_GF:
                total += amt
                top1 += self.dist(parts)["T1"]
        return round(total, 2), round(top1, 2), round(corp, 2), round(100 * (top1 + corp) / total)

    # ---- the year-by-year paths ----
    def profiles(self):
        if self._profiles is None:
            grow = [1.04 ** i for i in range(10)]
            norm = lambda v: [x / sum(v) for x in v]
            P_ = {}
            for r in read("incidence-phase-in.csv"):
                if r["same_as"]:
                    P_[r["id"]] = P_[r["same_as"]]
                    continue
                lv = [num(r[f"y{y}"]) for y in YRS]
                P_[r["id"]] = norm([a * g for a, g in zip(lv, grow)]) if r["method"] == "ramp" else norm(lv)
            self._profiles = P_
        return self._profiles

    def annual_fraction(self, rid, amount_tn, y):
        """A row's amount in year y ($T); the climate rows follow the climate account's own path."""
        CL = climate()
        a = CL.account(y)
        if rid == "C1P":
            return a["process_receipts_bn"] / 1000
        if rid == "CB1":
            return a["combustion_receipts_change_bn"] / 1000
        if rid in ("CLIW", "CLIL"):
            return CL.item("retrofits" if rid == "CLIW" else "bill", y) / 1000
        w = self.profiles().get(rid, self.profiles()["flat"])[y - 2030]
        if rid == "E2d":
            return 1.52 * w + a["dividend_bn"] / 1000
        if rid == "E1h":
            return .3 * .9 * w + .3 * CL.CONFIG["credit_split"]["CLI-1"] * CL.item("credits", y) / 1000
        return amount_tn * w

    def series(self, opts):
        """Net dollars per household by quintile, each year 2030-39, nominal."""
        rows = list(self.ROWS) + [(o, l, s, a, p, "") for o, (s, a, p, l) in self.OPTIONS.items() if o in opts]
        out = {y: {g: 0.0 for g in GROUPS} for y in YRS}
        for rid, label, side, amt, parts, _ in rows:
            d = self.dist(parts)
            sign = 1 if side == "benefit" else -1
            for y in YRS:
                f = self.annual_fraction(rid, amt, y) / amt if amt else 0
                for g in GROUPS:
                    out[y][g] += sign * d[g] * f
        return {y: {g: round(v * 1e12 / (self.HH * 0.2)) for g, v in out[y].items()} for y in YRS}

    # ---- the legacy model's output file ----
    def incidence_json(self):
        """What `incidence.py` wrote to `incidence.json`, for the consumers that read it."""
        out = {}
        for name, (o, drop) in self.SCEN.items():
            res, _ = self.run(o, drop)
            out[name] = dict(res=res, gf=self.gf_test(o))
        _, lines = self.run(self.QO)
        basis = {r[0]: r[5] for r in self.ROWS}
        out["lines"] = [(rid, label, side, amt, {g: round(v, 3) for g, v in d.items()}, basis.get(rid, "ledger option"))
                        for rid, label, side, amt, d in lines]
        return out


_CL = None


def climate():
    global _CL
    if _CL is None:
        spec = importlib.util.spec_from_file_location("climate_incidence", os.path.join(TOOLS, "climate-integration.py"))
        _CL = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_CL)
    return _CL


if __name__ == "__main__":
    # `python3 d3.py ledger.json incidence.json`: the legacy version's output file, for the budget-model consumers
    led = sys.argv[1] if len(sys.argv) > 1 else "ledger.json"
    out = sys.argv[2] if len(sys.argv) > 2 else "incidence.json"
    with open(out, "w") as f:
        json.dump(D3.load(led).incidence_json(), f, indent=1)
