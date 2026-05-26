# file for Oxygen Generation Assembly (OGA) & Water Electrolysis


#--------------------constants-----------------------♡
kelvin_offset = 273.15   # add to celsius to convert to kelvin
pa_per_kpa = 1000.0   # kilopascals to pascals
r_kpa = 0.008314   # universal gas constant, 8.314 / 1000
kg_per_g = 0.001

h2_molar_mass = 2.016   # 1 mole h2 = 2.016g b/c h2 = 2 hydrogen atoms (1.008 g/mol each)
o2_molar_mass = 32.0   # grams per mole

oga_max_o2_output_kpa = 0.5
base_oga_power_kw = 2.5
base_oga_heat_kw = 1.2

safety_backup_water_kg = 30.0
hysteresis_kpa = 0.002
water_kg_per_o2_kg = 1.11   # electrolysis
#----------------------------------------------------♡


#------------oxygen regeneration process-------------♡
def run_oga(state, o2_after_crew_kpa, dt_min):
    hours_per_step = dt_min / 60

    #---------------default oga values--------------♡
    oga_mode = "offline"
    o2_added_kpa = 0.0
    h2_produced_kg = 0.0
    water_used_kg = 0.0
    limited_by_water = False 

    sabatier_power_used_kw = 0.0
    oga_power_used_kw = 0.0
    oga_heat_added_kw = 0.0

    o2_needed_kpa = state.target_o2_kpa - o2_after_crew_kpa

    #-------------------oga modes-------------------♡  
    if not state.oga_on:
        oga_mode = "offline"
        oga_power_used_kw = 0.0
        oga_heat_added_kw = 0.0

    elif o2_needed_kpa <= hysteresis_kpa:
        oga_mode = "idle"
        oga_power_used_kw = 0.15
        oga_heat_added_kw = 0.4

    else:
        oga_mode = "running"
        
        o2_added_kpa = min(oga_max_o2_output_kpa, max(0.0, o2_needed_kpa + 0.001))
        
        o2_moles = (o2_added_kpa * state.hab_vol_m3) / (r_kpa * (state.hab_temp_c + kelvin_offset))
        o2_produced_kg = (o2_moles * o2_molar_mass) / kg_per_g
     
        h2_produced_kg = o2_produced_kg * (2 * h2_molar_mass) / o2_molar_mass
        water_used_kg = o2_produced_kg * water_kg_per_o2_kg

    #--------------water storage check--------------♡
        min_water_needed_kg = water_used_kg + (state.crew_count * 2.0) + safety_backup_water_kg
        
        if state.potable_water_storage_kg < min_water_needed_kg:
            oga_mode = "limited_water"
            limited_by_water = True
            water_used_kg = 0.0
            h2_produced_kg = 0.0
            o2_added_kpa = 0.0
        
            power_used_kw = base_oga_power_kw * 0.55
            heat_added_kw = base_oga_heat_kw * 0.55

        else:  
            power_used_kw = base_oga_power_kw
            heat_added_kw = base_oga_heat_kw


    #---------------handling excess o2---------------♡ 
    new_o2_kpa = o2_after_crew_kpa + o2_added_kpa
    o2_control_mode = "normal"
    o2_stored_kg = 0.0
    o2_vented_kg = 0.0
    new_o2_stored_kg = state.o2_stored_kg

    if new_o2_kpa > state.target_o2_kpa:
        excess_o2_kpa = new_o2_kpa - state.target_o2_kpa

        excess_o2_moles = (excess_o2_kpa * state.hab_vol_m3) / (r_kpa * (state.hab_temp_c + kelvin_offset))
        o2_stored_kg = (excess_o2_moles * o2_molar_mass) / 1000

        new_o2_stored_kg = state.o2_stored_kg + o2_stored_kg
              
        if new_o2_stored_kg >= state.o2_storage_capacity_kg:
            o2_control_mode = "venting"
            
            o2_leaked_kpa = state.o2_leak_rate_kpa_per_hr * hours_per_step
            o2_leaked_moles = (o2_leaked_kpa * state.hab_vol_m3) / (r_kpa * (state.hab_temp_c + kelvin_offset))
            o2_leaked_kg = (o2_leaked_moles * o2_molar_mass) / 1000

            o2_vented_kg = new_o2_stored_kg - state.o2_storage_capacity_kg + o2_leaked_kg
            new_o2_stored_kg = state.o2_storage_capacity_kg

        else:
            o2_control_mode = "storing"
        
        new_o2_kpa = state.target_o2_kpa


    #------------dict for updating state-------------♡ 
    oga_updates = {
        "o2_kpa": new_o2_kpa,
        "o2_stored_kg": new_o2_stored_kg,
        "h2_stored_kg": min(state.h2_storage_capacity_kg, state.h2_stored_kg + h2_produced_kg)
        }

    #-----------dict for printing outputs------------♡ 
    oga_outputs = {
        "oga_mode": oga_mode,
        "o2_added_kpa": o2_added_kpa,
        "h2_produced_kg": h2_produced_kg,
        "water_used_kg": water_used_kg,
        
        "oga_power_used_kw": power_used_kw,
        "oga_energy_used_kwh": power_used_kw * hours_per_step,
        "oga_heat_kw": heat_added_kw,
        "oga_heat_kwh": heat_added_kw * hours_per_step,
        
        "oga_limited_by_water": limited_by_water,
    }

    return oga_updates, oga_outputs
