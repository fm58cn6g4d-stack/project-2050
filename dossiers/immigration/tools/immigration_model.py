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

import os
import sys

INPUTS = {
    # ---- population and take-up (memo 1) ----
    'tier_b_m': (8.0, 7.0, 9.0, "assumption: MPI's 60% with ten years in 2021 (EV-IMM-617) moved to 2029, on 12-14.5 million"),
    'tier_a_outside_b_m': (2.25, 1.5, 3.0, 'assumption: memo 1; DACA 436,350 (EV-IMM-016), TPS about 274,000 (EV-IMM-022), farm, care and construction workers'),
    'registered_m': (3.0, 2.0, 4.0, 'assumption: memo 1, everyone else present on the cutoff'),
    'tier_a_late_arrivals_m': (0.05, 0.02, 0.10, 'assumption: people who would be in tier A but arrive between January 1 of the year of enactment and signature, so register instead (IMM-1.04, DEC-2026-11-12-12)'),
    # ---- the E-Verify start (memo 5 part 2; IMM-4.13) ----
    'everify_first_tranche_fy': (2031.75, 2031.25, 2032.75, 'commitment: no earlier than October 1 of the year after enactment, on a passing 90-day check (DEC-2026-11-12-12); assumption: the check first passes about July 2031 (FY2031 Q4)'),
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
    'completions_per_judge': (510, 450, 750, "EV-IMM-641: CRS's FY2017-22 average, excluding FY2021, about 510 a judge; assumption range: fuller hearings with counsel are slower (450), while FY2026's 1,293 (EV-IMM-102, EV-IMM-103) and the Manhattan Institute's 957 (EV-IMM-646) are inflated by in absentia orders (EV-IMM-106)"),
    'judge_team_cost_m': (1.5, 1.31, 2.45, "EV-IMM-644: the recurring 61% of EOIR's $367 million for 150 teams, about $1.49 million a team (central); EV-IMM-645: DOJ's FY2025 request, $1.31 million a judge (low); EV-IMM-644 with the space buildout, $2.45 million (high)"),
    'judge_attrition': (0.056, 0.035, 0.07, 'EV-IMM-646: about 5.6% a year (central); EV-IMM-643: 26 a year, about 3.5% of 753 (low); assumption: 7% (high)'),
    'hiring_ramp': (250, 150, 312, "EV-IMM-646: 250 added a year (central); assumption: 150 a year, EOIR's FY2024 request (EV-IMM-644), as the slow ramp; EV-IMM-103: 312 hired in FY2026 (fast)"),
    'cleared_receipts_years': (1.0, 0.75, 1.5, 'assumption: the backlog counts as cleared when pending cases fall to one year of receipts, so non-detained cases can be decided within two years (IMM-3.09)'),
    'new_judge_productivity': (0.5, 0.3, 0.7, 'assumption: judges hired during a year decide half a year of cases; CRS notes new judges need time to learn on the job (SRC-4089, R47637)'),
    'closed_on_filing_share': (0.35, 0.20, 0.50, 'assumption: pending cases of people who file for status and are closed (IMM-1.10); 29% of the unauthorized held TPS, DACA, a pending asylum claim or parole (EV-IMM-006)'),
    'officer_first_receipt_cut': (0.30, 0.15, 0.45, 'assumption: receipts avoided when officers grant first (EV-IMM-640, EV-IMM-322)'),
    'clear_years': (6, 6, 6, 'commitment: memo 4, clear the backlog in about six years (FY2030-35)'),
    'detained_avg_days': (60, 40, 90, 'assumption: average stay under the 90-day detained timeline (IMM-3.09)'),
    'detained_court_share': (0.60, 0.45, 0.75, 'assumption: share of detained people in court proceedings rather than expedited removal'),
    'counsel_cost_detained_usd': (4000, 2500, 6000, 'assumption: no national cost study is in the register (section 3, Evidence still needed); New York\'s program shows the effect, not the unit cost (EV-IMM-327)'),
    'children_cases_k': (40, 20, 60, 'assumption: children in removal proceedings a year'),
    'counsel_cost_child_usd': (5000, 3000, 7000, 'assumption, as above'),
    'children_backlog_k': (200, 100, 400, "assumption: children's cases in the 3.3 million court backlog (EV-IMM-100) that the corps decides by FY2035 and counsel B covers; no count in the register, decided evenly over FY2031-35"),
    'smi_cases_k': (5, 3, 10, 'assumption: people found to have a serious mental illness'),
    'counsel_cost_smi_usd': (8000, 5000, 12000, 'assumption, as above'),
    # ---- detention (memo 5) ----
    'base_beds': (41500, 41500, 41500, 'EV-IMM-362'),
    'cap': (30000, 30000, 30000, 'commitment: memo 5 (EV-IMM-571)'),
    'bed_day_usd_2023': (187.48, 152.0, 237.60, 'EV-IMM-628 (central), EV-IMM-359 (low), EV-IMM-355 (high, family detention)'),
    'cm_people_k': (150, 100, 250, 'assumption: memo 5, people in case management at a time: today\'s 183,181 on alternatives (EV-IMM-171) and about 35,000 released to reach the cap, less the 35-50% who file for status and leave proceedings (IMM-1.10), plus releases under the surge rule (IMM-3.02), which have no count'),
    'cm_day_usd': (30, 20, 40, 'assumption: between ISAP and family case management (EV-IMM-355)'),
    'atd_day_usd_2023': (4.11, 4.11, 4.41, 'EV-IMM-629 (central), EV-IMM-355 (ISAP III, high)'),
    # ---- the single plan under memo 6 as amended (Espen, November 12, lead session: lawful or registered status) ----
    'without_status_m': (2.25, 1.5, 3.0, "assumption: memo 6, the part of care's 1% residual (models/tools/health-coverage/inputs.csv, sp_residual_unins, about 3.55 million) that is people without any status; the rest is people not enrolled for other reasons"),
    'added_lawful_m_2039': (0.45, 0.3, 0.6, "assumption: memo 3's added immigrants above the baseline population by FY2039 (0.3-0.6 million, 3-design.md), rising evenly from FY2031; not in care's population base"),
    'lawful_added_cost_factor': (1.0, 0.5, 1.0, "assumption: care's path prices an added person at its average newly covered person, about $13,500 in 2032 (EV-CAR-120 for the plan's base); 0.5 is a lower bound for a working-age group, with no register source yet"),
    'returnees_m': (0.05, 0.02, 0.15, "assumption: people who return under IMM-1.15, from about 1.8 million removals in FY2025-28 (ICE: 442,640 in FY2025 and 483,200 in FY2026, EV-IMM-659, carried at that pace), of whom about 3% (1-8%) had three years here and a citizen, permanent-resident or newly legalized spouse, parent or child and come back; arriving over FY2031-33"),
    'return_case_usd': (1500, 1000, 2500, 'assumption: a USCIS and consular case from abroad (IMM-1.15), between an adjustment fee (EV-IMM-627) and a consular visa case with an interview'),
    'five_year_wait_bn': (3.0, 2.0, 4.0, "assumption: memo 6, no five-year wait for memo 1's new permanent residents in SNAP, SSI, TANF and Medicaid, a year from FY2031 (2026 dollars)"),
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
    eligible = v('tier_b_m') + v('tier_a_outside_b_m') + v('registered_m')   # late arrivals move between groups, not out
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
    # The money runs until the net backlog clears, so the six-month target (IMM-6.03) holds: about
    # a year longer than EV-IMM-575's four to five years at its pace.
    years_to_clear = v('uscis_net_backlog_m') / (v('backlog_bn_per_year') * 1000 / v('backlog_cost_per_case_usd'))
    yrs = max(v('backlog_years'), years_to_clear)
    backlog_money = {y: v('backlog_bn_per_year') * max(0.0, min(1.0, yrs - (y - 2030))) for y in YEARS}
    cleared = sum(backlog_money[y] for y in YEARS) * 1000 / v('backlog_cost_per_case_usd')   # million cases
    n400 = {y: v('n400_apps_m') * v('n400_fee_usd') * (v('n400_free_share') + 0.5 * v('n400_half_share')) * prices(y, case) / 1000 for y in YEARS}
    online = {y: v('online_ona_bn') / 10 for y in YEARS}
    bridge = {y: (v('fee_lag_bridge_bn') / 3 if y in (2030, 2031, 2032) else 0.0) for y in YEARS}
    memo7 = {y: backlog_money[y] + n400[y] + online[y] + bridge[y] for y in YEARS}
    return dict(filings_m=filings, filings_by_year=per_year, memo2=memo2, memo7=memo7,
                backlog_cleared_m=cleared, backlog_years_to_clear=years_to_clear,
                backlog_left_m=max(0.0, v('uscis_net_backlog_m') - cleared))


def court_path(target, case='central', ramp=None):
    """Judges, completions and pending cases by fiscal year, hiring toward `target` at `ramp` a year.

    FY2030 starts from today's corps and pending cases (EV-IMM-103, EV-IMM-100). Filing for status
    opens in FY2031, closing the share of pending cases whose people file (IMM-1.10), and officers
    deciding first cut receipts from then on (IMM-3.01). Hires decide half a year of cases in their
    first year. Once the backlog is cleared, the corps shrinks by attrition toward what receipts need.
    """
    v = lambda n: val(n, case)
    ramp = val('hiring_ramp') if ramp is None else ramp   # sized at the central ramp; the slow ramp is its own scenario
    c, att = v('completions_per_judge'), v('judge_attrition')
    judges, pending = v('judges_now'), v('court_pending_m') * 1e6
    base_receipts = v('court_receipts_k') * 1000
    rows, cleared_fy = {}, None
    for y in range(2030, 2046):
        receipts = base_receipts if y < FILING_OPENS else base_receipts * (1 - v('officer_first_receipt_cut'))
        if y == FILING_OPENS:
            pending *= 1 - v('closed_on_filing_share')
        need = receipts / c
        if cleared_fy is None:
            hires = max(0.0, min(ramp + judges * att, target - judges * (1 - att)))
            new = judges * (1 - att) + hires
            completions = (judges * (1 - att) + hires * v('new_judge_productivity')) * c
        else:
            new = max(need, judges * (1 - att))
            completions = new * c
        judges = new
        pending = max(receipts * v('cleared_receipts_years'), pending + receipts - completions)
        if cleared_fy is None and pending <= receipts * v('cleared_receipts_years') + 1:
            cleared_fy = y
        rows[y] = dict(judges=judges, pending=pending)
    return rows, cleared_fy


def eoir(case='central'):
    """The judges that clear the court backlog in about six years, their cost, and appointed counsel."""
    v = lambda n: val(n, case)
    deadline = 2029 + int(v('clear_years'))                     # FY2035
    # The smallest corps that clears by the deadline; if the ramp cannot reach one in time (low
    # productivity), the smallest corps that clears as early as the ramp allows.
    results = [(t, court_path(t, case)[1]) for t in range(int(v('judges_now')), 4001, 10)]
    clearing = [(t, fy) for t, fy in results if fy is not None]
    on_time = [t for t, fy in clearing if fy <= deadline]
    if on_time:
        target = min(on_time)
    else:
        earliest = min(fy for _, fy in clearing)
        target = min(t for t, fy in clearing if fy == earliest)
    rows, cleared = court_path(target, case)
    now = v('judges_now')
    judges_cost = {y: max(0.0, rows[y]['judges'] - now) * v('judge_team_cost_m') * prices(y, case) / 1000
                   if y in rows else 0.0 for y in YEARS}
    _, at_cap = court_path(800, case)
    _, slow = court_path(target, case, ramp=150)
    detained_cases = val('cap') * 365 / v('detained_avg_days') * v('detained_court_share')
    counsel_2026 = (detained_cases * v('counsel_cost_detained_usd') + v('children_cases_k') * 1000 * v('counsel_cost_child_usd')
                    + v('smi_cases_k') * 1000 * v('counsel_cost_smi_usd')) / 1e9
    backlog_children = v('children_backlog_k') * 1000 * v('counsel_cost_child_usd') / 5 / 1e9     # FY2031-35
    counsel = {y: (counsel_2026 * (0.5 if y == 2030 else 1.0) + (backlog_children if 2031 <= y <= 2035 else 0.0))
               * prices(y, case) for y in YEARS}
    peak = max(r['judges'] for r in rows.values())
    return dict(judges_needed=target, judges_added=target - now, judges_peak=peak, cleared_fy=cleared,
                cleared_at_800=at_cap, cleared_slow_ramp=slow, judges_by_year={y: rows[y]['judges'] for y in YEARS},
                judges_cost=judges_cost, detained_cases_k=detained_cases / 1000, counsel=counsel)


def term_increment(case='central'):
    """A-1 (milestone review): the added judges hired on terms that end once the backlog clears.

    After clearance the corps the model keeps shrinks only by attrition. Receipts then need about
    receipts after officers decide first / completions a judge, at or below today's 753. With the
    increment on terms, judges above today's corps end with the fiscal year after clearance, so the
    judge-team line after it is saved. Returns that saving (FY2036-39 and FY2040) and the need.
    """
    v = lambda n: val(n, case)
    e = eoir(case)
    need = v('court_receipts_k') * 1000 * (1 - v('officer_first_receipt_cut')) / v('completions_per_judge')
    after = [y for y in YEARS if e['cleared_fy'] is not None and y > e['cleared_fy']]
    saving = {y: (e['judges_cost'][y] if y in after else 0.0) for y in YEARS}
    return dict(need=need, saving_window=sum(saving[y] for y in WINDOW), saving_2040=saving[2040])


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


_CARE = {}


def care_cost_of_residual(n_m):
    """Net federal cost added on care's own path when n_m million more people join the single plan.

    Runs `dossiers/care/tools/health_path.py` with care's residual uninsured share
    (`sp_residual_unins`, 1%) lowered by n_m million, and returns the difference by fiscal year.
    Care's booked figures keep the 1%; this dossier counts the difference once (6-cost.md, part 3).
    """
    key = round(n_m, 4)
    if key not in _CARE:
        import importlib
        care = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'care', 'tools')
        if care not in sys.path:
            sys.path.insert(0, care)
        H = importlib.import_module('health_path')

        def run(n):
            I, B, P = H.setup()
            I['sp_residual_unins'] = I['sp_residual_unins'] - n / B['pop'] * (1 if B['pop'] < 1e3 else 1e6)
            B = H.M.build_base(I)
            s, _ = H.path(I, B, P, H.rate_path(H.hospital_start(I, B)))
            return {y: s[y]['total'] for y in YEARS}
        base, more = run(0.0), run(n_m)
        _CARE[key] = {y: more[y] - base[y] for y in YEARS}
    return _CARE[key]


