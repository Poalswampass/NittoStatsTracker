import tkinter as tk

# Ensure input correct value.
def validate_ratio_input(input_value):
    try:
        value = float(input_value)
    except ValueError:
        return False
    return value >= 0.5 and value <= 8.0

# Ensure input is correct value.
def validate_final_input(input_value):
    try:
        value = float(input_value)
    except ValueError:
        return False
    final_entry = tk.Entry(root, validate='key', validatecommand=(validate_final_input, '%P'))
    gear_ratios['final_drive'] = final_entry
    return value >= 2.000 and value <= 8.000

# Ensure input is correct value.
def validate_expected_et_input(expected_et_value):
    try:
        expected_et_value = float(expected_et_value)
    except ValueError:
        return False
    return expected_et_value >= 4 and expected_et_value <= 25
