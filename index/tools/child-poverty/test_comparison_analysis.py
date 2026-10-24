"""Meaningful alternative/later-year boundaries, using artificial units only."""
import copy
import json
import unittest
from comparison_analysis import (annual_analogue, alternative_increment,
    apply_overlays, carry_forward, analyze, evaluate, HERE)
from test_agenda_analysis import sample
from cps_projection import read_inputs


class ComparisonTests(unittest.TestCase):
    def test_source_schedule_and_newborn_sensitivity(self):
        self.assertEqual(annual_analogue([0,4,8],0,'head'),6360+4320+3600)
        self.assertEqual(annual_analogue([0],0,'head',newborn=False),4320)

    def test_first_phase_down_and_second_phase_out(self):
        self.assertAlmostEqual(annual_analogue([8],132500,'head'),2600)
        self.assertAlmostEqual(annual_analogue([8],300000,'head'),2000.04)
        self.assertEqual(annual_analogue([8],400000,'head'),0)

    def test_phaseout_never_increases_award(self):
        amounts=[annual_analogue([0,3,9],x,'joint') for x in range(0,1000001,10000)]
        self.assertEqual(amounts,sorted(amounts,reverse=True))

    def test_invalid_age_status_factor(self):
        for ages,filing,factor in [([18],'head',1),([True],'head',1),([4],'separate',1),([4],'joint',0)]:
            with self.assertRaises(ValueError):annual_analogue(ages,0,filing,factor)

    def test_signed_alternative_does_not_erase_credit_loss(self):
        t=dict(child_ages=[8],agi=500000,filing='joint',nonrefundable=2200,refundable=0)
        self.assertEqual(alternative_increment(t,1,'AFA_2025_real',1),-2200)

    def test_index_anchor_branches(self):
        t=dict(child_ages=[8],agi=0,filing='head',nonrefundable=0,refundable=0)
        self.assertGreater(alternative_increment(t,1.2,'AFA_2025_real',1.1),
                           alternative_increment(t,1.2,'FAM-1D_2030_face',1.1))

    def test_overlay_requires_reconciliation_and_no_double_entry(self):
        p={'u':dict(cost=0,source_moop=100)}
        row=dict(unit_id='u',component='health_moop_saving',delta_2025_dollars=50,
                 review='illustrative test',baseline_reconciled=True)
        apply_overlays(p,[row]);self.assertEqual(p['u']['cost'],50)
        for rows in ([row,row],[dict(row,delta_2025_dollars=101)],
                     [dict(row,baseline_reconciled=False)],[dict(row,component='construction_cash')]):
            with self.assertRaises(ValueError):apply_overlays(copy.deepcopy(p),rows)

    def test_finite_overlay_and_unknown_unit(self):
        row=dict(unit_id='u',component='net_tax_transfer_earnings',delta_2025_dollars=float('nan'),review='x',baseline_reconciled=True)
        with self.assertRaises(ValueError):apply_overlays({'u':dict(cost=0,source_moop=0)},[row])
        with self.assertRaises(ValueError):apply_overlays({},[dict(row,delta_2025_dollars=1)])

    def test_later_year_labels_do_not_invent_population_or_growth(self):
        stored=json.loads((HERE/'empirical/agenda-results.json').read_text())
        rows=carry_forward(stored)
        self.assertEqual(len(rows),12)
        for name in ('moderate','enhanced','full','stressed'):
            subset=[r for r in rows if r['scenario']==name]
            self.assertEqual({r['year'] for r in subset},{2034,2040,2050})
            self.assertEqual(len({r['poor_rate'] for r in subset}),1)
            self.assertEqual(len({r['poor_children'] for r in subset}),1)

    def test_path_requires_named_review_and_supported_year(self):
        for paths in ([dict(year=2090,delivery='moderate',resource_shift=0,review='x')],
                      [dict(year=2040,delivery='moderate',resource_shift=float('nan'),review='x')],
                      [dict(year=2040,delivery='moderate',resource_shift=0)]):
            with self.assertRaises(ValueError):analyze(paths=paths)

    def test_no_archive_no_fabricated_national_alternative(self):
        r=analyze()
        self.assertIsNone(r['national_cases'])
        self.assertEqual(r['status'],'NATIONAL_ALTERNATIVES_NOT_RUN')

    def test_awards_saturate_without_assigning_average_housing_cash(self):
        pop,econ,_=read_inputs(HERE/'empirical')
        spec=json.loads((HERE/'agenda-assumptions.json').read_text())
        d=sample()
        zero=evaluate(d,spec,pop,econ,'FAM-1A','full',0)
        full=evaluate(d,spec,pop,econ,'FAM-1A','full',100000000)
        self.assertEqual(zero['expected_awards'],0)
        self.assertEqual(full['expected_awards'],10000000)
        self.assertLessEqual(full['result']['poor_rate'],zero['result']['poor_rate'])
        self.assertIsNone(full['federal_cost'])

    def test_joint_alternative_and_delivery_runs_on_supplied_microdata(self):
        pop,econ,_=read_inputs(HERE/'empirical')
        spec=json.loads((HERE/'agenda-assumptions.json').read_text())
        r=evaluate(sample(),spec,pop,econ,'AFA_2025_real','enhanced',1000000)
        self.assertTrue(0 <= r['result']['poor_rate'] <= 1)
        self.assertEqual(r['award_cap'],1000000)
        self.assertAlmostEqual(r['expected_leases'],850000)


if __name__=='__main__':unittest.main()
