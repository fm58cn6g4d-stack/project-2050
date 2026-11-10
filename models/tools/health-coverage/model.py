#!/usr/bin/env python3
"""Health coverage model, first version (MOD-health-coverage). Exploratory.

Compares health design options on three things only: coverage (people by source and income band), federal
cost (federal subsidies, outlays plus forgone revenue, net of offsets) and household cost (premiums plus
out-of-pocket per person, before any new financing). One representative year (2032, a column CBO
tabulates); the FY2030-39 window grows the 2032 effects at CBO's growth in net subsidies. Standard library
only. It is not microsimulation and not an official score: see MODEL-CARD.md.

  python3 models/tools/health-coverage/model.py [--out DIR]    writes results.json, results.md, MODEL-CARD.md

Units: people in millions, money in $ billions (per-person amounts in dollars), year 2032 unless noted.
"""
import argparse, copy, csv, hashlib, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
VERSION = '0.1.0'
AS_OF = '2026-11-10'
YEAR = 2032
NYEARS = YEAR - 2024  # NHE base year to representative year
BANDS = ['<138%', '138-250%', '250-400%', '400%+']
SRCS = ['esi', 'ng_sub', 'ng_unsub', 'medicaid', 'medicaid_new', 'medicare', 'medicare_m60', 'medicare_m50',
        'medicare_kids', 'po', 'sp', 'other', 'uninsured']
LABEL = {'esi': 'Employer (ESI)', 'ng_sub': 'Marketplace, subsidized', 'ng_unsub': 'Nongroup, unsubsidized',
         'medicaid': 'Medicaid/CHIP', 'medicaid_new': 'Medicaid/CHIP, restored adults', 'medicare': 'Medicare',
         'medicare_m60': 'Medicare, new at 60-64', 'medicare_m50': 'Medicare, new at 50-59',
         'medicare_kids': "Medicare, children", 'po': 'Public option', 'sp': 'Single public plan',
         'other': 'Other (held fixed)', 'uninsured': 'Uninsured'}
WINDOWS = ['m60', 'm50', 'kids']


# ---------------------------------------------------------------- inputs and scenarios
def load_inputs(path=None):
    rows = {}
    with open(path or os.path.join(HERE, 'inputs.csv'), newline='') as f:
        for r in csv.DictReader(f):
            rows[r['id']] = dict(r, value=float(r['value']), low=float(r['low']), high=float(r['high']))
    return rows


def central(rows):
    return {k: r['value'] for k, r in rows.items()}


def load_scenarios(path=None):
    scn, order = {}, []
    with open(path or os.path.join(HERE, 'scenarios.csv'), newline='') as f:
        for r in csv.DictReader(f):
            s = r['scenario']
            if s not in scn:
                scn[s] = {}
                order.append(s)
            v = r['value']
            try:
                v = float(v)
            except ValueError:
                pass
            scn[s][r['parameter']] = v
    return scn, order


def phases(scn):
    out = {}
    for k, v in scn['_phase'].items():
        out[k] = int(v)
    return out


def phase_at(ph, comp, t):
    s, f = ph[comp + '.start'], ph[comp + '.full']
    return max(0.0, min(1.0, (t - s + 1) / (f - s + 1)))


# ---------------------------------------------------------------- baseline cells and per-person economics
def to_four(g1, g2, g3, f1, f2):
    v = [f1 * g1, (1 - f1) * g1 + f2 * g2, (1 - f2) * g2, g3]
    s = sum(v)
    return [x / s for x in v]


