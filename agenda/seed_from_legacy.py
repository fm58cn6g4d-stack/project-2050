#!/usr/bin/env python3
"""Seed agenda/agenda.csv from the legacy domain files and options register (stage A, step 2).

Run once; agenda.csv is then the authored record and is edited by hand. Re-running with --write
overwrites authored edits, so it refuses when agenda.csv exists unless --force is given.
--check (no writing) verifies that every ID the legacy files define is in agenda.csv exactly once.

  python3 agenda/seed_from_legacy.py --check
"""
import argparse
import csv
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = ROOT / 'legacy/domains'
REGISTER = ROOT / 'legacy/index/options-register.md'
OUT = ROOT / 'agenda/agenda.csv'
ID = r'[A-Z]{2,4}-[A-Z]{0,3}\d+[A-Za-z]?'
COLUMNS = ['id', 'name', 'home_dossier', 'level', 'status', 'source', 'note']


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def plain(text):
    text = re.sub(r'\*+|`', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)
    return re.sub(r'\s+', ' ', text).strip(' .;:')


def domain_definitions():
    """ID -> {name, flags, source} for IDs defined in their own domain file (table first cell or heading)."""
    found = {}
    for path in sorted(DOMAINS.glob('*.md')):
        text = path.read_text()
        m = re.search(r'\(([A-Z]{2,4})\)\s*$', text.splitlines()[0])
        prefix = m.group(1) if m else None
        rel = str(path.relative_to(ROOT))
        section = ''
        for n, line in enumerate(text.splitlines(), 1):
            if line.startswith('#'):
                section = line.lower()
            head = re.match(rf'#+\s+({ID})[.:]?\s+(.*)', line)
            row = re.match(rf'\|\s*\**({ID})\**\s*(\([^)|]*\))?\s*\|', line) if line.startswith('|') else None
            if head:
                pid, name, flag = head.group(1), head.group(2), ''
            elif row:
                c = cells(line)
                pid, flag = row.group(1), (row.group(2) or '')
                name = c[1] if len(c) > 1 else ''
            else:
                continue
            if prefix and not pid.startswith(prefix + '-'):
                continue
            entry = found.setdefault(pid, {'name': '', 'flags': set(), 'source': f'{rel}:{n}'})
            if not entry['name'] and name:
                entry['name'] = plain(name)
            entry['flags'].add(flag.lower() + ' ' + name.lower())
            if row and re.search(r'add-on|options\b|alternatives', section) and not re.match(rf'#+\s+{pid}\b', section):
                entry['flags'].add('(option in an options section)')
    return found


def expand(first):
    """'REV-G1, G3, G5-G11' -> ['REV-G1', 'REV-G3', 'REV-G5', ..., 'REV-G11']."""
    first = plain(first)
    m = re.match(r'([A-Z]{2,4})-', first)
    if not m:
        return []
    prefix, out = m.group(1), []
    for part in re.split(r',\s*|\s+and\s+|\s*/\s*', first):
        part = part.split(' ')[0]
        part = part if part.startswith(prefix + '-') else f'{prefix}-{part}'
        r = re.fullmatch(rf'{prefix}-([A-Z]*)(\d+)-([A-Z]*)(\d+)', part)
        if r and r.group(1) == r.group(3):
            out += [f'{prefix}-{r.group(1)}{i}' for i in range(int(r.group(2)), int(r.group(4)) + 1)]
        elif re.fullmatch(ID, part):
            out.append(part)
    return out


def register_statuses():
    """ID -> (status, what, line) from section 6 of the options register."""
    out, header, live = {}, None, False
    for n, line in enumerate(REGISTER.read_text().splitlines(), 1):
        if line.startswith('## '):
            live = line.startswith('## 6.')
        if not live or not line.startswith('|') or set(line) <= set('|- '):
            continue
        c = cells(line)
        if c[0] == 'ID':
            header = c
            continue
        if header and 'Status' in header and len(c) == len(header):
            ids = expand(c[0])
            for pid in ids:
                out.setdefault(pid, (plain(c[header.index('Status')]), plain(c[1]), n, len(ids)))
    return out

