"""Financing screens for stage G's settlement: the option library and the packages that `2-settlement.md` prices.

Role: one home for each option the settlement draft weighs (`dossiers/foundations/fair-financing/2-settlement.md`,
memos G1-G8). Each option is priced on the budget model's case `mixed` (`models/tools/recovery-budget/model.py`
`build_case`), as an explicit adjustment or a build_case argument, and on the D3 household test (scenario Q-H7, the
package the gap books; `models/tools/household/d3.py`). Status: exploratory screens for a provisional draft. Nothing
here is adopted or booked: no file under `models/data/inputs/` is read for writing, and G7 books what Espen decides.

Run after the common rebuild (`bash models/tools/run-all.sh`, which writes `build/`):
    python3 models/tools/financing-protection/packages.py            # JSON to stdout
    python3 models/tools/financing-protection/packages.py --markdown # the tables in the settlement's results note

Conventions:
  * Nominal $B, federal fiscal years. An adjustment is positive when it raises the general-fund gap.
  * Revenue options enter `build_case` as outlay-equivalent adjustments ("Exploratory: ..." audit lines). That moves
    the general-fund and unified primary balances by the right amount; it is not a revenue/outlay classification.
  * D3 amounts are FY2030-39 totals ($T), as the D3 test uses them. A row the test does not carry is reported as such.

This replaces the pre-PR26 historical ceilings that lived here (`focused_recovery`, `infrastructure_rebalance`); they
are in Git history. `climate_bridge.py` is unchanged.
"""
import argparse
import contextlib
import importlib.util
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
_spec = importlib.util.spec_from_file_location('rb_settlement', ROOT / 'models/tools/recovery-budget/model.py')
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)

YEARS = list(range(2026, 2057))
SHOW = (2030, 2035, 2040, 2045, 2050, 2056)

# ---------------------------------------------------------------- working figures (each with its source)
# Health's household contribution (HCU): the base rate's share of its FY2040 net yield. At R = 2.25% a quarter point
# moves booked revenue taken by $56B (health-household-contribution.md section 2: 516 -> 460 from 2.25% to 2.5%), so
# the base rate raises about 2.25 * 224 = $504B of HCU's $770.3B; the surcharge the rest.
HCU_BASE_SHARE = 504.0 / 770.3
HCU_PER_QUARTER_POINT_2040 = 56.0      # the same table: one quarter point of R in FY2040, net
# The 0.9% Additional Medicare Tax (HCA): booked at $53.5B in FY2040, a working figure; probably nearer $70B
# (1-audit.md part B1; health-household-contribution.md section 6).
HCA_REDERIVED_2040 = 70.0
# The stack cap menu (dossiers/foundations/notes/stack-2026-11-16.md part 4): FY2040 cost, central and range ($B).
CAP_MENU = {
    'A': ('No cap', 0, 0, 0),
    'B1': ('Drop the 3% tier', 16, 13, 20),
    'B2': ('Tiers at 1.5% / 2.5%', 23, 21, 26),
    'C1': ('Combined ceiling at 100% of a 6% imputed return', 40, 30, 55),
    'D2': ('Billionaires pay the larger of G11 or the wealth tax', 50, 35, 75),
    'D1': ('Income taxes on capital credited against the wealth tax', 100, 80, 120),
    'C2': ('Combined ceiling at 75%', 125, 100, 145),
}
# A value-added tax: about $105B a point in FY2040 on a broad base (checkpoint-financing.md part A4), from CBO's 5%
# broad-base option, $3.5T over 2026-35, about $4.2T over FY2030-39 (legacy/sources/revenue-channels-and-full-menu.md,
# line 112; legacy/domains/domain-revenue.md, "Other choices"). CBO's scores of indirect taxes are already net of the
# income and payroll tax offset (domain-revenue.md, REV-CX), so no second offset is taken. The general fund keeps that
# net yield; the trust funds are held harmless for their share of the payroll offset by a transfer from it, so Social
# Security and HI do not move. Households bear the gross tax: D3 charges net / (1 - 0.25) on the consumption key.
VAT_POINT_2040 = 105.0
EXCISE_OFFSET = 0.25


class Context:
    """The base case and the paths every option is scaled from."""

    def __init__(self):
        self.f, self.b, self.old, self.u = m.load()
        self.base = m.build_case('mixed', self.f, self.b, self.old, self.u)
        self.lines = {}
        for a in self.base['audit']:
            self.lines.setdefault(a['line'], {y: 0.0 for y in YEARS})[a['year']] += a['primary_deficit_change_bn']
        self.rows = {r['year']: r for r in self.base['rows']}
        self.gdp = {y: self.b[y]['gdp'] for y in YEARS}

    def line(self, name):
        return self.lines.get(name, {y: 0.0 for y in YEARS})

    def component(self, owner, name):
        for n, amt, p in self.f.PR.COMPONENTS[owner]:
            if n == name:
                return self.f.row_path(self.b, amt, p, p.get('years'))
        raise KeyError(owner + '/' + name)


