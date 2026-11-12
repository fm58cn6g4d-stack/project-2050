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
- HLT-4 split (review F-4 item 2): the safety-net items kept on the legacy profile; children's continuous coverage
  retired from wave 1 (January 2031), Medicaid dental and the items costed with it retired with Medicaid's wave-2
  thirds (January 2033, 2034, 2035). Its legacy long-term care part is retired by care parts B-D's booking, which
  owns the HLT-4 row (care_booking.py): these three parts are returned as hlt4_parts for it.
- HLT-6, the Advantage fix at MedPAC's lower estimate, calendar 2030-34, on the blend: the general fund books Part B's
  share; Part A's share (funds-parameters.csv hi_hlt6_part_a_share) is HI's, in the funds model (care follow-up 3).
- HLT-7, the single plan's spending line: outlays less the federal money it replaces and the states' payments
  (offsetting receipts, netted here), plus the hospital transition fund and the territories. Medicaid's long-term care
  stays in Medicaid at current-law cost (HLT-7.07; board row D-4c), so it is in none of these.
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
RATE_RANGE_TN = (21.74 - 18.57, 24.92 - 21.74)
# Medicaid long-term care kept in Medicaid (6-cost.md part 6, board row D-4c): nhe_mcd_ltc at 317 and 274, $T
LTC_RANGE_TN = (21.74 - 21.40, 21.81 - 21.74)
HALF_PASSTHROUGH_FY2040 = 370.0   # exclusion revenue lost at half pass-through, no contribution (review F-3), $B
# HLT-7.16, help for insurance and billing workers, FY2033-38: about $0.06T (range 0.03-0.15; 6-cost.md part 2), spread
# evenly; booked in B6 (the lead's brief, item 7), as part 5's open question 1 asked.
WORKER_HELP = {y: 10.0 for y in range(2033, 2039)}
# Federal coverage inside the employer cell (6-cost.md part 6): FEHB, TRICARE and the VA are priced as employer-group
# movers. Central 2032 full-scale figures, $B, on the cell's exclusion revenue (excl_full, about $680B): the spending
# line reads high by $65-130B (central 97.5), HX by $40-60B (central 50). Both scale with HX's moved-share path, so
# the correction follows the employer groups as they move. Booked in B6 (item 7).
FEDCOV_SPEND_2032, FEDCOV_REVENUE_2032 = 97.5, 50.0


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
                restore_cal=restore_cal, neutral=neutral, moved=HP.shares_moved, wave2=HP.WAVE2,
                HP=HP, I=I, B=B, P=P, gf=gf, kids=f["child_share_employer"], employer_premiums=emp)


def fiscal():
    return _load("hb_fiscal", os.path.join(HERE, "fiscal-model.py"))


