import requests
from datetime import datetime, UTC
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
API_KEY = os.getenv("VULNERS_API_KEY")

# Today's Date
today = datetime.now(UTC).strftime("%Y-%m-%d")
print("\n\n📆Today's Date:", today)
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Vulners Python Client",
    "X-Api-Key": API_KEY
}

query = {
    "query": f"type:cve AND published:[{today} TO {today}]",
    "size": 100
}

response = requests.post("https://vulners.com/api/v3/search/lucene/", headers=headers, json=query)
data = response.json()

# Prepare the file
with open("today_cves.txt", "w", encoding="utf-8") as f:
    if data.get("result") == "OK" and data["data"]["search"]:
        for vuln in data["data"]["search"]:
            if vuln.get("_source", {}).get("type") != "cve":
                continue

            source = vuln["_source"]
            cve_id = source.get("id", "N/A")
            desc = source.get("description", "No Description").replace("\n", " ").strip()
            desc = desc[:300]  # Truncate if too long

            f.write(f"{cve_id}: {desc}\n")

        print("\n✅ CVE data written to today_cves.txt\n\n")
    else:
        f.write("No new CVEs today.\n")
        print("✨ No new CVEs found for today.")
