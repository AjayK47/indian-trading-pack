---
name: indian-trading-pack
description: "All-in-one Indian Stock Trading Suite. Supports automated research, risk checklist scanners, portfolio monitors, and secure live trading on Groww or Zerodha Kite."
version: 1.0.0
author: Ajay
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [trading, finance, zerodha, groww, nse, bse, automation]
    category: trading
---

# Indian Trading Pack

An elite, modular AI Stock-Trading Desk designed for Indian retail traders. This plugin bundles 10 unified skills to scout, check, validate, execute, and monitor NSE/BSE mid and small-cap momentum positions.

## 🌟 Capabilities

1. **Broker Integration**: Trade securely with **Groww** (`growwapi`) or **Zerodha Kite** (`kiteconnect`).
2. **Execution Modes**:
   - 🛡️ **Research Only**: Scouting, scanner lists, 5-point fundamentals, and risk assessments with no real capital risk.
   - 🤝 **Copilot Mode**: Full analysis, checksheets, and pre-drafted orders waiting for your explicit `/approve` command.
   - ⚡ **Fully Autonomous**: Systematic position building governed by custom budgets and sizing parameters.
3. **Advanced Risk-Assessment**: Mandatory entry checks and Thesis Builders before executions.

---

## 🤖 Agent Guide: Conversational Onboarding (How to Setup)

When a user asks you to "setup the trading pack", "onboard me", or "configure my stock broker", **do NOT tell them to run script commands in their terminal.** 

Instead, you (the Hermes Agent) must guide the user through a secure, conversational setup directly in the chat. Follow these steps:

### 1. Present Choices Clearly
Ask the user to specify:
- **Broker**: Groww or Zerodha Kite.
- **Mode**: 
  - `Research`: Read-only, no real-money trading.
  - `Copilot`: Alerts you with pre-drafted slips, waits for your `/approve`.
  - `Autonomous`: Automated trading within custom budget limits.

### 2. Gather Risk Parameters (If Copilot or Autonomous)
Ask the user to define their risk boundaries:
- Maximum budget allowed *per trade* in INR (e.g., ₹5,000).
- Absolute maximum daily capital exposure cap in INR (e.g., ₹25,000).

### 3. Ask for API Credentials
Prompt the user to enter their credentials securely inside the chat. Reassure them that these keys will be saved *only on their local machine's directory* (`~/.hermes/.env`) and will never leave their computer.
- **For Groww**: `GROWW_API_KEY`, `GROWW_API_SECRET`, and `GROWW_TOTP_SECRET` (optional).
- **For Zerodha**: `KITE_API_KEY`, `KITE_API_SECRET`, `KITE_USER_ID`, and `KITE_TOTP_SECRET` (optional).

### 4. Persist the Setup Locally
Once the user provides the inputs, perform the following two operations using your file/terminal tools:

#### A. Write credentials to `~/.hermes/.env` (append without breaking existing values)
```env
# Managed by Indian Trading Pack
GROWW_API_KEY="user_supplied_key"
GROWW_API_SECRET="user_supplied_secret"
GROWW_TOTP_SECRET="user_supplied_seed"
```

#### B. Write the configuration profile to `~/.hermes/trading_config.json`
```json
{
  "broker": "groww", // or "zerodha_kite"
  "mode": "Copilot", // Research, Copilot, or Autonomous
  "max_cap_per_trade": 5000.00,
  "max_cap_daily": 25000.00
}
```

### 5. Finalize & Print Success
Tell the user that their setup is finished and complete, and let them know their stock trading desk is ready to run.
