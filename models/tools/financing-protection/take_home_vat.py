"""The take-home test with the VAT counted: the review of #469, B-3.

Role: health's take-home test (`DEC-2026-11-15-02`; `health_cost_review.take_home_micro`) asks whether a tax unit's
visible health costs fall under the plan. The settlement replaces the 2 points above $20K/$40K with a VAT, which that
test does not see. This screen adds each unit's VAT to the plan's side and reruns the test for each of memo G2's
options at the VAT rate that option needs in FY2040 (`packages.vat_schedule`). Status: exploratory screen for a
provisional draft; nothing adopted or booked.

The VAT a unit pays: the per-household VAT of its household's fifth on D3's consumption key, at the FY2040 rate (gross,
as households pay it; `packages.VAT_POINT_2040` / (1 - 0.25) a point), in 2026 dollars, split among the household's
tax units by persons. A rough allocation: consumption within a fifth is not modelled, and the per-household amounts
use the FY2034-35 household count (review N-6).

Retirees and others are reported two ways (the review's B-1): (b) CBO's convention, nominal incomes fixed, so the VAT
is borne as above; and (a) prices rise by the rate and Social Security and SSI rise with them, so the VAT on a unit is
reduced by the rate times its Social Security and SSI income. Fixed pensions and savings get no such offset.

Run after the common rebuild:  python3 models/tools/financing-protection/take_home_vat.py [--markdown]
"""
import argparse
import json
import os
import sys

import packages as K

TOOLS = str(K.ROOT / 'models/tools')
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)

# Memo G2's options: (package in packages.PACKAGES, the health contribution's base rate R, the 2 points kept?)
G2 = {'A: drop the 2 points': ('g2_dropped', 2.25, False),
      'B: keep them': ('g2_kept', 2.25, True),
      'C: fold into R = 3.25% (recommended)': ('recommended', 3.25, False),
      'D: drop, R = 2.5%': ('g2_r25', 2.5, False),
      'G3 E: no VAT, R = 4.45%': ('g3_contribution_only', 4.45, False)}


def vat_rate_2040(ctx, name):
    """The VAT rate in FY2040 of a package whose last option is `vat_closing` (0 for a package with no VAT)."""
    kind, params = K.PACKAGES[name][-1]
    if kind != 'vat_closing':
        return 0.0
    p = dict(params)
    return K.vat_schedule(ctx, list(p.pop('spec')), **p)['rate']


