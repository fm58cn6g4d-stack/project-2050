#!/usr/bin/env python3
"""program_inventory.py: every flagship's and major line's cost and timing in the booked budget model.

Role: a read-only inventory of the booked case's audit lines (recovery-budget `build_case('mixed', ...)`), grouped by
flagship, for stage G step 8b (the fiscal path review). It books nothing and writes nothing under models/data/inputs/.
Status: research helper, November 24, 2026; built by a Standard-tier subagent, checked by the step's author.

Run after the common rebuild (`bash models/tools/run-all.sh`, which writes build/):
    python3 models/tools/program_inventory.py             # the markdown tables to stdout
    python3 models/tools/program_inventory.py --json      # the same figures as JSON
    python3 models/tools/program_inventory.py --part tables|hump|top   # one part of the markdown

The model is loaded as models/tools/financing-protection/packages.py loads it. Conventions: nominal $B, federal fiscal
years; a spending line is its audit row's `primary_outlay_change_bn`, a revenue line its `revenue_change_bn`.
  * Start = first FY a line is at least $0.5B. Fully phased in = first FY its share of GDP reaches 90% of its peak share
    over FY2030-56 (a line still growing faster than GDP is "full" only when that growth levels off).
  * Time-limited = the line's FY2056 share of GDP is under 25% of its peak share (it ends or runs down); else permanent.
  * "Fund" lines are paid by a dedicated fund the model keeps out of the general-fund (GF) gap: Social Security,
    Medicare's HI account, the education fund and paid leave. The general-fund gap is the model's `agenda_gf_primary_bn`.
"""
import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'models/tools'), str(ROOT / 'models/tools/financing-protection')]
import packages as K  # noqa: E402

SHOW = (2030, 2033, 2036, 2037, 2038, 2039, 2040, 2045, 2056)
HUMP = (2036, 2037, 2038, 2039)
THRESH_SPEND, THRESH_REV = 5.0, 20.0
FUND_LINES = {'SS actual 2031 start, high-base package and SS-7.01 fallback', 'HI H1a and Part A HLT-6 share',
              'Paid leave actual contributions and benefits', 'EDU replacement, net of existing-law and old agenda'}
SKIP = {'Matched dedicated uses (gross presentation proxy)'}   # equal revenue and outlay: a presentation gross-up
ALSO_SHOW = ['CAP-7S', 'CAP-7P']                                # named in the brief; below the threshold
ORDER = ['Housing', 'Health (single plan and Medicaid)', 'Care parts B-D (long-term care, child care, care workforce)',
         'Secure floor', 'Immigration', 'Clean power', 'Work', 'Democratic renewal', 'Transportation',
         'Capacity (CAP-7, 7S)', 'Other (education, defense, AI, development, veterans, misc.)']
