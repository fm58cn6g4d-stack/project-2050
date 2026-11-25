#!/usr/bin/env python3
"""Build "A day in 2050", the front door's content, with its claim register.

Role: the stage H step H8 builder (`models/stage-h/1-audit.md`, part 3.1, row H8). It reads `day.json` (the
scenes, their provisions, start dates, costs, honest limits and hard questions, and the claim register),
checks every figure against an exact passage in a dossier's sections 1-8, and writes a working preview of the
page and its readable register. Status: draft content for review; nothing is published or deployed. The page
design is step H9's and the site build is H10's: the preview here is plain on purpose. Standard library only.

  python3 models/tools/public-product/day/build_day.py             # write the preview
  python3 models/tools/public-product/day/build_day.py --check     # verify the claims and the committed preview
  python3 models/tools/public-product/day/build_day.py --report    # as --check, but source drift only warns
  python3 models/tools/public-product/day/build_day.py --pin origin/main   # re-pin to a commit on main
  python3 models/tools/public-product/day/build_day.py --frame family --money first --no-optional --out DIR

The pin. Every claim's passages are pinned to `source_commit`, a commit on main. `anchors.lock.json` records,
for each passage, its line at that commit, and, for each cited file, the file's Git blob hash there. The build
and the checks read only the lock and the working tree, never Git history, so they pass from a normal (shallow)
clone however far main moves. Only `--pin` reads the commit itself, and it is run when the commit is fresh.

The drift check. Each passage is looked up in today's file. A passage that is gone, or a cited file whose blob
differs from the pinned one, is reported as drift: an editorial signal to reread those claims, never an error
in another change. Content errors (a figure without a claim, a claim whose figure is not in its passages, a
source outside sections 1-8, a banned phrase, a broken structure) always fail.
"""
import argparse
import hashlib
import html
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'models' / 'registry'))
import claims as claim_rules  # noqa: E402  (the shared claim-tracing rules, models/registry/claims.py)

CONTENT = HERE / 'day.json'
LOCK = HERE / 'anchors.lock.json'
CSS = HERE / 'day.css'
PREVIEW = HERE / 'preview'
OUTPUTS = ('day.html', 'day-claims.html', 'day-claims.json')
REPO = 'https://github.com/fm58cn6g4d-stack/project-2050/blob/'
TOOLKIT = ROOT / 'models' / 'toolkit.csv'

MARK = re.compile(r'\{c:([a-z0-9-]+)\}')
MARK_RUN = re.compile(r'(?:\{c:[a-z0-9-]+\})+')
numbers = claim_rules.numbers
FREE_NUMBERS = {'2050'}  # the project's name, not a claim
# Sections 1-8 of a dossier: a file directly in the dossier's folder named 1-... to 8-... (1b-, 4bcd-, ...).
SECTION_FILE = re.compile(r'^dossiers/(?:[a-z0-9-]+/){1,2}[1-8][a-z]*-[a-z0-9-]+\.md$')
BASES = {
    'decision': 'Decided design',
    'design': 'Proposed design',
    'estimate': 'Our estimate',
    'model': 'Our model result',
    'observed': 'Current fact',
    'research': 'Research finding',
}
ESTIMATE_WORDS = ('on our estimate', 'our estimates', 'about', 'our analysis', 'our working figure', 'we assume',
                  'our estimates assume')
# Phrases the front door must never use (PLAN 3.4; the section 9 can't-say lists), unless negated just before.
BANNED = ('official score', 'scored by', 'pays for itself', 'paid for itself', 'ends child poverty',
          'cuts it in half', 'a home for everyone', 'free child care for all', 'free long-term care',
          'no new taxes', 'every person in the country is covered', 'meets the 2035 goal', 'a right from 2037',
          'duty to house', 'zero uninsured', 'families come out ahead')
NEGATIONS = ('not ', 'no ', 'never ', "don't say ", "we don't say ", 'not an ', 'is not ')
SECTIONS = (('what_changed', 'What changed'), ('begins', 'When it begins'), ('cost', 'What it costs'),
            ('limits', 'The honest limit'))
