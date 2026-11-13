"""P.L. 119-21's SNAP changes in the household model's baseline (assumption A-8).

Role: the household model's application of the 2025 reconciliation law's nutrition subtitle to the CPS's reported
SNAP (`MODEL-CARD.md`, A-8). Status: working. The CPS's income year, 2025, is almost all before the law took effect, so
its SNAP is prior law; from 2026 this module applies the law, each section as CBO estimated it (EV-SEC-034 to 038):

  * sec. 10102, the work rule: the three-month time limit now reaches ages 55-64 and parents whose youngest child is
    14 or older, and the exemptions for veterans, people experiencing homelessness and former foster youth end, with
    fewer waivers. CBO: about 2.4 million fewer participants in an average month, of whom 800,000 are able-bodied
    adults 55-64 without dependents and 300,000 adults whose youngest child is 14 or older (EV-SEC-036). The CPS
    pools (adults not disabled who worked under 20 hours a week last year, counted in `extract.py`) are larger than
    CBO's counts, so each pool loses benefits with the probability that reproduces CBO's count as a share of
    participants (USDA's FY2025 average, 42,145,499, EV-SEC-039). The remaining 1.3 million fall on able-bodied adults
    18-54 without children, whom the time limit reached before the law (the exemptions and waivers they lose);
    *Interpretation:* CBO's 800,000 are "able-bodied adults through age 64 without dependent children" (EV-SEC-036),
    which could include some under 55 who lose waivers or exemptions; the model assigns all 800,000 to the new 55-64
    group, the reading under which the age change does the work. Moving part of them to 18-54 shifts losses between
    the two pools, not the total;
  * secs. 10103 and 10104, energy assistance and internet costs: about $100 a month less for about 3% of households,
    and about $10 a month less for about 65% (EV-SEC-038). Applied as expected values: the energy cut to SNAP units
    that get energy assistance and have no member 60 or older or disabled (6.4% of CPS SNAP units, so scaled to 3%),
    the internet cut to every SNAP unit;
  * sec. 10101, the Thrifty Food Plan: benefits follow prices only. The model already uprates SNAP with prices, so
    nothing more is applied;
  * not applied: sec. 10105's state cost share works through states' own choices (CBO: about 300,000 people), and
    sec. 10108's noncitizen rule (about 90,000 people) needs immigration status the CPS does not record. Both are
    behavior or data the model does not have (`MODEL-CARD.md`, limits).

Participation is running below CBO's path: USDA's preliminary FY2026 average is 38.0 million people, against 42.1
million in FY2025 (EV-SEC-039), a fall of about 4.1 million against CBO's expected effect of about 3 million in 2026
(EV-SEC-040). The model calibrates to CBO's counts, not to USDA's lower 2026 level, so if the gap persists the law's
effect is understated.

A person who loses benefits takes their per-person share of the unit's SNAP with them (the benefit falls with
household size; a per-person share is the simple approximation).
"""

USDA_PARTICIPANTS_FY2025 = 42_145_499      # EV-SEC-039
CBO_FEWER = {"n_abawd_55_64": 800_000,      # EV-SEC-036
             "n_parent_child14": 300_000,
             "n_abawd_prior": 2_400_000 - 800_000 - 300_000}
ENERGY_CUT_MONTHLY, ENERGY_SHARE = 100, 0.03      # EV-SEC-038
INTERNET_CUT_MONTHLY, INTERNET_SHARE = 10, 0.65   # EV-SEC-038
FIRST_YEAR = 2026


def calibrate(spm):
    """Probability that an at-risk adult in each pool loses benefits, so the pool's share of CPS SNAP participants
    matches CBO's count over USDA's participants; and the energy cut's scaling."""
    snap_units = [s for s in spm if s["snap"] > 0]
    people = sum(s["w_people"] for s in snap_units)
    p = {}
    for pool, fewer in CBO_FEWER.items():
        at_risk = sum(s["weight"] * s[pool] for s in snap_units)
        p[pool] = min(fewer / USDA_PARTICIPANTS_FY2025 * people / at_risk, 1.0) if at_risk else 0.0
    units = sum(s["weight"] for s in snap_units)
    energy_units = sum(s["weight"] for s in snap_units if s["energy"] > 0 and not s["elderly_or_disabled"])
    p["energy"] = min(ENERGY_SHARE * units / energy_units, 1.0) if energy_units else 0.0
    return p


def apply(spm, year):
    """Lowers each SPM unit's SNAP for the law in `year`; keeps the prior-law amount in `snap_prior_law`. Returns a
    summary for the results."""
    for s in spm:
        s["snap_prior_law"] = s["snap"]
    if year < FIRST_YEAR:
        return {"applied": False}
    p = calibrate(spm)
    lost_people = 0.0
    for s in spm:
        if s["snap"] <= 0:
            continue
        per_person = s["snap"] / max(s["numper"], 1)
        removed = sum(p[pool] * s[pool] for pool in CBO_FEWER)
        lost_people += s["weight"] * removed
        cut = per_person * removed
        if s["energy"] > 0 and not s["elderly_or_disabled"]:
            cut += p["energy"] * 12 * ENERGY_CUT_MONTHLY
        cut += INTERNET_SHARE * 12 * INTERNET_CUT_MONTHLY
        s["snap"] = max(s["snap"] - cut, 0.0)
    before = sum(s["weight"] * s["snap_prior_law"] for s in spm)
    after = sum(s["weight"] * s["snap"] for s in spm)
    return {"applied": True, "probabilities": {k: round(v, 3) for k, v in p.items()},
            "snap_prior_law_bn": round(before / 1e9, 1), "snap_bn": round(after / 1e9, 1),
            "cut_pct": round(100 * (1 - after / before), 1), "people_losing_m": round(lost_people / 1e6, 2)}
