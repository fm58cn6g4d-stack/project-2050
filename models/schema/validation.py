#!/usr/bin/env python3
"""The toolkit's validation-table convention: benchmarks defined in test code, judged by one rule, rendered as one table.

Role: how every model compares itself with official and independent estimates (`models/schema/README.md`,
"Validation tables"). Status: current (stage H step H2a).

A model's test file defines its benchmarks as `Benchmark` records, with the target, its source and
vintage, and the tolerance fixed in the code before the model figure is filled in. `evaluate()` works
out the difference and the pass or miss, so neither is typed by hand; `render()` writes the table;
`problems()` lists what makes a table unacceptable (a miss or an in-sample check without an
explanation, a target without a source). A miss is a result to report, not a test failure: the test
fails only on `problems()` or when the committed table no longer matches the one the code renders.

    from validation import Benchmark, evaluate, render, problems
    rows = [evaluate(Benchmark('BM-1', 'Uninsured, 2032', target=37.2, source='EV-CAR-051',
                               vintage='CBO, February 2026', unit='million people',
                               tolerance=0.05, tolerance_kind='relative'), model=37.2)]
"""
from dataclasses import dataclass, replace

KINDS = ('relative', 'absolute', 'range')


@dataclass(frozen=True)
class Benchmark:
    id: str
    quantity: str
    target: object          # a number, or (low, high) for a published range
    source: str             # evidence ID(s), e.g. 'EV-CAR-051' or 'SRC-3000; EV-CAR-052'
    vintage: str            # whose estimate and when, e.g. 'CBO, February 2026 baseline'
    unit: str
    tolerance: float = 0.0  # relative: share of the target (0.25 = 25%); absolute: in `unit`; range: slack beyond the ends, in `unit`
    tolerance_kind: str = 'relative'
    tolerance_basis: str = ''  # why this tolerance: the target's own precision, a published error band, a convention
    in_sample: bool = False  # the model was calibrated to this target: it checks arithmetic, not accuracy
    explanation: str = ''    # required for a miss or an in-sample row
    model: float = None
    difference: float = None
    difference_pct: float = None   # difference as a share of the target (of the nearer end for a range)
    passed: bool = None


def evaluate(b, model):
    """The benchmark with the model figure, the difference and the pass or miss filled in."""
    if b.tolerance_kind not in KINDS:
        raise ValueError(f'{b.id}: tolerance_kind must be one of {KINDS}')
    if b.tolerance < 0:
        raise ValueError(f'{b.id}: tolerance must not be negative')
    if isinstance(b.target, (tuple, list)):
        lo, hi = b.target
        if lo > hi:
            raise ValueError(f'{b.id}: target range runs backward')
        diff = 0.0 if lo <= model <= hi else (model - hi if model > hi else model - lo)
        end = hi if model > hi else lo
        if b.tolerance_kind == 'relative' and end == 0:
            raise ValueError(f'{b.id}: a relative tolerance needs a nonzero target; use an absolute one')
        ok = abs(diff) <= (b.tolerance * abs(end) if b.tolerance_kind == 'relative' else b.tolerance)
    else:
        if b.tolerance_kind == 'range':
            raise ValueError(f'{b.id}: a range tolerance needs a (low, high) target')
        end = b.target
        if b.tolerance_kind == 'relative' and end == 0:
            raise ValueError(f'{b.id}: a relative tolerance needs a nonzero target; use an absolute one')
        diff = model - b.target
        ok = abs(diff) <= (b.tolerance * abs(b.target) if b.tolerance_kind == 'relative' else b.tolerance)
    pct = diff / abs(end) if end else None
    return replace(b, model=model, difference=diff, difference_pct=pct, passed=bool(ok))


def problems(rows):
    out = []
    ids = [r.id for r in rows]
    out += [f'{i}: duplicate benchmark ID' for i in sorted({i for i in ids if ids.count(i) > 1})]
    for r in rows:
        if r.passed is None:
            out.append(f'{r.id}: not evaluated')
        if not r.source.strip() or not r.vintage.strip():
            out.append(f'{r.id}: a target needs its source and vintage')
        if not r.tolerance_basis.strip():
            out.append(f'{r.id}: a tolerance needs its basis (why this band, set before the model figure)')
        if (r.passed is False or r.in_sample) and not r.explanation.strip():
            out.append(f'{r.id}: {"a miss" if r.passed is False else "an in-sample check"} needs an explanation')
    return out


def fmt(x):
    if isinstance(x, (tuple, list)):
        return f'{fmt(x[0])} to {fmt(x[1])}'
    a = abs(x)
    return f'{x:,.0f}' if a >= 100 else f'{x:,.1f}' if a >= 10 else f'{x:,.2f}' if a >= 0.1 else f'{x:,.3f}'


def tol_text(r):
    if r.tolerance_kind == 'relative':
        return f'{r.tolerance:.0%}' + (' of the nearer end' if isinstance(r.target, (tuple, list)) else '')
    if r.tolerance_kind == 'range':
        return 'inside the range' + (f' or within {fmt(r.tolerance)}' if r.tolerance else '')
    return f'{fmt(r.tolerance)} {r.unit}'


def render(rows, title='Validation'):
    """The validation table in Markdown, with a one-line count."""
    ind = [r for r in rows if not r.in_sample]
    n_pass = sum(r.passed for r in ind)
    n_in = len(rows) - len(ind)
    head = f'{len(rows)} benchmarks. {len(ind)} independent: {n_pass} pass, {len(ind) - n_pass} miss.'
    if n_in:
        head += f' {n_in} in-sample by construction (they check arithmetic, not accuracy): {sum(r.passed for r in rows if r.in_sample)} pass.'
    L = [head, '', '| ID | Quantity | Target | Source and vintage | Model | Difference | Tolerance (set in advance) | Result | Explanation |',
         '| --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for r in rows:
        res = 'pass' if r.passed else '**miss**'
        if r.in_sample:
            res += ' (in-sample)'
        d = fmt(r.difference) + (f' ({r.difference_pct:+.1%})' if r.difference_pct is not None else '')
        L.append(f'| {r.id} | {r.quantity} | {fmt(r.target)} {r.unit} | {r.source}; {r.vintage} | {fmt(r.model)} | '
                 f'{d} | {tol_text(r)}; {r.tolerance_basis} | {res} | {r.explanation} |')
    return '\n'.join(L)
