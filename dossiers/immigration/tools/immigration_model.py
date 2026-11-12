#!/usr/bin/env python3
"""A first, scoped immigration model: system capacity, adjudication and fiscal effects.

Role: the immigration model `charter/PLAN.md` 3.4 says is built during this dossier, in a first
version for section 6 (`dossiers/immigration/6-cost.md`). Status: draft (board row I4). A full
model with a model card and benchmarks goes to `models/` at stage H (`7-validation.md`, part 2).
Run from the repository root: python3 dossiers/immigration/tools/immigration_model.py
Test: python3 dossiers/immigration/tools/test_immigration_model.py

Four modules, each on federal fiscal years FY2030-40, nominal $ billion, a cost positive:
  1. uscis()      USCIS throughput and backlog under the registry's volume (memo 2 C), and the
                  split between fees and the appropriation (memo 7 B);
  2. eoir()       immigration-court capacity: judges and years to clear the backlog with the
                  800-judge cap repealed (memo 4), and appointed counsel's cost (counsel B);
  3. detention()  the 30,000 cap against case management (memo 5, A's rules);
  4. status_fiscal()  the general-fund effect of status (memo 1) from CBO's published 2021
                  score, as `3-design.md`, "IMM-1's score, re-derived", sets it out.
Labor-market effects are not modeled: they stay as cited evidence (EV-IMM-223, EV-IMM-232).

Every input is in INPUTS with (central, low, high, basis). The basis is an evidence ID in
`dossiers/immigration/evidence.json`, or "assumption: ..." with its reasoning, or a legacy figure
with its file. Ranges run each module at its low and high inputs together (a bound, not a
probability interval). The test checks that every cited ID exists.
"""

YEARS = list(range(2030, 2041))
WINDOW = range(2030, 2040)
FILING_OPENS = 2031      # FY in which filing opens (about October 1, 2030; 4-specification.md)

