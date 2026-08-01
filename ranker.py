def rank_brands(results):
    return sorted(
        results,
        key=lambda x: (
            x[".com"] == "✅",
            x["Short"] == "✅",
            x["Score"],
        ),
        reverse=True,
    )
