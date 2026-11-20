"""Stage G step 4b: the whole-budget scan's baseline tables and its cut and reallocation options.

Role: prices the options in `dossiers/foundations/fair-financing/3-budget-scan.md` and the memos G10 onward, on the
same budget model and conventions as `packages.py`, against the settlement as Espen decided it on November 20
(`DEC-2026-11-20-05` to `-13`: G1 A, G2 C, G4 C1, G7 B at 1.65 points; no VAT, `DEC-2026-11-20-07`). Whatever the cuts
don't close falls to the fallback Espen named: a larger health contribution (memo G3 option E). Status: exploratory
screens for a provisional draft. Nothing here is adopted or booked; no file under `models/data/inputs/` is read for
writing. Stage G's step 7 books what Espen decides.

Run after the common rebuild (`bash models/tools/run-all.sh`):
    python3 models/tools/financing-protection/budget_scan.py            # JSON
    python3 models/tools/financing-protection/budget_scan.py --markdown # the tables in notes/budget-scan-results.md

Conventions (as `packages.py`): nominal $B, federal fiscal years, case `mixed`; an adjustment is positive when it raises
the general-fund gap, so a cut is negative. A cut enters `build_case` as an "Exploratory: ..." outlay adjustment; a tax
item as an outlay-equivalent adjustment, which moves the general-fund and unified balances by the right amount. The
fiscal rule tests the general-fund *primary* balance, so interest saved never counts toward closing a year; it shows in
debt and net interest, reported beside the gap.
"""
import argparse
import csv
import json
import math

import packages as K

m = K.m
ROOT = K.ROOT
YEARS = K.YEARS

# ---------------------------------------------------------------- the decided base (November 20)
DECIDED = [x if x[0] != 'education_rate' else ('education_rate', {'rate': 1.65}) for x in K.REC_BASE]

# The fallback's price: memo G2's fold, about $56B a quarter point of the health contribution's base rate R in FY2040,
# grown on HCU's path (health-household-contribution.md section 2; packages.HCU_PER_QUARTER_POINT_2040). Linear: the
# avoidance allowance at higher rates is a risk (2-settlement.md part 5), not modelled here.
R_DECIDED = 3.25
PER_POINT_2040 = 4 * K.HCU_PER_QUARTER_POINT_2040


def _csv(path):
    return list(csv.DictReader(open(ROOT / path)))


BASE = {int(r['year']): r for r in _csv('models/data/fiscal-baseline.csv')}
PRICE = {int(r['year']): float(r['gdp_price_index']) for r in _csv('models/data/budget/deflators.csv') if r['gdp_price_index']}


def base_path(col):
    return {y: float(BASE[y][col]) for y in YEARS}


def flat_real(col, from_year):
    """The baseline line held at its `from_year - 1` level in real terms (GDP price index) from `from_year`."""
    b = base_path(col)
    y0 = from_year - 1
    return {y: (b[y0] * PRICE[y] / PRICE[y0] if y >= from_year else b[y]) for y in YEARS}


def priced_from(level_2040, start, ramp, grow='price'):
    """A level in FY2040, grown with the GDP price index (or GDP), phased in from `start` over `ramp` years."""
    g = PRICE if grow == 'price' else {y: float(BASE[y]['gdp']) for y in YEARS}
    return {y: level_2040 * g[y] / g[2040] * m.phase(y, start, ramp) for y in YEARS}


def neg(p):
    return {y: -v for y, v in p.items()}


# ---------------------------------------------------------------- the options (each: label, adjust, range, d3 note)
def opt_defense_flat_real(ctx, from_year=2037):
    """NSC-1A's rule, defense "roughly flat in real terms" (D9; legacy/domains/domain-national-security.md, NSC-1), held
    after FY2036. CBO's ten-year baseline already grows defense with inflation to FY2036, so NSC-1A costs nothing
    there; after FY2036 the baseline grows discretionary spending with GDP (`categories.csv`, gdp_share_split). From
    FY2037 to FY2039 that is NSC-1A's own rule; from FY2040 it extends it."""
    b = base_path('out_disc_defense')
    fr = flat_real('out_disc_defense', from_year)
    return dict(label='Defense held flat in real terms from FY%d (NSC-1A extended)' % from_year,
                adjust={'Defense flat real from FY%d' % from_year: {y: fr[y] - b[y] for y in YEARS}}, d3=[])


