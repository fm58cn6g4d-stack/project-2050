"""Recommended path ('R') vs alternatives -- 2026-10-12. Builds on solvency_paths.py / solvency_grid.py.
Adds ICE fuel-economy gains of 1%/yr after FY2036 (conservative)."""
import solvency_paths as S, solvency_grid as G, transit_fiscal_model as M, merge_decisions as D
B="B: conditional tier"
_gv=S.gas_volume
S.gas_volume=lambda t: _gv(t)*(0.99**max(t-2036,0))
M.legacy=lambda t,acct="both": S._leg(t,acct)*(1-0.85*0.65*(1-S.gas_volume(t)))
def recon(rail,tra):
    M.RAIL_RECON.clear(); M.RAIL_RECON.update(rail)
    base=getattr(recon,"base",None) or list(M.TRANSIT_RECON); recon.base=base
    ys={y:sum(v for n,k,yy,v in base if yy==y) for y in (2029,2030,2031)}
    M.TRANSIT_RECON[:]=[(n,k,y,v*tra[y]/ys[y]) for n,k,y,v in base]
A8=({2029:16.0,2030:16.0,2031:16.5},{2029:10,2030:11,2031:11})
BACK=({2029:9.0,2030:17.0,2031:22.5},{2029:6,2030:12,2031:14})
def yrs(f,label):
    M.fund_revenue=f
    print(f"  {label}: "+" ".join(f"{t}:{M.allocate(t,'C',B)['gf_pct']:.3%}" for t in (2029,2030,2031)))
    M.fund_revenue=S.CURRENT
R  = G.make2(steps={y:3 for y in range(2030,2040)}, wd=(2030,3.0))
R29= G.make2(steps={y:3 for y in range(2029,2039)}, wd=(2030,3.0))
if __name__=="__main__":
    for lab,(rl,tr) in (("A-8 schedule",A8),("back-loaded",BACK)):
        recon(rl,tr); print(lab)
        yrs(S.CURRENT,"current design"); yrs(R,"R, steps from FY2030"); yrs(R29,"R, steps from FY2029")
    recon(*BACK)
    for k,f in (("current design",S.CURRENT),("R (back-loaded recon)",R),("R29 (back-loaded recon)",R29)):
        S.report(k,f)
    M.fund_revenue=R
    for t in (2030,2032,2036,2041,2046):
        a=M.allocate(t,"C",B); print(t, "fund",round(a['fund'],1),"cars-gas",round(S.M.legacy(t)*.85*.65*R.gr(t)/18.4,1),"WD",)
    M.fund_revenue=S.CURRENT

R29B = G.make2(steps={y:3 for y in (2029,2030,2032,2033,2035,2036,2038)}, wd=(2030,3.0))   # 3 of 10 steps skipped
def detail():
    recon(*BACK)
    M.fund_revenue=R29
    sh,_=M.solve_incremental_shares(B); print("share solve", {k:round(v*100,1) for k,v in sh.items()})
    old=dict(M.INCR_SHARES); M.INCR_SHARES.update({"hwy":0.45,"tra":0.41,"rail":0.14})
    r=M.period_rows("C",B)
    for x in r[1:]:
        print(x['period'], f"avg {x['gf_pct_avg']:.3%} peak {x['gf_pct_peak']:.3%}({x['peak_year']}) fund {x['fund']:.1f} ded {sum(x['ded'].values()):.1f} gf {sum(x['gf'].values()):.1f}",
              "cov "+"/".join(f"{x['ded'][k]/x['prog'][k]:.0%}" for k in x['ded']))
    for m in ("hwy","tra","rail"):
        need=lambda t:(M.highway_need(t) if m=="hwy" else M.transit_program(t,B,kind="R") if m=="tra" else M.rail_program(t)*(1-M.RAIL_EXPANSION_SHARE))
        ok=[t for t in range(2032,2047) if M.allocate(t,"C",B)["ded"][m]>=need(t)]; print(" renewal self-sufficient", m, ok[:1])
    allin=max((M.allocate(t,"C",B)["gf_total"]+D.G1112[t]+D.RESERVE.get(t,0))/M.gdp(t) for t in range(2032,2037)); print(" all-in peak", f"{allin:.3%}")
    M.fund_revenue=S.CURRENT; S.report("R29 shares 45/41/14", R29); S.report("R29 breaker skips 3", R29B); M.INCR_SHARES.update(old)
    for t in (2029,2031,2033,2036,2038,2041,2046):
        g=R29.gr(t); print(t, f"gas {g:.1f}c nominal, {g/1.025**(t-2029):.1f}c in 2029$, 25-mpg/12k-mi driver ${4.8*g:.0f}/yr (+${4.8*(g-18.4):.0f})  EV parity {g/25:.2f}c/mi")
    print("1993 rate in 2029$:", round(18.4*322/144.5*1.025**4,1))
if __name__=="__main__": detail()
