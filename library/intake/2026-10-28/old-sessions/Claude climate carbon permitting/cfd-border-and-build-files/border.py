import openpyxl,warnings,csv,json
warnings.filterwarnings('ignore')
U='/root/.claude/uploads/52892800-2b3a-5905-b5b4-99fea95347c9/'
def table(f,sheet,hdr_code_row_has):
    ws=openpyxl.load_workbook(U+f,read_only=True,data_only=True)[sheet]
    rows=[list(r) for r in ws.iter_rows(values_only=True)]
    hi=next(i for i,r in enumerate(rows) if any(str(c).strip()==hdr_code_row_has for c in r))
    codes=[str(c).strip() if c is not None else '' for c in rows[hi]]
    out={}
    for r in rows[hi+1:]:
        if r[0] is None: continue
        out[str(r[0]).strip()]={'name':r[1],**{codes[j]:(v if isinstance(v,(int,float)) else 0) for j,v in enumerate(r) if j>1 and codes[j]}}
    return out
num=lambda v:v if isinstance(v,(int,float)) else 0
sS=table('611f02bf-Supply_Summary.xlsx','2022','MCIF'); uS=table('c5c566f6-Use_Summary.xlsx','2022','F040')
sS17=table('611f02bf-Supply_Summary.xlsx','2017','MCIF'); uS17=table('c5c566f6-Use_Summary.xlsx','2017','F040')
sD=table('daf90c20-Supply_Detail.xlsx','2017','MCIF'); uD=table('81be31c1-Use_SUT_Detail.xlsx','2017','F04000')
# import factors, summary, kg CO2e per USD (GWP100, AR5 as EPA uses)
GWP={'Carbon dioxide':1,'Methane':28,'Nitrous oxide':265,'HFCs and PFCs, unspecified':1,'Sulfur hexafluoride':23500,'Nitrogen trifluoride':16100,'Carbon tetrafluoride':6630,'Hexafluoroethane':11100,'HFC-134a':1300,'HFC-125':3170,'HFC-143a':4800,'HFC-23':12400,'HFC-32':677,'HFC-236fa':8060,'Perfluoropropane':8900,'Perfluorobutane':9200,'Perfluorocyclobutane':9540,'Perfluorohexane':7910}
ief={}
for r in csv.DictReader(open(U+'fc22b06b-US_summary_import_factors_gloria_2022_17sch.csv')):
    if r['Flowable'] in GWP: ief[r['Sector']]=ief.get(r['Sector'],0)+float(r['FlowAmount'])*GWP[r['Flowable']]
# US factors by BEA detail code (kg CO2e per 2022 USD, without margins)
usf={}
for r in csv.DictReader(open(U+'676e525f-SupplyChainGHGEmissionFactors_v1.3.0_NAICS_CO2e_USD2022.csv')):
    usf.setdefault(r['Reference USEEIO Code'],float(r['Supply Chain Emission Factors without Margins']))
covered={'331110':'Iron and steel mills','331200':'Steel products from purchased steel','331313':'Alumina and primary aluminum','33131B':'Aluminum products',
 '327310':'Cement','327400':'Lime and gypsum','327200':'Glass','325310':'Fertilizer','325110':'Petrochemicals','325180':'Other basic inorganic chemicals','325190':'Other basic organic chemicals',
 '325211':'Plastics and resins','322110':'Pulp','322120':'Paper','322130':'Paperboard','324110':'Refined petroleum products'}
summ={'331':'331','327':'327','325':'325','322':'322','324':'324'}
out=[];
# ratio of foreign to U.S. intensity by summary sector: EPA import factor over the U.S. factor weighted by what is imported; capped at 2
def sumsec(code): return code[:3]
secw={}
for c,v in sD.items():
    k=sumsec(c)
    if k in summ and c in usf:
        q=num(v.get('MCIF',0)); secw.setdefault(k,[0,0]); secw[k][0]+=q*usf[c]; secw[k][1]+=q
usavg={k:a/b for k,(a,b) in secw.items()}
raw={k:ief[k]/usavg[k] for k in summ}
print('raw foreign/US ratio (EPA import factor, summary sector, per dollar) - shown for reference only',{k:round(v,2) for k,v in raw.items()})
# ASSUMED foreign-to-U.S. intensity ratio by product (low, central, high). Judgment, not measurement:
#   products whose emissions are fixed by chemistry or by a similar process everywhere sit near 1;
#   steel is higher because U.S. mills are mostly electric-arc and many suppliers are blast-furnace;
#   primary aluminum and paper can be BELOW 1 because Canada, on hydropower, is the main supplier.
RATIO={'331110':(1.1,1.5,2.0),'331200':(1.1,1.4,1.9),'331313':(0.6,0.9,1.4),'33131B':(0.9,1.2,1.7),
 '327310':(0.95,1.1,1.3),'327400':(0.95,1.1,1.3),'327200':(1.0,1.2,1.5),'325310':(1.0,1.3,1.7),'325110':(1.0,1.2,1.6),
 '325180':(1.0,1.3,1.7),'325190':(1.0,1.3,1.7),'325211':(1.0,1.3,1.7),'322110':(0.8,1.0,1.4),'322120':(0.8,1.0,1.4),'322130':(0.8,1.0,1.4),'324110':(0.95,1.1,1.3)}
for c,nm in covered.items():
    k=sumsec(c); imp17=num(sD[c].get('MCIF',0)); exp17=num(uD[c].get('F04000',0))
    gi=num(sS[k]['MCIF'])/num(sS17[k]['MCIF']); ge=num(uS[k]['F040'])/num(uS17[k]['F040'])
    imp22=imp17*gi; exp22=exp17*ge
    lo,mid,hi=RATIO[c]; fe=usf[c]; fi=fe*mid
    out.append(dict(code=c,name=nm,imp=imp22/1000,exp=exp22/1000,ratio=[lo,mid,hi],fImp=fi,fUS=fe,impMt=imp22*fi/1000,impLo=imp22*fe*lo/1000,impHi=imp22*fe*hi/1000,expMt=exp22*fe/1000,impMtUS=imp22*fe/1000))
print('imports low/central/high Mt',[round(sum(o[x] for o in out)) for x in ('impLo','impMt','impHi')])
print('summary import factor kgCO2e/$',{k:round(ief[k],3) for k in summ},'US avg',{k:round(v,3) for k,v in usavg.items()})
print(f"{'product':38s} imp$bn exp$bn fImp  fUS  impMt expMt")
for o in out: print(f"{o['name']:38s} {o['imp']:6.1f} {o['exp']:6.1f} {o['fImp']:5.2f} {o['fUS']:5.2f} {o['impMt']:6.1f} {o['expMt']:6.1f}")
ti=sum(o['impMt'] for o in out); te=sum(o['expMt'] for o in out)
nr=[o for o in out if o['code']!='324110']
print('imports at US intensity (ratio 1):',round(sum(o['impMtUS'] for o in out),1),'excl refined',round(sum(o['impMtUS'] for o in out if o['code']!='324110'),1))
print('TOTAL imports Mt',round(ti,1),'exports Mt',round(te,1),'| excl. refined products: imports',round(sum(o['impMt'] for o in nr),1),'exports',round(sum(o['expMt'] for o in nr),1))
json.dump(out,open('border.json','w'))
