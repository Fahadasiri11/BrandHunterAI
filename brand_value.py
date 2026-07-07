def estimate_brand_value(name, score):
    value = 100

    if len(name) <= 8:
        value += 400

    if len(name) <= 12:
        value += 300

    if score >= 90:
        value += 700

    if name.isalpha():
        value += 300

    minimum = value
    maximum = value * 4

    return {
        "min": minimum,
        "max": maximum
    }
