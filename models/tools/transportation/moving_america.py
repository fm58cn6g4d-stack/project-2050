#!/usr/bin/env python3
"""Moving America Act of 2031 (Draft 2, MOV-): the fiscal model in one module.

Folded on Oct 20, 2026 from the overlay stack in legacy/ (transit_fiscal_model.py plus merge_decisions,
solvency_paths, solvency_final, revenue_plan, funding_stack, final_architecture, final_bill, fossil_premium,
fossil_final and final_v3). Those scripts patched each other's functions at import time, so results depended
on import order. Here every Draft 2 decision is a plain value and nothing is patched. The arithmetic is kept
operation for operation, so report.py prints exactly what legacy/final_v3.py printed (test_moving_america.py
checks this).

Units: billions of nominal dollars by federal fiscal year, unless a name says % of GDP.
Tags: (S) sourced, (R) from the ARCA architecture doc, (A) assumption. The decision tags [A-n] are Draft 2's.

What is NOT here (it stays in legacy/transit_fiscal_model.py, which still runs): the ARCA validation runs,
the old architectures A and B, the per-mile all-vehicle design and the FY2031-35 calendar.
"""
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------------------------
# 1. Macro
# ---------------------------------------------------------------------------------------------
INFL = 0.025                         # (R) ARCA's inflation assumption
GDP_FY2026 = 60.4 / 0.00192          # (R) backed out of ARCA: $60.4B = 0.192% of GDP
GDP_GROWTH = 0.041                   # (A) nominal
CAP_ALL_IN = (60.4 + 2.629 + 1.7) / GDP_FY2026   # the 0.206% benchmark (A-4: a benchmark, not a cap)
EXCISE_OFFSET = 0.25                 # (R) CBO/JCT income-and-payroll offset on new excise receipts
BILL_START = 2032                    # the 2031 bill authorizes FY2032-36
PERIODS = {"FY2027-28": (2027, 2028), "FY2029-31": (2029, 2031), "FY2032-36": (2032, 2036),
           "FY2037-41": (2037, 2041), "FY2042-46": (2042, 2046)}
MODES = ("hwy", "tra", "rail")
B = "B: conditional tier"            # transit operating tier as drafted [A-3]

def gdp(t): return GDP_FY2026 * (1 + GDP_GROWTH) ** (t - 2026)
def infl(t, base=2026): return (1 + INFL) ** (t - base)

# ---------------------------------------------------------------------------------------------
# 2. Highways and safety (H.R. 8870 baseline, then division B)
# ---------------------------------------------------------------------------------------------
FHWA_FY2026 = 62.657                 # (R)
HR8870_HWY = {2027: 72.909, 2028: 73.684, 2029: 75.021, 2030: 76.296, 2031: 77.635}   # (S) sec. 1102 + exempt
CBO_OL = {2027: 91.183, 2028: 92.346, 2029: 94.053, 2030: 95.683, 2031: 97.393}       # (S) CBO Sept 30 2026
HR8870_EXEMPT = 0.639
HR8870_CA_EXACT = {2027: 16.868, 2028: 17.205, 2029: 17.527, 2030: 17.835, 2031: 18.157}  # (S) sec. 3023

def highway_program(t):
    if t in HR8870_HWY: return HR8870_HWY[t]
    if t < 2027: return FHWA_FY2026 * infl(t)
    return HR8870_HWY[2031] * infl(t, 2031)

def safety_program(t):
    """NHTSA and FMCSA from the Highway Account (CBO limitation less FHWA less FTA)."""
    if t in CBO_OL: return CBO_OL[t] - (HR8870_HWY[t] - HR8870_EXEMPT) - HR8870_CA_EXACT[t]
    return safety_program(2031) * infl(t, 2031) if t > 2031 else 0.0

# Interstate and Bridge Renewal, div. B sec. 1104 [A-23]: H.R. 8870's $2B bridge program as contract
# authority, grown 2.5%, plus new money 0/2/4/6/8 over FY2032-36, then the FY2036 level +2.5% a year.
IBR_NEW = {2032: 0, 2033: 2, 2034: 4, 2035: 6, 2036: 8}
def ibr(t):
    if t < 2032: return 0.0
    return 2.0 * 1.025 ** (t - 2031) + (IBR_NEW[t] if t <= 2036 else 8 * 1.025 ** (t - 2036))

