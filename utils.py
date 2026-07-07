import pandas as pd

def names_to_dataframe(names):
    data = []

    for name in names:
        data.append({
            "Brand": name,
            ".com": "⏳",
            ".ai": "⏳",
            "Risk": "-"
        })

    return pd.DataFrame(data)
