def rank_brands(results):
    """
    ترتيب الأسماء من الأفضل إلى الأقل جودة.
    """

    return sorted(
        results,
        key=lambda x: (
            x["Score"],
            x[".com"] == "✅"
        ),
        reverse=True
    )
