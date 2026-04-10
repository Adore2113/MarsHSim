from dataclasses import replace
from .state import Habitat_State
from .mars_time import get_sol_time, daylight_per_m2_kw, determine_sunlight_amount


#-----------which solar arrays are online------------♡
def solar_arrays_online(solar_array):
    new_solar_arrays = []
    solar_array_online_count = sum(1 for array in solar_array if array["status"] == "online")

    for array in solar_array:
        new_array = array.copy()

        if solar_array_online_count < 8 and new_array["status"] == "standby":
            new_array["status"] = "online"
            solar_array_online_count += 1

        new_solar_arrays.append(new_array)

    return new_solar_arrays, solar_array_online_count


#--------calculate solar power generated amount-------♡
def solar_generation(state, new_solar_arrays, dt_min):
    hours_per_step = dt_min / 60
    current_daylight_m2_kw = state.daylight_m2_kw
    power_generated_per_array = []
    total_solar_generated_kw = 0.0

    for array in new_solar_arrays:
        if array["status"] == "online":
            power_generated_kw = (current_daylight_m2_kw * array["area_m2"] * array["efficiency"] * array["dust_factor"])

        else:
            power_generated_kw = 0.0

        power_generated_per_array.append({"id" : array["id"], "power_generated_kw" : power_generated_kw})
        total_solar_generated_kw += power_generated_kw
        
    total_solar_generated_kwh = total_solar_generated_kw * hours_per_step

    return total_solar_generated_kw, power_generated_per_array


#--------save solar power generated to storage-------♡
def solar_battery_charge(state, total_solar_generated_kwh):
    battery_stored_kwh = state.battery_stored_kwh
    battery_max_capacity_kwh = state.battery_max_capacity_kwh
    
    if battery_stored_kwh < battery_max_capacity_kwh:
        new_battery_stored_kwh = max(battery_max_capacity_kwh, battery_stored_kwh + total_solar_generated_kwh)

    else:
        new_battery_stored_kwh = battery_stored_kwh
    
    return new_battery_stored_kwh


#-----------habitat main light power info------------♡
def lights(state, dt_min):
    hours_per_step = dt_min / 60
    _, sol_hour, minutes = get_sol_time(state)
    sunlight_amount = determine_sunlight_amount(state)
    crew_sleep_hours = 6 <= sol_hour < 21 or (sol_hour == 21 and minutes < 30)
    
    if crew_sleep_hours:
        base_light_level = 0.2

    else:
        base_light_level = 1.0

    sunlight_dimming = sunlight_amount * 0.6    # sunlight level changes light level need for power saving
    light_level_dimmed = base_light_level - sunlight_dimming

    if state.battery_stored_kwh < 300:
        min_light_level = 0.1

    else:
        min_light_level = 0.2
    
    final_light_level = max(min_light_level, light_level_dimmed)

    light_power_used_kw = 2.0 * final_light_level
    light_power_used_kwh = light_power_used_kw * hours_per_step

    light_heat_added_kw =  0.5 * final_light_level
    light_heat_added_kwh = light_heat_added_kw * hours_per_step

    return final_light_level, light_heat_added_kw, light_heat_added_kwh, light_power_used_kw, light_power_used_kwh


#--------wellness lights from lack of sunlight-------♡
def wellness_lights(state, dt_min):
    hours_per_step = dt_min / 60
    low_sunlight_streak = state.low_sunlight_streak_sols
    
    if low_sunlight_streak >= 3:
        wellness_lights_on = True
        wellness_light_level = 1.0
    
    else:
        wellness_lights_on = False
        wellness_light_level = 0.0
    
    w_light_power_used_kw = 0.5 * wellness_light_level
    w_light_power_used_kwh = w_light_power_used_kw * hours_per_step

    w_light_heat_added_kw =  0.1 * wellness_light_level
    w_light_heat_added_kwh = w_light_heat_added_kw * hours_per_step

    return wellness_lights_on, wellness_light_level, w_light_heat_added_kw, w_light_heat_added_kwh, w_light_power_used_kw, w_light_power_used_kwh
    

#-----how much power habitat systems are using-------♡
def total_power_usage(outputs):
    total_power_used_kw = outputs["co2_scrubber_power_used_kw"] + outputs["oga_power_used_kw"] + outputs["light_power_kw"] + outputs["w_light_power_used_kw"]
    total_energy_used_kwh = outputs["co2_scrubber_energy_used_kwh"] + outputs["oga_energy_used_kwh"] + outputs["light_power_used_kwh"] + outputs ["w_light_power_used_kwh"]
  
    return total_power_used_kw, total_energy_used_kwh


#-----battery usage and storage update per step------♡
def run_system_power(state):
    ...
    

#------------handling low power priorites------------♡
def low_power_mode(state):
    ...


#--------------------power alerts--------------------♡
def power_alerts(state):
    ...