import pandas as pd
from domain_checker import check_domain
from brand_score import score_brand
from brand_value import estimate_brand_value
from concurrent.futures import names_to_dataframe
def process_name(name):
    result = check_domain(name.lower() + ".com")
    domain = "✅" if result["status"] == "Available" else "❌"

    brand = score_brand(name)

    min_value, max_value = estimate_brand_value(
        name, brand["score"], domain == "✅"
    )

    return {
        "Brand": name,
        ".com": domain,
        "Score": brand["score"],
        "Stars": brand["stars"],
        "Value": f"${min_value:,} - ${max_value:,}",
    }


def names_to_dataframe(names):
    with ThreadPoolExecutor(max_workers=10) as executor:
        return list(executor.map(process_name, names))
