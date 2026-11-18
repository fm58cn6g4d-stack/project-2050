#!/usr/bin/env python3
"""democratic_renewal_pace.py: can the agency rebuild's sustained money be spent at the pace agencies can hire,
and what does re-laying it on that pace do to outlays and to the IRS's enforcement yield?

Role: democratic renewal's section 7 check of CAP-7.01's booked path against the hiring pace sections 3 and 5
assume (dossiers/foundations/democratic-renewal/7-validation.md, part 1.3), and the figures behind decision-sheet
item D4 (7-validation.md, part 10, question 4; 6-cost.md, part 7). Status: draft (stage F, milestone fix step 1:
rebased on one basis, review finding F-1). It books nothing and writes nothing: it reads the booked CAP-7 path and
the booked IRS enforcement lines through democratic_renewal_cost.py (the budget model's audit lines, case `mixed`,
at the October 26 scaling) and the legacy capacity review's midpoint path through capacity-review/review.py.

    python3 models/tools/democratic_renewal_pace.py            # the tables
    python3 models/tools/democratic_renewal_pace.py --json     # the same as JSON
    python3 models/tools/democratic_renewal_pace.py --check    # the self-checks (unit tests: test_democratic_renewal.py)

Method (every input a working assumption, with its basis in 7-validation.md, part 1.3):
- Full run rate. Part G's sustained allocation reaches $32.5 billion in FY2040; deflated to each earlier year at the
  booked CAP-7 path's own late growth (about 3.8% a year), it is the allocation's full run rate in each year.
- One basis (dossiers/TEMPLATE.md, "One basis for each fiscal figure"). The booking lays every dollar of CAP-7 on
  the booked ramp (33%, 67%, then 100% of the run rate in FY2030-32). On that basis part G's allocation is the
  full run rate times the booked ramp: about $243.9 billion over FY2030-39, not the $249.5 billion part G states
  on the legacy review's own ramp and growth. The pace effect is the allocation on the booked ramp less the same
  allocation on the hiring pace. Both use the same run rate; only the ramp differs.
  (The draft compared the paced result with part G's stated $249.5 billion, a different basis: review F-1.)
- Hiring pace. Staff on board ramp linearly from the start of FY2030 at a share `r` of each agency's added-staff
  target a year (part G, "Timing and pace": about a quarter a year, range a fifth to a third), so the average share
  on board in a year is the ramp's mean over that year.
- Pay share. A share `p` of each line is pay and follows staff on board; the rest (systems, space, contracts)
  follows the booked ramp. p = 1 is the strict case.
- Cross-checks on two other bases: part G's own path (the review's midpoint ramp, scaled to part G) re-ramped the
  same way; and the no-ramp path (the run rate from FY2030), which no design spends and which bounds the effect
  from above.
- The IRS's enforcement yield (G8, net of the booked allowance) follows IRS enforcement staff on board, as the
  booked G8 follows the booked ramp. Its in-window yield is the capacity review's lagged multiple (review.py,
  `lagged_yield`): a dollar of enforcement yields after `L` years (1 to 2; central 1), so yield in FY2030-39 comes
  from staff on board in FY2030 to FY(2039-L), scaled so that the booked shape gives the booked net $150 billion.
  The lag is the booked net yield less the same yield on the hiring pace.
- The booked path's implied pace is the ramp rate whose staffed shares best match the booked shares in FY2030-32.
Conventions: nominal $ billion by federal fiscal year, on the general fund. Effects are reported as a reduction
(a positive number is less outlay, or less revenue). Ranges are bounds across the runs, not probability intervals.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


drc = _load("drc", os.path.join(HERE, "democratic_renewal_cost.py"))
review = _load("capacity_review", os.path.join(HERE, "capacity-review", "review.py"))

WINDOW = list(range(2030, 2040))
YEARS = list(range(2030, 2041))
ALLOC_2040 = drc.BOTTOM_UP["sustained_2040"]      # $32.5 billion (part G)
ALLOC_WINDOW = drc.BOTTOM_UP["sustained"]         # $249.5 billion over FY2030-39 (part G, on its own path)
IRS_SUSTAINED = 94.2                              # part G's IRS line, FY2030-39 (3-design.md, part G)
STAFF_ADDED = {"IRS": 30000, "SSA": 12000, "CMS": 2500, "HUD": 2500, "FEMA": 5000, "Labor": 2000}  # EV-DEM-331
PACES = {"a fifth a year": 0.20, "a quarter a year (working)": 0.25, "a third a year": 1 / 3}
PAY_SHARES = {"strict (all pay)": 1.0, "working (70% pay)": 0.7, "loose (60% pay)": 0.6}
WORKING = "a quarter a year (working); working (70% pay)"
YIELD_LAGS = (1, 2)                                # review.py LAGS; central 1
CENTRAL_LAG = 1
G8_LINE = drc.OTHER_LINES["G8"]
ALLOWANCE_LINE = drc.OTHER_LINES["IRS yield allowance with smaller capacity budget"]


def ramp_mean(rate, k):
    """Mean of min(1, rate * t) over t in [k, k+1], t in years from the start of FY2030."""
    def integral(t):
        t_full = 1 / rate
        if t <= t_full:
            return rate * t * t / 2
        return rate * t_full * t_full / 2 + (t - t_full)
    return integral(k + 1) - integral(k)


def staffed(rate):
    """Average share of the added-staff target on board in each fiscal year."""
    return {y: ramp_mean(rate, i) for i, y in enumerate(YEARS)}


def full_staff_year(rate):
    """The first fiscal year in which every day is at the full target."""
    return next(y for y, v in staffed(rate).items() if v >= 1 - 1e-12)


def booked_cap7():
    rows, _ = drc.booked()
    return rows["CAP-7"]


def booked_g8_net():
    """The booked enforcement yield net of its allowance, as a gain (positive), by year."""
    _, other = drc.booked()
    return {y: -(other[G8_LINE][y] + other[ALLOWANCE_LINE][y]) for y in YEARS}


def full_rate(path, level_2040):
    """A full run rate reaching `level_2040` in FY2040, deflated at the path's own late growth."""
    g = path[2040] / path[2039]
    return {y: level_2040 / g ** (2040 - y) for y in YEARS}, g


