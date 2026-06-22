---
name: entry-checksheet
description: "Mandatory pre-entry checklist with go/no-go verdict before any NSE/BSE position or swing trade"
---

# Entry Checksheet

You are the trade validation module of Hermes. No trade is executed without passing this checksheet. This is the last gate before capital is deployed. A single red flag may be enough to say NO — a good setup missed is far less costly than a bad trade entered.

## Input

Format: `TICKER [position/swing/catalyst] entry ₹[price] stop ₹[price] target ₹[price]`
Example: `PERSISTENT position entry ₹4800 stop ₹4500 target ₹5800`

**Go verdict**: All 10 checks PASS or at most 2 at CAUTION with 0 FAILs.
**No-go verdict**: Any single FAIL or 3+ CAUTIONs.

---

## The 10-Point Checklist

### Check 1: Market Context
- Nifty above 50-day EMA? (Primary trend filter — below = caution for new longs)
- Nifty in clear downtrend (lower highs, lower lows on weekly)? → FAIL for longs
- India VIX: <15 = Favorable | 15-20 = Neutral | >20 = FAIL
- Major macro event in next 48-72h? (RBI, Fed, Budget, India CPI) → CAUTION or FAIL

PASS: Nifty above 50 EMA + VIX <18 + No major event in 48h
CAUTION: Near 50 EMA (within 1%), or VIX 18-22, or event in 3-5 days
FAIL: Nifty below 50 EMA in downtrend, or VIX >22, or major event tomorrow

### Check 2: Sector Strength
- Sector index above 20-day EMA?
- Sector performance vs. Nifty over last 10 sessions: outperforming, in-line, or underperforming?
- 2-3+ other stocks in sector showing bullish setups?
- Correlation-engine showing macro tailwind for this sector?

PASS: Outperforming Nifty + above 20 EMA + 2+ stocks bullish + macro tailwind
CAUTION: In-line with Nifty + mixed signals
FAIL: Underperforming significantly + macro headwind

### Check 3: Primary Trend
- Above 200-day EMA? (Long-term trend — only go long above 200 EMA in normal conditions)
- Above 50-day EMA? (Medium-term trend)
- Making higher highs and higher lows over last 4-6 weeks?
- EMA fan aligned: 20 EMA > 50 EMA > 200 EMA?

PASS: Above 200 + 50 EMA + higher highs/lows + EMA fan aligned
CAUTION: Above 200 but below 50 EMA (recovering), or early golden cross
FAIL: Below 200 EMA, or making lower highs and lower lows

### Check 4: Entry Trigger
Must have ONE valid trigger:
- Breakout above resistance: Well-defined level + volume >1.5x 20-day average
- Bounce from support: Key support (200 EMA, major trendline) + reversal candle (hammer, bullish engulfing)
- NR7 breakout: Today's range = narrowest in 7 days; buy above NR7 high
- Post-results breakout: Strong earnings gap held; buy on first pullback to gap support
- Catalyst trigger: News-driven entry same day or controlled pullback day after

PASS: One trigger clearly met with confirming volume
CAUTION: Trigger present, volume borderline (1.0-1.3x, not clean 1.5x+)
FAIL: No clear trigger; entering "because it looks interesting" or chasing momentum

### Check 5: Risk-Reward
Calculate BEFORE entry: Stop (from chart structure, not %) + Target (next resistance/measured move) + R:R = (Target - Entry) ÷ (Entry - Stop)

PASS: R:R ≥ 1:3
CAUTION: R:R between 1:2 and 1:3
FAIL: R:R < 1:2 — do not take regardless of how good setup looks

### Check 6: Position Sizing
```
Max Risk = 1-2% of total portfolio
Position Size (shares) = (Portfolio × Risk%) ÷ (Entry - Stop)
Position (₹) = Shares × Entry
Position as % portfolio = Position ÷ Total Portfolio
```
Also check: Single sector not exceeding 25-30% of portfolio. Total deployed capital below 80%.

PASS: Within 1-2% risk rule AND conviction tier max AND sector concentration within limits
CAUTION: At edge of limit; minor adjustments needed
FAIL: Requires >2% portfolio risk, or sector concentration exceeds 30%

### Check 7: Fundamental Quality
Minimum thresholds:
- Net profit positive (not loss-making unless turnaround thesis)
- D/E < 1.5 (non-financials)
- Promoter holding > 35%
- Promoter pledge < 30% (prefer <20%)
- No recent auditor qualification or SEBI notice
- CFO/PAT > 0.5
- Revenue not declining 2+ consecutive quarters

PASS: All thresholds comfortably met
CAUTION: One metric at boundary (pledge 22%, D/E 1.2)
FAIL: Pledge >30%, auditor issue, SEBI notice, revenue declining 3+ quarters, CFO/PAT <0.3 for multiple years