def highway_need(t):
    return highway_program(t) + safety_program(t) + ibr(t)

# ---------------------------------------------------------------------------------------------
# 3. Rail program (ARCA canonical table; reconciliation obligated over FY2029-31 [A-16])
# ---------------------------------------------------------------------------------------------
RAIL_250PLUS = {2027: 10.5, 2028: 11.0, 2029: 11.9, 2030: 12.9, 2031: 13.3}
RAIL_RECON = {2029: 6.0, 2030: 17.0, 2031: 25.5}
RAIL_ARCA_VALS = [39.95, 47.29, 52.07, 56.13, 58.59]     # $254.03B, FY2032-36
RAIL_EXPANSION_SHARE = (55.00 + 20.20 + 6.00 + 12.00) / 254.03   # secs 303, 310, 311, 312
# Rail expansion appropriations by year (div. A sec. 105). Typed in the legacy final_v3.py rather than computed.
RAIL_EXPANSION = dict(zip(range(2032, 2037), [11.6, 16.1, 19.1, 22.25, 24.15]))

def rail_program(t):
    b = BILL_START
    if b <= t < b + 5: return RAIL_ARCA_VALS[t - b]
    if b + 5 <= t < b + 10: return 214.3 / 5
    if b + 10 <= t < b + 15: return 242.4 / 5
    return RAIL_RECON.get(t, 0.0) + RAIL_250PLUS.get(t, 0.0)

# ---------------------------------------------------------------------------------------------
# 4. Transit program (division C, the canonical authorization table)
# ---------------------------------------------------------------------------------------------
HR8870_CA = {2027: 16.87, 2028: 17.21, 2029: 17.53, 2030: 17.84, 2031: 18.16}
CIG_250PLUS_DELIVERED = (5.0 + 10.0 * 0.70) / 5
def transit_250plus(t): return HR8870_CA[t] + CIG_250PLUS_DELIVERED + (0.15 if t == 2031 else 0.0)

#  sec, program, kind (R renewal / X expansion), source (TF trust fund / GF general fund), FY2032-36
AUTH = [
 ("201", "Service operating assistance (new 5307(i))",          "R", "TF", [6.00, 6.50, 7.00, 7.50, 8.00]),
 ("301", "State of good repair formula (5337)",                 "R", "TF", [5.20, 5.40, 5.60, 5.80, 6.00]),
 ("302", "Backlog retirement schedule (new 5337(g))",           "R", "TF", [6.00, 6.15, 6.30, 6.46, 6.62]),
 ("303", "Asset management enforcement and capacity (5326)",    "R", "TF", [0.10, 0.10, 0.10, 0.10, 0.10]),
 ("304", "Transit resilience",                                  "R", "TF", [0.60, 0.60, 0.60, 0.60, 0.60]),
 ("401", "Capital Investment Grants (5309)",                    "X", "GF", [4.50, 5.00, 5.50, 6.00, 6.50]),
 ("501", "Workforce: apprenticeship, training, operator safety","R", "TF", [0.50, 0.55, 0.60, 0.60, 0.60]),
 ("601", "Urbanized area formula, capital (5307, 5340)",        "R", "TF", [10.00, 10.40, 10.80, 11.20, 11.70]),
 ("602", "Buses and bus facilities (5339)",                     "R", "TF", [2.60, 2.70, 2.80, 2.90, 3.00]),
 ("603", "Rural, tribal and intercity bus (5311)",              "R", "TF", [1.40, 1.45, 1.50, 1.55, 1.60]),
 ("604", "Seniors and people with disabilities (5310)",         "R", "TF", [0.60, 0.62, 0.64, 0.66, 0.68]),
 ("605", "All Stations Accessibility",                          "R", "TF", [1.00, 1.00, 1.00, 1.00, 1.00]),
 ("606", "Joint transit-rail facilities and station access",    "X", "GF", [0.60] * 5),        # [A-6]
 ("607", "Ferries",                                             "R", "TF", [0.20, 0.20, 0.20, 0.20, 0.20]),
 ("608", "Emergency relief, quick release (5324)",              "R", "TF", [0.10, 0.10, 0.10, 0.10, 0.10]),
 ("701", "Planning, research, safety, FTA capacity, delivery",  "R", "TF", [0.90, 0.92, 0.95, 0.97, 1.00]),
]
OPERATING_SCENARIOS = {"A: bar kept": 0.0, "B: conditional tier": 1.0, "C: broad eligibility": 2.0}

