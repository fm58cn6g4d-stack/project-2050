#!/usr/bin/env python3
"""immigration_booking.py: the immigration dossier's booking in the adopted inputs, derived from the dossier's path.

Role: the one place the immigration rows, year-by-year shapes and ten-year amounts are computed (immigration
milestone review, step 5; dossiers/immigration/6-cost.md part 6). Status: current. It reads the dossier's
fiscal-year path (dossiers/immigration/tools/immigration_path.py) and returns the numbers that
models/data/inputs/ (ledger-bills.csv, ledger-revenue.csv, fiscal-years.csv, fiscal-components.csv,
fiscal-profiles.csv) hold. test_fiscal_immigration.py checks that the inputs equal them, so a change to the
dossier's path shows up as a failing test rather than a silent drift.

    python3 models/tools/immigration_booking.py           # the rows and the totals
    python3 models/tools/immigration_booking.py --json    # the same as JSON

What is booked (central path, $ billion by federal fiscal year; a cost positive):
- IMM-1 (ledger E11), the legacy "S.744 pattern" saving replaced by the decided set's spending, as components on
  the path: status and the registry (memos 1-2), the one eligibility table with the single plan for lawful or
  registered status and IMM-1.15's returnees (memo 6 as amended for health, Espen, November 12), legal immigration
  and the work routes (memo 3), asylum, refugees, counsel and the judge teams (memo 4, point 8), enforcement and
  E-Verify's operations (memo 5), and USCIS (memo 7). Point 7's wall money is zero against CBO's baseline.
- Two revenue effects, each its own base-revenue row on the path (6-cost.md, "Counting rules"): E-Verify's
  on-budget revenue under JCT's convention (IMM-EV, a gain) and the income-tax offset on the retained H-1B fee
  (IF1T, a loss). IF1's fee receipts stay outside the general fund, spent within receipts.
- CAP-7S's $40 billion USCIS share and CAP-7's pro-rata USCIS share (7%) go to zero: IMM-1's USCIS and asylum
  lines carry USCIS's public-interest work (6-cost.md part 4; point 9).
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
W = list(range(2030, 2040))
FY = list(range(2030, 2041))
GROW = "gdp"   # coverage, status and the agencies grow with the economy after 2040 (6-cost.md part 5)

# IMM-1's components and the path lines each takes (immigration_path.lines(), by label prefix)
COMPONENTS = {
    "status": ["IMM-1.01-1.14:", "IMM-1.05-1.09:"],
    "table": ["IMM-1.20-1.36:"],
    "legal": ["IMM-2.01-2.12:"],
    "asylum-courts": ["IMM-3.01-3.04, 3.12:", "IMM-3.08:", "IMM-3.06:"],
    "enforcement": ["IMM-4.05-4.06:", "IMM-4.01-4.02, 4.09:", "IMM-4.12-4.15:"],
    "uscis": ["IMM-6.01, IMM-5.04:"],
    None: ["IMM-3.07:"],   # wall money redirected: zero against CBO's baseline, not booked
}
REVENUE = {"IMM-EV": "IMM-4.12: E-Verify mandate, on-budget revenue", "IF1T": "IF1: income-tax offset"}
# CAP-7S and CAP-7, as booked, and USCIS's shares of each (legacy/domains/domain-capacity.md, lines 127 and 149)
CAP7S = (0.45, 0.6, 0.75)
CAP7S_USCIS = 0.04
CAP7S_PROXY = (70, 120, 130, 120, 100, 60, 0, 0, 0, 0)   # the cash proxy as booked before (fiscal-years.csv)
CAP7 = (0.4, 0.49, 0.6)
CAP7_USCIS_SHARE = 0.07


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def path_module():
    tools = os.path.join(ROOT, "dossiers", "immigration", "tools")
    if tools not in sys.path:
        sys.path.insert(0, tools)
    return _load("immigration_path", os.path.join(tools, "immigration_path.py"))


def fiscal():
    return _load("imb_fiscal", os.path.join(HERE, "fiscal-model.py"))


def r(x, n=4):
    return round(x + 0.0, n)


def window(d):
    return [round(d.get(y, 0.0) + 0.0, 2) for y in W]


def perm_for(F, B, v2039, v2040, grow=GROW):
    """The perm that makes a years row's FY2040 equal v2040 (row_path: FY2039 x perm x growth)."""
    if abs(v2039) < 1e-12:
        return 0.0
    g = F.growth_index(B, grow)
    return v2040 / (v2039 * g[2040] / g[2039])


