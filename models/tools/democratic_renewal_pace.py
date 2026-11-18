#!/usr/bin/env python3
"""democratic_renewal_pace.py: can the agency rebuild's sustained money be spent at the pace agencies can hire?

Role: democratic renewal's section 7 check of CAP-7.01's booked path against the hiring pace sections 3 and 5
assume (dossiers/foundations/democratic-renewal/7-validation.md, part 2). Status: draft (stage F, step 7). It books
nothing and writes nothing: it reads the booked CAP-7 path through democratic_renewal_cost.py (the budget model's
audit lines, case `mixed`, at the October 26 scaling) and sets beside it the outlays that part G's allocation
would reach if spending follows staff on board.

    python3 models/tools/democratic_renewal_pace.py            # the tables
    python3 models/tools/democratic_renewal_pace.py --json     # the same as JSON
    python3 models/tools/democratic_renewal_pace.py --check    # the self-checks

Method (every input a working assumption, with its basis in 7-validation.md, part 2):
- Part G's sustained allocation reaches its full run rate, $32.5 billion in FY2040, deflated to each earlier year at
  the booked CAP-7 path's own growth rate.
- Staff on board ramp linearly from the start of FY2030 at a share `r` of each agency's added-staff target a year
  (section 3, part G, "Timing and pace": about a quarter a year, range a fifth to a third), so the average share
  on board in a year is the ramp's mean over that year.
- A share `p` of each line is pay and follows staff on board; the rest (systems, space, contracts) is assumed
  to follow the booked path's own ramp. p = 1 is the strict case.
- The booked path's implied pace is the share of the full run rate it spends in each year.
Conventions: nominal $ billion by federal fiscal year, on the general fund, a cost positive.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("drc", os.path.join(HERE, "democratic_renewal_cost.py"))
drc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(drc)

WINDOW = list(range(2030, 2040))
YEARS = list(range(2030, 2041))
ALLOC_2040 = drc.BOTTOM_UP["sustained_2040"]      # $32.5 billion (part G)
ALLOC_WINDOW = drc.BOTTOM_UP["sustained"]         # $249.5 billion over FY2030-39 (part G)
STAFF_ADDED = {"IRS": 30000, "SSA": 12000, "CMS": 2500, "HUD": 2500, "FEMA": 5000, "Labor": 2000}  # EV-DEM-331
PACES = {"a fifth a year": 0.20, "a quarter a year (working)": 0.25, "a third a year": 1 / 3}
PAY_SHARES = {"strict (all pay)": 1.0, "working (70% pay)": 0.7, "loose (60% pay)": 0.6}


def ramp_mean(rate, k):
    """Mean of min(1, rate * t) over t in [k, k+1], t in years from the start of FY2030."""
    def integral(t):
        t_full = 1 / rate
        if t <= t_full:
            return rate * t * t / 2
        return rate * t_full * t_full / 2 + (t - t_full)
    return integral(k + 1) - integral(k)


def booked_cap7():
    rows, _ = drc.booked()
    return rows["CAP-7"]


def full_rate(path):
    """The full run rate in each year: the FY2040 allocation deflated at the booked path's late growth."""
    g = path[2040] / path[2039]
    return {y: ALLOC_2040 / g ** (2040 - y) for y in YEARS}, g


def booked_share(path, g):
    """The booked path as a share of its own full run rate (its FY2040 value deflated at g)."""
    return {y: min(1.0, path[y] / (path[2040] / g ** (2040 - y))) for y in YEARS}


def paced(rate, pay_share, path):
    full, g = full_rate(path)
    b = booked_share(path, g)
    out = {}
    for i, y in enumerate(YEARS):
        f = ramp_mean(rate, i)
        out[y] = full[y] * (pay_share * f + (1 - pay_share) * b[y])
    return out


