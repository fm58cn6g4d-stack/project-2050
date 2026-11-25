"""The immigration model: system capacity, adjudication and fiscal effects (`MOD-immigration`).

Role: the core of the immigration model `charter/PLAN.md` 3.4 names, moved from the immigration dossier's first
version (`dossiers/immigration/tools/`, board row I4) in stage H step H6; the card is `MODEL-CARD.md` beside this
file. Status: working (`models/toolkit.csv`). Version: see `immigration_run.VERSION`.
Run from the repository root: python3 models/tools/immigration/immigration_run.py [--scenario all] [--out DIR]
Test: python3 models/tools/immigration/test_immigration.py

Four modules, each on federal fiscal years FY2030-40, nominal $ billion, a cost positive:
  1. uscis()      USCIS throughput and backlog under the registry's volume (memo 2 C), and the
                  split between fees and the appropriation (memo 7 B);
  2. eoir()       immigration-court capacity: judges and years to clear the backlog with the
                  800-judge cap repealed (memo 4), and appointed counsel's cost (counsel B);
  3. detention()  the 30,000 cap against case management (memo 5, A's rules);
  4. status_fiscal()  the general-fund effect of status (memo 1) from CBO's published 2021
                  score, as `dossiers/immigration/3-design.md`, "IMM-1's score, re-derived", sets it out.
Labor-market effects are a separate module, `immigration_labor.py`, whose results are reported beside the
booked figures and never added to them.

Every input is a row of `parameters.csv` (or, for the plan's commitments, `plan.csv`), on the toolkit's parameter
schema (`models/schema/README.md`): value, unit, year, kind, source and a low and high. `INPUTS` below is built from
those files as {id: (central, low, high, basis)}; the basis is an evidence ID in
`dossiers/immigration/evidence.json`, "assumption: ..." with its reasoning, or a legacy figure with its file.
The scenarios `low` and `high` run each module at its low and high inputs together (a bound, not a probability
interval). A value with several years (a shape) is a tuple, held fixed across the scenarios.
"""

import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PARAMETERS = os.path.join(HERE, 'parameters.csv')
PLAN = os.path.join(HERE, 'plan.csv')
SHAPES = ('filing_shape', 'status_shape')     # multi-year rows read as one tuple, in year order

YEARS = list(range(2030, 2041))
WINDOW = range(2030, 2040)
COURT_LAST_FY = 2045   # court_path() runs FY2030-45


def _num(s):
    """A parameter value as the model uses it: an int when written without a point, else a float."""
    return int(s) if s.lstrip('-').isdigit() else float(s)


def load_parameters(paths=(PARAMETERS, PLAN)):
    """{id: (central, low, high, basis)} from the parameter files, in file order; shapes as (tuple, None, None, basis)."""
    out, shapes = {}, {}
    for path in paths:
        with open(path, newline='', encoding='utf-8') as f:
            for r in csv.DictReader(f):
                if r['id'] in SHAPES:
                    shapes.setdefault(r['id'], []).append((r['year'], _num(r['value']), r['source']))
                    if r['id'] not in out:
                        out[r['id']] = None          # keep the file's order
                    continue
                out[r['id']] = (_num(r['value']), _num(r['low']), _num(r['high']), r['source'])
    for k, rows in shapes.items():
        rows.sort(key=lambda t: int(t[0][2:]))
        out[k] = (tuple(v for _, v, _ in rows), None, None, rows[0][2])
    return out


_ALL = load_parameters()
FILING_OPENS = _ALL.pop('filing_opens_fy')[0]   # FY in which filing opens (about October 1, 2030; 4-specification.md)
# Memo 1's yearly profile: a cost rising through the decade, as in CBO's 2021 tables (EV-IMM-600).
STATUS_SHAPE = dict(zip(YEARS, _ALL.pop('status_shape')[0]))
INPUTS = _ALL


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