esc = html.escape


class ContentError(ValueError):
    pass


# ---------------------------------------------------------------- loading and walking the content

def load(path=CONTENT):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def strip_marks(text):
    return MARK.sub('', text)


def scene_blocks(scene):
    """(where, text) for every piece of reading text in a scene that may carry figures."""
    out = [(f'beat {i+1}', b['text']) for i, b in enumerate(scene['beats'])]
    d = scene['detail']
    for key, _ in SECTIONS:
        out += [(f'{key} {i+1}', t) for i, t in enumerate(d.get(key, []))]
    for i, q in enumerate(d.get('questions', [])):
        out.append((f'question {i+1}', q['q']))
        out += [(f'answer {i+1}.{k+1}', a) for k, a in enumerate(q['a'])]
    return out


def plain_texts(content):
    """(where, text) for reading text that must carry no figure at all (titles, framing, placeholders)."""
    out = [('title', content['title']), ('description', content['description']), ('closing', content['closing'])]
    out += [(f'reading key {i+1}', ' '.join(k)) for i, k in enumerate(content['reading_key'])]
    out += [(f'principle {i+1}', p['title'] + ' ' + p['body']) for i, p in enumerate(content['principles'])]
    out += [(f'movement {i+1}', m['title'] + ' ' + m['body']) for i, m in enumerate(content['movement'])]
    out += [(f'person {k}', p['name'] + ' ' + p['about']) for k, p in content['people'].items()]
    for s in content['scenes']:
        out += [(f'scene {s["id"]} {f}', s[f]) for f in ('place', 'title', 'flagship', 'illustration')]
        for ph in s['detail'].get('placeholders', []):
            out.append((f'scene {s["id"]} placeholder {ph["id"]}', ph['title'] + ' ' + ph['text']))
    return out


def public_texts(content):
    out = [(f'intro {i+1}', t) for i, t in enumerate(content['intro'])] + plain_texts(content)
    for s in content['scenes']:
        out += [(f'scene {s["id"]} {w}', t) for w, t in scene_blocks(s)]
    return out


def toolkit_ids():
    if not TOOLKIT.exists():
        return set()
    return {line.split(',', 1)[0] for line in TOOLKIT.read_text().splitlines()[1:] if line}


# ---------------------------------------------------------------- the pin and the lock

def anchor_key(path, anchor):
    return f'{path}#{hashlib.sha256(anchor.encode()).hexdigest()[:16]}'


def blob_hash(data):
    """Git's blob hash of a file's bytes, computed without Git."""
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def wanted_anchors(content):
    return {anchor_key(s['path'], s['anchor']): (s['path'], s['anchor'])
            for c in content['claims'].values() for s in c['sources']}


def read_lock():
    return json.loads(LOCK.read_text()) if LOCK.exists() else None


def lock_problems(content, lock):
    """Why the lock can't serve this content (empty when it can)."""
    if lock is None:
        return ['anchors.lock.json is missing: run --pin']
    out = []
    if lock.get('source_commit') != content['source_commit']:
        out.append('anchors.lock.json is for another source_commit: run --pin')
    missing = set(wanted_anchors(content)) - set(lock.get('lines', {}))
    if missing:
        out.append(f'{len(missing)} passage(s) not in anchors.lock.json (new or edited claims): run --pin')
    return out


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, stderr=subprocess.DEVNULL).decode()