def hlt6_part_a_share():
    """Part A's share of HLT-6's Advantage savings, credited to HI (funds-parameters.csv; care follow-up 3)."""
    with open(os.path.join(INPUTS, "funds-parameters.csv"), newline="", encoding="utf-8") as f:
        return float(next(r["value"] for r in csv.DictReader(f) if r["key"] == "hi_hlt6_part_a_share"))


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
    # part 6's federal-coverage correction, on HX's path: less spending (a negative component) and less HX
    xf = excl_full(hp)
    fedcov = {y: -FEDCOV_SPEND_2032 / xf * hp["excl"][y] for y in W + [2040]}
    hx = {y: hp["excl"][y] * (1 - FEDCOV_REVENUE_2032 / xf) for y in W + [2040]}
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
        "HLT-7/territories": window(terr), "HLT-7/worker-help": window(WORKER_HELP),
        "HLT-7/federal-coverage": window(fedcov),
        "HLT-4/children-continuous-coverage": window(kids), "HLT-4/medicaid-dental-and-bundle": window(dental),
        "HX": window(hx),
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

    # HLT-4's legacy long-term care part (0.3194) is retired by care parts B-D's booking (care_booking.py owns the
    # HLT-4 row: health's three parts below plus the bridge and its companions). Health's parts keep their amounts.
    hlt4_parts = [("safety-net-centers-residency-momnibus-title-x", round(tn(part["safety_net"]), 4), None),
                  ("children-continuous-coverage", round(amt["HLT-4/children-continuous-coverage"], 4), 0.0),
                  ("medicaid-dental-and-bundle", round(amt["HLT-4/medicaid-dental-and-bundle"], 4), 0.0)]
    hlt7_mid, c7 = parts("HLT-7", [("plan-spending", amt["HLT-7/plan-spending"],
                                    perm_for(B, F, {2039: years["HLT-7/plan-spending"][-1]}, spend[2040])),
                                   ("transition-fund", amt["HLT-7/transition-fund"], 0.0),
                                   ("territories", amt["HLT-7/territories"],
                                    perm_for(B, F, {2039: years["HLT-7/territories"][-1]}, TERRITORIES_FY2040,
                                             "out_health_other")),
                                   ("worker-help", amt["HLT-7/worker-help"], 0.0),
                                   ("federal-coverage", amt["HLT-7/federal-coverage"],
                                    perm_for(B, F, {2039: years["HLT-7/federal-coverage"][-1]}, fedcov[2040]))])
    comps = {"HLT-7": c7}
    ledger = {
        "HLT-1": (r3(amt["HLT-1"]), r3(amt["HLT-1"]), r3(amt["HLT-1"] + 0.25)),   # HLT-1.03's provider-tax range, $0-0.25T
        "HLT-2": (0.31, r3(amt["HLT-2"]), 0.53),                                 # 0.25-0.35 upgrades + 0.06-0.18 wait
        "HLT-3": (0, 0, 0), "HLT-5": (0, 0, 0),
        "HLT-6": (r3(amt["HLT-6"] * (1 - hlt6_part_a_share())),) * 3,   # Part B's share; Part A's goes to HI (funds model)
        "HLT-7": (r3(hlt7_mid - RATE_RANGE_TN[0] - LTC_RANGE_TN[0] - 0.05 - 0.04), hlt7_mid,
                  r3(hlt7_mid + RATE_RANGE_TN[1] + LTC_RANGE_TN[1] + 0.05 + 0.09)),
        "HLT-8": HLT8_TN,
        "HX": (r3(amt["HX"] * (1 - HALF_PASSTHROUGH_FY2040 / hp["excl"][2040])), r3(amt["HX"]), r3(amt["HX"])),
    }
    perms = {"HX": perm_for(B, F, {2039: years["HX"][-1]}, hx[2040])}
    fy2040 = dict(spending=spend[2040], exclusion=hx[2040], contribution=hp["contribution"][2040],
                  territories=TERRITORIES_FY2040, net=hp["net"][2040], federal_coverage=fedcov[2040],
                  exclusion_before_correction=hp["excl"][2040])
    fedcov_net = (sum(fedcov[y] for y in W) + sum(hp["excl"][y] - hx[y] for y in W)) / 1000
    totals = dict(net_window=sum(hp["net"][y] for y in W) / 1000, federal_coverage_net=fedcov_net,
                  worker_help=sum(WORKER_HELP.values()) / 1000,
                  with_contribution=(sum(hp["net"][y] for y in W) - sum(hp["contribution"][y] for y in W)) / 1000,
                  contribution_window=sum(hp["contribution"][y] for y in W) / 1000)
    hlt4_path = [round(part["safety_net"][y] + kids[y] + dental[y], 2) for y in W]   # health's parts of HLT-4
    return dict(years=years, components=comps, ledger=ledger, perms=perms, fy2040=fy2040, totals=totals, hlt4_path=hlt4_path,
                hlt4_parts=hlt4_parts,
                contribution={y: hp["contribution"][y] for y in W + [2040]})


# ---- the household test (D3): HLT-7's household rows (incidence-rows.csv H7h, H7w, H7x) ----
# Quintile boundaries on the persons key of incidence-keys.csv (cumulative shares of people), for the crosswalk from
# the coverage model's four income bands (<138%, 138-250%, 250-400%, 400%+ of poverty) to quintiles.
PERSONS_KEY = (15, 18, 21, 22, 24)
PERSONS_TOP1 = 1.0
GROUP_KEY = {"esi": "employer", "ng_sub": "individual", "ng_unsub": "individual", "medicaid": "medicaid",
             "medicare": "medicare", "uninsured": "uninsured"}


