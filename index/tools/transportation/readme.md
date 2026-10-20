# Transportation model (Moving America Act of 2031)

These scripts produce every figure in `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, MOV-). They came from the Surface Transportation claude.ai Project's `claude/` folder and were filed here on Oct 20, 2026, unchanged. They are separate from `run-all.sh`: the ledger rows MOV-29, MOV-30, MOV-31 and MR1-MR6 in `ledger-build.py` are keyed by hand from Draft 2, so a change here means updating those rows and regenerating.

## Running
From the repo root, Python 3 only (standard library):

```
python3 index/tools/transportation/final_v3.py      # Draft 2's governing figures
```

Each script imports the others from its own folder. Three write files into the current folder: `transit_fiscal_model.py --json` (transit_model_output.json), `transit_apportionment.py` (apportion_fy2031.json) and `transit_pipeline_data.py` (pipeline.json); run those from `build/` or a scratch folder so the output is not committed.

## The stack
`transit_fiscal_model.py` is the base model. It still carries some superseded settings (sec. 606, revenue, shares); the overlays below apply Draft 2's decisions on top, and folding them into the base model is an open item in Draft 2.

| Script | What it adds | Status |
| --- | --- | --- |
| `transit_fiscal_model.py` | Base fiscal model: programs, trust-fund receipts, general-fund draw, FY2032-36 calendar (`BILL_START = 2032`) | Base |
| `merge_decisions.py` | Merge-session decisions (A-6, A-8, A-11, A-14) | Overlay |
| `solvency_paths.py`, `solvency_grid.py`, `solvency_final.py` | Revenue paths to solvency; plug-in displacement of gasoline after FY2036 | Overlay |
| `revenue_plan.py` | Revenue across the 2029 act, 2030 act and 2031 bill; share splits | Overlay |
| `funding_stack.py` | Splits money by legal instrument; scores each reconciliation act against CBO's convention | Overlay |
| `final_architecture.py` | Integrated figures for the merged program | Overlay |
| `final_bill.py` | Division B redesign (Interstate and Bridge Renewal, sec. 1104) | Overlay |
| `fossil_premium.py`, `fossil_final.py` | Fossil transition premium (A-28) | Overlay |
| `final_v3.py` | Adds the 40-mpg clean-car peg and PHEVs at 30% (A-11); prints every figure Draft 2 carries | **Governing** |
| `rev_variant.py`, `rev_variant2.py` | Earlier revenue redesigns | Superseded by `solvency_paths.py` |
| `transit_apportionment.py` + `ntd_uza_2024.py` | Sec. 5307(i) operating-tier apportionment on NTD 2024 data | Supporting |
| `transit_pipeline_data.py` | Transit delivery pipeline (64 projects) behind the grid and map | Supporting |

## Related files
- Decision record for the FY2032-36 calendar: `sources/transportation-calendar-fy2032-36.md`.
- Status at the merge: `sources/transportation-merge-status-oct12.md`; earlier state in the other `sources/transportation-*` files.
- The ARCA, ATRA and section-by-section docs: `sources/transportation-*-bill-architecture.md` and `sources/transportation-package-section-by-section.md`. Draft 2 governs where they differ.
