def analyze_quality(name):
    score = 100

    if len(name) > 10:
        score -= 15

    vowels = sum(c in "aeiou" for c in name.lower())
    pronounce = "✅" if vowels >= 2 else "⚠️"

    memorable = "✅" if len(name) <= 8 else "⚠️"

    premium = "💎" if score >= 90 else "⭐"

    startup = "🚀" if score >= 85 else ""

    global_name = "🌍"

    trend = "🔥"

    return {
        "Global": global_name,
        "Pronounce": pronounce,
        "Memorability": memorable,
        "Trend": trend,
        "Premium": premium,
        "Startup": startup,
    }
