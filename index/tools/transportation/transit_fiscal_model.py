#!/usr/bin/env python3
"""
American Transit Renewal Act of 2031 (division C of the Moving America Act of 2031, FY2032-36) -- fiscal model
CORRECTED 2026-10-12 (fiscal-year window): the 2031 reauthorization authorizes FY2032-36, not FY2031-35.
BUILD America 250 / 250-Plus covers FY2027-31, with FY2031 as its FINAL year.  Periods are FY2027-28,
FY2029-31, FY2032-36, FY2037-41, FY2042-46.  Authorization levels are unchanged in nominal terms and read
as FY2032 dollars; they were not re-indexed.  BILL_START sets the window; calendar(2031) reproduces the
superseded FY2031-35 framing for ARCA's retired validation rows.  This file merges the ATRA chat's
parameterized re-key with the ARCA chat's inputs (FY2031 rail $13.3B; EV stock path).
====================================================
The transit side of the rail + transit parity envelope, built to sit beside the
ARCA (American Rail Competitiveness Act) fiscal envelope.

Run:  python3 transit_fiscal_model.py            -> prints every table
      python3 transit_fiscal_model.py --json     -> writes transit_model_output.json

All dollars are billions, nominal, by federal fiscal year unless a label says otherwise.

SOURCED INPUTS (S)   -- taken from a primary document
ARCA INPUTS   (R)    -- taken from the ARCA bill architecture doc, not re-derived
ASSUMPTIONS   (A)    -- mine; each is listed in ASSUMPTIONS at the bottom and printed
"""
import json, sys

# ----------------------------------------------------------------------------
# 1. Macro
# ----------------------------------------------------------------------------
INFL = 0.025                      # (R) ARCA's inflation assumption
GDP_FY2026 = 60.4 / 0.00192       # (R) backed out of ARCA: $60.4B = 0.192% of GDP -> $31,458B
GDP_GROWTH = 0.041                # (A) nominal; reproduces ARCA's %-of-GDP rows to +/-0.003 pt
CAP_ARCA_METHOD = 0.00192         # (R) Division J advance approps $36.8B + HTF transfer $23.6B
# NOTE: neither cap is a CBO or statutory limit. 0.192% is ARCA's own discipline rule (the FY2026
#     general-fund draw on surface programs, IIJA-era peak); 0.206% is this project's restatement of it.
#     It is a design benchmark written into Division A sec. 108 as a trigger, measured on transfers.
# (A) like-for-like cap when annual general-fund appropriations are counted too:
#     FY2026 annual GF: rail $2.629B (R) + transit CIG $1.7B (R) = $4.3B on top of $60.4B
CAP_ALL_IN = (60.4 + 2.629 + 1.7) / GDP_FY2026

# (A) rev. 2026-10-12: the 2031 bill (the Moving America Act of 2031) covers FY2032-36.  BUILD America
#     250-Plus runs through FY2031; the 2029-30 reconciliation money and 250-Plus carry FY2029-31.
#     calendar(2031) reproduces the earlier FY2031-35 framing (used for the ARCA validation sections).
BILL_START = 2032
def make_periods(b):
    p = {"FY2027-28": (2027, 2028), f"FY2029-{str(b - 1)[2:]}": (2029, b - 1)}
    for k in range(3):
        a = b + 5 * k; p[f"FY{a}-{str(a + 4)[2:]}"] = (a, a + 4)
    return p
PERIODS = make_periods(BILL_START)
YEARS = list(range(2027, BILL_START + 15))
def bill_period(): return list(PERIODS)[2]          # e.g. "FY2032-36"

def gdp(t):   return GDP_FY2026 * (1 + GDP_GROWTH) ** (t - 2026)
def infl(t, base=2026): return (1 + INFL) ** (t - base)

# ----------------------------------------------------------------------------
# 2. Highways and the parity envelope (R)
# ----------------------------------------------------------------------------
FHWA_FY2026 = 62.657              # (R) FY2026 obligation limitation
HR8870_HWY = {2027: 72.909, 2028: 73.684, 2029: 75.021, 2030: 76.296, 2031: 77.635}   # (S) sec. 1102 limitation + $0.639B exempt
def highway_program(t, basis="hr8870"):
    if basis == "arca":           # ARCA: flat real from FY2026
        return FHWA_FY2026 * infl(t)
    # (S) H.R. 8870 as introduced: sec. 1102 obligation limitation $372.35B + $3.2B exempt = ~$375.5B, FHWA total
    if t in HR8870_HWY: return HR8870_HWY[t]
    if t < 2027: return FHWA_FY2026 * infl(t)
    return HR8870_HWY[2031] * infl(t, 2031)

# (S) CBO Sept 30 2026, Table 5: obligation limitations for surface programs (FHWA + FTA + NHTSA + FMCSA), $B.
CBO_OL = {2027: 91.183, 2028: 92.346, 2029: 94.053, 2030: 95.683, 2031: 97.393}
HR8870_EXEMPT = 0.639
def safety_program(t):
    """NHTSA + FMCSA from the Highway Account: CBO limitation less FHWA limitation less FTA. ~$2.0-2.2B/yr.
    Paid from the Highway Account; folded into the highway account's need in allocate() when INCLUDE_SAFETY."""
    if t in CBO_OL: return CBO_OL[t] - (HR8870_HWY[t] - HR8870_EXEMPT) - HR8870_CA_EXACT[t]
    return safety_program(2031) * infl(t, 2031) if t > 2031 else 0.0
INCLUDE_SAFETY = True            # (A) rev. 2026-10-12: NHTSA + FMCSA counted in the Highway Account's program
def highway_need(t, basis="hr8870"):
    return highway_program(t, basis) + (safety_program(t) if INCLUDE_SAFETY else 0.0)
HR8870_CA_EXACT = {2027: 16.868, 2028: 17.205, 2029: 17.527, 2030: 17.835, 2031: 18.157}   # (S) sec. 3023