def opt_defense_restructure(ctx, share=0.05, start=2031, ramp=3, on_flat_real=True):
    """Targeted restructuring: about `share` below the path by FY2033 (memo G10: the nuclear path restructured, Golden
    Dome held to research, procurement mix, service contracts and headquarters, TRICARE fees for working-age
    retirees). Range 3-7%: no CBO score of this package exists; CBO's deepest topline option is about 10%."""
    path = flat_real('out_disc_defense', 2037) if on_flat_real else base_path('out_disc_defense')
    return dict(label='Defense restructured, %.0f%% below the path by FY%d' % (100 * share, start + ramp - 1),
                adjust={'Defense restructured %.0f%%' % (100 * share): {y: -share * path[y] * m.phase(y, start, ramp) for y in YEARS}},
                d3=[])


def opt_defense_topline(ctx, share=0.10, start=2031, ramp=4):
    """CBO's topline option (Options for Reducing the Deficit, 2025 to 2034, option 28, about $1T over ten years,
    read via search extract): `share` below the baseline at maturity, baseline growth."""
    b = base_path('out_disc_defense')
    return dict(label='Defense topline %.0f%% below the baseline (CBO option 28 scale)' % (100 * share),
                adjust={'Defense topline %.0f%%' % (100 * share): {y: -share * b[y] * m.phase(y, start, ramp) for y in YEARS}},
                d3=[])


# Farm programs. CRS R48775 [SRC-2113], Table 1: the 2025 law's non-nutrition agriculture title adds $65.690B over
# FY2025-34, of which commodity programs +$53.060B and crop insurance +$5.980B (CBO's score). Reversing those two is
# about $5.9B a year on average; FY2040 working figure $6.5B (range 3-10: PLC payments depend on prices).
FARM_OBBBA_2040 = (6.5, 3.0, 10.0)
# Crop insurance reform: the legacy menu's REV-SC3, $0.05T over FY2030-39 (range 0.03-0.10;
# legacy/domains/domain-revenue.md line 381): premium subsidies cut toward 40% for the costliest policies and the
# insurers' reimbursement and return capped. About $5B in FY2040 (range 3-10).
CROP_2040 = (5.0, 3.0, 10.0)


def opt_farm_obbba(ctx, end='central'):
    lvl = dict(zip(('central', 'low', 'high'), FARM_OBBBA_2040))[end]
    return dict(label="The 2025 law's commodity and crop-insurance increases reversed ($%.1fB in FY2040)" % lvl,
                adjust={'Farm: 2025 increases reversed': neg(priced_from(lvl, 2030, 2))},
                d3=[('absent', 'farm payments: D3 has no farm-payment row')])


def opt_crop_insurance(ctx, end='central'):
    lvl = dict(zip(('central', 'low', 'high'), CROP_2040))[end]
    return dict(label='Crop insurance reform (REV-SC3; $%.1fB in FY2040)' % lvl,
                adjust={'Farm: crop insurance reform': neg(priced_from(lvl, 2030, 2))},
                d3=[('absent', 'crop insurance: D3 has no farm row')])


# Tax expenditures the plan has not touched (memo G12). FY2029 tax expenditure from JCT's JCX-45-25 [SRC-1266], grown
# with GDP to FY2040, times a behavioral recapture factor (a tax expenditure is not a revenue estimate: JCX-45-25 says
# so). Values filled from the JCT table: (FY2029 total $B, recapture share, label).
TAX_ITEMS = {
    # JCX-45-25 Table 1, FY2029: exclusion of gain from certain small business stock, individuals $5.9B (line 2997);
    # the 2025 law widened it. Recapture 0.7: some gains move to other preferences; HS3 and C18 raise the rate the
    # repealed exclusion's gains then pay, which this ignores (cautious).
    'qsbs': (5.9, 0.7, 'Small business stock (sec. 1202) exclusion repealed'),
    # Deferral of gain on like-kind exchanges, $10.8B in FY2029 (lines 2960, 2996). The booked C38 (REV-TS9) already
    # caps deferral at $500K of gain a year, which reaches most of the dollars; repealing the rest is the remainder.
    # Working share 0.3 (range 0.15-0.45), net of TS9 and of behavior (exchanges become holds).
    'like_kind': (10.8, 0.3, 'Like-kind exchanges repealed beyond the booked $500K cap'),
    # Deduction for mortgage interest, $54.9B in FY2029 (line 2414). A $500K debt cap (from $750K) is about $130B over
    # FY2026-35 on CRFB's offsets bank (via search extract): about 0.18 of the tax expenditure by FY2040. Listed, not
    # recommended (memo G12).
    'mortgage_500k': (54.9, 0.18, 'Mortgage interest deduction capped at $500K of debt'),
}


