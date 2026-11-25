#!/usr/bin/env python3
"""Checks the toolkit's register, run log, results headers and versions.

Role: the `RUN-` and schema checks of stage H step H2a (`models/schema/README.md`). Status: current;
the release criteria it reads are provisional until Espen answers memo H1
(`models/stage-h/memos/H1-what-released-means.md`). Standard library only.

    python3 models/registry/toolkit_check.py [--base REF] [--no-git]

1. **The register** (`models/toolkit.csv`): its criterion columns are exactly the IDs in
   `models/release-criteria.csv`, so changing the criteria means editing that file and the columns
   together; model IDs are unique `MOD-` IDs; each criterion reads pass, partial, fail or n/a; no
   model is "released" or "preview" while memo H1 is undecided (CRITERIA_DECISION below); and for each
   criterion a script can test, a recorded "pass" the script can't confirm is an error (the register
   may understate a model, never overstate it; an understatement is a warning).
2. **The run log** (`models/runs.csv`): columns, `RUN-<model>-<date>-<letter>` IDs, unique, a
   registered model, a 40-character commit, a sha256 of the results.
3. **Results headers**: every file in a model's results column that carries a header is valid
   (`models/schema/results.py`); a JSON header's model ID matches the register row.
4. **Versions**: a model's CHANGELOG.md has an entry for its header's version, and it is the newest.
   Against the base (the merge base with origin/main; on main itself, the first parent): a changed
   results file needs a higher version and a changelog entry for it; a patch bump (same major and
   minor) may not change anything outside the header.

   The newest changelog entry has a "Results:" line; entries run newest first; every JSON results
   file of a model carries the same version. Any edit to a model's code changes its hash in the
   header, so it changes the results file and takes at least a patch bump.
5. **Recorded runs** are append-only against the base, and each row's commit is an ancestor of HEAD
   (a warning when a shallow clone lacks it); the register's `assessed_version` matches the results
   header, its status matches the header's, and a reviewed criterion's "pass" links its review.

Exit 1 on any error. `--no-git` skips the comparisons with the base; `--require-base` (for CI) fails
when no base is found instead of skipping.
"""
import argparse, csv, io, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'models' / 'schema'))
import parameters as params_schema  # noqa: E402
import results as results_schema  # noqa: E402



def set_root(root):
    """Point the check at a repository (the tests use a scratch one)."""
    global ROOT, TOOLKIT, CRITERIA, RUNS, TEMPLATE, CHECK_SCRIPTS
    ROOT = Path(root)
    TOOLKIT = ROOT / 'models' / 'toolkit.csv'
    CRITERIA = ROOT / 'models' / 'release-criteria.csv'
    RUNS = ROOT / 'models' / 'runs.csv'
    TEMPLATE = ROOT / 'models' / 'MODEL-CARD-TEMPLATE.md'
    CHECK_SCRIPTS = [ROOT / 'models/tools/run-all.sh', ROOT / '.github/scripts/run-checks.sh']


set_root(ROOT)
CRITERIA_DECISION = None   # the DEC- ID that answers memo H1; until then nothing is released or in preview
FIXED = ['model_id', 'name', 'path', 'status', 'owner', 'card', 'parameters', 'parameters_map', 'results', 'tests', 'assessed_version']
TAIL = ['notes']
VALUES = ('pass', 'partial', 'fail', 'n/a')
STATUSES = ('none', 'exploratory', 'working', 'preview', 'released')
RUN_COLUMNS = ['run_id', 'date', 'model_id', 'model_version', 'commit', 'python', 'command', 'results_path', 'results_sha256',
               'inputs_sha256', 'note']
URL_RE = re.compile(r'https://\S+')
RUN_RE = re.compile(r'^RUN-([a-z0-9]+(?:-[a-z0-9]+)*)-(\d{4}-\d{2}-\d{2})-([a-z])$')
VER_HEAD = re.compile(r'^## (\d+\.\d+\.\d+)\b', re.M)


def read_csv(path):
    return list(csv.DictReader(io.StringIO(Path(path).read_text(encoding='utf-8'))))


def split(cell):
    return [x.strip() for x in (cell or '').split(';') if x.strip()]


def template_headings():
    return [h.strip() for h in re.findall(r'^## (.+)$', TEMPLATE.read_text(encoding='utf-8'), re.M)]


