#!/usr/bin/env python3
"""Audit official 2026 ASEC ZIP and reproduce source-year SPM; no policy run."""
import argparse,csv,hashlib,io,json,math,zipfile
from pathlib import Path
from collections import Counter
from model import poverty_metrics,replicate_intervals,write_json

def audit(path):
 children={}; keys=set(); dates=Counter(); mismatches=0; excluded=0; total=poor=0.; count=poor_n=0
 with zipfile.ZipFile(path) as z:
  with z.open('pppub26.csv') as f:
   for r in csv.DictReader(io.TextIOWrapper(f)):
    key=(r['PH_SEQ'],r['PPPOS'])
    if key in keys:raise ValueError('duplicate person key')
    keys.add(key);dates[r['FILEDATE']]+=1
    threshold=float(r['SPM_POVTHRESHOLD']);resources=float(r['SPM_RESOURCES']);weight=float(r['MARSUPWT'])/100
    if threshold<=0:excluded+=1;continue
    ispoor=resources<threshold
    mismatches+=int(ispoor!=bool(int(r['SPM_POOR'])))
    count+=1;poor_n+=ispoor;total+=weight;poor+=weight*ispoor
    if int(r['A_AGE'])<18:children[key]={'person_weight':weight,'resources':resources,'threshold':threshold}
  joined=set();base_differences=[]
  with z.open('asec_csv_repwgt_2026.csv') as f:
   for r in csv.DictReader(io.TextIOWrapper(f)):
    key=(r['h_seq'],r['PPPOS'])
    if key in joined:raise ValueError('duplicate replicate key')
    joined.add(key)
    if key in children:
     c=children[key];c['replicate_weights']=[float(r['pwwgt'+str(i)]) for i in range(1,161)]
     c['replicate_base_weight']=float(r['pwwgt0']);base_differences.append(abs(c['person_weight']-c['replicate_base_weight']))
 if keys!=joined:raise ValueError('person/replicate key sets do not match')
 rows=list(children.values());point=poverty_metrics(rows)
 if mismatches or poor_n!=16941 or round(poor/1000)!=44390:
  raise ValueError('Census public-use accounting crosscheck failed')
 if not .1335 <= point['poor_rate'] < .1345:
  raise ValueError('Published rounded child SPM benchmark failed')
 # SDR centers on precise pwwgt0, not rounded person-file MARSUPWT.
 precise=[dict(r,person_weight=r['replicate_base_weight']) for r in rows]
 return {'source_url':'https://www2.census.gov/programs-surveys/cps/datasets/2026/march/asecpub26csv.zip',
 'archive_sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'survey_year':2026,'income_year':2025,
 'filedate_counts':dict(dates),'person_records':len(keys),'replicate_records':len(joined),'join_key':['PH_SEQ/h_seq','PPPOS'],
 'join_complete':True,'nonpositive_threshold_records_excluded':excluded,'spm_flag_disagreements':mismatches,
 'all_people':{'unweighted_people':count,'unweighted_poor':poor_n,'weighted_people':total,'weighted_poor':poor,'poverty_rate':poor/total},
 'children_marsupwt':point,'children_precise_replicate_base':poverty_metrics(precise),
 'children_sampling_uncertainty':replicate_intervals(precise),'max_base_weight_rounding_difference':max(base_differences),
 'scope':'Observed source-year SPM only; no Project policy, target-year aging, ID imputation or delivery assumptions',
 'census_readme_all_age_crosscheck':{'expected_unweighted_poor':16941,'expected_weighted_poor_thousands_rounded':44390,
 'unweighted_match':poor_n==16941,'weighted_rounded_match':round(poor/1000)==44390}}

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--archive',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 result=audit(a.archive);write_json(a.output,result)
 print(json.dumps(result,indent=2))
