import pandas as pd
from domain_checker import check_domain

print("NEW UTILS LOADED")

def names_to_dataframe(names):
    data = []

    for name in names:

        result = check_domain(name.lower() + ".com")

        if result["status"] == "Available":
            domain = "✅"
        else:
            domain = "❌"

        data.append({
            "Brand": name,
            ".com": domain
        })

    return pd.DataFrame(data)
