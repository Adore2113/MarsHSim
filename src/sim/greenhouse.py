#--------------------imports-------------------------♡
from .mars_time import get_daylight_per_m2_kw, get_sunlight_amount, get_daylight_fraction
#----------------------------------------------------♡

# file for greenhouse system

#--------------------constants-----------------------♡
best_sunlight_per_m2_kw = 0.45
min_useful_sunlight_per_m2_kw = 0.15

base_heat_light_power_usage_kw = 0.12

led_power_per_m2_kw = 0.12
led_heat_ratio = 0.68

base_power_per_m2_kw = 0.10    # led, pumps, circulation, ect.
#----------------------------------------------------♡


#----------------greenhouse lighting-----------------♡
def greenhouse_lighting(state, dt_min):
    hours_per_step = dt_min / 60.0

    sunlight_intensity = get_sunlight_amount(state)
    daylight_fraction = get_daylight_fraction(state)

    natural_light_kw_per_m2 = sunlight_intensity * get_daylight_per_m2_kw(state)

    total_led_power_kw = 0.0
    total_led_heat_kw = 0.0
    zone_lighting = {}

    for zone in state.greenhouse_zones:
        zone_name = zone["zone"]
        area_m2 = zone["effective_grow_area_m2"]

        light_target_kw = zone.get("light_target_kw", 0.70)
        light_absorption = zone.get("base_light_absorption_pct", 0.70)

        day_length_bonus = 0.70 + (0.30 * daylight_fraction)

        effective_light_kw = natural_light_kw_per_m2 * light_absorption * day_length_bonus

        if effective_light_kw <= min_useful_sunlight_per_m2_kw:
            light_mode = "low sunlight"
            led_level = 1.0

        elif effective_light_kw < light_target_kw:
            light_mode = "led support"
            led_level = (light_target_kw - effective_light_kw) / light_target_kw

        else:
            light_mode = "sunlight only"
            led_level = 0.0

        led_power_kw = led_power_per_m2_kw * area_m2 * led_level
        led_heat_kw = led_power_kw * led_heat_ratio

        total_led_power_kw += led_power_kw
        total_led_heat_kw += led_heat_kw
        
        light_exposure = min(1.0, effective_light_kw / light_target_kw + led_level)

        zone_lighting[zone_name] = {
            "light_mode": light_mode,
            "effective_light_kw": effective_light_kw,
            "led_level": led_level,
            "led_power_kw": led_power_kw,
            "led_heat_kw": led_heat_kw,
            "light_exposure": light_exposure,
        }

    return {
        "natural_light_kw_per_m2": natural_light_kw_per_m2,

        "total_led_power_kw": total_led_power_kw,
        "total_led_energy_kwh": total_led_power_kw * hours_per_step,

        "total_led_heat_kw": total_led_heat_kw,
        "total_led_heat_kwh": total_led_heat_kw * hours_per_step,

        "zone_lighting": zone_lighting,
    }


#-------------main greenhouse function---------------♡
def run_greenhouse(state, dt_min):
    hours_per_step = dt_min * 60
    sol_fraction = dt_min / (24 * 60.0)
  
    if state.greenhouse_on == False:
        greenhouse_mode = "offline"
    
    lighting = greenhouse_lighting(state, dt_min)
    zone_lighting = lighting["zone_lighting"]
    
    #-----------default greenhouse values-----------♡  
    total_co2_kpa = 0.0
    total_co2_consumed_kpa = 0.0
    total_water_consumed_kg = 0.0
    total_food_produced_kg = 0.0
    total_power_used_kw = 0.0
    total_heat_added = 0.0

    new_zones = []

    for zone in state.greenhouse_zones:
        zone_name = zone["zone"]
        area_m2 = zone["area_m2"]
        
        zone_light = zone_lighting[zone_name]
        natural_light_kw = zone_light["natural_light_kw"]
        
        target_light_kw = zone.get("light_target_kw", 0.70)
        
        if target_light_kw > 0:
            light_growth_efficiency = natural_light_kw / target_light_kw
        
        else:
            light_growth_efficiency = 0.0
        
        growth_rate = zone["base_growth_rate_per_sol"] * zone.get("growth_rate_multiplier", 1.0)
        daily_growth = growth_rate * light_growth_efficiency

        new_growth_progress = zone["growth_progress"] + daily_growth

        harvest_ready = new_growth_progress >= 1.0
        
        if harvest_ready:
            food_yeild = zone["food_yield_per_m2_kg_per_sol"] * area_m2 * zone.get("food_yield_multiplier", 1.0)
            total_food_produced_kg += food_yeild

            new_growth_progress = 0.0

        water_consumed_kg = zone["base_water_needed_per_m2_kg_per_sol"] * area_m2 * zone.get("water_multiplier")
        co2_consumed = zone["co2_consumed_per_m2_kpa_per_sol"] * area_m2
        o2_produced = zone["o2_produced_per_m2_kpa_per_sol"] * area_m2
    
        total_water_consumed_kg += water_consumed_kg
        total_co2_consumed_kpa += co2_consumed
        total_o2_produced_kpa += o2_produced
        total_bio_heat_added_kw += 0.015 * area_m2

        new_zones.append({"growth_progress": new_growth_progress, "harvest_ready": harvest_ready})
    
    #------------dict for updating state-------------♡ 
    greenhouse_updates = {
        "greenhouse_zones": new_zones
    }
    
    #-----------dict for printing outputs------------♡ 
    greenhouse_outputs = {
        "greenhouse_mode": "online",
        
        "total_food_produced_kg": total_food_produced_kg,
        
        "total_water_consumed_kg": total_water_consumed_kg,
        "total_co2_consumed_kpa": total_co2_consumed_kpa,
        "total_o2_produced_kpa": total_o2_produced_kpa,
        "total_bio_heat_kw": total_bio_heat_added_kw,
        "total_bio_heat_kwh": total_bio_heat_added_kw * hours_per_step,
        
        "lighting": lighting,
    }
    
    return greenhouse_updates, greenhouse_outputs
    

# growth speed
    
# O2/CO2 exchange rate
  
# food yield
  
# water use
  
# gray/black water to water filtration to UPA/WPA to potable to greenhouse

# loop = crew waste to treatment to greenhouse nutriant solutio to plants to humidity to CHX capture to water system!

# pros : massive water recylcing!

# cons: nutrient imbalance and pathogens (plant disease)

#--------------greenhouse water usage--------------♡