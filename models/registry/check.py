#!/usr/bin/env python3
"""Registry checker: every link between project records resolves (plan section 4; stage A, step 4).

Checks, in one run:
- agenda: agenda/agenda.csv has every legacy policy and option ID once, with valid levels;
- library: every document is catalogued and the name index is current;
- charter: DEC- and OUT- IDs are well formed and unique;
- dossiers: each evidence.json entry names a catalogued source, its anchor passage (or list of passages)
  exists in that source (for a citation-only source, a licensed one the repository does not hold, each anchor
  is a quotation of at most 60 words with a locator, which a reviewer checks against the original), its figures and every number in its statement trace to the anchors (the story
  builder's rules, models/registry/claims.py), its grade is A-E, it says whether it is data or analysis, and an
  analysis entry lists entries that support, contest or qualify it (a warning until one comes from an
  independent publisher)
  and its dates are valid; each provisions.json entry belongs to an agenda ID and cites known evidence;
- references: every SRC-, EV-, OUT- and DEC- ID cited in current text resolves, including inline code
  (in Markdown, an ID in a fenced code block is a format example and is not checked).

A re-check date in the past is reported as a warning (an error with --strict), so an evidence entry
falling due never breaks unrelated work.

  python3 models/registry/check.py [--strict]
"""
import argparse
import csv
import datetime
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import claims  # noqa: E402

TEXT = {'.md', '.txt', '.csv', '.json', '.html', '.htm', '.py', '.js', '.jsx', '.rtf'}
EV_ID = re.compile(r'^EV-[A-Z]{2,4}-\d{3}$')
REFS = {'SRC': re.compile(r'\bSRC-\d{4}\b'), 'EV': re.compile(r'\bEV-[A-Z]{2,4}-\d{3}\b'),
        'OUT': re.compile(r'\bOUT-\d{2}\b'), 'DEC': re.compile(r'\bDEC-\d{4}-\d{2}-\d{2}-\d{2}\b')}
GRADES = set('ABCDE')
CLAIMS = {'data', 'analysis'}  # a measured fact, or an interpretation of facts (causes, effects, projections, models)
STANCES = {'supports', 'contests', 'qualifies'}
CITATION = 'citation (not saved)'  # library/build_catalog.py: a cited source the repository does not hold
QUOTE_WORDS = 60  # a brief quotation from a licensed source; longer passages belong in a saved, open text
QUOTE_TOTAL = 120  # all quotations in one evidence entry together


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def publisher_of(row):
    """The publisher in a catalog origin: "Publisher: address" for saved texts, "Publisher (year)" for citations.
    Independence compares these names exactly, so a citation row spells its publisher as other rows do."""
    name = row.get('origin', '').split(': ', 1)[0]
    return re.sub(r'\s*\(\d{4}\)$', '', name).strip()


def date(value):
    try:
        return datetime.date.fromisoformat(value)
    except (TypeError, ValueError):
        return None


def rows(path):
    if not path.exists():
        return []
    with path.open(newline='') as f:
        return list(csv.DictReader(f))


def ids_in(path, pattern):
    """IDs that begin a table row of a charter file (where they are defined)."""
    if not path.exists():
        return []
    return [m.group(1) for line in path.read_text().splitlines()
            if (m := re.match(r'\|\s*\**(' + pattern + r')\**\s*\|', line))]


def check_charter(root):
    errors, known = [], {}
    for kind, path, pattern in (('DEC', 'charter/decisions.md', r'DEC-\d{4}-\d{2}-\d{2}-\d{2}'),
                                ('OUT', 'charter/outcomes.md', r'OUT-\d{2}')):
        found = ids_in(root / path, pattern)
        errors += [f'{path}: {i} defined twice' for i in sorted({i for i in found if found.count(i) > 1})]
        known[kind] = set(found)
    return errors, known


