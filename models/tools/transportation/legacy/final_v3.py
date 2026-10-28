"""Draft 2 governing figures (2026-10-12, late): final_bill program + fossil premium (A-28) + clean cars pegged to 40 mpg
and PHEVs at 30% (A-11). Prints every figure the doc carries."""
import fossil_final as FF, fossil_premium as FP, final_architecture as FA, transit_fiscal_model as M, merge_decisions as D, revenue_plan as R, funding_stack as FS, solvency_paths as S
B=FA.B
P0,P1,alloc=FF.build(FF.PREM)
M.allocate=alloc
yrs=range(2032,2037); cap=M.CAP_ALL_IN
need=lambda m,t,sc=B: M.highway_need(t) if m=="hwy" else M.transit_program(t,sc,kind="R") if m=="tra" else M.rail_program(t)*(1-M.RAIL_EXPANSION_SHARE)
rows=M.period_rows("C",B)
print("PERIODS")
for r in rows:
    a,b=M.PERIODS[r['period']]; ys=range(a,b+1)
    p1112=max((M.allocate(t,"C",B)["gf_total"]+D.G1112[t])/M.gdp(t) for t in ys)
    def cb(t):
        al=M.allocate(t,"C",B); new=P1(t)-M.legacy(t)-(M.ev_fee(t) if t<=2029 else 0)
        return (al["gf_total"]+(M.EXCISE_OFFSET*max(new,0) if t>=2030 else 0))/M.gdp(t)
    print(f" {r['period']}: {r['gf_pct_avg']:.3%}/{r['gf_pct_peak']:.3%}({r['peak_year']}) +1112 {p1112:.3%} cbo {max(cb(t) for t in ys):.3%} cov {'/'.join(f'{r['ded'][k]/r['prog'][k]:.0%}' for k in r['ded'])} | prog {'/'.join(f'{v:.2f}' for v in r['prog'].values())} ded {'/'.join(f'{v:.2f}' for v in r['ded'].values())} gf {'/'.join(f'{v:.2f}' for v in r['gf'].values())} trapped {r['trapped']:.1f}")
for a,b in ((2032,2036),(2037,2041),(2042,2046)):
    print(' rencov',a,'/'.join(f"{sum(M.allocate(t,'C',B)['ded'][m] for t in range(a,b+1))/sum(need(m,t) for t in range(a,b+1)):.0%}" for m in ('hwy','tra','rail')))
print(' self-suff', {m: next((t for t in range(2030,2047) if M.allocate(t,"C",B)["ded"][m]>=need(m,t)), None) for m in ("hwy","tra","rail")})
print(' $/yr 32-36',round(sum(rows[2]['gf'].values())/5,1),'42-46',round(sum(rows[4]['gf'].values())/5,1),'ded/yr42-46',round(sum(rows[4]['ded'].values())/5,1))
print("BY YEAR")
for t in range(2029,2037):
    a=M.allocate(t,"C",B); room=cap*M.gdp(t)-a["gf_total"]
    print(f" {t}: prog {'/'.join(f'{v:.2f}' for v in a['prog'].values())} draw {a['gf_pct']:.3%} room {room:.2f} -1112 {room-D.G1112[t]:.2f} -res {room-D.G1112[t]-D.RESERVE.get(t,0):.2f} allin {(a['gf_total']+D.G1112[t]+D.RESERVE.get(t,0))/M.gdp(t):.3%}")
railX=dict(zip(yrs,[11.6,16.1,19.1,22.25,24.15])); T=[0,0,0,0]; TU={}
print("TOPUPS")
for t in yrs:
    a=M.allocate(t,"C",B); tx=M.transit_program(t,B,kind='X')
    h=a['gf']['hwy']; tr=max(a['gf']['tra']-tx,0); rr=max(a['gf']['rail']-railX[t],0); ex=min(tx,a['gf']['tra'])+railX[t]
    TU[t]=(round(h,2),round(tr,2),round(rr,2)); T=[T[0]+h,T[1]+tr,T[2]+rr,T[3]+ex]
    print(f" {t}: {h:.2f} / {tr:.2f} / {rr:.2f}  exp {ex:.2f}")