def household_removed(hp):
    """Premiums and out-of-pocket costs households stop paying, by moving group and by income band, at the coverage
    model's full scale (2032 basis, $ billion): the baseline's household cost less the plan's copays."""
    M, I, B, P = hp["HP"].M, hp["I"], hp["B"], hp["P"]
    base = M.run(I, {}, B)["household"]
    sp = hp["HP"].model_full(I, B, P)["household"]
    sp_pp = sp["by_source"]["sp"]["oop_pp"]
    left_unins = sp["by_source"].get("uninsured", {"people": 0.0})["people"]
    by_group = {}
    for s, k in GROUP_KEY.items():
        v = base["by_source"][s]
        n = v["people"] - (left_unins if s == "uninsured" else 0.0)
        by_group[k] = by_group.get(k, 0.0) + n * (v["premium_pp"] + v["oop_pp"] - sp_pp) / 1000
    total = base["total_bn"] - sp["total_bn"]
    scale = total / sum(by_group.values())          # the group split's rounding, so the groups add to the total
    by_group = {k: v * scale for k, v in by_group.items()}
    bands = [(b0["people"], b0["premiums_bn"] + b0["oop_bn"] - b1["premiums_bn"] - b1["oop_bn"])
             for b0, b1 in zip(base["by_band"], sp["by_band"])]
    return dict(total=total, by_group=by_group, bands=bands)


def band_key(bands):
    """Crosswalk of band amounts to quintile shares (%), uniform per person within a band, people ranked by income;
    the top 1% is the top 1% of people at the 400%+ band's average."""
    pop = sum(n for n, _ in bands)
    total = sum(a for _, a in bands)
    edges, c = [], 0.0
    for n, a in bands:
        edges.append((c, c + n / pop, a))
        c += n / pop
    q, lo = [], 0.0
    for s in PERSONS_KEY:
        hi = lo + s / 100
        q.append(sum(a * max(0.0, min(hi, e1) - max(lo, e0)) / (e1 - e0) for e0, e1, a in edges) / total * 100)
        lo = hi
    n4, a4 = bands[-1]
    top1 = (PERSONS_TOP1 / 100) * (a4 / (n4 / pop)) / total * 100
    return close(q), round(top1, 1)


def close(q):
    """Shares rounded to 0.1 that add to exactly 100 (the largest takes the rounding)."""
    q = [round(x, 1) for x in q]
    big = q.index(max(q))
    q[big] = round(100 - sum(x for k, x in enumerate(q) if k != big), 1)
    return q


# The tax on former premiums (HX) by quintile: the employer_cov key (incidence-keys.csv, where employer premiums
# fall) times a combined income and payroll marginal rate per quintile. Working assumption: payroll tax (15.3%) for
# every quintile, less the EITC's offset in Q1, the income tax brackets above it, and the payroll cap in the top 1%.
EMPLOYER_COV_KEY = ((3, 12, 24, 31, 30), 2)
MARGINAL_RATES = ((0.10, 0.25, 0.30, 0.33, 0.38), 0.40)


def exclusion_key():
    (q, t1), (r, rt1) = EMPLOYER_COV_KEY, MARGINAL_RATES
    w = [a * b for a, b in zip(q, r)]
    return close([x / sum(w) * 100 for x in w]), round(t1 * rt1 / sum(w) * 100, 1)


