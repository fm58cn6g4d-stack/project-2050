#!/usr/bin/env python3
"""Tests of the housing model (`MOD-housing`): inputs, reproduction of 6-cost.md, benchmarks, the rent module and the card.

Run from anywhere: python3 models/tools/housing/test_housing.py
           python3 models/tools/housing/test_housing.py --write-card   # regenerate the card's two blocks

1. **Inputs:** the four parameter files meet the toolkit's schema; every evidence and policy row cites an entry
   that exists (an EV- ID in a dossier register, a DEC- ID in `charter/decisions.md`).
2. **Reproduction** (in-sample by construction: the inputs are 6-cost.md's): section 1.2 line by line, its totals,
   section 1.4's lease-up table, and the budget model's booking of housing (`fiscal-components.csv`, HOU-1;
   `recovery-adoption.json`, HOU-4D). Tolerances are the published figures' own rounding.
3. **Benchmarks** (independent): CBO's and HUD's per-household cost and lease-up figures from the register, with
   tolerances fixed in this file, as `models/schema/validation.py` records them.
4. **The rent module** stays out of the cost, and supply is a range with no year path (no forecast).
5. **The committed results** are what the code builds; the card's blocks are the ones the code renders.
"""
import csv, json, os, re, sys, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'models', 'schema'))
sys.path.insert(0, os.path.join(ROOT, 'models'))
import housing_model as m  # noqa: E402
import housing_run as run  # noqa: E402
import parameters as PS  # noqa: E402
import validation as V  # noqa: E402
import runlog  # noqa: E402

CARD = os.path.join(HERE, 'MODEL-CARD.md')
VSTART, VEND = '<!-- generated:validation:start -->', '<!-- generated:validation:end -->'
PARAM_FILES = [(m.PARAMETERS, 'the judgment inputs of the rental help lines, the stages\' counts and the indexation rates'),
               (m.PLAN, "the plan's decided amounts and schedules, held fixed across the cases"),
               (m.PUBLISHED, 'lines taken as 6-cost.md publishes them, because it states no build this model can rerun'),
               (m.MARKET, 'the reach, rent and supply evidence')]
B = V.Benchmark


def register_ids():
    ids = set()
    for dirpath, _, files in os.walk(os.path.join(ROOT, 'dossiers')):
        if 'evidence.json' in files:
            with open(os.path.join(dirpath, 'evidence.json'), encoding='utf-8') as f:
                ids |= {e['id'] for e in json.load(f)}
    return ids


def decision_ids():
    with open(os.path.join(ROOT, 'charter', 'decisions.md'), encoding='utf-8') as f:
        return set(re.findall(r'^\| (DEC-\d{4}-\d{2}-\d{2}-\d+) \|', f.read(), re.M))


# ---------------------------------------------------------------- 1. inputs
class Inputs(unittest.TestCase):
    def test_files_meet_the_schema(self):
        for f, _ in PARAM_FILES:
            self.assertEqual(PS.validate(PS.read(f)), [], f)

    def test_every_cited_id_exists(self):
        ev, dec = register_ids(), decision_ids()
        for f, _ in PARAM_FILES:
            for r in PS.read(f):
                for i in re.findall(r'\bEV-[A-Z]+-\d+\b', r['source']):
                    self.assertIn(i, ev, f'{os.path.basename(f)} {r["id"]}: {i} is not in any register')
                for i in re.findall(r'\bDEC-\d{4}-\d{2}-\d{2}-\d+\b', r['source']):
                    self.assertIn(i, dec, f'{os.path.basename(f)} {r["id"]}: {i} is not in charter/decisions.md')

    def test_duty_lift_base_is_the_central_leased_share(self):
        self.assertEqual(m.LEASED_CENTRAL, m.load('central')['leased_share'])

    def test_low_case_costs_less_and_high_more(self):
        t = {c: m.totals(m.lines(c))['housing_window'] for c in m.CASES}
        self.assertLess(t['low'], t['central'])
        self.assertLess(t['central'], t['high'])

    def test_every_line_runs_low_to_central_to_high(self):
        L = {c: m.lines(c) for c in m.CASES}
        for k in L['central']:
            if k == DUTY:
                continue
            lo, c, hi = (L[x][k]['window'] for x in ('low', 'central', 'high'))
            self.assertTrue(lo <= c + 1e-9 and c <= hi + 1e-9, f'{k}: {lo:.2f}, {c:.2f}, {hi:.2f}')

    def test_the_duty_to_house_with_stage_2_runs_low_to_high(self):
        # the duty's own line is the one exception (DUTY_NOTE); stage 2 with its duty must still be in order
        L = {c: m.lines(c) for c in m.CASES}
        s = [L[c]['hou-4d-01-stage-2']['window'] + L[c][DUTY]['window'] for c in ('low', 'central', 'high')]
        self.assertTrue(s[0] < s[1] < s[2], s)
        P = m.load('high')
        self.assertLessEqual(P['leased_share'] * (1 + min(P['duty_leased_share'] / m.LEASED_CENTRAL, 1 / P['leased_share']) - 1), 1 + 1e-9)