def parity_share(t):              # (R) rail + transit as a share of highways
    b = BILL_START
    return 0.45 if t < b else 0.75 if t < b + 5 else 0.90 if t < b + 10 else 1.00

# ----------------------------------------------------------------------------
# 3. Trust fund revenue
# ----------------------------------------------------------------------------
# (S) CBO, Highway Trust Fund Accounts, June 2026 baseline: receipts, $ millions
CBO_HWY = {2026: 41560, 2027: 42269, 2028: 42826, 2029: 43297, 2030: 43738, 2031: 44174,
           2032: 44623, 2033: 45091, 2034: 45576, 2035: 46083, 2036: 46607}
CBO_TRA = {2026: 5662, 2027: 5731, 2028: 5770, 2029: 5795, 2030: 5814, 2031: 5831,
           2032: 5847, 2033: 5864, 2034: 5881, 2035: 5901, 2036: 5921}
CBO_HWY_OUT = {2027: 64649, 2028: 66593, 2029: 66952, 2030: 67196, 2031: 67557}
CBO_TRA_OUT = {2027: 18092, 2028: 17959, 2029: 17445, 2030: 17383, 2031: 17490}
# (S) CBO June 2026: annual shortfall, both accounts = change in cumulative end-of-year balances, $B
CBO_SHORTFALL = {2029: 35.3, 2030: 35.0, 2031: 35.0, 2032: 35.4, 2033: 36.4, 2034: 37.1, 2035: 38.3, 2036: 39.5,
                 2037: 40.0, 2038: 40.5, 2039: 41.0, 2040: 41.5}   # (A) FY2037-40 extended at +0.5 a year
FLEX = 1.2                        # (S) CBO: highway account -> transit account each year

def legacy(t, acct="both"):
    """Current-law receipts, unindexed. After FY2036 grown 1%/yr (A)."""
    def one(d):
        return (d[t] if t in d else d[2036] * 1.01 ** (t - 2036)) / 1000.0
    h, tr = one(CBO_HWY), one(CBO_TRA)
    return {"hwy": h, "tra": tr, "both": h + tr}[acct]

# Per-mile yield basis.  "arca" reproduces ARCA's rows but rests on "2.4 cents replaces ~$44B".
# That anchor is wrong on the physical base: FHWA counts 3,323.8B vehicle-miles in 2025, so
# 2.4 cents grosses ~$80B, which is what Eno (Mar 2026) reports: 2.4 cents ~ $78B = full annual
# highway and transit OUTLAYS, not receipts.  "vmt" is the physical base, all vehicles.
PER_MILE_BASIS = "vmt"            # base case from 2026-10-12; "arca" reproduces ARCA's own rows
VMT_2025 = 3.3238                 # (S) trillion vehicle-miles, FHWA Traffic Volume Trends Dec 2025
EXCISE_OFFSET = 0.25            # (R) CBO/JCT standard income-and-payroll offset on new excise; H.R. 8870 EV fee 12.4/16.8 = 0.74
PER_MILE_ADMIN = 0.10             # (A) collection cost and leakage; ARCA cites 5-13% of collections
PER_MILE_START = 1.0              # base case; ARCA drafted 0.6 cents in FY2029, +0.2 a year, 3.6 cents by FY2044
def per_mile_rate(t):             # set PER_MILE_START = 0.8 for the "closing package" sensitivity
    return 0.0 if t < 2029 else min(PER_MILE_START + 0.2 * (t - 2029), 3.6)

def fund_revenue(t):
    """Reformed surface fund receipts.
    (R) fuel taxes retained and indexed from FY2029; per-mile fee phased 0.6 -> 3.6 cents;
        ARCA's anchor: 2.4 cents/mile replaces all current HTF revenue (~$44B).
    (A) fuel taxes are displaced linearly FY2029-FY2044 as the per-mile fee matures, which is
        what "displacing fuel taxes as the base erodes" and "3.6 cents is a 50 percent real
        expansion of the base" jointly require.  Validated against ARCA's dedicated-revenue rows.
    """
    if t < 2029:
        return legacy(t)
    leg = legacy(t) * infl(t, 2028)
    span = (3.6 - PER_MILE_START) / 0.2 + 1          # displacement completes the year the fee reaches 3.6 cents (16 years at ARCA's 0.6)
    displaced = min((t - 2028) / span, 1.0)
    if PER_MILE_BASIS == "arca":   # (R) ARCA's anchor; validated against ARCA's revenue rows
        pm = per_mile_rate(t) / 2.4 * 44.0 * infl(t) * 1.005 ** (t - 2026)
    else:                          # "vmt": rate x vehicle-miles, nominal cents, net of collection cost
        pm = per_mile_rate(t) * VMT_2025 * 10.0 * 1.005 ** (t - 2025) * (1 - PER_MILE_ADMIN)
    return leg * (1 - displaced) + pm + ev_fee(t)

# (S) CBO cost estimate of H.R. 8870, Sept 30 2026, Table 4 memorandum: gross registration-fee collections
#     remitted by states, $B (sec. 1129 runs through Sept 30 2036; the bill itself sends the money to the general
#     fund -- Division A sec. 103 redirects it to the trust fund).  Beyond FY2036 the stock-path model below.
EV_CBO = {2028: 0.207, 2029: 0.726, 2030: 1.177, 2031: 1.655, 2032: 1.951, 2033: 2.287, 2034: 2.554,
          2035: 2.942, 2036: 3.276}
def ev_fee(t):
    """FY2029-36: CBO's gross estimate.  After FY2036: (R) fee rising $5 a year to $200 on (A) a plug-in stock
    of 45M in 2040 and 70M in 2045, scaled to meet CBO's FY2036 figure."""
    if t < 2029: return 0.0
    if t in EV_CBO: return EV_CBO[t]
    return _ev_stock_model(t) * EV_CBO[2036] / _ev_stock_model(2036)

