#!/usr/bin/env python3
"""Build the public story page: illustrated essays with a claim register.

Reads essays.json, story.css and the SVG art in this folder. Every claim must name repository
sources and exact anchor passages; every figure in an essay paragraph must belong to a claim
that the paragraph cites. No model execution.

  python3 models/tools/public-product/story/build_story.py            # write outputs
  python3 models/tools/public-product/story/build_story.py --check    # verify outputs and claims
  python3 models/tools/public-product/story/build_story.py --report   # as --check, but only warn on moved passages
  python3 models/tools/public-product/story/build_story.py --review-ref origin/main

Evidence links point to the pinned source_commit. Their line numbers come from that commit and are kept
in anchors.lock.json, so later edits elsewhere in the repository do not change the generated page.
"""
import argparse
import hashlib
import html
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = ROOT / 'public/site'
REGISTER_MD = ROOT / 'legacy/sources/public-story-claim-register.md'
LOCK = HERE / 'anchors.lock.json'
REPO = 'https://github.com/fm58cn6g4d-stack/project-2050/blob/'
MARK = re.compile(r'\{c:([a-z0-9-]+)\}')
MARK_RUN = re.compile(r'(?:\{c:[a-z0-9-]+\})+')
NUMBER = re.compile(r'\d+(?:[.,]\d+)*')
# Figures that are part of the project's name rather than claims.
FREE_NUMBERS = {'2050'}
esc = html.escape


class ClaimError(ValueError):
    pass


def is_drift(problem):
    """A cited source passage or policy marker moved or changed: an editorial review signal, not a content error.

    Everything else (uncited figures, wrong rounding, unknown references, structure) is a content error and
    always fails, in report mode too.
    """
    return (problem.startswith('policy ') and ': marker ' in problem) or ': anchor not found in ' in problem


def numbers(text):
    return set(NUMBER.findall(text))


def strip_marks(text):
    return MARK.sub('', text)


def load(content_path=None):
    return json.loads((content_path or HERE / 'essays.json').read_text())


# Claims cite paths as they were at the pinned commits. The October 28 reset moved them (charter/STANDARDS.md).
MOVED = (('index/tools/', 'models/tools/'), ('index/data/', 'models/data/'), ('index/public-2050/', 'public/site/'))


def current_path(path, root=ROOT):
    """Today's repository path for a path cited at a pinned commit."""
    if (root / path).exists():
        return path
    for old, new in MOVED:
        if path.startswith(old):
            return new + path[len(old):]
    return 'legacy/' + path


def locate(root, path, anchor):
    """Return the 1-based line of an exact anchor passage, or None."""
    file = root / current_path(path, root)
    if not file.is_file():
        return None
    text = file.read_text()
    at = text.find(anchor)
    return None if at < 0 else text.count('\n', 0, at) + 1


def anchor_key(path, anchor):
    return f'{path}#{hashlib.sha256(anchor.encode()).hexdigest()[:16]}'


def source_ref(content, src):
    """The commit a source passage is pinned to: the evidence snapshot, or this edition's own research record."""
    return content['evidence_commit'] if src.get('pin') == 'evidence' else content['source_commit']


def pinned_lines(content):
    """Line of every claim passage in its pinned commit, from the lock or from Git."""
    wanted = {anchor_key(s['path'], s['anchor']): (source_ref(content, s), s['path'], s['anchor'])
              for c in content['claims'].values() for s in c['sources']}
    # Policy links point to files at the evidence snapshot; their markers prove those files exist there.
    wanted.update({anchor_key(p['path'], p['marker']): (content['source_commit'], p['path'], p['marker'])
                   for p in content['policies'].values()})
    if LOCK.exists():
        lock = json.loads(LOCK.read_text())
        if (lock['source_commit'] == content['source_commit'] and lock.get('evidence_commit') == content.get('evidence_commit')
                and set(lock['lines']) == set(wanted)):
            return lock['lines']
    lines, texts = {}, {}
    for key, (ref, path, anchor) in sorted(wanted.items()):
        if (ref, path) not in texts:
            try:
                texts[ref, path] = subprocess.check_output(['git', 'show', f'{ref}:{path}'], cwd=ROOT,
                                                      stderr=subprocess.DEVNULL).decode()
            except subprocess.CalledProcessError:
                raise ClaimError(f'anchors.lock.json is out of date and {ref[:12]}:{path} is not available; '
                                 'fetch the pinned commit and rebuild')
        at = texts[ref, path].find(anchor)
        if at < 0:
            raise ClaimError(f'passage not in pinned commit {ref[:12]}: {path}: {anchor[:70]!r}')
        lines[key] = texts[ref, path].count('\n', 0, at) + 1
    return lines


