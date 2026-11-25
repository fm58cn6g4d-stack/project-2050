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
- HLT-7's status-rule correction (DEC-2026-11-12-19): the single plan covers people with lawful or registered
  status, so care's base, which covered everyone but a 1% residual, is lowered by the people with no status beyond
  the residual, and Emergency Medicaid, which care's plan counted as replaced, keeps paying for everyone with no status,
  as does a federal uncompensated-care payment to hospitals at today's DSH-type share for them (DEC-2026-11-13-02)
  (dossiers/care/tools/status_rule.py; 6-cost.md part 2b). Its own component, so the correction stays visible.
- HLT-8, USDA rural health grants (discretionary).
FEHB's money is not booked (review F-4 item 3); contribution(), the care dossier's transitional employer contribution,
is reported only.

The health financing booking (stage E's financing checkpoint, DEC-2026-11-15-05 to -29; dossiers/foundations/
health-cost-review.md part 5; test_fiscal_health_financing.py):
- HLT-7's spending line on the corrected path (corrected()): each year's coverage groups from health_cost_review.rebuild()
  with the cost review's nine corrections, Medicare and Medicaid rebased to CBO (the seam, DEC-2026-11-15-28);
  components for D1 (admin-4pct), D5 (drug-prices), D2 (national-budget, from FY2037), the states at 100%
  (states-payment) and the worker transition credit (worker-credit, from FY2035);
- package E's revenue rows with the unified household contribution (financing()): HCU, the fold-in's HCW, HCA, HCP and
  HCH, the employer contribution HEC with HEX (the tax it takes from HX), and the five new streams HS1 to HS4 and H1a.
  The fold-in starts with the January 2035 endpoint; the household contribution steps with the waves before it and
  the streams start in FY2030 (DEC-2026-11-16-01, -02); transition_options() prices the proposals;
- health's first call on booked revenue (first_call()), a reassignment reported, not booked.
The booking's follow-up (no decision needed): HLT-7's status-rule component priced on the corrected base
(status_rule(corrected())); HEC and HEX after the window with the no-offer phase-in's last steps (employer_after(),
fiscal-after.csv); and the D3 household test's health rows on the corrected, booked path (incidence_booked():
incidence-rows.csv, incidence-keys.csv, incidence-phase-in.csv and scenario Q-H7 in scenarios.json).
The financing tools (health_financing.py, health_cost_review.py) read the budget as it stood before this booking
(health_before_booking.json), so the package is not counted twice; that file is frozen.
"""
import csv
import importlib.util
import json
import os
import sys

HERE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))   # models/tools: this file moved to models/bookings/ in stage H step H4
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


def status_rule(cor=None):
    """HLT-7's status-rule correction (DEC-2026-11-12-19): people with no immigration status beyond the residual are
    not covered, and Emergency Medicaid and hospitals' DSH-type uncompensated-care share (DEC-2026-11-13-02) keep paying
    for everyone with no status (dossiers/care/tools/status_rule.py,
    6-cost.md part 2b). Returns the central path and the low and high readings' FY2030-39 totals ($ billion).
    With `cor` (corrected()), the coverage removed is priced on the corrected base: care's average newly covered
    person, scaled each year by the cost review's price for the newly covered (people under 65 at private enrollees'
    repriced claims, correction 2) with D1 and D5 against the model's, at that year's hospital rate. D1 and D5 are
    priced on everyone the rebuild covers, so pricing the people removed with them on keeps each saving counted once.
    Emergency Medicaid and the DSH-type share are federal payments outside the plan's prices and stay as they are."""
    SR = _load("hb_status_rule", os.path.join(ROOT, "dossiers", "care", "tools", "status_rule.py"))
    hs = [SR.health(i) for i in range(3)]
    scale = {y: 1.0 for y in FY}
    if cor is not None:
        pp = cor["newly_pp"]
        scale = {y: pp["d5"][cor["glide"][y]] / pp["model"][cor["glide"][y]] for y in FY}
    runs = [{y: h["removed"][y] * scale[y] + h["em_kept"][y] + h["dsh_kept"][y] for y in FY} for h in hs]
    return dict(path=runs[1], window=[sum(r[y] for y in W) for r in runs], fy2040=[r[2040] for r in runs],
                care_base=[sum(h["net"][y] for y in W) for h in hs], scale=scale)


def hlt6_part_a_share():
    """Part A's share of HLT-6's Advantage savings, credited to HI (funds-parameters.csv; care follow-up 3)."""
    with open(os.path.join(INPUTS, "funds-parameters.csv"), newline="", encoding="utf-8") as f:
        return float(next(r["value"] for r in csv.DictReader(f) if r["key"] == "hi_hlt6_part_a_share"))


def perm_for(B, F, path, target2040, grow=GROW):
    """The perm that makes a years row's FY2040 equal target2040 (row_path: FY2039 x perm x growth)."""
    g = F.growth_index(B, grow)
    return target2040 / (path[2039] * g[2040] / g[2039])


