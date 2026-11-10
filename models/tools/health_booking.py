#!/usr/bin/env python3
"""health_booking.py: the health plan's booking in the adopted inputs, derived from the care dossier's path.

Role: the one place the health rows' year-by-year shapes and ten-year amounts are computed (care milestone review,
F-4; dossiers/care/6-cost.md part 5). Status: current. It reads the dossier's fiscal-year path
(dossiers/care/tools/health_path.py) and the legacy HLT-4 profile, and returns the numbers that
models/data/inputs/ (ledger-bills.csv, ledger-revenue.csv, fiscal-years.csv, fiscal-components.csv,
fiscal-profiles.csv) hold. test_fiscal_health.py checks that the inputs equal them, so a change to the dossier's path
shows up as a failing test rather than a silent drift.

    python3 models/tools/health_booking.py           # the rows and the FY2040 figures
    python3 models/tools/health_booking.py --json    # the same as JSON

What is booked (all $ billion by federal fiscal year unless noted; a cost positive):
- HLT-1, restoration before wave 1: calendar 2030 only, on the fiscal-year blend (FY2030 and a quarter in FY2031).
- HLT-2, Medicare upgrades and no disability wait for today's enrollees, calendar 2031-34, on the blend.
- HLT-3 and HLT-5 retired (memo 1 A and memo 5 D not chosen): $0.
- HLT-4 split (review F-4 item 2): long-term care and the safety-net items kept on the legacy profile; children's
  continuous coverage retired from wave 1 (January 2031), Medicaid dental and the items costed with it retired with
  Medicaid's wave-2 thirds (January 2033, 2034, 2035).
- HLT-6, the Advantage fix at MedPAC's lower estimate, calendar 2030-34, on the blend.
- HLT-7, the single plan's spending line: outlays less the federal money it replaces and the states' payments
  (offsetting receipts, netted here), plus the hospital transition fund and the territories.
- HX, the revenue from ending the employer tax exclusion, on the general fund, on CBO's convention (full pass-through).
- HLT-8, USDA rural health grants (discretionary).
The employer contribution and FEHB's money are not booked (review F-4 item 3): contribution() is reported only.
"""
import csv
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
INPUTS = os.path.join(ROOT, "models", "data", "inputs")
W = list(range(2030, 2040))
GROW = "out_medicare_net"   # CBO's Medicare category: about 5.7% a year after 2039, the dossier's growth path (as C19b)

# Calendar-year figures the dossier gives outside health_path.py (dossiers/care/6-cost.md part 2), $ billion
HLT2_UPGRADES = {2031: 29, 2032: 61, 2033: 97, 2034: 112}          # HLT-2.01, legacy profile moved to 2031
HLT2_DISABILITY_WAIT = {y: 25 for y in range(2031, 2035)}          # HLT-2.03, central $25B a year (range 15-45)
HLT6_ADVANTAGE = {2030: -51, 2031: -110, 2032: -119, 2033: -128, 2034: -138}   # HLT-6.01, MedPAC's 14%
TRANSITION_FUND = {2033: 10, 2034: 20, 2035: 25, 2036: 20, 2037: 15, 2038: 10}  # HLT-7.15, FY2033-38 (DEC-2026-11-10-13)
TERRITORIES_TN, TERRITORIES_FY2040 = 0.13, 23.0                    # HLT-7.01/.17/.28: window and FY2040, on the waves
HLT8_TN = (0.002, 0.004, 0.005)     # USDA grants, $200-500M a year; central $0.35B a year, at the ledger's $1B

# Legacy HLT-4 (legacy/domains/domain-health.md:14; ledger 0.40 / 0.625 / 0.85) and its parts, from the go-big
# bill's component midpoints (legacy/sources/health-working-group-memo-analysis.md, reconciliation table):
# HCBS and the care workforce $200-450B; children's continuous coverage, the immigrant waiting period, Medicaid dental
# and free primary care visits $120-220B (one estimate, no item-level score); health centers doubled, 14,000
# residency slots, the Momnibus and Title X $110-170B.
HLT4_LEGACY = (0.40, 0.625, 0.85)
HLT4_PROFILE = dict(cat="out_health_other", start=2030, ramp=3, grow="out_health_other", perm=1.0)
HLT4_PARTS = {"ltc": 325.0, "medicaid_bundle": 170.0, "safety_net": 140.0}
CHILDREN_SHARE_OF_BUNDLE = 0.25   # working assumption: a quarter each for the four items of the bundle