def court_path(target, case='central', ramp=None, **over):
    """Judges, completions and pending cases by fiscal year, hiring toward `target` at `ramp` a year.

    FY2030 starts from today's corps and pending cases (EV-IMM-103, EV-IMM-100). Filing for status
    opens in FY2031, closing the share of pending cases whose people file (IMM-1.10), and officers
    deciding first cut receipts from then on (IMM-3.01). Hires decide half a year of cases in their
    first year. Once the backlog is cleared, the corps shrinks by attrition toward what receipts need.

    Keyword overrides run the same mechanics on another projection's assumptions (the benchmarks replay
    CRS's R47637 this way, EV-IMM-642): `start` and `end` (fiscal years), `judges0`, `pending0` and `receipts` (people, cases, cases a year), `per_judge`,
    `attrition`, `new_productivity`, `cleared_years` (pending cases, in years of receipts, at which the backlog
    counts as cleared) and `plan` (False: no filing closure and no officer-first cut). With none given the
    path is the plan's, as section 6 uses it.
    """
    v = lambda n: val(n, case)
    ramp = val('hiring_ramp') if ramp is None else ramp   # sized at the central ramp; the slow ramp is its own scenario
    c = over.get('per_judge', v('completions_per_judge'))
    att = over.get('attrition', v('judge_attrition'))
    prod = over.get('new_productivity', v('new_judge_productivity'))
    cry = over.get('cleared_years', v('cleared_receipts_years'))
    plan = over.get('plan', True)
    start, end = over.get('start', 2030), over.get('end', COURT_LAST_FY)
    judges = over.get('judges0', v('judges_now'))
    pending = over.get('pending0', v('court_pending_m') * 1e6)
    base_receipts = over.get('receipts', v('court_receipts_k') * 1000)
    rows, cleared_fy = {}, None
    for y in range(start, end + 1):
        receipts = base_receipts if (y < FILING_OPENS or not plan) else base_receipts * (1 - v('officer_first_receipt_cut'))
        if y == FILING_OPENS and plan:
            pending *= 1 - v('closed_on_filing_share')
        need = receipts / c
        if cleared_fy is None:
            hires = max(0.0, min(ramp + judges * att, target - judges * (1 - att)))
            new = judges * (1 - att) + hires
            completions = (judges * (1 - att) + hires * prod) * c
        else:
            new = max(need, judges * (1 - att))
            completions = new * c
        judges = new
        pending = max(receipts * cry, pending + receipts - completions)
        if cleared_fy is None and pending <= receipts * cry + 1:
            cleared_fy = y
        rows[y] = dict(judges=judges, pending=pending)
    return rows, cleared_fy


def crs_replay(judges, case='central'):
    """CRS's R47637 projection (July 2023) run through court_path: the year the backlog reaches zero with `judges`.

    CRS's inputs, from the report (`library/text/crs-r47637-ij-hiring-backlog-projection.txt`, SRC-4089): 1.98
    million pending at the end of FY2023 Q2, 447,187 receipts a year (its five-year average), 509.6 completions a
    judge (EV-IMM-641's five years), the whole corps on staff at once, no attrition, nothing else changing. CRS's
    published years are reproduced counting whole fiscal years from FY2024 (the rest of FY2023 after Q2 is not
    counted). It returns the fiscal year the backlog reaches zero, or None by FY2100.
    """
    _, fy = court_path(judges, case, ramp=1e9, start=2024, end=2100, judges0=judges,
                       pending0=CRS_R47637['pending'], receipts=CRS_R47637['receipts'],
                       per_judge=CRS_R47637['per_judge'], attrition=0.0, new_productivity=1.0, cleared_years=0.0, plan=False)
    return fy


# CRS R47637's stated assumptions (SRC-4089, "Projected Impact of Immigration Judge Hiring" and Table 1); used only
# by the benchmark replay above, never by the plan's path.
CRS_R47637 = dict(pending=1.98e6, receipts=447187, per_judge=509.6, judges_now=649)


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
        care = os.path.join(ROOT, 'dossiers', 'care', 'tools')
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
    """For care's booking (not counted here): people care's base covered who have no status under memo 6 as amended.
    Booked by dossiers/care/tools/status_rule.py, which reads this function (HLT-7's status-rule component).

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


def fy_or_never(fy):
    """A fiscal year for the printout; None (the backlog does not clear inside court_path's years) in words."""
    return f'FY{fy}' if fy is not None else f'not by FY{COURT_LAST_FY}'


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
        print(f"Courts [{case}]: about {ec['judges_needed']:.0f} judges in all ({ec['judges_added']:.0f} added) clear the backlog by {fy_or_never(ec['cleared_fy'])}; "
              f"at 800 judges: {fy_or_never(ec['cleared_at_800'])}; at 150 hires a year: {fy_or_never(ec['cleared_slow_ramp'])}; "
              f"judge teams ${window(ec['judges_cost']):.1f}B over FY2030-39; counsel ${window(ec['counsel']):.1f}B")
    t = term_increment()
    print(f"Term-limited increment (A-1): steady-state need about {t['need']:.0f} judges; saves ${t['saving_window']:.1f}B "
          f"over FY2036-39 and ${t['saving_2040']:.1f}B in FY2040")
    cb = care_base_correction()
    print(f"Care's base (booked by care's status_rule.py): about {cb['people'][2031]:.1f} million people with no status counted as covered in FY2031, "
          f"{cb['people'][2035]:.1f} million in FY2035; about ${-window(cb['saving']):.0f}B over FY2030-39 and ${-cb['saving'][2040]:.1f}B in FY2040 too high")
    print('Judges by year (central): ' + ', '.join(f"{y}: {j:.0f}" for y, j in eoir()['judges_by_year'].items()))
    a = asylum_refugees()
    print('Memo 4 parts (FY2030-39): corps {:.1f}, refugees {:.1f}, regional {:.1f}, counsel {:.1f}'.format(
        window(a['corps']), window(a['refugees']), window(a['regional']), window(e['counsel'])))


if __name__ == '__main__':
    report()
