import json
import os
import tkinter as messagebox

def save_stats(car_data):
    global selected_car, car_folder

    # Check if a car has been selected
    if not selected_car:
        messagebox.showerror('Error', 'No car selected')
        return

    # Check if the selected car exists
    car_file = os.path.join(car_folder, f'{selected_car}.json')
    if not os.path.exists(car_file):
        messagebox.showerror('Error', f'{selected_car} does not exist')
        return

    # Save the updated car_data dictionary to a JSON file
    with open(car_file, 'w') as f:
        json.dump(car_data, f)

    # Show success message
    messagebox.showinfo('Success', f'Stats for {selected_car} saved')