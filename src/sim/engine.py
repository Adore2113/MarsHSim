from dataclasses import replace
from .state import Habitat_State

# ----default timestep----
default_dt_min = 5
#hours_per_step = dt_min / 60

# ----conversions ----
kelvin_offset = 273.15   # add to celsius to convert to kelvin
o2_kg_per_kpa = 18.2
co2_kg_per_kpa = 35.8
n2_kg_per_kpa = 22.75
ar_kg_per_kpa = 32.45
pa_per_kpa = 1000   # kilopascals to pascals

# ----chemistry constants----
r = 8.314   # the universal gas constant
h2_molar_mass = 2.016   # 1 mole h2 = 2.016g b/c h2 = 2 hydrogen atoms (1.008 g/mol each)
o2_molar_mass = 32.0

# ---- temperature targets----
target_temp_c = 23.0
min_temp_c = 20.0
max_temp_c = 25.0

# ----time----
def get_sol_time(mission_time_s):
    total_sol_seconds = 88775
    sol_seconds = mission_time_s % total_sol_seconds
    hour_24 = sol_seconds // 3600
    minutes = (sol_seconds % 3600) // 60
    return hour_24, minutes


# ----crew metabolism per default timestep----
def crew_metabolism(state, dt_min):
    hours_per_step = dt_min / 60
    # atmosphere gases
    o2_drop_kpa = 0.00011 * state.crew_count    # =: 0.0033
    co2_rise_kpa = 0.0000967 * state.crew_count    # = 0.0029

    # tempurature
    if state.crew_activity == "sleep":
        crew_temp_rise_kw = 0.083 * state.crew_count    # = 2.49
        crew_temp_rise_kwh = crew_temp_rise_kw * hours_per_step

    elif state.crew_activity == "exercise":   
        crew_temp_rise_kw = 0.280 * state.crew_count    # = 9.0
        crew_temp_rise_kwh = crew_temp_rise_kw * hours_per_step
    
    elif state.crew_activity == "intense":
        crew_temp_rise_kw = 0.350 * state.crew_count    # = 10.5
        crew_temp_rise_kwh = crew_temp_rise_kw * hours_per_step
    
    else: 
        crew_temp_rise_kw = 0.120 * state.crew_count    # = 3.78
        crew_temp_rise_kwh = crew_temp_rise_kw * hours_per_step

    return o2_drop_kpa, co2_rise_kpa, crew_temp_rise_kw, crew_temp_rise_kwh


def lights(state, dt_min):
    hour_24, minutes = get_sol_time(state.mission_time_s)
    hours_per_step = dt_min / 60
    light_heat_added_kw = 0.0

    if 6 <= hour_24 < 21 or (hour_24 == 21 and minutes < 30):
        light_level = 1.0
        light_heat_added_kw = 4.0
        light_heat_added_kwh = light_heat_added_kw * hours_per_step
    
    else:
        light_level = 0.2
        light_heat_added_kw = 0.8
        light_heat_added_kwh = light_heat_added_kw * hours_per_step

    return light_level, light_heat_added_kw, light_heat_added_kwh



# ----functions for amine beds scrubbing co2----
def run_co2_scrub(state, co2_after_crew_kpa, next_time_s, dt_min):  
    hours_per_step = dt_min / 60
    online_bed_count = 0
    for bed in state.amine_beds:
        if bed["status"] == "online":
            online_bed_count += 1
    
    max_scrub_removal_kpa = online_bed_count * state.scrub_per_bed_kpa

    # efficiency drop when co2 is already low
    if co2_after_crew_kpa < 0.2:
        max_scrub_removal_kpa *= 0.40
    elif co2_after_crew_kpa < 0.4:
        max_scrub_removal_kpa *= 0.70

    if next_time_s % 3300 == 0 and next_time_s != 0:   # every 55min switch beds w. a brief co2 spike
        max_scrub_removal_kpa *= 0.80

    excess_co2_kpa = co2_after_crew_kpa - state.target_co2_kpa
    
    co2_removed_kpa = min(max_scrub_removal_kpa, max(0.0, excess_co2_kpa))
    co2_after_scrub_kpa = co2_after_crew_kpa - co2_removed_kpa
    new_co2_stored_kpa = co2_removed_kpa + state.co2_stored_kpa
    
    # heat produced, according to removal
    co2_scrubber_heat_per_kpa_kw = 1200.0
    co2_scrubber_heat_added_kw = co2_removed_kpa * co2_scrubber_heat_per_kpa_kw / 1000.0
    
    baseline_bed_heat_added_kw = online_bed_count * 0.4

    co2_scrubber_heat_added_kw = co2_scrubber_heat_added_kw + baseline_bed_heat_added_kw    
    co2_scrubber_heat_added_kwh = co2_scrubber_heat_added_kw * hours_per_step

    return co2_after_scrub_kpa, co2_removed_kpa, new_co2_stored_kpa, co2_scrubber_heat_added_kw, co2_scrubber_heat_added_kwh


