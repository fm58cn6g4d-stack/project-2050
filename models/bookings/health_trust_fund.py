"""health_trust_fund.py: the health system's own account, FY2030-56, under Espen's trust-fund decision (DEC-2026-11-25-12).

Role: analysis for stage G step 10 (dossiers/foundations/fair-financing/8-health-trust-fund.md). Status: analysis; it
books nothing and changes no adopted input. It reads the budget model's booked case `mixed` (the settlement on, every
line as booked) and regroups the health lines into one account, the plan's fund (HLT-7.22):

  inflows  = the health system's dedicated sources: the unified health contribution (HCU, with the settlement's rate
             rise S06 and avoidance allowance S03, and the fold-in rows HCW, HCA (S02), HCP, HCH it replaces), the
             employer contribution (HEC, HEX), the tax on former premiums (HX, which DEC-2026-11-15-20 credits to
             health's need), the five health streams (HS1-HS4 with the stack cap S04, H1a, and HI's early H1a and
             HLT-6 Part A credit), and, in the wider scope, the states' long-term care payment (S05);
  outflows = the health system's expenses: HLT-1, -2, -4, -6, -7, -8 (DEC-2026-11-15-20's scope) and, in the wider
             scope, long-term care and the care workforce rows in the single plan from 2035 (HLT-9 to -11);
  balance  = inflows - outflows; a deficit is the general-fund transfer the account needs beyond the general revenue
             already committed to it in the baseline (health's "first call", DEC-2026-11-15-20).

All figures are increments to CBO's baseline, as every line in the budget model is: the general revenue the baseline
already spends on Medicare, Medicaid and the subsidies, and today's HI payroll tax, are committed to the plan's fund by
the plan's law (dossiers/foundations/health-financing.md part 2.1) and are not repeated here.

    python3 models/bookings/health_trust_fund.py            # print the account and the redraft
    python3 models/bookings/health_trust_fund.py --write    # write the dossier note
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'models/tools/financing-protection'))
import packages as K      # noqa: E402
import budget_scan as S   # noqa: E402

NOTE = ROOT / 'dossiers/foundations/fair-financing/notes/health-trust-fund-results.md'
YEARS = list(range(2030, 2057))
BOOKED_R = 3.80
FLOOR_R = 3.25

# the health contribution itself (what Espen's rule is about) and the rows it replaces (worker HI, the 0.9%, HI on
# former premiums, H1b's wage half)
CONTRIBUTION = ['HCU', 'Settlement S06', 'Settlement S03']
FOLD_IN = ['HCW', 'HCA', 'Settlement S02', 'HCP', 'HCH']
OTHER_SOURCES = ['HEC', 'HEX', 'HX', 'HS1', 'HS2', 'Settlement S04', 'HS3', 'HS4', 'H1a',
                 'HI H1a and Part A HLT-6 share']
HEALTH_SPENDING = ['HLT-1', 'HLT-2', 'HLT-4', 'HLT-6', 'HLT-7', 'HLT-8']
CARE_SPENDING = ['HLT-9', 'HLT-10', 'HLT-11']
CARE_SOURCES = ['Settlement S05']


def lines_of(case):
    out = {}
    for a in case['audit']:
        name = a['line']
        key = name.split(':')[0] if name.startswith('Settlement S') else name
        out.setdefault(key, {y: 0.0 for y in range(2026, 2057)})
        out[key][a['year']] = out[key].get(a['year'], 0.0) + a['primary_deficit_change_bn']
    return out


def grp(L, names, y):
    """The group's effect on the general fund ($B, + raises the gap) in year y; revenue rows are negative."""
    return sum(L.get(n, {}).get(y, 0.0) for n in names)


