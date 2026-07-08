def rank_brands(results):
    """
    ترتيب الأسماء من الأفضل إلى الأقل جودة.
    """

    return sorted(
        results,
        key=lambda x: (
            x["score"],
            x["domain"] == "✅"
        ),
        reverse=True
    )
