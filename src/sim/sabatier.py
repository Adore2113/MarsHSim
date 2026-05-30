# file for handling recycling co2 into water and methane (CH4)


#--------------------constants-----------------------♡
kelvin_offset = 273.15   # add to celsius to convert to kelvin
r_kpa = 0.008314   # universal gas constant, 8.314 / 1000 
pa_per_kpa = 1000.0
kg_per_g = 0.001
exothermic_reaction = 0.65

h2_molar_mass = 2.016   # 1 mole h2 = 2.016g b/c h2 = 2 hydrogen atoms (1.008 g/mol each)
o2_molar_mass = 32.0   # grams per mole
co2_molar_mass = 44.01
ch4_molar_mass = 16.043
h2o_molar_mass = 18.015

water_kg_per_h2_kg = 0.45

min_h2_for_reaction_kg = 0.012
min_co2_for_reaction_kg = 0.012

base_sabatier_power_kw = 0.85
base_sabatier_temp_c = 300.0
base_sabatier_efficiency = 0.88

hysteresis = 1.5
venting_hysteresis = 0.7
#----------------------------------------------------♡


#----------------co2 + h2 = ch4 + H2o----------------♡
def run_sabatier(state, dt_min):
    hours_per_step = dt_min / 60

    sabatier_mode = "offline"
    water_produced_kg = 0.0
    ch4_produced_kg = 0.0
    h2_consumed_kg = 0.0
    co2_consumed_kpa = 0.0
    co2_consumed_kg = 0.0
    ch4_vented_kg = 0.0

    new_ch4_stored_kg = state.ch4_stored_kg
    new_ch4_kpa = state.ch4_kpa
    new_co2_stored_kg = state.co2_stored_kg
    new_co2_kpa = state.co2_kpa
    new_h2_stored_kg = state.h2_stored_kg

    if not state.sabatier_on:
        sabatier_mode = "offline"
        sabatier_power_used_kw = 0.0
        sabatier_heat_added_kw = 0.0
    
    elif state.power_mode == "critical":
        sabatier_mode = "power_save"

    #--------------available reactants--------------♡  
    else:
        available_co2_kg = state.co2_stored_kg
        available_h2_kg = state.h2_stored_kg

    #----------------sabatier modes-----------------♡  
        if available_co2_kg <= min_co2_for_reaction_kg and available_h2_kg <= min_h2_for_reaction_kg:
            sabatier_mode = "idle"
        
        elif available_co2_kg <= min_co2_for_reaction_kg * hysteresis:
            sabatier_mode = "limited_co2"
        
        elif available_h2_kg <= min_h2_for_reaction_kg * hysteresis:
            sabatier_mode = "limited_h2"
        
        else:
            sabatier_mode = "running"

    #----------power usage / heat per mode----------♡  
    if sabatier_mode in ("offline", "idle", "power_save"):
        sabatier_power_used_kw = 0.1
        sabatier_heat_added_kw = 0.1

    elif sabatier_mode in ("limited_co2", "limited_h2"):
        sabatier_power_used_kw = base_sabatier_power_kw * 0.75   # use less power
        sabatier_heat_added_kw = sabatier_power_used_kw * exothermic_reaction

    else:
        sabatier_power_used_kw = base_sabatier_power_kw
        sabatier_heat_added_kw = sabatier_power_used_kw * exothermic_reaction

    #---------------running sabatier----------------♡  
    if sabatier_mode in ("running", "limited_co2", "limited_h2"):
        co2_moles = available_co2_kg / (co2_molar_mass * kg_per_g)
        h2_moles = available_h2_kg / (h2_molar_mass * kg_per_g)

        reactions_available = min(co2_moles, h2_moles / 4) * base_sabatier_efficiency     # 1 co2 : 4 h2

        water_produced_kg = reactions_available * 2 * h2o_molar_mass * kg_per_g
        ch4_produced_kg = reactions_available * ch4_molar_mass * kg_per_g
        h2_consumed_kg = reactions_available * 4  * h2_molar_mass * kg_per_g
        co2_consumed_kg = reactions_available * co2_molar_mass * kg_per_g    
       
        co2_consumed_kpa = (co2_consumed_kg * r_kpa * (state.hab_temp_c + kelvin_offset) * 1000) / (state.hab_vol_m3 * co2_molar_mass)
        
        new_co2_stored_kg = max(0.0, state.co2_stored_kg - co2_consumed_kg)
        new_h2_stored_kg = max(0.0, state.h2_stored_kg - h2_consumed_kg)

        #----use from atmosphere if low storage----♡
        if new_co2_stored_kg <= 0.01 and state.co2_kpa > min_co2_for_reaction_kg:
            atmosphere_co2_kpa = min(0.15, state.co2_kpa * 0.12)
            atmosphere_co2_kg = (atmosphere_co2_kpa * state.hab_vol_m3) / (r_kpa * (state.hab_temp_c + kelvin_offset)) * co2_molar_mass            
            new_co2_kpa = max(0.0, state.co2_kpa - atmosphere_co2_kpa)
            
            co2_consumed_kg += atmosphere_co2_kg
            co2_consumed_kpa = atmosphere_co2_kpa

        #--------------venting Methane-------------♡
        new_ch4_stored_kg = state.ch4_stored_kg + ch4_produced_kg

        if new_ch4_stored_kg > state.ch4_storage_capacity_kg * venting_hysteresis:
            excess_ch4 = new_ch4_stored_kg - (state.ch4_storage_capacity_kg * venting_hysteresis)
            amount_to_vent = min(excess_ch4 * 0.25, 0.8)
            
            new_ch4_stored_kg -= amount_to_vent
            ch4_vented_kg += amount_to_vent
            sabatier_mode = "venting"

        if new_ch4_stored_kg > state.ch4_storage_capacity_kg:
            amount_to_vent = new_ch4_stored_kg - state.ch4_storage_capacity_kg
            new_ch4_stored_kg = state.ch4_storage_capacity_kg
            ch4_vented_kg += amount_to_vent
            sabatier_mode = "venting"
            sabatier_power_used_kw *= 1.15
        
        ch4_pressure_increase_kpa = 0.0

        if ch4_produced_kg > 0.001:
            ch4_moles = ch4_produced_kg / ch4_molar_mass
            ch4_pressure_increase_kpa = (ch4_moles * r_kpa * (state.hab_temp_c + kelvin_offset)) / state.hab_vol_m3
    
    #-----------------small gas leaks----------------♡  
        ch4_leaked_kpa = state.ch4_leak_rate_kpa_per_hr * hours_per_step
        new_ch4_kpa = state.ch4_kpa + ch4_pressure_increase_kpa + ch4_leaked_kpa


    h2_stored_kg = max(0.0, state.h2_stored_kg - h2_consumed_kg)
    
    #------------dict for updating state-------------♡ 
    sabatier_updates = {
        "co2_stored_kg": new_co2_stored_kg,
        "co2_kpa": new_co2_kpa,
        "ch4_kpa": new_ch4_kpa,
        "ch4_stored_kg": new_ch4_stored_kg,
        "h2_stored_kg": h2_stored_kg,
    }
   
    #-----------dict for printing outputs------------♡ 
    sabatier_outputs = {
        "sabatier_mode": sabatier_mode,
        "sabatier_power_used_kw": sabatier_power_used_kw,
        "sabatier_energy_used_kwh": sabatier_power_used_kw * hours_per_step,
        "sabatier_heat_added_kw": sabatier_heat_added_kw,
        "sabatier_heat_added_kwh": sabatier_heat_added_kw * hours_per_step,
        "sabatier_water_produced_kg": water_produced_kg,
        "sabatier_ch4_produced_kg": ch4_produced_kg,
        "sabatier_ch4_vented_kg": ch4_vented_kg,
        "sabatier_h2_consumed_kg": h2_consumed_kg,
        "sabatier_co2_consumed_kg": co2_consumed_kg,
        "sabatier_co2_consumed_kpa": co2_consumed_kpa, 
    }

    return sabatier_updates, sabatier_outputs
            