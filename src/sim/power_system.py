#--------------------imports-------------------------♡
from .mars_time import get_sol_time, determine_sunlight_amount
#----------------------------------------------------♡


#--------------------constants-----------------------♡
min_arrays_online = 6
max_arrays_online = 10
target_power_usage_ratio = 0.85

base_light_power_kw = 2.0
base_light_heat_kw = 0.5

base_w_light_power_kw = 0.5
base_w_light_heat_kw = 0.1

min_light_level = 0.2
solar_hysteresis = 0.05
#---------------------------------------------------♡


#-----------which solar arrays are online------------♡
def solar_arrays_online(state):
    new_solar_arrays = []
    solar_arrays_online_count = 0

    battery_pct = state.battery_stored_kwh / state.battery_max_capacity_kwh
    
    #---------how many arrays needed online---------♡  
    if state.daylight_m2_kw < 0.1:
        target_arrays_online = 0
    
    elif battery_pct < (0.25 - solar_hysteresis):
        target_arrays_online = max_arrays_online
    
    elif battery_pct < (0.50 - solar_hysteresis):
        target_arrays_online = 8
    
    else:
        target_arrays_online = min_arrays_online

    #---------handling primary arrays first---------♡  
    primary_arrays_needed = target_arrays_online

    for array in state.solar_arrays:
        new_array = array.copy()

        if new_array["status"] == "standby" and primary_arrays_needed > 0:
            if new_array["type"] == "primary":
                new_array["status"] = "online"
                primary_arrays_needed -= 1

            elif new_array["type"] == "backup" and primary_arrays_needed <= 2:
                new_array["status"] = "online"

    #---------------switch to standby---------------♡ 
        elif new_array["status"] == "online":
            if solar_arrays_online_count >= target_arrays_online:
                
                if new_array["type"] == "backup" or solar_arrays_online_count > target_arrays_online:
                    new_array["status"] = "standby"

        if new_array["status"] == "online":
            solar_arrays_online_count += 1

        new_solar_arrays.append(new_array)

    return new_solar_arrays, solar_arrays_online_count


#--------calculate solar power generated amount-------♡
def solar_generation(state, new_solar_arrays, dt_min):
    hours_per_step = dt_min / 60
    power_generated_per_array = []
    total_solar_generated_kw = 0.0

    for array in new_solar_arrays:
        if array["status"] == "online":
            power_generated_kw = (state.daylight_m2_kw * array["area_m2"] * array["efficiency"] * array["dust_factor"])

        else:
            power_generated_kw = 0.0

        power_generated_per_array.append({"id": array["id"], "power_generated_kw": power_generated_kw})
        total_solar_generated_kw += power_generated_kw
        
    total_solar_generated_kwh = total_solar_generated_kw * hours_per_step

    return total_solar_generated_kw, total_solar_generated_kwh, power_generated_per_array


#--------save solar power generated to storage-------♡
def solar_battery_charge(state, total_solar_generated_kwh):
    if state.battery_stored_kwh < state.battery_max_capacity_kwh:
        new_battery_stored_kwh = min(state.battery_max_capacity_kwh, state.battery_stored_kwh + total_solar_generated_kwh)

    else:
        new_battery_stored_kwh = state.battery_stored_kwh
    
    return new_battery_stored_kwh


#-----------habitat main light power info------------♡
def lights(state, dt_min):
    hours_per_step = dt_min / 60
    _, sol_hour, minutes = get_sol_time(state)
    sunlight_amount = determine_sunlight_amount(state)
    
    crew_awake_hours = 6 <= sol_hour < 21 or (sol_hour == 21 and minutes < 30)

    if crew_awake_hours:
        base_light_level = min_light_level

    else:
        base_light_level = 1.0

    sunlight_dimming = sunlight_amount * 0.6    # sunlight level changes light level need for power saving
    light_level_dimmed = base_light_level - sunlight_dimming
    
    final_light_level = max(min_light_level, light_level_dimmed)

    light_power_used_kw = base_light_power_kw * final_light_level
    light_energy_used_kwh = light_power_used_kw * hours_per_step

    light_heat_kw =  base_light_heat_kw* final_light_level
    light_heat_kwh = light_heat_kw * hours_per_step

    return {
        "final_light_level": final_light_level,
        "light_heat_kw": light_heat_kw,
        "light_heat_kwh": light_heat_kwh,
        "light_power_used_kw": light_power_used_kw,
        "light_energy_used_kwh": light_energy_used_kwh
        }


#--------wellness lights from lack of sunlight-------♡
def wellness_lights(state, dt_min):
    hours_per_step = dt_min / 60
    low_sunlight_streak = state.low_sunlight_streak_sols

    #----------------hysteresis----------------------♡
    if low_sunlight_streak >= 3:
        wellness_lights_on = True
        wellness_light_level = 1.0
    
    elif low_sunlight_streak <= 1:
        wellness_lights_on = False
        wellness_light_level = 0.0
    
    else:
        wellness_lights_on = state.wellness_lights_on
    
    w_light_power_used_kw = base_w_light_power_kw * wellness_light_level
    w_light_energy_used_kwh = w_light_power_used_kw * hours_per_step

    w_light_heat_kw =  base_w_light_heat_kw * wellness_light_level
    w_light_heat_kwh = w_light_heat_kw * hours_per_step

    return {
            "wellness_lights_on": wellness_lights_on,
            "wellness_light_level": wellness_light_level,
            "w_light_power_used_kw": w_light_power_used_kw,
            "w_light_energy_used_kwh": w_light_energy_used_kwh,
            "w_light_heat_kw": w_light_heat_kw,
            "w_light_heat_kwh": w_light_heat_kwh
        }    


