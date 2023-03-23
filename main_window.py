from validate_inputs import validate_ratio_input, validate_final_input, validate_expected_et_input
from add_stats import add_stats
from clear_stats import clear_stats
from save_ratios import save_ratios
import tkinter as tk
import os
from add_ratios import gear_ratios

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

i = 0
gear_label = tk.Label(root, text=f'Gear {i} Ratio:')
gear_label.pack()
for i in range(1, 7):
    gear_entry = tk.Entry(root, validate='key', validatecommand=(validate_ratio_input, validate_final_input, validate_expected_et_input, root, '%P'))

    gear_entry.pack()
    gear_label.append(gear_label)
    gear_ratios.append(gear_entry)
    gear_ratios[f"gear{i}"] = 0
gear_menu_var = tk.StringVar()
gear_menu_var.set('Select Gear')
gear_options = []
for set_name, gear_dict in gear_ratios.items():
    for gear_name, ratio in gear_dict.items():
        if gear_name == "final":
            continue
        label = f"{set_name}: {gear_name} - {ratio:.2f}"
        gear_options.append(label)
gear_menu = tk.OptionMenu(root, gear_menu_var, *gear_options)
gear_menu.pack()

CURRENT_DIR = os.getcwd()
file_path = f'{selected_car}.json'
selected_car = car_dropdown.get()

gear_ratios = {}

num_sets = 50
num_gears = 6

for set_num in range(1, num_sets+1):
    set_name = f"gear_ratio_set_{set_num}"
    gear_ratios[set_name] = {}
    for gear_num in range(1, num_gears+1):
        gear_name = f"gear{gear_num}"
        gear_ratios[set_name][gear_name] = 0.000
    gear_ratios[set_name]["final"] = 0.000

add_ratio_button = tk.Button(root, text='Add Ratios', command=save_ratios(gear_ratios))
add_ratio_button.pack()

save_button = tk.Button(root, text='Save Stats', command=lambda: add_stats)
save_button.pack()    

clear_button = tk.Button(root, text='Clear Stats', command=lambda: clear_stats)
clear_button.pack()