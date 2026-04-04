from dataclasses import replace
from .state import Habitat_State

# file for handling all things time

def sol_time(seconds):
    total_sol_seconds = 88775    # one mars sol is 24h 39min 35sec
    sol_seconds = seconds % total_sol_seconds
    
    hour_24 = sol_seconds // 3600
    minutes = (sol_seconds % 3600) // 60     # 1h = 60min, 1min = 60 sec, 60*60 = 3600
    
    meridiem = "AM"
    hour_12 = hour_24

    if hour_24 >= 12:
        meridiem = "PM"
    if hour_24 > 12:
        hour_12 = hour_24 - 12
    if hour_24 == 0:
        hour_12 = 12

    return hour_12, minutes, meridiem