def scaled(path, k):
    return {y: k * path.get(y, 0.0) for y in YEARS}


def gdp_from(ctx, level_2040, start, ramp=1):
    """A level in FY2040, grown with GDP, phased in from `start` over `ramp` years."""
    return {y: level_2040 * ctx.gdp[y] / ctx.gdp[2040] * m.phase(y, start, ramp) for y in YEARS}


def decade(path):
    return sum(path.get(y, 0.0) for y in m.W)


# ---------------------------------------------------------------- the option library
# Each option returns dict(label, adjust={label: path}, kw={build_case arguments}, d3=[edits], note).
# D3 edits: ('drop', id), ('scale', id, factor), ('add', id, side, amount_tn, key, label), ('absent', text).

def opt_gx_narrowed(ctx):
    """Part D item 3: GX's 15% haircut stops applying to H1b's wage half once HCH takes it back (from 2035)."""
    p = scaled(ctx.line('HCH'), -0.15)
    gx = decade(ctx.line('GX'))
    return dict(label="GX narrowed to H1b's remaining half", adjust={'GX narrowed': p},
                d3=[('scale', 'GX', 1 + decade(p) / gx)] if gx else [])


def opt_hca_rederived(ctx, level=HCA_REDERIVED_2040):
    """Part C item 15: the 0.9% Additional Medicare Tax folded in is worth about $70B, not $53.5B, in FY2040."""
    hca = ctx.line('HCA')
    p = scaled(hca, level / hca[2040] - 1)
    return dict(label='HCA re-derived at $%.0fB' % level, adjust={'HCA re-derived': p},
                d3=[('scale', 'HCA', level / hca[2040])])


def opt_avoidance_by_tier(ctx, base_allowance=0.10):
    """Part C item 9: the 20% avoidance allowance set by tier: `base_allowance` on the base rate's withheld, broad base,
    20% on the surcharge. HCU is booked net of 20%, so the base part's gross is its net / 0.8."""
    k = HCU_BASE_SHARE * (0.20 - base_allowance) / 0.80
    p = scaled(ctx.line('HCU'), k)       # HCU's line is negative (revenue), so this lowers the gap when k > 0
    return dict(label='Avoidance allowance %.0f%% on the base rate, 20%% on the surcharge' % (100 * base_allowance),
                adjust={'Avoidance allowance by tier': p},
                d3=[('scale', 'HCU', 1 + k), ('scale', 'HCUw', 1 + k)])


def opt_stack_cap(ctx, design='C1', end='central'):
    """Part C item 11 (DEC-2026-11-15-16: stage G caps the wealth and accrual taxes together): a design from the stack
    note's menu, its FY2040 cost scaled on HS2's path."""
    label, central, lo, hi = CAP_MENU[design]
    cost = dict(central=central, low=lo, high=hi)[end]
    hs2 = ctx.line('HS2')
    k = cost / -hs2[2040]
    return dict(label='Stack cap %s: %s ($%dB in FY2040)' % (design, label, cost),
                adjust={'Stack cap ' + design: scaled(hs2, -k)} if cost else {},
                d3=[('scale', 'HS2', 1 - k)] if cost else [])


def opt_drop_broad_points(ctx):
    """Part C item 7: the booked 2 points on AGI above $20K/$40K dropped."""
    return dict(label='The 2 points above $20K/$40K dropped', kw=dict(broad_rate=0), d3=[('drop', 'ICB')])


def opt_fold_broad_points(ctx, rate=3.25):
    """Part C item 7, folded: the 2 points dropped and the health contribution's base rate R raised from 2.25%, from
    the 2035 endpoint, at about $56B a quarter point in FY2040 grown on HCU's path. R = 3.25% raises about the 2
    points' FY2040 yield (health-household-contribution.md section 2: 75.6% of workers ahead)."""
    hcu = ctx.line('HCU')
    level = HCU_PER_QUARTER_POINT_2040 * (rate - 2.25) / 0.25
    p = {y: (-level * hcu[y] / hcu[2040] if y >= 2035 else 0.0) for y in YEARS}
    return dict(label='The 2 points folded into R = %.2f%%' % rate, kw=dict(broad_rate=0),
                adjust={'R raised to %.2f%%' % rate: p},
                # HCU's D3 row is its FY2035-39 amount (a cost to households); the raise adds to it in proportion
                d3=[('drop', 'ICB'), ('scale', 'HCU', 1 + decade(p) / decade({y: hcu[y] for y in range(2035, 2040)}))])


def opt_end_adult_credit(ctx):
    """The legacy recovery budget's $300 refundable credit per adult (assumptions.json recovery_credit; README: "neither
    is an adopted benefit"). No flagship designs it and D3 does not carry it."""
    return dict(label='The legacy $300 adult credit ended', kw=dict(credit_multiple=0),
                d3=[('absent', 'D3 has no row for the credit, so its quintiles do not move')])