# Rate sensitivity on the plan's window (6-cost.md part 6): target 1.05 and 1.25 x Medicare, $T
RATE_RANGE_TN = (24.56 - 20.99, 28.12 - 24.56)
HALF_PASSTHROUGH_FY2040 = 370.0   # exclusion revenue lost at half pass-through, no contribution (review F-3), $B


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fy(cal):
    """Fiscal-year blend of calendar-year amounts: FY y takes a quarter of calendar y-1 and three quarters of y."""
    ys = range(min(cal), max(cal) + 2)
    return {y: 0.25 * cal.get(y - 1, 0.0) + 0.75 * cal.get(y, 0.0) for y in ys}


def window(d):
    return [round(d.get(y, 0.0), 2) for y in W]


def health_path():
    HP = _load("health_path", os.path.join(ROOT, "dossiers", "care", "tools", "health_path.py"))
    I, B, P = HP.setup()
    full = HP.model_full(I, B, P)
    net, _, _, f = HP.groups(I, B, P)
    emp = full["private_flows_removed_bn"]["employer_premiums"]
    neutral = net["employer"] / (emp * (1 - f["tau"]))
    series, gf = HP.path(I, B, P, HP.rate_path(HP.hospital_start(I, B)))
    contrib, _ = HP.contribution(I, B, P, series, gf, neutral)
    excl = {y: series[y]["moved_gf"] * f["tax_exclusion"] for y in W + [2040]}
    res = json.load(open(os.path.join(HP.MODEL, "results.json")))
    restore_cal = {r["year"]: r["federal_bn"] for r in res["fy2030_39"]["restore"]["series"]}[2030]
    return dict(net={y: series[y]["total"] for y in W + [2040]}, excl=excl, contribution=contrib,
                restore_cal=restore_cal, neutral=neutral, moved=HP.shares_moved, wave2=HP.WAVE2)


def fiscal():
    return _load("hb_fiscal", os.path.join(HERE, "fiscal-model.py"))


def perm_for(B, F, path, target2040, grow=GROW):
    """The perm that makes a years row's FY2040 equal target2040 (row_path: FY2039 x perm x growth)."""
    g = F.growth_index(B, grow)
    return target2040 / (path[2039] * g[2040] / g[2039])


