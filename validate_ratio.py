# Ensure input values are correct.
def validate_ratio_input(input_value):
    try:
        value = float(input_value)
    except ValueError:
        return False
    return value >= 0.5 and value <= 8.0
