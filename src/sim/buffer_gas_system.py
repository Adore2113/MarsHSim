# file for Major Constituent Analyzer and buffer gas control


#--------------------constants-----------------------♡
hysteresis_kpa = 0.05
#---------------------------------------------------♡


#-------------check habitat gas levels--------------♡
def mca(state): 
    total_pressure_kpa = state.o2_kpa + state.co2_kpa + state.n2_kpa + state.ar_kpa

    return total_pressure_kpa


#--------------stabilizing gas levels---------------♡
def buffer_gas_control_kpa(state):
    new_n2_kpa = state.n2_kpa
    new_ar_kpa = state.ar_kpa
    new_n2_stored_kpa = state.n2_stored_kpa
    new_ar_stored_kpa = state.ar_stored_kpa

    total_pressure_kpa = mca(state)
    pressure_gap_kpa = state.target_pressure_kpa - total_pressure_kpa
    
    total_buffer_gas_added_kpa = 0.0
    total_buffer_gas_vented_kpa = 0.0

    #---------------buffer gas modes----------------♡  
    if total_pressure_kpa <= state.min_safe_pressure_kpa:
        buffer_gas_mode = "emergency_add"
        pressure_needed_kpa = state.target_pressure_kpa - total_pressure_kpa
    
    elif pressure_gap_kpa > hysteresis_kpa:
        buffer_gas_mode = "add"
        pressure_needed_kpa = pressure_gap_kpa

    elif pressure_gap_kpa < -hysteresis_kpa:
        buffer_gas_mode = "vent"
        pressure_to_vent_kpa = -pressure_gap_kpa

    else:
        buffer_gas_mode = "stable"
        
    if buffer_gas_mode in ("emergency_add", "add"):
        pressure_to_add_kpa = pressure_needed_kpa

    #------------handling Nitrogen first------------♡  
        if new_n2_kpa < state.target_n2_kpa:
            n2_room_left_kpa = state.target_n2_kpa - new_n2_kpa
            n2_to_add_kpa = min(pressure_to_add_kpa, n2_room_left_kpa, new_n2_stored_kpa)

            new_n2_kpa += n2_to_add_kpa
            new_n2_stored_kpa -= n2_to_add_kpa
            
            total_buffer_gas_added_kpa += n2_to_add_kpa
            pressure_to_add_kpa -= n2_to_add_kpa

    #----------------handling Argon-----------------♡  
        if pressure_to_add_kpa > 0 and new_ar_kpa < state.target_ar_kpa:
            ar_room_left_kpa = state.target_ar_kpa - new_ar_kpa
            ar_to_add_kpa = min(pressure_to_add_kpa, ar_room_left_kpa, new_ar_stored_kpa)
            
            new_ar_kpa += ar_to_add_kpa
            new_ar_stored_kpa -= ar_to_add_kpa
            total_buffer_gas_added_kpa += ar_to_add_kpa
            pressure_to_add_kpa -= ar_to_add_kpa

    #---------------venting extra gas---------------♡  
    elif buffer_gas_mode == "vent":
        pressure_to_vent_kpa = -pressure_gap_kpa
        
        #-------------vent Argon first--------------♡  
        if new_ar_kpa > state.target_ar_kpa:
            ar_to_vent = min(pressure_to_vent_kpa, new_ar_kpa - state.target_ar_kpa)
            new_ar_kpa -= ar_to_vent
            pressure_to_vent_kpa -= ar_to_vent
            
            total_buffer_gas_vented_kpa += ar_to_vent 
  
        #-------------venting Nitrogen--------------♡  
        if pressure_to_vent_kpa > 0 and new_n2_kpa > state.target_n2_kpa:
            n2_to_vent = min(pressure_to_vent_kpa, new_n2_kpa - state.target_n2_kpa)
            new_n2_kpa -= n2_to_vent
            
            total_buffer_gas_vented_kpa += n2_to_vent
            
    else:
        pass
        
    return (new_n2_kpa, new_ar_kpa, new_n2_stored_kpa, new_ar_stored_kpa, total_buffer_gas_added_kpa, total_buffer_gas_vented_kpa, buffer_gas_mode, pressure_gap_kpa)
      

#----system power consumption and heat produced-----♡
def buffer_gas_power_and_heat(total_buffer_gas_added_kpa, total_buffer_gas_vented_kpa, dt_min):
    hours_per_step = dt_min / 60

    if total_buffer_gas_added_kpa > 0 or total_buffer_gas_vented_kpa > 0:
        buffer_gas_heat_per_kpa_kw = 1.5
        total_gas_moved_kpa = total_buffer_gas_added_kpa + total_buffer_gas_vented_kpa
        
        buffer_gas_heat_added_kw = total_gas_moved_kpa * buffer_gas_heat_per_kpa_kw
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
    n2_kpa, ar_kpa, n2_stored_kpa, ar_stored_kpa, total_buffer_gas_added_kpa, total_buffer_gas_vented_kpa, buffer_gas_mode, pressure_gap_kpa = buffer_gas_control_kpa(state)
    
    buffer_gas_heat_added_kw, buffer_gas_heat_added_kwh, buffer_gas_power_used_kw, buffer_gas_energy_used_kwh = buffer_gas_power_and_heat(total_buffer_gas_added_kpa, total_buffer_gas_vented_kpa, dt_min)
    

    return {
        "n2_kpa": n2_kpa,
        "ar_kpa": ar_kpa,
        "n2_stored_kpa": n2_stored_kpa,
        "ar_stored_kpa": ar_stored_kpa,
        "total_buffer_gas_added_kpa": total_buffer_gas_added_kpa,
        "buffer_gas_heat_added_kw": buffer_gas_heat_added_kw,
        "total_buffer_gas_vented_kpa": total_buffer_gas_vented_kpa,
        "buffer_gas_heat_added_kwh": buffer_gas_heat_added_kwh,
        "buffer_gas_power_used_kw": buffer_gas_power_used_kw, 
        "buffer_gas_energy_used_kwh": buffer_gas_energy_used_kwh,
        "buffer_gas_mode": buffer_gas_mode, 
        "pressure_gap_kpa":  pressure_gap_kpa 
    }