def booking(full=True):
    """The health rows. With `full` (the default), HLT-7 on the corrected path and the package's rows
    (DEC-2026-11-15-05 to -29: corrected(), financing()); `full=False` gives only the rows other bookings read
    (HLT-4's health parts, HLT-1, HLT-2, HLT-6), without the financing tools, which read them in turn."""
    hp = health_path()
    F = fiscal()
    B = F.read_baseline(os.path.join(ROOT, "models", "data", "fiscal-baseline.csv"))

    # HLT-1: restoration in calendar 2030, on fiscal years
    hlt1 = fy({2030: hp["restore_cal"]})
    # HLT-7 spending line: the path's net cost plus the exclusion revenue it nets, less the restoration (HLT-1). Booked
    # on the corrected path, Medicare rebased to CBO (DEC-2026-11-15-05, -28); spend0 is the care dossier's own path
    spend0 = {y: hp["net"][y] + hp["excl"][y] - hlt1.get(y, 0.0) for y in W + [2040]}
    cor = corrected() if full else None
    spend = {y: cor["errors"][y] + hp["excl"][y] - hlt1.get(y, 0.0) for y in W + [2040]} if full else spend0
    # part 6's federal-coverage correction, on HX's path: less spending (a negative component) and less HX
    xf = excl_full(hp)
    fedcov = {y: -FEDCOV_SPEND_2032 / xf * hp["excl"][y] for y in W + [2040]}
    # the status rule (DEC-2026-11-12-19): coverage removed for people with no status, Emergency Medicaid kept, and
    # hospitals' DSH-type uncompensated-care share kept for them (DEC-2026-11-13-02)
    sr = status_rule(cor)
    status = {y: sr["path"][y] for y in W + [2040]}
    hx = {y: hp["excl"][y] * (1 - FEDCOV_REVENUE_2032 / xf) for y in W + [2040]}
    terr_shape = {y: spend0[y] for y in W + [2040]}    # the territories phase in on the waves (HLT-7.28)
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
        "HLT-7/federal-coverage": window(fedcov), "HLT-7/status-rule": window(status),
        "HLT-4/children-continuous-coverage": window(kids), "HLT-4/medicaid-dental-and-bundle": window(dental),
        "HX": window(hx),
    }
    hlt7_fy = {"plan-spending": spend, "transition-fund": {y: TRANSITION_FUND.get(y, 0.0) for y in FY},
               "territories": terr, "worker-help": {y: WORKER_HELP.get(y, 0.0) for y in FY},
               "federal-coverage": fedcov, "status-rule": status}
    rev_fy, fin, after, hi_part = {}, None, {}, {}
    if full:
        fin = financing()
        # D2 on the plan's whole gross with the errors fixed: the coverage groups' gross cost and the HLT-7 items
        # that are part of it (the territories, the federal-coverage and status-rule corrections), as cost_cases()
        d2 = {y: (cor["gross_errors"][y] + terr.get(y, TERRITORIES_FY2040) + fedcov[y] + status[y]) * cor["hold"][y]
              for y in FY}
        hlt7_fy.update({"admin-4pct": cor["d1"], "drug-prices": cor["d5"], "national-budget": d2,
                        "states-payment": cor["states"], "worker-credit": fin["credit"]})
        for k in ("admin-4pct", "drug-prices", "national-budget", "states-payment", "worker-credit"):
            years["HLT-7/" + k] = window(hlt7_fy[k])
        after["HLT-7/worker-credit"] = credit_after(fin["credit"][2040])
        after.update(employer_after(fin, B, F))
        rev_fy = dict(fin["rows"])
        # DEC-2026-11-16-02 restores H1a's early years to Medicare's HI fund: HI keeps FY2030-34 and FY2035's
        # October-December 2034 quarter (funds-parameters.csv hi_h1a_bn, credited in funds-model.py), and the ledger
        # row books only what the decision leaves on the general fund, from the January 2035 endpoint, when HI folds
        # into the plan's fund (HLT-6's Part A pattern; financing audit part D, item 1). Households pay the whole
        # stream either way (incidence-rows.csv H1a).
        h1a = fin["rows"]["H1a"]
        rev_fy["H1a"] = {y: v * ENDPOINT[y] for y, v in h1a.items()}
        hi_part["H1a"] = window({y: h1a[y] * (1 - ENDPOINT[y]) for y in W})
        for k, v in rev_fy.items():
            years[k] = window(v)
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
                                    perm_for(B, F, {2039: years["HLT-7/federal-coverage"][-1]}, fedcov[2040])),
                                   ("status-rule", amt["HLT-7/status-rule"],
                                    perm_for(B, F, {2039: years["HLT-7/status-rule"][-1]}, status[2040]))]
                         + ([(k, amt["HLT-7/" + k], perm_for(B, F, {2039: years["HLT-7/" + k][-1]}, hlt7_fy[k][2040]))
                             for k in NEW_HLT7] if full else []))
    comps = {"HLT-7": c7}
    ledger = {
        "HLT-1": (r3(amt["HLT-1"]), r3(amt["HLT-1"]), r3(amt["HLT-1"] + 0.25)),   # HLT-1.03's provider-tax range, $0-0.25T
        "HLT-2": (0.31, r3(amt["HLT-2"]), 0.53),                                 # 0.25-0.35 upgrades + 0.06-0.18 wait
        "HLT-3": (0, 0, 0), "HLT-5": (0, 0, 0),
        "HLT-6": (r3(amt["HLT-6"] * (1 - hlt6_part_a_share())),) * 3,   # Part B's share; Part A's goes to HI (funds model)
        # the high end also carries D2 not achieved (DEC-2026-11-15-08: never done before, EV-CAR-742)
        "HLT-7": (r3(hlt7_mid - RATE_RANGE_TN[0] - LTC_RANGE_TN[0] - 0.05 - 0.04 - (sr["window"][1] - sr["window"][0]) / 1000),
                  hlt7_mid,
                  r3(hlt7_mid + RATE_RANGE_TN[1] + LTC_RANGE_TN[1] + 0.05 + 0.09 + (sr["window"][2] - sr["window"][1]) / 1000
                     - (amt.get("HLT-7/national-budget", 0.0) if full else 0.0))),
        "HLT-8": HLT8_TN,
        "HX": (r3(amt["HX"] * (1 - HALF_PASSTHROUGH_FY2040 / hp["excl"][2040])), r3(amt["HX"]), r3(amt["HX"])),
    }
    perms = {"HX": perm_for(B, F, {2039: years["HX"][-1]}, hx[2040])}
    revenue = {}
    for k, v in rev_fy.items():
        lo_m, hi_m = REVENUE_RANGE.get(k, (1.0, 1.0))
        mid = r3(amt[k])
        lo, hi = sorted((r3(mid * lo_m), r3(mid * hi_m)))
        revenue[k] = (lo, mid, hi)
        perms[k] = perm_for(B, F, {2039: years[k][-1]}, v[2040], REVENUE_CAT[k])
    fy2040 = dict(spending=spend[2040], exclusion=hx[2040], contribution=hp["contribution"][2040],
                  territories=TERRITORIES_FY2040, net=hp["net"][2040], federal_coverage=fedcov[2040],
                  exclusion_before_correction=hp["excl"][2040], status_rule=status[2040])
    fedcov_net = (sum(fedcov[y] for y in W) + sum(hp["excl"][y] - hx[y] for y in W)) / 1000
    totals = dict(net_window=sum(hp["net"][y] for y in W) / 1000, federal_coverage_net=fedcov_net,
                  worker_help=sum(WORKER_HELP.values()) / 1000,
                  with_contribution=(sum(hp["net"][y] for y in W) - sum(hp["contribution"][y] for y in W)) / 1000,
                  contribution_window=sum(hp["contribution"][y] for y in W) / 1000,
                  status_rule_window=sum(status[y] for y in W) / 1000, status_rule_range=sr["window"],
                  status_rule_fy2040_range=sr["fy2040"])
    hlt4_path = [round(part["safety_net"][y] + kids[y] + dental[y], 2) for y in W]   # health's parts of HLT-4
    if full:
        totals.update(seam_window=sum(cor["model"][y] - hp["net"][y] for y in W) / 1000,
                      corrected_window=sum(cor["errors"][y] - cor["model"][y] for y in W) / 1000)
        fy2040.update(seam=cor["model"][2040] - hp["net"][2040], corrections=cor["errors"][2040] - cor["model"][2040],
                      **{k: hlt7_fy[k][2040] for k in NEW_HLT7}, revenue={k: v[2040] for k, v in rev_fy.items()})
    return dict(years=years, components=comps, ledger=ledger, perms=perms, fy2040=fy2040, totals=totals, hlt4_path=hlt4_path,
                hlt4_parts=hlt4_parts, revenue=revenue, hlt7_fy=hlt7_fy, revenue_fy=rev_fy, hi=hi_part, spend_before=spend0, after=after,
                contribution={y: hp["contribution"][y] for y in W + [2040]})



