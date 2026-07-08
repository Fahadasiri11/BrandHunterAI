import pandas as pd
from domain_checker import check_domain
from brand_score import score_brand

def names_to_dataframe(names):
    data = []

    for name in names:

        result = check_domain(name.lower() + ".com")

        domain = "✅" if result["status"] == "Available" else "❌"

        score = score_brand(name)["score"]

     data.append({
    "Brand": name,
    ".com": domain,
    "Score": score,
    "Stars": score_brand(name)["stars"],
    "Value": f"${score * 100:,}"
})   
    return data