def account(case):
    L = lines_of(case)
    missing = [n for n in CONTRIBUTION + FOLD_IN + OTHER_SOURCES + HEALTH_SPENDING + CARE_SPENDING + CARE_SOURCES
               if n not in L]
    if missing:
        raise KeyError('lines not in the booked case: %s' % missing)
    hcu = L['HCU']
    rows = {}
    for y in YEARS:
        contrib = -grp(L, CONTRIBUTION, y)
        fold = -grp(L, FOLD_IN, y)          # negative: the HI revenue the contribution replaces
        other = -grp(L, OTHER_SOURCES, y)
        spend = grp(L, HEALTH_SPENDING, y)
        care = grp(L, CARE_SPENDING, y)
        care_src = -grp(L, CARE_SOURCES, y)
        per_point = S.PER_POINT_2040 * hcu[y] / hcu[2040] if hcu[2040] else 0.0
        rows[y] = dict(contribution=contrib, fold=fold, other=other, spend=spend, care=care, care_src=care_src,
                       balance=contrib + fold + other - spend,
                       balance_wide=contrib + fold + other + care_src - spend - care,
                       hi=-L['HI H1a and Part A HLT-6 share'].get(y, 0.0), per_point=per_point, gap=next(r['agenda_gf_primary_bn'] for r in case['rows'] if r['year'] == y))
    return rows


def rate_for(rows, y, share, wide=False):
    """The base rate at which the account, after a general-fund share `share` ($B), balances in year y."""
    r = rows[y]
    bal = r['balance_wide'] if wide else r['balance']
    return BOOKED_R + (-bal - share) / r['per_point']


def redraft(rows, case, gross=None):
    """Three ways to define the general fund's share of the plan's fund from FY2040, each set so the rate is the
    booked 3.80% in FY2040, and the rate each then needs, year by year (the wide scope, with long-term care). FY2035-39
    stay at 3.80% by law: the transition years, which the fund's own reserve from FY2030-34 meets (part 3 of the note).
      C_residual:         R fixed in law; the general fund pays whatever the fund lacks (the booking's arithmetic);
      A_contribution_share: the contribution pays a fixed share of the fund's spending (Medicare Part B's model, where
                          premiums are set at 25% of cost and general revenue pays the rest); R floats with that share;
      B_gf_share:         the general fund pays a fixed share of the fund's spending; R and the other sources the rest.
    `gross` adds the baseline's own federal health spending to the fund's spending (a sensitivity: in law the shares
    would be read on the fund's whole spending)."""
    y0 = 2040
    exp = {y: rows[y]['spend'] + rows[y]['care'] + (gross[y] if gross else 0.0) for y in YEARS}
    contrib_share = rows[y0]['contribution'] / exp[y0]
    gf0 = -rows[y0]['balance_wide'] + (gross[y0] if gross else 0.0)    # the general fund's whole payment in FY2040
    gf_share = gf0 / exp[y0]
    out = {}
    for y in YEARS:
        if y < y0:
            continue
        r = rows[y]
        a = BOOKED_R + (contrib_share * exp[y] - r['contribution']) / r['per_point']
        b = rate_for(rows, y, gf_share * exp[y] - (gross[y] if gross else 0.0), wide=True)
        gf_a = -r['balance_wide'] - (a - BOOKED_R) * r['per_point']
        out[y] = dict(C_residual=(-r['balance_wide'], BOOKED_R), A_contribution_share=(gf_a, a),
                      B_gf_share=(gf_share * exp[y] - (gross[y] if gross else 0.0), b))
    return out, contrib_share, gf_share


def debt_with_rate(ctx, rates):
    """The booked case with the base rate moved to `rates[y]` from 2035 (each point at HCU's per-point yield)."""
    base = K.m.build_case('mixed', ctx.f, ctx.b, ctx.old, ctx.u)
    rows = account(base)
    adj = {str(y): -(rates.get(y, BOOKED_R) - BOOKED_R) * rows[y]['per_point'] for y in YEARS if y >= 2035}
    c = K.m.build_case('rate', ctx.f, ctx.b, ctx.old, ctx.u, spending_adjustments={'rate': {'annual_bn': adj}})
    return {r['year']: r for r in c['rows']}


def gross_baseline():
    """The baseline's own federal health spending (CBO's Medicare, net of premiums, and other health), $B, FY2030-56:
    the money the plan's law commits to the fund. A sensitivity only (part 2 of the note)."""
    return {y: float(S.BASE[y]['out_medicare_net']) + float(S.BASE[y]['out_health_other']) for y in YEARS}