# 2029-30 reconciliation, transit packages one and two ($32B), obligated over FY2029-31 [A-16].
# The legacy stack spread each line over FY2029-31 at 10/11/11 (merge) and then rescaled to 4/13/15; the
# two steps are kept as written so the floating-point sums match the old output exactly.
_TRANSIT_RECON_LINES = [
 ("Operating transition grants", "R", 4.00), ("Operating transition grants", "R", 5.00),
 ("State of good repair, shovel-ready backlog", "R", 4.00), ("State of good repair, shovel-ready backlog", "R", 6.00),
 ("Bus and railcar replacement orders", "R", 3.00), ("Bus and railcar replacement orders", "R", 1.00),
 ("Station accessibility", "R", 3.00), ("Capital Investment Grants, executed agreements", "X", 3.00),
 ("Credit subsidy: transit and joint development", "X", 1.00), ("Credit subsidy: transit and joint development", "X", 1.00),
 ("Workforce and FTA capacity", "R", 1.00),
]
def _transit_recon(schedule={2029: 4.0, 2030: 13.0, 2031: 15.0}):
    merge = {2029: 10.0, 2030: 11.0, 2031: 11.0}
    base = [(n, k, ty, v / 32.0 * merge[ty]) for n, k, v in _TRANSIT_RECON_LINES for ty in merge]
    ys = {y: sum(v for n, k, yy, v in base if yy == y) for y in (2029, 2030, 2031)}
    return [(n, k, y, v * schedule[y] / ys[y]) for n, k, y, v in base]
TRANSIT_RECON = _transit_recon()

def transit_program(t, scenario=B, kind=None):
    """Transit by year. After FY2036: renewal +3.5%/yr, operating tier +4%, backlog 2.5%, CIG +5% to FY2041 then 2.5%."""
    if t < BILL_START:
        base = transit_250plus(t)
        rec = sum(v for n, k, y, v in TRANSIT_RECON if y == t and (kind is None or k == kind))
        if kind == "X": return CIG_250PLUS_DELIVERED + rec
        if kind == "R": return (base - CIG_250PLUS_DELIVERED) + rec
        return base + sum(v for n, k, y, v in TRANSIT_RECON if y == t)
    m = OPERATING_SCENARIOS[scenario]
    if t < BILL_START + 5:
        i = t - BILL_START; s = 0.0
        for sec, name, k, sr, vals in AUTH:
            v = vals[i] * (m if sec == "201" else 1.0)
            if kind is None or k == kind: s += v
        return s
    n = t - (BILL_START + 4); s = 0.0
    for sec, name, k, sr, vals in AUTH:
        v = vals[4]
        if sec == "201":   v = v * m * 1.04 ** n
        elif sec == "302": v = v * 1.025 ** n
        elif sec == "401": v = v * (1.05 ** min(n, 5)) * (1.025 ** max(n - 5, 0))
        elif sec == "606": v = v * 1.025 ** n
        else:              v = v * 1.035 ** n
        if kind is None or k == kind: s += v
    return s

def need(m, t, sc=B):
    """Renewal need by mode (expansion is general fund by design)."""
    if m == "hwy": return highway_need(t)
    if m == "tra": return transit_program(t, sc, kind="R")
    return rail_program(t) * (1 - RAIL_EXPANSION_SHARE)

# ---------------------------------------------------------------------------------------------
# 5. Current-law trust-fund receipts, corrected for plug-in displacement after FY2036
# ---------------------------------------------------------------------------------------------
CBO_HWY = {2026: 41560, 2027: 42269, 2028: 42826, 2029: 43297, 2030: 43738, 2031: 44174,
           2032: 44623, 2033: 45091, 2034: 45576, 2035: 46083, 2036: 46607}           # (S) $M, June 2026
CBO_TRA = {2026: 5662, 2027: 5731, 2028: 5770, 2029: 5795, 2030: 5814, 2031: 5831,
           2032: 5847, 2033: 5864, 2034: 5881, 2035: 5901, 2036: 5921}
FLEX = 1.2                           # (S) highway account -> transit account each year
EV_CBO = {2028: 0.207, 2029: 0.726, 2030: 1.177, 2031: 1.655, 2032: 1.951, 2033: 2.287, 2034: 2.554,
          2035: 2.942, 2036: 3.276}  # (S) H.R. 8870 EV fee, gross