def opt_tax_item(ctx, key):
    te_2029, recapture, label = TAX_ITEMS[key]
    lvl = te_2029 * recapture * float(BASE[2040]['gdp']) / float(BASE[2029]['gdp'])
    return dict(label='%s ($%.1fB in FY2040)' % (label, lvl),
                adjust={'Tax: ' + key: neg(priced_from(lvl, 2030, 1, grow='gdp'))}, d3=[])


def opt_fallback(ctx, rate):
    """Memo G3 option E, the fallback (`DEC-2026-11-20-07`): the health contribution's base rate R above G2 C's 3.25%,
    from the 2035 endpoint, at the fold's price."""
    o = K.OPTIONS['fold_broad_points'](ctx, rate=rate)
    o['label'] = 'Fallback: the health contribution at R = %.2f%%' % rate
    return o


OPTIONS = {k[4:]: v for k, v in globals().items() if k.startswith('opt_')}

# ---------------------------------------------------------------- the sets
SETS = {
    'decided': [],
    'defense_flat_real': [('defense_flat_real', {})],
    'defense_restructure_only': [('defense_restructure', {'on_flat_real': False})],
    'defense_recommended': [('defense_flat_real', {}), ('defense_restructure', {})],
    'defense_topline_10': [('defense_topline', {})],
    'farm': [('farm_obbba', {}), ('crop_insurance', {})],
    'tax_recommended': [('tax_item', {'key': 'qsbs'}), ('tax_item', {'key': 'like_kind'})],
    'tax_mortgage_cap': [('tax_item', {'key': 'mortgage_500k'})],
    # The recommended set (memos G10 to G12): defense flat in real terms after FY2036 and restructured 5%; the farm
    # items; the two tax items.
    'recommended': [('defense_flat_real', {}), ('defense_restructure', {}), ('farm_obbba', {}), ('crop_insurance', {}),
                    ('tax_item', {'key': 'qsbs'}), ('tax_item', {'key': 'like_kind'})],
    # The same with defense restructured only (memo G10 B), or at CBO's topline scale (G10 D).
    'recommended_defense_b': [('defense_restructure', {'on_flat_real': False}), ('farm_obbba', {}), ('crop_insurance', {}),
                              ('tax_item', {'key': 'qsbs'}), ('tax_item', {'key': 'like_kind'})],
    'recommended_defense_d': [('defense_topline', {}), ('farm_obbba', {}), ('crop_insurance', {}),
                              ('tax_item', {'key': 'qsbs'}), ('tax_item', {'key': 'like_kind'})],
    # Ranges: every item at its low end (defense restructuring 3%) and at its high end (7%).
    'recommended_low': [('defense_flat_real', {}), ('defense_restructure', {'share': 0.03}), ('farm_obbba', {'end': 'low'}),
                        ('crop_insurance', {'end': 'low'}), ('tax_item', {'key': 'qsbs'})],
    'recommended_high': [('defense_flat_real', {}), ('defense_restructure', {'share': 0.07}), ('farm_obbba', {'end': 'high'}),
                         ('crop_insurance', {'end': 'high'}), ('tax_item', {'key': 'qsbs'}), ('tax_item', {'key': 'like_kind'})],
}


def resolve(ctx, spec):
    out = []
    for name, params in spec:
        out.append((OPTIONS[name] if name in OPTIONS else K.OPTIONS[name])(ctx, **params))
    return out


