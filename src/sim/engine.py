from dataclasses import replace
from .state import Habitat_State

# ----default timestep----
default_dt_min = 5

hours_per_step = 5 / 60

crew_count = 30

# ----conversions ----
kelvin_offset = 273.15   # add to celsius to convert to kelvin
o2_kg_per_kpa = 18.2
co2_kg_per_kpa = 35.8
n2_kg_per_kpa = 22.75
ar_kg_per_kpa = 32.45
pa_per_kpa = 1000   # converts kilopascals to pascals

# ----targets and min/max values----
target_temp_c = 23.0
min_temp_c = 20.0
max_temp_c = 25.0

# 1 mole h2 = 2.016g b/c h2 = 2 hydrogen atoms (1.008 g/mol each)
r = 8.314   # the universal gas constant
h2_molar_mass = 2.016   # grams per mole of molecular hydrogen
o2_molar_mass = 32.0

# ----crew metabolism *per default timestep*----
def crew_metabolism_kpa(state):
# atmosphere gases
    o2_drop_kpa = 0.00011 * state.crew_count    # =: 0.0033
    co2_rise_kpa = 0.0000967 * state.crew_count    # = 0.0029

# temp in kW
    if state.crew_activity == "sleep":
        crew_temp_rise_kw = 0.083 * state.crew_count    # = 2.49
        crew_temp_rise_kwh = crew_temp_rise_kw * hours_per_step

    elif state.crew_activity == "exercise":   
        crew_temp_rise_kw = 0.30 * state.crew_count    # = 9.0
        crew_temp_rise_kwh = crew_temp_rise_kw * hours_per_step
    
    elif state.crew_activity == "intense":
        crew_temp_rise_kw = 0.35 * state.crew_count    # = 10.5
        crew_temp_rise_kwh = crew_temp_rise_kw * hours_per_step
    
    else: 
        crew_temp_rise_kw = 0.126 * state.crew_count    # = 3.78
        crew_temp_rise_kwh = crew_temp_rise_kw* hours_per_step

    return o2_drop_kpa, co2_rise_kpa, crew_temp_rise_kw, crew_temp_rise_kwh


# ----functions for amine beds scrubbing co2----
def removing_co2(state, co2_after_crew_kpa, next_time_s):  
    online_beds = 0
    for bed in state.amine_beds:
        if bed["status"] == "online":
            online_beds += 1
    
    total_scrub_kpa = online_beds * state.scrub_per_bed_kpa

    if next_time_s % 3300 == 0 and next_time_s != 0:   # every 55min switch beds w. a brief co2 spike
        total_scrub_kpa *= 0.80

    co2_excess_kpa = co2_after_crew_kpa - state.target_co2_kpa
    co2_scrubbed_kpa = min(total_scrub_kpa, max(0.0, co2_excess_kpa))
    new_co2_kpa = co2_after_crew_kpa - co2_scrubbed_kpa

    co2_stored_kpa = co2_scrubbed_kpa + state.co2_stored_kpa

    return new_co2_kpa, co2_scrubbed_kpa, co2_stored_kpa


# ----functions for OGA and water electrolysis----    Oxygen Generation Assembly
def o2_regen_kpa(state, o2_after_crew_kpa):
    o2_deficit_kpa = state.target_o2_kpa - o2_after_crew_kpa
    #make enough o2 to fill deficit + a bit extra, never negative
    oga_o2_output_kpa = min(0.004, max(0.0, o2_deficit_kpa + 0.001))
    new_o2_kpa = o2_after_crew_kpa + oga_o2_output_kpa

    return new_o2_kpa, oga_o2_output_kpa


def oga_h2_byproduct(state, o2_added_kpa):
    temp_k = state.hab_temp_c + kelvin_offset   # Kelvin conversion: 23C = 296.15K
    o2_added_pa = o2_added_kpa * pa_per_kpa   # convert: 1kPa = 1000 Pascals (p)
    o2_moles = (o2_added_pa * state.hab_vol_m3) / (r * temp_k)   # ideal gas law: convert pressure increase to moles
    h2_moles = o2_moles * 2   #electrolysis: 1o2 to 2h2
    h2_generated_kg = (h2_moles * h2_molar_mass) / 1000   #convert h2 moles to kg

    return h2_generated_kg
# storing hydrogen for now to use it later 


def oga_water_consumed(state, o2_added_kpa):
    temp_k = state.hab_temp_c + kelvin_offset
    o2_added_pa = o2_added_kpa * pa_per_kpa
    o2_moles = (o2_added_pa * state.hab_vol_m3) / (r * temp_k)
    o2_added_kg = (o2_moles * o2_molar_mass) / 1000
    h2o_consumed_kg = o2_added_kg * 1.125    #1.125kg H2O per 1kg of O2 produced
    
    return h2o_consumed_kg


