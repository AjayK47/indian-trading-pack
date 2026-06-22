---
name: groww
description: "Trade stocks and manage portfolio on Groww (Indian broker) securely. Uses local environment keys for authentication."
version: 1.0.0
author: pushp1997
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [trading, groww, nse, bse, finance]
    category: trading
---

# Groww Trading

Trade Indian stocks via Groww. Supports portfolio management, market data, and order execution.

## Setup

1. Get your API key from your Groww developer portal.
2. Put the credentials in your local `.env` or set them locally as environment variables:
   ```bash
   export GROWW_API_KEY="your-actual-api-key"
   ```

## Direct API Usage

You can query the Groww endpoint directly using curl with your environment key.

### Base URL
```
https://api.groww.in/v1/
```

### Endpoints

**Portfolio/Holdings:**
```bash
curl -H "Authorization: Bearer $GROWW_API_KEY" -H "Accept: application/json" \
  "https://api.groww.in/v1/holdings/user"
```

**Live Quote:**
```bash
curl -H "Authorization: Bearer $GROWW_API_KEY" -H "Accept: application/json" \
  "https://api.groww.in/v1/live-data/quote?exchange=NSE&segment=CASH&trading_symbol=TATAMOTORS"
```

**LTP (Last Traded Price):**
```bash
curl -H "Authorization: Bearer $GROWW_API_KEY" -H "Accept: application/json" \
  "https://api.groww.in/v1/live-data/ltp?segment=CASH&exchange_symbols=NSE:TATAMOTORS,NSE:RELIANCE"
```

**OHLC:**
```bash
curl -H "Authorization: Bearer $GROWW_API_KEY" -H "Accept: application/json" \
  "https://api.groww.in/v1/live-data/ohlc?segment=CASH&exchange_symbols=NSE:TATAMOTORS"
```

**Historical Candles:**
```bash
curl -H "Authorization: Bearer $GROWW_API_KEY" -H "Accept: application/json" \
  "https://api.groww.in/v1/historical/candle/range?exchange=NSE&segment=CASH&trading_symbol=TATAMOTORS&interval=5m&start_time=2024-06-01T09:15:00&end_time=2024-06-01T15:30:00"
```

**Place Order:**
```bash
curl -X POST -H "Authorization: Bearer $GROWW_API_KEY" \
  -H "Accept: application/json" -H "Content-Type: application/json" \
  -d '{"trading_symbol":"TATAMOTORS","quantity":10,"validity":"DAY","exchange":"NSE","segment":"CASH","product":"CNC","order_type":"MARKET","transaction_type":"BUY"}' \
  "https://api.groww.in/v1/order/create"
```

**Order Status:**
```bash
curl -H "Authorization: Bearer $GROWW_API_KEY" -H "Accept: application/json" \
  "https://api.groww.in/v1/order/detail/{groww_order_id}?segment=CASH"
```

**Cancel Order:**
```bash
curl -X POST -H "Authorization: Bearer $GROWW_API_KEY" \
  -H "Accept: application/json" -H "Content-Type: application/json" \
  -d '{"segment":"CASH","groww_order_id":"ABC123"}' \
  "https://api.groww.in/v1/order/cancel"
```

## Stock Symbols

Use NSE trading symbols:
- TATAMOTORS, RELIANCE, TCS, INFY, HDFCBANK, WIPRO, ICICIBANK, SBIN, BHARTIARTL, ITC

## Market Hours

- Pre-open: 9:00 - 9:15 AM IST
- Trading: 9:15 AM - 3:30 PM IST
- Monday to Friday (except holidays)

## Example Queries

- "Show my Groww portfolio"
- "What's TATAMOTORS price?"
- "Buy 10 RELIANCE shares"
- "Sell 5 TCS at limit 4200"
- "Cancel order ABC123"
- "Get historical data for INFY"
