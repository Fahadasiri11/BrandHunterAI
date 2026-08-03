def analyze_quality(name):
    score = 100

    if len(name) > 10:
        score -= 15

    vowels = sum(c in "aeiou" for c in name.lower())

    pronounce = "✅" if vowels >= 2 else "⚠️"

    memorable = "✅" if len(name) <= 8 else "⚠️"

    global_name = "🌍" if len(name) <= 10 else "⚠️"

    trend_words = [
    "ai", "neo", "nova", "sync", "flow",
    "cloud", "gen", "labs", "verse",
    "core", "logic", "mind", "stack"
]

trend = "🔥" if any(
    x in name.lower() for x in trend_words
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

    if score >= 95:
    brandability = "A+"
    elif score >= 85:
    brandability = "A"
    elif score >= 75:
    brandability = "B"
    else:
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