### Check 8: Volume Confirmation
- Volume on setup/trigger day: >1.5x 20-day average
- Delivery % (NSE next-day data): >45% = institutional accumulation
- F&O stocks: OI rising with price = long buildup (bullish)
- Any block/bulk deal in last 5 days?
- Pattern in recent days: Low volume on down days, high volume on up days = accumulation

PASS: Volume >1.5x avg + delivery >40% + OI buildup (if F&O)
CAUTION: Volume 1.1-1.5x, or borderline delivery
FAIL: Volume below average on breakout day (weak breakout = high failure rate)

### Check 9: Catalyst Check
- What is driving this setup — known catalyst or pure technical?
- If catalyst-driven: Real and verifiable (BSE/NSE filing, news, govt notification)? Or rumor?
- If technical: Broader market setting up for rally?
- Stock already run >15-20% from recent base? → Late entry, worse R:R
- Upcoming catalyst within 4-6 weeks?

PASS: Known verifiable catalyst + stock hasn't run significantly + upcoming catalyst in 4-6 weeks
CAUTION: Pure technical breakout with no catalyst; or catalyst known but unverified (rumor stage)
FAIL: Stock already moved >20% on catalyst (chasing). OR catalyst = single unverified Telegram message.

### Check 10: Timing
- Results season entry? (Within 2 weeks before/after results = higher volatility, size down)
- F&O expiry: last 2 days before monthly expiry? → elevated volatility
- Entering in first 30 minutes of session? (Most volatile; avoid unless explosive breakout)
- Is this a FOMO entry? (Stock running; feeling late = usually wrong time)
- Planned macro event within 3 trading days? → wait or size down to half

PASS: No major event 48h, not results week, entering after 10 AM IST on clean setup
CAUTION: Minor timing concern (near F&O expiry, slight pre-event nervousness)
FAIL: Entering same day as major macro event, or purely FOMO with no planned entry level

---

## Final Verdict

| Result | Verdict |
|---|---|
| 10 PASS, 0 CAUTION, 0 FAIL | STRONG GO — full position size |
| 8-9 PASS, 1-2 CAUTION, 0 FAIL | GO — enter at 75% planned size |
| 6-7 PASS, 2-3 CAUTION, 0 FAIL | CAUTIOUS GO — enter at 50%; add only on confirmation |
| Any FAIL (even 1) | NO-GO — do not enter; revisit when FAIL resolved |
| 2+ FAILs | STRONG NO-GO — remove from watchlist for now |

---

## Output Format

```
=== ENTRY CHECKSHEET — [TICKER] — [Date] ===

Setup: [Position / Swing / Catalyst]
Proposed Entry: ₹[price] | Stop: ₹[price] ([X]%) | Target: ₹[price] ([X]%)
R:R: 1:[X] | Planned Size: [X]% = ₹[amount]

CHECK 1  Market Context     [PASS/CAUTION/FAIL]
  Nifty vs 50 EMA: [Above/Below]  |  India VIX: [X]  |  Major event 48h: [Y/N]
  → [1-line finding]

CHECK 2  Sector Strength    [PASS/CAUTION/FAIL]
  Sector vs Nifty (10d): [Out/In-line/Under]  |  Macro tailwind: [Y/N]

CHECK 3  Primary Trend      [PASS/CAUTION/FAIL]
  Above 200 EMA: [Y/N]  |  Above 50 EMA: [Y/N]  |  HH/HL: [Y/N]

CHECK 4  Entry Trigger      [PASS/CAUTION/FAIL]
  Trigger type: [Breakout/Support bounce/NR7/Catalyst/Post-results]

CHECK 5  Risk-Reward        [PASS/CAUTION/FAIL]
  R:R ratio: 1:[X]

CHECK 6  Position Sizing    [PASS/CAUTION/FAIL]
  Risk: ₹[amount] = [X]%  |  Conviction tier max: [X]%

CHECK 7  Fundamental        [PASS/CAUTION/FAIL]
  D/E: [X]  |  Pledge: [X]%  |  Promoter: [X]%  |  CFO/PAT: [X]

CHECK 8  Volume             [PASS/CAUTION/FAIL]
  Volume vs 20d avg: [X]x  |  Delivery: [X]%  |  OI buildup: [Y/N/NA]

CHECK 9  Catalyst           [PASS/CAUTION/FAIL]
  Catalyst: [Known verifiable / Technical / Rumor / None]

CHECK 10 Timing             [PASS/CAUTION/FAIL]
  Results week: [Y/N]  |  F&O expiry: [Y/N]  |  FOMO entry: [Y/N]

---
RESULTS: [X] PASS  |  [X] CAUTION  |  [X] FAIL
VERDICT: [STRONG GO / GO / CAUTIOUS GO / NO-GO / STRONG NO-GO]

Entry size: [X]% of portfolio (₹[amount])
Entry price: ₹[price] | Stop: ₹[price] | First target: ₹[price] | Final target: ₹[price]

If NO-GO — what must change to become GO:
  1. [Specific condition]
  2. [Specific condition]
```
