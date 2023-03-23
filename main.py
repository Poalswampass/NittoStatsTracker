from update_ratios import update_ratios
from add_stats import add_stats
from calculate_averages import calculate_averages
from show_stats import show_stats
from init import car_dropdown
import init

def main():
    # Initialize variables
    race_data = {'rt': 0.5, 'et': 4.395, 'mph': 292.86}
    averages = {'rt': {'count': 0, 'total': 0, 'average': 0},
                'et': {'count': 0, 'total': 0, 'average': 0},
                'mph': {'count': 0, 'total': 0, 'average': 0}}
    
    # Update ratios with the selected car
    selected_car = car_dropdown.get()
    update_ratios(selected_car)

    # Add new race data to the stats and update averages
    add_stats(race_data)
    calculate_averages(averages)
    
    # Show current stats and ratios
    show_stats()
    
if __name__ == '__main__':
    init.setup()
