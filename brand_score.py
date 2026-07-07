def score_brand(name):
    score = 100
    reasons = []

    # الطول
    if len(name) > 12:
        score -= 15
        reasons.append("الاسم طويل")
    else:
        reasons.append("اسم قصير")

    # الأرقام
    if any(c.isdigit() for c in name):
        score -= 20
        reasons.append("يحتوي على أرقام")

    # الشرطة
    if "-" in name or "_" in name:
        score -= 15
        reasons.append("يحتوي على رموز")

    # سهولة النطق
    vowels = "aeiou"

    vowel_count = sum(1 for c in name.lower() if c in vowels)

    if vowel_count < 2:
        score -= 10
        reasons.append("صعب النطق")
    else:
        reasons.append("سهل النطق")

    # البداية بحرف كبير (للشكل فقط)
    reasons.append("مناسب كعلامة تجارية")

    if score >= 90:
        stars = "⭐⭐⭐⭐⭐"
    elif score >= 75:
        stars = "⭐⭐⭐⭐"
    elif score >= 60:
        stars = "⭐⭐⭐"
    elif score >= 40:
        stars = "⭐⭐"
    else:
        stars = "⭐"

    return {
        "score": score,
        "stars": stars,
        "reasons": reasons
    }
