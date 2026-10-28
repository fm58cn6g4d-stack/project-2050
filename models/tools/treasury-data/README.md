# Treasury actuals: isolated snapshot adapter

Use Monthly Treasury Statement (MTS) actuals to check recent total-government receipts/outlays before designing the financing envelope. This is a prepared raw-data adapter, **pending live validation**. October 26 attempts to open the supplied documentation and API both returned HTTP 403; no Treasury observations were fetched or inserted into the model. The six tests use synthetic responses. The subsequently supplied 13-page printout verifies the request contract; it does not resolve live API access.

References:
- [Fiscal Data API documentation](https://fiscaldata.treasury.gov/api-documentation/) — verified using the [user-supplied printout](../../../sources/treasury-fiscal-data-api-documentation-2026-10-26.pdf); direct web access unavailable in this session.
- [Treasury MTS description](https://fiscal.treasury.gov/accounting/monthly-treasury-statement) — describes modified-cash receipts, outlays and financing.
- [Official data catalog](https://catalog.data.gov/dataset/monthly-treasury-statement-mts) — confirms MTS table resources and values in millions of dollars.

From repository root, when API access is available:

```sh
python3 models/tools/treasury-data/fetch.py --start 2024-10-01 --end 2025-09-30 --output /tmp/mts-fy2025-snapshot.json
python3 -m unittest discover -s models/tools/treasury-data -p 'test_*.py'
```

The adapter requests all fields for MTS table 1, preserves raw response text, hashes, metadata, exact query URLs and retrieval time. It follows numbered pages, rejects missing/inconsistent completeness metadata and repeated rows, and refuses partial or empty results. Existing snapshots cannot be overwritten. Do not omit classification dimensions or aggregate every table row: table 1 contains reporting categories/comparisons, not a flat series of independent additive amounts. Live schema and pagination conventions must be verified before claiming production readiness.

The next integration step is to inspect the field dictionary and a successful snapshot, select mutually exclusive current-period totals, and reconcile receipts minus outlays with the stated balance. Preserve fiscal versus calendar years, monthly versus fiscal-year-to-date values, signs, units and revisions. Nulls remain source strings and must not become zero. Test the mapping against the published MTS before building an actuals-to-CBO comparison.

MTS provides historical execution, not an estimate of a new tax's yield or a forward current-law projection. Agency outlays do not equal budget authority or staffing costs. Debt-series extensions should distinguish debt held by the public from gross debt and intragovernmental holdings; no debt endpoint is implemented here. The common rebuild does not fetch live data or change vintages. Once retrieved and verified, snapshots belong in a dated evidence package, with an explicit reviewed bridge into fiscal assumptions.


## Documentation verification

The supplied printout is dated October 26, 2026, 11:32. Page 3 confirms the exact MTS table-1 endpoint and its classification fields. Pages 7–10 confirm all-field default, string/null handling, filter syntax, nested sorting, numbered pagination and total-count/total-pages metadata. Page 11 warns that selecting too few dimensions can trigger automatic aggregation. The adapter therefore requests all fields and sorts by record date, parent and classification; uniqueness still requires verification against the live table dictionary. It retains metadata and numeric strings rather than prematurely assigning budget meanings.

Page 2 says no registration or token is needed. The observed Python error was a proxy tunnel 403, not evidence that Treasury requires credentials. Page 9's generic status-code table does not justify requesting a key. No credentials or third-party data proxy were introduced. The printed endpoint table shows only ten of 182 rows; this is not a complete dataset dictionary or endpoint inventory.
