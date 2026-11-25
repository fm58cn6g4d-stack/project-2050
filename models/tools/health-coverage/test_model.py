#!/usr/bin/env python3
"""Tests for the health coverage model: input traceability, accounting identities, boundary cases, benchmarks.

  python3 models/tools/health-coverage/test_model.py

Benchmark misses are reported in the model card and results.md, not tuned away. A known miss is listed in
EXPECTED_MISSES with its explanation; the test fails if an unlisted benchmark misses, and also if a listed
miss starts to pass (so the list does not go stale).
"""
import json
import os
import re
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '..', 'schema'))
import model as M  # noqa: E402
import validation as V  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

EXPECTED_MISSES = {
    'BM-1a': 'The high corner (about $4.4 trillion) is 31 percent above the top of CBO\'s range grown to 2032 ($3.3 trillion); the low corner (about $3.0 trillion) is inside it. '
             'The plan carries 79 to 82 percent of national spending, close to the federal share CBO\'s range implies, so the gap is in scale: the model\'s '
             'national spending base is CMS\'s projection ($8.3 trillion in 2032) and the register does not give CBO\'s option specifications or its 2020 baseline.',
    'BM-1b': 'The high corner is about +$0.6 trillion against CBO\'s scaled +$0.33 trillion because it includes long-term care ($0.2 trillion), the newly covered '
             '(about $0.5 trillion, paid in full by the plan) and added use; the low corner (about -$0.55 trillion) is inside CBO\'s scaled range (-$0.78 to +$0.33 trillion). '
             'The register does not say which of CBO\'s five options include long-term care or how much cost sharing each has.',
    'BM-3b': 'The model prices 3.7 million new enrollees, repricing of about 12 million existing enrollees and the end of the 400 percent cliff, about 65 billion in 2032 '
             'against 37.5 billion; CBO\'s $350 billion also nets a premium reduction from a healthier pool and offsets from employer coverage, which the model leaves out.',
}


def load_all():
    rows = M.load_inputs()
    scn, order = M.load_scenarios()
    return rows, scn, order


class InputTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.scn, cls.order = load_all()
        with open(os.path.join(ROOT, 'dossiers/care/evidence.json')) as f:
            cls.ev = {e['id'] for e in json.load(f)}

    def test_kind_and_range(self):
        for k, r in self.rows.items():
            self.assertIn(r['kind'], ('evidence', 'assumption'), k)
            self.assertTrue(r['source'].strip(), f'{k} has no evidence ID or basis')
            self.assertLessEqual(r['low'], r['value'] + 1e-12, k)
            self.assertGreaterEqual(r['high'], r['value'] - 1e-12, k)
            if r['kind'] == 'assumption':
                self.assertTrue(r['low'] < r['high'] or k.startswith('overlap_w_') or k in ('ap_enh_b1', 'ap_enh_b4'), f'assumption {k} needs a tested range')

    def test_evidence_ids_resolve_and_evidence_inputs_cite_one(self):
        for k, r in self.rows.items():
            ids = re.findall(r'EV-CAR-\d{3}', r['source'])
            for i in ids:
                self.assertIn(i, self.ev, f'{k}: {i}')
            if r['kind'] == 'evidence':
                self.assertTrue(ids, f'{k}: evidence input must cite an EV ID')

    def test_every_scenario_override_is_known(self):
        for name, p in self.scn.items():
            if name == '_phase':
                continue
            for k in p:
                self.assertTrue(k.startswith('_') or k in self.rows or k in KNOWN_SWITCHES, f'{name}: unknown parameter {k}')


KNOWN_SWITCHES = {'restore', 'restore_medicaid', 'restore_marketplace', 'restore_credits', 'po', 'po_richer', 'po_takeup_scale', 'po_autoenroll',
                  'm60', 'm50', 'kids', 'medicare_takeup_scale', 'sp', 'sp_rate_basis', 'sp_rate_factor', 'sp_cs', 'sp_ltc', 'sp_ma_to_ffs'}


class AccountingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.scn, cls.order = load_all()
        cls.res = {n: M.evaluate(cls.rows, cls.scn, n) for n in cls.order if not n.startswith('_')}
        cls.I = M.central(cls.rows)
        cls.base = cls.res['baseline_2029']

    def test_population_sums_to_total_in_every_scenario(self):
        for n, r in self.res.items():
            self.assertAlmostEqual(sum(r['people'].values()), self.I['cbo_pop'], places=6, msg=n)
            for b in range(4):
                band0 = sum(v[b] for v in self.base['cells'].values())
                self.assertAlmostEqual(sum(v[b] for v in r['cells'].values()), band0, places=6, msg=f'{n} band {b}')

    def test_no_negative_cells(self):
        for n, r in self.res.items():
            for s, v in r['cells'].items():
                for b, x in enumerate(v):
                    self.assertGreaterEqual(x, -1e-9, f'{n} {s} band {b}')

    def test_baseline_reproduces_cbo(self):
        I = self.I
        self.assertAlmostEqual(self.base['uninsured'], I['cbo_unins'], places=6)
        self.assertAlmostEqual(self.base['federal']['total_subsidies_bn'], I['net_sub_2032'], places=6)
        self.assertAlmostEqual(self.base['federal']['net_change_bn'], 0, places=9)
        B = M.build_base(I)
        gross = B['gross']
        # people with two sources are netted out once: sources plus uninsured sum to the population (tested above) and the
        # amount removed is CBO's 19.6 million plus rounding in its table
        self.assertLess(abs(B['overlap'] - I['cbo_multi']), 0.2)
        for s_ in ['esi', 'medicaid', 'medicare', 'other']:
            self.assertLessEqual(B['net'][s_], B['gross'][s_])

    def test_federal_cost_is_sum_of_components(self):
        for n, r in self.res.items():
            f = r['federal']
            self.assertAlmostEqual(sum(f['delta_components_bn'].values()), f['net_change_bn'], places=6, msg=n)
            self.assertAlmostEqual(f['gross_new_bn'] - f['offsets_bn'], f['net_change_bn'], places=6, msg=n)
            self.assertAlmostEqual(f['total_subsidies_bn'] - self.base['federal']['total_subsidies_bn'], f['net_change_bn'], places=6, msg=n)
            self.assertGreaterEqual(f['gross_new_bn'], -1e-9)
            self.assertGreaterEqual(f['offsets_bn'], -1e-9)

    def test_household_totals_add_up(self):
        for n, r in self.res.items():
            h = r['household']
            self.assertAlmostEqual(sum(b['premiums_bn'] + b['oop_bn'] for b in h['by_band']), h['total_bn'], places=6, msg=n)
            self.assertAlmostEqual(sum(b['people'] for b in h['by_band']), self.I['cbo_pop'], places=6, msg=n)

    def test_scenario_chain_is_ordered(self):
        r = self.res
        self.assertLess(r['restore']['uninsured'], r['baseline_2029']['uninsured'])
        self.assertLess(r['public_option']['uninsured'], r['restore']['uninsured'])
        self.assertLessEqual(r['staged']['uninsured'], r['public_option']['uninsured'])
        self.assertLessEqual(r['staged_full']['uninsured'], r['staged']['uninsured'])
        self.assertLessEqual(r['staged_full_kids']['uninsured'], r['staged_full']['uninsured'])


class BoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.scn, cls.order = load_all()
        cls.I = M.central(cls.rows)
        cls.B = M.build_base(cls.I)
        cls.base = M.run(cls.I, {}, cls.B)

    def test_zero_take_up_gives_baseline(self):
        P = {'po': 1, 'po_takeup_scale': 0.0, 'm60': 1, 'm50': 1, 'kids': 1, 'medicare_takeup_scale': 0.0}
        r = M.run(self.I, P, self.B)
        self.assertEqual(r['cells'], self.base['cells'])
        self.assertAlmostEqual(r['federal']['net_change_bn'], 0.0, places=9)
        self.assertAlmostEqual(r['nhe_change_bn'], 0.0, places=9)
        self.assertAlmostEqual(r['household']['total_bn'], self.base['household']['total_bn'], places=6)

    def test_restore_with_no_coverage_effects_and_no_credits_gives_baseline(self):
        I = dict(self.I, law_mcd_unins_2034=0.0, mkt_insured_2030=0.0, mkt_insured_2035=0.0)
        r = M.run(I, {'restore_medicaid': 1, 'restore_marketplace': 1}, M.build_base(I))
        self.assertEqual(r['uninsured'], self.base['uninsured'])
        self.assertAlmostEqual(r['federal']['net_change_bn'], I['mcd_financing_restore'], places=9)

    def test_single_payer_leaves_only_the_residual_uninsured(self):
        P = {'sp': 1}
        r = M.run(self.I, P, self.B)
        self.assertAlmostEqual(r['uninsured'], self.I['sp_residual_unins'] * self.I['cbo_pop'], places=9)
        r0 = M.run(dict(self.I, sp_residual_unins=0.0), P, M.build_base(dict(self.I, sp_residual_unins=0.0)))
        self.assertAlmostEqual(r0['uninsured'], 0.0, places=9)
        for s in ['esi', 'ng_sub', 'ng_unsub', 'medicaid', 'medicare', 'po']:
            self.assertEqual(sum(r['cells'][s]), 0.0)
        self.assertEqual(r['cells']['other'], self.base['cells']['other'])  # held fixed

    def test_single_payer_federal_cost_ignores_how_uninsured_care_was_paid(self):
        # Codex review of #201: the share of uninsured care paid out of pocket changes national spending only
        P = {'sp': 1}
        nets = []
        for v in (0.2, 0.5):
            I = dict(self.I, unins_paid_share=v)
            nets.append(M.run(I, P, M.build_base(I))['federal']['net_change_bn'])
        self.assertAlmostEqual(nets[0], nets[1], places=6)

    def test_age_window_movers_compare_like_with_like(self):
        # Codex review of #201: with equal prices and administration, an employer-covered 60-64-year-old who moves
        # to Medicare changes national spending only by the difference in out-of-pocket spending
        I = dict(self.I, hosp_commercial_ratio=1.0, phys_commercial_ratio=1.0, admin_medicare=self.I['admin_phi'],
                 win_unins_m60=0.0, win_ng_m60=0.0)
        B = M.build_base(I)
        r = M.run(I, {'m60': 1}, B)
        moved = sum(r['cells']['medicare_m60'])
        self.assertGreater(moved, 0)
        per = r['nhe_change_bn'] * 1000 / moved
        self.assertAlmostEqual(per, B['oop_pp']['medicare'] - B['oop_pp']['esi'], places=6)

    def test_single_payer_identities(self):
        r = M.run(self.I, {'sp': 1, 'sp_cs': 'low', 'sp_ltc': 1}, self.B)
        s = r['single_payer']
        self.assertAlmostEqual(s['plan_outlay_bn'], s['plan_gross_bn'] - s['cost_sharing_bn'], places=9)
        self.assertAlmostEqual(s['plan_gross_bn'], s['provider_revenue_bn'] + s['admin_bn'], places=9)
        self.assertAlmostEqual(r['federal']['net_change_bn'], s['amount_to_be_financed_bn'], places=9)
        self.assertAlmostEqual(r['federal']['net_change_bn'], s['plan_outlay_bn'] - s['state_and_retained_bn'] - 3070, places=6)
        sp = r['household']['by_source']['sp']
        self.assertAlmostEqual(sp['people'] * sp['oop_pp'] / 1000, s['cost_sharing_bn'], places=6)  # patients pay the plan's cost sharing
        self.assertEqual(sp['premium_pp'], 0.0)

    def test_directions(self):
        def fed(over=None, P=None, base_I=None):
            I = dict(self.I, **(over or {}))
            return M.run(I, P or {}, M.build_base(I))['federal']['net_change_bn']
        sp = {'sp': 1}
        self.assertLess(fed({'sp_drug_cut': 0.25}, sp), fed({'sp_drug_cut': 0.05}, sp))
        self.assertLess(fed({'sp_rate_pct_medicare': 1.0}, sp), fed({'sp_rate_pct_medicare': 1.4}, sp))
        self.assertLess(fed({'sp_state_moe': 0.8}, sp), fed({'sp_state_moe': 0.0}, sp))
        self.assertLess(fed({}, {'sp': 1, 'sp_cs': 'low'}), fed({}, {'sp': 1, 'sp_cs': 'none'}))
        self.assertLess(fed({}, {'sp': 1, 'sp_ltc': 0}), fed({}, {'sp': 1, 'sp_ltc': 1}))
        po = {'restore': 1, 'po': 1}
        self.assertLess(fed({'po_rate_pct_medicare': 1.2}, po), fed({'po_rate_pct_medicare': 2.0}, po))
        self.assertLess(fed({'po_autoenroll_takeup': 0.5}, po), fed({'po_autoenroll_takeup': 0.9}, po))

    def test_restore_costs_more_with_richer_subsidies(self):
        a = M.run(self.I, {'restore': 1, 'po': 1}, self.B)['federal']['net_change_bn']
        b = M.run(self.I, {'restore': 1, 'po': 1, 'po_richer': 1}, self.B)['federal']['net_change_bn']
        self.assertGreater(b, a)


