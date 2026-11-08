#!/usr/bin/env python3
"""Extract The Downballot's special-election trackers (2017-2026) into one committed CSV.

Role: builds dossiers/scenario/specials-by-year.csv, the special-election series behind the scorecard's
"specials average" benchmark (2027-scorecard.md). Status: current (November 8, 2026).

Source: The Downballot, "D-vs.-R special elections vs. presidential results", one public Google Sheet per
cycle (Donner, Lambert and Nir) [SRC-1092]; presidential baselines by legislative district are their
calculations from Dave's Redistricting App. Special-election results are the official canvass where the
sheet's "Official" column is marked (2021 onward). The Downballot asks users to cite it with a link and to
"refrain from reproducing entire spreadsheets", so only the derived per-year series is committed; the full
race-level extract is written to dossiers/scenario/.local/ (untracked) for checking and reruns.

Inclusion follows the sheet: a race counts toward an average only when the Democratic and Republican shares
together reach 90%, and races the sheet marks with an asterisk are excluded.

Run (needs network; reads the sheets' gviz JSON, which carries unrounded values):
  python3 -I dossiers/scenario/tools/specials_extract.py           print per-year averages
  python3 -I dossiers/scenario/tools/specials_extract.py --write   rewrite the per-year CSV and the local extract
"""
import csv
import json
import os
import re
import sys
import urllib.request

SHEETS = {   # cycle: (sheet id, {calendar year: gid}), from the-downballot.com/data, read 2026-11-08
    '2017-18': ('1C2MVeM2K7WgqmJw5RCQbWyTo2u73CX1pI8zw_G-7BJo', {2017: '0', 2018: '2144047916'}),
    '2019-20': ('1dXQhlzCAw05fC7P21eCivdfLOB-F3nykPVRPzG49U9g', {2019: '0', 2020: '539852412'}),
    '2021-22': ('1G1SeLtlfDY9xqqVfFTsoh0jwr6h7aQzOOWpJ29aez2w', {2021: '0', 2022: '523128020'}),
    '2023-24': ('1ajyphWQru9TgDDiBe8kvEmApBEXND2wl9MVaxi1dndk', {2023: '0', 2024: '995309150'}),
    '2025-26': ('1JGk1r1VXnxBrAIVHz1C5HTB5jxCO6Zw4QNPivdhyWHw', {2025: '415249345', 2026: '1173601967'}),
}
BASELINE = {'2017-18': 'Clinton 2016', '2019-20': 'Clinton 2016', '2021-22': 'Biden 2020',
            '2023-24': 'Biden 2020', '2025-26': 'Harris 2024'}
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'specials-by-year.csv')                    # committed: derived series only
LOCAL = os.path.join(HERE, '..', '.local', 'specials-2017-2026-full.csv')  # untracked: race-level extract
FIELDS = ['cycle', 'year', 'date', 'state', 'district', 'level', 'held_by', 'winner', 'flip', 'official',
          'd_pct', 'r_pct', 'margin', 'baseline', 'pres_d_pct', 'pres_r_pct', 'pres_margin', 'swing', 'counted']
FEDERAL = re.compile(r'^([A-Z]{2})-(\d{2}|AL)$')   # a congressional district: the prefix is the state


def is_federal(district, state):
    """A congressional district is named for its state (NJ-11, MT-AL); SD-/HD-/AD- are legislative."""
    m = FEDERAL.match(district)
    if not m or m.group(1) != state:
        return False
    return state != 'SD' or m.group(2) == 'AL'   # South Dakota is at-large; its SD-nn are Senate districts


def fetch(sheet, gid):
    url = 'https://docs.google.com/spreadsheets/d/%s/gviz/tq?tqx=out:json&headers=0&gid=%s' % (sheet, gid)
    req = urllib.request.Request(url, headers={'User-Agent': 'project-2050-research'})
    with urllib.request.urlopen(req, timeout=60) as r:
        text = r.read().decode('utf-8')
    return json.loads(text[text.index('{'):text.rindex('}') + 1])['table']['rows']


def val(c):
    return None if c is None else c.get('v')


