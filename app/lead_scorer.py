def score_lead(row):
    score = 0

    # Funding weight
    try:
        if isinstance(row["Funding"], str) and "$" in row["Funding"]:
            amount = float(row["Funding"].replace("$", "").replace("B", "e9").replace("M", "e6").replace("+", ""))
            score += amount / 1e8
        elif isinstance(row["Funding"], (int, float)):
            score += row["Funding"] / 1e8
    except:
        pass

    # Team size weight
    try:
        if isinstance(row["Team Size"], str):
            size = int(str(row["Team Size"]).split("-")[0].replace(">", ""))
            if size >= 1000:
                score += 10
            elif size >= 500:
                score += 8
            elif size >= 200:
                score += 6
        elif isinstance(row["Team Size"], (int, float)):
            size = row["Team Size"]
            if size >= 1000:
                score += 10
            elif size >= 500:
                score += 8
            elif size >= 200:
                score += 6
    except:
        pass

    # Industry relevance
    if isinstance(row["Industry"], str) and any(keyword in row["Industry"].lower() for keyword in ["ai", "automation", "software"]):
        score += 5

    return round(score, 2)

if __name__ == "__main__":
    from app.scraper import scrape_via_clearbit
    api_key = "sk_your_clearbit_key_here"
    df = scrape_via_clearbit(["openai.com", "notion.so"], api_key)
    df["Score"] = df.apply(score_lead, axis=1)
    print(df.sort_values("Score", ascending=False))