class WindowTests(unittest.TestCase):
    def test_phase_and_growth(self):
        rows, scn, order = load_all()
        ph = M.phases(scn)
        self.assertEqual(M.phase_at(ph, 'restore', 2029), 0.0)
        self.assertEqual(M.phase_at(ph, 'restore', 2032), 1.0)
        self.assertAlmostEqual(M.phase_at(ph, 'sp', 2032), 0.25)
        I = M.central(rows)
        gf, gn, cagr = M.growth_paths(I)
        self.assertEqual(gf[2032], 1.0)
        self.assertAlmostEqual(gf[2036], I['net_sub_2036'] / I['net_sub_2032'])
        self.assertAlmostEqual(gf[2037], gf[2036] * (1 + cagr))

    def test_window_totals_match_series_and_mature_year(self):
        out = M.build_all()
        for n, f in out['fy2030_39'].items():
            self.assertAlmostEqual(sum(r['federal_bn'] for r in f['series']), f['total_2030_39']['federal_bn'], places=6, msg=n)
        y2032 = {r['year']: r for r in out['fy2030_39']['restore']['series']}[2032]
        self.assertAlmostEqual(y2032['federal_bn'], out['results']['restore']['federal']['net_change_bn'], places=6)
        y2032 = {r['year']: r for r in out['fy2030_39']['staged']['series']}[2032]
        self.assertAlmostEqual(y2032['federal_bn'], out['results']['staged']['federal']['net_change_bn'], places=6)
        # staged_full adds Medicare at 50 only from 2035
        a = {r['year']: r['federal_bn'] for r in out['fy2030_39']['staged']['series']}
        b = {r['year']: r['federal_bn'] for r in out['fy2030_39']['staged_full']['series']}
        for t in range(2030, 2035):
            self.assertAlmostEqual(a[t], b[t], places=6)
        self.assertNotAlmostEqual(a[2037], b[2037], places=3)
        # the path to single payer ends on single payer
        p = out['staged_path_to_single_payer']
        self.assertEqual(p[0]['weight_single_payer'], 0.0)
        self.assertGreater(p[-1]['weight_single_payer'], 0.85)

    def test_deterministic(self):
        a = json.dumps(M.r3(M.build_all()), sort_keys=True)
        b = json.dumps(M.r3(M.build_all()), sort_keys=True)
        self.assertEqual(a, b)


