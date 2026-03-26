from dataclasses import replace
from .state import Habitat_State

# file for co2 removal and amine bed functions

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
