#!/usr/bin/env python3
"""Stage G step 9: the clean-energy credits' (CLI-1) cost after FY2039, checked against the decided step-down.

Role: answers the question in `DEC-2026-11-25-03` (Espen: "don't the clean energy credits phase down anyways?"). The
budget model books CLI-1 at about $56B in FY2040 rising to about $77-82B a year from FY2045 to FY2056
(`dossiers/foundations/fair-financing/notes/program-inventory.md`), although clean power's specification steps the
credits down by statute (`dossiers/clean-power/4-specification.md`, CLI-1A.02). This tool shows where the tail comes
from, sets it beside the energy model's own path for the decided step-down, and prices the correction as a what-if on
the booked case. Status: stage G step 9, tier 2 (analysis; books nothing). The correction itself is a row in
`models/data/inputs/fiscal-after.csv` (an adopted input, tier 3), proposed in its own PR; `after_row()` gives it.

Where the tail comes from (`models/tools/climate-integration.py`): CLI-1's general-fund path is a baseline row plus the
climate export's redesign delta. The baseline row is the legacy credit set ($0.90T over FY2030-39) on its profile in
`fiscal-profiles.csv` (perm 0.8, fade 4% a year, grown with GDP: "scale down as deployment saturates after 2039
(estimate)"), which never reaches zero. The delta (`legacy/sources/climate-portfolio-pricing.json`, item `credits`,
case `conservative`, 80.4% of it to CLI-1) is the redesign's saving against a legacy credit set that itself ends: it is
−$35B in FY2040, shrinks to −$3B in FY2046 and is zero from FY2047. So from FY2047 the booked path is the legacy
baseline's tail alone, about $80B a year, a cost the decided statute doesn't have.

What the decided step-down leaves after FY2039 (CLI-1A.02; the energy model, `models/tools/energy/`, case `decided`,
which runs the statute's schedule: power credits at full value for construction starts through 2034, 60% for 2035-37,
none after, storage and firm power through 2039, vehicles through 2034, household credits through 2039 for low-income
heat pumps, 45X and 48C through 2039; wind's production credit paid for ten years after a plant starts): $62.7B in
2040, falling to $24.6B in 2043, $7.4B in 2045 and nothing from 2047. That is the real tail: ten-year production credits
and storage and firm power started by 2039.

The correction: CLI-1's path after FY2039 is the energy model's, at the booking's own level: energy(y) x (booked
FY2030-39 / energy FY2030-39), about 0.73. Not anchored on the booked FY2039 level, whose rise in FY2038-39 is the export's
artifact. Not verified: whether the energy model lags plants' entry into service after construction starts; if it
doesn't, the ten-year production credits run a few years past FY2047. The window FY2030-39 is untouched (it is
calibrated to the ledger, and G17 B's hold of FY2038-39 is decided on it).

Project arithmetic on exploratory models, not official scores.

    python3 models/tools/cli1_tail.py            # print the note
    python3 models/tools/cli1_tail.py --write    # write dossiers/foundations/fair-financing/notes/cli1-tail-check.md
    python3 models/tools/cli1_tail.py --after    # print the fiscal-after.csv row the correction needs
    python3 models/tools/cli1_tail.py --engine   # re-run the energy model's decided case and compare (node; slow)
"""
import argparse
import copy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'models/tools'), str(ROOT / 'models/tools/financing-protection')]
import packages as K   # noqa: E402

OUT = ROOT / 'dossiers/foundations/fair-financing/notes/cli1-tail-check.md'
YEARS = range(2026, 2057)
# The energy model's credit cost on the decided set (case `decided`; `models/tools/energy/model.py` accounts()
# ['credits'], nominal $B, calendar year y read as fiscal year y, the clean-power booking's convention). Re-run with
# --engine; it agrees with results.json's FY2040 (62.69) and FY2030-39 total (1,037.03).
ENERGY_DECIDED = {2030: 86.3, 2031: 98.7, 2032: 126.4, 2033: 130.0, 2034: 128.0, 2035: 98.0, 2036: 103.3,
                  2037: 98.1, 2038: 81.6, 2039: 86.7, 2040: 62.7, 2041: 56.3, 2042: 47.4, 2043: 24.6, 2044: 11.7,
                  2045: 7.4, 2046: 3.7, 2047: 0.0, 2048: 0.0, 2049: 0.0, 2050: 0.0}
AFTER_YEARS = range(2040, 2051)   # fiscal-after.csv's columns; the row grows with its index after FY2050 (from zero)


def line(case, name='CLI-1'):
    out = {y: 0.0 for y in YEARS}
    for a in case['audit']:
        if a['line'] == name:
            out[a['year']] += a['primary_deficit_change_bn']
    return out


def scale(booked):
    """The booking's level against the energy model's: booked FY2030-39 over the energy model's FY2030-39. A ten-year
    ratio, not FY2039's, because the booked FY2038-39 shape is the export's artifact (memo G25)."""
    return sum(booked[y] for y in range(2030, 2040)) / sum(ENERGY_DECIDED[y] for y in range(2030, 2040))


