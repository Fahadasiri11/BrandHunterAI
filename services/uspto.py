from search_engine import SearchEngine

engine = SearchEngine()

def search_uspto(brand_name):
    """
    بحث مؤقت - سيتم استبداله بالبحث الحقيقي لاحقًا.
    """

    return {
        "source": "USPTO",
        "success": True,
        "query": brand_name,
        "results": [],
        "message": "لا توجد نتائج حالياً."
    }