def build_base(I):
    """Baseline cells (CBO 2032 by source, split into four income bands) and the per-person arithmetic."""
    B = {}
    pop = I['cbo_pop']
    ng_sub_g = I['cbo_ng_mkt_sub'] + I['cbo_bhp']
    ng_unsub_g = I['cbo_ng_mkt_unsub'] + I['cbo_ng_outside']
    gross = {'esi': I['cbo_esi'], 'ng_sub': ng_sub_g, 'ng_unsub': ng_unsub_g, 'medicaid': I['cbo_medicaid'],
             'medicare': I['cbo_medicare'], 'other': I['cbo_other']}
    overlap = sum(gross.values()) + I['cbo_unins'] - pop  # people counted under two sources (CBO: 19.6, plus rounding)
    rest = 1 - I['overlap_medicaid']
    wsum = I['overlap_w_esi'] + I['overlap_w_ng'] + I['overlap_w_other']
    remove = {'medicaid': overlap * I['overlap_medicaid'],
              'esi': overlap * rest * I['overlap_w_esi'] / wsum,
              'other': overlap * rest * I['overlap_w_other'] / wsum,
              'ng_sub': overlap * rest * I['overlap_w_ng'] / wsum * ng_sub_g / (ng_sub_g + ng_unsub_g),
              'ng_unsub': overlap * rest * I['overlap_w_ng'] / wsum * ng_unsub_g / (ng_sub_g + ng_unsub_g)}
    net = {k: gross[k] - remove.get(k, 0.0) for k in gross}
    net['uninsured'] = I['cbo_unins']
    f1, f2 = I['band_f1'], I['band_f2']
    share = {}
    for src, key in [('medicaid', 'medicaid'), ('esi', 'esi'), ('other', 'other'), ('uninsured', 'unins')]:
        share[src] = to_four(I[f'grp_{key}_1'], I[f'grp_{key}_2'], I[f'grp_{key}_3'], f1, f2)
    share['ng_sub'] = to_four(I['grp_ng_1'], I['grp_ng_2'], 0.0, f1, f2)
    b3 = I['ngu_share_b3']
    share['ng_unsub'] = [0.0, 0.0, b3, 1 - b3]
    low = I['medicare_low_share']
    share['medicare'] = [0.4 * low, 0.6 * low, I['medicare_b3_share'], 1 - low - I['medicare_b3_share']]
    cells = {s: [0.0] * 4 for s in SRCS}
    for s, sh in share.items():
        cells[s] = [net[s] * x for x in sh]
    B.update(gross=gross, net=net, share=share, cells0=cells, overlap=overlap, pop=pop)
    # national spending 2032 by payer: CMS 2024 levels grown at CMS growth (EV-CAR-056)
    S = {'medicare': I['nhe_medicare'] * (1 + I['nhe_g_medicare']) ** NYEARS,
         'medicaid': I['nhe_medicaid'] * (1 + I['nhe_g_medicaid']) ** NYEARS,
         'phi': I['nhe_phi'] * (1 + I['nhe_g_phi']) ** NYEARS,
         'oop': I['nhe_oop'] * (1 + I['nhe_g_total']) ** NYEARS}
    S['other'] = (I['nhe_total_2024'] - I['nhe_medicare'] - I['nhe_medicaid'] - I['nhe_phi'] - I['nhe_oop']) \
        * (1 + I['nhe_g_total']) ** NYEARS
    B['S'] = S
    B['nhe0'] = sum(S.values())
    B['P_phi'] = S['phi'] / (gross['esi'] + ng_sub_g + ng_unsub_g) * 1000  # $ per private enrollee
    # out of pocket per person by group
    shares = {k: I[f'oop_sh_{k}'] for k in ['esi', 'medicare', 'medicaid', 'ng', 'unins', 'other']}
    tot = sum(shares.values())
    cnt = {'esi': gross['esi'], 'medicare': gross['medicare'], 'medicaid': gross['medicaid'],
           'ng': ng_sub_g + ng_unsub_g, 'unins': I['cbo_unins'], 'other': gross['other']}
    B['oop_pp'] = {k: S['oop'] * shares[k] / tot / cnt[k] * 1000 for k in shares}
    B['unins_total_pp'] = B['oop_pp']['unins'] / I['unins_paid_share']
    idx = [I[f'oop_idx_b{b}'] for b in range(1, 5)]
    B['oop_idx'] = idx
    grp_share = {'esi': share['esi'], 'medicare': share['medicare'], 'medicaid': share['medicaid'],
                 'ng': share['ng_sub'], 'unins': share['uninsured'], 'other': share['other']}
    B['oop_norm'] = {k: sum(w * i for w, i in zip(grp_share[k], idx)) for k in grp_share}
    # income per person by band
    fpl_pp = (I['fpl_single'] + I['fpl_add'] * (I['hh_size'] - 1)) / I['hh_size'] * (1 + I['fpl_growth']) ** (YEAR - 2026)
    B['inc'] = [I[f'mid_b{b}'] / 100 * fpl_pp for b in range(1, 5)]
    B['ap_orig'] = [I['ap_orig_b1'], I['ap_orig_b2'], I['ap_orig_b3'], None]
    B['ap_enh'] = [I['ap_enh_b1'], I['ap_enh_b2'], I['ap_enh_b3'], I['ap_enh_b4']]
    # calibrate the marketplace premium so the original schedule reproduces CBO's PTC and related spending
    nsub = cells['ng_sub']
    contrib = sum(nsub[b] * B['ap_orig'][b] * B['inc'][b] for b in range(3))
    B['prem_ng'] = (I['sub_ptc'] + contrib / 1000) / sum(nsub) * 1000
    # federal per-person amounts (dollars)
    B['esi_fed_pp'] = I['sub_esi'] / sum(cells['esi']) * 1000
    B['mcd_fed_pp'] = I['sub_medicaid'] / sum(cells['medicaid']) * 1000
    B['mcare_fed_pp'] = I['sub_medicare'] / sum(cells['medicare']) * 1000
    B['mcd_new_fed_pp'] = I['sub_medicaid_exp'] / I['cbo_medicaid_exp'] * 1000
    B['mcd_new_total_pp'] = B['mcd_new_fed_pp'] / I['mcd_fmap_exp']
    B['mcd_total_pp'] = S['medicaid'] / gross['medicaid'] * 1000
    B['mcare_total_pp'] = S['medicare'] / gross['medicare'] * 1000
    B['mcare_fed_share'] = I['sub_medicare'] / S['medicare']
    # price relatives
    wh = I['nhe_hospital'] / (I['nhe_hospital'] + I['nhe_physician'])
    B['c_phi'] = wh * I['hosp_commercial_ratio'] + (1 - wh) * I['phys_commercial_ratio']
    B['c'] = {'medicare': 1 + I['ma_spend_share'] * I['ma_gap'], 'medicaid': I['medicaid_fee_idx'],
              'phi': B['c_phi'], 'oop': B['c_phi']}
    B['adm'] = {'medicare': I['admin_medicare'], 'medicaid': I['admin_medicaid'], 'phi': I['admin_phi'], 'oop': 0.0}
    # Medicare-rate cost of covering one person in each age window
    B['win_cost'] = {w: B['P_phi'] * I[f'age_idx_{w}'] * (1 - I['admin_phi']) / B['c_phi'] / (1 - I['admin_medicare'])
                     for w in WINDOWS}
    B['rho'] = (1 - I['admin_phi']) * (I['po_rate_pct_medicare'] / B['c_phi']) / (1 - I['po_admin'])
    B['cliff_share'] = I['cbo_ng_mkt_unsub'] / (I['cbo_ng_mkt_unsub'] + I['cbo_ng_outside'])
    B['base_total_sub'] = I['sub_medicare'] + I['sub_medicaid'] + I['sub_esi'] + I['sub_ptc'] + I['sub_other']
    return B


# ---------------------------------------------------------------- scenario mechanics (cells and flows)
class Ctx:
    """Mutable cells plus a ledger of flows (for national spending)."""

    def __init__(self, B):
        self.cells = {s: list(v) for s, v in B['cells0'].items()}
        self.flows = []

    def move(self, frm, to, n, weights=None, spend_to=None, label=''):
        src = self.cells[frm]
        w = weights if weights is not None else [x / sum(src) if sum(src) else 0 for x in src]
        moved = 0.0
        for b in range(4):
            k = min(max(n * w[b], 0.0), src[b])
            src[b] -= k
            self.cells[to][b] += k
            moved += k
        self.flows.append({'label': label, 'from': frm, 'to': to, 'n': moved, 'spend_to': spend_to})
        return moved

    def total(self, s):
        return sum(self.cells[s])


def spend_pp(B, s):
    """National spending per person (provider revenue incl. premiums' administrative load, plus out of pocket), $."""
    oop = B['oop_pp']
    if s == 'esi':
        return B['P_phi'] + oop['esi']
    if s in ('ng_sub', 'ng_unsub'):
        return B['prem_ng'] + oop['ng']
    if s == 'po':
        return B['prem_ng'] * B['rho'] + oop['ng']
    if s == 'medicaid':
        return B['mcd_total_pp'] + oop['medicaid']
    if s == 'medicaid_new':
        return B['mcd_new_total_pp'] + oop['medicaid']
    if s == 'medicare':
        return B['mcare_total_pp'] + oop['medicare']
    if s.startswith('medicare_'):
        return B['win_cost'][s.split('_', 1)[1]] + oop['medicare']
    if s == 'uninsured':
        return B['unins_total_pp']
    return 0.0