# ---------------------------------------------------------------- 2. reproduction (in-sample)
DUTY = 'hou-4d-01-duty-to-house'
DUTY_NOTE = ("the duty to house's high falls below its central: in the high case awards already lease at 98%, so the duty "
             "can add only the last 2 points; 6-cost.md's high of $5 billion would need stage 2 to lease more than 100% of "
             "its awards. Stage 2 with the duty runs $48.5, 84.2 and 144.3 billion")
KNOWN = {   # lines where 6-cost.md 1.2's figure differs from the section's own build, with the reason
    'hou-3c-02-construction-loan-subsidy': ("6-cost.md's own inputs give $14.7 billion: $15 billion of subsidy at 5% on $300 billion "
                                            "committed evenly FY2030-38, less the 20% of FY2038's disbursed in FY2040 ($0.3 billion, "
                                            "the table's 0.4). Section 3.5 prints 14.6; the table rounds it to 14. The booking carries 14 "
                                            "(fiscal-components.csv 0.014)."),
    'hou-13-01-property-tax-match': ("Section 2.9's own schedule ($0.5, 1.5, 2 and 2.5 billion in FY2031-34, then 4% a year) sums to "
                                     "$20.58 billion; the table prints 20.5 and the booking 0.0205."),
}


SHORT = {'hou-4a-one-million-awards-full-fees': 'HOU-4A', 'hou-4-07-search-help': 'HOU-4.07', 'hou-4d-01-stage-2': 'HOU-4D',
         'hou-4d-01-duty-to-house': 'HOU-4D-DUTY', 'hou-4d-01-wider-entry': 'HOU-4D-WIDER', 'hou-4d-01-restated-count': 'HOU-4D-RESTATED',
         'hou-4-08-stage-3-under-62': 'HOU-4.08-U62', 'hou-4-08-stage-3-62-and-over': 'HOU-4.08-62UP', 'hou-1d-04-one-time-start': 'HOU-1D.04',
         'hou-1d-01-standing-emergency-fund': 'HOU-1D.01', 'hou-3c-01-revolving-fund-grants': 'HOU-3C.01', 'hou-3c-02-construction-loan-subsidy': 'HOU-3C.02',
         'hou-5-01-public-housing-repair': 'HOU-5.01', 'hou-4-10-recovery-housing': 'HOU-4.10', 'hou-4-12-services-backstop': 'HOU-4.12',
         'hou-4-12-wider-backstop-to-2035': 'HOU-4.12-WIDER', 'hou-4-06-testing-grants': 'HOU-4.06', 'payment-standards-to-120-percent': 'PAYSTD',
         'inspector-general-set-aside': 'IG', 'hou-10-01-down-payment-help': 'HOU-10.01', 'hou-12-01-home-repair-fund': 'HOU-12.01',
         'hou-13-01-property-tax-match': 'HOU-13.01', 'hou-13-02-to-04-equity-coordinators-sharing': 'HOU-13.02', 'hou-14-01-rural-development-staff': 'HOU-14.01',
         'hou-14-02-section-502-at-scale': 'HOU-14.02', 'hou-14-03-rural-rental-fund-and-vouchers': 'HOU-14.03'}


def tol_for(published):
    return 0.5 if float(published).is_integer() else 0.05