def pin(content, ref):
    """Pin every passage to `ref` (a commit on main): verify each passage there, record lines and blob hashes."""
    try:
        sha = git('rev-parse', '--verify', f'{ref}^{{commit}}').strip()
    except subprocess.CalledProcessError:
        raise ContentError(f'{ref} is not a commit in this clone')
    try:
        main = git('rev-parse', '--verify', 'origin/main^{commit}').strip()
        subprocess.check_call(['git', 'merge-base', '--is-ancestor', sha, main], cwd=ROOT,
                              stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        raise ContentError(f'{sha[:12]} is not on origin/main: pin to a commit main holds, so its links last')
    lines, blobs, problems = {}, {}, []
    for key, (path, anchor) in sorted(wanted_anchors(content).items()):
        if path not in blobs:
            try:
                blobs[path] = git('rev-parse', f'{sha}:{path}').strip()
                text = git('show', f'{sha}:{path}')
            except subprocess.CalledProcessError:
                problems.append(f'{path} is not in {sha[:12]}')
                continue
            texts = {path: text}
        else:
            texts = {path: git('show', f'{sha}:{path}')}
        line = claim_rules.line_of(texts[path], anchor)
        if line is None:
            problems.append(f'passage not in {sha[:12]}:{path}: {anchor[:70]!r}')
        else:
            lines[key] = line
    if problems:
        raise ContentError('cannot pin:\n  ' + '\n  '.join(problems))
    content['source_commit'] = sha
    return {'source_commit': sha, 'blobs': dict(sorted(blobs.items())), 'lines': dict(sorted(lines.items()))}


def drift(content, lock, root=ROOT):
    """Source drift against today's files: passages gone, and cited files changed since the pin."""
    gone, changed = [], set()
    for cid, claim in content['claims'].items():
        for s in claim['sources']:
            file = root / s['path']
            if not file.is_file() or claim_rules.line_of(file.read_text(encoding='utf-8'), s['anchor']) is None:
                gone.append(f'claim {cid}: passage no longer in {s["path"]}: {s["anchor"][:70]!r}')
    for path, blob in (lock or {}).get('blobs', {}).items():
        file = root / path
        if not file.is_file() or blob_hash(file.read_bytes()) != blob:
            changed.add(path)
    return gone, sorted(changed)


def claims_citing(content, paths):
    return sorted(cid for cid, c in content['claims'].items() if any(s['path'] in paths for s in c['sources']))


# ---------------------------------------------------------------- validation

def banned_hits(text):
    low = strip_marks(text).lower()
    hits = []
    for phrase in BANNED:
        for m in re.finditer(re.escape(phrase), low):
            before = low[max(0, m.start() - 16):m.start()]
            if not any(before.endswith(n) or f' {n}' in before for n in NEGATIONS):
                hits.append(phrase)
    return hits


def validate(content, root=ROOT):
    """Content problems: each a string. Empty means every figure traces and the structure holds."""
    p = []
    claims = content['claims']
    if not re.fullmatch(r'[0-9a-f]{40}', content.get('source_commit', '')):
        p.append('source_commit must be a full commit SHA (run --pin)')
    # Claims: sources in sections 1-8, figures in their passages.
    for cid, c in claims.items():
        if c.get('basis') not in BASES:
            p.append(f'claim {cid}: basis must be one of {sorted(BASES)}')
        if not c.get('sources'):
            p.append(f'claim {cid}: no source')
        for s in c.get('sources', []):
            if not SECTION_FILE.match(s['path']) or '/memos/' in s['path'] or '/notes/' in s['path']:
                p.append(f'claim {cid}: {s["path"]} is not a dossier section 1-8 file')
            if '\n' in s['anchor'] or len(s['anchor']) < 12:
                p.append(f'claim {cid}: a passage must be one line of at least 12 characters')
        p += [f'claim {cid}: {x}' for x in claim_rules.figure_problems(
            [s['anchor'] for s in c.get('sources', [])], c.get('figures', []), c.get('rounded', []), (), FREE_NUMBERS)]
    # Reading text: every figure belongs to a claim the same block cites; estimates are worded as estimates.
    used = set()

    def check_block(where, text):
        cited = MARK.findall(text)
        allowed = set(FREE_NUMBERS)
        for cid in cited:
            if cid not in claims:
                p.append(f'{where}: unknown claim {cid}')
                continue
            used.add(cid)
            for f in claims[cid].get('figures', []):
                allowed |= numbers(f)
            for r in claims[cid].get('rounded', []):
                allowed |= numbers(r['figure'])
        loose = numbers(strip_marks(text)) - allowed
        if loose:
            p.append(f'{where}: figures without a cited claim: {sorted(loose)}')
        if any(claims.get(c, {}).get('basis') in ('estimate', 'model') for c in cited):
            if not any(w in strip_marks(text).lower() for w in ESTIMATE_WORDS):
                p.append(f'{where}: cites an estimate but does not say "on our estimates" or "about"')

    for i, t in enumerate(content['intro']):
        check_block(f'intro {i+1}', t)
    for where, t in plain_texts(content):
        if numbers(t) - FREE_NUMBERS:
            p.append(f'{where}: a title, framing line or placeholder may not carry a figure: {t[:60]!r}')
        if MARK.search(t):
            p.append(f'{where}: no claim marks here')
    for where, t in public_texts(content):
        for hit in banned_hits(t):
            p.append(f'{where}: banned phrase {hit!r}')
    # Scenes and structure.
    people, scenes = content['people'], content['scenes']
    ids = [s['id'] for s in scenes]
    if len(ids) != len(set(ids)):
        p.append('duplicate scene id')
    models = toolkit_ids()
    for s in scenes:
        for where, t in scene_blocks(s):
            check_block(f'scene {s["id"]} {where}', t)
        d = s['detail']
        for key in ('begins', 'limits', 'questions'):
            if s['id'] != 'money' and not d.get(key):
                p.append(f'scene {s["id"]}: needs at least one item under {key}')
        for b in s['beats']:
            if b['person'] is not None and b['person'] not in people:
                p.append(f'scene {s["id"]}: unknown person {b["person"]}')
        for key in ('brief', 'dossier'):
            if not (root / d[key]).is_file():
                p.append(f'scene {s["id"]}: {key} {d[key]} does not exist')
        for m in d.get('models', []):
            if models and m not in models:
                p.append(f'scene {s["id"]}: {m} is not in models/toolkit.csv')
        if s.get('optional') and s['optional'] not in content['config']['optional_scenes']:
            p.append(f'scene {s["id"]}: optional flag {s["optional"]} is not in config.optional_scenes')
        for ph in d.get('placeholders', []):
            if not all(ph.get(k) for k in ('id', 'title', 'text', 'waits_on')):
                p.append(f'scene {s["id"]}: a placeholder needs id, title, text and waits_on')
    if 'money' not in ids:
        p.append('the money scene is missing')
    cfg = content['config']
    if cfg.get('frame') not in content['orders']:
        p.append(f'config.frame must be one of {sorted(content["orders"])}')
    if cfg.get('money_position') not in ('first', 'last'):
        p.append('config.money_position must be "first" or "last"')
    for name, order in content['orders'].items():
        if sorted(order) != sorted(ids):
            p.append(f'orders.{name} must list every scene exactly once')
    family = content['family']
    for s in scenes:
        if s['id'] != 'money' and not any(b['person'] and people.get(b['person'], {}).get('household') == family
                                          for b in s['beats']):
            p.append(f'scene {s["id"]}: no beat for the {family} household, so the family frame would drop it')
    unused = sorted(set(claims) - used)
    if unused:
        p.append(f'claims not used on the page: {unused}')
    return p


# ---------------------------------------------------------------- rendering

def arrange(content, frame=None, money=None, optional=None):
    """The scenes in reading order for a frame, with the money placed and optional scenes kept or dropped."""
    cfg = content['config']
    frame = frame or cfg['frame']
    money = money or cfg['money_position']
    flags = dict(cfg['optional_scenes'], **(optional or {}))
    by_id = {s['id']: s for s in content['scenes']}
    order = [by_id[i] for i in content['orders'][frame] if not by_id[i].get('optional') or flags[by_id[i]['optional']]]
    rest = [s for s in order if s['id'] != 'money']
    order = ([by_id['money']] + rest) if money == 'first' else (rest + [by_id['money']])
    family = content['family'] if frame == 'family' else None
    out = []
    for s in order:
        beats = s['beats']
        if family and s['id'] != 'money':
            beats = [b for b in beats if b['person'] and content['people'][b['person']]['household'] == family]
        out.append(dict(s, beats=beats))
    return out, frame, money, flags


def render(content, lock, frame=None, money=None, optional=None):
    """The page, the readable register and the register's JSON, as strings."""
    claims = content['claims']
    ref = content['source_commit']
    lines = lock['lines']
    scenes, frame, money, flags = arrange(content, frame, money, optional)

    def src_url(path, line=None):
        return f'{REPO}{ref}/{esc(path, quote=True)}' + (f'#L{line}' if line else '')

    def gh(path):
        return f'{REPO}main/{esc(path, quote=True)}'

    where_used = {}
    body = []
    for n, s in enumerate(scenes, start=1):
        order = []

        def cite(m, sid=s['id'], order=order):
            ks = []
            for cid in MARK.findall(m.group(0)):
                if cid not in order:
                    order.append(cid)
                where_used.setdefault(cid, [])
                if sid not in where_used[cid]:
                    where_used[cid].append(sid)
                ks.append(order.index(cid) + 1)
            return '<sup class="cite">' + ','.join(
                f'<a href="#{sid}-n{k}" aria-label="Evidence note {k}">{k}</a>' for k in ks) + '</sup>'

        def para(text):
            return MARK_RUN.sub(cite, esc(re.sub(r'\s+(?=\{c:)', '', text)))

        d = s['detail']
        tag = ' <span class="tag">Optional scene</span>' if s.get('optional') else ''
        beats = ''.join(f'<p>{para(b["text"])}</p>' for b in s['beats'])
        parts = []
        for key, label in SECTIONS:
            if d.get(key):
                parts.append(f'<h4>{label}</h4><ul>' + ''.join(f'<li>{para(t)}</li>' for t in d[key]) + '</ul>')
        for ph in d.get('placeholders', []):
            parts.append(f'<div class="placeholder" data-placeholder="{esc(ph["id"])}"><h4>{esc(ph["title"])}</h4>'
                         f'<p>{esc(ph["text"])}</p></div>')
        if d.get('questions'):
            parts.append('<h4>Hard questions</h4>' + ''.join(
                f'<div class="qa"><p class="q">{para(q["q"])}</p>' + ''.join(f'<p>{para(a)}</p>' for a in q['a'])
                + '</div>' for q in d['questions']))
        deeper = [f'<li><a href="{gh(d["brief"])}">The brief behind this scene</a></li>',
                  f'<li><a href="{gh(d["dossier"])}">The full dossier</a></li>']
        deeper += [f'<li><a href="docs/{esc(m)}.html">The model: {esc(m)}</a> (our analysis, not an official score)</li>'
                   for m in d.get('models', [])]
        if not d.get('models'):
            deeper.append('<li>No model yet: this scene\'s costs are priced by hand in the dossier.</li>')
        parts.append('<h4>Go deeper</h4><ul>' + ''.join(deeper) + '</ul>')
        notes = []
        for k, cid in enumerate(order, start=1):
            c = claims[cid]
            links = '; '.join(f'<a href="{src_url(x["path"], lines[anchor_key(x["path"], x["anchor"])])}">'
                              f'{esc(x["path"])}, line {lines[anchor_key(x["path"], x["anchor"])]}</a>'
                              for x in c['sources'])
            notes.append(f'<li id="{s["id"]}-n{k}"><span class="basis">{esc(BASES[c["basis"]])}.</span> '
                         f'{esc(c["statement"])} {links}</li>')
        notes_html = f'<h4>Evidence notes</h4><ol class="notes">{"".join(notes)}</ol>' if notes else ''
        body.append(
            f'<section class="scene" id="{s["id"]}" data-flagship="{esc(s["flagship"])}">'
            f'<p class="when">{esc(s["time"])} · {esc(s["place"])} · <span class="flagship">{esc(s["flagship"])}</span>{tag}</p>'
            f'<h2>{esc(s["title"])}</h2>'
            f'<figure class="art"><div class="art-brief" role="img" aria-label="{esc(s["illustration"], quote=True)}">'
            f'<span>Imagined scene</span>{esc(s["illustration"])}</div></figure>'
            f'{beats}<details><summary>What made the difference</summary>{"".join(parts)}{notes_html}</details>'
            '</section>')

    intro = ''.join(f'<p>{MARK_RUN.sub("", esc(t))}</p>' for t in content['intro'])
    key = ''.join(f'<li><strong>{esc(a)}</strong> {esc(b)}</li>' for a, b in content['reading_key'])
    principles = ''.join(f'<li><strong>{esc(x["title"])}.</strong> {esc(x["body"])}</li>' for x in content['principles'])
    movement = ''.join(f'<li><strong>{esc(x["title"])}.</strong> {esc(x["body"])}</li>' for x in content['movement'])
    toc = ''.join(f'<li><a href="#{s["id"]}">{esc(s["time"])}: {esc(s["title"])}</a></li>' for s in scenes)
    css = CSS.read_text()
    edition = (f'{esc(content["edition_label"])}. Evidence pinned to <a href="{REPO}{ref}">{ref[:12]}</a> '
               f'({esc(content["source_label"])}). Frame: {frame}; the money {money}.')
    page = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f'<title>{esc(content["title"])}</title><meta name="description" content="{esc(content["description"], quote=True)}">'
        '<meta name="robots" content="noindex">'
        f'<style>{css}</style></head><body><a class="skip" href="#day">Skip to the day</a>'
        f'<header><p class="draft">Working draft for review. Not published.</p><h1>{esc(content["title"])}</h1>{intro}'
        f'<ul class="key">{key}</ul></header>'
        f'<nav aria-label="The day"><ol>{toc}</ol></nav>'
        f'<main id="day">{"".join(body)}</main>'
        f'<section class="close"><h2>What it is for</h2><ul>{principles}</ul>'
        f'<h2>How it happens</h2><ul>{movement}</ul></section>'
        f'<footer><p>{esc(content["closing"])}</p><p>{edition}</p>'
        '<p><a href="day-claims.html">The claim register</a> · <a href="docs/index.html">The toolkit</a></p></footer>'
        '</body></html>\n')

    register = []
    for cid in sorted(claims):
        c = claims[cid]
        srcs = ''.join(f'<li><a href="{src_url(x["path"], lines[anchor_key(x["path"], x["anchor"])])}">{esc(x["path"])}'
                       f'#L{lines[anchor_key(x["path"], x["anchor"])]}</a>: <q>{esc(x["anchor"])}</q></li>'
                       for x in c['sources'])
        flag = f'<p class="recheck">Recheck: {esc(c["recheck"])}</p>' if c.get('recheck') else ''
        register.append(f'<tr id="{cid}"><th scope="row"><code>{cid}</code></th><td>{esc(BASES[c["basis"]])}</td>'
                        f'<td>{esc(", ".join(c.get("figures", [])) or "none")}</td><td>{esc(c["statement"])}'
                        f'<ul>{srcs}</ul>{flag}</td><td>{esc(", ".join(where_used.get(cid, [])) or "not shown in this frame")}</td></tr>')
    placeholders = ''.join(f'<li><strong>{esc(ph["title"])}</strong>: waits on {esc(ph["waits_on"])}</li>'
                           for s in content['scenes'] for ph in s['detail'].get('placeholders', []))
    register_page = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f'<title>Claim register</title><meta name="robots" content="noindex"><style>{css}</style></head><body>'
        f'<header><p class="draft">Working draft for review. Not published.</p><h1>Claim register: {esc(content["title"])}</h1>'
        f'<p>Every figure on the page and the passage in a dossier\'s sections 1-8 it comes from, pinned to '
        f'<a href="{REPO}{ref}">{ref[:12]}</a>. {len(claims)} claims.</p></header><main>'
        '<table class="register"><thead><tr><th scope="col">Claim</th><th scope="col">Basis</th><th scope="col">Figures</th>'
        '<th scope="col">What it says, and its passages</th><th scope="col">Scenes</th></tr></thead><tbody>'
        f'{"".join(register)}</tbody></table><h2>Not yet on the page</h2><ul>{placeholders}</ul></main>'
        '<footer><p><a href="day.html">Back to the day</a></p></footer></body></html>\n')
    data = {'title': content['title'], 'source_commit': ref, 'frame': frame, 'money_position': money,
            'optional_scenes': flags, 'scenes': [s['id'] for s in scenes],
            'claims': {cid: {'basis': c['basis'], 'figures': c.get('figures', []), 'statement': c['statement'],
                             'recheck': c.get('recheck', ''), 'scenes': where_used.get(cid, []),
                             'sources': [dict(x, line=lines[anchor_key(x['path'], x['anchor'])],
                                              url=src_url(x['path'], lines[anchor_key(x['path'], x['anchor'])]))
                                         for x in c['sources']]}
                       for cid, c in sorted(claims.items())},
            'placeholders': [dict(ph, scene=s['id']) for s in content['scenes'] for ph in s['detail'].get('placeholders', [])]}
    return {'day.html': page, 'day-claims.html': register_page,
            'day-claims.json': json.dumps(data, indent=1, ensure_ascii=False) + '\n'}


