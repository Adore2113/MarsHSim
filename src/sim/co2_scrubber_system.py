from dataclasses import replace
from .state import Habitat_State
from crew_metabolism import crew_metabolism

# file for co2 removal and amine bed functions

def bed_online_count(state):
    count = 0
    for bed in state.amine_beds:
        if bed["status"] == "online":
            count += 1
    
    return count


def co2_scrub_capacity_kpa(state, co2_after_crew_kpa):
    beds_online = bed_online_count(state)
    max_scrub_removal_kpa = beds_online * state.scrub_per_bed_kpa

    if co2_after_crew_kpa < 0.2:    # # efficiency drop when co2 is already low
        max_scrub_removal_kpa *= 0.40
    elif co2_after_crew_kpa < 0.4:
        max_scrub_removal_kpa *= 0.70

    if state.next_time_s % 3300 == 0 and state.next_time_s != 0:   # every 55min switch beds w. a brief co2 spike
        max_scrub_removal_kpa *= 0.80

    return max_scrub_removal_kpa, beds_online


def co2_removal_and_storage_update(state, co2_after_crew_kpa, target_co2_kpa, co2_kpa):
    excess_co2_kpa = co2_after_crew_kpa - state.target_co2_kpa

    co2_removed_kpa = min(max_scrub_removal_kpa, max(0.0, excess_co2_kpa))
    co2_after_scrub_kpa = co2_after_crew_kpa - co2_removed_kpa
    new_co2_stored_kpa = co2_removed_kpa + state.co2_stored_kpa
    
    return co2_after_scrub_kpa, co2_removed_kpa




def run_co2_scrub(co2_removed_kpa, bed_online_count, dt_min):  
    hours_per_step = dt_min / 60
    beds_online = bed_online_count(state)
    
    # heat produced, according to removal
    co2_scrubber_heat_per_kpa_kw = 1200.0
    co2_scrubber_heat_added_kw = co2_removed_kpa * co2_scrubber_heat_per_kpa_kw / 1000.0
    
    baseline_bed_heat_added_kw = beds_online * 0.4

    co2_scrubber_heat_added_kw = co2_scrubber_heat_added_kw + baseline_bed_heat_added_kw    
    co2_scrubber_heat_added_kwh = co2_scrubber_heat_added_kw * hours_per_step

    return co2_after_scrub_kpa, co2_removed_kpa, new_co2_stored_kpa, co2_scrubber_heat_added_kw, co2_scrubber_heat_added_kwh
