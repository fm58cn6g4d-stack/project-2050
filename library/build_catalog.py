#!/usr/bin/env python3
"""Library catalog, file facts and name index (stage A, step 3; plan section 4).

  library/catalog.csv        authored: one row per document, SRC-0001 IDs, kind, origin, rights, status, aliases
  library/catalog-facts.csv  generated: bytes, SHA-256 and Git dates for each catalogued file
  library/name-index.md      generated: every name a document has gone by -> its one home

  python3 library/build_catalog.py           # add rows for new files (existing rows are never changed), rebuild generated files
  python3 library/build_catalog.py --check   # fail if a file is uncatalogued, a path is gone or the name index is stale;
                                             # stale file facts only print a note

The first run seeded the authored fields by the rules below; after that they are edited by hand.
"""
import argparse
import csv
import hashlib
import html
import io
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIB = ROOT / 'library'
CATALOG, FACTS, INDEX = LIB / 'catalog.csv', LIB / 'catalog-facts.csv', LIB / 'name-index.md'
SCOPE = ('legacy', 'library/intake')
COLUMNS = ['id', 'path', 'title', 'kind', 'origin', 'rights', 'status', 'aliases', 'copy_of', 'note']
FACT_COLUMNS = ['id', 'path', 'bytes', 'sha256', 'first_commit', 'last_content_commit']
STAGING = 'legacy/staging/unified-reform-inventory-current.md'
BILL_BOOK = ('library/intake/2026-10-28/old-sessions/Claude_project-2050-archive-extras_left_out_of_initial_'
             'claude_project_fileset/archive/wargame-floor-time-bill-book.html')

# Aliases the project's documents use for one home (the brief for stage A lists them).
ALIASES = {
    BILL_BOOK: ['Bill Book', 'the Bill Book', 'Floor Time Bill Book'],
    'library/intake/2026-10-28/old-sessions/Claude climate carbon permitting/Thriving-Economy-Project-session/'
    'Thriving Economy Project - Legislative Agenda Map.docx': ['the map', 'Thriving Economy map', 'SEEC map'],
    'legacy/sources/health-go-big-bill-detail-and-financing.md': ['go-big tab', 'Go-big bill detail and financing'],
    'legacy/sources/revenue-channels-and-full-menu.md': ['revenue tab', 'Revenue channels and full menu'],
    'legacy/sources/climate-durability-pathway-session-findings.md': ['the durability session', 'durability findings'],
    STAGING: ['staging inventory', 'the staging file', 'unified reform inventory'],
    'library/intake/2026-10-28/old-sessions/Claude_project-2050-archive-extras_left_out_of_initial_claude_project_'
    'fileset/archive/wargame-nineteen-months.html': ['Nineteen Months'],
    'library/intake/2026-10-28/old-sessions/Claude_project-2050-archive-extras_left_out_of_initial_claude_project_'
    'fileset/archive/wargame-ledger-outcomes.html': ['Ledger outcomes'],
}
# Intake files published by governments or legislatures; everything else in the intake is Espen's session work.
PUBLIC = {'7-23-2025_hr_4669_-_section_by_section.pdf': 'public (House committee document)',
          'R48856.3.pdf': 'public (Congressional Research Service)',
          'fema_text.pdf': 'public (bill text)',
          'BipartisanAmericanAffordabilityandJobsAct.pdf': 'public (bill text)',
          '1791753732441_house-democrats-health-care-working-group-agenda-2026.pdf': 'public (House Democrats working group)',
          'project-2050-cms-imp-02-source-records.zip': 'public (state procurement records, with project notes)',
          'permitting-reform-summary-1.pdf': 'public (Senate Energy and Natural Resources Committee one-pager)'}
CHECK = {}  # files whose rights need a person's check before they stay in the public repository


def tracked():
    out = subprocess.check_output(['git', 'ls-files', '-z', '--', *SCOPE], cwd=ROOT).decode().split('\0')
    return sorted(p for p in out if p)


def generated_outputs():
    import json
    policy = json.loads((ROOT / '.github/merge-policy.json').read_text())
    return set(policy['generated_outputs'])


def title_of(path):
    p = ROOT / path
    try:
        if p.suffix == '.md':
            for line in p.read_text(errors='replace').splitlines():
                if line.startswith('# '):
                    return re.sub(r'[*`]', '', line[2:]).strip()
        if p.suffix == '.html':
            m = re.search(r'<title>(.*?)</title>', p.read_text(errors='replace'), re.S | re.I)
            if m and m.group(1).strip():
                return html.unescape(re.sub(r'\s+', ' ', m.group(1))).strip()
    except OSError:
        pass
    return re.sub(r'[_-]+', ' ', p.stem).strip()


