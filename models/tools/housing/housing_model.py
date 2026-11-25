#!/usr/bin/env python3
"""The housing model (`MOD-housing`): cost, reach and rents of the housing flagship's decided design.

Role: the engine of `MOD-housing` (`MODEL-CARD.md`; stage H step H7, memo H5 A, `DEC-2026-11-25-22`). Status:
exploratory. Standard library only.

Three parts, all read from the parameter files beside this file:
1. **Cost** (`lines`): each provision of `dossiers/home/6-cost.md` section 1.2 by federal fiscal year, FY2030-45,
   nominal $ billion, a cost positive. The rental help lines are built month by month: awards issued on the
   plan's schedule (`plan.csv`), each leased after the lag at the steady-state share, paying the subsidy plus fees,
   search help and the higher payment standards (`parameters.csv`). The capital, emergency, owner and rural lines
   are each year's budget authority times its spend-out. Lines whose build 6-cost.md does not state are taken as
   published (`published.csv`) and marked so.
2. **Reach** (`reach`): households leased by stage and year, the other programs' yearly counts, and the stages'
   pools against HUD's worst case needs counts by income band (`market.csv`).
3. **Rents** (`rents`): landlord capture and spillover to unassisted renters where supply is short, as ranges from
   the register (`market.csv`), never added to the cost; supply only as the evidence's range, never forecast.

Cases: `central`, `low` and `high` move every judgment input together (6-cost.md, "Low, central and high"): a
bound, not a probability. `leased` overrides the steady-state leased share for every rental line (section 1.4).
"""
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
PARAMETERS = os.path.join(HERE, 'parameters.csv')
PLAN = os.path.join(HERE, 'plan.csv')
PUBLISHED = os.path.join(HERE, 'published.csv')
MARKET = os.path.join(HERE, 'market.csv')
INPUTS = [PARAMETERS, PLAN, PUBLISHED, MARKET]

FY0, FY_LAST = 2030, 2045
YEARS = list(range(FY0, FY_LAST + 1))
WINDOW = list(range(2030, 2040))
MONTHS = 12 * len(YEARS)          # month 0 is October 2029, the first month of FY2030
CASES = ('central', 'low', 'high')

# Inputs whose low value raises cost (a longer lag delays spending): the low case takes their high end.
COST_FALLS_AS_VALUE_RISES = {'lag_months'}
LEASED_CENTRAL = 0.9   # leased_share's central value, the base the duty to house's lift is read against (checked in the tests)


def _read(path):
    with open(path, encoding='utf-8') as f:
        return list(csv.DictReader(f))


def _year_key(y):
    if y == 'none':
        return None
    y = y.replace('FY', '').replace('CY', '')
    if '-' in y:
        a, b = y.split('-')
        return (int(a), int(b))
    return int(y)


def _pick(r, case):
    v = float(r['value'])
    if case == 'central' or not r.get('low') or not r.get('high'):
        return v
    lo, hi = float(r['low']), float(r['high'])
    up = r['id'] in COST_FALLS_AS_VALUE_RISES
    return (hi if up else lo) if case == 'low' else (lo if up else hi)


def load(case='central', path=None):
    """{id: value} for scalar rows, {id: {year: value}} for rows keyed by year (a span is spread to each year)."""
    out = {}
    for p in ([path] if path else INPUTS):
        for r in _read(p):
            v = _pick(r, case)
            k = _year_key(r['year'])
            rid = r['id']
            if k is None or rid in ('subsidy_fy2030', 'search_help', 'standing_fund_ba', 'services_backstop',
                                    'ig_set_aside', 'section502_subsidy_rate'):
                out[rid] = v
            elif isinstance(k, tuple):
                if rid in ('revolving_grants_ba', 'public_housing_ba', 'loan_commitments', 'subsidy_growth',
                           'duty_leased_share', 'direct_homes_m', 'construction_homes_m', 'section502_to_100_ami'):
                    out[rid] = v if rid not in out else out[rid]
                    out[rid + '.span'] = k
                elif r['group'] in ('published', 'credits'):
                    out.setdefault(rid, {})['window'] = v
                else:
                    d = out.setdefault(rid, {})
                    for y in range(k[0], k[1] + 1):
                        d[y] = v
            else:
                if r['group'] in ('published', 'credits'):
                    out.setdefault(rid, {})[k] = v
                elif rid in ('stage2_pool_m', 'wider_pool_m', 'stage2_restated_total_m', 'stage3_under62_m', 'stage3_older_eligible_m'):
                    out[rid] = v
                else:
                    out.setdefault(rid, {})[k] = v
    return out


