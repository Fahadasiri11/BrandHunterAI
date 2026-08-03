from brand_type import detect_brand_type
import pandas as pd
from domain_checker import check_domain
from brand_score import score_brand
from brand_value import estimate_brand_value
from concurrent.futures import ThreadPoolExecutor
from quality import analyze_quality

def process_name(name, industry):
    quality = analyze_quality(name)
    result = check_domain(name.lower() + ".com")
    domain = "✅" if result["status"] == "Available" else "❌"

    brand = score_brand(name)

    min_value, max_value = estimate_brand_value(
        name,
        brand["score"],
        domain == "✅"
    )

    is_short = "✅" if len(name) <= 8 else "❌"
    brand_type = detect_brand_type(industry)
    quality = analyze_quality(name)
    if brand["score"] >= 90 and domain == "✅":
        risk = "🟢 منخفض"
    elif brand["score"] >= 75:
        risk = "🟡 متوسط"
    else:
        risk = "🔴 مرتفع"

    ai_pick = "⭐" if (
        domain == "✅"
        and brand["score"] >= 90
        and len(name) <= 8
    ) else ""

    print(quality)
    return {
    "AI Pick": ai_pick,
    "Brand": name,
    "Brand Type": brand_type,
    "Global": quality["Global"],
    "Pronounce": quality["Pronounce"],
    "Memorability": quality["Memorability"],
    "Trend": quality["Trend"],
    "Premium": quality["Premium"],
    "Startup": quality["Startup"],
    "Brandability": quality["Brandability"],

    ".com": domain,
    "Short": is_short,
    "Score": brand["score"],
    "Risk": risk,
    "Stars": brand["stars"],
    "Value": f"${min_value:,} - ${max_value:,}",
    }


def names_to_dataframe(names, industry):
    with ThreadPoolExecutor(max_workers=10) as executor:
        return list(executor.map(lambda n: process_name(n, industry), names))