def seed_row(path, generated):
    """Default authored fields for a newly catalogued file."""
    parts, name = path.split('/'), Path(path).name
    if path.startswith('legacy/'):
        folder = parts[1] if len(parts) > 2 else ''
        kind = {'domains': 'policy design', 'governing': 'governing record', 'frameworks': 'reasoning note',
                'archive': 'history', 'staging': 'draft inventory', 'index': 'register or model report',
                'sources': 'research note or source'}.get(folder, 'navigation')
        if path in generated or (folder == 'sources' and re.search(r'climate-portfolio-(pricing|packages)|claim-register', name)):
            kind, status = 'generated model output', 'generated by the legacy model suite'
        else:
            status = 'legacy (read-only)'
        return kind, 'project repository, before October 28, 2026', 'project', status
    archive = {'old-sessions': 'old-sessions.zip', 'claude-more': 'claude-more.zip', 'project-2029': 'project_2029.zip'}
    origin = archive.get(parts[3], 'intake') if len(parts) > 4 else 'intake'
    if len(parts) > 5:
        origin += ': ' + parts[4]
    rights = PUBLIC.get(name) or CHECK.get(name) or 'project (Espen\'s session original)'
    kind = 'original (public document)' if name in PUBLIC else 'original (session upload)'
    if name == 'manifest.json' or name == 'README.md':
        kind = 'intake record'
    return kind, origin, rights, 'untriaged original'


def load(path, columns):
    if not path.exists():
        return []
    with path.open(newline='') as f:
        rows = list(csv.DictReader(f))
    return rows


def write_csv(rows, columns):
    buf = io.StringIO()
    w = csv.DictWriter(buf, columns, lineterminator='\n')
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue()


def git_dates(path):
    """(first commit date, last commit date that changed content), following renames."""
    log = subprocess.check_output(['git', 'log', '--follow', '--format=@%cs', '--name-status', '--', path],
                                  cwd=ROOT).decode()
    dates, last = [], ''
    for block in log.split('@')[1:]:
        lines = block.strip().splitlines()
        date, changes = lines[0], [l for l in lines[1:] if l.strip()]
        dates.append(date)
        if not last and not all(l.startswith('R100') for l in changes):
            last = date
    return (dates[-1] if dates else '', last or (dates[-1] if dates else ''))


def copies(rows):
    """copy_of for rows without one: an intake original whose title matches a legacy document is a copy of
    it (the legacy file is the working home); a byte-identical intake file is a copy of the first one."""
    legacy_titles = {r['title'].lower(): r['id'] for r in rows if r['path'].startswith('legacy/')}
    first_by_hash = {}
    for r in rows:
        if r.get('copy_of') is not None or not r['path'].startswith('library/intake/'):
            r.setdefault('copy_of', '')
            continue
        digest = hashlib.sha256((ROOT / r['path']).read_bytes()).hexdigest() if (ROOT / r['path']).exists() else ''
        r['copy_of'] = legacy_titles.get(r['title'].lower()) or first_by_hash.get(digest, '')
        first_by_hash.setdefault(digest, r['id'])
    return rows


def catalog_rows():
    rows = load(CATALOG, COLUMNS)
    known = {r['path'] for r in rows}
    generated = generated_outputs()
    n = max([int(r['id'][4:]) for r in rows] or [0])
    for path in tracked():
        if path in known:
            continue
        n += 1
        kind, origin, rights, status = seed_row(path, generated)
        rows.append({'id': f'SRC-{n:04d}', 'path': path, 'title': title_of(path), 'kind': kind, 'origin': origin,
                     'rights': rights, 'status': status, 'aliases': '; '.join(ALIASES.get(path, [])), 'note': ''})
    return copies(rows)


def facts(rows):
    out = []
    for r in rows:
        p = ROOT / r['path']
        if not p.exists():
            continue
        data = p.read_bytes()
        first, last = git_dates(r['path'])
        out.append({'id': r['id'], 'path': r['path'], 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                    'first_commit': first, 'last_content_commit': last})
    return out


