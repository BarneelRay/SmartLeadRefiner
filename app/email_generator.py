def generate_email(company_name, industry, pain_point, contact_name="there"):
    email_template = f"""
    Hi {contact_name},

    I came across {company_name} and was really impressed by your work in the {industry} space.

    I've worked with a number of growing companies facing similar challenges around {pain_point}. Based on what I've seen, I believe there's real potential to optimize operations and accelerate growth with a bit of smart tooling.

    Would love to share a few ideas — totally no pressure. Let me know if a quick 15-minute chat next week works for you.

    Best,
    Barneel Ray
    AI & Automation Enthusiast | Robotics Engineer
    """
    return email_template.strip()

# Example:
if __name__ == "__main__":
    print(generate_email("Notion", "Productivity Software", "managing cross-functional remote teams", "Akshay"))
