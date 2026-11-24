#!/usr/bin/env python3
"""democratic_renewal_cost.py: democratic renewal's section 6 lines on federal fiscal years (draft scenario).

Role: the one place the foundation's cost lines are laid on fiscal years, so that
dossiers/foundations/democratic-renewal/6-cost.md and the booking (democratic_renewal_booking.py) read the same
numbers. Status: current (booked, stage F). It writes nothing: the booked rows are read from the budget model's audit
lines (legacy/sources/recovery-budget-audit.csv, case `mixed`); the priced lines are this file's working assumptions,
each with its basis in 6-cost.md. The library line and legal aid are booked (rows DEM-17.02 and CRT-20.01), as are
D4's two timing rows (CAP-7P, G8P); the court's structure and statute tracking stay unbooked, and IMM-1's rebooking is
a later tier-3 change.

    python3 models/tools/democratic_renewal_cost.py            # the tables
    python3 models/tools/democratic_renewal_cost.py --json     # the same as JSON
    python3 models/tools/democratic_renewal_cost.py --check    # the self-checks

Conventions: nominal $ billion by federal fiscal year, a cost positive, on the general fund unless a line says
otherwise. Ranges run each line's low and high inputs together: a bound, not a probability interval.
"""
import csv
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AUDIT = os.path.join(ROOT, "legacy", "sources", "recovery-budget-audit.csv")
PATHS = os.path.join(ROOT, "models", "data", "recovery-budget-paths.csv")
YEARS = list(range(2030, 2041))
WINDOW = list(range(2030, 2040))

# The budget model's scaling of the capacity rows to Espen's October 26 sizes (recovery-adoption.json,
# cap_surge_tn 0.105 against 0.6; cap_sustained_tn 0.3 against 0.49; models/tools/budget/note-cap7-sizes.md).
CAP_SCALE = {"CAP-7S": 0.105 / 0.6, "CAP-7": 0.3 / 0.49}
BOOKED_ROWS = ["DEM-1", "DEM-11", "DEM-16", "DEM-17", "DEM-3", "CRT-P1", "CAP-8", "CAP-7S", "CAP-7",
               "DEM-17.02", "CRT-20.01", "CAP-7P"]          # the last three are this booking's (not scaled)
OTHER_LINES = {
    "delivery_contingency": "Delivery contingency (October 26, $100B; not this foundation's row)",
    "SSA OASDI capacity reclassification": "SSA's OASDI share moved off the general fund",
    "G8": "IRS enforcement revenue (G8), a gain",
    "IRS yield allowance with smaller capacity budget": "IRS yield allowance with the smaller capacity budget",
    "G8P": "IRS yield lagged with the hiring pace (G8P, D4 option B), a loss of revenue",
}

# Part G's bottom-up allocation and the booked sizes (3-design.md, part G; note-cap7-sizes.md).
BOTTOM_UP = {"surge": 54.8, "sustained": 249.5, "sustained_2040": 32.5}
RESIDUAL_404 = {"surge": 7.0, "sustained": 20.8, "fy2040": 2.8}


def grow(start, rate, first, years=YEARS):
    return {y: (start * (1 + rate) ** (y - first) if y >= first else 0.0) for y in years}


def library_line(level):
    """DEM-17.02: about $0.5-1 billion a year (central 0.75) in FY2030 dollars, half in its first year, indexed 2%."""
    p = grow(level, 0.02, 2030)
    p[2030] *= 0.5
    return p


def court_structure(full, office):
    """CRT-5.09: a transition office in FY2030-31, the court from October 1, 2031 (FY2032), grown 3% a year."""
    p = {y: 0.0 for y in YEARS}
    p[2030], p[2031] = office * 0.33, office
    for y in YEARS:
        if y >= 2032:
            p[y] = full * 1.03 ** (y - 2032)
    return p


def statute_tracking(level_mn):
    """CAP-6.01: about $8 million a year (range $5-12 million), indexed 2%."""
    return {y: v / 1000 for y, v in grow(level_mn, 0.02, 2030).items()}


def legal_aid(step_2035):
    """CRT-20.01: LSC's appropriation raised in equal steps to `step_2035` above its FY2029 level by FY2035, then
    indexed 2%. The steps are released against grantee hiring (CAP-7.02's logic), so a slow year delays them."""
    p = {}
    for y in YEARS:
        if y <= 2035:
            p[y] = step_2035 * (y - 2029) / 6
        else:
            p[y] = step_2035 * 1.02 ** (y - 2035)
    return p


def imm1_split(total_3639):
    """CRT-5.06's regular and temporary split against IMM-1: about 78% of the -$5.5 billion all-temporary saving
    over FY2036-39 (-$4.3 billion), with an illustrative year shape (the immigration model's own saving falls with attrition after FY2036; only the totals come from it)."""
    shape = {2036: 0.12, 2037: 0.21, 2038: 0.30, 2039: 0.37}
    p = {y: 0.0 for y in YEARS}
    for y, s in shape.items():
        p[y] = total_3639 * s
    p[2040] = total_3639 * 0.193  # 78% of the immigration model's -1.062 is -0.83 at the central -4.3 (review C-6)
    return p


