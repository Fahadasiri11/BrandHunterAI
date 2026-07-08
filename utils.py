import pandas as pd
from domain_checker import check_domain
from brand_score import score_brand

def names_to_dataframe(names):
    data = []

    for name in names:

        result = check_domain(name.lower() + ".com")

        domain = "✅" if result["status"] == "Available" else "❌"

        brand = score_brand(name)

        data.append({
            "Brand": name,
            ".com": domain,
            "Score": brand["score"],
            "Stars": brand["stars"],
            "Value": f"${brand['score'] * 100:,}"
        })

    return data