def per_person_on_care_path():
    """Care's net federal cost of one more person in the single plan, $ thousand by FY (FY2031 is 0.75 of a year)."""
    return care_cost_of_residual(1.0)


def lawful_added(case='central'):
    """People with lawful status who are not in care's population base: memo 3's added immigrants,
    the refugees above the baseline (IMM-3.04) and returnees under IMM-1.15, million by FY. Everyone already resident, the newly
    legalized and registered included, is in care's base (6-cost.md, part 3)."""
    v = lambda n: val(n, case)
    out = {}
    for y in YEARS:
        memo3 = v('added_lawful_m_2039') * min(1.0, max(0.0, (y - 2030) / 9))
        refugees = v('refugees_added_k') / 1000 * max(0, y - 2029)
        returnees = v('returnees_m') * min(1.0, max(0.0, (y - 2030) / 3))   # IMM-1.15, over FY2031-33
        out[y] = memo3 + refugees + returnees
    return out


def table(case='central'):
    """Memo 6 as amended for health (Espen, November 12, lead session).

    The single plan covers people with lawful or registered status; people with no status keep
    emergency care as today (EMTALA and Emergency Medicaid), which the January 2029 law already pays.
    The newly legalized and registered are already in care's population base, and the plan's
    replacement of federal Medicaid money there already nets their Emergency Medicaid. So the only
    added coverage is for lawful residents above care's base, priced on care's own path; plus the
    five-year wait's programs.
    """
    v = lambda n: val(n, case)
    pp = per_person_on_care_path()
    added = lawful_added(case)
    cover = {y: added[y] * pp[y] * v('lawful_added_cost_factor') for y in YEARS}
    wait = {y: (v('five_year_wait_bn') * (0.75 if y == 2031 else 1.0) * prices(y, case) if y >= 2031 else 0.0) for y in YEARS}
    # IMM-1.15's cases from abroad: about 1.4 applications a returnee (some are refused or do not come), over FY2031-33.
    returns = {y: (v('returnees_m') * 1.4 / 3 * 1e6 * v('return_case_usd') * prices(y, case) / 1e9 if 2031 <= y <= 2033 else 0.0) for y in YEARS}
    return {y: cover[y] + wait[y] + returns[y] for y in YEARS}


