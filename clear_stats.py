import json
from init import messagebox, calculate_averages
from gui import avg_rt_output, avg_et_output, avg_mph_output

def clear_stats():
    global TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED, json_data, selected_car
    file_path = f'{selected_car}.json'
    with open(file_path) as f:
        json_data = json.load(f)
    confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all data?")
    if confirmed:
        # Clear the stats from the JSON file
        json_data['stats'] = []
        json_data['ratios'] = []
        json_data['matches_played'] = 0
        with open(file_path, 'w') as f:
            json.dump(json_data, f)

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