NAMES = {
    'HLT-7': 'Single plan (Medicare for All), gross spending, waves 2031-35',
    'HLT-9': 'Long-term care in the single plan, from 2035',
    'HLT-10': 'Care wage floor in the plan\'s rates, from 2035',
    'HLT-11': 'Nursing home staffing standard',
    'HLT-4': 'Medicaid, long-term care, safety net (wave to 2034, then lower)', 'HLT-6': 'Medicare Advantage fix, a saving (to the 2035 endpoint)',
    'MOV-29': 'Moving America 2029 reconciliation act', 'CLI-11': 'Transition guarantee for workers and places',
    'HLT-2': 'Medicare upgrades until the 2035 endpoint', 'HLT-1': 'Restore pre-H.R. 1 coverage (2030)',
    'FAM-2': 'Child care and universal pre-K (with educators\' pay)', 'FAM-1': 'Monthly child benefit',
    'HOU-1': 'Housing reconciliation title (aid, credits, construction, vouchers, repair)',
    'housing_extra': 'Housing stage 2 and other added housing money (model "extras")',
    'CLI-1': 'Clean-energy credits restored', 'CLI-5': 'Thriving Economy add-ons (credits, LIHEAP/WAP, minerals)',
    'CLI-9': 'Clean-industry contracts', 'CLI-7': 'Disaster permanent pieces', 'CLI-7K': 'Disaster capital pieces',
    'CLI-10': 'Second grid tranche, builder of last resort', 'CLI-5W': 'Low-income heat-pump retrofits',
    'CLI-5H': 'Automatic energy bill credit (from FY2040)',
    'CAP-7': 'Sustained agency capacity (about 0.12% of GDP)', 'CAP-7S': 'Agency rebuild surge', 'CAP-7P': 'CAP-7 hiring-pace timing',
    'CAP-8': 'Civil service and congressional capacity',
    'EDU-1': 'K-12 and special education formulas', 'EDU-3': 'Free school meals, Summer EBT', 'EDU-5': 'Pell and student-loan fixes',
    'MOV-31': 'Moving America Act of 2031', 'MOV-30': 'Moving America 2030 reconciliation act',
    'IMM-1': 'Immigration (status, courts, enforcement, USCIS)', 'AI-4': 'AI and work: wage insurance, training',
    'INC-1': 'EITC for workers without children', 'INC-2': 'SNAP cuts repealed', 'INC-2B': 'SNAP earned-income deduction',
    'INC-3': 'SSI asset limits, territories', 'LAB-1': 'Labor bill (PRO Act core, wage floor, enforcement)',
    'LAB-9': 'National service', 'LAB-11': 'Unemployment insurance on the general fund',
    'participation (LAB-10, paid on-ramps)': 'Participation help, paid on-ramps (LAB-10)',
    'DEV-P permanent development programs': 'Permanent development programs', 'NSC-10': 'Veterans health and capacity',
    'EDU replacement, net of existing-law and old agenda': 'Education fund, benefits net of current law (fund)', 'HI H1a and Part A HLT-6 share': 'Medicare HI fund: Part A savings (fund)',
    'SS actual 2031 start, high-base package and SS-7.01 fallback': 'Social Security package (fund)',
    'Paid leave actual contributions and benefits': 'Paid family and medical leave (fund)',
}
REV_NAMES = {
    'HEC': 'Employer health contribution (19.3% of pay)', 'HEX': 'Tax on former premiums (offsets HX)',
    'HX': 'End of employer tax exclusion', 'HCU': 'Household health contribution (HCU)',
    'HCW': 'Worker 1.45% HI tax folded in', 'HCA': 'Additional Medicare Tax folded in', 'HCH': 'H1b wage half folded in',
    'HS1': 'Financial transactions tax to 0.1%', 'HS2': 'Annual wealth tax', 'HS3': 'Capital gains as ordinary income above $1M',
    'HS4': 'Corporate rate 30%, expensing repealed', 'H1a': 'Investment-income tax on pass-through income (GF share)',
    'H1b': 'Medicare/investment-income rates 5% above $400K', 'G1': 'Corporate rate 28%', 'G3': 'Top rate 39.6%',
    'G5': 'Buyback tax, corporate minimum', 'G6': 'Capital gains at death', 'G7': 'Foreign income at full corporate rate',
    'G8': 'IRS enforcement yield', 'G9': 'Reverse 2025 tax cuts above $450K', 'G10': 'Financial transactions tax 0.01%',
    'G11': 'Billionaire mark-to-market', 'GX': 'Overlap and avoidance adjustment (high-income)', 'CX': 'Income/payroll offset on carbon fees',
    'MR6': 'Income/payroll offset on new excises', 'C18': 'Legacy revenue row C18', 'C35': 'Legacy revenue row C35',
    'C38': 'Legacy revenue row C38', 'C39': 'Legacy revenue row C39', 'C43': 'Legacy revenue row C43',
    'C3A': 'Clean electricity standard payments', 'C1T': 'Carbon transition remainder in GF (from FY2040)',
    'EDU replacement, net of existing-law and old agenda': 'Education payroll contribution (EDUP), net of its offset (fund)',
    'SS actual 2031 start, high-base package and SS-7.01 fallback': 'Social Security package receipts (fund)',
    'Paid leave actual contributions and benefits': 'Paid leave contributions (fund)',
    'New indexed income contributions': 'New indexed income contributions (4 high-income points)',
    'Matched dedicated uses (gross presentation proxy)': 'Matched dedicated receipts (gross proxy, equal outlay)',
    'IRS yield allowance with smaller capacity budget': 'IRS yield allowance (reduces G8)',
    'Settlement S03: HCU\'s avoidance allowance by tier: 10% on the base rate, 20% on the surcharge': 'S03: HCU avoidance allowance',
    'Settlement S04: Stack cap C1: the wealth tax capped at 100% of a 6% return with the income taxes': 'S04: stack cap on the wealth tax',
    'Settlement S06: The health contribution\'s base rate R raised from 2.25% from 2035': 'S06: HCU base rate raised above 2.25% from FY2035',
}
# Who pays: a judgement label for the brief's "falls on the middle class" flag. The ledger's reaches_middle is used when an
# ID has one; the rest are tagged here from the line's own definition.
MIDDLE_TAG = {
    'HCU': 'YES (HCU: 2.25% of AGI, exempt to 138% of poverty, phased to 250%; surcharge above $205,400)',
    'HCW': 'YES, a cut: the worker 1.45% HI tax ends, replaced inside HCU', 'HCA': 'No (top earners; a cut)',
    'HCH': 'No (high earners; a cut)', 'HEC': 'YES, payroll: employer contribution, 19.3% of pay between $20,000 and the wage base (wages bear part of it)',
    'HEX': 'YES (reduces HX; same households)', 'HX': 'YES: employer premium exclusion ends, on the full pass-through convention',
    'EDU replacement, net of existing-law and old agenda': 'YES, payroll: education contribution (EDUP), 1.4 points, all on workers',
    'SS actual 2031 start, high-base package and SS-7.01 fallback': 'Mostly high earners (wage-base lift, high-base package); a payroll piece reaches workers; check SS dossier',
    'Paid leave actual contributions and benefits': 'YES, payroll: leave contributions on workers and employers',
    'Settlement S06: The health contribution\'s base rate R raised from 2.25% from 2035': 'YES: raises HCU\'s base rate (a step in FY2036)',
    'Settlement S03: HCU\'s avoidance allowance by tier: 10% on the base rate, 20% on the surcharge': 'YES: a yield allowance on HCU (booked as added receipts; the label says allowance, so the sign is worth a check by the step author)',
    'New indexed income contributions': 'No: high-income points only (broad rate 0)',
    'CX': 'Offset on carbon fees, which reach households (see carbon row)', 'MR6': 'Offset on excises that reach households',
    'IRS yield allowance with smaller capacity budget': 'No',
    'Settlement S04: Stack cap C1: the wealth tax capped at 100% of a 6% return with the income taxes': 'No (wealth tax)',
    'Matched dedicated uses (gross presentation proxy)': 'Includes carbon, fuel taxes: reaches households',
}


