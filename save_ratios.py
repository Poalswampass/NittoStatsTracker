# Create a function to save the gear ratios to the car_data dictionary.
def save_ratios(gear_ratios, json_data, car, gear_ratios_var):
    # Get the selected car and gear
    car = car_dropdown.get()
    num_sets = 50
    num_gears = 6

    for set_num in range(1, num_sets+1):
        set_name = f"gear_ratio_set_{set_num}"
        gear_ratios[set_name] = {}
        for gear_num in range(1, num_gears+1):
            gear_name = f"gear{gear_num}"
            gear_ratios[set_name][gear_name] = 0.000
        gear_ratios[set_name]["final"] = 0.000

    folder_path = os.path.join(os.getcwd(), "cars")
    filename = os.path.join(folder_path, "{}.json".format(car))
    
    # Check if the gear ratios for the selected car have already been entered
    if car in gear_ratios:
        # Check if the gear ratios for the selected gear have already been entered
        if gear in gear_ratios[car]:
            messagebox.showerror('Error', f'Gear ratios for {car} and {gear} already exist')
            return
    else:
        gear_ratios[car] = {}

    # Get the gear ratios from the entry boxes
    gear1, gear2, gear3, gear4, gear5, gear6 = [gear_entry.get() for gear_entry in gear_entries]
    final = final_entry.get()
    expected_et = expected_et_entry.get()
    
    # Validate the gear ratios and expected ET.
    if not validate_ratio_input(gear1):
        messagebox.showerror('Error', 'Gear 1 ratio must be a number between 0.5 and 8.0')
        return
    if not validate_ratio_input(gear2):
        messagebox.showerror('Error', 'Gear 2 ratio must be a number between 0.5 and 8.0')
        return
    if not validate_ratio_input(gear3):
        messagebox.showerror('Error', 'Gear 3 ratio must be a number between 0.5 and 8.0')
        return
    if not validate_ratio_input(gear4):
        messagebox.showerror('Error', 'Gear 4 ratio must be a number between 0.5 and 8.0')
        return
    if not validate_ratio_input(gear5):
        messagebox.showerror('Error', 'Gear 5 ratio must be a number between 0.5 and 8.0')
        return
    if not validate_ratio_input(gear6):
        messagebox.showerror('Error', 'Gear 6 ratio must be a number between 0.5 and 8.0')
        return
    if not validate_ratio_input(final):
        messagebox.showerror('Error', 'Final drive ratio must be a number between 2.0 and 8.0')
        return
    if not validate_et_input(expected_et):
        messagebox.showerror('Error', 'Expected ET must be a number between 4.37 and 25')
        return

    # Convert the gear ratios to floats and save them to the ratios dictionary.
    gear_ratios = [float(gear1), float(gear2), float(gear3), float(gear4), float(gear5), float(gear6), float(final)]
    ratios[car][gear] = {'ratios': gear_ratios, 'expected_et': float(expected_et_entry.get())}
    json_data[car]['ratios'][gear] = {'ratios': gear_ratios, 'expected_et': float(expected_et_entry.get())}

    # Update the car_data dictionary with the entered gear ratios and expected ET.
    if car not in json_data:
        json_data[car] = {'ratios': {}, 'stats': []}
    ratios = json_data[car]['ratios']
    ratios['1'] = float(gear1)
    ratios['2'] = float(gear2)
    ratios['3'] = float(gear3)
    ratios['4'] = float(gear4)
    ratios['5'] = float(gear5)
    ratios['6'] = float(gear6)
    ratios['final'] = float(final_entry.get())
    json_data[car]['expected_et'] = float(expected_et_entry.get())

    # Save the updated car_data dictionary to a file.
    with open('json_data.json', 'w') as f:
        json.dump(json_data, f)