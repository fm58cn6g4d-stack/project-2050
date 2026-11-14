#!/usr/bin/env python3
"""clean_power_booking.py: the clean power dossier's booking in the adopted inputs, derived from the dossier's path.

Role: the one place the clean power rows, year-by-year shapes and ten-year amounts are computed (clean power's
L3 close-out; dossiers/clean-power/6-cost.md part 6; review-m4.md, "What the booking (tier 3) must use"). Status:
current. It reads the dossier's fiscal-year path (dossiers/clean-power/tools/clean_power_path.py, on the climate
rows as booked before this booking, frozen in booked-before.csv) and the energy model's results.json for the clean
standard's payments, and returns the numbers that models/data/inputs/ (ledger-bills.csv, ledger-revenue.csv,
fiscal-years.csv, fiscal-after.csv, fiscal-profiles.csv, climate-adoption.json) hold. test_fiscal_clean_power.py
checks that the inputs equal them, so a change to the dossier's path shows up as a failing test, not a silent drift.

    python3 models/tools/clean_power_booking.py           # the rows and the totals
    python3 models/tools/clean_power_booking.py --json    # the same as JSON

What is booked (central path, $ billion by federal fiscal year; a cost positive):
- Memo 1 B (DEC-2026-11-13-06): REV-C1 (C1) on power plants and large industry only, each year's booked receipts
  times the covered share; CX, JCT's 24.4% offset, falls with it; CLI-2, the dividend, stays 80% of C1. CLI-5's
  add-ons lose 20% of the receipts no longer charged as financing through FY2039: CLI-5 takes a year shape (its
  booked base path plus that loss) and keeps its booked FY2040, since the add-ons end with the window.
- Memo 4 B: CLI-10, the second grid tranche and the builder of last resort at subsidy cost, time-limited capital (D4-B).
- Memo 5 B: CLI-5H, the bill credit, inside CLI-5's energy line through FY2039 and permanent from FY2040.
- Memo 7 B: CLI-11, the transition guarantee, on the energy model's closure timing.
- DEC-2026-11-13-13 (option A): from FY2040 the 20% transition share is general-fund revenue (C1T); its waterfall's
  draws are CLI-5H and CLI-11, booked on the general fund.
- The clean standard's capped payments (CLI-3A.02; memo 9 B, DEC-2026-11-13-14): Treasury's receipts (C3A) and JCT's
  24.4% offset on them (CXA), since the payment is a new fee (DEC-2026-11-12-08, part 4). The payments go to a grid
  account sized each year to ready-to-build transmission, not to bill protection and the bill credit. The account
  first funds the second tranche's milestone releases, already booked in CLI-10, so those draws add nothing; CLI-3A is
  what it spends beyond them (siting grants and the equipment reserve's net cost: a working assumption,
  ACCOUNT_NEW_USES), capped by each year's payments. Everything else is general-fund receipts.
"""
import csv
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
W = list(range(2030, 2040))
FY = list(range(2030, 2041))
OFFSET = 0.244            # excise-offset.csv (DEC-2026-11-12-08)
C1_BOOKED = (1.65, 1.9, 2.1)
CLI2_BOOKED = (1.3438334774729577, 1.5311296000407166, 1.6184)   # cost lo/mid/hi before: 80% of C1 plus O5's increment
CLI5_LEGACY_GF = 0.168     # climate-adoption.json legacy_gf_tn before this booking
ACP_PERMIT_WINDOW = None   # read from results.json (the decided set with the permitting package): the low end
GRID2_RANGE = (0.0, 0.08)  # 6-cost.md part 5
GUARANTEE_RANGE = (0.006, 0.040)
# Memo 9 B: the grid account's uses beyond CLI-10's milestone draws, $ billion a year in FY2026 dollars from the first
# year of payments, grown with the CPI (working assumption, 6-cost.md part 6, 6a: a siting-grant program the size of
# IRA section 50152's and the net cost of a pooled equipment reserve; low, central, high)
ACCOUNT_NEW_USES = (0.25, 0.5, 1.5)


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def path_module():
    tools = os.path.join(ROOT, "dossiers", "clean-power", "tools")
    if tools not in sys.path:
        sys.path.insert(0, tools)
    return _load("clean_power_path", os.path.join(tools, "clean_power_path.py"))