def apply_scenario(I, B, P):
    """Apply restore, public option and Medicare-age stages to the baseline cells. Returns Ctx and context numbers."""
    C = Ctx(B)
    nf = I['new_enrollee_factor']
    restore = P.get('restore', 0)
    r_mcd = P.get('restore_medicaid', restore)
    r_mkt = P.get('restore_marketplace', restore)
    r_cred = P.get('restore_credits', restore)
    X = {'sched': 'enh' if r_cred else 'orig', 'mult': 1.0, 'red': 0.0, 'restore_medicaid': r_mcd, 'restore_credits': r_cred}
    # 1. restore: the law's coverage losses reversed, credits made permanent
    if r_mcd:
        ph = (I['law_unins_2029'] + (I['law_unins_2034'] - I['law_unins_2029']) * (YEAR - 2029) / 5) / I['law_unins_2034']
        n = I['law_mcd_unins_2034'] * ph * r_mcd
        w1 = I['restore_mcd_w1']
        C.move('uninsured', 'medicaid_new', n, [w1, 1 - w1, 0, 0], spend_pp(B, 'medicaid_new') * nf, 'restore: Medicaid')
    ngw = [I['restore_ng_w1'], I['restore_ng_w2'], 1 - I['restore_ng_w1'] - I['restore_ng_w2'], 0]
    if r_mkt:
        n = (I['mkt_insured_2030'] + (I['mkt_insured_2035'] - I['mkt_insured_2030']) * (YEAR - 2030) / 5) * r_mkt
        C.move('uninsured', 'ng_sub', n, ngw, spend_pp(B, 'ng_sub') * nf, 'restore: marketplace provisions')
    if r_cred:
        n = (I['credits_insured_2030'] + (I['credits_insured_2035'] - I['credits_insured_2030']) * (YEAR - 2030) / 5) * r_cred
        C.move('uninsured', 'ng_sub', n, ngw, spend_pp(B, 'ng_sub') * nf, 'restore: enhanced credits')
        C.move('ng_unsub', 'ng_sub', B['cliff_share'] * C.cells['ng_unsub'][3] * r_cred, [0, 0, 0, 1],
               spend_pp(B, 'ng_unsub'), 'restore: credits reach above 400% FPL')
    # 2. public option
    if P.get('po', 0):
        if P.get('po_richer', 0):
            X['mult'] = I['po_ap_mult']
        k = P.get('po_takeup_scale', 1.0)
        rho = B['rho']
        X['red'] = I['po_benchmark_pass'] * (1 - rho) * (1 if k > 0 else 0)
        C.move('uninsured', 'po', C.total('uninsured') * I['po_eligible_share'] * I['po_autoenroll_takeup'] * k * P.get('po_autoenroll', 1),
               None, spend_pp(B, 'po') * nf, 'public option: auto-enrolled uninsured')
        for src, key, prem in [('ng_sub', 'po_shift_ng_sub', B['prem_ng']), ('ng_unsub', 'po_shift_ng_unsub', B['prem_ng']),
                               ('esi', 'po_shift_esi', B['P_phi'])]:
            C.move(src, 'po', C.total(src) * I[key] * k, None, spend_pp(B, src) - prem * (1 - rho), f'public option: from {src}')
    # 3. Medicare age stages
    mk = P.get('medicare_takeup_scale', 1.0)
    for w in WINDOWS:
        if not P.get(w, 0):
            continue
        mk = P.get('medicare_takeup_scale', 1.0) * (I['m50_takeup_scale'] if w == 'm50' else 1.0)
        to = 'medicare_' + w
        cost = spend_pp(B, to)
        if w == 'kids':
            C.move('uninsured', to, C.total('uninsured') * I['win_unins_kids'] * I['kids_takeup_unins'] * mk, None, cost * nf, 'children: uninsured')
            for src in ['esi', 'ng_sub', 'ng_unsub', 'po']:
                key = 'win_esi_kids' if src == 'esi' else 'win_ng_kids'
                C.move(src, to, C.total(src) * I[key] * I['kids_switch'] * mk, None, cost, f'children: from {src}')
        else:
            C.move('uninsured', to, C.total('uninsured') * I[f'win_unins_{w}'] * I['takeup_unins_med'] * mk, None, cost * nf, f'{w}: uninsured')
            for src in ['ng_sub', 'ng_unsub', 'po']:
                C.move(src, to, C.total(src) * I[f'win_ng_{w}'] * I['takeup_ng_med'] * mk, None, cost, f'{w}: from {src}')
            C.move('esi', to, C.total('esi') * I[f'win_esi_{w}'] * I['esi_dropout_med'] * mk, None, cost, f'{w}: from esi')
    return C, X


def ptc_pp(B, X, b):
    """Premium tax credit per subsidized enrollee in band b ($): benchmark premium less required contribution."""
    if b == 3 and X['sched'] == 'orig':
        return 0.0
    ap = (B['ap_enh'] if X['sched'] == 'enh' else B['ap_orig'])[b] * X['mult']
    return max(0.0, B['prem_ng'] * (1 - X['red']) - ap * B['inc'][b])


def fed_components(I, B, C, X, P):
    """Federal subsidies by component, $ billion: outlays plus forgone revenue, CBO's definition."""
    K = {}
    K['Medicare, existing enrollees'] = sum(C.cells['medicare']) * B['mcare_fed_pp'] / 1000
    for w, name in [('m60', 'Medicare, new at 60-64'), ('m50', 'Medicare, new at 50-59'), ('kids', "Medicare, children")]:
        K[name] = sum(C.cells['medicare_' + w]) * B['mcare_fed_share'] * B['win_cost'][w] / 1000
    K['Medicaid and CHIP, existing enrollees'] = sum(C.cells['medicaid']) * B['mcd_fed_pp'] / 1000
    K['Medicaid and CHIP, restored adults'] = sum(C.cells['medicaid_new']) * B['mcd_new_fed_pp'] / 1000
    K['Medicaid financing restored (provider taxes, directed payments)'] = I['mcd_financing_restore'] * (1 if X['restore_medicaid'] else 0)
    K['Employer-coverage tax exclusion'] = sum(C.cells['esi']) * B['esi_fed_pp'] / 1000
    prem_eff = B['prem_ng'] * (1 - X['red'])
    K['Premium tax credit, marketplace'] = sum(C.cells['ng_sub'][b] * min(ptc_pp(B, X, b), prem_eff) for b in range(4)) / 1000
    prem_po = B['prem_ng'] * B['rho']
    K['Premium tax credit, public option'] = sum(C.cells['po'][b] * min(ptc_pp(B, X, b), prem_po) for b in range(4)) / 1000
    K['Other subsidies (held fixed)'] = I['sub_other']
    return K


def household(I, B, cells, X, sp=None):
    """Premiums and out of pocket per person and in total, by source and band ($ per person; $ billion)."""
    oop, idx, norm = B['oop_pp'], B['oop_idx'], B['oop_norm']
    prem_eff = B['prem_ng'] * (1 - X['red'])
    prem_po = B['prem_ng'] * B['rho']
    grp = {'esi': 'esi', 'ng_sub': 'ng', 'ng_unsub': 'ng', 'po': 'ng', 'medicaid': 'medicaid', 'medicaid_new': 'medicaid',
           'medicare': 'medicare', 'medicare_m60': 'medicare', 'medicare_m50': 'medicare', 'medicare_kids': 'medicare',
           'other': 'other', 'uninsured': 'unins'}
    pp = {}
    for s in SRCS:
        if s == 'sp':
            continue
        row = []
        for b in range(4):
            o = oop[grp[s]] * idx[b] / norm[grp[s]]
            if s == 'esi':
                p = I['esi_employee_share'] * B['P_phi']
            elif s == 'ng_sub':
                p = prem_eff - min(ptc_pp(B, X, b), prem_eff)
            elif s == 'ng_unsub':
                p = prem_eff
            elif s == 'po':
                p = prem_po - min(ptc_pp(B, X, b), prem_po)
            elif s.startswith('medicare'):
                p = I['medicare_prem_pp']
            else:
                p = 0.0
            row.append((p, o))
        pp[s] = row
    if sp is not None:  # single public plan: no premiums, cost sharing only
        pp['sp'] = [(0.0, sp['oop_pp'][b]) for b in range(4)]
    return pp


def summarize_people(cells):
    return {s: sum(v) for s, v in cells.items()}