INPUTS = {
    # ---- population and take-up (memo 1) ----
    'tier_b_m': (8.0, 7.0, 9.0, "assumption: MPI's 60% with ten years in 2021 (EV-IMM-617) moved to 2029, on 12-14.5 million"),
    'tier_a_outside_b_m': (2.25, 1.5, 3.0, 'assumption: memo 1; DACA 436,350 (EV-IMM-016), TPS about 274,000 (EV-IMM-022), farm, care and construction workers'),
    'registered_m': (3.0, 2.0, 4.0, 'assumption: memo 1, everyone else present on the cutoff'),
    'take_up': (0.70, 0.60, 0.85, 'EV-IMM-609'),
    'filing_shape': ((0.35, 0.30, 0.15, 0.06, 0.04, 0.03, 0.03, 0.02, 0.02), None, None,
                     'assumption: IRCA-like front loading (EV-IMM-635); known people on notice first'),
    # ---- USCIS unit costs and fees (memos 2 and 7) ----
    'cost_per_case_usd': (900, 600, 1200, 'assumption: between DACA fees $495 (EV-IMM-638) and an adjustment fee $1,440 (EV-IMM-627); records-first is nearer the low end'),
    'waived_share': (0.50, 0.40, 0.60, 'assumption: memo 2, share of filers below 200% of poverty'),
    'match_build_bn': (0.5, 0.3, 1.0, 'assumption: IRS-SSA-USCIS matching build and the test match, FY2030-31'),
    'uscis_pending_m': (12.8, 12.0, 13.5, 'EV-IMM-140'),
    'uscis_net_backlog_m': (7.7, 7.0, 8.5, 'EV-IMM-140'),
    'backlog_bn_per_year': (0.7, 0.5, 1.0, 'EV-IMM-575'),
    'backlog_years': (4.5, 4.0, 5.0, 'EV-IMM-575'),
    'backlog_cost_per_case_usd': (500, 350, 800, 'assumption: backlog cases are mostly renewals and petitions, below a registry case'),
    'online_ona_bn': (0.7, 0.4, 1.2, 'legacy estimate: online filing $0.5B and the Office of New Americans $0.02B a year (legacy-research.md, section 2)'),
    'fee_lag_bridge_bn': (1.0, 0.5, 2.0, "assumption: hiring ahead of fee receipts for the non-waived filings (memo 7's 'ahead of fees')"),
    'n400_apps_m': (1.0, 0.85, 1.3, 'assumption: 823,702 applied in FY2023 (EV-IMM-428), rising with the discount (EV-IMM-425)'),
    'n400_fee_usd': (760, 760, 760, 'EV-IMM-422'),
    'n400_free_share': (0.30, 0.20, 0.40, 'assumption: applicants below 200% of poverty'),
    'n400_half_share': (0.30, 0.20, 0.40, 'assumption: applicants from 200% to 400% (the 2024 rule gave half price from 150% to 400%, EV-IMM-424)'),
    # ---- asylum and refugees (memo 4) ----
    'asylum_cost_per_case_usd': (2400, 2000, 3000, 'EV-IMM-302: $180 million for 75,000 cases a year'),
    'asylum_decisions_k': (300, 250, 350, 'assumption: memo 4, while the affirmative backlog of 1.5 million (EV-IMM-146) clears'),
    'asylum_decisions_after_k': (150, 100, 200, 'assumption: after the backlog clears, from FY2036'),
    'refugees_added_k': (37.5, 30, 45, 'assumption: the 50,000 floor against a baseline of 5,000-20,000 admissions (EV-IMM-052)'),
    'cost_per_refugee_usd': (15000, 10000, 20000, 'assumption: memo 4, first-year reception and placement'),
    'regional_bn': (0.4, 0.3, 0.5, 'assumption: memo 4, regional access a year'),
    # ---- the courts (memo 4 part 2) ----
    'court_pending_m': (3.30, 3.0, 3.5, 'EV-IMM-100'),
    'judges_now': (753, 753, 753, 'EV-IMM-103'),
    'court_receipts_k': (529, 450, 700, 'EV-IMM-102'),
    'court_completions_now_k': (974, 974, 974, 'EV-IMM-102'),
    'completions_per_judge': (900, 700, 1100, 'assumption: below FY2026\'s 1,293 a judge (EV-IMM-102, EV-IMM-103), which in absentia orders inflate (EV-IMM-106); fuller hearings with counsel take longer'),
    'closed_on_filing_share': (0.35, 0.20, 0.50, 'assumption: pending cases of people who file for status and are closed (IMM-1.10); 29% of the unauthorized held TPS, DACA, a pending asylum claim or parole (EV-IMM-006)'),
    'officer_first_receipt_cut': (0.30, 0.15, 0.45, 'assumption: receipts avoided when officers grant first (EV-IMM-640, EV-IMM-322)'),
    'clear_years': (6, 6, 6, 'commitment: memo 4, clear the backlog in about six years'),
    'detained_avg_days': (60, 40, 90, 'assumption: average stay under the 90-day detained timeline (IMM-3.09)'),
    'detained_court_share': (0.60, 0.45, 0.75, 'assumption: share of detained people in court proceedings rather than expedited removal'),
    'counsel_cost_detained_usd': (4000, 2500, 6000, 'assumption: no national cost study is in the register (section 3, Evidence still needed); New York\'s program shows the effect, not the unit cost (EV-IMM-327)'),
    'children_cases_k': (40, 20, 60, 'assumption: children in removal proceedings a year'),
    'counsel_cost_child_usd': (5000, 3000, 7000, 'assumption, as above'),
    'smi_cases_k': (5, 3, 10, 'assumption: people found to have a serious mental illness'),
    'counsel_cost_smi_usd': (8000, 5000, 12000, 'assumption, as above'),
    # ---- detention (memo 5) ----
    'base_beds': (41500, 41500, 41500, 'EV-IMM-362'),
    'cap': (30000, 30000, 30000, 'commitment: memo 5 (EV-IMM-571)'),
    'bed_day_usd_2023': (187.48, 152.0, 237.60, 'EV-IMM-628 (central), EV-IMM-359 (low), EV-IMM-355 (high, family detention)'),
    'cm_people_k': (100, 70, 140, 'assumption: memo 5, people in case management at a time'),
    'cm_day_usd': (30, 20, 40, 'assumption: between ISAP and family case management (EV-IMM-355)'),
    'atd_day_usd_2023': (4.11, 4.11, 4.41, 'EV-IMM-629 (central), EV-IMM-355 (ISAP III, high)'),
    # ---- status's fiscal effect (memo 1) ----
    'hr6_deficit_bn': (35.33, 35.33, 35.33, 'EV-IMM-600: CBO, H.R. 6, $35,330 million over 2021-2031'),
    'reach_scale': (2.5, 2.0, 3.0, 'assumption: memo 1 reaches two to three times H.R. 6\'s population in its first decade (3-design.md)'),
    'window_growth': (1.25, 1.20, 1.30, 'assumption: 2.5-3% a year nominal from 2021-31 to 2030-39 (3-design.md)'),
    'health_share': (0.60, 0.40, 0.70, 'assumption: marketplace credits and Medicaid are the largest on-budget sources (EV-IMM-602); share of the cost'),
    'covered_anyway_share': (0.90, 0.85, 0.95, 'assumption: share of the window after the single plan covers every resident (January 2031, HLT-7.01)'),
    'price_growth': (0.025, 0.02, 0.03, 'assumption: nominal growth of unit costs'),
}