SHORT = {'Paid leave actual contributions and benefits': 'LEAVE', 'SS actual 2031 start, high-base package and SS-7.01 fallback': 'SS pkg',
         'EDU replacement, net of existing-law and old agenda': 'EDU fund', 'participation (LAB-10, paid on-ramps)': 'LAB-10',
         'DEV-P permanent development programs': 'DEV-P', 'HI H1a and Part A HLT-6 share': 'HI fund',
         'New indexed income contributions': 'NIC', 'Matched dedicated uses (gross presentation proxy)': 'MATCHED',
         'IRS yield allowance with smaller capacity budget': 'IRS allow.'}


def sid(l):
    if l in SHORT: return SHORT[l]
    if l.startswith('Settlement S'): return l.split(':')[0].replace('Settlement ', '')
    return l


def group_of(line):
    p = line
    if line.startswith('Settlement S05'): return ORDER[2]
    if line.startswith('Settlement S11'): return ORDER[0]
    if line.startswith('Settlement'): return ORDER[10]
    if p in ('HLT-9', 'HLT-10', 'HLT-11', 'FAM-2'): return ORDER[2]
    if p.startswith('HLT-'): return ORDER[1]
    if p.startswith('HOU-') or p == 'housing_extra': return ORDER[0]
    if p in ('FAM-1', 'FAM-3') or p.startswith('INC-') or p.startswith('SS') or p.startswith('Paid leave') or 'LAB-10' in p: return ORDER[3]
    if p.startswith('IMM-'): return ORDER[4]
    if p.startswith('CLI-'): return ORDER[5]
    if p.startswith('LAB-') or p == 'AI-4': return ORDER[6]
    if p.startswith('DEM-') or p.startswith('CRT-') or p == 'CAP-8': return ORDER[7]
    if p.startswith('MOV-'): return ORDER[8]
    if p.startswith('CAP-'): return ORDER[9]
    return ORDER[10]


