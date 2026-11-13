#!/usr/bin/env bash
# Rebuild the common ledger/fiscal/calendar suite; independent poverty products have their own runners.
# Usage (from the repo root):   bash models/tools/run-all.sh          # rebuild, show a diff, do not overwrite
#                               bash models/tools/run-all.sh --write  # rebuild and copy outputs into place
#                               bash models/tools/run-all.sh --fetch  # also re-download CBO's data first
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
TOOLS="$ROOT/models/tools"; DATA="$ROOT/models/data"; BUILD="$ROOT/build"
WRITE=0; FETCH=0
for a in "$@"; do [[ "$a" == "--write" ]] && WRITE=1; [[ "$a" == "--fetch" ]] && FETCH=1; done

rm -rf "$BUILD"; mkdir -p "$BUILD"
cp "$TOOLS"/ledger-build.py "$TOOLS"/ledger-paths.py "$TOOLS"/ledger-make-md.py "$TOOLS"/incidence-make-md.py \
   "$TOOLS"/climate-integration.py "$TOOLS"/fiscal-data.py "$TOOLS"/fiscal-profiles.py "$TOOLS"/inputs.py "$TOOLS"/scenarios.py "$TOOLS"/fiscal-model.py "$TOOLS"/fiscal-make-md.py "$BUILD"/
# the two incidence scripts import each other under their working names
cp "$TOOLS"/incidence-model.py "$BUILD"/incidence.py
cp "$TOOLS"/incidence-years.py "$BUILD"/years.py

cd "$BUILD"
echo "== 0. transportation";    python3 "$TOOLS"/transportation/test_moving_america.py --quiet
                                python3 "$TOOLS"/transportation/report.py --json "$BUILD"/moving-america.json >/dev/null
echo "== 0a. ledger precision"; python3 "$TOOLS"/test_ledger_rounding.py
echo "== 0b. fiscal components"; python3 "$TOOLS"/test_fiscal_components.py
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
echo "== 5b. budget data layer"; python3 -W ignore::ResourceWarning "$TOOLS"/budget/test_data.py 2>&1 | tail -1
echo "== 6. fiscal model";      python3 fiscal-model.py --baseline "$BUILD/fiscal-baseline.csv" > fiscal-model.log; head -1 fiscal-model.log
python3 fiscal-make-md.py --baseline "$BUILD/fiscal-baseline.csv" >/dev/null
python3 "$TOOLS"/test_climate_integration.py
echo "== 6. MR6 booking check (transportation offset on the general fund)"; BUILD="$BUILD" python3 -W ignore::ResourceWarning "$TOOLS"/test_fiscal_mr6.py 2>&1 | tail -1
echo "== 6. counting inputs check (board 0q, DEC-2026-11-12-08: Moving America timing, C35, DEM-11, the offset rate)"; BUILD="$BUILD" python3 -W ignore::ResourceWarning "$TOOLS"/test_fiscal_counting.py 2>&1 | tail -1
echo "== 6. health booking check (care review F-4: the plan on the dossier's fiscal-year path)"; BUILD="$BUILD" python3 -W ignore::ResourceWarning "$TOOLS"/test_fiscal_health.py 2>&1 | tail -1
echo "== 6. care booking check (care B-D review F-3: parts B-D on the dossier's fiscal-year path)"; BUILD="$BUILD" python3 -W ignore::ResourceWarning "$TOOLS"/test_fiscal_care.py 2>&1 | tail -1
echo "== 6a. provision specs (budget B3)"; python3 -W ignore::ResourceWarning "$TOOLS"/budget/test_provisions.py 2>&1 | tail -1
python3 "$TOOLS"/budget/provisions_report.py --ledger "$BUILD/ledger.json" --out "$BUILD/budget-provisions.md"
echo "== 6b. carbon model";    (cd "$TOOLS"/carbon && node cfd-tests.js >/dev/null) || { echo "carbon model checks failed: run node models/tools/carbon/cfd-tests.js"; exit 1; }
                                cp "$TOOLS"/carbon-model.py "$BUILD"/; python3 carbon-model.py
echo "== 6c. dedicated funds";  cp "$TOOLS"/funds-model.py "$BUILD"/; python3 funds-model.py
echo "== 6d. surge funding";  python3 "$TOOLS"/test_capacity_funding.py
                               cp "$TOOLS"/capacity-funding.py "$BUILD"/; python3 capacity-funding.py
echo "== 6e. budget benchmarks and model card (budget B4)"
P2050_BUILD="$BUILD" python3 -W ignore::ResourceWarning "$TOOLS"/budget/test_benchmarks.py 2>&1 | tail -1
echo "== 6f. health coverage model (tests, then results and model card)"
python3 -W ignore::ResourceWarning "$TOOLS"/health-coverage/test_model.py 2>&1 | tail -1
python3 "$TOOLS"/health-coverage/model.py --out "$BUILD/health-coverage"
echo "== 7. dashboard data";   python3 "$TOOLS"/dashboard-data.py >/dev/null
echo "== 8. consistency check"; cp "$TOOLS"/check-project.py "$TOOLS"/window.py "$BUILD"/; python3 check-project.py

echo "== 8b. education adoption and recovery bridge"
python3 "$TOOLS"/fiscal-recovery/model.py --output-dir "$BUILD"
python3 -W ignore::ResourceWarning "$TOOLS"/fiscal-recovery/test_model.py

