#--------------------imports-------------------------♡
from .mars_time import get_sol_time, get_sunlight_amount
#----------------------------------------------------♡


#--------------------constants-----------------------♡
min_arrays_online = 6
max_arrays_online = 10
min_light_level = 0.2

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
                primary_arrays_needed -= 1

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


#-----------habitat main light power info------------♡
def light_system(state, dt_min, power_mode):
    hours_per_step = dt_min / 60
    _, sol_hour, minutes = get_sol_time(state)

    sunlight_amount = get_sunlight_amount(state)
    low_sunlight_streak = state.low_sunlight_streak_sols

    #------------------main lights------------------♡ 
    crew_awake_hours = 6 <= sol_hour < 21 or (sol_hour == 21 and minutes < 30)

    if crew_awake_hours:
        base_light_level = 1.0

    else:
        base_light_level = min_light_level

    sunlight_dimming = sunlight_amount * 0.6    # sunlight level changes light level need for power saving
    light_level_dimmed = base_light_level - sunlight_dimming
    adjusted_light_level = max(min_light_level, light_level_dimmed)

    #----------------wellness lights----------------♡ 
    if low_sunlight_streak >= 3:
        wellness_lights_on = True
        wellness_light_level = 1.0
    
    elif low_sunlight_streak <= 1:
        wellness_lights_on = False
        wellness_light_level = 0.0
    
    else:
        wellness_lights_on = state.wellness_lights_on
        
        if wellness_lights_on:
            wellness_light_level = 1.0

        else:
            wellness_light_level = 0.0
    
    adjusted_light_level, wellness_light_level = apply_low_power_mode_lights(power_mode, adjusted_light_level, wellness_light_level)

    light_power_used_kw = base_light_power_kw * adjusted_light_level
    light_heat_kw =  base_light_heat_kw* adjusted_light_level

    w_light_power_used_kw = base_w_light_power_kw * wellness_light_level
    w_light_heat_kw =  base_w_light_heat_kw * wellness_light_level

    #------------total light heat added-------------♡ 
    total_light_heat_kw = light_heat_kw + w_light_heat_kw

    return {
        "adjusted_light_level": adjusted_light_level,
        "light_heat_kw": light_heat_kw,
        "light_heat_kwh": light_heat_kw * hours_per_step,
        "light_power_used_kw": light_power_used_kw,
        "light_energy_used_kwh": light_power_used_kw * hours_per_step,

        "wellness_lights_on": wellness_lights_on,
        "wellness_light_level": wellness_light_level,
        "w_light_power_used_kw": w_light_power_used_kw,
        "w_light_energy_used_kwh":  w_light_power_used_kw * hours_per_step,
        "w_light_heat_kw": w_light_heat_kw,
        "w_light_heat_kwh": w_light_heat_kw * hours_per_step,

        "total_light_heat_kw": total_light_heat_kw,
        "total_light_heat_kwh": total_light_heat_kw * hours_per_step,
        }


#------------------total power usage-----------------♡
def get_total_power_usage(amine_bed_power_used_kw, oga_power_used_kw, light_power_used_kw, w_light_power_used_kw, greenhouse_led_power_kw, radiator_power_kw, heater_power_kw, chx_power_used_kw, upa_power_used_kw, wpa_power_used_kw, bpa_power_used_kw, sabatier_power_used_kw, isru_power_used_kw):
    total_power_used_kw = (amine_bed_power_used_kw + oga_power_used_kw + light_power_used_kw + w_light_power_used_kw + greenhouse_led_power_kw + radiator_power_kw + heater_power_kw + chx_power_used_kw  + upa_power_used_kw + wpa_power_used_kw + bpa_power_used_kw + sabatier_power_used_kw + isru_power_used_kw)

    return total_power_used_kw

def get_total_energy_usage(amine_bed_energy_used_kwh, oga_energy_used_kwh, light_energy_used_kwh, w_light_energy_used_kwh, greenhouse_led_energy_kwh, radiator_energy_kwh, heater_energy_kwh, chx_energy_used_kwh, upa_energy_used_kwh, wpa_energy_used_kwh, bpa_energy_used_kwh, sabatier_energy_used_kwh, isru_energy_used_kwh):
    total_energy_used_kwh = (amine_bed_energy_used_kwh + oga_energy_used_kwh + light_energy_used_kwh + w_light_energy_used_kwh + greenhouse_led_energy_kwh + radiator_energy_kwh + heater_energy_kwh + chx_energy_used_kwh + upa_energy_used_kwh + wpa_energy_used_kwh + bpa_energy_used_kwh + sabatier_energy_used_kwh + isru_energy_used_kwh)  

    return total_energy_used_kwh