def run_case(ctx, opts):
    """build_case with the options; returns the gap path, debt, and net interest."""
    kw, adjust = {}, {}
    for o in opts:
        kw.update(o.get('kw', {}))
        for label, path in o.get('adjust', {}).items():
            if label in adjust:
                raise ValueError('option counted twice: ' + label)
            adjust[label] = {'annual_bn': {str(y): v for y, v in path.items()}}
    rate = kw.pop('education_rate', None)
    points = kw.pop('hi_grant_points', None)
    with K.education_rate(rate), K.hi_grant(points):
        c = m.build_case('scan', ctx.f, ctx.b, ctx.old, ctx.u, spending_adjustments=adjust, **kw)
    by = {r['year']: r for r in c['rows']}
    return dict(gap={y: by[y]['agenda_gf_primary_bn'] for y in YEARS},
                debt_gdp={y: by[y]['debt_gdp'] for y in YEARS},
                interest={y: by[y]['interest_bn'] for y in YEARS},
                baseline_debt_gdp={y: 100 * by[y]['baseline_debt_bn'] / by[y]['gdp_bn'] for y in YEARS})


def r_needed(ctx, gap):
    """The health contribution's base rate R each year from FY2040 that closes the gap left (linear at the fold's price)."""
    hcu = ctx.line('HCU')
    return {y: round(R_DECIDED + max(gap[y], 0.0) / (PER_POINT_2040 * hcu[y] / hcu[2040]), 2) for y in range(2040, 2057)}


def evaluate(ctx, name, spec):
    base = run_case(ctx, K.resolve(ctx, DECIDED))
    opts = K.resolve(ctx, DECIDED) + resolve(ctx, spec)
    c = run_case(ctx, opts)
    cut = {y: c['gap'][y] - base['gap'][y] for y in YEARS}
    rn = r_needed(ctx, c['gap'])
    return dict(name=name, options=[o['label'] for o in resolve(ctx, spec)],
                cut={y: round(cut[y], 1) for y in K.SHOW}, cut_2030_39=round(sum(cut[y] for y in m.W), 1),
                left={y: round(c['gap'][y], 1) for y in K.SHOW}, left_2030_39=round(sum(c['gap'][y] for y in m.W), 1),
                r_needed={y: rn[y] for y in (2040, 2045, 2050, 2056)}, r_max=max(rn.values()),
                debt_gdp={y: round(c['debt_gdp'][y], 1) for y in (2040, 2056)},
                interest_saved={y: round(base['interest'][y] - c['interest'][y], 1) for y in (2040, 2056)},
                _gap=c['gap'])


def defense_shares():
    b = base_path('out_disc_defense')
    fr = flat_real('out_disc_defense', 2037)
    gdp = {y: float(BASE[y]['gdp']) for y in YEARS}
    return {y: dict(baseline=round(b[y], 1), baseline_gdp=round(100 * b[y] / gdp[y], 2),
                    flat_real=round(fr[y], 1), flat_real_gdp=round(100 * fr[y] / gdp[y], 2),
                    recommended=round(0.95 * fr[y], 1), recommended_gdp=round(100 * 0.95 * fr[y] / gdp[y], 2))
            for y in (2029, 2036, 2040, 2045, 2050, 2056)}


# ---------------------------------------------------------------- the take-home test (DEC-2026-11-20-06, G2b)
def take_home(rates):
    """Health's take-home test at each base rate R, with no VAT: the unified contribution on the decided steady-rate
    exemption (`take_home_vat.py`'s method). "Health costs only" and "everything counted" are the same here unless a
    cut charges workers directly; the recommended cuts don't (3-budget-scan.md part D)."""
    import take_home_vat as T
    K.PACKAGES['_scan_novat'] = [('education_rate', {'rate': 1.65})]   # any last option but a VAT: rate 0
    T.G2 = {'R = %.2f%%' % r: ('_scan_novat', r, False) for r in rates}
    return T.build()['options']


# ---------------------------------------------------------------- the baseline tables (part A)
FUNCTIONS = {'050': 'National defense', '150': 'International affairs', '250': 'Science, space and technology',
             '270': 'Energy', '300': 'Natural resources and environment', '350': 'Agriculture',
             '370': 'Commerce and housing credit', '400': 'Transportation', '450': 'Community and regional development',
             '500': 'Education, training, employment and social services', '550': 'Health (Medicaid, ACA and other)',
             '570': 'Medicare', '600': 'Income security', '650': 'Social Security', '700': 'Veterans',
             '750': 'Administration of justice', '800': 'General government', '900': 'Net interest',
             '950': 'Undistributed offsetting receipts'}


def by_function(years=(2029, 2032, 2036)):
    out = {}
    for r in _csv('models/data/budget/cbo-spending-by-function.csv'):
        y = int(r['year'])
        if y in years:
            d = out.setdefault(r['function_code'], {}).setdefault(y, {'discretionary': 0.0, 'mandatory': 0.0})
            d[r['disc_or_mand']] += float(r['outlays'])
    return out