PRICED = {
    "DEM-17.02, the permanent library line": (library_line(0.5), library_line(0.75), library_line(1.0)),
    "CRT-5.09, the immigration court's structure": (court_structure(0.35, 0.08), court_structure(0.75, 0.15),
                                                     court_structure(1.05, 0.30)),
    "CAP-6.01, statute tracking": (statute_tracking(5), statute_tracking(8), statute_tracking(12)),
    "CRT-20.01, civil legal aid through LSC": (legal_aid(0.3), legal_aid(0.6), legal_aid(1.1)),
}
# Booked in democratic_renewal_booking.py (rows DEM-17.02 and CRT-20.01); the others stay unbooked.
BOOKED_AT_BOOKING = ("DEM-17.02, the permanent library line", "CRT-20.01, civil legal aid through LSC")
UNBOOKED = {k: v for k, v in PRICED.items() if k not in BOOKED_AT_BOOKING}
LATER_TIER3 = {
    "CRT-5.06, the judges' split, against IMM-1": (imm1_split(-3.5), imm1_split(-4.3), imm1_split(-5.0)),
}


def read_audit():
    out = {}
    with open(AUDIT) as f:
        for r in csv.DictReader(f):
            if r["case"] != "mixed":
                continue
            y = int(r["year"])
            if y not in YEARS and y != 2029:
                continue
            out.setdefault(r["line"], {}).setdefault(y, 0.0)
            out[r["line"]][y] += float(r["primary_deficit_change_bn"])
    return out


def booked():
    a = read_audit()
    rows = {}
    for k in BOOKED_ROWS:
        scale = CAP_SCALE.get(k, 1.0)
        rows[k] = {y: a.get(k, {}).get(y, 0.0) * scale for y in YEARS}
    other = {label: {y: a.get(k, {}).get(y, 0.0) for y in YEARS} for k, label in OTHER_LINES.items()}
    return rows, other


def gap_2040():
    with open(PATHS) as f:
        for r in csv.DictReader(f):
            # the plan-wide gap before stage G's settlement, which closes FY2040 on (step 7): the dossier's share is of that
            if r["case"] == "mixed_before_settlement" and r["year"] == "2040":
                return float(r["agenda_gf_primary_bn"]), float(r["gdp_bn"])
    raise SystemExit("no FY2040 row for case mixed")


def total(p, years=WINDOW):
    return sum(p[y] for y in years)


def summary():
    rows, other = booked()
    gap, gdp = gap_2040()
    s = {"booked": {}, "other": {}, "priced": {}, "unbooked": {}, "later_tier3": {}}
    for k, p in rows.items():
        s["booked"][k] = dict(fy2030_39=total(p), fy2040=p[2040])
    for k, p in other.items():
        s["other"][k] = dict(fy2030_39=total(p), fy2040=p[2040])
    for group, src in (("priced", PRICED), ("unbooked", UNBOOKED), ("later_tier3", LATER_TIER3)):
        for k, (lo, mid, hi) in src.items():
            s[group][k] = dict(fy2030_39=total(mid), fy2040=mid[2040], lo_30_39=total(lo), hi_30_39=total(hi),
                               lo_2040=lo[2040], hi_2040=hi[2040], path={y: round(mid[y], 3) for y in YEARS})
    b = s["booked"]
    s["booked_all"] = dict(fy2030_39=sum(v["fy2030_39"] for v in b.values()),
                           fy2040=sum(v["fy2040"] for v in b.values()))
    keys = ("fy2030_39", "fy2040", "lo_30_39", "hi_30_39", "lo_2040", "hi_2040")
    s["priced_all"] = {k: sum(v[k] for v in s["priced"].values()) for k in keys}
    s["unbooked_all"] = {k: sum(v[k] for v in s["unbooked"].values()) for k in keys}
    lag = s["other"][OTHER_LINES["G8P"]]
    s["d4_booked"] = dict(outlay_fy2030_39=b["CAP-7P"]["fy2030_39"], revenue_lag_fy2030_39=lag["fy2030_39"],
                          net_fy2030_39=b["CAP-7P"]["fy2030_39"] + lag["fy2030_39"],
                          fy2040=b["CAP-7P"]["fy2040"] + lag["fy2040"])
    s["contingency"] = dict(
        surge=b["CAP-7S"]["fy2030_39"] - BOTTOM_UP["surge"],
        sustained=b["CAP-7"]["fy2030_39"] - BOTTOM_UP["sustained"],
        fy2040=b["CAP-7"]["fy2040"] - BOTTOM_UP["sustained_2040"],
        residual_404=RESIDUAL_404)
    s["gap_2040"] = gap
    s["gdp_2040"] = gdp
    s["share_of_gap_2040"] = dict(booked=b and s["booked_all"]["fy2040"] / gap,
                                  unbooked=s["unbooked_all"]["fy2040"] / gap,
                                  unbooked_hi=s["unbooked_all"]["hi_2040"] / gap,
                                  priced=s["priced_all"]["fy2040"] / gap,
                                  imm1=s["later_tier3"]["CRT-5.06, the judges' split, against IMM-1"]["fy2040"] / gap)
    return s


