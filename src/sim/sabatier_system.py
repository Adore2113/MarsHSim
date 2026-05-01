# file for handling recylcing co2 into water and methane (CH4)


#--------------------constants-----------------------♡
kelvin_offset = 273.15   # add to celsius to convert to kelvin
r_kpa = 0.008314   # the universal gas constant, 8.314 / 1000 
pa_per_kpa = 1000.0   # 1kpa = 1000pa

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

hysteresis_kpa = 0.05
#----------------------------------------------------♡


#-------------convert co2 from kpa to kg-------------♡
def run_conversions(state):
    temp_k = state.hab_temp_c + kelvin_offset
    co2_kg = (state.co2_kpa * state.hab_vol_m3 * co2_molar_mass) / (r_kpa * temp_k * 1000)

    return temp_k, co2_kg
#----------------co2 + h2 = ch4 + H2o----------------♡
def run_sabatier(state, dt_min, co2_kg):
    hours_per_step = dt_min / 60
    current_h2_kg = state.h2_kg
    current_co2_kg = co2_kg

    #----------------sabatier modes-----------------♡  
    if not state.sabatier_on:
        sabatier_mode = "offline"

    elif current_co2_kg <= min_co2_for_reaction_kpa and current_h2_kg <= min_h2_for_reaction_kg:
        sabatier_mode = "idle"
    
    elif current_co2_kg <= min_co2_for_reaction_kpa:
        sabatier_mode = "idle, limited co2"
    
    elif current_h2_kg <= min_h2_for_reaction_kg:
        sabatier_mode = "idle, limited h2"
    
    else:
        sabatier_mode = "running"

    if sabatier_mode =  "running":
        ...