def reproduction_rows():
    C, Lo, Hi = m.lines('central'), m.lines('low'), m.lines('high')
    tc, tl, th = m.totals(C), m.totals(Lo), m.totals(Hi)
    ev = V.evaluate
    rows = []
    for k, label, c, lo, hi, f40 in m.TABLE_1_2:
        if C[k]['method'] != 'built':
            continue
        rows.append(ev(B(f'REP-{SHORT[k]}', f'{label}, FY2030-39', c, '6-cost.md 1.2', 'the dossier, central', '$ billion',
                         tol_for(c), 'absolute', "the table's own rounding (half its last digit)",
                         in_sample=True, explanation=KNOWN.get(k, DUTY_NOTE if k == DUTY else "the dossier's arithmetic, rebuilt from its inputs")), round(C[k]['window'], 6)))
    sums = sum(x[2] for x in m.TABLE_1_2)
    rows += [
        ev(B('REP-TOTAL', 'Housing, total, FY2030-39 (spending and credits)', m.TABLE_HOUSING[0], '6-cost.md 1.2 and In brief ($0.81 trillion)', 'the dossier, central', '$ billion',
             1.5, 'absolute', 'the published total is the sum of 33 lines each rounded to $1 billion or $0.1 billion (0.2%)', in_sample=True,
             explanation=f"the model sums unrounded lines; the table's lines sum to {sums + m.TABLE_CREDITS[0]:.1f}. The two known differences above add $0.7 billion and $0.1 billion; the rest is the other lines' rounding"),
           tc['housing_window']),
        ev(B('REP-SPEND', 'Spending, total, FY2030-39', m.TABLE_SPENDING[0], '6-cost.md 1.2', 'the dossier, central', '$ billion', 1.5, 'absolute',
             'as REP-TOTAL', in_sample=True, explanation='as REP-TOTAL'), tc['spending_window']),
        ev(B('REP-FY2040', 'Housing, FY2040 (with the capital tail)', m.TABLE_HOUSING[3], '6-cost.md 1.2; 3.2 (the model booked $120.5 billion)', 'the dossier and the budget model', '$ billion',
             1.5, 'absolute', "the table's rounding to $1 billion and the booking's fit", in_sample=True,
             explanation='the lines taken as published carry their FY2040 figures as printed'), tc['housing_fy2040']),
        ev(B('REP-LOW', 'Housing, low case, FY2030-39', m.TABLE_HOUSING[1], '6-cost.md 1.2', 'the dossier, low', '$ billion', 0.02, 'relative',
             'the low case moves every judgment input together; 2% allows for the lag and count rounding', in_sample=True,
             explanation='rental lines rebuilt at every input\'s low; lines built from decided amounts take the published ranges as ratios to the central'), tl['housing_window']),
        ev(B('REP-HIGH', 'Housing, high case, FY2030-39', m.TABLE_HOUSING[2], '6-cost.md 1.2', 'the dossier, high', '$ billion', 0.02, 'relative',
             'as REP-LOW', in_sample=True,
             explanation=(f"6-cost.md's high total is below the sum of its own line highs ({sum(x[4] for x in m.TABLE_1_2) + m.TABLE_CREDITS[2]:.0f}). "
                          "The model's lines differ from the published highs by up to $2.7 billion each, in both directions: search help +1.9, "
                          "the older stage 3 group +1.3, the wider entry +0.4, HOU-4A -0.5, stage 3 under 62 -0.4 and the duty to house -2.7 "
                          "(see REP-HOU-4D-DUTY), so the total's pass partly rests on offsets")),
           th['housing_window']),
    ]
    lu = m.lease_up()
    for s, (w, f, hh) in {'0.57': (160, 36, 1.49), '0.75': (208, 47, 1.97), '0.90': (248, 57, 2.36)}.items():
        d = lu[s]
        rows += [ev(B(f'REP-LEASE-{s}-W', f'Rental help at {float(s):.0%} leased, FY2030-39', w, '6-cost.md 1.4', 'the dossier', '$ billion', 1, 'absolute',
                      'the table rounds to $1 billion', in_sample=True, explanation='HOU-4A, HOU-4D\'s first count and stage 3 under 62, with fees, search help and the higher payment standards'), d['rental_window']),
                 ev(B(f'REP-LEASE-{s}-40', f'Rental help at {float(s):.0%} leased, FY2040', f, '6-cost.md 1.4', 'the dossier', '$ billion', 1, 'absolute',
                      'as above', in_sample=True, explanation='as above'), d['rental_fy2040']),
                 ev(B(f'REP-LEASE-{s}-HH', f'Households housed by those three lines at {float(s):.0%} leased, FY2042', hh, '6-cost.md 1.4', 'the dossier', 'million households',
                      0.01, 'absolute', 'the table rounds to 10,000', in_sample=True, explanation='leased at the end of FY2042'), d['all_three_fy2042'] / 1e6)]
    rows.append(ev(B('REP-REACH-ALL', 'Households housed in FY2042, all three stages with the added counts, 90% leased', 3.6, '6-cost.md 1.4 and 2.12 (3.0-3.6 million)', 'the dossier', 'million households',
                     0.05, 'absolute', 'printed to 0.1 million', in_sample=True, explanation='before the financing settlement capped stage 2 (DEC-2026-11-24-09)'), lu['0.90']['all_stages_fy2042'] / 1e6))
    # the budget model's booking
    booked = {x['component']: float(x['mid10']) * 1000 for x in csv.DictReader(open(os.path.join(ROOT, 'models', 'data', 'inputs', 'fiscal-components.csv'), encoding='utf-8')) if x['owner'] == 'HOU-1'}
    hou4d = ('hou-4d-01-stage-2', 'hou-4d-01-wider-entry', 'hou-4d-01-restated-count')
    with open(os.path.join(ROOT, 'models', 'data', 'inputs', 'recovery-adoption.json'), encoding='utf-8') as f:
        extra = json.load(f)
    extra = extra.get('housing_extra_tn', extra.get('params', {}).get('housing_extra_tn')) if isinstance(extra, dict) else None
    rows.append(ev(B('REP-BOOK-HOU1', "HOU-1 as booked: the 31 components (the duty to house removed by the settlement)", sum(booked.values()), 'models/data/inputs/fiscal-components.csv (HOU-1); DEC-2026-11-24-09',
                     'the budget model, as booked', '$ billion', 1.5, 'absolute', 'the components carry 6-cost.md\'s rounded figures', in_sample=True,
                     explanation='the model\'s same 31 lines; the booking takes the table\'s rounded figures'), sum(C[k]['window'] for k in booked)))
    if extra is not None:
        rows.append(ev(B('REP-BOOK-HOU4D', "HOU-4D as booked (housing_extra): stage 2, its wider entry and the restated count", extra * 1000, 'models/data/inputs/recovery-adoption.json',
                         'the budget model, as booked', '$ billion', 1.5, 'absolute', 'as above', in_sample=True, explanation='81 + 17 + 17 in the table'), sum(C[k]['window'] for k in hou4d)))
    return rows


