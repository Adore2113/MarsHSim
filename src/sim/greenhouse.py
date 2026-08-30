#--------------------imports-------------------------♡
from .mars_time import get_daylight_per_m2_kw, get_sunlight_amount, get_daylight_fraction, seconds_per_sol, get_sol_time
#----------------------------------------------------♡

# file for greenhouse system

#--------------------constants-----------------------♡
#---sunlight & lighting----♡
best_sunlight_per_m2_kw = 0.45
min_useful_sunlight_per_m2_kw = 0.15

base_heat_light_power_usage_kw = 0.12
led_power_per_m2_kw = 0.12
led_heat_ratio = 0.68
base_gh_light_hours_per_sol = 16.0    # test and try 12 or 14
gh_light_start_hour = 5

#---greenhouse operation---♡
base_power_per_m2_kw = 0.05
gh_heat_per_m2_kw = 0.015
gh_chx_capture_efficency = 0.95

#------greenhouse CHX------♡
gh_condensate_heat_kj_per_kg = 2450.0
base_gh_chx_power_kw = 0.5
gh_chx_running_power_kw = 8.0    # placeholder
gh_chx_waste_heat_ratio = 0.60
gh_chx_capacity_kg_per_hour = 173.0

#-------gas exchange-------♡
pq = 1.03    # photosynthetic quotient
rq = 0.90    # respiratory_quotient

#--------crop model--------♡
transpiration_ratio = 0.95
default_health = 0.98
default_light_exposure = 0.65
default_growth_multiplier = 1.0
#----------------------------------------------------♡


