from dataclasses import replace
from .state import Habitat_State

# state.battery_max_capacity_kwh
# state.battery_stored_kwh 
# state.solar_capacity_kw
# state.solar_efficiency

def solar_arrays_online(solar_array):
    new_solar_array = []
    solar_array_online_count = sum(1 for array in solar_array if array["status"] == "online")

    for array in solar_array:
        new_array = array.copy()

        if solar_array_online_count < 8 and new_array["status"] == "standby":
            new_array["status"] = "online"
            solar_array_online_count += 1

        new_solar_array.append(new_array)

    return new_solar_array, solar_array_online_count


def power_usage_kw(outputs):
    total_power_used_kw = 0.0
    total_energy_used_kw = 0.0

    total_power_used_kw = outputs["co2_scrubber_power_used_kw"] + outputs["oga_power_used_kw"] + outputs["light_power_kw"]
    total_energy_used_kwh = outputs["co2_scrubber_energy_used_kwh"] + outputs["oga_energy_used_kwh"] + outputs["light_power_used_kwh"]
  
    return total_power_used_kw, total_energy_used_kwh
 