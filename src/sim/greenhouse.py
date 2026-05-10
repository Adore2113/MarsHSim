#--------------------imports-------------------------♡
from .mars_time import get_daylight_per_m2_kw, get_sunlight_amount, get_daylight_fraction
#----------------------------------------------------♡

# file for greenhouse system

#--------------------constants-----------------------♡
greenhouse_temp_target_c = 24    # break this up into a few different heat light areas for different plants

best_sunlight_per_m2_kw = 0.45
min_useful_sunlight_per_m2_kw = 0.15

base_heat_light_power_usage_kw = 0.12

led_power_per_m2_kw = 0.12
led_heat_ratio = 0.68

food_yield_per_m2_kg_per_sol = 0.085    # start off with no food yeild? make into seperate variables for each food yield

co2_consumed_per_m2_kpa_per_sol = 0.025
o2_produced_per_m2_kpa_per_sol = 0.020

base_light_absorption_pct = 0.7    # plants soak up 70% of sunlight from the amount avaliable
base_power_per_m2_kw = 0.10    # led, pumps, circulation, ect.
base_water_needed_per_m2_kg_per_sol = 3.3
#----------------------------------------------------♡


#----------------greenhouse lighting-----------------♡
def greenhouse_lighting(state, dt_min):
    hours_per_step = dt_min / 60
    sunlight_intensity = get_sunlight_amount(state)
    daylight_fraction = get_daylight_fraction(state)

    natural_light_kw = sunlight_intensity * get_daylight_per_m2_kw(state)
    day_length_bonus = base_light_absorption_pct + (0.3 * daylight_fraction) 

    effective_daylight_kw = natural_light_kw * day_length_bonus

    #-----------decide if LEDs are needed------------♡
    if effective_daylight_kw <= min_useful_sunlight_per_m2_kw:
        gh_lighting_mode = "Low Sunlight"
        led_level = 1.0

    elif effective_daylight_kw < best_sunlight_per_m2_kw:
        gh_lighting_mode = "LED needed"
        led_level = (best_sunlight_per_m2_kw - effective_daylight_kw) / best_sunlight_per_m2_kw

    else:
        gh_lighting_mode = "Optimal Sunlight"
        led_level = 0.0
    
    led_power_usage_kw = led_power_per_m2_kw * state.greenhouse_floor_area_m2 * led_level

    return(
        gh_lighting_mode,
        natural_light_kw,
        effective_daylight_kw,
        led_level,
        led_power_usage_kw,
        daylight_fraction,
        )

# growth speed
    
# O2/CO2 exchange rate
  
# food yield
  
# water use
  
# gray/black water to water filtration to UPA/WPA to potable to greenhouse

# loop = crew waste to treatment to greenhouse nutriant solutio to plants to humidity to CHX capture to water system!

# pros : massive water recylcing!

# cons: nutrient imbalance and pathogens (plant disease)

#--------------greenhouse water usage--------------♡