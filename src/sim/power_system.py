from dataclasses import replace
from .state import Habitat_State


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


def solar_generation_kw(state, new_solar_array):
    power_generated_per_array = []
    total_solar_generated_kw = 0.0

    for array in new_solar_array:
        if array["status"] == "online":
            power_generated_kw = (state.daylight_m2_kw * array["area_m2"] * array["efficiency"] * array["dust_factor"])

        else:
            power_generated_kw = 0.0

        power_generated_per_array.append({"id" : array["id"], "power_generated_kw" : power_generated_kw})
        total_solar_generated_kw += power_generated_kw

    return total_solar_generated_kw, power_generated_per_array


def power_usage_kw(outputs):
    total_power_used_kw = outputs["co2_scrubber_power_used_kw"] + outputs["oga_power_used_kw"] + outputs["light_power_kw"]
    total_energy_used_kwh = outputs["co2_scrubber_energy_used_kwh"] + outputs["oga_energy_used_kwh"] + outputs["light_power_used_kwh"]
  
    return total_power_used_kw, total_energy_used_kwh
 