"""Isolated Fiscal Data snapshot retrieval; no model-input updates.
Request contract checked against Treasury documentation printed October 26, 2026.
Live validation pending: session network returned HTTP 403. Standard library only.
"""
import argparse, datetime, hashlib, json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
BASE='https://api.fiscaldata.treasury.gov/services/api/fiscal_service'
ENDPOINT='/v1/accounting/mts/mts_table_1'

def retrieve(start, end, request=None, max_pages=100):
    def network(url):
        with urlopen(url, timeout=30) as r:
            return r.read()
    request=request or network
    pages=[]; total=None; seen=set(); count=0
    for n in range(1,max_pages+1):
        query={'format':'json','filter':f'record_date:gte:{start},record_date:lte:{end}',
               'sort':'record_date,parent_id,classification_id','page[size]':1000,'page[number]':n}
        url=BASE+ENDPOINT+'?'+urlencode(query)
        raw=request(url); data=json.loads(raw)
        rows=data.get('data'); meta=data.get('meta',{})
        if not isinstance(rows,list) or 'total-pages' not in meta or 'total-count' not in meta:
            raise ValueError('Missing data or completeness metadata; refusing snapshot')
        observed=(int(meta['total-pages']),int(meta['total-count']))
        if total is not None and observed!=total:
            raise ValueError('Result count changed during pagination; retry a fresh snapshot')
        total=observed
        for row in rows:
            date=row.get('record_date','')
            if not start<=date<=end: raise ValueError('Record outside requested dates')
            key=json.dumps(row,sort_keys=True)
            if key in seen: raise ValueError('Duplicate row across pages; refusing snapshot')
            seen.add(key)
        count+=len(rows)
        pages.append({'url':url,'sha256':hashlib.sha256(raw).hexdigest(),
                      'raw_response_utf8':raw.decode('utf-8')})
        if n>=total[0]:
            if count!=total[1]: raise ValueError('Incomplete result count')
            if not count: raise ValueError('Empty result; no snapshot saved')
            return {'retrieved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    'endpoint':ENDPOINT,'start':start,'end':end,'row_count':count,
                    'status':'raw evidence; requires semantic review before model integration',
                    'pages':pages}
    raise ValueError('Page limit exceeded; no partial snapshot saved')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--start',required=True); p.add_argument('--end',required=True)
    p.add_argument('--output',required=True,type=Path)
    a=p.parse_args()
    start=datetime.date.fromisoformat(a.start).isoformat()
    end=datetime.date.fromisoformat(a.end).isoformat()
    if start>end: p.error('start must precede end')
    # Download and validate before opening output. Exclusive creation preserves prior vintages.
    result=retrieve(start,end)
    with a.output.open('x') as f: json.dump(result,f,indent=2); f.write('\n')

if __name__=='__main__': main()
