#!/usr/bin/env python3
"""The run-log helper: stamps the results header into a model's output and records published runs in `models/runs.csv`.

Role: the toolkit's run log (`charter/PLAN.md` 3.4, "a run log"; `models/schema/README.md`). Status:
current (stage H step H2a). Standard library only.

A model calls it in two places:

    import runlog
    h = runlog.header('MOD-health-coverage', VERSION, 'exploratory',
                      code=[__file__], inputs=['inputs.csv', 'scenarios.csv'], base=HERE,
                      units='...', price_basis='nominal dollars', year_type='calendar',
                      baseline_vintage='CBO, February 2026', scoring_convention='conventional',
                      scenarios=[...], uncertainty='...',
                      commit=runlog.commit_for(paths) if args.record else None)
    out = runlog.stamp(results, h)                       # header added, validated
    runlog.write_json(path, out)                         # the one serialization
    if args.record: runlog.record(results_path, command)   # appends a RUN- row

Two kinds of run:
- **Reference runs** (`run-all.sh`, the drift check, a model's tests): commit is null and nothing is
  appended, so a rerun reproduces the committed output byte for byte.
- A recorded row's `results_sha256` is the hash of the results with commit null, which is the committed
  reference output when the run is the one committed: anyone can check it with `git show <commit>:<path>`.
- **Recorded runs** (a figure about to be quoted in a dossier, a booking, a release): `--record`
  stamps the commit the run started from and appends one `RUN-` row to `models/runs.csv`. It refuses
  if the model's code or inputs differ from that commit, so the row always names code that exists.

    python3 models/runlog.py record RESULTS.json --command "python3 ... --record" [--note TEXT]
    python3 models/runlog.py check RESULTS...     # validate headers (models/schema/results.py)
"""
import argparse, csv, datetime, hashlib, io, json, platform, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / 'models' / 'runs.csv'
sys.path.insert(0, str(ROOT / 'models' / 'schema'))
import results as schema  # noqa: E402

COLUMNS = ['run_id', 'date', 'model_id', 'model_version', 'commit', 'python', 'command', 'results_path', 'results_sha256',
           'inputs_sha256', 'note']
FRAME = ('models/runlog.py', 'models/schema/')   # the frame stamps results; it never changes a figure, so it is not hashed
RUN_RE = re.compile(r'^RUN-([a-z0-9]+(?:-[a-z0-9]+)*)-(\d{4}-\d{2}-\d{2})-([a-z])$')


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def rel(path, base=None):
    p = Path(path)
    if not p.is_absolute():
        p = Path(base or ROOT) / p
    p = p.resolve()
    try:
        return p.relative_to(ROOT).as_posix()
    except ValueError:
        raise ValueError(f'{p} is outside the repository; a run log names repository files only')


def hashes(paths, base=None):
    return {rel(p, base): sha256_file(ROOT / rel(p, base)) for p in paths}


def git(*args):
    r = subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f'git {" ".join(args)}: {r.stderr.strip()}')
    return r.stdout.strip()


def commit_for(paths, base=None):
    """HEAD's hash, if none of these files differs from HEAD; otherwise an error naming them."""
    files = [rel(p, base) for p in paths]
    dirty = git('status', '--porcelain', '--', *files)
    if dirty:
        raise RuntimeError('a recorded run needs committed code and inputs; these differ from HEAD:\n' + dirty)
    return git('rev-parse', 'HEAD')


def unlisted_imports(code):
    """Repository modules loaded in this process that the code list leaves out (tests and the frame excepted)."""
    listed = set(code)
    out = []
    for name, m in list(sys.modules.items()):
        f = getattr(m, '__file__', None)
        if not f or name == '__main__':
            continue
        try:
            r = Path(f).resolve().relative_to(ROOT).as_posix()
        except ValueError:
            continue
        if r.startswith(FRAME) or Path(r).name.startswith('test_') or r in listed:
            continue
        out.append(r)
    return sorted(out)


