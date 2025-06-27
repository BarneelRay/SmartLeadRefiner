from app.scraper import scrape_via_clearbit
from app.lead_scorer import score_lead
from app.email_generator import generate_email
import pandas as pd

# Step 1: Provide your API Key and domains
api_key = "sk_your_clearbit_key_here"
domains = ["openai.com", "notion.so", "zapier.com"]

# Step 2: Enrich data
df = scrape_via_clearbit(domains, api_key)

# Step 3: Score leads
df["Score"] = df.apply(score_lead, axis=1)

# Step 4: Add pain points + generate emails
pain_point_map = {
    "AI Research": "scaling AI model deployment and compliance",
    "Productivity Software": "managing cross-functional remote teams",
    "Automation SaaS": "workflow fragmentation and integration bottlenecks"
}

def get_pain_point(industry):
    return pain_point_map.get(industry, "growth challenges in tech sectors")

df["Pain Point"] = df["Industry"].apply(get_pain_point)
df["Email"] = df.apply(lambda row: generate_email(row["Company Name"], row["Industry"], row["Pain Point"]), axis=1)

# Step 5: Sort + Save
sorted_df = df.sort_values("Score", ascending=False)
sorted_df.to_csv("data/leads_scored.csv", index=False)

print("\n--- Pipeline Complete: Top Leads ---\n")
print(sorted_df[["Company Name", "Score"]])
print(sorted_df)