def json_header(path):
    try:
        d = json.loads(Path(path).read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        return None
    return d.get('header') if isinstance(d, dict) else None


def model_version(row):
    for f in split(row['results']):
        if f.endswith('.json'):
            h = json_header(ROOT / f)
            if h:
                return h.get('model_version')
    return None


# ---------------------------------------------------------------- what a script can see per criterion
def auto_criteria(row, runs):
    """{criterion: (value, reason)} for the criteria a script can test."""
    out = {}
    out['rc_license'] = ('pass', 'LICENSE found') if (ROOT / 'LICENSE').exists() else ('fail', 'no LICENSE at the root (memo H2, step H2b)')
    path = ROOT / row['path'] if row['path'] else None
    ver = model_version(row)
    cl = path / 'CHANGELOG.md' if path else None
    if not ver:
        out['rc_versioned'] = ('fail', 'no results header with a version')
    elif not cl or not cl.exists():
        out['rc_versioned'] = ('fail', 'no CHANGELOG.md')
    else:
        vs = VER_HEAD.findall(cl.read_text(encoding='utf-8'))
        out['rc_versioned'] = ('pass', f'{ver}, changelog current') if vs and vs[0] == ver else ('fail', f'changelog newest entry {vs[:1]} is not {ver}')
    card = ROOT / row['card'] if row['card'] else None
    if not card or not card.exists():
        out['rc_card'] = ('fail', 'no card')
        out['rc_known_issues'] = ('fail', 'no card')
    else:
        text = card.read_text(encoding='utf-8')
        heads = [h.strip().lower() for h in re.findall(r'^## (.+)$', text, re.M)]
        need = [h for h in template_headings() if h.lower() not in heads]
        head_ok = bool(re.search(r'Status: \*\*(exploratory|working|preview|released)\*\*', text)) and 'Owner:' in text[:3000]
        if need or not head_ok:
            out['rc_card'] = ('fail', ('missing headings: ' + '; '.join(need) if need else '') + ('' if head_ok else ' no status/owner line'))
        else:
            out['rc_card'] = ('pass', 'on the template')
        out['rc_known_issues'] = ('pass', 'heading found') if 'known issues' in heads else ('fail', 'no "Known issues" heading')
    if not row['parameters']:
        out['rc_parameters'] = ('fail', 'no parameter file')
    else:
        colmap = dict(m.split('=', 1) for m in split(row['parameters_map']))
        errs = []
        for f in split(row['parameters']):
            errs += params_schema.validate(params_schema.read(ROOT / f, colmap))
        out['rc_parameters'] = ('pass', 'meets the schema') if not errs else ('fail', f'{len(errs)} schema problem(s), first: {errs[0]}')
    tests = split(row['tests'])
    scripts = '\n'.join(p.read_text(encoding='utf-8') for p in CHECK_SCRIPTS if p.exists())
    def in_checks(t):
        short = t[len('models/tools/'):] if t.startswith('models/tools/') else t
        return t in scripts or ('"$TOOLS"/' + short) in scripts
    missing = [t for t in tests if not in_checks(t)]
    out['rc_tests_in_checks'] = ('fail', 'no tests listed') if not tests else (('pass', 'all in the checks') if not missing else ('fail', 'not in the checks: ' + ', '.join(missing)))
    mine = [r for r in runs if r['model_id'] == row['model_id']]
    if not mine:
        out['rc_run_log'] = ('fail', 'no RUN- row in models/runs.csv')
    elif ver and not any(r['model_version'] == ver for r in mine):
        out['rc_run_log'] = ('fail', f'no RUN- row for the current version {ver}')
    else:
        out['rc_run_log'] = ('pass', 'a RUN- row for the current version')
    res = split(row['results'])
    if not res:
        out['rc_disclaimer'] = ('fail', 'no results files listed')
    else:
        bad = [f for f in res if results_schema.check_file(ROOT / f)]
        out['rc_disclaimer'] = ('pass', 'every results file has the header') if not bad else ('fail', 'no valid header: ' + ', '.join(bad))
    return out


# ---------------------------------------------------------------- checks
def check_register(errs, warns):
    crit = [r['id'] for r in read_csv(CRITERIA)]
    rows = read_csv(TOOLKIT)
    cols = list(rows[0].keys()) if rows else []
    if cols != FIXED + crit + TAIL:
        errs.append(f'toolkit.csv columns must be {FIXED} + the criteria in release-criteria.csv {crit} + {TAIL}; found {cols}')
        return rows
    runs = read_csv(RUNS) if RUNS.exists() else []
    auto = {r['id'] for r in read_csv(CRITERIA) if r['auto'] == 'yes'}
    seen = set()
    for r in rows:
        m = r['model_id']
        if not results_schema.MOD_RE.match(m):
            errs.append(f'toolkit.csv: "{m}" is not a MOD- ID')
        if m in seen:
            errs.append(f'toolkit.csv: {m} appears twice')
        seen.add(m)
        if r['status'] not in STATUSES:
            errs.append(f'toolkit.csv {m}: status must be one of {STATUSES}')
        ver = model_version(r)
        if ver and r['assessed_version'] != ver:
            errs.append(f'toolkit.csv {m}: assessed_version "{r["assessed_version"]}" is not the results header\'s {ver}; reassess the criteria')
        for f in split(r['results']):
            h = json_header(ROOT / f) if f.endswith('.json') else None
            if h and h.get('status') != r['status']:
                errs.append(f'{f}: header status "{h.get("status")}" is not the register\'s "{r["status"]}"')
        manual = {c['id'] for c in read_csv(CRITERIA) if c['auto'] != 'yes'}
        for c in sorted(manual):
            if r.get(c) == 'pass' and not URL_RE.search(r['notes']):
                errs.append(f'toolkit.csv {m}: {c} is a reviewed criterion; a "pass" needs a link to the review in notes')
        if r['status'] in ('released', 'preview') and not CRITERIA_DECISION:
            errs.append(f'toolkit.csv {m}: "{r["status"]}" before memo H1 is decided (the criteria are provisional)')
        if r['status'] == 'released' and any(r[c] != 'pass' for c in crit if r[c] != 'n/a'):
            errs.append(f'toolkit.csv {m}: released with a criterion not passed')
        for f in [r['path'], r['card']] + split(r['parameters']) + split(r['results']) + split(r['tests']):
            if f and not (ROOT / f).exists():
                errs.append(f'toolkit.csv {m}: {f} does not exist')
        for c in crit:
            if r[c] not in VALUES:
                errs.append(f'toolkit.csv {m}: {c} is "{r[c]}", not one of {VALUES}')
        if r['status'] == 'none':
            continue
        computed = auto_criteria(r, runs)
        for c in sorted(auto & set(computed)):
            got, why = computed[c]
            if r[c] in ('pass', 'partial') and got == 'fail':
                errs.append(f'toolkit.csv {m}: {c} recorded "{r[c]}" but the check finds fail ({why})')
            elif r[c] == 'fail' and got == 'pass':
                warns.append(f'toolkit.csv {m}: {c} recorded fail but the check finds pass ({why}); update the register')
    return rows


def check_runs(errs, models, base=None, warns=None):
    if not RUNS.exists():
        errs.append('models/runs.csv is missing')
        return []
    text = RUNS.read_text(encoding='utf-8')
    if text.splitlines()[0] != ','.join(RUN_COLUMNS):
        errs.append(f'runs.csv header must be {",".join(RUN_COLUMNS)}')
        return []
    runs = read_csv(RUNS)
    seen = set()
    for r in runs:
        rid = r['run_id']
        m = RUN_RE.match(rid)
        if not m:
            errs.append(f'runs.csv: "{rid}" is not RUN-<model>-<YYYY-MM-DD>-<letter>')
            continue
        if rid in seen:
            errs.append(f'runs.csv: {rid} appears twice')
        seen.add(rid)
        if 'MOD-' + m.group(1) != r['model_id'] or m.group(2) != r['date']:
            errs.append(f'runs.csv {rid}: the ID does not match its model ID and date')
        if r['model_id'] not in models:
            errs.append(f'runs.csv {rid}: {r["model_id"]} is not in toolkit.csv')
        if not results_schema.COMMIT_RE.match(r['commit']):
            errs.append(f'runs.csv {rid}: commit must be a 40-character hash')
        if not results_schema.SHA_RE.match(r['results_sha256']) or not results_schema.SHA_RE.match(r['inputs_sha256']):
            errs.append(f'runs.csv {rid}: results_sha256 and inputs_sha256 must be full sha256 hashes')
        if not results_schema.semver(r['model_version']):
            errs.append(f'runs.csv {rid}: model_version is not MAJOR.MINOR.PATCH')
        if results_schema.COMMIT_RE.match(r['commit']):
            if git('cat-file', '-e', r['commit'] + '^{commit}')[0]:
                if warns is not None:
                    warns.append(f'runs.csv {rid}: commit {r["commit"][:12]} is not in this clone (a shallow history?); ancestry not checked')
            elif git('merge-base', '--is-ancestor', r['commit'], 'HEAD')[0]:
                errs.append(f'runs.csv {rid}: commit {r["commit"][:12]} is not an ancestor of HEAD (a squash or rewrite orphaned it)')
        if r['results_path'].startswith('/') or '..' in Path(r['results_path']).parts:
            errs.append(f'runs.csv {rid}: results_path must be a path from the repository root')
    if base:
        rc, old = git('show', f'{base}:models/runs.csv')
        if not rc and not text.startswith(old):
            errs.append('runs.csv: rows already on the base were changed or removed; the run log is append-only')
    return runs


def check_headers(errs, rows):
    for r in rows:
        for f in split(r['results']):
            p = ROOT / f
            if not p.exists():
                continue
            text = p.read_text(encoding='utf-8')
            has = bool(json_header(p)) if p.suffix == '.json' else (results_schema.MD_START in text)
            if not has:
                continue
            for e in results_schema.check_file(p):
                errs.append(f'{f}: {e}')
            if p.suffix == '.json':
                h = json_header(p) or {}
                if h.get('model_id') != r['model_id']:
                    errs.append(f'{f}: header model_id {h.get("model_id")} is not {r["model_id"]}')


def git(*args):
    r = subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, text=True)
    return r.returncode, r.stdout


