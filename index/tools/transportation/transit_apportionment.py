"""Section 5307(i) apportionment, run against NTD 2024 and ACS 2019-23 (data in ntd_uza_2024.py).
As drafted Oct 4: 50/30/20 with a 0.5% State floor (report_floor_version).
As redrafted Oct 12: no floor; no area above 25% of its net operating cost (report_ceiling_version).
Run: python3 transit_apportionment.py  (ntd_uza_2024.py in the same folder)"""
import sys, json, collections
sys.path.insert(0, '.')
from ntd_uza_2024 import load
R = load()
assert all(r['li'] is not None for r in R), [r['name'] for r in R if r['li'] is None]

def apportion(total, w=(0.5, 0.3, 0.2), floor=0.005, rows=R):
    T = {k: sum(r[k] for r in rows) for k in ('vrh', 'upt', 'li')}
    a = {r['uace']: total * (w[0] * r['vrh'] / T['vrh'] + w[1] * r['upt'] / T['upt'] + w[2] * r['li'] / T['li']) for r in rows}
    if floor:
        st = lambda r: r['states'].split('--')[0]      # (A) multi-state area assigned to its first-listed State
        for _ in range(50):
            bys = collections.defaultdict(float)
            for r in rows: bys[st(r)] += a[r['uace']]
            short = {s: floor * total - v for s, v in bys.items() if v < floor * total - 1e-6}
            if not short: break
            add = sum(short.values())
            donors = [r for r in rows if st(r) not in short]
            dsum = sum(a[r['uace']] for r in donors)
            for r in rows:
                s = st(r)
                if s in short: a[r['uace']] *= (floor * total) / bys[s]
                else: a[r['uace']] -= add * a[r['uace']] / dsum
    return a

def report(total=6.0e9, w=(0.5, 0.3, 0.2), label="as drafted"):
    a = apportion(total, w)
    rows = sorted(R, key=lambda r: -a[r['uace']])
    out = []
    for r in rows:
        net = r['opex'] - r['fares']
        out.append(dict(name=r['name'], states=r['states'], amt=a[r['uace']], share=a[r['uace']] / total,
                        pct_opex=a[r['uace']] / r['opex'] if r['opex'] else 0,
                        pct_net=a[r['uace']] / net if net > 0 else 0,
                        fare_loss=r['fares19'] - r['fares'], opex=r['opex']))
    return out, a

def report_floor_version():
    out, a = report()
    tot_opex = sum(r['opex'] for r in R); tot_fl = sum(max(r['fares19'] - r['fares'], 0) for r in R)
    print(f"areas {len(R)}; total 2024 opex ${tot_opex/1e9:.1f}B; fare loss 2019->2024 (nominal) ${tot_fl/1e9:.2f}B")
    print(f"{'area':38s} {'$M':>8s} {'share':>6s} {'%opex':>6s} {'%net':>6s} {'fareloss$M':>10s}")
    for o in out[:25]:
        print(f"{o['name'][:38]:38s} {o['amt']/1e6:8.0f} {o['share']:6.1%} {o['pct_opex']:6.1%} {o['pct_net']:6.1%} {o['fare_loss']/1e6:10.0f}")
    # 50% federal share check: grant cannot exceed 50% of net operating cost
    over = [o for o in out if o['pct_net'] > 0.5]
    print("areas where $6.0B allocation exceeds 50% of 2024 net operating cost:", len(over), [(o['name'][:22], round(o['pct_net'], 2)) for o in over][:15])
    sz = collections.OrderedDict([(">=5M", lambda p: p >= 5e6), ("1-5M", lambda p: 1e6 <= p < 5e6), ("200k-1M", lambda p: p < 1e6)])
    for k, f in sz.items():
        rs = [r for r in R if f(r['pop'])]
        print(f"size {k}: {len(rs)} areas, share {sum(a[r['uace']] for r in rs)/6e9:.1%}, of opex {sum(r['opex'] for r in rs)/tot_opex:.1%}, of pop {sum(r['pop'] for r in rs)/sum(r['pop'] for r in R):.1%}")
    # alternatives
    for w, lab in [((0.5, 0.3, 0.2), "50/30/20 drafted"), ((0.4, 0.4, 0.2), "40/40/20"), ((0.6, 0.2, 0.2), "60/20/20"), ((0.5, 0.2, 0.3), "50/20/30")]:
        aa = apportion(6e9, w); ny = aa['63217'] / 6e9
        top5 = sorted(aa.values(), reverse=True)[:5]
        print(f"weights {lab:18s} NY {ny:6.1%}  top-5 {sum(top5)/6e9:6.1%}  max %net {max(aa[r['uace']]/(r['opex']-r['fares']) for r in R if r['opex']>r['fares']):.2f}")
    # floor effect
    nf = apportion(6e9, floor=0)
    st = collections.defaultdict(float); stn = collections.defaultdict(float)
    for r in R: st[r['states'].split('--')[0]] += a[r['uace']]; stn[r['states'].split('--')[0]] += nf[r['uace']]
    lifted = {s: (stn[s] / 1e6, st[s] / 1e6) for s in st if st[s] > stn[s] + 1}
    print("states lifted by the 0.5% floor ($M before -> after):", {k: (round(v[0]), round(v[1])) for k, v in lifted.items()})
    print("cost of the floor $M:", round(sum(st[s] - stn[s] for s in lifted) / 1e6))
    json.dump([dict(o, amt=round(o['amt'] / 1e6, 1)) for o in out], open('apportion_fy2031.json', 'w'), indent=0)


def capped(total, cap, w=(0.5, 0.3, 0.2)):
    """Redrafted paragraph (2): no State floor; no area above `cap` x its net operating cost (opex - fares);
    the excess is reapportioned among the other areas by the same formula."""
    net = {r['uace']: max(r['opex'] - r['fares'], 0) for r in R}
    fixed = {}
    for _ in range(100):
        free = [r for r in R if r['uace'] not in fixed]
        rem = total - sum(fixed.values())
        a = apportion(rem, w, floor=0, rows=free)
        over = [u for u, v in a.items() if v > cap * net[u]]
        if not over:
            a.update(fixed)
            return a
        for u in over:
            fixed[u] = cap * net[u]

def report_ceiling_version(total=6e9, cap=0.25):
    a = capped(total, cap)
    tot_net = sum(r['opex'] - r['fares'] for r in R)
    print(f"Ceiling version: ${total/1e9:.1f}B, cap {cap:.0%} of net operating cost; tier = {total/tot_net:.1%} of national net cost")
    for r in sorted(R, key=lambda r: -a[r['uace']])[:15]:
        net = r['opex'] - r['fares']
        print(f"  {r['name'][:34]:34s} ${a[r['uace']]/1e6:6.0f}M  {a[r['uace']]/total:5.1%} of tier  {net/tot_net:5.1%} of national net  {a[r['uace']]/net:5.1%} of own net")
    n_cap = sum(1 for r in R if abs(a[r['uace']] - cap * max(r['opex'] - r['fares'], 0)) < 1e3)
    print(f"  areas at the ceiling: {n_cap} of {len(R)}")

if __name__ == "__main__":
    report_floor_version()
    print()
    report_ceiling_version()
