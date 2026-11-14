"""One-off design runs on the energy model (MOD-energy), for testing clean power designs without committing results.

Role: the "menu" interface of `models/tools/energy/` (ranked capability 3): start from the decided set (or any committed case),
change the price path, what the price covers, the standby builder, the clean standard's payment cap or the retrofit option, and
compare the run with its base. Status: working. Figures it prints are one-off runs, not results of record: quote a run only once
it is a named case in `model.py` and `results.json`.

Examples (from the repository root):
  python3 models/tools/energy/menu.py --price scale:1.5
  python3 models/tools/energy/menu.py --price linear:2030:50:5 --sector buildings=1,nonroad=1,industry=1
  python3 models/tools/energy/menu.py --builder 0.75 --acp 20
  python3 models/tools/energy/menu.py --base opt_1a --methane off --json
"""
import argparse
import copy
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as m  # noqa: E402

YEARS = (2030, 2035, 2040, 2050)


def price_path(spec, base):
    """decided | none | scale:X (the base path times X) | linear:YEAR:START:GROWTH (2025 $/t from YEAR, +GROWTH% a year)."""
    if spec in (None, "decided"):
        return base
    if spec == "none":
        return None
    kind, _, rest = spec.partition(":")
    if kind == "scale":
        x = float(rest)
        return {y: v * x for y, v in (base or m.PRICE).items()}
    if kind == "linear":
        y0, p0, g = rest.split(":")
        return {y: (float(p0) * (1 + float(g) / 100) ** (y - int(y0)) if y >= int(y0) else 0.0) for y in m.YRS}
    raise SystemExit(f"unknown price path: {spec}")


def build(args):
    """The base case from model.config(), changed as asked. Returns (base case, changed case) as engine case dicts."""
    cfg = m.config()
    base = next((c for c in cfg["cases"] if c["id"] == args.base), None)
    if base is None:
        raise SystemExit(f"no case {args.base}; see model.py")
    base = copy.deepcopy(base)
    for k in ("mc", "households"):
        base.pop(k, None)
    case = copy.deepcopy(base)
    case["id"], pol, world = "menu", case["policy"], case.setdefault("world", {})
    case["price"] = price_path(args.price, base["price"])
    if args.sector:
        sp = dict(pol.get("sectorPrice") or m.MEMO1B)
        for kv in args.sector.split(","):
            k, v = kv.split("=")
            if k not in ("buildings", "industry", "nonroad"):
                raise SystemExit(f"--sector takes buildings, industry or nonroad, not {k}")
            if not 0 <= float(v) <= 1:
                raise SystemExit(f"--sector {k} takes 0 to 1")
            sp[k] = float(v)
        pol["sectorPrice"] = sp
    for flag, key in (("border", "border"), ("process", "process")):
        v = getattr(args, flag)
        if v:
            pol["cover"] = dict(pol.get("cover") or m.COVER_NONE, **{key: v == "on"})
    if args.methane:
        pol["methaneFee"] = m.METHANE_FEE if args.methane == "on" else None
    if args.builder is not None:
        k = args.builder
        pol["grid"] = k > 0
        if not 0 <= k <= 1:
            raise SystemExit("--builder takes 0 to 1")
        world.update(m.grid_world(k))
    if args.acp is not None:
        world["cesAcp"] = args.acp
    if args.retro is not None:
        world["retro"] = m.retro(args.retro)
    if args.stack:
        world["q45Stack"] = True
    return cfg, base, case


def summary(rows):
    acc, E = m.accounts(rows), {r["year"]: r for r in rows}
    return dict(
        co2_below_2005={y: round(100 * E[y]["below2005"], 1) for y in YEARS},
        ghg_below_2005={y: round(100 * E[y]["ghgBelow2005"], 1) for y in YEARS},
        clean_share_2040=round(100 * E[2040]["cleanShare"], 1),
        retail_2040=round(E[2040]["retail"], 2),
        energy_co2_2030_50_mt=round(sum(E[y]["energy"] for y in range(2030, 2051))),
        fy2030_39_bn={k: round(m.window(acc, k)) for k in ("c1", "c1p", "c2", "c3", "acp", "credits", "dividend")})


def main(argv=None, show=True):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default="decided", help="committed case to start from (default: decided)")
    ap.add_argument("--price", help="decided | none | scale:X | linear:YEAR:START:GROWTH (2025 dollars)")
    ap.add_argument("--sector", help="share of the price each sector's fuel pays, e.g. buildings=1,nonroad=1,industry=1")
    ap.add_argument("--border", choices=("on", "off"))
    ap.add_argument("--process", choices=("on", "off"), help="price industrial process CO2 and N2O")
    ap.add_argument("--methane", choices=("on", "off"), help="the methane fee")
    ap.add_argument("--builder", type=float, help="standby builder strength, 0-1 of the full grid program (decided 0.5)")
    ap.add_argument("--acp", type=float, help="clean standard's payment cap, 2025 $/MWh (decided 40)")
    ap.add_argument("--retro", type=float, help="carbon-capture retrofit scale (0 off, 1 research limits, 2 double)")
    ap.add_argument("--stack", action="store_true", help="45Q stacks on the carbon price avoided")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    cfg, base, case = build(args)
    cfg["cases"] = [base, case]
    out = m.run_engine(cfg)["cases"]
    res = {"base": args.base, "run": summary(out["menu"]), "base_run": summary(out[base["id"]]), "note": "one-off run, not a result of record"}
    if args.json or not show:
        if show:
            print(json.dumps(res, indent=1))
        return res
    b, r = res["base_run"], res["run"]
    print(f"One-off run against '{args.base}' (not a result of record):")
    print(f"{'':42}{'base':>10}{'run':>10}")
    for y in YEARS:
        print(f"{'energy CO2 below 2005, ' + str(y) + ' %':42}{b['co2_below_2005'][y]:>10}{r['co2_below_2005'][y]:>10}")
    for y in (2035, 2050):
        print(f"{'net GHG below 2005, ' + str(y) + ' %':42}{b['ghg_below_2005'][y]:>10}{r['ghg_below_2005'][y]:>10}")
    print(f"{'energy CO2 2030-50, Mt':42}{b['energy_co2_2030_50_mt']:>10,}{r['energy_co2_2030_50_mt']:>10,}")
    print(f"{'clean share 2040, %':42}{b['clean_share_2040']:>10}{r['clean_share_2040']:>10}")
    print(f"{'retail price 2040, 2025 c/kWh':42}{b['retail_2040']:>10}{r['retail_2040']:>10}")
    for k, lab in (("c1", "carbon price receipts"), ("c1p", "process receipts"), ("c2", "border adjustment"), ("c3", "methane fee"),
                   ("acp", "standard's payments"), ("credits", "credits (engine estimate)"), ("dividend", "Climate Dividend")):
        print(f"{lab + ', FY2030-39 $bn':42}{b['fy2030_39_bn'][k]:>10,}{r['fy2030_39_bn'][k]:>10,}")
    return res


if __name__ == "__main__":
    main()