# ---------------------------------------------------------------- 3. benchmarks (independent)
def benchmark_rows():
    P = m.load('central')
    per_hh_2030 = P['subsidy_fy2030'] * (1 + P['fee_rate'])          # subsidy plus fees per leased household-year
    back = lambda y: per_hh_2030 / 1.04 ** (2030 - y)                   # back along 6-cost.md 1.1's 4% path from 2023
    ev = V.evaluate
    lu = m.lease_up((P['leased_share'],))
    return [
        ev(B('BM-CBO-1', 'Cost per assisted household-year with fees, 2020 dollars: CBO\'s vouchers for all ELI households', 290e9 / 4.5e6 / 5.5,
             'EV-HOU-390', 'CBO budget option, 2015: $290 billion over 2016-25 for 4.5 million more households, phased in over ten years (5.5 household-years each if even; 7-validation.md 1.1)', '$ a household-year',
             0.25, 'relative', 'two vintages a decade apart, a different population (every ELI household) and an assumed even phase-in: a gap beyond a quarter would mean the subsidy is out of line',
             explanation='the model\'s FY2030 cost per leased household with fees, taken back to 2020 along 6-cost.md 1.1\'s 4% path'), back(2020)),
        ev(B('BM-CBO-2', 'Federal spending per voucher household, 2019 dollars', 9400, 'EV-HOU-391', 'CBO budget option, December 2018 (for 2019)', '$ a household-year',
             0.25, 'relative', 'as BM-CBO-1',
             explanation=('a miss: HUD\'s own 2023 figure ($12,816, EV-HOU-370) is already 36% above CBO\'s 2019 one, and the account grew 34% in FY2019-23 '
                          '(EV-HOU-187), much faster than the 4% path the model is taken back along; the plan\'s households are also poorer than '
                          'the average voucher household (7-validation.md 1.1). It supports the dossier\'s verdict: the risk is upward')), back(2019)),
        ev(B('BM-CBO-3', 'Cost per added voucher household-year, 2020 dollars: CBO\'s 10% voucher increase', 18e9 / 200e3 / 10, 'EV-HOU-390', 'CBO budget option, 2015: about 200,000 more households for $18 billion over ten years', '$ a household-year',
             0.25, 'relative', 'as BM-CBO-1',
             explanation=('a miss: CBO priced added vouchers at the existing program\'s 2015 mix and costs; per-voucher costs rose much faster after 2019 '
                          '(EV-HOU-187), and the plan pays full fees, an issuance fee and higher payment standards for poorer households')), back(2020)),
        ev(B('BM-HUD-1', 'Rent subsidy per leased household, 2023', 1068 * 12, 'EV-HOU-370', 'HUD, Picture of Subsidized Households, end of 2023', '$ a household-year',
             0.02, 'relative', 'the subsidy input was grown from this figure, so only arithmetic is checked', in_sample=True,
             explanation='in-sample by construction: 6-cost.md 1.1 grows HUD\'s 2023 figure 4% a year to $17,000 in FY2030'), P['subsidy_fy2030'] / 1.04 ** 7),
        ev(B('BM-HUD-2', 'Share of awards leased, steady state', 0.84, 'EV-HOU-370', 'HUD, end of 2023: units occupied of units authorized', 'share',
             0.1, 'absolute', 'ten points: occupancy is held down by funding as well as by search, so it is a loose floor for the plan\'s measure',
             explanation='the model\'s 90% is above it by six points; the measures differ (7-validation.md 1.2)'), P['leased_share']),
        ev(B('BM-HUD-3', 'Share of awards leased, measured the plan\'s way (with reissue)', 0.67, 'EV-HOU-345', 'HUD, Emergency Housing Vouchers, February 2023 (about two years after award)', 'share',
             0.1, 'absolute', 'ten points: the only precedent measured as the plan measures, at full fees and with waivers',
             explanation=('a miss, and the reason section 1.4\'s sensitivity exists: the dossier rates lease-up at risk (7-validation.md 1.2). '
                          '`--leased 0.75` and `--leased 0.57` rerun every rental line; at 67% the first million houses about 670,000')), P['leased_share']),
        ev(B('BM-HUD-4', "Stage 2's renter families: HUD's ELI families with children with worst case needs, less those stage 1 houses", (1.4, 1.8), 'EV-HOU-186',
             'HUD, Worst Case Housing Needs 2025 (2023 data): 1.717 million', 'million families', 0.0, 'range', 'the dossier\'s own range around HUD\'s count', in_sample=True,
             explanation='in-sample: the restated count is built from HUD\'s 1.717 million (6-cost.md 2.12)'), P['stage2_restated_total_m']),
        ev(B('BM-HUD-5', 'Stage 3 under 62: households applying', (0.817 * 0.686, 0.817 * 0.85), 'EV-HOU-371; EV-HOU-185',
             'HUD, Worst Case Housing Needs 2025: 1.162 million VLI renter households with a disabled member under 62 and worst case needs, less 345,000 families with children, at a 68.6-85% ELI share',
             'million households', 0.05, 'range', 'the 85-100% take-up and room for growth that 6-cost.md 2.1 adds', in_sample=True,
             explanation='in-sample: 6-cost.md 2.1 builds the 600,000 from these counts'), P['stage3_under62_m']),
        ev(B('BM-URB-1', 'Average subsidy of a new voucher, 2022 dollars, per month', 765, 'EV-HOU-392', 'Urban Institute, 2023 (full funding of vouchers)', '$ a month',
             0.25, 'relative', 'as BM-CBO-1',
             explanation=('a miss: Urban\'s new vouchers reach every household under 50% of area median income, who pay more of their rent; the plan\'s go '
                          'to homeless households and the poorest families and disabled renters (7-validation.md 1.1)')), P['subsidy_fy2030'] / 1.04 ** 8 / 12),
    ]


