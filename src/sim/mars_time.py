#--------------------imports-------------------------♡
import math
#----------------------------------------------------♡


#--------------------constants-----------------------♡
seconds_per_sol = 88775.244     # one mars sol is 24h 39min 35sec
sols_per_year = 668.599     # one full Mars orbit
seconds_per_mars_year = sols_per_year * seconds_per_sol
degrees_per_second = 360.0 / seconds_per_mars_year

# habitat location = 47° North, 184° East (Arcadia Planitia)
latitude_north_deg = 47.0
longitude_east_deg = 184.0

mars_axial_tilt_deg = 25.19    # how much Mars is tilted for changing sun angle 
max_daylight_m2_kw = 0.57
low_sunlight_kw = 0.3    # < 0.3 sunlight per m2 = low sunlight

#----------------------------------------------------♡


#--------------time within current sol---------------♡
def sol_time_seconds(mission_time_s):
    return mission_time_s % seconds_per_sol


#----------------current sol number------------------♡
def current_sol_number(mission_time_s):
    return mission_time_s // seconds_per_sol


#----------------24 hour time format-----------------♡ 
def get_sol_time(state):
    sol_number = state.mission_time_s // seconds_per_sol
    sol_seconds = sol_time_seconds(state.mission_time_s)
    sol_hour = int(sol_seconds // 3600)
    minutes = int((sol_seconds % 3600) // 60)
    
    return sol_number, sol_hour, minutes


#----------------current season angle----------------♡ 
def get_season_angle_deg(mission_time_s):
    season_angle_deg = (mission_time_s * degrees_per_second) % 360
    
    return season_angle_deg


#-------how far the sun is shifted in the sky--------♡ 
def get_solar_decline_deg(state):
    season_angle_deg = get_season_angle_deg(state.mission_time_s)
    solar_decline_deg = mars_axial_tilt_deg * math.sin(math.radians(season_angle_deg))

    return solar_decline_deg


#----------what fraction of sol is daylight----------♡ 
def get_daylight_fraction(state):
    latitude_rad = math.radians(latitude_north_deg)    #controls day length
    solar_declination_rad = math.radians(get_solar_decline_deg(state))

    sun_visibility = -math.tan(latitude_rad) * math.tan(solar_declination_rad)    # how extreme the sun's tilt is vs how extreme the habitat position is

    if sun_visibility <= -1.0:
        return 0.0

    if sun_visibility >= 1.0:
        return 1.0

    sun_visibility_half_rad = math.acos(sun_visibility)
    daylight_fraction = sun_visibility_half_rad / math.pi
    
    return daylight_fraction


#-----------when daylight starts and ends-----------♡
def sunrise_sunset_seconds(state):
    current_daylight_fraction = get_daylight_fraction(state)
    
    daylight_seconds = int(seconds_per_sol * current_daylight_fraction)
    night_seconds = seconds_per_sol - daylight_seconds
    sunrise_seconds = night_seconds // 2
    sunset_seconds = sunrise_seconds + daylight_seconds
    
    return sunrise_seconds, sunset_seconds


#-------------calculate sunlight amount-------------♡
def get_sunlight_amount(state):
    current_sol_seconds = sol_time_seconds(state.mission_time_s)
    sunrise_seconds, sunset_seconds = sunrise_sunset_seconds(state)

    if current_sol_seconds < sunrise_seconds or current_sol_seconds > sunset_seconds:
        sunlight_amount = 0.0
    
    else:
        daylight_seconds = sunset_seconds - sunrise_seconds
        
        if daylight_seconds <= 0:
            sunlight_amount = 0.0
        
        else:
            seconds_since_sunrise = current_sol_seconds - sunrise_seconds
            daylight_amount = seconds_since_sunrise / daylight_seconds
            sunlight_amount = math.sin(math.pi * daylight_amount)
            
    return sunlight_amount


#---------------solar generation info----------------♡
def get_daylight_per_m2_kw(state):
    daylight_per_m2 = max_daylight_m2_kw * get_sunlight_amount(state)
    
    return daylight_per_m2


#--------------define northern seasons---------------♡
def current_mars_season(state):
    season_angle_deg = get_season_angle_deg(state.mission_time_s)
    # ls = areocentric solar longitude (season angle)

    if 0 <= season_angle_deg < 90:
        return "northern_spring" 
    
    elif 90 <= season_angle_deg < 180:
        return "northern_summer" 
    
    elif 180 <= season_angle_deg < 270:
        return "northern_autumn" 
    
    else:
        return "northern_winter"
    

#--------------low sunlight streak info--------------♡
def get_low_sunlight_streak(state):
    if state.peak_sunlight_today < low_sunlight_kw:
        new_low_sunlight_streak_sols = state.low_sunlight_streak_sols + 1
    
    else:
        new_low_sunlight_streak_sols = 0
    
    return new_low_sunlight_streak_sols