#!/usr/bin/env python3
"""Build the public edition and its separate analytical companion from pinned evidence.

No model execution. --check verifies outputs. --review-ref REF reports which public
records need review when repository evidence changes; it never rewrites claims.
"""
import argparse
import csv
import hashlib
import html
import json
import re
from pathlib import Path
from string import Template
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = ROOT / 'index/public-2050'
esc = html.escape
MODEL_SOURCES = ['index/data/fiscal-paths.csv', 'index/fiscal-long-term-model.md',
                 'index/tools/readme.md', 'sources/family-comparison-model-checks.json',
                 'index/tools/child-poverty/adopted-package.json']
AUTHORITY = ['governing/project-charter.md', 'governing/project-2050-governing-decisions.md']


def domain_path(key):
    if key == 'transportation':
        return 'domains/transportation-moving-america-act-2031-draft-2.md'
    return f'domains/domain-{key}.md'


def content_map(content):
    """Explicit editorial -> policy -> evidence graph; names never substitute for IDs."""
    policies = content['policies']
    records = {}
    for scene in content['stops']:
        ids = sorted({pid for step in scene['steps'] for pid in step['policy_ids']})
        if any(pid not in policies for pid in ids):
            raise ValueError(f'Unknown policy reference in {scene["id"]}')
        paths = {p[0] for p in scene['sources']} | {policies[pid]['path'] for pid in ids} | set(AUTHORITY)
        records['scene:'+scene['id']] = {'public_url':'index.html#'+scene['id'],
            'analysis_url':'analysis.html#'+scene['id'], 'policy_ids':ids,
            'source_paths':sorted(paths), 'step_ids':[step['id'] for step in scene['steps']]}
    for theme in content['themes']:
        records['theme:'+theme['id']] = {'public_url':'index.html#theme-'+theme['id'],
            'source_paths':sorted([domain_path(d[0]) for d in theme['domains']] + AUTHORITY)}
    for section in ['vision', 'goals', 'movement']:
        records['section:'+section] = {'public_url':'index.html#'+section, 'source_paths':AUTHORITY}
    records['analysis:models'] = {'public_url':'analysis.html#models', 'source_paths':MODEL_SOURCES + AUTHORITY}
    return {'schema_version':1, 'source_commit':content['source_commit'],
            'editorial_date':content['edition_date'], 'policies':policies, 'records':records}


def source_paths(mapping):
    return sorted({p for record in mapping['records'].values() for p in record['source_paths']})


def review_changes(content, target):
    mapping = content_map(content)
    # Resolve refs as commit objects, without allowing options to become Git arguments.
    commit = subprocess.check_output(['git','rev-parse','--verify', '--end-of-options',target+'^{commit}'], cwd=ROOT, text=True).strip()
    changed = subprocess.check_output(['git','diff','--name-only',content['source_commit'],commit,'--'], cwd=ROOT, text=True).splitlines()
    affected = {key:{'url':record['public_url'], 'changed_sources':sorted(set(record['source_paths']) & set(changed))}
                for key,record in mapping['records'].items() if set(record['source_paths']) & set(changed)}
    return {'source_commit':content['source_commit'], 'target_commit':commit,
            'changed_sources':sorted(set(changed) & set(source_paths(mapping))), 'review_required':affected,
            'action':'Review affected wording and model contracts before explicitly advancing source_commit; no automatic publication.'}


