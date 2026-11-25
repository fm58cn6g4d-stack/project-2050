#!/usr/bin/env python3
"""The toolkit's parameter-file schema, its validator and the evidence-table generator.

Role: one rule for every model's inputs (`models/schema/README.md`, "Parameter files"). Status:
current (stage H step H2a); provisional until the first models move onto it (H3 to H6).

A parameter file is a CSV, one row per input, with these columns:

  id      required  unique, lower case: letters, digits, '_' and '.'
  value   required  a number (or, with unit 'text', a label)
  unit    required  e.g. '$ billion', 'million people', 'share', 'ratio', 'text'
  year    required  the year the value is for: 2032, FY2032, CY2032, a span 2025-2034 or FY2030-FY2039,
                    or 'none' for a value with no year (an elasticity, a ratio held fixed)
  kind    required  evidence (a measured or published figure), assumption (a judgment), or
                    policy (a parameter of current law or of a reform, set by statute or by the plan)
  source  required  evidence and policy rows: an evidence ID (EV-, SRC-, DEC-, ASM-) or an https URL,
                    several joined by '; '; assumption rows: the basis in words, IDs where they exist
  low     optional  required for an assumption: the low end of its tested range
  high    optional  required for an assumption: the high end; low <= value <= high
  note    optional  plain words

Optional extra columns ('label', 'group', 'statute') are allowed and carried into the table.

  python3 models/schema/parameters.py FILE [--map old=new ...] [--table] [--card CARD]

--map reads a file whose columns still have older names (health coverage's 'evidence_id_or_basis'
is 'source'); --table prints the evidence table; --card rewrites the card's generated block
(between '<!-- generated:parameters:start -->' and '<!-- generated:parameters:end -->').
Exit 1 if the file breaks the schema. Standard library only.
"""
import argparse, csv, io, re, sys
from pathlib import Path

REQUIRED = ['id', 'value', 'unit', 'year', 'kind', 'source']
OPTIONAL = ['low', 'high', 'note']
KINDS = ('evidence', 'assumption', 'policy')
ID_RE = re.compile(r'^[a-z0-9][a-z0-9_.]*$')
YEAR_RE = re.compile(r'^(?:(FY|CY)?(\d{4})(?:-(?:FY|CY)?(\d{4}))?|none)$')
EVID_RE = re.compile(r'\b(?:EV-[A-Z]+-\d+[a-z]?|SRC-\d+|DEC-\d{4}-\d{2}-\d{2}-\d+|ASM-[A-Za-z0-9-]+)\b')
URL_RE = re.compile(r'https://\S+')
START, END = '<!-- generated:parameters:start -->', '<!-- generated:parameters:end -->'


def number(s):
    try:
        return float(s.replace(',', ''))
    except (ValueError, AttributeError):
        return None


def read(path, colmap=None):
    """Rows as dicts with schema column names (colmap renames old column names)."""
    text = Path(path).read_text(encoding='utf-8')
    rows = list(csv.DictReader(io.StringIO(text)))
    colmap = colmap or {}
    return [{colmap.get(k, k): (v or '').strip() for k, v in r.items()} for r in rows]


def validate(rows):
    """A list of problems, each 'row N (id): message'. Empty means the file meets the schema."""
    errs = []
    if not rows:
        return ['no rows']
    missing = [c for c in REQUIRED if c not in rows[0]]
    if missing:
        return [f'missing column(s): {", ".join(missing)}']
    seen = set()
    for n, r in enumerate(rows, start=2):
        rid = r['id']
        at = f'row {n} ({rid or "no id"})'
        if not ID_RE.match(rid):
            errs.append(f'{at}: id must be lower case letters, digits, "_" or "."')
        if rid in seen:
            errs.append(f'{at}: duplicate id')
        seen.add(rid)
        for c in REQUIRED:
            if not r.get(c):
                errs.append(f'{at}: empty {c}')
        if r['kind'] and r['kind'] not in KINDS:
            errs.append(f'{at}: kind must be one of {", ".join(KINDS)}')
        m = YEAR_RE.match(r['year']) if r['year'] else None
        if r['year'] and not m:
            errs.append(f'{at}: year "{r["year"]}" is not 2032, FY2032, CY2032, 2025-2034 or none')
        elif m and m.group(3) and int(m.group(3)) < int(m.group(2)):
            errs.append(f'{at}: year span runs backward')
        v = number(r['value'])
        if r['value'] and v is None and r['unit'] != 'text':
            errs.append(f'{at}: value "{r["value"]}" is not a number (use unit "text" for a label)')
        src = r['source']
        if r['kind'] in ('evidence', 'policy') and src and not (EVID_RE.search(src) or URL_RE.search(src)):
            errs.append(f'{at}: a {r["kind"]} row needs an evidence ID (EV-, SRC-, DEC-, ASM-) or an https URL')
        lo, hi = number(r.get('low', '')), number(r.get('high', ''))
        if r['kind'] == 'assumption':
            if lo is None or hi is None:
                errs.append(f'{at}: an assumption needs a low and a high value')
        if lo is not None and hi is not None:
            if lo > hi:
                errs.append(f'{at}: low is above high')
            elif v is not None and not (lo <= v <= hi):
                errs.append(f'{at}: value is outside its range')
        elif (r.get('low') or r.get('high')) and (lo is None or hi is None):
            errs.append(f'{at}: low and high must both be numbers')
    return errs


def summary(rows):
    k = {kind: sum(1 for r in rows if r['kind'] == kind) for kind in KINDS}
    return (f"{len(rows)} inputs: {k['evidence']} traced to evidence, {k['policy']} policy parameters, "
            f"{k['assumption']} labeled assumptions with a tested range.")


def esc(s):
    return s.replace('|', '\\|')


def table(rows):
    """The card's evidence table (Markdown), generated from the parameter file."""
    out = [summary(rows), '', '| ID | Value | Unit | Year | Kind | Source or basis | Range |', '| --- | --- | --- | --- | --- | --- | --- |']
    for r in rows:
        rng = f"{r.get('low', '')} to {r.get('high', '')}" if r.get('low') and r.get('high') and r['low'] != r['high'] else ''
        label = r.get('label') or r.get('note', '')
        rid = f"`{r['id']}`" + (f" {esc(label)}" if label else '')
        out.append(f"| {rid} | {esc(r['value'])} | {esc(r['unit'])} | {r['year']} | {r['kind']} | {esc(r['source'])} | {rng} |")
    return '\n'.join(out)


def update_card(card, text):
    """Replace the generated block in a card; return the new card text (the caller writes it)."""
    s = Path(card).read_text(encoding='utf-8')
    if START not in s or END not in s:
        raise ValueError(f'{card}: no generated parameters block ({START} ... {END})')
    a, b = s.index(START) + len(START), s.index(END)
    return s[:a] + '\n' + text + '\n' + s[b:]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('file')
    ap.add_argument('--map', action='append', default=[], help='old=new column name')
    ap.add_argument('--table', action='store_true')
    ap.add_argument('--card')
    a = ap.parse_args(argv)
    colmap = dict(m.split('=', 1) for m in a.map)
    rows = read(a.file, colmap)
    errs = validate(rows)
    for e in errs[:50]:
        print(f'{a.file}: {e}')
    if len(errs) > 50:
        print(f'... and {len(errs) - 50} more')
    if errs:
        print(f'{a.file}: {len(errs)} problem(s)')
        return 1
    if a.table:
        print(table(rows))
    if a.card:
        Path(a.card).write_text(update_card(a.card, table(rows)), encoding='utf-8')
    print(f'{a.file}: meets the parameter schema. {summary(rows)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
