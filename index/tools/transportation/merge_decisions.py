"""Moving America Act of 2031 -- merge-session overlay on transit_fiscal_model.py (2026-10-12).
Applies the decisions recorded in the unified doc's 'Assumptions not yet approved' and prints every
figure the doc carries.  Does not edit the model; import it from the same folder.
  A-6  sec. 606 retargeted outside the five sec. 310 nodes, $0.60B a year ($3.00B)
  A-8  2029-30 reconciliation obligated on a FY2029-31 schedule (rail 16.0/16.0/16.5; transit 10.0/11.0/11.0)
  A-11 div. B sec. 1112 general-fund grants counted against the benchmark (overlay, reported separately)
  A-14 ARCA readiness reserve illustrated at 0/5/7/7/6 over FY2032-36
"""
import transit_fiscal_model as M
B = "B: conditional tier"
APPLY_606, APPLY_SCHEDULE = True, True
if APPLY_606:
    for row in M.AUTH:
        if row[0] == "606": row[4][:] = [0.60] * 5
if APPLY_SCHEDULE:
    M.RAIL_RECON.clear(); M.RAIL_RECON.update({2029: 16.0, 2030: 16.0, 2031: 16.5})
    TRA = {2029: 10.0, 2030: 11.0, 2031: 11.0}
    M.TRANSIT_RECON[:] = [(n, k, ty, v / 32.0 * TRA[ty]) for n, k, y, v in M.TRANSIT_RECON for ty in TRA]
G1112 = {t: 5.2 for t in range(2027, 2032)}; G1112.update({t: 5.2 * 1.025 ** (t - 2031) for t in range(2032, 2047)})
RESERVE = dict(zip(range(2032, 2037), [0, 5, 7, 7, 6]))
cap = M.CAP_ALL_IN
P = print
if __name__ == "__main__":
    b5 = range(2032, 2037)
    P("program by year: hwy", [round(M.highway_need(t), 2) for t in b5], "transit", [round(M.transit_program(t, B), 2) for t in b5],
      "rail", [round(M.rail_program(t), 2) for t in b5])
    P("totals", round(sum(M.highway_need(t) for t in b5), 2), round(sum(M.transit_program(t, B) for t in b5), 2),
      round(sum(M.rail_program(t) for t in b5), 2), round(sum(M.highway_need(t) + M.transit_program(t, B) + M.rail_program(t) for t in b5), 2))
    P("by year total", [round(M.highway_need(t) + M.transit_program(t, B) + M.rail_program(t), 2) for t in b5])
    P("transit expansion", round(sum(M.transit_program(t, B, kind='X') for t in b5), 2))
    for r in M.period_rows("C", B):
        P(f"{r['period']}: prog {r['prog']['hwy']:.2f}/{r['prog']['tra']:.2f}/{r['prog']['rail']:.2f} ded {r['ded']['hwy']:.2f}/{r['ded']['tra']:.2f}/{r['ded']['rail']:.2f} "
          f"gf {r['gf']['hwy']:.2f}/{r['gf']['tra']:.2f}/{r['gf']['rail']:.2f} trapped {r['trapped']:.2f} avg {r['gf_pct_avg']:.3%} peak {r['gf_pct_peak']:.3%} ({r['peak_year']}) "
          f"cov {r['ded']['hwy']/r['prog']['hwy']:.0%}/{r['ded']['tra']/r['prog']['tra']:.0%}/{r['ded']['rail']/r['prog']['rail']:.0%}")
    for t in range(2027, 2047):
        a = M.allocate(t, "C", B); room = cap * M.gdp(t) - a["gf_total"]
        cbo = (a["gf_total"] + (M.EXCISE_OFFSET * (M.fund_revenue(t) - M.legacy(t) - M.ev_fee(t)) if t >= 2029 else 0)) / M.gdp(t)
        P(f"FY{t}: prog h/t/r {a['prog']['hwy']:.2f}/{a['prog']['tra']:.2f}/{a['prog']['rail']:.2f} draw {a['gf_pct']:.3%} +1112 {(a['gf_total']+G1112[t])/M.gdp(t):.3%} "
          f"cbo {cbo:.3%} room {room:.2f} room-1112 {room-G1112[t]:.2f} room-1112-res {room-G1112[t]-RESERVE.get(t,0):.2f} trapped {sum(a['trapped'].values()):.2f} "
          f"fund {a['fund']:.2f} ded {a['ded']['hwy']:.2f}/{a['ded']['tra']:.2f}/{a['ded']['rail']:.2f}")
    P("CBO-basis offset FY2032-36", round(sum(M.EXCISE_OFFSET * (M.fund_revenue(t) - M.legacy(t) - M.ev_fee(t)) for t in b5), 2))
    P("fund FY2032-36", round(sum(M.fund_revenue(t) for t in b5), 2), "aviation", round(sum(M.aviation(t) for t in b5), 2), "diesel", round(sum(M.rail_diesel(t) for t in b5), 2))
    P("shares solve", {k: round(v * 100, 1) for k, v in M.solve_incremental_shares(B)[0].items()})
    yrs = range(2042, 2047)
    P("FY42-46 per yr: ded", round(sum(sum(M.allocate(t, 'C', B)['ded'].values()) for t in yrs) / 5, 1),
      "prog", round(sum(M.highway_need(t) + M.transit_program(t, B) + M.rail_program(t) for t in yrs) / 5, 1))
    P("ARCA readiness reserve sched", RESERVE, "1112 FY32-36", round(sum(G1112[t] for t in b5), 2))
    # sec. 310 joint-terminal arithmetic (sec. 109 rule applied to renewal of the four existing terminals)
    t310 = {"Chicago": (9.0, 0.79), "New York Penn/Sunnyside": (4.0, 0.92), "Washington Union": (3.5, 45000 / 61500), "Los Angeles Union": (0.7, 20000 / 22900)}
    s = 0
    for k, (amt, sh) in t310.items():
        P(f"  {k}: ${amt}B x {sh:.1%} = {amt*sh:.2f}"); s += amt * sh
    P("  transit share of existing-terminal work", round(s, 2), "of", sum(v[0] for v in t310.values()),
      "; as share of five-year 5337 SGR + backlog money (28.00 + 31.53):", f"{s/(28.00+31.53):.1%}")