def run(I, P, B=None):
    """One scenario, one input set -> results dict."""
    B = B or build_base(I)
    base_cells = B['cells0']
    if P.get('sp', 0):
        return run_single_payer(I, B, P)
    C, X = apply_scenario(I, B, P)
    K = fed_components(I, B, C, X, P)
    base_C = Ctx(B)
    K0 = fed_components(I, B, base_C, {'sched': 'orig', 'mult': 1.0, 'red': 0.0, 'restore_medicaid': 0, 'restore_credits': 0}, {})
    dK = {k: K[k] - K0[k] for k in K}
    gross = sum(v for v in dK.values() if v > 0)
    offsets = -sum(v for v in dK.values() if v < 0)
    nhe_d = sum(f['n'] * ((f['spend_to'] if f['spend_to'] is not None else spend_pp(B, f['to'])) - spend_pp(B, f['from']))
                for f in C.flows) / 1000
    if P.get('po', 0):  # private premiums fall as the public option competes
        nhe_d -= (C.total('ng_sub') + C.total('ng_unsub')) * B['prem_ng'] * X['red'] / 1000
    hh = household(I, B, C.cells, X)
    res = assemble(I, B, C.cells, K, dK, gross, offsets, nhe_d, hh, X)
    res['flows'] = [dict(label=f['label'], frm=f['from'], to=f['to'], millions=round(f['n'], 4)) for f in C.flows]
    return res


def assemble(I, B, cells, K, dK, gross, offsets, nhe_d, hh, X, extra=None):
    people = summarize_people(cells)
    unins0 = sum(B['cells0']['uninsured'])
    emp = sum(cells['esi']) * (1 - I['esi_employee_share']) * B['P_phi'] / 1000
    emp0 = sum(B['cells0']['esi']) * (1 - I['esi_employee_share']) * B['P_phi'] / 1000
    by_band, tot_prem, tot_oop = [], 0.0, 0.0
    for b in range(4):
        n = sum(cells[s][b] for s in cells)
        pr = sum(cells[s][b] * hh[s][b][0] for s in cells if s in hh) / 1000
        oo = sum(cells[s][b] * hh[s][b][1] for s in cells if s in hh) / 1000
        by_band.append({'band': BANDS[b], 'people': n, 'premiums_bn': pr, 'oop_bn': oo,
                        'per_person': (pr + oo) / n * 1000 if n else 0.0})
        tot_prem += pr
        tot_oop += oo
    by_source = {}
    for s in cells:
        if s in hh and sum(cells[s]) > 1e-9:
            n = sum(cells[s])
            by_source[s] = {'people': n, 'premium_pp': sum(cells[s][b] * hh[s][b][0] for b in range(4)) / n,
                            'oop_pp': sum(cells[s][b] * hh[s][b][1] for b in range(4)) / n}
    res = {'cells': cells, 'people': people, 'uninsured': people['uninsured'], 'uninsured_change': people['uninsured'] - unins0,
           'insured_change': -(people['uninsured'] - unins0),
           'nhe_change_bn': nhe_d, 'nhe_bn': B['nhe0'] + nhe_d,
           'federal': {'components_bn': K, 'delta_components_bn': dK, 'gross_new_bn': gross, 'offsets_bn': offsets,
                       'net_change_bn': gross - offsets, 'total_subsidies_bn': sum(K.values())},
           'household': {'by_band': by_band, 'by_source': by_source, 'premiums_bn': tot_prem, 'oop_bn': tot_oop,
                         'total_bn': tot_prem + tot_oop, 'employer_premiums_bn': emp,
                         'matrix': {s: [(hh[s][b][0] + hh[s][b][1]) if cells[s][b] > 1e-9 else None for b in range(4)] for s in cells if s in hh}},
           'private_flows_removed_bn': {'household_premiums_and_oop': None, 'employer_premiums': emp0 - emp}}
    if extra:
        res.update(extra)
    return res


# ---------------------------------------------------------------- single payer
def run_single_payer(I, B, P):
    S, c, adm = B['S'], dict(B['c']), dict(B['adm'])
    ma_ffs = P.get('sp_ma_to_ffs', 1)
    claims0 = {g: S[g] * (1 - adm[g]) for g in ['medicare', 'medicaid', 'phi', 'oop']}
    if P.get('sp_rate_basis', 'medicare') == 'blended':
        r = sum(claims0.values()) / sum(claims0[g] / c[g] for g in claims0) * P.get('sp_rate_factor', 1.0)
    else:
        r = I['sp_rate_pct_medicare']
    rx = I['nhe_rx'] / I['nhe_total_2024']
    d = I['sp_drug_cut']
    claims1 = {}
    for g in claims0:
        cg = c[g] if (g != 'medicare' or ma_ffs) else 1.0
        claims1[g] = claims0[g] * ((1 - rx) * (r / cg) + rx * (1 - d))
    cs_low = P.get('sp_cs', 'none') == 'low'
    u = I['sp_util_uplift'] * (0.5 if cs_low else 1.0) * (1 - I['sp_unmet_share'])
    C1 = sum(claims1.values()) * (1 + u)
    unins0 = sum(B['cells0']['uninsured'])
    resid = I['sp_residual_unins'] * B['pop']
    covered_now = B['pop'] - sum(B['cells0']['other']) - unins0
    new_n = max(0.0, unins0 - resid)
    avg_pp = C1 / covered_now * 1000
    new_spend = new_n * max(0.0, I['new_enrollee_factor'] * avg_pp - B['unins_total_pp']) / 1000
    ltc = I['sp_ltc_added'] * P.get('sp_ltc', 0)
    Cc = C1 + new_spend + ltc  # provider revenue under the plan
    adm_sp = I['sp_admin']
    A = Cc * adm_sp / (1 - adm_sp)
    cs = I['sp_cs_low_rate'] if cs_low else 0.0
    oop_sp = cs * Cc
    plan_gross = Cc + A
    plan_outlay = plan_gross - oop_sp
    R = I['sp_state_moe'] * max(0.0, S['medicaid'] - I['sub_medicaid']) + I['sp_retained_other']
    replaced = {'Medicare subsidies replaced': I['sub_medicare'], 'Medicaid and CHIP federal funding replaced': I['sub_medicaid'],
                'Premium tax credit and related spending replaced': I['sub_ptc'],
                'Employer-coverage tax exclusion ended': I['sub_esi']}
    dK = {'Single-payer plan outlays, net of cost sharing': plan_outlay,
          'State maintenance of effort and other retained non-federal flows': -R}
    for k, v in replaced.items():
        dK[k] = -v
    gross = plan_outlay
    offsets = R + sum(replaced.values())
    net = gross - offsets
    nhe_sp = plan_gross + S['other']
    # cells: everyone except other coverage and the residual uninsured is in the plan
    cells = {s: [0.0] * 4 for s in SRCS}
    cells['other'] = list(B['cells0']['other'])
    ush = B['share']['uninsured']
    cells['uninsured'] = [resid * x for x in ush]
    allb = [sum(B['cells0'][s][b] for s in B['cells0']) for b in range(4)]
    cells['sp'] = [allb[b] - cells['other'][b] - cells['uninsured'][b] for b in range(4)]
    idx = B['oop_idx']
    wt = sum(cells['sp'][b] * idx[b] for b in range(4))
    oop_pp_sp = [oop_sp * 1000 * idx[b] / wt if wt else 0.0 for b in range(4)]
    X = {'sched': 'orig', 'mult': 1.0, 'red': 0.0, 'restore_medicaid': 0, 'restore_credits': 0}
    hh = household(I, B, cells, X, sp={'oop_pp': oop_pp_sp})
    K = {'Single-payer plan outlays, net of cost sharing': plan_outlay, 'Less: state maintenance of effort and retained flows': -R,
         'Other subsidies (held fixed)': I['sub_other']}
    res = assemble(I, B, cells, K, dK, gross, offsets, nhe_sp - B['nhe0'], hh, X)
    res['federal']['total_subsidies_bn'] = B['base_total_sub'] + net
    res['single_payer'] = {'rate_multiple_of_medicare': r, 'provider_revenue_bn': Cc, 'claims_before_use_bn': sum(claims1.values()),
                           'use_increase': u, 'newly_covered_millions': new_n, 'new_use_bn': new_spend, 'ltc_bn': ltc,
                           'admin_bn': A, 'cost_sharing_bn': oop_sp, 'plan_gross_bn': plan_gross, 'plan_outlay_bn': plan_outlay,
                           'state_and_retained_bn': R, 'baseline_claims_bn': sum(claims0.values()),
                           'amount_to_be_financed_bn': net}
    return res


