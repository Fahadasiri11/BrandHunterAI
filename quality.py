def analyze_quality(name):
    score = 100

    if len(name) > 10:
        score -= 15

    vowels = sum(c in "aeiou" for c in name.lower())

    pronounce = "✅" if vowels >= 2 else "⚠️"

    memorable = "✅" if len(name) <= 8 else "⚠️"

    global_name = "🌍" if len(name) <= 10 else "⚠️"

    trend = "🔥" if any(
        x in name.lower()
        for x in ["ai", "neo", "nova", "sync", "flow", "cloud", "gen"]
    ) else "⭐"

    premium = "💎" if (
        score >= 90
        and len(name) <= 8
        and pronounce == "✅"
    ) else "⭐"

    startup = "🚀" if (
        score >= 85
        and memorable == "✅"
        and pronounce == "✅"
    ) else ""

    brandability = "A+"

    if score < 90:
        brandability = "A"

    if score < 80:
        brandability = "B"

    if score < 70:
        brandability = "C"

    return {
        "Global": global_name,
        "Pronounce": pronounce,
        "Memorability": memorable,
        "Trend": trend,
        "Premium": premium,
        "Startup": startup,
        "Brandability": brandability,
    }