# ----functions for OGA and water electrolysis----    Oxygen Generation Assembly
def o2_regen_kpa(state, o2_after_crew_kpa, dt_min):
    o2_needed_kpa = state.target_o2_kpa - o2_after_crew_kpa
    oga_max_o2_output = 0.004
    o2_added_kpa = min(oga_max_o2_output, max(0.0, o2_needed_kpa + 0.001))     # make enough o2 to fill deficit + a bit extra, never negative
    o2_after_oga_kpa = o2_after_crew_kpa + o2_added_kpa

    return o2_after_oga_kpa, o2_added_kpa


def oga_h2_byproduct(state, o2_added_kpa):
    hab_temp_k = state.hab_temp_c + kelvin_offset
    o2_added_pa = o2_added_kpa * pa_per_kpa
    o2_produced_moles = (o2_added_pa * state.hab_vol_m3) / (r * hab_temp_k)    # ideal gas law: convert o2 pressure increase to moles
  
    h2_produced_moles = o2_produced_moles * 2    # electrolysis makes 2 moles of h2 for every mole of o2
    h2_produced_kg = (h2_produced_moles * h2_molar_mass) / 1000 

    return h2_produced_kg
    # storing hydrogen for now to use it later 


def oga_water_consumed(state, o2_added_kpa):
    hab_temp_k = state.hab_temp_c + kelvin_offset
    o2_added_pa = o2_added_kpa * pa_per_kpa
    o2_produced_moles = (o2_added_pa * state.hab_vol_m3) / (r * hab_temp_k)
    o2_produced_kg = (o2_produced_moles * o2_molar_mass) / 1000
    water_used_kg = o2_produced_kg * 1.125    # 1.125kg H2O per 1kg of O2 produced
    
    return water_used_kg


def run_oga(state, o2_after_crew_kpa, dt_min):
    hours_per_step = dt_min / 60
    o2_after_oga_kpa, o2_added_kpa = o2_regen_kpa(state, o2_after_crew_kpa, dt_min)
    water_used_kg = oga_water_consumed(state, o2_added_kpa)
    
    if state.water_for_oga_kg < water_used_kg:
        return {
            "o2_after_oga_kpa": o2_after_crew_kpa,
            "o2_added_kpa": 0.0,
            "h2_produced_kg": 0.0,
            "water_used_kg": 0.0,
            "oga_heat_kw": 0.0,
            "oga_heat_kwh": 0.0,
        }

    h2_produced_kg = oga_h2_byproduct(state, o2_added_kpa)

    oga_heat_kw = 1.2
    oga_heat_kwh = oga_heat_kw * hours_per_step

    return {
        "o2_after_oga_kpa": o2_after_oga_kpa,
        "o2_added_kpa": o2_added_kpa,
        "h2_produced_kg": h2_produced_kg,
        "water_used_kg": water_used_kg,
        "oga_heat_kw": oga_heat_kw,
        "oga_heat_kwh": oga_heat_kwh,
    }

# ----checking atmosphere gas levels---- 
def mca(state):     # major constituant analyzer  
    total_pressure_kpa = state.o2_kpa + state.co2_kpa + state.n2_kpa + state.ar_kpa 
    return total_pressure_kpa