def load():
    f, b, old, u = K.m.load()
    c = K.m.build_case('mixed', f, b, old, u)
    led = json.loads((ROOT / 'build/ledger.json').read_text())
    return f, b, u, c, led


def series(audit, field):
    d = collections.defaultdict(dict)
    for r in audit:
        d[r['line']][r['year']] = d[r['line']].get(r['year'], 0.0) + r[field]
    return d


def timing(y, b, floor=0.5):
    """start, full, kind, last. Full = first FY after which every year's growth stays within 2 points of GDP growth."""
    yrs = list(range(2030, 2057))
    share = {t: y.get(t, 0) / b[t]['gdp'] for t in yrs}
    start = next((t for t in range(2026, 2057) if y.get(t, 0) >= floor), None)
    peak = max(share.values())
    if peak <= 0 or start is None: return start, None, 'n/a', None
    gg = {t: b[t]['gdp'] / b[t - 1]['gdp'] - 1 for t in range(2031, 2057)}

    def calm(t):   # growth into every later year is within 2 points of GDP growth (or the line shrinks)
        return all(y.get(u, 0) / y[u - 1] - 1 <= gg[u] + 0.02 for u in range(t + 1, 2057) if y.get(u - 1, 0) >= floor)
    full = next((t for t in yrs if t >= start and calm(t)), None)
    last = max((t for t in yrs if y.get(t, 0) >= floor), default=None)
    if y.get(2056, 0) < floor: kind = f'ends after FY{last}'
    elif share[2056] < 0.25 * peak: kind = f'permanent but runs down to {100 * share[2056] / peak:.0f}% of its peak share'
    else: kind = 'permanent'
    return start, full, kind, last


def fmt(v):
    return f'{v:,.1f}'


