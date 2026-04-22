from dataclasses import replace
from .state import Habitat_State
from .oxygen_system import run_oga
from .buffer_gas_system import run_buffer_gas_control
from .co2_scrubber_system import run_co2_scrub
from .crew_metabolism import total_crew_metabolism
from .power_system import lights, wellness_lights, run_system_power
from .mars_time import get_sol_time, daylight_per_m2_kw, determine_sunlight_amount, current_sol_number, determine_low_sunlight_streak
from .temp_system import run_thermal_control, update_humidity

#--------------------constants-----------------------♡
default_dt_min = 5
#----------------------------------------------------♡


#------------what happens in one timestep------------♡
def step(state: Habitat_State, dt_min: int = default_dt_min):
    dt_s = int(dt_min * 60)
    next_time_s = state.mission_time_s + dt_s


#-----------time, solar, and daylight update---------♡    
    previous_sol_number = current_sol_number(state.mission_time_s)
    new_sol_number = current_sol_number(next_time_s)
    new_sol_started = new_sol_number != previous_sol_number

    NEW_STATE = replace(state, mission_time_s = next_time_s)

    current_sunlight_amount = determine_sunlight_amount(NEW_STATE)
    new_daylight_per_m2_kw = daylight_per_m2_kw(NEW_STATE)

    if new_sol_started:
        new_peak_sunlight_today = current_sunlight_amount
        new_low_sunlight_streak_sols = determine_low_sunlight_streak(NEW_STATE)
    else:
        new_peak_sunlight_today = max(state.peak_sunlight_today, current_sunlight_amount)
        new_low_sunlight_streak_sols = state.low_sunlight_streak_sols

    NEW_STATE = replace(NEW_STATE, daylight_m2_kw = new_daylight_per_m2_kw, peak_sunlight_today = new_peak_sunlight_today, low_sunlight_streak_sols = new_low_sunlight_streak_sols,)


#------------------crew metabolism-------------------♡
    crew_results = total_crew_metabolism(NEW_STATE, dt_min) 
    
    o2_after_crew_kpa = NEW_STATE.o2_kpa - crew_results["o2_drop_kpa"]
    co2_after_crew_kpa = NEW_STATE.co2_kpa + crew_results["co2_rise_kpa"]


#-------------------co2 scrubbing--------------------♡
    co2_results = run_co2_scrub(NEW_STATE, co2_after_crew_kpa, next_time_s, dt_min)
    
    co2_after_scrub_kpa = co2_results["co2_after_scrub_kpa"]
    co2_removed_kpa = co2_results["co2_removed_kpa"]
   
    new_co2_stored_kpa = co2_results["new_co2_stored_kpa"]


#----------------oga (o2 generation)-----------------♡
    oga_results = run_oga(NEW_STATE, o2_after_crew_kpa, dt_min)
    
    o2_after_oga_kpa = oga_results["o2_after_oga_kpa"]
    o2_added_kpa = oga_results["o2_added_kpa"]
    
    h2_produced_kg = oga_results["h2_produced_kg"]
    water_used_kg = oga_results["water_used_kg"]

    new_water_for_oga_kg = max(0.0, NEW_STATE.water_for_oga_kg - water_used_kg)
    new_h2_stored_kg = state.h2_stored_kg + h2_produced_kg

    NEW_STATE = replace(NEW_STATE, o2_kpa = o2_after_oga_kpa, co2_kpa = co2_after_scrub_kpa, co2_stored_kpa = new_co2_stored_kpa, h2_stored_kg = new_h2_stored_kg, water_for_oga = new_water_for_oga_kg, amine_beds = co2_results["amine_beds"])


#------------------lighting systems------------------♡
    light_results = lights(NEW_STATE, dt_min)
    wellness_results = wellness_lights(NEW_STATE, dt_min)


