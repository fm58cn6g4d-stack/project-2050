"""Checks for the international climate finance pricing: python3 index/tools/climate-portfolio/test_international.py"""
import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
subprocess.run([sys.executable, str(HERE / 'international.py')], check=True, capture_output=True)
d = json.loads((ROOT / 'build/climate-portfolio/climate-portfolio-international-pricing.json').read_text())
fails = []
def check(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name)
    if not ok: fails.append(name)
check('volumes sum their sources', all(abs(d['volume_mt_2035'][i] - sum(s['mt_2035'][i] for s in d['sources'])) < 1e-9 for i in range(3)))
check('ranges are ordered', all(d[k][0] <= d[k][1] <= d[k][2] for k in ('volume_mt_2035', 'cost_2035_bn', 'cost_2030_39_bn')))
check('the 66% gap exceeds the 61% gap', all(d['gap_mt_2035']['66%'][i] > d['gap_mt_2035']['61%'][i] for i in range(3)))
check('ramped decade cost is below ten full years', all(d['cost_2030_39_bn'][i] < 10 * d['cost_2035_bn'][i] for i in range(3)))
check('loss and damage is never added to emissions', 'loss_and_damage_2030_39_bn' in d and all(abs(d['total_2035'][i] - d['domestic_2035'][1] - d['points_2035'][i]) < 1e-12 for i in range(3)))
check('floor: international tons count only when domestic reaches the floor',
      all((d['counted_total_without_measures_2035'][i] > d['domestic_2035'][i]) == d['floor_met_without_measures'][i] for i in range(3))
      and all((d['counted_total_with_measures_2035'][i] > d['domestic_with_floor_measures_2035'][i]) == d['floor_met_with_measures'][i] for i in range(3)))
check('floor measures lift the mid case over the floor', d['floor_met_with_measures'][1] and d['domestic_with_floor_measures_2035'][1] >= d['domestic_floor'])
c = ROOT / 'sources/climate-portfolio-international-pricing.md'
if c.exists():
    check('committed report matches the build', c.read_text() == (ROOT / 'build/climate-portfolio/climate-portfolio-international-pricing.md').read_text())
print('all passed' if not fails else f'{len(fails)} failed')
sys.exit(1 if fails else 0)
