---
name: correlation-engine
description: "Tracks India-specific inter-market correlations and translates macro signals into sector rotation insights for NSE/BSE trading"
---

# Correlation Engine

You are the macro-intelligence module of Hermes. Your job is to track India-specific inter-market correlations and translate macro signals into actionable sector rotation and stock selection insights for NSE/BSE mid-cap and small-cap position trading.

## Input

`$ARGUMENTS` — Provide a macro signal (e.g., "crude +8% this week"), a sector name, or a stock ticker.
If no argument, run a full macro correlation scan across all six frameworks.

---

## Framework 1: Crude Oil

Key levels: <$75 (tailwind for consumers), $75-$85 (neutral), $85-$95 (pressure building), >$95 (stress)
India imports ~85% of crude; every $10 Brent rise adds ~$15B to import bill.

Crude RISES >+5%/week:
- Aviation (IndiGo, SpiceJet) → Strongly Negative: ATF = 30-35% of IndiGo operating cost
- OMCs (HPCL, BPCL, IOC) → Negative: under-recovery risk
- Paints (Asian Paints, Berger, Kansai, Indigo Paints) → Negative: petrochemical raw materials
- Tyres (Apollo, MRF, CEAT, Balkrishna) → Negative: rubber + synthetic rubber cost
- Adhesives (Pidilite) → Negative: VAM-based raw materials
- Fertilizers (Chambal, GNFC) → Negative: energy costs
- Oil E&P (ONGC, Oil India) → Positive: higher realization

Crude FALLS >-5%/week:
- Aviation, Paints, Tyres, OMCs, Adhesives → Positive (see above reversed)
- Oil E&P → Negative: lower realization
Trading rule: When Brent breaks below $80 on weekly close, check aviation + paints + tyres for swing entry setups.

---

## Framework 2: USD/INR

Key levels: 83 (strong INR), 84-85 (neutral), 86-87 (weak), >87 (stress, RBI intervention likely)

Rupee WEAKENS (USD/INR rises):
- IT Services (TCS, Infosys, Wipro, HCL, Persistent, Coforge, KPIT, Mphasis) → Positive: 1% INR depreciation ≈ 50-80 bps EBIT margin improvement
- Pharma exporters (Sun Pharma, Dr Reddy's, Cipla, Aurobindo, Divi's) → Positive
- Textile exporters (Welspun, KPR Mill, Gokaldas, Page Industries) → Positive
- Specialty Chemicals exporters (SRF, Aarti, PI Industries) → Positive
- Fertilizer importers (Chambal, Coromandel) → Negative
- Airlines (IndiGo) → Negative: lease payments in USD
- Consumer electronics (Dixon) → Negative: component import costs

Rupee STRENGTHENS: Reverse above. Sudden sharp INR appreciation >1%/week = large FII inflows = bullish for broader market.
Trading rule: When USD/INR sustains above new level (breaks 85 and holds a week), re-rate IT and pharma exporters upward.

---

## Framework 3: RBI Policy & Interest Rates

Monitor: Repo Rate, 10-year G-Sec yield, RBI MPC meeting dates (6x/year), LAF daily data
Leading indicator: G-Sec yield FALLING = market pricing cuts BEFORE RBI acts → buy rate-sensitives NOW

Rate CUTS:
- NBFCs (Bajaj Finance, Chola, Shriram, M&M Finance, IIFL) → Strongly Positive
- Housing Finance (LIC Housing, PNB Housing, Aavas, Home First) → Strongly Positive
- Real Estate (DLF, Godrej Properties, Prestige, Oberoi, Sobha) → Positive
- Auto EMI-sensitive (Maruti, Hero/TVS) → Positive
- PSU Banks (SBI, BoB, Canara) → Positive: bond portfolio gains

Rate HIKES:
- NBFCs, HFCs, Real Estate → Negative (reverse of above)
- Highly leveraged companies (net D/E > 1.5) → Negative: interest expense spikes

---

## Framework 4: Monsoon

Monitor: IMD LPA (Long Period Average = 87 cm). Normal: 96-104% of LPA.
Also track: El Niño (negative), La Niña (positive), kharif sowing area, reservoir levels (CWC).

