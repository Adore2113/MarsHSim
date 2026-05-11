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

base_power_per_m2_kw = 0.10    # led, pumps, circulation, ect.
#----------------------------------------------------♡


#----------------greenhouse lighting-----------------♡
def greenhouse_lighting(state, dt_min):
    hours_per_step = dt_min / 60
    sunlight_intensity = get_sunlight_amount(state)
    daylight_fraction = get_daylight_fraction(state)

    natural_light_kw = sunlight_intensity * get_daylight_per_m2_kw(state)   

    zone_light_targets_kw = {"structural": 0.85, "container": 0.70, "rack": 0.60}

    #---------------------defaults-------------------♡
    total_led_power_usage_kw = 0.0
    total_led_heat_kw = 0.0
    zone_results = {}

    #-------------adjust light for zones-------------♡
    for zone in state.greenhouse_zones:
        zone_name = zone["zone"]
        area_m2 = zone["area_m2"]
        
        target_light = zone_light_targets_kw.get(zone_name, 0.70)
        zone_absorption = zone["base_light_absorption_pct"]
        day_length_bonus = 0.70 + (0.3 * daylight_fraction) 

        effective_daylight_kw = natural_light_kw * zone_absorption * day_length_bonus

        if effective_daylight_kw <= min_useful_sunlight_per_m2_kw:
            led_level = 1.0
            light_mode = "Low Sunlight"
        
        elif effective_daylight_kw < target_light:
            led_level = (target_light - effective_daylight_kw) / target_light
            light_mode = "LED Needed"
        
        else:
            led_level = 0.0
            light_mode = "Optimal Sunlight"

        led_power_usage_kw = led_power_per_m2_kw * area_m2 * led_level
        led_heat_kw = led_power_usage_kw * led_heat_ratio
        
        total_led_power_usage_kw += led_power_usage_kw
        total_led_heat_kw += led_heat_kw
        
        new_light_exposure = min(1.0, effective_daylight_kw / target_light + led_level)

        zone_results[zone_name] = {
            "light_mode": light_mode,
            "effective_light_kw": effective_daylight_kw,
            "led_level": led_level,
            "led_power_usage_kw": led_power_usage_kw,
            "led_heat_kw": led_heat_kw,
            "new_light_exposure": new_light_exposure,
            }

    return {
        "gh_lighting_mode": "active",        
        "natural_light_kw": natural_light_kw,
        
        "total_led_power_kw": total_led_power_usage_kw,
        "total_led_energy_kwh": total_led_power_usage_kw * hours_per_step,

        "total_led_heat_kw": total_led_heat_kw,
        "total_led_heat_kwh": total_led_heat_kw * hours_per_step,

        "zone_lighting": zone_results, 
    }

#-------------main greenhouse function---------------♡
def run_greenhouse(state, dt_min):
    hours_per_step = dt_min * 60
    sol_fraction = dt_min / (24 * 60.0)

    if state.greenhouse_on == False:
        greenhouse_mode = "offline"
    
    lighting = greenhouse_lighting(state, dt_min)
    natural_light_kw = lighting["natural_light_kw"]

    #-----------default greenhouse values-----------♡  
    total_co2_kpa = 0.0
    total_co2_consumed_kpa = 0.0
    total_water_used_kg = 0.0
    total_food_produced_kg = 0.0
    total_power_used_kw = 0.0
    total_heat_added = 0.0

    new_zones = []
    
# growth speed
    
# O2/CO2 exchange rate
  
# food yield
  
# water use
  
# gray/black water to water filtration to UPA/WPA to potable to greenhouse

# loop = crew waste to treatment to greenhouse nutriant solutio to plants to humidity to CHX capture to water system!

# pros : massive water recylcing!

# cons: nutrient imbalance and pathogens (plant disease)

#--------------greenhouse water usage--------------♡