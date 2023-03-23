# Ensure input values are correct.
def validate_ratio_input(input_value):
    try:
        value = float(input_value)
    except ValueError:
        return False
    return value >= 0.5 and value <= 8.0
    return True

# Ensure input is correct for final drive.
def validate_final_input(input_value):
    try:
        value = float(input_value)
    except ValueError:
        return False
    return value >= 2.000 and value <= 8.000
    return True

# Add input field for the final drive and save the entry to the ratios dictionary.
final_label = tk.Label(root, text='Final Drive Ratio:')
final_label.pack()
final_entry = tk.Entry(root, validate='key', validatecommand=(validate_final_input, '%P'))
final_entry.pack()
gear_ratios['final_drive'] = final_entry

def validate_et_input(expected_et_value):
    try:
        expected_et_value = float(expected_et_value)
    except ValueError:
        return False
    return expected_et_value >= 4 and expected_et_value <= 25

# Add input field for the expected ET and save the entry to the ratios dictionary.
expected_et_label = tk.Label(root, text='Expected ET:')
expected_et_label.pack()
expected_et_entry = tk.Entry(root, validate='key', validatecommand=(validate_et_input, '%P'))
expected_et_entry.pack()
gear_ratios['expected_et'] = expected_et_entry