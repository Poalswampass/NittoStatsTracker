from gui import car_dropdown, root, gear_menu_var
from update_ratios import update_ratios
from add_stats import add_stats
from calculate_averages import calculate_averages
from clear_stats import clear_stats
from save_ratios import save_ratios
from show_stats import show_stats
import validate_ratio
import validate_final
import validate_expected_et

def main():
    # Initialize variables
    race_data = {'rt': 0.5, 'et': 4.395, 'mph': 292}
    averages = {'rt': {'count': 0, 'total': 0, 'average': 0},
                'et': {'count': 0, 'total': 0, 'average': 0},
                'mph': {'count': 0, 'total': 0, 'average': 0}}
    
    # Update ratios with the selected car
    selected_car = car_dropdown.get()
    update_ratios(selected_car)

    # Add new race data to the stats and update averages
    add_stats(race_data)
    calculate_averages(averages, race_data)
    
    # Show current stats and ratios
    show_stats()
    gear_menu_var.get()
    validate_ratio()
    validate_final()
    validate_expected_et()
    
if __name__ == '__main__':
    main()

# Start the main loop of the gui
root.mainloop()
