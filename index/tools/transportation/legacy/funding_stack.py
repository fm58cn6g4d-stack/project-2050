"""Funding stack by legal instrument (2026-10-12). Separates trust-fund receipts, general-fund transfers INTO the fund
(barred in reconciliation), and general-fund appropriations TO programs (reconciliation-eligible), and scores each
reconciliation act's new revenue against CBO's baseline convention (expiring trust-fund excises assumed extended)."""
import revenue_plan as R, solvency_paths as S, solvency_final as F, transit_fiscal_model as M, merge_decisions as D
B="B: conditional tier"
F.recon({2029:6.0,2030:17.0,2031:25.5},{2029:4.0,2030:13.0,2031:15.0})
P=R.plan(); M.fund_revenue=P
SPL=R.SPLITS["35/50/15 -> 40/45/15 FY37"]
_alloc=M.allocate
def alloc(t,a="C",sc=B,hb="hr8870"):
    M.INCR_SHARES.update(SPL(t)); return _alloc(t,a,sc,hb)
leg=lambda t:M.legacy(t)
def comp(t):
    L=leg(t)*0.85
    gas=L*0.65*P.gr(t)/18.4 if t>=2029 else L*0.65
    dsl=L*0.35*P.dr(t)/24.4*(1-S.heavy_clean(t)) if t>=2029 else L*0.35
    other=(leg(t)*0.15*M.infl(t,2028)-6.5*M.infl(t,2028)*S.heavy_sales(t)*8/12-(1.3*M.infl(t,2028) if t>=2031 else 0)) if t>=2029 else leg(t)*0.15
    ev=M.ev_fee(t) if 2029<t<=2030 else 0.0   # FY2029: fee still goes to general fund under 250-Plus
    cp=S._lerp(t)*11000*0.9*P.gr(t)/25/1e5*0.9 if t>=2031 else 0
    ch=S.HEAVY_VMT(t)*S.heavy_clean(t)*P.dr(t)/6.5/100*0.9 if t>=2031 else 0
    wd=S.HEAVY_VMT(t)*0.7*3*1.03**(t-2031)/100*0.95 if t>=2031 else 0
    rail=M.aviation(t)+M.rail_diesel(t)
    return dict(gas=gas,dsl=dsl,other=other,ev=ev,cp=cp,ch=ch,wd=wd,rail=rail)
def show_revenue():
    cols=["gas","dsl","other","ev","cp","ch","wd","rail"]
    print("FY | gasoline | diesel | other TF taxes | EV fee | clean-car per-mile | clean-truck per-mile | weight-distance | rail acct (aviation+rail diesel) | total dedicated")
    tot={}
    for t in range(2029,2037):
        c=comp(t); s=sum(c.values()); tot[t]=s
        print(t, " | ".join(f"{c[k]:.1f}" for k in cols), f"| {s:.1f}  [model fund {P(t)+0:.1f} + rail {c['rail']:.1f}; diff {s-(P(t)+c['rail']):.2f}]")
    for a,b in ((2032,2036),(2037,2041),(2042,2046)):
        cs={k:sum(comp(t)[k] for t in range(a,b+1)) for k in cols}
        print(f"FY{a}-{str(b)[2:]}", " | ".join(f"{cs[k]:.1f}" for k in cols), f"| {sum(cs.values()):.1f}")
def scored(t):
    """New revenue vs CBO baseline (expiring HTF taxes assumed extended at current rates; EV fee in baseline to FY2036 as GF)."""
    c=comp(t); base_fuel=leg(t)*0.85; base_other=leg(t)*0.15
    fuel=c["gas"]+c["dsl"]-base_fuel
    other=c["other"]-base_other*M.infl(t,2028)  # FET cut and HVUT repeal (inflation drift in 'other' netted out)
    ev_loss=-M.ev_fee(t) if 2031<=t<=2036 else 0.0
    return dict(fuel=fuel, other=other, ev=ev_loss, cp=c["cp"], ch=c["ch"], wd=c["wd"], rail=c["rail"])
def show_scores():
    for act,yrs,keys in (("2029 act (window FY2029-38)",range(2029,2039),["fuel","other","ev","cp","ch"]),
                         ("2030 act (window FY2030-39)",range(2030,2040),["wd","rail"])):
        g={k:sum(scored(t)[k] for t in yrs) for k in keys}; gross=sum(g.values())
        print(act, {k:round(v,1) for k,v in g.items()}, f"gross {gross:.1f}, net of 25% offset {gross*0.75:.1f}")
def show_stack():
    print("\nFY | program h/t/r | dedicated h/t/r | GF need h/t/r | of which reconciliation approps (rail, transit) | trust-fund gap on fund-financed programs (hwy need + transit CA - TF receipts)")
    for t in range(2029,2032):
        a=alloc(t); rr=M.RAIL_RECON.get(t,0); tr=sum(v for n,k,y,v in M.TRANSIT_RECON if y==t)
        gap=(M.highway_need(t)+M.HR8870_CA[t])-(a['ded']['hwy']+a['ded']['tra'])
        print(t, "/".join(f"{a['prog'][m]:.1f}" for m in a['prog']), "|", "/".join(f"{a['ded'][m]:.1f}" for m in a['ded']), "|",
              "/".join(f"{a['gf'][m]:.1f}" for m in a['gf']), f"| {rr:.1f}, {tr:.1f} | {gap:.1f}", f"| rail acct receipts unspent {a['ded']['rail']:.1f}")
    railX=dict(zip(range(2032,2037),[11.6,16.1,19.1,22.25,24.15]))
    print("\nFY | dedicated h/t/r | GF expansion (transit CIG+606, rail 303/310/311/312) | GF renewal supplement h/t/r | total GF")
    T={k:0 for k in ("exp","h","t","r")}
    for t in range(2032,2037):
        a=alloc(t); tx=M.transit_program(t,B,kind='X')
        trx=min(tx,a['gf']['tra']); trr=max(a['gf']['tra']-tx,0); rx=railX[t]; rrn=max(a['gf']['rail']-rx,0)
        exp=trx+min(rx,a['gf']['rail']); T["exp"]+=exp; T["h"]+=a['gf']['hwy']; T["t"]+=trr; T["r"]+=rrn
        print(t, "/".join(f"{a['ded'][m]:.1f}" for m in a['ded']), f"| {exp:.2f} ({trx:.2f} + {rx:.2f}) | {a['gf']['hwy']:.2f}/{trr:.2f}/{rrn:.2f} | {a['gf_total']:.1f}  draw {a['gf_pct']:.3%}")
    print("totals: expansion", round(T['exp'],2), "renewal supplements", round(T['h'],2), round(T['t'],2), round(T['r'],2), "=", round(T['h']+T['t']+T['r'],2), "GF", round(T['exp']+T['h']+T['t']+T['r'],2))
if __name__=="__main__":
    show_revenue(); print(); show_scores(); show_stack()
