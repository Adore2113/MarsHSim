#--------------------imports-------------------------♡
from .mars_time import get_daylight_per_m2_kw, get_sunlight_amount, get_daylight_fraction, seconds_per_sol
#----------------------------------------------------♡

# file for greenhouse system

#--------------------constants-----------------------♡
best_sunlight_per_m2_kw = 0.45
min_useful_sunlight_per_m2_kw = 0.15

base_heat_light_power_usage_kw = 0.12

led_power_per_m2_kw = 0.12
led_heat_ratio = 0.68
transpiration_ratio = 0.85

base_power_per_m2_kw = 0.10    # led, pumps, circulation, ect.
greenhouse_heat_per_m2_kw = 0.015

default_health = 0.98
default_light_exposure = 0.65
default_growth_multiplier = 1.0
runoff_water_ratio = 0.08
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

        light_target_kw = zone.get("light_target_kw_per_m2", 0.70)
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


#-----------------zone plant growth------------------♡
def greenhouse_zone_growth(zone, zone_light, sol_fraction):
    area_m2 = zone["effective_grow_area_m2"]
    light_exposure = zone_light["light_exposure"]
    health = zone.get("health", default_health)
    
    base_growth_rate = zone["base_growth_rate_per_sol"]
    growth_multiplier = zone.get("growth_rate_multiplier", 1.0)

    growth_increase = base_growth_rate * growth_multiplier * light_exposure * health * sol_fraction

    new_growth_progress = zone["growth_progress"] + growth_increase
    harvest_ready = new_growth_progress >= 1.0

    food_produced_kg = 0.0
    food_yield = zone["food_yield_per_m2_kg_per_sol"]
    yield_multiplier = zone.get("food_yield_multiplier", 1.0)

    if harvest_ready:
        food_produced_kg = food_yield * area_m2 * yield_multiplier
        new_growth_progress = 0.0
    
    return new_growth_progress, harvest_ready, food_produced_kg


#----------------water / co2 / oxygen----------------♡
def greenhouse_resources(zone, zone_light, sol_fraction):
    area_m2 = zone["effective_grow_area_m2"]
    base_water_needed = zone["base_water_needed_per_m2_kg_per_sol"]
    water_multiplier = zone.get("water_multiplier", 1.0)
    water_recirculation_efficiency = zone.get("water_recirculation_efficiency", 0.93)
    
    light_exposure = zone_light["light_exposure"]
    plant_health = zone.get("health", default_health)

    water_needed_kg = base_water_needed * area_m2 * water_multiplier * sol_fraction    
    water_consumed_kg = water_needed_kg * (1.0 - water_recirculation_efficiency)    # pct of water not recovered
    water_recirculated_kg = water_needed_kg * water_recirculation_efficiency
    water_runoff_kg = runoff_water_kg = water_needed_kg * runoff_water_ratio
    
    transpiration_kg = water_consumed_kg * transpiration_ratio
    plant_mass_water_kg = water_consumed_kg * (1.0 - transpiration_ratio)

    photosynthesis = light_exposure * plant_health

    co2_consumed_per_m2_kpa = zone["co2_consumed_per_m2_kpa_per_sol"]
    total_co2_consumed_kpa = co2_consumed_per_m2_kpa * area_m2 * sol_fraction * photosynthesis

    o2_produced_per_m2_kpa =  zone["o2_produced_per_m2_kpa_per_sol"]
    total_o2_produced_kpa = o2_produced_per_m2_kpa * area_m2 * sol_fraction * photosynthesis

    greenhouse_heat_added_kw = greenhouse_heat_per_m2_kw * area_m2

    return {
        "water_needed_kg": water_needed_kg,
        "water_consumed_kg": water_consumed_kg,
        "water_recirculated_kg": water_recirculated_kg,
        "runoff_water_kg": runoff_water_kg,
        "transpiration_kg": transpiration_kg,
        "plant_mass_water_kg": plant_mass_water_kg,

        "co2_consumed_kpa": total_co2_consumed_kpa,
        "o2_produced_kpa": total_o2_produced_kpa,
        
        "greenhouse_heat_added_kw": greenhouse_heat_added_kw,
    }


