###This module is a stats tracker ;
###for a racing game called Nitto 1320 Challenge Remade;
import ast
from calendar import c
import csv
import json
import  os
import tkinter as tk
import  tkinter.ttk as ttk
import  tkinter.messagebox as messagebox

CURRENT_DIR = os.getcwd()
file_path = os.path.join(CURRENT_DIR, 'car_data.json')

gear_ratios = {f'Gear {i+1}': 0 for i in range(7)}
ratios = {}

# Variables;
TOTAL_RT = 0
TOTAL_ET = 0
TOTAL_MPH = 0
MATCHES_PLAYED = 0

# Dictionary for storing the gear ratios and car stats of each car.;
car_data = {}

# Read the car ratios and stats from car_data.json, if it exists.;
try:
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            car_data = json.load(f)
except FileNotFoundError:
    messagebox.showerror('Error', 'File not found: car_data.json')
except json.JSONDecodeError:
    messagebox.showerror('Error', 'Error reading car ratios from car_data.json')

# car list and number to be called in indice;
all_cars = {'challenger': 0,
            'charger': 1,
            'civic': 2,
            'funnycar': 3,
            'ftype': 4,
            'lancer': 5,
            'mopar': 6,
            'mustang': 7,
            'nsx': 8,
            'ram': 9,
            'rsx': 10,
            'rx8': 11,
            'skyline': 12,
            'srt4': 15,
            'subaru': 16,
            'supra': 17,
            'tfd': 18,
            'viper': 19}

# Check if all the cars in the menu are present in the car_data dictionary;
for car in all_cars:
    if car not in car_data:
        # Add the car to the car_data dictionary with an empty ratios list;
        car_data[car] = {'ratios': []}
        
        # Add the rt, et, and mph entries for the car;
        for i in range(1, 11):
            car_data[car][f'rt{i}'] = ''
            car_data[car][f'et{i}'] = ''
            car_data[car][f'mph{i}'] = ''
    
        # Add the gear ratios list for the car;
        car_data[car]['gear_ratios'] = {f'Gear {i+1}': 0 for i in range(7)}

# Create main window;
root = tk.Tk()
root.title('Race Stats')
root.geometry('240x750')

car_dropdown = tk.StringVar()
car_dropdown.set('challenger')

car_label = tk.Label(root, text='Cars:')
car_label.pack()
car_menu = tk.OptionMenu(root, car_dropdown, *all_cars)
car_menu.pack()

gear_label = tk.Label(root, text='Gear:')
gear_label.pack()

gear_menu_var = tk.StringVar()
gear_menu_var.set('Select Gear')
gear_options = [f'{gear}: {ratio:.2f}' for gear, ratio in gear_ratios.items()]
gear_menu = tk.OptionMenu(root, gear_menu_var, *gear_options)
gear_menu.pack()

# Get the selected car and gear;
car = car_dropdown.get()
gear = gear_menu_var.get()

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

def load_car_data(car):
    filename = "{}.json".format(car)
    with open(filename) as f:
        data = json.load(f)
    return data

