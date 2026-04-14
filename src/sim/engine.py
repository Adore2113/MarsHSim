from dataclasses import replace
from .state import Habitat_State
from .oxygen_system import run_oga
from .buffer_gas_system import mca, run_buffer_gas_control
from .co2_scrubber_system import run_co2_scrub
from .crew_metabolism import crew_metabolism
from .power_system import total_power_usage, wellness_lights, run_system_power
from .mars_time import get_sol_time, determine_sunlight_amount, daylight_per_m2_kw, current_sol_number
from .power_system import lights
from .alerts import get_status, gas_alerts, power_alerts
#----------------------------------------------------♡

#--------------------constants-----------------------♡
default_dt_min = 5    # default timestep
#----------------------------------------------------♡


#-----------advance time info per timestep-----------♡
def collect_advance_time(state, dt_min):
    dt_s = int(dt_min * 60)
    next_time_s = state.mission_time_s + dt_s
    
    return dt_s, next_time_s    # maybe remove dt_s?


#-----------heat generated info per timestep---------♡
def collect_heat_generated(state, dt_min, light_results, wellness_light_results, oga_results):
    light_heat_kw = light_results["light_heat_added_kw"]
    light_heat_kwh = light_results["light_heat_added_kwh"] 
    
    w_light_heat_kw = wellness_light_results["w_light_heat_kw"]
    w_light_heat_kwh = wellness_light_results["w_light_heat_kwh"]
    
    oga_heat_kw = oga_results["oga_heat_kw"]
    oga_heat_kwh = oga_results["oga_heat_kwh"]

#---------------power info per timestep--------------♡
def collect_power_info(state, dt_min):
    light_level, _, _, light_power_used_kw, light_power_used_kwh = lights(state, dt_min)
    wellness_lights_on, wellness_light_level, _, _, w_light_power_used_kw, w_light_power_used_kwh = wellness_lights(state, dt_min)


#------------atmosphere info per timestep------------♡


#----------------------------------------------------♡

#----------------------------------------------------♡

#----------------------------------------------------♡

#----------------------------------------------------♡

#----------------------------------------------------♡

#----------------------------------------------------♡


