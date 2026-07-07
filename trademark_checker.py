from rapidfuzz import fuzz

KNOWN_BRANDS = [
    "google",
    "openai",
    "apple",
    "microsoft",
    "tesla",
    "amazon",
    "meta",
    "netflix",
    "samsung",
    "nike",
    "adidas"
]

def check_trademark(name):
    name = name.lower()

    best_score = 0
    best_match = None

    for brand in KNOWN_BRANDS:
        score = fuzz.ratio(name, brand)

        if score > best_score:
            best_score = score
            best_match = brand

    if best_score >= 90:
        risk = "مرتفع جداً"
    elif best_score >= 70:
        risk = "متوسط"
    else:
        risk = "منخفض"

    return {
        "closest": best_match,
        "score": best_score,
        "risk": risk
    }
