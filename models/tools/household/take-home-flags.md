# Take-home flags: provenance

Role: documents `take-home-flags.csv.gz`, the one data file the household model's replicate-weight intervals read from the health cost review (step H3; the model no longer imports `health_cost_review.py` or `health_financing.py`). Status: current, written 2026-11-25 on the commit that adds it.

**What the file is.** One row per tax unit of the 2029 baseline, in the order of `budget.baseline(2029)["units"]` (72,979 rows, the committed extract's units). Columns: `worker` (1 if `health_cost_review._is_worker`), `agi_nonneg` (the unit's AGI in the test's 2026 dollars is not negative: the test's bands leave negative AGI out of the "all" share), `below_200fpl`, then for each package `recommended_2.25`, `alternative_2.5` and `package_E` an `.ok` flag (what visibly leaves the unit's pay and wallet does not rise under the package) and, for the first two, `.ok_low2` (the low-2 variant). A package's pass share is the weighted share of `ok` among the units in its mask: workers with non-negative AGI (`_workers`), workers below 200% of poverty (`_workers_below_200fpl`), the same under the low-2 variant (`_workers_with_low2`), and non-workers with non-negative AGI (`_others`). `intervals.py` does this once per Census replicate weight.

**Why a file.** The flags depend on the package (its rates and lines, held fixed) and on each unit's own fields, not on the weights, so the replicate loop needs only the flags. The household model reads them as data, and the boundary between the household model and the health scripts (which move to `models/bookings/` in stage H) stays clean.

**Check.** With the model's own weights the shares equal `health_cost_review.take_home_micro`'s `all` and `below_200fpl` for the three packages to 13 digits (checked when the file was made), and a rerun of `intervals.py` on the Census archive with these flags gives the committed `intervals.json`'s `take_home` block exactly (four decimals, all 10 metrics; the `d3_net_per_household` block has since moved with the ledger).

**When to regenerate.** When the recommended health design changes (`TAKE_HOME` in `intervals.py` names the specifications), or when the extract's units change (`intervals.py` and a test check the row count). The script that made it is below; it needs the health scripts in `models/tools/` (or wherever the stage H move puts them) and writes the file into this folder.

```python
import sys, os, csv, gzip, json
ROOT = os.getcwd()   # run from the repository root
sys.path.insert(0, ROOT + '/models/tools'); sys.path.insert(0, ROOT + '/models/tools/household')
import health_cost_review as HC, health_financing as HF
ctx = HF.context()
case = HC.cost_cases(HC._g40())["design"]
fold = HC.h1b_restated(ctx)["fold_into_s_points"]
K, _, _, _, X = HF.keys()
U = X["B"]["units"]
TAKE_HOME = {"recommended_2.25": dict(R=2.25, hi=2.5, form="linear"), "alternative_2.5": dict(R=2.5, hi=2.5, form="linear")}
pkgs = {k: HC.unified_package(ctx, case, HC.unified_spec(S=5.0 + fold, **v)) for k, v in TAKE_HOME.items()}
pkgs["package_E"] = HC.health_package(ctx, case, HC.PACKAGES2["E"][2])
g, oop = HC._setup_visible(ctx)
hgrow = 1.048 ** 11 / ctx["price_2040"]; igrow = X["grow"] / ctx["price_2040"]
partb = HC.PART_B_2026 * HC.REAL_HEALTH_2040
def flags(u, o, low2):
    agi = u["t_agi"] * igrow
    fs = "joint" if u["t_fs"] == "joint" else "single"
    n = max(u["n_people"], 1)
    kind = "job" if u["n_employer_cov"] > 0 else ("own" if u["n_marketplace"] > 0 else ("medicaid" if u["n_medicaid"] > 0 else ("medicare" if u["n_medicare"] > 0 else "uninsured")))
    prem = u["premiums_paid"] * hgrow
    oo = (u["n_employer_cov"] * oop["esi"] + u["n_marketplace"] * oop["ng_sub"] + u["n_medicaid"] * oop["medicaid"] + u["n_medicare"] * oop["medicare"]
          + max(n - u["n_employer_cov"] - u["n_marketplace"] - u["n_medicaid"] - u["n_medicare"], 0) * oop["uninsured"]) + u["n_medicare"] * partb
    today, plan = HC.visible(agi, fs, n, kind, prem if kind == "job" else 0.0, oo + (prem if kind != "job" else 0.0), o, HC.fpl200(n), earn=HC.earn_unit(u) * igrow, low2=low2)
    return int(plan <= today), agi, n
names = list(pkgs)
cols = ["worker", "agi_nonneg", "below_200fpl"]
for k in names:
    cols += [f"{k}.ok", f"{k}.ok_low2"] if k != "package_E" else [f"{k}.ok"]
rows = []
for u in U:
    w = int(HC._is_worker(u))
    row = [w]
    first = True
    vals = {}
    for k in names:
        ok, agi, n = flags(u, pkgs[k], False)
        vals[k] = [ok]
        if k != "package_E":
            vals[k].append(flags(u, pkgs[k], True)[0])
    row += [int(agi >= 0), int(agi < HC.fpl200(n))]
    for k in names:
        row += vals[k]
    rows.append(row)
out = ROOT + '/models/tools/household/take-home-flags.csv.gz'
import io
buf = io.StringIO(); w = csv.writer(buf, lineterminator='\n'); w.writerow(cols); w.writerows(rows)
with gzip.GzipFile(out, 'wb', mtime=0) as f:
    f.write(buf.getvalue().encode())
```
