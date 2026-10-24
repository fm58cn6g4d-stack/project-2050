"""Agenda experiment tests: nonlinear receipt, scarce awards and boundaries."""
import copy
import json
import unittest
from pathlib import Path
from array import array
from fixtures import unit
from model import credit_for_ages, credit_amount
from agenda_analysis import (binary, coupled_access, concentrate_coverage, expected_metrics, tax_increment,
    prepare_units, policy_parameters, unit_effect, aggregate, validate_assumptions,
    weighted_quantile, fpg, HERE)
from cps_projection import read_inputs, COMPONENTS


def sample():
    people = {'a':dict(age=35), 'b':dict(age=4), 'c':dict(age=8), 'd':dict(age=45)}
    units = {}
    for uid,members,hh in [('u',['a','b','c'],'h'),('v',['d'],'j')]:
        u = dict.fromkeys(COMPONENTS,0.)
        u.update(uid=uid,hh=hh,members=members,child_ids=['b','c'] if uid=='u' else [],
            SPM_TOTVAL=8000.,SPM_RESOURCES=5000.,SPM_POVTHRESHOLD=10000.,
            SPM_SCHLUNCH=861.,SPM_MEDXPNS=1000.,care=2000.,work=1000.,deduction=1500.,
            wages=10000.,earnings=10000.,weight=2.,hispanic=False,race=1)
        units[uid] = u
    households = dict(h=dict(state='01',members=3,cash=8000.,weight=2e6,renter=True,
                            summer_reported=False,units={'u'},quintile=0),
                      j=dict(state='01',members=1,cash=0.,weight=8e6,renter=True,
                            summer_reported=False,units={'v'},quintile=0))
    children=[]
    for p in ('b','c'):
        people[p].update(pid=p,uid='u',hh='h',weight=1.,reps=array('d',[1.]*160),sex='male',dependent=1)
        children.append(people[p])
    tax = dict(child_ages=[4,8],agi=8000.,filing='head',nonrefundable=0.,refundable=1000.,adult_dependents=0)
    return dict(units=units,child_units={'u':units['u']},households=households,people=people,
                taxes_by_unit={'u':[tax]},smi={'01':60000.},lunch=861.,children=children)