def check_dossiers(root, catalog, agenda, today):
    """Evidence registers and provisions under dossiers/."""
    errors, warnings, evidence = [], [], set()
    analyses, source_of = [], {}
    src_paths = {r['id']: r['path'] for r in catalog}
    src_kinds = {r['id']: r['kind'] for r in catalog}
    registers = sorted((root / 'dossiers').rglob('evidence.json')) if (root / 'dossiers').exists() else []
    for path in registers:
        rel = path.relative_to(root)
        try:
            entries = json.loads(path.read_text())
        except json.JSONDecodeError as e:
            errors.append(f'{rel}: not valid JSON ({e})')
            continue
        for e in entries:
            eid = e.get('id', '?')
            where = f'{rel}: {eid}'
            if not EV_ID.match(eid):
                errors.append(f'{where}: ID must look like EV-HOU-001')
            if eid in evidence:
                errors.append(f'{where}: defined twice')
            evidence.add(eid)
            source_of[eid] = e.get('source')
            for field in ('statement', 'source', 'anchor', 'grade', 'fact_date', 'checked', 'recheck'):
                if not e.get(field):
                    errors.append(f'{where}: missing {field}')
            if e.get('grade') and e['grade'] not in GRADES:
                errors.append(f'{where}: grade must be one of A-E')
            if e.get('claim') not in CLAIMS:
                errors.append(f'{where}: claim must be "data" or "analysis"')
            analyses.append((where, e))
            for field in ('checked', 'recheck'):
                if e.get(field) and not date(e[field]):
                    errors.append(f'{where}: {field} must be a date (YYYY-MM-DD)')
            # The fact's own date may be a year or a month: a 2025 poverty rate, a March 2026 count.
            if e.get('fact_date') and not re.fullmatch(r'\d{4}(-\d{2}(-\d{2})?)?', str(e['fact_date'])):
                errors.append(f'{where}: fact_date must be YYYY, YYYY-MM or YYYY-MM-DD')
            if date(e.get('recheck')) and date(e['recheck']) < today:
                warnings.append(f'{where}: re-check was due {e["recheck"]}')
            src = e.get('source')
            if src and src not in src_paths:
                errors.append(f'{where}: source {src} is not in library/catalog.csv')
                continue
            if not src or not e.get('anchor'):
                continue
            # One exact passage, or a list of them when a claim spans a page or column break.
            anchors = e['anchor'] if isinstance(e['anchor'], list) else [e['anchor']]
            if src_kinds[src] == CITATION and not e.get('text_version'):
                # A source the repository cites but does not hold: its anchors are short quotations, checked by
                # a reviewer against the original at the locator; the rules below still trace every number to them.
                if not e.get('locator'):
                    errors.append(f'{where}: a quotation from {src} needs a locator (page, section or table)')
                long_ = [a for a in anchors if len(a.split()) > QUOTE_WORDS]
                errors += [f'{where}: quotation over {QUOTE_WORDS} words; quote less: {a[:70]!r}' for a in long_]
                if sum(len(a.split()) for a in anchors) > QUOTE_TOTAL:
                    errors.append(f'{where}: quotations total over {QUOTE_TOTAL} words; quote less')
            else:
                text_path = root / (e.get('text_version') or src_paths[src])
                if text_path.suffix.lower() not in TEXT:
                    errors.append(f'{where}: {src} is not a text file; give a text_version in library/ to anchor against')
                    continue
                text = text_path.read_text(errors='replace') if text_path.exists() else ''
                missing = [a for a in anchors if claims.line_of(text, a) is None]
                for a in missing:
                    errors.append(f'{where}: anchor not found in {text_path.relative_to(root)}: {a[:70]!r}')
                if missing:
                    continue
            errors += [f'{where}: {p}' for p in claims.figure_problems(
                anchors, e.get('figures', []), e.get('rounded', []), e.get('series', []))]
            # The statement is what a dossier repeats, so its numbers must trace too; its year is fact_date.
            traced = claims.numbers(' '.join(anchors)).union(
                {str(e.get('fact_date', ''))[:4]}, *(claims.numbers(r['figure']) for r in e.get('rounded', [])))
            loose = sorted(claims.numbers(e.get('statement', '')) - traced)
            if loose:
                errors.append(f'{where}: statement number(s) {", ".join(loose)} not in its anchors')
    # Analysis is only as good as its independent corroboration: each analysis entry lists the entries that
    # support, contest or qualify it. It is relied on only once one that supports or qualifies it comes from
    # a different publisher; an independent entry that contests it means the dossier must present both views.
    publisher = {r['id']: publisher_of(r) for r in catalog}
    for where, e in analyses:
        links = e.get('corroboration', [])
        if not isinstance(links, list) or not all(isinstance(link, dict) for link in links):
            errors.append(f'{where}: corroboration must be a list of {{"evidence", "stance"}} entries')
            continue
        if e.get('claim') != 'analysis':
            if links:
                errors.append(f'{where}: only an analysis entry takes corroboration')
            continue
        for link in links:
            if link.get('evidence') not in evidence:
                errors.append(f'{where}: corroboration {link.get("evidence")} is not an evidence ID')
            if link.get('stance') not in STANCES:
                errors.append(f'{where}: corroboration stance must be supports, contests or qualifies')
        own = publisher.get(e.get('source'))
        independent = [link for link in links if publisher.get(source_of.get(link.get('evidence'))) not in (None, own)]
        if not any(link.get('stance') in ('supports', 'qualifies') for link in independent):
            warnings.append(f'{where}: analysis without corroboration from an independent publisher')
        if any(link.get('stance') == 'contests' for link in independent):
            warnings.append(f'{where}: contested by an independent publisher; present both views')
    for path in sorted((root / 'dossiers').rglob('provisions.json')) if (root / 'dossiers').exists() else []:
        rel = path.relative_to(root)
        try:
            entries = json.loads(path.read_text())
        except json.JSONDecodeError as e:
            errors.append(f'{rel}: not valid JSON ({e})')
            continue
        seen = set()
        for p in entries:
            pid = p.get('id', '?')
            parent = pid.rsplit('.', 1)[0]
            if not re.fullmatch(r'[A-Z]{2,4}-[A-Z]{0,3}\d+[A-Za-z]?\.\d{2}', pid):
                errors.append(f'{rel}: {pid}: ID must look like HOU-4A.01')
            elif parent not in agenda:
                errors.append(f'{rel}: {pid}: {parent} is not in agenda/agenda.csv')
            if pid in seen:
                errors.append(f'{rel}: {pid}: defined twice')
            seen.add(pid)
            errors += [f'{rel}: {pid}: unknown evidence {ev}' for ev in p.get('evidence', []) if ev not in evidence]
    return errors, warnings, evidence


