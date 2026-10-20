"""Moving America Act of 2031 -- final integrated figures (2026-10-12, night).
Base case: merged program (sec. 606 at $3.0B), scenario B, revenue plan (revenue_plan.plan), shares 35/50/15 to FY2036
then 40/45/15, reconciliation obligations rail 6/17/25.5 and transit 4/13/15 over FY2029-31, sec. 1112 and reserve as overlays."""
import revenue_plan as R, solvency_paths as S, solvency_final as F, transit_fiscal_model as M, merge_decisions as D
B="B: conditional tier"
F.recon({2029:6.0,2030:17.0,2031:25.5},{2029:4.0,2030:13.0,2031:15.0})
SPL=R.SPLITS["35/50/15 -> 40/45/15 FY37"]
_alloc=M.allocate
def alloc(t,a="C",sc=B,hb="hr8870"):
    M.INCR_SHARES.update(SPL(t)); return _alloc(t,a,sc,hb)
M.allocate=alloc
cap=M.CAP_ALL_IN
def summary(fund,label,sc=B):
    M.fund_revenue=fund
    rows=M.period_rows("C",sc)
    allin=max((M.allocate(t,"C",sc)["gf_total"]+D.G1112[t]+D.RESERVE.get(t,0))/M.gdp(t) for t in range(2032,2037))
    p1112=max((M.allocate(t,"C",sc)["gf_total"]+D.G1112[t])/M.gdp(t) for t in range(2032,2037))
    out=f"{label:<28}"+" ".join(f"{r['period'][2:]} {r['gf_pct_avg']:.3%}/{r['gf_pct_peak']:.3%}({r['peak_year']})" for r in rows)
    out+=f" | +1112 {p1112:.3%} all-in {allin:.3%} | GF32-36 {sum(rows[2]['gf'].values()):.1f}"
    print(out); return rows
if __name__=="__main__":
    P=R.plan()
    rows=summary(P,"BASE")
    M.fund_revenue=P
    for r in rows:
        print(f"  {r['period']}: prog {'/'.join(f'{v:.2f}' for v in r['prog'].values())} ded {'/'.join(f'{v:.2f}' for v in r['ded'].values())} gf {'/'.join(f'{v:.2f}' for v in r['gf'].values())} cov {'/'.join(f'{r['ded'][k]/r['prog'][k]:.0%}' for k in r['ded'])} trapped {r['trapped']:.2f}")
    print("  FY by year: draw / CBO-basis / room / room-1112 / room-1112-reserve")
    for t in range(2027,2047):
        a=M.allocate(t,"C",B); room=cap*M.gdp(t)-a["gf_total"]
        new=P(t)-M.legacy(t)-(M.ev_fee(t) if t<=2029 else 0)
        cbo=(a["gf_total"]+(M.EXCISE_OFFSET*max(new,0) if t>=2030 else 0))/M.gdp(t)
        print(f"   {t}: prog {a['prog']['hwy']:.2f}/{a['prog']['tra']:.2f}/{a['prog']['rail']:.2f} draw {a['gf_pct']:.3%} cbo {cbo:.3%} room {room:.2f} {room-D.G1112[t]:.2f} {room-D.G1112[t]-D.RESERVE.get(t,0):.2f}")
    print("  CBO offset FY2032-36", round(sum(M.EXCISE_OFFSET*(P(t)-M.legacy(t)) for t in range(2032,2037)),1))
    print("  FY2042-46 per yr ded", round(sum(sum(M.allocate(t,'C',B)['ded'].values()) for t in range(2042,2047))/5,1), "prog", round(sum(M.highway_need(t)+M.transit_program(t,B)+M.rail_program(t) for t in range(2042,2047))/5,1))
    print("  draw $/yr FY2032-36", round(sum(rows[2]['gf'].values())/5,1), "FY2042-46", round(sum(rows[4]['gf'].values())/5,1))
    print("\nSENSITIVITIES")
    summary(R.plan(steps={y:3 for y in (2030,2031,2033,2034,2036,2037,2039,2040,2041,2042)}),"3 pauses (deferred)")
    summary(R.plan(wd=2.0),"weight-distance 2c avg")
    summary(R.plan(steps={}),"indexing only, no steps")
    summary(R.plan(steps={y:2 for y in range(2030,2040)}),"steps 2c not 3c")
    summary(P,"scenario C",sc="C: broad eligibility")
    summary(P,"scenario A",sc="A: bar kept")
    old=M.PER_MILE_ADMIN
    # fallback rounds: cut GF dollar for dollar
    gdp5=sum(M.gdp(t) for t in range(2032,2037)); M.fund_revenue=P
    GF=sum(M.period_rows("C",B)[2]['gf'].values())
    for lab,cut in (("bill",0),("round1",71.58),("round2",132.27),("round3",197.32)):
        print(f"  fallback {lab}: GF {GF-cut:.1f} draw avg {(GF-cut)/gdp5:.3%}")
    print("  highway option -30.97 -> -", f"{30.97/gdp5:.3%}")
    print("\nshares solve (FY2042-46)", {k:round(v*100,1) for k,v in M.solve_incremental_shares(B)[0].items()})
