from config import car_folder
from gui import gear_menu
from save_ratios import set_name

global selected_car

def update_ratios(selected_car):
    ratios = car_folder[selected_car]['ratios'][set_name]
    options = [{'label': f'{r:.2f}', 'value': r} for r in ratios]
    gear_menu.options = options
    gear_menu.value = options[0]['value']    
    return options

def update_ratio_var(value):
    return value