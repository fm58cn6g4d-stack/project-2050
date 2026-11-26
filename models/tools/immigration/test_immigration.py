#!/usr/bin/env python3
"""Tests of the immigration model (`MOD-immigration`): inputs, modules, reproduction, benchmarks and the card.

Run from anywhere: python3 models/tools/immigration/test_immigration.py
           python3 models/tools/immigration/test_immigration.py --write-card   # regenerate the card's two blocks

1. **Inputs:** the parameter files meet the toolkit's schema; every input traces to a register entry or is a
   labeled assumption with a range; the shapes sum as they should.
2. **Modules** behave as the dossier's design says (the first version's tests, kept).
3. **Reproduction:** the dossier's wrappers run this code; section 6's total is the path's; the committed
   `results.json` is what the code builds; no printout says "FYNone".
4. **Validation:** the benchmarks against CBO, CRS and DHS (and the labor module's), as
   `models/schema/validation.py` records with tolerances fixed here before the model figure is filled in; the
   card's table is the one this code renders.
5. **The card:** its evidence map is generated from the parameter files.
"""
import importlib.util
import json
import os
import re
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'models', 'schema'))
sys.path.insert(0, os.path.join(ROOT, 'models'))
import immigration_model as m  # noqa: E402
import immigration_path as p  # noqa: E402
import immigration_labor as lab  # noqa: E402
import immigration_run as run  # noqa: E402
import parameters as PS  # noqa: E402
import validation as V  # noqa: E402
import runlog  # noqa: E402

CARD = os.path.join(HERE, 'MODEL-CARD.md')
DOSSIER_TOOLS = os.path.join(ROOT, 'dossiers', 'immigration', 'tools')
VSTART, VEND = '<!-- generated:validation:start -->', '<!-- generated:validation:end -->'
PARAM_FILES = [(m.PARAMETERS, 'the model'), (m.PLAN, "the plan's commitments, held fixed across the scenarios"),
               (lab.PARAMETERS, 'the labor-market module (not booked)')]


def register_ids():
    ids = set()
    for dirpath, _, files in os.walk(os.path.join(ROOT, 'dossiers')):
        if 'evidence.json' in files:
            with open(os.path.join(dirpath, 'evidence.json'), encoding='utf-8') as f:
                ids |= {e['id'] for e in json.load(f)}
    return ids


