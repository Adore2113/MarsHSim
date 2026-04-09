import math
from dataclasses import replace
from .state import Habitat_State

#--------------------constants-----------------------♡
seconds_per_sol = 88775     # one mars sol is 24h 39min 35sec
hours_per_sol = seconds_per_sol / 3600
sols_per_year = 668.6     # one full Mars orbit

# habitat location = 47° North, 184° East (Arcadia Planitia)
longitude_east_deg = 184.0
latitude_north_deg = 47.0

# ls = areocentric solar longitude (season angle)
solar_longitude_ls_deg_spring = 0    # equinox
solar_longitude_ls_deg_summer = 90    # solstice
solar_longitude_ls_deg_autumn = 180    # equinox
solar_longitude_ls_deg_winter = 270    # solstice

mars_axial_tilt_deg = 25.19    # how much Mars is tilted for changing sun angle 

max_daylight_m2_kw = 0.57
#----------------------------------------------------♡


#--------------time within current sol---------------♡
def sol_time_seconds(mission_time_s):
    return mission_time_s % seconds_per_sol


#----------------current sol number-----------------♡
def current_sol_number(mission_time_s):
    return mission_time_s // seconds_per_sol


#----------------24 hour time format-----------------♡ 
def get_sol_time(state):
    sol_number = state.mission_time_s // seconds_per_sol
    sol_seconds = sol_time_seconds(state.mission_time_s)

    sol_hour = sol_seconds // 3600
    minutes = (sol_seconds % 3600) // 60
    
    return sol_number, sol_hour, minutes


#----------------current season angle----------------♡ 
def season_angle_deg(mission_time_s):    # ls = areocentric solar longitude (season angle)
    seconds_per_year = sols_per_year * seconds_per_sol
    degrees_per_second = 360.0 / seconds_per_year

    current_season_angle_deg = (mission_time_s * degrees_per_second) % 360
    
    return current_season_angle_deg


#-------how far the sun is shifted in the sky--------♡ 
def solar_declination_deg(state):
    current_season_angle_deg = season_angle_deg(state.mission_time_s)
    solar_decline_deg = mars_axial_tilt_deg * math.sin(math.radians(current_season_angle_deg))

    return solar_decline_deg


#----------what fraction of sol is daylight----------♡ 
def daylight_fraction_result(state):
    latitude_north_rad = math.radians(latitude_north_deg)    #controls day length
    solar_declination_rad = math.radians(solar_declination_deg(state))

    sun_visibility = -math.tan(latitude_north_rad) * math.tan(solar_declination_rad)    # how extreme the sun's tilt is vs how extreme the habitat position is

    if sun_visibility <= -1:
        daylight_fraction = 1.0
        return daylight_fraction
    
    if sun_visibility >= 1:
        daylight_fraction = 0.0
        return daylight_fraction

    sun_visibility_half_rad = math.acos(sun_visibility)
    daylight_fraction = sun_visibility_half_rad / math.pi
    
    return daylight_fraction


#---sunset/sunrise (when daylight starts and ends)--♡
def sunrise_sunset_seconds(state):
    current_daylight_fraction = daylight_fraction_result(state)
    
    daylight_seconds = int(seconds_per_sol * current_daylight_fraction)
    night_seconds = seconds_per_sol - daylight_seconds
    half_night_seconds = night_seconds // 2
    sunrise_seconds = half_night_seconds
    sunset_seconds = sunrise_seconds + daylight_seconds
    return sunrise_seconds, sunset_seconds


#-------------calculate sunlight amount-------------♡
def determine_sunlight_amount(state):
    current_sol_seconds = sol_time_seconds(state.mission_time_s)
    sunrise_seconds, sunset_seconds = sunrise_sunset_seconds(state)

    if current_sol_seconds < sunrise_seconds or current_sol_seconds > sunset_seconds:
        sunlight_fraction = 0.0
        return sunlight_fraction

    daylight_seconds = sunset_seconds - sunrise_seconds
    
    if daylight_seconds == 0:
        sunlight_amount = 0.0
        return sunlight_amount
    
    seconds_since_sunrise = current_sol_seconds - sunrise_seconds
    daylight_amount = seconds_since_sunrise / daylight_seconds

    sunlight_amount = math.sin(math.pi * daylight_amount)
    
    return sunlight_amount


#-------------low sunlight streak info--------------♡
def determine_low_sunlight_streak(state):
    low_sunlight = 0.3

    if state.peak_sunlight_today < low_sunlight:
        new_low_sunlight_streak_sols = state.low_sunlight_streak_sols + 1
    
    else:
        new_low_sunlight_streak_sols = 0
    
    return new_low_sunlight_streak_sols


#---------------solar generation info---------------♡
def daylight_per_m2_kw(state):
    sunlight_amount = determine_sunlight_amount(state)
    daylight_per_m2_kw = max_daylight_m2_kw * sunlight_amount
    
    return daylight_per_m2_kw