import os
import sys
import json
import re

# Simple ANSI terminal colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_banner():
    print(f"\n{CYAN}{BOLD}==================================================")
    print(f"       🇮🇳  INDIAN TRADING PACK FOR HERMES  🇮🇳")
    print(f"       Modular Onboarding & Config Wizard")
    print(f"=================================================={RESET}\n")

def print_legal_disclaimer():
    print(f"{RED}{BOLD}⚠️  CRITICAL FINANCIAL & LEGAL NOTICE{RESET}")
    print(f"{YELLOW}This trading pack executes transactions directly to your Indian Broker accounts.")
    print("Algotrading and automated order placing carries extreme capital risk, including")
    print("risks of duplicate trades, communication delay, or complete loss of funds.")
    print("")
    print("  1. The author is NOT a SEBI-registered broker, advisor, or portfolio manager.")
    print("  2. This code is purely for educational, technical, and testing purposes.")
    print("  3. Your API keys are saved raw, 100% LOCALLY on your computer.")
    print("  4. You assume 100% LIABILITY for any financial outcomes or losses incurred.")
    print(f"=================================================={RESET}")
    
    consent = ""
    while consent.lower() not in ["y", "yes"]:
        consent = input(f"\nDo you understand these terms and agree to proceed? (y/n): ").strip()
        if consent.lower() in ["n", "no"]:
            print(f"\n{RED}Onboarding aborted. You must agree to the terms to utilize live setups.{RESET}\n")
            sys.exit(0)

def get_hermes_env_path():
    return os.path.expanduser("~/.hermes/.env")

def get_trading_config_path():
    return os.path.expanduser("~/.hermes/trading_config.json")

def load_trading_config():
    path = get_trading_config_path()
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except:
            pass
    return {}

def save_trading_config(config):
    path = get_trading_config_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(config, f, indent=4)
    print(f"{GREEN}✓ Global Mode and Profile saved locally at {path}{RESET}\n")

def save_secrets_to_hermes_env(secrets):
    env_path = get_hermes_env_path()
    os.makedirs(os.path.dirname(env_path), exist_ok=True)
    
    current_lines = []
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            current_lines = f.readlines()
            
    env_dict = {}
    for line in current_lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            k = k.strip()
            v = v.strip().strip("'\"")
            env_dict[k] = v
            
    for k, v in secrets.items():
        env_dict[k] = v
        
    with open(env_path, "w") as f:
        f.write("# Hermes Agent Environment Secrets\n# Managed by Indian Trading Pack Wizard\n\n")
        for k, v in sorted(env_dict.items()):
            f.write(f"{k}=\"{v}\"\n")
            
    print(f"{GREEN}✓ Secure credentials written to {env_path}{RESET}\n")

def get_user_input(prompt, default=None):
    if default:
        full_prompt = f"{prompt} [{default}]: "
    else:
        full_prompt = f"{prompt}: "
    val = input(full_prompt).strip()
    if not val and default is not None:
        return default
    return val

