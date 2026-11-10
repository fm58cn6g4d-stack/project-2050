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
import model as M  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

EXPECTED_MISSES = {
    'BM-1a': 'Both single-payer corners sit above CBO\'s 2020 range after it is grown to 2032 (low corner about $2.9 trillion against $1.7 to $3.3 trillion). '
             'The plan carries 79 to 82 percent of national spending, close to the federal share CBO\'s range implies, so the gap is in scale: the model\'s '
             'national spending base is CMS\'s projection ($8.3 trillion in 2032) and the register does not give CBO\'s option specifications or its 2020 baseline.',
    'BM-1b': 'The low corner is about $0.56 trillion below baseline against CBO\'s scaled -$0.78 trillion (just outside 25 percent); the high corner is about '
             '+$0.6 trillion against +$0.33 trillion because it includes long-term care ($0.2 trillion), the newly covered (about $0.28 trillion) and added use. '
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
            self.assertTrue(r['evidence_id_or_basis'].strip(), f'{k} has no evidence ID or basis')
            self.assertLessEqual(r['low'], r['value'] + 1e-12, k)
            self.assertGreaterEqual(r['high'], r['value'] - 1e-12, k)
            if r['kind'] == 'assumption':
                self.assertTrue(r['low'] < r['high'] or k.startswith('overlap_w_') or k in ('ap_enh_b1', 'ap_enh_b4'), f'assumption {k} needs a tested range')

    def test_evidence_ids_resolve_and_evidence_inputs_cite_one(self):
        for k, r in self.rows.items():
            ids = re.findall(r'EV-CAR-\d{3}', r['evidence_id_or_basis'])
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


if __name__ == '__main__':
    unittest.main(verbosity=1)
