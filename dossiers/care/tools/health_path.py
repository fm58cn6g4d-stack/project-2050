#!/usr/bin/env python3
"""Project arithmetic for dossiers/care/6-cost.md: the decided health design priced year by year.

Not part of the coverage model and not an official score. It reuses the coverage model's inputs and single-plan
formulas (models/tools/health-coverage/model.py) for the design Espen decided (DEC-2026-11-10-09, -11):

  - the single plan at full scale: rates about 1.15 times Medicare (memo 5 B), comprehensive benefits with small
    capped copays above 200% of poverty (memo 4 C: the model's "low" cost sharing), long-term care left to part B
    (sp_ltc = 0), states paying half their Medicaid spending (memo 3 B's working figure);
  - the order (memo 2 by payer, children first; DEC-2026-11-10-11): 2030 restoration; wave 1 in 2031 (the uninsured,
    the individual market and every child, plus Medicare at 60); wave 2 in 2033-35 (Medicaid and employer groups, a
    third of each on January 1 of 2033, 2034 and 2035, a working assumption); the endpoint, January 1, 2035
    (everyone else, including today's Medicare enrollees);
  - the hospital glide path (memo 2 protection 3): hospital rates start in 2031 at today's all-payer hospital
    average and fall in a straight line to the target over five years (2036);
  - the employer transitional contribution (DEC-2026-11-10-11): a share of the employer's current premium for the
    coverage it no longer provides, from each move until the financing settlement's payroll contribution starts.

    python3 dossiers/care/tools/health_path.py           # tables for 6-cost.md
    python3 dossiers/care/tools/health_path.py --json    # the same numbers as JSON

Simplifications, each labeled in 6-cost.md: each group's 2032 cost is grown on the model's growth path (CBO's growth
in net federal health subsidies); each fiscal year takes a quarter of the calendar year before it and three quarters
of its own (FY2031 runs from October 2030), so a January move counts for nine months of its first fiscal year
(review of the milestone, F-2); people restored to Medicaid in
2030 are counted with the uninsured who join the plan in 2031; children's share of Medicaid spending is an assumption
(CHILD_MCD_SHARE); the glide path is applied to hospital claims only, as a hospital share of non-drug claims; items
the model does not price (the Medicare upgrades, the Advantage fix, worker help, the hospital transition fund and the
smaller lines) are added in 6-cost.md, not here, except the Advantage fix and upgrades, shown as separate lines.
"""
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
MODEL = os.path.join(ROOT, 'models', 'tools', 'health-coverage')
sys.path.insert(0, MODEL)
import model as M  # noqa: E402

YEARS = list(range(2030, 2040))
WAVE1 = 2031
WAVE2 = (2033, 2034, 2035)          # a third of Medicaid and of employer groups each January
ENDPOINT = 2035
GLIDE_START, GLIDE_YEARS = 2031, 5  # hospital rates reach the target in 2036
TARGET = 1.15
CHILD_MCD_SHARE = 0.20              # children's share of Medicaid and CHIP spending (assumption; range 0.15-0.25)
NEUTRAL = None                      # computed: the employer contribution share that makes employer moves cost nothing


def setup():
    rows = M.load_inputs()
    I = M.central(rows)
    I['sp_rate_pct_medicare'] = TARGET
    B = M.build_base(I)
    P = {'sp': 1.0, 'sp_rate_basis': 'medicare', 'sp_cs': 'low', 'sp_ltc': 0.0}
    return I, B, P


def model_full(I, B, P):
    """The coverage model's own single-plan result for the decided variant (the check on the group split)."""
    return M.run_single_payer(I, B, P)