def _ev_stock_model(t):
    pts = [(2029, 9), (2035, 25), (2040, 45), (2045, 70), (2052, 90)]   # (A) as set by the ARCA chat's re-key, Oct 12
    for (a, va), (b, vb) in zip(pts, pts[1:]):
        if a <= t <= b:
            stock = va + (vb - va) * (t - a) / (b - a); break
    fee = min(130 + 5 * (t - 2027), 200) * 0.85      # 0.85 = BEV/PHEV blend
    return stock * fee / 1000.0

def aviation(t):                  # (R) $4 in the bill's first year -> $12 in its fifth -> cap $16; $1 = $0.70B on 2026 base
    b = BILL_START
    if t < b: return 0.0
    rate = 4 + 2 * (t - b) if t <= b + 4 else min(12 + 0.4 * (t - b - 4), 16)
    return rate * 0.70 * 1.0215 ** (t - 2026)

def rail_diesel(t):               # (R) 10/5 cents from the 2030 reconciliation, 15/7.5 cents from the bill's first year
    return 0.0 if t < 2030 else 0.36 if t < BILL_START else 0.53 * 1.004 ** (t - BILL_START)

# ----------------------------------------------------------------------------
# 4. Rail program (R) -- ARCA canonical table and fiscal-envelope rows
# ----------------------------------------------------------------------------
RAIL_250PLUS = {2027: 10.5, 2028: 11.0, 2029: 11.9, 2030: 12.9, 2031: 13.3}   # delivered; FY2031 = ARCA's 250-Plus delivered total $59.6B less FY2027-30 (ARCA chat, Oct 12)
RAIL_RECON = {2029: 24.25, 2030: 24.25}                              # $48.5B
RAIL_ARCA_VALS = [39.95, 47.29, 52.07, 56.13, 58.59]   # $254.03B, years 1-5 of the bill (FY2032-36)
RAIL_EXPANSION_SHARE = (55.00 + 20.20 + 6.00 + 12.00) / 254.03       # secs 303, 310, 311, 312
def ARCA_RAIL_SHARE(t):           # (R) ARCA's original schedule, shifted with the bill's calendar
    u = t - (BILL_START - 2031)
    return 0.0 if t < 2029 else 0.08 if u <= 2031 else 0.15 if u <= 2035 else 0.22 if u <= 2040 else 0.28
def rail_program(t, include_baseline=True):
    b = BILL_START
    if b <= t < b + 5: return RAIL_ARCA_VALS[t - b]
    if b + 5 <= t < b + 10: return 214.3 / 5
    if b + 10 <= t < b + 15: return 242.4 / 5
    return RAIL_RECON.get(t, 0.0) + (RAIL_250PLUS.get(t, 0.0) if include_baseline else 0.0)

# ----------------------------------------------------------------------------
# 5. Transit program
# ----------------------------------------------------------------------------
# (S) H.R. 8870 sec. 3023, Mass Transit Account contract authority, FY2027-31
HR8870_CA = {2027: 16.87, 2028: 17.21, 2029: 17.53, 2030: 17.84, 2031: 18.16}   # $87.61B; two-decimal values from a secondary tracker
# (A) BUILD America 250-Plus, transit: contract authority as reported; CIG $15B authorized of
#     which $5B guaranteed and the other $10B delivered at 70% (ARCA's competitive-program rate);
#     WMATA $0.15B in FY2031 only, per CBO's Sept 30 2026 estimate.
CIG_250PLUS_DELIVERED = (5.0 + 10.0 * 0.70) / 5
def transit_250plus(t): return HR8870_CA[t] + CIG_250PLUS_DELIVERED + (0.15 if t == 2031 else 0.0)   # (S) CBO: WMATA $150M in FY2031 only (sec. 3109)

# The canonical authorization table, FY2032-36 (years 1-5 of the bill; nominal amounts as drafted for
# FY2031-35, carried forward one year unchanged -- (A) a ~2.5% real reduction, flagged).  Every figure in the doc is read from here.
#   kind: R = renewal (first call on dedicated revenue), X = expansion (bears forecast risk)
#   src : TF = contract authority from the Mass Transit Account
#         GF = mandatory general-fund appropriation
AUTH = [
 # sec,  program,                                              kind src   FY31   FY32   FY33   FY34   FY35
 ("201", "Service operating assistance (new 5307(i))",          "R","TF", [6.00, 6.50, 7.00, 7.50, 8.00]),
 ("301", "State of good repair formula (5337)",                 "R","TF", [5.20, 5.40, 5.60, 5.80, 6.00]),
 ("302", "Backlog retirement schedule (new 5337(g))",           "R","TF", [6.00, 6.15, 6.30, 6.46, 6.62]),
 ("303", "Asset management enforcement and capacity (5326)",    "R","TF", [0.10, 0.10, 0.10, 0.10, 0.10]),
 ("304", "Transit resilience",                                  "R","TF", [0.60, 0.60, 0.60, 0.60, 0.60]),
 ("401", "Capital Investment Grants (5309)",                    "X","GF", [4.50, 5.00, 5.50, 6.00, 6.50]),
 ("501", "Workforce: apprenticeship, training, operator safety","R","TF", [0.50, 0.55, 0.60, 0.60, 0.60]),
 ("601", "Urbanized area formula, capital (5307, 5340)",        "R","TF", [10.00,10.40,10.80,11.20,11.70]),
 ("602", "Buses and bus facilities (5339)",                     "R","TF", [2.60, 2.70, 2.80, 2.90, 3.00]),
 ("603", "Rural, tribal and intercity bus (5311)",              "R","TF", [1.40, 1.45, 1.50, 1.55, 1.60]),
 ("604", "Seniors and people with disabilities (5310)",         "R","TF", [0.60, 0.62, 0.64, 0.66, 0.68]),
 ("605", "All Stations Accessibility",                          "R","TF", [1.00, 1.00, 1.00, 1.00, 1.00]),
 ("606", "Joint transit-rail facilities and station access",    "X","GF", [1.00, 1.20, 1.40, 1.40, 1.00]),
 ("607", "Ferries",                                             "R","TF", [0.20, 0.20, 0.20, 0.20, 0.20]),
 ("608", "Emergency relief, quick release (5324)",              "R","TF", [0.10, 0.10, 0.10, 0.10, 0.10]),
 ("701", "Planning, research, safety, FTA capacity, delivery",  "R","TF", [0.90, 0.92, 0.95, 0.97, 1.00]),
]
OPERATING_SCENARIOS = {            # multiplier on sec. 201
    "A: bar kept":          0.0,   # no new operating tier
    "B: conditional tier":  1.0,   # the drafted bill
    "C: broad eligibility": 2.0,   # $12B rising to $16B
}
# (A) 2029-30 reconciliation, transit.  Sized to the spend-out test; see section 5 of the doc.
TRANSIT_RECON = [
 ("Operating transition grants",                     "R", 2029,  4.00),
 ("Operating transition grants",                     "R", 2030,  5.00),
 ("State of good repair, shovel-ready backlog",      "R", 2029,  4.00),
 ("State of good repair, shovel-ready backlog",      "R", 2030,  6.00),
 ("Bus and railcar replacement orders",              "R", 2029,  3.00),
 ("Bus and railcar replacement orders",              "R", 2030,  1.00),
 ("Station accessibility",                           "R", 2030,  3.00),
 ("Capital Investment Grants, executed agreements",  "X", 2030,  3.00),
 ("Credit subsidy: transit and joint development",   "X", 2029,  1.00),
 ("Credit subsidy: transit and joint development",   "X", 2030,  1.00),
 ("Workforce and FTA capacity",                      "R", 2030,  1.00),
]