print(" totals", [round(x,2) for x in T], "GF", round(sum(T),2))
act29=sum(sum(TU[t]) for t in (2032,2033,2034))+TU[2035][0]+TU[2035][1]; act30=TU[2035][2]+sum(TU[2036])
print(f" 2029 act top-ups {act29:.2f}  2030 act {act30:.2f}")
print("REVENUE BY SOURCE (clean-car column + totals)")
for t in list(range(2029,2037)):
    c=FS.comp(t); cp=P0.cp(t); tot=sum(c.values())-c['cp']+cp
    print(f" {t}: cleancar {cp:.2f} total {tot:.1f}")
for a,b in ((2032,2036),(2037,2041),(2042,2046)):
    ys=range(a,b+1); cp=sum(P0.cp(t) for t in ys); tot=sum(sum(FS.comp(t).values())-FS.comp(t)['cp']+P0.cp(t) for t in ys); pr=sum(P1(t)-P0(t) for t in ys)
    print(f" FY{a}-{b}: cleancar {cp:.1f} total ex prem {tot:.1f} prem {pr:.1f} total {tot+pr:.1f}")
print(" check ded FY32-36", round(sum(sum(M.allocate(t,'C',B)['ded'].values()) for t in yrs),2))
cp29=sum(P0.cp(t) for t in range(2029,2039))
print(f" 2029 act clean-car score {cp29:.1f}; gross {380.4-8.4-14.7+cp29+12.9:.1f} net {(380.4-8.4-14.7+cp29+12.9)*0.75:.1f}")
print("SENS")
for lab,kw in (("3 pauses",dict(steps={y:3 for y in (2030,2031,2033,2034,2036,2037,2039,2040,2041,2042)})),("WD2",dict(wd=2.0)),("steps2",dict(steps={y:2 for y in range(2030,2040)})),("index only",dict(steps={})),("scen C",dict(sc="C: broad eligibility")),("scen A",dict(sc="A: bar kept")),("no premium",dict(prem={})),("25mpg PHEV50",None)):
    if kw is None:
        p0,p1,al=FF.build(FF.PREM,mpg=25.0,ldf=1-0.2*0.5); sc=B
    else:
        sc=kw.pop('sc',B); prem=kw.pop('prem',FF.PREM); p0,p1,al=FF.build(prem,**kw)
    M.allocate=al; rr=M.period_rows("C",sc)
    allin=max((M.allocate(t,"C",sc)["gf_total"]+D.G1112[t]+D.RESERVE.get(t,0))/M.gdp(t) for t in yrs)
    cov=[sum(M.allocate(t,"C",sc)["ded"][m] for t in range(2042,2047))/sum(need(m,t,sc) for t in range(2042,2047)) for m in ("hwy","tra","rail")]
    print(f" {lab}: {rr[2]['gf_pct_avg']:.3%}/{rr[2]['gf_pct_peak']:.3%} allin {allin:.3%} 42-46 {rr[4]['gf_pct_avg']:.3%} cov {'/'.join(f'{c:.0%}' for c in cov)} GF {sum(rr[2]['gf'].values()):.1f}")
M.allocate=alloc
gdp5=sum(M.gdp(t) for t in yrs); GF=sum(rows[2]['gf'].values())
for lab,cut in (("r1",71.55),("r2",132.27),("r3",197.32)): print(" fallback",lab,f"{(GF-cut)/gdp5:.3%}")
print(" share solve", {k:round(v*100,1) for k,v in M.solve_incremental_shares(B)[0].items()})
for t in (2031,2036,2046): print(' rates',t,'clean c/mi',round(P1.rg(t)/40,2),'EV$',round(P1.rg(t)/40*120),'hybrid40$',round(P1.gr(t)*3),'gas25$',round(P1.gr(t)*4.8),'PHEV40%$',round(P1.gr(t)*1.8+0.3*P1.rg(t)/40*120))
