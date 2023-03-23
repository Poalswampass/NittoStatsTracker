import os
import tkinter as messagebox
from calculate_averages import calculate_averages
from init import car_folder
from gui import rt_entry, et_entry, mph_entry
from menu import gear_menu_var

def add_stats(gear_entries):
    global selected_car, gear_menu_var
    # Check if a car has been selected
    if not selected_car:
        messagebox.showerror('Error', 'No car selected')
        return

    # Check if the selected car exists
    os.path.join(car_folder, f'{selected_car}.json')
    if not os.path.exists(car_folder):
        messagebox.showerror('Error', f'{selected_car} does not exist')
        return

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
        return

    # Check that rt is between 0 and 1
    if rt < 0 or rt > 1:
        messagebox.showerror('Error', 'Invalid input for RT')
        return

    # Check that et and mph are positive
    if et < 0 or mph < 0:
        messagebox.showerror('Error', 'Invalid input for ET or MPH')
        return

    # Check if the race was fouled (rt < 0.500)
    if rt >= 0.500:
        # Update the total stats and matches played
        TOTAL_RT += rt
        MATCHES_PLAYED += 1
    else:
        messagebox.showinfo('Fouled Race', 'The race was fouled')

    # Get the selected gear ratio set
    selected_gear = gear_menu_var.get()

    # Add the stats to the car_data dictionary under the selected gear
    gear_entries[selected_gear].append({
        'rt': rt,
        'et': et,
        'mph': mph
    })

    # Update the total stats
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
