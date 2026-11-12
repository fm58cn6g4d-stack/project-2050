#!/usr/bin/env python3
"""care_booking.py: care parts B-D's booking in the adopted inputs, derived from the care dossier's path.

Role: the one place the care rows' year-by-year shapes and ten-year amounts are computed (care parts B-D milestone
review, step 8 and F-3; dossiers/care/6bcd-cost.md part 5). Status: current. It reads the dossier's fiscal-year path
(dossiers/care/tools/care_bcd_path.py, which imports care_repricing.py) and health's parts of HLT-4
(health_booking.py), and returns the numbers that models/data/inputs/ (ledger-bills.csv, fiscal-years.csv,
fiscal-components.csv, fiscal-profiles.csv, incidence-*.csv, ledger-dynamic.csv) hold. test_fiscal_care.py checks
that the inputs equal them, so a change to the dossier's path shows up as a failing test rather than a silent drift.

    python3 models/tools/care_booking.py           # the rows and the totals
    python3 models/tools/care_booking.py --json    # the same as JSON

What is booked (central path, $ billion by federal fiscal year; a cost positive). Every line of care_bcd_path.py's
decided path and of part 2's items goes to exactly one row, by the vehicle section 4 gives it
(dossiers/care/4bcd-specification.md, "The vehicles"):
- HLT-4 (the 2029 reconciliation act, R1): HLT-4's legacy long-term care component (0.3194, "HCBS down payment and
  care workforce") is retired; in its place the bridge (HLT-4.01), the care wage floor in Medicaid in 2030-34
  (HLT-10.01's Medicaid part), the training and supply money (HLT-10.06, 10.07), the small items (HLT-4.02-4.04,
  4.07) and the territories' bridge and floor outside the capped allotments (M-1). Health's parts (safety net,
  children's coverage, Medicaid dental) are unchanged.
- HLT-9 (the Medicare for All Act's long-term care title, regular order): the home and community care benefit and
  the care part of institutional care booked gross, with the states' long-term care payment (HLT-9.09) as an
  offsetting receipt on HLT-7.17's offset instrument, its own negative component, labeled with the joint-failure
  risk (review F-1); the state option below the line and room-and-board help (HLT-4.08, 9.08; B-1), which exist
  only with the title; the territories' long-term care (M-1).
- HLT-10 (the same act): the floor in the plan's rates from 2035, net of option 4's delay on new users' hours.
- HLT-11 (the same act): the nursing home staffing standard.
- FAM-2 (reconciliation on the FY2030 budget resolution, R2): child care at the decided shares with labor grown with
  wages, pre-K, the facilities fund, CCDF kept for school-age children (M-2), the territories (M-1) and early
  educators' pay (FAM-2G.01, in FAM-2's payment rules). In case `mixed` of the recovery budget FAM-2 is carried by
  the EDU-9B fund, whose care component now reads FAM-2's booked path (recovery-budget/model.py), so part C is
  counted in one place.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
W = list(range(2030, 2040))
FY = list(range(2030, 2041))
LTC_GROW = "out_medicare_net"     # part B grows 5.5% a year (3b); CBO's Medicare category is the nearest, as HLT-7's
OTHER_GROW = "out_health_other"   # small Medicaid items, staffing and training
CARE_GROW = "gdp"                 # child care and pre-K track wages after 2040, as FAM-2's legacy profile did
LEGACY_FAM2_TN = 0.6              # FAM-2's legacy ledger midpoint (DY6 was sized against it)


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def path_module():
    return _load("care_bcd_path", os.path.join(ROOT, "dossiers", "care", "tools", "care_bcd_path.py"))


# Each row's component and the path lines it takes ((line name, sign) pairs; "D" lines are part 1's decided lines,
# "X" lines part 2's items). MOE lines are added below: the states' payment, gross and receipt.
ROWS = {
    "HLT-4": [
        ("bridge", OTHER_GROW, [("D", "B bridge (point 1)")],
         "HLT-4.01, the bridge: 6 entry points from FY2030, up to 4 progress points from FY2032, to December 31, 2034"),
        ("care-floor-in-medicaid", OTHER_GROW, [("D", "D floor, bridge (memo 14)")],
         "HLT-10.01's Medicaid part: the $20 care wage floor in Medicaid home care, 2030-34, at each state's bridge rate"),
        ("training-and-supply", OTHER_GROW, [("D", "D points 5 and 7")],
         "HLT-10.06 and 10.07: training money and health supply, about $2B a year"),
        ("small-items", OTHER_GROW, [("X", "B small items (points 2-4, 6)")],
         "HLT-4.02-4.04 and 4.07: Money Follows the Person, the resource limits, no estate recovery, CAPABLE"),
        ("territories-bridge-floor", OTHER_GROW, [("X", "Territories: bridge and floor outside the cap (M-1)")],
         "M-1: the territories' bridge points and floor outside the capped allotments, 2030-34"),
    ],
    "HLT-9": [
        ("home-care-benefit", LTC_GROW,
         [("D", "B memo6b"), ("D", "B below_line"), ("D", "B opt2"), ("D", "B opt4"), ("MOE", "home")],
         "HLT-9.01-9.07: the home and community care benefit from January 1, 2035 (memo 6 B, three activities, the "
         "hold-harmless; options 2 and 4; people below the line out), gross of the states' payment"),
        ("institutional-care-part", LTC_GROW, [("D", "B memo8c"), ("D", "B opt5"), ("MOE", "inst")],
         "HLT-9.08: the care part of institutional care (memo 8 C; option 5), gross of the states' payment"),
        ("states-payment", LTC_GROW, [("MOE", "-home"), ("MOE", "-inst")],
         "HLT-9.09: states' long-term care payment, 50% of current spending, indexed: offsetting receipts collected "
         "by offset on HLT-7.17's instrument (negative outlays)"),
        ("state-option-below-line", LTC_GROW, [("D", "B state_option")],
         "HLT-4.08: the state option below the line at the regular match"),
        ("room-and-board", LTC_GROW, [("X", "B room and board without an asset test (B-1)")],
         "HLT-4.08, 9.08 (B-1): room-and-board help income-tested only from 2035"),
        ("territories", LTC_GROW, [("X", "Territories: long-term care from 2035 (M-1)")],
         "HLT-9.01 (M-1): the territories' long-term care from 2035"),
    ],
    "HLT-10": [
        ("floor-in-plan-rates", LTC_GROW, [("D", "D floor, plan (memo 14)"), ("X", "D floor delayed with option 4")],
         "HLT-10.01: the care wage floor in the plan's rates from 2035, net of option 4's delay on new users' hours"),
    ],
    "HLT-11": [
        ("staffing", OTHER_GROW, [("D", "D staffing (memo 16)")],
         "HLT-11.01-11.05: RN around the clock and 0.55 RN hours from 2031, 3.48 total hours from 2035"),
    ],
    "FAM-2": [
        ("child-care", CARE_GROW,
         [("D", "C child_care"), ("D", "C state_share_cut"), ("X", "C wage growth in labor (3d)")],
         "FAM-2.01, 2.08: the capped-cost guarantee at 90%, 80% from 2033-34, labor grown with wages (3d)"),
        ("pre-k", CARE_GROW, [("D", "C pre_k")], "FAM-2.02: pre-K, 90% then 75% of the cost above states' spending"),
        ("facilities", CARE_GROW, [("D", "C facilities")], "FAM-2.05: the facilities fund, $5B a year for five years"),
        ("ccdf-school-age", CARE_GROW, [("X", "C CCDF kept for school-age children (M-2)")],
         "FAM-2.04 (M-2): CCDF kept as a block grant for children 5 to 12, indexed to prices"),
        ("territories", CARE_GROW, [("X", "Territories: child care and pre-K (M-1)")],
         "FAM-2.07 (M-1): the territories' child care and pre-K"),
        ("educator-pay", CARE_GROW, [("D", "D parity (memo 15)")],
         "FAM-2G.01: early educators' floor and salary scale to parity in 2036-37, at child care's share"),
    ],
}
# Health's parts of HLT-4, kept as booked (health_booking.py derives them)
HEALTH_HLT4 = ("safety-net-centers-residency-momnibus-title-x", "children-continuous-coverage",
               "medicaid-dental-and-bundle")
RETIRED = ("HLT-4", "ltc-hcbs-care-workforce", 0.3194)


def moe(P):
    """States' long-term care payment (HLT-9.09), calendar years from 2035, by part: 50% of states' 2035 home and
    institutional spending (47% state share), indexed with the line (care_bcd_path.py main(); 6bcd-cost.md part 3)."""
    R = P.R
    home35 = R.STATE_LTC_SHARE * R.medicaid_home(2035) * 0.5 / 1e9
    inst35 = R.STATE_LTC_SHARE * R.MEDICAID_INST_2023 * R.GROWTH ** 12 * 0.5 / 1e9
    cy = lambda v: {y: v * R.GROWTH ** (y - 2035) for y in range(2035, 2041)}  # noqa: E731
    return {"home": P.fy_from_cy(cy(home35)), "inst": P.fy_from_cy(cy(inst35))}


def lines_for(P, i):
    """Each row component's fiscal-year path for reading i (0 low, 1 central, 2 high)."""
    d, x, _ = P.fy_lines(i)
    m = moe(P)
    out = {}
    for owner, comps in ROWS.items():
        for name, _, srcs, _ in comps:
            s = {y: 0.0 for y in FY}
            for kind, key in srcs:
                if kind == "MOE":
                    sign, k = (-1.0, key[1:]) if key.startswith("-") else (1.0, key)
                    src = {y: sign * m[k].get(y, 0.0) for y in FY}
                else:
                    src = (d if kind == "D" else x)[key]
                for y in FY:
                    s[y] += src.get(y, 0.0)
            out[(owner, name)] = s
    used = {k for comps in ROWS.values() for _, _, srcs, _ in comps for kind, k in srcs if kind in ("D", "X")}
    missing = (set(d) | set(x)) - used
    if missing:
        raise ValueError("care_bcd_path.py lines not booked: %s" % sorted(missing))
    return out, d, x