def build():
    f, b, u, c, led = load()
    audit = c['audit']
    out = series(audit, 'primary_outlay_change_bn'); rev = series(audit, 'revenue_change_bn')
    gf = {r['year']: r['agenda_gf_primary_bn'] for r in c['rows']}
    bills = {x['id']: x for x in led['bills']}; rrows = {x['id']: x for x in led['revenue']}
    spend = []
    for l, y in out.items():
        if l in SKIP: continue
        hit = max(y.get(t, 0) for t in HUMP) >= THRESH_SPEND or y.get(2040, 0) >= THRESH_SPEND
        if hit or l in ALSO_SHOW:
            st, fu, kind, last = timing(y, b)
            spend.append(dict(id=l, name=NAMES.get(l) or (bills[l]['bill'][:70] if l in bills else l), group=group_of(l),
                              fund=l in FUND_LINES, vals={t: y.get(t, 0) for t in SHOW}, tot3039=sum(y.get(t, 0) for t in range(2030, 2040)),
                              hump=sum(y.get(t, 0) for t in HUMP), start=st, full=fu, kind=kind, last=last,
                              domain=bills[l]['domain'] if l in bills else '', below=l in ALSO_SHOW and not hit))
    revl = []
    for l, y in rev.items():
        if abs(y.get(2040, 0)) >= THRESH_REV:
            st, fu, kind, last = timing(y if y.get(2040, 0) > 0 else {t: -v for t, v in y.items()}, b)
            mid = MIDDLE_TAG.get(l) or (('Ledger says reaches the middle class: ' + rrows[l]['reaches_middle']) if l in rrows else '')
            revl.append(dict(id=l, name=REV_NAMES.get(l) or l, vals={t: y.get(t, 0) for t in SHOW}, tot3039=sum(y.get(t, 0) for t in range(2030, 2040)),
                             start=st, full=fu, kind=kind, middle=mid, fund=l in FUND_LINES))
    # carbon: gross C1/C2 receipts are inside the matched gross-up line; recompute them from the model's own carbon table and rule
    car = {r['year']: r for r in u.carbon}
    cc = {}
    for k in ('c1', 'c2'):
        cc[k] = {t: car[t][k] for t in range(2030, 2040)}
        for t in range(2040, 2057): cc[k][t] = cc[k][2039] * b[t]['gdp'] / b[2039]['gdp'] * .98 ** (t - 2039)
    carbon = {t: cc['c1'][t] + cc['c2'][t] for t in cc['c1']}
    return dict(f=f, b=b, c=c, gf=gf, spend=spend, revl=revl, carbon=carbon, out=out, rev=rev, deficit=series(audit, 'primary_deficit_change_bn'), bills=bills)


HEALTH_FIN = ['HX', 'HCU', 'HEC', 'HEX', 'HCW', 'HCA', 'HCH', 'HS1', 'HS2', 'HS3', 'HS4', 'H1a', 'H1b']
HEALTH_SPEND = ['HLT-1', 'HLT-2', 'HLT-4', 'HLT-6', 'HLT-7', 'HLT-9', 'HLT-10', 'HLT-11']