def shares(path):
    """A path as a share of its own full run rate (its FY2040 value deflated at its late growth)."""
    full, _ = full_rate(path, path[2040])
    return {y: min(1.0, path[y] / full[y]) for y in YEARS}


def paced(full, rate, pay_share, other_ramp):
    """The allocation with pay following staff on board and the rest following `other_ramp`."""
    f = staffed(rate)
    return {y: full[y] * (pay_share * f[y] + (1 - pay_share) * other_ramp[y]) for y in YEARS}


def total(p, years=WINDOW):
    return sum(p[y] for y in years)


def part_g_own_path():
    """Part G's allocation on its own ramp: the legacy review's midpoint path (review.py), scaled to part G."""
    data, _ = review.load()
    path = {y: sum(data[a]["path"][y][1] for a in review.AGENCIES) for y in review.YEARS}
    run_2040 = sum(data[a]["rate"][1] for a in review.AGENCIES) * (1 + review.GROWTH) ** 14
    review_full = {y: run_2040 / (1 + review.GROWTH) ** (2040 - y) for y in review.YEARS}
    ramp = {y: min(1.0, path[y] / review_full[y]) for y in review.YEARS}
    ramp[2040] = 1.0
    full = {y: ALLOC_2040 / (1 + review.GROWTH) ** (2040 - y) for y in YEARS}
    return {"review_path": path, "review_window": sum(path.values()), "ramp": ramp, "full": full,
            "allocation": {y: full[y] * ramp[y] for y in YEARS}}


def g8_lag(rate, lag):
    """Net enforcement yield lost in FY2030-39 when IRS enforcement staff follow the hiring pace (a positive number
    is less revenue). Review.py's lagged multiple: yield in the window comes from staff on board through FY(2039-lag),
    scaled so that the booked shape gives the booked net yield."""
    net = booked_g8_net()
    full, _ = full_rate(net, net[2040])
    b8 = shares(net)
    f = staffed(rate)
    years = [y for y in WINDOW if y + lag <= 2039]
    y_booked = sum(full[y] * b8[y] for y in years)
    y_paced = sum(full[y] * min(1.0, f[y]) for y in years)
    return total(net) * (1 - y_paced / y_booked)


