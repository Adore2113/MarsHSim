#--------------------imports-------------------------♡
from dataclasses import replace
from .state import Habitat_State
from .oxygen_system import run_oga
from .buffer_gas_system import run_buffer_gas_control
from .co2_scrubber_system import run_co2_scrub
from .crew_metabolism import total_crew_metabolism
from .power_system import lights, wellness_lights, run_system_power
from .mars_time import daylight_per_m2_kw, determine_sunlight_amount, current_sol_number, determine_low_sunlight_streak
from .temp_system import run_thermal_control, update_humidity
from .water_system import run_water_system
from .dust_system import get_dust_accumulation
from .sabatier_system import run_conversions, run_sabatier
#----------------------------------------------------♡


#--------------------constants-----------------------♡
default_dt_min = 5
#----------------------------------------------------♡


#------------what happens in one timestep------------♡
def step(state: Habitat_State, dt_min: int = default_dt_min):
    dt_s = int(dt_min * 60)
    next_time_s = state.mission_time_s + dt_s
        
        #--time, solar, and daylight update---♡
    previous_sol_number = current_sol_number(state.mission_time_s)
    new_sol_number = current_sol_number(next_time_s)
    new_sol_started = new_sol_number != previous_sol_number

    new_state = replace(state, mission_time_s = next_time_s)

    current_sunlight_amount = determine_sunlight_amount(new_state)
    new_daylight_per_m2_kw = daylight_per_m2_kw(new_state)

    if new_sol_started:
        new_peak_sunlight_today = current_sunlight_amount
        new_low_sunlight_streak_sols = determine_low_sunlight_streak(new_state)
    
    else:
        new_peak_sunlight_today = max(state.peak_sunlight_today, current_sunlight_amount)
        new_low_sunlight_streak_sols = state.low_sunlight_streak_sols

    new_state = replace(
        new_state, 
        daylight_m2_kw = new_daylight_per_m2_kw, 
        peak_sunlight_today = new_peak_sunlight_today, 
        low_sunlight_streak_sols = new_low_sunlight_streak_sols
        )
    
        #----------------crew-----------------♡
    crew_results = total_crew_metabolism(new_state, dt_min) 

        #-------------atmosphere--------------♡
        #----------------mca------------------♡
    o2_after_crew_kpa = new_state.o2_kpa - crew_results["o2_drop_kpa"]
    co2_after_crew_kpa = new_state.co2_kpa + crew_results["co2_rise_kpa"]

    co2_results = run_co2_scrub(new_state, co2_after_crew_kpa, next_time_s, dt_min)
    oga_results = run_oga(new_state, o2_after_crew_kpa, dt_min)

        #-------------buffer gas--------------♡
    buffer_gas_results = run_buffer_gas_control(new_state, dt_min)

        #--------------sabatier---------------♡
    co2_kg, temp_k = run_conversions(state)
    sabatier_updates, sabatier_outputs = run_sabatier(state, dt_min, co2_kg, temp_k)
    # state_after_sabatier = replace(new_state, **sabatier_updates)

        #--------------humidity---------------♡
    humidity_results = update_humidity(
        new_state,
        crew_results["breath_vapor_added_kg"],
        crew_results["skin_vapor_added_kg"],
        dt_min
    )

        #----------------water----------------♡
    water_updates, water_outputs = run_water_system(
        new_state,
        crew_results,
        humidity_results["vapor_removed_kg"],
        oga_results["water_used_kg"],
        dt_min
    )
        
        #---------------lights----------------♡
    light_results = lights(new_state, dt_min)
    wellness_results = wellness_lights(new_state, dt_min)
 
        #--------------thermal----------------♡
    thermal_updates, thermal_outputs = run_thermal_control(
        new_state,
        crew_results["crew_temp_rise_kw"],
        oga_results["oga_heat_kw"],
        co2_results["co2_scrubber_heat_kw"],
        light_results["light_heat_kw"],
        wellness_results["w_light_heat_kw"],
        humidity_results["chx_heat_added_kw"],
        dt_min,
        current_sunlight_amount
    )
       
        #----------------dust-----------------♡
    dust_results = get_dust_accumulation(new_state, dt_min)

        #----------------power----------------♡
    power_updates, power_outputs = run_system_power(
        new_state,
        co2_results,
        oga_results,
        light_results,
        wellness_results,
        thermal_outputs,
        humidity_results,
        dt_min
    )