def check_references(root, known):
    """Every registry ID cited in current text resolves to its record."""
    errors = []
    for folder in ('charter', 'dossiers', 'public', 'agenda', 'models'):
        base = root / folder
        if not base.exists():
            continue
        for path in sorted(base.rglob('*')):
            if path.suffix not in {'.md', '.json', '.csv'} or not path.is_file() or 'site' in path.parts:
                continue
            text = path.read_text(errors='replace')
            if path.suffix == '.md':
                # An ID in a fenced block is a format example, not a citation. Inline code is checked: a real
                # decision cited as `DEC-…` must resolve, and placeholders like DEC-YYYY-MM-DD-NN never match.
                text = re.sub(r'```.*?```', '', text, flags=re.S)
            for kind, pattern in REFS.items():
                for ref in sorted(set(pattern.findall(text)) - known[kind]):
                    errors.append(f'{path.relative_to(root)}: {ref} does not resolve')
    return errors


def run(root=ROOT, today=None, with_legacy=True):
    """(errors, warnings). with_legacy=False skips the agenda and library checks (they need the real tree)."""
    today = today or datetime.date.today()
    errors, warnings, notes = [], [], []
    catalog = rows(root / 'library/catalog.csv')
    agenda = {r['id'] for r in rows(root / 'agenda/agenda.csv')}
    if with_legacy:
        seed = module(root / 'agenda/seed_from_legacy.py', 'agenda_seed')
        listed = [r['id'] for r in rows(root / 'agenda/agenda.csv')]
        missing = sorted({r['id'] for r in seed.seed()} - set(listed))
        errors += [f'agenda/agenda.csv: {i} listed twice' for i in sorted({i for i in listed if listed.count(i) > 1})]
        errors += [f'agenda/agenda.csv: legacy ID {i} missing' for i in missing]
        errors += [f'agenda/agenda.csv: {r["id"]}: level {r["level"]!r} is not L0-L4'
                   for r in rows(root / 'agenda/agenda.csv') if r['level'] not in {'L0', 'L1', 'L2', 'L3', 'L4'}]
        # An item its own domain file marks "(adopted ...)", "(decided ...)" or "Pointer only" must say so.
        # A legacy decision may also be chosen: DEC-2026-10-30-02 reopened them as working choices.
        status_of = {r['id']: r['status'] for r in rows(root / 'agenda/agenda.csv')}
        allowed = {'decided': ('decided', 'chosen'), 'pointer': ('pointer',)}
        for pid, d in seed.domain_definitions().items():
            own = seed.own_status(d['flags'])
            if own in allowed and status_of.get(pid) not in allowed[own]:
                errors.append(f'agenda/agenda.csv: {pid} is {status_of.get(pid)}, but its domain file marks it {own}')
        lib = module(root / 'library/build_catalog.py', 'library_catalog')
        current = lib.catalog_rows()
        if [r['path'] for r in current] != [r['path'] for r in catalog]:
            errors.append('library/catalog.csv: files are uncatalogued or out of order (run library/build_catalog.py)')
        errors += [f'library/catalog.csv: {r["id"]}: {r["path"]} no longer exists'
                   for r in catalog if not lib.is_citation(r) and not (root / r['path']).exists()]
        errors += [f'library/catalog.csv: {r["id"]}: a citation row needs an http(s) address as its path'
                   for r in catalog if lib.is_citation(r) and not r['path'].startswith(('https://', 'http://'))]
        if (root / 'library/name-index.md').read_text() != lib.name_index(current):
            errors.append('library/name-index.md is stale (run library/build_catalog.py)')
    charter_errors, known = check_charter(root)
    errors += charter_errors
    dossier_errors, dossier_warnings, evidence = check_dossiers(root, catalog, agenda, today)
    errors += dossier_errors
    warnings += dossier_warnings
    known.update({'SRC': {r['id'] for r in catalog}, 'EV': evidence})
    errors += check_references(root, known)
    return errors, warnings, {'agenda': len(agenda), 'sources': len(catalog), 'evidence': len(evidence),
                              'decisions': len(known['DEC']), 'outcomes': len(known['OUT'])}


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--strict', action='store_true', help='treat past-due re-checks as errors')
    args = ap.parse_args()
    errors, warnings, counts = run()
    if args.strict:
        errors, warnings = errors + warnings, []
    for w in warnings:
        print('warning:', w)
    for e in errors:
        print('error:', e)
    summary = ', '.join(f'{v} {k}' for k, v in counts.items())
    print(f'Registry: {summary}; ' + ('all links resolve' if not errors else f'{len(errors)} problem(s)'))
    sys.exit(1 if errors else 0)
