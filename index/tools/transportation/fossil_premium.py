"""Fossil transition premium (2026-10-12, late). Clean vehicles pay the ROAD-USE rate (base + Fix-It-First steps, CPI-indexed)
per mile at 25 mpg / 6.5 mpg; gasoline and diesel pay road-use rate + a fossil transition premium of 2 cents a year (2029 $)
from FY2040, ten steps, same price pause. Premium is not passed to clean vehicles. Everything else as final_bill."""
import final_bill as FB, final_architecture as FA, revenue_plan as R, transit_fiscal_model as M, merge_decisions as D, solvency_paths as S
B=FA.B
def plan3(steps=R.STEPS, prem_steps=None, wd=3.0, wd_from=2031, clean_from=2031, index_from=2030, ev_to=2030, mpg=25.0, hmpg=6.5, ld_factor=1.0):
    prem_steps = {y:2 for y in range(2040,2050)} if prem_steps is None else prem_steps
    cum=lambda t: sum(v for y,v in steps.items() if y<=t)
    pc=lambda t: sum(v for y,v in prem_steps.items() if y<=t)
    idx=lambda t: 1.0 if t<index_from else 1.025**(t-index_from+1)
    rg=lambda t:(18.4+cum(t))*idx(t); rd=lambda t:(24.4+cum(t))*idx(t)          # road-use rates
    gr=lambda t:(18.4+cum(t)+pc(t))*idx(t); dr=lambda t:(24.4+cum(t)+pc(t))*idx(t)  # fuel rates incl premium
    def fund(t):
        if t<2029: return M.legacy(t)
        leg=M.legacy(t)*0.85
        gas=leg*0.65*gr(t)/18.4; dsl=leg*0.35*dr(t)/24.4*(1-S.heavy_clean(t))
        other=M.legacy(t)*0.15*M.infl(t,2028) - 6.5*M.infl(t,2028)*S.heavy_sales(t)*8/12
        other-= (0 if t<wd_from else 1.3*M.infl(t,2028))
        ev=M.ev_fee(t) if t<=ev_to else 0.0
        cp=0 if t<clean_from else S._lerp(t)*11000*0.9*rg(t)/mpg/1e5*0.9*ld_factor
        ch=0 if t<clean_from else S.HEAVY_VMT(t)*S.heavy_clean(t)*rd(t)/hmpg/100*0.9
        w=0 if t<wd_from else S.HEAVY_VMT(t)*0.7*wd*1.03**(t-wd_from)/100*0.95
        return gas+dsl+other+ev+cp+ch+w
    fund.gr,fund.dr,fund.rg,fund.rd=gr,dr,rg,rd
    fund.cp=lambda t: 0 if t<clean_from else S._lerp(t)*11000*0.9*rg(t)/mpg/1e5*0.9*ld_factor
    return fund
def report(P,label):
    M.fund_revenue=P
    rows=FA.summary(P,label)
    need=lambda m,t: M.highway_need(t) if m=="hwy" else M.transit_program(t,B,kind="R") if m=="tra" else M.rail_program(t)*(1-M.RAIL_EXPANSION_SHARE)
    for r in rows: print(f"  {r['period']}: ded {'/'.join(f'{v:.2f}' for v in r['ded'].values())} gf {'/'.join(f'{v:.2f}' for v in r['gf'].values())} cov {'/'.join(f'{r['ded'][k]/r['prog'][k]:.0%}' for k in r['ded'])} trapped {r['trapped']:.1f}")
    for a,b in ((2037,2041),(2042,2046)):
        cov=[sum(M.allocate(t,"C",B)["ded"][m] for t in range(a,b+1))/sum(need(m,t) for t in range(a,b+1)) for m in ("hwy","tra","rail")]
        print(f"  renewal cov FY{a}-{b}", "/".join(f"{c:.0%}" for c in cov))
    first={m: next((t for t in range(2030,2047) if M.allocate(t,"C",B)["ded"][m]>=need(m,t)), None) for m in ("hwy","tra","rail")}; print("  self-sufficient", first)
    r=M.period_rows("C",B); print("  draw $/yr 32-36",round(sum(r[2]['gf'].values())/5,1),"42-46",round(sum(r[4]['gf'].values())/5,1),"ded/yr 42-46",round(sum(r[4]['ded'].values())/5,1))
    print("  shares solve", {k:round(v*100,1) for k,v in M.solve_incremental_shares(B)[0].items()})
    for t in (2036,2039,2040,2042,2046,2049): print("   ",t,"gas",round(P.gr(t),1),"road",round(P.rg(t),1),"clean c/mi",round(P.rg(t)/25,2),"25mpg car $",round(P.gr(t)*4.8))
if __name__=="__main__":
    report(plan3(prem_steps={}),"NO PREMIUM (check = final)")
    report(plan3(),"PREMIUM 2c x10 from FY2040")