def validation_block():
    rep, bm = reproduction_rows(), benchmark_rows()
    return (VSTART + '\n**Reproduction of `dossiers/home/6-cost.md` and the booking** (in-sample by construction: they check the rebuild, not accuracy). '
            + V.render(rep) + '\n\n**Benchmarks against CBO, HUD and the Urban Institute.** ' + V.render(bm) + '\n' + VEND)


def parameters_block():
    parts = [f'**`{os.path.basename(f)}`** ({what}). ' + PS.table(PS.read(f)) for f, what in PARAM_FILES]
    return PS.START + '\n' + '\n\n'.join(parts) + '\n' + PS.END


def write_card():
    s = open(CARD, encoding='utf-8').read()
    for start, end, block in ((VSTART, VEND, validation_block()), (PS.START, PS.END, parameters_block())):
        a, b = s.index(start), s.index(end) + len(end)
        s = s[:a] + block + s[b:]
    with open(CARD, 'w', encoding='utf-8') as f:
        f.write(s)


class Reproduction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = reproduction_rows()

    def test_no_problems(self):
        self.assertEqual(V.problems(self.rows), [])

    def test_every_built_line_reproduces_but_the_known_differences(self):
        line_ids = {f'REP-{v}' for v in SHORT.values()}
        miss = {r.id for r in self.rows if r.id in line_ids and not r.passed}
        known = {f'REP-{SHORT[k]}' for k in KNOWN}
        self.assertEqual(miss - known, set(), 'a line no longer reproduces 6-cost.md')

    def test_headline_reproduces(self):
        t = m.totals(m.lines())
        self.assertEqual(round(t['housing_window'] / 1000, 2), 0.81)          # "about $0.81 trillion"
        self.assertLessEqual(abs(t['housing_window'] - 806), 1.5)
        self.assertLessEqual(abs(t['housing_fy2040'] - 120), 1.5)

    def test_lease_up_table_and_booking_pass(self):
        for r in self.rows:
            if r.id.startswith(('REP-LEASE', 'REP-BOOK', 'REP-TOTAL', 'REP-SPEND', 'REP-FY2040', 'REP-LOW', 'REP-REACH')):
                self.assertTrue(r.passed, r.id)


