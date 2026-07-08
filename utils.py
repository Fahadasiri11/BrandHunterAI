import pandas as pd
from domain_checker import check_domain
from brand_score import score_brand
from brand_value import estimate_brand_value

def names_to_dataframe(names):
    data = []

    for name in names:

        result = check_domain(name.lower() + ".com")

        domain = "✅" if result["status"] == "Available" else "❌"

        brand = score_brand(name)

        domain_available = (domain == "✅")

        min_value, max_value = estimate_brand_value(
            name,
            brand["score"],
            domain_available
        )

        data.append({
            "Brand": name,
            ".com": domain,
            "Score": brand["score"],
            "Stars": brand["stars"],
            "Value": f"${min_value:,} - ${max_value:,}"
        })

    return data