# ----controlling atmosphere gas levels----
def run_buffer_gas_control(state, dt_min):
    hours_per_step = dt_min / 60

    n2_kpa = state.n2_kpa
    n2_stored_kpa = state.n2_stored_kpa
    ar_kpa = state.ar_kpa
    ar_stored_kpa = state.ar_stored_kpa

    total_buffer_gas_added_kpa = 0.0

    buffer_gas_heat_per_kpa_kw = 1.5

    buffer_gas_heat_added_kw = 0.0
    buffer_gas_heat_added_kwh = 0.0

    total_pressure_kpa = state.o2_kpa + state.co2_kpa + n2_kpa + ar_kpa

    if total_pressure_kpa <= state.min_safe_pressure_kpa:
        pressure_needed_kpa = state.target_pressure_kpa - total_pressure_kpa

        if n2_stored_kpa > 0 and n2_stored_kpa >= pressure_needed_kpa:
           n2_kpa += pressure_needed_kpa
           n2_stored_kpa -= pressure_needed_kpa
           total_buffer_gas_added_kpa += pressure_needed_kpa

        else:
            n2_kpa += n2_stored_kpa
            total_buffer_gas_added_kpa += n2_stored_kpa
            n2_stored_kpa = 0.0

    elif total_pressure_kpa < state.target_pressure_kpa:
        pressure_needed_kpa = state.target_pressure_kpa - total_pressure_kpa

        if n2_kpa < state.target_n2_kpa:
            n2_room_left_kpa = state.target_n2_kpa - n2_kpa
            n2_to_add_kpa = min(pressure_needed_kpa, n2_room_left_kpa, n2_stored_kpa)
            
            n2_kpa += n2_to_add_kpa
            n2_stored_kpa -= n2_to_add_kpa
            total_buffer_gas_added_kpa += n2_to_add_kpa
            
            pressure_needed_kpa -= n2_to_add_kpa

        if pressure_needed_kpa > 0 and ar_kpa < state.target_ar_kpa:
            ar_room_left_kpa = state.target_ar_kpa - ar_kpa
            ar_to_add_kpa = min(pressure_needed_kpa, ar_room_left_kpa, ar_stored_kpa)
            
            ar_kpa += ar_to_add_kpa
            ar_stored_kpa -= ar_to_add_kpa
            total_buffer_gas_added_kpa += ar_to_add_kpa
            
            pressure_needed_kpa -= ar_to_add_kpa

    else:
        pass

    buffer_gas_heat_added_kw = total_buffer_gas_added_kpa * buffer_gas_heat_per_kpa_kw
    buffer_gas_heat_added_kwh = buffer_gas_heat_added_kw * hours_per_step
    
    return {
        "n2_kpa" : n2_kpa,
        "ar_kpa" : ar_kpa,
        "n2_stored_kpa": n2_stored_kpa,
        "ar_stored_kpa": ar_stored_kpa,
        "buffer_gas_heat_added_kw": buffer_gas_heat_added_kw,
        "buffer_gas_heat_added_kwh": buffer_gas_heat_added_kwh,
    }


# ----alerts ----
def gas_alert(state):
    gas_alerts = []
    
    #o2
    if state.o2_kpa <= 17.0:
        gas_alerts.append("ALERT: Oxygen critical")
    
    elif state.o2_kpa <= 19.5:
        gas_alerts.append("ALERT: Oxygen low")
    
    if state.o2_kpa >= 22.0:
        gas_alerts.append("ALERT: Oxygen very high | fire risk")

    #co2
    if state.co2_kpa >= 2.0:
        gas_alerts.append("ALERT: Carbon Dioxide critical")

    elif state.co2_kpa >= 1.0:
        gas_alerts.append("ALERT: Carbon Dioxide high")

    # later add total pressure, leak detection, when scrubbers are full (saturated)
    # water supply low, n2 supply low, temp out of range
    # eventually airlocks humidity, temp loops

    return gas_alerts


def step(state: Habitat_State, dt_min: int = default_dt_min):
    dt_s = int(dt_min * 60)
    next_time_s = state.mission_time_s + dt_s

    o2_drop_kpa, co2_rise_kpa, crew_temp_rise_kw, crew_temp_rise_kwh = crew_metabolism(state, dt_min)

    o2_after_crew_kpa = state.o2_kpa - o2_drop_kpa
    co2_after_crew_kpa = state.co2_kpa + co2_rise_kpa

    oga_results = run_oga(state, o2_after_crew_kpa, dt_min)
    o2_after_oga_kpa = oga_results["o2_after_oga_kpa"]
    o2_added_kpa = oga_results["o2_added_kpa"]
    h2_produced_kg = oga_results["h2_produced_kg"]
    water_used_kg = oga_results["water_used_kg"]
    oga_heat_kw = oga_results["oga_heat_kw"]
    oga_heat_kwh = oga_results["oga_heat_kwh"]

    co2_after_scrub_kpa, co2_removed_kpa, new_co2_stored_kpa, co2_scrubber_heat_added_kw, co2_scrubber_heat_added_kwh = run_co2_scrub(state, co2_after_crew_kpa, next_time_s, dt_min)

    new_water_for_oga_kg = max(0.0, state.water_for_oga_kg - water_used_kg)
    new_h2_stored_kg = state.h2_stored_kg + h2_produced_kg

    pre_buffer_state = replace(
        state,
        mission_time_s=next_time_s,
        light_level = lights(state, dt_min),
        o2_kpa=round(o2_after_oga_kpa, 4),
        co2_kpa=round(co2_after_scrub_kpa, 4),
        co2_stored_kpa=round(new_co2_stored_kpa, 4),
        h2_stored_kg=round(new_h2_stored_kg, 6),
        water_for_oga_kg=round(new_water_for_oga_kg, 3),
    )

    buffer_gas_results = run_buffer_gas_control(pre_buffer_state, dt_min)

    new_state = replace(
    pre_buffer_state,
    n2_kpa=round(buffer_gas_results["n2_kpa"], 4),
    ar_kpa=round(buffer_gas_results["ar_kpa"], 4),
    n2_stored_kpa=round(buffer_gas_results["n2_stored_kpa"], 4),
    ar_stored_kpa=round(buffer_gas_results["ar_stored_kpa"], 4),
    )

    return new_state, co2_removed_kpa