def groups(I, B, P, hosp_rate=TARGET):
    """Net 2032 federal cost of moving each group into the single plan, at the target rate for physicians and other
    services and at `hosp_rate` for hospital claims. Returns (net, cost, today, facts)."""
    S, c, adm = B['S'], B['c'], B['adm']
    g = B['gross']
    ng = g['ng_sub'] + g['ng_unsub']
    esi_sh = g['esi'] / (g['esi'] + ng)
    oop_in = S['oop'] - B['oop_pp']['unins'] * sum(B['cells0']['uninsured']) / 1000 \
        - B['oop_pp']['other'] * sum(B['cells0']['other']) / 1000
    cnt = {'esi': g['esi'], 'medicare': g['medicare'], 'medicaid': g['medicaid'], 'ng': ng}
    oopg = {k: B['oop_pp'][k] * n / 1000 for k, n in cnt.items()}
    k = oop_in / sum(oopg.values())
    oopg = {key: v * k for key, v in oopg.items()}
    rx, d = I['nhe_rx'] / I['nhe_total_2024'], I['sp_drug_cut']
    wh = I['nhe_hospital'] / (I['nhe_hospital'] + I['nhe_physician'])
    u = I['sp_util_uplift'] * 0.5 * (1 - I['sp_unmet_share'])   # memo 4 C: the model's low cost sharing
    a, cs = I['sp_admin'], I['sp_cs_low_rate']
    r_eff = (1 - wh) * TARGET + wh * hosp_rate                    # rate on non-drug claims

    def plan(amount, payer):  # today's claims repriced, more use, administration, less cost sharing
        return amount * (1 - adm[payer]) * ((1 - rx) * (r_eff / c[payer]) + rx * (1 - d)) * (1 + u) * (1 / (1 - a) - cs)

    cost = {
        'medicare': plan(S['medicare'], 'medicare') + plan(oopg['medicare'], 'oop'),
        'medicaid': plan(S['medicaid'], 'medicaid') + plan(oopg['medicaid'], 'oop'),
        'employer': plan(S['phi'] * esi_sh, 'phi') + plan(oopg['esi'], 'oop'),
        'individual': plan(S['phi'] * (1 - esi_sh), 'phi') + plan(oopg['ng'], 'oop'),
    }
    today = {'medicare': S['medicare'] + oopg['medicare'], 'medicaid': S['medicaid'] + oopg['medicaid'],
             'employer': S['phi'] * esi_sh + oopg['esi'], 'individual': S['phi'] * (1 - esi_sh) + oopg['ng']}
    # newly covered people: the model's own formula, at this rate
    claims_now = sum(S[x] * (1 - adm[x]) * ((1 - rx) * (r_eff / c[x]) + rx * (1 - d))
                     for x in ['medicare', 'medicaid', 'phi'])
    claims_now += (S['oop'] - B['oop_pp']['unins'] * sum(B['cells0']['uninsured']) / 1000
                   - B['oop_pp']['other'] * sum(B['cells0']['other']) / 1000) * (1 - adm['oop']) \
        * ((1 - rx) * (r_eff / c['oop']) + rx * (1 - d))
    unins0 = sum(B['cells0']['uninsured'])
    covered_now = B['pop'] - sum(B['cells0']['other']) - unins0
    new_n = max(0.0, unins0 - I['sp_residual_unins'] * B['pop'])
    new_cost = new_n * I['new_enrollee_factor'] * claims_now * (1 + u) / covered_now * (1 / (1 - a) - cs)
    R = I['sp_state_moe'] * max(0.0, S['medicaid'] - I['sub_medicaid']) + I['sp_retained_other']
    net = {
        'medicare': cost['medicare'] - I['sub_medicare'],
        'medicaid': cost['medicaid'] - I['sub_medicaid'] - R,
        'employer': cost['employer'] - I['sub_esi'],
        'individual': cost['individual'] - I['sub_ptc'],
        'uninsured': new_cost,
    }
    kids_esi = I['win_esi_kids'] * I['age_idx_kids']           # children's share of employer-group spending
    facts = {
        'employer_premiums': S['phi'] * esi_sh,
        'employer_share': B['gross'] and None,
        'tax_exclusion': I['sub_esi'],
        'tau': I['sub_esi'] / (S['phi'] * esi_sh),
        'state_moe': R,
        'child_share_employer': kids_esi,
        'child_share_medicaid': CHILD_MCD_SHARE,
        'hospital_weight': wh,
        'people': {'employer': g['esi'], 'individual': ng, 'medicaid': g['medicaid'], 'medicare': g['medicare'],
                   'uninsured': I['cbo_unins']},
        'national_change': {key: cost[key] - today[key] for key in cost},
    }
    return net, cost, today, facts


