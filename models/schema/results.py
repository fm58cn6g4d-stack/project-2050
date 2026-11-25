#!/usr/bin/env python3
"""The toolkit's results schema: the fixed header every results file carries, and its validator.

Role: one header for every model's results (`models/schema/README.md`, "Results files"). Status:
current (stage H step H2a). `models/runlog.py` builds and stamps the header; this file says what a
valid one is.

A JSON results file is an object with a top-level "header" object (any key order; files written
with sort_keys stay byte-stable):

  schema              "p2050-results/1"
  model_id            the register's ID (`models/toolkit.csv`), e.g. MOD-health-coverage
  model_version       semantic version, MAJOR.MINOR.PATCH (README, "Versions")
  status              exploratory, working, preview or released, as the register records it
  commit              the 40-character commit the run started from, for a recorded run; null in a
                      committed reference output (a file can't hold the hash of the commit that adds
                      it); the code and input hashes below identify that run exactly instead
  code                {path: sha256} of the model's own code files, paths from the repository root
  inputs              {path: sha256} of every input file the run read
  units               plain words: what the money and people figures are in
  price_basis         e.g. "nominal dollars", "2025 dollars"
  year_type           "fiscal", "calendar" or "fiscal and calendar (see units)"
  baseline_vintage    the baseline the run starts from, e.g. "CBO, The Budget and Economic Outlook, February 2026"
  scoring_convention  e.g. "conventional: no macroeconomic feedback"
  scenarios           the scenario or reform IDs the file holds (a list), e.g. ["baseline_2029", "restore"]
  uncertainty         plain words on what the figures' uncertainty is and how it is shown, or
                      "not quantified"
  disclaimer          exactly DISCLAIMER below

A Markdown results file opens with the block `markdown_header()` writes, which carries the same
fields and the disclaimer line.

  python3 models/schema/results.py FILE...    exit 1 if any header is missing or invalid
"""
import json, re, sys
from pathlib import Path

SCHEMA = 'p2050-results/1'
DISCLAIMER = ("Project 2050 analysis of the evidence: not an official score or a benefit determination. "
              "It never stands in for a CBO or JCT estimate or for an agency's decision on an individual case.")
FIELDS = ['schema', 'model_id', 'model_version', 'status', 'commit', 'code', 'inputs', 'units', 'price_basis',
          'year_type', 'baseline_vintage', 'scoring_convention', 'scenarios', 'uncertainty', 'disclaimer']
STATUSES = ('exploratory', 'working', 'preview', 'released')
MOD_RE = re.compile(r'^MOD-[a-z0-9]+(?:-[a-z0-9]+)*$')
SEMVER_RE = re.compile(r'^(\d+)\.(\d+)\.(\d+)$')
SHA_RE = re.compile(r'^[0-9a-f]{64}$')
COMMIT_RE = re.compile(r'^[0-9a-f]{40}$')
MD_START, MD_END = '<!-- results-header:start -->', '<!-- results-header:end -->'


def semver(v):
    m = SEMVER_RE.match(v or '')
    return tuple(int(x) for x in m.groups()) if m else None


def validate_header(h):
    """Problems with a header dict; empty means valid."""
    if not isinstance(h, dict):
        return ['no "header" object']
    errs = [f'missing field "{f}"' for f in FIELDS if f not in h]
    extra = [k for k in h if k not in FIELDS]
    errs += [f'unknown field "{k}"' for k in extra]
    if errs:
        return errs
    if h['schema'] != SCHEMA:
        errs.append(f'schema is "{h["schema"]}", not "{SCHEMA}"')
    if not MOD_RE.match(str(h['model_id'])):
        errs.append(f'model_id "{h["model_id"]}" is not a MOD- ID')
    if not semver(h['model_version']):
        errs.append(f'model_version "{h["model_version"]}" is not MAJOR.MINOR.PATCH')
    if h['status'] not in STATUSES:
        errs.append(f'status must be one of {", ".join(STATUSES)}')
    if h['commit'] is not None and not COMMIT_RE.match(str(h['commit'])):
        errs.append('commit must be a 40-character hash or null')
    for part in ('code', 'inputs'):
        if not isinstance(h[part], dict) or not h[part]:
            errs.append(f'{part} must list at least one file with its sha256')
            continue
        for p, s in h[part].items():
            if p.startswith('/') or '..' in Path(p).parts:
                errs.append(f'{part}: "{p}" must be a path from the repository root')
            if not SHA_RE.match(str(s)):
                errs.append(f'{part}: "{p}" needs a full sha256')
    if not isinstance(h['scenarios'], list) or not h['scenarios'] or not all(isinstance(x, str) and x for x in h['scenarios']):
        errs.append('scenarios must be a list of scenario or reform IDs')
    for f in ('units', 'price_basis', 'year_type', 'baseline_vintage', 'scoring_convention', 'uncertainty'):
        if not isinstance(h[f], str) or not h[f].strip():
            errs.append(f'{f} must be plain words')
    if h['disclaimer'] != DISCLAIMER:
        errs.append('disclaimer is not the standard line (models/schema/results.py DISCLAIMER)')
    return errs


def markdown_header(h):
    """The block a Markdown results file opens with."""
    files = lambda d: ', '.join(f'`{p}` `{s[:12]}`' for p, s in d.items())
    commit = f"`{h['commit']}`" if h['commit'] else 'none (a committed reference output: the hashes identify the run)'
    return '\n'.join([
        MD_START,
        f"> **{h['disclaimer']}**",
        '>',
        f"> Model `{h['model_id']}` {h['model_version']} ({h['status']}). Commit: {commit}.",
        f"> Code: {files(h['code'])}. Inputs: {files(h['inputs'])}.",
        f"> Units: {h['units']}. Prices: {h['price_basis']}. Years: {h['year_type']}. "
        f"Baseline: {h['baseline_vintage']}. Scoring: {h['scoring_convention']}.",
        f"> Scenarios: {', '.join(h['scenarios'])}. Uncertainty: {h['uncertainty']}",
        MD_END])


def check_file(path):
    """Problems with one results file (JSON or Markdown)."""
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    if p.suffix == '.json':
        try:
            d = json.loads(text)
        except json.JSONDecodeError as e:
            return [f'not JSON: {e}']
        if not isinstance(d, dict) or 'header' not in d:
            return ['no "header" object']
        return validate_header(d['header'])
    if MD_START not in text or MD_END not in text:
        return ['no results header block']
    if DISCLAIMER not in text[text.index(MD_START):text.index(MD_END)]:
        return ['the header block lacks the disclaimer line']
    return []


def main(argv=None):
    bad = 0
    for f in (argv if argv is not None else sys.argv[1:]):
        errs = check_file(f)
        for e in errs:
            print(f'{f}: {e}')
        bad += bool(errs)
        if not errs:
            print(f'{f}: header OK')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
