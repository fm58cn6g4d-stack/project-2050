import solvency_paths as S, transit_fiscal_model as M, merge_decisions as D
B="B: conditional tier"
def make2(index_from=2029, steps=None, wd=None, parity=True, ev_to=2029, clean_from=2030, mpg=25.0, hmpg=6.5):
    steps=steps or {}
    cum=lambda t: sum(v for y,v in steps.items() if y<=t)
    idx=lambda t: 1.0 if index_from is None or t<index_from else 1.025**(t-index_from+1)
    gr=lambda t:(18.4+cum(t))*idx(t); dr=lambda t:(24.4+cum(t))*idx(t)
    def fund(t):
        if t<2029: return M.legacy(t)
        leg=M.legacy(t)*0.85
        gas=leg*0.65*gr(t)/18.4; dsl=leg*0.35*dr(t)/24.4*(1-S.heavy_clean(t))
        other=M.legacy(t)*0.15*M.infl(t,2028)-6.5*M.infl(t,2028)*S.heavy_sales(t)*8/12
        ev=M.ev_fee(t) if t<=ev_to else 0
        prate=gr(t)/mpg if parity else 1.5*1.03**(t-clean_from)
        hrate=dr(t)/hmpg if parity else 8.5*1.03**(t-clean_from)
        cp=0 if t<clean_from else S._lerp(t)*11000*0.9*prate/1e5*0.9
        ch=0 if t<clean_from else S.HEAVY_VMT(t)*S.heavy_clean(t)*hrate/100*0.9
        w=0 if not wd or t<wd[0] else S.HEAVY_VMT(t)*0.7*(1-S.heavy_clean(t))*wd[1]*1.03**(t-wd[0])/100*0.95
        return gas+dsl+other+ev+cp+ch+w
    fund.gr=gr; return fund
if __name__=="__main__":
    S.report("0 current design", S.CURRENT)
    S.report("v2 +10/15/20 (parity EV rates)", make2(index_from=2032, steps={2029:10,2030:5,2031:5}))
    for wdr in (2.0,3.0):
      for start,sz in ((2030,2),(2030,3),(2032,3),(2030,4)):
        st={y:sz for y in range(start,start+10)}
        S.report(f"idx29 parity WD{wdr} +{sz}c/yr {start}-{start+9}", make2(steps=st, wd=(2030,wdr)))
    f=make2(steps={y:3 for y in range(2030,2040)}, wd=(2030,3.0))
    print("gas rate cents", {t:round(f.gr(t),1) for t in (2029,2030,2031,2032,2036,2039,2041,2046)})
    print("EV parity c/mi", {t:round(f.gr(t)/25,2) for t in (2030,2036,2046)})
