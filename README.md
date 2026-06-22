# 🇮🇳 Indian Trading Pack for Hermes

An elite, modular algorithmic stock-trading desk designed for Indian retail traders. This plugin bundles **11 unified skills** to seamlessly scout, check, validate, execute, and monitor NSE/BSE mid and small-cap momentum positions.

---

## 🌟 Key Capabilities

1. **Broker-Agnostic Core**: Trade securely on **Groww** (utilizing `growwapi`) or **Zerodha Kite** (utilizing `kiteconnect`).
2. **Three Operational Modes**:
   - 🛡️ **Research Only (Read-Only)**: Automatically scouts momentum candidates, prints 5-point fundamental scores, and creates reports without capital risk.
   - 🤝 **Copilot Mode**: Prepares order tickets and alerts you in private chat. Submitting the order to market waits for your explicit `/approve` command.
   - ⚡ **Autonomous Mode**: Allows the agent to trade systematically within strict, user-established per-trade and daily budgets.
3. **Multi-Agent Coordination**: Bundles 11 specialized skills that act like an institutional trading desk.

---

## 📂 Bundled Skills (11 Total)

When you download this trading pack, Hermes instantly registers these 11 skills to your profile:
- `trading-expert` — The master coordinator.
- `candidate-finder` — Momentum & technical scanners.
- `market-news-scanner` — News sentiment & catalyst scouts.
- `social-rumor-detector` — Informal social/retail discussion scanners.
- `correlation-engine` — Sector rotation & indices analyzers.
- `fundamental-quick-read` — Instant 5-point balance-sheet validators.
- `entry-checksheet` — Rigid pre-trade Gatekeeper.
- `thesis-builder` — Builds full 7-layer investment reports.
- `position-monitor` — Tracks active targets & trailing stops.
- `groww` — Groww execution connector. (Source: [pushp1997/groww](https://clawhub.ai/pushp1997/groww))
- `zerodha-kite` — Zerodha Kite execution connector. (Source: [jatinbansal1998/zerodha-kite](https://clawhub.ai/jatinbansal1998/zerodha-kite))

---

## 🚀 Getting Started (Installation)

### 1. Register the Repository Source
Add this repo to your local Hermes installation as a trusted skill source:
```bash
hermes skills tap add ajay/indian-trading-pack
```

### 2. Download and Install the Suite
Download all 11 synchronized trading tools into your profile directory with one command:
```bash
hermes skills install indian-trading-pack
```

### 3. Setup and Conversational Onboarding
Once installed, you don't need to run complex scripts. You can simply open your Hermes session and say:
> *"set up my indian stock trading pack"*

Hermes will conversationally guide you through:
1. Choosing your operational broker (Zerodha or Groww).
2. Selecting your mode (Research, Copilot, or Autonomous).
3. Defining your maximum investment per trade and daily budget caps (e.g., ₹5,000 max per trade).
4. Securely pasting your API credentials (saved *only locally* under `~/.hermes/.env`).

*Alternatively, you can run the terminal-level wizard script:*
```bash
python3 ~/.hermes/skills/trading/indian-trading-pack/trading_setup.py
```

---

## 🔒 Security & Privacy (Local-First Design)
- **Zero Cloud transmission**: Your keys, secrets, and trade budgets are written strictly to your local computer's memory (`~/.hermes/.env` and `~/.hermes/trading_config.json`).
- **Workspace Isolation**: Your transaction data, shortlisted targets, and investment reports are saved directly to your local computer's workspace directory (`~/Documents/ajay/trading_workspace/`) and are never committed to git logs or repositories.

---

## ⚖️ Legal & Financial Notice (Disclaimer)
This repository is strictly a technical integration client provided for educational and testing purposes. The authors and contributors are **NOT** SEBI-registered financial advisers. Algorithmic trading carries high capital risks. By downloading or running this software, you take full liability for any financial losses or actions taken. 

For the complete legal terms, constraints, and liability disclosures, please refer to the [DISCLAIMER.md](./DISCLAIMER.md) document in this repository. All users must read and agree to the terms in the disclaimer before utilizing this pack.
