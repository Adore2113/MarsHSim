from dataclasses import replace
from .state import Habitat_State

# file for handling crew metabolsim

# ----crew metabolism per default timestep----
def crew_metabolism(state, dt_min):
    hours_per_step = dt_min / 60
    # ----atmosphere gases----
    o2_drop_kpa = 0.00011 * state.crew_count    # =: 0.0033
    co2_rise_kpa = 0.0000967 * state.crew_count    # = 0.0029

    # ----tempurature----
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