# Memo 1's yearly profile: a cost rising through the decade, as in CBO's 2021 tables (EV-IMM-600).
STATUS_SHAPE = {2030: 0.0, 2031: 1.0, 2032: 2.0, 2033: 3.5, 2034: 5.0, 2035: 5.5, 2036: 6.5,
                2037: 8.0, 2038: 9.0, 2039: 9.5, 2040: 10.0}


def val(name, case='central'):
    c, lo, hi, _ = INPUTS[name]
    return {'central': c, 'low': lo, 'high': hi}[case] if lo is not None else c


def prices(y, case='central', base=2026):
    return (1 + val('price_growth', case)) ** (y - base)


def uscis(case='central'):
    """Filings, the appropriated waiver cost (memo 2), USCIS's other public work (memo 7) and the backlog."""
    v = lambda n: val(n, case)
    eligible = v('tier_b_m') + v('tier_a_outside_b_m') + v('registered_m')
    filings = eligible * v('take_up')                                  # million, over the decade
    shape = INPUTS['filing_shape'][0]
    per_year = {y: 0.0 for y in YEARS}
    for i, share in enumerate(shape):
        if FILING_OPENS + i in per_year:
            per_year[FILING_OPENS + i] = filings * share
    per_year[2040] = per_year[2039]                                    # people reaching ten years
    waivers = {y: per_year[y] * v('waived_share') * v('cost_per_case_usd') * prices(y, case) / 1000 for y in YEARS}
    build = {y: (v('match_build_bn') * (0.6 if y == 2030 else 0.4 if y == 2031 else 0)) for y in YEARS}
    memo2 = {y: waivers[y] + build[y] for y in YEARS}
    # Backlog clearance (EV-IMM-575): money a year for 4-5 years, from FY2030.
    yrs = v('backlog_years')
    backlog_money = {y: v('backlog_bn_per_year') * max(0.0, min(1.0, yrs - (y - 2030))) for y in YEARS}
    cleared = sum(backlog_money[y] for y in YEARS) * 1000 / v('backlog_cost_per_case_usd')   # million cases
    years_to_clear = v('uscis_net_backlog_m') / (v('backlog_bn_per_year') * 1000 / v('backlog_cost_per_case_usd'))
    n400 = {y: v('n400_apps_m') * v('n400_fee_usd') * (v('n400_free_share') + 0.5 * v('n400_half_share')) * prices(y, case) / 1000 for y in YEARS}
    online = {y: v('online_ona_bn') / 10 for y in YEARS}
    bridge = {y: (v('fee_lag_bridge_bn') / 3 if y in (2030, 2031, 2032) else 0.0) for y in YEARS}
    memo7 = {y: backlog_money[y] + n400[y] + online[y] + bridge[y] for y in YEARS}
    return dict(filings_m=filings, filings_by_year=per_year, memo2=memo2, memo7=memo7,
                backlog_cleared_m=cleared, backlog_years_to_clear=years_to_clear,
                backlog_left_m=max(0.0, v('uscis_net_backlog_m') - cleared))


