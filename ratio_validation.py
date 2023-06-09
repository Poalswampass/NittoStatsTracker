# Ensure input values are correct.
def validate_ratio(value):
    try:
        value = float(value)
    except ValueError:
        return False
    return value >= 0.5 and value <= 8.0