HOME = {'HLT': 'care', 'HOU': 'home', 'CLI': 'clean-power', 'LAB': 'work', 'IMM': 'immigration',
        'DEM': 'foundations/democratic-renewal', 'INT': 'foundations/democratic-renewal',
        'CRT': 'foundations/democratic-renewal', 'CAP': 'foundations/democratic-renewal',
        'REV': 'foundations/fair-financing', 'SS': 'secure-floor', 'EDU': 'agenda/education',
        'MOV': 'agenda/transportation', 'MR': 'agenda/transportation', 'AMD': 'agenda/amendments',
        'EXE': 'agenda/executive-power', 'RTS': 'agenda/rights', 'SAF': 'agenda/public-safety',
        'NSC': 'agenda/national-security', 'COM': 'agenda/competition', 'AI': 'agenda/ai'}


def home(pid):
    """Plan 3.1: the flagship or foundation an item belongs to; dossier work may refine it."""
    if pid.startswith('FAM-2'):
        return 'care'
    if pid.startswith('FAM-4'):
        return 'agenda/education'
    if pid.startswith(('FAM-', 'LAB-10')):
        return 'secure-floor'
    if pid.startswith('SS-B'):
        return 'agenda/social-security'
    if re.match(r'REV-C\d', pid):
        return 'clean-power'
    return HOME[re.match(r'[A-Z]+', pid).group(0)]


def status(pid, flags, reg, group=1):
    """Normalize to decided / chosen / option / alternative / held / declined / retired / pointer.

    Only the first clause of the register's status counts. A register row covering several lettered
    options ("C chosen; ...") applies to the named letter; its siblings are alternatives.
    """
    f = ' '.join(flags)
    text = (reg or '').split(';')[0].lower()
    if group > 1:
        letter = re.match(r'[A-Z]+-[A-Z]*\d+([A-Z]?)', pid).group(1).lower()
        named = re.match(r'(?:[a-z]+-)?(?:\d+)?([a-z])\b\s+(chosen|decided|amended|adopted)', text)
        if named:
            text = text if letter == named.group(1) else ''
            if not text:
                return ('chosen' if '(chosen' in f else 'alternative'), reg
    if text.startswith('open') or 'not adopted' in text:
        return 'option', reg
    for key, words in (('retired', ('retired', 'duplicate')), ('pointer', ('pointer',)),
                       ('declined', ('declined', 'not recommended', 'not chosen', 'rejected')),
                       ('held', ('held', 'parked', 'reserve')),
                       ('decided', ('decided', 'selected', 'booked', 'adopted', 'accepted', 'approved')),
                       ('chosen', ('chosen', 'kept', 'revised', 'sized', 'amended')),
                       ('option', ('option', 'open', 'study', 'explore', 'pending', 'unselected'))):
        if any(w in text for w in words):
            return key, reg
    if 'option, not chosen' in f or '(option' in f or 'option)' in f or '*option' in f:
        return 'option', reg
    if 'chosen' in f or 'selected' in f:
        return 'chosen', reg
    if re.search(r'\d[A-Za-z]$', pid):
        return 'alternative', reg   # a lettered variant with no chosen mark
    return 'chosen', reg            # a numbered program in its domain's design


LEVEL = {'decided': 'L2', 'chosen': 'L2', 'option': 'L1', 'alternative': 'L1', 'held': 'L1', 'declined': 'L1',
         'pointer': 'L1', 'retired': 'L0'}


def transportation():
    out = []
    for name in ('ledger-bills.csv', 'ledger-revenue.csv'):
        path = ROOT / 'models/data/inputs' / name
        with path.open(newline='') as f:
            for n, r in enumerate(csv.DictReader(f), 2):
                if re.match(r'(MOV-\d+|MR\d+)$', r['id']):
                    out.append((r['id'], plain(r.get('bill') or r.get('name') or r.get(list(r)[1])),
                                f'{path.relative_to(ROOT)}:{n}'))
    return out


# Components of the decided climate package (Package A, O5, CLI-7C), booked by PR #45 on October 28.
CLIMATE_COMPONENTS = {'CLI-2O', 'CLI-4H', 'CLI-5L', 'CLI-5W', 'CLI-7K', 'CLI-7N', 'CLI-10G', 'CLI-13A', 'CLI-13F',
                      'REV-C1P', 'REV-CB1', 'REV-CXP'}