def pick(lines, prefix):
    hits = [k for k in lines if k.startswith(prefix)]
    if len(hits) != 1:
        raise ValueError("immigration_path.py line %r matched %d times" % (prefix, len(hits)))
    return hits[0]


def booking():
    P = path_module()
    F = fiscal()
    B = F.read_baseline(os.path.join(ROOT, "models", "data", "fiscal-baseline.csv"))
    spend, rev = P.lines(), P.revenue_lines()
    used = {pick(spend, p) for ps in COMPONENTS.values() for p in ps}
    if set(spend) - used:
        raise ValueError("immigration_path.py lines not booked: %s" % sorted(set(spend) - used))

    years, comps, fy2040, lo_hi = {}, [], {}, {}
    for name, prefixes in COMPONENTS.items():
        if name is None:
            continue
        keys = [pick(spend, p) for p in prefixes]
        s = {y: sum(spend[k][0][y] for k in keys) for y in FY}
        key = "IMM-1/" + name
        years[key] = window(s)
        fy2040[key] = s[2040]
        comps.append((name, r(sum(years[key]) / 1000), perm_for(F, B, years[key][-1], s[2040])))
        lo_hi[name] = (sum(spend[k][1] for k in keys) / 1000, sum(spend[k][2] for k in keys) / 1000)
    # The ledger keeps $1 billion (ledger-build.py rounds to three decimals); the table takes the rounding
    mid = r(sum(a for _, a, _ in comps), 3)
    i = [c[0] for c in comps].index("table")
    comps[i] = ("table", r(mid - sum(a for nm, a, _ in comps if nm != "table")), comps[i][2])
    ledger = {"IMM-1": (r(sum(v[0] for v in lo_hi.values()), 3), mid, r(sum(v[1] for v in lo_hi.values()), 3))}

    revenue, rperms = {}, {}
    for rid, prefix in REVENUE.items():
        p, lo, hi, lo40, hi40 = rev[pick(rev, prefix)]
        years[rid] = window(p)
        fy2040[rid] = p[2040]
        rperms[rid] = perm_for(F, B, years[rid][-1], p[2040])
        m = -sum(years[rid]) / 1000                # revenue: a gain is positive in ledger-revenue.csv
        ends = sorted([-lo / 1000, -hi / 1000])
        revenue[rid] = (r(ends[0]), r(m), r(ends[1]))

    # CAP-7S's interim cash proxy (fiscal-years.csv) must add to its lifetime amount (capacity-funding.py):
    # the USCIS share comes out of each year pro rata, the last year taking the cent's rounding
    k = (CAP7S[1] - CAP7S_USCIS) / CAP7S[1]
    proxy = [round(v * k, 2) for v in CAP7S_PROXY]
    proxy[0] = round(proxy[0] + (CAP7S[1] - CAP7S_USCIS) * 1000 - sum(proxy), 2)
    years["CAP-7S"] = proxy
    cap = {"CAP-7S": tuple(r(x - CAP7S_USCIS, 3) for x in CAP7S),
           "CAP-7": tuple(r(x * (1 - CAP7_USCIS_SHARE), 4) for x in CAP7)}

    tn = lambda d: sum(d.get(y, 0.0) for y in W) / 1000  # noqa: E731
    all_ = {y: sum(v[0][y] for v in list(spend.values()) + list(rev.values())) for y in FY}
    totals = dict(dossier_window=tn(all_), dossier_fy2040=all_[2040],
                  spending_window=mid, revenue_window=-sum(v[1] for v in revenue.values()),
                  cap_window=(CAP7S[1] - cap["CAP-7S"][1]) + (CAP7[1] - cap["CAP-7"][1]))
    return dict(years=years, components={"IMM-1": comps}, ledger=ledger, revenue=revenue, revenue_perms=rperms,
                fy2040=fy2040, cap=cap, totals=totals)


if __name__ == "__main__":
    b = booking()
    if "--json" in sys.argv:
        print(json.dumps(b, indent=1, default=str))
    else:
        for k, v in b["years"].items():
            print(f"{k:24s} {sum(v)/1000:8.4f}T  FY2040 {b['fy2040'][k]:7.2f}  {v}")
        print("ledger", b["ledger"])
        print("components", [(n, a, round(pm, 6)) for n, a, pm in b["components"]["IMM-1"]])
        print("revenue", b["revenue"], {k: round(v, 6) for k, v in b["revenue_perms"].items()})
        print("cap", b["cap"])
        print("totals", {k: round(v, 4) for k, v in b["totals"].items()})
