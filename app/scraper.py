# smart_lead_refiner/app/scraper.py

import requests
import pandas as pd
import os
import json

# Load mock data from JSON file
MOCK_FILE = "data/mock_company_data.json"

def load_mock_data():
    with open(MOCK_FILE, "r") as file:
        return json.load(file)

# Clearbit or mock enrichment function
def enrich_company(domain, api_key):
    if os.environ.get("USE_MOCK_DATA") == "1":
        mock_db = load_mock_data()
        return mock_db.get(domain, None)

    url = f"https://company.clearbit.com/v2/companies/find?domain={domain}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# Wrapper to build DataFrame from list of domains
def scrape_via_clearbit(domains, api_key="mock"):
    data = []
    for domain in domains:
        company = enrich_company(domain, api_key)
        if company:
            data.append({
                "Company Name": company.get("name"),
                "Website": company.get("domain"),
                "Industry": company.get("category", {}).get("industry", "N/A"),
                "Team Size": company.get("metrics", {}).get("employees", "N/A"),
                "Funding": company.get("metrics", {}).get("raised", "N/A"),
                "Location": company.get("location", "N/A")
            })
    return pd.DataFrame(data)

# Example usage:
if __name__ == "__main__":
    os.environ["USE_MOCK_DATA"] = "1"
    domains = ["openai.com", "notion.so", "zapier.com", "loom.com", "figma.com"]
    df = scrape_via_clearbit(domains)
    print(df)