class Benchmarks(unittest.TestCase):
    def test_no_problems_and_both_publishers(self):
        rows = benchmark_rows()
        self.assertEqual(V.problems(rows), [])
        self.assertTrue({'CBO', 'HUD'} <= {r.id.split('-')[1] for r in rows})


# ---------------------------------------------------------------- 4. rents and supply
class Rents(unittest.TestCase):
    def test_rent_readings_are_not_in_the_cost(self):
        r = m.rents()
        t = m.totals(m.lines())
        self.assertNotIn('rents', m.lines())
        self.assertLessEqual(r['readings']['high']['fy2040']['landlord_capture_tight'], r['added_rent_subsidy']['fy2040'])
        self.assertEqual(r['readings']['low']['fy2040']['landlord_capture_tight'], 0.0)       # Eriksen and Ross: no rise
        self.assertIsNone(r['readings']['central']['fy2040']['spillover_to_unassisted_tight'])  # no central: the evidence is split
        self.assertAlmostEqual(t['housing_window'], m.totals(m.lines())['housing_window'])

    def test_supply_is_a_range_not_a_forecast(self):
        s = m.supply()
        self.assertIn('not a forecast', s['statement'])
        self.assertFalse(any(isinstance(v, dict) for v in s.values()), 'supply has no year path')
        lo, hi = s['net_homes_added_m']
        self.assertEqual(lo, 0.0)
        self.assertLess(hi, s['homes_paid_for_directly_m'][2])


# ---------------------------------------------------------------- 5. results and the card
class ResultsAndCard(unittest.TestCase):
    def test_committed_results_are_what_the_code_builds(self):
        built = runlog.dumps(run.run())
        with open(os.path.join(HERE, 'results.json'), encoding='utf-8') as f:
            self.assertEqual(f.read(), built, 'results.json is stale: run housing_run.py')

    def test_leased_override_changes_reach_not_inputs(self):
        a = m.reach('central', 0.75)['leased_by_stage']['stage_1_first_million']['2034']
        self.assertAlmostEqual(a, 750000, delta=1)

    def test_card_blocks_are_the_ones_the_code_renders(self):
        s = open(CARD, encoding='utf-8').read()
        self.assertIn(validation_block(), s, 'the card\'s validation tables are stale: run test_housing.py --write-card')
        self.assertIn(parameters_block(), s, 'the card\'s evidence map is stale: run test_housing.py --write-card')


if __name__ == '__main__':
    if '--write-card' in sys.argv:
        write_card()
        print('wrote the card\'s evidence map and validation tables')
        sys.exit(0)
    unittest.main()
