def validate_et_entry(value):
    try:
        value = float(value)
    except ValueError:
        return False
    return value >= 4 and value <= 25