def zeros():
    return {y: 0.0 for y in YEARS}


def window(path):
    return sum(path.get(y, 0.0) for y in WINDOW)


def add(*paths):
    out = zeros()
    for p in paths:
        for y, v in p.items():
            if y in out:
                out[y] += v
    return out


def scale(path, k):
    return {y: v * k for y, v in path.items()}


# ------------------------------------------------------------------ rental help, built month by month
def subsidy(P, y):
    """Rent subsidy per leased household-year in FY y (dollars)."""
    return P['subsidy_fy2030'] * (1 + P['subsidy_growth']) ** (y - FY0)


def even(fy, total, first_month=0):
    """Awards issued evenly over the months of FY fy from first_month (0 = October)."""
    base, n = (fy - FY0) * 12, 12 - first_month
    return {base + first_month + i: total / n for i in range(n)}


def merge(*ds):
    out = {}
    for d in ds:
        for m, a in d.items():
            out[m] = out.get(m, 0.0) + a
    return out


def leased_by_month(issue, share, lag, share_from=None):
    """Households leased in each month: each award leases `lag` months after issue at `share` (from fiscal year
    share_from[0], at share_from[1] instead: the duty to house)."""
    lag = int(round(lag))
    out = [0.0] * MONTHS
    for m, a in issue.items():
        for k in range(m + lag, MONTHS):
            s = share
            if share_from and FY0 + k // 12 >= share_from[0]:
                s = share_from[1]
            out[k] += a * s
    return out


