def update_ratios(car_dropdown):
    ratios = json_data[car_dropdown]['ratios']
    options = [{'label': f'{r:.2f}', 'value': r} for r in ratios]
    gear_menu.options = options
    gear_menu.value = options[0]['value']    
    return options

def update_ratio_var(value):
    return value