def _legacy_cbo(t, acct="both"):
    """CBO's current-law receipts, unindexed; after FY2036 grown 1%/yr."""
    def one(d): return (d[t] if t in d else d[2036] * 1.01 ** (t - 2036)) / 1000.0
    h, tr = one(CBO_HWY), one(CBO_TRA)
    return {"hwy": h, "tra": tr, "both": h + tr}[acct]

_PLUGIN_STOCK = [(2029, 9), (2035, 25), (2040, 45), (2045, 70), (2052, 90)]   # (A) millions
def plugin_stock(t):
    for (a, va), (b, vb) in zip(_PLUGIN_STOCK, _PLUGIN_STOCK[1:]):
        if a <= t <= b: return va + (vb - va) * (t - a) / (b - a)
    return 9

def _ev_stock_model(t):
    stock = None
    for (a, va), (b, vb) in zip(_PLUGIN_STOCK, _PLUGIN_STOCK[1:]):
        if a <= t <= b:
            stock = va + (vb - va) * (t - a) / (b - a); break
    fee = min(130 + 5 * (t - 2027), 200) * 0.85
    return stock * fee / 1000.0

def ev_fee(t):
    if t < 2029: return 0.0
    if t in EV_CBO: return EV_CBO[t]
    return _ev_stock_model(t) * EV_CBO[2036] / _ev_stock_model(2036)

FLEET = lambda t: 290 * 1.005 ** (t - 2029)          # (A) light-duty fleet, millions
def _plug(t): return _ev_stock_model(t) / (_ev_stock_model(t) / plugin_stock(t)) if t >= 2029 else 7
def gas_volume(t):
    """Gasoline volume relative to CBO's path: plug-in displacement after FY2036, and ICE fuel economy +1%/yr."""
    if t <= 2036: v = 1.0
    else:
        s, s0 = _plug(t) / FLEET(t), _plug(2036) / FLEET(2036)
        v = (1 - s) / (1 - s0) * 1.005 ** (t - 2036) / 1.01 ** (t - 2036)
    return v * (0.99 ** max(t - 2036, 0))

def legacy(t, acct="both"):
    return _legacy_cbo(t, acct) * (1 - 0.85 * 0.65 * (1 - gas_volume(t)))

def floors(t):
    """Div. A sec. 101(c): highway and transit accounts first credited their FY2028 amounts, CPI-indexed."""
    return (legacy(2028, "hwy") - FLEX) * infl(t, 2028), (legacy(2028, "tra") + FLEX) * infl(t, 2028)

HEAVY_VMT = lambda t: 300 * 1.01 ** (t - 2025)       # (A) Class 6-8, billion miles
def _lerp2(t, pts):
    for (a, va), (b, vb) in zip(pts, pts[1:]):
        if a <= t <= b: return va + (vb - va) * (t - a) / (b - a)
    return pts[-1][1] if t > pts[-1][0] else 0.0
def heavy_clean(t): return 0 if t < 2030 else _lerp2(t, [(2030, .01), (2036, .08), (2046, .30)])
def heavy_sales(t): return 0 if t < 2030 else _lerp2(t, [(2030, .05), (2036, .25), (2046, .50)])

def aviation(t):                     # (R) $4 -> $12 -> cap $16 per segment; $1 = $0.70B on the 2026 base [A-13]
    b = BILL_START
    if t < b: return 0.0
    rate = 4 + 2 * (t - b) if t <= b + 4 else min(12 + 0.4 * (t - b - 4), 16)
    return rate * 0.70 * 1.0215 ** (t - 2026)

def rail_diesel(t):                  # (R) 10/5 cents from FY2031 (2030 act), 15/7.5 cents from FY2032 [A-13]
    return 0.0 if t < 2030 else 0.36 if t < BILL_START else 0.53 * 1.004 ** (t - BILL_START)