def build():
    content = json.loads((HERE/'content.json').read_text())
    ref = content['source_commit']
    if not re.fullmatch(r'[0-9a-f]{40}', ref):
        raise ValueError('source_commit must be a full commit SHA')
    mapping = content_map(content)
    hashes = {}
    for path in source_paths(mapping):
        data = (ROOT/path).read_bytes()
        pinned = subprocess.check_output(['git','show',f'{ref}:{path}'], cwd=ROOT)
        if data != pinned:
            affected = [key for key,r in mapping['records'].items() if path in r['source_paths']]
            raise ValueError(f'Source changed: {path}; review {", ".join(affected)} before advancing source_commit')
        hashes[path] = hashlib.sha256(data).hexdigest()
    for pid, policy in content['policies'].items():
        text = (ROOT/policy['path']).read_text()
        if policy['marker'] not in text or (policy.get('selected_option') and policy['selected_option'] not in text):
            raise ValueError(f'Canonical reference missing: {pid}')
    with (ROOT/'index/data/fiscal-paths.csv').open() as f:
        fiscal = [r for r in csv.DictReader(f) if r['scenario']=='DEC' and r['year']=='2040']
    if len(fiscal) != 1:
        raise ValueError('Expected one FY2040 DEC result')
    gap = float(fiscal[0]['gf_primary'])
    if gap <= 0:
        raise ValueError('Financing analysis needs editorial review: no longer a positive gap')
    results = json.loads((ROOT/'sources/family-comparison-model-checks.json').read_text())
    selected = json.loads((ROOT/'index/tools/child-poverty/adopted-package.json').read_text())
    if selected != results['adopted_package'] or selected['credit_policy']!='FAM-1D' or selected['new_voucher_awards']!=1000000:
        raise ValueError('Adopted package and aggregate results need reconciliation')
    cases = results['adopted_cases']
    if results['source_income_year']!=2025 or results['valuation_year']!=2034 or [c['delivery'] for c in cases]!=['moderate','enhanced','full']:
        raise ValueError('Poverty comparison vintage or case meanings changed')
    if not all(c['award_cap']==1000000 and c['design']=='AFA_2025_real' for c in cases):
        raise ValueError('Poverty cases do not match the selected annual analogue')
    stops = content['stops']
    ids = [s['id'] for s in stops]
    if len(set(ids))!=len(ids) or not all(r in ids for s in stops for r in s['related']):
        raise ValueError('Invalid scene navigation')
    if not all(g['stop'] in ids for g in content['outcomes']):
        raise ValueError('Goal lacks a scene destination')
    base = f'https://github.com/fm58cn6g4d-stack/project-2050/blob/{ref}/'

    def source_link(path, label):
        return f'<a href="{base}{esc(path, quote=True)}">{esc(label)}</a>'

    def place_link(stop, on_map=False):
        label = stop['number'] if on_map else f'<b>{stop["number"]}</b> {esc(stop["place"])}'
        return f'<a class="{"map-link" if on_map else "stop-link"}" data-stop="{stop["id"]}" href="#{stop["id"]}" aria-label="{esc(stop["place"])}">{label}</a>'

    chapters = []
    analysis_sections = []
    for s in stops:
        steps = ''.join(f'<li id="step-{s["id"]}-{step["id"]}" data-policy-ids="{esc(" ".join(step["policy_ids"]))}"><h3>{esc(step["title"])}</h3><p>{esc(step["body"])}</p></li>' for step in s['steps'])
        related = ''.join(place_link(next(t for t in stops if t['id']==rid)) for rid in s['related'])
        chapters.append(f'''<article class="chapter" id="{s['id']}" aria-labelledby="title-{s['id']}">
<p class="eyebrow">{s['number']} / {esc(s['place'])}</p><h2 id="title-{s['id']}" tabindex="-1">{esc(s['title'])}</h2>
<span class="tag">Imagine 2050 · an illustrative scene</span><p class="scene">{esc(s['scene'])}</p>
<p>{esc(s['connection'])}</p><h3 class="small-title">How the choices work together</h3><ol class="policy-steps">{steps}</ol>
<div class="lived-test"><h3>What progress would mean</h3><p>{esc(s['lived_test'])}</p></div>
<details class="evidence"><summary>Explore the policies behind this story</summary><p>Read the supporting explanation and evidence for these proposals, including the conditions that matter for their success.</p>
<a href="analysis.html#{s['id']}">Read about {esc(s['place'].lower())} in the analysis →</a></details>
<div class="related"><span>Follow the connection →</span>{related}</div></article>''')
        source_list = ''.join(f'<li>{source_link(path,label)}<small>{esc(kind)}</small></li>' for path,label,kind in s['sources'])
        policy_list = ''.join(f'<li data-policy-id="{pid}">{source_link(content["policies"][pid]["path"],content["policies"][pid]["name"])}</li>' for pid in mapping['records']['scene:'+s['id']]['policy_ids'])
        # Historical identifiers remain in structured records; analytical notes may use them.
        analysis_sections.append(f'''<section class="section analysis-section" id="{s['id']}"><p class="eyebrow">{esc(s['place'])}</p><h2>{esc(s['title'])}</h2>
<p class="section-intro">{esc(s['connection'])}</p><h3>Policy designs supporting the story</h3><ul class="policy-index">{policy_list}</ul>
<details class="technical"><summary>Research questions and delivery conditions</summary><p>{esc(s['analysis_notes'])}</p></details>
<h3>Evidence and further reading</h3><ul class="sources">{source_list}</ul><p><a href="index.html#{s['id']}">Return to the story →</a></p></section>''')
    principles = ''.join(f'<article><span class="principle-number">0{i+1}</span><h3>{esc(p["title"])}</h3><p>{esc(p["body"])}</p></article>' for i,p in enumerate(content['principles']))
    goals = ''.join(f'<a class="goal" data-stop="{g["stop"]}" href="#{g["stop"]}"><h3>{esc(g["title"])}</h3><p>{esc(g["body"])}</p><span>Explore this future <span aria-hidden="true">↗</span></span></a>' for g in content['outcomes'])
    movement = ''.join(f'<li><h3>{esc(m["title"])}</h3><p>{esc(m["body"])}</p></li>' for m in content['movement'])
    themes = []
    analytic_themes = []
    for theme in content['themes']:
        urls = ''.join(f'<li>{source_link(domain_path(key),label)}</li>' for key,label in theme['domains'])
        public_names = ''.join(f'<li>{esc(label)}</li>' for _,label in theme['domains'])
        themes.append(f'<details id="theme-{theme["id"]}"><summary>{esc(theme["title"])}</summary><p>{esc(theme["body"])}</p><ul>{public_names}</ul><a href="analysis.html#theme-{theme["id"]}">Explore these policy areas →</a></details>')
        analytic_themes.append(f'<section id="theme-{theme["id"]}" class="theme-analysis"><h3>{esc(theme["title"])}</h3><p>{esc(theme["body"])}</p><ul>{urls}</ul></section>')
    css = (HERE/'style.css').read_text()
    page = Template((HERE/'site.html').read_text()).substitute(
        style=css, principles=principles, goals=goals, illustration=(HERE/'community.svg').read_text(),
        map_links=''.join(place_link(s,True) for s in stops), place_links=''.join('<li>'+place_link(s)+'</li>' for s in stops),
        chapters=''.join(chapters), movement=movement, themes=''.join(themes), edition=content['edition_date'],
        script=(HERE/'interaction.js').read_text())
    rows = ''.join(f'<tr><th scope="row">{esc(c["delivery"].capitalize())}</th><td>{100*c["result"]["poor_rate"]:.2f}%</td><td>{100*c["result"]["deep_poor_rate"]:.2f}%</td></tr>' for c in cases)
    poverty = f'''<div class="table-scroll"><table><caption>Selected channels under three delivery assumptions</caption><thead><tr><th scope="col">Research case</th><th scope="col">Child poverty</th><th scope="col">Deep poverty</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Same-scenario baseline: {100*cases[0]['baseline']['poor_rate']:.2f}% child poverty using the Supplemental Poverty Measure, which considers resources after taxes and transfers and certain necessary expenses. Deep poverty means resources below half the poverty threshold.</p>
<p>These are conditional results for credit, care/pre-K expense relief, meals and housing channels using 2025 source income and a 2034 valuation reference. They are not forecasts of 2050, full-agenda effects or adopted delivery rates. They do not include the full health, paid-leave, tax or earnings effects of the agenda.</p>
<p>The annual American Family Act analogue, eligibility proxies and assumed receipt and lease-up limit the comparison. Conditional sampling intervals in the results exclude model uncertainty. Ending child poverty remains a goal, not a finding established by these experiments.</p><p>{source_link('sources/family-comparison-model-checks.json','Inspect aggregate results, assumptions and sampling uncertainty')}</p>'''
    analysis = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Policies and evidence · Project 2050</title><style>{css}</style></head><body>
