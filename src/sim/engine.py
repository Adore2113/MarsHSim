#--------------------imports-------------------------♡
from dataclasses import replace
from .state import Habitat_State
from .oxygen import run_oga
from .buffer_gas import run_buffer_gas_control
from .co2_scrub import run_co2_scrub
from .crew import total_crew_metabolism
from .power import light_system, run_system_power
from .mars_time import get_daylight_per_m2_kw, get_sunlight_amount, current_sol_number, get_low_sunlight_streak, get_ls_deg, current_mars_season
from .temp import run_thermal_control, update_humidity
from .water import run_water_system
from .dust import get_dust_accumulation
from .sabatier import run_sabatier
from .greenhouse import run_greenhouse
from .isru_water import run_isru_water
from .isru_atm import run_isru_atm
#----------------------------------------------------♡


#--------------------constants-----------------------♡
default_dt_min = 5
#----------------------------------------------------♡


#------------what happens in one timestep------------♡
def step(state: Habitat_State, dt_min: int = default_dt_min):
    dt_s = int(dt_min * 60)
    next_time_s = state.mission_time_s + dt_s

    #-------time / solar / daylight-------♡
    previous_sol_number = current_sol_number(state.mission_time_s)
    new_sol_number = current_sol_number(next_time_s)
    new_sol_started = new_sol_number != previous_sol_number

    new_state = replace(state, mission_time_s = next_time_s)

    current_sunlight_amount = get_sunlight_amount(new_state)
    new_daylight_per_m2_kw = get_daylight_per_m2_kw(new_state)

    if new_sol_started:
        new_peak_sunlight_today = current_sunlight_amount
        new_low_sunlight_streak_sols = get_low_sunlight_streak(new_state)
    
    else:
        new_peak_sunlight_today = max(state.peak_sunlight_today, current_sunlight_amount)
        new_low_sunlight_streak_sols = state.low_sunlight_streak_sols

    new_ls_deg = get_ls_deg(new_state.mission_time_s)
    new_season = current_mars_season(new_state)

    new_state = replace(
    new_state, 
    daylight_m2_kw = new_daylight_per_m2_kw, 
    peak_sunlight_today = new_peak_sunlight_today, 
    low_sunlight_streak_sols = new_low_sunlight_streak_sols,
    ls_deg = new_ls_deg,
    current_season = new_season
    )
    
    #----------------crew-----------------♡
    crew_results = total_crew_metabolism(new_state, dt_min) 

    #-------------greenhouse--------------♡
    greenhouse_updates, greenhouse_outputs = run_greenhouse(new_state, dt_min)
    new_state = replace(new_state, **greenhouse_updates)

    #--------------sabatier---------------♡
    sabatier_updates, sabatier_outputs = run_sabatier(new_state, dt_min)
    new_state = replace(new_state, **sabatier_updates)

    #-----------isru atmosphere-----------♡
    isru_atm_updates, isru_atm_outputs = run_isru_atm(new_state, dt_min)
    new_state = replace(new_state, **isru_atm_updates)

    #-------------atmosphere--------------♡
    o2_after_crew_kpa = new_state.o2_kpa - crew_results["o2_drop_kpa"]
    co2_after_crew_kpa = new_state.co2_kpa + crew_results["co2_rise_kpa"]

    min_greenhouse_co2_kpa = state.target_co2_kpa - 0.05

    o2_after_greenhouse_kpa = min(state.max_safe_o2_kpa, o2_after_crew_kpa + greenhouse_outputs.get("greenhouse_o2_produced_kpa", 0.0))
    co2_after_greenhouse_kpa = max( min_greenhouse_co2_kpa, co2_after_crew_kpa - greenhouse_outputs.get("greenhouse_co2_consumed_kpa", 0.0))

    co2_scrubber_updates, co2_scrubber_outputs = run_co2_scrub(new_state, co2_after_crew_kpa, co2_after_greenhouse_kpa, next_time_s, dt_min)
    oga_updates, oga_outputs = run_oga(new_state, o2_after_greenhouse_kpa, dt_min)

    #-------------buffer gas--------------♡
    buffer_gas_updates, buffer_gas_outputs = run_buffer_gas_control(new_state, dt_min)
 
    #--------------humidity---------------♡
    humidity_results = update_humidity(new_state, crew_results["breath_vapor_added_kg"], crew_results["skin_vapor_added_kg"], greenhouse_outputs.get("greenhouse_transpiration_kg", 0.0), dt_min)
    
    #-------------isru water--------------♡
    isru_water_updates, isru_water_outputs = run_isru_water(new_state, dt_min)
    new_state = replace(new_state, **isru_water_updates)

    #----------------water----------------♡
    water_updates, water_outputs = run_water_system(
        new_state,
        crew_results,
        humidity_results["vapor_removed_kg"],
        oga_outputs["oga_water_used_kg"],
        greenhouse_outputs.get("greenhouse_water_consumed_kg", 0.0),
        greenhouse_outputs.get("greenhouse_transpiration_kg", 0.0),
        sabatier_outputs.get("sabatier_water_produced_kg", 0.0),
        greenhouse_outputs.get("greenhouse_runoff_water_kg", 0.0),
        dt_min
    )

    #---------------lights----------------♡
    light_results = light_system(new_state, dt_min, new_state.power_mode)

    #--------------thermal----------------♡
    thermal_updates, thermal_outputs = run_thermal_control(
        new_state,
        crew_results["crew_temp_rise_kw"],
        oga_outputs["oga_heat_kw"],
        co2_scrubber_outputs["amine_bed_heat_added_kw"],
        light_results["light_heat_kw"],
        light_results["w_light_heat_kw"],
        greenhouse_outputs.get("greenhouse_heat_kw", 0.0),
        greenhouse_outputs.get("greenhouse_led_heat_kw", 0.0),
        humidity_results["chx_heat_added_kw"],
        isru_water_outputs["isru_water_heat_added_kw"],
        isru_atm_outputs["isru_atm_heat_added_kw"],
        dt_min,
        current_sunlight_amount
    )
       
    #----------------dust-----------------♡
    dust_results = get_dust_accumulation(new_state, dt_min)

    #----------------power----------------♡
    power_updates, power_outputs = run_system_power(
        new_state,
        co2_scrubber_outputs,
        oga_outputs,
        light_results,
        thermal_outputs,
        humidity_results,
        greenhouse_outputs,
        water_outputs,
        sabatier_outputs,
        isru_water_outputs,
        isru_atm_outputs,
        dt_min
    )

