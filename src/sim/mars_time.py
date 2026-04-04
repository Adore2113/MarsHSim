import math
from dataclasses import replace
from .state import Habitat_State

# file for handling all things time

total_sol_seconds = 88775     # one mars sol is 24h 39min 35sec
sunrise_seconds = round(total_sol_seconds / 4 )   # ~ 22193
afternoon_seconds = round(total_sol_seconds / 2)   # ~ 44387
sunset_seconds = round(total_sol_seconds * 3 / 4)    # ~ 66581
max_daylight_m2_kw = 0.6    # placeholder

def sol_time(seconds):    # for a readable clock
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


def daylight_per_m2_kw(seconds, mission_time_s):
    sol_seconds = seconds % total_sol_seconds

    if sol_seconds < sunrise_seconds or sol_seconds >= sunset_seconds:
        return 0.0
    
    daylight_length_seconds = sunset_seconds - sunrise_seconds
    daylight_progress = (sol_seconds - sunrise_seconds) / daylight_length_seconds

    # using a sine wave, so using .sin from math import to get a radian and .pi 
    daylight_m2_kw = max_daylight_m2_kw * math.sin(math.pi * daylight_progress)

    return daylight_m2_kw