# ---- the health financing booking (stage E's financing checkpoint; DEC-2026-11-15-05 to -29) ----------------------
# Espen's decisions of November 15 (PR #393): the cost review's corrections (DEC-2026-11-15-05), D5 drugs 25% below
# today's (-06), D1 administration at 4% (-07), D2 a national health budget at GDP + 1 from 2037 (-08), package E
# (-09) with the unified household contribution (-10 to -13), the small-employer allowance (-14), the five new streams
# (-15 to -19), health's first call on booked revenue (-20), the employer contribution and its rules (-21 to -23), the
# worker transition credit (-24), the states at 100% (-25), the self-employed (-26), D3 and D4 kept (-27), HLT-7 on
# CBO's Medicare figure (-28) and counting in the plan's fund (-29). Espen's answers of November 16 settle the
# transition: the household contribution steps with the waves from 2031, with the 5-point surcharge, and the fold-in
# starts with the January 2035 endpoint (DEC-2026-11-16-01); the five new streams start in FY2030 (-02); the
# small-employer allowance applies to the premium-based contribution in FY2031-34 too (-03).
FY = W + [2040]
# DEC-2026-11-16-01: the unified contribution's base rate before the January 2035 endpoint, by calendar year, in steps
# with the share of people moved (2.25% x 26% in 2031-32, x 44% in 2033, x 63% in 2034; transition_options())
WAVE_STEPS = {2031: 0.6, 2032: 0.6, 2033: 1.0, 2034: 1.4}
NEW_HLT7 = ("admin-4pct", "drug-prices", "national-budget", "states-payment", "worker-credit")
D1_ADMIN, D5_DRUGS = 0.04, 0.25           # DEC-2026-11-15-07, -06
D2_EXTRA, D2_START = 0.01, 2037           # DEC-2026-11-15-08
STATES_SHARE = 1.0                        # DEC-2026-11-15-25: 100% of former Medicaid spending, on the rebased base
UNIFIED = dict(R=2.25, S_BASE=5.0, lo=1.38, hi=2.5, form="linear")   # DEC-2026-11-15-11 to -13; S = 5 + H1b's points
ENDPOINT = {y: (0.0 if y < 2035 else (0.75 if y == 2035 else 1.0)) for y in FY}   # calendar 2035 on fiscal years
# The package's revenue rows ($B a year, a gain positive): (id, the cost review's FY2040 figure's key, category, growth
# index before FY2040, from), with the range's (lo, hi) as multiples of the central figure.
STREAMS = [   # health_cost_review.NEW_STREAMS, in order (DEC-2026-11-15-15 to -19); H1a is the ledger's own row
    ("HS1", "rev_other", (0.5, 1.5)), ("HS2", "rev_individual", (0.0, 250 / 150)),
    ("HS3", "rev_individual", (20 / 45, 70 / 45)), ("HS4", "rev_corporate", (40 / 70, 100 / 70)),
    ("H1a", "rev_individual", (45 / 60, 75 / 60))]
