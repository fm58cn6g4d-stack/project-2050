#!/usr/bin/env python3
"""The immigration model's labor-market module: what legal status does to earnings, work and the taxes paid on them.

Role: the labor-market effects `charter/PLAN.md` 3.4 names for `MOD-immigration` (stage H step H6; the design was
reviewed with a Fable consult, November 25, 2026). Status: working, **not booked**: its figures sit beside the
booked lines in `results.json` (`labor_market`) and are never added to them. It is a reading of the evidence, not a
dynamic score, and never a pay-for (`dossiers/immigration/7-validation.md`, section 2).

It runs on the model's own filings (`immigration_model.uscis()`), cohort by cohort, FY2030-40, nominal $ billion:

  (a) premium      filers' income rises by the wage gain of legal status (EV-IMM-232), building over a few years;
                   registered people (a work permit, no green card yet) and people already holding DACA or TPS get
                   part of it;
  (b) employment   a small share of filers move into work (DACA's effect, EV-IMM-235), earning less than average;
  (c) taxes        the federal tax on the income that newly comes on the books: before status a share of income
                   is taxed (ITEP's 60%, SRC-4185), after it a larger share (92%) of a larger income. Social
                   Security's payroll tax is off-budget; Medicare's HI tax and the income tax (CBO's 9.7% average,
                   SRC-4181) are on-budget, gross of refundable credits. Three layers are reported apart: the
                   premium alone, the employment gain, and formalization (the rest);
  (d) natives      the change in average wages from the larger labor force, as a range only (CBO's S. 744 short-
                   and long-run responses, EV-IMM-203, -204), with the groups most exposed named in words
                   (EV-IMM-223). It is not distinguishable from zero.

What overlaps the booked lines: the status line is CBO's H.R. 6 score scaled, and CBO's score already counts
revenue from people coming on the books (SRC-4178: +$8,950 million off-budget, -$5,945 million on-budget after
credits, over 2021-31). So (c)'s formalization layer is a cross-check of that line's revenue side, not an addition.
Memo 3's added workers' taxes are in its booked line (EV-IMM-219, -220); here they enter (d) only. E-Verify's
effects on people left without status are the booked E-Verify lines (EV-IMM-394, -395), not recomputed here.

Inputs: `labor.csv`, on the toolkit's parameter schema. The `low` and `high` scenarios run every input at its low
or high value together, except `lm_formal_before`, which runs the other way (more income already on the books means
less new tax). Run: python3 models/tools/immigration/immigration_labor.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import immigration_model as M  # noqa: E402

PARAMETERS = os.path.join(HERE, 'labor.csv')
INPUTS = M.load_parameters((PARAMETERS,))
REVERSED = {'lm_formal_before'}
BASE_YEAR = 2022            # the income figure's year (ITEP, 2022)
LAST_COHORT = 2039          # uscis() copies FY2039's filings into FY2040 for people reaching ten years; not a new cohort here
CASES = ('central', 'low', 'high')


def val(name, case='central'):
    c, lo, hi, _ = INPUTS[name]
    if case == 'central':
        return c
    if name in REVERSED:
        case = 'high' if case == 'low' else 'low'
    return lo if case == 'low' else hi


def phase(y, cohort, years):
    """Share of the wage gain a cohort that filed in `cohort` has in FY y: half a year in the filing year, then linear."""
    t = y - cohort + 0.5
    return 0.0 if y < cohort else min(1.0, t / years)


def paths(case='central'):
    """Every output by fiscal year: $ billion, people million, wage change in percent."""
    v = lambda n: val(n, case)  # noqa: E731
    u = M.uscis(case)
    filings = {c: u['filings_by_year'][c] for c in M.YEARS if c <= LAST_COHORT}
    eligible = M.val('tier_b_m', case) + M.val('tier_a_outside_b_m', case) + M.val('registered_m', case)
    reg_share = M.val('registered_m', case) / eligible
    auth_share = v('lm_authorized_already_m') / eligible
    green_share = 1 - reg_share - auth_share
    weight = green_share + reg_share * v('lm_registered_premium_share') + auth_share * v('lm_authorized_premium_share')
    f0, f1 = v('lm_formal_before'), v('lm_formal_after')
    out = {k: {} for k in ('income_base', 'premium_gain', 'entrant_earnings', 'people_into_work_m', 'newly_taxed',
                           'tax_premium', 'tax_employment', 'tax_formalization', 'oasdi_off_budget', 'hi_on_budget',
                           'income_tax_on_budget', 'federal_total', 'labor_force_added_m', 'native_wage_pct_low',
                           'native_wage_pct_high')}
    rate_all = v('lm_oasdi_rate') + v('lm_hi_rate') + v('lm_income_tax_rate')
    memo3 = M.lawful_added(case)
    for y in M.YEARS:
        e = v('lm_income_per_person') * (1 + v('lm_earnings_growth')) ** (y - BASE_YEAR) / 1000     # $ thousand
        base = prem = moved = 0.0
        for c, n in filings.items():
            if c > y:
                continue
            base += n * e                                                    # $ billion (million people x $ thousand)
            prem += n * e * v('lm_wage_premium') * phase(y, c, v('lm_premium_phase_years')) * weight
            moved += n * v('lm_emp_gain') * phase(y, c, v('lm_premium_phase_years'))
        entrants = moved * e / v('lm_employed_share') * v('lm_entrant_earnings_factor')
        newly = (base + prem) * f1 - base * f0 + entrants * f1
        out['income_base'][y] = base
        out['premium_gain'][y] = prem
        out['entrant_earnings'][y] = entrants
        out['people_into_work_m'][y] = moved
        out['newly_taxed'][y] = newly
        out['tax_premium'][y] = prem * f1 * rate_all
        out['tax_employment'][y] = entrants * f1 * rate_all
        out['tax_formalization'][y] = base * (f1 - f0) * rate_all
        out['oasdi_off_budget'][y] = newly * v('lm_oasdi_rate')
        out['hi_on_budget'][y] = newly * v('lm_hi_rate')
        out['income_tax_on_budget'][y] = newly * v('lm_income_tax_rate')
        out['federal_total'][y] = newly * rate_all
        added = memo3[y] * v('lm_employed_share') + moved                    # million workers
        share = added / v('lm_labor_force_m') * 100                          # % of the labor force
        out['labor_force_added_m'][y] = added
        out['native_wage_pct_low'][y] = v('lm_wage_beta_low') * share
        out['native_wage_pct_high'][y] = v('lm_wage_beta_high') * share
    return out


def itep_check():
    """Federal tax gain per person a year at ITEP's own settings (10% wage gain, 60% to 92% on the books, 2022 income,
    fully phased in), on this module's rates: the benchmark against ITEP's $33.1 billion for 10.9 million people."""
    e = val('lm_income_per_person')
    rates = val('lm_oasdi_rate') + val('lm_hi_rate') + val('lm_income_tax_rate')
    return e * ((1 + 0.10) * val('lm_formal_after') - val('lm_formal_before')) * rates


def pope_check():
    """People moved into work by DACA's 1.7 million on this module's employment gain, thousand (EV-IMM-235)."""
    return 1.7e3 * val('lm_emp_gain')


def hr6_off_budget_check():
    """The module's off-budget payroll tax over FY2030-39 against CBO's H.R. 6 off-budget revenue scaled as the
    status line scales its deficit (reach and window growth): the ratio module / CBO."""
    mod = sum(paths()['oasdi_off_budget'][y] for y in M.WINDOW)
    cbo = 8.950 * M.val('reach_scale') * M.val('window_growth')
    return mod, cbo


def r(x, n=4):
    return round(x + 0.0, n)


def results():
    keys_money = ('premium_gain', 'entrant_earnings', 'newly_taxed', 'tax_premium', 'tax_employment', 'tax_formalization',
                  'oasdi_off_budget', 'hi_on_budget', 'income_tax_on_budget', 'federal_total')
    out = {'booked': False,
           'note': ("Not booked and never added to a booked line: a reading of the evidence beside them. The formalization layer "
                    "and the payroll and income taxes overlap the status line's revenue side (CBO's H.R. 6 score counts people "
                    "coming on the books), so they are a cross-check of it; the premium and employment layers are the "
                    "dynamic increment no booked line counts. Income tax is gross of refundable credits."),
           'scenarios': {}}
    for c in CASES:
        P = paths(c)
        out['scenarios'][c] = {
            'fy': {k: {str(y): r(P[k][y]) for y in M.YEARS} for k in P},
            'fy2030_39': {k: r(sum(P[k][y] for y in M.WINDOW)) for k in keys_money},
            'fy2040': {k: r(P[k][2040]) for k in keys_money + ('people_into_work_m', 'labor_force_added_m',
                                                                  'native_wage_pct_low', 'native_wage_pct_high')}}
    mod, cbo = hr6_off_budget_check()
    out['checks'] = {'itep_federal_gain_per_person_usd': r(itep_check(), 1), 'pope_people_into_work_k': r(pope_check(), 1),
                     'hr6_off_budget_scaled_bn': r(cbo), 'module_off_budget_fy2030_39_bn': r(mod), 'ratio': r(mod / cbo, 2)}
    return out


def validation_rows(B, ev):
    """The module's benchmarks, in the model's validation table (test_immigration.py builds them with its helpers)."""
    mod, cbo = hr6_off_budget_check()
    return [
        ev(B('BM-LAB-ITEP', "Federal tax gain per undocumented resident from work authorization, at ITEP's settings (10% wage gain, 60% to 92% of income on the books, 2022)",
             33.1e9 / 10.9e6, 'EV-IMM-229; SRC-4185', 'ITEP, July 2024: $33.1 billion more federal tax a year, 10.9 million people (Appendix Table 5)', '$ per person a year',
             0.25, 'relative', "a quarter: ITEP's income-tax detail by income source is not reproduced",
             "In-sample by construction for the income base and the two shares on the books, which come from ITEP; the check covers the tax rates. It passes high because CBO's 9.7% income tax rate (SRC-4181) is applied to all newly taxed income, before refundable credits.",
             in_sample=True), itep_check()),
        ev(B('BM-LAB-POPE', "People DACA moved into work, on the module's employment gain (1.7 million eligible)",
             (50, 75), 'EV-IMM-235', 'Pope, Journal of Public Economics, 2016', 'thousand people', 0.0, 'range',
             "Pope's published range",
             'In-sample by construction: `lm_emp_gain` is set from it.', in_sample=True), pope_check()),
        ev(B('BM-CBO-4', "Off-budget payroll tax from people coming on the books, FY2030-39: the module against CBO's H.R. 6 off-budget revenue, scaled as the status line scales the score",
             cbo, 'SRC-4178; EV-IMM-600', "CBO, H.R. 6, 2021: off-budget revenues +$8,950 million over 2021-31 (verified against the PDF, November 25, 2026)", '$ billion',
             0.5, 'relative', 'a half: a different population and method; set before running',
             ("A miss, kept: the module's figure is about {:.0f} times CBO's scaled one. CBO's population was largely DACA and TPS holders already on payrolls, so "
              "CBO's share of income on the books before status is far higher than ITEP's 60%; and the module's income base is ITEP's whole undocumented "
              "population. The formalization layer is therefore an upper reading, and the reason the module is not booked.").format(mod / cbo)), mod),
    ]


def report():
    for c in CASES:
        P = paths(c)
        w = lambda k: sum(P[k][y] for y in M.WINDOW)  # noqa: E731
        print(f"Labor market [{c}] (not booked), FY2030-39: earnings gain ${w('premium_gain'):.0f}B; federal tax on newly taxed income "
              f"${w('federal_total'):.0f}B (premium ${w('tax_premium'):.0f}B, employment ${w('tax_employment'):.0f}B, formalization "
              f"${w('tax_formalization'):.0f}B; off-budget ${w('oasdi_off_budget'):.0f}B); {P['people_into_work_m'][2039]:.2f} million more at work "
              f"by FY2039; average wages {P['native_wage_pct_low'][2039]:+.3f}% to {P['native_wage_pct_high'][2039]:+.3f}% in FY2039")


if __name__ == '__main__':
    report()
