# file for Major Constituent Analyzer and buffer gas control


#--------------------constants-----------------------♡
kelvin_offset = 273.15   # add to celsius to convert to kelvin
pa_per_kpa = 1000.0   # kilopascals to pascals
r_kpa = 0.008314   # universal gas constant, 8.314 / 1000
kg_per_g = 0.001
n2_molar_mass_kg = 0.028014
ar_molar_mass_kg = 0.039948

base_buffer_gas_power_kw = 0.84
gas_moved_power_multiplier = 0.4
base_buffer_gas_heat_kw = 1.5
gas_moved_heat_multiplier = 0.9 
mca_update_power_kw = 0.1

hysteresis_kpa = 0.05
safe_usage_ratio = 0.9
vent_loss_fraction = 0.08
#---------------------------------------------------♡


#-------------check habitat gas levels--------------♡
def mca(state): 
    total_pressure_kpa = state.o2_kpa + state.co2_kpa + state.n2_kpa + state.ar_kpa

    return total_pressure_kpa


#-----------------buffer gas system-----------------♡
def run_buffer_gas_control(state, dt_min):
    hours_per_step = dt_min / 60

    buffer_gas_mode = "stable"
    total_buffer_gas_added_kpa = 0.0
    total_buffer_gas_vented_kpa = 0.0
    
    pressure_gap_kpa = 0.0
    pressure_to_add_kpa = 0.0
    pressure_to_vent_kpa = 0.0

    new_n2_kpa = state.n2_kpa
    new_ar_kpa = state.ar_kpa
    new_n2_stored_kg = state.n2_stored_kg
    new_ar_stored_kg = state.ar_stored_kg

    buffer_gas_power_used_kw = mca_update_power_kw
    buffer_gas_heat_added_kw = 0.0


    #---------calculate pressure difference---------♡  
    total_pressure_kpa = mca(state)
    pressure_gap_kpa = state.target_pressure_kpa - total_pressure_kpa


    #----------------buffer gas modes---------------♡  
    if total_pressure_kpa <= state.min_safe_pressure_kpa:
        buffer_gas_mode = "emergency_add"
        pressure_to_add_kpa = state.target_pressure_kpa - total_pressure_kpa
    
    elif pressure_gap_kpa > hysteresis_kpa:
        buffer_gas_mode = "add"
        pressure_to_add_kpa = pressure_gap_kpa

    elif pressure_gap_kpa < -hysteresis_kpa:
        buffer_gas_mode = "vent"
        pressure_to_vent_kpa = -pressure_gap_kpa

    else:
        buffer_gas_mode = "stable"


  #-----------------adding buffer gas---------------♡  
    if buffer_gas_mode in ("emergency_add", "add"):
        left_to_add_kpa = pressure_to_add_kpa
        
        #--------------Nitrogen first---------------♡  
        if new_n2_kpa < state.target_n2_kpa and left_to_add_kpa > 0.01:
            n2_room_left_kpa = state.target_n2_kpa - new_n2_kpa
            n2_to_add_kpa = min(left_to_add_kpa, n2_room_left_kpa)

            n2_added_moles = (n2_to_add_kpa * state.hab_vol_m3) / (r_kpa * (state.hab_temp_c + kelvin_offset))
            n2_added_kg = n2_added_moles * n2_molar_mass_kg

            if new_n2_stored_kg * safe_usage_ratio >= n2_added_kg:
                new_n2_kpa += n2_to_add_kpa
                new_n2_stored_kg -= n2_added_kg
                
                total_buffer_gas_added_kpa += n2_to_add_kpa
                left_to_add_kpa -= n2_to_add_kpa
                
        #----------------Argon second---------------♡
        if left_to_add_kpa > 0.01 and new_ar_kpa < state.target_ar_kpa:
            ar_room_left_kpa = state.target_ar_kpa - new_ar_kpa
            ar_to_add_kpa = min(left_to_add_kpa, ar_room_left_kpa)
            
            ar_added_moles = (ar_to_add_kpa * state.hab_vol_m3) / (r_kpa * (state.hab_temp_c + kelvin_offset))
            ar_added_kg = ar_added_moles * ar_molar_mass_kg

            if new_ar_stored_kg * safe_usage_ratio >= ar_added_kg:
                new_ar_kpa += ar_to_add_kpa
                new_ar_stored_kg -= ar_added_kg
                total_buffer_gas_added_kpa += ar_to_add_kpa


    #---------------venting extra gas---------------♡  
    elif buffer_gas_mode == "vent":
        left_to_vent_kpa = pressure_to_vent_kpa
        
        #-------------vent Argon first--------------♡  
        if new_ar_kpa > state.target_ar_kpa and left_to_vent_kpa > 0.01:
            excess_ar_kpa = new_ar_kpa - state.target_ar_kpa
            ar_to_vent = min(left_to_vent_kpa, excess_ar_kpa)

            vented_amount_kpa = ar_to_vent * (1 - vent_loss_fraction)
            new_ar_kpa -= vented_amount_kpa
            total_buffer_gas_vented_kpa += vented_amount_kpa
            left_to_vent_kpa -= vented_amount_kpa 
  
        #-------------venting Nitrogen--------------♡  
        if left_to_vent_kpa > 0.01 and new_n2_kpa > state.target_n2_kpa:
            excess_n2_kpa = new_n2_kpa - state.target_n2_kpa
            n2_to_vent_kpa = min(left_to_vent_kpa, excess_n2_kpa)
            
            vented_amount_kpa = n2_to_vent_kpa * (1 - vent_loss_fraction)
            new_n2_kpa -= vented_amount_kpa
            total_buffer_gas_vented_kpa += vented_amount_kpa
            left_to_vent_kpa -= vented_amount_kpa


    #----------------small gas leaks----------------♡  
    n2_leak_kpa = state.n2_leak_rate_kpa_per_hr * hours_per_step
    ar_leak_kpa = state.ar_leak_rate_kpa_per_hr * hours_per_step

    new_n2_kpa = max(0.0, new_n2_kpa - n2_leak_kpa)
    new_ar_kpa = max(0.0, new_ar_kpa - ar_leak_kpa)        

    total_buffer_gas_moved_kpa = total_buffer_gas_added_kpa + total_buffer_gas_vented_kpa
   

    #----------------power and heat-----------------♡  
    if total_buffer_gas_moved_kpa > 0.01:
        buffer_gas_power_used_kw = base_buffer_gas_power_kw + (gas_moved_power_multiplier * total_buffer_gas_moved_kpa)
        buffer_gas_heat_added_kw = base_buffer_gas_heat_kw * total_buffer_gas_moved_kpa + (gas_moved_heat_multiplier * total_buffer_gas_moved_kpa)


    #------------dict for updating state-------------♡ 
    buffer_gas_updates = {
    "n2_kpa": new_n2_kpa,
    "ar_kpa": new_ar_kpa,
    "n2_stored_kg": new_n2_stored_kg,
    "ar_stored_kg": new_ar_stored_kg,
    }
    

    #-----------dict for printing outputs------------♡ 
    buffer_gas_outputs = {
    "buffer_gas_mode": buffer_gas_mode,
    "total_buffer_gas_added_kpa": total_buffer_gas_added_kpa,
    "total_buffer_gas_vented_kpa": total_buffer_gas_vented_kpa,
    "pressure_gap_kpa": pressure_gap_kpa, 

    "n2_leaked_kpa": n2_leak_kpa,
    "ar_leaked_kpa": ar_leak_kpa,

    "buffer_gas_power_used_kw": buffer_gas_power_used_kw,
    "buffer_gas_energy_used_kwh": buffer_gas_power_used_kw * hours_per_step,
    "buffer_gas_heat_added_kw": buffer_gas_heat_added_kw,
    "buffer_gas_heat_added_kwh": buffer_gas_heat_added_kw * hours_per_step, 
    }   

    return buffer_gas_updates, buffer_gas_outputs