def corrected(booked):
    """CLI-1 after FY2039 on the decided step-down: the energy model's path at the booking's ten-year level."""
    out = dict(booked)
    k = scale(booked)
    for y in YEARS:
        if y > 2039:
            out[y] = k * ENERGY_DECIDED.get(y, 0.0)
    return out


def after_row(f, booked):
    """The fiscal-after.csv amounts for CLI-1's baseline row (climate-integration adds the export's delta on top), so
    that baseline + delta equals the corrected path, FY2040-50."""
    share = f.CL.CONFIG['credit_split']['CLI-1']
    tgt = corrected(booked)
    return {y: round(tgt[y] - share * f.CL.item('credits', y), 2) for y in AFTER_YEARS}


def profile_path(f, b):
    """CLI-1 as the profile alone gives it (no fiscal-after.csv row): the legacy baseline's tail plus the delta. This
    is the path booked before the correction, rebuilt the same way whether or not the correction is booked."""
    base = f._row_path(b, f.CL.CONFIG['legacy_gf_tn']['CLI-1'], f.PR.BILLS['CLI-1'], 'CLI-1')
    share = f.CL.CONFIG['credit_split']['CLI-1']
    return {y: base.get(y, 0.0) + share * f.CL.item('credits', y) for y in YEARS}


def with_path(f, b, old, u, target):
    """The booked case with CLI-1's FY2040-56 rows set to `target` ({year: $B})."""
    m2 = copy.deepcopy(old)
    row = next(r for r in m2['rows'] if r['id'] == 'CLI-1')
    for key in ('gf', 'uni'):
        for y in range(2040, 2057):
            row[key][str(y)] = target[y]
    return K.m.build_case('mixed', f, b, m2, u)


def booked_now(old):
    row = next(r for r in old['rows'] if r['id'] == 'CLI-1')
    return {y: float(row['gf'].get(str(y), 0.0)) for y in YEARS}


def is_booked(f, b, old):
    """True once the fiscal-after.csv row is in the committed model: the booked path is the corrected one."""
    now, pre = booked_now(old), profile_path(f, b)
    return all(abs(now[y] - corrected(pre)[y]) < 0.05 for y in YEARS)


def what_if(f, b, old, u):
    """(the case before the correction, the case after it, CLI-1 before, CLI-1 after). The booked case is one of the
    two, so the base every later tool reads is the corrected one, counted once."""
    pre = profile_path(f, b)
    fix = corrected(pre)
    c_booked = K.m.build_case('mixed', f, b, old, u)
    if is_booked(f, b, old):
        c_pre = with_path(f, b, old, u, pre)
        return c_pre, c_booked, line(c_pre), line(c_booked)
    c_fix = with_path(f, b, old, u, fix)
    return c_booked, c_fix, line(c_booked), line(c_fix)


def build():
    f, b, old, u = K.m.load()
    c0, c1, p0, p1 = what_if(f, b, old, u)
    r0 = {r['year']: r for r in c0['rows']}
    r1 = {r['year']: r for r in c1['rows']}
    return dict(f=f, booked=p0, fixed=p1, r0=r0, r1=r1, after=after_row(f, p0), is_booked=is_booked(f, b, old),
                share=f.CL.CONFIG['credit_split']['CLI-1'],
                delta={y: f.CL.CONFIG['credit_split']['CLI-1'] * f.CL.item('credits', y) for y in YEARS})


def engine_path():
    """Re-run the energy model's decided case and return its annual credit cost (nominal $B)."""
    sys.path.insert(0, str(ROOT / 'models/tools/energy'))
    import model as E
    cfg = E.config()
    cfg['cases'] = [c for c in cfg['cases'] if c['id'] == 'decided']
    for c in cfg['cases']:
        c.pop('mc', None)
        c.pop('households', None)
    cfg['mcDraws'] = 0
    acc = E.accounts(E.run_engine(cfg)['cases']['decided'])
    return {y: round(acc[y]['credits'], 1) for y in sorted(acc) if y >= 2030}


def f1(v):
    return '{:,.1f}'.format(v).replace('-', '−')