def opt_ltc_state_share(ctx, share=1.0):
    """Care memo 17 option 7, extended: the states' long-term care payment (HLT-9.09, 50% of their current long-term
    care spending, indexed) raised to `share`, as health's states pay 100% (DEC-2026-11-15-25)."""
    sp = ctx.component('HLT-9', 'states-payment')     # negative: an offsetting receipt
    p = scaled(sp, share / 0.5 - 1)
    return dict(label="States' long-term care payment at %.0f%%" % (100 * share), adjust={'LTC states at %.0f%%' % (100 * share): p},
                d3=[('absent', "a state payment: D3 counts federal rows only, so households' benefits (H9) do not move")])


def opt_hi_grant_ended(ctx):
    """A proposed accounting correction (for G5 to check, G7 to book): the recovery budget's general-fund grant to
    Medicare's HI fund, 0.35 points of HI payroll phased in from 2035 (`recovery-budget/assumptions.json` `hi`, "not an
    actuarially verified adopted amount"), starts at the January 2035 endpoint, when HI folds into the plan's fund
    (HLT-7.22; `funds-model.py`: "the years after 2035 are shown for current-law comparison only"). The plan's fund is
    already booked on the general fund, so the grant pays the general fund's money to a fund the plan has folded in.
    It is intragovernmental: ending it moves the general-fund reading, not the unified budget."""
    return dict(label="The general fund's grant to HI ended from the 2035 endpoint (accounting correction)",
                kw=dict(hi_grant_points=0.0), d3=[])


def opt_vat(ctx, rate=3.0, start=2033, ramp=2, rebate_per_adult_2040=0.0, steps=None):
    """A broad value-added tax, net of the 25% offset, from `start`; optional later steps {year: rate} and an optional
    per-adult rebate (2040 dollars, CPI-indexed)."""
    adults = {y: m.credit(y) / m.A['recovery_credit']['annual_per_adult_2030_dollars']
              / (m.A['recovery_credit']['first_year_fraction'] if y == m.A['recovery_credit']['start'] else 1)
              / (1 + m.A['recovery_credit']['cpi']) ** (y - 2030) for y in YEARS}   # adults, millions / 1000 ($B per $)
    steps = {int(k): v for k, v in (steps or {}).items()}
    def r(y):
        return max([rate] + [v for k, v in steps.items() if y >= k])
    rev = {y: r(y) * VAT_POINT_2040 * ctx.gdp[y] / ctx.gdp[2040] * m.phase(y, start, ramp)
           for y in YEARS}
    reb = {y: rebate_per_adult_2040 * adults[y] * (1.023 ** (y - 2040)) * m.phase(y, start, ramp) for y in YEARS}
    adj = {'VAT %.1f%%' % rate: scaled(rev, -1)}
    d3 = [('add', 'VAT', 'cost', decade(rev) / 1000 / (1 - EXCISE_OFFSET), 'consumption', 'VAT %.1f%%' % rate)]
    if rebate_per_adult_2040:
        adj['VAT rebate'] = reb
        d3.append(('add', 'VATR', 'benefit', decade(reb) / 1000, 'adults', 'VAT rebate per adult'))
    later = ''.join(', %.2f%% from FY%d' % (v, k) for k, v in sorted(steps.items()))
    return dict(label='VAT %.2f%% from FY%d%s%s' % (rate, start, later, ', rebate $%.0f an adult' % rebate_per_adult_2040 if rebate_per_adult_2040 else ''),
                adjust=adj, d3=d3)


def opt_benefit_trims(ctx):
    """Memo G1 option B: the cheaper designs the flagships' own memos priced, in FY2040 terms ($B):
    the child benefit at the 2021 credit's amounts (secure floor memo 1 C: about 50 of FAM-1's 220); and in care, the
    $18 care wage floor (care memo 14 A, about 33), early educators on the floor without parity (memo 15 C, about 41)
    and pre-K for 4-year-olds only (memo 11 C, about 35), together about 109, scaled on FAM-2 and HLT-10's paths."""
    fam1 = ctx.line('FAM-1')
    care = {y: ctx.line('FAM-2')[y] + ctx.line('HLT-10')[y] for y in YEARS}
    k1, k2 = 50.0 / fam1[2040], 109.0 / care[2040]
    return dict(label='Benefit trims: child benefit at 2021 amounts; $18 care floor; no educator parity; pre-K at 4 only',
                adjust={'Child benefit at 2021 amounts': scaled(fam1, -k1), 'Care trims': scaled(care, -k2)},
                d3=[('scale', 'F1', 1 - k1), ('scale', 'F2', 1 - k2)])


