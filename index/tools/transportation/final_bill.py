"""Moving America Act of 2031 -- final bill fiscals (2026-10-12 night), incl. division B redesign.
Division B change: new Interstate and Bridge Renewal formula program (sec. 1104) =
  H.R. 8870's competitive bridge program ($2B/yr GF, subject to appropriation) converted to contract authority, grown 2.5%,
  plus new money 0/2/4/6/8 over FY2032-36, continuing at FY2036 level +2.5%/yr.
Sec. 1112 general-fund grants shrink to multimodal freight ($1.2B) + National Infrastructure Grants ($2B), grown 2.5%.
Readiness reserve illustrated 0/0/5/8/12. Shares 35/50/15 through FY2036, 45/40/15 from FY2037."""
import final_architecture as FA, revenue_plan as R, merge_decisions as D, transit_fiscal_model as M
B=FA.B
BIP=lambda t: 2.0*1.025**(t-2031)
NEW={2032:0,2033:2,2034:4,2035:6,2036:8}
def ibr(t):
    if t<2032: return 0.0
    return BIP(t)+(NEW[t] if t<=2036 else 8*1.025**(t-2036))
_hn=M.highway_need
M.highway_need=lambda t,basis="hr8870": _hn(t,basis)+ibr(t)
for t in list(D.G1112): D.G1112[t]=(3.2*1.025**(t-2031) if t>=2032 else 5.2)
D.RESERVE.clear(); D.RESERVE.update({2032:0,2033:0,2034:5,2035:8,2036:12})
cap=M.CAP_ALL_IN
R.SPLITS["final"]=lambda t:({"hwy":.35,"tra":.50,"rail":.15} if t<2037 else {"hwy":.45,"tra":.40,"rail":.15})
FA.SPL=R.SPLITS["final"]
if __name__=="__main__":
    P=R.plan(); M.fund_revenue=P
    yrs=range(2032,2037)
    print("IBR by year", [round(ibr(t),2) for t in yrs], round(sum(ibr(t) for t in yrs),2), " 1112", [round(D.G1112[t],2) for t in yrs], round(sum(D.G1112[t] for t in yrs),2))
    print("highways by year", [round(M.highway_need(t),2) for t in yrs], round(sum(M.highway_need(t) for t in yrs),2))
    tot=[M.highway_need(t)+M.transit_program(t,B)+M.rail_program(t) for t in yrs]; print("bill by year",[round(x,2) for x in tot], round(sum(tot),2))
    rows=FA.summary(P,"FINAL")
    M.fund_revenue=P
    for r in rows:
        print(f"  {r['period']}: prog {'/'.join(f'{v:.2f}' for v in r['prog'].values())} ded {'/'.join(f'{v:.2f}' for v in r['ded'].values())} gf {'/'.join(f'{v:.2f}' for v in r['gf'].values())} cov {'/'.join(f'{r['ded'][k]/r['prog'][k]:.0%}' for k in r['ded'])}")
    for t in range(2029,2037):
        a=M.allocate(t,"C",B); room=cap*M.gdp(t)-a["gf_total"]
        new=P(t)-M.legacy(t)-(M.ev_fee(t) if t<=2029 else 0)
        cbo=(a["gf_total"]+(M.EXCISE_OFFSET*max(new,0) if t>=2030 else 0))/M.gdp(t)
        print(f"   {t}: draw {a['gf_pct']:.3%} cbo {cbo:.3%} room {room:.2f} -1112 {room-D.G1112[t]:.2f} -res {room-D.G1112[t]-D.RESERVE.get(t,0):.2f} allin {(a['gf_total']+D.G1112[t]+D.RESERVE.get(t,0))/M.gdp(t):.3%}")
    # renewal coverage and stack
    need=lambda m,t: M.highway_need(t) if m=="hwy" else M.transit_program(t,B,kind="R") if m=="tra" else M.rail_program(t)*(1-M.RAIL_EXPANSION_SHARE)
    for a_,b_ in ((2032,2036),(2042,2046)):
        cov=[sum(M.allocate(t,"C",B)["ded"][m] for t in range(a_,b_+1))/sum(need(m,t) for t in range(a_,b_+1)) for m in ("hwy","tra","rail")]
        print(f"  renewal cov FY{a_}-{b_}", "/".join(f"{c:.0%}" for c in cov))
    first={m: next((t for t in range(2030,2047) if M.allocate(t,"C",B)["ded"][m]>=need(m,t)), None) for m in ("hwy","tra","rail")}; print("  self-sufficient from", first)
    railX=dict(zip(yrs,[11.6,16.1,19.1,22.25,24.15])); T=[0,0,0,0]
    print("  top-ups by year hwy/tra/rail, expansion")
    for t in yrs:
        a=M.allocate(t,"C",B); tx=M.transit_program(t,B,kind='X')
        h=a['gf']['hwy']; tr=max(a['gf']['tra']-tx,0); rr=max(a['gf']['rail']-railX[t],0); ex=min(tx,a['gf']['tra'])+railX[t]
        T=[T[0]+h,T[1]+tr,T[2]+rr,T[3]+ex]; print(f"   {t}: {h:.2f} / {tr:.2f} / {rr:.2f}  total {h+tr+rr:.2f}  expansion {ex:.2f}")
    print("  totals", [round(x,2) for x in T], "top-ups", round(sum(T[:3]),2), "FY32-34", round(sum(M.allocate(t,'C',B)['gf']['hwy'] for t in (2032,2033,2034)),2))
    print("  shares solve", {k:round(v*100,1) for k,v in M.solve_incremental_shares(B)[0].items()})
    r=M.period_rows("C",B); print("  draw $/yr FY32-36", round(sum(r[2]['gf'].values())/5,1), "FY42-46", round(sum(r[4]['gf'].values())/5,1), "ded/yr 42-46", round(sum(r[4]['ded'].values())/5,1), "prog/yr", round(sum(r[4]['prog'].values())/5,1))
    print("\nSENS")
    for lab,f,sc in (("3 pauses",R.plan(steps={y:3 for y in (2030,2031,2033,2034,2036,2037,2039,2040,2041,2042)}),B),("WD2",R.plan(wd=2.0),B),
                     ("steps2",R.plan(steps={y:2 for y in range(2030,2040)}),B),("index only",R.plan(steps={}),B),("scen C",P,"C: broad eligibility"),("scen A",P,"A: bar kept")):
        M.fund_revenue=f; rr_=M.period_rows("C",sc)
        allin=max((M.allocate(t,"C",sc)["gf_total"]+D.G1112[t]+D.RESERVE.get(t,0))/M.gdp(t) for t in yrs)
        cov=[sum(M.allocate(t,"C",sc)["ded"][m] for t in range(2042,2047))/sum((M.highway_need(t) if m=="hwy" else M.transit_program(t,sc,kind="R") if m=="tra" else M.rail_program(t)*(1-M.RAIL_EXPANSION_SHARE)) for t in range(2042,2047)) for m in ("hwy","tra","rail")]
        print(f" {lab}: {rr_[2]['gf_pct_avg']:.3%}/{rr_[2]['gf_pct_peak']:.3%} allin {allin:.3%} 42-46 {rr_[4]['gf_pct_avg']:.3%} cov {'/'.join(f'{c:.0%}' for c in cov)} GF {sum(rr_[2]['gf'].values()):.1f}")
    M.fund_revenue=P
    gdp5=sum(M.gdp(t) for t in yrs); GF=sum(M.period_rows("C",B)[2]['gf'].values())
    for lab,cut in (("round1",71.58),("round2",132.27),("round3",197.32)): print(" fallback",lab, f"{(GF-cut)/gdp5:.3%}")

    print("\nPERIOD TABLE")
    M.fund_revenue=P
    for name,(a,b) in M.PERIODS.items():
        ys=range(a,b+1)
        p1112=max((M.allocate(t,"C",B)["gf_total"]+D.G1112[t])/M.gdp(t) for t in ys)
        def cb(t):
            al=M.allocate(t,"C",B); new=P(t)-M.legacy(t)-(M.ev_fee(t) if t<=2029 else 0)
            return (al["gf_total"]+(M.EXCISE_OFFSET*max(new,0) if t>=2030 else 0))/M.gdp(t)
        r=[x for x in M.period_rows("C",B) if x["period"]==name][0]
        print(f" {name}: {r['gf_pct_avg']:.3%}/{r['gf_pct_peak']:.3%}({r['peak_year']}) +1112 {p1112:.3%} cbo-peak {max(cb(t) for t in ys):.3%} cov {'/'.join(f'{r["ded"][k]/r["prog"][k]:.0%}' for k in r['ded'])}")
    print("CANON B rows")
    f=[M.highway_program(t) for t in yrs]; sf=[M.safety_program(t) for t in yrs]; ib=[ibr(t) for t in yrs]
    print(" FHWA", [round(x,3) for x in f]); print(" safety", [round(x,3) for x in sf]); print(" IBR", [round(x,3) for x in ib])