def care_base_correction(case='central'):
    """For the lead (not counted here): people care's base covers who have no status under memo 6 as amended.

    Care covers everyone but a 1% residual. Under the amendment, people with no status are not covered:
    eligible people who have not yet filed (a filing receipt counts as status for the plan) and those
    who never file. Those beyond the residual's status share are an overstatement in care's base.
    Returns $ billion by FY (negative: a saving to care's booked figures) and the people, million.
    """
    v = lambda n: val(n, case)
    u = uscis(case)
    eligible = v('tier_b_m') + v('tier_a_outside_b_m') + v('registered_m')
    pp = per_person_on_care_path()
    cum, people, saving = 0.0, {}, {}
    for y in YEARS:
        cum += u['filings_by_year'][y] if y < 2040 else 0.0
        people[y] = max(0.0, eligible - cum - v('without_status_m')) if y >= 2031 else 0.0
        saving[y] = -people[y] * pp[y]
    return dict(saving=saving, people=people)


def status_fiscal(case='central'):
    """Memo 1 on CBO's 2021 score of H.R. 6, scaled, grown and netted for the single plan."""
    v = lambda n: val(n, case)
    gross = v('hr6_deficit_bn') * v('reach_scale') * v('window_growth')
    net = gross * (1 - v('health_share') * v('covered_anyway_share'))
    # Tier A's January 1 cutoff moves late arrivals to registered status: they wait for a green
    # card, so the status line falls by their share of the green-card population (IMM-1.04).
    green = v('tier_b_m') + v('tier_a_outside_b_m')
    net *= 1 - v('tier_a_late_arrivals_m') / green
    w = sum(STATUS_SHAPE[y] for y in WINDOW)
    return {y: net * STATUS_SHAPE[y] / w for y in YEARS}


