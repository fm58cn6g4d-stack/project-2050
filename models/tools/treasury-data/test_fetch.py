"""Synthetic transport tests, not evidence of live Treasury compatibility."""
import json, unittest
from urllib.parse import parse_qs,urlparse
from fetch import retrieve

def payload(rows,pages=2,count=2):
    return json.dumps({'data':rows,'meta':{'total-pages':pages,'total-count':count}}).encode()
class Tests(unittest.TestCase):
    def test_all_pages_and_raw_provenance(self):
        urls=[]
        def request(url):
            urls.append(url); n=int(parse_qs(urlparse(url).query)['page[number]'][0])
            return payload([{'record_date':f'2025-0{n}-28','amount':'null'}])
        d=retrieve('2025-01-01','2025-03-01',request)
        self.assertEqual(d['row_count'],2)
        self.assertEqual(len(d['pages']),2)
        self.assertIn('"amount": "null"',d['pages'][0]['raw_response_utf8'])
        self.assertEqual(parse_qs(urlparse(urls[0]).query)['filter'],parse_qs(urlparse(urls[1]).query)['filter'])
    def test_changing_result_count_rejected(self):
        responses=iter([payload([{'record_date':'2025-01-28'}]),payload([{'record_date':'2025-02-28'}],2,3)])
        with self.assertRaises(ValueError): retrieve('2025-01-01','2025-03-01',lambda _:next(responses))
    def test_duplicate_page_rejected(self):
        with self.assertRaises(ValueError): retrieve('2025-01-01','2025-03-01',lambda _:payload([{'record_date':'2025-01-28'}]))
    def test_incomplete_rejected(self):
        with self.assertRaises(ValueError): retrieve('2025-01-01','2025-03-01',lambda _:payload([{'record_date':'2025-01-28'}],1,2))
    def test_missing_metadata_rejected(self):
        with self.assertRaises(ValueError): retrieve('2025-01-01','2025-03-01',lambda _:b'{"data":[]}')
    def test_date_range_rejected(self):
        with self.assertRaises(ValueError): retrieve('2025-01-01','2025-03-01',lambda _:payload([{'record_date':'2026-01-28'}],1,1))
if __name__=='__main__': unittest.main()