def by_fy(months):
    out = zeros()
    for k, v in enumerate(months):
        out[FY0 + k // 12] += v / 12
    return out


def issued_by_fy(issue):
    out = zeros()
    for m, a in issue.items():
        out[FY0 + m // 12] += a
    return out


def program(P, issue, share=None, cost_ratio=1.0, share_from=None):
    """One rental program's household-years and dollars by FY: rent, fees (rate on the rent plus the issuance fee),
    search help (per award and per reissue, growing with the subsidy) and leased households at the end of each FY."""
    share = P['leased_share'] if share is None else share
    lea = leased_by_month(issue, share, P['lag_months'], share_from)
    hy, iss = by_fy(lea), issued_by_fy(issue)
    g = lambda y: (1 + P['subsidy_growth']) ** (y - FY0)
    rent = {y: hy[y] * subsidy(P, y) * cost_ratio / 1e9 for y in YEARS}
    fees = {y: (P['fee_rate'] * hy[y] * subsidy(P, y) * cost_ratio + P['issuance_fee'] * iss[y] * cost_ratio) / 1e9 for y in YEARS}
    search = {y: P['search_help'] * g(y) * (iss[y] + P['reissue_rate'] * hy[y]) / 1e9 for y in YEARS}
    end = {y: lea[(y - FY0) * 12 + 11] for y in YEARS}
    return {'household_years': hy, 'issued': iss, 'rent': rent, 'fees': fees, 'search': search, 'leased_end': end}


def schedules(P):
    """The award and enrollment schedules (awards by month)."""
    a = P['awards_4a_per_year']
    s4a = merge(even(2030, a[2030], int(P['awards_4a_first_month'][2030])), *(even(y, a[y]) for y in (2031, 2032, 2033)))
    cap, right = P['stage2_cap_per_year'], int(P['stage2_right_fy'])
    apply2 = P['stage2_pool_m'] * 1e6 * P['stage2_takeup']
    left, s2 = apply2, {}
    for y in range(2034, right):
        n = min(cap[y], left)
        s2 = merge(s2, even(y, n))
        left -= n
    s2 = merge(s2, even(right, left))                          # every remaining family enrolls when it becomes a right

    def added(pool_m):
        """Stage 2's added families: under the cap if room is left before the right, else in the right's year."""
        n = pool_m * 1e6 * P['stage2_takeup']
        room = sum(cap[y] for y in range(2034, right)) - apply2
        if room >= n:
            return even(right - 1, n)
        return even(right, n)

    f3 = int(P['stage3_first_fy'])
    s3 = merge(*(even(y, P['stage3_under62_m'] * 1e6 / 3) for y in range(f3, f3 + 3)))
    old = P['stage3_older_eligible_m'] * 1e6 * P['stage3_older_takeup']
    s3o = merge(*(even(y, old / 3) for y in range(f3, f3 + 3)))
    return {'4a': s4a, 'stage2': s2, 'wider': added(P['wider_pool_m']), 'restated': added(P['stage2_restated_total_m'] - P['stage2_pool_m']),
            'stage3': s3, 'stage3_older': s3o}


def rental(P, leased=None):
    """The rental help lines (6-cost.md 1.2, 1.3, 2.1, 2.5, 2.7, 2.12), each a path of $ billion by FY."""
    if leased is not None:
        P = dict(P, leased_share=leased)
    S = schedules(P)
    right = int(P['stage2_right_fy'])
    # the duty's added leasing, on stage 2's count from the right: relative to the central leased share, so it
    # scales with the leased share (6-cost.md 1.4 and 2.5)
    # (capped so no line leases more than every award)
    lift = min(P['duty_leased_share'] / LEASED_CENTRAL, 1 / P['leased_share']) - 1
    pu = P['payment_standard_uplift']
    a4 = program(P, S['4a'])
    s2 = program(P, S['stage2'])
    s3 = program(P, S['stage3'])
    s3o = program(P, S['stage3_older'], cost_ratio=P['stage3_older_cost_ratio'])
    rf = lambda p: add(p['rent'], p['fees'])
    duty_path = {y: (v * lift if y >= right else 0.0) for y, v in rf(s2).items()}

    def added_line(key):
        p = program(P, S[key])
        base = rf(p)
        sh = {y: P['added_search_award_only'] * p['issued'][y] / 1e9 for y in YEARS}
        d = {y: (v * lift if y >= right else 0.0) for y, v in base.items()}
        ps = scale(p['rent'], pu)
        return add(base, sh, d, ps), p

    wider, pw = added_line('wider')
    restated, pr = added_line('restated')
    lines = {
        'hou-4a-one-million-awards-full-fees': rf(a4),
        'hou-4-07-search-help': add(a4['search'], s2['search'], s3['search']),
        'hou-4d-01-stage-2': rf(s2),
        'hou-4d-01-duty-to-house': duty_path,
        'hou-4d-01-wider-entry': wider,
        'hou-4d-01-restated-count': restated,
        'hou-4-08-stage-3-under-62': rf(s3),
        'hou-4-08-stage-3-62-and-over': rf(s3o),
        'payment-standards-to-120-percent': scale(add(a4['rent'], s2['rent'], s3['rent'], s3o['rent']), pu),
    }
    progs = {'4a': a4, 'stage2': s2, 'wider': pw, 'restated': pr, 'stage3': s3, 'stage3_older': s3o}
    return lines, progs


# ------------------------------------------------------------------ the other lines: budget authority times spend-out
def spend(ba_by_year, shares):
    """Outlays by FY from budget authority by FY and the share spent in each year after award."""
    out = zeros()
    for y, ba in ba_by_year.items():
        for i, s in enumerate(shares):
            if y + i in out:
                out[y + i] += ba * s
    return out


def spread(total, span):
    a, b = span
    return {y: total / (b - a + 1) for y in range(a, b + 1)}


def other(P):
    cap = [P['capital_spend_y%d' % i] for i in range(4)]
    loans = [P['loan_disburse_y%d' % i] for i in range(3)]
    st = {y: P['emergency_start_spend'].get(y, 0.0) * P['emergency_start_ba'][2030] for y in YEARS}
    fund = {y: P['standing_fund_ba'] * (1 + P['standing_fund_growth']) ** (y - 2031) if y >= 2031 else 0.0 for y in YEARS}
    loan_subsidy = {y: v * 0.05 for y, v in spread(P['loan_commitments'], P['loan_commitments.span']).items()}
    backstop = {y: P['services_backstop'] * (1 + P['backstop_growth']) ** (y - FY0) for y in YEARS}
    ig = {y: P['ig_set_aside'] * (1 + P['standing_fund_growth']) ** (y - FY0) for y in YEARS}
    dp = spend(P['down_payment_ba'], [1 - P['down_payment_spill'], P['down_payment_spill']])
    repair = spend(P['repair_fund_ba'], [1 - P['repair_fund_spill'], P['repair_fund_spill']])
    ptm = zeros()
    for y in YEARS:
        if y in P['property_tax_match']:
            ptm[y] = P['property_tax_match'][y]
        elif y > max(P['property_tax_match']):
            ptm[y] = ptm[y - 1] * (1 + P['property_tax_growth'])
    eq = add(P['legal_help'], P['service_coordinators'], P['home_sharing'])
    staff = add(P['rural_staff'], P['rural_system'])
    staff[2040] = P['rural_staff_fy2040'][2040]
    for y in YEARS:
        if y > 2040:
            staff[y] = staff[2040]
    s502 = {y: v * P['section502_subsidy_rate'] for y, v in P['section502_added_lending'].items()}
    s502 = add(s502, spread(P['section502_to_100_ami'], P['section502_to_100_ami.span']))
    s502[2040] = P['section502_fy2040_tail'][2040]
    pres = add(spend(P['rural_preservation_ba'], [P['rural_preservation_spend_y%d' % i] for i in range(3)]), P['rural_vouchers'])
    return {
        'hou-1d-04-one-time-start': st,
        'hou-1d-01-standing-emergency-fund': fund,
        'hou-3c-01-revolving-fund-grants': spend(spread(P['revolving_grants_ba'], P['revolving_grants_ba.span']), cap),
        'hou-3c-02-construction-loan-subsidy': spend(loan_subsidy, loans),
        'hou-5-01-public-housing-repair': spend(spread(P['public_housing_ba'], P['public_housing_ba.span']), cap),
        'hou-4-10-recovery-housing': add(P['recovery_housing']),
        'hou-4-12-services-backstop': backstop,
        'hou-4-12-wider-backstop-to-2035': add(P['wider_backstop']),
        'hou-4-06-testing-grants': add(P['testing_grants']),
        'inspector-general-set-aside': ig,
        'hou-10-01-down-payment-help': dp,
        'hou-12-01-home-repair-fund': repair,
        'hou-13-01-property-tax-match': ptm,
        'hou-13-02-to-04-equity-coordinators-sharing': eq,
        'hou-14-01-rural-development-staff': staff,
        'hou-14-02-section-502-at-scale': s502,
        'hou-14-03-rural-rental-fund-and-vouchers': pres,
    }


PUBLISHED_LINES = {   # line id -> published.csv id
    'hou-6-01-zoning-reward': 'zoning_reward',
    'hou-8-01-social-housing-pilot': 'social_housing_pilot',
    'hou-9a-01-federal-builder-capital': 'federal_builder',
    'federal-administration-set-aside': 'federal_admin',
    'hou-10-02-fha-premium-cut': 'fha_premium_cut',
    'hou-11-01-manufactured-home-grants': 'manufactured_home_grants',
    'hou-14-04-self-help-and-farmworker': 'self_help_farmworker',
    'hou-2d-01-low-income-credit': 'low_income_credit',
    'hou-2d-02-03-trial-credits': 'trial_credits',
}
CREDITS = ('hou-2d-01-low-income-credit', 'hou-2d-02-03-trial-credits')

# 6-cost.md section 1.2's rows, in its order: (line id, label, central window, low, high, FY2040) as published.
TABLE_1_2 = [
    ('hou-4a-one-million-awards-full-fees', 'HOU-4A.01-.02 One million awards, with full fees', 147, 116, 194, 22),
    ('hou-4-07-search-help', 'HOU-4.07 Search help', 8, 3, 17, 1),
    ('hou-4d-01-stage-2', 'HOU-4D.01 Stage 2 guarantee, 2034 on', 81, 44, 142, 23),
    ('hou-4d-01-duty-to-house', 'HOU-4D.01 Duty to house, 2037 on', 3, 1, 5, 1),
    ('hou-4d-01-wider-entry', "HOU-4D.01 Stage 2's wider entry", 17, 8, 54, 8),
    ('hou-4d-01-restated-count', 'HOU-4D.01 Stage 2 restated (stage 1 uncapped)', 17, 11, 22, 8),
    ('hou-4-08-stage-3-under-62', 'HOU-4.08 Stage 3, disabled renters under 62', 5, 2, 13, 9),
    ('hou-4-08-stage-3-62-and-over', "HOU-4.08 Stage 3's disabled renters 62 and over", 5, 2, 16, 9),
    ('hou-1d-04-one-time-start', 'HOU-1D.04 One-time start', 15, 10, 25, 0),
    ('hou-1d-01-standing-emergency-fund', 'HOU-1D.01-.03 Standing emergency fund', 49, 29, 78, 6),
    ('hou-3c-01-revolving-fund-grants', 'HOU-3C.01 State revolving fund grants', 70, 70, 70, 2),
    ('hou-3c-02-construction-loan-subsidy', 'HOU-3C.02 Construction loans (subsidy)', 14, 14, 14, 0.4),
    ('hou-5-01-public-housing-repair', 'HOU-5.01 Public housing repair', 57, 57, 57, 1.5),
    ('hou-6-01-zoning-reward', 'HOU-6.01 Zoning reward', 25, 25, 25, 3),
    ('hou-8-01-social-housing-pilot', 'HOU-8.01 Social housing pilot', 9, 9, 9, 1),
    ('hou-9a-01-federal-builder-capital', 'HOU-9A.01 Small federal builder', 5, 2, 20, 0),
    ('hou-4-10-recovery-housing', 'HOU-4.10 Recovery housing', 1.5, 1.5, 1.5, 0),
    ('hou-4-12-services-backstop', 'HOU-4.12 HUD services backstop', 6, 6, 6, 1),
    ('hou-4-12-wider-backstop-to-2035', 'HOU-4.12 Wider backstop through 2035', 6, 3, 12, 0),
    ('hou-4-06-testing-grants', 'HOU-4.06 Fair housing testing grants', 0.5, 0.5, 0.5, 0),
    ('payment-standards-to-120-percent', 'Payment standards up to 120%', 7, 2, 20, 2),
    ('inspector-general-set-aside', 'Inspector general set-aside', 0.6, 0.3, 1.1, 0.1),
    ('federal-administration-set-aside', 'Federal administration set-aside', 2, 1, 7, 0.4),
    ('hou-10-01-down-payment-help', 'HOU-10.01 Down payment help', 28, 19, 47, 0.15),
    ('hou-10-02-fha-premium-cut', "HOU-10.02 FHA's premium cut", 25, 15, 35, 0),
    ('hou-11-01-manufactured-home-grants', 'HOU-11.01 Manufactured-home community grants', 3.5, 2, 5, 0.3),
    ('hou-12-01-home-repair-fund', 'HOU-12.01 Home repair fund', 37, 25, 54, 1.2),
    ('hou-13-01-property-tax-match', 'HOU-13.01 Property-tax match', 20.5, 8, 35, 3.1),
    ('hou-13-02-to-04-equity-coordinators-sharing', 'HOU-13.02-.04 Equity, coordinators, home sharing', 3.6, 2, 5, 0.35),
    ('hou-14-01-rural-development-staff', 'HOU-14.01 Rural Development staff and system', 3.5, 2.5, 5, 0.35),
    ('hou-14-02-section-502-at-scale', 'HOU-14.02 Section 502 at scale', 3.5, 2.5, 5.5, 0.1),
    ('hou-14-03-rural-rental-fund-and-vouchers', 'HOU-14.03 Rural rental fund and vouchers', 5.2, 3.3, 8.6, 0.46),
    ('hou-14-04-self-help-and-farmworker', 'HOU-14.04 Self-help and farmworker housing', 2.3, 1.5, 3.5, 0.2),
]
TABLE_RANGE = {k: (lo, hi) for k, _, _, lo, hi, _ in TABLE_1_2}
TABLE_SPENDING = (683, 500, 995)       # 6-cost.md 1.2, "Spending, total"
TABLE_CREDITS = (123, 102, 144, 16)    # HOU-2D, option D
TABLE_HOUSING = (806, 602, 1139, 120)  # "Housing, total"
TABLE_FY2040_SPENDING = 104            # "104 with the capital tail"


def published(P, key):
    d = P[key]
    return {'window': d['window'], **{y: v for y, v in d.items() if y != 'window'}}


def lines(case='central', leased=None):
    """Every line of 6-cost.md 1.2 as {'path': {FY: $bn} or None, 'window', 'fy2040', 'method'}."""
    P = load(case)
    rl, _ = rental(P, leased)
    out = {}
    for k, p in rl.items():
        out[k] = {'path': p, 'window': window(p), 'fy2040': p[2040], 'fy2041': p[2041], 'method': 'built'}
    central = other(load('central')) if case != 'central' else None
    for k, p in other(P).items():
        if central is not None:
            # built from decided amounts held fixed, so the low and high are 6-cost.md's own ranges
            # (sizes and spend-outs it priced before or beside the decisions): the path is scaled to them
            lo, hi = TABLE_RANGE[k]
            c = window(central[k])
            p = scale(central[k], (lo if case == 'low' else hi) / c if c else 1.0)
        out[k] = {'path': p, 'window': window(p), 'fy2040': p[2040], 'fy2041': p[2041],
                  'method': 'built' if central is None else 'built; range as published'}
    for k, pid in PUBLISHED_LINES.items():
        d = published(P, pid)
        out[k] = {'path': None, 'window': d['window'], 'fy2040': d.get(2040, 0.0), 'fy2041': d.get(2041),
                  'method': 'published'}
    return out


def totals(L):
    sp = [k for k in L if k not in CREDITS]
    return {'spending_window': sum(L[k]['window'] for k in sp), 'credits_window': sum(L[k]['window'] for k in CREDITS),
            'housing_window': sum(L[k]['window'] for k in L), 'spending_fy2040': sum(L[k]['fy2040'] for k in sp),
            'housing_fy2040': sum(L[k]['fy2040'] for k in L)}


def displayed(x, published_value):
    """A model figure rounded as 6-cost.md 1.2 prints the published one (whole billions, or the published decimals)."""
    s = repr(float(published_value))
    d = 0 if float(published_value).is_integer() else len(s.split('.')[1])
    return round(x + 1e-9, d)


RENTAL = ('hou-4a-one-million-awards-full-fees', 'hou-4-07-search-help', 'hou-4d-01-stage-2', 'hou-4-08-stage-3-under-62',
          'payment-standards-to-120-percent')


def lease_up(shares=(0.57, 0.75, 0.9)):
    """6-cost.md 1.4's table: the rental help lines (HOU-4A, HOU-4D's first count, stage 3 under 62, with fees,
    search help and the higher payment standards) and households housed, at each leased share."""
    out = {}
    for s in shares:
        P = load('central')
        rl, pr = rental(P, s)
        # 1.4's rows carry the payment standards on the three lines it names (not stage 3's older group)
        ps = scale(add(pr['4a']['rent'], pr['stage2']['rent'], pr['stage3']['rent']), P['payment_standard_uplift'])
        keys = ('hou-4a-one-million-awards-full-fees', 'hou-4-07-search-help', 'hou-4d-01-stage-2', 'hou-4-08-stage-3-under-62')
        path = add(ps, *(rl[k] for k in keys))
        L = lines('central', leased=s)
        out[f'{s:.2f}'] = {
            'rental_window': window(path), 'rental_fy2040': path[2040],
            'first_million_fy2034': pr['4a']['leased_end'][2034], 'stage2_fy2039': pr['stage2']['leased_end'][2039],
            'stage3_fy2042': pr['stage3']['leased_end'][2042],
            'all_three_fy2042': pr['4a']['leased_end'][2042] + pr['stage2']['leased_end'][2042] + pr['stage3']['leased_end'][2042],
            'all_stages_fy2042': sum(pr[k]['leased_end'][2042] for k in pr),
            'housing_window': totals(L)['housing_window']}
    return out


# ------------------------------------------------------------------ reach
def reach(case='central', leased=None):
    P = load(case)
    _, pr = rental(P, leased)
    M = {r['id']: _pick(r, case) for r in _read(MARKET)}
    yrs = (2030, 2031, 2032, 2033, 2034, 2036, 2037, 2038, 2039, 2040, 2042, 2045)
    stage = lambda k: {str(y): pr[k]['leased_end'][y] for y in yrs}
    by_stage = {
        'stage_1_first_million': stage('4a'), 'stage_2_first_count': stage('stage2'), 'stage_2_wider_entry': stage('wider'),
        'stage_2_restated_count': stage('restated'), 'stage_3_under_62': stage('stage3'), 'stage_3_62_and_over': stage('stage3_older')}
    total = {str(y): sum(pr[k]['leased_end'][y] for k in pr) for y in yrs}
    L = other(P)
    fund = L['hou-1d-01-standing-emergency-fund']
    per_hh = M['emergency_cost_per_household']
    ec = {str(y): fund[y] * 1e9 / (per_hh * (1 + P['standing_fund_growth']) ** (y - 2031)) for y in (2031, 2035, 2040)}
    rep = P['repair_fund_ba']
    homes = {str(y): rep[y] * 1e9 / M['repair_cost_per_home'] for y in (2030, 2035, 2039)}
    buyers = sum(P['down_payment_ba'].values()) * 1e9 / M['buyer_help_average']
    s2 = sum(pr[k]['leased_end'][2040] for k in ('stage2', 'wider', 'restated'))
    s3 = sum(pr[k]['leased_end'][2042] for k in ('stage3', 'stage3_older'))
    bands = [
        {'program': 'Stage 1 (HOU-4A.01, 2030-33): people with no home of their own', 'income_band': 'no separate income test in HOU-4.03; the voucher rules\' income limits apply (most awards go to extremely low-income households under 42 U.S.C. 1437n(b); not modeled)',
         'leased': pr['4a']['leased_end'][2034], 'year': 'FY2034',
         'against': {'people homeless on a night, 2025 (EV-HOU-014)': M['homeless_night_2025'], 'people who used shelter over FY2022 (EV-HOU-427)': M['shelter_users_fy2022']},
         'note': 'people and households are different units, so the counts give scale, not a share'},
        {'program': 'Stage 2 (HOU-4D.01): extremely low-income families with children, severe problems, and families with no home of their own',
         'income_band': 'at or below 30% of area median income (extremely low income)', 'leased': s2, 'year': 'FY2040',
         'against': {'ELI families with children with worst case needs, 2023 (EV-HOU-186)': M['eli_families_worst_case_m'] * 1e6},
         'share_of_pool': s2 / (M['eli_families_worst_case_m'] * 1e6),
         'note': 'the wider entry adds doubled-up and homeless families outside HUD\'s renter count, so the share overstates coverage of HUD\'s group; the financing settlement (DEC-2026-11-24-09) caps stage 2 at about 810,000 in FY2040'},
        {'program': 'Stage 3 (HOU-4.08): extremely low-income renters with long-term disabilities, every age',
         'income_band': 'at or below 30% of area median income', 'leased': s3, 'year': 'FY2042',
         'against': {'VLI renters with a disabled member under 62, worst case needs (EV-HOU-371)': M['vli_disabled_worst_case_m'] * 1e6,
                     'ELI older-adult households with worst case needs (EV-HOU-186)': M['eli_older_worst_case_m'] * 1e6}},
        {'program': 'Stages 2 and 3 together', 'income_band': 'extremely low income', 'leased': s2 + s3, 'year': 'FY2040 and FY2042',
         'against': {'ELI renter households with worst case needs, 2023 (EV-HOU-186)': M['eli_worst_case_m'] * 1e6},
         'share_of_pool': (s2 + s3) / (M['eli_worst_case_m'] * 1e6),
         'note': 'about 2.5 million ELI worst-case households (single adults and older renters who are not disabled, and families at 30-50% of AMI) wait for the 2040s route (HOU-4.03), unfunded in R2'},
        {'program': 'Emergency fund (HOU-1D.01)', 'income_band': 'at or below 50% of area median income, or enrolled in SNAP, Medicaid or SSI (very low income)',
         'households_a_year': ec},
        {'program': 'Home repair fund (HOU-12.01)', 'income_band': 'owners at or below 80% of AMI (grants); 80-120% (loans)', 'homes_a_year': homes},
        {'program': 'Down payment help (HOU-10.01)', 'income_band': 'first-time buyers up to 140% of AMI (160% in high-cost areas)', 'buyers_fy2030_39': buyers},
    ]
    return {'leased_by_stage': by_stage, 'leased_total': total, 'by_income_band': bands,
            'existing_voucher_households_2023': M['voucher_households_m'] * 1e6}


# ------------------------------------------------------------------ rents where supply is short
def rents(leased=None):
    """Landlord capture and spillover ranges on the added rent subsidy in tight markets: reported beside the cost,
    never added to it. Each reading runs one input across its range with the others central."""
    P = load('central')
    _, pr = rental(P, leased)
    sub = {y: sum(pr[k]['rent'][y] for k in pr) for y in YEARS}      # added rent subsidy, $ billion
    M = {r['id']: r for r in _read(MARKET)}
    v = lambda k, c='value': float(M[k][c])
    out = {'added_rent_subsidy': {'fy2030_39': window(sub), 'fy2040': sub[2040], 'fy2045': sub[2045]}, 'readings': {}}
    for case in ('low', 'central', 'high'):
        col = {'low': 'low', 'central': 'value', 'high': 'high'}[case]
        ts = v('tight_share', col)
        cap_t, cap_e = v('pass_through_tight', col), v('pass_through_elastic', col)
        sp = {'low': 0.0, 'central': None, 'high': v('spillover_ratio_tight_high')}[case]
        r = {}
        for label, base in (('fy2030_39', window(sub)), ('fy2040', sub[2040])):
            tight = base * ts
            r[label] = {'tight_market_subsidy': tight, 'landlord_capture_tight': tight * cap_t,
                        'landlord_capture_other': (base - tight) * cap_e,
                        'landlord_capture_share_of_all': (tight * cap_t + (base - tight) * cap_e) / base,
                        'spillover_to_unassisted_tight': None if sp is None else tight * sp}
        out['readings'][case] = r
    out['spillover_note'] = ('rent paid by unassisted low-income renters in tight markets: 0 (EV-HOU-096) to the high reading, '
                             'which applies Susin\'s 1974-93 ratio of 1.41 (EV-HOU-397) "if the ratio held"; no central reading, '
                             'since the evidence is split (7-validation.md 5.1); never added to landlord capture or to the cost')
    out['unassisted_rent_rise_tight_pct'] = [0.0, v('spillover_pct_tight_high')]
    sh = v('tight_share')
    out['sweep_tight_share'] = {f'{s:.2f}': {'landlord_capture_fy2040': sub[2040] * (s * v('pass_through_tight') + (1 - s) * v('pass_through_elastic'))}
                                for s in (v('tight_share', 'low'), sh, v('tight_share', 'high'))}
    out['supply_range'] = supply()
    out['design_features'] = [
        {'feature': 'Neighborhood payment limits (HOU-4.05, Small Area FMRs)', 'direction': 'lowers capture', 'evidence': 'EV-HOU-095; EV-HOU-158'},
        {'feature': 'Payment standards up to 120% where lease-up is low', 'direction': 'raises capture, in exactly the tight markets and near-ceiling units', 'evidence': 'EV-HOU-096; EV-HOU-095'},
        {'feature': 'Attached homes built or bought in tight markets (HOU-4.04, HOU-3C)', 'direction': 'lowers it, by the net homes they add', 'evidence': 'EV-HOU-114; EV-HOU-115; EV-HOU-133'},
        {'feature': 'Phase-in of 250,000 awards a year; the 2037 right', 'direction': 'the phase-in lowers short-run pressure; the right lifts the cap on demand', 'evidence': 'no register evidence on size (7-validation.md 5.1)'},
    ]
    out['warning_signal'] = ("7-validation.md section 6: rent growth for units near the payment standard more than 2 points a year above "
                             "other units for two years, in tight markets, triggers a review (8-change-our-minds.md)")
    return out


def supply():
    M = {r['id']: r for r in _read(MARKET)}
    v = lambda k, c='value': float(M[k][c])
    lo_add, hi_add = v('net_add_per_subsidized_low'), v('net_add_per_subsidized_high')
    c_lo, c_hi = v('construction_homes_m', 'low'), v('construction_homes_m', 'high')
    return {'statement': 'a range from the evidence, not a forecast',
            'homes_paid_for_directly_m': [v('direct_homes_m', 'low'), v('direct_homes_m'), v('direct_homes_m', 'high')],
            'construction_money_homes_m': [c_lo, v('construction_homes_m'), c_hi],
            'net_homes_added_m': [0.0, c_hi * hi_add],
            'net_homes_added_basis': ('0 if building is fully offset (EV-HOU-115, tax credits) to the construction money\'s high count times '
                                      'EV-HOU-114\'s half a home; 7-validation.md 1.4 reads about 0.2-0.5 million'),
            'shortage_eli_m': v('shortage_eli_m'), 'shortage_national_m': [v('shortage_national_low_m'), v('shortage_national_high_m')],
            'local_rent_effect': 'each 10% more housing nearby lowers rents about 1% (EV-HOU-133); a local effect, not a national elasticity'}


if __name__ == '__main__':
    L = lines()
    for k, d in L.items():
        print(f"{k:48s} {d['window']:8.2f} {d['fy2040']:7.2f} {d['method']}")
    print(totals(L))