def everify_coverage(case='central'):
    """Share of the unauthorized workforce left after memo 1 that the mandate covers, by FY.

    Tranches a year apart from the first (IMM-4.12, 4.13), covering 0.2, 0.45, 0.7 and 1.0 of
    that workforce (judgment: unauthorized workers sit mostly in small firms and households).
    A tranche starting part-way through a fiscal year counts for the part of the year it runs.
    """
    start = val('everify_first_tranche_fy', case)
    steps = (0.2, 0.45, 0.7, 1.0)
    out = {}
    for y in YEARS:
        share = 0.0
        for i, level in enumerate(steps):
            t = start + i                           # fiscal-year time the tranche begins
            frac = min(1.0, max(0.0, y - (t - 1)))  # FY y covers (y-1, y]
            prev = steps[i - 1] if i else 0.0
            share += (level - prev) * frac
        out[y] = share
    return out


def window(path):
    return sum(path[y] for y in WINDOW)


def lines(case='central'):
    """The model's general-fund lines for section 6 (immigration_path.py adds the rest)."""
    u, e, a = uscis(case), eoir(case), asylum_refugees(case)
    memo4 = {y: a['corps'][y] + a['refugees'][y] + a['regional'][y] + e['counsel'][y] for y in YEARS}
    return {'memo1': status_fiscal(case), 'memo2': u['memo2'], 'memo4': memo4, 'judges': e['judges_cost'],
            'detention': detention(case), 'memo7': u['memo7'], 'memo6': table(case)}


