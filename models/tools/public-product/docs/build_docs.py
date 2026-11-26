#!/usr/bin/env python3
"""Generate a docs page per core model, and the toolkit's front page, from the toolkit's own files.

Role: stage H step H8's per-model docs pages (`models/stage-h/1-audit.md`, part 3.1, row H8; part 3.5). Each
page is built at build time from the files the models already keep, so it can't drift from them:
  - `models/toolkit.csv`: the register row (status, owner, paths, each release criterion's pass or fail);
  - `models/release-criteria.csv`: what each criterion means;
  - the model's card (`MODEL-CARD.md`), rendered whole: its evidence map, validation table and how to run;
  - its parameter file, as the evidence table `models/schema/parameters.py` generates;
  - the header of its results file (version, baseline vintage, scoring convention, the disclaimer);
  - its `CHANGELOG.md`, and its rows in the run log, `models/runs.csv`.
Nothing here is committed output: the pages are written to `build/public-product/docs/` (ignored by Git), and
H10 publishes them with the site. Status: draft for review; not published. Standard library only.

  python3 models/tools/public-product/docs/build_docs.py              # write build/public-product/docs/
  python3 models/tools/public-product/docs/build_docs.py --out DIR
  python3 models/tools/public-product/docs/build_docs.py --check      # build to a temporary folder and verify
"""
import argparse
import csv
import html
import io
import json
import re
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'models' / 'schema'))
import parameters  # noqa: E402  (models/schema/parameters.py)

OUT = ROOT / 'build' / 'public-product' / 'docs'
REPO = 'https://github.com/fm58cn6g4d-stack/project-2050/blob/main/'
DISCLAIMER = 'Our analysis of the evidence: not an official score or a benefit determination.'
esc = html.escape
CSS = ('body{margin:0 auto;max-width:52rem;padding:0 1rem 3rem;font:1rem/1.6 system-ui,sans-serif;background:#fbfaf7;color:#1d1f22}'
       'a{color:#1f5f8b}table{border-collapse:collapse;display:block;overflow-x:auto;font-size:.88rem}'
       'th,td{border:1px solid #d9d5cc;padding:.3rem .5rem;text-align:left;vertical-align:top}'
       'pre{background:#f1eee7;padding:.8rem;overflow-x:auto}code{font-size:.9em}.draft{color:#8a4b00;font-weight:600}'
       '.pass{color:#1d6b35}.fail{color:#a1261b}.partial{color:#8a4b00}.disclaimer{border-left:4px solid #8a4b00;padding-left:.8rem}'
       '@media (prefers-color-scheme:dark){body{background:#141619;color:#ecebe7}a{color:#8cc4ef}th,td{border-color:#3a3e45}'
       'pre{background:#1d2025}.pass{color:#7fd49a}.fail{color:#ff9b8f}.partial,.draft{color:#ffcf8a}}')


# ---------------------------------------------------------------- a small Markdown renderer for the cards

def inline(text, base):
    """Inline Markdown: code, bold, italics, links (relative links point into the repository on GitHub)."""
    parts = re.split(r'(`[^`]+`)', text)
    out = []
    for part in parts:
        if part.startswith('`') and part.endswith('`') and len(part) > 1:
            out.append(f'<code>{esc(part[1:-1])}</code>')
            continue
        s = esc(part, quote=False)

        def link(m):
            label, href = m.group(1), m.group(2)
            if not re.match(r'^(https?:|#|mailto:)', href):
                href = REPO + str((base / href).resolve().relative_to(ROOT)) if (base / href.split('#')[0]).exists() else REPO + href
            return f'<a href="{esc(href, quote=True)}">{label}</a>'
        s = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', link, s)
        s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)', r'<em>\1</em>', s)
        out.append(s)
    return ''.join(out)