def hospital_revenue(I, B, P, hosp_rate, net_current='all'):
    """Change in hospital revenue, 2032, when each group moves (project arithmetic). Hospital and physician rates by
    payer are the model's (commercial hospital 2.54 and physician 1.4 times Medicare; Medicaid at its fee index;
    Medicare 1.04). For the newly covered, the plan's payment for their hospital care is new revenue less what
    hospitals collect for them today (review of #220): net_current='selfpay' subtracts only their own payments
    (unins_paid_share of their current care), the high reading; 'all' also subtracts the rest of their current care
    (uncompensated care funded by Medicaid DSH, state and other payments, and cost shifting), treating all of it as
    revenue hospitals lose, the low reading. Medicaid DSH inside Medicaid's spending is repriced with it, a small
    upward bias on the Medicaid line."""
    S, c, adm = B['S'], B['c'], B['adm']
    g = B['gross']
    ng = g['ng_sub'] + g['ng_unsub']
    esi_sh = g['esi'] / (g['esi'] + ng)
    rx = I['nhe_rx'] / I['nhe_total_2024']
    wh = I['nhe_hospital'] / (I['nhe_hospital'] + I['nhe_physician'])
    u = I['sp_util_uplift'] * 0.5 * (1 - I['sp_unmet_share'])
    h = {'medicare': c['medicare'], 'medicaid': I['medicaid_fee_idx'], 'phi': I['hosp_commercial_ratio']}
    f = {'medicare': c['medicare'], 'medicaid': I['medicaid_fee_idx'], 'phi': I['phys_commercial_ratio']}
    net, _, _, _ = groups(I, B, P, hosp_rate)
    out = {}
    for grp, payer, amount in [('medicare', 'medicare', S['medicare']), ('medicaid', 'medicaid', S['medicaid']),
                               ('employer', 'phi', S['phi'] * esi_sh), ('individual', 'phi', S['phi'] * (1 - esi_sh))]:
        D = amount * (1 - adm[payer]) * (1 - rx)
        share = wh * h[payer] / (wh * h[payer] + (1 - wh) * f[payer])
        H = D * share
        out[grp] = H / h[payer] * hosp_rate * (1 + u) - H
    # newly covered: the hospital part of their new care, at the plan's rates
    a, cs = I['sp_admin'], I['sp_cs_low_rate']
    claims_new = net['uninsured'] / (1 / (1 - a) - cs)
    gain = claims_new * (1 - rx) * wh * hosp_rate / (wh * hosp_rate + (1 - wh) * TARGET)
    new_n = max(0.0, sum(B['cells0']['uninsured']) - I['sp_residual_unins'] * B['pop'])
    current = new_n * (B['oop_pp']['unins'] if net_current == 'selfpay' else B['unins_total_pp']) / 1000
    out['uninsured'] = gain - current * (1 - rx) * wh
    return out


def hospital_start(I, B):
    """Today's all-payer average hospital rate, as a multiple of Medicare (claims-weighted by payer)."""
    S, c, adm = B['S'], B['c'], B['adm']
    hosp = {'medicare': c['medicare'], 'medicaid': I['medicaid_fee_idx'], 'phi': I['hosp_commercial_ratio']}
    vol = {x: S[x] * (1 - adm[x]) / c[x] for x in hosp}
    return sum(vol[x] * hosp[x] for x in hosp) / sum(vol.values())