def quintile_vat_per_point(hh):
    """FY2040 VAT a household pays per point, by fifth, nominal $ (gross)."""
    import provisions as P
    gross = K.VAT_POINT_2040 / (1 - K.EXCISE_OFFSET)
    d = P.dist([('consumption', gross * 10 / 1000)], hh.D.K)
    return {g: hh.D.per_hh(d[g], g) for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')}


def build():
    import health_cost_review as HC
    import health_financing as HF
    ctx = K.Context()
    hh = K.Household()
    per_point = quintile_vat_per_point(hh)
    hctx = HF.context()
    case = HC.cost_cases(HC._g40())['design']
    fold = HC.h1b_restated(hctx)['fold_into_s_points']
    X = HF.keys()[4]
    units = X['B']['units']
    g5 = {h['hh']: h['g5'] for h in X['B']['households']}
    hh_units = {}
    for u in units:
        hh_units.setdefault(u['hh'], []).append(u)
    hgrow = 1.048 ** 11 / hctx['price_2040']
    igrow = X['grow'] / hctx['price_2040']
    HC._setup_visible(hctx)
    g, oop = HC._setup_visible(hctx)
    partb = HC.PART_B_2026 * HC.REAL_HEALTH_2040
    out = {}
    for label, (pkg, R, low2) in G2.items():
        rate = vat_rate_2040(ctx, pkg)
        o = HC.unified_package(hctx, case, HC.unified_spec(R=R, S=5.0 + fold, hi=2.5, form='linear'))
        tally = {k: [0.0, 0.0] for k in ('workers', 'workers_no_vat', 'workers_below_200fpl', 'workers_250_400fpl',
                                         'others_b', 'others_a', 'others_ss_ssi_a', 'others_other_a')}
        for u in units:
            members = hh_units[u['hh']]
            share = max(u['n_people'], 1) / sum(max(v['n_people'], 1) for v in members)
            q = 'Q%d' % g5.get(u['hh'], 3)
            vat = rate * per_point[q] / hctx['price_2040'] * share
            agi = u['t_agi'] * igrow
            fs = 'joint' if u['t_fs'] == 'joint' else 'single'
            n = max(u['n_people'], 1)
            kind = 'job' if u['n_employer_cov'] > 0 else ('own' if u['n_marketplace'] > 0 else
                                                          ('medicaid' if u['n_medicaid'] > 0 else
                                                           ('medicare' if u['n_medicare'] > 0 else 'uninsured')))
            prem = u['premiums_paid'] * hgrow
            oo = (u['n_employer_cov'] * oop['esi'] + u['n_marketplace'] * oop['ng_sub'] + u['n_medicaid'] * oop['medicaid']
                  + u['n_medicare'] * oop['medicare']
                  + max(n - u['n_employer_cov'] - u['n_marketplace'] - u['n_medicaid'] - u['n_medicare'], 0)
                  * oop['uninsured']) + u['n_medicare'] * partb
            today, plan = HC.visible(agi, fs, n, kind, prem if kind == 'job' else 0.0,
                                     oo + (prem if kind != 'job' else 0.0), o, HC.fpl200(n),
                                     earn=HC.earn_unit(u) * igrow, low2=low2)
            w = u['weight']
            pov = agi / (HC.fpl200(n) / 2)
            if HC._is_worker(u):
                for k, ok in (('workers', plan + vat <= today), ('workers_no_vat', plan <= today)):
                    tally[k][0] += w
                    tally[k][1] += w * ok
                if pov < 2:
                    tally['workers_below_200fpl'][0] += w
                    tally['workers_below_200fpl'][1] += w * (plan + vat <= today)
                if 2.5 <= pov < 4:
                    tally['workers_250_400fpl'][0] += w
                    tally['workers_250_400fpl'][1] += w * (plan + vat <= today)
            else:
                cola = rate / 100 * (u['ss'] + u['ssi']) * igrow
                vat_a = max(vat - cola, 0.0)
                for k, ok in (('others_b', plan + vat <= today), ('others_a', plan + vat_a <= today)):
                    tally[k][0] += w
                    tally[k][1] += w * ok
                k = 'others_ss_ssi_a' if (u['ss'] + u['ssi']) > 0.5 * max(u['cash'], 1) else 'others_other_a'
                tally[k][0] += w
                tally[k][1] += w * (plan + vat_a <= today)
        out[label] = dict(vat_rate_2040=rate, **{k: round(100 * v[1] / v[0], 1) if v[0] else None for k, v in tally.items()})
    return dict(status='exploratory: the take-home test with the VAT counted (review B-3)', per_point_fy2040=per_point,
                options=out)


def markdown(d):
    L = ['## The take-home test with the VAT counted', '',
         'Share of tax units whose visible health costs plus the VAT fall under the plan, FY2040. Each option at the '
         'VAT rate its package needs in FY2040. Generated by `models/tools/financing-protection/take_home_vat.py`. '
         'Rough: the VAT is allocated by fifth on D3\'s consumption key (see the file\'s header).', '',
         '| Memo G2 option | VAT, FY2040 | Workers ahead (health costs only) | Workers ahead, VAT counted | '
         'Below 200% of poverty | 250-400% of poverty | Retirees and others, (b) | Retirees and others, (a) | '
         'Of them: mostly Social Security or SSI, (a) | Mostly other income, (a) |',
         '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for k, v in d['options'].items():
        L.append('| %s | %.2f%% | %s%% | **%s%%** | %s%% | %s%% | %s%% | %s%% | %s%% | %s%% |' % (
            k, v['vat_rate_2040'], v['workers_no_vat'], v['workers'], v['workers_below_200fpl'], v['workers_250_400fpl'],
            v['others_b'], v['others_a'], v['others_ss_ssi_a'], v['others_other_a']))
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--markdown', action='store_true')
    d = build()
    print(markdown(d) if ap.parse_args().markdown else json.dumps(d, indent=1, default=str))