# ---------------------------------------------------------------- the whole scenario set
def scenario_params(scn, name, I_rows):
    """Split scenario rows into policy switches and input overrides."""
    P, over = {}, {}
    for k, v in scn[name].items():
        if k.startswith('_'):
            continue
        (over if k in I_rows else P)[k] = v
    return P, over


def evaluate(I_rows, scn, name, override=None):
    I = central(I_rows)
    P, over = scenario_params(scn, name, I_rows)
    I.update(over)
    if override:
        I.update(override)
    return run(I, P)


def metrics(res):
    return {'fed': res['federal']['net_change_bn'], 'nhe': res['nhe_change_bn'], 'unins': res['uninsured']}


def uncertainty(I_rows, scn, name):
    base = metrics(evaluate(I_rows, scn, name))
    P, over = scenario_params(scn, name, I_rows)
    oat = []
    for k, row in I_rows.items():
        if row['low'] == row['high'] or k in over:
            continue
        lo = metrics(evaluate(I_rows, scn, name, {k: row['low']}))
        hi = metrics(evaluate(I_rows, scn, name, {k: row['high']}))
        oat.append({'input': k, 'low_value': row['low'], 'high_value': row['high'], 'fed_at_low': lo['fed'], 'fed_at_high': hi['fed'],
                    'nhe_at_low': lo['nhe'], 'nhe_at_high': hi['nhe'], 'unins_at_low': lo['unins'], 'unins_at_high': hi['unins'],
                    'swing': abs(hi['fed'] - lo['fed'])})
    oat.sort(key=lambda r: (-r['swing'], r['input']))
    ranged = {k: r for k, r in I_rows.items() if r['low'] != r['high'] and k not in over}
    corners = {}
    corners['all_low'] = metrics(evaluate(I_rows, scn, name, {k: r['low'] for k, r in ranged.items()}))
    corners['all_high'] = metrics(evaluate(I_rows, scn, name, {k: r['high'] for k, r in ranged.items()}))
    lowcost, highcost = {}, {}
    for r in oat:
        lo_cheaper = r['fed_at_low'] <= r['fed_at_high']
        lowcost[r['input']] = r['low_value'] if lo_cheaper else r['high_value']
        highcost[r['input']] = r['high_value'] if lo_cheaper else r['low_value']
    corners['cost_min'] = metrics(evaluate(I_rows, scn, name, lowcost))
    corners['cost_max'] = metrics(evaluate(I_rows, scn, name, highcost))
    return {'central': base, 'corners': corners, 'tornado': oat[:5], 'n_ranged_inputs': len(oat)}


# ---------------------------------------------------------------- FY2030-39 window
def growth_paths(I):
    net = {y: I[f'net_sub_{y}'] for y in range(2030, 2037)}
    cagr = (net[2036] / net[2032]) ** (1 / 4) - 1
    for y in range(2037, 2040):
        net[y] = net[y - 1] * (1 + cagr)
    gf = {y: net[y] / net[2032] for y in net}
    gn = {y: (1 + I['nhe_g_total']) ** (y - YEAR) for y in range(2030, 2040)}
    return gf, gn, cagr


def fy_series(I, ph, comps):
    """comps: [(phase_key, fed_2032, nhe_2032)]; effect(t) = effect_2032 x growth(t) x phase(t)."""
    gf, gn, _ = growth_paths(I)
    out = []
    for t in range(2030, 2040):
        fed = sum(f * gf[t] * phase_at(ph, k, t) for k, f, n in comps)
        nhe = sum(n * gn[t] * phase_at(ph, k, t) for k, f, n in comps)
        out.append({'year': t, 'federal_bn': fed, 'nhe_bn': nhe})
    return out


def window_total(series):
    return {'federal_bn': sum(r['federal_bn'] for r in series), 'nhe_bn': sum(r['nhe_bn'] for r in series)}


def build_all(rows=None, scn=None, order=None):
    rows = rows or load_inputs()
    if scn is None:
        scn, order = load_scenarios()
    I0 = central(rows)
    ph = phases(scn)
    results = {name: evaluate(rows, scn, name) for name in order if not name.startswith('_')}
    m = {n: metrics(r) for n, r in results.items()}
    base_hh = results['baseline_2029']['household']['total_bn']
    for r in results.values():
        r['private_flows_removed_bn']['household_premiums_and_oop'] = base_hh - r['household']['total_bn']
    # the staged scenarios stack the same increments; the public option scenario is restore plus the PO increment
    def delta(a, b):
        return (m[a]['fed'] - m[b]['fed'], m[a]['nhe'] - m[b]['nhe'])
    seq = {
        'restore': [('restore',) + delta('restore', 'baseline_2029')],
        'public_option': [('restore',) + delta('restore', 'baseline_2029'), ('po',) + delta('public_option', 'restore')],
        'staged': [('restore',) + delta('restore', 'baseline_2029'), ('po',) + delta('public_option', 'restore'),
                   ('m60',) + delta('staged', 'public_option')],
    }
    seq['staged_full'] = seq['staged'] + [('m50',) + delta('staged_full', 'staged')]
    seq['staged_full_kids'] = seq['staged_full'] + [('kids',) + delta('staged_full_kids', 'staged_full')]
    for n in ['single_payer_cbo_like', 'single_payer_cbo_like_high', 'single_payer_cbo_like_low', 'single_payer_project_central']:
        seq[n] = [('sp', m[n]['fed'], m[n]['nhe'])]
    fy = {}
    for n, comps in seq.items():
        s = fy_series(I0, ph, comps)
        fy[n] = {'series': s, 'total_2030_39': window_total(s)}
    # staged path to single payer: linear blend, fully staged option -> project-central single payer
    gf, gn, cagr = growth_paths(I0)
    path = []
    st = {r['year']: r for r in fy['staged_full_kids']['series']}
    for t in range(2030, 2040):
        w = max(0.0, min(1.0, (t - ph['path.start']) / (ph['path.target'] - ph['path.start'])))
        sp = m['single_payer_project_central']
        path.append({'year': t, 'weight_single_payer': w,
                     'federal_bn': (1 - w) * st[t]['federal_bn'] + w * sp['fed'] * gf[t],
                     'nhe_bn': (1 - w) * st[t]['nhe_bn'] + w * sp['nhe'] * gn[t]})
    unc = {n: uncertainty(rows, scn, n) for n in order if not n.startswith('_') and n != 'baseline_2029' and not scn[n].get('_hidden')}
    bench = benchmarks(rows, scn, results, m, I0)
    out = {'model': 'MOD-health-coverage', 'version': VERSION, 'as_of': AS_OF, 'status': 'exploratory', 'year': YEAR,
           'run_log': run_log(), 'scenario_titles': {n: scn[n].get('_title', n) for n in order if not n.startswith('_')},
           'hidden': [n for n in order if scn[n].get('_hidden')],
           'baseline_checks': baseline_checks(I0, results['baseline_2029']),
           'growth': {'net_subsidy_cagr_2032_36': cagr}, 'results': results, 'fy2030_39': fy,
           'staged_path_to_single_payer': path, 'uncertainty': unc, 'benchmarks': bench}
    return out


