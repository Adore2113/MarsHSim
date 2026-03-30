from dataclasses import replace
from .state import Habitat_State

# state.battery_max_capacity_kwh
# state.battery_stored_kwh 
# state.solar_capacity_kw
# state.solar_efficiency

def solar_generation_kw(state):
    ...



def power_usage_kw(outputs):
    total_power_used_kw = 0.0
    total_energy_used_kw = 0.0

    total_power_used_kw = outputs["co2_scrubber_power_used_kw"] + outputs["oga_power_used_kw"] + outputs["light_power_kw"]
    total_energy_used_kwh = outputs["co2_scrubber_energy_used_kwh"] + outputs["oga_energy_used_kwh"] + outputs["light_power_used_kwh"]
  
    return total_power_used_kw, total_energy_used_kwh
 