def check():
    s = summary()
    b = s["booked"]
    assert abs(b["CAP-7S"]["fy2030_39"] - 98.0) < 0.05, b["CAP-7S"]
    assert abs(b["CAP-7"]["fy2030_39"] - 279.2) < 0.05, b["CAP-7"]
    assert abs(b["CAP-7"]["fy2040"] - 37.2) < 0.05, b["CAP-7"]
    assert abs(b["DEM-11"]["fy2030_39"] - 20.0) < 0.05 and abs(b["DEM-11"]["fy2040"] - 2.26) < 0.01
    assert abs(s["gap_2040"] - 614.6) < 0.1, s["gap_2040"]        # before the settlement; 615.6 before G14 C took out the duty to house's HOU-1 component, 614.0 before this booking
    t = s["later_tier3"]["CRT-5.06, the judges' split, against IMM-1"]
    assert abs(t["fy2030_39"] + 4.3) < 0.01 and abs(t["fy2040"] + 0.83) < 0.01, t
    d = s["d4_booked"]
    assert abs(d["outlay_fy2030_39"] + 17.0) < 0.05 and abs(d["revenue_lag_fy2030_39"] - 16.1) < 0.05, d
    assert abs(d["fy2040"]) < 0.005, d
    c = s["contingency"]
    assert abs(c["surge"] - 43.2) < 0.1 and abs(c["sustained"] - 29.7) < 0.1, c
    u = s["priced_all"]
    assert 8 <= u["lo_30_39"] and u["fy2030_39"] <= 30, u
    print("democratic_renewal_cost: all checks passed")


def fmt(s):
    out = ["Booked rows (case mixed; CAP rows at the October 26 scaling), $B: FY2030-39 | FY2040"]
    for k, v in s["booked"].items():
        out.append(f"  {k:8} {v['fy2030_39']:8.1f} | {v['fy2040']:6.2f}")
    out.append(f"  {'all':8} {s['booked_all']['fy2030_39']:8.1f} | {s['booked_all']['fy2040']:6.2f}")
    out.append("Other booked lines that touch this foundation:")
    for k, v in s["other"].items():
        out.append(f"  {k}: {v['fy2030_39']:.1f} | {v['fy2040']:.2f}")
    for group in ("priced", "unbooked", "later_tier3"):
        out.append(f"{group}: central (low to high)")
        for k, v in s[group].items():
            out.append(f"  {k}: {v['fy2030_39']:.2f} ({v['lo_30_39']:.2f} to {v['hi_30_39']:.2f}) | "
                       f"{v['fy2040']:.2f} ({v['lo_2040']:.2f} to {v['hi_2040']:.2f})")
            out.append("    " + " ".join(f"{y}:{v['path'][y]:.2f}" for y in YEARS))
    for label, key in (("Priced in section 6, all four", "priced_all"), ("Still unbooked", "unbooked_all")):
        u = s[key]
        out.append(f"{label}: {u['fy2030_39']:.1f} ({u['lo_30_39']:.1f} to {u['hi_30_39']:.1f}) | "
                   f"{u['fy2040']:.2f} ({u['lo_2040']:.2f} to {u['hi_2040']:.2f})")
    d = s["d4_booked"]
    out.append(f"D4 option B, booked: outlays {d['outlay_fy2030_39']:.1f}, IRS yield lag {d['revenue_lag_fy2030_39']:+.1f}, "
               f"net {d['net_fy2030_39']:+.1f} over FY2030-39; FY2040 {d['fy2040']:+.2f}")
    c = s["contingency"]
    out.append(f"Memo 10's contingency: surge {c['surge']:.1f}, sustained {c['sustained']:.1f}, FY2040 {c['fy2040']:.1f}")
    sh = s["share_of_gap_2040"]
    out.append(f"FY2040 gap {s['gap_2040']:.1f} (GDP {s['gdp_2040']:.0f}): booked rows {100*sh['booked']:.2f}%, "
               f"unbooked {100*sh['unbooked']:.2f}% (high {100*sh['unbooked_hi']:.2f}%), IMM-1 split {100*sh['imm1']:.2f}%")
    return "\n".join(out)


if __name__ == "__main__":
    if "--check" in sys.argv:
        check()
    elif "--json" in sys.argv:
        print(json.dumps(summary(), indent=1, default=str))
    else:
        print(fmt(summary()))