def rate_path(start, years=GLIDE_YEARS, begin=GLIDE_START):
    return {y: TARGET + (start - TARGET) * max(0.0, (begin + years - y) / years) if y >= begin else start
            for y in YEARS + [2040]}


def shares_moved(y):
    """Share of each group in the single plan in year y (memo 2's order, DEC-2026-11-10-11)."""
    third = sum(1 for w in WAVE2 if y >= w) / 3.0
    full = y >= ENDPOINT
    return {
        'uninsured': 1.0 if y >= WAVE1 else 0.0,
        'individual': 1.0 if y >= WAVE1 else 0.0,
        'medicaid': 1.0 if full else (CHILD_MCD_SHARE if y >= WAVE1 else 0.0) + (1 - CHILD_MCD_SHARE) * third,
        'employer': 1.0 if full else 0.0,   # set in employer_share() (children first, then thirds)
        'medicare': 1.0 if full else 0.0,
    }


def employer_share(y, kids):
    if y >= ENDPOINT:
        return 1.0
    third = sum(1 for w in WAVE2 if y >= w) / 3.0
    return (kids if y >= WAVE1 else 0.0) + (1 - kids) * third


def path(I, B, P, glide):
    """Year-by-year net federal cost (model basis: outlays less replaced federal funding, the tax exclusion that
    ends and state maintenance of effort), before any employer contribution, plus the pieces."""
    gf, _, cagr = M.growth_paths(I)
    gf = dict(gf)
    gf[2040] = gf[2039] * (1 + cagr)
    res = json.load(open(os.path.join(MODEL, 'results.json')))
    restore = {r['year']: r['federal_bn'] for r in res['fy2030_39']['restore']['series']}
    staged = {r['year']: r['federal_bn'] for r in res['fy2030_39']['staged']['series']}
    pubopt = {r['year']: r['federal_bn'] for r in res['fy2030_39']['public_option']['series']}
    m60 = {y: staged[y] - pubopt[y] for y in staged}
    cal = {2029: {'plan': 0.0, 'other': 0.0, 'total': 0.0, 'employer_moved': 0.0, 'shares': None, 'rate': None}}
    cache = {}
    for y in YEARS + [2040]:
        r = glide[y]
        if r not in cache:
            cache[r] = groups(I, B, P, hosp_rate=r)
        net, _, _, f = cache[r]
        sh = shares_moved(y)
        sh['employer'] = employer_share(y, f['child_share_employer'])
        plan = sum(sh[k] * net[k] for k in net) * gf[y]
        extra = 0.0
        if y == 2030:
            extra = restore[2030]                      # restoration only, before wave 1
        elif y < ENDPOINT:
            extra = m60.get(y, m60[2039] * gf[y] / gf[2039])  # Medicare at 60 until the endpoint (an upper bound)
        cal[y] = {'plan': plan, 'other': extra, 'total': plan + extra, 'shares': sh, 'rate': r,
                  'employer_moved': sh['employer']}
    # fiscal years: FY y = October of y-1 to September of y
    out = {}
    for y in YEARS + [2040]:
        a, b = cal[y - 1], cal[y]
        out[y] = {k: 0.25 * a[k] + 0.75 * b[k] for k in ('plan', 'other', 'total', 'employer_moved')}
        out[y].update({'shares': b['shares'], 'rate': b['rate'], 'calendar_total': b['total'],
                       # the employer share moved times growth, on the same fiscal-year blend (review of #226)
                       'moved_gf': 0.25 * a['employer_moved'] * gf.get(y - 1, 0.0) + 0.75 * b['employer_moved'] * gf[y]})
    return out, gf


def contribution(I, B, P, series, gf, share, until=None):
    """Employer transitional contribution at `share` of today's employer premiums for the coverage moved, net of the
    income and payroll tax the same money would raise as wages (the exclusion is counted only on premiums that become
    wages). `until`: the last fiscal year it is paid (default: through FY2040, i.e. until the settlement's payroll
    contribution replaces it)."""
    _, _, _, f = groups(I, B, P)
    emp = model_full(I, B, P)['private_flows_removed_bn']['employer_premiums']
    out = {}
    for y, v in series.items():
        if until is not None and y > until:
            out[y] = 0.0
            continue
        out[y] = v['moved_gf'] * share * emp * (1 - f['tau'])
    return out, emp


