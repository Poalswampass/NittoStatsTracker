import tkinter as tk

# Create main window
root = tk.Tk()
root.title('Race Stats')
root.geometry('240x750')

gear_menu_var = tk.StringVar()
gear_menu_var.set('Select Gear')

gear_options = ["Select Gear", "Gear1", "Gear2", "Gear3", "Gear4", "Gear5", "Gear6", "Final"]

gear_menu = tk.OptionMenu(None, gear_menu_var, *gear_options)

__all__ = ['gear_menu', 'gear_menu_var', 'gear_options']