class UncertaintyTests(unittest.TestCase):
    def test_ranges_and_tornado(self):
        out = M.build_all()
        for n, u in out['uncertainty'].items():
            self.assertLessEqual(len(u['tornado']), 5)
            sw = [t['swing'] for t in u['tornado']]
            self.assertEqual(sw, sorted(sw, reverse=True), n)
            c = u['corners']
            self.assertLessEqual(c['cost_min']['fed'], u['central']['fed'] + 1e-6, n)
            self.assertGreaterEqual(c['cost_max']['fed'], u['central']['fed'] - 1e-6, n)


class BenchmarkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bm = M.build_all()['benchmarks']

    def test_benchmarks_present(self):
        ids = {b['id'] for b in self.bm}
        for i in ['BM-1a', 'BM-1b', 'BM-2', 'BM-3a', 'BM-3b', 'BM-4', 'BM-5', 'BM-6a', 'BM-6b']:
            self.assertIn(i, ids)

    def test_misses_are_exactly_the_expected_ones(self):
        missed = {b['id'] for b in self.bm if not b['pass']}
        self.assertEqual(missed, set(EXPECTED_MISSES), 'a benchmark result changed: update the model card and EXPECTED_MISSES, do not tune the model')
        for k, why in EXPECTED_MISSES.items():
            self.assertGreater(len(why), 60, k)
        for b in self.bm:
            if not b['pass']:
                print(f"  benchmark miss (expected): {b['id']} model {b['model']} vs {b['target']}")


# ---------------------------------------------------------------- the validation table (models/schema/validation.py)
# Targets, tolerances and their basis are fixed here, before the model figure is filled in. The tolerance for every
# benchmark is 25 percent of the target (of the nearer end for a range): the model is a cell model built from CBO's
# own estimates, and the project's tolerance for a published figure it did not calibrate to is a quarter of it.
CARD = os.path.join(HERE, 'MODEL-CARD.md')
VSTART, VEND = '<!-- generated:validation:start -->', '<!-- generated:validation:end -->'
BASIS = 'a quarter of the target: a cell model fed by CBO estimates, not a microsimulation'


