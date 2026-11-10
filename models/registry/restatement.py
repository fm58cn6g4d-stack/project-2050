"""Restatement check: what a legacy file says that the dossier replacing it no longer says.

Role: the check `charter/PLAN.md` section 4 calls for. When legacy content becomes a canonical dossier, every
number and policy ID in the source should appear in the result, or be accounted for: dropped on purpose
with a reason in the decision log, or flagged. Status: current; it reports and never fails the checks.

Usage (from the repo root):
  python3 models/registry/restatement.py SOURCE RESULT [RESULT ...] [--accounted FILE ...] [--limit N]
  python3 models/registry/restatement.py --all          # every dossiers/**/restatement.json, summary only
  python3 models/registry/restatement.py --map dossiers/agenda/transportation/restatement.json

RESULT and --accounted take paths or glob patterns relative to the repo root. A token counts as accounted
for when it appears in `backticks` in an accounted file (the dossier's restatement log, or the decision
log), so an explicit flag is needed, not a stray match.

What counts:
- policy IDs: hyphenated IDs (A-23, MOV-29, HOU-4A.01, DEC-2026-10-30-02) and every agenda ID in
  agenda/agenda.csv that the source names (MR1, R2);
- numbers: every other run of digits, with thousands commas and trailing decimal zeros dropped, so
  "$55.00B" in the source matches "$55B" in the result, "1,000" matches "1000" and "07" matches "7".
  Matching is set-wide: a token counts as carried over if it appears anywhere in the result files, not
  necessarily in the same statement, so the report finds what was dropped, not what was changed.
  The map file and the accounted files are never counted as results. Numbers inside IDs,
  link targets and bare URLs are ignored.

A restatement map (JSON) lists the pairs for one dossier:
  {"role": "...", "pairs": [{"source": "legacy/...md", "result": ["dossiers/x/*.md"], "accounted": ["..."]}]}
"""
import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HYPHEN_ID = re.compile(r'\b[A-Z][A-Z0-9]{0,4}(?:-[A-Z0-9]+)*-\d+[A-Za-z]?(?:\.\d{2})?\b')
NUMBER = re.compile(r'\d+(?:,\d{3})*(?:\.\d+)?')
LINK_TARGET = re.compile(r'\]\([^)]*\)')
URL = re.compile(r'https?://\S+')
TICKED = re.compile(r'`([^`\n]+)`')


def norm(number):
    """'1,000' -> '1000'; '55.00' -> '55'; '0.180' -> '0.18'; '07' -> '7'."""
    n = number.replace(',', '')
    if '.' in n:
        n = n.rstrip('0').rstrip('.')
    whole, dot, frac = n.partition('.')
    return (whole.lstrip('0') or '0') + dot + frac


def agenda_ids(root):
    path = root / 'agenda/agenda.csv'
    if not path.exists():
        return set()
    with path.open(newline='') as f:
        return {r['id'] for r in csv.DictReader(f)}


def tokens(text, known_ids=frozenset()):
    """(ids, numbers) in text, each a dict of token -> first 1-based line."""
    ids, nums = {}, {}
    for lineno, line in enumerate(text.splitlines(), 1):
        line = URL.sub(' ', LINK_TARGET.sub(']', line))
        found = HYPHEN_ID.findall(line)
        found += [w for w in re.findall(r'\b[A-Z][A-Z0-9.-]*[0-9A-Za-z]\b', line)
                  if w in known_ids and w not in found]
        for tok in found:
            ids.setdefault(tok, lineno)
        rest = HYPHEN_ID.sub(' ', line)
        for tok in found:
            rest = re.sub(rf'\b{re.escape(tok)}\b', ' ', rest)
        for raw in NUMBER.findall(rest):
            nums.setdefault(norm(raw), lineno)
    return ids, nums


def expand(root, patterns):
    paths = []
    for p in patterns:
        hits = sorted(root.glob(p)) if any(c in p for c in '*?[') else [root / p]
        paths += [h for h in hits if h.is_file() and h not in paths]
    return paths


def accounted_tokens(paths):
    """Tokens written in backticks in the accounted files, normalized like the source's."""
    out = set()
    for path in paths:
        for tick in TICKED.findall(path.read_text(errors='replace')):
            tick = tick.strip()
            out.add(tick)
            if NUMBER.fullmatch(tick.lstrip('$').rstrip('%BMTK¢')):
                out.add(norm(tick.lstrip('$').rstrip('%BMTK¢')))
    return out