def fiscal():
    return _load("cb_fiscal", os.path.join(HERE, "fiscal-model.py"))


def health_hlt4():
    """Health's HLT-4 parts as health_booking.py derives them: [(name, amount $T, perm or None)]."""
    HB = _load("cb_health_booking", os.path.join(HERE, "health_booking.py"))
    return HB, HB.booking()["hlt4_parts"]


def perm_for(F, B, v2039, v2040, grow):
    """The perm that makes a years row's FY2040 equal v2040 (row_path: FY2039 x perm x growth)."""
    if abs(v2039) < 1e-12:
        return 0.0
    g = F.growth_index(B, grow)
    return v2040 / (v2039 * g[2040] / g[2039])


def window(d):
    return [round(d.get(y, 0.0) + 0.0, 2) for y in W]


def r3(x):
    return round(x + 0.0, 3)


def booking():
    P = path_module()
    F = fiscal()
    B = F.read_baseline(os.path.join(ROOT, "models", "data", "fiscal-baseline.csv"))
    central, d, x = lines_for(P, 1)
    low, _, _ = lines_for(P, 0)
    high, _, _ = lines_for(P, 2)
    tn = lambda s: sum(s.get(y, 0.0) for y in W) / 1000  # noqa: E731

    years, comps, ledger, fy2040, rows_fy, perms = {}, {}, {}, {}, {}, {}
    HB, hlt4_health = health_hlt4()
    for owner, items in ROWS.items():
        parts = []
        for name, grow, _, _ in items:
            s = central[(owner, name)]
            key = "%s/%s" % (owner, name)
            years[key] = window(s)
            amount = sum(years[key]) / 1000
            parts.append((name, amount, perm_for(F, B, years[key][-1], s[2040], grow), grow))
            fy2040[key] = s[2040]
        if owner == "HLT-4":
            parts = [(n, a, pm, None) for n, a, pm in hlt4_health] + parts
        # The ledger keeps $1 billion; components keep $0.1 billion and the largest part takes the rounding, so the
        # parts add to the ledger amount exactly (health_booking.py's rule).
        mid = r3(sum(a for _, a, _, _ in parts))
        out = [(n, round(a, 4), pm, g) for n, a, pm, g in parts]
        big = max((k for k in range(len(out)) if out[k][3] is not None), key=lambda k: abs(out[k][1]))
        rest = sum(a for k, (_, a, _, _) in enumerate(out) if k != big)
        out[big] = (out[big][0], round(mid - rest, 4), out[big][2], out[big][3])
        if len(items) == 1 and owner != "HLT-4":     # one line: a years bill (fiscal-years.csv row keyed by the bill)
            years[owner] = years.pop("%s/%s" % (owner, items[0][0]))
            fy2040[owner] = fy2040.pop("%s/%s" % (owner, items[0][0]))
            perms[owner] = out[0][2]
        else:
            comps[owner] = out
        lo = sum(tn(low[(owner, n)]) for n, _, _, _ in items)
        hi = sum(tn(high[(owner, n)]) for n, _, _, _ in items)
        if owner == "HLT-4":    # health's parts keep their legacy range (0.40-0.85 on 0.625)
            h = sum(a for _, a, _ in hlt4_health)
            lo += h * HB.HLT4_LEGACY[0] / HB.HLT4_LEGACY[1]
            hi += h * HB.HLT4_LEGACY[2] / HB.HLT4_LEGACY[1]
        ledger[owner] = (r3(lo), mid, r3(hi))
        rows_fy[owner] = {y: sum(central[(owner, n)][y] for n, _, _, _ in items) for y in FY}

    decided = {y: sum(s.get(y, 0.0) for s in d.values()) for y in FY}
    allin = {y: decided[y] + sum(s.get(y, 0.0) for s in x.values()) for y in FY}
    booked = {y: sum(r[y] for r in rows_fy.values()) for y in FY}
    m = moe(P)
    receipts = {y: m["home"].get(y, 0.0) + m["inst"].get(y, 0.0) for y in FY}
    totals = dict(decided_window=tn(decided), decided_fy2040=decided[2040], allin_window=tn(allin),
                  allin_fy2040=allin[2040], booked_window=tn(booked), booked_fy2040=booked[2040],
                  receipts_window=tn(receipts), receipts_fy2040=receipts[2040],
                  retired_component_tn=RETIRED[2])
    return dict(years=years, components=comps, ledger=ledger, perms=perms, fy2040=fy2040, totals=totals,
                rows_fy={k: {y: round(v[y], 3) for y in FY} for k, v in rows_fy.items()})