def parse(cycle, year, rows):
    out = []
    for row in rows:
        c = [val(x) for x in row['c']]
        c += [None] * (16 - len(c))
        date, state, dist = c[1], c[2], c[3]
        if not (isinstance(date, str) and date.startswith('Date(') and state and dist):
            continue
        if not isinstance(c[7], (int, float)) or not isinstance(c[13], (int, float)):
            continue
        y, m, d = (int(x) for x in re.findall(r'\d+', date)[:3])
        dname = str(dist).strip()
        star = dname.endswith('*')
        dname = dname.rstrip(' *')
        dp, rp, pd, pr = c[7], c[8], c[11], c[12]
        margin = 100 * (dp - rp)
        pmargin = 100 * (pd - pr)
        winner = str(c[5] or '')
        out.append(dict(
            cycle=cycle, year=year, date='%04d-%02d-%02d' % (y, m + 1, d), state=state, district=dname,
            level='federal' if is_federal(dname, state) else 'state legislative',
            held_by=str(c[4] or '').strip('() '), winner=winner.replace('✓', '').strip('() '),
            flip='yes' if '✓' in winner else 'no', official='yes' if (c[0] or '').strip().lower() == 'x' else 'no',
            d_pct='%.2f' % (100 * dp), r_pct='%.2f' % (100 * rp), margin='%.2f' % margin, baseline=BASELINE[cycle],
            pres_d_pct='%.2f' % (100 * pd), pres_r_pct='%.2f' % (100 * pr), pres_margin='%.2f' % pmargin,
            swing='%.2f' % (margin - pmargin), counted='no' if star or dp + rp < 0.9 else 'yes'))
    return out


YEAR_FIELDS = ['year', 'cycle', 'baseline', 'races', 'races_counted', 'avg_swing', 'median_swing', 'official',
               'federal_counted', 'federal_avg_swing']


def by_year(rows):
    out = []
    for y in sorted({r['year'] for r in rows}):
        rr = [r for r in rows if r['year'] == y]
        cc = [float(r['swing']) for r in rr if r['counted'] == 'yes']
        fed = [float(r['swing']) for r in rr if r['counted'] == 'yes' and r['level'] == 'federal']
        cc_s = sorted(cc)
        mid = (cc_s[(len(cc_s) - 1) // 2] + cc_s[len(cc_s) // 2]) / 2
        out.append(dict(year=y, cycle=rr[0]['cycle'], baseline=rr[0]['baseline'], races=len(rr),
                        races_counted=len(cc), avg_swing='%.2f' % (sum(cc) / len(cc)), median_swing='%.2f' % mid,
                        official=sum(r['official'] == 'yes' for r in rr), federal_counted=len(fed),
                        federal_avg_swing='%.2f' % (sum(fed) / len(fed)) if fed else ''))
    return out


def main():
    rows = []
    for cycle, (sheet, tabs) in SHEETS.items():
        for year, gid in tabs.items():
            rows += parse(cycle, year, fetch(sheet, gid))
    rows.sort(key=lambda r: (r['date'], r['state'], r['district']))
    years = by_year(rows)
    for y in years:
        print(y['year'], y['races_counted'], y['avg_swing'], 'federal', y['federal_counted'])
    if '--write' in sys.argv:
        with open(OUT, 'w', newline='') as f:
            f.write('# Derived from The Downballot, D-vs.-R special elections vs. presidential results, 2017-2026 '
                    '(Donner, Lambert, Nir; the-downballot.com/data) [SRC-1092], by tools/specials_extract.py on '
                    '2026-11-08. Swing = D-minus-R margin minus the district\'s last presidential margin, points; '
                    'counted = D + R at 90% or more and not starred by the sheet.\n')
            w = csv.DictWriter(f, fieldnames=YEAR_FIELDS, lineterminator='\n')
            w.writeheader()
            w.writerows(years)
        os.makedirs(os.path.dirname(LOCAL), exist_ok=True)
        with open(os.path.join(os.path.dirname(LOCAL), '.gitignore'), 'w') as f:
            f.write('*\n')
        with open(LOCAL, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n')
            w.writeheader()
            w.writerows(rows)
        print('wrote', os.path.normpath(OUT), len(years), 'years; local extract', os.path.normpath(LOCAL), len(rows), 'rows')


if __name__ == '__main__':
    main()