def main():
    I, B, P = setup()
    full = model_full(I, B, P)
    net, cost, today, f = groups(I, B, P)
    emp = full['private_flows_removed_bn']['employer_premiums']
    neutral = net['employer'] / (emp * (1 - f['tau']))
    h0 = hospital_start(I, B)
    base_glide = rate_path(h0)
    no_glide = {y: TARGET for y in YEARS + [2040]}
    slow_glide = rate_path(h0, years=7)
    series, gf = path(I, B, P, base_glide)
    flat, _ = path(I, B, P, no_glide)
    slow, _ = path(I, B, P, slow_glide)
    c_neutral, _ = contribution(I, B, P, series, gf, neutral)
    c80, _ = contribution(I, B, P, series, gf, 0.80)
    tot = lambda s: sum(s[y]['total'] if isinstance(s[y], dict) else s[y] for y in YEARS)  # noqa: E731
    sp = full['single_payer']
    gf_, gn_, _ = M.growth_paths(I)
    hosp = {}
    for y in YEARS:
        hr = hospital_revenue(I, B, P, base_glide[y])
        hs = hospital_revenue(I, B, P, base_glide[y], 'selfpay')
        sh = series[y]['shares']
        hosp[y] = {'net': sum(sh[k] * hr[k] for k in hr) * gn_[y],
                   'net_high': sum(sh[k] * hs[k] for k in hs) * gn_[y],
                   'commercial_loss': (sh['employer'] * hr['employer'] + sh['individual'] * hr['individual']) * gn_[y]}
    exclusion = {y: series[y]['moved_gf'] * f['tax_exclusion'] for y in YEARS + [2040]}
    # half pass-through of employer-paid premiums into wages (review F-3): revenue lost against CBO's convention
    half = {s_: {y: series[y]['moved_gf'] * 0.5 * f['tau'] * emp * (1 - s_) for y in [2032, 2040]}
            for s_ in (0.0, neutral)}
    out = {
        'hospital_revenue_change': {y: {k_: round(v, 1) for k_, v in hosp[y].items()} for y in YEARS},
        'hospital_by_group_2032_at_target': {k_: round(v, 1) for k_, v in hospital_revenue(I, B, P, TARGET).items()},
        'hospital_by_group_2032_at_target_high': {k_: round(v, 1) for k_, v in
                                                  hospital_revenue(I, B, P, TARGET, 'selfpay').items()},
        'exclusion_by_year': {y: round(v, 1) for y, v in exclusion.items()},
        'half_passthrough_loss_full_scale_2032': {'no_contribution': round(0.5 * f['tau'] * emp, 1),
                                                  'neutral_contribution': round(0.5 * f['tau'] * emp * (1 - neutral), 1)},
        'half_passthrough_loss_fy2040': {str(round(k_, 3)): round(v[2040], 1) for k_, v in half.items()},
        'calendar_series': {y: round(series[y]['calendar_total'], 1) for y in YEARS + [2040]},
        'full_2032': {'net_model': full['federal']['net_change_bn'], 'net_groups': sum(net.values()),
                      'plan_outlay': sp['plan_outlay_bn'], 'cost_sharing': sp['cost_sharing_bn'],
                      'admin': sp['admin_bn'], 'state_moe': sp['state_and_retained_bn'],
                      'nhe_change': full['nhe']['change_bn'] if 'nhe' in full else None,
                      'household_removed': None, 'employer_premiums_removed': emp},
        'groups_2032': net, 'national_change_2032': f['national_change'],
        'tau': f['tau'], 'neutral_share': neutral, 'hospital_start': h0,
        'child_share_employer': f['child_share_employer'],
        'series': {y: round(series[y]['total'], 1) for y in YEARS + [2040]},
        'rate': {y: round(base_glide[y], 3) for y in YEARS + [2040]},
        'fy2030_39': tot(series), 'fy2030_39_no_glide': tot(flat), 'fy2030_39_slow_glide': tot(slow),
        'glide_cost_by_year': {y: round(series[y]['total'] - flat[y]['total'], 1) for y in YEARS + [2040]},
        'slow_glide_extra_by_year': {y: round(slow[y]['total'] - series[y]['total'], 1) for y in YEARS + [2040]},
        'contribution_neutral': {y: round(v, 1) for y, v in c_neutral.items()},
        'contribution_80': {y: round(v, 1) for y, v in c80.items()},
        'fy2030_39_with_neutral': tot(series) - sum(c_neutral[y] for y in YEARS),
        'fy2030_39_with_80': tot(series) - sum(c80[y] for y in YEARS),
        'fy2040': series[2040]['total'],
        'exclusion_2032': f['tax_exclusion'], 'employer_premiums_2032': f['employer_premiums'],
        'growth_2040': gf[2040],
    }
    if '--json' in sys.argv:
        print(json.dumps(out, indent=1, default=float))
        return
    print('Decided single plan at full scale, 2032 ($ billion; project arithmetic on the coverage model)')
    print(f"  model net federal change {out['full_2032']['net_model']:.0f}; sum of groups {sum(net.values()):.0f}")
    print(f"  plan outlay {sp['plan_outlay_bn']:.0f}, cost sharing {sp['cost_sharing_bn']:.0f}, administration "
          f"{sp['admin_bn']:.0f}, state maintenance of effort {sp['state_and_retained_bn']:.0f}")
    for k_, v in net.items():
        print(f'    {k_:11s} {v:7.0f}   national change {f["national_change"].get(k_, 0):7.0f}')
    print(f"  employer premiums {f['employer_premiums']:.0f} (employers' share {emp:.0f}), exclusion {f['tax_exclusion']:.0f}"
          f" (rate {f['tau']:.3f}); neutral contribution share {neutral:.2f}")
    print(f"  today's all-payer hospital rate {h0:.2f} x Medicare; children's share of employer spending "
          f"{f['child_share_employer']:.2f}")
    print('\nYear  rate  share-employer  net federal  glide cost  slow-glide extra  contribution(neutral)')
    for y in YEARS + [2040]:
        print(f"{y}  {base_glide[y]:.3f}  {series[y]['employer_moved']:.2f}  {series[y]['total']:9.0f}  "
              f"{out['glide_cost_by_year'][y]:8.0f}  {out['slow_glide_extra_by_year'][y]:8.0f}  {c_neutral[y]:8.0f}")
    print(f"\nFY2030-39: {out['fy2030_39'] / 1000:.2f} trillion (no glide {out['fy2030_39_no_glide'] / 1000:.2f}; "
          f"seven-year glide {out['fy2030_39_slow_glide'] / 1000:.2f}); with the neutral contribution "
          f"{out['fy2030_39_with_neutral'] / 1000:.2f}; with 80% {out['fy2030_39_with_80'] / 1000:.2f}")
    print(f"FY2040: {out['fy2040']:.0f} billion; of which the ended tax exclusion (a revenue effect) "
          f"{exclusion[2040]:.0f}, so spending net of replaced federal funding and state payments "
          f"{out['fy2040'] + exclusion[2040]:.0f}")
    print('\nHospital revenue change (all hospitals, $ billion, nominal): year, net (low to high reading), commercial loss')
    for y in YEARS:
        print(f"  {y}  {hosp[y]['net']:8.0f} to {hosp[y]['net_high']:6.0f}  {hosp[y]['commercial_loss']:8.0f}")
    print('  2032 by group at the target rate:', out['hospital_by_group_2032_at_target'])


if __name__ == '__main__':
    main()