def opt_education_rate(ctx, rate=1.7):
    """Part C item 28: the education fund's contribution rate (EDU-9B), 1.4 points as booked. The general fund keeps
    its 30% share of outlays; a higher rate costs the general fund only the 12.5% income-tax offset."""
    return dict(label='Education fund at %g points' % rate, kw=dict(education_rate=rate),
                d3=[('scale', 'EDUP', rate / 1.4)])


def opt_education_corridor(ctx):
    """Part C item 28, alternative: keep 1.4 points and add the reserve corridor's general-fund grants."""
    return dict(label='Education fund at 1.4 points with the reserve corridor', kw=dict(corridor=True), d3=[])


def opt_without_d2(ctx):
    """DEC-2026-11-15-08: the gap reported without D2, the national health budget (HLT-7/national-budget)."""
    return dict(label='Without D2', adjust={'Without D2': scaled(ctx.component('HLT-7', 'national-budget'), -1)}, d3=[])


def opt_without_hs2(ctx):
    """Part C item 13: the wealth tax (HS2) struck down, with no fallback counted."""
    return dict(label='Without HS2', adjust={'Without HS2': scaled(ctx.line('HS2'), -1)}, d3=[('drop', 'HS2')])


def opt_backstop(ctx, level_2040=250.0, start=2040):
    """Memo G4 option C: a contingent backstop enacted with the plan, drawn only if D2 or HS2 fails (priced as if drawn)."""
    return dict(label='Backstop drawn', adjust={'Backstop': scaled(gdp_from(ctx, level_2040, start), -1)}, d3=[])


OPTIONS = {k[4:]: v for k, v in globals().items() if k.startswith('opt_')}

# ---------------------------------------------------------------- the packages (2-settlement.md part 2)
FIXES = [('gx_narrowed', {}), ('hca_rederived', {}), ('avoidance_by_tier', {}), ('stack_cap', {'design': 'C1'})]
CORE = FIXES + [('hi_grant_ended', {}), ('end_adult_credit', {}), ('ltc_state_share', {'share': 1.0}),
               ('education_rate', {'rate': 1.7})]
# Memo G8: the VAT's rate steps keep every year to FY2056 closed as health's budget grows at GDP plus 1. The VAT starts
# with health's January 2035 endpoint (the review of #469: started in FY2033, it put the fourth fifth behind on D3 in
# FY2033-34, before health's savings arrive); FY2035 is booked at the full year, a small overstatement of its yield.
VAT_REC = {'rate': 4.75, 'start': 2035, 'ramp': 1, 'steps': {2041: 5.25, 2044: 5.6, 2051: 6.3}}
VAT_AT_ENDPOINT = {'start': 2035, 'ramp': 1}
PACKAGES = {
    'booked': [],
    'fixes': FIXES + [('hi_grant_ended', {})],
    # The recommended package (provisional): the fixes and cap, the HI correction, the legacy credit ended, the states'
    # long-term care payment at 100%, the education fund at 1.7 points, the 2 points dropped, and a VAT that steps.
    'recommended': CORE + [('drop_broad_points', {}), ('vat', VAT_REC)],
    # Memo G1 B: the recommended package with the flagships' own cheaper designs; the VAT that then closes it.
    'g1_with_benefit_trims': CORE + [('drop_broad_points', {}), ('benefit_trims', {}),
                                     ('vat', dict(VAT_AT_ENDPOINT, rate=3.3, steps={2041: 3.75, 2044: 4.1, 2051: 4.8}))],
    # Memo G2 C: the 2 points folded into the health contribution (R = 3.25%) instead of dropped.
    'g2_folded': CORE + [('fold_broad_points', {'rate': 3.25}),
                         ('vat', dict(VAT_AT_ENDPOINT, rate=2.75, steps={2041: 3.0, 2043: 3.3, 2051: 4.0}))],
    # G1 B and G2 C together: the smallest VAT among the screened packages (the revenue-mix test's best case).
    'g1b_g2c': CORE + [('fold_broad_points', {'rate': 3.25}), ('benefit_trims', {}),
                       ('vat', dict(VAT_AT_ENDPOINT, rate=1.25, steps={2041: 1.45, 2043: 1.6, 2044: 1.8, 2050: 2.0, 2052: 2.2, 2054: 2.5}))],
    # Memo G3 C: no VAT; the recommended package without it, to show what cuts would have to close.
    'g3_no_vat': CORE + [('drop_broad_points', {})],
}


def resolve(ctx, spec):
    return [OPTIONS[name](ctx, **params) for name, params in spec]


@contextlib.contextmanager
def hi_grant(points):
    """The HI grant's rate in payroll points (assumptions.json `hi`), set for one screen and restored."""
    if points is None:
        yield
        return
    orig = m.A['hi']['gf_support_payroll_points']
    m.A['hi']['gf_support_payroll_points'] = points
    try:
        yield
    finally:
        m.A['hi']['gf_support_payroll_points'] = orig