REVENUE_CAT = dict(HCU="rev_individual", HCW="rev_payroll", HCA="rev_payroll", HCP="rev_payroll",
                   HCH="rev_individual", HEC="rev_payroll", HEX="rev_individual", **{k: c for k, c, _ in STREAMS})
# Ranges: the streams' own (health-cost-review.md part 2.2); the household contribution at a 30% and a 10% avoidance
# allowance against the central 20% (health-household-contribution.md part 7); the rest are formula rows, mid only
REVENUE_RANGE = dict(HCU=(0.7 / 0.8, 0.9 / 0.8), **{k: r for k, _, r in STREAMS})
_CACHE = {}


def _hf():
    sys.path.insert(0, HERE)
    sys.path.insert(0, os.path.join(HERE, "household"))
    import health_cost_review as CR
    import health_financing as HF
    return HF, CR


def corrected():
    """HLT-7's spending line on the corrected care path (DEC-2026-11-15-05, -28): dossiers/care/tools/health_path.py's
    fiscal-year path, run with each year's coverage groups from health_cost_review.rebuild() with every correction on
    (CORRECTED) and Medicare rebased to CBO (health_financing.coverage(True)), in place of health_path.groups(). rebuild()
    at its DEFAULT options reproduces groups() exactly (check_reproduces()), so the corrections are the only change.
    Then D1 and D5 on the same path, each its own component; D2 on the gross cost from FY2037; and the states' payment
    from 50% (what the path nets) to 100% of their former spending on the rebased base, CHIP's included ($ billion by
    fiscal year; a cost positive)."""
    if "corrected" in _CACHE:
        return _CACHE["corrected"]
    HF, CR = _hf()
    c = HF.coverage(True)
    HP, I, B, P = c["HP"], c["I"], c["B"], c["P"]
    glide = HP.rate_path(HP.hospital_start(I, B))
    ctx0 = CR._ctx()
    keep = CR._ctx
    CR._ctx = lambda: ctx0
    try:
        cases = {"model": (None, {}), "errors": (CR.CORRECTED, {}), "d1": (CR.CORRECTED, dict(sp_admin=D1_ADMIN)),
                 "d5": (CR.CORRECTED, dict(sp_admin=D1_ADMIN, sp_drug_cut=D5_DRUGS))}
        reb = {k: {r: CR.rebuild(o, hosp_rate=r, I_over=i) for r in set(glide.values())} for k, (o, i) in cases.items()}
    finally:
        CR._ctx = keep
    facts = HP.groups(I, B, P)[3]
    orig = HP.groups
    series = {}
    try:
        for k, cache in reb.items():
            HP.groups = lambda I_, B_, P_, hosp_rate=HP.TARGET, cache=cache: (cache[hosp_rate]["net"], None, None, facts)
            series[k], gf = HP.path(I, B, P, glide)
    finally:
        HP.groups = orig
    tot = {k: {y: s[y]["total"] for y in FY} for k, s in series.items()}
    r0 = reb["errors"][HP.TARGET]
    # the states: the path nets sp_state_moe (50%) of Medicaid's state part outside long-term care; at 100% they pay all
    # of their former spending for the people who move, CHIP's state part included (health_cost_review's states, $466B)
    netted = r0["state_moe_booked"] - I["sp_retained_other"]
    extra_full = STATES_SHARE * r0["state_former"] - netted
    mcd = HF.moved_shares(c)["medicaid"]
    states = {y: -extra_full * mcd[y] for y in FY}
    # D2: the plan's gross cost held to GDP + 1 point from 2037 (health_financing.growth_hold(), year by year), on the
    # errors-fixed gross, as health_cost_review.cost_cases() prices it
    gdp = HF.plan_gap()["gdp"]
    gdp[2040] = float(HF.paths()[2040]["gdp_bn"])
    g = {y: series["errors"][y]["moved_gf"] for y in FY}    # all groups moved from 2036: the gross grows with gf
    gross = {y: r0["cost_total"] * g[y] for y in FY}
    hold = {y: ((gdp[y] / gdp[2036]) * (1 + D2_EXTRA) ** (y - D2_START + 1) / (gf[y] / gf[2036]) - 1)
            if y >= D2_START else 0.0 for y in FY}
    out = dict(model=tot["model"], errors=tot["errors"], d1={y: tot["d1"][y] - tot["errors"][y] for y in FY},
               d5={y: tot["d5"][y] - tot["d1"][y] for y in FY}, hold=hold, states=states, gross_errors=gross,
               state_former_full=r0["state_former"], states_netted_full=netted, glide=glide,
               full_2032={k: {r: v["net_total"] for r, v in c_.items()} for k, c_ in reb.items()},
               newly_pp={k: {r: v["groups"]["uninsured"]["per_person_2032"] for r, v in c_.items()}
                         for k, c_ in reb.items()})
    _CACHE["corrected"] = out
    return out