def incidence():
    """HLT-7's household rows on the booked fiscal-year path, FY2030-39 ($ trillion), with their year shapes and the
    distribution key for household premiums and out-of-pocket costs removed."""
    hp = health_path()
    HP, gf = hp["HP"], hp["gf"]
    hh = household_removed(hp)
    cal = {}
    for y in range(2030, 2041):
        sh = HP.shares_moved(y)
        sh["employer"] = HP.employer_share(y, hp["kids"])
        cal[y] = sum(hh["by_group"][k] * sh[k] for k in hh["by_group"]) * gf[y]
    h7h = fy(cal)
    # employer-paid premiums that become wages (full pass-through, HX's convention): the same moved-share path as HX
    wages = {y: hp["excl"][y] * hp["employer_premiums"] / excl_full(hp) for y in W + [2040]}
    tn = lambda d: round(sum(d.get(y, 0.0) for y in W) / 1000, 3)  # noqa: E731
    shape = lambda d: [round(d.get(y, 0.0) / max(d.get(y2, 0.0) for y2 in W), 3) for y in W]  # noqa: E731
    key, top1 = band_key(hh["bands"])
    return dict(
        rows={"H7h": tn(h7h), "H7w": tn(wages), "H7x": tn(hp["excl"])},
        shapes={"H7h": shape(h7h), "H7w": shape(wages), **legacy_shapes()},
        key={"health_hh": (key, top1), "exclusion_end": exclusion_key()},
        full_scale=dict(household_removed=hh["total"], by_group=hh["by_group"], bands=hh["bands"],
                        employer_premiums=hp["employer_premiums"]),
        fy2040={"H7h": h7h[2040], "H7w": wages[2040], "H7x": hp["excl"][2040]})


def legacy_shapes():
    """Phase-in shapes (incidence-phase-in.csv, method norm) for the health rows rebooked in #230: H1 (HLT-1), H2 and
    PB (HLT-2) and MA (HLT-6), each its booked fiscal-year path scaled to its largest year. H4 (HLT-4) is now
    care_booking.py's, since care parts B-D's booking rebuilt HLT-4."""
    b = booking()
    sc = lambda v: [round(x / max(v, key=abs), 3) + 0.0 if max(v, key=abs) else 0.0 for x in v]  # noqa: E731
    return {"H1": sc(b["years"]["HLT-1"]), "H2": sc(b["years"]["HLT-2"]), "MA": sc(b["years"]["HLT-6"])}


# C19b (Package B's cap on the employer exclusion at the 75th-percentile premium) taxes a base that HX ends: as each
# employer group moves (children 2031, thirds 2033-35) its premiums leave the exclusion, so the cap has nothing left to
# collect on them. The cap's ten-year amount before the plan, on its own profile (fiscal-profiles.csv: from 2031, a
# two-year ramp, premium growth), is scaled each fiscal year by the share of employer coverage not yet moved.
C19B_BEFORE_PLAN_TN = 0.66
C19_BEFORE_PLAN_TN = 1.25   # C19, the median-premium cap (the listed fallback), on the same profile and base
C19B_PROFILE = dict(cat="rev_individual", start=2031, ramp=2, grow="out_medicare_net")


def c19b(before_tn=C19B_BEFORE_PLAN_TN):
    """C19b's (or C19's) path with the exclusion it caps ending as groups move (care follow-up 2, the lead's item)."""
    hp = health_path()
    F = fiscal()
    B = F.read_baseline(os.path.join(ROOT, "models", "data", "fiscal-baseline.csv"))
    before = F.row_path(B, before_tn, C19B_PROFILE)
    cal_left = {y: 1.0 - hp["HP"].employer_share(y, hp["kids"]) for y in range(2029, 2041)}
    left = fy(cal_left)
    after = {y: before[y] * left.get(y, 0.0) for y in W}
    mid = round(sum(after.values()) / 1000, 3)
    return dict(years=window(after), mid=mid, before_2040=before[2040], before=window(before))


def excl_full(hp):
    """The exclusion revenue at full scale (2032 basis), the base HX's path scales."""
    _, _, _, f = hp["HP"].groups(hp["I"], hp["B"], hp["P"])
    return f["tax_exclusion"]


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
        if "--c19b" in sys.argv:
            print("c19b", c19b())
            print("c19", c19b(C19_BEFORE_PLAN_TN))
        if "--incidence" in sys.argv:
            print("incidence", json.dumps(incidence(), default=str))