def summary():
    path = booked_cap7()
    full, g = full_rate(path, ALLOC_2040)
    b = shares(path)
    alloc_booked = {y: full[y] * b[y] for y in YEARS}             # part G's allocation laid on the booked ramp
    own = part_g_own_path()
    net = booked_g8_net()
    s = {"booked": {y: round(path[y], 2) for y in YEARS},
         "booked_window": round(total(path), 1),
         "allocation_window": ALLOC_WINDOW,
         "growth": round(g - 1, 4),
         "booked_share_of_full": {y: round(b[y], 2) for y in YEARS},
         "allocation_on_booked_ramp": {y: round(alloc_booked[y], 2) for y in YEARS},
         "allocation_on_booked_ramp_window": round(total(alloc_booked), 1),
         "contingency_on_booked_ramp_window": round(total(path) - total(alloc_booked), 1),
         "full_allocation_window": round(total(full), 1),
         "part_g_own_path": {y: round(own["allocation"][y], 2) for y in YEARS},
         "part_g_own_path_window": round(total(own["allocation"]), 1),
         "part_g_own_ramp": {y: round(own["ramp"][y], 2) for y in range(2030, 2034)},
         "g8_net_booked": {y: round(net[y], 2) for y in YEARS},
         "g8_net_booked_window": round(total(net), 1),
         "runs": {}, "hiring": {}}
    for pname, r in PACES.items():
        for qname, p in PAY_SHARES.items():
            x = paced(full, r, p, b)
            xo = paced(own["full"], r, p, own["ramp"])
            outlay = total(alloc_booked) - total(x)
            lag = {L: g8_lag(r, L) for L in (0,) + YIELD_LAGS}
            s["runs"][f"{pname}; {qname}"] = {
                "path": {y: round(x[y], 2) for y in YEARS}, "window": round(total(x), 1),
                "fy2030_33": round(sum(x[y] for y in range(2030, 2034)), 1),
                "fy2040_change": round(alloc_booked[2040] - x[2040], 6),
                # The pace effect on one basis (the booking's), and the two cross-check bases.
                "outlay_effect": round(outlay, 1),
                "outlay_effect_part_g_own_path": round(total(own["allocation"]) - total(xo), 1),
                "outlay_effect_no_ramp": round(total(full) - total(x), 1),
                "irs_outlay_effect": round(outlay * IRS_SUSTAINED / ALLOC_WINDOW, 1),
                "g8_lag": {str(L): round(v, 1) for L, v in lag.items()},
                "net_deficit_change": round(-outlay + lag[CENTRAL_LAG], 1),
                "short_of_booked": round(total(path) - total(x), 1)}
        s["hiring"][pname] = {"net_added_a_year_six_agencies": round(sum(STAFF_ADDED.values()) * r),
                              "irs_net_added_a_year": round(STAFF_ADDED["IRS"] * r),
                              "years_to_target": round(1 / r, 1),
                              "full_staff_fy": full_staff_year(r)}
    runs = list(s["runs"].values())
    rng = lambda key: (round(min(v[key] for v in runs), 1), round(max(v[key] for v in runs), 1))
    lag_all = [v["g8_lag"][str(L)] for v in runs for L in YIELD_LAGS]
    w = s["runs"][WORKING]
    s["d4"] = {"outlay_effect": w["outlay_effect"], "outlay_range": rng("outlay_effect"),
               "g8_lag": w["g8_lag"][str(CENTRAL_LAG)], "g8_lag_range": (min(lag_all), max(lag_all)),
               "net_deficit_change": w["net_deficit_change"], "net_range": rng("net_deficit_change"),
               "irs_outlay_effect": w["irs_outlay_effect"],
               "own_path_range": rng("outlay_effect_part_g_own_path"), "no_ramp_range": rng("outlay_effect_no_ramp"),
               "superseded_draft_figure": round(ALLOC_WINDOW - w["window"], 1)}
    best = min((abs(sum(ramp_mean(r / 100, i) - b[2030 + i] for i in range(3))), r / 100) for r in range(15, 101))
    s["booked_implied_rate"] = round(best[1], 2)
    return s