def financing():
    """Package E with the unified household contribution (DEC-2026-11-15-09 to -24), FY2040 from
    health_cost_review.unified_package() and year by year FY2030-40 ($ billion; revenue a gain positive, spending a cost
    positive). The employer contribution follows the waves from 2031 (health_financing.package_path(): on the premiums
    of the coverage moved, with the small-employer allowance, DEC-2026-11-16-03, then the payroll-based contribution
    with the no-offer phase-in from 2035), and the credit starts in 2035. The household contribution steps with the
    waves from 2031 with the 5-point surcharge (DEC-2026-11-16-01), in full from the January 2035 endpoint, when the
    fold-in starts (the worker's HI, the 0.9% and worker HI on former premiums end; H1b's wage half loses its base, won
    back in the surcharge). The five new streams start in FY2030 (DEC-2026-11-16-02). Health's first call on booked
    revenue is what is left of health's need each year (a reassignment, not a row: it changes no total)."""
    if "financing" in _CACHE:
        return _CACHE["financing"]
    HF, CR = _hf()
    ctx = HF.context()
    case = CR.cost_cases(CR._g40())["design"]
    h1b = CR.h1b_restated(ctx)
    u = CR.unified_spec(UNIFIED["R"], S=UNIFIED["S_BASE"] + h1b["fold_into_s_points"], lo=UNIFIED["lo"],
                        hi=UNIFIED["hi"], form=UNIFIED["form"])
    o = CR.unified_package(ctx, case, u)
    # the employer contribution and the credit, year by year, on package F's spec (health_cost_review.health_package)
    allow = CR.SMALL_FIRM_ALLOWANCE_SHARE / HF.band_share()
    f40 = dict(ctx["f40"])
    f40["states_moved"] += case["state"]
    f40["households"] -= case["outside"]
    spec = dict(HF.COMMON, emp_share=1 - allow, need=o["need_case"], f40=f40, first=0.0, second=0.0,
                savings=o["streams"] + o["remainder_F"], close="second")
    pp = HF.package_path(ctx, spec, ctx["need_p"], ctx["flows_p"], ctx["gap"])
    per = {y: HF.per_point(ctx["gap"], y) for y in FY}
    inc = {y: per[y]["high_income"] / per[2040]["high_income"] for y in FY}       # GDP, as the income tiers
    pay = {y: per[y]["payroll_gross"] / per[2040]["payroll_gross"] for y in FY}   # the payroll point
    b = booking_base()
    hxr = {y: b["hx"][y] / b["hx"][2040] for y in FY}
    E, tau, lost = ENDPOINT, ctx["tau"], o["lost"]
    emp = {y: pp[y]["employer_gross"] for y in FY}
    rows = {
        "HCU": {y: o["household_collected"] * inc[y] * E[y] for y in FY},
        "HCW": {y: -lost["W"] * pay[y] * E[y] for y in FY},
        "HCA": {y: -lost["A"] * pay[y] * E[y] for y in FY},
        "HCP": {y: -lost["hxp"] * hxr[y] * E[y] for y in FY},
        "HCH": {y: -lost["H1b"] * inc[y] * E[y] for y in FY},
        "HEC": emp,
        "HEX": {y: -tau * emp[y] for y in FY},
    }
    # DEC-2026-11-16-01: before the endpoint the base rate steps with the waves (WAVE_STEPS) and the surcharge is 5
    # points from wave 1 (H1b keeps its own base until the fold-in), with no credit for premiums still paid; the fold-in
    # rows start with the endpoint. Calendar years on the fiscal-year blend, at each fiscal year's income growth.
    h = o["haircut"]
    base40 = CR.unified_statutory_bn(ctx, dict(u, S=0.0), "base") * (1 - h)              # R in full, FY2040
    sur40 = CR.unified_statutory_bn(ctx, dict(u, S=UNIFIED["S_BASE"]), "surcharge") * (1 - h)   # 5 points, FY2040
    cal = {c: base40 * WAVE_STEPS[c] / UNIFIED["R"] + sur40 for c in WAVE_STEPS}
    pre = {y: (0.25 * cal.get(y - 1, 0.0) + 0.75 * cal.get(y, 0.0)) * inc[y] for y in FY}
    rows["HCU"] = {y: rows["HCU"][y] + pre[y] for y in FY}
    # DEC-2026-11-16-02: the five streams start with the 2029 act, in FY2030, at their central yields grown with GDP
    for (rid, _, _), (_, v, _, _) in zip(STREAMS, CR.NEW_STREAMS):
        rows[rid] = {y: v * inc[y] for y in FY}
    credit = {y: pp[y]["credit"] for y in FY}
    out = dict(rows=rows, credit=credit, package=o, spec=u, tau=tau, allowance_share=allow, path=pp, case=case,
               h1b=h1b, statutory_2040=o["statutory"], haircut=o["haircut"], before_endpoint=pre,
               base_2040=base40, surcharge5_2040=sur40)
    _CACHE["financing"] = out
    return out


CREDIT_LAST_FULL, CREDIT_NONE_FROM = 2044, 2049   # DEC-2026-11-15-24: in full through 2044, none from 2049
AFTER_YEARS = list(range(2040, 2051))   # through FY2050, the first year at zero


