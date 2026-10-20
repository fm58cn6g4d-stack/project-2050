"""fiscal-profiles.py: year profiles for every ledger row the long-term model uses.

The ledger scores everything as 2030-39 totals. The long-term model needs annual paths, so
each row gets a profile here. The model calibrates every profile so its FY2030-39 sum equals
the ledger's ten-year midpoint exactly; the profile only decides how that total is spread
across the window and how the row runs on after 2039. Every profile is an estimate (basis
noted) until a domain file supplies a year-by-year score; when one does, put it in YEARS.

Fields
  cat     baseline category the row adds to (see fiscal-data.py), so the all-of-government
          view stays in CBO's categories. Outlay rows use out_*, revenue rows rev_*.
  start   first fiscal year with any effect (default 2030)
  ramp    years to full phase-in from start (1 = full in the first year)
  grow    growth index: "gdp", "cpi", or a baseline category name (the row then keeps a
          constant share of that category: health rows track CBO's health spending,
          revenue rows track their tax base, including bracket creep)
  end     last year of a time-limited line (None = permanent)
  perm    share of the 2039 run rate that continues after 2039 (1.0 = all; time-limited
          capital and temporary credits carry less)
  fade    after 2039, the continuing part shrinks this share a year (e.g. credits that phase
          down as clean energy saturates)

Sign convention: positive = raises the deficit. Ledger outlay rows are costs (positive),
revenue rows are entered as negatives, savings as negatives.
"""