def run_wizard():
    print_banner()
    print_legal_disclaimer()
    
    # 1. Broker Choice
    print(f"\n{BOLD}1. Select Your Stock Broker{RESET}")
    print("   [1] Groww (utilizes growwapi)")
    print("   [2] Zerodha Kite (utilizes kiteconnect SDK)")
    print("   [3] More Brokers Coming Soon!")
    
    broker_choice = ""
    while broker_choice not in ["1", "2"]:
        broker_choice = get_user_input("Choose an option (1-2)", "1")
        
    broker_name = "Groww" if broker_choice == "1" else "Zerodha Kite"
    print(f"\n{GREEN}Selected Broker: {broker_name}{RESET}\n")
    
    # 2. Select Operating Mode
    print(f"{BOLD}2. Select Operating Mode{RESET}")
    print(f"   {CYAN}[1] Research & Analyst (Read-Only Mode){RESET}")
    print("       Highly recommended for starters. Safe, identifies key opportunities,")
    print("       momentum candidates, and builds theses. Never places real-money trades.")
    print(f"   {CYAN}[2] Copilot (Interactive Mode){RESET}")
    print("       Runs all checksheets and prepares orders, but alerts you first and waits")
    print("       for you to run '/approve' to submit to your broker.")
    print(f"   {CYAN}[3] Fully Autonomous (Automated Executions){RESET}")
    print("       Enables systematic execution directly to markets governed by your risk")
    print("       allowances and budget per trade.")
    
    mode_choice = ""
    while mode_choice not in ["1", "2", "3"]:
        mode_choice = get_user_input("Choose operational mode (1-3)", "1")
        
    modes = {
        "1": "Research",
        "2": "Copilot",
        "3": "Autonomous"
    }
    selected_mode = modes[mode_choice]
    print(f"\n{GREEN}Selected Operational Mode: {selected_mode}{RESET}\n")
    
    budget_cap_per_trade = 0
    budget_cap_daily = 0
    
    if selected_mode in ["Copilot", "Autonomous"]:
        print(f"{BOLD}3. Set Trading Risk Boundaries{RESET}")
        cap_val = get_user_input("What is your maximum allowed budget *per trade* in INR?", "5000")
        try:
            budget_cap_per_trade = float(cap_val)
        except ValueError:
            budget_cap_per_trade = 5000.0
            
        daily_val = get_user_input("What is your absolute maximum daily exposure cap in INR?", "25000")
        try:
            budget_cap_daily = float(daily_val)
        except ValueError:
            budget_cap_daily = 25000.0
            
        print(f"\n{GREEN}Trading Caps Registered:{RESET}")
        print(f"   Per-trade limit: {YELLOW}₹{budget_cap_per_trade:.2f}{RESET}")
        print(f"   Daily limit: {YELLOW}₹{budget_cap_daily:.2f}{RESET}\n")
        
    # 3. Enter Broker Credentials
    print(f"{BOLD}4. Onboard Credentials{RESET}")
    secrets = {}
    
    if broker_choice == "1": # Groww
        print(f"Configure Groww credentials. Credentials will be written to local .env and are never shared.")
        api_key = get_user_input("Enter your Groww API Key")
        api_secret = get_user_input("Enter your Groww Client Secret")
        totp_secret = get_user_input("Enter your Groww TOTP Seed (Optional, for auto-token login)")
        
        secrets["GROWW_API_KEY"] = api_key
        secrets["GROWW_API_SECRET"] = api_secret
        if totp_secret:
            secrets["GROWW_TOTP_SECRET"] = totp_secret
            
    elif broker_choice == "2": # Zerodha Kite
        print(f"Configure Zerodha Kite credentials. Credentials will be written to local .env.")
        api_key = get_user_input("Enter your Kite API Key")
        api_secret = get_user_input("Enter your Kite API Secret")
        user_id = get_user_input("Enter your Zerodha Client User ID")
        totp_secret = get_user_input("Enter your Zerodha TOTP Seed (Optional, for instant non-prompt session)")
        
        secrets["KITE_API_KEY"] = api_key
        secrets["KITE_API_SECRET"] = api_secret
        secrets["KITE_USER_ID"] = user_id
        if totp_secret:
            secrets["KITE_TOTP_SECRET"] = totp_secret

    # Save details
    save_secrets_to_hermes_env(secrets)
    
    config = {
        "broker": "groww" if broker_choice == "1" else "zerodha_kite",
        "mode": selected_mode,
        "max_cap_per_trade": budget_cap_per_trade,
        "max_cap_daily": budget_cap_daily
    }
    save_trading_config(config)
    
    print(f"{GREEN}{BOLD}🎉 INDIAN TRADING PACK COMPLETED SUCCESSFULLY!{RESET}")
    print(f"Your Hermes Stock Trader is now ready to execute under '{selected_mode}' mode on {broker_name}.")
    print(f"Please restart your Hermes console session (/reset) to load the active context.\n")

if __name__ == "__main__":
    try:
        run_wizard()
    except KeyboardInterrupt:
        print(f"\n{RED}Wizard interrupted by user. Exiting safely.{RESET}")
        sys.exit(0)