def auth_total(year, scenario="B: conditional tier", kind=None, src=None):
    i = year - BILL_START; m = OPERATING_SCENARIOS[scenario]; s = 0.0
    for sec, name, k, sr, vals in AUTH:
        v = vals[i] * (m if sec == "201" else 1.0)
        if (kind is None or k == kind) and (src is None or sr == src): s += v
    return s

def transit_program(t, scenario="B: conditional tier", kind=None, src=None):
    """Federal transit program by year.  After the bill's fifth year, extends its fifth-year lines (A):
    renewal lines +3.5%/yr; operating tier +4%/yr; backlog retirement indexed 2.5%;
    CIG +5%/yr to FY2040 then flat real; joint facilities flat real."""
    if t < BILL_START:
        base = transit_250plus(t)
        rec = sum(v for n, k, y, v in TRANSIT_RECON if y == t and (kind is None or k == kind))
        if kind == "X": return CIG_250PLUS_DELIVERED + rec if src in (None, "GF") else 0.0
        if kind == "R": return (base - CIG_250PLUS_DELIVERED) * (0 if src == "GF" else 1) + (rec if src in (None, "GF") else 0)
        if src == "GF": return CIG_250PLUS_DELIVERED + (0.15 if t == 2031 else 0.0) + sum(v for n, k, y, v in TRANSIT_RECON if y == t)
        if src == "TF": return HR8870_CA[t]
        return base + sum(v for n, k, y, v in TRANSIT_RECON if y == t)
    if t < BILL_START + 5:
        return auth_total(t, scenario, kind, src)
    n = t - (BILL_START + 4); m = OPERATING_SCENARIOS[scenario]; s = 0.0
    for sec, name, k, sr, vals in AUTH:
        v = vals[4]
        if sec == "201":   v = v * m * 1.04 ** n
        elif sec == "302": v = v * 1.025 ** n
        elif sec == "401": v = v * (1.05 ** min(n, 5)) * (1.025 ** max(n - 5, 0))
        elif sec == "606": v = v * 1.025 ** n
        else:              v = v * 1.035 ** n
        if (kind is None or k == kind) and (src is None or sr == src): s += v
    return s

# ----------------------------------------------------------------------------
# 6. Backlog amortization (sec. 302)
# ----------------------------------------------------------------------------
BACKLOG_2025USD = 127.8            # (S) DOT C&P 25th ed.: 2018 backlog, in 2025 dollars (CRS R48644)
AMORT_YEARS = 20                   # (A) FY2032-51, the horizon DOT's own scenarios use
FED_SHARE_RETIRE = 0.80            # (A) the capital share already in 5337(e)
def amortization():
    rows = []; real_pay = BACKLOG_2025USD / AMORT_YEARS
    for i, t in enumerate(range(BILL_START, BILL_START + AMORT_YEARS)):
        f = infl(t, 2025)
        rows.append({"fy": t, "total_nominal": real_pay * f, "federal_nominal": real_pay * f * FED_SHARE_RETIRE,
                     "backlog_end_2025usd": BACKLOG_2025USD - real_pay * (i + 1),
                     "backlog_end_nominal": (BACKLOG_2025USD - real_pay * (i + 1)) * f})
    return rows

# ----------------------------------------------------------------------------
# 7. Three trust-fund architectures
# ----------------------------------------------------------------------------
def floors(t):
    """SEC. 101(d): highway and transit accounts not less than FY2028 credited amounts, indexed."""
    h = (legacy(2028, "hwy") - FLEX) * infl(t, 2028)
    tr = (legacy(2028, "tra") + FLEX) * infl(t, 2028)
    return h, tr

# (A) Architecture C's statutory split of *incremental* revenue (fund receipts above the two floors).
#     Solved by solve_incremental_shares() so that the three modes' renewal programs reach the same
#     dedicated-coverage ratio in FY2041-45, then rounded to whole percents for the bill text.
INCR_SHARES = {"hwy": 0.35, "tra": 0.50, "rail": 0.15}   # rev. 2026-10-12: near-equal renewal coverage on the physical base

