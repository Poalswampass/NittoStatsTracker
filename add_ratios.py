import os
import json
import tkinter as tk
from config import car_folder
from final_validation import validate_final
from menu import gear_menu, gear_menu_var, gear_options


def add_ratio(gear_ratios, gear_entries):
    global selected_car
    if os.path.exists(car_folder, f'{selected_car}.json'):
        with open(car_folder, 'r') as f:
            json_data = json.load(f)

    if selected_car in car_folder:
        ratios = car_folder[selected_car]['ratios']
        for i in range(1, 7):
            gear_ratio = ratios.get(f'gear_{i}')
            if gear_ratio is not None:
                gear_ratios[str(i)] = float(gear_ratio.get())
                gear_menu['menu'].entryconfig(i, label=f'Gear {i} Ratio: {gear_ratios[str(i)]}')
    else:
        gear_ratios = {'gear1': 0,
                       'gear2': 0,
                       'gear3': 0,
                       'gear4': 0,
                       'gear5': 0,
                       'gear6': 0,
                       'final': 0,
                       'expected_et': 0}

    # Get the selected gear ratio set
    gear_menu_var.get()
    
    # Update gear_ratios with the selected gear ratio
    gear, ratio = gear_entries[0].get().split(':')
    gear_ratios[gear] = float(ratio)

    # Update the car_data dictionary with the new gear ratios
    if selected_car in car_folder:
        [selected_car]['gear_ratios'] = ratios
    else:
        [selected_car] = {'gear_ratios': ratios}

    # Write the updated car_data dictionary to the corresponding JSON file
    file_path = (car_folder, f'{selected_car}.json')
    with open(file_path, 'w') as f:
        json.dump(json_data, f)

    gear_menu['menu'].delete(0, 'end')
    for option in gear_options:
        gear_menu['menu'].add_command(label=option, command=tk._setit(gear_menu, option))

    # Update the gear ratio entry fields with the new values.
    for i, gear_entry in enumerate(gear_entries):
        gear_entry.delete(0, 'end')
        gear_entry.insert(0, str(gear_ratios[str(i+1)]))