# ---------------------------------------------------------------------------------------------
# 6. The revenue design (div. A secs. 102-104) and the design dials
# ---------------------------------------------------------------------------------------------
@dataclass
class Design:
    """Every dial Draft 2 lists, at its drafted value. Change one to run a sensitivity."""
    steps: dict = field(default_factory=lambda: {y: 3 for y in range(2030, 2040)})   # Fix-It-First, cents [A-10]
    prem_steps: dict = field(default_factory=lambda: {y: 2 for y in range(2040, 2045)})  # fossil premium [A-28]
    wd: float = 3.0                  # weight-distance average, cents a mile [A-12]
    wd_from: int = 2031
    clean_from: int = 2031           # clean-vehicle per-mile charge starts [A-11]
    index_from: int = 2030           # CPI indexing of fuel rates
    ev_to: int = 2030                # EV fee bridge into the fund through FY2030
    mpg: float = 40.0                # clean cars pay parity with a 40-mpg car [A-11]
    hmpg: float = 6.5                # clean trucks: parity with a 6.5-mpg truck
    ld_factor: float = 1 - 0.20 * 0.70   # PHEVs (20% of plug-ins) pay 30% [A-11]
    shares: tuple = ({"hwy": .35, "tra": .50, "rail": .15}, {"hwy": .45, "tra": .40, "rail": .15}, 2037)  # [A-7, A-8]
    scenario: str = B

class Revenue:
    """Fund receipts by fiscal year for one design. premium=False gives the receipts without the fossil premium."""
    def __init__(self, d: Design, premium=True):
        self.d, self.premium = d, premium
    def cum(self, t): return sum(v for y, v in self.d.steps.items() if y <= t)
    def pc(self, t): return sum(v for y, v in self.d.prem_steps.items() if y <= t) if self.premium else 0
    def idx(self, t): return 1.0 if t < self.d.index_from else 1.025 ** (t - self.d.index_from + 1)
    def rg(self, t): return (18.4 + self.cum(t)) * self.idx(t)                 # gasoline road-use rate, cents
    def rd(self, t): return (24.4 + self.cum(t)) * self.idx(t)                 # diesel road-use rate
    def gr(self, t): return (18.4 + self.cum(t) + self.pc(t)) * self.idx(t)    # gasoline rate incl. premium
    def dr(self, t): return (24.4 + self.cum(t) + self.pc(t)) * self.idx(t)
    def cp(self, t):                                                           # clean-car per-mile charge
        d = self.d
        return 0 if t < d.clean_from else plugin_stock(t) * 11000 * 0.9 * self.rg(t) / d.mpg / 1e5 * 0.9 * d.ld_factor
    def __call__(self, t):
        d = self.d
        if t < 2029: return legacy(t)
        leg = legacy(t) * 0.85
        gas = leg * 0.65 * self.gr(t) / 18.4
        dsl = leg * 0.35 * self.dr(t) / 24.4 * (1 - heavy_clean(t))
        other = legacy(t) * 0.15 * infl(t, 2028) - 6.5 * infl(t, 2028) * heavy_sales(t) * 8 / 12
        other -= (0 if t < d.wd_from else 1.3 * infl(t, 2028))                 # heavy-vehicle use tax repealed
        ev = ev_fee(t) if t <= d.ev_to else 0.0
        cp = self.cp(t)
        ch = 0 if t < d.clean_from else HEAVY_VMT(t) * heavy_clean(t) * self.rd(t) / d.hmpg / 100 * 0.9
        w = 0 if t < d.wd_from else HEAVY_VMT(t) * 0.7 * d.wd * 1.03 ** (t - d.wd_from) / 100 * 0.95
        return gas + dsl + other + ev + cp + ch + w

def components(t, d: Design = None):
    """Dedicated revenue by source (Draft 2's table). The clean-car column comes from the design; the other
    columns use the legacy funding_stack convention (EV fee shown from FY2030; FY2029 is current law)."""
    d = d or Design()
    r25 = Revenue(Design(steps=d.steps, prem_steps={}, wd=3.0, mpg=25.0, ld_factor=1.0), premium=False)
    L = legacy(t) * 0.85
    gas = L * 0.65 * r25.rg(t) / 18.4 if t >= 2029 else L * 0.65
    dsl = L * 0.35 * r25.rd(t) / 24.4 * (1 - heavy_clean(t)) if t >= 2029 else L * 0.35
    other = (legacy(t) * 0.15 * infl(t, 2028) - 6.5 * infl(t, 2028) * heavy_sales(t) * 8 / 12
             - (1.3 * infl(t, 2028) if t >= 2031 else 0)) if t >= 2029 else legacy(t) * 0.15
    ev = ev_fee(t) if 2029 < t <= 2030 else 0.0
    cp25 = plugin_stock(t) * 11000 * 0.9 * r25.rg(t) / 25 / 1e5 * 0.9 if t >= 2031 else 0
    ch = HEAVY_VMT(t) * heavy_clean(t) * r25.rd(t) / 6.5 / 100 * 0.9 if t >= 2031 else 0
    wd = HEAVY_VMT(t) * 0.7 * 3 * 1.03 ** (t - 2031) / 100 * 0.95 if t >= 2031 else 0
    rail = aviation(t) + rail_diesel(t)
    c = dict(gas=gas, dsl=dsl, other=other, ev=ev, cp=cp25, ch=ch, wd=wd, rail=rail)
    c["total"] = sum(c.values()) - c["cp"] + Revenue(d, premium=False).cp(t)
    c["cp"] = Revenue(d, premium=False).cp(t)
    return c

