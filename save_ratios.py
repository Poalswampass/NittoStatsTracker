import os
import tkinter as messagebox
import json
from ratio_validation import validate_ratio
from final_validation import validate_final
from expected_et import validate_et_entry
from add_ratios import gear_menu
from config import car_folder
from gui import set_name, expected_et_entry, final_entry

# Create a function to save the gear ratios to the car_data dictionary.
def save_ratios(gear_ratios, car, gear_ratios_var):
    # Get the selected car and gear
    global selected_car

    os.path.join(car_folder, f"{selected_car}.json".format(car))
    
    # Check if the gear ratios for the selected car have already been entered
    if car in gear_ratios:
        # Check if the gear ratios for the selected gear have already been entered
        if set_name in gear_ratios[car]:
            messagebox.showerror('Error', f'Gear ratios for {car} and {set_name} already exist')
            return
    else:
        gear_ratios[car] = {}

    # Get the gear ratios from the entry boxes
    gear1, gear2, gear3, gear4, gear5, gear6 = [gear_entry.get() for gear_entry in gear_menu]
    final = final_entry.get()
    expected_et = expected_et_entry.get()
    
    # Validate the gear ratios and expected ET.
    if not validate_ratio(gear1):
        messagebox.showerror('Error', 'Gear 1 ratio must be a number between 0.5 and 8.0')
        return
    if not validate_ratio(gear2):
        messagebox.showerror('Error', 'Gear 2 ratio must be a number between 0.5 and 8.0')
        return
    if not validate_ratio(gear3):
        messagebox.showerror('Error', 'Gear 3 ratio must be a number between 0.5 and 8.0')
        return
    if not validate_ratio(gear4):
        messagebox.showerror('Error', 'Gear 4 ratio must be a number between 0.5 and 8.0')
        return
    if not validate_ratio(gear5):
        messagebox.showerror('Error', 'Gear 5 ratio must be a number between 0.5 and 8.0')
        return
    if not validate_ratio(gear6):
        messagebox.showerror('Error', 'Gear 6 ratio must be a number between 0.5 and 8.0')
        return
    if not validate_final(final):
        messagebox.showerror('Error', 'Final drive ratio must be a number between 2.0 and 8.0')
        return
    if not validate_et_entry(expected_et):
        messagebox.showerror('Error', 'Expected ET must be a number between 4.37 and 25')
        return

    # Convert the gear ratios to floats and save them to the ratios dictionary.
    gear_ratios = [float(gear1), float(gear2), float(gear3), float(gear4), float(gear5), float(gear6), float(final)]
    ratios[car][gear_ratios] = {'ratios': gear_ratios, 'expected_et': float(expected_et_entry.get())}
    car_folder[car]['ratios'][set_name] = {'ratios': gear_ratios, 'expected_et': float(expected_et_entry.get())}

    # Update the car_data dictionary with the entered gear ratios and expected ET.
    if selected_car not in car_folder:
        car_folder[car] = {'ratios': {}, 'stats': []}
    ratios = car_folder[car]['ratios']
    ratios['1'] = float(gear1)
    ratios['2'] = float(gear2)
    ratios['3'] = float(gear3)
    ratios['4'] = float(gear4)
    ratios['5'] = float(gear5)
    ratios['6'] = float(gear6)
    ratios['final'] = float(final_entry.get())
    car_folder[car]['expected_et'] = float(expected_et_entry.get())

    # Save the updated car_data dictionary to a file.
    with open('json_data.json', 'w') as f:
        json.dump(car_folder, f)