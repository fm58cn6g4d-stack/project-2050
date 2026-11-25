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

REGISTERED = json.loads((ROOT / 'models/bookings/fiscal_dynamic_params.json').read_text())
AMENDMENTS = json.loads((ROOT / 'models/bookings/fiscal_dynamic_amendments.json').read_text())['amendments']


def amended(reg, amendments):
    """The registration with the dated amendments applied (the registered file itself is never edited)."""
    out = json.loads(json.dumps(reg))
    for a in amendments:
        for path, v in a.get('set', {}).items():
            node = out
            *head, last = path.split('.')
            for k in head:
                node = node[k]
            node[last] = v
        for k, v in a.get('add', {}).items():
            out['channels'][k] = v
    return out


PARAMS = amended(REGISTERED, AMENDMENTS)
OUT = ROOT / 'dossiers/foundations/fair-financing/notes/dynamic-results.md'
YEARS = FP.YEARS
START, REF_YEAR = 2030, 2029
SHOW = (2035, 2040, 2045, 2050, 2056)
# The readings: C, the plan's channels alone (no feedback); A, feedback from the FY2029 debt ratio on both paths
# (symmetric, the headline); B, feedback from CBO's baseline debt path (a sensitivity: it credits the plan's whole
# distance below current law at the average coefficients). The cases: central; pessimistic, every channel at its low end
# and, on each reading, whichever feedback end gives the plan the higher FY2056 debt; optimistic, the reverse.
# (Not pre-registered: the engine, this pairing and the readings' roles were set after the first run; AM-1 to AM-3.)
READINGS = ('C', 'A', 'B')
CASES = (('central', 'central'), ('pessimistic', 'low'), ('optimistic', 'high'))


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


def channels(gdp, end, params=None):
    return {k: channel_path(v, end, gdp) for k, v in (params or PARAMS)['channels'].items() if not k.startswith('_')}


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
    on = reference != 'C'                                       # reading C: the channels alone, no feedback
    beta = on * sym['rate_bp_per_point'][fb_end] / 10000       # per point of debt ratio, as a rate
    c = on * sym['crowd_gdp_pct_per_point'][fb_end] / 100      # GDP fraction per point
    tau, adj_r, adj_k = sym['budget_share_of_gdp_change'], sym['rate_bp_per_point']['adjust_years'], \
        sym['crowd_gdp_pct_per_point']['adjust_share_per_year']
    flows = flows or {}
    dref = 100 * debt[REF_YEAR] / gdp[REF_YEAR]
    ref = (lambda y: ref_path[y]) if reference == 'B' else (lambda y: dref)
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


def net_of(ch):
    return {y: sum(p[y] for p in ch.values()) for y in YEARS}


def plan_run(bk, debt, net, reading, fb_end, base_ratio):
    return run(bk, debt, bk.gdp, net, fb_end=fb_end, reference=reading, ref_path=base_ratio)


def case_run(bk, debt, net, reading, name, base_ratio):
    """The case's plan path on one reading: the central feedback, or the feedback end worst (pessimistic) or best
    (optimistic) for the plan's FY2056 debt on that reading. Returns (path, feedback end)."""
    if name == 'central' or reading == 'C':
        return plan_run(bk, debt, net, reading, 'central', base_ratio), 'central'
    runs = {e: plan_run(bk, debt, net, reading, e, base_ratio) for e in ('low', 'high')}
    pick = (max if name == 'pessimistic' else min)(runs, key=lambda e: runs[e][2056]['debt_gdp'])
    return runs[pick], pick


