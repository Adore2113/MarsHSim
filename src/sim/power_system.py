#--------------------imports-------------------------♡
from .mars_time import get_sol_time, determine_sunlight_amount
#----------------------------------------------------♡


#--------------------constants-----------------------♡
max_arrays_online = 10

target_power_usage_ratio = 0.85
base_solar_power_per_array_kw = 0.0

min_light_level = 0.2

base_light_power_kw = 2.0
base_light_heat_kw = 0.5
base_w_light_power_kw = 0.5
base_w_light_heat_kw = 0.1
#---------------------------------------------------♡


#-----------which solar arrays are online------------♡
def solar_arrays_online(solar_array):
    new_solar_arrays = []
    solar_arrays_online_count = sum(1 for array in solar_array if array["status"] == "online")

    for array in solar_array:
        new_array = array.copy()

        if solar_arrays_online_count < 8 and new_array["status"] == "standby":
            new_array["status"] = "online"
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

        power_generated_per_array.append({"id" : array["id"], "power_generated_kw" : power_generated_kw})
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
    light_power_used_kwh = light_power_used_kw * hours_per_step

    light_heat_kw =  base_w_light_heat_kw * final_light_level
    light_heat_kwh = light_heat_kw * hours_per_step

    return {
        "final_light_level" : final_light_level,
        "light_heat_kw" : light_heat_kw,
        "light_heat_kwh" : light_heat_kwh,
        "light_power_used_kw" : light_power_used_kw,
        "light_power_used_kwh" : light_power_used_kwh
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
    w_light_power_used_kwh = w_light_power_used_kw * hours_per_step

    w_light_heat_kw =  base_w_light_heat_kw * wellness_light_level
    w_light_heat_kwh = w_light_heat_kw * hours_per_step

    return {
            "wellness_lights_on": wellness_lights_on,
            "wellness_light_level": wellness_light_level,
            "w_light_power_used_kw": w_light_power_used_kw,
            "w_light_power_used_kwh": w_light_power_used_kwh,
            "w_light_heat_kw": w_light_heat_kw,
            "w_light_heat_kwh": w_light_heat_kwh,
        }    


#-----how much power habitat systems are using-------♡
def total_power_usage(
    co2_scrubber_power_used_kw, co2_scrubber_energy_used_kwh,
    oga_power_used_kw, oga_energy_used_kwh,
    light_power_used_kw, light_power_used_kwh,
    w_light_power_used_kw, w_light_power_used_kwh,
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
        + light_power_used_kwh
        + w_light_power_used_kwh
        + radiator_energy_kwh
        + heater_energy_kwh
        + chx_energy_used_kwh
        )  

    return total_power_used_kw, total_energy_used_kwh


#-----how much heat was generated--------------------♡
def total_heat_generated(light_heat_kw, light_heat_kwh ,w_light_heat_kw, w_light_heat_kwh):
    total_heat_added_kw = light_heat_kw + w_light_heat_kw

    total_heat_added_kwh =  light_heat_kwh + w_light_heat_kwh

    return total_heat_added_kw, total_heat_added_kwh


#-----battery usage and storage update per step------♡
def run_system_power(state,
    co2_scrubber_power_used_kw, co2_scrubber_energy_used_kwh,
    oga_power_used_kw, oga_energy_used_kwh,
    light_power_used_kw, light_power_used_kwh,
    w_light_power_used_kw, w_light_power_used_kwh,
    light_heat_kw, light_heat_kwh,
    w_light_heat_kw, w_light_heat_kwh,
    radiator_power_kw, radiator_energy_kwh,
    heater_power_kw, heater_energy_kwh,
    chx_power_used_kw, chx_energy_used_kwh,
    dt_min):

    new_solar_arrays, solar_arrays_online_count = solar_arrays_online(state.solar_arrays)
    total_solar_generated_kw, total_solar_generated_kwh, power_generated_per_array = solar_generation(state, new_solar_arrays, dt_min)
    battery_after_charge = solar_battery_charge(state, total_solar_generated_kwh)
    total_power_used_kw, total_energy_used_kwh = total_power_usage(co2_scrubber_power_used_kw, co2_scrubber_energy_used_kwh, oga_power_used_kw, oga_energy_used_kwh, light_power_used_kw, light_power_used_kwh, w_light_power_used_kw, w_light_power_used_kwh, radiator_power_kw, radiator_energy_kwh, heater_power_kw, heater_energy_kwh, chx_power_used_kw, chx_energy_used_kwh)
    total_heat_added_kw, total_heat_added_kwh = total_heat_generated(light_heat_kw, light_heat_kwh ,w_light_heat_kw, w_light_heat_kwh)
    new_battery_stored_kwh = max(0.0, battery_after_charge - total_energy_used_kwh)

    return {
        "new_solar_arrays": new_solar_arrays,
        "solar_arrays_online_count" : solar_arrays_online_count,
        "total_solar_generated_kw" : total_solar_generated_kw, "total_solar_generated_kwh" : total_solar_generated_kwh,
        "total_power_used_kw" : total_power_used_kw, "total_energy_used_kwh" : total_energy_used_kwh,
        "total_heat_added_kw" : total_heat_added_kw, "total_heat_added_kwh" : total_heat_added_kwh,
        "new_battery_stored_kwh" : new_battery_stored_kwh,
        "power_generated_per_array":  power_generated_per_array
    }
    

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
    