#--------------------timed lights--------------------♡
def are_timed_gh_lights_on(state, gh_light_hours_per_sol):
    _, sol_hour, minutes = get_sol_time(state)
    current_hour = sol_hour + (minutes / 60)
    hours_since_start = (current_hour - gh_light_start_hour) % 24
    
    return hours_since_start < gh_light_hours_per_sol


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

        light_target_kw_per_m2 = zone.get("light_target_kw_per_m2", 0.23)
        light_absorption = zone.get("base_light_absorption_pct", 0.70)
        gh_light_hours_per_sol = zone.get("gh_light_hours_per_sol", base_gh_light_hours_per_sol)

        day_length_bonus = 0.70 + (0.30 * daylight_fraction)
        effective_light_kw_per_m2 = natural_light_kw_per_m2 * light_absorption * day_length_bonus

        if not are_timed_gh_lights_on(state, gh_light_hours_per_sol):
            light_mode = "dark cycle"
            led_level = 0.0

        elif effective_light_kw_per_m2 <= min_useful_sunlight_per_m2_kw:
            light_mode = "full led support"
            led_level = 1.0

        elif effective_light_kw_per_m2 < light_target_kw_per_m2:
            light_mode = "led support"
            led_level = (light_target_kw_per_m2 - effective_light_kw_per_m2) / light_target_kw_per_m2

        else:
            light_mode = "sunlight only"
            led_level = 0.0
        
        if state.power_mode == "low":
            led_level *= 0.6

        elif state.power_mode == "critical":
            led_level *= 0.2

        led_power_kw = led_power_per_m2_kw * area_m2 * led_level
        led_heat_kw = led_power_kw * led_heat_ratio

        total_led_power_kw += led_power_kw
        total_led_heat_kw += led_heat_kw
        
        light_exposure = min(1.0, effective_light_kw_per_m2 / light_target_kw_per_m2 + led_level)

        zone_lighting[zone_name] = {
            "light_mode": light_mode,
            "effective_light_kw_per_m2": effective_light_kw_per_m2,
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


#-----------------------water------------------------♡
def greenhouse_water(zone, sol_fraction):
    area_m2 = zone["effective_grow_area_m2"]
    uptake_rate_kg_per_m2 = zone["plant_water_uptake_kg_per_m2_per_sol"]
    operational_loss_pct = zone.get("operational_water_loss_pct", 0.03)

    plant_water_uptake_kg = uptake_rate_kg_per_m2 * area_m2 * sol_fraction
    transpiration_kg = plant_water_uptake_kg * transpiration_ratio
    plant_mass_water_kg = plant_water_uptake_kg * (1.0 - transpiration_ratio)
 
    gh_condensate_captured_kg = transpiration_kg * gh_chx_capture_efficency
    gh_transpiration_uncaptured_kg = transpiration_kg * (1.0 - gh_chx_capture_efficency)

    operational_loss_kg = plant_water_uptake_kg * operational_loss_pct
    
    make_up_water_kg = plant_mass_water_kg + + gh_transpiration_uncaptured_kg + operational_loss_kg

    return {
        "plant_water_uptake_kg": plant_water_uptake_kg,
        "gh_condensate_captured_kg": gh_condensate_captured_kg,
        "gh_transpiration_uncaptured_kg": gh_transpiration_uncaptured_kg,
        "plant_mass_water_kg": plant_mass_water_kg,
        "operational_loss_kg": operational_loss_kg,
        "make_up_water_kg": make_up_water_kg,
    }


#-------------------gas exchange---------------------♡
def greenhouse_gas_exchange(zone, zone_light, sol_fraction):
    area_m2 = zone["effective_grow_area_m2"]
    light_exposure = zone_light["light_exposure"]
    plant_health = zone.get("health", default_health)

    co2_consumed_mol = 0.0
    co2_released_mol = 0.0
    o2_produced_mol = 0.0
    o2_consumed_mol = 0.0

    if zone_light["light_mode"] == "dark cycle":
        co2_dark_rate = zone["co2_dark_release_mol_per_m2_per_sol"]
        co2_released_mol = co2_dark_rate * area_m2 * sol_fraction * plant_health
        o2_consumed_mol = co2_released_mol / rq

    else:    # photosynthesis active in light mode
        co2_light_rate = zone["co2_light_uptake_mol_per_m2_per_sol"]
        photosynthesis_factor = light_exposure * plant_health
        co2_consumed_mol = co2_light_rate * area_m2 * sol_fraction * photosynthesis_factor
        o2_produced_mol = co2_consumed_mol * pq

    return {
        "co2_consumed_mol": co2_consumed_mol,
        "co2_released_mol": co2_released_mol,
        "o2_produced_mol": o2_produced_mol,
        "o2_consumed_mol": o2_consumed_mol,
    }

#-----------------greenhouse CHX---------------------♡
def greenhouse_chx(total_condensate_captured_kg, dt_min):
    hours_per_step = dt_min / 60.0
    seconds_per_step = dt_min * 60.0

    gh_chx_cooling_kj = total_condensate_captured_kg * gh_condensate_heat_kj_per_kg
    gh_chx_cooling_kw = gh_chx_cooling_kj / seconds_per_step

    max_capacity_kg_this_step = gh_chx_capacity_kg_per_hour * hours_per_step

    if max_capacity_kg_this_step > 0:
        amount_factor = min(1.0, total_condensate_captured_kg / max_capacity_kg_this_step)

    else:
        amount_factor = 0.0

    gh_chx_power_kw = base_gh_chx_power_kw + (gh_chx_running_power_kw - base_gh_chx_power_kw) + amount_factor
    gh_chx_waste_heat_kw = gh_chx_power_kw * gh_chx_waste_heat_ratio
    gh_chx_heat_added_kw = max(0.0, gh_chx_waste_heat_kw - gh_chx_cooling_kw)

    return {
        "gh_chx_power_kw": gh_chx_power_kw,
        "gh_chx_energy_kwh": gh_chx_power_kw * hours_per_step,
        "gh_chx_cooling_kw": gh_chx_cooling_kw,
        "gh_chx_cooling_kwh": gh_chx_cooling_kw * hours_per_step,
        "gh_chx_heat_added_kw": gh_chx_heat_added_kw,
        "gh_chx_heat_added_kwh": gh_chx_heat_added_kw * hours_per_step
    } 

#-------------main greenhouse function---------------♡
def run_greenhouse(state, dt_min):
    hours_per_step = dt_min / 60.0
    sol_fraction = dt_min / (seconds_per_sol / 60.0)
  
    if not state.greenhouse_on:
        return {}, {
            "greenhouse_mode": "offline", "gh_food_produced_kg": 0.0,
            "gh_plant_water_uptake_kg": 0.0, "gh_condensate_captured_kg": 0.0,
            "gh_transpiration_uncaptured_kg": 0.0, "gh_plant_mass_water_kg": 0.0,
            "gh_operational_loss_kg": 0.0, "gh_make_up_water_kg": 0.0,

            "gh_co2_consumed_mol": 0.0, "gh_co2_released_mol": 0.0,
            "gh_o2_produced_mol": 0.0, "gh_o2_consumed_mol": 0.0,

            "total_gh_heat_kw": 0.0, "total_gh_heat_kwh": 0.0,
            "gh_equipment_power_kw": 0.0, "gh_equipment_energy_kwh": 0.0,
            "gh_led_power_kw": 0.0, "gh_led_energy_kwh": 0.0,
            "gh_led_heat_kw": 0.0, "gh_led_heat_kwh": 0.0,
            
            "gh_chx_power_kw": 0.0, "gh_chx_energy_kwh": 0.0,
            "gh_chx_cooling_kw": 0.0, "gh_chx_cooling_kwh": 0.0,
            "gh_chx_heat_added_kw": 0.0, "gh_chx_heat_added_kwh": 0.0,

            "natural_light_kw_per_m2": 0.0, "zone_outputs": {}
            }
    
    lighting = greenhouse_lighting(state, dt_min)
    zone_lighting = lighting["zone_lighting"]
    total_equipment_power_kw = 0.0
 
    total_plant_water_uptake_kg = 0.0
    total_condensate_captured_kg = 0.0
    total_transpiration_kg = 0.0
    total_plant_mass_water_kg = 0.0
    total_operational_loss_kg = 0.0
    total_direct_make_up_kg = 0.0
 
    total_co2_consumed_mol = 0.0
    total_co2_released_mol = 0.0
    total_o2_produced_mol = 0.0
    total_o2_consumed_mol = 0.0
 
    total_food_produced_kg = 0.0
    total_gh_heat_added_kw = 0.0
 
    new_zones = []
    zone_outputs = {}

    for zone in state.greenhouse_zones:
        zone_name = zone["zone"]
        zone_light = zone_lighting[zone_name]

        floor_area = zone.get("floor_area_m2", zone["effective_grow_area_m2"])
        total_equipment_power_kw += base_power_per_m2_kw * floor_area

        new_growth_progress, harvest_ready, food_produced_kg = greenhouse_zone_growth(zone, zone_light, sol_fraction)
        water_results = greenhouse_water(zone, sol_fraction)
        gas_results = greenhouse_gas_exchange(zone, zone_light, sol_fraction)
    
        total_food_produced_kg += food_produced_kg
        
        total_plant_water_uptake_kg += water_results["plant_water_uptake_kg"]
        total_condensate_captured_kg += water_results["gh_condensate_captured_kg"]
        total_transpiration_kg += water_results["gh_transpiration_uncaptured_kg"]
        total_plant_mass_water_kg += water_results["plant_mass_water_kg"]
        total_operational_loss_kg += water_results["operational_loss_kg"]
        total_direct_make_up_kg += water_results["make_up_water_kg"]
 
        total_co2_consumed_mol += gas_results["co2_consumed_mol"]
        total_co2_released_mol += gas_results["co2_released_mol"]
        total_o2_produced_mol += gas_results["o2_produced_mol"]
        total_o2_consumed_mol += gas_results["o2_consumed_mol"]
        
        gh_heat_added_kw = gh_heat_per_m2_kw * zone["effective_grow_area_m2"]
        total_gh_heat_added_kw += gh_heat_added_kw

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
            
            "plant_water_uptake_kg": water_results["plant_water_uptake_kg"],
            "gh_condensate_captured_kg": water_results["gh_condensate_captured_kg"],
            "gh_transpiration_uncaptured_kg": water_results["gh_transpiration_uncaptured_kg"],
            "plant_mass_water_kg": water_results["plant_mass_water_kg"],
            "operational_loss_kg": water_results["operational_loss_kg"],
            "make_up_water_kg": water_results["make_up_water_kg"],
 
            "co2_consumed_mol": gas_results["co2_consumed_mol"],
            "co2_released_mol": gas_results["co2_released_mol"],
            "o2_produced_mol": gas_results["o2_produced_mol"],
            "o2_consumed_mol": gas_results["o2_consumed_mol"],
            
            "gh_heat_added_kw": gh_heat_added_kw,
            
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
        "gh_food_produced_kg": total_food_produced_kg,
 
        "gh_plant_water_uptake_kg": total_plant_water_uptake_kg,
        "gh_condensate_captured_kg": total_condensate_captured_kg,
        "gh_transpiration_uncaptured_kg": total_transpiration_kg,
        "gh_plant_mass_water_kg": total_plant_mass_water_kg,
        "gh_operational_loss_kg": total_operational_loss_kg,
        "gh_make_up_water_kg": total_direct_make_up_kg,
 
        "gh_co2_consumed_mol": total_co2_consumed_mol,
        "gh_co2_released_mol": total_co2_released_mol,
        "gh_o2_produced_mol": total_o2_produced_mol,
        "gh_o2_consumed_mol": total_o2_consumed_mol,
 
        "total_gh_heat_kw": total_gh_heat_added_kw,
        "total_gh_heat_kwh": total_gh_heat_added_kw * hours_per_step,
       
        "gh_equipment_power_kw": total_equipment_power_kw,
        "gh_equipment_energy_kwh": total_equipment_power_kw * hours_per_step,
 
        "gh_led_power_kw": lighting["total_led_power_kw"],
        "gh_led_energy_kwh": lighting["total_led_energy_kwh"],
        "gh_led_heat_kw": lighting["total_led_heat_kw"],
        "gh_led_heat_kwh": lighting["total_led_heat_kwh"],
 
        "gh_chx_power_kw": chx_results["gh_chx_power_kw"],
        "gh_chx_energy_kwh": chx_results["gh_chx_energy_kwh"],
        "gh_chx_cooling_kw": chx_results["gh_chx_cooling_kw"],
        "gh_chx_cooling_kwh": chx_results["gh_chx_cooling_kwh"],
        "gh_chx_heat_added_kw": chx_results["gh_chx_heat_added_kw"],
        "gh_chx_heat_added_kwh": chx_results["gh_chx_heat_added_kwh"],

        "natural_light_kw_per_m2": lighting["natural_light_kw_per_m2"],
        "zone_outputs": zone_outputs,
    }
    
    return greenhouse_updates, greenhouse_outputs
    