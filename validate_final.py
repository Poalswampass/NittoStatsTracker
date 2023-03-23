# Ensure input is correct for final drive.
def validate_final(value):
    try:
        value = float(value)
    except ValueError:
        return False
    return value >= 2.000 and value <= 8.000