#------------------total power usage-----------------♡
def get_total_power_usage(
        co2_scrubber_power_used_kw, co2_scrubber_energy_used_kwh,
        oga_power_used_kw, oga_energy_used_kwh,
        light_power_used_kw, light_energy_used_kwh,
        w_light_power_used_kw, w_light_energy_used_kwh,
        radiator_power_kw, radiator_energy_kwh,
        heater_power_kw, heater_energy_kwh,
        chx_power_used_kw, chx_energy_used_kwh
    ):
    
    total_power_used_kw = (
        + co2_scrubber_power_used_kw
        + oga_power_used_kw
        + light_power_used_kw
        + w_light_power_used_kw
        + radiator_power_kw
        + heater_power_kw
        + chx_power_used_kw
        )
    
    total_energy_used_kwh = (
        + co2_scrubber_energy_used_kwh
        + oga_energy_used_kwh
        + light_energy_used_kwh
        + w_light_energy_used_kwh
        + radiator_energy_kwh
        + heater_energy_kwh
        + chx_energy_used_kwh
        )  

    return total_power_used_kw, total_energy_used_kwh


#-----------------total heat generated---------------♡
def total_heat_generated(light_heat_kw, light_heat_kwh ,w_light_heat_kw, w_light_heat_kwh):
    total_heat_added_kw = light_heat_kw + w_light_heat_kw

    total_heat_added_kwh =  light_heat_kwh + w_light_heat_kwh

    return total_heat_added_kw, total_heat_added_kwh


#------------------full power system-----------------♡
def run_system_power(
    state,
    co2_results,
    oga_results,
    light_results,
    wellness_results,
    thermal_outputs,
    humidity_results,
    dt_min):

    new_solar_arrays, solar_arrays_online_count = solar_arrays_online(state)
    
    total_solar_generated_kw, total_solar_generated_kwh, power_generated_per_array = solar_generation(state, new_solar_arrays, dt_min)
    
    battery_after_charge = solar_battery_charge(state, total_solar_generated_kwh)
    
    total_power_used_kw, total_energy_used_kwh = get_total_power_usage(
        co2_results["co2_scrubber_power_used_kw"], co2_results["co2_scrubber_energy_used_kwh"],
        oga_results["oga_power_used_kw"], oga_results["oga_energy_used_kwh"],
        light_results["light_power_used_kw"], light_results["light_energy_used_kwh"],
        wellness_results["w_light_power_used_kw"], wellness_results["w_light_energy_used_kwh"],
        thermal_outputs.get("radiator_power_kw", 0.0), thermal_outputs.get("radiator_energy_kwh", 0.0),
        thermal_outputs.get("heater_power_kw", 0.0), thermal_outputs.get("heater_energy_kwh", 0.0),
        humidity_results.get("chx_power_used_kw", 0.0), humidity_results.get("chx_energy_used_kwh", 0.0)
        )


    total_heat_added_kw, total_heat_added_kwh = total_heat_generated(
        light_results["light_heat_kw"],
        light_results["light_heat_kwh"],
        wellness_results["w_light_heat_kw"],
        wellness_results["w_light_heat_kwh"]
        )   
    
    new_battery_stored_kwh = max(0.0, battery_after_charge - total_energy_used_kwh)

    #------------dict for updating state-------------♡ 
    power_updates = {
        "battery_stored_kwh": new_battery_stored_kwh,
        "solar_arrays": new_solar_arrays,
    }
    
    #-----------dict for printing outputs------------♡ 
    power_outputs = {
        "solar_arrays_online_count": solar_arrays_online_count,
        "power_generated_per_array":  power_generated_per_array,

        "total_solar_generated_kw": total_solar_generated_kw,
        "total_solar_generated_kwh": total_solar_generated_kwh,
        
        "total_power_used_kw": total_power_used_kw,
        "total_energy_used_kwh": total_energy_used_kwh,
        
        "total_heat_added_kw": total_heat_added_kw,
        "total_heat_added_kwh": total_heat_added_kwh,
    }

    return power_updates, power_outputs

#------------checking power current mode------------♡
def check_power_mode(state):
    battery_percentage = state.battery_stored_kwh / state.battery_max_capacity_kwh

    if battery_percentage <= 0.10:
        power_mode = "critical"

    elif battery_percentage <= 0.25:
        power_mode = "low"
    
    else:
        power_mode = "normal"
    
    return power_mode


#------------deciding low power priorites------------♡
def apply_low_power_mode(power_mode, final_light_level, wellness_light_level):
    if power_mode == "low":
        final_light_level = max(0.02, final_light_level * 0.5)
        wellness_light_level = 0.0
    
    elif power_mode == "critical":
        final_light_level = max(0.02, final_light_level * 0.3)
        wellness_light_level = 0.0

    return final_light_level, wellness_light_level
