"""SPM-style poverty from the household model's SPM units.

Role: the household model's poverty layer (`MODEL-CARD.md`, "Poverty"). Status: working.

A person is poor when their SPM unit's resources fall below its threshold, counted with the CPS person weights
(MARSUPWT), as the Census does. Rates are for all people, children under 18, adults 18-64 and people 65 and over.
`resources` names the resource field: `resources` (the Census's SPM_RESOURCES, the source year only),
`resources_census` (Census taxes) or `resources_model` (the model's taxes), or any field a provision adds.
"""

GROUPS = {"all": "w_people", "children": "w_children", "18_64": "w_18_64", "65_plus": "w_65"}


def rates(spm, resources="resources_model", threshold="threshold", line=1.0):
    out = {}
    for name, wkey in GROUPS.items():
        tot = sum(s[wkey] for s in spm)
        poor = sum(s[wkey] for s in spm if s[resources] < line * s[threshold])
        out[name] = {"rate": 100 * poor / tot, "poor_m": poor / 1e6, "people_m": tot / 1e6}
    return out


def gap(spm, resources="resources_model", threshold="threshold"):
    """The aggregate SPM poverty gap (dollars a year): what it would take to lift every poor unit to its line."""
    return sum(s["weight"] * max(s[threshold] - s[resources], 0) for s in spm)
