# Agenda

Role: `agenda.csv` lists every policy and option ID, one row each. Status: seeded October 28, 2026 from `legacy/domains/`, `legacy/index/options-register.md` and the transportation rows of the ledger inputs; now the authored record, edited by hand. New ideas are logged here as L0 rows, not as new policy areas.

| Column | Meaning |
| --- | --- |
| `id` | The existing ID (`HOU-4A`, `MOV-29`, `MR1`). IDs are never reused |
| `name` | Plain name, from the legacy definition |
| `home_dossier` | Folder under `dossiers/` that will own it (plan 3.1); dossier work may move items |
| `level` | Specification ladder, L0–L4 (plan 3.2) |
| `status` | See below |
| `source` | Where the legacy definition is (`path:line`) |
| `note` | The options register's status text, or why the row differs from the default |

**Status.**
- `decided`: Espen decided this item individually (the options register or the decision record says so), or it is a component of a decided package.
- `chosen`: part of a legacy domain file's chosen design. Espen accepted those files as canonical batches, not item by item.
  A `chosen` item is a working starting point, not a settled decision: a dossier's design section may recommend changing its form, scale or funding, and Espen decides in a memo (`DEC-2026-10-30-02`).
- `option`: filed, not chosen; would need a decision.
- `alternative`: a lettered variant whose sibling was chosen.
- `held`, `declined`, `retired`, `pointer`: as the options register defines them.

**Seed levels.**
- `decided` and `chosen` items start at **L2**: the legacy domain files give each a chosen design with key parameters, a ten-year cost range and a vehicle.
- Options, alternatives, held, declined and pointer rows start at **L1**; retired IDs at **L0**.
- Nothing is L3 yet. L3 needs provisions, an evidence register and model validation in a dossier. Transportation has draft bill text and is converted first, as the reference dossier.

`python3 agenda/seed_from_legacy.py --check` confirms every ID the legacy files define appears exactly once; the registry checker (stage A, step 4) will run it with the other checks. The seed script records how the list was built and refuses to overwrite `agenda.csv`.
