# file for Oxygen Generation Assembly (OGA) & Water Electrolysis


#--------------------constants-----------------------♡
kelvin_offset = 273.15   # add to celsius to convert to kelvin
pa_per_kpa = 1000.0   # kilopascals to pascals

r = 8.314   # the universal gas constant (pascals)
# or r = 0.008314 (for kpa)
h2_molar_mass = 2.016   # 1 mole h2 = 2.016g b/c h2 = 2 hydrogen atoms (1.008 g/mol each)
o2_molar_mass = 32.0

oga_max_o2_output_kpa = 0.004
#----------------------------------------------------♡


#------------oxygen regeneration process-------------♡
def o2_regen_kpa(state, o2_after_crew_kpa, dt_min):
    o2_needed_kpa = state.target_o2_kpa - o2_after_crew_kpa
    o2_added_kpa = min(oga_max_o2_output_kpa, max(0.0, o2_needed_kpa + 0.001))    o2_after_oga_kpa = o2_after_crew_kpa + o2_added_kpa

    return o2_after_oga_kpa, o2_added_kpa


#-------------handling hydrogen created--------------♡
def oga_h2_byproduct(state, o2_added_kpa):
    hab_temp_k = state.hab_temp_c + kelvin_offset
    o2_added_pa = o2_added_kpa * pa_per_kpa
    o2_produced_moles = (o2_added_pa * state.hab_vol_m3) / (r * hab_temp_k)    # ideal gas law: convert o2 pressure increase to moles
  
    h2_produced_moles = o2_produced_moles * 2    # electrolysis makes 2 moles of h2 for every mole of o2
    h2_produced_kg = (h2_produced_moles * h2_molar_mass) / 1000 

    return h2_produced_kg
    # storing hydrogen for now to use it later 


#-------------handling water consumption-------------♡
def oga_water_consumed(state, o2_added_kpa):
    hab_temp_k = state.hab_temp_c + kelvin_offset
    o2_added_pa = o2_added_kpa * pa_per_kpa
    o2_produced_moles = (o2_added_pa * state.hab_vol_m3) / (r * hab_temp_k)
    o2_produced_kg = (o2_produced_moles * o2_molar_mass) / 1000
    water_used_kg = o2_produced_kg * 1.125    # 1.125kg H2O per 1kg of O2 produced
    
    return water_used_kg
#----------------------------------------------------♡


#-----system power consumption and heat produced-----♡
def oga_power_and_heat(o2_added_kpa, dt_min):
    hours_per_step = dt_min / 60
    
    if o2_added_kpa > 0:
        oga_heat_kw = 1.2
        oga_heat_kwh = oga_heat_kw * hours_per_step
        oga_power_used_kw = 2.5
        oga_energy_used_kwh = oga_power_used_kw * hours_per_step

    else:
        oga_heat_kw = 0.0
        oga_heat_kwh = 0.0
        oga_power_used_kw = 0.0
        oga_energy_used_kwh = 0.0

    return oga_heat_kw, oga_heat_kwh, oga_power_used_kw, oga_energy_used_kwh


#------------oga result info per timestep------------♡
def run_oga(state, o2_after_crew_kpa, dt_min):
    hours_per_step = dt_min / 60.0
    o2_needed_kpa = state.target_o2_kpa - o2_after_crew_kpa
    
    hysteresis_kpa = 0.002    # only enough to avoid quick switching on and off, subject to change 

    if o2_needed_kpa < hysteresis_kpa:
        o2_added_kpa = 0.0

    else:
        o2_added_kpa = min(oga_max_o2_output, max(0.0, o2_needed_kpa + 0.001))
    
    water_used_kg = oga_water_consumed(state, o2_added_kpa)
 
    safety_backup_water_kg = 30.0 + (state.crew_count * 2.0)
    min_water_needed_for_oga_kg = water_used_kg + safety_backup_water_kg

    if state.potable_water_storage_kg < min_water_needed_for_oga_kg:
        return {
            "o2_after_oga_kpa": o2_after_crew_kpa,
            "o2_added_kpa": 0.0,
            "h2_produced_kg": 0.0,
            "water_used_kg": 0.0,
            "oga_heat_kw": 0.0,
            "oga_heat_kwh": 0.0,
            "oga_power_used_kw": 0.0,
            "oga_energy_used_kwh": 0.0,
            "oga_limited_by_water": True,
            "water_needed_for_oga_kg": min_water_needed_for_oga_kg - state.potable_water_storage_kg
        }

    o2_after_oga_kpa = o2_after_crew_kpa + o2_added_kpa
    h2_produced_kg = oga_h2_byproduct(state, o2_added_kpa)
    
    oga_heat_kw, oga_heat_kwh, oga_power_used_kw, oga_energy_used_kwh = oga_power_and_heat(o2_added_kpa, dt_min)

    return {
        "o2_after_oga_kpa": o2_after_oga_kpa,
        "o2_added_kpa": o2_added_kpa,
        "h2_produced_kg": h2_produced_kg,
        "water_used_kg": water_used_kg,
        "oga_heat_kw": oga_heat_kw,
        "oga_heat_kwh": oga_heat_kwh,
        "oga_power_used_kw": oga_power_used_kw,
        "oga_energy_used_kwh": oga_energy_used_kwh,
        "oga_limited_by_water": False
    }