@contextlib.contextmanager
def education_rate(rate):
    """build_case fixes the education fund's rate at 1.4 points; a screen may set another without touching inputs."""
    if rate is None:
        yield
        return
    orig = m.edu_fund

    def patched(*a, **k):
        if k.get('rate') == 1.4:
            k['rate'] = rate
        return orig(*a, **k)
    m.edu_fund = patched
    try:
        yield
    finally:
        m.edu_fund = orig


def price(ctx, opts, name='screen'):
    """Run build_case with the options' adjustments and arguments; return the fiscal summary."""
    kw, adjust = {}, {}
    for o in opts:
        for k, v in o.get('kw', {}).items():
            if k in kw and kw[k] != v:
                raise ValueError('conflicting options on ' + k)
            kw[k] = v
        for label, path in o.get('adjust', {}).items():
            if label in adjust:
                raise ValueError('option counted twice: ' + label)
            adjust[label] = {'annual_bn': {str(y): v for y, v in path.items()}}
    rate = kw.pop('education_rate', None)
    points = kw.pop('hi_grant_points', None)
    with education_rate(rate), hi_grant(points):
        c = m.build_case(name, ctx.f, ctx.b, ctx.old, ctx.u, spending_adjustments=adjust, **kw)
    by = {r['year']: r for r in c['rows']}
    base = ctx.rows
    gap = {y: by[y]['agenda_gf_primary_bn'] for y in YEARS}
    s = c['summary']
    return dict(
        gap={y: round(gap[y], 1) for y in SHOW}, gap_2030_39=round(decade(gap), 1),
        gap_gdp={y: round(100 * gap[y] / ctx.gdp[y], 2) for y in SHOW},
        worst_2040_56_gdp=round(max(100 * gap[y] / ctx.gdp[y] for y in range(2040, 2057)), 2),
        worst_year=max(range(2040, 2057), key=lambda y: gap[y] / ctx.gdp[y]),
        closes_2040_on=all(gap[y] <= 0.05 for y in range(2040, 2057)),
        path_2030_39={y: round(gap[y], 1) for y in m.W},
        debt_gdp={y: round(by[y]['debt_gdp'], 1) for y in (2039, 2040, 2056)},
        baseline_debt_gdp={y: round(100 * base[y]['baseline_debt_bn'] / ctx.gdp[y], 1) for y in (2039, 2040, 2056)},
        unified_primary_2030_39=round(decade({y: by[y]['program_primary_bn'] for y in YEARS}), 1),
        ss_depletion=s['ss_depletion'], ss_balance=round(s['ss_actuarial_balance'], 2), hi_depletion=s['hi_depletion'],
        education_depletion=s['education_depletion'],
        education_reserve_2040=round(next(r['reserve'] for r in c['education']['rows'] if r['year'] == 2040), 1),
        _gap=gap)


