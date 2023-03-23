# Function to calculate and display the average stats
def calculate_averages():
    global json_data, car_dropdown, avg_rt_output, avg_et_output, avg_mph_output, selected_car
    with open(file_path) as f:
        json_data = json.load(f)
    stats = json_data['stats']

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