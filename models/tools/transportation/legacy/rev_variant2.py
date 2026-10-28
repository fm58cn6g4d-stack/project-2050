"""Revenue redesign v2 (2026-10-12): fuel taxes +5c/gal a year FY2029-31 then CPI-indexed, never phased out;
EV/PHEV registration fee kept as a bridge through FY2029; per-mile charge on clean passenger vehicles from FY2030;
clean heavy trucks (Class 6-8) pay a per-mile charge instead of diesel tax, with the 12% retail FET cut to 4% for them.
All (A) assumptions are listed in ASSUME and printed."""
import merge_decisions as D, transit_fiscal_model as M
B = "B: conditional tier"
ASSUME = {
 "fuel share of legacy receipts": 0.85, "gasoline share of fuel receipts": 0.65, "diesel share of fuel receipts": 0.35,
 "step-up": "+5c gas and diesel in each of FY2029-31, CPI-indexed from FY2032",
 "clean passenger rate": "1.5c/mi FY2030, +3%/yr (NHCCI + 0.5%)", "miles per plug-in": 11000, "PHEV discount": "10% of stock-miles",
 "heavy truck VMT 2025 (Class 6-8, B mi)": 300, "heavy VMT growth": 0.01,
 "clean heavy truck rate": "8.5c/mi FY2030, +3%/yr",
 "clean share of heavy VMT": "1% FY2030 -> 8% FY2036 -> 30% FY2046 (linear between)",
 "clean share of new heavy sales": "5% FY2030 -> 25% FY2036 -> 50% FY2046",
 "retail FET (4051) receipts FY2028, $B": 6.5, "collection cost": 0.10,
}
def lerp(t, pts):
    for (a, va), (b, vb) in zip(pts, pts[1:]):
        if a <= t <= b: return va + (vb - va) * (t - a) / (b - a)
    return pts[-1][1] if t > pts[-1][0] else pts[0][1]
def heavy_clean_share(t): return 0 if t < 2030 else lerp(t, [(2030, .01), (2036, .08), (2046, .30)])
def heavy_sales_share(t): return 0 if t < 2030 else lerp(t, [(2030, .05), (2036, .25), (2046, .50)])
def step(t): return 0 if t < 2029 else 5 * min(t - 2028, 3)
def gas_factor(t): return (18.4 + step(t)) / 18.4 * 1.025 ** max(t - 2031, 0)
def dsl_factor(t): return (24.4 + step(t)) / 24.4 * 1.025 ** max(t - 2031, 0)
def fuel(t):
    leg = M.legacy(t) * 0.85
    return leg * 0.65 * gas_factor(t) + leg * 0.35 * dsl_factor(t) * (1 - heavy_clean_share(t))   # clean trucks leave diesel tax
def other(t):   # HVUT, tires, retail FET; FET cut to 4% on clean truck sales
    o = M.legacy(t) * 0.15 * M.infl(t, 2028)
    fet_loss = 6.5 * M.infl(t, 2028) * heavy_sales_share(t) * (8 / 12)
    return o - fet_loss
def ev_fee_bridge(t): return M.ev_fee(t) if t <= 2029 else 0.0
def clean_pass(t):
    if t < 2030: return 0.0
    return M._ev_stock_model(t) / (M._ev_stock_model(t) / lerp(t, [(2029, 9), (2035, 25), (2040, 45), (2045, 70), (2052, 90)])) * 11000 * 0.9 * 1.5 * 1.03 ** (t - 2030) / 100 / 1000 * 0.9
def clean_heavy(t):
    if t < 2030: return 0.0
    vmt = 300 * 1.01 ** (t - 2025)
    return vmt * heavy_clean_share(t) * 8.5 * 1.03 ** (t - 2030) / 100 * 0.9
def fund_v2(t):
    if t < 2029: return M.legacy(t)
    return fuel(t) + other(t) + ev_fee_bridge(t) + clean_pass(t) + clean_heavy(t)
if __name__ == "__main__":
    P = print; old = M.fund_revenue
    P("-- Why FY2029 falls short in the first redesign: current design vs v2, FY2029 ($B)")
    t = 2029; leg = M.legacy(t) * M.infl(t, 2028)
    P(f"  current: fuel/other {leg*(1-1/14):.1f} (1/14 displaced) + per-mile all vehicles {M.per_mile_rate(t)*M.VMT_2025*10*1.005**4*0.9:.1f} + EV fee {M.ev_fee(t):.2f} = {old(t):.1f}")
    P(f"  v2:      fuel {fuel(t):.1f} + other {other(t):.1f} + EV fee {ev_fee_bridge(t):.2f} + clean pass {clean_pass(t):.1f} + clean heavy {clean_heavy(t):.1f} = {fund_v2(t):.1f}")
    P(f"  step-up adds {fuel(t)-M.legacy(t)*0.85:.1f} over unindexed current-law fuel taxes")
    base = {t: old(t) for t in range(2029, 2047)}
    M.fund_revenue = fund_v2
    P("\n FY   current  v2    fuel  other  EVfee  cleanPax cleanHvy  draw  CBObasis")
    for t in range(2029, 2047):
        a = M.allocate(t, "C", B)
        cbo = (a["gf_total"] + M.EXCISE_OFFSET * (fund_v2(t) - M.legacy(t) - (M.ev_fee(t) if t <= 2029 else 0))) / M.gdp(t)
        P(f" {t} {base[t]:6.1f} {fund_v2(t):6.1f} {fuel(t):6.1f} {other(t):5.1f} {ev_fee_bridge(t):5.2f} {clean_pass(t):7.1f} {clean_heavy(t):7.1f}  {a['gf_pct']:.3%} {cbo:.3%}")
    for r in M.period_rows("C", B)[1:]:
        P(r['period'], f"avg {r['gf_pct_avg']:.3%} peak {r['gf_pct_peak']:.3%} ({r['peak_year']}) fund {r['fund']:.1f}",
          "cov", "/".join(f"{r['ded'][k]/r['prog'][k]:.0%}" for k in r['ded']), "ded", {k: round(v, 1) for k, v in r['ded'].items()}, "gf", {k: round(v, 1) for k, v in r['gf'].items()})
    for name, (a, b) in list(M.PERIODS.items())[1:3]:
        room = [M.CAP_ALL_IN * M.gdp(t) - M.allocate(t, "C", B)["gf_total"] for t in range(a, b + 1)]
        P(name, "room", [round(x, 1) for x in room], "less 1112", [round(x - D.G1112[t], 1) for x, t in zip(room, range(a, b + 1))],
          "less reserve", [round(x - D.G1112[t] - D.RESERVE.get(t, 0), 1) for x, t in zip(room, range(a, b + 1))])
    P("FY2032-36 fund v2", round(sum(fund_v2(t) for t in range(2032, 2037)), 1), "vs current", round(sum(base[t] for t in range(2032, 2037)), 1))
    P("FY2032-36 clean heavy", round(sum(clean_heavy(t) for t in range(2032, 2037)), 1), "clean pax", round(sum(clean_pass(t) for t in range(2032, 2037)), 1),
      "FET loss", round(sum(6.5 * M.infl(t, 2028) * heavy_sales_share(t) * 8 / 12 for t in range(2032, 2037)), 1))
    P("shares solve", {k: round(v * 100, 1) for k, v in M.solve_incremental_shares(B)[0].items()})
    for k, v in ASSUME.items(): P(f"  (A) {k}: {v}")