def mentioned_decisions(reg):
    """IDs a register status names as adopted inside another row, e.g. DEM-1A's '1E adopted Oct 20'."""
    out = {}
    for pid, (text, _, n, _) in reg.items():
        prefix = pid.split('-')[0]
        for num, word in re.findall(r'\b(\d+[A-Z])\s+(adopted|decided)', text):
            out.setdefault(f'{prefix}-{num}', f'{prefix}-{num} {word} (register line {n})')
    return out


def seed():
    defs, reg = domain_definitions(), register_statuses()
    mentioned = mentioned_decisions(reg)
    corpus = '\n'.join(p.read_text() for p in DOMAINS.glob('*.md'))
    rows = []
    for pid in sorted(set(defs) | set(reg), key=sort_key):
        if pid not in defs and not re.search(rf'\b{re.escape(pid)}\b', corpus):
            continue  # a register shorthand, not an ID any domain file uses
        d = defs.get(pid, {'name': '', 'flags': set(), 'source': ''})
        r = reg.get(pid)
        st, why = status(pid, d['flags'], r[0] if r else '', r[3] if r else 1)
        name = d['name'] or (r[1] if r else '')
        source = d['source'] or f'{REGISTER.relative_to(ROOT)}:{r[2]}'
        note = f'Register: {why}' if why else ''
        if pid in CLIMATE_COMPONENTS:
            st, note = 'decided', 'Component of the decided climate package (Package A, O5, CLI-7C), booked by PR #45'
        elif pid in mentioned and st != 'decided':
            st, note = 'decided', 'Register: ' + mentioned[pid]
        rows.append({'id': pid, 'name': name[:160], 'home_dossier': home(pid), 'level': LEVEL[st],
                     'status': st, 'source': source, 'note': note[:200]})
    for pid, name, source in transportation():
        rows.append({'id': pid, 'name': name[:160], 'home_dossier': home(pid), 'level': 'L2', 'status': 'chosen',
                     'source': source, 'note': 'Draft 2 bill text exists (legacy/domains/transportation-moving-america-act-2031-draft-2.md); L3 when converted to a dossier with evidence'})
    return rows


def sort_key(pid):
    m = re.match(r'([A-Z]+)-([A-Z]*)(\d+)(.*)', pid)
    return (m.group(1), m.group(2), int(m.group(3)), m.group(4)) if m else (pid, '', 0, '')


def load():
    with OUT.open(newline='') as f:
        return list(csv.DictReader(f))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--write', action='store_true', help='write the seed (only when agenda.csv does not exist)')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--dump', action='store_true', help='print the raw extraction as CSV')
    args = ap.parse_args()
    defs, reg = domain_definitions(), register_statuses()
    if args.dump:
        w = csv.writer(sys.stdout)
        w.writerow(['id', 'name', 'flags', 'source', 'reg_status', 'reg_what'])
        for pid in sorted(set(defs) | set(reg)):
            d, r = defs.get(pid, {}), reg.get(pid, ('', '', ''))
            w.writerow([pid, d.get('name', ''), ' || '.join(sorted(d.get('flags', []))), d.get('source', ''), r[0], r[1]])
        sys.exit(0)
    if args.write:
        if OUT.exists() and not args.force:
            sys.exit('agenda.csv exists and is authored; pass --force to overwrite it')
        with OUT.open('w', newline='') as f:
            w = csv.DictWriter(f, COLUMNS, lineterminator='\n')
            w.writeheader()
            w.writerows(seed())
        print(f'wrote {OUT.relative_to(ROOT)}')
        sys.exit(0)
    if args.check:
        rows = load()
        ids = [r['id'] for r in rows]
        dup = sorted({i for i in ids if ids.count(i) > 1})
        missing = sorted({r['id'] for r in seed()} - set(ids))
        bad = [r['id'] for r in rows if r['level'] not in {'L0', 'L1', 'L2', 'L3', 'L4'} or list(r) != COLUMNS]
        for label, items in (('duplicate', dup), ('missing from agenda.csv', missing), ('bad level/columns', bad)):
            if items:
                print(f'{label}: {", ".join(items)}')
        sys.exit(1 if dup or missing or bad else print(f'agenda.csv: {len(rows)} rows; every legacy ID present once') or 0)
