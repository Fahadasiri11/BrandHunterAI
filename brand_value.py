def estimate_brand_value(name, score, domain_available=True):
    value = 0

    # التقييم الأساسي
    value += score * 80

    # الاسم القصير أكثر قيمة
    if len(name) <= 6:
        value += 4000
    elif len(name) <= 8:
        value += 2500
    elif len(name) <= 10:
        value += 1500

    # توفر .com
    if domain_available:
        value += 3000

    minimum = round(value)
    maximum = round(value * 3)

    return minimum, maximum