def booking():
    hp = health_path()
    F = fiscal()
    B = F.read_baseline(os.path.join(ROOT, "models", "data", "fiscal-baseline.csv"))

    # HLT-1: restoration in calendar 2030, on fiscal years
    hlt1 = fy({2030: hp["restore_cal"]})
    # HLT-7 spending line: the path's net cost plus the exclusion revenue it nets, less the restoration (HLT-1)
    spend = {y: hp["net"][y] + hp["excl"][y] - hlt1.get(y, 0.0) for y in W + [2040]}
    terr_shape = {y: spend[y] for y in W + [2040]}     # the territories phase in on the waves (HLT-7.28)
    s = sum(terr_shape[y] for y in W)
    terr = {y: terr_shape[y] * TERRITORIES_TN * 1000 / s for y in W}
    terr[2040] = TERRITORIES_FY2040
    hlt2 = fy({y: HLT2_UPGRADES[y] + HLT2_DISABILITY_WAIT[y] for y in HLT2_UPGRADES})
    hlt6 = fy(HLT6_ADVANTAGE)

    # HLT-4: legacy path by part; the bundle retires as its groups move
    legacy = F.row_path(B, HLT4_LEGACY[1], HLT4_PROFILE)
    tot = sum(HLT4_PARTS.values())
    part = {k: {y: legacy[y] * v / tot for y in legacy} for k, v in HLT4_PARTS.items()}
    kids_left = fy({y: (0.0 if y >= 2031 else 1.0) for y in range(2030, 2041)})
    adult_left = fy({y: 1.0 - sum(1 for w in hp["wave2"] if y >= w) / 3.0 for y in range(2030, 2041)})
    kids = {y: part["medicaid_bundle"][y] * CHILDREN_SHARE_OF_BUNDLE * kids_left[y] for y in W}
    dental = {y: part["medicaid_bundle"][y] * (1 - CHILDREN_SHARE_OF_BUNDLE) * adult_left[y] for y in W}

    tn = lambda d: sum(d.get(y, 0.0) for y in W) / 1000  # noqa: E731
    years = {
        "HLT-1": window(hlt1), "HLT-2": window(hlt2), "HLT-6": window(hlt6),
        "HLT-7/plan-spending": window(spend), "HLT-7/transition-fund": window(TRANSITION_FUND),
        "HLT-7/territories": window(terr),
        "HLT-4/children-continuous-coverage": window(kids), "HLT-4/medicaid-dental-and-bundle": window(dental),
        "HX": window(hp["excl"]),
    }
    # The ledger keeps $1 billion ($0.001T; ledger-build.py rounds gf_mid to three places), so each row's ten-year
    # amount is its shape's sum rounded to that; the fiscal model scales the shape to it. Components keep $0.1 billion
    # and the largest part takes the rounding, so the parts add to the ledger amount exactly.
    r3 = lambda x: round(x + 0.0, 3)  # noqa: E731
    amt = {k: sum(v) / 1000 for k, v in years.items()}

    def parts(owner, items):
        mid = r3(sum(a for _, a, _ in items))
        out = [(n, round(a, 4), pm) for n, a, pm in items]
        big = max(range(len(out)), key=lambda k: out[k][1])
        rest = sum(a for k, (_, a, _) in enumerate(out) if k != big)
        out[big] = (out[big][0], round(mid - rest, 4), out[big][2])
        return mid, out

    hlt4_mid, c4 = parts("HLT-4", [("ltc-hcbs-care-workforce", tn(part["ltc"]), None),
                                   ("safety-net-centers-residency-momnibus-title-x", tn(part["safety_net"]), None),
                                   ("children-continuous-coverage", amt["HLT-4/children-continuous-coverage"], 0.0),
                                   ("medicaid-dental-and-bundle", amt["HLT-4/medicaid-dental-and-bundle"], 0.0)])
    hlt7_mid, c7 = parts("HLT-7", [("plan-spending", amt["HLT-7/plan-spending"],
                                    perm_for(B, F, {2039: years["HLT-7/plan-spending"][-1]}, spend[2040])),
                                   ("transition-fund", amt["HLT-7/transition-fund"], 0.0),
                                   ("territories", amt["HLT-7/territories"],
                                    perm_for(B, F, {2039: years["HLT-7/territories"][-1]}, TERRITORIES_FY2040,
                                             "out_health_other"))])
    comps = {"HLT-4": c4, "HLT-7": c7}
    ledger = {
        "HLT-1": (r3(amt["HLT-1"]), r3(amt["HLT-1"]), r3(amt["HLT-1"] + 0.25)),   # HLT-1.03's provider-tax range, $0-0.25T
        "HLT-2": (0.31, r3(amt["HLT-2"]), 0.53),                                 # 0.25-0.35 upgrades + 0.06-0.18 wait
        "HLT-3": (0, 0, 0), "HLT-5": (0, 0, 0),
        "HLT-4": (r3(HLT4_LEGACY[0] * hlt4_mid / HLT4_LEGACY[1]), hlt4_mid, r3(HLT4_LEGACY[2] * hlt4_mid / HLT4_LEGACY[1])),
        "HLT-6": (r3(amt["HLT-6"]),) * 3,
        "HLT-7": (r3(hlt7_mid - RATE_RANGE_TN[0] - 0.05 - 0.04), hlt7_mid, r3(hlt7_mid + RATE_RANGE_TN[1] + 0.05 + 0.09)),
        "HLT-8": HLT8_TN,
        "HX": (r3(amt["HX"] * (1 - HALF_PASSTHROUGH_FY2040 / hp["excl"][2040])), r3(amt["HX"]), r3(amt["HX"])),
    }
    perms = {"HX": perm_for(B, F, {2039: years["HX"][-1]}, hp["excl"][2040])}
    fy2040 = dict(spending=spend[2040], exclusion=hp["excl"][2040], contribution=hp["contribution"][2040],
                  territories=TERRITORIES_FY2040, net=hp["net"][2040])
    totals = dict(net_window=sum(hp["net"][y] for y in W) / 1000,
                  with_contribution=(sum(hp["net"][y] for y in W) - sum(hp["contribution"][y] for y in W)) / 1000,
                  contribution_window=sum(hp["contribution"][y] for y in W) / 1000)
    return dict(years=years, components=comps, ledger=ledger, perms=perms, fy2040=fy2040, totals=totals,
                contribution={y: hp["contribution"][y] for y in W + [2040]})


if __name__ == "__main__":
    b = booking()
    if "--json" in sys.argv:
        print(json.dumps(b, indent=1, default=str))
    else:
        for k, v in b["years"].items():
            print(f"{k:40s} {sum(v)/1000:8.4f}T  {v}")
        print("ledger", b["ledger"])
        print("components", b["components"])
        print("perms", b["perms"])
        print("FY2040", {k: round(v, 1) for k, v in b["fy2040"].items()})
        print("totals", {k: round(v, 3) for k, v in b["totals"].items()})