def prose(essay):
    """(where, text) for every piece of reading text, in either essay format.

    A plain essay has `body` paragraphs. A brief has `blocks`: {"h": heading}, {"p": paragraph},
    {"points": [the argument in brief]}, {"quote": pull quote}, {"objection": ..., "answer": [...]},
    and {"figure": diagram id}.
    """
    if 'body' in essay:
        return [(f'paragraph {i+1}', p) for i, p in enumerate(essay['body'])]
    out = []
    for i, b in enumerate(essay['blocks']):
        where = f'block {i+1}'
        if 'h' in b:
            out.append((where + ' heading', b['h']))
        elif 'p' in b:
            out.append((where, b['p']))
        elif 'quote' in b:
            out.append((where + ' quote', b['quote']))
        elif 'points' in b:
            out += [(f'{where} point {k+1}', t) for k, t in enumerate(b['points'])]
        elif 'objection' in b:
            out.append((where + ' objection', b['objection']))
            out += [(f'{where} answer {k+1}', t) for k, t in enumerate(b['answer'])]
    return out


def word_count(essay):
    return len(strip_marks(' '.join(t for w, t in prose(essay) if 'heading' not in w)).split())


def validate(content, root=ROOT):
    """Return (claim locations, problems). Problems are claim-tracing failures."""
    problems = []
    policies, claims = content['policies'], content['claims']
    if not re.fullmatch(r'[0-9a-f]{40}', content['source_commit']):
        problems.append('source_commit must be a full commit SHA')
    for pid, policy in policies.items():
        line = locate(root, policy['path'], policy['marker'])
        if line is None:
            problems.append(f'policy {pid}: marker {policy["marker"]!r} not found in {policy["path"]}')
    locations = {}
    for cid, claim in claims.items():
        if not claim.get('sources'):
            problems.append(f'claim {cid}: no source')
        for pid in claim.get('policy_ids', []):
            if pid not in policies:
                problems.append(f'claim {cid}: unknown policy {pid}')
        found = []
        for src in claim['sources']:
            line = locate(root, src['path'], src['anchor'])
            if line is None:
                problems.append(f'claim {cid}: anchor not found in {src["path"]}: {src["anchor"][:70]!r}')
            found.append(line)
        locations[cid] = found
        anchored = set().union(*(numbers(s['anchor']) for s in claim['sources']))
        for r in claim.get('rounded', []):
            # A displayed figure rounded from an anchored raw value, e.g. a model share shown as a percent.
            shown = f'{float(r["value"]) * r["scale"]:.{r["places"]}f}'
            if r['value'] not in anchored or numbers(r['figure']) != {shown}:
                problems.append(f'claim {cid}: rounded figure {r["figure"]!r} does not follow from {r["value"]}')
            else:
                anchored = anchored | {shown}
        for fig in claim.get('figures', []):
            # A figure must appear, digit for digit, in at least one anchor passage.
            if not numbers(fig) <= anchored | FREE_NUMBERS:
                problems.append(f'claim {cid}: figure {fig!r} not in its anchors')
        for year, value in claim.get('series', []):
            if not {str(year), f'{value:,}'} <= anchored:
                problems.append(f'claim {cid}: series point {year}={value} not in its anchors')
    used = set()
    ids = [e['id'] for e in content['essays']]
    if len(ids) != len(set(ids)):
        problems.append('duplicate essay id')
    for essay in content['essays']:
        for pid in essay['policy_ids']:
            if pid not in policies:
                problems.append(f'essay {essay["id"]}: unknown policy {pid}')
        blocks = prose(essay) + [('limits', essay['limits'])]
        if 'blocks' in essay:
            ids = {d['id'] for d in essay.get('diagrams', [])}
            placed = [b['figure'] for b in essay['blocks'] if 'figure' in b]
            if sorted(placed) != sorted(ids):
                problems.append(f'essay {essay["id"]}: each diagram must be placed exactly once')
        for diagram in essay.get('diagrams', []):
            drawn = svg_text(diagram['file']) if diagram.get('file') else ''
            blocks.append((f'diagram {diagram["id"]}', diagram['caption'] + ' ' + drawn +
                           ''.join(f'{{c:{c}}}' for c in diagram['claims'])))
        for where, text in blocks:
            cited = MARK.findall(text)
            for cid in cited:
                if cid not in claims:
                    problems.append(f'essay {essay["id"]} {where}: unknown claim {cid}')
            used.update(cited)
            allowed = set(FREE_NUMBERS)
            for cid in cited:
                if cid in claims:
                    allowed |= set().union(*(numbers(f) for f in claims[cid].get('figures', [])), set())
                    allowed |= {str(y) for y, _ in claims[cid].get('series', [])}
                    allowed |= {f'{v:,}' for _, v in claims[cid].get('series', [])}
            loose = numbers(strip_marks(text)) - allowed
            if loose:
                problems.append(f'essay {essay["id"]} {where}: figures without a cited claim: {sorted(loose)}')
        for text in [essay['title'], essay['dek'], essay['short'], essay['art']['caption'], svg_text(essay['art']['file'])]:
            if numbers(text) - FREE_NUMBERS:
                problems.append(f'essay {essay["id"]}: number in title, dek or illustration text: {text[:60]!r}')
    for text in content['intro']:
        if numbers(text) - FREE_NUMBERS:
            problems.append(f'intro: number without a claim: {text[:60]!r}')
    unused = sorted(set(claims) - used)
    if unused:
        problems.append(f'claims not used on the page: {unused}')
    return locations, problems