def validation_rows():
    """Every benchmark with the model's figure: the same quantities model.py's benchmarks() tests, as numbers."""
    rows = M.load_inputs()
    I = M.central(rows)
    scn, order = M.load_scenarios()
    out = M.build_all(rows)
    R = out['results']
    gf, gn, _ = M.growth_paths(I)
    sub_scale = I['net_sub_2032'] / I['net_sub_2030']
    nhe_scale = gn[2032] / gn[2030]
    lo, hi = R['single_payer_cbo_like_low'], R['single_payer_cbo_like_high']
    fed_rng = (1500 * sub_scale, 3000 * sub_scale)
    nhe_rng = (-700 * nhe_scale, 300 * nhe_scale)

    def worst(vals, rng):  # the corner furthest outside the range (or, if both are inside, the nearer to an end)
        dist = lambda x: max(rng[0] - x, x - rng[1], -min(x - rng[0], rng[1] - x))
        return max(vals, key=dist)
    def B(id, q, target, source, vintage, unit, expl, in_sample=False):
        return V.Benchmark(id, q, target, source, vintage, unit, tolerance=0.25, tolerance_kind='relative', tolerance_basis=BASIS,
                           in_sample=in_sample, explanation=expl)
    law, cr = R['bench_law_only'], R['bench_credits_only']
    cost_t = I['credits_cost_10yr'] / 10 * I['ptc_sub_2032'] / (sum(I[f'ptc_sub_{y}'] for y in range(2026, 2036)) / 10)
    mcd_t = I['law_mcd_outlays_10yr'] / 10 * I['mcd_sub_2032'] / (sum(I[f'mcd_sub_{y}'] for y in range(2025, 2035)) / 10)
    comp = law['federal']['delta_components_bn']
    mcd_m = comp.get('Medicaid and CHIP, restored adults', 0) + comp.get('Medicaid financing restored (provider taxes, directed payments)', 0)
    enroll = sum(f['millions'] for f in R['bench_medicare60_only']['flows'])
    denom = I['sub_medicare'] + I['sub_medicaid'] + I['sub_ptc']
    spc = R['single_payer_project_central']['federal']['net_change_bn'] / denom
    popt = R['public_option']['federal']['net_change_bn'] / denom
    ev = lambda b, m: V.evaluate(b, m)
    return [
        ev(B('BM-1a', 'CBO 2020 single-payer options: change in federal subsidies, 2032, $B (the model corner furthest from the range; both corners are in results.md)',
             fed_rng, 'EV-CAR-218; EV-CAR-052', 'CBO 2020, $1.5-3.0 trillion in 2030, grown to 2032 at CBO subsidy growth', '$ billion',
             EXPECTED_MISSES['BM-1a']), worst([lo['federal']['net_change_bn'], hi['federal']['net_change_bn']], fed_rng)),
        ev(B('BM-1b', 'CBO 2020 single-payer options: change in national health expenditures, 2032, $B (the model corner furthest from the range)',
             nhe_rng, 'EV-CAR-218; EV-CAR-120', 'CBO 2020, -$0.7 to +$0.3 trillion in 2030, grown at NHE growth', '$ billion',
             EXPECTED_MISSES['BM-1b']), worst([lo['nhe_change_bn'], hi['nhe_change_bn']], nhe_rng)),
        ev(B('BM-2', 'P.L. 119-21: fewer uninsured when its coverage provisions are restored, 2032, millions',
             10.0, 'EV-CAR-038; EV-CAR-025; EV-CAR-049', 'CBO, about 10 million more uninsured in 2034 (9.4 million on the 2029-34 path interpolated to 2032)', 'million people',
             'In-sample by construction: the restore flows are set from these same CBO estimates (7.5 million Medicaid, 2.8-2.9 million marketplace). The check covers the phase-in and band arithmetic, not an independent estimate.',
             in_sample=True), -law['uninsured_change']),
        ev(B('BM-3a', 'Enhanced credits made permanent: more insured, 2032, millions',
             3.7, 'EV-CAR-029', 'CBO, 3.6 million (2030) and 3.8 million (2035), interpolated', 'million people',
             'In-sample by construction (the flow is set from CBO).', in_sample=True), -cr['uninsured_change']),
        ev(B('BM-3b', 'Enhanced credits made permanent: 2032 federal cost, $B, against the ten-year average shaped by CBO premium-credit growth',
             cost_t, 'EV-CAR-029; EV-CAR-052', 'CBO, about $350 billion over 2026-35', '$ billion',
             EXPECTED_MISSES['BM-3b']), cr['federal']['net_change_bn']),
        ev(B('BM-4', 'P.L. 119-21 Medicaid provisions: federal outlays the restore reverses, 2032, $B',
             mcd_t, 'EV-CAR-025; EV-CAR-052', 'CBO, $989.7 billion over FY2025-34, spread on CBO Medicaid growth', '$ billion',
             'Passes on the coverage-linked cost alone; CBO also counts provider-tax and state-directed-payment cuts, which the model leaves at zero in the central case (`mcd_financing_restore`).'), mcd_m),
        ev(B('BM-5', 'CBO Medicare at 60: people who move to Medicare, 2032, millions',
             7.3, 'EV-CAR-207; EV-CAR-208', 'CBO 2022 as cited in legacy/sources/health-working-group-memo-analysis.md, line 420; UNVERIFIED (the saved CBO text, SRC-3204, gives shares, not this count)', 'million people',
             'The target is unverified, so the pass is weak. The model counts uninsured, nongroup and ESI people who move; it does not count people who add Part A while keeping employer coverage.'), enroll),
        ev(B('BM-6a', 'Urban 2019 single-payer: rise in federal spending, share of current federal health spending (project central)',
             (1.5 / 1.090, 2.8 / 1.090), 'EV-CAR-222; EV-CAR-224; EV-CAR-229', 'Urban 2019, $1.5-2.8 trillion in 2020 on RAND\'s $1,090 billion 2019 federal base', 'share',
             'Secondary and indicative: Urban\'s baseline is not in the register, so RAND\'s federal base stands in; the model also counts the tax exclusion.'), spc),
        ev(B('BM-6b', 'Urban 2019 hybrid reform with a public option: federal cost, share of current federal health spending (restore plus public option)',
             0.1221 / 1.090, 'EV-CAR-225; EV-CAR-229', 'Urban 2019, $122.1 billion in 2020 on $1,090 billion', 'share',
             'Secondary: Urban\'s bundle adds a mandate and rate caps and covers fewer people than restore plus public option; not a like-for-like test.'), popt),
    ]


