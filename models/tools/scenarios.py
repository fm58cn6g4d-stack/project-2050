"""scenarios.py: the shared scenario file (models/data/inputs/scenarios.json), read by the fiscal model
(SCENARIOS) and the incidence model (SCEN), so the decided package and every variant of it have one home
(budget workflow B6). Standard library only; run-all.sh copies it into build/ with the other scripts."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))


def path():
    for d in (os.environ.get("P2050_INPUTS"), os.path.join(HERE, "..", "data", "inputs"), os.path.join(HERE, "..", "models", "data", "inputs")):
        if d and os.path.exists(os.path.join(d, "scenarios.json")):
            return os.path.normpath(os.path.join(d, "scenarios.json"))
    raise FileNotFoundError("models/data/inputs/scenarios.json")


def load():
    with open(path(), encoding="utf-8") as f:
        return json.load(f)


def expand(names, packages, seen=()):
    """Package names and option IDs -> option IDs, in order; packages may name packages."""
    out = []
    for n in names:
        if n in packages:
            if n in seen:
                raise ValueError("scenarios.json: package %s includes itself" % n)
            out += expand(packages[n]["options"], packages, seen + (n,))
        else:
            out.append(n)
    if len(set(out)) != len(out):
        raise ValueError("scenarios.json: an option appears twice in %s" % names)
    return out


def package(name, doc=None):
    doc = doc or load()
    return expand([name], doc["packages"])


def options(sc, doc):
    """A scenario's option list (None for the current-law baseline), with remove and replace applied."""
    if sc["options"] is None:
        return None
    o = [x for x in expand(sc["options"], doc["packages"]) if x not in sc.get("remove", [])]
    rep = sc.get("replace", {})
    return [rep.get(x, x) for x in o]


def fiscal(doc=None):
    """[(id, label, options or None, settings)] in the fiscal model's SCENARIOS form."""
    doc = doc or load()
    return [(s["id"], s["label"], options(s, doc), dict(s.get("settings", {}))) for s in doc["fiscal"]]


def incidence(doc=None):
    """{label: (options, drop)} in the incidence model's SCEN form."""
    doc = doc or load()
    return {s["label"]: (options(s, doc), tuple(s.get("drop", ()))) for s in doc["incidence"]}