echo "== 8c. total-federal Recovery and Solvency budget (exploratory)"
python3 -W ignore::ResourceWarning "$TOOLS"/recovery-budget/model.py --output-dir "$BUILD" > "$BUILD/recovery-budget.log"
python3 -W ignore::ResourceWarning "$TOOLS"/recovery-budget/test_model.py
echo "== 8c. secure floor booking check (review step 7: FAM-1, INC-1 to 5, the leave step, Social Security as decided)"; BUILD="$BUILD" python3 -W ignore::ResourceWarning "$TOOLS"/test_fiscal_secure_floor.py 2>&1 | tail -1
echo "== 8c. immigration booking check (review step 5: IMM-1 as components, E-Verify revenue and the H-1B offset apart, USCIS shares out)"; BUILD="$BUILD" python3 -W ignore::ResourceWarning "$TOOLS"/test_fiscal_immigration.py 2>&1 | tail -1

echo "== 8d. public story page (claim register and generated page)"
# Fails if the story's own content changed without a rebuild; only reports a cited source passage that moved.
python3 "$TOOLS"/public-product/story/build_story.py --report
PUBLIC_STORY_REPORT_ONLY=1 python3 "$TOOLS"/public-product/story/test_story.py 2>&1 | tail -1

echo "== 8e. registry (agenda, library catalog, charter IDs, evidence and provisions, references)"
python3 "$ROOT"/models/registry/check.py
python3 "$ROOT"/models/registry/test_registry.py 2>&1 | tail -1
# Restatement check (charter/PLAN.md 4): a report, never a failure. Lists what each legacy file a dossier
# replaces says that the dossier no longer does (models/registry/restatement.py; maps in dossiers/**/restatement.json).
python3 "$ROOT"/models/registry/test_restatement.py 2>&1 | tail -1
python3 "$ROOT"/models/registry/restatement.py --all || true
python3 "$ROOT"/library/test_fetch_public.py 2>&1 | tail -1
python3 "$ROOT"/library/test_build_catalog.py 2>&1 | tail -1

python3 "$TOOLS"/climate-integration-report.py

echo "== 8f. budget assumptions page (from models/data/budget/assumptions.csv)"
python3 "$TOOLS"/budget/assumptions_page.py --out "$BUILD/budget-assumptions.md" >/dev/null

echo "== 8g. fiscal viewer (B5): tests, then the page from this run's fiscal-model.json"
python3 -W ignore::ResourceWarning "$TOOLS"/budget/viewer/test_viewer.py 2>&1 | tail -1
python3 "$TOOLS"/budget/viewer/build_viewer.py --model "$BUILD/fiscal-model.json" --out "$BUILD/fiscal-viewer.html" --snapshot-out "$BUILD/viewer-snapshot.json" >/dev/null

OUT=(
  'climate-ledger-integration.md|legacy/sources/climate-ledger-integration.md'
  'budget-assumptions.md|models/tools/budget/assumptions.md'
  'fiscal-viewer.html|models/tools/budget/viewer/fiscal-viewer.html'
  'viewer-snapshot.json|models/tools/budget/viewer/snapshot.json'
  'budget-provisions.md|models/tools/budget/provisions.md'
  'budget-benchmarks.md|models/tools/budget/benchmarks.md'
  'budget-benchmarks.json|models/tools/budget/benchmarks.json'
  'budget-model-card.md|models/tools/budget/MODEL-CARD.md'
  'health-coverage/results.json|models/tools/health-coverage/results.json'
  'health-coverage/results.md|models/tools/health-coverage/results.md'
  'health-coverage/MODEL-CARD.md|models/tools/health-coverage/MODEL-CARD.md'
  'recovery-budget.md|legacy/index/recovery-budget.md'
  'recovery-budget.json|models/data/recovery-budget.json'
  'recovery-budget-paths.csv|models/data/recovery-budget-paths.csv'
  'recovery-budget-audit.csv|legacy/sources/recovery-budget-audit.csv'
  'education-component-reconciliation.csv|legacy/sources/education-component-reconciliation.csv'
  'fiscal-recovery-model.md|legacy/index/fiscal-recovery-model.md'
  'fiscal-recovery-model.json|models/data/fiscal-recovery-model.json'
  'fiscal-recovery-inventory.csv|legacy/sources/fiscal-recovery-inventory.csv'
  'calendar-scenarios.md|legacy/index/calendar-scenarios.md'
  'calendar-delivery-opportunities.md|legacy/index/calendar-delivery-opportunities.md'
  'calendar-scenario-explorer.html|legacy/index/calendar-scenario-explorer.html'
  'calendar-scenarios.json|models/data/calendar-scenarios.json'
  'calendar-delivery.json|models/data/calendar-delivery.json'
  'dashboard/calendar.json|models/data/dashboard/calendar.json'
  'capacity-funding-model.md|legacy/index/capacity-funding-model.md'
  '2029-trifecta-master-ledger-v2.md|legacy/index/2029-trifecta-master-ledger.md'
  'revenue-household-incidence-model.md|legacy/index/revenue-household-incidence-model.md'
  'fiscal-long-term-model.md|legacy/index/fiscal-long-term-model.md'
  'fiscal-baseline.csv|models/data/fiscal-baseline.csv'
  'fiscal-paths.csv|models/data/fiscal-paths.csv'
  'check-report.md|legacy/index/check-report.md'
  'vote-simulation.md|legacy/index/vote-simulation.md'
  'dedicated-funds.md|legacy/index/dedicated-funds.md'
  'climate-carbon-model.md|legacy/index/climate-carbon-model.md'
  'dashboard/bills.json|models/data/dashboard/bills.json'
  'dashboard/revenue.json|models/data/dashboard/revenue.json'
  'dashboard/cuts.json|models/data/dashboard/cuts.json'
  'dashboard/conflicts.json|models/data/dashboard/conflicts.json'
  'dashboard/paths.json|models/data/dashboard/paths.json'
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
  echo "Copied outputs into place."
else
  echo "Dry run: nothing copied. Rerun with --write to update them."
fi