#-----------------final state update-----------------♡
    updates = {
        **water_updates,
        **thermal_updates,
        **power_updates,
        **sabatier_updates,
        **isru_atm_updates,
        **oga_updates,
        **co2_scrubber_updates,
        **buffer_gas_updates,
        **greenhouse_updates,
        **isru_water_updates,

        "solar_arrays": dust_results["new_solar_arrays"],
        "radiators": dust_results["new_radiators"],
        "isru_compressors": dust_results["new_compressors"],
        "light_level": light_results["adjusted_light_level"],
        "wellness_lights_on": light_results["wellness_lights_on"],
        "current_humidity_pct": humidity_results["new_humidity_pct"],
    }

    new_state = replace(new_state, **updates)

#--------------------outputs dict--------------------♡
    outputs = {
        "crew_heat_kw": crew_results["crew_temp_rise_kw"],
        "breath_vapor_added_kg": crew_results["breath_vapor_added_kg"],
        "skin_vapor_added_kg": crew_results["skin_vapor_added_kg"],
    }
    
    outputs.update(oga_outputs)
    outputs.update(co2_scrubber_outputs)
    outputs.update(buffer_gas_outputs)
    outputs.update(humidity_results)
    outputs.update(isru_water_outputs)
    outputs.update(isru_atm_outputs)
    outputs.update(water_outputs)
    outputs.update(greenhouse_outputs)
    outputs.update(thermal_outputs)
    outputs.update(power_outputs)
    outputs.update(sabatier_outputs)

    return new_state, outputs