def allocate(t, arch, scenario, hwy_basis="hr8870"):
    F = fund_revenue(t); av, dz = aviation(t), rail_diesel(t)
    H = highway_need(t, hwy_basis); T = transit_program(t, scenario); R = rail_program(t)
    fh, ft = floors(t)
    if t < 2029:                                  # current law: two accounts, legacy split
        ded = {"hwy": legacy(t, "hwy") - FLEX, "tra": legacy(t, "tra") + FLEX, "rail": 0.0}
    elif arch == "A":                             # standalone rail fund; surface fund split 88/12
        s = (legacy(2028, "tra") + FLEX) / legacy(2028)
        ded = {"hwy": F * (1 - s), "tra": F * s, "rail": av + dz}
    elif arch == "B":                             # SEC. 101 as drafted in ARCA
        r = ARCA_RAIL_SHARE(t) * F
        rest = F - r
        h = min(max(fh, rest - ft), max(H, fh)) if rest >= fh + ft else rest * fh / (fh + ft)
        tr = rest - h
        ded = {"hwy": h, "tra": tr, "rail": r + av + dz}
    else:                                         # C: floors, then incremental shares
        inc = max(F - fh - ft, 0.0)
        scale = min(F / (fh + ft), 1.0)
        ded = {"hwy": fh * scale + inc * INCR_SHARES["hwy"],
               "tra": ft * scale + inc * INCR_SHARES["tra"],
               "rail": inc * INCR_SHARES["rail"] + av + dz}
    prog = {"hwy": H, "tra": T, "rail": R}
    gf = {m: max(prog[m] - ded[m], 0.0) for m in prog}
    trapped = {m: max(ded[m] - prog[m], 0.0) for m in prog}
    return {"fy": t, "fund": F, "aviation": av, "diesel": dz, "prog": prog, "ded": ded, "gf": gf,
            "trapped": trapped, "gf_total": sum(gf.values()), "gdp": gdp(t),
            "gf_pct": sum(gf.values()) / gdp(t)}

def solve_incremental_shares(scenario="B: conditional tier"):
    """Equal dedicated coverage of each mode's RENEWAL program in FY2041-45."""
    yrs = range(BILL_START + 10, BILL_START + 15)
    F = sum(fund_revenue(t) for t in yrs); fh = sum(floors(t)[0] for t in yrs); ft = sum(floors(t)[1] for t in yrs)
    inc = F - fh - ft
    ren = {"hwy": sum(highway_need(t) for t in yrs),
           "tra": sum(transit_program(t, scenario, kind="R") for t in yrs),
           "rail": sum(rail_program(t) * (1 - RAIL_EXPANSION_SHARE) for t in yrs)}
    other = {"hwy": fh, "tra": ft, "rail": sum(aviation(t) + rail_diesel(t) for t in yrs)}
    c = (inc + sum(other.values())) / sum(ren.values())          # common coverage ratio
    raw = {m: max(c * ren[m] - other[m], 0.0) / inc for m in ren}
    tot = sum(raw.values())
    return {m: raw[m] / tot for m in raw}, c

# ----------------------------------------------------------------------------
# 8. Reporting helpers
# ----------------------------------------------------------------------------
def period_rows(arch, scenario, hwy_basis="hr8870"):
    out = []
    for name, (a, b) in PERIODS.items():
        ys = [allocate(t, arch, scenario, hwy_basis) for t in range(a, b + 1)]
        n = len(ys); agg = lambda f: sum(f(y) for y in ys)
        row = {"period": name, "years": n,
               "fund": agg(lambda y: y["fund"]),
               "prog": {m: agg(lambda y: y["prog"][m]) for m in ("hwy", "tra", "rail")},
               "ded":  {m: agg(lambda y: y["ded"][m]) for m in ("hwy", "tra", "rail")},
               "gf":   {m: agg(lambda y: y["gf"][m]) for m in ("hwy", "tra", "rail")},
               "trapped": agg(lambda y: sum(y["trapped"].values())),
               "gf_per_year": agg(lambda y: y["gf_total"]) / n,
               "gf_pct_avg": agg(lambda y: y["gf_total"]) / agg(lambda y: y["gdp"]),
               "gf_pct_peak": max(y["gf_pct"] for y in ys),
               "peak_year": max(ys, key=lambda y: y["gf_pct"])["fy"]}
        out.append(row)
    return out

def envelope():
    rows = []
    for name, (a, b) in list(PERIODS.items())[1:]:
        yrs = range(a, b + 1); n = len(yrs)
        hw = sum(highway_program(t) for t in yrs)
        comb = sum(highway_program(t) * parity_share(t) for t in yrs)
        rows.append({"period": name, "highways": hw, "combined_envelope": comb, "years": n})
    return rows

def validate_against_arca():
    """ARCA's own rows: rail dedicated revenue $9.4B / $83.7B / $165.9B / $244.5B."""
    target = {"FY2029-30": 9.4, "FY2031-35": 83.7, "FY2036-40": 165.9, "FY2041-45": 244.5}
    out = {}
    for name, (a, b) in list(PERIODS.items())[1:]:
        mine = sum(ARCA_RAIL_SHARE(t) * fund_revenue(t) + aviation(t) + rail_diesel(t) for t in range(a, b + 1))
        out[name] = (mine, target[name], mine / target[name] - 1)
    return out