def svg_text(name):
    """Visible text and titles in an SVG, so drawn figures face the same figure check as prose."""
    return ' '.join(re.findall(r'>([^<>]+)<', (HERE / 'art' / name).read_text()))


def svg(name, label=None):
    text = (HERE / 'art' / name).read_text()
    if '<script' in text or 'href=' in text or 'style=' in text:
        raise ValueError(f'{name}: art must be static and self-contained')
    text = text.strip()
    if label:
        # Scene art is described by its caption; the drawing carries the same text for screen readers.
        text = text.replace('<svg ', f'<svg role="img" aria-label="{esc(label, quote=True)}" ', 1)
    return text


def dividend_chart(claim):
    """Single-series bar chart of the per-adult dividend, drawn from the claim's anchored series."""
    series = claim['series']
    w, h, left, bottom, top = 640, 300, 56, 252, 24
    peak = 1000
    step = (w - left - 16) / len(series)
    bar = step * 0.62
    grid = ''.join(f'<line x1="{left}" x2="{w-8}" y1="{bottom-(bottom-top)*v/peak:.1f}" y2="{bottom-(bottom-top)*v/peak:.1f}" class="grid"/>'
                   f'<text x="{left-8}" y="{bottom-(bottom-top)*v/peak+4:.1f}" class="axis" text-anchor="end">${v:,}</text>'
                   for v in (0, 250, 500, 750, 1000))
    bars, labels = [], []
    for i, (year, value) in enumerate(series):
        x = left + i * step + (step - bar) / 2
        y = bottom - (bottom - top) * value / peak
        bars.append(f'<g class="bar"><title>{year}: ${value:,} per adult (nominal, model estimate)</title>'
                    f'<rect x="{x-4:.1f}" y="{top-8}" width="{bar+8:.1f}" height="{bottom-top+30}" class="hit"/>'
                    f'<path d="M{x:.1f},{bottom} V{y+4:.1f} Q{x:.1f},{y:.1f} {x+4:.1f},{y:.1f} H{x+bar-4:.1f} Q{x+bar:.1f},{y:.1f} {x+bar:.1f},{y+4:.1f} V{bottom} Z" class="mark"/></g>')
        labels.append(f'<text x="{x+bar/2:.1f}" y="{bottom+18}" class="axis" text-anchor="middle">{"’"+str(year)[2:] if i else year}</text>')
        if year in (series[0][0], 2037, series[-1][0]):
            labels.append(f'<text x="{x+bar/2:.1f}" y="{y-8:.1f}" class="value" text-anchor="middle">${value:,}</text>')
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-labelledby="chart-title chart-desc" class="chart">'
            f'<title id="chart-title">Climate Dividend per adult by year, 2030 to 2040</title>'
            f'<desc id="chart-desc">Bars rise from ${series[0][1]:,} per adult in {series[0][0]} to ${dict(series)[2037]:,} in 2037, '
            f'when the fee reaches $150 a ton, then hold near that level. Nominal dollars, carbon-model estimates.</desc>'
            f'{grid}{"".join(bars)}<line x1="{left}" x2="{w-8}" y1="{bottom}" y2="{bottom}" class="baseline"/>{"".join(labels)}</svg>'
            '<details class="table-view"><summary>Show the numbers as a table</summary><table><caption>Climate Dividend per adult, nominal dollars (model estimate)</caption>'
            '<thead><tr><th scope="col">Year</th><th scope="col">Per adult</th></tr></thead><tbody>'
            + ''.join(f'<tr><th scope="row">{y}</th><td>${v:,}</td></tr>' for y, v in series) + '</tbody></table></details>')


