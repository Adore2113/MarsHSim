from dataclasses import replace
from .state import Habitat_State

default_dt_min = 5

crew_count = 30
hab_vol_m3 = 2000.0
hab_temp_c = 23

kelvin_offset = 273.15   # add to celsius to convert to kelvin

target_pressure_kpa = 60.0
target_o2_kpa = 20.0
target_co2_kpa = 0.4
target_nitrogen_kpa = 17.0
target_argon_kpa = 22.6
 
# 1 mole h2 = 2.016g b/c h2 = 2 hydrogen atoms (1.008 g/mol each)
r = 8.314   # the universal gas constant
pa_per_kpa = 1000   # converts kilopascals to pascals
h2_molar_mass = 2.016   # grams per mole of molecular hydrogen
o2_molar_mass = 32.0

scrub_per_bed_kpa = 0.0045

def crew_metabolism_kpa(state):
# o2 drop for 30p: 0.0033
# co2 rise for 30p: 0.0029
    o2_drop_kpa = 0.00011 * state.crew_count
    co2_rise_kpa = 0.0000967 * state.crew_count

    return o2_drop_kpa, co2_rise_kpa


def gas_alert(state):
    alerts = []
    if state.o2_kpa <= 19.5:
        alerts.append("ALERT: Oxygen low")
   
    if state.o2_kpa <= 17.0:
        alerts.append("ALERT: Oxygen critical")
    
    if state.o2_kpa >= 22.0:
        alerts.append("ALERT: Oxygen very high | fire risk")

    if state.co2_kpa >= 1.0:
        alerts.append("ALERT: Carbon Dioxide high")

    if state.co2_kpa >= 2.0:
        alerts.append("ALERT: Carbon Dioxide critical")

    return alerts


def removing_co2(state, co2_after_crew_kpa, next_time_s):  
    online_beds = 0
    for bed in state.amine_beds:
        if bed["status"] == "online":
            online_beds += 1
    
    total_scrub_kpa = online_beds * scrub_per_bed_kpa

# every 55min switch beds w. a brief co2 spike
    if next_time_s % 3300 == 0 and next_time_s != 0:
        total_scrub_kpa *= 0.80

    co2_excess_kpa = co2_after_crew_kpa - target_co2_kpa
    co2_scrubbed_kpa = min(total_scrub_kpa, max(0.0, co2_excess_kpa))
    new_co2_kpa = co2_after_crew_kpa - co2_scrubbed_kpa

    return new_co2_kpa, co2_scrubbed_kpa

# ---functions for OGA and water electrolysis---
def o2_regen_kpa(state, o2_after_crew_kpa):
    o2_deficit_kpa = target_o2_kpa - o2_after_crew_kpa
#make enough o2 to fill deficit + a bit extra, never negative
    oga_o2_output_kpa = min(0.004, max(0.0, o2_deficit_kpa + 0.001))
    new_o2_kpa = o2_after_crew_kpa + oga_o2_output_kpa

    return new_o2_kpa, oga_o2_output_kpa


def oga_h2_byproduct(o2_added_kpa):
    temp_k = hab_temp_c + kelvin_offset   # Kelvin conversion: 23C = 296.15K
    o2_added_pa = o2_added_kpa * pa_per_kpa   # convert: 1kPa = 1000 Pascals (p)
    o2_moles = (o2_added_pa * hab_vol_m3) / (r * temp_k)   # ideal gas law: convert pressure increase to moles
    h2_moles = o2_moles * 2   #electrolysis: 1o2 to 2h2
    h2_generated_kg = (h2_moles * h2_molar_mass) / 1000   #convert h2 moles to kg

    return h2_generated_kg

# storing hydrogen for now to use it later 

def oga_water_consumed(o2_added_kpa):
    temp_k = hab_temp_c + kelvin_offset
    o2_added_pa = o2_added_kpa * pa_per_kpa
    o2_moles = (o2_added_pa * hab_vol_m3) / (r * temp_k)

    o2_added_kg = (o2_moles * o2_molar_mass) / 1000

    h2o_consumed_kg = o2_added_kg * 1.125    #1.125kg H2O per 1kg of O2 produced

    return h2o_consumed_kg


def step(state: Habitat_State, dt_min: int = default_dt_min):
    dt_s = int(dt_min * 60)
    next_time_s = state.mission_time_s + dt_s

    o2_drop_kpa, co2_rise_kpa = crew_metabolism_kpa(state)

    o2_after_crew_kpa = state.o2_kpa - o2_drop_kpa
    co2_after_crew_kpa = state.co2_kpa + co2_rise_kpa

    new_o2_kpa, oga_o2_output_kpa = o2_regen_kpa(state, o2_after_crew_kpa)
    
    h2_generated_kg = oga_h2_byproduct(oga_o2_output_kpa)
    
    new_co2_kpa, scrubbed_amount_kpa = removing_co2(state, co2_after_crew_kpa, next_time_s)
    
    water_used_kg = oga_water_consumed(oga_o2_output_kpa)

    new_h2_stored_kg = state.h2_stored_kg + h2_generated_kg


    new_state = replace(
        state,
        mission_time_s = next_time_s,
        o2_kpa = round(new_o2_kpa, 4),
        co2_kpa = round(new_co2_kpa, 4),
        h2_stored_kg = round(new_h2_stored_kg, 6)
    )

    return new_state, scrubbed_amount_kpa