# Function to add stats;
def add_stats(gear_entries):
    global car_data, car, TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED, gear_ratios

    car = car_dropdown.get()

    # Get the values from the entry boxes;
    rt = rt_entry.get()
    et = et_entry.get()
    mph = mph_entry.get()

    # Check that the values are valid;
    try:
        rt = float(rt)
        et = float(et)
        mph = float(mph)
    except ValueError:
        messagebox.showerror('Error', 'Invalid input')
        return

    # Check that rt is between 0 and 1;
    if rt < 0 or rt > 1:
        messagebox.showerror('Error', 'Invalid input for RT')
        return

    # Check that et and mph are positive;
    if et < 0 or mph < 0:
        messagebox.showerror('Error', 'Invalid input for ET or MPH')
        return

    # Check if the race was fouled (rt < 0.500);
    if rt >= 0.500:
        # Update the total stats and matches played;
        TOTAL_RT += rt
        MATCHES_PLAYED += 1
    else:
        messagebox.showinfo('Fouled Race', 'The race was fouled')

    # Add the stats to the car_data dictionary;
    car_data[car]['ratios'].append({
        'rt': rt,
        'et': et,
        'mph': mph
    })

    # Update the total stats and matches played;
    TOTAL_ET += et
    TOTAL_MPH += mph

    # Recalculate and display the averages;
    calculate_averages()

    # Clear the entry boxes;
    rt_entry.delete(0, 'end')
    et_entry.delete(0, 'end')
    mph_entry.delete(0, 'end')

    # Show success message;
    messagebox.showinfo('Success', 'Stats added successfully')

    # Get the gear ratio for the selected gear;
    gear_ratio = float(gear_entries.get())

    # Update the gear ratios dictionary with the new value;
    gear_ratios[gear_menu.cget('text')[:-5]] = gear_ratio

    # Recreate the gear_options list with the updated gear ratios;
    gear_options = [f'{gear}: {ratio:.2f}' for gear, ratio in gear_ratios.items()]

    # Update the gear menu with the new gear ratios;
    gear_menu.set('Select Gear')
    gear_menu['menu'].delete(0, 'end')
    for gear in gear_options:
        gear_menu['menu'].add_command(label=gear, command=tk._setit(gear_menu, gear))

    # Clear the gear entry box;
    gear_entries.delete(0, 'end')

def save_stats():
    # Write the updated car_data dictionary to the car_data.json file;
    with open('car_data.json', 'w') as f:
        json.dump(car_data, f)
        
save_button = tk.Button(root, text='Save Stats', command=save_stats)
save_button.pack()    

def show_stats():
    global TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED
    if MATCHES_PLAYED > 0:
        calculate_averages()
        messagebox.showinfo('Stats', f'Total Matches Played: {MATCHES_PLAYED}\n\n'
                                     f'Total RT: {TOTAL_RT}\n\n'
                                     f'Total ET: {TOTAL_ET}\n\n'
                                     f'Total MPH: {TOTAL_MPH}\n\n'
                                     f'Average RT: {avg_rt_output.get()}\n\n'
                                     f'Average ET: {avg_et_output.get()}\n\n'
                                    f'Average MPH: {avg_mph_output.get()}\n\n')
    else:
        messagebox.showinfo('Stats', 'No matches played yet.')

def update_stats(data, averages):
    global TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED

    # Update total matches;
    MATCHES_PLAYED += 1

    # update total rt et mph;
    TOTAL_RT += data['rt']
    TOTAL_ET += data['et']
    TOTAL_MPH += data['mph']

    # update averages;
    for key, value in data.items():
        if key in averages:
            averages[key]['count'] += 1
            averages[key]['total'] += value
            averages[key]['average'] = averages[key]['total'] / averages[key]['count']
        else:
            averages[key] = {'count': 1, 'total': value, 'average': value}

    return TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED, averages

# Function to calculate and display the average stats;
def calculate_averages():
    global car_data, car_dropdown, avg_rt_output, avg_et_output, avg_mph_output
    stats = car_data[car_dropdown.get()]['stats']
    total_rt = sum([s['rt'] for s in stats if s['rt'] >= 0.5])
    total_et = sum([s['et'] for s in stats])
    total_mph = sum([s['mph'] for s in stats])
    matches_played = len(stats)
    if matches_played > 0:
        avg_rt = round(total_rt / matches_played, 3)
        avg_et = round(total_et / matches_played, 3)
        avg_mph = round(total_mph / matches_played, 3)
    else:
        avg_rt, avg_et, avg_mph = 0, 0, 0
    avg_rt_output.config(state='normal')
    avg_rt_output.delete(0, 'end')
    avg_rt_output.insert(0, avg_rt)
    avg_rt_output.config(state='disabled')
    avg_et_output.config(state='normal')
    avg_et_output.delete(0, 'end')
    avg_et_output.insert(0, avg_et)
    avg_et_output.config(state='disabled')
    avg_mph_output.config(state='normal')
    avg_mph_output.delete(0, 'end')
    avg_mph_output.insert(0, avg_mph)
    avg_mph_output.config(state='disabled')

