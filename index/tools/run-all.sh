#!/usr/bin/env bash
# Regenerate every generated file in index/ from the scripts in index/tools/.
# Usage (from the repo root):   bash index/tools/run-all.sh          # rebuild, show a diff, do not overwrite
#                               bash index/tools/run-all.sh --write  # rebuild and copy outputs into index/
#                               bash index/tools/run-all.sh --fetch  # also re-download CBO's data first
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
TOOLS="$ROOT/index/tools"; DATA="$ROOT/index/data"; BUILD="$ROOT/build"
WRITE=0; FETCH=0
for a in "$@"; do [[ "$a" == "--write" ]] && WRITE=1; [[ "$a" == "--fetch" ]] && FETCH=1; done

rm -rf "$BUILD"; mkdir -p "$BUILD"
cp "$TOOLS"/ledger-build.py "$TOOLS"/ledger-paths.py "$TOOLS"/ledger-make-md.py "$TOOLS"/incidence-make-md.py \
   "$TOOLS"/fiscal-data.py "$TOOLS"/fiscal-profiles.py "$TOOLS"/inputs.py "$TOOLS"/fiscal-model.py "$TOOLS"/fiscal-make-md.py "$BUILD"/
# the two incidence scripts import each other under their working names
cp "$TOOLS"/incidence-model.py "$BUILD"/incidence.py
cp "$TOOLS"/incidence-years.py "$BUILD"/years.py

cd "$BUILD"
echo "== 0. transportation";    python3 "$TOOLS"/transportation/test_moving_america.py --quiet
                                python3 "$TOOLS"/transportation/report.py --json "$BUILD"/moving-america.json >/dev/null
echo "== 1. ledger";            python3 ledger-build.py >/dev/null
echo "== 2. floor paths";       python3 ledger-paths.py >/dev/null
echo "== 2a. scenario calendar"; python3 "$TOOLS/calendar/test_model.py"; python3 "$TOOLS/calendar/build.py"
echo "== 2b. vote simulation"; cp "$TOOLS"/votes-model.py "$BUILD"/; python3 votes-model.py
echo "== 2c. calendar checks"; python3 "$TOOLS"/test_calendar.py
echo "== 3. ledger markdown";   python3 ledger-make-md.py >/dev/null
echo "== 4. incidence";         python3 incidence.py >/dev/null; python3 years.py >/dev/null; python3 incidence-make-md.py >/dev/null
if [[ $FETCH == 1 ]]; then
  echo "== 5a. fetch CBO data";  python3 fiscal-data.py --fetch --cache "$DATA/cbo" --out "$BUILD/fiscal-baseline.csv"
else
  echo "== 5. fiscal baseline";  python3 fiscal-data.py --cache "$DATA/cbo" --out "$BUILD/fiscal-baseline.csv"
fi
echo "== 6. fiscal model";      python3 fiscal-model.py --baseline "$BUILD/fiscal-baseline.csv" > fiscal-model.log; head -1 fiscal-model.log
python3 fiscal-make-md.py --baseline "$BUILD/fiscal-baseline.csv" >/dev/null
echo "== 6b. carbon model";    (cd "$TOOLS"/carbon && node cfd-tests.js >/dev/null) || { echo "carbon model checks failed: run node index/tools/carbon/cfd-tests.js"; exit 1; }
                                cp "$TOOLS"/carbon-model.py "$BUILD"/; python3 carbon-model.py
echo "== 6c. dedicated funds";  cp "$TOOLS"/funds-model.py "$BUILD"/; python3 funds-model.py
echo "== 6d. surge funding";  python3 "$TOOLS"/test_capacity_funding.py
                               cp "$TOOLS"/capacity-funding.py "$BUILD"/; python3 capacity-funding.py
echo "== 7. dashboard data";   python3 "$TOOLS"/dashboard-data.py >/dev/null
echo "== 8. consistency check"; cp "$TOOLS"/check-project.py "$TOOLS"/window.py "$BUILD"/; python3 check-project.py

OUT=(
  'calendar-scenarios.md|index/calendar-scenarios.md'
  'calendar-delivery-opportunities.md|index/calendar-delivery-opportunities.md'
  'calendar-scenario-explorer.html|index/calendar-scenario-explorer.html'
  'calendar-scenarios.json|index/data/calendar-scenarios.json'
  'calendar-delivery.json|index/data/calendar-delivery.json'
  'dashboard/calendar.json|index/data/dashboard/calendar.json'
  'capacity-funding-model.md|index/capacity-funding-model.md'
  '2029-trifecta-master-ledger-v2.md|index/2029-trifecta-master-ledger.md'
  'revenue-household-incidence-model.md|index/revenue-household-incidence-model.md'
  'fiscal-long-term-model.md|index/fiscal-long-term-model.md'
  'fiscal-baseline.csv|index/data/fiscal-baseline.csv'
  'fiscal-paths.csv|index/data/fiscal-paths.csv'
  'check-report.md|index/check-report.md'
  'vote-simulation.md|index/vote-simulation.md'
  'dedicated-funds.md|index/dedicated-funds.md'
  'climate-carbon-model.md|index/climate-carbon-model.md'
  'dashboard/bills.json|index/data/dashboard/bills.json'
  'dashboard/revenue.json|index/data/dashboard/revenue.json'
  'dashboard/cuts.json|index/data/dashboard/cuts.json'
  'dashboard/conflicts.json|index/data/dashboard/conflicts.json'
  'dashboard/paths.json|index/data/dashboard/paths.json'
)
echo; echo "== changes against the committed files"
for pair in "${OUT[@]}"; do
  f="${pair%%|*}"; dest="${pair#*|}"
  if diff -q "$BUILD/$f" "$ROOT/$dest" >/dev/null 2>&1; then echo "  unchanged  $dest";
  elif [[ ! -f "$ROOT/$dest" ]]; then echo "  NEW        $dest";
  else echo "  CHANGED    $dest  ($(diff "$BUILD/$f" "$ROOT/$dest" | grep -c '^[<>]') lines differ)"; fi
done
if [[ $WRITE == 1 ]]; then
  for pair in "${OUT[@]}"; do cp "$BUILD/${pair%%|*}" "$ROOT/${pair#*|}"; done
  echo "Copied outputs into index/."
else
  echo "Dry run: nothing copied. Rerun with --write to update index/."
fi