def run_oga(state, o2_after_crew_kpa):
    if state.water_for_oga_kg <= 0:
        new_o2_kpa = o2_after_crew_kpa
        oga_o2_output_kpa = 0.0
        h2_generated_kg = 0.0
        water_used_kg = 0.0

        return new_o2_kpa, oga_o2_output_kpa, h2_generated_kg, water_used_kg

    new_o2_kpa, oga_o2_output_kpa = o2_regen_kpa(state, o2_after_crew_kpa)
    
    h2_generated_kg = oga_h2_byproduct(state, oga_o2_output_kpa)
    water_used_kg = oga_water_consumed(state, oga_o2_output_kpa)

    oga_temp_rise_kw = 1.2
    oga_temp_rise_kwh = oga_temp_rise_kw * hours_per_step

    return new_o2_kpa, oga_o2_output_kpa, h2_generated_kg, water_used_kg


# ----checking atmosphere gas levels----    #major constituant analyzer
def mca(state):  
    total_pressure_kpa = state.o2_kpa + state.co2_kpa + state.n2_kpa + state.ar_kpa 
    return total_pressure_kpa


# ----controlling atmosphere gas levels----
def run_buffer_gas_control(state):
    total_pressure_kpa = mca(state)

    if total_pressure_kpa <= state.min_safe_pressure_kpa:
        amount_to_add_kpa = state.target_pressure_kpa - total_pressure_kpa
        
        if state.n2_stored_kpa >= amount_to_add_kpa:    # emergency (pressure recover first)
            state.n2_kpa += amount_to_add_kpa
            state.n2_stored_kpa -= amount_to_add_kpa    # capped by avaliable supply
        
        else:
            state.n2_kpa += state.n2_stored_kpa
            state.n2_stored_kpa = 0.0

    elif total_pressure_kpa < state.target_pressure_kpa:    # pressure balance first, but capped so it doesn't over-add
        amount_to_add_kpa = state.target_pressure_kpa - total_pressure_kpa

        if state.n2_kpa < state.target_n2_kpa:
            n2_space_kpa = state.target_n2_kpa - state.n2_kpa
            n2_to_add_kpa = min(amount_to_add_kpa, n2_space_kpa)
            state.n2_kpa += n2_to_add_kpa
            amount_to_add_kpa -= n2_to_add_kpa
        
        if amount_to_add_kpa > 0 and state.ar_kpa < state.target_ar_kpa:
            ar_space_kpa = state.target_ar_kpa - state.ar_kpa
            ar_to_add_kpa = min(amount_to_add_kpa, ar_space_kpa)
            state.ar_kpa += ar_to_add_kpa
            amount_to_add_kpa -= ar_to_add_kpa
    
    return state


# ----alerts ----
def gas_alert(state):
    alerts = []
    if state.o2_kpa <= 17.0:
        alerts.append("ALERT: Oxygen critical")
    
    elif state.o2_kpa <= 19.5:
        alerts.append("ALERT: Oxygen low")
    
    if state.o2_kpa >= 22.0:
        alerts.append("ALERT: Oxygen very high | fire risk")

    if state.co2_kpa >= 1.0:
        alerts.append("ALERT: Carbon Dioxide high")

    if state.co2_kpa >= 2.0:
        alerts.append("ALERT: Carbon Dioxide critical")

    # later add total pressure, leak detection, when scrubbers are full (saturated)
    # water supply low, n2 supply low, temp out of range
    
    # eventually airlocks humidyity, temp loops

    return alerts


def step(state: Habitat_State, dt_min: int = default_dt_min):
    dt_s = int(dt_min * 60)
    next_time_s = state.mission_time_s + dt_s

    o2_drop_kpa, co2_rise_kpa = crew_metabolism_kpa(state)

    o2_after_crew_kpa = state.o2_kpa - o2_drop_kpa
    co2_after_crew_kpa = state.co2_kpa + co2_rise_kpa

    new_o2_kpa, oga_o2_output_kpa, h2_generated_kg, water_used_kg = run_oga(state, o2_after_crew_kpa)
    new_co2_kpa, scrubbed_amount_kpa, new_co2_stored_kpa = removing_co2(state, co2_after_crew_kpa, next_time_s)
    new_co2_stored_kpa = state.co2_stored_kpa

    new_water_kg = max(0.0, state.water_for_oga_kg - water_used_kg)
    new_h2_stored_kg = state.h2_stored_kg + h2_generated_kg


    new_state = replace(
        state,
        mission_time_s = next_time_s,
        o2_kpa = round(new_o2_kpa, 4),
        co2_kpa = round(new_co2_kpa, 4),
        co2_stored_kpa = round(state.co2_stored_kpa, 4),
        h2_stored_kg = round(new_h2_stored_kg, 6),
        water_for_oga_kg = round(new_water_kg, 3)
    )

    return new_state, scrubbed_amount_kpa