def staging_rows():
    """'staging N.N' names: rows of the staging inventory, by line."""
    out = []
    for n, line in enumerate((ROOT / STAGING).read_text().splitlines(), 1):
        m = re.match(r'\|\s*(\d+\.\d+)\s*\|\s*([^|]*)', line)
        if m:
            out.append((f'staging {m.group(1)}', f'{STAGING}:{n}', re.sub(r'\s+', ' ', m.group(2)).strip()[:90]))
    return out


def home_of(row, by_id):
    """(SRC ID, path) of a document's one home: itself, or the working copy an original upload duplicates."""
    target = by_id.get(row.get('copy_of', ''))
    return (target['id'], target['path']) if target else (row['id'], row['path'])


def names(rows):
    """(name, SRC, home path, how the name is used) for titles, file names and aliases."""
    by_id, out = {r['id']: r for r in rows}, []
    for r in rows:
        sid, home = home_of(r, by_id)
        copy = f' of the original upload {r["id"]} (`{r["path"]}`)' if home != r['path'] else ''
        out.append((r['title'], sid, home, 'title' + copy))
        out.append((Path(r['path']).name, sid, home, 'file name' + copy))
        out += [(a.strip(), sid, home, 'alias' + copy) for a in r['aliases'].split(';') if a.strip()]
    return out


def name_index(rows):
    names_ = names(rows)
    src = {r['path']: r['id'] for r in rows}
    names_ += [(name, src.get(STAGING, ''), where, 'staging row: ' + what) for name, where, what in staging_rows()]
    names_ += [(f'Bill Book {n}', src.get(BILL_BOOK, ''), BILL_BOOK, 'alias: chapter of the Bill Book')
              for n in sorted({int(m) for m in re.findall(r'Bill Book (\d+)', '\n'.join(
                  (ROOT / p).read_text(errors='replace') for p in tracked() if p.endswith('.md')))})]
    seen, lines = set(), []
    for name, sid, path, how in sorted(names_, key=lambda x: (x[0].lower(), x[2], x[3])):
        key = (name.lower(), path)
        if key in seen or not name:
            continue
        seen.add(key)
        cell = lambda s: s.replace('|', '\\|')
        lines.append(f'| {cell(name)} | {sid} | `{cell(path)}` | {cell(how)} |')
    return ('# Name index\n\nGenerated by `library/build_catalog.py` from `library/catalog.csv`; do not edit by hand. '
            'Every name a document has gone by (title, file name, alias, staging row) leads to its one home; an original '
            'upload that duplicates a working copy (`copy_of` in the catalog) leads to the working copy. '
            'Add a name by adding it to the `aliases` column of the catalog.\n\n'
            '| Name | Source | Home | How the name is used |\n| --- | --- | --- | --- |\n' + '\n'.join(lines) + '\n')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    rows = catalog_rows()
    outputs = {CATALOG: write_csv(rows, COLUMNS), FACTS: write_csv(facts(rows), FACT_COLUMNS), INDEX: name_index(rows)}
    if args.check:
        stale = [p for p, text in outputs.items() if not p.exists() or p.read_text() != text]
        # File facts change whenever a document or a model output does; that is a refresh, not an error.
        if FACTS in stale:
            print('note: catalog-facts.csv is out of date; run library/build_catalog.py to refresh it')
        problems = [f'{p.relative_to(ROOT)} is stale or missing (run library/build_catalog.py)' for p in stale if p != FACTS]
        problems += [f'{r["id"]}: {r["path"]} no longer exists' for r in rows if not (ROOT / r['path']).exists()]
        ids = [r['id'] for r in rows]
        # One home per name: a title or alias that leads to two documents is ambiguous. File names may repeat.
        homes = {}
        for name, _, home, how in names(rows):
            if not how.startswith('file name'):
                homes.setdefault(name.lower(), set()).add(home)
        problems += [f'name {n!r} leads to {len(h)} homes: {", ".join(sorted(h))}' for n, h in homes.items() if len(h) > 1]
        problems += [f'{r["id"]}: copy_of {r["copy_of"]} is not a catalog ID' for r in rows
                     if r.get('copy_of') and r['copy_of'] not in set(ids)]
        problems += [f'duplicate ID {i}' for i in sorted({i for i in ids if ids.count(i) > 1})]
        print('\n'.join(problems) or f'library catalog: {len(rows)} documents, facts and name index current')
        sys.exit(1 if problems else 0)
    for p, text in outputs.items():
        p.write_text(text)
    print(f'wrote {len(rows)} catalog rows, facts and the name index')