def build():
    bk = FP.Booked()
    gdp = bk.gdp
    base_debt = {y: bk.rows[y]['baseline_debt_bn'] for y in YEARS}
    plan_debt = bk.debt
    base_ratio = {y: 100 * base_debt[y] / gdp[y] for y in YEARS}
    res = dict(bk=bk, conv=dict(base=base_ratio, plan={y: 100 * plan_debt[y] / gdp[y] for y in YEARS}), cases={},
               channels={}, registered_channels={}, wad={})
    for end in ('low', 'central', 'high'):
        res['channels'][end] = channels(gdp, end)
        res['registered_channels'][end] = channels(gdp, end, REGISTERED)
        res['wad'][end] = wad_h1(gdp, end)
    for name, ch_end in CASES:
        net = net_of(res['channels'][ch_end])
        row = dict(net=net)
        for reading in READINGS:
            path, fb = case_run(bk, plan_debt, net, reading, name, base_ratio)
            fb_only, _ = case_run(bk, plan_debt, None, reading, name, base_ratio)
            base = run(bk, base_debt, gdp, None, fb_end=fb, reference=reading, ref_path=base_ratio)
            row[reading] = dict(plan=path, feedback_only=fb_only, base=base, fb=fb)
        res['cases'][name] = row
    # the registered channels (before AM-1 to AM-3), central and pessimistic, reading A: what the amendments moved
    res['registered'] = {name: case_run(bk, plan_debt, net_of(res['registered_channels'][ch_end]), 'A', name,
                                        base_ratio)[0] for name, ch_end in CASES[:2]}
    for end in ('central', 'high'):
        sim = FP.simulate(bk, res['wad'][end])
        res.setdefault('wad_debt', {})[end] = {y: sim[y]['debt_gdp'] for y in YEARS}
    res['growth'] = {(fac, sh): growth_sensitivity(bk, fac, sh) for fac in ('productivity', 'labor_force')
                     for sh in (-0.3, 0.3)}
    # The goals: the conventional share (the requirement, by the hard rule) and what each dynamic case would need
    res['goals'] = {}
    for g, lab in FP.GOALS:
        row = dict(label=lab, conventional=FP.solve_share(bk, g, 0.0))
        for name, ch_end in CASES:
            net = res['cases'][name]['net']
            for reading in READINGS:
                row[(name, reading)] = solve_dynamic(bk, g, net, reading, name, base_ratio)
        res['goals'][g] = row
    return res


def growth_sensitivity(bk, factor, shift):
    """The booked plan's debt ratio when productivity or labor-force growth runs `shift` points a year off CBO's
    path from FY2030 (the budget model's own growth link, ASM-GROWTH-LINK: CBO's rules of thumb, publication 62257).
    A CBO-style sensitivity of the economy, not a policy effect; the plan's rows stay in dollars."""
    gp = bk.f.growth_path(bk.b, factor, shift, START)
    return {y: 100 * (bk.debt[y] + gp[y]['debt']) / (bk.gdp[y] * (1 + gp[y]['gap'])) if y in gp
            else 100 * bk.debt[y] / bk.gdp[y] for y in YEARS}


def dynamic_with_x(bk, s, net, reading, fb_end, base_ratio):
    sim = FP.simulate(bk, FP.shape(bk, s))
    return plan_run(bk, {y: sim[y]['debt'] for y in YEARS}, net, reading, fb_end, base_ratio)


def _solve(ok):
    if ok(0.0):
        return 0.0
    lo, hi = 0.0, 8.0
    for _ in range(40):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if ok(mid) else (mid, hi)
    return round(hi + 0.0005, 3)


def solve_dynamic(bk, goal, net, reading, name, base_ratio):
    """The smallest share (the conventional shape) that meets the goal on one dynamic reading and case. The pessimistic
    (optimistic) case takes whichever feedback end makes THIS goal dearest (cheapest), judged by the goal's own test
    years, not FY2056 alone (the reviewer's note on #483)."""
    ends = ('central',) if name == 'central' or reading == 'C' else ('low', 'high')
    shares = [_solve(lambda s, e=e: FP.met(goal, dynamic_with_x(bk, s, net, reading, e, base_ratio))) for e in ends]
    return max(shares) if name == 'pessimistic' else min(shares)


RLAB = {'C': 'C, channels alone', 'A': 'A, symmetric from FY2029 (headline)', 'B': 'B, from CBO\'s baseline path (sensitivity)'}