def credit_after(credit_2040, B=None, F=None):
    """The worker transition credit after the window, FY2040-49 ($ billion), for fiscal-after.csv: in full through
    calendar 2044, growing with pay (the payroll category), then a fifth less each year (80% in 2045 to 20% in 2048)
    and none from calendar 2049 (DEC-2026-11-15-24; health_financing.py WORKER_CREDIT), on the fiscal-year blend.
    FY2049 keeps a quarter of calendar 2048's 20%; from FY2050 it is zero."""
    F = F or fiscal()
    B = B or F.read_baseline(os.path.join(ROOT, "models", "data", "fiscal-baseline.csv"))
    g = F.growth_index(B, "rev_payroll")
    share = lambda y: 1.0 if y <= CREDIT_LAST_FULL else max(0.0, 1 - (y - CREDIT_LAST_FULL) / (CREDIT_NONE_FROM - CREDIT_LAST_FULL))  # noqa: E731
    return {y: round(credit_2040 * g[y] / g[2040] * (0.25 * share(y - 1) + 0.75 * share(y)), 2) for y in AFTER_YEARS}


HEC_AFTER_YEARS = list(range(2040, 2046))   # the no-offer phase-in is full in calendar 2044, so in FY2045


def employer_after(fin, B=None, F=None):
    """The employer contribution (HEC) and the tax it takes from HX (HEX) after the window, FY2040-45, for
    fiscal-after.csv ($ billion): the gross on the premiums moved, growing with pay (the payroll category), less what
    employers with no 2028 coverage do not yet pay (DEC-2026-11-15-23 (b): a tenth of the rate in 2035, full in 2044;
    health_financing.phase_left()), so the phase-in's last steps are counted. From FY2046 the rows grow with their
    growth index, as before. Signs as fiscal-after.csv keeps them for revenue rows: a gain negative."""
    HF, _ = _hf()
    F = F or fiscal()
    B = B or F.read_baseline(os.path.join(ROOT, "models", "data", "fiscal-baseline.csv"))
    g = F.growth_index(B, "rev_payroll")
    p40 = fin["path"][2040]
    gross40 = p40["employer_gross"] + p40["phase_in"]
    per_left = p40["phase_in"] / HF.phase_left(2040)          # the uncharged pay at the whole rate, FY2040
    hec = {y: (gross40 - per_left * HF.phase_left(y)) * g[y] / g[2040] for y in HEC_AFTER_YEARS}
    # a revenue row's path in fiscal-after.csv is in deficit terms: a gain is negative (as C1T's)
    return {"HEC": {y: round(-v, 2) for y, v in hec.items()}, "HEX": {y: round(fin["tau"] * v, 2) for y, v in hec.items()}}


def booking_base():
    """The pieces of the booking that the financing reads: HX's path ($ billion by fiscal year)."""
    hp = health_path()
    xf = excl_full(hp)
    return dict(hx={y: hp["excl"][y] * (1 - FEDCOV_REVENUE_2032 / xf) for y in FY})


def first_call(b=None):
    """Health's first call on booked revenue (DEC-2026-11-15-20), by fiscal year ($ billion): health's own booked need
    after this booking (its spending rows, less HX), less the package's own revenue rows. Plan-wide, the gap is the
    rest of the plan's (about $70B in FY2040, health_cost_review.GAP_BEFORE_REASSIGN) plus this."""
    HF, _ = _hf()
    b = b or booking()
    before = HF.audit_lines()
    old7 = {y: before["HLT-7"].get(y, 0.0) for y in FY}
    new7 = {y: sum(b["hlt7_fy"][k][y] for k in b["hlt7_fy"]) for y in FY}
    need0 = HF.need_path(HF.seam())
    need = {y: need0[y]["booked"] + new7[y] - old7[y] for y in FY}
    own = {y: sum(v[y] for v in b["revenue_fy"].values()) for y in FY}
    return {y: need[y] - own[y] for y in FY}, need, own


def transition_options():
    """Part 9, question 9 for the unified contribution, as priced for Espen (decided November 16: 'waves',
    DEC-2026-11-16-01): what each path for FY2031-35 collects before the endpoint ($ billion by fiscal year), and the
    share of people moved that sets the steps. 'endpoint': nothing before January 2035; 'waves': the base rate in steps
    with the share of people moved (the exemption as decided) and the surcharge at 5 points from wave 1, no fold-in
    before the endpoint (HI still pays Medicare's claims) and no credit for premiums still paid; 'full': R and S = 5
    in full from wave 1. first_call is the booked first call less what each option collects beyond the booked one."""
    HF, CR = _hf()
    ctx = HF.context()
    f = financing()
    u = f["spec"]
    h = f["haircut"]
    base40 = CR.unified_statutory_bn(ctx, dict(u, S=0.0), "base") * (1 - h)
    sur40 = CR.unified_statutory_bn(ctx, dict(u, S=UNIFIED["S_BASE"]), "surcharge") * (1 - h)
    c = HF.coverage(True)
    HP, I, B, P = c["HP"], c["I"], c["B"], c["P"]
    facts = HP.groups(I, B, P)[3]
    people = facts["people"]
    moved = {}
    for y in range(2030, 2036):
        sh = HP.shares_moved(y, facts["child_share_moving"])
        sh["employer"] = HP.employer_share(y, facts["child_share_employer"])
        moved[y] = sum(sh[k] * people[k] for k in people) / sum(people.values())
    mfy = {y: 0.25 * moved.get(y - 1, 0.0) + 0.75 * moved[y] for y in range(2031, 2036)}
    per = {y: HF.per_point(ctx["gap"], y) for y in FY}
    inc = {y: per[y]["high_income"] / per[2040]["high_income"] for y in FY}
    on = {y: 0.25 * (y - 1 >= 2031) + 0.75 * (y >= 2031) for y in FY}
    pre = {y: 1.0 - ENDPOINT[y] for y in FY}          # the part of each fiscal year before calendar 2035
    calls, _, _ = first_call()
    out = dict(moved_share=moved, steps={y: round(UNIFIED["R"] * moved[y], 2) for y in range(2031, 2035)},
               base_2040=base40, surcharge5_2040=sur40, options={})
    for name in ("endpoint", "waves", "full"):
        got = {}
        for y in range(2031, 2036):
            if name == "endpoint":
                got[y] = 0.0
            elif name == "waves":
                got[y] = (base40 * mfy[y] + sur40) * inc[y] * on[y] * pre[y]
            else:
                got[y] = (base40 + sur40) * inc[y] * on[y] * pre[y]
        booked = {y: f["before_endpoint"][y] for y in got}
        out["options"][name] = dict(collected=got, first_call={y: calls[y] - got[y] + booked[y] for y in got},
                                    collected_window=sum(got.values()))
    return out


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
    """HLT-7's household rows on the care dossier's own fiscal-year path, FY2030-39 ($ trillion), with their year
    shapes and the distribution key for household premiums and out-of-pocket costs removed. The financing tools
    (health_financing.py, health_cost_review.py) measure from these; the D3 test's rows are incidence_booked()'s,
    on the corrected, booked path."""
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
        paths={"H7h": h7h, "H7w": wages},
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
    b = booking(full=False)
    sc = lambda v: [round(x / max(v, key=abs), 3) + 0.0 if max(v, key=abs) else 0.0 for x in v]  # noqa: E731
    return {"H1": sc(b["years"]["HLT-1"]), "H2": sc(b["years"]["HLT-2"]), "MA": sc(b["years"]["HLT-6"])}