def compare(root, source, results, accounted=(), known_ids=None):
    """Tokens in source missing from every result file, split into accounted and unaccounted."""
    known_ids = agenda_ids(root) if known_ids is None else known_ids
    src_text = (root / source).read_text(errors='replace')
    src_ids, src_nums = tokens(src_text, known_ids)
    have_ids, have_nums = set(), set()
    for path in results:
        i, n = tokens(path.read_text(errors='replace'), known_ids)
        have_ids |= set(i)
        have_nums |= set(n)
    flagged = accounted_tokens(accounted)
    report = {'source': str(source), 'results': [str(p.relative_to(root)) for p in results],
              'ids': len(src_ids), 'numbers': len(src_nums), 'missing': [], 'accounted': []}
    for kind, src, have in (('id', src_ids, have_ids), ('number', src_nums, have_nums)):
        for tok, line in sorted(src.items(), key=lambda kv: kv[1]):
            if tok in have:
                continue
            row = {'kind': kind, 'token': tok, 'line': line}
            report['accounted' if tok in flagged else 'missing'].append(row)
    return report


def context(root, source, line, width=90):
    text = (root / source).read_text(errors='replace').splitlines()
    return text[line - 1].strip()[:width] if 0 < line <= len(text) else ''


def print_report(root, r, limit):
    ids = sum(1 for m in r['missing'] if m['kind'] == 'id')
    nums = len(r['missing']) - ids
    print(f"{r['source']} -> {len(r['results'])} file(s): {r['ids']} IDs and {r['numbers']} numbers in the source; "
          f"not carried over: {ids} IDs, {nums} numbers; accounted for in the log: {len(r['accounted'])}")
    if limit is None:
        return
    shown = r['missing'] if limit == 0 else r['missing'][:limit]
    for m in shown:
        print(f"  L{m['line']:<5} {m['kind']:<6} {m['token']:<14} {context(root, r['source'], m['line'])}")
    if limit and len(r['missing']) > limit:
        print(f"  ... {len(r['missing']) - limit} more (run with --limit 0 for all)")


def run_map(root, map_path, limit):
    spec = json.loads((root / map_path).read_text())
    reports = []
    for pair in spec.get('pairs', []):
        accounted = expand(root, pair.get('accounted', []))
        # The map and the accounted files are not the restatement: a token in them must not read as carried over.
        skip = {(root / map_path).resolve()} | {p.resolve() for p in accounted}
        results = [p for p in expand(root, pair.get('result', [])) if p.resolve() not in skip]
        if not (root / pair['source']).exists():
            print(f"{map_path}: source {pair['source']} not found")
            continue
        r = compare(root, pair['source'], results, accounted)
        print_report(root, r, limit)
        reports.append(r)
    return reports


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('source', nargs='?')
    ap.add_argument('result', nargs='*')
    ap.add_argument('--accounted', nargs='*', default=[])
    ap.add_argument('--map', help='a restatement map (JSON)')
    ap.add_argument('--all', action='store_true', help='every dossiers/**/restatement.json, summary lines only')
    ap.add_argument('--limit', type=int, default=40, help='missing tokens to list per pair (0: all)')
    ap.add_argument('--strict', action='store_true', help='exit 1 when anything is unaccounted for')
    a = ap.parse_args(argv)
    if a.all:
        maps = sorted((ROOT / 'dossiers').rglob('restatement.json'))
        reports = []
        for m in maps:
            reports += run_map(ROOT, m.relative_to(ROOT), limit=None)
        if not maps:
            print('No restatement maps yet (dossiers/**/restatement.json).')
    elif a.map:
        reports = run_map(ROOT, a.map, a.limit)
    elif a.source and a.result:
        r = compare(ROOT, a.source, expand(ROOT, a.result), expand(ROOT, a.accounted))
        print_report(ROOT, r, a.limit)
        reports = [r]
    else:
        ap.error('give SOURCE and RESULT files, --map or --all')
    missing = sum(len(r['missing']) for r in reports)
    return 1 if a.strict and missing else 0


if __name__ == '__main__':
    sys.exit(main())
