from dataclasses import replace
from .state import Habitat_State

# file for Major Constituant Analyzer and buffer gas control


# ----checking atmosphere gas levels---- 
def mca(o2_kpa, co2_kpa, n2_kpa, ar_kpa): 
    total_pressure_kpa = o2_kpa + co2_kpa + n2_kpa + ar_kpa

    return total_pressure_kpa


# ----controlling atmosphere gas levels----
def run_buffer_gas_control(state, dt_min):
    hours_per_step = dt_min / 60

    n2_kpa = state.n2_kpa
    n2_stored_kpa = state.n2_stored_kpa
    ar_kpa = state.ar_kpa
    ar_stored_kpa = state.ar_stored_kpa

    total_buffer_gas_added_kpa = 0.0

    buffer_gas_heat_per_kpa_kw = 1.5

    buffer_gas_heat_added_kw = 0.0
    buffer_gas_heat_added_kwh = 0.0

    total_pressure_kpa = state.o2_kpa + state.co2_kpa + n2_kpa + ar_kpa

    if total_pressure_kpa <= state.min_safe_pressure_kpa:
        pressure_needed_kpa = state.target_pressure_kpa - total_pressure_kpa

        if n2_stored_kpa > 0 and n2_stored_kpa >= pressure_needed_kpa:
           n2_kpa += pressure_needed_kpa
           n2_stored_kpa -= pressure_needed_kpa
           total_buffer_gas_added_kpa += pressure_needed_kpa

        else:
            n2_kpa += n2_stored_kpa
            total_buffer_gas_added_kpa += n2_stored_kpa
            n2_stored_kpa = 0.0

    elif total_pressure_kpa < state.target_pressure_kpa:
        pressure_needed_kpa = state.target_pressure_kpa - total_pressure_kpa

        if n2_kpa < state.target_n2_kpa:
            n2_room_left_kpa = state.target_n2_kpa - n2_kpa
            n2_to_add_kpa = min(pressure_needed_kpa, n2_room_left_kpa, n2_stored_kpa)
            
            n2_kpa += n2_to_add_kpa
            n2_stored_kpa -= n2_to_add_kpa
            total_buffer_gas_added_kpa += n2_to_add_kpa
            
            pressure_needed_kpa -= n2_to_add_kpa

        if pressure_needed_kpa > 0 and ar_kpa < state.target_ar_kpa:
            ar_room_left_kpa = state.target_ar_kpa - ar_kpa
            ar_to_add_kpa = min(pressure_needed_kpa, ar_room_left_kpa, ar_stored_kpa)
            
            ar_kpa += ar_to_add_kpa
            ar_stored_kpa -= ar_to_add_kpa
            total_buffer_gas_added_kpa += ar_to_add_kpa
            
            pressure_needed_kpa -= ar_to_add_kpa

    else:
        pass

    buffer_gas_heat_added_kw = total_buffer_gas_added_kpa * buffer_gas_heat_per_kpa_kw
    buffer_gas_heat_added_kwh = buffer_gas_heat_added_kw * hours_per_step
    
    return {
        "n2_kpa" : n2_kpa,
        "ar_kpa" : ar_kpa,
        "n2_stored_kpa": n2_stored_kpa,
        "ar_stored_kpa": ar_stored_kpa,
        "buffer_gas_heat_added_kw": buffer_gas_heat_added_kw,
        "buffer_gas_heat_added_kwh": buffer_gas_heat_added_kwh,
    }

