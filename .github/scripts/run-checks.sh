#!/usr/bin/env bash
# PR checks for Project 2050: the common rebuild (dry run), a drift check and the focused test suites
# that run-all.sh does not already include. Standard-library Python 3.10+ and Node.js only.
# Usage (from the repo root): bash .github/scripts/run-checks.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"; cd "$ROOT"
LOG="${RUNNER_TEMP:-/tmp}/run-all.log"

echo "::group::common rebuild (index/tools/run-all.sh, dry run)"
bash index/tools/run-all.sh | tee "$LOG"
echo "::endgroup::"

# run-all.sh compares every generated file with the committed copy. Any CHANGED or NEW line means the
# committed outputs no longer follow from the committed inputs and code.
if grep -E '^  (CHANGED|NEW) ' "$LOG"; then
  echo "::error::Generated files under index/ (and their sources/ companions) drift from their inputs. Run 'bash index/tools/run-all.sh --write', inspect the diff and commit it."
  exit 1
fi
echo "Drift check: every generated file matches its inputs."

echo "::group::focused tests not run by run-all.sh"
python3 -W ignore::ResourceWarning index/tools/test_family_financing.py
python3 -W ignore::ResourceWarning index/tools/health/test_decision_analysis.py
python3 -W ignore::ResourceWarning index/tools/strategic-review/test_analysis.py
python3 -W ignore::ResourceWarning index/tools/strategic-review/test_redesign.py
python3 index/tools/child-poverty/run_validation.py --out "${RUNNER_TEMP:-/tmp}/child-poverty-validation"
python3 .github/scripts/test_agent_gate.py
echo "::endgroup::"
# Not run: index/tools/public-product/test_build.py stops by design when a pinned source changes
# ("review ... before advancing source_commit"); the public edition is deliberately not refreshed.

if ! git diff --quiet; then
  echo "::error::A check modified tracked files:"; git diff --stat; exit 1
fi
echo "All checks passed."