def broad(years=(2029, 2036, 2040, 2045, 2050, 2056)):
    cols = ['out_social_security', 'out_medicare_net', 'out_health_other', 'out_other_mandatory', 'out_disc_defense',
            'out_disc_nondefense', 'out_net_interest', 'out_total', 'rev_total', 'deficit']
    return {y: {c: (round(float(BASE[y][c]), 1), round(100 * float(BASE[y][c]) / float(BASE[y]['gdp']), 2)) for c in cols}
            for y in years}


def accounts(titles, years=('FY2029', 'FY2036')):
    """Named CBO accounts' outlays ($B), from the account file (publication 51142, February 2026)."""
    out = {}
    for r in _csv('models/data/cbo/budget_spending_detail_annual_fy_2026-02.csv'):
        for key, test in titles.items():
            if r['date'] in years and test(r):
                out.setdefault(key, {}).setdefault(r['date'], 0.0)
                out[key][r['date']] += float(r['outlays'] or 0) / 1000
    return {k: {y: round(v, 1) for y, v in d.items()} for k, d in out.items()}


PROGRAMS = {
    'DoD operation and maintenance': lambda r: r['function_code'] == '050' and r['bureau'] == 'Operation and Maintenance',
    'DoD military personnel': lambda r: r['function_code'] == '050' and r['bureau'] == 'Military Personnel',
    'DoD procurement': lambda r: r['function_code'] == '050' and r['bureau'] == 'Procurement',
    'DoD research, development, test and evaluation': lambda r: r['function_code'] == '050' and r['bureau'].startswith('Research, Development'),
    'NNSA (nuclear weapons, atomic energy defense)': lambda r: r['bureau'] == 'National Nuclear Security Administration',
    'Crop insurance (FCIC fund)': lambda r: r['title'] == 'Federal crop insurance corporation fund',
    'Commodity Credit Corporation (commodity programs)': lambda r: r['title'] == 'Commodity Credit Corporation fund',
    'VA compensation and pensions': lambda r: r['agency'].startswith('Department of Veterans') and r['title'] == 'Compensation and pensions',
    'VA medical care (services and community care)': lambda r: r['agency'].startswith('Department of Veterans') and r['title'] in ('Medical services', 'Medical Community Care'),
    'Civil service retirement and disability': lambda r: r['title'] == 'Civil service retirement and disability fund',
    'Military retirement fund': lambda r: r['title'] == 'Military retirement fund',
    'SNAP': lambda r: r['title'] == 'Supplemental Nutrition Assistance Program',
    'SSI': lambda r: r['title'] == 'Supplemental security income program',
    'EITC (refundable part)': lambda r: r['title'].startswith('Payment where earned income credit'),
    'Child tax credit (refundable part)': lambda r: r['title'].startswith('Payment Where Child Tax Credit'),
    'ACA premium tax credit': lambda r: r['title'] == 'Refundable Premium Tax Credit',
    'Tenant-based rental assistance': lambda r: r['title'] == 'Tenant based rental assistance',
    'Federal-aid highways': lambda r: r['title'] == 'Federal-aid highways',
    'Student financial assistance (Pell)': lambda r: r['title'] == 'Student financial assistance',
    'Unemployment trust fund': lambda r: r['title'] == 'Unemployment Trust Fund',
}


R_FALLBACK = 3.9   # the lowest rate, to 0.05, that closes FY2040-56 with the recommended set held from 2035


def with_fallback(ctx, R, extra):
    """The decided settlement with the fold at base rate R (the fallback) plus the cut set `extra`."""
    base = [x if x[0] != 'fold_broad_points' else ('fold_broad_points', {'rate': R}) for x in DECIDED]
    return K.resolve(ctx, base) + resolve(ctx, extra), base


