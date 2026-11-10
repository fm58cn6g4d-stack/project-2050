#!/usr/bin/env python3
"""Project arithmetic for dossiers/care/research-s1506-comparison.md, part (b): the employer wave.

Not part of the coverage model and not an official score. It reuses the coverage model's own inputs and
single-payer formulas (models/tools/health-coverage/model.py, project central variant) to split the single
plan's 2032 net federal cost by the group that moves, then prices four employer-timing options over FY2030-39
on a 2037 endpoint, using the model's growth path and its staged path (staged_full_kids) for wave 1.

    python3 dossiers/care/tools/employer_wave.py

Simplifications, all labeled in the note: each group is moved at the single plan's target rate (1.15 times
Medicare) with no glide path; wave 1 is the model's staged path (children's stage moved from 2035 to 2031 is
not re-run); Medicare enrollees and long-term care join at the endpoint in every option; people the staged path
has already moved (Medicare at 60, the public option) are not netted out of the later waves.
"""
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
MODEL = os.path.join(ROOT, 'models', 'tools', 'health-coverage')
sys.path.insert(0, MODEL)
import model as M  # noqa: E402

YEARS = list(range(2030, 2040))
ENDPOINT = 2037
WAVE2 = 2034  # midpoint of memo 2's wave 2 (2033-35)


def split_2032():
    rows = M.load_inputs()
    I = M.central(rows)
    scn, _ = M.load_scenarios()
    P, over = M.scenario_params(scn, 'single_payer_project_central', rows)
    I.update(over)
    B = M.build_base(I)
    res = M.run_single_payer(I, B, P)
    S, c, adm, g = B['S'], B['c'], B['adm'], B['gross']
    ng = g['ng_sub'] + g['ng_unsub']
    esi_sh = g['esi'] / (g['esi'] + ng)
    # out-of-pocket spending inside the plan, split by today's coverage source on the model's shares
    oop_in = S['oop'] - B['oop_pp']['unins'] * sum(B['cells0']['uninsured']) / 1000 \
        - B['oop_pp']['other'] * sum(B['cells0']['other']) / 1000
    cnt = {'esi': g['esi'], 'medicare': g['medicare'], 'medicaid': g['medicaid'], 'ng': ng}
    oopg = {k: B['oop_pp'][k] * n / 1000 for k, n in cnt.items()}
    k = oop_in / sum(oopg.values())
    oopg = {key: v * k for key, v in oopg.items()}
    r, rx, d = I['sp_rate_pct_medicare'], I['nhe_rx'] / I['nhe_total_2024'], I['sp_drug_cut']
    u = I['sp_util_uplift'] * (1 - I['sp_unmet_share'])
    a = I['sp_admin']

    def plan(amount, payer):  # today's claims repriced to the plan's rates, more use, plan administration
        return amount * (1 - adm[payer]) * ((1 - rx) * (r / c[payer]) + rx * (1 - d)) * (1 + u) / (1 - a)

    sp = res['single_payer']
    cost = {
        'medicare': plan(S['medicare'], 'medicare') + plan(oopg['medicare'], 'oop'),
        'medicaid': plan(S['medicaid'], 'medicaid') + plan(oopg['medicaid'], 'oop'),
        'employer': plan(S['phi'] * esi_sh, 'phi') + plan(oopg['esi'], 'oop'),
        'individual': plan(S['phi'] * (1 - esi_sh), 'phi') + plan(oopg['ng'], 'oop'),
    }
    today = {'medicare': S['medicare'] + oopg['medicare'], 'medicaid': S['medicaid'] + oopg['medicaid'],
             'employer': S['phi'] * esi_sh + oopg['esi'], 'individual': S['phi'] * (1 - esi_sh) + oopg['ng']}
    net = {
        'medicare': cost['medicare'] - I['sub_medicare'],
        'medicaid': cost['medicaid'] - I['sub_medicaid'] - sp['state_and_retained_bn'],
        'employer': cost['employer'] - I['sub_esi'],
        'individual': cost['individual'] - I['sub_ptc'],
        'uninsured': sp['new_use_bn'] / (1 - a),
        'ltc': sp['ltc_bn'] / (1 - a),
    }
    esi_prem = S['phi'] * esi_sh
    facts = {
        'people_millions': {'employer': g['esi'], 'individual': ng, 'medicaid': g['medicaid'],
                            'medicare': g['medicare'], 'uninsured': I['cbo_unins']},
        'national_change': {key: cost[key] - today[key] for key in cost},
        'employer_premiums_total': esi_prem,
        'employer_share': res['private_flows_removed_bn']['employer_premiums'],
        'employer_oop': oopg['esi'],
        'tax_exclusion': I['sub_esi'],
        'tax_rate_on_premiums': I['sub_esi'] / esi_prem,
        'model_net': sp['amount_to_be_financed_bn'],
    }
    return net, facts