class AgendaAnalysisTests(unittest.TestCase):
    def setUp(self):
        self.spec=json.loads((HERE/'agenda-assumptions.json').read_text())
        self.pop,self.econ,_=read_inputs(HERE/'empirical')

    def test_probability_mixture_not_mean_income(self):
        r=expected_metrics(7000,10000,[(.5,0),(.5,5000)])
        self.assertEqual(r[0],.5)
        self.assertLess(7000+.5*5000,10000)
        self.assertEqual(r[4],2500)

    def test_probabilities_must_sum_to_one(self):
        with self.assertRaises(ValueError):expected_metrics(0,1,[(.3,0)])

    def test_binary_boundaries(self):
        self.assertEqual(binary(0),[(1,False)])
        self.assertEqual(binary(1),[(1,True)])
        with self.assertRaises(ValueError):binary(1.1)

    def test_coupled_access_is_normalized(self):
        rows=coupled_access(.5,.8)
        self.assertAlmostEqual(sum(r[0] for r in rows),1)
        self.assertAlmostEqual(sum(p for p,c,k in rows if c),.5)
        self.assertAlmostEqual(sum(p for p,c,k in rows if k),.8)
        self.assertFalse(any(c and not k for p,c,k in rows))

    def test_shared_credit_schedule_preserves_existing_engine(self):
        policy,_cpi,_anchor=policy_parameters(2030,self.spec['common'],self.econ)
        t={'agi':30000,'filing_status':'head','claimant_ids':['ssn']}
        kids=[dict(age=4,child_id='ssn',qualifying_child=True)]
        self.assertEqual(credit_amount(kids,t,'ssn_only',policy),credit_for_ages([4],30000,'head',policy))

    def test_odc_bounds_and_preservation(self):
        policy,cpi,_=policy_parameters(2030,self.spec['common'],self.econ)
        t=dict(child_ages=[4],agi=30000,filing='head',nonrefundable=2200,
               refundable=0,adult_dependents=1)
        self.assertGreaterEqual(tax_increment(t,policy,cpi,'lower'),tax_increment(t,policy,cpi,'upper'))
        t['nonrefundable']=100000
        self.assertEqual(tax_increment(t,policy,cpi,'upper'),0)

    def test_index_anchor_changes_real_credit(self):
        p,c,_=policy_parameters(2030,self.spec['common'],self.econ)
        p2,c2,_=policy_parameters(2030,dict(self.spec['common'],index_base_year=2025),self.econ)
        self.assertGreater(credit_for_ages([4],0,'other',p2)/c2,credit_for_ages([4],0,'other',p)/c)

    def test_voucher_cap_includes_adult_only_households(self):
        ps,checks=prepare_units(sample(),2030,self.spec['common'],self.pop,self.econ)
        self.assertAlmostEqual(checks['expected_awarded_households'],100000)
        self.assertAlmostEqual(ps['u']['voucher_probability'],.01)

    def test_housing_cap_net_of_existing_subsidy(self):
        d=sample();d['units']['u']['SPM_CAPHOUSESUB']=9999
        ps,checks=prepare_units(d,2030,self.spec['common'],self.pop,self.econ)
        self.assertFalse(ps['u']['service']['voucher_awarded'])
        self.assertEqual(ps['u']['service']['housing_increment_cap'],0)

    def test_food_net_of_baseline_and_calendar(self):
        ps,_=prepare_units(sample(),2030,self.spec['common'],self.pop,self.econ)
        self.assertEqual(ps['u']['service']['school_meal_spm_delta'],0)
        self.assertEqual(ps['u']['service']['summer_ebt_spm_delta'],0)
        d=sample();d['units']['u']['SPM_SCHLUNCH']=0
        ps,_=prepare_units(d,2030,self.spec['common'],self.pop,self.econ)
        self.assertAlmostEqual(ps['u']['service']['school_meal_spm_delta'],861*80/179)

    def test_summer_net_of_embedded_baseline(self):
        d=sample();d['households']['h']['summer_reported']=True
        d['units']['u']['SPM_SCHLUNCH']=981
        ps,_=prepare_units(d,2034,self.spec['common'],self.pop,self.econ)
        self.assertEqual(ps['u']['service']['school_meal_spm_delta'],0)
        self.assertLess(ps['u']['service']['summer_ebt_spm_delta'],180)

    def test_care_reduction_never_exceeds_actual_deduction(self):
        ps,_=prepare_units(sample(),2030,self.spec['common'],self.pop,self.econ)
        v=ps['u'];v['ctc']=0
        d=dict(self.spec['scenarios']['full'],coverage=0)
        effects=unit_effect(v,2030,d,2)
        self.assertLessEqual(effects[4],1500)
        self.assertGreaterEqual(effects[4],0)

    def test_temporary_emergency_expires(self):
        cfg=dict(self.spec['common'],emergency_cash_budget_2030=1e10)
        ps,checks=prepare_units(sample(),2034,cfg,self.pop,self.econ)
        self.assertEqual(checks['expected_emergency_cash_all_households'],0)
        self.assertEqual(ps['u']['emergency_probability'],0)

    def test_emergency_budget_is_separate_and_bounded(self):
        cfg=dict(self.spec['common'],emergency_cash_budget_2030=1e9)
        _,checks=prepare_units(sample(),2030,cfg,self.pop,self.econ)
        self.assertAlmostEqual(checks['expected_emergency_cash_all_households'],1e9)

    def test_sdr_and_lifted_newly_poor_identity(self):
        d=sample();base={'u':[1.,1.,1.,5000.,0.]};ef={'u':[.5,0.,1.,2500.,5000.]}
        r=aggregate(d,ef,[1.,1.],base)
        self.assertEqual(r['poor_children_lifted'],1)
        self.assertEqual(r['children_newly_poor'],0)
        self.assertEqual(r['sampling_uncertainty']['paired_poor_rate_change']['se'],0)

    def test_assumptions_reject_invalid_probability(self):
        self.spec['scenarios']['moderate']['coverage']=1.1
        with self.assertRaises(ValueError):validate_assumptions(self.spec)

    def test_guidelines_use_separate_geographies(self):
        self.assertEqual(fpg(4,'01'),32150)
        self.assertEqual(fpg(4,'02'),40190)
        self.assertEqual(fpg(4,'15'),36980)

    def test_weighted_quantile(self):
        self.assertEqual(weighted_quantile([(1,1),(2,10),(100,1)]),2)

    def test_coverage_concentration_preserves_total_gap(self):
        d=sample()
        ps,_=prepare_units(d,2030,self.spec['common'],self.pop,self.econ)
        concentrate_coverage(d,ps,[1.,1.],.95)
        self.assertAlmostEqual(ps['u']['coverage_override'],.95)


if __name__=='__main__':unittest.main()
