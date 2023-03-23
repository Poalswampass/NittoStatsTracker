from update_ratios import update_ratios
from main_window import car_dropdown
from main_window import root

selected_car = car_dropdown.get()

if __name__ == '__main__':
    race_data = {'rt': 0.05, 'et': 9.9, 'mph': 135}
    averages = {'rt': {'count': 0, 'total': 0, 'average': 0},
                'et': {'count': 0, 'total': 0, 'average': 0},
                'mph': {'count': 0, 'total': 0, 'average': 0}}

    TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED, averages = update_ratios(race_data, averages)
    print(TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED, averages)

# Start the main loop of the gui
root.mainloop()
