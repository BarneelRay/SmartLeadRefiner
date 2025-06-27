# Smart Lead Refiner – Rationale

This project was developed as a rapid demo solution for Caprae Capital’s AI-Readiness Challenge. The core objective was to build a lightweight, modular lead refinement tool capable of:

- Ingesting basic company data (via domain names)
- Enriching and scoring leads based on funding, team size, and industry relevance
- Auto-generating personalized cold email templates for outreach
- Exporting structured outputs (CSV/email text) for practical use

### Key Decisions:
- **Mock API simulation** using a local JSON store to avoid Clearbit API quotas
- **Simple scoring logic** using interpretable rules instead of ML models for transparency
- **Template-based emails** to simulate outreach without using external APIs
- **Colab compatibility** for easy demonstration and reproducibility

This approach balances feasibility, clarity, and speed — ideal for both MVP-style outreach tools and portfolio company enrichment workflows.