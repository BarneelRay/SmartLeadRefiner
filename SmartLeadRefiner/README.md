# Smart Lead Refiner 🚀

A lightweight, AI-inspired lead generation and outreach refinement tool — built in under 3 hours for the Caprae Capital AI-Readiness Challenge.

## 🔧 Features

- 🧠 Enrich company data from a list of domains (via Clearbit or mock)
- 📊 Score leads using funding, team size, and AI/tech relevance
- ✉️ Generate custom cold email templates for outreach
- 📁 Export everything into a clean CSV report

---

## 📦 Project Structure

```
SmartLeadRefiner/
├── app/                    # Core modules
│   ├── scraper.py
│   ├── lead_scorer.py
│   └── email_generator.py
├── data/
│   ├── mock_company_data.json
│   └── leads_scored.csv
├── report/
│   └── rationale.md
├── SmartLeadRefiner.ipynb  # Notebook demo version
├── main_pipeline.py        # Run full process as script
├── requirements.txt
└── README.md
```

---

## 🚀 Quickstart (Mock Mode)

```bash
# Set up environment
pip install -r requirements.txt

# Run with mock data
export USE_MOCK_DATA=1
python main_pipeline.py
```

---

## 📝 Notes

- You can swap mock enrichment with live Clearbit by changing the `USE_MOCK_DATA` flag and adding your API key.
- Output CSV includes lead scores and personalized emails, ready for campaign use.

---

Built by Barneel Ray ⚡ | Robotics + AI + Hustle