def fiscal():
    if HERE not in sys.path:
        sys.path.insert(0, HERE)
    return _load("cpb_fiscal", os.path.join(HERE, "fiscal-model.py"))


def climate_delta():
    if HERE not in sys.path:
        sys.path.insert(0, HERE)
    return _load("cpb_climate", os.path.join(HERE, "climate-integration.py"))


def r(x, n=4):
    return round(x + 0.0, n)


def window(d):
    return [round(d.get(y, 0.0) + 0.0, 2) for y in W]


def perm_for(F, B, v2039, v2040, grow):
    """The perm that makes a years row's FY2040 equal v2040 (row_path: FY2039 x perm x growth)."""
    if abs(v2039) < 1e-12:
        return 0.0
    g = F.growth_index(B, grow)
    return v2040 / (v2039 * g[2040] / g[2039])


def ledger_row(path, rid):
    with open(path) as f:
        for row in csv.reader(f):
            if row and row[0] == rid:
                return row
    raise KeyError(rid)


def energy_acp():
    res = json.load(open(os.path.join(ROOT, "models", "tools", "energy", "results.json")))
    p = res["provisions"]["CLI-3A.02"]["by_year"]
    permit = res["scenarios"]["decided_permit"]["window_2030_39"]["acp"]
    return {y: -float(p[str(y)]) for y in FY}, permit


