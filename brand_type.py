def detect_brand_type(industry):
    types = {
        "AI": "🤖 AI",
        "SaaS": "☁️ SaaS",
        "Cybersecurity": "🛡️ Security",
        "Finance": "💰 Finance",
        "Healthcare": "🏥 Healthcare",
    }

    return types.get(industry, "⭐ General")

    ai_words = [
        "ai", "mind", "brain", "bot", "gpt",
        "neuro", "smart", "vision", "intel"
    ]

    finance_words = [
        "pay", "bank", "cash", "coin",
        "fund", "capital", "money"
    ]

    health_words = [
        "med", "health", "care", "bio",
        "clinic", "pharma"
    ]

    security_words = [
        "secure", "shield", "guard",
        "lock", "cyber", "safe"
    ]

    saas_words = [
        "cloud", "stack", "flow",
        "hub", "sync", "app"
    ]

    if any(word in name for word in ai_words):
        return "🤖 AI"

    if any(word in name for word in finance_words):
        return "💰 Finance"

    if any(word in name for word in health_words):
        return "🏥 Healthcare"

    if any(word in name for word in security_words):
        return "🛡️ Security"

    if any(word in name for word in saas_words):
        return "☁️ SaaS"

    return "⭐ General"