def clear_stats():
    global TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED, car_data
    confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all data?")
    if confirmed:
        # Clear the stats from the car_data dictionary;
        car_data[car_dropdown]['stats'] = []
        car_data[gear_entries]['ratios'] = []
        car_data[car_dropdown]['matches_played'] = 0

        # Save the updated car_data to the json file;
        with open(file_path, 'w') as f:
            json.dump(car_data, f)

        TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED = 0, 0, 0, 0

        # Clear average Entry widgets;
        avg_rt_output.delete(0, 'end')
        avg_et_output.delete(0, 'end')
        avg_mph_output.delete(0, 'end')

        # Reset global variables;
        TOTAL_RT = 0
        TOTAL_ET = 0
        TOTAL_MPH = 0
        MATCHES_PLAYED = 0

        messagebox.showinfo('Stats Cleared', 'All stats have been cleared.')

clear_button = tk.Button(root, text='Clear Stats', command=clear_stats)
clear_button.pack()

gear_ratios = {}

# function that adds gear ratio sets to a car and populates drop down list;
# so one can track  stats for each ratio;
# eventually the data will be a working dataset to trrain an ai;
def add_ratio(gear_ratios):
    # Declare global variables;
    global ratios
    # Get the gear ratios for the current car from the car_data dictionary;
    car = car_dropdown.get()

    if car in car_data:
        gear_ratios = car_data[car]['gear_ratios']
        for i, ratio in enumerate(gear_ratios):
            gear_ratios[str(i+1)] = float(ratio)
            gear_menu['menu'].entryconfig(i+1, label=f'Gear {i+1} Ratio: {gear_ratios[str(i+1)]}')
    else:
        gear_ratios = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, 'final': 0}

    # Update gear_ratios with the selected gear ratio;
    gear, ratio = gear_entries.split(':')
    gear_ratios[gear] = {'ratio': float(ratio)}

    # Calculate the ratios and store in the ratios dictionary;
    ratios = {gear_ratios['Gear 1'],
              gear_ratios['Gear 2'],
              gear_ratios['Gear 3'],
              gear_ratios['Gear 4'],
              gear_ratios['Gear 5'],
              gear_ratios['Gear 6'],
              gear_ratios['final']}

    gear_menu['menu'].delete(0, 'end')
    for option in gear_options:
        gear_menu['menu'].add_command(label=option, command=tk._setit(gear_menu, option))

    # Update the gear ratio entry fields with the new values.;
    for i, gear_entry in enumerate(gear_entries):
        gear_entry.delete(0, 'end')
        gear_entry.insert(0, str(gear_ratios[str(i+1)]))

# Ensure input values are correct.;
def validate_ratio_input(input_value):
    try:
        value = float(input_value)
    except ValueError:
        return False
    return value >= 0.5 and value <= 8.0

# Add input fields for the gear ratios and save the entries to the ratios dictionary.;
gear_labels = []
gear_entries = []
for i in range(1, 7):
    gear_label = tk.Label(root, text=f'Gear {i} Ratio:')
    gear_label.pack()
    gear_entry = tk.Entry(root, validate='key', validatecommand=(validate_ratio_input, '%P'))
    gear_entry.pack()
    gear_labels.append(gear_label)
    gear_entries.append(gear_entry)
    ratios[f'gear_{i}'] = gear_entry

# Ensure input is correct for final drive.;
def validate_final_input(input_value):
    try:
        value = float(input_value)
    except ValueError:
        return False
    return value >= 2.000 and value <= 8.000

