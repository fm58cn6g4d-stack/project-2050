"""Final with fossil transition premium: clean vehicles pay road-use rate; gasoline/diesel pay road-use rate + premium of
2c (2029 $) a year from FY2040, steps stop once no account draws general fund (modelled as steps FY2040-44 = 10c).
Premium receipts credited among accounts in proportion to projected general-fund need (div. A sec. 101(e)(2) new)."""
import fossil_premium as FP, final_architecture as FA, transit_fiscal_model as M, merge_decisions as D, revenue_plan as R
B=FA.B
base_alloc=M.allocate
MPG=40.0; LDF=1-0.20*0.70   # clean cars pegged to a 40-mpg car; PHEVs (assumed 20% of plug-in stock) pay 30%
def build(prem_steps, steps=R.STEPS, wd=3.0, mpg=None, ldf=None):
    mpg=MPG if mpg is None else mpg; ldf=LDF if ldf is None else ldf
    P0=FP.plan3(steps=steps,prem_steps={},wd=wd,mpg=mpg,ld_factor=ldf); P1=FP.plan3(steps=steps,prem_steps=prem_steps,wd=wd,mpg=mpg,ld_factor=ldf)
    def alloc(t,a="C",sc=B,hb="hr8870"):
        M.fund_revenue=P0; r=base_alloc(t,a,sc,hb); pr=max(P1(t)-P0(t),0)
        g=r['gf']; G=sum(g.values()); w={m:(g[m]/G if G>0 else 1/3) for m in g}
        ded={m:r['ded'][m]+pr*w[m] for m in w}; prog=r['prog']
        gf={m:max(prog[m]-ded[m],0) for m in prog}; tr={m:max(ded[m]-prog[m],0) for m in prog}
        r.update(ded=ded,gf=gf,trapped=tr,gf_total=sum(gf.values()),gf_pct=sum(gf.values())/r['gdp'],prem=pr); return r
    return P0,P1,alloc
PREM={y:2 for y in range(2040,2045)}
need=lambda m,t: M.highway_need(t) if m=="hwy" else M.transit_program(t,B,kind="R") if m=="tra" else M.rail_program(t)*(1-M.RAIL_EXPANSION_SHARE)
def show(prem=PREM, steps=R.STEPS, wd=3.0, sc=B, label=""):
    P0,P1,alloc=build(prem,steps,wd); M.allocate=alloc
    rows=M.period_rows("C",sc)
    out={'rows':rows}
    cov42=[sum(M.allocate(t,"C",sc)["ded"][m] for t in range(2042,2047))/sum((M.highway_need(t) if m=="hwy" else M.transit_program(t,sc,kind="R") if m=="tra" else M.rail_program(t)*(1-M.RAIL_EXPANSION_SHARE)) for t in range(2042,2047)) for m in ("hwy","tra","rail")]
    allin=max((M.allocate(t,"C",sc)["gf_total"]+D.G1112[t]+D.RESERVE.get(t,0))/M.gdp(t) for t in range(2032,2037))
    print(f"{label:14}", " ".join(f"{r['period'][2:]} {r['gf_pct_avg']:.3%}/{r['gf_pct_peak']:.3%}({r['peak_year']})" for r in rows[1:]), f"allin {allin:.3%} cov42 {'/'.join(f'{c:.0%}' for c in cov42)} GF32-36 {sum(rows[2]['gf'].values()):.1f}")
    M.allocate=base_alloc; return P0,P1,alloc
if __name__=="__main__":
    P0,P1,alloc=show(label="BASE")
    M.allocate=alloc
    rows=M.period_rows("C",B)
    for r in rows: print(f"  {r['period']}: prog {'/'.join(f'{v:.2f}' for v in r['prog'].values())} ded {'/'.join(f'{v:.2f}' for v in r['ded'].values())} gf {'/'.join(f'{v:.2f}' for v in r['gf'].values())} cov {'/'.join(f'{r['ded'][k]/r['prog'][k]:.0%}' for k in r['ded'])} trapped {r['trapped']:.2f}")
    for name,(a,b) in M.PERIODS.items():
        ys=range(a,b+1); r=[x for x in rows if x['period']==name][0]
        p1112=max((M.allocate(t,"C",B)["gf_total"]+D.G1112[t])/M.gdp(t) for t in ys)
        def cb(t):
            al=M.allocate(t,"C",B); new=P1(t)-M.legacy(t)-(M.ev_fee(t) if t<=2029 else 0)
            return (al["gf_total"]+(M.EXCISE_OFFSET*max(new,0) if t>=2030 else 0))/M.gdp(t)
        print(f"  {name}: {r['gf_pct_avg']:.3%}/{r['gf_pct_peak']:.3%}({r['peak_year']}) +1112 {p1112:.3%} cbo {max(cb(t) for t in ys):.3%}")
    for a,b in ((2032,2036),(2037,2041),(2042,2046)):
        print(' rencov',a,'/'.join(f"{sum(M.allocate(t,'C',B)['ded'][m] for t in range(a,b+1))/sum(need(m,t) for t in range(a,b+1)):.0%}" for m in ('hwy','tra','rail')))
    print(' self-sufficient renewal', {m: next((t for t in range(2030,2047) if M.allocate(t,"C",B)["ded"][m]>=need(m,t)), None) for m in ("hwy","tra","rail")})
    print(' GF by yr', [(t,round(M.allocate(t,'C',B)['gf_total'],1)) for t in range(2037,2047)])
    print(' draw $/yr 32-36',round(sum(rows[2]['gf'].values())/5,1),'37-41',round(sum(rows[3]['gf'].values())/5,1),'42-46',round(sum(rows[4]['gf'].values())/5,1),'ded/yr',round(sum(rows[4]['ded'].values())/5,1),'prog/yr',round(sum(rows[4]['prog'].values())/5,1))
    print(' premium rcpts', {t:round(P1(t)-P0(t),1) for t in range(2040,2047)}, 'sum37-41',round(sum(P1(t)-P0(t) for t in range(2037,2042)),1),'42-46',round(sum(P1(t)-P0(t) for t in range(2042,2047)),1))
    for t in (2031,2036,2040,2044,2046): print('  ',t,'gas',round(P1.gr(t),1),'road',round(P1.rg(t),1),'diesel',round(P1.dr(t),1),'clean c/mi',round(P1.rg(t)/25,2),'car$',round(P1.gr(t)*4.8),'EV$',round(P1.rg(t)/25*120))
    M.allocate=base_alloc
    print("SENS")
    show(prem={y:3 for y in (2041,2042,2043,2044,2045)} if False else PREM, steps={y:3 for y in (2030,2031,2033,2034,2036,2037,2039,2040,2041,2042)}, label="3 pauses")
    show(wd=2.0,label="WD2")
    show(steps={y:2 for y in range(2030,2040)},label="steps2")
    show(steps={},label="index only")
    show(sc="C: broad eligibility",label="scen C")
    show(sc="A: bar kept",label="scen A")
    show(prem={},label="no premium")
