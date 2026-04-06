import math
from dataclasses import replace
from .state import Habitat_State

# file for handling all things time 

seconds_per_sol = 88775     # one mars sol is 24h 39min 35sec
hours_per_sol = seconds_per_sol / 3600
max_daylight_m2_kw = 0.6    # placeholder

# habitat location = 47° North, 184° East (Arcadia Planitia)
longitude_east_deg = 184
latitude_north_deg = 47

# ls = areocentric solar longitude (season angle)
solar_longitude_ls_deg = 0    # 0 = northern spring equinox


def advance_time(state, dt_s):
    new_mission_time_s = state.mission_time_s + dt_s
    
    degrees_per_second = 360.0 / (668.6 * seconds_per_sol)
    new_ls_deg = (solar_longitude_ls_deg + dt_s * degrees_per_second) % 360.0
    
    return replace(state, new_mission_time_s = new_mission_time_s, solar_longitude_ls_deg = new_ls_deg)


def get_sol_and_time(state):    # for sol number and 24 hour time format
    sol = int(state.mission_time_s // seconds_per_sol)
    seconds_into_sol = state.mission_time_s % seconds_per_sol

    hour_24 = seconds_into_sol // 3600
    minute = (seconds_into_sol % 3600) // 60

    return sol, hour_24, minute


def daytime_check(state):
    #I'll finish this later
    _, hour, _ = get_sol_and_time(state)

    is_daytime = 6 <= hour < 20

    return is_daytime


def sun_tilt_degree(solar_longitude_ls_deg):
    mars_axial_tilt_deg = 25.19
    sun_tilt_deg = mars_axial_tilt_deg * math.sin(math.radians(solar_longitude_ls_deg))
   
    return sun_tilt_deg


def daylight_per_m2_kw(mission_time_s):
    time_in_sol_s = mission_time_s % seconds_per_sol
    
    sunrise_s = seconds_per_sol * 0.25    # ~6am
    sunset_s = seconds_per_sol * 0.75    # ~6pm
    
    if time_in_sol_s < sunrise_s or time_in_sol_s >= sunset_s:
        return 0.0

    daylight_length_s = sunset_s - sunrise_s
    daylight_progress = (time_in_sol_s - sunrise_s) / daylight_length_s

    # using a sine wave, so using .sin from math import to get a radian and .pi 
    daylight_m2_kw = 0.6 * math.sin(math.pi * daylight_progress)

    return daylight_m2_kw