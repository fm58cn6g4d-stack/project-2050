#!/usr/bin/env python3
"""Stage G step 8a: the fiscal path review's contained dynamic layer, beside the conventional score.

Role: a small, symmetric macro-feedback layer on the budget model's debt paths (`fiscal_path.py`), for the current-law
baseline and the settlement as booked. Its parameters were registered before any run
(`fiscal_dynamic_params.json`; `dossiers/foundations/fair-financing/notes/dynamic-preregistration.md`). It is shown
beside the conventional score and never replaces it: nothing here enters the ledger, the gap, D3 or D4, and by the
review's hard rule no debt goal may rely on it. Status: stage G step 8a, tier 2; needs an independent red-team review.
Writes `dossiers/foundations/fair-financing/notes/dynamic-results.md` with `--write`; `test_fiscal_path.py` checks it.

The engine, year by year from FY2030 (all of it in the registration):
  * the debt ratio d (dynamic debt over dynamic GDP) sets a rate target beta * (d - reference), which the average rate
    on the debt reaches over 5.9 years (ASM-RATE-ROLLOVER's average time to repricing), and an output target
    -c * (d - reference), which GDP approaches by 10% of the distance a year (capital accumulates slowly);
  * the plan's own channels are budget effects as shares of GDP (+ lowers the deficit); each moves GDP by its budget
    effect over 0.25, the deficit's response to a change in GDP;
  * the extra debt pays the model's marginal rate plus the rate change; the rate change also falls on the
    conventional debt.
  * Reading A measures d from the FY2029 ratio for the baseline and the plan alike; reading B from CBO's baseline debt
    path, so the baseline is unchanged and only the plan's difference gets the feedback.
WAD-H1 (health "works as designed") is reported on its own line, never in the dynamic net.

    python3 models/tools/fiscal_dynamic.py            # print
    python3 models/tools/fiscal_dynamic.py --write    # write the results note
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'models/tools'))
import fiscal_path as FP   # noqa: E402

PARAMS = json.loads((ROOT / 'models/tools/fiscal_dynamic_params.json').read_text())
OUT = ROOT / 'dossiers/foundations/fair-financing/notes/dynamic-results.md'
YEARS = FP.YEARS
START, REF_YEAR = 2030, 2029
SHOW = (2035, 2040, 2045, 2050, 2056)
# the combined cases: (channel end, feedback end); the feedback's high end is the larger effect
CASES = (('central', 'central', 'central'), ('pessimistic', 'low', 'high'), ('optimistic', 'high', 'low'))


def channel_path(spec, end, gdp):
    """{year: budget effect, $B} (+ lowers the deficit) for one channel at one end."""
    lvl40 = spec[end]
    lvl56 = spec['y2056'][end] if 'y2056' in spec else lvl40
    out = {}
    for y in YEARS:
        ph = 0.0 if y < spec['start'] else min(1.0, (y - spec['start'] + 1) / spec['ramp'])
        share = lvl40 if y <= 2040 else lvl40 + (lvl56 - lvl40) * (y - 2040) / 16
        out[y] = ph * share / 100 * gdp[y]
    return out


def channels(gdp, end):
    return {k: channel_path(v, end, gdp) for k, v in PARAMS['channels'].items() if not k.startswith('_')}


def wad_h1(gdp, end):
    """{year: saving, $B}: the single plan's gross cost growing `points` below D2's cap from FY2037, on the D2-held
    path ($7,681B in FY2040, grown at GDP + 1 point; the D2 check is in the registration, part C)."""
    w = PARAMS['works_as_designed']['WAD-H1']
    s = w['points_below_cap'][end] / 100
    out = {}
    for y in YEARS:
        held = w['held_gross_2040_bn'] * gdp[y] / gdp[2040] * 1.01 ** (y - 2040)
        out[y] = held * (1 - (1 - s) ** (y - w['start'] + 1)) if y >= w['start'] else 0.0
    return out


def run(bk, debt, gdp, flows=None, fb_end='central', reference='A', ref_path=None):
    """Dynamic debt for a conventional path (debt {year: $B}, gdp {year: $B}). `flows` {year: $B} are the plan's
    channel budget effects (+ lowers the deficit). Returns {year: dict(debt, gdp, debt_gdp, rate_pts, gap)}."""
    sym = PARAMS['symmetric']
    beta = sym['rate_bp_per_point'][fb_end] / 10000            # per point of debt ratio, as a rate
    c = sym['crowd_gdp_pct_per_point'][fb_end] / 100           # GDP fraction per point
    tau, adj_r, adj_k = sym['budget_share_of_gdp_change'], sym['rate_bp_per_point']['adjust_years'], \
        sym['crowd_gdp_pct_per_point']['adjust_share_per_year']
    flows = flows or {}
    dref = 100 * debt[REF_YEAR] / gdp[REF_YEAR]
    ref = (lambda y: dref) if reference == 'A' else (lambda y: ref_path[y])
    out, E, dr, crowd = {}, 0.0, 0.0, 0.0
    prev_ratio = 100 * debt[REF_YEAR] / gdp[REF_YEAR]
    for y in YEARS:
        if y < START:
            out[y] = dict(debt=debt[y], gdp=gdp[y], debt_gdp=100 * debt[y] / gdp[y], rate_pts=0.0, gap=0.0)
            continue
        target_r = beta * (prev_ratio - ref(y - 1))
        dr += (target_r - dr) / adj_r
        target_k = -c * (prev_ratio - ref(y - 1))
        crowd += adj_k * (target_k - crowd)
        fl = flows.get(y, 0.0)
        gap = crowd + fl / tau / gdp[y]
        rm = bk.f.marginal_rate(bk.b, y)
        extra_interest = dr * (debt[y - 1] + E) + rm * E
        E += extra_interest - fl - tau * crowd * gdp[y]
        D, G = debt[y] + E, gdp[y] * (1 + gap)
        prev_ratio = 100 * D / G
        out[y] = dict(debt=D, gdp=G, debt_gdp=prev_ratio, rate_pts=100 * dr, gap=100 * gap)
    return out


def build():
    bk = FP.Booked()
    gdp = bk.gdp
    base_debt = {y: bk.rows[y]['baseline_debt_bn'] for y in YEARS}
    plan_debt = bk.debt
    base_ratio = {y: 100 * base_debt[y] / gdp[y] for y in YEARS}
    res = dict(bk=bk, conv=dict(base=base_ratio, plan={y: 100 * plan_debt[y] / gdp[y] for y in YEARS}), cases={},
               channels={}, wad={})
    for end in ('low', 'central', 'high'):
        ch = channels(gdp, end)
        res['channels'][end] = ch
        res['wad'][end] = wad_h1(gdp, end)
    for name, ch_end, fb_end in CASES:
        net = {y: sum(p[y] for p in res['channels'][ch_end].values()) for y in YEARS}
        row = {}
        for reading in ('A', 'B'):
            kw = dict(fb_end=fb_end, reference=reading, ref_path=base_ratio)
            row[reading] = dict(base=run(bk, base_debt, gdp, None, **kw), plan=run(bk, plan_debt, gdp, net, **kw),
                                plan_feedback_only=run(bk, plan_debt, gdp, None, **kw))
        row['net'] = net
        res['cases'][name] = row
    # WAD-H1 alone, on the conventional score (a primary saving rolled at the model's rate)
    for end in ('central', 'high'):
        sim = FP.simulate(bk, res['wad'][end])
        res.setdefault('wad_debt', {})[end] = {y: sim[y]['debt_gdp'] for y in YEARS}
    res['growth'] = {(fac, sh): growth_sensitivity(bk, fac, sh) for fac in ('productivity', 'labor_force')
                     for sh in (-0.3, 0.3)}
    # The goals: the conventional share (the recommendation, by the hard rule) and what dynamic cases would need
    res['goals'] = {}
    for g, lab in FP.GOALS:
        conv = FP.solve_share(bk, g, 0.0)
        row = dict(label=lab, conventional=conv)
        for name, ch_end, fb_end in CASES:
            net = res['cases'][name]['net']
            row[name] = solve_dynamic(bk, g, net, fb_end, base_ratio)
        res['goals'][g] = row
    return res


def growth_sensitivity(bk, factor, shift):
    """The booked plan's debt ratio when productivity or labor-force growth runs `shift` points a year off CBO's
    path from FY2030 (the budget model's own growth link, ASM-GROWTH-LINK: CBO's rules of thumb, publication 62257).
    A CBO-style sensitivity of the economy, not a policy effect; the plan's rows stay in dollars."""
    gp = bk.f.growth_path(bk.b, factor, shift, START)
    return {y: 100 * (bk.debt[y] + gp[y]['debt']) / (bk.gdp[y] * (1 + gp[y]['gap'])) if y in gp
            else 100 * bk.debt[y] / bk.gdp[y] for y in YEARS}


