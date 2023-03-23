from add_ratios import *
from add_stats import *
from calculate_averages import *
from clear_stats import *
from config import *
from gui import *
from save_ratios import *
from show_stats import *
from save_stats import *
from update_ratios import *
from validate_ratio import *
from validate_final import *
from et_validate import *
import os
import json

__all__ = [
    'add_ratios',
    'add_stats',
    'calculate_averages',
    'clear_stats',
    'config',
    'car_name',
    'save_ratios',
    'show_stats',
    'save_stats',
    'update_ratios',
    'validate_ratio',
    'validate_final',
    'et_validate'
]

car_name = {}
for file_name in os.listdir(os.path.dirname(__file__) + '/car_name'):
    if file_name.endswith('.json'):
        with open(os.path.dirname(__file__) + '/car_name/' + file_name) as f:
            car_name[file_name[:-5]] = json.load(f)