#-----------------final state update-----------------♡
    updates = {
        **water_updates,
        **thermal_updates,
        **power_updates,
        **sabatier_updates,

        "o2_kpa": oga_results["o2_after_oga_kpa"],
        "co2_kpa": co2_results["co2_after_scrub_kpa"],
        "co2_stored_kpa": co2_results["new_co2_stored_kpa"],
        "n2_kpa": buffer_gas_results["n2_kpa"],
        "ar_kpa": buffer_gas_results["ar_kpa"],
        "n2_stored_kpa": buffer_gas_results["n2_stored_kpa"],
        "ar_stored_kpa": buffer_gas_results["ar_stored_kpa"],
        "h2_stored_kg": new_state.h2_stored_kg + oga_results["h2_produced_kg"],
        
        "solar_arrays": dust_results["new_solar_arrays"],
        "radiators": dust_results["new_radiators"],
        "amine_beds": co2_results["amine_beds"],
        "light_level": light_results["final_light_level"],
        "wellness_lights_on": wellness_results["wellness_lights_on"],
        "current_humidity_pct": humidity_results["new_humidity_pct"],
    }

    new_state = replace(new_state, **updates)

#--------------------outputs dict--------------------♡
    outputs = {
        #----------------crew-----------------♡
        "crew_heat_kw": crew_results["crew_temp_rise_kw"],

        #-------------atmosphere--------------♡
        #--------------co2 / OGA--------------♡
        "co2_scrubber_power_used_kw": co2_results["co2_scrubber_power_used_kw"],
        "co2_scrubber_energy_used_kwh": co2_results["co2_scrubber_energy_used_kwh"],
        "co2_scrubber_heat_kw": co2_results["co2_scrubber_heat_kw"],
        "co2_scrubber_heat_kwh": co2_results["co2_scrubber_heat_kwh"],
        "co2_removed_kpa": co2_results["co2_removed_kpa"],
        "beds_online_count": co2_results["beds_online_count"],

        "oga_power_used_kw": oga_results["oga_power_used_kw"],
        "oga_energy_used_kwh": oga_results["oga_energy_used_kwh"],
        "oga_heat_kw": oga_results["oga_heat_kw"],
        "oga_heat_kwh": oga_results["oga_heat_kwh"],
        "o2_added_kpa": oga_results["o2_added_kpa"],
        "h2_produced_kg": oga_results["h2_produced_kg"],
        "oga_water_used_kg": oga_results["water_used_kg"],

        #-------------buffer gas--------------♡
        "buffer_gas_heat_kw": 0.0,
        "buffer_gas_vented_kpa": buffer_gas_results["total_buffer_gas_vented_kpa"],
        "total_buffer_gas_added_kpa": buffer_gas_results["total_buffer_gas_added_kpa"],
        "buffer_gas_mode": buffer_gas_results["buffer_gas_mode"],
        "pressure_gap_kpa": buffer_gas_results["pressure_gap_kpa"],

        #---------------lights----------------♡
        "light_power_used_kw": light_results["light_power_used_kw"],
        "light_energy_used_kwh": light_results["light_energy_used_kwh"],
        "light_heat_kw": light_results["light_heat_kw"],
        "light_heat_kwh": light_results["light_heat_kwh"],

        "w_light_power_used_kw": wellness_results["w_light_power_used_kw"],
        "w_light_energy_used_kwh": wellness_results["w_light_energy_used_kwh"],
        "w_light_heat_kw": wellness_results["w_light_heat_kw"],
        "w_light_heat_kwh": wellness_results["w_light_heat_kwh"],
        
        #--------------humidity---------------♡
        "breath_vapor_added_kg": crew_results["breath_vapor_added_kg"],
        "skin_vapor_added_kg": crew_results["skin_vapor_added_kg"]
    }

    #-----------------humidity (CHX)-----------------♡
    outputs.update(humidity_results)

    #---------------------water----------------------♡
    outputs.update(water_outputs)
    
    #--------------------thermal---------------------♡
    outputs.update(thermal_outputs)

    #---------------------power----------------------♡
    outputs.update(power_outputs)

    #-------------------sabatier---------------------♡
    outputs.update(sabatier_outputs)

    return new_state, outputs