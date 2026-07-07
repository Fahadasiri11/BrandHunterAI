from rapidfuzz import process, fuzz

# قاعدة بيانات مبدئية
TRADEMARKS = [
    "google",
    "apple",
    "microsoft",
    "tesla",
    "amazon",
    "meta",
    "nike",
    "adidas",
    "samsung",
    "sony",
    "openai",
    "netflix",
    "spotify",
    "intel",
    "nvidia",
    "coca cola",
    "pepsi",
    "toyota",
    "bmw",
    "mercedes"
]

def check_trademark(name):
    result = process.extract(
        name.lower(),
        TRADEMARKS,
        scorer=fuzz.WRatio,
        limit=5
    )

    return [
        {
            "name": r[0],
            "score": round(r[1], 1)
        }
        for r in result
    ]
