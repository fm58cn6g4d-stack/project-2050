"""Boundary tests for the annual net fiscal comparison; no economic certification."""
import copy,json,unittest
import climate_bridge as C

class ClimateBridgeTests(unittest.TestCase):
    def test_exported_totals_and_finite_capital(self):
        b=json.loads(C.SOURCE.read_text())['budget']
        p=json.loads((C.ROOT/'models/tools/climate-portfolio/pricing.json').read_text())
        for case in b['cases']:
            a=C.adjustments(b,case,p['inflation'],p['disaster']['ramp'])
            gf,cap=[v['annual_bn'] for v in a.values()]
            r=b['results'][case]
            self.assertAlmostEqual(sum(gf[str(y)] for y in C.m.W),r['general_fund_window_bn'])
            self.assertAlmostEqual(sum(cap[str(y)] for y in C.m.W),r['d4b_window_bn'])
            self.assertTrue(all(cap[str(y)]==0 for y in range(2040,2057)))
            self.assertAlmostEqual(gf['2040'],r['general_fund_fy2040_bn'])
            self.assertAlmostEqual(gf['2056'],gf['2050']*(1+p['inflation'])**6)

    def test_annual_overlay_charges_exact_year_and_preserves_inputs(self):
        f,b,old,u=C.m.load();before=copy.deepcopy(C.m.ADOPTION)
        base=C.m.build_case('base',f,b,old,u)
        test=C.m.build_case('test',f,b,old,u,spending_adjustments={'pulse':{'annual_bn':{'2030':100,'2040':-10}}})
        for a,z in zip(test['rows'],base['rows']):
            self.assertAlmostEqual(a['program_primary_bn']-z['program_primary_bn'],{2030:100,2040:-10}.get(a['year'],0))
        self.assertEqual(C.m.ADOPTION,before)

if __name__=='__main__':unittest.main()