# ---------------------------------------------------------------------------------------------
# 7. Allocation: floors, incremental shares, premium credited by general-fund need [A-7, A-8, A-28]
# ---------------------------------------------------------------------------------------------
class Model:
    def __init__(self, d: Design = None):
        self.d = d or Design()
        self.P0, self.P1 = Revenue(self.d, premium=False), Revenue(self.d, premium=True)
        self._cache = {}

    def shares(self, t):
        a, b, y = self.d.shares
        return a if t < y else b

    def _base(self, t, sc, fund, shares):
        F = fund(t); av, dz = aviation(t), rail_diesel(t)
        H = highway_need(t); T = transit_program(t, sc); R = rail_program(t)
        fh, ft = floors(t)
        if t < 2029:
            ded = {"hwy": legacy(t, "hwy") - FLEX, "tra": legacy(t, "tra") + FLEX, "rail": 0.0}
        else:
            inc = max(F - fh - ft, 0.0)
            scale = min(F / (fh + ft), 1.0)
            ded = {"hwy": fh * scale + inc * shares["hwy"],
                   "tra": ft * scale + inc * shares["tra"],
                   "rail": inc * shares["rail"] + av + dz}
        prog = {"hwy": H, "tra": T, "rail": R}
        gf = {m: max(prog[m] - ded[m], 0.0) for m in prog}
        trapped = {m: max(ded[m] - prog[m], 0.0) for m in prog}
        return {"fy": t, "fund": F, "aviation": av, "diesel": dz, "prog": prog, "ded": ded, "gf": gf,
                "trapped": trapped, "gf_total": sum(gf.values()), "gdp": gdp(t), "gf_pct": sum(gf.values()) / gdp(t)}

    def allocate(self, t, sc=None):
        sc = sc or self.d.scenario
        key = (t, sc)
        if key in self._cache: return self._cache[key]
        r = self._base(t, sc, self.P0, self.shares(t))
        pr = max(self.P1(t) - self.P0(t), 0)
        g = r["gf"]; G = sum(g.values()); w = {m: (g[m] / G if G > 0 else 1 / 3) for m in g}
        ded = {m: r["ded"][m] + pr * w[m] for m in w}; prog = r["prog"]
        gf = {m: max(prog[m] - ded[m], 0) for m in prog}; tr = {m: max(ded[m] - prog[m], 0) for m in prog}
        r.update(ded=ded, gf=gf, trapped=tr, gf_total=sum(gf.values()), gf_pct=sum(gf.values()) / r["gdp"], prem=pr)
        self._cache[key] = r
        return r

    def period_rows(self, sc=None):
        out = []
        for name, (a, b) in PERIODS.items():
            ys = [self.allocate(t, sc) for t in range(a, b + 1)]
            n = len(ys); agg = lambda f: sum(f(y) for y in ys)
            out.append({"period": name, "years": n, "fund": agg(lambda y: y["fund"]),
                        "prog": {m: agg(lambda y: y["prog"][m]) for m in MODES},
                        "ded": {m: agg(lambda y: y["ded"][m]) for m in MODES},
                        "gf": {m: agg(lambda y: y["gf"][m]) for m in MODES},
                        "trapped": agg(lambda y: sum(y["trapped"].values())),
                        "gf_per_year": agg(lambda y: y["gf_total"]) / n,
                        "gf_pct_avg": agg(lambda y: y["gf_total"]) / agg(lambda y: y["gdp"]),
                        "gf_pct_peak": max(y["gf_pct"] for y in ys),
                        "peak_year": max(ys, key=lambda y: y["gf_pct"])["fy"]})
        return out

    def solve_shares(self, sc=None):
        """Incremental shares giving equal renewal coverage in FY2042-46 (receipts without the premium)."""
        sc = sc or self.d.scenario
        yrs = range(BILL_START + 10, BILL_START + 15)
        F = sum(self.P0(t) for t in yrs); fh = sum(floors(t)[0] for t in yrs); ft = sum(floors(t)[1] for t in yrs)
        inc = F - fh - ft
        ren = {"hwy": sum(highway_need(t) for t in yrs), "tra": sum(transit_program(t, sc, kind="R") for t in yrs),
               "rail": sum(rail_program(t) * (1 - RAIL_EXPANSION_SHARE) for t in yrs)}
        other = {"hwy": fh, "tra": ft, "rail": sum(aviation(t) + rail_diesel(t) for t in yrs)}
        c = (inc + sum(other.values())) / sum(ren.values())
        raw = {m: max(c * ren[m] - other[m], 0.0) / inc for m in ren}
        tot = sum(raw.values())
        return {m: raw[m] / tot for m in raw}, c

    # --- derived figures Draft 2 carries ---
    def all_in_peak(self, sc=None):
        return max((self.allocate(t, sc)["gf_total"] + G1112[t] + RESERVE.get(t, 0)) / gdp(t) for t in range(2032, 2037))

    def renewal_coverage(self, a, b, sc=None):
        sc = sc or self.d.scenario
        return {m: sum(self.allocate(t, sc)["ded"][m] for t in range(a, b + 1)) / sum(need(m, t, sc) for t in range(a, b + 1))
                for m in MODES}

    def self_sufficient(self, sc=None):
        sc = sc or self.d.scenario
        return {m: next((t for t in range(2030, 2047) if self.allocate(t, sc)["ded"][m] >= need(m, t, sc)), None) for m in MODES}

    def topups(self):
        """Renewal top-ups (2029 and 2030 acts) and expansion appropriations (2031 bill) by year, FY2032-36 [A-14, A-15]."""
        rows = {}
        for t in range(2032, 2037):
            a = self.allocate(t); tx = transit_program(t, self.d.scenario, kind="X")
            h = a["gf"]["hwy"]; tr = max(a["gf"]["tra"] - tx, 0); rr = max(a["gf"]["rail"] - RAIL_EXPANSION[t], 0)
            ex = min(tx, a["gf"]["tra"]) + RAIL_EXPANSION[t]
            rows[t] = dict(hwy=h, tra=tr, rail=rr, exp=ex)
        return rows

    def cbo_basis(self, t, sc=None):
        al = self.allocate(t, sc); new = self.P1(t) - legacy(t) - (ev_fee(t) if t <= 2029 else 0)
        return (al["gf_total"] + (EXCISE_OFFSET * max(new, 0) if t >= 2030 else 0)) / gdp(t)