# ---- the household test (D3) on the corrected, booked path (incidence-rows.csv; scenario Q-H7) ----
# Each row follows the cost review's household record (health_cost_review.unified_package()'s rows, FY2040) on the
# booked fiscal-year paths, FY2030-39. Keys the D3 test already holds are used where the base is the same; the
# contribution's, the employer contribution's and the credit's keys are the household model's measurements that the
# record uses, typed into incidence-keys.csv (keys.csv marks them kept). Where the record and D3's conventions differ,
# D3's are kept: HS4's corporate increment on the 25/75 convention, and H1b's wage half (HCH) on H1b's own key, so the
# two cancel exactly. The 0.9% (HCA) uses the key of wages above $250,000 (the record's own key is measured on the
# CPS, which top-codes wages).
D3_FOLD = {"HCW": "wages", "HCA": "above250k_wages", "HCP": "exclusion_end", "HCH": "inv400k"}
D3_STREAMS = {"HS1": "ftt", "HS2": "billionaires", "HS3": "inv400k", "HS4": "wages 0.25*x; capital 0.75*x"}
# DEC-2026-11-15-29: health's contributions are counted outside D3's revenue-mix test, as replacements for premiums:
# the household and employer contributions and the rows that fold into them. HEX stays in, with HX: it is the part of
# HX's tax on former premiums that never arises because employers pay the contribution instead (models/tools/
# household/d3.py, HEALTH_CONTRIBUTIONS, holds the same list).
D3_CONTRIBUTIONS = ("HCU", "HCUw", "HCW", "HCA", "HCP", "HCH", "HEC")
D3_KEY_NOTES = {
    "health_contrib": "the unified household contribution from the January 2035 endpoint (DEC-2026-11-15-10 to -13: "
                      "2.25% of AGI with the exemption from 138% to 250% of poverty, plus the surcharge with H1b's "
                      "points), its statutory charge on the 2029 households at FY2040's parameters "
                      "(health_cost_review.py _unified_key(); health_booking.py incidence_booked())",
    "health_contrib_wave": "the unified household contribution before the endpoint (DEC-2026-11-16-01: the base rate "
                           "in steps with the waves, at its window-weighted average, and the 5-point surcharge), as "
                           "health_contrib (health_booking.py incidence_booked())",
    "health_contrib_avoid": "what avoidance keeps the unified contribution from collecting (the 20% allowance): all in "
                            "the top quintile, the top 1% scaled as the contribution's own key "
                            "(health_financing.py avoidance_key(); health_booking.py incidence_booked())",
    "employer_contrib": "the employer health contribution (DEC-2026-11-15-21 to -23): pay between $20,000 and the "
                        "wage base, less the no-offer phase-in's uncharged pay, weighted by the booked FY2031-39 path; "
                        "on workers, as premiums are (health_financing.py wages_band and wages_band_nooffer; "
                        "health_booking.py incidence_booked())",
    "health_credit": "the worker transition credit (DEC-2026-11-15-24): band pay of workers with no employer, "
                     "marketplace or Medicare coverage, phased out from $60,000 to $120,000 of AGI, weighted by the "
                     "booked FY2035-39 path (health_financing.py credit_key(); health_booking.py incidence_booked())",
}


def _shape(v):
    """A year path as a phase-in shape (incidence-phase-in.csv, method norm): each year over the largest in size."""
    m = max(v, key=abs)
    return [round(x / m, 3) + 0.0 if m else 0.0 for x in v]


def _blend(parts):
    """A key from (weight, (shares, top 1%)) pairs."""
    tot = sum(w for w, _ in parts)
    q = [sum(w * k[0][i] for w, k in parts) / tot for i in range(5)]
    return q, sum(w * k[1] for w, k in parts) / tot


