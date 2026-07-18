#--------------------imports-------------------------♡
import math
#----------------------------------------------------♡


#--------------------constants-----------------------♡
seconds_per_sol = 88775.244     # one mars sol is 24h 39min 35sec
sols_per_year = 668.599     # one full Mars orbit
seconds_per_mars_year = sols_per_year * seconds_per_sol
degrees_per_second = 360.0 / seconds_per_mars_year

# habitat location (Arcadia Planitia)
latitude_north_deg = 47.0
longitude_east_deg = 184.0

mars_axial_tilt_deg = 25.19    # how much Mars is tilted for changing sun angle 
mars_orbit_eccentricity = 0.0934
mars_ls_perihelion_deg = 251.0    # ls = areocentric solar longitude (season angle), perihelion = closest to the sun

max_daylight_m2_kw = 0.57
low_sunlight_kw = 0.3    # < 0.3 sunlight per m2 = low sunlight
#----------------------------------------------------♡


#--------------time within current sol---------------♡
def sol_time_seconds(mission_time_s):
    return mission_time_s % seconds_per_sol


#----------------current sol number------------------♡
def current_sol_number(mission_time_s):
    return int(mission_time_s // seconds_per_sol)


#----------------24 hour time format-----------------♡ 
def get_sol_time(state):
    sol_number = int(state.mission_time_s // seconds_per_sol)
    sol_seconds = sol_time_seconds(state.mission_time_s)
    
    mars_hour_length_s = seconds_per_sol/ 24
    mars_minute_length_s = mars_hour_length_s / 60

    sol_hour = int(sol_seconds // mars_hour_length_s)
    minutes = int((sol_seconds % mars_hour_length_s) // mars_minute_length_s)
    
    return sol_number, sol_hour, minutes

#-----areocentric solar longitude (season angle)-----♡ 
def true_to_mean_anomaly_deg(true_anomaly_deg, eccentricity):
    # true anomaly deg: actual position angle in orbit
    # mean anomaly deg: time based orbital progress angle
    # eccentricity: how not circular the orbit is
    
    true_anomaly_rad = math.radians(true_anomaly_deg)
    half_true_anomaly_rad = true_anomaly_rad / 2
    
    sin_part = math.sqrt(1 - eccentricity) * math.sin(half_true_anomaly_rad)
    cos_part = math.sqrt(1 + eccentricity) * math.cos(half_true_anomaly_rad)

    eccentric_anomaly_rad = 2 * math.atan2(sin_part, cos_part)

    mean_anomaly_rad = eccentric_anomaly_rad - eccentricity * math.sin(eccentric_anomaly_rad)
    mean_anomaly_deg = math.degrees(mean_anomaly_rad) % 360
    
    return mean_anomaly_deg

def mean_to_true_anomaly_deg(mean_anomaly_deg, eccentricity):
    mean_anomaly_rad = math.radians(mean_anomaly_deg % 360)
    eccentric_anomaly_rad = mean_anomaly_rad

    for _ in range(5):
        kepler_error = eccentric_anomaly_rad - eccentricity * math.sin(eccentric_anomaly_rad) - mean_anomaly_rad
        kepler_slope = 1 - eccentricity * math.cos(eccentric_anomaly_rad)
        
        eccentric_anomaly_rad -= kepler_error / kepler_slope

    half_eccentric_anomaly_rad = eccentric_anomaly_rad / 2

    sin_part = math.sqrt(1 + eccentricity) * math.sin(half_eccentric_anomaly_rad)
    cos_part = math.sqrt(1 - eccentricity) * math.cos(half_eccentric_anomaly_rad)
    
    true_anomaly_rad = 2 * math.atan2(sin_part, cos_part)    
    true_anolamly_deg = math.degrees(true_anomanly_rad) % 360

    return true_anolamly_deg

#-------how far the sun is shifted in the sky--------♡ 
def get_solar_decline_deg(state):
    season_angle_deg = get_ls_deg(state.mission_time_s)
    solar_decline_deg = mars_axial_tilt_deg * math.sin(math.radians(ls_deg))

    return solar_decline_deg


#----------what fraction of sol is daylight----------♡ 
def get_daylight_fraction(state):
    latitude_rad = math.radians(latitude_north_deg)    #controls day length
    solar_declination_rad = math.radians(get_solar_decline_deg(state))

    sun_visibility = -math.tan(latitude_rad) * math.tan(solar_declination_rad)    # how extreme the sun's tilt is vs how extreme the habitat position is

    if sun_visibility <= -1.0:
        return 1.0

    if sun_visibility >= 1.0:
        return 0.0

    sun_visibility_half_rad = math.acos(sun_visibility)
    daylight_fraction = sun_visibility_half_rad / math.pi
    
    return daylight_fraction


#-----------when daylight starts and ends-----------♡
def sunrise_sunset_seconds(state):
    current_daylight_fraction = get_daylight_fraction(state)
    
    daylight_seconds = seconds_per_sol * current_daylight_fraction
    night_seconds = seconds_per_sol - daylight_seconds
    
    sunrise_seconds = night_seconds / 2
    sunset_seconds = sunrise_seconds + daylight_seconds
    
    return sunrise_seconds, sunset_seconds


#-------------calculate sunlight amount-------------♡
def get_sunlight_amount(state):
    current_sol_seconds = sol_time_seconds(state.mission_time_s)
    sunrise_seconds, sunset_seconds = sunrise_sunset_seconds(state)

    if current_sol_seconds < sunrise_seconds or current_sol_seconds >= sunset_seconds:
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