def package(ctx, hh=None, R=R_FALLBACK, extra=None):
    extra = SETS['recommended'] if extra is None else extra
    opts, base = with_fallback(ctx, R, extra)
    c = run_case(ctx, opts)
    g = c['gap']
    out = dict(R=R, gap={y: round(g[y], 1) for y in (2035, 2040, 2041, 2042, 2043, 2044, 2045, 2050, 2056)},
               gap_2030_39=round(sum(g[y] for y in m.W), 1),
               worst_year=max(range(2040, 2057), key=lambda y: g[y]), worst=round(max(g[y] for y in range(2040, 2057)), 1),
               debt_gdp={y: round(c['debt_gdp'][y], 1) for y in (2040, 2056)},
               baseline_debt_gdp={y: round(c['baseline_debt_gdp'][y], 1) for y in (2040, 2056)})
    back = {}
    for name, extra_risk in (('without D2', ['without_d2']), ('without HS2', ['without_hs2']),
                             ('without both', ['without_d2', 'without_hs2'])):
        r = run_case(ctx, opts + [K.OPTIONS[k](ctx) for k in extra_risk])['gap']
        hcu = ctx.line('HCU')
        back[name] = {y: (round(r[y], 1), round(max(r[y], 0) / (PER_POINT_2040 * hcu[y] / hcu[2040]), 2)) for y in (2040, 2056)}
    out['backstop'] = back
    if hh is not None:
        d = hh.run([e for o in K.resolve(ctx, base) for e in o.get('d3', [])])
        st = d.pop('_state')
        out['d3'] = d['net']
        out['revenue_mix_2030_39'] = hh.revenue_mix(st)
    return out


def build(with_take_home=True):
    ctx = K.Context()
    out = dict(status='exploratory screens for the provisional budget scan (stage G step 4b); nothing adopted or booked',
               broad=broad(), functions=by_function(), programs=accounts(PROGRAMS), defense=defense_shares(),
               sets={n: evaluate(ctx, n, s) for n, s in SETS.items()})
    for v in out['sets'].values():
        v.pop('_gap')
    out['package'] = package(ctx, K.Household() if with_take_home else None)
    if with_take_home:
        rates = sorted({R_DECIDED, R_FALLBACK, 4.45, 5.0, 5.65} | {math.ceil(20 * v['r_needed'][2040]) / 20 for v in out['sets'].values()})
        out['take_home'] = take_home(rates)
    return out


