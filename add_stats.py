def add_stats(gear_entries):
    global json_data, car_dropdown, TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED, gear_ratios, selected_car
    selected_car = car_dropdown.get()
    
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                json.load(f)
        else:
            print(f"{file_path} does not exist.")
    except:
        print(error)

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
    gear_menu_var.get()

    # Add the stats to the car_data dictionary under the selected gear
    json_data[gear_ratios].append({
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