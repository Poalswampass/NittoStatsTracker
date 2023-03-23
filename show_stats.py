from calculate_averages import calculate_averages
import tkinter as messagebox
from gui import avg_rt_output, avg_et_output, avg_mph_output

def show_stats():
    global TOTAL_RT, TOTAL_ET, TOTAL_MPH, MATCHES_PLAYED
    if MATCHES_PLAYED > 0:
        calculate_averages()
        messagebox.showinfo('Stats', f'Total Matches Played: {MATCHES_PLAYED}\n\n'
                                     f'Total RT: {TOTAL_RT}\n\n'
                                     f'Total ET: {TOTAL_ET}\n\n'
                                     f'Total MPH: {TOTAL_MPH}\n\n'
                                     f'Average RT: {avg_rt_output.get()}\n\n'
                                     f'Average ET: {avg_et_output.get()}\n\n'
                                    f'Average MPH: {avg_mph_output.get()}\n\n')
    else:
        messagebox.showinfo('Stats', 'No matches played yet.')