def build(content=None, root=ROOT, strict=True):
    content = content or load()
    _, problems = validate(content, root)
    errors = [p for p in problems if strict or not is_drift(p)]
    if errors:
        raise ClaimError('Claim register problems:\n  ' + '\n  '.join(errors))
    ref = content['source_commit']
    pinned = pinned_lines(content)
    locations = {cid: [pinned[anchor_key(s['path'], s['anchor'])] for s in c['sources']]
                 for cid, c in content['claims'].items()}
    claims, policies, essays = content['claims'], content['policies'], content['essays']

    def src_url(path, line=None, commit=None):
        return f'{REPO}{commit or ref}/{esc(path, quote=True)}' + (f'#L{line}' if line else '')

    page_parts, toc = [], []
    for n, essay in enumerate(essays):
        order = []  # claim ids in order of first citation within this essay

        def number(cid):
            if cid not in order:
                order.append(cid)
            return order.index(cid) + 1

        def cite(match):
            # One superscript per run of adjacent markers, e.g. notes 4, 5.
            ks = [number(cid) for cid in MARK.findall(match.group(0))]
            links = ','.join(f'<a href="#{essay["id"]}-n{k}" aria-label="Evidence note {k}">{k}</a>' for k in ks)
            return f'<sup class="cite">{links}</sup>'

        def para(text):
            # Escape prose, attach each marker to the preceding word, then turn markers into note links.
            return MARK_RUN.sub(cite, esc(re.sub(r'\s+(?=\{c:)', '', text)))

        def figures(diagram_list):
            out = ''
            for d in diagram_list:
                for cid in d['claims']:
                    if cid not in order:
                        order.append(cid)
                graphic = dividend_chart(claims[d['chart']]) if d.get('chart') else svg(d['file'])
                refs = sorted(order.index(c) + 1 for c in d['claims'])
                notes = ', '.join(f'<a href="#{essay["id"]}-n{k}" aria-label="evidence note {k}">{k}</a>' for k in refs)
                out += (f'<figure class="diagram" id="{d["id"]}">{graphic}<figcaption>{esc(d["caption"])} '
                        f'<span class="fig-sources">Evidence: note{"s" if len(refs) > 1 else ""} {notes}.</span></figcaption></figure>')
            return out

        if 'body' in essay:
            # Number notes in reading order: paragraphs before the figures, the figures, then the rest.
            place = essay.get('diagram_after', len(essay['body']))
            before = ''.join(f'<p>{para(p)}</p>' for p in essay['body'][:place])
            drawn = figures(essay.get('diagrams', []))
            body = before + drawn + ''.join(f'<p>{para(p)}</p>' for p in essay['body'][place:])
        else:
            diagrams = {d['id']: d for d in essay.get('diagrams', [])}
            parts = []
            for b in essay['blocks']:
                if 'h' in b:
                    slug = essay['id'] + '-' + re.sub(r'[^a-z0-9]+', '-', b['h'].lower()).strip('-')
                    parts.append(f'<h3 class="section-h" id="{slug}">{esc(b["h"])}</h3>')
                elif 'p' in b:
                    parts.append(f'<p>{para(b["p"])}</p>')
                elif 'quote' in b:
                    parts.append(f'<blockquote class="pull"><p>{para(b["quote"])}</p></blockquote>')
                elif 'points' in b:
                    items = ''.join(f'<li>{para(t)}</li>' for t in b['points'])
                    parts.append(f'<section class="brief" aria-label="The argument in brief"><h3>The argument in brief</h3><ol>{items}</ol></section>')
                elif 'objection' in b:
                    answer = ''.join(f'<p>{para(t)}</p>' for t in b['answer'])
                    parts.append(f'<div class="objection"><h4><span class="obj-k">Objection</span> {para(b["objection"])}</h4>'
                                 f'<div class="obj-a"><span class="obj-k">Response</span>{answer}</div></div>')
                elif 'figure' in b:
                    parts.append(figures([diagrams[b['figure']]]))
            body = ''.join(parts)
        limits = para(essay['limits'])
        notes = []
        for k, cid in enumerate(order, 1):
            claim = claims[cid]
            links = ' · '.join(f'<a href="{src_url(s["path"], line, source_ref(content, s))}">{esc(s.get("label") or s["path"])}</a>'
                               for s, line in zip(claim['sources'], locations[cid]))
            ext = ''.join(f' · <a href="{esc(x["url"], quote=True)}">{esc(x["label"])}</a> (checked {esc(x["checked"])})'
                          for x in claim.get('external', []))
            notes.append(f'<li id="{essay["id"]}-n{k}" data-claim-id="{cid}"><span class="basis basis-{claim["basis"]}">'
                         f'{esc(content["basis_labels"][claim["basis"]])}</span> {esc(claim["summary"])} '
                         f'<span class="note-src">{links}{ext}</span></li>')
        policy_list = ''.join(f'<li data-policy-id="{pid}"><a href="{src_url(policies[pid]["path"])}">{esc(policies[pid]["name"])}</a></li>'
                              for pid in essay['policy_ids'])
        prev_link = f'<a href="#{essays[n-1]["id"]}">← {esc(essays[n-1]["title"])}</a>' if n else '<a href="#essays">← All essays</a>'
        next_link = f'<a href="#{essays[n+1]["id"]}">{esc(essays[n+1]["title"])} →</a>' if n + 1 < len(essays) else '<a href="#essays">All essays ↑</a>'
        art = essay['art']
        page_parts.append(f'''<article class="essay" id="{essay["id"]}" aria-labelledby="{essay["id"]}-title" data-policy-ids="{esc(" ".join(essay["policy_ids"]))}">
<header class="essay-head"><p class="eyebrow">Essay {n+1} of {len(essays)} · {esc(essay["principle"])}{" · Research brief" if "blocks" in essay else ""}</p>
<h2 id="{essay["id"]}-title" tabindex="-1">{esc(essay["title"])}</h2><p class="dek">{esc(essay["dek"])}</p></header>
<figure class="scene"><div class="scene-art">{svg(art["file"], "Imagined scene: " + art["caption"])}</div><figcaption><span class="fiction">Imagined scene</span> {esc(art["caption"])}</figcaption></figure>
<div class="prose">{body}</div>
<aside class="limits" aria-label="What this essay does not claim"><h3>What this essay does not claim</h3><p>{limits}</p></aside>
<div class="essay-foot"><section aria-labelledby="{essay["id"]}-pol"><h3 id="{essay["id"]}-pol">Policies in this essay</h3><ul class="policies">{policy_list}</ul></section>
<section aria-labelledby="{essay["id"]}-ev"><h3 id="{essay["id"]}-ev">Evidence notes</h3><ol class="notes">{"".join(notes)}</ol></section></div>
<nav class="essay-nav" aria-label="Essay navigation">{prev_link}{next_link}</nav></article>''')
        toc.append(f'<li><a href="#{essay["id"]}"><span class="toc-n">{n+1:02d}</span><span class="toc-t">{esc(essay["title"])}</span>'
                   f'<span class="toc-d">{esc(essay["short"])}</span></a></li>')

    intro = ''.join(f'<p>{esc(p)}</p>' for p in content['intro'])
    key = ''.join(f'<li><b>{esc(k)}</b> {esc(v)}</li>' for k, v in content['reading_key'])
    css = (HERE / 'story.css').read_text()
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Essays · Project 2050</title><meta name="description" content="{esc(content["description"], quote=True)}">
<style>{css}</style></head><body>
<a class="skip" href="#essays">Skip to the essays</a>
<header class="site"><div class="wrap bar"><a class="brand" href="index.html"><span class="brand-mark">2050</span>Project 2050</a>
<nav aria-label="Main"><a href="index.html">A day in 2050</a><a href="#essays" aria-current="page">Essays</a><a href="analysis.html">The analysis</a></nav></div></header>
<main id="main">
<section class="hero" aria-labelledby="page-title"><div class="wrap hero-grid"><div>
<p class="eyebrow">Working edition · {esc(content["edition_label"])} · not published</p>
<h1 id="page-title">{esc(content["title"])}</h1>{intro}</div>
<aside class="key" aria-labelledby="key-title"><h2 id="key-title">How to read these essays</h2><ul>{key}</ul></aside></div></section>
<section class="toc-wrap" id="essays" aria-labelledby="toc-title"><div class="wrap"><h2 id="toc-title" class="toc-title">Reading order</h2><ol class="toc">{"".join(toc)}</ol></div></section>
<div class="wrap essays">{"".join(page_parts)}</div>
<section class="wrap closing" aria-labelledby="closing-title"><h2 id="closing-title">About this edition</h2>
<p>{esc(content["closing"])}</p>
<p>Evidence snapshot: <code>{ref[:12]}</code> ({esc(content["source_label"])}). Each note links to the passage it rests on at that version. Repository documents may require GitHub access; the essays remain readable without it.</p>
<p><a href="story-claims.json">Claim register (structured)</a> · <a href="story-claims.html">Claim register (readable)</a> · <a href="index.html">A day in a possible 2050</a> · <a href="analysis.html">The analysis companion</a></p></section>
</main>
<footer class="site"><div class="wrap">Project 2050 · Working essays · {esc(content["edition_date"])} · Imagined scenes are fiction; policy descriptions are proposals, not law or benefits available through this site.</div></footer>
</body></html>
'''
    register = {'schema_version': 1, 'source_commit': ref, 'edition_date': content['edition_date'],
                'status': 'working_edition_not_published', 'basis_labels': content['basis_labels'],
                'claims': {cid: {'summary': c['summary'], 'basis': c['basis'], 'figures': c.get('figures', []),
                                 'series': c.get('series', []), 'policy_ids': c.get('policy_ids', []),
                                 'sources': [{'path': s['path'], 'commit': source_ref(content, s), 'line': line, 'anchor': s['anchor']}
                                             for s, line in zip(c['sources'], locations[cid])],
                                 'external': c.get('external', []),
                                 'essays': [e['id'] for e in essays if f'{{c:{cid}}}' in json.dumps(e, ensure_ascii=False)
                                            or any(cid in d['claims'] for d in e.get('diagrams', []))]}
                           for cid, c in claims.items()},
                'essays': [{'id': e['id'], 'title': e['title'], 'url': f'story.html#{e["id"]}',
                            'policy_ids': e['policy_ids']} for e in essays],
                'policies': policies, 'left_out': content['left_out']}
    md = [f'# Public story page: claim register', '',
          f'Generated by `models/tools/public-product/story/build_story.py` from `essays.json`; do not edit by hand. '
          f'Evidence snapshot `{ref}`; edition {content["edition_date"]}. Each claim names the exact passage it rests on. '
          'The builder fails if a passage disappears or if an essay paragraph shows a figure that its cited claims do not carry.', '',
          '| Claim | Essays | Basis | What the page says | Source passage (path:line) |', '| --- | --- | --- | --- | --- |']
    for cid, c in register['claims'].items():
        srcs = '<br>'.join(f'`{s["path"]}:{s["line"]}`' for s in c['sources'])
        ext = ''.join(f'<br>External: [{x["label"]}]({x["url"]}), checked {x["checked"]}' for x in c['external'])
        md.append(f'| `{cid}` | {", ".join(c["essays"])} | {content["basis_labels"][c["basis"]]} | {c["summary"]} | {srcs}{ext} |')
    md += ['', '## Claims deliberately left out', '']
    md += [f'- **{x["claim"]}** {x["why"]}' for x in content['left_out']]
    rows = []
    for cid, c in register['claims'].items():
        srcs = '<br>'.join(f'<a href="{src_url(s["path"], s["line"], s["commit"])}">{esc(s["path"])}:{s["line"]}</a>'
                           for s in c['sources'])
        ext = ''.join(f'<br><a href="{esc(x["url"], quote=True)}">{esc(x["label"])}</a> (checked {esc(x["checked"])})'
                      for x in c['external'])
        used = ', '.join(f'<a href="story.html#{e}">{esc(e)}</a>' for e in c['essays'])
        rows.append(f'<tr id="claim-{cid}"><th scope="row"><code>{cid}</code></th><td>{used}</td>'
                    f'<td>{esc(content["basis_labels"][c["basis"]])}</td><td>{esc(c["summary"])}</td><td>{srcs}{ext}</td></tr>')
    left = ''.join(f'<li><b>{esc(x["claim"])}</b> {esc(x["why"])}</li>' for x in content['left_out'])
    register_page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Claim register · Project 2050</title><style>{css}</style></head><body>
<a class="skip" href="#main">Skip to the register</a>
<header class="site"><div class="wrap bar"><a class="brand" href="index.html"><span class="brand-mark">2050</span>Project 2050</a>
<nav aria-label="Main"><a href="index.html">A day in 2050</a><a href="story.html">Essays</a><a href="analysis.html">The analysis</a></nav></div></header>
<main id="main" class="wrap register"><h1>Claim register</h1>
<p>Every claim on the <a href="story.html">essay page</a>, the exact passage it rests on, and its basis. Evidence snapshot <code>{ref[:12]}</code>; edition {esc(content["edition_date"])}. Generated from the same records as the page.</p>
<div class="table-scroll"><table><caption>Claims and their sources</caption><thead><tr><th scope="col">Claim</th><th scope="col">Essays</th><th scope="col">Basis</th><th scope="col">What the page says</th><th scope="col">Source passage</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table></div>
<h2>Claims deliberately left out</h2><ul>{left}</ul></main>
<footer class="site"><div class="wrap">Project 2050 · Working essays · {esc(content["edition_date"])}</div></footer></body></html>
'''
    outputs = {OUT / 'story.html': page.encode(),
               OUT / 'story-claims.html': register_page.encode(),
               OUT / 'story-claims.json': (json.dumps(register, indent=2, ensure_ascii=False) + '\n').encode(),
               REGISTER_MD: ('\n'.join(md) + '\n').encode(),
               LOCK: (json.dumps({'source_commit': ref, 'evidence_commit': content.get('evidence_commit'),
                                  'lines': dict(sorted(pinned.items()))}, indent=1) + '\n').encode()}
    return outputs, problems


