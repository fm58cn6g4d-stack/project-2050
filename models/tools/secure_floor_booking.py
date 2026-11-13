#!/usr/bin/env python3
"""secure_floor_booking.py: the secure floor's booking in the adopted inputs, derived from the dossier's path.

Role: the one place the secure floor's rows, year-by-year shapes and ten-year amounts are computed (secure floor
milestone review, step 7, F-2 and F-4; dossiers/secure-floor/6-cost.md part 6). Status: current. It reads the
dossier's fiscal-year path (dossiers/secure-floor/tools/secure_floor_path.py) and returns the numbers that
models/data/inputs/ (ledger-bills.csv, fiscal-years.csv, fiscal-components.csv, fiscal-profiles.csv,
funds-parameters.csv) and models/tools/recovery-budget/assumptions.json hold. test_fiscal_secure_floor.py checks
that the inputs equal them, so a change to the dossier's path shows up as a failing test rather than a silent drift.

    python3 models/tools/secure_floor_booking.py           # the rows and the totals
    python3 models/tools/secure_floor_booking.py --json    # the same as JSON

What is booked (central path, $ billion by federal fiscal year; a cost positive):
- FAM-1 (R1), as components: the child benefit at the decided path, the American Family Act without the $2,200
  floor (DEC-2026-11-12-06, point 2): $1.85T over FY2030-39 (range 1.65-2.05) on the CPI profile it had, in place
  of $1.9T (6-cost.md part 1, "Memo 1 A without the floor"); delivery (FAM-1.04 the child's own ID, FAM-1.06 the
  repayment safe harbor, FAM-1.08-1.10 records-based delivery) on the path; and the two lines part 2 leaves to the
  booking, each at the middle of its range (judgment): no offset or garnishment of the benefit (FAM-1.07, review
  B-1, the federal-debt and federal-tax share, $1-3B a year) and the territories' child benefit (FAM-1.07, review
  M-1, about 0.6 million children, $1-3B a year).
- INC-1 to INC-5 (R1, general fund), one years row each on the path: the childless earned income credit, SNAP
  restored, SNAP's earned income deduction at 45% (INC-2B, INC-2.02: Espen's option D on the 65-cent ceiling,
  DEC-2026-11-13-03; its own row so its range and incidence key stay its own), SSI (the asset limits, the indexed exclusions and SSI in the four territories, INC-3.03), the refundable
  dependent care credit, and the exclusion rule's forgone offsets.
- LAB-10: unchanged, the participation envelope ($0.1T, recovery-adoption.json), now named for LAB-10.
- FAM-3: the leave fund's step from 0.05 to 0.10 points (funds-parameters.csv leave_step; Espen, November 12).
- Social Security (recovery-budget/assumptions.json, social_security): the two-point broad rate phased in over
  2035-44 is replaced by SS-7.01's one point, its expected path (6-cost.md part 4): 0.1 point a year from 2037 to
  the full point in 2046. SS-8's reserve investment is recorded at zero in the budget and flagged: how the budget
  records the trust funds' stock purchases is not settled (6-cost.md part 4; review F-2).
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
W = list(range(2030, 2040))
FY = list(range(2030, 2041))
GROW = "cpi"   # every line here is fixed in dollars or indexed to prices (6-cost.md part 5, "permanent cost")

# The child benefit, decided: the legacy planning range less the declined floor (6-cost.md part 1 and part 6 item 1)
BENEFIT_TN = (1.65, 1.85, 2.05)
# Part 2's two lines left to the booking: the middle of each $1-3B range in calendar 2030, prices, paid monthly
B1_M1_CY2030_BN = (1.0, 2.0, 3.0)
PRICES = 0.023     # the path's own price growth (secure_floor_path.py)
# Each new row's range, from 6-cost.md part 7 (sensitivities) and the provisions' own ranges in section 4
RANGES = {
    "INC-1": (0.13, 0.16),     # JCT and TPC [EV-SEC-609] [EV-SEC-610]
    "INC-2": (0.20, 0.25),     # CBO's window's later years [EV-SEC-035] [EV-SEC-038]
    "INC-2B": (0.092, 0.183),  # INC-2.02: $8-16B in FY2030 on the path's growth (6-cost.md part 1; DEC-2026-11-13-03)
    "INC-3": (0.034, 0.058),   # INC-3.03 $15-30B (4-specification.md); 3.01-3.02 within 20% (judgment)
    "INC-4": (0.03, 0.06),     # section 3, point 7
    "INC-5": (0.01, 0.03),     # memo 7 part 1 B, $1-3B a year
}

# Each row's component and the path lines it takes
FAM1_PARTS = {
    "delivery": ["FAM-1.04, the child's own ID (part 2 B)", "FAM-1.08-1.10, records-based delivery (memo 2 B)",
                 "FAM-1.06, the repayment safe harbor (point 4)"],
}
INC_ROWS = {
    "INC-1": ["INC-1.01, the childless earned income credit (memo 3 part 1 B)"],
    "INC-2": ["INC-2.01, SNAP restored (memo 3 part 2 B)"],
    "INC-2B": ["INC-2.02, SNAP's earned income deduction at 45% (Espen's option D)"],
    "INC-3": ["INC-3.01, SSI's asset limits (memo 3 part 2 B)", "INC-3.02, SSI's exclusions indexed (point 8)",
              "INC-3.03, SSI in the territories (Espen, November 12)"],
    "INC-4": ["INC-4.01, the refundable dependent care credit (point 7)"],
    "INC-5": ["INC-5.01, the exclusion rule (memo 7 part 1 B)"],
}
BOOKED = ("FAM-1, as booked (memo 1 A, legacy planning range)", "less: the $2,200 floor, declined (point 2)",
          "LAB-10, as booked (memo 4 B, inside the envelope)")

# Social Security (memo 6 C as decided, DEC-2026-11-12-06; 6-cost.md part 4): SS-7.01's one point as the expected
# path. Its trigger reads the Trustees reports from 2035; the first 0.1-point step comes about 2037, the full point
# about 2046.
SS7 = dict(fallback_rate_points=1, fallback_start=2037, fallback_phase_years=10)
# SS-8: up to 20% of reserves in a stock index from 2032; about +0.05 to +0.2% of payroll on the trust funds
# (6-cost.md part 4). Recorded at zero in the budget: how the stock purchases are recorded is open.
SS8_BOOKED_PAYROLL_POINTS = 0.0
SS8_RANGE_PAYROLL_POINTS = (0.05, 0.2)
# FAM-3.04: the step (Espen, November 12, lead session; review A-1)
LEAVE_STEP = 0.10


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def path_module():
    return _load("secure_floor_path", os.path.join(ROOT, "dossiers", "secure-floor", "tools", "secure_floor_path.py"))


def fiscal():
    return _load("sfb_fiscal", os.path.join(HERE, "fiscal-model.py"))


def b1_m1(P, i):
    """FAM-1.07's two lines (review B-1, M-1) for reading i (0 low, 1 central, 2 high): monthly from January 2030."""
    return P.monthly_to_fy(P.grown(2030, B1_M1_CY2030_BN[i], PRICES))