# ---- the household test (D3): F2, H4 and a new H9 row, and the dynamic sensitivity DY6 ----
# HLT-9's key (review F-3 item 3; 7bcd-validation.md, "a benefit with no asset test reaches higher quintiles than
# Medicaid does"): the part that relieves today's Medicaid users and their states (states' relief and richer budgets
# for today's users, 2035 central) on medicaid_ltc; the new users and the care part of institutional care, who now
# pay out of pocket or give unpaid care, on the older population's income distribution (the medicare key). Estimate.
MEDICAID_LTC_KEY = ((50, 25, 14, 7, 4), 0)
MEDICARE_KEY = ((24, 26, 21, 16, 13), 1)


def close(q):
    """Shares rounded to 0.1 that add to exactly 100 (the largest takes the rounding)."""
    q = [round(v, 1) for v in q]
    big = q.index(max(q))
    q[big] = round(100 - sum(v for k, v in enumerate(q) if k != big), 1)
    return q


def ltc_universal_key():
    P = path_module()
    R = P.R
    today = (R.RELIEF_2035[1] + R.RICHER_2035[1]) / 1e9
    new = P.newb[1] + R.MEMO8C_2035[1] / 1e9
    w = new / (today + new)
    (qa, ta), (qb, tb) = MEDICAID_LTC_KEY, MEDICARE_KEY
    return close([(1 - w) * a + w * b for a, b in zip(qa, qb)]), round((1 - w) * ta + w * tb, 1), w