def tables(D):
    L = []
    hdr = '| ID | Line | ' + ' | '.join(f'FY{t}' for t in SHOW) + ' | FY2030-39 | Start | Full | Term |\n|---|---|' + '---:|' * (len(SHOW) + 1) + '---|---|---|'
    S = D['spend']
    L.append('## 1. Spending lines\n')
    L.append(f'Lines with at least ${THRESH_SPEND:.0f}B in any of FY2036-39 or in FY2040, plus CAP-7S and CAP-7P (named in the brief, below the cut). '
             '$B, nominal. "Full" is the first FY after which the line\'s growth stays within 2 points of GDP growth (for a line that ends, the year it stops growing faster). "Term" says whether it is permanent or ends. F = paid by a dedicated fund, outside the general-fund gap.\n')
    for g in ORDER:
        rows = sorted([s for s in S if s['group'] == g], key=lambda s: -s['hump'])
        if not rows: continue
        L.append(f'### {g}\n'); L.append(hdr)
        for s in rows:
            tag = ' (F)' if s['fund'] else ''
            term = s['kind']
            if s['below']: term += '; below the cut'
            L.append(f"| {sid(s['id'])}{tag} | {s['name']} | " + ' | '.join(fmt(s['vals'][t]) for t in SHOW) + f" | {fmt(s['tot3039'])} | {s['start'] or '-'} | {s['full'] or '-'} | {term} |")
        L.append('')
    L.append('## 2. Revenue lines of at least $20B in FY2040 (either sign)\n')
    L.append('Positive = more receipts; negative = receipts lost or an offset. "Middle class" is a reading of each line\'s definition, not a model output; the ledger\'s `reaches_middle` flag is quoted where the line has an ID in it.\n')
    L.append('| ID | Line | ' + ' | '.join(f'FY{t}' for t in SHOW) + ' | FY2030-39 | Start | Full | Falls on the middle class? |\n|---|---|' + '---:|' * (len(SHOW) + 1) + '---|---|---|')
    for r in sorted(D['revl'], key=lambda r: -abs(r['vals'][2040])):
        tag = ' (F)' if r['fund'] else ''
        L.append(f"| {sid(r['id'])}{tag} | {r['name']} | " + ' | '.join(fmt(r['vals'][t]) for t in SHOW) + f" | {fmt(r['tot3039'])} | {r['start'] or '-'} | {r['full'] or '-'} | {r['middle']} |")
    cv = D['carbon']
    L.append('\nCarbon fee receipts (REV-C1 plus REV-C2, gross), which sit inside the "matched dedicated receipts" gross-up and are not a line of their own in the audit. '
             'Recomputed from the model\'s carbon table (`u.carbon`, FY2030-39) and its post-2039 rule (GDP growth less 2% a year). Ledger: reaches the middle class, YES (C1, C2). Offset line CX is in the table above.\n')
    L.append('| ' + ' | '.join(f'FY{t}' for t in SHOW) + ' |\n|' + '---:|' * len(SHOW))
    L.append('| ' + ' | '.join(fmt(cv[t]) for t in SHOW) + ' |\n')
    # revenue-side spending offsets
    L.append('## 3. Settlement lines that reduce spending (negative outlay of at least $5B in any hump year or FY2040)\n')
    L.append('These are in the booked case as explicit adjustments; they net against the lines above in each group. Spending lines in section 1 are before them.\n')
    L.append('| Line | Group | ' + ' | '.join(f'FY{t}' for t in SHOW) + ' |\n|---|---|' + '---:|' * len(SHOW))
    for l, y in sorted(D['out'].items()):
        if l.startswith(('Settlement', 'Smaller capacity')) and min(y.get(t, 0) for t in HUMP + (2040,)) <= -5:
            L.append(f"| {l[:110]} | {group_of(l)} | " + ' | '.join(fmt(y.get(t, 0)) for t in SHOW) + ' |')
    L.append('')
    # flagship totals
    L.append('## 4. Flagship totals (all audit spending lines mapped to the group, before settlement reductions)\n')
    L.append('Sums every positive-or-negative outlay line the mapping puts in the group, small lines included; fund lines (F) are kept in the totals and shown separately. $B.\n')
    L.append('| Group | ' + ' | '.join(f'FY{t}' for t in SHOW) + ' | FY2030-39 |\n|---|' + '---:|' * (len(SHOW) + 1))
    for g in ORDER:
        ls = [l for l in D['out'] if l not in SKIP and not l.startswith(('Settlement', 'Smaller capacity', 'Exploratory', 'SSA OASDI', 'SMI ', 'HOU-4A', '2029 delivery', 'Downside', 'Recovery credit', 'HI H1a')) and group_of(l) == g]
        if not ls: continue
        L.append(f'| {g} | ' + ' | '.join(fmt(sum(D['out'][l].get(t, 0) for l in ls)) for t in SHOW) + f" | {fmt(sum(D['out'][l].get(t, 0) for l in ls for t in range(2030, 2040)))} |")
    L.append('')
    return L


