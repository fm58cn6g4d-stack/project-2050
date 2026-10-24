# Parked: a detailed border carbon adjustment model

Written 4 Oct 2026 in case this is spun off from the carbon dividend model. Nothing here is built.

## What the current model does

`border.py` multiplies 2022 trade values for 16 basic-materials products (BEA) by U.S. supply-chain emissions per dollar (EPA v1.3), then scales imports by an assumed foreign/U.S. intensity ratio per product. Imports 284 Mt CO2e (219 to 374), exports 211 Mt. In `cfd-model.js`: charge = fee x imports x (1 - 15% origin credit), with a small import elasticity; rebate = fee x exports, shrinking as U.S. industry decarbonises. Net revenue is about $3bn in 2035.

## Why that is not good enough for a border model

1. **Intensity ratios are judgment.** No country or plant data behind them.
2. **Per-dollar factors mix price and carbon.** A cheaper foreign tonne looks dirtier per dollar. EPA's GLORIA import factors gave foreign/U.S. ratios of 7.3 for nonmetallic minerals and 5.3 for refined products for this reason, and are published only at summary-sector level.
3. **No source countries.** Aluminum from Canada and from India are treated alike. The origin carbon-price credit is one flat 15%.
4. **Stale product detail.** BEA detail tables are 2017, scaled to 2022 by sector growth.
5. **No trade response.** No resource shuffling (clean plants redirected to the U.S.), no change in sourcing, no leakage estimate, no effect on U.S. output.
6. **Scope is undefined.** U.S. factors are full supply chain; a statute would pick direct plus electricity, or a list of precursors.
7. **Downstream goods are excluded.** Steel in cars and machinery escapes; exporters of those goods get no rebate.

## What a real model would need

- Physical intensity benchmarks, tonnes CO2 per tonne of product, by country and process route: steel (blast furnace vs electric arc), primary aluminum (grid mix), cement (clinker ratio), ammonia and urea, plus refining and key petrochemicals.
- Import and export tonnage and value by product and partner country, current year (Census / USITC DataWeb, HS 6 to 10 digit).
- Effective carbon prices paid at origin by country and sector (EU ETS, UK, Canada's industrial pricing, China's ETS), net of free allocation.
- Design choices as switches: covered products; scope; default values vs verified plant data; export rebates (and their WTO exposure); treatment of low-income countries; interaction with EU CBAM and existing tariffs (Section 232).
- Trade elasticities by product (Armington) to estimate leakage, shuffling and revenue erosion; ideally a comparison against RFF's Global Economic Model runs of the Clean Competition Act and Foreign Pollution Fee Act.
- Outputs: revenue by product and partner, leakage rate with and without the adjustment, effect on U.S. energy-intensive output, cost passed to downstream users.

## Unverified claims to check first

- U.S. steel is roughly 70% electric-arc and therefore well below the world average per tonne.
- Canada supplies most U.S. primary aluminum imports, on hydropower.
- Cement and refining intensities vary little across countries.

## On hand

BEA supply-use tables (summary 2017-2022, detail 2017); EPA GLORIA import factors 2022; EPA Supply Chain GHG Emission Factors v1.3 (total and by gas); `border.py` and `border.json` in the working session (logic summarised in `cfd-model-notes.md`, v2.8 and v2.9).
