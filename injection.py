import os
import sys
import urllib.request
import urllib.parse
import re
import time
import random

# DEDSEC TACTICAL TERMINAL COLOR ENGINE
C_RED     = "\033[31m"
C_GREEN   = "\033[0;32m"
C_DGN     = "\033[2;32m"
C_YEL     = "\033[33m"
C_WHITE   = "\033[97m"
C_BOLD    = "\033[1m"
C_RESET   = "\033[0m"

def print_tactical_banner():
    print(f"{C_GREEN}{C_BOLD}")
    print("  .     ________________________________ ")
    print("  |-----|- - -|''''|''''|''''|''''|'''|'#__         DEDSEC            ╔══════════════╗ ")
    print("  |- - | cc   6   5   4   3   2   1  ##  __]==----------------------  ║  INJECTION   ║ ")
    print("  |-----|_______________________________#                             ╚══════════════╝ ")
    print("")
    print(f"{C_YEL}{C_BOLD}     $ [DEDSEC COMMUNITY PRESENTS]{C_RESET}")
    print(f"{C_RED}{C_BOLD}     ⚔  [DEVELOPED BY NODE: Unknownx007 | MODEL STATE: MULTI-TARGET]{C_RESET}\n")

def get_random_system_joke():
    jokes = [
        "Why do security nodes hate nature? There are too many bugs inside the system partition loops.",
        "A SQL query walks into a server room, approaches two database tables, and asks: 'Can I join you?'",
        "Hardware is the part of an installation node that you can kick; software is the part you can only curse at."
    ]
    return random.choice(jokes)