def markdown(r):
    f1, f2, f0 = FP.f1, FP.f2, FP.f0
    bk, gdp = r['bk'], r['bk'].gdp
    ends = ('low', 'central', 'high')
    L = ['# The fiscal path review, part 2: the dynamic layer (results)', '',
         'Generated by `models/tools/fiscal_dynamic.py --write` (stage G step 8a), on the parameters registered before '
         'any run (`models/tools/fiscal_dynamic_params.json`, commit 87125a0) with the dated amendments AM-1 to AM-3 '
         '(`fiscal_dynamic_amendments.json`; [`dynamic-preregistration.md`](dynamic-preregistration.md), "Changes after '
         'registration"), made after the red-team of #483. **Shown beside the conventional score, never instead of it; '
         'no debt goal may rely on it (the hard rule).** Debt held by the public, % of GDP. Project arithmetic, not an '
         'official score.', '',
         '**Readings.** C: the plan\'s own channels alone, no feedback. **A: the rate and output feedback from the FY2029 '
         'debt ratio, on the baseline and the plan alike (symmetric; the headline).** B: the feedback from CBO\'s own '
         'baseline debt path, so only the plan\'s difference from current law gets it (a sensitivity: it credits the '
         'plan\'s whole distance below current law at average coefficients, which likely overstates it; see part 2 of '
         '`../4-fiscal-path.md`). **Cases.** Pessimistic: every channel at its low end and, on each reading, whichever '
         'feedback end gives the plan the higher FY2056 debt (for the goals, whichever end makes each goal dearest by its '
         'own test years); optimistic: the reverse. **Not pre-registered:** the engine, this pairing and the readings\' '
         'roles; the first results were committed about 6.5 minutes after the registration.', '']
    L += ['## 1. Debt, conventional and dynamic', '',
          '| Path | Reading | Case (feedback end) | ' + ' | '.join('FY%d' % y for y in SHOW) + ' |',
          '| --- | --- | --- |' + ' --- |' * len(SHOW)]
    L.append('| Baseline (current law) | conventional | — | ' + ' | '.join(f1(r['conv']['base'][y]) for y in SHOW) + ' |')
    L.append('| The plan as booked | conventional | — | ' + ' | '.join(f1(r['conv']['plan'][y]) for y in SHOW) + ' |')
    for name, _ in CASES:
        for reading in READINGS:
            c = r['cases'][name][reading]
            tag = '%s (%s)' % (name, c['fb']) if reading != 'C' else name
            if reading == 'A':
                L.append('| Baseline | A | %s | ' % tag + ' | '.join(f1(c['base'][y]['debt_gdp']) for y in SHOW) + ' |')
            if reading != 'C':
                L.append('| Plan, feedback only | %s | %s | ' % (reading, tag) + ' | '.join(f1(c['feedback_only'][y]['debt_gdp']) for y in SHOW) + ' |')
            L.append('| **Plan%s** | %s | %s | ' % (', channels alone' if reading == 'C' else ', feedback and channels', reading, tag) +
                     ' | '.join(f1(c['plan'][y]['debt_gdp']) for y in SHOW) + ' |')
    L.append('')
    a = r['cases']['central']['A']
    L += ['On reading A (central), the plan\'s FY2056 debt is %s%% against %s%% on the conventional score, and %s points '
          'below the baseline\'s (%s points on the conventional score): the plan\'s own channels cost a little, and the '
          'symmetric feedback raises both paths, the baseline\'s more.' % (
              f1(a['plan'][2056]['debt_gdp']), f1(r['conv']['plan'][2056]), f1(a['base'][2056]['debt_gdp'] - a['plan'][2056]['debt_gdp']),
              f1(r['conv']['base'][2056] - r['conv']['plan'][2056])), '',
          'The amendments\' effect (reading A, FY2056): central %s%% as registered, %s%% amended; pessimistic %s%% as '
          'registered, %s%% amended.' % (f1(r['registered']['central'][2056]['debt_gdp']), f1(a['plan'][2056]['debt_gdp']),
                                         f1(r['registered']['pessimistic'][2056]['debt_gdp']),
                                         f1(r['cases']['pessimistic']['A']['plan'][2056]['debt_gdp'])), '']
    L += ['## 2. The plan\'s channels, one by one ($B; + lowers the deficit)', '',
          '| ID | Channel | FY2040 low / central / high | FY2056 low / central / high |', '| --- | --- | --- | --- |']
    for k, v in PARAMS['channels'].items():
        if k.startswith('_'):
            continue
        am = ' (AM)' if k in ('N-TOP', 'N-CONTRIB', 'N-CTC', 'N-CARBON') else ''
        L.append('| %s%s | %s | %s | %s |' % (k, am, v['label'], ' / '.join(f0(r['channels'][e][k][2040]) for e in ends),
                                              ' / '.join(f0(r['channels'][e][k][2056]) for e in ends)))
    nets = {e: net_of(r['channels'][e]) for e in ends}
    L.append('| | **Net** | %s | %s |' % (' / '.join(f0(nets[e][2040]) for e in ends), ' / '.join(f0(nets[e][2056]) for e in ends)))
    L.append('| | Net, %% of GDP | %s | %s |' % (' / '.join(f2(100 * nets[e][2040] / gdp[2040]) for e in ends),
                                                ' / '.join(f2(100 * nets[e][2056] / gdp[2056]) for e in ends)))
    L.append('')
    w = r['wad']
    L += ['## 3. Health "works as designed" (WAD-H1), on its own line', '',
          'The single plan\'s gross cost growing below D2\'s cap, measured against the D2-held path (the conventional base '
          'already banks D2\'s −$249B in FY2040, so this counts only spending below the cap). Void if D2 fails. Never in '
          'a debt goal.', '',
          '| Points below the cap | FY2040 | FY2045 | FY2050 | FY2056 | Debt FY2056 with it (conventional otherwise) |',
          '| --- | --- | --- | --- | --- | --- |']
    for e in ('central', 'high'):
        L.append('| %s | %s | %s | %s | %s | %s |' % (f2(PARAMS['works_as_designed']['WAD-H1']['points_below_cap'][e]),
                                                     f0(w[e][2040]), f0(w[e][2045]), f0(w[e][2050]), f0(w[e][2056]), f1(r['wad_debt'][e][2056])))
    L.append('')
    L += ['## 4. The future economy: growth 0.3 points a year off CBO\'s path (a sensitivity, not a policy effect)', '',
          'The budget model\'s growth link (`ASM-GROWTH-LINK`, CBO\'s rules of thumb, publication 62257), from FY2030, on '
          'the plan as booked, extended past CBO\'s eleventh year on a straight line; the plan\'s rows stay in dollars. '
          'CBO\'s rules moved 20-33% between their 2025 and 2026 editions.', '',
          '| Growth a year, from FY2030 | ' + ' | '.join('FY%d' % y for y in SHOW) + ' |', '| --- |' + ' --- |' * len(SHOW)]
    L.append('| CBO\'s path (the booked plan) | ' + ' | '.join(f1(r['conv']['plan'][y]) for y in SHOW) + ' |')
    for (fac, sh), path in r['growth'].items():
        L.append('| %s %s point | ' % (fac.replace('_', ' ').capitalize(), f1(sh) if sh < 0 else '+' + f1(sh)) + ' | '.join(f1(path[y]) for y in SHOW) + ' |')
    L.append('')
    L += ['## 5. The goals: what the conventional score needs, and what the dynamic cases would need', '',
          'Share of GDP from FY2036 (the FY2032-36 ramp), central r − g. **By the hard rule the conventional share is the '
          'requirement.** A dynamic case that needs more shows the risk of the channels and the feedback; one that needs '
          'less is not a lower requirement.', '',
          '| Goal | Conventional (the requirement) | ' + ' | '.join('%s, %s' % (n, rd) for n, _ in CASES for rd in READINGS) + ' |',
          '| --- | --- |' + ' --- |' * (len(CASES) * len(READINGS))]
    for g, row in r['goals'].items():
        L.append('| %s | **%s** | ' % (row['label'], f2(row['conventional'])) +
                 ' | '.join(f2(row[(n, rd)]) for n, _ in CASES for rd in READINGS) + ' |')
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