# Add input field for the final drive and save the entry to the ratios dictionary.;
final_label = tk.Label(root, text='Final Drive Ratio:')
final_label.pack()
final_entry = tk.Entry(root, validate='key', validatecommand=(validate_final_input, '%P'))
final_entry.pack()
ratios['final_drive'] = final_entry

def validate_et_input(input_value):
    try:
        value = float(input_value)
    except ValueError:
        return False
    return value >= 4.37 and value <= 25

# Add input field for the expected ET and save the entry to the ratios dictionary.;
expected_et_label = tk.Label(root, text='Expected ET:')
expected_et_label.pack()
expected_et_entry = tk.Entry(root, validate='key', validatecommand=(validate_et_input, '%P'))
expected_et_entry.pack()
ratios['expected_et'] = expected_et_entry 

# Create a function to save the gear ratios to the car_data dictionary.;
def save_ratios(gear_entries):
    global ratios, car_data, all_cars

    all_cars = car_dropdown.get()
    filename =os.path.join(CURRENT_DIR, "cars/{}.json".format(all_cars))

    with open(filename) as f:
        car_data = json.load(f)

    gear = gear_menu_var.get()
    gear_ratio = gear[gear_menu_var.get()]['ratio']

    # Check if the gear ratios for the selected car have already been entered;
    if all_cars in ratios:
        # Check if the gear ratios for the selected gear have already been entered;
        if gear in ratios[car]:
            messagebox.showerror('Error', f'Gear ratios for {car} and {gear} already exist')
            return
    else:
        ratios[all_cars] = {}

    # Get the gear ratios from the entry boxes;
    gear1, gear2, gear3, gear4, gear5, gear6 = [gear_entry.get() for gear_entry in gear_entries]
    final = final_entry.get()
    expected_et = expected_et_entry.get()
    
    # Validate the gear ratios and expected ET.;
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

    # Convert the gear ratios to floats and save them to the ratios dictionary.;
    gear_ratios = [float(gear1), float(gear2), float(gear3), float(gear4), float(gear5), float(gear6), float(final)]
    key_tuple = (all_cars, tuple(gear.items()))
    ratios[key_tuple] = {'ratios': gear_ratios, 'expected_et': float(expected_et_entry.get())}
    car_data[all_cars]['ratios'][gear] = {'ratios': gear_ratios, 'expected_et': float(expected_et_entry.get())}

    # Update the car_data dictionary with the entered gear ratios and expected ET.;
    if all_cars not in car_data:
        car_data[all_cars] = {'ratios': {}, 'stats': []}

    # Convert the gear ratios to floats and save them to the ratios dictionary.;
    gear_ratios = [float(gear1), float(gear2), float(gear3), float(gear4), float(gear5), float(gear6), float(final)]
    ratios[gear] = {'ratios': gear_ratios, 'expected_et': float(expected_et_entry.get())}

    # Update the car_data dictionary with the entered gear ratios and expected ET.;
    car_data['ratios'] = ratios
    car_data['expected_et'] = float(expected_et_entry.get())

    # Save the updated car_data dictionary to a file.;
    with open(f"{all_cars}.json", 'w') as f:
        json.dump(car_data, f)

def update_ratios(car_dropdown):
    ratios = car_data[car_dropdown]['ratios']
    options = [{'label': f'{r:.2f}', 'value': r} for r in ratios]
    gear_menu.options = options
    gear_menu.value = options[0]['value']    
    return options

def update_ratio_var(value):
    return value

add_ratio_button = tk.Button(root, text='Add Ratios', command=lambda: save_ratios(gear_entries))
add_ratio_button.pack()

if __name__ == '__main__':
    race_data = {'rt': 0.05, 'et': 9.9, 'mph': 135}
    averages = {'rt': {'count': 0, 'total': 0, 'average': 0},
                'et': {'count': 0, 'total': 0, 'average': 0},
                'mph': {'count': 0, 'total': 0, 'average': 0}}

    TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED, averages = update_stats(race_data, averages)
    print(TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED, averages)

# Start the main loop of the gui;
root.mainloop()
