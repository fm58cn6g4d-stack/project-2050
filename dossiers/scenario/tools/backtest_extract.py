#!/usr/bin/env python3
"""Extract state-level Senate and presidential margins, 2000-2024, for the model back-test.

Role: builds dossiers/scenario/model-credibility-data.json from FiveThirtyEight's election-results files
(CC BY 4.0) [SRC-0600]. Status: run once by hand; the JSON is committed so the back-test needs no network.
Usage: python3 dossiers/scenario/tools/backtest_extract.py <dir with election_results_senate.csv and
election_results_presidential.csv>
"""
import csv
import json
import os
import sys
from collections import defaultdict


def top(rows, party):
    v = [float(r['percent']) for r in rows if r['ballot_party'] == party and r['percent']]
    return max(v) if v else None


def main(src):
    pres = defaultdict(dict)
    by = defaultdict(list)
    for r in csv.DictReader(open(os.path.join(src, 'election_results_presidential.csv'))):
        if r['stage'] == 'general' and r['state_abbrev'] and len(r['state_abbrev']) == 2:
            by[(int(r['cycle']), r['state_abbrev'])].append(r)
    for (cy, st), rows in by.items():
        d, rp = top(rows, 'DEM'), top(rows, 'REP')
        if d is not None and rp is not None:
            pres[cy][st] = round(d - rp, 2)
    races = defaultdict(list)
    for r in csv.DictReader(open(os.path.join(src, 'election_results_senate.csv'))):
        if r['stage'] in ('general', 'jungle primary', 'runoff') and int(r['cycle']) >= 2000:
            races[(int(r['cycle']), r['state_abbrev'], r['office_seat_name'], r['special'], r['stage'])].append(r)
    sen = []
    for (cy, st, seat, special, stage), rows in sorted(races.items()):
        if stage == 'jungle primary' and any(k[:4] == (cy, st, seat, special) and k[4] == 'runoff' for k in races):
            continue   # a runoff decided it
        d, rp = top(rows, 'DEM'), top(rows, 'REP')
        win = [r for r in rows if r['winner'] == 'true']
        sen.append(dict(cycle=cy, state=st, seat=seat, special=special == 'true', stage=stage, d=d, r=rp,
                        winner=win[0]['candidate_name'] if win else None,
                        winner_party=win[0]['ballot_party'] if win else None,
                        candidates=sorted({r['candidate_name'] for r in rows if r['candidate_name']})))
    out = dict(source='FiveThirtyEight election-results (CC BY 4.0), github.com/fivethirtyeight/election-results',
               pres={str(k): v for k, v in sorted(pres.items())}, senate=sen)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'model-credibility-data.json')
    json.dump(out, open(path, 'w'), indent=0, sort_keys=True)
    print('wrote', os.path.normpath(path), len(sen), 'Senate races;', {k: len(v) for k, v in pres.items()})


if __name__ == '__main__':
    main(sys.argv[1])
