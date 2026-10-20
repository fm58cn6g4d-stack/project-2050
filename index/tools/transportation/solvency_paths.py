"""Paths to solvency (2026-10-12). Revenue packages compared on the merged program (merge_decisions overlay).
Fixes one flaw in rev_variant/rev_variant2: after FY2036 the model grew legacy fuel receipts 1%/yr, ignoring that
plug-ins displace gasoline. Here gasoline volume after FY2036 shrinks with the plug-in share of the fleet."""
import merge_decisions as D, transit_fiscal_model as M
B = "B: conditional tier"
_leg = M.legacy
FLEET = lambda t: 290 * 1.005 ** (t - 2029)            # (A) light-duty fleet, millions
def plug(t): return M._ev_stock_model(t) / (M._ev_stock_model(t) / _lerp(t)) if t >= 2029 else 7
def _lerp(t):
    pts = [(2029, 9), (2035, 25), (2040, 45), (2045, 70), (2052, 90)]
    for (a, va), (b, vb) in zip(pts, pts[1:]):
        if a <= t <= b: return va + (vb - va) * (t - a) / (b - a)
    return 9
def gas_volume(t):  # relative to CBO's path; CBO's baseline (through FY2036) already embeds its own EV view
    if t <= 2036: return 1.0
    s, s0 = plug(t) / FLEET(t), plug(2036) / FLEET(2036)
    return (1 - s) / (1 - s0) * 1.005 ** (t - 2036) / 1.01 ** (t - 2036)
def legacy_fixed(t, acct="both"):
    x = _leg(t, acct)
    return x * (1 - 0.85 * 0.65 * (1 - gas_volume(t)))
M.legacy = legacy_fixed
HEAVY_VMT = lambda t: 300 * 1.01 ** (t - 2025)          # (A) Class 6-8, billion miles
def lerp2(t, pts):
    for (a, va), (b, vb) in zip(pts, pts[1:]):
        if a <= t <= b: return va + (vb - va) * (t - a) / (b - a)
    return pts[-1][1] if t > pts[-1][0] else 0.0
def heavy_clean(t): return 0 if t < 2030 else lerp2(t, [(2030, .01), (2036, .08), (2046, .30)])
def heavy_sales(t): return 0 if t < 2030 else lerp2(t, [(2030, .05), (2036, .25), (2046, .50)])

def make(steps=None, index_from=None, ev_bridge_to=2029, clean_from=2030, clean_rate=1.5, heavy_rate=8.5,
         truck_wd=None, all_vehicle_permile=False):
    """steps: {fy: cents added that year (cumulative)}; index_from: CPI indexing of fuel rates from that FY;
       truck_wd: (start FY, cents/mi) weight-distance charge on all Class 7-8 diesel trucks (~70% of heavy VMT)."""
    steps = steps or {}
    def cum(t): return sum(v for y, v in steps.items() if y <= t)
    def idx(t): return 1.0 if index_from is None or t < index_from else 1.025 ** (t - index_from + 1)
    def fund(t):
        if t < 2029: return M.legacy(t)
        if all_vehicle_permile: return CURRENT(t)
        leg = M.legacy(t) * 0.85
        gas = leg * 0.65 * (18.4 * idx(t) + cum(t)) / 18.4
        dsl = leg * 0.35 * (24.4 * idx(t) + cum(t)) / 24.4 * (1 - heavy_clean(t))
        other = M.legacy(t) * 0.15 * M.infl(t, 2028) - 6.5 * M.infl(t, 2028) * heavy_sales(t) * 8 / 12
        ev = M.ev_fee(t) if t <= ev_bridge_to else 0.0
        cp = 0 if t < clean_from else _lerp(t) * 11000 * 0.9 * clean_rate * 1.03 ** (t - clean_from) / 1e5 * 0.9
        ch = 0 if t < clean_from else HEAVY_VMT(t) * heavy_clean(t) * heavy_rate * 1.03 ** (t - clean_from) / 100 * 0.9
        wd = 0 if not truck_wd or t < truck_wd[0] else HEAVY_VMT(t) * 0.7 * (1 - heavy_clean(t)) * truck_wd[1] * 1.03 ** (t - truck_wd[0]) / 100 * 0.95
        return gas + dsl + other + ev + cp + ch + wd
    return fund