def review(target):
    content = load()
    commit = subprocess.check_output(['git', 'rev-parse', '--verify', '--end-of-options', target + '^{commit}'],
                                     cwd=ROOT, text=True).strip()
    paths = sorted({s['path'] for c in content['claims'].values() for s in c['sources']} |
                   {p['path'] for p in content['policies'].values()})

    def blob(ref, path):
        r = subprocess.run(['git', 'rev-parse', '--verify', '--quiet', f'{ref}:{path}'], cwd=ROOT,
                           capture_output=True, text=True)
        return r.stdout.strip() or None
    # Compare each cited file with its moved location, so the reset's renames are not reported as edits.
    changed = {p for p in paths if blob(content['source_commit'], p) != blob(commit, current_path(p))}
    affected = {cid: sorted({s['path'] for s in c['sources']} & changed)
                for cid, c in content['claims'].items() if {s['path'] for s in c['sources']} & changed}
    return {'source_commit': content['source_commit'], 'target_commit': commit,
            'changed_sources': sorted(set(paths) & changed), 'claims_to_review': affected,
            'action': 'Reread each listed claim against the new passage; edit essays.json, then advance source_commit and rebuild.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true', help='verify committed outputs and every claim anchor')
    mode.add_argument('--report', action='store_true',
                      help='like --check, but only warn about moved claim anchors (used by the common runner)')
    mode.add_argument('--review-ref', metavar='REF')
    parser.add_argument('--content', type=Path, help=argparse.SUPPRESS)  # alternate essays.json (tests)
    parser.add_argument('--root', type=Path, default=ROOT, help=argparse.SUPPRESS)  # alternate source tree (tests)
    args = parser.parse_args()
    if args.review_ref:
        print(json.dumps(review(args.review_ref), indent=2))
        sys.exit(0)
    try:
        products, problems = build(load(args.content), args.root, strict=not args.report)
    except ClaimError as e:
        sys.exit(str(e))
    if args.check or args.report:
        # Outputs are built from pinned lines, so moved sources never make them stale; a stale output always fails.
        stale = [str(p.relative_to(ROOT)) for p, data in products.items() if not p.exists() or p.read_bytes() != data]
        if stale:
            sys.exit('Stale story outputs: ' + ', '.join(stale) + '. Run build_story.py and commit.')
        if problems:
            print('REVIEW public story claims (a cited passage moved or changed; the page is unchanged until an '
                  'editor rereads them):\n  ' + '\n  '.join(problems))
        print('Public story: outputs and claim register verified')
    else:
        for path, data in products.items():
            path.write_bytes(data)
        print('Built ' + ', '.join(str(p.relative_to(ROOT)) for p in products))