def summary():
    path = booked_cap7()
    full, g = full_rate(path)
    b = booked_share(path, g)
    s = {"booked": {y: round(path[y], 2) for y in YEARS},
         "booked_window": round(sum(path[y] for y in WINDOW), 1),
         "allocation_window": ALLOC_WINDOW,
         "growth": round(g - 1, 4),
         "booked_share_of_full": {y: round(b[y], 2) for y in YEARS},
         "full_allocation_window": round(sum(full[y] for y in WINDOW), 1),
         "runs": {}, "hiring": {}}
    for pname, r in PACES.items():
        for qname, p in PAY_SHARES.items():
            x = paced(r, p, path)
            w = sum(x[y] for y in WINDOW)
            s["runs"][f"{pname}; {qname}"] = {
                "path": {y: round(x[y], 2) for y in YEARS}, "window": round(w, 1),
                "short_of_allocation": round(ALLOC_WINDOW - w, 1),
                "short_of_booked": round(s["booked_window"] - w, 1),
                "fy2030_33": round(sum(x[y] for y in range(2030, 2034)), 1)}
        s["hiring"][pname] = {"net_added_a_year_six_agencies": round(sum(STAFF_ADDED.values()) * r),
                              "irs_net_added_a_year": round(STAFF_ADDED["IRS"] * r),
                              "years_to_target": round(1 / r, 1)}
    # The booked path's implied pace: the ramp rate whose staffed shares best match the booked shares, FY2030-32.
    best = min((abs(sum(ramp_mean(r / 100, i) - b[2030 + i] for i in range(3))), r / 100) for r in range(15, 101))
    s["booked_implied_rate"] = round(best[1], 2)
    return s


def check():
    s = summary()
    assert abs(s["booked_window"] - 279.2) < 0.1, s["booked_window"]
    assert abs(ramp_mean(0.25, 0) - 0.125) < 1e-9 and abs(ramp_mean(0.25, 4) - 1.0) < 1e-9
    assert abs(ramp_mean(0.5, 1) - 0.75) < 1e-9
    # Part G's allocation, laid on the full-rate path with no ramp, should be near its stated $249.5 billion plus the
    # ramp it already carries; it cannot be below it.
    assert s["full_allocation_window"] > ALLOC_WINDOW, s["full_allocation_window"]
    w = s["runs"]["a quarter a year (working); working (70% pay)"]
    assert w["window"] < s["booked_window"], w
    for k, v in s["runs"].items():
        assert v["path"][2040] <= ALLOC_2040 + 1e-6, (k, v["path"][2040])
    print("democratic_renewal_pace: all checks passed")


def fmt(s):
    out = ["CAP-7.01: booked sustained path against part G's allocation spent at the hiring pace ($B, FY)",
           "  booked:     " + " ".join(f"{y}:{s['booked'][y]:.1f}" for y in YEARS)
           + f"  | FY2030-39 {s['booked_window']:.1f}",
           "  booked as a share of its full run rate: " + " ".join(f"{y}:{s['booked_share_of_full'][y]:.2f}" for y in range(2030, 2035)),
           f"  booked path's implied hiring pace: about {s['booked_implied_rate']:.2f} of the target a year",
           f"  part G's allocation over FY2030-39: {s['allocation_window']:.1f}; at full rate from FY2030 with no ramp: {s['full_allocation_window']:.1f}",
           "", "Allocation spent at the hiring pace (FY2030-39 | short of the allocation | short of the booking | FY2030-33):"]
    for k, v in s["runs"].items():
        out.append(f"  {k:48s} {v['window']:6.1f} | {v['short_of_allocation']:5.1f} | {v['short_of_booked']:5.1f} | {v['fy2030_33']:5.1f}")
    out += ["", "Net added staff a year (six agencies sized, EV-DEM-331):"]
    for k, v in s["hiring"].items():
        out.append(f"  {k:28s} {v['net_added_a_year_six_agencies']:6d} all six; IRS {v['irs_net_added_a_year']:5d}; target in {v['years_to_target']} years")
    return "\n".join(out)


if __name__ == "__main__":
    if "--check" in sys.argv:
        check()
    elif "--json" in sys.argv:
        print(json.dumps(summary(), indent=1))
    else:
        print(fmt(summary()))
