#!/usr/bin/env python3
"""Tests for senate_model.py: seat bookkeeping, input arithmetic, the Alaska submodel and the simulation.

Role: checks that the 2028 Senate model's inputs add up and that its mechanics behave as documented in
dossiers/scenario/senate-model-2028.md. Status: current. Run: python3 dossiers/scenario/tools/test_senate_model.py
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senate_model as m  # noqa: E402

CLASS3_2028 = {'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
               'LA', 'MD', 'MO', 'NV', 'NH', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'SC', 'SD', 'UT', 'VT',
               'WA', 'WI'}


class Bookkeeping(unittest.TestCase):
    def test_2028_races_are_class3_plus_tennessee_special(self):
        regular = {k for k in m.RACES if not k.endswith('*')}
        self.assertEqual(regular, CLASS3_2028)
        self.assertEqual(len(CLASS3_2028), 34)
        self.assertEqual({k for k in m.RACES if k.endswith('*')}, {'TN*'})

    def test_montana_and_texas_have_no_2028_race(self):
        self.assertNotIn('MT', m.RACES)
        self.assertNotIn('TX', m.RACES)
        self.assertIn('MT', m.CLASS1)   # Sheehy, up 2030
        self.assertIn('MT', m.CLASS2)   # elected 2026, up 2032

    def test_classes_are_disjoint_and_complete(self):
        self.assertEqual(len(m.CLASS1), 33)
        self.assertEqual(len(m.CLASS2), 33)
        # every state appears exactly twice across the three classes
        count = {}
        for s in list(m.CLASS1) + list(m.CLASS2) + list(CLASS3_2028):
            count[s] = count.get(s, 0) + 1
        self.assertEqual(len(count), 50)
        self.assertTrue(all(v == 2 for v in count.values()), count)

    def test_2027_senate_is_56_democratic_caucus_when_ak_and_ms_go_democratic(self):
        d1 = sum(1 for p, _ in m.CLASS1.values() if p == 'D')
        d2 = sum(1 for p, _ in m.CLASS2.values() if p == 'D')
        d3 = sum(1 for k, r in m.RACES.items() if r['p'] == 'D' and not k.endswith('*'))
        self.assertEqual((d1, d2, d3), (19, 21, 16))
        self.assertEqual(d1 + d2 + d3, 56)
        # 37 certain seats not up: Class 1 less Minnesota, Class 2 less Alaska and Mississippi
        self.assertEqual(m.CERTAIN_D_NOT_UP, (d1 - 1) + (d2 - 2))

    def test_every_state_has_inputs(self):
        for s in list(m.CLASS1) + list(m.CLASS2) + [m.state_of(k) for k in m.RACES]:
            self.assertIn(s, m.P20)
            self.assertIn(s, m.P24)
            self.assertIn(s, m.REGION_OF)


class Arithmetic(unittest.TestCase):
    def test_lean_hand_example_ohio(self):
        l20 = -8.03 - 4.46
        l24 = -11.21 + 1.48
        # Senate special against an appointed Republican incumbent (+2 back), governor open, weight 0.5
        l26 = ((4.8 + 2.0) + 0.5 * 7.9) / 1.5 - 12.9
        want = 0.2 * l20 + 0.5 * l24 + 0.3 * l26
        self.assertAlmostEqual(m.lean('OH'), want, places=6)

    def test_governor_incumbency_is_removed(self):
        prm = dict(m.BASE_PARAMS)
        self.assertAlmostEqual(m.adjusted_2026('NV', prm), 7.6 + 3.0)   # Lombardo (R) was the incumbent
        self.assertAlmostEqual(m.adjusted_2026('AZ', prm), 13.1 - 3.0)  # Hobbs (D) was the incumbent

    def test_lean_without_2026_data_renormalizes(self):
        want = (0.2 * (-16.07 - 4.46) + 0.5 * (-18.96 + 1.48)) / 0.7
        self.assertAlmostEqual(m.lean('IN'), want, places=6)

    def test_candidate_effect_signs_and_cap(self):
        self.assertGreater(m.candidate_effect('AZ'), 0)   # Kelly ran well ahead of the state in 2022
        self.assertLess(m.candidate_effect('SC'), 0)      # Scott ran well ahead for Republicans
        for k in m.RACES:
            if not m.RACES[k].get('alaska'):
                self.assertLessEqual(abs(m.candidate_effect(k)), m.BASE_PARAMS['cap'] + 1e-9)

    def test_midterm_history(self):
        self.assertEqual(len(m.MIDTERM_SWINGS), 10)
        self.assertAlmostEqual(sum(m.MIDTERM_SWINGS) / 10, 7.18, places=2)


class Alaska(unittest.TestCase):
    def test_retire_branch_is_a_two_party_race(self):
        self.assertEqual(m.alaska_outcome(5.0, 'retire')[0], 'D')
        self.assertEqual(m.alaska_outcome(-5.0, 'retire')[0], 'R')

    def test_independent_caucusing_with_democrats_beats_a_generic_democrat(self):
        # at a generic margin of D-6, a Democrat loses but Murkowski as a D-caucusing independent wins
        self.assertEqual(m.alaska_outcome(-6.0, 'retire')[0], 'R')
        self.assertEqual(m.alaska_outcome(-6.0, 'I-D')[0], 'D')

    def test_republican_murkowski_wins_as_republican_in_a_red_year(self):
        self.assertEqual(m.alaska_outcome(-15.0, 'R')[0], 'R')

    def test_repealed_primary_winner_faces_no_dunleavy(self):
        import random
        win, _, who = m.alaska_outcome(-12.0, 'R', rcv=False, rng=random.Random(1), r_primary_win=1.0)
        self.assertEqual(who, 'M')
        self.assertEqual(win, 'R')

    def test_calibration_to_2022(self):
        # 2022: D side about 45% of voters; Murkowski 43.4, Democrat 10.4 on first choices
        p, a, b = 0.45, 0.77, 0.16
        self.assertAlmostEqual(a * p + b * (1 - p), 0.434, delta=0.01)
        self.assertAlmostEqual((1 - a) * p, 0.104, delta=0.01)


class Simulation(unittest.TestCase):
    def test_deterministic(self):
        a = m.simulate_2028(0.0, n=500, seed=3)
        b = m.simulate_2028(0.0, n=500, seed=3)
        self.assertEqual(a['seats'], b['seats'])

    def test_more_seats_in_better_environments(self):
        means = [m.summarize(m.simulate_2028(e, n=3000, seed=4))['mean'] for e in (-3, 0, 3, 6)]
        self.assertEqual(means, sorted(means))

    def test_seat_bounds(self):
        o = m.simulate_2028(0.0, n=2000, seed=5)
        lo = m.CERTAIN_D_NOT_UP
        hi = m.CERTAIN_D_NOT_UP + len(m.UNCERTAIN_NOT_UP) + len(m.RACES)
        self.assertTrue(all(lo <= s <= hi for s in o['seats']))

    def test_tipping_point_counts(self):
        o = m.simulate_2028(0.0, n=2000, seed=6)
        self.assertLessEqual(sum(o['tip51'].values()), o['n'])

    def test_presidency_conditioning_splits_runs(self):
        o = m.simulate_2028(3.0, n=4000, seed=7, env_sd=4.5)
        d = m.summarize(o, 'D')
        r = m.summarize(o, 'R')
        self.assertAlmostEqual(d['share'] + r['share'], 1.0, places=9)
        self.assertGreater(d['mean'], r['mean'])

    def test_chain_runs_and_midterm_hurts_president(self):
        res = m.simulate_chain(3.0, n=3000, seed=8, env_sd=0.0)
        n, rows, thru = m.chain_table(res, 'D')
        self.assertGreater(n, 0)
        for t in thru:
            self.assertTrue(all(0 <= x <= 1 for x in t))
        # held continuously can only fall as more elections are added
        self.assertGreaterEqual(thru[0][0], thru[1][0])
        self.assertGreaterEqual(thru[1][0], thru[2][0])

    def test_tennessee_special_is_not_double_counted(self):
        # With every 2030 Class 1 race lost, January 2031 seats are the Class 2 and 3 Democrats only:
        # s28 minus the Class 1 Democrats held in 2029, which includes a Democratic Tennessee winner.
        o = m.simulate_2028(13.0, n=300, seed=15)
        for i in range(o['n']):
            c1 = 18 + o['draws'][i]['MN-2027'] + ('TN*' in o['dwon'][i])
            c23 = o['seats'][i] - c1
            self.assertEqual(c23, m.CERTAIN_D_NOT_UP - 18 + o['draws'][i]['AK-2026'] + o['draws'][i]['MS-2026']
                             + len(o['dwon'][i]) - ('TN*' in o['dwon'][i]))

    def test_overrides_raise_target_seats(self):
        a = m.simulate_2028(0.0, n=3000, seed=9)
        b = m.simulate_2028(0.0, n=3000, seed=9, overrides={'NV': 5.0})
        self.assertGreater(b['wins']['NV'], a['wins']['NV'])


class Round4(unittest.TestCase):
    def test_minnesota_special_rises_with_environment(self):
        ps = [m.p_mn_2027(e) for e in (-3, 0, 3, 8)]
        self.assertEqual(ps, sorted(ps))
        self.assertGreater(m.p_mn_2027(0), m.p_mn_2027(0, appointee=0.0))

    def test_whip_opponents_bounded_by_caucus(self):
        o = m.simulate_2028(3.0, n=500, seed=12)
        for seats, opp, _ in m.whip_d2f(o):
            self.assertLessEqual(opp, seats)
        lo = m.d2f_summary(o, None, scale=0.5)
        hi = m.d2f_summary(o, None, scale=2.0)
        self.assertGreater(lo['p_pass'], hi['p_pass'])
        self.assertLess(lo['opp'], hi['opp'])

    def test_statehood_adds_seats_when_seated(self):
        base = m.simulate_chain(3.0, n=1500, seed=13, env_sd=0.0)
        dc31 = m.simulate_chain(3.0, n=1500, seed=13, env_sd=0.0, statehood='DC', statehood_from=2031)
        dc33 = m.simulate_chain(3.0, n=1500, seed=13, env_sd=0.0, statehood='DC', statehood_from=2033)
        self.assertEqual(dc31['s28'], base['s28'])
        self.assertEqual([a - b for a, b in zip(dc31['s30'], base['s30'])], [2] * base['kept'])
        self.assertEqual(dc33['s30'], base['s30'])
        self.assertEqual([a - b for a, b in zip(dc33['s32'], base['s32'])], [2] * base['kept'])

    def test_pr_split_probabilities_sum_to_one(self):
        self.assertAlmostEqual(sum(p for _, p in m.PR_SPLIT), 1.0)

    def test_drivers_shares_sum_to_one(self):
        res = m.simulate_chain(3.0, n=1500, seed=14, env_sd=0.0)
        rows = m.drivers_2032(res, None)
        self.assertAlmostEqual(sum(r[2] for r in rows), 1.0, places=6)
        self.assertTrue(all(0 <= r[1] <= 1 for r in rows))

    def test_repeal_assumption_matches_count(self):
        self.assertLess(m.AK_P_REPEAL, 0.10)   # No leads 51.85% with about 60,000 ballots out


if __name__ == '__main__':
    unittest.main(verbosity=1)