def validation_block():
    return VSTART + '\n' + V.render(validation_rows()) + '\n' + VEND


class ValidationTableTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = validation_rows()

    def test_table_has_no_problems(self):
        self.assertEqual(V.problems(self.rows), [])

    def test_pass_and_miss_agree_with_model_py(self):
        mine = {r.id: r.passed for r in self.rows}
        theirs = {b['id']: b['pass'] for b in M.build_all()['benchmarks']}
        self.assertEqual(mine, theirs, 'the test code and model.py disagree about a benchmark')

    def test_the_three_misses_stay_in_the_table(self):
        self.assertEqual({r.id for r in self.rows if not r.passed}, {'BM-1a', 'BM-1b', 'BM-3b'})

    def test_card_table_is_the_one_the_code_renders(self):
        s = open(CARD, encoding='utf-8').read()
        self.assertIn(validation_block(), s, 'the card\'s validation table is stale: run python3 test_model.py --write-validation')


# ---------------------------------------------------------------- inputs without a register source
USTART, UEND = '<!-- generated:untraced:start -->', '<!-- generated:untraced:end -->'


def untraced_block():
    """The assumptions, in three groups by how far the evidence reaches: none, direction or analogy only, or a named gap."""
    import re as _re
    rows = [r for r in M.load_inputs().values() if r['kind'] == 'assumption']
    def group(r):
        if 'evidence still needed' in r['source']:
            return 'c'
        return 'b' if _re.search(r'\b(EV|SRC)-', r['source']) else 'a'
    names = {'a': 'Judgment with no register source', 'b': 'Judgment informed by a register entry (direction or analogy, not a measurement)',
             'c': 'Judgment with a named evidence gap (the source that would replace it)'}
    L = [f'{len(rows)} of the {len(M.load_inputs())} inputs are assumptions, each run across its low-high range in the uncertainty block of `results.json`. '
         'None is traced to a measured figure. By how far the evidence reaches:', '']
    for g in 'cba':
        part = [r for r in rows if group(r) == g]
        L += [f'**{names[g]}: {len(part)}**', '', '| Input | Value (low to high) | Basis |', '| --- | --- | --- |']
        for r in part:
            L.append(f"| `{r['id']}` | {r['value']:g} ({r['low']:g} to {r['high']:g}) | {r['source'].replace('|', '/')} |")
        L.append('')
    return USTART + '\n' + '\n'.join(L).rstrip() + '\n' + UEND


def write_validation():
    s = open(CARD, encoding='utf-8').read()
    for st, en, blk in ((VSTART, VEND, validation_block()), (USTART, UEND, untraced_block())):
        a, b = s.index(st), s.index(en) + len(en)
        s = s[:a] + blk + s[b:]
    open(CARD, 'w', encoding='utf-8').write(s)


class CardTests(unittest.TestCase):
    def test_untraced_list_is_current(self):
        self.assertIn(untraced_block(), open(CARD, encoding='utf-8').read(), 'the card\'s untraced-inputs list is stale: run python3 test_model.py --write-validation')


if __name__ == '__main__':
    if '--write-validation' in sys.argv:
        write_validation()
        print('wrote the validation table and the untraced-inputs list into MODEL-CARD.md')
    else:
        unittest.main(verbosity=1)