def base_ref(explicit):
    if explicit:
        return explicit
    rc, out = git('rev-parse', '--verify', '-q', 'origin/main')
    if rc:
        return None
    rc, mb = git('merge-base', 'HEAD', 'origin/main')
    rc2, head = git('rev-parse', 'HEAD')
    if rc or rc2:
        return None
    if mb.strip() == head.strip():
        rc, parent = git('rev-parse', '-q', '--verify', 'HEAD^1')
        return parent.strip() if not rc else None
    return mb.strip()


def strip_header(d):
    return {k: v for k, v in d.items() if k != 'header'} if isinstance(d, dict) else d


def check_versions(errs, warns, rows, base):
    for r in rows:
        res = split(r['results'])
        js = [f for f in res if f.endswith('.json') and json_header(ROOT / f)]
        if not js:
            continue
        main = js[0]
        h = json_header(ROOT / main)
        ver = h.get('model_version')
        cl = ROOT / r['path'] / 'CHANGELOG.md'
        cl_text = cl.read_text(encoding='utf-8') if cl.exists() else ''
        entries = VER_HEAD.findall(cl_text)
        for f in js[1:]:
            if (json_header(ROOT / f) or {}).get('model_version') != ver:
                errs.append(f'{r["model_id"]}: {f} carries a different version from {main}')
        sv = [results_schema.semver(v) for v in entries]
        if any(a <= b for a, b in zip(sv, sv[1:])):
            errs.append(f'{r["model_id"]}: CHANGELOG.md entries are not newest first with rising versions')
        if not entries:
            errs.append(f'{r["model_id"]}: {cl.relative_to(ROOT)} is missing or has no "## X.Y.Z" entry')
            continue
        if entries[0] != ver:
            errs.append(f'{r["model_id"]}: the newest changelog entry is {entries[0]}, the results header says {ver}')
        if base is None:
            continue
        changed = [f for f in res if git('diff', '--quiet', base, '--', f)[0] == 1]
        if not changed:
            continue
        rc, old_text = git('show', f'{base}:{main}')
        old = json.loads(old_text) if not rc else None
        old_ver = (old or {}).get('header', {}).get('model_version') if isinstance(old, dict) else None
        if old_ver is None:
            if isinstance(old, dict) and old.get('version'):
                old_ver = old['version']  # a results file from before the header (health coverage's 0.1.0)
        if old_ver is None:
            continue  # a new results file: the changelog entry above is all that is required
        nv, ov = results_schema.semver(ver), results_schema.semver(old_ver)
        if not ov or not nv or nv <= ov:
            errs.append(f'{r["model_id"]}: {", ".join(changed)} changed but the version did not go up ({old_ver} -> {ver}); '
                        f'see models/schema/README.md, "Versions"')
            continue
        if ver not in entries:
            errs.append(f'{r["model_id"]}: no CHANGELOG.md entry for {ver}')
        else:
            entry = re.split(r'^## ', cl_text.split(f'## {ver}', 1)[1], flags=re.M)[0]
            if 'Results:' not in entry:
                errs.append(f'{r["model_id"]}: the {ver} changelog entry needs a "Results:" line saying how far the headline figures moved')
        if nv[:2] == ov[:2]:
            for f in [x for x in res if x.endswith('.json')]:
                rc, t = git('show', f'{base}:{f}')
                if not rc and strip_header(json.loads(t)) != strip_header(json.loads((ROOT / f).read_text(encoding='utf-8'))):
                    errs.append(f'{r["model_id"]}: {ver} is a patch release but {f} changed outside its header; '
                                f'a results change takes a minor or major version')


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--base')
    ap.add_argument('--no-git', action='store_true')
    ap.add_argument('--require-base', action='store_true', help='fail if no base is found (for CI: fetch origin/main first)')
    a = ap.parse_args(argv)
    errs, warns = [], []
    base = None if a.no_git else base_ref(a.base)
    if a.require_base and not base:
        errs.append('no base to compare versions against: fetch origin/main (git fetch origin main) or pass --base')
    rows = check_register(errs, warns)
    check_runs(errs, {r['model_id'] for r in rows}, base, warns)
    check_headers(errs, rows)
    check_versions(errs, warns, rows, base)
    for w in warns:
        print('warning:', w)
    for e in errs:
        print('ERROR:', e)
    print(f'toolkit check: {len(rows)} models, {len(errs)} error(s), {len(warns)} warning(s)'
          + ('' if base or a.no_git else ' (no base found: version bumps not compared)') + (f' (base {base[:12]})' if base else ''))
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main())
