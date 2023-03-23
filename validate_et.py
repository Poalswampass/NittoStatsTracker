# Ensure input is correct value.
def validate_expected_et_input(expected_et_value):
    try:
        expected_et_value = float(expected_et_value)
    except ValueError:
        return False
    return expected_et_value >= 4 and expected_et_value <= 25
