"""Revenue plan across three vehicles (2026-10-12). Realistic effective dates:
 - FY2029 (Oct 2028-Sep 2029): current-law rates, assumed carried by a clean 2028 extension (A-1 dependency)
 - 2029 reconciliation, effective Oct 1, 2029 (FY2030): permanence, CPI indexing, Fix-It-First step 1 of 10,
   EV fee redirected to the fund as a bridge, clean-truck FET at 4%, per-mile machinery authorized
 - Oct 1, 2030 (FY2031): clean-vehicle per-mile (parity) and weight-distance charge (all trucks >26,000 lb,
   clean trucks included) go live; EV fee and HVUT end.  Rates for weight-distance set in the 2030 package.
Shares tested: 35/50/15, 40/45/15, 45/41/14, and 35/50/15 -> 40/45/15 at FY2037."""
import solvency_paths as S, solvency_final as F, transit_fiscal_model as M, merge_decisions as D
B="B: conditional tier"
STEPS={y:3 for y in range(2030,2040)}
def plan(steps=STEPS, wd=3.0, wd_from=2031, clean_from=2031, index_from=2030, ev_to=2030, mpg=25.0, hmpg=6.5):
    cum=lambda t: sum(v for y,v in steps.items() if y<=t)
    idx=lambda t: 1.0 if t<index_from else 1.025**(t-index_from+1)
    gr=lambda t:(18.4+cum(t))*idx(t); dr=lambda t:(24.4+cum(t))*idx(t)
    def fund(t):
        if t<2029: return M.legacy(t)
        leg=M.legacy(t)*0.85
        gas=leg*0.65*gr(t)/18.4; dsl=leg*0.35*dr(t)/24.4*(1-S.heavy_clean(t))
        hvut=1.3*M.infl(t,2028) if t<wd_from else 0.0                         # (A) HVUT ~$1.3B, ends when WD starts
        other=M.legacy(t)*0.15*M.infl(t,2028)-hvut*0 - 6.5*M.infl(t,2028)*S.heavy_sales(t)*8/12
        other-= (0 if t<wd_from else 1.3*M.infl(t,2028))                     # HVUT repealed
        ev=M.ev_fee(t) if t<=ev_to else 0.0
        cp=0 if t<clean_from else S._lerp(t)*11000*0.9*gr(t)/mpg/1e5*0.9
        ch=0 if t<clean_from else S.HEAVY_VMT(t)*S.heavy_clean(t)*dr(t)/hmpg/100*0.9
        w=0 if t<wd_from else S.HEAVY_VMT(t)*0.7*wd*1.03**(t-wd_from)/100*0.95   # all trucks >26,000 lb incl. clean
        return gas+dsl+other+ev+cp+ch+w
    fund.gr, fund.dr = gr, dr
    return fund
def run(fund, shares_fn, label):
    M.fund_revenue=fund
    orig=M.allocate
    def alloc(t,arch,sc,hb="hr8870"):
        M.INCR_SHARES.update(shares_fn(t)); return orig(t,arch,sc,hb)
    M.allocate=alloc
    rows=M.period_rows("C",B)
    yrs=range(2042,2047)
    need=lambda m,t: M.highway_need(t) if m=="hwy" else M.transit_program(t,B,kind="R") if m=="tra" else M.rail_program(t)*(1-M.RAIL_EXPANSION_SHARE)
    cov={m: sum(M.allocate(t,"C",B)["ded"][m] for t in yrs)/sum(need(m,t) for t in yrs) for m in ("hwy","tra","rail")}
    first={m: next((t for t in range(2030,2047) if M.allocate(t,"C",B)["ded"][m]>=need(m,t)), None) for m in cov}
    trapped=sum(r["trapped"] for r in rows)
    allin=max((M.allocate(t,"C",B)["gf_total"]+D.G1112[t]+D.RESERVE.get(t,0))/M.gdp(t) for t in range(2032,2037))
    gf3236=sum(rows[2]["gf"].values())
    print(f"{label:<34} " + " ".join(f"{r['period'][2:]} {r['gf_pct_avg']:.3%}/{r['gf_pct_peak']:.3%}" for r in rows[1:]) +
          f" | all-in {allin:.3%} | GF32-36 {gf3236:.1f} | trapped {trapped:.1f} | renewal cov 42-46 " + "/".join(f"{v:.0%}" for v in cov.values()) +
          " | self-sufficient " + "/".join(str(v) for v in first.values()))
    M.allocate=orig; M.INCR_SHARES.update({"hwy":.35,"tra":.50,"rail":.15}); M.fund_revenue=S.CURRENT
    return rows
SPLITS={"35/50/15":lambda t:{"hwy":.35,"tra":.50,"rail":.15},
        "40/45/15":lambda t:{"hwy":.40,"tra":.45,"rail":.15},
        "45/41/14":lambda t:{"hwy":.45,"tra":.41,"rail":.14},
        "35/50/15 -> 40/45/15 FY37":lambda t:({"hwy":.35,"tra":.50,"rail":.15} if t<2037 else {"hwy":.40,"tra":.45,"rail":.15})}
if __name__=="__main__":
    F.recon({2029:6.0,2030:17.0,2031:25.5},{2029:4.0,2030:13.0,2031:15.0})   # FY2029 obligations small: enactment mid-year
    P=plan()
    print("current design (same recon schedule)"); run(S.CURRENT, SPLITS["35/50/15"], "current design 35/50/15")
    for k,fn in SPLITS.items(): run(P, fn, "plan "+k)
    print("breaker skips 3 of 10:"); run(plan(steps={y:3 for y in (2030,2031,2033,2034,2036,2037,2039)}), SPLITS["35/50/15 -> 40/45/15 FY37"], "plan, 3 skips, glide split")
    print("WD at 2c:"); run(plan(wd=2.0), SPLITS["35/50/15 -> 40/45/15 FY37"], "plan WD2, glide split")
    M.fund_revenue=P
    print("\nFY  fund   gas_c  dsl_c  EVpm_c/mi  truckWD  25mpg driver $/yr")
    for t in (2029,2030,2031,2032,2034,2036,2039,2041,2046):
        print(t, round(P(t),1), round(P.gr(t),1), round(P.dr(t),1), round(P.gr(t)/25,2) if t>=2031 else "-", 
              round(S.HEAVY_VMT(t)*0.7*3*1.03**(t-2031)/100*0.95,1) if t>=2031 else "-", round(4.8*P.gr(t)))
    M.fund_revenue=S.CURRENT
    comp=lambda f,t:f(t)
    print("fund FY2030-36 plan", round(sum(P(t) for t in range(2030,2037)),1), "current", round(sum(S.CURRENT(t) for t in range(2030,2037)),1))
    # components FY2032-36
    import math