def report():
    for case in ('central', 'low', 'high'):
        L = lines(case)
        print(f'[{case}] ' + '; '.join(f'{k} {window(p):.1f} / {p[2040]:.1f}' for k, p in L.items()))
    u, e = uscis(), eoir()
    print(f"USCIS: about {u['filings_m']:.1f} million filings; the net backlog of {val('uscis_net_backlog_m')} million "
          f"clears in about {u['backlog_years_to_clear']:.1f} years at the backlog money's pace ({u['backlog_left_m']:.1f} million left when it ends)")
    for case in ('central', 'low', 'high'):
        ec = eoir(case)
        print(f"Courts [{case}]: about {ec['judges_needed']:.0f} judges in all ({ec['judges_added']:.0f} added) clear the backlog by FY{ec['cleared_fy']}; "
              f"at 800 judges: FY{ec['cleared_at_800']}; at 150 hires a year: FY{ec['cleared_slow_ramp']}; "
              f"judge teams ${window(ec['judges_cost']):.1f}B over FY2030-39; counsel ${window(ec['counsel']):.1f}B")
    t = term_increment()
    print(f"Term-limited increment (A-1): steady-state need about {t['need']:.0f} judges; saves ${t['saving_window']:.1f}B "
          f"over FY2036-39 and ${t['saving_2040']:.1f}B in FY2040")
    cb = care_base_correction()
    print(f"Care's base, for the lead: about {cb['people'][2031]:.1f} million people with no status counted as covered in FY2031, "
          f"{cb['people'][2035]:.1f} million in FY2035; about ${-window(cb['saving']):.0f}B over FY2030-39 and ${-cb['saving'][2040]:.1f}B in FY2040 too high")
    print('Judges by year (central): ' + ', '.join(f"{y}: {j:.0f}" for y, j in eoir()['judges_by_year'].items()))
    a = asylum_refugees()
    print('Memo 4 parts (FY2030-39): corps {:.1f}, refugees {:.1f}, regional {:.1f}, counsel {:.1f}'.format(
        window(a['corps']), window(a['refugees']), window(a['regional']), window(e['counsel'])))


if __name__ == '__main__':
    report()