#------state/checkpoint before buffer gas system-----♡
    pre_buffer_state = replace(
        NEW_STATE,
        daylight_m2_kw = new_daylight_per_m2_kw,
        peak_sunlight_today = new_peak_sunlight_today,
        low_sunlight_streak_sols = new_low_sunlight_streak_sols,
        light_level = light_results["final_light_level"],
        amine_beds = co2_results["amine_beds"],
        o2_kpa = o2_after_oga_kpa,
        co2_kpa = co2_after_scrub_kpa,
        co2_stored_kpa = new_co2_stored_kpa,
        h2_stored_kg = new_h2_stored_kg,
        water_for_oga_kg = new_water_for_oga_kg,
        )

#----------------run buffer gas system---------------♡
    buffer_gas_results = run_buffer_gas_control(pre_buffer_state, dt_min)

#---------------state after gas update---------------♡
    new_state = replace(
        pre_buffer_state,
        n2_kpa=buffer_gas_results["n2_kpa"],
        ar_kpa=buffer_gas_results["ar_kpa"],
        n2_stored_kpa=buffer_gas_results["n2_stored_kpa"],
        ar_stored_kpa=buffer_gas_results["ar_stored_kpa"],
    )

#-------------power and subsystem outputs------------♡
    outputs = {
        "co2_scrubber_power_used_kw" : co2_results["co2_scrubber_power_used_kw"],
        "co2_scrubber_energy_used_kwh" : co2_results["co2_scrubber_energy_used_kwh"],
        
        "oga_power_used_kw" : oga_results["oga_power_used_kw"],
        "oga_energy_used_kwh" : oga_results["oga_energy_used_kwh"],

        "light_power_used_kw" : light_results["light_power_used_kw"],
        "light_power_used_kwh" : light_results["light_power_used_kwh"],
        
        "w_light_power_used_kw" : wellness_results["w_light_power_used_kw"],
        "w_light_power_used_kwh" : wellness_results["w_light_power_used_kwh"],

#---------------------heat/temp----------------------♡
        "co2_scrubber_heat_kw" : co2_results["co2_scrubber_heat_kw"],
        "co2_scrubber_heat_kwh" : co2_results["co2_scrubber_heat_kwh"],
        
        "oga_heat_kw" : oga_results["oga_heat_kw"],
        "oga_heat_kwh" : oga_results["oga_heat_kwh"],
        
        "light_heat_kw" : light_results["light_heat_kw"],
        "light_heat_kwh" : light_results["light_heat_kwh"],
        
        "w_light_heat_kw" : wellness_results["w_light_heat_kw"],
        "w_light_heat_kwh" : wellness_results["w_light_heat_kwh"],

        "crew_heat_kw" : state.crew_count * 0.1,
        "buffer_gas_heat_kw" : 0.0,

#-------------humidity/moisture control--------------♡
        "breath_vapor_added_kg" : crew_results["breath_vapor_added_kg"],
        "skin_vapor_added_kg" : crew_results["skin_vapor_added_kg"],

#--------------------gas/atmosphere------------------♡
        "co2_removed_kpa" : co2_removed_kpa,
        "o2_added_kpa": o2_added_kpa,
        "h2_produced_kg" : h2_produced_kg,
        
#-------------------water subsystem------------------♡
        "water_used_kg" : water_used_kg,
        }

#----------------run thermal control-----------------♡
    humidity_results = update_humidity(new_state, outputs, dt_min)
    outputs.update(humidity_results)
    
    thermal_results = run_thermal_control(new_state, outputs, dt_min, current_sunlight_amount)
    outputs.update(thermal_results)

#-----------------power system update----------------♡
    power_results = run_system_power(new_state, outputs, dt_min)
    outputs.update(power_results)

#-----------------final state update-----------------♡
    new_state = replace(
        new_state,
        battery_stored_kwh = power_results["new_battery_stored_kwh"],
        solar_arrays = power_results["new_solar_arrays"],
        light_level = light_results["final_light_level"],
        hab_temp_c = thermal_results["new_hab_temp_c"],
        heaters = thermal_results["new_heaters"],
        radiators = thermal_results["new_radiators"],
        current_humidity_pct = humidity_results["new_humidity_pct"]
        )

    return new_state, outputs