def markdown(d):
    L = ['# Budget scan: results', '',
         'Generated by `models/tools/financing-protection/budget_scan.py --markdown` after the common rebuild. Exploratory; '
         'nothing here is adopted or booked. Nominal $B, case `mixed`, on the settlement as decided on November 20 '
         '(G1 A, G2 C, G4 C1, G7 at 1.65 points, no VAT). Read with [`../3-budget-scan.md`](../3-budget-scan.md).', '',
         '## The current-law baseline by broad category ($B, % of GDP)', '',
         '| | ' + ' | '.join('FY%d' % y for y in d['broad']) + ' |', '| --- |' + ' --- |' * len(d['broad'])]
    labels = dict(out_social_security='Social Security', out_medicare_net='Medicare (net)',
                  out_health_other='Medicaid, CHIP, ACA credits', out_other_mandatory='Other mandatory',
                  out_disc_defense='Discretionary defense', out_disc_nondefense='Discretionary nondefense',
                  out_net_interest='Net interest', out_total='Total outlays', rev_total='Revenue', deficit='Deficit')
    for c, lab in labels.items():
        L.append('| %s | ' % lab + ' | '.join('%.0f (%.2f%%)' % d['broad'][y][c] for y in d['broad']) + ' |')
    L += ['', '## Outlays by budget function, discretionary and mandatory ($B; CBO account file, February 2026)', '',
          '| Function | FY2029 disc. | FY2029 mand. | FY2036 disc. | FY2036 mand. |', '| --- | --- | --- | --- | --- |']
    for code, name in FUNCTIONS.items():
        f = d['functions'].get(code)
        if f:
            L.append('| %s %s | %.1f | %.1f | %.1f | %.1f |' % (code, name, f[2029]['discretionary'], f[2029]['mandatory'],
                                                          f[2036]['discretionary'], f[2036]['mandatory']))
    L += ['', '## Main programs ($B outlays; CBO account file)', '', '| Program | FY2029 | FY2036 |', '| --- | --- | --- |']
    for k, v in d['programs'].items():
        L.append('| %s | %.1f | %.1f |' % (k, v.get('FY2029', 0), v.get('FY2036', 0)))
    L += ['', '## Defense paths ($B, % of GDP)', '', '| | Baseline | Flat real from FY2037 | Recommended (flat real, 5% restructured) |',
          '| --- | --- | --- | --- |']
    for y, v in d['defense'].items():
        L.append('| FY%s | %.0f (%.2f%%) | %.0f (%.2f%%) | %.0f (%.2f%%) |' % (y, v['baseline'], v['baseline_gdp'], v['flat_real'],
                                                                     v['flat_real_gdp'], v['recommended'], v['recommended_gdp']))
    L += ['', '## The sets, against the decided settlement', '',
          '"Cut" is the set\'s effect on the general-fund gap (− lowers it). "Left" is the gap after it. "R needed" is the '
          'health contribution\'s base rate that would close the year (decided: 3.25%).', '',
          '| Set | Cut FY2040 | FY2045 | FY2056 | FY2030-39 | Left FY2040 | Left FY2056 | R needed FY2040 / 2045 / 2050 / 2056 | Debt FY2056 | Interest saved FY2056 |',
          '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for n, s in d['sets'].items():
        L.append('| %s | %.1f | %.1f | %.1f | %.1f | %.1f | %.1f | %s | %.1f%% | %.1f |' % (
            n, s['cut'][2040], s['cut'][2045], s['cut'][2056], s['cut_2030_39'], s['left'][2040], s['left'][2056],
            ' / '.join('%.2f%%' % s['r_needed'][y] for y in (2040, 2045, 2050, 2056)), s['debt_gdp'][2056],
            s['interest_saved'][2056]))
        L.append('|  ↳ options: %s | | | | | | | | | |' % ('; '.join(s['options']) or 'none (the decided settlement)'))
    p = d['package']
    L += ['', '## The recommended package: the set, with the fallback at R = %.2f%% from 2035' % p['R'], '',
          '| | ' + ' | '.join('FY%d' % y for y in p['gap']) + ' | FY2030-39 |', '| --- |' + ' --- |' * (len(p['gap']) + 1),
          '| General-fund gap ($B) | ' + ' | '.join('%.1f' % v for v in p['gap'].values()) + ' | %.1f |' % p['gap_2030_39'], '',
          '- Closes FY2040 and every later year to FY2056: worst year FY%d, %.1f.' % (p['worst_year'], p['worst']),
          '- Debt, %% of GDP: %.1f in FY2040 (baseline %.1f), %.1f in FY2056 (baseline %.1f).' % (
              p['debt_gdp'][2040], p['baseline_debt_gdp'][2040], p['debt_gdp'][2056], p['baseline_debt_gdp'][2056])]
    if 'd3' in p:
        q = p['d3']
        L.append('- D3 (FY2030-39 average, $ a household a year): Q1 %+d, Q2 %+d, Q3 %+d, Q4 %+d, Q5 %+d, top 1%% %+d. '
                 'D3 has no rows for defense, farm payments or the two tax items, so they do not move it.' % (
                     q['Q1'], q['Q2'], q['Q3'], q['Q4'], q['Q5'], q['T1']))
        L.append('- Revenue-mix test, FY2030-39: %.0f%%.' % p['revenue_mix_2030_39'])
    L += ['', '### The backstop (memo G13): the gap if D2 or HS2 fails, and the base-rate points that would close it', '',
          '| | FY2040 gap | R points | FY2056 gap | R points |', '| --- | --- | --- | --- | --- |']
    for k, v in p['backstop'].items():
        L.append('| %s | %.1f | +%.2f | %.1f | +%.2f |' % (k, v[2040][0], v[2040][1], v[2056][0], v[2056][1]))
    if 'take_home' in d:
        L += ['', '## The take-home test with no VAT (FY2040)', '',
              '| Base rate R | Workers ahead (health costs only) | Workers ahead, everything counted | Below 200% of poverty | 250-400% of poverty | Retirees and others |',
              '| --- | --- | --- | --- | --- | --- |']
        for k, v in d['take_home'].items():
            L.append('| %s | %s%% | %s%% | %s%% | %s%% | %s%% |' % (k, v['workers_no_vat'], v['workers'], v['workers_below_200fpl'],
                                                           v['workers_250_400fpl'], v['others_b']))
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--markdown', action='store_true')
    ap.add_argument('--no-take-home', action='store_true')
    a = ap.parse_args()
    d = build(with_take_home=not a.no_take_home)
    print(markdown(d) if a.markdown else json.dumps(d, indent=1, default=str))