def markdown(d):
    p0, p1, r0, r1 = d['booked'], d['fixed'], d['r0'], d['r1']
    show = (2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2050, 2056)
    L = ['# CLI-1\'s cost after FY2039: the check (results)', '',
         'Generated by `models/tools/cli1_tail.py --write` after the common rebuild (stage G step 9). Read with '
         '[`../7-batch3-revision.md`](../7-batch3-revision.md) part 2. Nominal $B by federal fiscal year; project '
         'arithmetic on exploratory models, not official scores.', '',
         '## 1. Where the booked tail comes from', '',
         'CLI-1 in the budget model is a baseline row (the legacy credit set, $0.90T over FY2030-39, on its '
         '`fiscal-profiles.csv` profile: 80% kept after FY2039, fading 4% a year, grown with GDP) plus the climate '
         'export\'s redesign delta (80.4% of the item `credits`, case `conservative`). The delta ends in FY2047; the '
         'baseline row never does.', '',
         '| | ' + ' | '.join('FY%d' % y for y in show) + ' |', '| --- |' + ' --- |' * len(show)]
    base = {y: p0[y] - d['delta'][y] for y in YEARS}
    L.append('| Baseline row (legacy credit set, its profile) | ' + ' | '.join(f1(base[y]) for y in show) + ' |')
    L.append('| Redesign delta (the export, to CLI-1) | ' + ' | '.join(f1(d['delta'][y]) for y in show) + ' |')
    L.append('| **CLI-1 on the old profile (booked before the correction)** | ' + ' | '.join('**%s**' % f1(p0[y]) for y in show) + ' |')
    L.append('| Energy model, decided step-down (CLI-1A.02) | ' + ' | '.join(
        f1(ENERGY_DECIDED.get(y, 0.0)) if y <= 2050 else '0.0' for y in show) + ' |')
    L.append('| **CLI-1 corrected** (the energy model\'s path at the booking\'s FY2030-39 level, ×%.2f) |' % scale(p0) + ' ' + ' | '.join(
        '**%s**' % f1(p1[y]) for y in show) + ' |')
    L += ['', 'The energy model\'s level differs from the booking\'s (it counts the standby builder\'s credited '
          'generation and prices take-up on its own build: $1,037B over FY2030-39 against the booked $757B, '
          '`dossiers/clean-power/6-cost.md` part 5). Its path after FY2039 is scaled to the booking\'s level by the ten-year ratio.', '']
    sav = {y: p0[y] - p1[y] for y in YEARS}
    L += ['## 2. The correction, priced on the booked case (%s)' % ('booked: `fiscal-after.csv` carries the row' if d['is_booked'] else 'a what-if until the tier-3 input row lands'), '',
          '| | ' + ' | '.join('FY%d' % y for y in (2040, 2041, 2042, 2043, 2045, 2047, 2050, 2056)) + ' | FY2040-56 |',
          '| --- |' + ' --- |' * 9]
    ys = (2040, 2041, 2042, 2043, 2045, 2047, 2050, 2056)
    L.append('| CLI-1 saving | ' + ' | '.join(f1(sav[y]) for y in ys) + ' | %s |' % f1(sum(sav[y] for y in range(2040, 2057))))
    L.append('| General-fund gap, old profile (− is a margin) | ' + ' | '.join(f1(r0[y]['agenda_gf_primary_bn']) for y in ys) + ' | |')
    L.append('| General-fund gap, corrected | ' + ' | '.join(f1(r1[y]['agenda_gf_primary_bn']) for y in ys) + ' | |')
    L.append('| Debt, % of GDP, old profile | ' + ' | '.join(f1(r0[y]['debt_gdp']) for y in ys) + ' | |')
    L.append('| Debt, % of GDP, corrected | ' + ' | '.join(f1(r1[y]['debt_gdp']) for y in ys) + ' | |')
    t0 = max(range(2040, 2057), key=lambda y: r0[y]['agenda_gf_primary_bn'])
    t1 = max(range(2040, 2057), key=lambda y: r1[y]['agenda_gf_primary_bn'])
    L += ['', '- The tightest year FY2040-56: FY%d at %s on the old profile; FY%d at %s corrected.' % (
        t0, f1(r0[t0]['agenda_gf_primary_bn']), t1, f1(r1[t1]['agenda_gf_primary_bn'])),
          '- Interest is included in the debt figures (the model\'s own marginal rate).', '']
    L += ['## 3. The tier-3 row', '',
          'In `models/data/inputs/fiscal-after.csv`, CLI-1\'s baseline row after the window (climate-integration then '
          'adds the export\'s delta, so the sum is the corrected path):', '',
          '| ' + ' | '.join('FY%d' % y for y in AFTER_YEARS) + ' |', '|' + ' --- |' * len(AFTER_YEARS),
          '| ' + ' | '.join('%.2f' % d['after'][y] for y in AFTER_YEARS) + ' |', '']
    return '\n'.join(L) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--after', action='store_true')
    ap.add_argument('--engine', action='store_true')
    a = ap.parse_args()
    if a.engine:
        e = engine_path()
        bad = {y: (v, ENERGY_DECIDED.get(y)) for y, v in e.items() if abs(v - ENERGY_DECIDED.get(y, 0.0)) > 0.06}
        print('energy model decided credits:', e)
        print('differs from ENERGY_DECIDED:', bad or 'no')
        return
    d = build()
    if a.after:
        print('CLI-1,' + ','.join('%.2f' % d['after'][y] for y in AFTER_YEARS))
        return
    md = markdown(d)
    if a.write:
        OUT.write_text(md)
        print('wrote', OUT.relative_to(ROOT))
    else:
        print(md)


if __name__ == '__main__':
    main()
