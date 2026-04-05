import math
from dataclasses import replace
from .state import Habitat_State

# file for handling all things time

#    --------------------------------  

total_sol_seconds = 88775     # one mars sol is 24h 39min 35sec
sunrise_seconds = total_sol_seconds // 4   # ~ 22193
afternoon_seconds = total_sol_seconds // 2   # ~ 44387
sunset_seconds = (total_sol_seconds * 3) // 4    # ~ 66581

max_daylight_m2_kw = 0.6    # placeholder

# habitat location = 47° North, 184° East
longitude_east_deg = 184
longitude_north_deg = 47

#    --------------------------------

def time_in_sol_seconds(mission_time_s):
    longitude_offset_s = (longitude_east_deg * total_sol_seconds) // 3 
    return (mission_time_s + longitude_offset_s) % total_sol_seconds


def sol_time(mission_time_s):    # for a readable clock
    time_in_sol_s = time_in_sol_seconds(mission_time_s)
    
    hour_24 = (time_in_sol_s * 24) // total_sol_seconds
    hour_remainder = (time_in_sol_s * 24) % total_sol_seconds
    
    minutes = (hour_remainder * 60) // total_sol_seconds
    minute_remainder = (hour_remainder * 60) % total_sol_seconds 
    seconds = (minute_remainder * 60) // total_sol_seconds 
    
    meridiem = "AM"
    hour_12 = hour_24

    if hour_24 >= 12:
        meridiem = "PM"
    if hour_24 > 12:
        hour_12 = hour_24 - 12
    if hour_24 == 0:
        hour_12 = 12

    return hour_12, minutes, seconds, meridiem



def daylight_per_m2_kw(mission_time_s):
    time_in_sol_s = time_in_sol_seconds(mission_time_s)
    
    if time_in_sol_s < sunrise_seconds or time_in_sol_s >= sunset_seconds:
        return 0.0
    
    daylight_length_s = sunset_seconds - sunrise_seconds
    daylight_progress = (time_in_sol_s - sunrise_seconds) / daylight_length_s

    # using a sine wave, so using .sin from math import to get a radian and .pi 
    daylight_m2_kw = max_daylight_m2_kw * math.sin(math.pi * daylight_progress)

    return daylight_m2_kw