#-------------main greenhouse function---------------♡
def run_greenhouse(state, dt_min):
    hours_per_step = dt_min / 60
    sol_fraction = dt_min / (seconds_per_sol / 60.0)
  
    if not state.greenhouse_on:
        return {}, {
            "greenhouse_mode": "offline",
            "total_food_produced_kg": 0.0,
            "total_water_consumed_kg": 0.0,
            "total_co2_consumed_kpa": 0.0,
            "total_o2_produced_kpa": 0.0,
            "transpiration_kg": 0.0,
            "total_greenhouse_heat_kw": 0.0,
            "total_led_power_kw": 0.0,
            "total_led_heat_kw": 0.0,
            "zone_outputs": {}
            }
    
    lighting = greenhouse_lighting(state, dt_min)
    zone_lighting = lighting["zone_lighting"]
    
    total_water_needed_kg = 0.0
    total_water_consumed_kg = 0.0
    total_water_recirculated_kg = 0.0
    total_transpiration_kg = 0.0
    total_runoff_water_kg = 0.0

    total_co2_consumed_kpa = 0.0
    total_o2_produced_kpa = 0.0

    total_food_produced_kg = 0.0
    total_greenhouse_heat_added_kw = 0.0

    new_zones = []
    zone_outputs = {}

    for zone in state.greenhouse_zones:
        zone_name = zone["zone"]
        zone_light = zone_lighting[zone_name]

        new_growth_progress, harvest_ready, food_produced_kg = greenhouse_zone_growth(zone, zone_light, sol_fraction)
        resources = greenhouse_resources(zone, zone_light, sol_fraction)

        total_food_produced_kg += food_produced_kg
        
        total_water_needed_kg += resources["water_needed_kg"]
        total_water_consumed_kg += resources["water_consumed_kg"]
        total_water_recirculated_kg += resources["water_recirculated_kg"]
        total_transpiration_kg += resources["transpiration_kg"]    
        total_runoff_water_kg += resources["runoff_water_kg"]

        total_co2_consumed_kpa += resources["co2_consumed_kpa"]
        total_o2_produced_kpa += resources["o2_produced_kpa"]
        
        total_greenhouse_heat_added_kw += resources["greenhouse_heat_added_kw"]

        new_zone = zone.copy()
        new_zone["growth_progress"] = new_growth_progress
        new_zone["harvest_ready"] = harvest_ready
        new_zone["light_exposure"] = zone_light["light_exposure"]

        new_zones.append(new_zone)

        zone_outputs[zone_name] = {
            "grow_method": zone["grow_method"],
            "light_mode": zone_light["light_mode"],
            "light_exposure": zone_light["light_exposure"],
            "led_level": zone_light["led_level"],
            
            "food_produced_kg": food_produced_kg,
            
            "water_needed_kg": resources["water_needed_kg"],
            "water_consumed_kg": resources["water_consumed_kg"],
            "water_recirculated_kg": resources["water_recirculated_kg"],
            "transpiration_kg": resources["transpiration_kg"],
            "greenhouse_runoff_water_kg": total_runoff_water_kg,

            "co2_consumed_kpa": resources["co2_consumed_kpa"],
            "o2_produced_kpa": resources["o2_produced_kpa"],
            
            "greenhouse_heat_added_kw": resources["greenhouse_heat_added_kw"],

            "growth_progress": new_growth_progress,
            "harvest_ready": harvest_ready,
        }

    #------------dict for updating state-------------♡ 
    greenhouse_updates = {
        "greenhouse_zones": new_zones
    }
    
    #-----------dict for printing outputs------------♡ 
    greenhouse_outputs = {
        "greenhouse_mode": "online",

        "total_food_produced_kg": total_food_produced_kg,

        "total_water_needed_kg": total_water_needed_kg,
        "total_water_consumed_kg": total_water_consumed_kg,
        "total_water_recirculated_kg": total_water_recirculated_kg,
        "transpiration_kg": total_transpiration_kg,

        "total_co2_consumed_kpa": total_co2_consumed_kpa,
        "total_o2_produced_kpa": total_o2_produced_kpa,

        "total_greenhouse_heat_kw": total_greenhouse_heat_added_kw,
        "total_greenhouse_heat_kwh": total_greenhouse_heat_added_kw * hours_per_step,

        "total_led_power_kw": lighting["total_led_power_kw"],
        "total_led_energy_kwh": lighting["total_led_energy_kwh"],
        "total_led_heat_kw": lighting["total_led_heat_kw"],
        "total_led_heat_kwh": lighting["total_led_heat_kwh"],

        "natural_light_kw_per_m2": lighting["natural_light_kw_per_m2"],
        "zone_outputs": zone_outputs,
    }
    
    return greenhouse_updates, greenhouse_outputs
    

    

# gray/black water to water filtration to UPA/WPA to potable to greenhouse

# loop = crew waste to treatment to greenhouse nutriant solutio to plants to humidity to CHX capture to water system!

# pros : massive water recylcing!
