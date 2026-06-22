---
name: zerodha-kite
description: "Route natural-language trading/account queries to the correct zerodha CLI command. Supports viewing holdings, placing orders, checking margins, and managing GTT/Mutual Funds."
version: 1.0.1
author: jatinbansal1998
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [trading, zerodha, kite, finance]
    category: trading
---

# Zerodha Kite Connect CLI

Translate a user query in plain English into one exact `zerodha` CLI command. Use this skill when executing transactions, reading positions, or checking margins on Zerodha.

## Setup

Place these credentials in your local `~/.hermes/.env` file:
- `KITE_API_KEY`
- `KITE_API_SECRET`
- `KITE_USER_ID`

Profile selection:
- Most commands require an active profile. If no active profile is set, run:
  `zerodha config profile use default`

## Command Catalog

### Profile & Margins
- `zerodha profile show` — View your account details
- `zerodha margins` — Check your available funds and segment margins

### Quotes & Market Data
- `zerodha quote get <EXCHANGE:SYMBOL>` — Get detailed live quote (e.g. `NSE:TATAMOTORS`)
- `zerodha quote ltp <EXCHANGE:SYMBOL>` — Get Last Traded Price (LTP)
- `zerodha quote historical --instrument-token <int> --interval <val> --from YYYY-MM-DD --to YYYY-MM-DD`

### Orders & Portfolio
- `zerodha order place --exchange <EX> --symbol <SYM> --txn <BUY|SELL> --type <MARKET|LIMIT> --product <CNC|MIS> --qty <qty> [--price <p>]`
- `zerodha order cancel --order-id <id>`
- `zerodha orders list` — See orderbook
- `zerodha holdings` — See demat portfolio holdings
- `zerodha positions` — See active net positions

### GTT (Good Till Triggered)
- `zerodha gtt place --exchange <EX> --symbol <SYM> --last-price <p> --txn BUY --trigger <trigger_price> --limit-price <limit_price> --qty <qty>`
- `zerodha gtt list`
- `zerodha gtt delete --trigger-id <id>`

## Synonym Map

- `my portfolio` -> `zerodha holdings`
- `net positions` -> `zerodha positions`
- `available funds` -> `zerodha margins`
- `buy TCS` -> `zerodha order place --exchange NSE --symbol TCS --txn BUY ...`
