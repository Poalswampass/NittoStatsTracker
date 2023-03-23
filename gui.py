from validate_final import validate_final
from validate_et import validate_et
import tkinter as tk
from add_stats import add_stats
from clear_stats import clear_stats
from save_ratios import save_ratios
import os
from config import car_folder

gear_ratios = {}

# Create main window
root = tk.Tk()
root.title('Race Stats')
root.geometry('240x750')

car_dropdown = tk.StringVar()
car_dropdown.set('challenger')

car_label = tk.Label(root, text='Cars:')
car_label.pack()
car_menu = tk.OptionMenu(root, car_dropdown,
                         'challenger',
                         'charger',
                         'civic',
                         'funnycar',
                         'ftype',
                         'lancer',
                         'mopar',
                         'mustang',
                         'nsx',
                         'ram',
                         'rsx',
                         'rx8',
                         'skyline',
                         'srt4',
                         'subaru',
                         'supra',
                         'tfd',
                         'viper')
car_menu.pack()

rt_label = tk.Label(root, text='RT:')
rt_label.pack()
rt_entry = tk.Entry(root)
rt_entry.pack()

et_label = tk.Label(root, text='ET:')
et_label.pack()
et_entry = tk.Entry(root)
et_entry.pack()

mph_label = tk.Label(root, text='MPH:')
mph_label.pack()
mph_entry = tk.Entry(root)
mph_entry.pack()

avg_rt_label = tk.Label(root, text='Average RT:')
avg_rt_label.pack()
avg_rt_output = tk.Entry(root, state='disabled')
avg_rt_output.pack()

avg_et_label = tk.Label(root, text='Average ET:')
avg_et_label.pack()
avg_et_output = tk.Entry(root, state='disabled')
avg_et_output.pack()

avg_mph_label = tk.Label(root, text='Average MPH:')
avg_mph_label.pack()
avg_mph_output = tk.Entry(root, state='disabled')
avg_mph_output.pack()

selected_car = car_dropdown.get()
num_sets = 50
num_gears = 6

for set_num in range(1, num_sets+1):
    set_name = f"gear_ratio_set_{set_num}"
    gear_ratios[set_name] = {}
    for gear_num in range(1, num_gears+1):
        gear_name = f"gear{gear_num}"
        gear_ratios[set_name][gear_name] = 0.000
    gear_ratios[set_name]["final"] = 0.000
    gear_options = ["Select Gear", "Gear1", "Gear2", "Gear3", "Gear4", "Gear5", "Gear6", "Final"]
    gear_options[0] = set_name
    gear_menu_var = tk.StringVar()
    gear_menu_var.set('Select Gear')
    gear_menu = tk.OptionMenu(root, gear_menu_var, *gear_options)
    gear_menu.pack()

# add final ratio box
final_label = tk.Label(root, text='Final Drive Ratio:')
final_label.pack()
final_entry = tk.Entry(root, validate='key', validatecommand=(validate_final, '%P'))
final_entry.pack()
gear_ratios['final_drive'] = final_entry

# Add input field for the expected ET and save the entry to the ratios dictionary.
expected_et_label = tk.Label(root, text='Expected ET:')
expected_et_label.pack()
expected_et_entry = tk.Entry(root, validate='key', validatecommand=(validate_et, '%P'))
expected_et_entry.pack()
gear_ratios['expected_et'] = expected_et_entry


add_ratio_button = tk.Button(root, text='Add Ratios', command=lambda: save_ratios(gear_ratios))
add_ratio_button.pack()

save_button = tk.Button(root, text='Save Stats', command=add_stats)
save_button.pack()    

clear_button = tk.Button(root, text='Clear Stats', command=clear_stats)
clear_button.pack()