def header(model_id, version, status, code, inputs, units, price_basis, year_type, baseline_vintage,
           scoring_convention, scenarios, uncertainty, commit=None, base=None, check_imports=True):
    """The results header. `code` lists every repository file the run executes; an imported repository
    module missing from it is an error, so the hashes cover all the code that made the figures."""
    code_h = hashes(code, base)
    if check_imports:
        missing = unlisted_imports(code_h)
        if missing:
            raise ValueError('results header: these imported repository modules are not in code: ' + ', '.join(missing))
    h = {'schema': schema.SCHEMA, 'model_id': model_id, 'model_version': version, 'status': status, 'commit': commit,
         'code': code_h, 'inputs': hashes(inputs, base), 'units': units, 'price_basis': price_basis,
         'year_type': year_type, 'baseline_vintage': baseline_vintage, 'scoring_convention': scoring_convention,
         'scenarios': list(scenarios), 'uncertainty': uncertainty, 'disclaimer': schema.DISCLAIMER}
    errs = schema.validate_header(h)
    if errs:
        raise ValueError('results header: ' + '; '.join(errs))
    return h


def stamp(results, h):
    """A copy of the results with the header as its first key (any old header replaced)."""
    errs = schema.validate_header(h)
    if errs:
        raise ValueError('results header: ' + '; '.join(errs))
    out = {'header': h}
    out.update({k: v for k, v in results.items() if k != 'header'})
    return out


def dumps(results):
    """The one serialization of a JSON results file, so a recorded run's hash can be checked against the
    committed reference output (`git show <commit>:<path>`)."""
    return json.dumps(results, indent=1, sort_keys=True) + '\n'


def write_json(path, results):
    Path(path).write_text(dumps(results), encoding='utf-8')


def reference_sha256(results):
    """The sha256 of the results as a reference output: the same file with commit null."""
    d = dict(results)
    d['header'] = dict(d['header'], commit=None)
    return hashlib.sha256(dumps(d).encode('utf-8')).hexdigest()


def read_runs(path=RUNS):
    if not Path(path).exists():
        return []
    return list(csv.DictReader(io.StringIO(Path(path).read_text(encoding='utf-8'))))


def next_run_id(model_id, date, rows):
    slug = model_id[len('MOD-'):]
    used = {r['run_id'] for r in rows}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        rid = f'RUN-{slug}-{date}-{letter}'
        if rid not in used:
            return rid
    raise RuntimeError(f'more than 26 recorded runs of {model_id} on {date}')


def inputs_digest(h):
    """One hash for the whole input set, so a row stays short."""
    return hashlib.sha256(json.dumps(h['inputs'], sort_keys=True).encode()).hexdigest()


def record(results_path, command, note='', runs=RUNS, date=None):
    """Append a RUN- row for a results file stamped with a commit; return its run ID."""
    p = Path(results_path)
    d = json.loads(p.read_text(encoding='utf-8'))
    h = d.get('header')
    errs = schema.validate_header(h)
    if errs:
        raise ValueError(f'{p}: ' + '; '.join(errs))
    if not h['commit']:
        raise ValueError(f'{p}: a reference output (commit null) is not recorded; rerun with --record')
    for f, s in {**h['code'], **h['inputs']}.items():
        if git('rev-parse', f'{h["commit"]}:{f}') != git('hash-object', str(ROOT / f)) or sha256_file(ROOT / f) != s:
            raise ValueError(f'{p}: {f} differs from the commit or the header; rerun the model')
    date = date or datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    rows = read_runs(runs)
    rid = next_run_id(h['model_id'], date, rows)
    where = rel(p)   # refuses a file outside the repository
    if dumps(d) != p.read_text(encoding='utf-8'):
        raise ValueError(f'{p}: not written by runlog.write_json, so its hash could not be checked against a reference output')
    row = {'run_id': rid, 'date': date, 'model_id': h['model_id'], 'model_version': h['model_version'],
           'commit': h['commit'], 'python': platform.python_version(), 'command': command, 'results_path': where,
           'results_sha256': reference_sha256(d), 'inputs_sha256': inputs_digest(h), 'note': note}
    new = not Path(runs).exists() or not Path(runs).read_text(encoding='utf-8').strip()
    with open(runs, 'a', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator='\n')
        if new:
            w.writeheader()
        w.writerow(row)
    return rid


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    r = sub.add_parser('record')
    r.add_argument('results')
    r.add_argument('--command', required=True)
    r.add_argument('--note', default='')
    c = sub.add_parser('check')
    c.add_argument('files', nargs='+')
    a = ap.parse_args(argv)
    if a.cmd == 'check':
        return schema.main(a.files)
    print(record(a.results, a.command, a.note))
    return 0


if __name__ == '__main__':
    sys.exit(main())