def reserve(rows, keep):
    """The fund's own reserve if FY2030-34's surplus stays in it: the part that reaches the general fund's figures (the
    surplus less HI's credit of H1a and HLT-6's Part A share, which HI already holds and which folds into the fund in
    2035), `keep` held back as a standing reserve (G6 C's $250B), the rest drawn to lower the general fund's transfer in
    FY2035-39, earliest first."""
    built = sum(rows[y]['balance_wide'] - rows[y]['hi'] for y in range(2030, 2035))
    spend = built - keep
    draw = {}
    for y in range(2035, 2040):
        d = min(spend, -rows[y]['balance_wide'])
        draw[y] = d
        spend -= d
    return built, draw


def run():
    ctx = K.Context()
    case = K.m.build_case('mixed', ctx.f, ctx.b, ctx.old, ctx.u)
    rows = account(case)
    rd, cs, gs = redraft(rows, case)
    rdg, csg, gsg = redraft(rows, case, gross_baseline())
    debt = {r['year']: r for r in case['rows']}
    variants = {}
    for k in ('A_contribution_share', 'B_gf_share'):
        variants[k] = debt_with_rate(ctx, {y: rd[y][k][1] for y in rd})
    rates = sorted({FLOOR_R, BOOKED_R, round(rd[2056]['A_contribution_share'][1], 2), round(rd[2056]['B_gf_share'][1], 2)})
    th = S.take_home(rates)
    built, draw = reserve(rows, 250.0)
    hf = case['health_fund']      # the fund as the budget model books it (settlement.json's health_fund)
    fund = dict(built_2030_34=sum(hf[y]['balance'] for y in range(2030, 2035)), standing=hf[2039]['reserve'],
                transfer={y: hf[y]['transfer'] for y in YEARS}, reserve={y: hf[y]['reserve'] for y in YEARS})
    fund['drawn'] = fund['built_2030_34'] - fund['standing']
    return dict(rows=rows, redraft=rd, shares=(cs, gs), redraft_gross=rdg, shares_gross=(csg, gsg), debt=debt,
                variants=variants, take_home=th, reserve=(built, draw), fund=fund)


def f(x):
    return '%.1f' % x