# ----- program rows (ledger bills, keyed by domain-file ID) -----
BILLS = {
    "HLT-1": dict(cat="out_health_other", ramp=1, grow="out_health_other", basis="Repeal of H.R. 1 cuts and permanent ACA credits take full effect at once"),
    "HLT-2": dict(cat="out_medicare_net", ramp=3, grow="out_medicare_net", basis="Medicare cap and benefits phase in over three years (dental last)"),
    "HLT-3": dict(cat="out_health_other", start=2031, ramp=3, grow="out_health_other", basis="Public option enrollment builds from 2031"),
    "HLT-4": dict(cat="out_health_other", ramp=3, grow="out_health_other", basis="Medicaid and LTC expansions phase in"),
    "HLT-5": dict(cat="out_medicare_net", start=2031, ramp=5, grow="out_medicare_net", basis="Price caps tighten over five years"),
    "HLT-6": dict(cat="out_medicare_net", ramp=4, grow="out_medicare_net", basis="MA payment reform phases in over four years"),
    "FAM-1": dict(cat="out_other_mandatory", ramp=1, grow="cpi", basis="CTC indexed to prices; child population roughly flat"),
    "FAM-2": dict(cat="out_other_mandatory", ramp=6, grow="gdp", basis="Child care and pre-K phase in over six years, then track wages (GDP)"),
    "FAM-3": dict(cat="out_other_mandatory", ramp=1, grow="gdp", unified_zero=True, basis="Paid leave is self-funded by its contribution (net zero, automatic step-up)"),
    "EDU-1": dict(cat="out_other_mandatory", ramp=3, grow="gdp", basis="Formula funding steps up over three years"),
    "EDU-3": dict(cat="out_other_mandatory", ramp=1, grow="cpi", basis="Universal meals at once, price-indexed"),
    "EDU-4": dict(cat="out_disc_nondefense", ramp=2, grow="gdp", basis=""),
    "EDU-5": dict(cat="out_other_mandatory", ramp=1, grow="cpi", basis="Pell increment indexed to prices"),
    "EDU-7": dict(cat="out_other_mandatory", ramp=1, grow="gdp", basis="Repeal saves from the first year"),
    "EDU-8": dict(cat="out_disc_nondefense", ramp=2, grow="gdp", basis=""),
    "SS-1": dict(cat="out_social_security", ramp=1, grow="special_ss", basis="D8 package: net -$2.75T in window; after 2039 the benefit credit and CPI-E grow faster than the revenue, so the net saving shrinks ~1.5% a year relative to GDP (estimate)"),
    "CLI-1": dict(cat="out_other_mandatory", ramp=1, grow="gdp", perm=0.8, fade=0.04, basis="Clean-energy credits; scale down as deployment saturates after 2039 (estimate)"),
    "CLI-2": dict(cat="out_other_mandatory", ramp=1, grow="gdp", unified_zero=True, basis="Dividend is paid from the carbon fee; its 20% remainder funds CLI-5 (counted there)"),
    "CLI-3": dict(cat="out_disc_nondefense", ramp=2, grow="gdp", basis=""),
    "CLI-5": dict(cat="out_other_mandatory", ramp=3, grow="gdp", perm=0.3, basis="Net of fee and border revenue; capital-heavy, so most ends with the window (estimate)"),
    "CLI-6": dict(cat="out_other_mandatory", ramp=1, grow="gdp", basis=""),
    "CLI-7": dict(cat="out_other_mandatory", ramp=1, grow="gdp", basis=""),
    "HOU-1": dict(cat="out_other_mandatory", ramp=2, grow="gdp", perm=0.55, basis="Emergency aid and public-housing repair are time-limited; credits and vouchers continue (estimate)"),
    "HOU-7": dict(cat="out_other_mandatory", ramp=1, grow="gdp", basis=""),
    "LAB-1": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", basis=""),
    "LAB-5": dict(cat="out_other_mandatory", start=2031, ramp=1, grow="gdp", end=2036, perm=0.0, basis="Wage-transition credit is temporary"),
    "LAB-8": dict(cat="out_disc_nondefense", ramp=2, grow="gdp", basis=""),
    "LAB-9": dict(cat="out_other_mandatory", ramp=4, grow="gdp", basis="National service slots build over four years"),
    "COM-1": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", basis=""),
    "IMM-1": dict(cat="out_other_mandatory", ramp=3, grow="gdp", basis="Net saving grows as legalized workers enter the tax base"),
    "AI-1": dict(cat="out_disc_nondefense", ramp=2, grow="gdp", basis=""),
    "AI-4": dict(cat="out_other_mandatory", start=2031, ramp=3, grow="gdp", basis="Displacement-triggered; builds with take-up"),
    "AI-9": dict(cat="out_other_mandatory", ramp=1, grow="gdp", basis=""),
    "D2-RULES": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", basis=""),
    "DEM-1": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", basis=""),
    "DEM-5": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", basis=""),
    "DEM-6": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", basis=""),
    "DEM-11": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", basis=""),
    "DEM-16": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", basis=""),
    "DEM-17": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", end=2036, perm=0.0, basis="Time-limited community infrastructure fund"),
    "DEM-3": dict(cat="out_disc_nondefense", start=2033, ramp=1, grow="gdp", basis="House enlargement from 2033"),
    "DEM-4": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", basis=""),
    "INT-1": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", basis=""),
    "CRT-P1": dict(cat="out_disc_nondefense", ramp=3, grow="gdp", basis="Judgeships phased"),
    "EXE-1": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", basis=""),
    "CAP-8": dict(cat="out_disc_nondefense", ramp=2, grow="gdp", basis=""),
    "CAP-7": dict(cat="out_disc_nondefense", ramp=3, grow="gdp", basis="Agency rebuild steps up over three years, then tracks GDP"),
    "NSC-1": dict(cat="out_disc_defense", ramp=1, grow="gdp", basis=""),
    "NSC-8": dict(cat="out_disc_nondefense", ramp=2, grow="gdp", basis=""),
    "NSC-10": dict(cat="out_disc_nondefense", ramp=3, grow="gdp", basis=""),
    "RTS-1": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", basis=""),
    "RTS-3": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", basis=""),
    "SAF-1": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", basis=""),
    "SAF-10": dict(cat="out_disc_nondefense", ramp=3, grow="gdp", basis="Compacts build over three years"),
    "MOV-29": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", perm=0.3, basis="General-fund top-ups and capital lines; mostly time-limited (C30)"),
    "MOV-30": dict(cat="out_disc_nondefense", ramp=1, grow="gdp", perm=0.3, basis="Same"),
    "MOV-31": dict(cat="out_disc_nondefense", start=2032, ramp=1, grow="gdp", end=2036, perm=0.3, basis="FY2032-36 renewal top-ups; a successor authorization is assumed at 30% of the run rate"),
}