# Sec. 1112 general-fund grants (multimodal freight + National Infrastructure Grants) and the readiness
# reserve as illustrated [A-18, A-22]: counted in the "all-in" draw, outside both renewal and expansion.
G1112 = {t: (3.2 * 1.025 ** (t - 2031) if t >= 2032 else 5.2) for t in range(2027, 2047)}
RESERVE = {2032: 0, 2033: 0, 2034: 5, 2035: 8, 2036: 12}

# Fallback rounds (cuts to the general-fund draw, $B FY2032-36); typed in the legacy final_v3.py.
FALLBACK_CUTS = {"r1": 71.55, "r2": 132.27, "r3": 197.32}

# Sensitivities Draft 2 reports ("What breaks this")
SENSITIVITIES = {
    "3 pauses": dict(steps={y: 3 for y in (2030, 2031, 2033, 2034, 2036, 2037, 2039, 2040, 2041, 2042)}),
    "WD2": dict(wd=2.0),
    "steps2": dict(steps={y: 2 for y in range(2030, 2040)}),
    "index only": dict(steps={}),
    "scen C": dict(scenario="C: broad eligibility"),
    "scen A": dict(scenario="A: bar kept"),
    "no premium": dict(prem_steps={}),
    "25mpg PHEV50": dict(mpg=25.0, ld_factor=1 - 0.2 * 0.5),
}