def booking():
    P = path_module().compute()
    F = fiscal()
    B = F.read_baseline(os.path.join(ROOT, "models", "data", "fiscal-baseline.csv"))
    D = climate_delta()
    rows, years, after, perms, ledger, revenue = P["rows"], {}, {}, {}, {}, {}
    inputs = os.path.join(ROOT, "models", "data", "inputs")
    rv = {k: tuple(float(x) for x in ledger_row(os.path.join(inputs, "ledger-revenue.csv"), k)[3:6])
          for k in ("C2", "C3")}

    # Memo 1 B: C1, CX and CLI-2
    k = sum(P["c1"][y] for y in W) / 1000 / C1_BOOKED[1]
    c1 = tuple(r(x * k) for x in C1_BOOKED)
    revenue["C1"] = c1
    cx = {y: rows["CX"][y] + P["cx"][y] for y in FY}            # a cost (the offset), $B
    years["CX"] = [-v for v in window(cx)]                       # the row's own sign: revenue lost
    perms["CX"] = perm_for(F, B, cx[2039], cx[2040], "gdp")
    # The ledger keeps JCT's rate times the three fees at each end, to $1 billion (test_fiscal_counting.py); the
    # path's shape carries the year-by-year detail (it sums to within $0.1 billion of the rounded midpoint)
    fees = lambda i: c1[i] + rv["C2"][i] + rv["C3"][i]  # noqa: E731
    revenue["CX"] = tuple(round(-OFFSET * fees(i), 3) for i in (2, 1, 0))   # lo: the most revenue lost
    ledger["CLI-2"] = tuple(r(0.8 * c + (b - 0.8 * c0)) for c, b, c0 in zip(c1, CLI2_BOOKED, C1_BOOKED))

    # CLI-5: its booked base path plus the lost transition share, ending with the window
    # ledger-build.py rounds CLI-5's own financing to three decimals (_c5), so the loss the ledger books is the
    # rounded difference; the path's year shape takes that rounding (about $0.2 billion over the ten years)
    delta = {y: D.delta_rows(y)["CLI-5"] for y in FY}
    base = {y: rows["CLI-5"][y] - delta[y] for y in FY}
    own = lambda c: round(0.2 * c + rv["C2"][1] + rv["C3"][1], 3)  # noqa: E731
    lost = own(C1_BOOKED[1]) - own(c1[1])
    s = lost * 1000 / sum(P["c5"][y] for y in W)
    c5 = {y: base[y] + P["c5"][y] * s for y in FY}
    years["CLI-5"] = window(c5)
    perms["CLI-5"] = perm_for(F, B, c5[2039], base[2040], "gdp")
    legacy_gf = r(CLI5_LEGACY_GF + lost, 6)

    # Memo 4 B, memo 5 B, memo 7 B
    years["CLI-10"] = window(P["grid2"])
    perms["CLI-10"] = 0.0
    ledger["CLI-10"] = (GRID2_RANGE[0], r(sum(years["CLI-10"]) / 1000), GRID2_RANGE[1])
    after["CLI-5H"] = {2040: round(P["bills"][2040], 2)}
    ledger["CLI-5H"] = (0.0, 0.0, 0.0)
    years["CLI-11"] = window(P["g7"])
    perms["CLI-11"] = perm_for(F, B, P["g7"][2039], P["g7"][2040], "gdp")
    # ledger-build.py keeps a bill's general-fund amount to $1 billion: $14.0B for the path's $13.6B
    ledger["CLI-11"] = (GUARANTEE_RANGE[0], r(sum(years["CLI-11"]) / 1000, 3), GUARANTEE_RANGE[1])

    # DEC-2026-11-13-13 A: the transition share is general-fund revenue from FY2040
    after["C1T"] = {2040: -round(P["ts"][2040], 2)}           # a revenue row's path: a gain is negative
    revenue["C1T"] = (0.0, 0.0, 0.0)

    # The clean standard's payments, their pay-out and the offset on them
    acp, permit = energy_acp()
    years["C3A"] = window(acp)
    years["CXA"] = [round(-OFFSET * v, 2) for v in window(acp)]
    for rid, grow in (("C3A", "gdp"), ("CXA", "gdp")):
        perms[rid] = perm_for(F, B, acp[2039], acp[2040], grow)
    mid = r(sum(years["C3A"]) / 1000, 3)
    low = r(permit / 1000, 3)
    revenue["C3A"] = (low, mid, mid)
    revenue["CXA"] = (r(-OFFSET * mid), r(-OFFSET * mid), r(-OFFSET * low))
    # Memo 9 B: the grid account. Its draws for CLI-10's milestones are already booked there; CLI-3A is its spending
    # beyond them, capped by what is left of each year's payments; the rest stays as receipts
    cpi = F.growth_index(B, "cpi")
    def account(level):
        return {y: (min(level * cpi[y] / cpi[2026], max(0.0, acp[y] - P["grid2"].get(y, 0.0))) if acp[y] > 0 else 0.0)
                for y in FY}
    acct = {k: account(v) for k, v in zip(("lo", "mid", "hi"), ACCOUNT_NEW_USES)}
    years["CLI-3A"] = window(acct["mid"])
    perms["CLI-3A"] = perm_for(F, B, acct["mid"][2039], acct["mid"][2040], "gdp")
    ledger["CLI-3A"] = tuple(r(sum(acct[k][y] for y in W) / 1000, 3) for k in ("lo", "mid", "hi"))
    kept = {y: acp[y] - acct["mid"][y] for y in FY}

    tn = lambda d: sum(d.get(y, 0.0) for y in W) / 1000  # noqa: E731
    totals = dict(change_window=tn(P["change"]), change_fy2040=P["change"][2040],
                  acp_offset_window=OFFSET * mid, acp_offset_fy2040=OFFSET * acp[2040],
                  acp_kept_window=mid - ledger["CLI-3A"][1], acp_kept_fy2040=kept[2040],
                  account_window=ledger["CLI-3A"][1], account_fy2040=acct["mid"][2040],
                  account_cli10_window=tn(P["grid2"]),
                  c1_window=c1[1], cx_window=revenue["CX"][1], transition_fy2040=P["ts"][2040])
    fy2040 = dict(CX=cx[2040], **{"CLI-5": base[2040] + delta[2040]}, **{"CLI-10": 0.0},
                  **{"CLI-5H": P["bills"][2040], "CLI-11": P["g7"][2040], "C1T": P["ts"][2040],
                     "C3A": acp[2040], "CLI-3A": acct["mid"][2040], "CXA": -OFFSET * acp[2040]})
    return dict(years=years, after=after, perms=perms, ledger=ledger, revenue=revenue,
                legacy_gf_cli5=legacy_gf, fy2040=fy2040, totals=totals)


if __name__ == "__main__":
    b = booking()
    if "--json" in sys.argv:
        print(json.dumps(b, indent=1, default=str))
    else:
        for k, v in b["years"].items():
            print(f"{k:8s} {sum(v)/1000:8.4f}T  perm {b['perms'].get(k, 1.0):.6f}  {v}")
        print("after", b["after"])
        print("ledger", b["ledger"])
        print("revenue", b["revenue"])
        print("legacy_gf CLI-5", b["legacy_gf_cli5"])
        print("fy2040", {k: round(v, 2) for k, v in b["fy2040"].items()})
        print("totals", {k: round(v, 4) for k, v in b["totals"].items()})
