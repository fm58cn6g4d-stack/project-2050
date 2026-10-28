"""Claim-tracing rules shared by the registry checker and the public story builder.

A figure must appear, digit for digit, in at least one anchor passage of the source it cites. A rounded
figure must follow from an anchored raw value by its stated scale and places. These are the rules the
story builder proved on the essays (PR #39), lifted out so evidence registers use the same ones.
"""
import re

NUMBER = re.compile(r'\d+(?:[.,]\d+)*')


def numbers(text):
    return set(NUMBER.findall(text))


def line_of(text, anchor):
    """1-based line of an exact anchor passage in text, or None."""
    at = text.find(anchor)
    return None if at < 0 else text.count('\n', 0, at) + 1


def figure_problems(anchors, figures=(), rounded=(), series=(), free=frozenset()):
    """Problems with a claim's figures against its anchor passages (empty when every figure traces).

    rounded: [{"figure": "0.9%", "value": "0.00873", "scale": 100, "places": 1}] - a displayed figure
    rounded from an anchored raw value. series: [(year, value)] - chart points that must be anchored.
    """
    problems = []
    anchored = set().union(*(numbers(a) for a in anchors)) if anchors else set()
    for r in rounded:
        shown = f'{float(r["value"]) * r["scale"]:.{r["places"]}f}'
        if r['value'] not in anchored or numbers(r['figure']) != {shown}:
            problems.append(f'rounded figure {r["figure"]!r} does not follow from {r["value"]}')
        else:
            anchored = anchored | {shown}
    for fig in figures:
        if not numbers(fig) <= anchored | set(free):
            problems.append(f'figure {fig!r} not in its anchors')
    for year, value in series:
        if not {str(year), f'{value:,}'} <= anchored:
            problems.append(f'series point {year}={value} not in its anchors')
    return problems