def markdown(text, base, shift=1):
    """Block Markdown: headings (shifted down), paragraphs, lists, tables, fenced code, comments dropped."""
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    lines = text.split('\n')
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith('```'):
            j = i + 1
            while j < len(lines) and not lines[j].startswith('```'):
                j += 1
            out.append('<pre><code>' + esc('\n'.join(lines[i + 1:j])) + '</code></pre>')
            i = j + 1
            continue
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            level = min(6, len(m.group(1)) + shift)
            out.append(f'<h{level}>{inline(m.group(2), base)}</h{level}>')
            i += 1
            continue
        if line.lstrip().startswith('|'):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                rows.append(lines[i].strip())
                i += 1
            cells = [[c.strip() for c in re.split(r'(?<!\\)\|', r.strip('|'))] for r in rows]
            cells = [[c.replace('\\|', '|') for c in r] for r in cells]
            head, body = cells[0], [r for r in cells[1:] if not all(re.fullmatch(r':?-{3,}:?', c) for c in r if c)]
            out.append('<table><thead><tr>' + ''.join(f'<th scope="col">{inline(c, base)}</th>' for c in head)
                       + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{inline(c, base)}</td>' for c in r) + '</tr>'
                                                          for r in body) + '</tbody></table>')
            continue
        if re.match(r'^\s*([-*]|\d+\.)\s+', line):
            items, j = [], i
            ordered = bool(re.match(r'^\s*\d+\.', line))
            while j < len(lines) and (re.match(r'^\s*([-*]|\d+\.)\s+', lines[j]) or (lines[j].startswith('  ') and lines[j].strip())):
                m2 = re.match(r'^(\s*)([-*]|\d+\.)\s+(.*)', lines[j])
                if m2:
                    items.append([len(m2.group(1)), m2.group(3)])
                else:
                    items[-1][1] += ' ' + lines[j].strip()
                j += 1
            html_items, depth0 = [], items[0][0]
            for indent, body in items:
                cls = ' class="sub"' if indent > depth0 else ''
                html_items.append(f'<li{cls}>{inline(body, base)}</li>')
            tag = 'ol' if ordered else 'ul'
            out.append(f'<{tag}>' + ''.join(html_items) + f'</{tag}>')
            i = j
            continue
        para = [line.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,6}\s|```|\s*\||\s*([-*]|\d+\.)\s)', lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append(f'<p>{inline(" ".join(para), base)}</p>')
    return '\n'.join(out)


# ---------------------------------------------------------------- reading the toolkit's files

def read_csv(path):
    return list(csv.DictReader(io.StringIO(Path(path).read_text(encoding='utf-8'))))


def results_header(row):
    for path in filter(None, (row.get('results') or '').split(';')):
        p = ROOT / path
        if p.suffix == '.json' and p.is_file():
            try:
                h = json.loads(p.read_text()).get('header')
            except (ValueError, AttributeError):
                h = None
            if isinstance(h, dict):
                return path, h
    return None, None


def param_files(row):
    return [f.strip() for f in (row.get('parameters') or '').split(';') if f.strip()]


def parameter_table(row):
    if not row.get('parameters'):
        return None
    colmap = dict(x.split('=', 1) for x in filter(None, (row.get('parameters_map') or '').split(';')))
    # A register row may list several parameter files separated by ';' (immigration, housing); the first is the
    # model's main parameter file on the schema, and the page links the others.
    rows = parameters.read(ROOT / param_files(row)[0], colmap)
    problems = parameters.validate(rows)
    # A file not yet on the schema (health coverage's has no year column until step H3) still shows its rows.
    rows = [{**{k: '' for k in parameters.REQUIRED + parameters.OPTIONAL}, **r} for r in rows]
    return parameters.table(rows), problems


def slug(model_id):
    return model_id


def page(title, body):
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex">'
            f'<title>{esc(title)}</title><style>{CSS}</style></head><body>'
            '<p class="draft">Working draft for review. Not published.</p>' + body + '</body></html>\n')


def model_page(row, criteria, runs):
    mid, name = row['model_id'], row['name']
    base = ROOT / (row['path'] or 'models')
    out = [f'<p><a href="index.html">The toolkit</a></p><h1>{esc(name)} <small>({esc(mid)})</small></h1>',
           f'<p class="disclaimer">{esc(DISCLAIMER)}</p>']
    rpath, header = results_header(row)
    facts = [('Status', row['status']), ('Owner', row['owner'] or 'not yet named'),
             ('Code', row['path'] or 'no model yet'),
             ('Version', header.get('model_version') if header else 'no versioned results header yet')]
    if header:
        facts += [('Baseline', header.get('baseline_vintage', '')), ('Scoring convention', header.get('scoring_convention', '')),
                  ('Price basis', header.get('price_basis', '')), ('Uncertainty', header.get('uncertainty', ''))]
    out.append('<h2>At a glance</h2><table><tbody>' + ''.join(
        f'<tr><th scope="row">{esc(k)}</th><td>{esc(str(v))}</td></tr>' for k, v in facts) + '</tbody></table>')
    out.append('<h2>Release criteria</h2><p>Provisional until Espen answers memo H1. The register can understate a model, '
               'never overstate it.</p><table><thead><tr><th scope="col">Criterion</th><th scope="col">Result</th></tr></thead><tbody>'
               + ''.join(f'<tr><td>{esc(c["criterion"])}</td><td class="{esc(row.get(c["id"], ""))}">{esc(row.get(c["id"], ""))}</td></tr>'
                         for c in criteria) + '</tbody></table>')
    if row.get('notes'):
        out.append(f'<p><strong>Register notes:</strong> {esc(row["notes"])}</p>')
    card = ROOT / row['card'] if row.get('card') else None
    out.append('<h2>The model card</h2>')
    if card and card.is_file():
        out.append(f'<p>From <a href="{REPO}{esc(row["card"])}">{esc(row["card"])}</a>, rendered whole.</p>')
        out.append(markdown(card.read_text(encoding='utf-8'), card.parent, shift=2))
    else:
        out.append('<p>No card yet. It is written on the template in its toolkit step (part 3.1 of the stage H audit).</p>')
    out.append('<h2>Parameters</h2>')
    table = parameter_table(row)
    if table:
        text, problems = table
        files = param_files(row)
        out.append(f'<p>Generated from <a href="{REPO}{esc(files[0])}">{esc(files[0])}</a>.'
                   + (' Other parameter files: ' + ', '.join(f'<a href="{REPO}{esc(f)}">{esc(f)}</a>' for f in files[1:]) + '.'
                      if len(files) > 1 else '')
                   + (f' The file does not yet meet the schema in {len(problems)} place(s); see its toolkit step.' if problems else '')
                   + '</p>' + markdown(text, ROOT))
    else:
        out.append('<p>No parameter file on the schema yet.</p>')
    changelog = ROOT / row['path'] / 'CHANGELOG.md' if row.get('path') else None
    out.append('<h2>Changelog</h2>')
    if changelog and changelog.is_file():
        out.append(markdown(changelog.read_text(encoding='utf-8'), changelog.parent, shift=2))
    else:
        out.append('<p>No changelog yet.</p>')
    mine = [r for r in runs if r['model_id'] == mid]
    out.append('<h2>Recorded runs</h2>')
    if mine:
        out.append('<table><thead><tr><th scope="col">Run</th><th scope="col">Version</th><th scope="col">Commit</th>'
                   '<th scope="col">Command</th></tr></thead><tbody>' + ''.join(
                       f'<tr><td>{esc(r["run_id"])}</td><td>{esc(r["model_version"])}</td><td><code>{esc(r["commit"][:12])}</code></td>'
                       f'<td><code>{esc(r["command"])}</code></td></tr>' for r in mine) + '</tbody></table>')
    else:
        out.append('<p>None recorded yet (<code>models/runs.csv</code>).</p>')
    if rpath:
        out.append(f'<p>Results file: <a href="{REPO}{esc(rpath)}">{esc(rpath)}</a>.</p>')
    return page(f'{name}: docs', '\n'.join(out))


def build_all():
    rows = read_csv(ROOT / 'models' / 'toolkit.csv')
    criteria = read_csv(ROOT / 'models' / 'release-criteria.csv')
    runs = read_csv(ROOT / 'models' / 'runs.csv')
    pages = {f'{slug(r["model_id"])}.html': model_page(r, criteria, runs) for r in rows}
    items = ''.join(f'<tr><td><a href="{slug(r["model_id"])}.html">{esc(r["name"])}</a></td><td><code>{esc(r["model_id"])}</code></td>'
                    f'<td>{esc(r["status"])}</td><td>{sum(r.get(c["id"]) == "pass" for c in criteria)} of {len(criteria)}</td></tr>'
                    for r in rows)
    pages['index.html'] = page('The toolkit', (
        '<h1>The toolkit</h1><p>The models behind Project 2050\'s figures, for professionals who want to check them, rerun '
        'them or use them. Each page is generated from the model\'s own files: its register row, card, parameters, '
        'results header, changelog and recorded runs.</p>'
        f'<p class="disclaimer">{esc(DISCLAIMER)}</p>'
        '<table><thead><tr><th scope="col">Model</th><th scope="col">ID</th><th scope="col">Status</th>'
        f'<th scope="col">Release criteria passed</th></tr></thead><tbody>{items}</tbody></table>'
        '<p>Nothing here is released yet: what "released" means is memo H1, still open.</p>'))
    return rows, pages


def check(pages, rows):
    """Problems with the generated pages (empty when every page is whole and every internal link resolves)."""
    p = []
    for r in rows:
        name = f'{r["model_id"]}.html'
        text = pages.get(name, '')
        for heading in ('At a glance', 'Release criteria', 'The model card', 'Parameters', 'Changelog', 'Recorded runs'):
            if f'<h2>{heading}</h2>' not in text:
                p.append(f'{name}: no "{heading}" section')
        if DISCLAIMER not in text:
            p.append(f'{name}: no disclaimer')
    for name, text in pages.items():
        for href in re.findall(r'href="([^"#:]+\.html)"', text):
            if href not in pages:
                p.append(f'{name}: link to {href}, which is not generated')
    return p


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--out', type=Path, default=OUT)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args(argv)
    rows, pages = build_all()
    problems = check(pages, rows)
    if problems:
        print('Docs pages:\n  ' + '\n  '.join(problems), file=sys.stderr)
        return 1
    out = Path(tempfile.mkdtemp()) if a.check else a.out
    out.mkdir(parents=True, exist_ok=True)
    for name, text in pages.items():
        (out / name).write_text(text, encoding='utf-8')
    print(f'Docs pages: {len(rows)} models and the toolkit page {"verified" if a.check else "written to " + str(out)}.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
