import json
import os
import tkinter as tk
import tkinter.messagebox as messagebox

CURRENT_DIR = os.getcwd()
file_path = os.path.join(CURRENT_DIR, '/cars/{}.json')

gear_ratios = {
    "gear_ratio_set_1": {"gear1": 0.000, "gear2": 0.000, "gear3": 0.000, "gear4": 0.000, "gear5": 0.000, "gear6": 0.000, "final": 0.000},
}

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

gear_label = tk.Label(root, text='Gear:')
gear_label.pack()

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
# Dictionary for storing the gear ratios and car stats of each car.
car_data = {'selected_car.json'}

# Read the car ratios and stats from car_data.json, if it exists.
def load_car_data(car):
    global selected_car
    try:
        filename = os.path.join(CURRENT_DIR, "cars/{}.json".format(selected_car))
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                car_data = json.load(f)
            return car_data
        else:
            print(f"{filename} does not exist.")
            return {}
    except Exception as e:
        print(e)
        return {}

# Variables
TOTAL_RT = 0
TOTAL_ET = 0
TOTAL_MPH = 0
MATCHES_PLAYED = 0

def add_stats(gear_entries):
    global car_data, car_dropdown, TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED, gear_ratios, selected_car
    
    # Check if the car data file exists
    file_path = os.path.join(CURRENT_DIR, "cars/{}.json".format(car))
    if not os.path.exists(file_path):
        messagebox.showerror('Error', f'{selected_car} data file not found')
        return False

    # Load the car data from the JSON file
    with open(file_path) as f:
        car_data = json.load(f)
    
    # Get the values from the entry boxes
    rt = rt_entry.get()
    et = et_entry.get()
    mph = mph_entry.get()

    # Check that the values are valid
    try:
        rt = float(rt)
        et = float(et)
        mph = float(mph)
    except ValueError:
        messagebox.showerror('Error', 'Invalid input')
        return False

    # Check that rt is between 0 and 1
    if rt < 0 or rt > 1:
        messagebox.showerror('Error', 'Invalid input for RT')
        return False

    # Check that et and mph are positive
    if et < 0 or mph < 0:
        messagebox.showerror('Error', 'Invalid input for ET or MPH')
        return False

    # Check if the race was fouled (rt < 0.500)
    if rt >= 0.500:
        # Update the total stats and matches played
        TOTAL_RT += rt
        MATCHES_PLAYED += 1
    else:
        messagebox.showinfo('Fouled Race', 'The race was fouled')

    # Get the selected gear ratio set
    selected_set = gear_menu_var.get()
    gear_ratio = gear_ratios[int(selected_set.split(':')[0])]

    # Add the stats to the car_data dictionary under the selected gear
    car_data[gear]['ratios'].append({
        'rt': rt,
        'et': et,
        'mph': mph
    })

    # Update the total stats and matches played
    TOTAL_ET += et
    TOTAL_RT += rt
    TOTAL_MPH += mph

    # Recalculate and display the averages
    calculate_averages()

    # Clear the entry boxes
    rt_entry.delete(0, 'end')
    et_entry.delete(0, 'end')
    mph_entry.delete(0, 'end')

    # Show success message
    messagebox.showinfo('Success', 'Stats added successfully')
        
save_button = tk.Button(root, text='Save Stats', command=add_stats)
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

# Function to calculate and display the average stats
def calculate_averages():
    global car_data, car_dropdown, avg_rt_output, avg_et_output, avg_mph_output, selected_car
    file_path = f'{selected_car}.json'
    with open(file_path) as f:
        car_data = json.load(f)
    stats = car_data['stats']

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
    global TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED, car_data, selected_car
    file_path = f'{selected_car}.json'
    with open(file_path) as f:

        car_data = json.load(f)
    confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all data?")
    if confirmed:
        # Clear the stats from the JSON file
        car_data['stats'] = []
        car_data['ratios'] = []
        car_data['matches_played'] = 0
        with open(file_path, 'w') as f:
            json.dump(car_data, f)

        TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED = 0, 0, 0, 0

        # Clear average Entry widgets
        avg_rt_output.delete(0, 'end')
        avg_et_output.delete(0, 'end')
        avg_mph_output.delete(0, 'end')

        # Reset global variables
        TOTAL_RT = 0
        TOTAL_ET = 0
        TOTAL_MPH = 0
        MATCHES_PLAYED = 0

        messagebox.showinfo('Stats Cleared', 'All stats have been cleared.')

clear_button = tk.Button(root, text='Clear Stats', command=clear_stats)
clear_button.pack()

