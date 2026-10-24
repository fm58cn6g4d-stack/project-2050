#!/usr/bin/env python3
"""Validate empirical accounting and scenario invariants; no desired outcome fit."""
import argparse
from model import load_json


def check(result):
    assert result['external_comparator']['passed']
    assert result['source_audit']['unresolved_child_claimants'] == 327
    assert result['source_audit']['child_own_return_differs'] == 141
    assert len(result['cases']) == 8
    assert abs(result['source_baseline']['poor_rate']-.1339131451759891) < 1e-9
    for year in (2030,2034):
        cases={c['scenario']:c for c in result['cases'] if c['year']==year}
        rates=[cases[n]['stages'][-1]['poor_rate'] for n in ('stressed','moderate','enhanced','full')]
        assert rates == sorted(rates,reverse=True)
        for c in cases.values():
            previous=c['baseline']['poor_rate']
            for s in c['stages']:
                if s['stage'] <= 4:
                    assert s['poor_rate'] <= previous+1e-12
                else:
                    assert s['poor_rate'] >= previous-1e-12
                previous=s['poor_rate']
                assert 0 <= s['deep_poor_rate'] <= s['poor_rate'] <= s['below150_rate'] <= 1
                assert abs(s['poor_children']-s['poor_rate']*s['weighted_children']) < .01
                assert abs(c['baseline']['poor_children']-s['poor_children']-
                           (s['poor_children_lifted']-s['children_newly_poor'])) < .01
                if s['stage'] in (1,5):
                    ci=s['sampling_uncertainty']['poor_rate']
                    assert ci['lower95'] <= s['poor_rate'] <= ci['upper95']
                    assert s['sampling_uncertainty']['paired_poor_rate_change']['se'] >= 0
            a=c['award_checks']
            assert a['expected_awarded_households'] <= a['award_cap']+.01
            assert a['expected_leased_households'] <= a['expected_awarded_households']+.01
            assert c['residual']['additional_poor_under_selected_delivery'] >= -.01
        sensitivities={s['name']:s for s in result['sensitivities'] if s['year']==year}
        central=cases['moderate']['stages'][-1]['poor_rate']
        assert sensitivities['index_from_2025']['result']['poor_rate'] <= central
        assert sensitivities['retain_adult_ODC_bound']['result']['poor_rate'] <= central
        assert sensitivities['health_MOOP_minus_30pct']['result']['poor_rate'] <= sensitivities['health_MOOP_minus_15pct']['result']['poor_rate'] <= central
        assert sensitivities['employer_leave_fully_wage_borne']['result']['poor_rate'] >= central
        if year==2034:
            assert abs(sensitivities['temporary_cash_10B']['result']['poor_rate']-central) < 1e-12
    return dict(status='passed',cases=8,sensitivities=len(result['sensitivities']),
        checks='Source/comparator; monotonic delivery; stage accounting; lifted/newly-poor identity; household award caps; sampling fields; temporary aid expiry')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--results',required=True)
    a=p.parse_args();print(check(load_json(a.results)))