#------------what happens in one timestep------------♡
def step(state: Habitat_State, dt_min: int = default_dt_min):
    # dt_s = int(dt_min * 60)
    # next_time_s = state.mission_time_s + dt_s
    

   # light_level, light_heat_kw, light_heat_kwh, light_power_used_kw, light_power_used_kwh = lights(state, dt_min)
   # wellness_lights_on, wellness_light_level, w_light_heat_added_kw, w_light_heat_added_kwh, w_light_power_used_kw, w_light_power_used_kwh = wellness_lights(state, dt_min)
    o2_drop_kpa, co2_rise_kpa, crew_temp_rise_kw, crew_temp_rise_kwh = crew_metabolism(state, dt_min)

    o2_after_crew_kpa = state.o2_kpa - o2_drop_kpa
    co2_after_crew_kpa = state.co2_kpa + co2_rise_kpa

   
    oga_results = run_oga(state, o2_after_crew_kpa, dt_min)
    o2_after_oga_kpa = oga_results["o2_after_oga_kpa"]
    o2_added_kpa = oga_results["o2_added_kpa"]
    h2_produced_kg = oga_results["h2_produced_kg"]
    

    water_used_kg = oga_results["water_used_kg"]
   

    #oga_heat_kw = oga_results["oga_heat_kw"]
    #oga_heat_kwh = oga_results["oga_heat_kwh"]
    oga_power_used_kw = oga_results["oga_power_used_kw"]
    oga_energy_used_kwh = oga_results["oga_energy_used_kwh"]
   

    co2_results = run_co2_scrub(state, co2_after_crew_kpa, next_time_s, dt_min)


    co2_after_scrub_kpa = co2_results["co2_after_scrub_kpa"]
    co2_removed_kpa = co2_results["co2_removed_kpa"]
    new_co2_stored_kpa = co2_results["new_co2_stored_kpa"]
    co2_scrubber_heat_kw = co2_results["co2_scrubber_heat_kw"]
    co2_scrubber_heat_kwh = co2_results["co2_scrubber_heat_kwh"]
    co2_scrubber_power_used_kw = co2_results["co2_scrubber_power_used_kw"]
    co2_scrubber_energy_used_kwh = co2_results["co2_scrubber_energy_used_kwh"]
    

    new_water_for_oga_kg = max(0.0, state.water_for_oga_kg - water_used_kg)
    new_h2_stored_kg = state.h2_stored_kg + h2_produced_kg


    time_advanced_state = replace(state, mission_time_s=next_time_s)
    previous_sol_number = current_sol_number(state.mission_time_s)
    new_sol_number = current_sol_number(next_time_s)
    new_sol_started = new_sol_number != previous_sol_number

    new_daylight_per_m2_kw = daylight_per_m2_kw(time_advanced_state)
    current_sunlight_amount = determine_sunlight_amount(time_advanced_state)
    if new_sol_started:
        new_peak_sunlight_today = current_sunlight_amount
    else:
        new_peak_sunlight_today = max(state.peak_sunlight_today, current_sunlight_amount)
        

    pre_buffer_state = replace(
        time_advanced_state,
        mission_time_s = next_time_s,
        daylight_m2_kw = round(new_daylight_per_m2_kw, 2),
        peak_sunlight_today = round(new_peak_sunlight_today, 2),
        light_level = light_level,
        amine_beds = co2_results["amine_beds"],
        o2_kpa = round(o2_after_oga_kpa, 4),
        co2_kpa = round(co2_after_scrub_kpa, 4),
        co2_stored_kpa = round(new_co2_stored_kpa, 4),
        h2_stored_kg = round(new_h2_stored_kg, 4),
        water_for_oga_kg = round(new_water_for_oga_kg, 3),
    )

    buffer_gas_results = run_buffer_gas_control(pre_buffer_state, dt_min)

    new_state = replace(
    pre_buffer_state,
    n2_kpa = round(buffer_gas_results["n2_kpa"], 4),
    ar_kpa = round(buffer_gas_results["ar_kpa"], 4),
    n2_stored_kpa = round(buffer_gas_results["n2_stored_kpa"], 4),
    ar_stored_kpa = round(buffer_gas_results["ar_stored_kpa"], 4),
    )

    outputs = {
    "co2_removed_kpa" : co2_removed_kpa,
    "co2_scrubber_power_used_kw" : co2_scrubber_power_used_kw,
    "co2_scrubber_heat_kw" : co2_scrubber_heat_kw,
    "co2_scrubber_energy_used_kwh" : co2_scrubber_energy_used_kwh,
    "oga_heat_kw" : oga_heat_kw,
    "oga_power_used_kw" : oga_power_used_kw,
    "oga_energy_used_kwh" : oga_energy_used_kwh,
    "light_power_kw" : light_power_used_kw,
    "light_power_used_kwh" : light_power_used_kwh,
    "w_light_power_used_kw" : w_light_power_used_kw, 
    "w_light_power_used_kwh" : w_light_power_used_kwh, 
    }

    power_results = run_system_power(new_state, outputs, dt_min)
    outputs["total_power_used_kw"], outputs["total_energy_used_kwh"] = total_power_usage(outputs)
    outputs["total_solar_generated_kw"] = power_results["total_solar_generated_kw"]
    outputs["total_solar_generated_kwh"] = power_results["total_solar_generated_kwh"]
    outputs["new_battery_stored_kwh"] = power_results["new_battery_stored_kwh"]
    
    new_state = replace(
        new_state,
        battery_stored_kwh = round(power_results["new_battery_stored_kwh"], 3),
        solar_arrays = power_results["new_solar_arrays"]
    )

    return new_state, outputs