def load_by_path(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------- 1. inputs
class Inputs(unittest.TestCase):
    def test_parameter_files_meet_the_schema(self):
        for f, _ in PARAM_FILES:
            self.assertEqual(PS.validate(PS.read(f)), [], f)

    def test_every_input_traces(self):
        known = register_ids()
        for name, (c, lo, hi, basis) in {**m.INPUTS, **lab.INPUTS}.items():
            cited = re.findall(r'EV-[A-Z]{2,4}-\d{3}', basis)
            labeled = basis.startswith(('assumption', 'legacy estimate', 'commitment'))
            catalogued = re.findall(r'SRC-\d{4}', basis) or 'https://' in basis
            self.assertTrue(cited or labeled or catalogued, f'{name}: no evidence ID, source ID, URL or label')
            for ev in cited:
                self.assertIn(ev, known, f'{name}: {ev} is not in a register')
            if lo is not None:
                self.assertTrue(lo <= c <= hi, f'{name}: central outside its range')
            if basis.startswith('assumption') and lo is not None and not isinstance(c, tuple):
                self.assertTrue(lo < hi, f'{name}: an assumption needs a range')

    def test_shapes(self):
        self.assertAlmostEqual(sum(m.INPUTS['filing_shape'][0]), 1.0, places=6)
        self.assertEqual(len(m.INPUTS['filing_shape'][0]), 9)
        self.assertEqual(sorted(m.STATUS_SHAPE), m.YEARS)
        self.assertEqual(m.FILING_OPENS, 2031)


# ---------------------------------------------------------------- 2. modules (the dossier's first tests, kept)
class Modules(unittest.TestCase):
    def test_uscis_volume_matches_memo_1(self):
        self.assertTrue(8.0 <= m.uscis()['filings_m'] <= 10.0)   # memo 7: 8-10 million filings

    def test_courts_need_more_judges_when_slower(self):
        slow, fast = m.eoir('low'), m.eoir('high')
        self.assertGreater(slow['judges_needed'], fast['judges_needed'])
        central = m.eoir()
        self.assertGreater(central['judges_added'], 300)
        self.assertLessEqual(central['cleared_fy'], 2035)
        self.assertTrue(central['cleared_at_800'] is None or central['cleared_at_800'] > 2035)
        self.assertGreater(central['cleared_slow_ramp'], central['cleared_fy'])

    def test_detention_near_zero(self):
        self.assertLess(abs(m.window(m.detention())), 10)

    def test_status_is_a_cost_bounded_by_section_3(self):
        self.assertTrue(0 < m.window(m.status_fiscal()) < 150)

    def test_status_splits_cbos_unified_score(self):
        # I1 A (DEC-2026-11-25-27): the general-fund line scales CBO's on-budget figure, Social Security's side its
        # off-budget one; the two add to CBO's unified $35.33 billion (EV-IMM-600, EV-IMM-669)
        v = m.val
        self.assertAlmostEqual(v('hr6_onbudget_deficit_bn') + v('hr6_offbudget_deficit_bn'), 35.33, places=6)
        self.assertLess(m.window(m.status_offbudget()), 0)          # a gain to the funds
        self.assertAlmostEqual(m.window(m.status_offbudget()) / v('hr6_offbudget_deficit_bn'),
                               m.window(m.status_fiscal()) / v('hr6_onbudget_deficit_bn')
                               / (1 - v('health_share') * v('covered_anyway_share')), places=6)

    def test_counsel_inside_memo_4(self):
        self.assertTrue(4 <= m.window(m.eoir()['counsel']) <= 14)

    def test_court_path_overrides_leave_the_plan_alone(self):
        self.assertEqual(m.court_path(1673), m.court_path(1673, start=2030, end=m.COURT_LAST_FY, plan=True))


# ---------------------------------------------------------------- 3. reproduction
class Reproduction(unittest.TestCase):
    def test_dossier_wrappers_run_this_code(self):
        wm = load_by_path('wrapped_model', os.path.join(DOSSIER_TOOLS, 'immigration_model.py'))
        self.assertEqual(os.path.realpath(wm.__file__), os.path.realpath(m.__file__))
        for c in run.SCENARIOS:
            self.assertEqual(wm.lines(c), m.lines(c))
        wrapper = open(os.path.join(DOSSIER_TOOLS, 'immigration_path.py'), encoding='utf-8').read()
        self.assertIn('models/tools/immigration/immigration_path.py', wrapper)
        self.assertLess(len(wrapper.splitlines()), 25, 'the dossier keeps a thin wrapper only')

    def test_section_6_reports_the_tool(self):
        spend, rev = p.lines(), p.revenue_lines()
        t = p.total({**spend, **rev})[0]
        window, y2040 = sum(t[y] for y in p.WINDOW), t[2040]
        text = open(os.path.join(ROOT, 'dossiers/immigration/6-cost.md'), encoding='utf-8').read()
        row = next(line for line in text.splitlines() if line.startswith('| **Immigration on the general fund, all**'))
        self.assertIn(f'**{window:.1f}**', row)
        self.assertIn(f'**{y2040:.1f}**', row)
        self.assertEqual((round(window, 1), round(y2040, 1)), (159.2, 24.6))   # 6-cost.md part 1, as booked (I1 A)

    def test_committed_results_are_what_the_code_builds(self):
        with open(os.path.join(HERE, 'results.json'), encoding='utf-8') as f:
            committed = json.load(f)
        built = runlog.stamp(run.build(), run.header(run.SCENARIOS))
        self.assertEqual(runlog.dumps(built), runlog.dumps(committed),
                         'results.json is stale: run python3 models/tools/immigration/immigration_run.py')

    def test_no_fy_none_in_the_printout(self):
        import contextlib, io
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            m.report()
        self.assertNotIn('FYNone', buf.getvalue())
        self.assertIn(f'at 800 judges: not by FY{m.COURT_LAST_FY}', buf.getvalue())


# ---------------------------------------------------------------- 4. validation
# Tolerances and their basis are fixed here, before the model figure is filled in. Default: a quarter of the target,
# the project's tolerance for a published figure the model did not calibrate to (as the health coverage model uses).
QUARTER = 'a quarter of the target: a published figure the model did not calibrate to'


def B(id, q, target, source, vintage, unit, tol, kind, basis, expl='', in_sample=False):
    return V.Benchmark(id, q, target, source, vintage, unit, tolerance=tol, tolerance_kind=kind, tolerance_basis=basis,
                       in_sample=in_sample, explanation=expl)


def validation_rows():
    v = m.val
    crs_grid = list(range(m.CRS_R47637['judges_now'], m.CRS_R47637['judges_now'] + 1001, 100))
    clears_by_2032 = min(j for j in crs_grid if (m.crs_replay(j) or 9999) <= 2032)
    green = (v('tier_b_m') + v('tier_a_outside_b_m')) * v('take_up')
    per_person = v('hr6_onbudget_deficit_bn') * v('reach_scale') / green  # $ thousand, 2021-31 dollars, on-budget
    hr6_own = v('hr6_onbudget_deficit_bn') * 1.0 * 1.0                    # reach 1, growth 1, no netting: H.R. 6 itself
    shape = sum(m.STATUS_SHAPE[y] for y in range(2030, 2036)) / sum(m.STATUS_SHAPE.values())
    custody_2027 = v('base_beds') * 365 * v('bed_day_usd_2023') * m.prices(2027, base=2023) / 1e9
    asylum_case = v('asylum_cost_per_case_usd') / 1.0
    ev = V.evaluate
    rows = [
        ev(B('BM-CRS-1', "Immigration judges needed to clear the court backlog by FY2032 on CRS's R47637 assumptions (court_path replaying CRS; smallest corps on CRS's 100-judge grid)",
             1349, 'EV-IMM-642; SRC-4089', 'CRS R47637, July 2023 (FY2023 Q2 data)', 'judges', 100, 'absolute',
             "CRS's grid steps 100 judges, so a model one step off still reads CRS's table; set before running"), clears_by_2032),
        ev(B('BM-CRS-2', "Years from FY2023 until the backlog is eliminated with 300 judges added (949 in all), on CRS's assumptions (CRS: FY2078)",
             55, 'EV-IMM-112; SRC-4089 (footnote 28)', 'CRS R47637, July 2023', 'years', 1, 'absolute',
             'one year: CRS starts inside FY2023 (Q2), which a whole-year model can place a year either way'), m.crs_replay(949) - 2023),
        ev(B('BM-DHS-1', "ICE Custody Operations for 41,500 beds in FY2027: the model's base account (41,500 beds at the FY2023 bed-day rate, grown)",
             3.7, 'EV-IMM-362; EV-IMM-628', "ICE (DHS) FY2027 request, April 2026 (second Trump administration); the bed-day rate from ICE's FY2025 justification", '$ billion',
             0.25, 'relative', QUARTER,
             "Passes about 15% low, as expected: the bed-day rate counts direct costs only (beds, guards, food, health care, facilities; EV-IMM-628), while Custody Operations also funds transport and other custody costs. The request is a second Trump administration figure, read with the skepticism DEC-2026-10-30-01 asks."),
         custody_2027),
        ev(B('BM-DHS-2', "Asylum officer cost of a merits case (DHS's $180 million for 75,000 cases a year)",
             2400, 'EV-IMM-302', 'DHS, asylum processing rule, March 2022 (Biden administration)', '$ per case', 0.05, 'relative',
             'the input is set from this figure, so it must match to rounding',
             "In-sample by construction: `asylum_cost_per_case_usd` is DHS's figure divided out. It checks the input's arithmetic, not the corps' cost; no independent check of DHS's estimate is in the register (EV-IMM-574, the legacy review, sits below it).",
             in_sample=True), asylum_case),
        ev(B('BM-CBO-1', "Status line on H.R. 6's own terms (reach 1, no growth, no single-plan netting): CBO's on-budget deficit increase over 2021-31",
             42.48, 'EV-IMM-669', "CBO, H.R. 6 (American Dream and Promise Act), 2021, on its February 2021 baseline", '$ billion', 0.001, 'relative',
             'an identity: the line is CBO\'s score scaled',
             "In-sample by construction: status_fiscal() scales this score, so the check covers the scaling's arithmetic only. The status line is not a microsimulation (Limits).",
             in_sample=True), hr6_own),
        ev(B('BM-CBO-2', "Share of the status line's FY2030-40 cost in its first six years, against CBO's share of H.R. 6's 2021-31 deficit in 2021-26",
             10115 / 35330, 'EV-IMM-600; EV-IMM-213', 'CBO, H.R. 6, 2021: $10,115 million of $35,330 million', 'share', 0.03, 'absolute',
             'three points: the yearly profile was drawn by hand from CBO\'s table',
             "In-sample by construction: STATUS_SHAPE was drawn from CBO's 2021 yearly figures, so this checks the drawing.",
             in_sample=True), shape),
        ev(B('BM-CBO-3', "Status cost per person granted a green card in the first decade, before the single plan's netting, 2021-31 dollars: against CBO's Farm Workforce Modernization Act (unified to on-budget, per person)",
             (4.719 / 0.5, 8.246 / 0.5), 'EV-IMM-215; EV-IMM-216', "CBO, H.R. 1603, 2021: +$4.7 billion unified and +$8.2 billion on-budget over 2021-31, for more than 300,000 workers and 200,000 dependents", '$ thousand per person',
             0.0, 'range', "CBO's unified and on-budget per-person figures bound the line, which carries CBO's on-budget score on the general fund (I1 A, DEC-2026-11-25-27)",
             "An independent check of `reach_scale`: memo 1's gross status cost per green card sits inside the band CBO's other 2021 legalization score implies. Weak: the farm bill's people reach green cards after 4-8 years in a temporary status (EV-IMM-523), so fewer benefits fall in its window, and 'more than' 500,000 people makes its per-person figures upper bounds."),
         per_person),
    ]
    return rows + lab.validation_rows(B, ev)


def validation_block():
    return VSTART + '\n' + V.render(validation_rows()) + '\n' + VEND


def parameters_block():
    parts = []
    for f, what in PARAM_FILES:
        parts.append(f'**`{os.path.basename(f)}`** ({what}). ' + PS.table(PS.read(f)))
    return PS.START + '\n' + '\n\n'.join(parts) + '\n' + PS.END


def write_card():
    s = open(CARD, encoding='utf-8').read()
    for start, end, block in ((VSTART, VEND, validation_block()), (PS.START, PS.END, parameters_block())):
        a, b = s.index(start), s.index(end) + len(end)
        s = s[:a] + block + s[b:]
    with open(CARD, 'w', encoding='utf-8') as f:
        f.write(s)


class Validation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = validation_rows()

    def test_table_has_no_problems(self):
        self.assertEqual(V.problems(self.rows), [])

    def test_every_named_publisher_has_a_benchmark(self):
        ids = {r.id.split('-')[1] for r in self.rows}
        self.assertTrue({'CBO', 'CRS', 'DHS'} <= ids)

    def test_crs_replay_matches_crs(self):
        self.assertEqual(m.crs_replay(1349), 2032)
        self.assertEqual(m.crs_replay(949), 2078)
        self.assertIsNone(m.crs_replay(849))      # CRS: under 300 added, the backlog grows

    def test_card_tables_are_the_ones_the_code_renders(self):
        s = open(CARD, encoding='utf-8').read()
        self.assertIn(validation_block(), s, 'the card\'s validation table is stale: run test_immigration.py --write-card')
        self.assertIn(parameters_block(), s, 'the card\'s evidence map is stale: run test_immigration.py --write-card')


# ---------------------------------------------------------------- 5. the labor-market module stays unbooked
class LaborModule(unittest.TestCase):
    def test_labor_results_are_not_in_any_booked_line(self):
        res = lab.results()
        self.assertIs(res['booked'], False)
        booked = {k for k in p.lines()} | {k for k in p.revenue_lines()}
        self.assertFalse(any('labor' in k.lower() for k in booked))

    def test_labor_module_reads_its_own_file(self):
        self.assertTrue(set(lab.INPUTS).isdisjoint(m.INPUTS))


if __name__ == '__main__':
    if '--write-card' in sys.argv:
        write_card()
        print('wrote the card\'s evidence map and validation table')
        sys.exit(0)
    unittest.main()