ASSUMPTIONS = [
 ("GDP path", "FY2026 GDP $31.46T backed out of ARCA's 0.192% rule; 4.1% nominal growth", "low"),
 ("Fuel-tax displacement", "fuel taxes displaced linearly FY2029-44 as the per-mile fee reaches 3.6 cents", "HIGH"),
 ("Per-mile yield", "physical base: rate x FHWA vehicle-miles (3.32T in 2025, +0.5%/yr), all vehicles, nominal cents, 10% collection cost and leakage. ARCA's anchor (2.4 cents = ~$44B) understates the yield by ~40% and is kept only to reproduce ARCA's rows", "HIGH"),
 ("Per-mile start", "1.0 cent in FY2029, +0.2 a year, 3.6 cents in FY2042. On H.R. 8870 highway levels 0.6 and 0.8 cents both breach the benchmark (0.8 cents by $2.7B over FY2029-30, NHTSA/FMCSA included)", "HIGH"),
 ("250-Plus transit", "H.R. 8870 contract authority as reported; CIG $5B guaranteed + 70% of $10B", "medium"),
 ("Backlog", "$127.8B (2018 data, 2025 dollars) held flat in real terms to FY2032", "medium"),
 ("Federal share of backlog retirement", "80%", "medium"),
 ("Bill calendar", "2031 bill covers FY2032-36; nominal program tables drafted for FY2031-35 carried forward a year unchanged; 250-Plus covers FY2031 (rail FY2031 delivered $13.7B assumed)", "medium"),
 ("Operating tier size", "$6B in FY2032 = holding the federal share of operating cost at its 2024 level (17%)", "HIGH"),
 ("Plug-in vehicle stock", "9M (2029) -> 70M (2045)", "low"),
 ("Out-year transit growth", "renewal lines +3.5%/yr, CIG +5%/yr to FY2040", "medium"),
 ("Highway denominator", "H.R. 8870 as introduced: sec. 1102 limitation + exempt, $72.9B FY2027 to $77.6B FY2031, then +2.5%/yr; ARCA's flat-real $62.657B run as a sensitivity", "medium"),
]

# ----------------------------------------------------------------------------
# 9. Main
# ----------------------------------------------------------------------------
BASE_START = PER_MILE_START
from contextlib import contextmanager
@contextmanager
def settings(basis, start):
    """Temporarily switch the per-mile yield basis and starting rate."""
    global PER_MILE_BASIS, PER_MILE_START
    old = (PER_MILE_BASIS, PER_MILE_START)
    PER_MILE_BASIS, PER_MILE_START = basis, start
    try: yield
    finally: PER_MILE_BASIS, PER_MILE_START = old

@contextmanager
def calendar(b):
    """Temporarily move the bill's first year (2031 reproduces ARCA's original FY2031-35 framing)."""
    global BILL_START, PERIODS, YEARS
    old = (BILL_START, PERIODS, YEARS)
    BILL_START, PERIODS, YEARS = b, make_periods(b), list(range(2027, b + 15))
    try: yield
    finally: BILL_START, PERIODS, YEARS = old

def fmt(x, d=1): return f"{x:,.{d}f}"

