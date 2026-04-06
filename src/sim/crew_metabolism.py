from dataclasses import replace
from .state import Habitat_State

# ----crew activites and metabolism rates-----------♡
crew_activity_states = {
    "normal" : {"o2_drop_multiplier" : 1.0, "co2_rise_multiplier" : 1.0},
    "sleep" : {"o2_drop_multiplier" : 0.8, "co2_rise_multiplier" : 0.8},
    "exercise" : {"o2_drop_multiplier" : 1.5, "co2_rise_multiplier" : 1.5},  
    "intense" : {"o2_drop_multiplier" : 2.0, "co2_rise_multiplier" : 2.0},
}
 
# ----crew metabolism per default timestep----------♡
def crew_metabolism(state, dt_min):
    hours_per_step = dt_min / 60
    
    # ----atmosphere gases----♡
    crew_activity = crew_activity_states[state.crew_activity]
    o2_drop_x = crew_activity["o2_drop_multiplier"]
    co2_rise_x = crew_activity["co2_rise_multiplier"]
    
    o2_drop_kpa = 0.00011 * state.crew_count * o2_drop_x
    co2_rise_kpa = 0.0000967 * state.crew_count * co2_rise_x

    # ----tempurature rise----♡
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