def options(net, facts):
    gf, _, cagr = M.growth_paths(I_global())
    res = json.load(open(os.path.join(MODEL, 'results.json')))
    base = {r['year']: r['federal_bn'] for r in res['fy2030_39']['staged_full_kids']['series']}
    full = {y: facts['model_net'] * gf[y] for y in YEARS}

    def path(moves):
        out = {}
        for y in YEARS:
            if y >= ENDPOINT:
                out[y] = full[y]
                continue
            out[y] = base[y] + sum(share * net[grp] * gf[y] for grp, start, share in moves if y >= start)
        return out

    emp, tau = facts['employer_share'], facts['tax_rate_on_premiums']

    def contribution(share, start, take=1.0):
        # an employer contribution of `share` of today's employer premiums, net of the income and payroll tax the
        # same money would have raised as wages (the model's tax-exclusion offset), from `start` to the endpoint
        return sum(take * share * emp * (1 - tau) * gf[y] for y in YEARS if start <= y < ENDPOINT)

    opts = {
        'A. Employers last (memo 2 as decided)': (path([('medicaid', WAVE2, 1.0)]), 0.0),
        'B. Employer groups with Medicaid in wave 2': (path([('medicaid', WAVE2, 1.0), ('employer', WAVE2, 1.0)]), 1.0),
        'C. Voluntary early opt-in (25%, range 10-40%)': (path([('medicaid', WAVE2, 1.0), ('employer', WAVE2, 0.25)]), 0.25),
        'D. Employer groups in wave 2, Medicaid at the endpoint': (path([('employer', WAVE2, 1.0)]), 1.0),
    }
    out = {}
    for name, (series, take) in opts.items():
        out[name] = {'series': series, 'total': sum(series.values()),
                     'with_contribution_71': sum(series.values()) - contribution(0.71, WAVE2, take),
                     'with_contribution_80': sum(series.values()) - contribution(0.80, WAVE2, take)}
    for lo_hi, take in (('C low (10%)', 0.10), ('C high (40%)', 0.40)):
        s = path([('medicaid', WAVE2, 1.0), ('employer', WAVE2, take)])
        out[lo_hi] = {'series': s, 'total': sum(s.values()), 'with_contribution_80': sum(s.values()) - contribution(0.80, WAVE2, take)}
    out['_check: everyone else at the endpoint'] = {'total': sum(path([]).values())}
    out['_fy2040'] = facts['model_net'] * gf[2039] * (1 + cagr)
    return out


_I = None


def I_global():
    global _I
    if _I is None:
        _I = M.central(M.load_inputs())
    return _I


def main():
    net, f = split_2032()
    print('2032 net federal cost of the single plan, by the group that moves ($ billion; project arithmetic)')
    for k, v in net.items():
        print(f'  {k:11s} {v:7.0f}')
    print(f'  {"sum":11s} {sum(net.values()):7.0f}  (model: {f["model_net"]:.0f})')
    print('people today, millions (CBO 2032, gross of double counting):',
          {k: round(v, 1) for k, v in f['people_millions'].items()})
    print('change in national spending when the group moves, 2032 ($ billion):',
          {k: round(v) for k, v in f['national_change'].items()})
    print(f'employer-group premiums {f["employer_premiums_total"]:.0f}, employer share {f["employer_share"]:.0f}, '
          f'their out-of-pocket {f["employer_oop"]:.0f}, tax exclusion {f["tax_exclusion"]:.0f} '
          f'(implied rate {f["tax_rate_on_premiums"]:.3f})')
    be = net['employer'] / (f['employer_share'] * (1 - f['tax_rate_on_premiums']))
    print(f'employer contribution, as a share of today\'s employer premiums, at which moving employer groups costs '
          f'the federal budget nothing: {be:.2f}')
    print('\nFY2030-39 federal cost on a 2037 endpoint ($ trillion; contribution from 2034 to the endpoint)')
    for k, v in options(net, f).items():
        if k == '_fy2040':
            print(f'  FY2040, any path at the endpoint: {v / 1000:.2f}')
            continue
        line = f'  {k:55s} {v["total"] / 1000:6.2f}'
        if 'with_contribution_71' in v:
            line += f'   with 71% contribution {v["with_contribution_71"] / 1000:6.2f}'
        if 'with_contribution_80' in v:
            line += f'   with 80% {v["with_contribution_80"] / 1000:6.2f}'
        print(line)


if __name__ == '__main__':
    main()