<a class="skip" href="#analysis">Skip to the analysis</a><header><div class="shell header"><a class="brand" href="index.html"><span class="brand-mark">2050</span>Project 2050</a><nav aria-label="Main"><a href="index.html">The public vision</a><a href="#models">Models &amp; funding</a><a href="#sources">All policy areas</a></nav></div></header>
<main class="analysis-shell" id="analysis"><p class="eyebrow">The work behind the vision</p><h1>Policies you can examine.<br>A program you can question.</h1>
<p class="section-intro">The public vision explains what we are trying to achieve. Here you can examine the designs, evidence and assumptions behind it. Selected project policies are proposals, not enacted law or benefits available through this site.</p>
<nav class="analysis-nav" aria-label="Analysis topics">{''.join(f'<a href="#{s["id"]}">{esc(s["place"])}</a>' for s in stops)}</nav>
{''.join(analysis_sections)}
<section id="models" class="section"><p class="eyebrow">Inspecting the analytical foundation</p><h2>What the models can—and cannot—tell us.</h2>
<p>Model results answer particular questions under particular assumptions. A household effect, a federal budget cost and a legislative timetable are different things; they should not be added together or treated as one forecast.</p>
<details class="model-details" id="poverty"><summary>What the child-poverty experiments show</summary>{poverty}</details>
<details class="model-details" id="funding"><summary>How the funding strategy is being assessed</summary>
<p>The program’s fiscal rule calls for permanent programs to be funded at maturity and afterward. Financing strategy remains under holistic redesign; none of the three recent financing illustrations has been selected.</p>
<p>The current working case shows a <strong>FY2040 general-fund primary gap of ${gap:.2f} billion</strong> in nominal dollars. That is about {100*gap/float(fiscal[0]['gdp']):.2f}% of modeled GDP. It is a fiscal-model finding, not a measure of the whole program’s value or an official score. It does not establish that the agenda is fully financed.</p>
<p>The existing agency-surge cash profile remains a proxy, and some costs remain unpriced. These questions belong in the continuing funding and distributional analysis.</p>
<p>{source_link('index/fiscal-long-term-model.md','Read the long-term fiscal analysis')} · {source_link('governing/project-2050-governing-decisions.md','Read the selected policy and fiscal rules')}</p></details>
<p>{source_link('index/tools/readme.md','Models, methods and reproduction commands')}</p></section>
<section id="sources" class="section"><h2>The wider policy program</h2><p>Each link opens the canonical policy home at this edition’s source version. These documents distinguish selected designs from alternatives and supporting research.</p>{''.join(analytic_themes)}</section>
<section id="edition" class="section"><h2>About this edition</h2><p>Public wording and policy references are maintained together in GitHub. The publishing tools identify stories affected by a source change for editorial review before a new edition is built.</p>
<p>Source commit: <code>{ref}</code>. Editorial edition: {content['edition_date']}. Repository documents may require GitHub access. The explanations here remain readable without it.</p>
<p><a href="public-map.json">Structured story and policy references</a> · <a href="manifest.json">Source and build hashes</a> · <a href="directions.html">Original design treatments</a></p></section></main>
<footer><div class="shell"><a href="index.html">Return to the public vision</a> · Working edition · {content['edition_date']}</div></footer></body></html>'''
    outputs = {'index.html':page.encode(), 'analysis.html':analysis.encode(),
               'directions.html':(HERE/'directions.html').read_text().replace('{{STYLE}}',css).encode(),
               'public-map.json':(json.dumps(mapping,indent=2,ensure_ascii=False)+'\n').encode()}
    for p in sorted(HERE.iterdir()):
        if p.is_file() and p.suffix in {'.py','.json','.css','.js','.cjs','.svg','.html','.md'}:
            hashes[str(p.relative_to(ROOT))] = hashlib.sha256(p.read_bytes()).hexdigest()
    manifest = {'schema_version':2, 'status':'working_public_edition_not_deployed', 'source_commit':ref,
        'edition_date':content['edition_date'], 'editorial_mapping':'public-map.json',
        'numeric_contracts':{
            'fiscal_gap':{'view':'analysis.html#funding','path':'index/data/fiscal-paths.csv','selector':{'scenario':'DEC','year':'2040'},'field':'gf_primary','unit':'nominal USD billion','positive':'deficit','value':gap,'gdp_share_percent':100*gap/float(fiscal[0]['gdp'])},
            'poverty':{'view':'analysis.html#poverty','path':'sources/family-comparison-model-checks.json','selector':'adopted_cases','source_income_year':2025,'valuation_year':2034,'kind':'conditional_selected_channels_not_forecast'}},
        'sha256':hashes, 'outputs_sha256':{k:hashlib.sha256(v).hexdigest() for k,v in outputs.items()}}
    outputs['manifest.json'] = (json.dumps(manifest,indent=2,sort_keys=True)+'\n').encode()
    return outputs


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    mode=parser.add_mutually_exclusive_group()
    mode.add_argument('--check',action='store_true')
    mode.add_argument('--review-ref',metavar='REF')
    args=parser.parse_args()
    if args.review_ref:
        print(json.dumps(review_changes(json.loads((HERE/'content.json').read_text()),args.review_ref),indent=2))
    else:
        products=build()
        if args.check:
            stale=[name for name,data in products.items() if not (OUT/name).exists() or (OUT/name).read_bytes()!=data]
            if stale: raise SystemExit('Stale products: '+', '.join(stale))
            print('Public edition: generated bytes, mappings and pinned evidence verified')
        else:
            OUT.mkdir(parents=True,exist_ok=True)
            for name,data in products.items(): (OUT/name).write_bytes(data)
            print('Built '+', '.join(products))