def main():
    P = print
    P("=" * 96); P("TRANSIT FISCAL MODEL"); P("=" * 96)
    P(f"GDP FY2026 ${GDP_FY2026/1000:,.2f}T | cap, ARCA method {CAP_ARCA_METHOD:.3%} | cap, all-in {CAP_ALL_IN:.3%}")

    P("\n-- 1. Validation: can this revenue model reproduce ARCA's dedicated-revenue rows? (ARCA's anchor, 0.6c) --")
    with settings("arca", 0.6), calendar(2031):
        for k, (mine, tgt, d) in validate_against_arca().items():
            P(f"  {k}: model {fmt(mine)}  ARCA {fmt(tgt)}  diff {d:+.1%}")

    P("\n-- 2. Fund revenue by year --")
    for t in YEARS:
        P(f"  FY{t}: fund {fmt(fund_revenue(t))}  per-mile rate {per_mile_rate(t):.1f}c  EV {fmt(ev_fee(t))}  aviation {fmt(aviation(t))}  floors hwy/transit {fmt(floors(t)[0])}/{fmt(floors(t)[1])}")

    P("\n-- 3. BUILD America 250-Plus, transit, FY2027-31 --")
    asrep = sum(HR8870_CA.values()); P(f"  contract authority as reported: {fmt(asrep)} ({fmt(asrep/5)}/yr)")
    P(f"  CIG authorized 15.0, delivered {fmt(CIG_250PLUS_DELIVERED*5)}; WMATA 0.15 (FY2031 only)")
    deliv = sum(transit_250plus(t) for t in HR8870_CA); P(f"  delivered total {fmt(deliv)} ({fmt(deliv/5)}/yr) vs IIJA 21.6/yr -> {deliv/5/21.6-1:+.1%} nominal, {deliv/5/(21.6*infl(2029,2024))-1:+.1%} real (FY2024->FY2029 dollars)")

    B5 = range(BILL_START, BILL_START + 5)
    P(f"\n-- 4. Canonical authorization table, {bill_period()} (scenario B) --")
    tot = [0] * 5
    for sec, name, k, sr, vals in AUTH:
        P(f"  {sec:>4} {name:<58} {k} {sr} " + " ".join(f"{v:6.2f}" for v in vals) + f"  {sum(vals):7.2f}")
        tot = [a + b for a, b in zip(tot, vals)]
    P(f"  {'':>4} {'TOTAL':<58}     " + " ".join(f"{v:6.2f}" for v in tot) + f"  {sum(tot):7.2f}")
    for sc in OPERATING_SCENARIOS:
        s5 = sum(auth_total(y, sc) for y in B5)
        P(f"  scenario {sc:<22}: {fmt(s5,2)} over five years, {fmt(s5/5,2)}/yr; renewal {fmt(sum(auth_total(y,sc,kind='R') for y in B5),2)}, expansion {fmt(sum(auth_total(y,sc,kind='X') for y in B5),2)}")
    P("  reconciliation, transit: " + fmt(sum(v for *_, v in TRANSIT_RECON), 2))

    P("\n-- 5. The parity envelope and the split --")
    for e in envelope():
        P(f"  {e['period']}: highways {fmt(e['highways'])}  combined rail+transit envelope {fmt(e['combined_envelope'])}")
    env = {e["period"]: e for e in envelope()}[bill_period()]["combined_envelope"]
    rail5 = sum(RAIL_ARCA_VALS)
    for sc in OPERATING_SCENARIOS:
        t5 = sum(auth_total(y, sc) for y in B5)
        P(f"  {sc:<22}: transit {fmt(t5)}  rail {fmt(rail5)}  combined {fmt(t5+rail5)} = {(t5+rail5)/env:.2f}x envelope; "
          f"split {t5/(t5+rail5):.0%}/{rail5/(t5+rail5):.0%}; transit as share of envelope {t5/env:.0%}; rail residual inside envelope {fmt(env-t5)} -> ARCA = {rail5/(env-t5):.2f}x")
    P(f"  handoff: 60% of envelope = {fmt(0.6*env)} ; ARCA = {rail5/(0.4*env):.2f}x its 40%")

    P("\n-- 6. Backlog amortization schedule (sec. 302) --")
    for r in amortization():
        if r["fy"] in tuple(range(BILL_START, BILL_START + 5)) + (BILL_START + 9, BILL_START + 14, BILL_START + 19):
            P(f"  FY{r['fy']}: total {fmt(r['total_nominal'],2)}  federal {fmt(r['federal_nominal'],2)}  backlog left {fmt(r['backlog_end_2025usd'])} (2025$)")

    P(f"\n-- 7. Incremental shares that equalize renewal coverage in {list(PERIODS)[-1]} --")
    for sc in OPERATING_SCENARIOS:
        sh, c = solve_incremental_shares(sc)
        P(f"  {sc:<22}: hwy {sh['hwy']:.1%} transit {sh['tra']:.1%} rail {sh['rail']:.1%}  (common coverage {c:.0%})")
    P(f"  drafted in bill text: {INCR_SHARES}")

    P("\n-- 8. Architectures x operating scenarios: general-fund draw --")
    for arch, label in (("A", "A standalone rail fund"), ("B", "B SEC.101 as drafted"), ("C", "C floors + incremental shares")):
        for sc in OPERATING_SCENARIOS:
            P(f"\n  [{label}] [{sc}]")
            P("   period     fund   prog h/t/r             dedicated h/t/r        GF h/t/r             trapped  GF/yr  %GDP avg  peak(yr)   vs caps")
            for r in period_rows(arch, sc):
                ok1 = "ok" if r["gf_pct_peak"] <= CAP_ARCA_METHOD else "OVER"
                ok2 = "ok" if r["gf_pct_peak"] <= CAP_ALL_IN else "OVER"
                P(f"   {r['period']} {r['fund']:7.1f}  {r['prog']['hwy']:6.1f}/{r['prog']['tra']:6.1f}/{r['prog']['rail']:6.1f}  "
                  f"{r['ded']['hwy']:6.1f}/{r['ded']['tra']:6.1f}/{r['ded']['rail']:6.1f}  "
                  f"{r['gf']['hwy']:6.1f}/{r['gf']['tra']:6.1f}/{r['gf']['rail']:6.1f}  {r['trapped']:6.1f}  {r['gf_per_year']:6.1f}  "
                  f"{r['gf_pct_avg']:.3%}  {r['gf_pct_peak']:.3%} ({r['peak_year']})  {ok1}/{ok2}")

    P("\n-- 9. Base-case choices, side by side (arch C, scenario B): average / peak year, % of GDP --")
    P(f"   cap, all-in {CAP_ALL_IN:.3%}.  Base case: physical per-mile base, H.R. 8870 highway levels, {BASE_START:.1f}-cent start.")
    for basis in ("vmt", "arca"):
        for hb in ("hr8870", "arca"):
            for start in (0.6, 0.8, 1.0):
                with settings(basis, start):
                    rr = period_rows("C", "B: conditional tier", hb)
                    flag = "ok" if max(r["gf_pct_peak"] for r in rr[1:3]) <= CAP_ALL_IN else "OVER"
                    P(f"   yield {basis:<4} highways {hb:<6} start {start:.1f}c  " + "  ".join(f"{r['period'][2:]}: {r['gf_pct_avg']:.3%}/{r['gf_pct_peak']:.3%}" for r in rr[1:]) + f"  {flag}")

    P("\n-- 9b. ARCA alone, all-in accounting (transit held at its 250-Plus baseline, flat real), base case --")
    for name, (a, b) in PERIODS.items():
        g = G = 0.0
        for t in range(a, b + 1):
            Tb = transit_250plus(min(t, 2031)) * infl(max(t, 2031), 2031)
            g += highway_need(t) + rail_program(t) + Tb - fund_revenue(t) - aviation(t) - rail_diesel(t); G += gdp(t)
        P(f"   {name}  GF/yr {g/(b-a+1):.1f}  {g/G:.3%}   (ARCA reports 0.105% for FY2029-30 and 0.099% for FY2031-35)")

    P("\n-- 9c. Operating tier size under the base case (arch C) --")
    for sc in OPERATING_SCENARIOS:
        rr = period_rows("C", sc)
        P(f"   {sc:<22} " + "  ".join(f"{r['period'][2:]}: {r['gf_pct_avg']:.3%}/{r['gf_pct_peak']:.3%}" for r in rr[1:]))
    P("   coverage of each program by dedicated revenue, scenario B:")
    for r in period_rows("C", "B: conditional tier"):
        P(f"     {r['period']}: fund {r['fund']:.0f}  highways {r['ded']['hwy']/r['prog']['hwy']:.0%}  transit {r['ded']['tra']/r['prog']['tra']:.0%}  rail {r['ded']['rail']/r['prog']['rail']:.0%}   GF/yr {r['gf_per_year']:.1f}")

    P("\n-- 9e. ARCA's dedicated-revenue rows restated on the physical base (ARCA's own shares, 0.6-cent schedule, original FY2031-35 calendar) --")
    target = {"FY2029-30": 9.4, "FY2031-35": 83.7, "FY2036-40": 165.9, "FY2041-45": 244.5}
    with settings("vmt", 0.6), calendar(2031):
        for name, (a, b) in list(PERIODS.items())[1:]:
            mine = sum(ARCA_RAIL_SHARE(t) * fund_revenue(t) + aviation(t) + rail_diesel(t) for t in range(a, b + 1))
            prog = sum(rail_program(t) for t in range(a, b + 1))
            P(f"   {name}: ARCA {target[name]:6.1f} -> restated {mine:6.1f} ({mine/target[name]-1:+.0%}); share of rail program {mine/prog:.0%}")

    P("\n-- 9f. ARCA's affordability rows, reproduced by ARCA's method (ARCA's yield anchor, 0.6-cent schedule, original calendar) --")
    P("   draw = rail general fund + (CBO baseline trust fund shortfall - (1 - rail share) x new per-mile and EV receipts)")
    P("   i.e. highways and transit frozen at CBO baseline outlays, no fuel-tax displacement, no continuing")
    P("   general-fund appropriations for highways or transit.  ARCA reports $38.1B / $41.3B / $9.7B / $0.3B a year.")
    with settings("arca", 0.6), calendar(2031):
        for name, (a, b) in list(PERIODS.items())[1:]:
            yrs = range(a, b + 1); n = len(yrs)
            rgf = sum(max(rail_program(t, False) - (ARCA_RAIL_SHARE(t) * fund_revenue(t) + aviation(t) + rail_diesel(t)), 0) for t in yrs) / n
            htf = sum(max(CBO_SHORTFALL.get(t, 0) - (1 - ARCA_RAIL_SHARE(t)) * (fund_revenue(t) - legacy(t) * infl(t, 2028) * (1 - min((t - 2028) / 16.0, 1.0))), 0) for t in yrs) / n if a <= 2036 else 0.0
            P(f"   {name}: rail {rgf:5.1f} + trust fund {htf:5.1f} = {rgf + htf:5.1f} a year = {(rgf + htf) * n / sum(gdp(t) for t in yrs):.3%} of GDP")

    P("\n-- 9g. Headroom under the cap, base case, scenario B: what else fits --")
    for name, (a, b) in list(PERIODS.items())[1:3]:
        room = [CAP_ALL_IN * gdp(t) - allocate(t, "C", "B: conditional tier")["gf_total"] for t in range(a, b + 1)]
        P(f"   {name}: room by year " + " ".join(f"{x:5.1f}" for x in room) + f"  (min {min(room):.1f}, total {sum(room):.1f})")
    P(f"   ARCA's $25B readiness reserve (sec. 106(e)) released evenly {bill_period()} = 5.0 a year")

    P("\n-- 9h. Draw vs deficit cost: the excise offset CBO applies (scenario B) --")
    P("   The cap counts general-fund transfers. CBO scores new excise receipts net of a ~25% income/payroll offset")
    P("   (H.R. 8870 EV fee: $16.8B gross, $12.4B net, FY2026-36). New receipts vs baseline = fund - legacy - EV fee.")
    for name, (a, b) in list(PERIODS.items())[1:3]:
        rows = []
        for t in range(a, b + 1):
            draw = allocate(t, "C", "B: conditional tier")["gf_total"]
            off = EXCISE_OFFSET * (fund_revenue(t) - legacy(t) - ev_fee(t))
            rows.append((draw / gdp(t), (draw + off) / gdp(t), off))
        P(f"   {name}: draw %GDP " + " ".join(f"{r[0]:.3%}" for r in rows))
        P(f"   {'':9}  +offset  " + " ".join(f"{r[1]:.3%}" for r in rows) + f"   offset {sum(r[2] for r in rows):.1f} total")

    P("\n-- 9i. NHTSA and FMCSA, folded into the Highway Account's need (scenario B) --")
    P("   safety by year FY2027-35: " + " ".join(f"{safety_program(t):.2f}" for t in range(2027, BILL_START + 5)))
    global INCLUDE_SAFETY
    for name, (a, b) in list(PERIODS.items())[1:3]:
        INCLUDE_SAFETY = False; off = [allocate(t, "C", "B: conditional tier")["gf_pct"] for t in range(a, b + 1)]
        INCLUDE_SAFETY = True;  on = [allocate(t, "C", "B: conditional tier")["gf_pct"] for t in range(a, b + 1)]
        P(f"   {name}: FHWA only " + " ".join(f"{x:.3%}" for x in off) + "  | with safety " + " ".join(f"{x:.3%}" for x in on))

    P("\n-- 9d. Rail + transit against highways, and the split, by period (scenario B) --")
    for name, (a, b) in PERIODS.items():
        T = sum(transit_program(t) for t in range(a, b + 1)); R = sum(rail_program(t) for t in range(a, b + 1)); H = sum(highway_program(t) for t in range(a, b + 1))
        P(f"   {name}: transit {T:.1f}  rail {R:.1f}  highways {H:.1f}  (T+R)/H {(T+R)/H:.2f}  split {T/(T+R):.0%}/{R/(T+R):.0%}")

    P("\n-- 10. Assumptions, by sensitivity --")
    for n, d, s in ASSUMPTIONS: P(f"  [{s:>6}] {n}: {d}")

def to_json(path="transit_model_output.json"):
    out = {"auth": [{"sec": s, "name": n, "kind": k, "src": sr, "vals": v, "total": round(sum(v), 2)} for s, n, k, sr, v in AUTH],
           "scenarios": {sc: {"five_year": round(sum(auth_total(y, sc) for y in range(BILL_START, BILL_START + 5)), 2)} for sc in OPERATING_SCENARIOS},
           "fund": {t: round(fund_revenue(t), 2) for t in YEARS},
           "arch": {a: {sc: period_rows(a, sc) for sc in OPERATING_SCENARIOS} for a in "ABC"},
           "amortization": amortization(), "envelope": envelope(),
           "caps": {"arca_method": CAP_ARCA_METHOD, "all_in": CAP_ALL_IN}}
    json.dump(out, open(path, "w"), indent=1)

if __name__ == "__main__":
    main()
    if "--json" in sys.argv: to_json()