#------------------full power system-----------------♡
def run_system_power(
    state,
    co2_results,
    oga_results,
    light_results,
    thermal_outputs,
    humidity_results,
    greenhouse_outputs,
    water_outputs,
    sabatier_outputs,
    isru_outputs,
    dt_min
    ):

    new_solar_arrays, solar_arrays_online_count = solar_arrays_online(state) 
    total_solar_generated_kw, total_solar_generated_kwh, power_generated_per_array = solar_generation(state, new_solar_arrays, dt_min)

    total_power_used_kw = get_total_power_usage(
        co2_results["amine_bed_power_used_kw"],
        oga_results["oga_power_used_kw"],
        light_results["light_power_used_kw"],
        light_results["w_light_power_used_kw"],
        greenhouse_outputs.get("total_led_power_kw", 0.0),
        thermal_outputs.get("radiator_power_kw", 0.0),
        thermal_outputs.get("heater_power_kw", 0.0),
        humidity_results.get("chx_power_used_kw", 0.0),
        water_outputs.get("upa_power_used_kw", 0.0),
        water_outputs.get("wpa_power_used_kw", 0.0),
        water_outputs.get("bpa_power_used_kw", 0.0),
        sabatier_outputs.get("sabatier_power_used_kw", 0.0),
        isru_outputs.get("isru_power_used_kw", 0.0)
    )

    total_energy_used_kwh = get_total_energy_usage(
    co2_results["amine_bed_energy_used_kwh"],
    oga_results["oga_energy_used_kwh"],
    light_results["light_energy_used_kwh"],
    light_results["w_light_energy_used_kwh"],
    greenhouse_outputs.get("total_led_energy_kwh", 0.0),
    thermal_outputs.get("radiator_energy_kwh", 0.0),
    thermal_outputs.get("heater_energy_kwh", 0.0),
    humidity_results.get("chx_energy_used_kwh", 0.0),
    water_outputs.get("upa_energy_used_kwh", 0.0),
    water_outputs.get("wpa_energy_used_kwh", 0.0),
    water_outputs.get("bpa_energy_used_kwh", 0.0),
    sabatier_outputs.get("sabatier_energy_used_kwh", 0.0),
    isru_outputs.get("isru_energy_used_kwh", 0.0),
    )

    net_energy_kwh = total_solar_generated_kwh - total_energy_used_kwh
   
    new_battery_stored_kwh = state.battery_stored_kwh + net_energy_kwh
    new_battery_stored_kwh = max(0.0, min(state.battery_max_capacity_kwh, new_battery_stored_kwh))
   
    battery_percentage = (new_battery_stored_kwh / state.battery_max_capacity_kwh)

    if battery_percentage <= 0.10:
        power_mode = "critical"

    elif battery_percentage <= 0.25:
        power_mode = "low"

    else:
        power_mode = "normal"

    total_heat_added_kw = light_results["total_light_heat_kw"]
    total_heat_added_kwh = light_results["total_light_heat_kwh"]

    #------------dict for updating state-------------♡ 
    power_updates = {
        "battery_stored_kwh": new_battery_stored_kwh,
        "solar_arrays": new_solar_arrays,
        "power_mode": power_mode,
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

        "greenhouse_led_power_kw": greenhouse_outputs.get("total_led_power_kw", 0.0),
        "greenhouse_led_energy_kwh": greenhouse_outputs.get("total_led_energy_kwh", 0.0),

        **light_results,
        "net_energy_kwh": net_energy_kwh,
    }

    return power_updates, power_outputs


#------------deciding low power priorites------------♡
def apply_low_power_mode_lights(power_mode, adjusted_light_level, wellness_light_level):
    if power_mode == "low":
        adjusted_light_level = max(0.02, adjusted_light_level * 0.5)
        wellness_light_level = 0.0
    
    elif power_mode == "critical":
        adjusted_light_level = max(0.02, adjusted_light_level * 0.3)
        wellness_light_level = 0.0

    return adjusted_light_level, wellness_light_level