# ---------------------------------------------------------------------------------------------
# 8. Ledger rows (what models/tools/ledger-build.py reads)
# ---------------------------------------------------------------------------------------------
def ledger_rows(m: Model = None):
    """Draft 2's figures that the master ledger carries, in $T. Spending is budget authority."""
    m = m or Model()
    tu = m.topups()
    act29_top = sum(tu[t]["hwy"] + tu[t]["tra"] + tu[t]["rail"] for t in (2032, 2033, 2034)) + tu[2035]["hwy"] + tu[2035]["tra"]
    act30_top = tu[2035]["rail"] + tu[2036]["hwy"] + tu[2036]["tra"] + tu[2036]["rail"]
    pkg29 = sum(RAIL_RECON_PACKAGE1.values()) + sum(TRANSIT_PACKAGE1.values())
    pkg30 = sum(RAIL_RECON_PACKAGE2.values()) + sum(TRANSIT_PACKAGE2.values())
    s29 = score_2029(m); s30 = score_2030()
    return dict(act29_package=pkg29, act29_topups=act29_top, act30_package=pkg30, act30_topups=act30_top,
                expansion=sum(r["exp"] for r in tu.values()), expansion_authority=expansion_authority(m.d.scenario),
                act29_gross=s29["gross"], act29_net=s29["net"], act30_gross=s30["gross"], act30_net=s30["net"],
                score_fuel_steps=SCORE_2029["fuel_steps"], score_clean_vehicle=s29["clean_vehicle"],
                score_truck_excise_ev_fee=SCORE_2029["zev_truck_excise"] + SCORE_2029["ev_fee_end"],
                score_weight_distance=SCORE_2030["weight_distance"], score_rail_aviation=SCORE_2030["rail_aviation"],
                score_offset=-EXCISE_OFFSET * (s29["gross"] + s30["gross"]))

def expansion_authority(sc=B):
    """Expansion appropriated in div. A sec. 105, FY2032-36: transit CIG and sec. 606 plus rail secs 303, 310-312."""
    return sum(transit_program(t, sc, kind="X") for t in range(2032, 2037)) + sum(RAIL_EXPANSION.values())

# Reconciliation scores, $B over each act's ten-year window (Draft 2, "Scoring"). Only the clean-car charge is
# computed here; the other lines were scored in the legacy funding_stack run and are carried as typed.
SCORE_2029 = {"fuel_steps": 380.4, "zev_truck_excise": -8.4, "ev_fee_end": -14.7, "clean_truck": 12.9}  # FY2029-38
SCORE_2030 = {"weight_distance": 53.4, "rail_aviation": 73.3}                                           # FY2030-39

def score_2029(m: Model = None):
    m = m or Model(); S = SCORE_2029
    cp = sum(m.P0.cp(t) for t in range(2029, 2039))
    gross = S["fuel_steps"] + S["zev_truck_excise"] + S["ev_fee_end"] + cp + S["clean_truck"]
    return dict(clean_car=cp, clean_vehicle=cp + S["clean_truck"], gross=gross, net=gross * (1 - EXCISE_OFFSET))

def score_2030():
    gross = SCORE_2030["weight_distance"] + SCORE_2030["rail_aviation"]
    return dict(gross=gross, net=gross * (1 - EXCISE_OFFSET))

# Package contents (Draft 2, "The packages"), $B
RAIL_RECON_PACKAGE1 = {"RRIF credit risk premium": 6.00, "Zero-emission rail": 9.00, "State of good repair": 8.00,
                       "Long-distance fleet": 5.50, "Corridor ID": 3.50, "Station access and ADA": 3.00}
TRANSIT_PACKAGE1 = {"Operating transition": 4.00, "State of good repair": 4.00, "Bus and railcar": 3.00, "Credit subsidy": 1.00}
RAIL_RECON_PACKAGE2 = {"RRIF second tranche": 4.00, "Grade crossings": 4.00, "Electrification": 3.00, "Workforce": 2.50}
TRANSIT_PACKAGE2 = {"Operating transition": 5.00, "State of good repair": 6.00, "Bus replacement": 1.00,
                    "Station accessibility": 3.00, "CIG": 3.00, "Credit subsidy": 1.00, "Workforce and FTA": 1.00}

if __name__ == "__main__":
    import report
    report.main()