# ---------------------------------------------------------------- D3
class Household:
    """D3 on Q-H7 (the package the gap books), edited per option. Measured keys, $ a household a year, FY2030-39."""

    def __init__(self, ledger=None):
        here = str(ROOT / 'models/tools/household')
        for p in (here, str(ROOT / 'models/tools')):
            if p not in sys.path:
                sys.path.insert(0, p)
        cwd = os.getcwd()
        os.chdir(here)
        try:
            from budget import baseline
            import d3
            self.B = baseline(2029)
            self.D = d3.D3.load(str(ledger or ROOT / 'build/ledger.json'), model=self.B)
        finally:
            os.chdir(cwd)
        name = next(n for n in self.D.SCEN if n.startswith('Q-H7'))
        self.opts = list(self.D.SCEN[name][0])
        self.drop = tuple(self.D.SCEN[name][1]) if len(self.D.SCEN[name]) > 1 else ()

    # The reviewer's note on #467: EDUP entered D3 net of its 12.5% income-tax offset while the other payroll rows
    # (P1, O1) are gross. The screens put every payroll row on one convention, gross (what households pay), by
    # scaling EDUP back to gross. `convention=False` gives Q-H7 exactly as the committed scenario reads it.
    EDUP_GROSS = 1 / (1 - 0.125)

    def run(self, edits=(), convention=True):
        edits = ([('scale', 'EDUP', self.EDUP_GROSS)] if convention else []) + list(edits)
        opts, drop = list(self.opts), set(self.drop)
        table = dict(self.D.OPTIONS)
        rows = list(self.D.ROWS)
        notes = []
        for e in edits:
            if e[0] == 'drop':
                if e[1] in table and e[1] in opts:
                    opts.remove(e[1])
                else:
                    drop.add(e[1])
            elif e[0] == 'scale':
                rid, k = e[1], e[2]
                if rid in table:
                    side, amt, ps, label = table[rid]
                    table[rid] = (side, amt * k, [(key, a * k) for key, a in ps], label)
                else:
                    rows = [(r[0], r[1], r[2], r[3] * k, [(key, a * k) for key, a in r[4]], r[5]) if r[0] == rid else r
                            for r in rows]
            elif e[0] == 'add':
                _, rid, side, amt, key, label = e
                table[rid] = (side, amt, [(key, amt)], label)
                opts.append(rid)
            elif e[0] == 'absent':
                notes.append(e[1])
        import provisions as P
        res = P.run(rows, table, opts, tuple(drop), self.D.K, self.D.HH, self.D.INC)[0]
        out = dict(net={g: res[g]['net'] for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'T1')}, notes=notes)
        out['_state'] = (rows, table, opts, drop)
        return out

    # ---- D3's revenue-mix test (d3.D3.gf_test), on the edited package ----
    def revenue_mix(self, state, levels=None):
        """The share of new general-fund revenue from the top 1% (by incidence) and corporations, health's contributions
        left out (DEC-2026-11-15-29), as d3.gf_test computes it. `levels` maps a row id to its weight in place of its
        FY2030-39 amount (for a single-year reading); the VAT counts at its general-fund (net) yield."""
        import d3
        rows, table, opts, drop = state
        items = [(r[0], r[3], r[4], r[0] in d3.CORPORATE) for r in rows if r[0] in d3.GF_IDS and r[0] not in drop]
        for o in opts:
            side, amt, ps, label = table[o]
            if side == 'cost' and o not in d3.NOT_GF + d3.HEALTH_CONTRIBUTIONS:
                items.append((o, amt * (1 - EXCISE_OFFSET) if o == 'VAT' else amt, ps, False))
        total = top = 0.0
        for rid, amt, ps, corp in items:
            if not amt:
                continue
            share = 1.0 if corp else self.D.dist(ps)['T1'] / amt
            w = levels.get(rid, amt) if levels else amt
            total += w
            top += w * share
        return round(100 * top / total, 1)

    def series(self, state, profiles=None, years=(2033, 2034, 2035, 2036, 2039)):
        """Net $ a household by quintile in single years, on D3's phase-in profiles (d3.D3.series), with the package's
        edits and dropped rows applied; `profiles` gives rows the screens add (the VAT) their own year shape."""
        rows, table, opts, drop = state
        rs = [r for r in rows if r[0] not in drop] + [(o, table[o][3], table[o][0], table[o][1], table[o][2], '') for o in opts]
        out = {y: {g: 0.0 for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')} for y in years}
        for rid, label, side, amt, parts, _ in rs:
            d = self.D.dist(parts)
            sign = 1 if side == 'benefit' else -1
            for y in years:
                if profiles and rid in profiles:
                    f = profiles[rid][y - 2030]
                else:
                    f = self.D.annual_fraction(rid, amt, y) / amt if amt else 0
                for g in out[y]:
                    out[y][g] += sign * d[g] * f
        return {y: {g: round(v * 1e12 / (self.D.HH * 0.2)) for g, v in out[y].items()} for y in years}


# ---------------------------------------------------------------- the take-home test (DEC-2026-11-15-02)
# Workers ahead on health's take-home test at the decided 2.25% (health-household-contribution.md sections 2 and 8;
# intervals in #467). The test counts visible health costs only; no other option here moves it.
TAKE_HOME = {'booked': (70.1, 'with the 2 points'), 'drop': (88.7, 'without them'),
             'fold_3.25': (75.6, 'R = 3.25%'), 'fold_2.5': (85.9, 'R = 2.5%')}


def single_year_levels(ctx, state, year, vat_path=None):
    """Each counted revenue row's weight in one year: its D3 amount scaled by its own path's year/decade ratio, from the
    budget model's audit lines (the indexed income contributions from `tax_yield`; the VAT from its own path)."""
    rows, table, opts, drop = state
    t = m.A['tax']
    paths = {'ICH': {y: m.tax_yield(ctx.b, y, t['high_rate_points'], 0, t['additional_yield_haircut']) for y in YEARS},
             'ICB': {y: m.tax_yield(ctx.b, y, 0, t['broad_rate_points'], t['additional_yield_haircut']) for y in YEARS},
             'H7x': ctx.line('HX')}
    if vat_path:
        paths['VAT'] = vat_path
    amounts = {r[0]: r[3] for r in rows}
    amounts.update({o: table[o][1] for o in opts})
    out = {}
    for rid, amt in amounts.items():
        path = paths.get(rid) or ctx.lines.get(rid)
        if path and decade(path):
            w = amt * 10 * path[year] / decade(path)
            out[rid] = w * (1 - EXCISE_OFFSET) if rid == 'VAT' else w
    return out


def take_home(spec):
    names = [n for n, _ in spec]
    if 'fold_broad_points' in names:
        r = dict(spec)['fold_broad_points'].get('rate', 3.25)
        return TAKE_HOME['fold_%g' % r] if 'fold_%g' % r in TAKE_HOME else (None, 'not priced')
    return TAKE_HOME['drop'] if 'drop_broad_points' in names else TAKE_HOME['booked']


def evaluate(ctx, hh, name, spec, variants=True):
    opts = resolve(ctx, spec)
    out = dict(name=name, options=[o['label'] for o in opts], fiscal=price(ctx, opts, name),
               take_home=take_home(spec))
    if hh is not None:
        d = hh.run([e for o in opts for e in o.get('d3', [])])
        state = d.pop('_state')
        out['d3'] = d
        vat = next((o for o in opts if o['label'].startswith('VAT')), None)
        vpath = next((v for k, v in vat['adjust'].items() if k.startswith('VAT')), None) if vat else None
        prof = {'VAT': [vpath[y] / decade(vpath) for y in m.W]} if vpath else None
        out['revenue_mix'] = {'FY2030-39': hh.revenue_mix(state)}
        for y in (2040, 2056):
            out['revenue_mix']['FY%d' % y] = hh.revenue_mix(state, single_year_levels(ctx, state, y, vpath))
        out['d3_by_year'] = hh.series(state, prof)
        if not spec:
            c = hh.run([], convention=False)
            c.pop('_state')
            out['d3_as_committed'] = c
    if variants:
        for vname, extra in (('without_d2', [OPTIONS['without_d2'](ctx)]), ('without_hs2', [OPTIONS['without_hs2'](ctx)]),
                             ('without_both', [OPTIONS['without_d2'](ctx), OPTIONS['without_hs2'](ctx)])):
            f = price(ctx, opts + extra, name + '_' + vname)
            out[vname] = dict(gap={y: f['gap'][y] for y in (2040, 2045, 2050, 2056)}, gap_2030_39=f['gap_2030_39'],
                              worst_2040_56_gdp=f['worst_2040_56_gdp'])
    return out


def vat_needed(ctx, spec):
    """The VAT rate each year FY2040-56 that would close the general-fund gap left by `spec` (no VAT in it)."""
    f = price(ctx, resolve(ctx, spec))
    gap = f['_gap']
    return {y: round(gap[y] / (VAT_POINT_2040 * ctx.gdp[y] / ctx.gdp[2040]), 2) for y in range(2040, 2057)}


def option_sizes(ctx, hh=None):
    """Each option alone against the booked package: its effect on the gap and, with `hh`, on D3's quintiles."""
    rows = []
    base = price(ctx, [])
    d3base = hh.run([])['net'] if hh else None
    for name, params in [('gx_narrowed', {}), ('hca_rederived', {}), ('avoidance_by_tier', {}),
                         ('avoidance_by_tier', {'base_allowance': 0.05}), ('avoidance_by_tier', {'base_allowance': 0.20}),
                         ] + [('stack_cap', {'design': d}) for d in CAP_MENU if d != 'A'] + [
                         ('drop_broad_points', {}), ('fold_broad_points', {'rate': 3.25}), ('fold_broad_points', {'rate': 2.5}),
                         ('end_adult_credit', {}), ('hi_grant_ended', {}), ('benefit_trims', {}), ('ltc_state_share', {'share': 0.65}), ('ltc_state_share', {'share': 0.8}),
                         ('ltc_state_share', {'share': 1.0}), ('education_rate', {'rate': 1.55}), ('education_rate', {'rate': 1.6}),
                         ('education_rate', {'rate': 1.7}), ('education_corridor', {}), ('vat', {'rate': 1.0}), ('vat', {'rate': 3.5}),
                         ('vat', {'rate': 5.0, 'rebate_per_adult_2040': 350}), ('without_d2', {}), ('without_hs2', {})]:
        o = OPTIONS[name](ctx, **params)
        p = price(ctx, [o])
        rows.append(dict(option=o['label'], d2040=round(p['gap'][2040] - base['gap'][2040], 1),
                         d2045=round(p['gap'][2045] - base['gap'][2045], 1), d2056=round(p['gap'][2056] - base['gap'][2056], 1),
                         d2030_39=round(p['gap_2030_39'] - base['gap_2030_39'], 1), education_depletion=p['education_depletion']))
        if hh:
            q = hh.run(o.get('d3', []))['net']
            rows[-1]['d3'] = {g: q[g] - d3base[g] for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'T1')}
    return rows


def build(with_d3=True):
    ctx = Context()
    hh = Household() if with_d3 else None
    return dict(status='exploratory screens for the provisional settlement draft (stage G step 4); nothing adopted or booked',
                options=option_sizes(ctx, hh),
                packages={n: evaluate(ctx, hh, n, s) for n, s in PACKAGES.items()})


def money(v):
    return '%+.1f' % v if isinstance(v, (int, float)) else str(v)


def markdown(d):
    L = ['# Settlement screens: results', '',
         'Generated by `models/tools/financing-protection/packages.py --markdown` after the common rebuild. Exploratory; '
         'nothing here is adopted or booked. Nominal $B, case `mixed`; a positive gap is a shortfall. Read with '
         '[`../2-settlement.md`](../2-settlement.md).', '', '## Each option alone, against the booked package', '',
         'Gap effects in $B (+ raises the gap). D3 effects in $ a household a year, FY2030-39 average, against the booked '
         'package on one payroll convention (+ leaves households better off).', '',
         '| Option | FY2040 | FY2045 | FY2056 | FY2030-39 | Education fund depletes | D3 Q1 | Q2 | Q3 | Q4 | Q5 |',
         '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for r in d['options']:
        q = r.get('d3', {})
        L.append('| %s | %s | %s | %s | %s | %s | %s |' % (r['option'], money(r['d2040']), money(r['d2045']), money(r['d2056']),
                                                    money(r['d2030_39']), r['education_depletion'] or 'never (to 2104)',
                                                    ' | '.join('%+d' % q[g] for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')) if q else '| | | |'))
    L += ['', '## The packages', '']
    for n, p in d['packages'].items():
        f = p['fiscal']
        L += ['### %s' % n, '', 'Options: ' + ('; '.join(p['options']) or 'none (as booked)') + '.', '',
              '| | ' + ' | '.join('FY%d' % y for y in SHOW) + ' | FY2030-39 |', '| --- |' + ' --- |' * (len(SHOW) + 1),
              '| General-fund gap ($B) | ' + ' | '.join('%.1f' % f['gap'][y] for y in SHOW) + ' | %.1f |' % f['gap_2030_39'],
              '| Share of GDP | ' + ' | '.join('%.2f%%' % f['gap_gdp'][y] for y in SHOW) + ' | |']
        for v in ('without_d2', 'without_hs2', 'without_both'):
            if v in p:
                L.append('| %s ($B) | | | ' % v.replace('_', ' ').capitalize() +
                         ' | '.join('%.1f' % p[v]['gap'][y] for y in (2040, 2045, 2050, 2056)) + ' | %.1f |' % p[v]['gap_2030_39'])
        L += ['', '- Closes FY2040 and every later year to FY2056: **%s** (worst year %d, %.2f%% of GDP).' %
              ('yes' if f['closes_2040_on'] else 'no', f['worst_year'], f['worst_2040_56_gdp']),
              '- Debt, %% of GDP: %.1f in FY2040 (baseline %.1f), %.1f in FY2056 (baseline %.1f).' %
              (f['debt_gdp'][2040], f['baseline_debt_gdp'][2040], f['debt_gdp'][2056], f['baseline_debt_gdp'][2056]),
              '- Decade path (FY2030-39): ' + ', '.join('%d %.0f' % (y, v) for y, v in f['path_2030_39'].items()) + '.',
              '- Social Security depletes %s (75-year balance %.2f%% of payroll); HI depletes %s; the education fund %s '
              '(reserve $%.0fB in FY2040).' % (f['ss_depletion'] or 'never', f['ss_balance'], f['hi_depletion'],
                                              'depletes in %d' % f['education_depletion'] if f['education_depletion'] else 'stays solvent',
                                              f['education_reserve_2040']),
              '- Take-home test: %s%% of workers ahead (%s).' % p['take_home']]
        if 'd3_as_committed' in p:
            q = p['d3_as_committed']['net']
            L.append('- D3 as the committed Q-H7 reads it (EDUP net of its offset): Q1 %+d, Q2 %+d, Q3 %+d, Q4 %+d, Q5 %+d, top 1%% %+d.' %
                     (q['Q1'], q['Q2'], q['Q3'], q['Q4'], q['Q5'], q['T1']))
        if 'd3' in p:
            q = p['d3']['net']
            L.append('- D3 (FY2030-39 average, $ a household a year): Q1 %+d, Q2 %+d, Q3 %+d, Q4 %+d, Q5 %+d, top 1%% %+d.' %
                     (q['Q1'], q['Q2'], q['Q3'], q['Q4'], q['Q5'], q['T1']) +
                     (' ' + '; '.join(p['d3']['notes']).capitalize() + '.' if p['d3']['notes'] else ''))
        if 'revenue_mix' in p:
            L.append('- Revenue-mix test (top 1%% and corporations, share of new general-fund revenue; health\'s contributions '
                     'out): %s.' % ', '.join('%s %.0f%%' % (k, v) for k, v in p['revenue_mix'].items()))
        if 'd3_by_year' in p:
            L.append('- D3 by year (Q1 / Q2 / Q3 / Q4 / Q5, $ a household, nominal): ' + '; '.join(
                'FY%d %s' % (y, ' / '.join('%+d' % v[g] for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')))
                for y, v in p['d3_by_year'].items()) + '.')
        L.append('')
    return '\n'.join(L)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--markdown', action='store_true')
    ap.add_argument('--no-d3', action='store_true')
    a = ap.parse_args()
    d = build(with_d3=not a.no_d3)
    print(markdown(d) if a.markdown else json.dumps(d, indent=1, default=str))