def baseline_checks(I, base):
    B = build_base(I)
    return {'model_federal_per_person_2032': {'medicare': B['mcare_fed_pp'], 'medicaid': B['mcd_fed_pp'], 'esi': B['esi_fed_pp'],
                                              'ptc': I['sub_ptc'] / sum(B['cells0']['ng_sub']) * 1000},
            'implied_marketplace_premium_pp': B['prem_ng'], 'private_plan_cost_pp': B['P_phi'],
            'commercial_to_medicare_price_ratio': B['c_phi'], 'public_option_premium_ratio': B['rho'],
            'overlap_removed_millions': B['overlap'], 'nhe_baseline_by_payer_bn': B['S'],
            'population_total': sum(base['people'].values()), 'cbo_population': I['cbo_pop'],
            'federal_subsidies_total_bn': base['federal']['total_subsidies_bn'],
            'cbo_net_subsidies_2032_bn': I['net_sub_2032'],
            'nhe_2032_bn': base['nhe_bn'],
            'cbo_per_enrollee_2036_for_comparison': {k: I[f'xchk_pp_{k}'] for k in ['medicare', 'medicaid', 'esi', 'ng']}}


def run_log():
    def sha(p):
        with open(os.path.join(HERE, p), 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:12]
    return {'model_version': VERSION, 'inputs_csv_sha256': sha('inputs.csv'), 'scenarios_csv_sha256': sha('scenarios.csv'),
            'evidence_register': 'dossiers/care/evidence.json (EV-CAR-020 to 061, 120-121, 131, 135, 206-209, 217-229, 236-237, 243, 263)',
            'as_of': AS_OF}


# ---------------------------------------------------------------- benchmarks
def within(x, target, tol=0.25):
    return abs(x - target) <= tol * abs(target)


def benchmarks(I_rows, scn, results, m, I):
    gf, gn, _ = growth_paths(I)
    sub_scale = I['net_sub_2032'] / I['net_sub_2030']  # CBO's 2030 numbers brought to 2032
    nhe_scale = gn[2032] / gn[2030]
    B = []

    def add(id, name, model, target, tol, passed, source, note):
        B.append({'id': id, 'benchmark': name, 'model': model, 'target': target, 'tolerance': tol, 'pass': bool(passed),
                  'source': source, 'note': note})

    # BM-1 CBO single-payer options, federal subsidies and NHE
    lo, hi = results['single_payer_cbo_like_low'], results['single_payer_cbo_like_high']
    fed_rng = (1500 * sub_scale, 3000 * sub_scale)
    nhe_rng = (-700 * nhe_scale, 300 * nhe_scale)

    def end_ok(x, rng):
        return rng[0] <= x <= rng[1] or any(within(x, e) for e in rng)
    fl, fh = lo['federal']['net_change_bn'], hi['federal']['net_change_bn']
    add('BM-1a', 'CBO 2020 single-payer options: change in federal subsidies (corners reproduce the range)',
        f'{fl:,.0f} to {fh:,.0f} $B in 2032', f'{fed_rng[0]:,.0f} to {fed_rng[1]:,.0f} $B (CBO $1.5-3.0T in 2030, grown to 2032 at CBO subsidy growth)',
        'each corner inside the range or within 25% of the nearer end', end_ok(fl, fed_rng) and end_ok(fh, fed_rng), 'EV-CAR-218',
        'Corners use only the payment-rate, cost-sharing and long-term-care assumptions the register gives (EV-CAR-220); CBO option specifications are not saved.')
    nl, nh = lo['nhe_change_bn'], hi['nhe_change_bn']
    add('BM-1b', 'CBO 2020 single-payer options: change in national health expenditures',
        f'{nl:,.0f} to {nh:,.0f} $B in 2032', f'{nhe_rng[0]:,.0f} to {nhe_rng[1]:,.0f} $B (CBO -$0.7T to +$0.3T in 2030, grown at NHE growth)',
        'each corner inside the range or within 25% of the nearer end', end_ok(nl, nhe_rng) and end_ok(nh, nhe_rng), 'EV-CAR-218',
        'CBO also changes provider supply and uses its 2020 baseline; the model grows both ends of the range to 2032.')
    # BM-2 law coverage effect
    law = results['bench_law_only']
    d = -law['uninsured_change']
    add('BM-2', 'P.L. 119-21: about 10 million more uninsured in 2034 (restoring the law provisions reverses it)',
        f'{d:.1f} million fewer uninsured in 2032', '10.0 million (2034); 9.4 million on the 2029-34 CBO path interpolated to 2032',
        '25%', within(d, 10.0), 'EV-CAR-038; EV-CAR-025; EV-CAR-049',
        'In-sample by construction: the restore flows are set from these same CBO estimates (7.5 million Medicaid, 2.8-2.9 million marketplace). The test checks the phase-in and band arithmetic, not an independent estimate.')
    # BM-3 credits
    cr = results['bench_credits_only']
    ins = -cr['uninsured_change']
    cost_t = I['credits_cost_10yr'] / 10 * I['ptc_sub_2032'] / (sum(I[f'ptc_sub_{y}'] for y in range(2026, 2036)) / 10)
    add('BM-3a', 'Enhanced credits permanent: 3.8 million more insured',
        f'{ins:.1f} million in 2032', '3.6 million (2030), 3.8 million (2035)', '25%', within(ins, 3.7), 'EV-CAR-029',
        'In-sample by construction (flow set from CBO).')
    add('BM-3b', 'Enhanced credits permanent: about $350 billion over ten years (2032 annual cost against the ten-year average, shaped by CBO PTC growth)',
        f'{cr["federal"]["net_change_bn"]:,.1f} $B in 2032', f'{cost_t:,.1f} $B ($350B over 2026-35, spread on the PTC profile)', '25%',
        within(cr['federal']['net_change_bn'], cost_t), 'EV-CAR-029; EV-CAR-052',
        'Independent of the coverage inputs. The model prices new enrollees, repricing of existing enrollees and removal of the 400% cliff at CBO-calibrated premiums; it has no risk-pool premium reduction or employer-coverage offset.')
    # BM-4 law Medicaid outlays
    mcd_t = I['law_mcd_outlays_10yr'] / 10 * I['mcd_sub_2032'] / (sum(I[f'mcd_sub_{y}'] for y in range(2025, 2035)) / 10)
    mcd_m = law['federal']['delta_components_bn'].get('Medicaid and CHIP, restored adults', 0) + \
        law['federal']['delta_components_bn'].get('Medicaid financing restored (provider taxes, directed payments)', 0)
    add('BM-4', 'P.L. 119-21 Medicaid provisions cut federal outlays $989.7 billion over FY2025-34 (restore reverses it)',
        f'{mcd_m:,.1f} $B in 2032', f'{mcd_t:,.1f} $B (average spread on CBO Medicaid growth)', '25%', within(mcd_m, mcd_t), 'EV-CAR-025; EV-CAR-052',
        'The model restores only the coverage-linked cost unless mcd_financing_restore is raised; CBO also counts provider-tax and state-directed-payment cuts.')
    # BM-5 Medicare at 60
    m60 = results['bench_medicare60_only']
    enroll = sum(f['millions'] for f in m60['flows'])
    add('BM-5', 'CBO Medicare at 60 (2022): 7.3 million enrollees',
        f'{enroll:.1f} million movers in 2032', '7.3 million (spec target; the saved CBO text gives shares, not this count)', '25%',
        within(enroll, 7.3), 'EV-CAR-207; EV-CAR-208',
        'Unverified target: the figure comes from the model spec, and the saved text (SRC-3204) does not contain it. The model counts uninsured, nongroup and ESI people who move to Medicare; it does not count people who add Part A while keeping employer coverage.')
    # BM-6 Urban (secondary)
    denom = I['sub_medicare'] + I['sub_medicaid'] + I['sub_ptc']
    spc = results['single_payer_project_central']['federal']['net_change_bn']
    popt = results['public_option']['federal']['net_change_bn']
    urban_lo, urban_hi = 1.5 / 1.090, 2.8 / 1.090
    add('BM-6a', 'Urban 2019 single-payer federal cost (secondary): rise in federal spending relative to current federal health spending',
        f'{spc / denom:.0%} (project central)', f'{urban_lo:.0%} (Urban lite, $1.5T in 2020) to {urban_hi:.0%} (enhanced, $2.8T), on RAND\'s $1,090B 2019 federal base',
        'inside the range or within 25% of an end', urban_lo <= spc / denom <= urban_hi or any(within(spc / denom, e) for e in (urban_lo, urban_hi)),
        'EV-CAR-222; EV-CAR-224; EV-CAR-229', 'Indicative only: Urban\'s baseline is not in the register, so RAND\'s federal base (EV-CAR-229) stands in; the model also counts the tax exclusion.')
    add('BM-6b', 'Urban 2019 hybrid reform with a public option (secondary): federal cost relative to current federal health spending',
        f'{popt / denom:.0%} (restore plus public option)', f'{0.1221 / 1.090:.0%} ($122.1B in 2020 on $1,090B)', '25%', within(popt / denom, 0.1221 / 1.090),
        'EV-CAR-225; EV-CAR-229', 'Urban\'s bundle adds a mandate and rate caps and covers fewer people than restore plus public option; not a like-for-like test.')
    return B