def markdown(r):
    rows, rd = r['rows'], r['redraft']
    show = [2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2042, 2045, 2048, 2050, 2053, 2056]
    gdp = {y: r['debt'][y]['gdp_bn'] for y in YEARS}
    L = ['# The health system\'s own account: results', '',
         'Generated by `models/bookings/health_trust_fund.py --write` after the common rebuild (stage G step 10; '
         'regenerated in step 11 and checked by `test_health_trust_fund.py`, so it can\'t go stale). The '
         'budget model\'s booked case `mixed` (the settlement on, the base rate at 3.80% from 2035, the health fund its own account), with the health '
         'lines regrouped into the plan\'s fund (HLT-7.22). Nominal $B, increments to CBO\'s baseline: the general revenue the '
         'baseline already spends on health and today\'s HI tax are committed to the fund by the plan\'s law and are not repeated. '
         'Project arithmetic on exploratory models, not official scores. Read with [`../8-health-trust-fund.md`](../8-health-trust-fund.md).', '',
         '## 1. The account by year', '',
         '"Contribution" is the unified health contribution at the booked rate (HCU, S06, S03); "fold-in" is the HI revenue it '
         'replaces (worker HI, the 0.9%, HI on former premiums, H1b\'s wage half: HCW, HCA with S02, HCP, HCH; negative). '
         '"Other sources" are the employer contribution (HEC, HEX), HX and the five health streams (HS1-HS4 with S04, H1a, and '
         'HI\'s early H1a and HLT-6 Part A credit). "Health spending" is HLT-1, -2, -4, -6, -7 and -8 (`DEC-2026-11-15-20`\'s '
         'scope); long-term care is HLT-9 to -11, in the single plan from 2035 (`DEC-2026-11-11-02`), with the states\' payment '
         '(S05). "Balance" is sources less spending: a minus is the general-fund transfer the fund needs; a plus is health money '
         'the booking spends elsewhere.', '',
         '| FY | Contribution | Fold-in | Other sources | Health spending | Balance, health | Long-term care | States\' LTC payment | **Balance, with long-term care** | % of GDP | Settlement gap (booked) |',
         '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for y in show:
        x = rows[y]
        L.append('| %d | %s | %s | %s | %s | %s | %s | %s | **%s** | %.2f%% | %s |' % (
            y, f(x['contribution']), f(x['fold']), f(x['other']), f(x['spend']), f(x['balance']), f(x['care']),
            f(x['care_src']), f(x['balance_wide']), 100 * x['balance_wide'] / gdp[y], f(x['gap'])))
    s30 = sum(rows[y]['balance'] for y in range(2030, 2035))
    s30w = sum(rows[y]['balance_wide'] for y in range(2030, 2035))
    s35 = sum(rows[y]['balance_wide'] for y in range(2035, 2040))
    pos = [y for y in YEARS if rows[y]['balance_wide'] > 0]
    pos_c = [y for y in YEARS if rows[y]['contribution'] > rows[y]['spend'] + rows[y]['care']]
    contrib_early = sum(rows[y]['contribution'] for y in range(2030, 2035))
    L += ['', '- **Sources above expenses, spent elsewhere by the booking:** %s over FY2030-34 (health scope %s): %s. The contribution collects %s in those years, so the surplus is less than the contribution itself.' % (
        f(s30w), f(s30), ', '.join('FY%d' % y for y in pos) or 'none', f(contrib_early)),
          '- **The contribution alone above the fund\'s new spending:** %s.' % (', '.join('FY%d' % y for y in pos_c) or 'in no year'),
          '- **FY2035-39:** balance %s in all, which the booking\'s general fund covers.' % f(s35),
          '- **The general-fund transfer from FY2040** (beyond the baseline\'s own): FY2040 %s, FY2045 %s, FY2050 %s, FY2056 %s.' % (
              f(-rows[2040]['balance_wide']), f(-rows[2045]['balance_wide']), f(-rows[2050]['balance_wide']), f(-rows[2056]['balance_wide'])),
          '- **A point of the base rate** raises %s in FY2040 and %s in FY2056 (`budget_scan.PER_POINT_2040`, grown on HCU\'s path). The rate at which the contribution would pay all of the fund\'s new cost, with no transfer beyond the baseline\'s: %.2f%% in FY2040, %.2f%% in FY2056.' % (
              f(rows[2040]['per_point']), f(rows[2056]['per_point']),
              BOOKED_R - rows[2040]['balance_wide'] / rows[2040]['per_point'], BOOKED_R - rows[2056]['balance_wide'] / rows[2056]['per_point']),
          '- **That ceiling by year** (the rate above which the contribution would pay more than the fund\'s new cost): ' + ', '.join(
              'FY%d %.2f%%' % (y, BOOKED_R - rows[y]['balance_wide'] / rows[y]['per_point']) for y in range(2035, 2057)) + '.',
          '', '## 2. The rate the fund needs, by how the general fund\'s share is defined', '',
          'Each rule is set so the rate is the booked 3.80%% in FY2040; FY2035-39 stay at 3.80%% (the transition years, met by the fund\'s reserve, part 3). '
          'A: the contribution pays a fixed %.1f%% of the fund\'s new spending (Medicare Part B\'s model, premiums at 25%% of cost). '
          'B: the general fund pays a fixed %.1f%% of it. C: the rate fixed in law, the general fund the residual (the booking). Each cell: the general fund\'s transfer ($B) / the rate.' % (
              100 * r['shares'][0], 100 * r['shares'][1]), '',
          '| FY | A: contribution\'s share fixed | B: general fund\'s share fixed | C: rate fixed, general fund the residual | A on the fund\'s whole spending (sensitivity) | B on the fund\'s whole spending (sensitivity) |',
          '| --- | --- | --- | --- | --- | --- |']
    g = r['redraft_gross']
    for y in [2040, 2042, 2045, 2048, 2050, 2053, 2056]:
        a, b, c = rd[y]['A_contribution_share'], rd[y]['B_gf_share'], rd[y]['C_residual']
        L.append('| %d | %s / %.2f%% | %s / %.2f%% | %s / %.2f%% | %.2f%% | %.2f%% |' % (
            y, f(a[0]), a[1], f(b[0]), b[1], f(c[0]), c[1], g[y]['A_contribution_share'][1], g[y]['B_gf_share'][1]))
    L += ['', 'The sensitivity adds the baseline\'s own federal health spending (CBO\'s Medicare net of premiums and other health) to the fund\'s spending, '
          'with the shares re-set on that whole (A: %.1f%%; B: %.1f%%, the general fund\'s whole payment, the baseline\'s included).' % (100 * r['shares_gross'][0], 100 * r['shares_gross'][1])]
    built, draw = r['reserve']
    hi_early = sum(rows[y]['hi'] for y in range(2030, 2035))
    L += ['', '## 3. The fund\'s reserve if FY2030-34\'s surplus stays in it', '',
          '- Of FY2030-34\'s surplus, %s is HI\'s credit of H1a and HLT-6\'s Part A share, which HI already holds and which folds into the fund in 2035.' % f(hi_early),
          '- The rest, which reaches the general fund\'s figures, built over FY2030-34: %s. Held as the fund\'s standing reserve: 250.0 (G6 C\'s amount). Drawn to lower the general fund\'s transfer: %s.' % (
              f(built), ', '.join('FY%d %s' % (y, f(v)) for y, v in draw.items() if v)),
          '- Unified debt is unchanged: the money is the same; only the split between the general fund and the fund moves. The general fund\'s own FY2030-34 position is %s worse, and its FY2035-39 transfer %s smaller.' % (f(built), f(sum(draw.values()))),
          '- Interest the fund would be credited on its reserve is an intragovernmental payment, netted out of the unified budget; it is not modeled.',
          '- **As booked** (stage G step 11; `settlement.json`\'s `health_fund`, `recovery-budget/model.py`\'s `health_fund()`): the fund holds %s built over FY2030-34, keeps %s as its standing reserve and draws %s; the general fund\'s transfer to the fund is %s. HI\'s line is HI\'s own account until the fold-in, so it is not one of the fund\'s sources there.' % (
              f(r['fund']['built_2030_34']), f(r['fund']['standing']), f(r['fund']['drawn']),
              ', '.join('FY%d %s' % (y, f(r['fund']['transfer'][y])) for y in (2035, 2036, 2037, 2038, 2039, 2040, 2045, 2050, 2056))),
          '', '## 4. Debt with the rate set by the fund (% of GDP, the booked plan, no debt goal)', '',
          '| | FY2040 | FY2045 | FY2050 | FY2056 | General-fund gap FY2045 / FY2050 / FY2056 |', '| --- | --- | --- | --- | --- | --- |',
          '| C: booked (R 3.80%% throughout) | %s | %s |' % (' | '.join('%.1f' % r['debt'][y]['debt_gdp'] for y in (2040, 2045, 2050, 2056)),
                                                    ' / '.join(f(r['debt'][y]['agenda_gf_primary_bn']) for y in (2045, 2050, 2056)))]
    for k, lab in (('A_contribution_share', 'A: contribution\'s share fixed'), ('B_gf_share', 'B: general fund\'s share fixed')):
        v = r['variants'][k]
        L.append('| %s | %s | %s |' % (lab, ' | '.join('%.1f' % v[y]['debt_gdp'] for y in (2040, 2045, 2050, 2056)),
                                         ' / '.join(f(v[y]['agenda_gf_primary_bn']) for y in (2045, 2050, 2056))))
    L += ['', '## 5. The take-home test at the rates in question', '',
          'FY2040\'s population and incomes (`budget_scan.take_home`, no VAT). For the later rates this is an indication only: the test runs on FY2040.', '',
          '| Base rate R | Workers ahead | Below 200% of poverty | 250-400% of poverty |', '| --- | --- | --- | --- |']
    for k, v in r['take_home'].items():
        L.append('| %s | %s%% | %s%% | %s%% |' % (k, v['workers'], v['workers_below_200fpl'], v['workers_250_400fpl']))
    return '\n'.join(L) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    a = ap.parse_args()
    md = markdown(run())
    if a.write:
        NOTE.write_text(md)
        print('wrote', NOTE.relative_to(ROOT))
    else:
        print(md)


if __name__ == '__main__':
    main()