def hump(D):
    L = []; o, d, gf = D['out'], D['deficit'], D['gf']
    L.append('### The general-fund gap, by year ($B; positive = shortfall; the model\'s `agenda_gf_primary_bn`)\n')
    ys = (2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041)
    L.append('| ' + ' | '.join(f'FY{t}' for t in ys) + ' |\n|' + '---:|' * len(ys))
    L.append('| ' + ' | '.join(fmt(gf[t]) for t in ys) + ' |\n')
    L.append('### Spending lines that step up or grow fastest ($B; non-fund lines first)\n')
    L.append('Step = FY2036 less FY2035. Growth = FY2039 less FY2036. Ranked by step plus growth, lines with at least $2B of either.\n')
    L.append('| ID | Line | FY2034 | FY2035 | FY2036 | Step into FY2036 | FY2039 | Growth FY2036-39 | Growth % | FY2040 less FY2039 |\n|---|---|---:|---:|---:|---:|---:|---:|---:|---:|')
    rows = []
    nm = {s['id']: s for s in D['spend']}
    for l, y in o.items():
        if l in SKIP or l.startswith(('Settlement', 'Smaller')): continue
        step = y.get(2036, 0) - y.get(2035, 0); gr = y.get(2039, 0) - y.get(2036, 0)
        if abs(step) >= 2 or abs(gr) >= 2: rows.append((l, y, step, gr))
    for l, y, step, gr in sorted(rows, key=lambda r: -(r[2] + r[3]))[:20]:
        pct = 100 * gr / y[2036] if y.get(2036) else float('nan')
        L.append(f"| {sid(l)}{' (F)' if l in FUND_LINES else ''} | {NAMES.get(l) or (nm[l]['name'] if l in nm else l[:50])} | {fmt(y.get(2034, 0))} | {fmt(y.get(2035, 0))} | {fmt(y.get(2036, 0))} | {fmt(step)} | {fmt(y.get(2039, 0))} | {fmt(gr)} | {pct:.1f}% | {fmt(y.get(2040, 0) - y.get(2039, 0))} |")
    L.append('\n### Lines that fall away just before or inside the hump (spending that ends)\n')
    L.append('| ID | Line | FY2033 | FY2034 | FY2035 | FY2036 | FY2039 | FY2040 |\n|---|---|---:|---:|---:|---:|---:|---:|')
    for l, y in sorted(o.items(), key=lambda kv: kv[1].get(2035, 0) - kv[1].get(2036, 0), reverse=True)[:8]:
        if l in SKIP or l.startswith(('Settlement', 'Smaller')): continue
        L.append(f"| {sid(l)} | {NAMES.get(l) or (nm[l]['name'] if l in nm else l[:50])} | " + ' | '.join(fmt(y.get(t, 0)) for t in (2033, 2034, 2035, 2036, 2039, 2040)) + ' |')
    L.append('\n### Revenue lines that step up or down into FY2036 ($B)\n')
    r = D['rev']; rr = []
    for l, y in r.items():
        step = y.get(2036, 0) - y.get(2035, 0)
        if l not in SKIP and abs(step) >= 15: rr.append((l, y, step))
    L.append('| Line | FY2034 | FY2035 | FY2036 | Step | FY2039 |\n|---|---:|---:|---:|---:|---:|')
    for l, y, step in sorted(rr, key=lambda t: t[2]):
        L.append(f"| {REV_NAMES.get(l, l)[:80]} | " + ' | '.join(fmt(y.get(t, 0)) for t in (2034, 2035, 2036)) + f" | {fmt(step)} | {fmt(y.get(2039, 0))} |")
    # decomposition of the GF gap change by group, non-fund lines, remainder = fund net
    L.append('\n### What moves the general-fund gap, by group ($B, change in primary deficit, non-fund lines; the fund remainder is by difference)\n')
    gsum = collections.defaultdict(lambda: collections.defaultdict(float))
    for l, y in d.items():
        if l in SKIP or l in FUND_LINES: continue
        g = group_of(l) if not (l in D['rev'] and max(abs(v) for v in o.get(l, {0: 0}).values()) == 0 and not l.startswith('Settlement')) else 'Small revenue lines (under $20B in FY2040)'
        if l in HEALTH_FIN or l.startswith('Settlement S03') or l.startswith('Settlement S06'): g = 'Health financing (HX, HCU, HEC, HEX, HCW, HCA, HCH, HS1-4, H1a, H1b, S03, S06)'
        elif l.startswith('HLT-'): g = 'Health spending (HLT-1 to HLT-11, gross)'
        elif l in ('G1', 'G3', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'GX', 'CX', 'MR6', 'C18', 'C35', 'C38', 'C39', 'C43', 'C3A', 'C1T') or l.startswith(('New indexed', 'IRS yield', 'Settlement S04')): g = 'Other revenue lines (taxes, carbon offsets, IRS)'
        for t, v in y.items(): gsum[g][t] += v
    tot = collections.defaultdict(float)
    for g in gsum:
        for t, v in gsum[g].items(): tot[t] += v
    gsum['Dedicated funds (SS, HI, education, paid leave), net, by difference'] = {t: D['gf'][t] - tot[t] for t in D['gf']}
    cols = (2035, 2036, 2037, 2038, 2039, 2040)
    L.append('| Group | ' + ' | '.join(f'FY{t}' for t in cols) + ' | Step into FY2036 | Change FY2036-39 |\n|---|' + '---:|' * (len(cols) + 2))
    for g, v in sorted(gsum.items(), key=lambda kv: -abs(kv[1].get(2036, 0) - kv[1].get(2035, 0))):
        L.append(f'| {g} | ' + ' | '.join(fmt(v.get(t, 0)) for t in cols) + f" | {fmt(v.get(2036, 0) - v.get(2035, 0))} | {fmt(v.get(2039, 0) - v.get(2036, 0))} |")
    L.append('| **General-fund gap (sum)** | ' + ' | '.join(fmt(D['gf'][t]) for t in cols) + f" | {fmt(D['gf'][2036] - D['gf'][2035])} | {fmt(D['gf'][2039] - D['gf'][2036])} |")
    # net health
    L.append('\n### Health, net: gross spending less the health financing lines ($B; positive = health costs the general fund more than it raises)\n')
    L.append('| | ' + ' | '.join(f'FY{t}' for t in SHOW) + ' |\n|---|' + '---:|' * len(SHOW))
    hs = {t: sum(v.get(t, 0) for l, v in o.items() if l.startswith('HLT-')) for t in range(2026, 2057)}
    hf = {t: sum(D['rev'].get(l, {}).get(t, 0) for l in HEALTH_FIN) + sum(v.get(t, 0) for k, v in D['rev'].items() if k.startswith(('Settlement S03', 'Settlement S06'))) for t in range(2026, 2057)}
    L.append('| Health spending (HLT lines) | ' + ' | '.join(fmt(hs[t]) for t in SHOW) + ' |')
    L.append('| Health financing lines | ' + ' | '.join(fmt(hf[t]) for t in SHOW) + ' |')
    L.append('| Net | ' + ' | '.join(fmt(hs[t] - hf[t]) for t in SHOW) + ' |\n')
    L.append('The health financing set is HX, HCU, HEC, HEX, HCW, HCA, HCH, HS1-HS4, H1a, H1b and settlement S03 and S06. Lines that also appear as '
             'general revenue (G-rows) are not counted here. This is a reading of the audit, not a model total.\n')
    return L


