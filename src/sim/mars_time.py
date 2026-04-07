import math
from dataclasses import replace
from .state import Habitat_State

#--------------------constants-----------------------♡
seconds_per_sol = 88775     # one mars sol is 24h 39min 35sec
hours_per_sol = seconds_per_sol / 3600
sols_per_year = 668.6     # one full Mars orbit

max_daylight_m2_kw = 0.6    # placeholder

# habitat location = 47° North, 184° East (Arcadia Planitia)
longitude_east_deg = 184
latitude_north_deg = 47

# ls = areocentric solar longitude (season angle)
solar_longitude_ls_deg_spring = 0    # equinox
solar_longitude_ls_deg_summer = 90    # solstice
solar_longitude_ls_deg_autumn = 180    # equinox
solar_longitude_ls_deg_winter = 270    # solstice
#----------------------------------------------------♡


#---------current time within current sol------------♡
def sol_time_seconds(mission_time_s):
    return mission_time_s % seconds_per_sol


#----------------24 hour time format-----------------♡ 
def get_sol_time(state):
    sol_number = int(state.mission_time_s // seconds_per_sol)
    sol_seconds = sol_time_seconds(state.mission_time_s)
    
    hour_24 = sol_seconds // 3600
    minutes = (sol_seconds % 3600) // 60
    
    return sol_number, hour_24, minutes


#----------------------season------------------------♡ 



#----------------current season angle----------------♡ 
def get_season_angle_deg(mission_time_s):    # ls = areocentric solar longitude (season angle)
    seconds_per_year = sols_per_year * seconds_per_sol
    degrees_per_second = 360.0 / seconds_per_year

    ls_deg = (mission_time_s * degrees_per_second) % 360
    
    return ls_deg


#--------convert sesason angle to sun's tilt---------♡ 




#----------what fraction is sol is daylight----------♡ 




#---------------sunset/sunrise & sine----------------♡




#---------------solar generatioin info---------------♡

        # handle this in power_system.py





















seconds_per_sol = 88775     # one mars sol is 24h 39min 35sec
hours_per_sol = seconds_per_sol / 3600
max_daylight_m2_kw = 0.6    # placeholder

# habitat location = 47° North, 184° East (Arcadia Planitia)
longitude_east_deg = 184
latitude_north_deg = 47

# ls = areocentric solar longitude (season angle)
solar_longitude_ls_deg = 0

# 0 = northern spring equinox
# 90 = northern summer solstice
# 180 = northern autumn equinox
# 270 = northern winter solstice


#----------move simulation time step ahead-----------♡ 
def advance_time(state, dt_s):
    new_mission_time_s = state.mission_time_s + dt_s
    
    degrees_per_second = 360.0 / (668.6 * seconds_per_sol)    # one full orbit ~ 668.6
    new_ls_deg = (solar_longitude_ls_deg + dt_s * degrees_per_second) % 360.0
    
    return replace(state, mission_time_s = new_mission_time_s, solar_longitude_ls_deg = new_ls_deg)


#--------sol number and 24 hour time format----------♡ 
def get_sol_and_time(state):
    sol = int(state.mission_time_s // seconds_per_sol)
    seconds_into_sol = state.mission_time_s % seconds_per_sol

    hour_24 = seconds_into_sol // 3600
    minute = (seconds_into_sol % 3600) // 60

    return sol, hour_24, minute

#------------decide if it's day or night------------♡ 
def daytime_check(state):
    #I'll finish this later
    _, hour, _ = get_sol_and_time(state)

    is_daytime = 6 <= hour < 20

    return is_daytime

#----------_-----------♡ 
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
    daylight_m2_kw = max_daylight_m2_kw * math.sin(math.pi * daylight_progress)

    return daylight_m2_kw