# Ensure input is correct for final drive.
def validate_final_input(input_value):
    try:
        value = float(input_value)
    except ValueError:
        return False
    return value >= 2.000 and value <= 8.000