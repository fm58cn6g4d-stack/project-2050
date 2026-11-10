"""Protect component ownership, calibration and permanent voucher spending."""
import importlib.util
from pathlib import Path
import sys
import unittest

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
spec=importlib.util.spec_from_file_location('component_fiscal',HERE/'fiscal-model.py')
fiscal=importlib.util.module_from_spec(spec);spec.loader.exec_module(fiscal)

class ComponentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base=fiscal.read_baseline(HERE.parent/'data/fiscal-baseline.csv')

    def mid(self):
        import csv
        return float(next(r for r in csv.DictReader(open(HERE.parent/'data/inputs/ledger-bills.csv')) if r['id']=='HOU-1')['cost_mid'])

    def test_total_is_ledger_cost_not_an_additional_claim(self):
        path=fiscal.row_path(self.base,self.mid(),fiscal.PR.BILLS['HOU-1'],'HOU-1')
        self.assertAlmostEqual(sum(path[y] for y in range(2030,2040)),self.mid()*1000)

    def test_permanent_rental_help_survives_2040(self):
        parts={name:(amount,p) for name,amount,p in fiscal.PR.COMPONENTS['HOU-1']}
        amount,p=parts['hou-4a-one-million-awards-full-fees']
        path=fiscal.row_path(self.base,amount,p)
        self.assertGreater(path[2040],path[2039]); self.assertNotIn('end',p)

    def test_time_limited_capital_closes_its_tail(self):
        parts={name:(amount,p) for name,amount,p in fiscal.PR.COMPONENTS['HOU-1']}
        amount,p=parts['hou-3c-01-revolving-fund-grants']
        path=fiscal.row_path(self.base,amount,p)
        self.assertGreater(path[2040],0); self.assertEqual(path[2041],0)

    def test_mismatched_component_allocation_fails(self):
        with self.assertRaises(ValueError):
            fiscal.row_path(self.base,self.mid()-.01,fiscal.PR.BILLS['HOU-1'],'HOU-1')

class BookingShapeTests(unittest.TestCase):
    """Optional shapes: a ramp that runs past 2039, an end year after 2039 that closes a tail,
    and fade. Rows without them keep their old paths exactly."""
    @classmethod
    def setUpClass(cls):
        cls.base=fiscal.read_baseline(HERE.parent/'data/fiscal-baseline.csv')

    def test_ramp_past_2039_keeps_rising(self):
        p=fiscal.row_path(self.base,.01,dict(start=2039,ramp=3,grow='cpi'))
        self.assertAlmostEqual(sum(p[y] for y in range(2030,2040)),10)
        self.assertGreater(p[2040],p[2039]*1.9); self.assertGreater(p[2041],p[2040]*1.4)
        self.assertAlmostEqual(p[2042]/p[2041],p[2043]/p[2042],places=2)

    def test_end_after_2039_closes_a_tail(self):
        p=fiscal.row_path(self.base,.07,dict(ramp=1,grow='cpi',perm=.2,end=2040))
        self.assertGreater(p[2040],0); self.assertEqual(p[2041],0); self.assertEqual(p[2056],0)

    def test_end_inside_window_keeps_perm_continuation(self):
        p=fiscal.row_path(self.base,.01,dict(start=2032,ramp=1,end=2036,perm=.3))
        self.assertEqual(p[2037],0); self.assertGreater(p[2040],0)

    def test_library_matches_model_for_new_shapes(self):
        spec=importlib.util.spec_from_file_location('prov',HERE/'budget/provisions.py')
        P=importlib.util.module_from_spec(spec);spec.loader.exec_module(P)
        B=P.baseline()
        for prof in (dict(start=2039,ramp=3,grow='cpi'),dict(ramp=1,grow='cpi',perm=.2,end=2040),
                     dict(start=2031,ramp=3,grow='gdp',perm=.4,fade=.1)):
            a=fiscal.row_path(self.base,.02,prof); b=P.profile_path(B,.02,prof)
            for y in range(2030,2057): self.assertEqual(a[y],b[y],(prof,y))

if __name__=='__main__':unittest.main()