def incidence():
    """The household test's care rows: F2 ([FAM-2]) and H4 ([HLT-4]) keep their keys with the booked shapes; H9
    ([HLT-9]) on its own key. Shapes are each booked fiscal-year path scaled to its largest year (method norm)."""
    b = booking()
    HB = _load("cb_health_booking2", os.path.join(HERE, "health_booking.py"))
    hlt4_health = HB.booking()["hlt4_path"]
    sc = lambda v: [round(t / max(v, key=abs), 3) + 0.0 if max(v, key=abs) else 0.0 for t in v]  # noqa: E731
    rows = b["rows_fy"]
    hlt4 = [hlt4_health[k] + rows["HLT-4"][y] for k, y in enumerate(W)]
    key, top1, w = ltc_universal_key()
    return dict(shapes={"F2": sc([rows["FAM-2"][y] for y in W]), "H4": sc(hlt4), "H9": sc([rows["HLT-9"][y] for y in W])},
                key={"ltc_universal": (key, top1)}, new_user_weight=w)


def dynamic_dy6():
    """DY6 (parents' added employment from FAM-2, FAM-3, EDU-1) scaled with FAM-2's child care and pre-K amount
    (educators' pay left out), so it keeps the legacy row's ratio to the program it follows (6bcd-cost.md part 5
    item 9). An upper reading: the row's FAM-3 and EDU-1 parts are not separated, so they scale too."""
    b = booking()
    care = sum(a for n, a, _, _ in b["components"]["FAM-2"] if n != "educator-pay")
    r = care / LEGACY_FAM2_TN
    legacy = (0.15, 0.22, 0.30, 0.40)
    return tuple(round(v * r, 2) for v in legacy), r


if __name__ == "__main__":
    b = booking()
    if "--json" in sys.argv:
        print(json.dumps(dict(b, incidence=incidence(), dy6=dynamic_dy6()), indent=1, default=str))
    else:
        for k, v in b["years"].items():
            print(f"{k:42s} {sum(v)/1000:8.4f}T  FY2040 {b['fy2040'][k]:7.1f}  {v}")
        print("ledger", b["ledger"])
        for o, c in b["components"].items():
            print("components", o, [(n, a, round(pm, 6) if pm is not None else None) for n, a, pm, _ in c])
        print("perms", b["perms"])
        print("totals", {k: round(v, 3) for k, v in b["totals"].items()})
        print("incidence", incidence())
        print("dy6", dynamic_dy6())