# ----- revenue rows in the top-end base (ledger REV rows with in_base) -----
REVENUE = {
    "G1": dict(cat="rev_corporate", ramp=1, grow="rev_corporate"),
    "H1b": dict(cat="rev_individual", ramp=1, grow="rev_individual"),
    "G3": dict(cat="rev_individual", ramp=1, grow="rev_individual"),
    "G11": dict(cat="rev_individual", ramp=1, grow="rev_individual", basis="Mark-to-market; the deemed-realization transition is front-loaded in scores, flattened here"),
    "G5": dict(cat="rev_corporate", ramp=1, grow="rev_corporate"),
    "G6": dict(cat="rev_individual", ramp=2, grow="rev_individual"),
    "G7": dict(cat="rev_corporate", ramp=1, grow="rev_corporate"),
    "G8": dict(cat="rev_individual", ramp=3, grow="rev_individual", basis="Enforcement yield builds as staff are hired"),
    "G9": dict(cat="rev_individual", ramp=1, grow="rev_individual"),
    "G10": dict(cat="rev_other", ramp=1, grow="gdp"),
    "GX": dict(cat="rev_individual", ramp=1, grow="rev_individual"),
}

# ----- options from the cuts table (ledger CUTS, keyed by C-number) -----
# kind "revenue" adds revenue; "trim" cuts spending; "borrow" changes no deficit (it only
# labels what is financed by borrowing under D4), so borrow rows carry no profile effect.
CUTS = {
    "C18": dict(kind="revenue", cat="rev_individual", ramp=1, grow="rev_individual"),
    "C35": dict(kind="revenue", cat="rev_other", ramp=1, grow="gdp", basis="Estate tax increment; exemption frozen in nominal terms, so it grows faster than GDP in practice (held at GDP)"),
    "C19b": dict(kind="revenue", cat="rev_individual", start=2031, ramp=2, grow="out_medicare_net", basis="Exclusion cap revenue tracks premium growth (proxied by Medicare per-GDP growth)"),
    "C19": dict(kind="revenue", cat="rev_individual", start=2031, ramp=2, grow="out_medicare_net"),
    "C20": dict(kind="revenue", cat="rev_individual", ramp=1, grow="rev_individual"),
    "C38": dict(kind="revenue", cat="rev_corporate", ramp=2, grow="rev_corporate", basis="Sprint package: about three-quarters corporate"),
    "C5": dict(kind="trim", cat="out_medicare_net", ramp=1, grow="out_medicare_net", perm=0.0, basis="Dental delayed past the window: saves inside it, none after"),
    "C17": dict(kind="trim", cat="out_disc_nondefense", ramp=3, grow="gdp"),
    "C33": dict(kind="trim", cat="out_other_mandatory", ramp=4, grow="gdp"),
    "C34": dict(kind="trim", cat="out_disc_nondefense", ramp=3, grow="gdp"),
    "C36": dict(kind="trim", cat="out_other_mandatory", ramp=1, grow="cpi"),
    "C29": dict(kind="trim", cat="out_other_mandatory", ramp=3, grow="gdp", perm=0.3),
    "C21": dict(kind="borrow"), "C30": dict(kind="borrow"), "C31": dict(kind="borrow"),
    "C32": dict(kind="borrow"), "C37": dict(kind="borrow"),
}

# ----- explicit year-by-year paths that override a profile (billions, 2030-39) -----
YEARS = {
    # e.g. "HLT-3": [0, 120, 170, 190, 200, 205, 210, 215, 220, 225],
}