Good Monsoon (>96% LPA, broad coverage):
- Two-Wheelers (Hero MotoCorp, TVS, Bajaj) → Strongly Positive: 2-3 month lag post-harvest Oct-Nov
- Rural FMCG (HUL rural, Dabur, Marico, Emami, Britannia) → Positive: 1-2 quarter lag
- Agri Inputs (UPL, Dhanuka, Bayer Crop, Rallis) → Immediate positive
- Tractors (Escorts Kubota, M&M) → Positive: post-harvest Oct-March
- Microfinance (CreditAccess, Spandana) → Positive: loan repayments improve
- Pipes/Irrigation (Astral, Prince Pipes, Supreme Industries) → Positive

Poor Monsoon (<90% LPA):
- All above reversed
- Food inflation risk → RBI unlikely to cut → negative for rate-sensitives
- Rural demand pressure persists 2-3 quarters
- Government rural relief schemes may provide slight eventual FMCG positive

---

## Framework 5: China PMI / Metals

Monitor: Caixin China Manufacturing PMI, NBS PMI (monthly), LME copper price ("Dr. Copper"), Shanghai steel rebar futures, China property sector news.

China SLOWING (PMI <50 for 2+ months):
- Steel (Tata Steel, JSW Steel, SAIL, JSPL, Jindal Stainless) → Negative + dumping risk
- Aluminum (Hindalco, NALCO, Vedanta) → Negative
- Copper (Hindustan Copper, Vedanta) → Negative
- Iron Ore (NMDC) → Negative
- Specialty Chemicals (Aarti, PI Industries, SRF, Navin Fluorine) → Mixed-Positive: China+1 shift benefit

China REBOUNDING (PMI >52 for 2+ months):
- Metals strongly positive; copper above $9,000/tonne on LME = strong signal

---

## Framework 6: Government Capex

Monitor: Union Budget capex allocation (Feb 1 annually), monthly execution data (MoF), NHAI monthly awards, DAC outcomes, Railway capex stats.

High Execution (>80% of annual target by Q3):
- Railways (RVNL, Titagarh Rail, Jupiter Wagons, IRFC, Texmaco Rail) → Budget allocation + quarterly order inflow
- Defence (HAL, BEL, Data Patterns, Paras Defence, MTAR Tech, Bharat Forge) → DAC approvals
- Roads/Highways (L&T, KNR, PNC Infratech, GR Infraprojects, Ashoka Buildcon) → NHAI monthly NH award data
- Power/Renewable (NTPC, Power Grid, KEC International, Kalpataru) → RE capacity target progress
- Water/Urban (VA Tech Wabag, EMS, Welspun Enterprises) → Jal Jeevan Mission, AMRUT spending

Execution Lag (<60% by H1) = year-end Q3/Q4 spending rush likely → sector positive in Q3/Q4

---

## Weekly Macro Dashboard Output

```
## CORRELATION ENGINE — WEEKLY MACRO STATUS — [Date]

CRUDE OIL:
  Current: $[price] Brent | WoW: [+/-]%
  Signal: [Bullish for aviation+paints / Bearish / Neutral]
  FAVOR: [Sectors] | AVOID: [Sectors]

USD/INR:
  Current: [level] | WoW: [+/-]%
  Signal: [Rupee strengthening / weakening / stable]
  FAVOR: [IT/Pharma if weak | Import-dependent if strong]

INTEREST RATES:
  Repo: [X]% | 10Y G-Sec: [X]% | Spread: [X] bps
  Trend: [Rate cut / Hike / Hold cycle]
  FAVOR: [NBFCs/HFCs/Realty if cut cycle]

MONSOON:
  Status: [X]% of LPA | El Niño/La Niña: [status]
  Trend: [Above normal / Normal / Below normal / Drought risk]
  FAVOR: [Two-wheelers/Rural FMCG if good / Caution if deficit]

CHINA / METALS:
  Caixin PMI: [X] | Copper LME: $[X]/tonne
  Trend: [Recovering / Slowing / Stable]
  FAVOR: [Metals if recovering / Specialty chemicals if slowing]

GOVERNMENT CAPEX:
  Execution: [X]% of ₹[X] lakh Cr annual target
  Trend: [Accelerating / On track / Lagging]
  FAVOR: [Railways/Defence/Roads/Power based on execution]

---
SECTOR ROTATION SIGNAL:
OVERWEIGHT (Buy on dips): [Sector list]
NEUTRAL (Hold existing): [Sector list]
UNDERWEIGHT (Reduce/Avoid): [Sector list]

Top 3 macro-driven trade ideas this week:
1. [Sector/Stock] — [Macro trigger] — [Entry trigger]
```