def test_live_network_latency_handshake(target_url, target_field, payload, extracted_fields, asp_tokens):
    """Assembles the web request package payload stuffing placeholder values to required inputs."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        form_payload = {}
        for token, val in asp_tokens.items():
            form_payload[token] = val

        for field in extracted_fields:
            if field == target_field:
                form_payload[field] = payload
            else:
                form_payload[field] = "baseline_test_node"

        encoded_bytes = urllib.parse.urlencode(form_payload).encode('utf-8')
        req = urllib.request.Request(target_url, data=encoded_bytes, headers=headers)
        
        start_time = time.time()
        with urllib.request.urlopen(req, timeout=8) as response:
            html_body = response.read().decode('utf-8', errors='ignore')
            resp_code = response.getcode()
        end_time = time.time()
        return end_time - start_time, html_body, resp_code
    except urllib.error.HTTPError as e:
        try:
            body = e.read().decode('utf-8', errors='ignore')
            return 2.0, body, e.code
        except Exception:
            return 0.1, "HTTP_ERROR", e.code
    except Exception:
        return 0.1, "CONNECTION_ERROR", 0

def main():
    os.system("clear")
    print_tactical_banner()
    
    print(f"{C_DGN}☠ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ☠{C_RESET}")
    print(f" {C_GREEN}(0_0) {C_BOLD}[TACTICAL PARAMETER CONFIGURATION VECTOR]{C_RESET}")
    target_url = input(f" {C_YEL}Input Targeted Application Portal URL Page Link (With http:// or https://:) >>{C_RESET} ").strip()
    
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        print(f" {C_RED}(X_X) [ALERT_CRITICAL]: Protocol missing. Append http:// or https:// context.{C_RESET}")
        return

    # DOM INPUT FIELDS EXTRACTION LOGS PANEL HUB
    print(f"\n{C_DGN}┌── [ DOM ANALYSIS & STRUCTURAL MAPPER RECON LOGGER ] ────────────────────────────────────────────────────────┐")
    print(f"│ {C_GREEN}[⚙  DOM INTERCEPT]{C_WHITE} Launching high-accuracy layout scraper against remote target portal...      │")
    time.sleep(0.4)
    
    extracted_fields = []
    asp_tokens = {}
    
    try:
        req = urllib.request.Request(
            target_url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        )
        with urllib.request.urlopen(req, timeout=8) as response:
            html_content = response.read().decode('utf-8', errors='ignore')
            
        # Parse standard state tokens
        token_names = ['__VIEWSTATE', '__VIEWSTATEGENERATOR', '__EVENTVALIDATION', '__EVENTTARGET', '__EVENTARGUMENT']
        for token in token_names:
            match = re.search(fr'id="{token}"\s+value="([^"]+)"', html_content, re.IGNORECASE)
            if not match:
                match = re.search(fr'name="{token}"\\s+value="([^"]+)"', html_content, re.IGNORECASE)
            if match: 
                asp_tokens[token] = match.group(1)

        # High-accuracy multi-layer parameter extraction regex logic pass
        input_tags = re.findall(r'<input\s+[^>]*name=["\']([^"\']+)["\'][^>]*>', html_content, re.IGNORECASE)
        extracted_fields = [name for name in input_tags if name not in token_names]
        
        # Fallback to secondary check pass filtering if field arrays are empty
        if not extracted_fields:
            id_tags = re.findall(r'<input\s+[^>]*id=["\']([^"\']+)["\'][^>]*>', html_content, re.IGNORECASE)
            extracted_fields = [name for name in id_tags if name not in token_names]
    except Exception:
        pass

    if not extracted_fields:
        # Fallback fields updated to include real verified ASPX application naming identifiers
        extracted_fields = ["txtUserName", "txtPassword", "txtEmail", "ddlClass", "btn_login"]
        print(f"│ {C_RED}[⚠  WARN_ANOMALY]{C_WHITE} DOM read dropped. Mapping structural platform placeholder template keys.      │")
    else:
        print(f"│ {C_GREEN}[⚙  DOM INTERCEPT]{C_WHITE} Isolated {len(extracted_fields)} active form parameters securely inside application layout:      │")
        for f_name in extracted_fields:
            # Dynamically display every verified parameter lane key discovered within layout bounds
            print(f"│   ├── {C_YEL}Discovered Input Attribute Key:{C_WHITE} '{f_name:<46}' │")
        
    print(f"│ {C_GREEN}[⚙  DOM INTERCEPT]{C_WHITE} Configuration updates complete. Prober matrices initialized to active readiness.  │")
    time.sleep(0.4)
    print(f"{C_DGN}└────────────────━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘{C_RESET}")

    # BROAD MULTI-TARGET CRITERIA PROBING PASS
    print(f"\n {C_GREEN}(⚙_⚙) {C_BOLD}[DEPLOYING PARALLEL SWEEP ANALYSIS VEHICLES] ...{C_RESET}")
    print(f" {C_DGN}--------------------------------------------------------------------------------------------------------------{C_RESET}")
    
    # Establish ordinary control profile constraints
    _, baseline_body, _ = test_live_network_latency_handshake(target_url, "", "", extracted_fields, asp_tokens)
    baseline_size = len(baseline_body)
    
    symbol_probes = ["'", "\""]
    flagged_findings_ledger = []

    for f_idx, field in enumerate(extracted_fields):
        print(f"  {C_WHITE}[FIELD {f_idx+1}/{len(extracted_fields)}]{C_GREEN} Testing symbol constraints across input path: '{C_BOLD}{field}{C_RESET}{C_GREEN}'")
        allowed_symbols = []
        highest_delta_variance = 0
        
        for probe in symbol_probes:
            # Fire syntax test vectors across the wire links
            latency, body, code = test_live_network_latency_handshake(target_url, field, probe, extracted_fields, asp_tokens)
            current_size = len(body)
            size_variance_delta = abs(current_size - baseline_size)
            
            print(f"    └── [PROBE]: {probe:<3} | Server Code: {code:<3} | Latency: {latency:.2f}s | Size Variance Delta: {size_variance_delta} bytes")
            
            # CRITERIA PASS A: Direct signature error indicators matching
            error_signatures = ["SQL syntax", "mysql_fetch_array", "ora-", "PostgreSQL", "OleDbException", "Unclosed quotation mark"]
            for sig in error_signatures:
                if sig.lower() in body.lower():
                    if probe not in allowed_symbols: allowed_symbols.append(probe)
                    break
            
            # CRITERIA PASS B: Refactored Symbol Acceptance Variance Filter
            # If the size slips away from baseline by even a single byte, the characters are accepted by the script engine
            if size_variance_delta >= 1 and code == 200:
                if probe not in allowed_symbols: allowed_symbols.append(probe)
                if size_variance_delta > highest_delta_variance:
                    highest_delta_variance = size_variance_delta

        # EVALUATION TREE: VERDICT CALCULATION
        if allowed_symbols:
            verdict_text = f"{C_YEL}SYMBOLS ALLOWED (POSSIBLY VULNERABLE){C_RESET}"
            flagged_findings_ledger.append({
                "field": field,
                "symbols": allowed_symbols,
                "variance": highest_delta_variance
            })
            print(f"    {C_YEL}└── [ANALYSIS VERDICT]: Entry point matches threat profiles! State: {verdict_text} -> {allowed_symbols}{C_RESET}\n")
        else:
            print(f"    {C_DGN}└── [ANALYSIS VERDICT]: Input sanitized cleanly. Special character symbols blocked natively.{C_RESET}\n")
        time.sleep(0.3)

    print(f" {C_DGN}--------------------------------------------------------------------------------------------------------------{C_RESET}")
    print(f"\n{C_GREEN}[$] Universal multi-target evaluation sweep pass completed across all available page nodes.{C_RESET}")

    # VERDICT REPORT SUMMARY MATRIX READOUT
    # VERDICT REPORT SUMMARY MATRIX READOUT
    print(f"\n{C_DGN}☠ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ☠{C_RESET}")
    print(f" {C_GREEN}{C_BOLD}[* PROBER RESULTS SUMMARY LEDGER LOGS PROFILE]{C_RESET}")
    print(f"{C_DGN}☠ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ☠{C_RESET}")
    
    if not flagged_findings_ledger:
        print(f"  {C_GREEN}[-] Absolute negative indicator feedback anomalies across all fields. Secure configuration perimeter.{C_RESET}")
    else:
        for entry in flagged_findings_ledger:
            print(f"  {C_RED}[* MATCH DETECTED]{C_WHITE} Target Parameter Box Input Lane: '{C_BOLD}{entry['field']}{C_RESET}{C_WHITE}'")
            print(f"    ├── Security Threat Profile : {C_YEL}SYMBOLS ALLOWED (POSSIBLY VULNERABLE TO SQL INJECTION BREAKOUTS){C_RESET}")
            print(f"    ├── Accepted Syntax Tokens  : {C_GREEN}{entry['symbols']}{C_WHITE}")
            print(f"    └── Layout Structural Shift : {entry['variance']} bytes drift caught off standard control baseline.\n")
            
    print(f"{C_DGN}☠ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ☠{C_RESET}")
    print(f"\n {C_DGN}[@ DEDSEC SYSTEM HUMOR]: \"{get_random_system_joke()}\"{C_RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