def top10(D):
    S = sorted(D['spend'], key=lambda s: -s['hump'])
    return [(s['id'], s['hump'], s['fund']) for s in S[:10]]


def main():
    D = build()
    if '--json' in sys.argv:
        print(json.dumps(dict(spend=[{k: v for k, v in s.items()} for s in D['spend']], revenue=D['revl'], gf=D['gf'], carbon=D['carbon'], top10=top10(D)), indent=1, default=str))
        return
    part = sys.argv[sys.argv.index('--part') + 1] if '--part' in sys.argv else 'all'
    if part in ('all', 'tables'): print('\n'.join(tables(D)))
    if part in ('all', 'hump'): print('\n'.join(hump(D)))
    if part in ('all', 'top'):
        print('\nTop 10 by FY2036-39 cost (sum of the four years, $B):\n')
        print('| # | Line | FY2036-39 total |\n|---|---|---:|')
        for i, (l, v, fd) in enumerate(top10(D), 1): print(f"| {i} | {sid(l)}{' (F)' if fd else ''} | {v:,.1f} |")
        ex = [t for t in top10x(D)]
        print('\nTop 10 without the single plan\'s gross line and without fund lines (the general-fund view):\n')
        print('| # | Line | FY2036-39 total |\n|---|---|---:|')
        for i, (l, v) in enumerate(ex, 1): print(f'| {i} | {sid(l)} | {v:,.1f} |')


def top10x(D):
    S = sorted([s for s in D['spend'] if not s['fund'] and s['id'] != 'HLT-7'], key=lambda s: -s['hump'])
    return [(s['id'], s['hump']) for s in S[:10]]


if __name__ == '__main__':
    main()