# function that adds gear ratio sets to a car and populates drop down list
# so one can track  stats for each ratio
# eventually the data will be a working dataset to trrain an ai
def add_ratio(gear_ratios):
    # Declare global variables
    global ratios
    # Get the gear ratios for the current car from the car_data dictionary.
    car = car_dropdown.get()
    load_data(car)

    if car in car_data:
        ratios = car_data[car]['ratios']
        gear_ratios = {}
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
    selected_set = gear_menu_var.get()
    
    # Update gear_ratios with the selected gear ratio
    gear, ratio = gear_entries.split(':')
    gear_ratios[gear] = float(ratio)

    # Update the car_data dictionary with the new gear ratios
    if car in car_data:
        car_data[car]['ratios'] = ratios
    else:
        car_data[car] = {'ratios': ratios}

    # Write the updated car_data dictionary to the corresponding JSON file
    file_path = f'{selected_car}.json'
    with open(file_path, 'w') as f:
        json.dump(car_data, f)

    gear_menu['menu'].delete(0, 'end')
    for option in gear_options:
        gear_menu['menu'].add_command(label=option, command=tk._setit(gear_menu, option))

    # Update the gear ratio entry fields with the new values.
    for i, gear_entry in enumerate(gear_entries):
        gear_entry.delete(0, 'end')
        gear_entry.insert(0, str(gear_ratios[str(i+1)]))

# Ensure input values are correct.
def validate_ratio_input(input_value):
    try:
        value = float(input_value)
    except ValueError:
        return False
    return value >= 0.5 and value <= 8.0
    return True

# Add input fields for the gear ratios and save the entries to the gear_ratios dictionary.
gear_labels = []
gear_entries = []
for i in range(1, 7):
    gear_label = tk.Label(root, text=f'Gear {i} Ratio:')
    gear_label.pack()
    gear_entry = tk.Entry(root, validate='key', validatecommand=(validate_ratio_input, '%P'))
    gear_entry.pack()
    gear_labels.append(gear_label)
    gear_entries.append(gear_entry)
    gear_ratios["gear_ratio_set_1"][f"gear{i}"] = gear_entry

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
        expected_et_value = float(input_value)
    except ValueError:
        return False
    return expected_et_value >= 4 and expected_et_value <= 25
    return True

# Add input field for the expected ET and save the entry to the ratios dictionary.
expected_et_label = tk.Label(root, text='Expected ET:')
expected_et_label.pack()
expected_et_entry = tk.Entry(root, validate='key', validatecommand=(validate_et_input, '%P'))
expected_et_entry.pack()
gear_ratios['expected_et'] = expected_et_entry

# Create a function to save the gear ratios to the car_data dictionary.
def save_ratios(gear_entries):
    
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

    global ratios, car_data, all_cars

    all_cars = car_dropdown.get()
    folder_path = os.path.join(os.getcwd(), "cars")
    filename = os.path.join(folder_path, "{}.json".format(all_cars))

    # Get the selected car and gear
    car = car_dropdown.get()
    
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
    ratios[car][gear] = {'ratios': gear_ratios, 'expected_et': float(xptdet_entry.get())}
    car_data[car]['ratios'][gear] = {'ratios': gear_ratios, 'expected_et': float(expected_et_entry.get())}

    # Update the car_data dictionary with the entered gear ratios and expected ET.
    car = car_dropdown.get()
    if car not in car_data:
        car_data[car] = {'ratios': {}, 'stats': []}
    ratios = car_data[car]['ratios']
    ratios['1'] = float(gear1)
    ratios['2'] = float(gear2)
    ratios['3'] = float(gear3)
    ratios['4'] = float(gear4)
    ratios['5'] = float(gear5)
    ratios['6'] = float(gear6)
    ratios['final'] = float(final_entry.get())
    car_data[car]['expected_et'] = float(expected_et_entry.get())

    # Save the updated car_data dictionary to a file.
    with open('car_data.json', 'w') as f:
        json.dump(car_data, f)

def update_ratios(car_dropdown):
    ratios = car_data[car_dropdown]['ratios']
    options = [{'label': f'{r:.2f}', 'value': r} for r in ratios]
    gear_menu.options = options
    gear_menu.value = options[0]['value']    
    return options

def update_ratio_var(value):
    return value

add_ratio_button = tk.Button(root, text='Add Ratios', command=save_ratios(gear_entries))
add_ratio_button.pack()

if __name__ == '__main__':
    race_data = {'rt': 0.05, 'et': 9.9, 'mph': 135}
    averages = {'rt': {'count': 0, 'total': 0, 'average': 0},
                'et': {'count': 0, 'total': 0, 'average': 0},
                'mph': {'count': 0, 'total': 0, 'average': 0}}

    TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED, averages = update_ratios(race_data, averages)
    print(TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED, averages)

# Start the main loop of the gui
root.mainloop()