def window(d):
    return [round(d.get(y, 0.0) + 0.0, 2) for y in W]


def r3(x):
    return round(x + 0.0, 3)


def perm_for(F, B, v2039, v2040, grow=GROW):
    """The perm that makes a years row's FY2040 equal v2040 (row_path: FY2039 x perm x growth)."""
    if abs(v2039) < 1e-12:
        return 0.0
    g = F.growth_index(B, grow)
    return v2040 / (v2039 * g[2040] / g[2039])


def total(paths):
    return {y: sum(p.get(y, 0.0) for p in paths) for y in FY}


def booking():
    P = path_module()
    F = fiscal()
    B = F.read_baseline(os.path.join(ROOT, "models", "data", "fiscal-baseline.csv"))
    L = P.lines()
    used = set(BOOKED) | {k for v in FAM1_PARTS.values() for k in v} | {k for v in INC_ROWS.values() for k in v}
    missing = set(L) - used
    if missing:
        raise ValueError("secure_floor_path.py lines not booked: %s" % sorted(missing))

    years, perms, ledger, fy2040, rows_fy = {}, {}, {}, {}, {}
    # FAM-1: the benefit on its CPI profile, then the path's components
    lines = {"delivery": total([L[k] for k in FAM1_PARTS["delivery"]]),
             "offset-protection": b1_m1(P, 1), "territories": b1_m1(P, 1)}
    parts = []
    for name, s in lines.items():
        key = "FAM-1/" + name
        years[key] = window(s)
        fy2040[key] = s[2040]
        parts.append([name, round(sum(years[key]) / 1000, 4), perm_for(F, B, years[key][-1], s[2040])])
    mid = r3(BENEFIT_TN[1] + sum(a for _, a, _ in parts))
    # The ledger keeps $1 billion; the benefit stays at the decided $1.85T and delivery takes the rounding
    parts[0][1] = round(mid - BENEFIT_TN[1] - sum(a for _, a, _ in parts[1:]), 4)
    comps = [("benefit", BENEFIT_TN[1], None)] + [tuple(p) for p in parts]
    other_lo = parts[0][1] + 2 * sum(b1_m1(P, 0)[y] for y in W) / 1000
    other_hi = parts[0][1] + 2 * sum(b1_m1(P, 2)[y] for y in W) / 1000
    ledger["FAM-1"] = (r3(BENEFIT_TN[0] + other_lo), mid, r3(BENEFIT_TN[2] + other_hi))
    g = F.growth_index(B, GROW)
    booked_fam1 = dict(zip(FY, P.BOOKED_FAM1))
    benefit = {y: booked_fam1[y] * BENEFIT_TN[1] / 1.9 for y in FY}   # the CPI profile scaled to $1.85T
    rows_fy["FAM-1"] = total([benefit] + list(lines.values()))
    # INC-1 to INC-5: one years row each
    for rid, keys in INC_ROWS.items():
        s = total([L[k] for k in keys])
        years[rid] = window(s)
        fy2040[rid] = s[2040]
        perms[rid] = perm_for(F, B, years[rid][-1], s[2040])
        lo, hi = RANGES[rid]
        ledger[rid] = (lo, r3(sum(years[rid]) / 1000), hi)
        rows_fy[rid] = s
    rows_fy["LAB-10"] = dict(zip(FY, P.BOOKED_LAB10))

    tn = lambda s: sum(s.get(y, 0.0) for y in W) / 1000  # noqa: E731
    dossier = total(list(L.values()))
    booked = total(list(rows_fy.values()))
    before = total([L[BOOKED[0]], L[BOOKED[2]]])
    extra = total([lines["offset-protection"], lines["territories"]])
    totals = dict(dossier_window=tn(dossier), dossier_fy2040=dossier[2040], booked_window=tn(booked),
                  booked_fy2040=booked[2040], before_window=tn(before), before_fy2040=before[2040],
                  b1_m1_window=tn(extra), b1_m1_fy2040=extra[2040])
    return dict(years=years, components={"FAM-1": comps}, ledger=ledger, perms=perms, fy2040=fy2040,
                totals=totals, rows_fy={k: {y: round(v[y], 3) for y in FY} for k, v in rows_fy.items()},
                social_security=dict(SS7, reserve_investment_booked_payroll_points=SS8_BOOKED_PAYROLL_POINTS),
                leave_step=LEAVE_STEP, growth_index_2040_2039=g[2040] / g[2039])


if __name__ == "__main__":
    b = booking()
    if "--json" in sys.argv:
        print(json.dumps(b, indent=1, default=str))
    else:
        for k, v in b["years"].items():
            print(f"{k:28s} {sum(v)/1000:8.4f}T  FY2040 {b['fy2040'][k]:7.2f}  {v}")
        print("ledger", b["ledger"])
        print("components", [(n, a, round(pm, 6) if pm is not None else None) for n, a, pm in b["components"]["FAM-1"]])
        print("perms", {k: round(v, 6) for k, v in b["perms"].items()})
        print("totals", {k: round(v, 3) for k, v in b["totals"].items()})
        print("social security", b["social_security"], "leave step", b["leave_step"])