def eoir(case='central'):
    """Judges needed to clear the court backlog in about six years, and appointed counsel's cost."""
    v = lambda n: val(n, case)
    pending_after = v('court_pending_m') * (1 - v('closed_on_filing_share'))
    receipts = v('court_receipts_k') / 1000 * (1 - v('officer_first_receipt_cut'))
    yrs = v('clear_years')
    judges = (pending_after + receipts * yrs) * 1e6 / (yrs * v('completions_per_judge'))
    # Years to clear with the cap kept at 800 judges, for comparison.
    net = 800 * v('completions_per_judge') / 1e6 - receipts
    years_at_cap = pending_after / net if net > 0 else float('inf')
    detained_cases = val('cap') * 365 / v('detained_avg_days') * v('detained_court_share')
    counsel_2026 = (detained_cases * v('counsel_cost_detained_usd') + v('children_cases_k') * 1000 * v('counsel_cost_child_usd')
                    + v('smi_cases_k') * 1000 * v('counsel_cost_smi_usd')) / 1e9
    # Counsel from the act (about FY2030, phased in over its first year).
    counsel = {y: counsel_2026 * prices(y, case) * (0.5 if y == 2030 else 1.0) for y in YEARS}
    return dict(judges_needed=judges, years_at_800=years_at_cap, pending_after_m=pending_after,
                receipts_m=receipts, detained_cases_k=detained_cases / 1000, counsel=counsel)


def asylum_refugees(case='central'):
    """The rest of memo 4: the officer corps, the refugee floor and regional access."""
    v = lambda n: val(n, case)
    corps = {}
    for y in YEARS:
        k = v('asylum_decisions_k') if y <= 2035 else v('asylum_decisions_after_k')
        ramp = 0.5 if y == 2030 else 1.0
        corps[y] = k * 1000 * v('asylum_cost_per_case_usd') * prices(y, case) * ramp / 1e9
    refugees = {y: v('refugees_added_k') * 1000 * v('cost_per_refugee_usd') * prices(y, case) / 1e9 for y in YEARS}
    regional = {y: v('regional_bn') * prices(y, case) / prices(2030, case) for y in YEARS}
    return dict(corps=corps, refugees=refugees, regional=regional)


def detention(case='central'):
    """The cap's saving against the base account, against case management's added cost."""
    v = lambda n: val(n, case)
    out = {}
    for y in YEARS:
        p = prices(y, case, base=2023)
        saving = (v('base_beds') - v('cap')) * 365 * v('bed_day_usd_2023') * p / 1e9
        added = v('cm_people_k') * 1000 * 365 * (v('cm_day_usd') * prices(y, case) - v('atd_day_usd_2023') * p) / 1e9
        out[y] = added - saving
    return out


def status_fiscal(case='central'):
    """Memo 1 on CBO's 2021 score of H.R. 6, scaled, grown and netted for the single plan."""
    v = lambda n: val(n, case)
    gross = v('hr6_deficit_bn') * v('reach_scale') * v('window_growth')
    net = gross * (1 - v('health_share') * v('covered_anyway_share'))
    w = sum(STATUS_SHAPE[y] for y in WINDOW)
    return {y: net * STATUS_SHAPE[y] / w for y in YEARS}


def window(path):
    return sum(path[y] for y in WINDOW)


def lines(case='central'):
    """The model's general-fund lines for section 6 (immigration_path.py adds the rest)."""
    u, e, a = uscis(case), eoir(case), asylum_refugees(case)
    memo4 = {y: a['corps'][y] + a['refugees'][y] + a['regional'][y] + e['counsel'][y] for y in YEARS}
    return {'memo1': status_fiscal(case), 'memo2': u['memo2'], 'memo4': memo4,
            'detention': detention(case), 'memo7': u['memo7']}


def report():
    for case in ('central', 'low', 'high'):
        L = lines(case)
        print(f'[{case}] ' + '; '.join(f'{k} {window(p):.1f} / {p[2040]:.1f}' for k, p in L.items()))
    u, e = uscis(), eoir()
    print(f"USCIS: about {u['filings_m']:.1f} million filings; the net backlog of {val('uscis_net_backlog_m')} million "
          f"clears in about {u['backlog_years_to_clear']:.1f} years at the backlog money's pace ({u['backlog_left_m']:.1f} million left when it ends)")
    for case in ('central', 'low', 'high'):
        ec = eoir(case)
        print(f"Courts [{case}]: about {ec['judges_needed']:.0f} judges clear the backlog in six years "
              f"({ec['pending_after_m']:.2f} million after closures, {ec['receipts_m']*1000:.0f}k receipts a year); "
              f"at 800 judges about {ec['years_at_800']:.1f} years; counsel ${window(ec['counsel']):.1f}B over FY2030-39")
    a = asylum_refugees()
    print('Memo 4 parts (FY2030-39): corps {:.1f}, refugees {:.1f}, regional {:.1f}, counsel {:.1f}'.format(
        window(a['corps']), window(a['refugees']), window(a['regional']), window(e['counsel'])))


if __name__ == '__main__':
    report()
