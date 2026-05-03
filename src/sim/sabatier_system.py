# file for handling recycling co2 into water and methane (CH4)


#--------------------constants-----------------------♡
kelvin_offset = 273.15   # add to celsius to convert to kelvin
r_kpa = 0.008314   # the universal gas constant, 8.314 / 1000 
pa_per_kpa = 1000.0
kg_per_g = 0.001
exothermic_reaction = 0.65

h2_molar_mass = 2.016   # 1 mole h2 = 2.016g b/c h2 = 2 hydrogen atoms (1.008 g/mol each)
o2_molar_mass = 32.0   # grams per mole
co2_molar_mass = 44.01
ch4_molar_mass = 16.043
h2o_molar_mass = 18.015

h2_to_water_ratio = 0.45

min_h2_for_reaction_kg = 0.05
min_co2_for_reaction_kpa = 0.05

base_sabatier_power_kw = 0.85
base_sabatier_temp_c = 300.0
base_sabatier_efficiency = 0.75

hysteresis = 1.5
#----------------------------------------------------♡


#-------------convert co2 from kpa to kg-------------♡
def run_conversions(state):
    temp_k = state.hab_temp_c + kelvin_offset
    co2_kg = (state.co2_kpa * state.hab_vol_m3 * co2_molar_mass) / (r_kpa * temp_k * 1000)

    return temp_k, co2_kg


#----------------co2 + h2 = ch4 + H2o----------------♡
def run_sabatier(state, dt_min, co2_kg, temp_k):
    hours_per_step = dt_min / 60
    _, co2_kg = run_conversions(state)
    h2_kg = state.h2_stored_kg

    #------------default sabatier values------------♡  
    sabatier_mode = "offline"
    water_produced_kg = 0.0
    ch4_produced_kg = 0.0
    h2_consumed_kg = 0.0
    co2_consumed_kpa = 0.0
    ch4_vented_kg = 0.0
    new_ch4_stored_kg = state.ch4_stored_kg
    ch4_kpa = state.ch4_kpa

    #----------------sabatier modes-----------------♡  
    if not state.sabatier_on:
        sabatier_mode = "offline"

    elif co2_kg <= min_co2_for_reaction_kpa and h2_kg <= min_h2_for_reaction_kg:
        sabatier_mode = "idle"
    
    elif co2_kg <= min_co2_for_reaction_kpa * hysteresis:
        sabatier_mode = "limited co2"
    
    elif h2_kg <= min_h2_for_reaction_kg * hysteresis:
        sabatier_mode = "limited h2"
    
    else:
        sabatier_mode = "running"

    #----------power usage / heat per mode----------♡  
    if sabatier_mode in ("offline", "idle"):
        sabatier_power_used_kw = 0.0
        sabatier_heat_added_kw = 0.0

    elif sabatier_mode in ("limited_co2", "limited_h2"):
        sabatier_power_used_kw = base_sabatier_power_kw * 0.55    # use less power
        sabatier_heat_added_kw = sabatier_power_used_kw * exothermic_reaction

    elif sabatier_mode == "venting":
        sabatier_power_used_kw = base_sabatier_power_kw * 1.25    # more power
        sabatier_heat_added_kw = sabatier_power_used_kw * exothermic_reaction

    else:  # normal running
        sabatier_power_used_kw = base_sabatier_power_kw
        sabatier_heat_added_kw = sabatier_power_used_kw * exothermic_reaction

    #---------------running sabatier----------------♡  
    if sabatier_mode in ("running", "limited co2", "limited h2"):
        h2_moles = h2_kg / h2_molar_mass
        co2_moles = co2_kg / co2_molar_mass

        reactions_avaliable = min(h2_moles / 4, co2_moles) * base_sabatier_efficiency     # 1 co2 : 4 h2

        water_produced_kg = reactions_avaliable * 2 * h2o_molar_mass * kg_per_g
        ch4_produced_kg = reactions_avaliable * 1 * ch4_molar_mass * kg_per_g
        h2_consumed_kg = reactions_avaliable * 4  * h2_molar_mass * kg_per_g
        co2_consumed_kg = reactions_avaliable * 1 * co2_molar_mass * kg_per_g
        co2_consumed_kpa = (co2_consumed_kg * r_kpa * (state.hab_temp_c + kelvin_offset) * 1000) / (state.hab_vol_m3 * co2_molar_mass)
        #-----------ventting excess Methane---------♡
        ch4_max_storage_kg = state.ch4_storage_capacity_kg
        new_ch4_stored_kg = state.ch4_stored_kg + ch4_produced_kg

        if new_ch4_stored_kg > ch4_max_storage_kg:
            ch4_vented_kg = min(new_ch4_stored_kg - ch4_max_storage_kg)
            new_ch4_stored_kg = ch4_max_storage_kg
            sabatier_mode = "venting"

        ch4_kpa = state.ch4_kpa + (ch4_produced_kg * 0.2)    # hinting at a tiny leak from atmosphere, might remove later   
    
        sabatier_energy_used_kwh = sabatier_power_used_kw * hours_per_step
        
        sabatier_heat_added_kw = sabatier_power_used_kw * exothermic_reaction
        sabatier_heat_added_kwh  = sabatier_heat_added_kw * hours_per_step
    #------------dict for updating state-------------♡ 
    sabatier_updates = {
        "ch4_kpa": ch4_kpa,
        "ch4_stored_kg": new_ch4_stored_kg,
    }
   
    #-----------dict for printing outputs------------♡ 
    sabatier_outputs = {
        "sabatier_mode": sabatier_mode,
        "sabatier_power_used_kw": sabatier_power_used_kw,
        "sabatier_energy_used_kwh": sabatier_energy_used_kwh,
        "sabatier_heat_added_kw": sabatier_heat_added_kw,
        "sabatier_heat_added_kwh": sabatier_heat_added_kwh,
        "sabatier_water_produced_kg": water_produced_kg,
        "sabatier_ch4_produced_kg": ch4_produced_kg,
        "sabatier_ch4_vented_kg": ch4_vented_kg,
        "sabatier_h2_consumed_kg": h2_consumed_kg,
        "sabatier_co2_consumed_kpa": co2_consumed_kpa, 
    }

    return sabatier_updates, sabatier_outputs
            