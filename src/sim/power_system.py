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


#--------calulate solar power generated amount-------♡
def solar_generation_kw(state, new_solar_arrays):
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

    return total_solar_generated_kw, power_generated_per_array


#--------------habitat light power info--------------♡
def lights(state, dt_min):
    hours_per_step = dt_min / 60
    sol_number, sol_hour, minutes = get_sol_time(state)

    light_power_used_kw = 0.0
    light_power_used_kwh = 0.0
    light_heat_added_kw = 0.0
    light_heat_added_kwh = 0.0

    # consider making daytime power not 100% brightness so that 100% can be used for emergencies or for boosting crew alertness later

    if 6 <= sol_hour < 21 or (sol_hour == 21 and minutes < 30):
        light_level = 1.0
        light_power_used_kw = 2.0
        light_power_used_kwh = light_power_used_kw * hours_per_step
        light_heat_added_kw = 0.5
        light_heat_added_kwh = light_heat_added_kw * hours_per_step
    
        # make the amount used come out of storage

    else:
        light_level = 0.2
        light_power_used_kw = 0.2
        light_power_used_kwh = light_power_used_kw * hours_per_step
        light_heat_added_kw = 0.1
        light_heat_added_kwh = light_heat_added_kw * hours_per_step

    return light_level, light_heat_added_kw, light_heat_added_kwh, light_power_used_kw, light_power_used_kwh


#-----how much power habitat systems are using-------♡
def power_usage_kw(outputs):
    total_power_used_kw = outputs["co2_scrubber_power_used_kw"] + outputs["oga_power_used_kw"] + outputs["light_power_kw"]
    total_energy_used_kwh = outputs["co2_scrubber_energy_used_kwh"] + outputs["oga_energy_used_kwh"] + outputs["light_power_used_kwh"]
  
    return total_power_used_kw, total_energy_used_kwh
 