def incidence_booked():
    """The D3 test's health rows on the corrected, booked path (DEC-2026-11-15-05 to -29, DEC-2026-11-16-01 to -03):
    HLT-7's household rows, the worker transition credit, package E's household-facing rows and the four new streams
    with their own rows (H1a keeps its package row), FY2030-39 ($ trillion), with their keys and year shapes.
    - H7h: premiums and out-of-pocket costs households stop paying, less the spending that stays outside the plan
      (the cost review's correction: nursing and non-durables bought out of pocket), on the groups' moves;
    - H7w: employer premiums that become pay, without federal coverage (FEHB, TRICARE and the VA), on HX's path;
    - H7x: HX as booked (already corrected); H7c: the credit (HLT-7/worker-credit);
    - HCU (from the endpoint) and HCUw (before it) split HCU's booked path; HCW to HCH, HEC, HEX and HS1 to HS4 are
      their ledger rows."""
    if "incidence_booked" in _CACHE:
        return _CACHE["incidence_booked"]
    HF, CR = _hf()
    ctx = HF.context()
    K = ctx["K"]
    f = financing()
    b = booking()
    inc = incidence()
    f40 = ctx["f40"]
    k_hh = (f40["households"] - f["case"]["outside"]) / f40["households"]
    k_emp = f40["employers"] / f40["employers_all"]
    tn = lambda d: round(sum(d.get(y, 0.0) for y in W) / 1000, 3)  # noqa: E731
    paths = {"H7h": {y: v * k_hh for y, v in inc["paths"]["H7h"].items()},
             "H7w": {y: v * k_emp for y, v in inc["paths"]["H7w"].items()},
             "H7c": f["credit"],
             "HCUw": f["before_endpoint"],
             "HCU": {y: f["rows"]["HCU"][y] - f["before_endpoint"][y] for y in FY}}
    for k in ("HCW", "HCA", "HCP", "HCH", "HEC", "HEX", *D3_STREAMS):
        paths[k] = f["rows"][k]
    # keys: the contribution's at FY2040's parameters (financing() registered it), and before the endpoint at the
    # window-weighted step with the 5-point surcharge
    u = f["spec"]
    pre = f["before_endpoint"]
    step = {y: 0.25 * WAVE_STEPS.get(y - 1, 0.0) + 0.75 * WAVE_STEPS.get(y, 0.0) for y in W}
    r_wave = sum(pre[y] * step[y] for y in W) / sum(pre[y] for y in W)
    tag = f["package"]["key"]
    tag_w = CR._unified_key(ctx, dict(u, R=round(r_wave, 4), S=UNIFIED["S_BASE"]))
    # the employer contribution: band pay less the no-offer phase-in's uncharged pay, on the booked path
    HF.no_offer()
    pp = f["path"]
    emp = _blend([(pp[y]["employer_gross"] + pp[y]["phase_in"], K["wages_band"]) for y in W if pp[y]["employer_gross"]]
                 + [(-pp[y]["phase_in"], K["wages_band_nooffer"]) for y in W if pp[y]["phase_in"]])
    c = HF.WORKER_CREDIT
    cred = _blend([(f["credit"][y], K[HF.credit_key(c["start"], c["end"], HF.phase_left(y), c["nocov_only"])[0]])
                   for y in W if f["credit"][y]])
    keys = {"health_contrib": K[tag], "health_contrib_wave": K[tag_w], "health_contrib_avoid": K["avoid_" + tag],
            "employer_contrib": emp, "health_credit": cred}
    keys = {k: (close(q), round(t1, 1)) for k, (q, t1) in keys.items()}
    h = f["haircut"]
    contrib = f"{{key}} {round(1 / (1 - h), 6):g}*x; health_contrib_avoid {-round(h / (1 - h), 6):g}*x"
    rows = {"H7h": tn(paths["H7h"]), "H7w": tn(paths["H7w"]), "H7c": tn(paths["H7c"]), "HCUw": tn(paths["HCUw"])}
    amounts = {"H7h": rows["H7h"], "H7w": rows["H7w"], "H7x": "[HX]", "H7c": rows["H7c"], "HCUw": rows["HCUw"],
               "HCU": f"[HCU]-{rows['HCUw']}", **{k: f"[{k}]" for k in ("HCW", "HCA", "HCP", "HCH", "HEC", "HEX")},
               **{k: f"[{k}]" for k in D3_STREAMS}}
    parts = {"H7h": "health_hh", "H7w": "employer_cov", "H7x": "exclusion_end", "H7c": "health_credit",
             "HCU": contrib.format(key="health_contrib"), "HCUw": contrib.format(key="health_contrib_wave"),
             **D3_FOLD, "HEC": "employer_contrib", "HEX": "employer_contrib", **D3_STREAMS}
    shapes = {k: _shape([paths[k].get(y, 0.0) for y in W]) for k in paths}
    out = dict(rows=rows, amounts=amounts, parts=parts, keys=keys, shapes=shapes, paths=paths, r_wave=r_wave,
               factors=dict(households=k_hh, employers=k_emp), haircut=h,
               window={k: tn(v) for k, v in paths.items()}, credit_window=sum(b["years"]["HLT-7/worker-credit"]) / 1000)
    _CACHE["incidence_booked"] = out
    return out


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
        print("totals", {k: (round(v, 3) if not isinstance(v, list) else [round(x, 1) for x in v])
                         for k, v in b["totals"].items()})
        if "--c19b" in sys.argv:
            print("c19b", c19b())
            print("c19", c19b(C19_BEFORE_PLAN_TN))
        if "--incidence" in sys.argv:
            print("incidence", json.dumps(incidence(), default=str))
