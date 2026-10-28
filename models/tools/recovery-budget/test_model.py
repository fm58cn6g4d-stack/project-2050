#!/usr/bin/env python3
"""Financial accounting and regression checks, not validation of economic assumptions."""
import hashlib, json, unittest
import model as M

class BudgetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.paths=['models/data/fiscal-baseline.csv','models/data/fiscal-paths.csv','models/data/inputs/education-adoption.json']
        cls.hashes={p:hashlib.sha256((M.ROOT/p).read_bytes()).hexdigest() for p in cls.paths}
        cls.d=M.run(); cls.f,cls.b,cls.m,cls.u=M.load()

    def test_capacity_integration_single_housing_charge(self):
        c=self.d['cases']['mixed']
        housing=[r for r in c['audit'] if r['line']=='HOU-4A PHA administration correction' and r['year'] in M.W]
        self.assertAlmostEqual(sum(r['primary_outlay_change_bn'] for r in housing),12.2)
        self.assertAlmostEqual(sum(r['revenue_change_bn'] for r in c['audit'] if r['line']=='IRS yield allowance with smaller capacity budget' and r['year'] in M.W),-250)
        self.assertEqual(M.ADOPTION['spending']['cap_sustained_tn'],.3)

    def test_administration_costs_and_fund_routing(self):
        c=self.d['cases']['mixed']
        for r in c['leave']['rows']:
            self.assertAlmostEqual(r['administration'],.03*r['benefits']+(3 if r['year']==2030 else 0))
        self.assertAlmostEqual(sum(r['development_program_bn'] for r in c['rows'] if r['year'] in M.W),92)
        for r in c['rows']:
            self.assertAlmostEqual(r['smi_admin_premiums_bn'],.25*r['smi_admin_bn'])

    def test_exploratory_ceiling_changes_do_not_mutate_adoption(self):
        import copy
        before=copy.deepcopy(M.ADOPTION)
        c=M.build_case('ceiling',self.f,self.b,self.m,self.u,spending_adjustments={'test':{'delta_tn':-.1,'profile':{'ramp':4,'grow':'gdp','perm':1}}})
        base=self.d['cases']['mixed']
        delta=sum(a['program_primary_bn']-b['program_primary_bn'] for a,b in zip(c['rows'],base['rows']) if a['year'] in M.W)
        self.assertAlmostEqual(delta,-100)
        self.assertEqual(M.ADOPTION,before)
        self.assertLess(c['summary']['debt_gdp_2056'],base['summary']['debt_gdp_2056'])

    def test_component_gross_net_identity_and_named_old_scope(self):
        for r in self.d['education_components']:
            self.assertAlmostEqual(r['full_fund_outlays_bn'],r['current_law_transfer_bn']+r['old_agenda_transfer_bn']+r['change_over_old_agenda_bn'])
        w=[r for r in self.d['education_components'] if r['year'] in M.W]
        self.assertAlmostEqual(sum(r['old_agenda_transfer_bn'] for r in w)/1000,1.23,places=5)
        self.assertGreater(sum(r['current_law_transfer_bn'] for r in w)/1000,.85)
        self.assertLess(sum(r['change_over_old_agenda_bn'] for r in w)/1000,.50)

    def test_consolidating_existing_childcare_is_not_new_spending(self):
        base=self.d['education_components']; full=self.d['consolidated_childcare']
        for a,b in zip(base,full):
            self.assertAlmostEqual(a['increment_over_current_law_bn'],b['increment_over_current_law_bn'])
            self.assertAlmostEqual(b['full_fund_outlays_bn']-a['full_fund_outlays_bn'],b['current_law_transfer_bn']-a['current_law_transfer_bn'])
        self.assertGreater(sum(r['full_fund_outlays_bn'] for r in full),sum(r['full_fund_outlays_bn'] for r in base))

    def test_source_rounding_and_early_policy_tension_not_hidden(self):
        self.assertAlmostEqual(sum(r['full_fund_outlays_bn'] for r in self.d['education_components'] if r['year']==2049),441)
        early=next(r for r in self.d['education_components'] if r['year']==2032 and r['component']=='idea')
        self.assertTrue(early['lower_than_old_component'])
        self.assertLess(early['change_over_old_agenda_bn'],0)

    def test_total_budget_identities(self):
        for c in self.d['cases'].values():
            for r in c['rows']:
                self.assertAlmostEqual(r['deficit_bn'],r['outlays_bn']-r['revenue_bn'])
                self.assertAlmostEqual(r['program_primary_bn'],r['primary_outlay_change_bn']-r['revenue_change_bn'])
                ar=[x for x in c['audit'] if x['year']==r['year']]
                self.assertAlmostEqual(r['revenue_change_bn'],sum(x['revenue_change_bn'] for x in ar))
                self.assertAlmostEqual(r['primary_outlay_change_bn'],sum(x['primary_outlay_change_bn'] for x in ar))

    def test_ss_starts_2031_no_legacy_net_receipt_double_count(self):
        ar=self.d['cases']['mixed']['audit']
        self.assertFalse(any(r['line']=='SS-1' for r in ar))
        r=next(r for r in ar if r['line'].startswith('SS actual') and r['year']==2030)
        self.assertEqual(r['revenue_change_bn'],0)
        routed=next(r for r in ar if r['line']=='SSA OASDI capacity reclassification' and r['year']==2030)
        self.assertAlmostEqual(r['primary_outlay_change_bn'],-routed['primary_outlay_change_bn'])
        self.assertTrue(any(r['line'].startswith('SS actual') and r['year']==2031 for r in ar))

    def test_2029_cash_and_surge_advance_not_free(self):
        ar=self.d['cases']['mixed']['audit']
        advances=[r['primary_outlay_change_bn'] for r in ar if r['line'].startswith('2029 delivery')]
        self.assertAlmostEqual(sum(advances),0)
        row=next(r for r in self.d['cases']['mixed']['rows'] if r['year']==2029)
        self.assertGreater(row['program_primary_bn'],44)
        self.assertAlmostEqual(row['program_primary_bn'],M.credit(2029)+5)

    def test_fund_grant_is_not_consolidated_revenue(self):
        a=self.d['cases']['mixed']; b=self.d['cases']['mixed_reserve_corridor']
        self.assertGreater(b['summary']['education_grants_tn'],a['summary']['education_grants_tn'])
        for x,y in zip(a['rows'],b['rows']):
            self.assertAlmostEqual(x['program_primary_bn'],y['program_primary_bn'])
            self.assertAlmostEqual(y['agenda_gf_primary_bn']-x['agenda_gf_primary_bn'],y['education_gf_grant_bn']-x['education_gf_grant_bn'])

    def test_leave_extension_reproduces_existing_engine(self):
        cap=self.u.P['leave_cap']; self.u.P['leave_cap']=1.1
        try: old=self.u.run_leave('high')
        finally: self.u.P['leave_cap']=cap
        new=M.leave_fund(self.u,1.1,'high',admin_fraction=0)
        for a,b in zip(old['rows'],new['rows']):
            for k in ('rate','receipts','benefits','reserve','loan'): self.assertAlmostEqual(a[k],b[k],places=6)
        self.assertEqual(new['rows'][-1]['year'],2100)
        self.assertEqual(new['terminal_loan'],0)

    def test_all_debt_rate_shock_and_downside_fail_visible(self):
        c=self.d['cases']
        self.assertGreater(c['mixed_all_debt_rate_plus1']['summary']['debt_gdp_2056'],c['mixed']['summary']['debt_gdp_2056']+30)
        self.assertFalse(c['mixed_downside']['summary']['debt_ratio_nonincreasing_2045_56'])
        self.assertEqual(c['mixed_downside']['summary']['education_depletion'],2035)
        self.assertIsNone(c['mixed_corridor_downside']['summary']['education_depletion'])

    def test_income_tax_solution_actually_stabilizes_not_just_endpoint(self):
        for name,options in [('mixed',{}),('mixed_downside',{'stress':True})]:
            rate=self.d['required_broad_rate_points'][name]
            c=M.build_case('solve',self.f,self.b,self.m,self.u,broad_rate=rate,**options)
            self.assertTrue(c['summary']['debt_ratio_nonincreasing_2045_56'])

    def test_no_unsupported_household_pass(self):
        h=self.d['household_diagnostic']['per_household_annual_dollars']
        self.assertLess(h['mixed'][2039]['Q4'],0)
        self.assertLess(h['larger_payroll'][2039]['Q4'],h['mixed'][2039]['Q4'])
        self.assertGreater(h['mixed_larger_credit'][2039]['Q4'],h['mixed'][2039]['Q4'])

    def test_historical_numeric_inputs_unchanged(self):
        for p,h in self.hashes.items(): self.assertEqual(hashlib.sha256((M.ROOT/p).read_bytes()).hexdigest(),h)

if __name__=='__main__': unittest.main()