# ---------------------------------------------------------------- output
def r3(x):
    if isinstance(x, float):
        return round(x, 3)
    if isinstance(x, dict):
        return {k: r3(v) for k, v in x.items()}
    if isinstance(x, list):
        return [r3(v) for v in x]
    return x


def cell(x):
    return '-' if x is None else f'{x:,.0f}'


def md_results(out, rows):
    R = out['results']
    shown = [n for n in R if n not in out['hidden']]
    T = out['scenario_titles']
    L = []
    w = L.append
    w('# Health coverage model: results')
    w('')
    w(f"Generated by `models/tools/health-coverage/model.py` (model {out['version']}, status {out['status']}, {out['as_of']}). "
      f"Representative year {out['year']}; money in $ billion unless noted; people in millions. Run log: inputs.csv `{out['run_log']['inputs_csv_sha256']}`, "
      f"scenarios.csv `{out['run_log']['scenarios_csv_sha256']}`. Exploratory analysis of the evidence in `dossiers/care/evidence.json`; not an official score.")
    w('')
    w('## Headline, 2032 and FY2030-39')
    w('')
    w('| Scenario | Uninsured (M) | Change vs baseline (M) | National spending change | Federal cost change, gross new | Offsets | Net federal change 2032 | FY2030-39 federal | FY2030-39 national spending |')
    w('| --- | --- | --- | --- | --- | --- | --- | --- | --- |')
    for n in shown:
        r = R[n]
        fy = out['fy2030_39'].get(n, {}).get('total_2030_39', {})
        fed = r['federal']
        w(f"| {T[n]} | {r['uninsured']:.1f} | {r['uninsured_change']:+.1f} | {r['nhe_change_bn']:+,.0f} | {fed['gross_new_bn']:,.0f} | {-fed['offsets_bn']:,.0f} | {fed['net_change_bn']:+,.0f} | "
          + (f"{fy['federal_bn']:+,.0f} | {fy['nhe_bn']:+,.0f} |" if fy else 'n/a | n/a |'))
    w('')
    w('Federal cost means CBO\'s "federal subsidies": outlays plus forgone revenue (the employer tax exclusion). Baseline net subsidies in 2032: '
      f"{out['baseline_checks']['federal_subsidies_total_bn']:,.0f} (CBO {out['baseline_checks']['cbo_net_subsidies_2032_bn']:,.0f}). "
      'FY2030-39 totals grow each stage\'s 2032 effect at CBO\'s growth in net subsidies (2030-36 from SRC-3000, 2037-39 at the 2032-36 average of '
      f"{out['growth']['net_subsidy_cagr_2032_36']:.1%} a year), scaled by the phase-in years in scenarios.csv; national spending grows at the CMS NHE rate.")
    w('')
    w('## People by coverage source, 2032 (millions)')
    w('')
    srcs = [s for s in SRCS if any(R[n]['people'][s] > 1e-9 for n in shown)]
    w('| Source | ' + ' | '.join(T[n] for n in shown) + ' |')
    w('| --- |' + ' --- |' * len(shown))
    for s in srcs:
        w(f'| {LABEL[s]} | ' + ' | '.join(f"{R[n]['people'][s]:.1f}" for n in shown) + ' |')
    w('')
    w('Medicare and Medicaid rows split restored or newly eligible groups out so their cost can be priced separately. Counts net out people with two sources (CBO: 19.6 million) using the overlap assumptions.')
    w('')
    w('## Federal cost by component, change from baseline (2032)')
    w('')
    for n in shown:
        if n == 'baseline_2029':
            continue
        dk = R[n]['federal']['delta_components_bn']
        w(f"**{T[n]}**: " + '; '.join(f'{k} {v:+,.1f}' for k, v in dk.items() if abs(v) > 0.05) + f"; net {R[n]['federal']['net_change_bn']:+,.1f}.")
        w('')
    w('## Household cost per person (premiums plus out of pocket, before new financing), 2032')
    w('')
    w('Dollars per person per year, all people in the band (uninsured included). Employer premium contributions are shown separately and not charged to households.')
    w('')
    w('| Scenario | ' + ' | '.join(BANDS) + ' | All | Employer premium contributions ($B) |')
    w('| --- |' + ' --- |' * 6)
    for n in shown:
        h = R[n]['household']
        tot = sum(b['people'] for b in h['by_band'])
        w(f'| {T[n]} | ' + ' | '.join(f"{b['per_person']:,.0f}" for b in h['by_band']) + f" | {h['total_bn'] / tot * 1000:,.0f} | {h['employer_premiums_bn']:,.0f} |")
    w('')
    w('### Baseline: dollars per person by coverage source and income band')
    w('')
    w('| Source | ' + ' | '.join(BANDS) + ' | Premium (avg) | Out of pocket (avg) |')
    w('| --- |' + ' --- |' * 6)
    b0 = R['baseline_2029']['household']
    for s, v in b0['by_source'].items():
        w(f"| {LABEL[s]} | " + ' | '.join(cell(x) for x in b0['matrix'][s]) + f" | {v['premium_pp']:,.0f} | {v['oop_pp']:,.0f} |")
    w('')
    w('### Public option: dollars per person by coverage source and income band')
    w('')
    w('| Source | ' + ' | '.join(BANDS) + ' |')
    w('| --- |' + ' --- |' * 4)
    h = R['public_option']['household']
    for s in h['by_source']:
        w(f"| {LABEL[s]} | " + ' | '.join(cell(x) for x in h['matrix'][s]) + ' |')
    w('')
    w('## Amount to be financed (reported, not allocated: the financing settlement allocates it)')
    w('')
    w('| Scenario | Net increase in federal subsidies, 2032 | Gross new federal outlay | Household premiums and out-of-pocket removed | Employer premium contributions removed |')
    w('| --- | --- | --- | --- | --- |')
    for n in shown:
        if n == 'baseline_2029':
            continue
        r = R[n]
        pf = r['private_flows_removed_bn']
        hhr = pf['household_premiums_and_oop']
        w(f"| {T[n]} | {r['federal']['net_change_bn']:+,.0f} | {r['federal']['gross_new_bn']:,.0f} | {hhr:,.0f} | {pf['employer_premiums']:,.0f} |")
    w('')
    sp = R['single_payer_project_central']['single_payer']
    w(f"Single payer, project central: plan pays providers {sp['provider_revenue_bn']:,.0f} (rate {sp['rate_multiple_of_medicare']:.2f} x Medicare; use up {sp['use_increase']:.1%}; "
      f"newly covered {sp['newly_covered_millions']:.1f} million add {sp['new_use_bn']:,.0f}; long-term care {sp['ltc_bn']:,.0f}), plus administration {sp['admin_bn']:,.0f}, "
      f"less cost sharing {sp['cost_sharing_bn']:,.0f}, less state and retained flows {sp['state_and_retained_bn']:,.0f}.")
    w('')
    w('## Staged path to single payer (stylized linear blend)')
    w('')
    w('| Year | Weight on single payer | Federal change | National spending change |')
    w('| --- | --- | --- | --- |')
    for r in out['staged_path_to_single_payer']:
        w(f"| {r['year']} | {r['weight_single_payer']:.0%} | {r['federal_bn']:+,.0f} | {r['nhe_bn']:+,.0f} |")
    w('')
    w('## Ranges (from the input ranges in inputs.csv)')
    w('')
    w('Net federal change 2032 ($B). One-at-a-time swings drive the tornado. "All low" and "all high" set every ranged input to its low or high value; "cost min" and "cost max" set each to whichever end lowers or raises federal cost.')
    w('')
    w('| Scenario | Central | All low | All high | Cost min | Cost max | National spending central | Uninsured central | Uninsured at cost min | Uninsured at cost max |')
    w('| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |')
    for n, u in out['uncertainty'].items():
        c = u['corners']
        w(f"| {T[n]} | {u['central']['fed']:+,.0f} | {c['all_low']['fed']:+,.0f} | {c['all_high']['fed']:+,.0f} | {c['cost_min']['fed']:+,.0f} | {c['cost_max']['fed']:+,.0f} | "
          f"{u['central']['nhe']:+,.0f} | {u['central']['unins']:.1f} | {c['cost_min']['unins']:.1f} | {c['cost_max']['unins']:.1f} |")
    w('')
    w('### Tornado: five inputs that move federal cost most')
    w('')
    for n, u in out['uncertainty'].items():
        w(f"**{T[n]}**: " + '; '.join(f"`{t['input']}` {t['low_value']:g} to {t['high_value']:g} moves net federal change {t['fed_at_low']:+,.0f} to {t['fed_at_high']:+,.0f}" for t in u['tornado']) + '.')
        w('')
    w('## Benchmarks')
    w('')
    w(benchmark_table(out['benchmarks']))
    w('')
    w('Benchmark misses are reported, not tuned away. Where a model flow is set from the same CBO estimate it is checked against, the note says the benchmark is in-sample.')
    w('')
    return '\n'.join(L) + '\n'


