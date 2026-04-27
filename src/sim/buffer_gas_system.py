# file for Major Constituent Analyzer and buffer gas control


#-------------check habitat gas levels--------------♡
def mca(state): 
    total_pressure_kpa = state.o2_kpa + state.co2_kpa + state.n2_kpa + state.ar_kpa

    return total_pressure_kpa


#--------------stabilizing gas levels---------------♡
def buffer_gas_control_kpa(state):
    n2_kpa = state.n2_kpa
    n2_stored_kpa = state.n2_stored_kpa
    ar_kpa = state.ar_kpa
    ar_stored_kpa = state.ar_stored_kpa

    hysteresis_kpa = 0.05
    target_pressure_kpa = state.target_pressure_kpa
    
    total_buffer_gas_added_kpa = 0.0
    total_pressure_kpa = mca(state)
    
    #---------handling emergency gas levels---------♡  
    if total_pressure_kpa <= state.min_safe_pressure_kpa:
        pressure_needed_kpa = state.target_pressure_kpa - total_pressure_kpa

        n2_to_add_kpa = min(pressure_needed_kpa, n2_stored_kpa)    # use nitrogen first
        n2_kpa += n2_to_add_kpa
        n2_stored_kpa -= n2_to_add_kpa
        total_buffer_gas_added_kpa += n2_to_add_kpa
        pressure_needed_kpa -= n2_to_add_kpa

        if pressure_needed_kpa > 0:    # use argon next
            ar_to_add_kpa = min(pressure_needed_kpa, ar_stored_kpa)
            ar_kpa += ar_to_add_kpa
            ar_stored_kpa -= ar_to_add_kpa
            total_buffer_gas_added_kpa += ar_to_add_kpa
            pressure_needed_kpa -= ar_to_add_kpa

    elif total_pressure_kpa < (target_pressure_kpa - hysteresis_kpa):
        pressure_needed_kpa = target_pressure_kpa - total_pressure_kpa

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
        
    return n2_kpa, ar_kpa, n2_stored_kpa, ar_stored_kpa, total_buffer_gas_added_kpa
      

#----system power consumption and heat produced-----♡
def buffer_gas_power_and_heat(total_buffer_gas_added_kpa, dt_min):
    hours_per_step = dt_min / 60

    if total_buffer_gas_added_kpa > 0:
        buffer_gas_heat_per_kpa_kw = 1.5
        buffer_gas_heat_added_kw = total_buffer_gas_added_kpa * buffer_gas_heat_per_kpa_kw
        buffer_gas_heat_added_kwh = buffer_gas_heat_added_kw * hours_per_step
    
        buffer_gas_power_used_kw = 0.4
        buffer_gas_energy_used_kwh = buffer_gas_power_used_kw * hours_per_step

    else:
        buffer_gas_heat_added_kw = 0.0
        buffer_gas_heat_added_kwh = 0.0

        buffer_gas_power_used_kw = 0.0
        buffer_gas_energy_used_kwh = 0.0
    
    return buffer_gas_heat_added_kw, buffer_gas_heat_added_kwh, buffer_gas_power_used_kw, buffer_gas_energy_used_kwh


#-------buffer gas control info per timestep--------♡
def run_buffer_gas_control(state, dt_min):
    n2_kpa, ar_kpa, n2_stored_kpa, ar_stored_kpa, total_buffer_gas_added_kpa = buffer_gas_control_kpa(state)
    buffer_gas_heat_added_kw, buffer_gas_heat_added_kwh, buffer_gas_power_used_kw, buffer_gas_energy_used_kwh = buffer_gas_power_and_heat(total_buffer_gas_added_kpa, dt_min)

    return {
        "n2_kpa" : n2_kpa,
        "ar_kpa" : ar_kpa,
        "n2_stored_kpa" : n2_stored_kpa,
        "ar_stored_kpa" : ar_stored_kpa,
        "total_buffer_gas_added_kpa" : total_buffer_gas_added_kpa,
        "buffer_gas_heat_added_kw" : buffer_gas_heat_added_kw,
        "buffer_gas_heat_added_kwh" : buffer_gas_heat_added_kwh,
        "buffer_gas_power_used_kw" : buffer_gas_power_used_kw, 
        "buffer_gas_energy_used_kwh" : buffer_gas_energy_used_kwh,
    }