def check():
    s = summary()
    assert abs(s["booked_window"] - 279.2) < 0.1, s["booked_window"]
    assert abs(s["g8_net_booked_window"] - 150.0) < 0.1, s["g8_net_booked_window"]
    assert abs(ramp_mean(0.25, 0) - 0.125) < 1e-9 and abs(ramp_mean(0.25, 4) - 1.0) < 1e-9
    # One basis: the allocation on the booked ramp is below part G's stated figure and below the no-ramp path.
    assert s["allocation_on_booked_ramp_window"] < ALLOC_WINDOW < s["full_allocation_window"], s
    for k, v in s["runs"].items():
        assert v["path"][2040] <= ALLOC_2040 + 1e-6, (k, v["path"][2040])
        assert abs(v["fy2040_change"]) < 1e-6, (k, v["fy2040_change"])            # FY2040 does not change
        assert 0 < v["outlay_effect"] < v["outlay_effect_no_ramp"], (k, v)
        assert all(v["g8_lag"][str(L)] > 0 for L in YIELD_LAGS), (k, v)
    print("democratic_renewal_pace: all checks passed")


def fmt(s):
    d = s["d4"]
    out = ["CAP-7.01: booked sustained path against part G's allocation spent at the hiring pace ($B, FY)",
           "  booked:     " + " ".join(f"{y}:{s['booked'][y]:.1f}" for y in YEARS)
           + f"  | FY2030-39 {s['booked_window']:.1f}",
           "  booked as a share of its full run rate: " + " ".join(f"{y}:{s['booked_share_of_full'][y]:.2f}" for y in range(2030, 2035)),
           f"  booked path's implied hiring pace: about {s['booked_implied_rate']:.2f} of the target a year",
           f"  part G's allocation over FY2030-39: {s['allocation_window']:.1f} on its own path (rebuilt here: "
           f"{s['part_g_own_path_window']:.1f}); on the booked ramp {s['allocation_on_booked_ramp_window']:.1f} "
           f"(the contingency on that basis {s['contingency_on_booked_ramp_window']:.1f}); "
           f"at full rate from FY2030 with no ramp {s['full_allocation_window']:.1f}",
           "", "Allocation spent at the hiring pace. FY2030-39 | FY2030-33 | pace effect on the booking's basis "
           "(part G's own path; no ramp) | G8 lag, lag 1 (0 to 2) | net deficit change:"]
    for k, v in s["runs"].items():
        g = v["g8_lag"]
        out.append(f"  {k:48s} {v['window']:6.1f} | {v['fy2030_33']:5.1f} | {v['outlay_effect']:5.1f} "
                   f"({v['outlay_effect_part_g_own_path']:5.1f}; {v['outlay_effect_no_ramp']:5.1f}) | "
                   f"{g['1']:5.1f} ({g['0']:.1f} to {g['2']:.1f}) | {v['net_deficit_change']:+5.1f}")
    out += ["", f"D4 on one basis (working pace, 70% pay, lag 1): outlays {d['outlay_effect']:.1f} less "
            f"(range {d['outlay_range'][0]:.1f}-{d['outlay_range'][1]:.1f}; the IRS's share {d['irs_outlay_effect']:.1f}); "
            f"G8's net yield {d['g8_lag']:.1f} less (range {d['g8_lag_range'][0]:.1f}-{d['g8_lag_range'][1]:.1f}); "
            f"net deficit change {d['net_deficit_change']:+.1f} (range {d['net_range'][0]:+.1f} to {d['net_range'][1]:+.1f}); "
            "FY2040 unchanged in every run.",
            f"  cross-checks: on part G's own path {d['own_path_range'][0]:.1f}-{d['own_path_range'][1]:.1f}; "
            f"against the no-ramp path {d['no_ramp_range'][0]:.1f}-{d['no_ramp_range'][1]:.1f} (an upper bound no design spends); "
            f"the draft's mixed-basis figure was {d['superseded_draft_figure']:.1f}",
            f"  booked net G8 over FY2030-39: {s['g8_net_booked_window']:.1f}",
            "", "Net added staff a year (six agencies sized, EV-DEM-331):"]
    for k, v in s["hiring"].items():
        out.append(f"  {k:28s} {v['net_added_a_year_six_agencies']:6d} all six; IRS {v['irs_net_added_a_year']:5d}; "
                   f"target in {v['years_to_target']} years; full strength from FY{v['full_staff_fy']}")
    return "\n".join(out)


if __name__ == "__main__":
    if "--check" in sys.argv:
        check()
    elif "--json" in sys.argv:
        print(json.dumps(summary(), indent=1))
    else:
        print(fmt(summary()))