def benchmark_table(bm):
    L = ['| ID | Benchmark | Model | Target | Tolerance | Result | Note |', '| --- | --- | --- | --- | --- | --- | --- |']
    for b in bm:
        L.append(f"| {b['id']} | {b['benchmark']} ({b['source']}) | {b['model']} | {b['target']} | {b['tolerance']} | {'pass' if b['pass'] else '**miss**'} | {b['note']} |")
    return '\n'.join(L)


def card_block(out):
    b = out['benchmarks']
    n_pass = sum(1 for x in b if x['pass'])
    R = out['results']
    kinds = [r['kind'] for r in load_inputs().values()]
    L = [f"*Generated by `model.py` ({out['as_of']}); the rest of the card is written by hand.* Run log: model {out['run_log']['model_version']}, inputs.csv `{out['run_log']['inputs_csv_sha256']}`, scenarios.csv `{out['run_log']['scenarios_csv_sha256']}`.", '',
         f'Inputs: {len(kinds)} in inputs.csv, {kinds.count("evidence")} traced to evidence IDs and {kinds.count("assumption")} labeled assumptions with a tested range.', '',
         f'{len(b)} benchmarks: {n_pass} pass, {len(b) - n_pass} miss.', '', benchmark_table(b), '',
         'Headline results, 2032 (net federal change in $ billion, national spending change in $ billion, uninsured in millions):', '',
         '| Scenario | Uninsured | Net federal change | National spending change |', '| --- | --- | --- | --- |']
    for n, r in R.items():
        if n in out['hidden']:
            continue
        L.append(f"| {out['scenario_titles'][n]} | {r['uninsured']:.1f} | {r['federal']['net_change_bn']:+,.0f} | {r['nhe_change_bn']:+,.0f} |")
    return '\n'.join(L)


def build_card(out):
    src = open(os.path.join(HERE, 'MODEL-CARD.md')).read()
    pat = re.compile(r'<!-- generated:results:start -->.*?<!-- generated:results:end -->', re.S)
    block = '<!-- generated:results:start -->\n' + card_block(out) + '\n<!-- generated:results:end -->'
    return pat.sub(lambda m: block, src)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=HERE)
    a = ap.parse_args()
    rows = load_inputs()
    out = r3(build_all(rows))
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, 'results.json'), 'w') as f:
        json.dump(out, f, indent=1, sort_keys=True)
        f.write('\n')
    with open(os.path.join(a.out, 'results.md'), 'w') as f:
        f.write(md_results(out, rows))
    with open(os.path.join(a.out, 'MODEL-CARD.md'), 'w') as f:
        f.write(build_card(out))
    print(f"health coverage model: {len(out['results'])} scenarios, {sum(1 for b in out['benchmarks'] if b['pass'])}/{len(out['benchmarks'])} benchmarks pass")


if __name__ == '__main__':
    main()