# ---------------------------------------------------------------- commands

def build(content, lock, strict=True, root=ROOT, **frame):
    problems = validate(content, root) + lock_problems(content, lock)
    if problems:
        raise ContentError('Content problems:\n  ' + '\n  '.join(problems))
    gone, changed = drift(content, lock, root)
    if gone and strict:
        raise ContentError('Source drift (cited passages gone; reread these claims, then --pin):\n  ' + '\n  '.join(gone))
    return render(content, lock, **frame), gone, changed


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true', help='verify claims and the committed preview')
    mode.add_argument('--report', action='store_true', help='as --check, but source drift only warns')
    mode.add_argument('--pin', metavar='REF', help='re-pin every passage to REF, a commit on origin/main')
    ap.add_argument('--out', type=Path, help='write the preview here instead of preview/')
    ap.add_argument('--frame', choices=('town', 'family'))
    ap.add_argument('--money', choices=('first', 'last'))
    ap.add_argument('--no-optional', action='store_true', help='leave out the optional scenes')
    a = ap.parse_args(argv)
    content = load()
    try:
        if a.pin:
            lock = pin(content, a.pin)
            CONTENT.write_text(json.dumps(content, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
            LOCK.write_text(json.dumps(lock, indent=1) + '\n')
            print(f'Pinned {len(lock["lines"])} passages in {len(lock["blobs"])} files to {lock["source_commit"]}.')
            return 0
        lock = read_lock()
        frame = {}
        if a.frame or a.money or a.no_optional:
            if a.check or a.report:
                ap.error('--check and --report verify the committed preview, which uses the config in day.json')
            frame = dict(frame=a.frame, money=a.money,
                         optional={k: False for k in content['config']['optional_scenes']} if a.no_optional else None)
        outputs, gone, changed = build(content, lock, strict=not a.report, **frame)
    except ContentError as e:
        print(e, file=sys.stderr)
        return 1
    if gone or changed:
        print('REVIEW the front door\'s claims (source drift since the pin; not an error in your change):')
        for g in gone:
            print('  ' + g)
        if changed:
            print(f'  cited files changed since {content["source_commit"][:12]}: {", ".join(changed)}')
            print(f'  claims citing them: {", ".join(claims_citing(content, set(changed)))}')
    if a.check or a.report:
        stale = [n for n in OUTPUTS if not (PREVIEW / n).is_file() or (PREVIEW / n).read_text(encoding='utf-8') != outputs[n]]
        if stale:
            print(f'The committed preview is stale: {", ".join(stale)}. Run build_day.py and commit it.', file=sys.stderr)
            return 1
        print(f'Front door content: {len(content["claims"])} claims trace to dossier sections 1-8; the preview is current.')
        return 0
    out = a.out or PREVIEW
    out.mkdir(parents=True, exist_ok=True)
    for name, text in outputs.items():
        (out / name).write_text(text, encoding='utf-8')
    print(f'Wrote {", ".join(OUTPUTS)} to {out}.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