def dynamic_with_x(bk, s, net, fb_end, base_ratio):
    sim = FP.simulate(bk, FP.shape(bk, s))
    return run(bk, {y: sim[y]['debt'] for y in YEARS}, bk.gdp, net, fb_end=fb_end, reference='B', ref_path=base_ratio)


def solve_dynamic(bk, goal, net, fb_end, base_ratio):
    """The smallest share (the conventional shape) that meets the goal on dynamic reading B."""
    ok = lambda s: FP.met(goal, dynamic_with_x(bk, s, net, fb_end, base_ratio))
    if ok(0.0):
        return 0.0
    lo, hi = 0.0, 8.0
    for _ in range(40):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if ok(mid) else (mid, hi)
    return round(hi + 0.0005, 3)


def markdown(r):
    f1, f2, f0 = FP.f1, FP.f2, FP.f0
    bk, gdp = r['bk'], r['bk'].gdp
    L = ['# The fiscal path review, part 2: the dynamic layer (results)', '',
         'Generated by `models/tools/fiscal_dynamic.py --write` (stage G step 8a), on the parameters registered before '
         'any run ([`dynamic-preregistration.md`](dynamic-preregistration.md); `models/tools/fiscal_dynamic_params.json`). '
         '**Shown beside the conventional score, never instead of it; no debt goal may rely on it (the hard rule). It '
         'needs an independent red-team review.** Debt held by the public, % of GDP. Reading A measures the feedback '
         'from the FY2029 debt ratio for both paths; reading B from CBO\'s baseline debt path, so only the plan\'s '
         'difference from current law gets it. Pessimistic: every channel at its low end and the feedback at its high '
         'end; optimistic: the reverse. Project arithmetic, not an official score.', '']
    L += ['## 1. Debt, conventional and dynamic', '',
          '| Path | Reading | Case | ' + ' | '.join('FY%d' % y for y in SHOW) + ' |', '| --- | --- | --- |' + ' --- |' * len(SHOW)]
    L.append('| Baseline (current law) | conventional | — | ' + ' | '.join(f1(r['conv']['base'][y]) for y in SHOW) + ' |')
    L.append('| The plan as booked | conventional | — | ' + ' | '.join(f1(r['conv']['plan'][y]) for y in SHOW) + ' |')
    for name, _, _ in CASES:
        for reading in ('A', 'B'):
            c = r['cases'][name][reading]
            if reading == 'A':
                L.append('| Baseline | A | %s | ' % name + ' | '.join(f1(c['base'][y]['debt_gdp']) for y in SHOW) + ' |')
            L.append('| Plan, feedback only | %s | %s | ' % (reading, name) + ' | '.join(f1(c['plan_feedback_only'][y]['debt_gdp']) for y in SHOW) + ' |')
            L.append('| **Plan, feedback and channels** | %s | %s | ' % (reading, name) + ' | '.join(f1(c['plan'][y]['debt_gdp']) for y in SHOW) + ' |')
    L.append('')
    c = r['cases']['central']['A']
    L += ['On reading A (central), the plan\'s debt is %s points below the baseline\'s in FY2056, against %s points on '
          'the conventional score: the feedback widens the plan\'s advantage, because the baseline\'s debt is higher.' % (
              f1(c['base'][2056]['debt_gdp'] - c['plan'][2056]['debt_gdp']), f1(r['conv']['base'][2056] - r['conv']['plan'][2056])), '']
    # channels
    L += ['## 2. The plan\'s channels, one by one ($B; + lowers the deficit)', '',
          '| ID | Channel | FY2040 low / central / high | FY2056 low / central / high |', '| --- | --- | --- | --- |']
    for k, v in PARAMS['channels'].items():
        if k.startswith('_'):
            continue
        L.append('| %s | %s | %s | %s |' % (k, v['label'], ' / '.join(f0(r['channels'][e][k][2040]) for e in ('low', 'central', 'high')),
                                            ' / '.join(f0(r['channels'][e][k][2056]) for e in ('low', 'central', 'high'))))
    nets = {e: {y: sum(p[y] for p in r['channels'][e].values()) for y in YEARS} for e in ('low', 'central', 'high')}
    L.append('| | **Net** | %s | %s |' % (' / '.join(f0(nets[e][2040]) for e in ('low', 'central', 'high')),
                                           ' / '.join(f0(nets[e][2056]) for e in ('low', 'central', 'high'))))
    L.append('| | Net, %% of GDP | %s | %s |' % (' / '.join(f2(100 * nets[e][2040] / gdp[2040]) for e in ('low', 'central', 'high')),
                                                ' / '.join(f2(100 * nets[e][2056] / gdp[2056]) for e in ('low', 'central', 'high'))))
    L.append('')
    # WAD
    w = r['wad']
    L += ['## 3. Health "works as designed" (WAD-H1), on its own line', '',
          'The single plan\'s gross cost growing below D2\'s cap, measured against the D2-held path (so D2\'s booked '
          '−$249B in FY2040 isn\'t counted twice). Void if D2 fails. Never in a debt goal.', '',
          '| Points below the cap | FY2040 | FY2045 | FY2050 | FY2056 | Debt FY2056 with it (conventional otherwise) |',
          '| --- | --- | --- | --- | --- | --- |']
    for e in ('central', 'high'):
        L.append('| %s | %s | %s | %s | %s | %s |' % (f2(PARAMS['works_as_designed']['WAD-H1']['points_below_cap'][e]),
                                                     f0(w[e][2040]), f0(w[e][2045]), f0(w[e][2050]), f0(w[e][2056]), f1(r['wad_debt'][e][2056])))
    L.append('')
    # growth
    L += ['## 4. The future economy: growth 0.3 points a year off CBO\'s path (a sensitivity, not a policy effect)', '',
          'The budget model\'s growth link (`ASM-GROWTH-LINK`, CBO\'s rules of thumb, publication 62257), from FY2030, on '
          'the plan as booked. It shows how much the debt path rests on the economy\'s own growth, next to which the '
          'policy channels above are small. CBO\'s rules moved 20-33% between their 2025 and 2026 editions.', '',
          '| Growth a year, from FY2030 | ' + ' | '.join('FY%d' % y for y in SHOW) + ' |', '| --- |' + ' --- |' * len(SHOW)]
    L.append('| CBO\'s path (the booked plan) | ' + ' | '.join(f1(r['conv']['plan'][y]) for y in SHOW) + ' |')
    for (fac, sh), path in r['growth'].items():
        L.append('| %s %+.1f point | ' % (fac.replace('_', ' ').capitalize(), sh) + ' | '.join(f1(path[y]) for y in SHOW) + ' |')
    L.append('')
    # goals
    L += ['## 5. The goals: what the conventional score needs, and what the dynamic cases would need', '',
          'Share of GDP from FY2036 (the FY2032-36 ramp), central r − g. Dynamic shares are on reading B. **By the hard '
          'rule the conventional share is the one a recommendation must meet**; a dynamic shortfall below it is margin, '
          'or a rate lowered later by a trigger once it shows up in receipts.', '',
          '| Goal | Conventional (the requirement) | Dynamic central | Dynamic pessimistic | Dynamic optimistic |',
          '| --- | --- | --- | --- | --- |']
    for g, row in r['goals'].items():
        L.append('| %s | %s | %s | %s | %s |' % (row['label'], f2(row['conventional']), f2(row['central']), f2(row['pessimistic']), f2(row['optimistic'])))
    L.append('')
    return '\n'.join(L) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    a = ap.parse_args()
    md = markdown(build())
    if a.write:
        OUT.write_text(md)
        print('wrote', OUT.relative_to(ROOT))
    else:
        print(md)


if __name__ == '__main__':
    main()