CURRENT = M.fund_revenue          # all-vehicle per-mile, fuel phase-out (now on the corrected legacy base)

def report(name, fund, quiet=False):
    M.fund_revenue = fund
    rows = M.period_rows("C", B)
    peak = lambda a, b: max(M.allocate(t, "C", B)["gf_pct"] for t in range(a, b + 1))
    allin = max((M.allocate(t, "C", B)["gf_total"] + D.G1112[t] + D.RESERVE.get(t, 0)) / M.gdp(t) for t in range(2032, 2037))
    # renewal coverage FY2042-46 (expansion is general fund by design)
    yrs = range(2042, 2047)
    ren = {"hwy": sum(M.highway_need(t) for t in yrs), "tra": sum(M.transit_program(t, B, kind="R") for t in yrs),
           "rail": sum(M.rail_program(t) * (1 - M.RAIL_EXPANSION_SHARE) for t in yrs)}
    ded = {m: sum(M.allocate(t, "C", B)["ded"][m] for t in yrs) for m in ren}
    renall = sum(ded.values()) / sum(ren.values())
    out = dict(name=name, f29=M.allocate(2029, "C", B)["gf_pct"], p2931=peak(2029, 2031), a3236=rows[2]["gf_pct_avg"], p3236=peak(2032, 2036),
               allin=allin, a4246=rows[4]["gf_pct_avg"], fund3236=sum(fund(t) for t in range(2032, 2037)),
               fund46=fund(2046), ren=renall, rencov={m: ded[m] / ren[m] for m in ren}, ded46=ded, renneed=ren)
    M.fund_revenue = CURRENT
    if not quiet:
        print(f"{name:<44} FY29 {out['f29']:.3%} | 29-31pk {out['p2931']:.3%} | 32-36 {out['a3236']:.3%}/{out['p3236']:.3%} all-in {out['allin']:.3%} | 42-46 {out['a4246']:.3%} | "
              f"fund32-36 {out['fund3236']:.0f} FY46 {out['fund46']:.0f} | renewal cov 42-46 {out['ren']:.0%} ({'/'.join(f'{v:.0%}' for v in out['rencov'].values())})")
    return out

PKGS = {
 "0 current design (all-vehicle per-mile, fuel phase-out)": CURRENT,
 "1 v2: +10/15/20c steps, indexed FY32": make(steps={2029: 10, 2030: 5, 2031: 5}, index_from=2032),
 "2 index only from FY29 + clean per-mile FY30 + trucks": make(index_from=2029),
 "3 = 2 + truck weight-distance 2c/mi FY30": make(index_from=2029, truck_wd=(2030, 2.0)),
 "4 = 3 + 2c/yr gated steps FY32-41 (+20c by FY41)": make(index_from=2029, truck_wd=(2030, 2.0), steps={y: 2 for y in range(2032, 2042)}),
 "5 = 4 but 3 of 10 steps skipped by price breaker": make(index_from=2029, truck_wd=(2030, 2.0), steps={y: 2 for y in (2032, 2033, 2035, 2036, 2038, 2039, 2041)}),
 "6 = 4 + 5c 'catch-up' in FY29": make(index_from=2029, truck_wd=(2030, 2.0), steps={2029: 5, **{y: 2 for y in range(2032, 2042)}}),
 "7 = 4 + clean per-mile at 2.0c": make(index_from=2029, truck_wd=(2030, 2.0), clean_rate=2.0, steps={y: 2 for y in range(2032, 2042)}),
}
if __name__ == "__main__":
    print("gas volume vs CBO-path growth, FY2041/2046:", round(gas_volume(2041), 3), round(gas_volume(2046), 3))
    R = {k: report(k, f) for k, f in PKGS.items()}
