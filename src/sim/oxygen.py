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
water_kg_per_o2_kg = 1.125
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

    o2_needed_kpa = state.target_o2_kpa - o2_after_crew_kpa

    #-------------------oga modes-------------------♡  
    if o2_needed_kpa <= hysteresis_kpa:
        oga_mode = "idle"

    else:
        oga_mode = "running"

    #------------------oga running------------------♡
    if oga_mode == "running":
        o2_added_kpa = min(oga_max_o2_output_kpa, max(0.0, o2_needed_kpa + 0.001))
        
        o2_produced_moles = (o2_added_kpa * state.hab_vol_m3) / (r_kpa * (state.hab_temp_c + kelvin_offset))
        o2_produced_kg = (o2_produced_moles * o2_molar_mass) / 1000
     
        h2_produced_moles = o2_produced_moles * 2
        h2_produced_kg = (h2_produced_moles * h2_molar_mass) / 1000
    
        water_used_kg = o2_produced_kg * water_kg_per_o2_kg

    #--------------water storage check--------------♡
        min_water_needed_kg = water_used_kg + (state.crew_count * 2.0) + safety_backup_water_kg
        
        if state.potable_water_storage_kg < min_water_needed_kg:
            oga_mode = "limited_water"
            limited_by_water = True
            water_used_kg = 0.0
            h2_produced_kg = 0.0
            o2_added_kpa = 0.0
        
    #----------power usage / heat per mode----------♡  
    if oga_mode in ("offline", "idle"):
        power_used_kw = 0.1
        heat_added_kw = 0.5
    
    elif oga_mode == "limited_water":
        power_used_kw = base_oga_power_kw * 0.60
        heat_added_kw = base_oga_heat_kw * 0.60

    elif oga_mode == "running":
        power_used_kw = base_oga_power_kw
        heat_added_kw = base_oga_heat_kw
    
    else:
        power_used_kw = 0.0
        heat_added_kw = 0.0

    #------------dict for updating state-------------♡ 
    oga_updates = {
        "o2_kpa": o2_after_crew_kpa + o2_added_kpa,
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
