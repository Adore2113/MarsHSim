from dataclasses import replace
from .state import Habitat_State
from .crew_metabolism import crew_metabolism

# file for co2 removal and amine bed functions

def bed_online_count(state):
    count = 0
    for bed in state.amine_beds:
        if bed["status"] == "online":
            count += 1
    
    return count


def co2_scrub_capacity_kpa(state, co2_after_crew_kpa, next_time_s):
    beds_online = bed_online_count(state)
    scrub_per_bed_kpa = state.scrub_per_bed_kpa
    regen_rate_kpa = 0.01    # how fast a bed is venting co2 outside during regen
    max_scrub_removal_kpa = beds_online * state.scrub_per_bed_kpa

    if co2_after_crew_kpa < 0.2:    # # efficiency drop when co2 is already low
        max_scrub_removal_kpa *= 0.40
    elif co2_after_crew_kpa < 0.4:
        max_scrub_removal_kpa *= 0.70

    if next_time_s % 3300 == 0 and next_time_s != 0:    # every 55min switch beds w. a brief co2 spike
        max_scrub_removal_kpa *= 0.80

    return max_scrub_removal_kpa, beds_online


def co2_removed_and_storage_update(state, co2_after_crew_kpa, max_scrub_removal_kpa):
    co2_above_target_kpa = co2_after_crew_kpa - state.target_co2_kpa

    co2_removed_kpa = min(max_scrub_removal_kpa, max(0.0, co2_above_target_kpa))
    co2_after_scrub_kpa = co2_after_crew_kpa - co2_removed_kpa
    new_co2_stored_kpa = co2_removed_kpa + state.co2_stored_kpa
    
    return co2_after_scrub_kpa, co2_removed_kpa, new_co2_stored_kpa


def co2_scrub_gas_power_and_heat(co2_removed_kpa, bed_online_count, next_time_s, dt_min):
    hours_per_step = dt_min / 60

    co2_scrubber_heat_added_kw = 0.0
    co2_scrubber_heat_added_kwh = 0.0
    co2_scrubber_power_used_kw = 0.0
    co2_scrubber_energy_used_kwh = 0.0

    if co2_removed_kpa > 0:
        co2_scrubber_heat_per_kpa_kw = 1200.0
        co2_scrubber_heat_added_kw = co2_removed_kpa * co2_scrubber_heat_per_kpa_kw / 1000.0
        baseline_bed_heat_kw = bed_online_count * 0.4
        
        co2_scrubber_heat_added_kw = co2_scrubber_heat_added_kw + baseline_bed_heat_kw
        co2_scrubber_heat_added_kwh = co2_scrubber_heat_added_kw * hours_per_step

        baseline_bed_power_used_kw = bed_online_count * 0.6    # placeholder amount
        co2_removal_power_per_kpa_kw = 1500.0    # placeholder amount
        co2_removal_power_used_kw = co2_removed_kpa * co2_removal_power_per_kpa_kw / 1000.0

        co2_scrubber_power_used_kw = baseline_bed_power_used_kw + co2_removal_power_used_kw
        
        if next_time_s % 3300 == 0 and next_time_s != 0:    # temporary power increase when beds switch
            co2_scrubber_power_used_kw *= 1.10

        co2_scrubber_energy_used_kwh = co2_scrubber_power_used_kw * hours_per_step
    
    return co2_scrubber_heat_added_kw, co2_scrubber_heat_added_kwh, co2_scrubber_power_used_kw, co2_scrubber_energy_used_kwh


def run_co2_scrub(state, co2_after_crew_kpa, next_time_s, dt_min):
    max_scrub_removal_kpa, beds_online = co2_scrub_capacity_kpa(state, co2_after_crew_kpa, next_time_s)
    co2_after_scrub_kpa, co2_removed_kpa, new_co2_stored_kpa = co2_removed_and_storage_update(state, co2_after_crew_kpa, max_scrub_removal_kpa)
    co2_scrubber_heat_kw, co2_scrubber_heat_kwh, co2_scrubber_power_used_kw, co2_scrubber_energy_used_kwh = co2_scrub_gas_power_and_heat(co2_removed_kpa, beds_online, next_time_s, dt_min)
    return {
        "co2_after_scrub_kpa": co2_after_scrub_kpa,
        "co2_removed_kpa": co2_removed_kpa,
        "new_co2_stored_kpa": new_co2_stored_kpa,
        "co2_scrubber_heat_kw": co2_scrubber_heat_kw,
        "co2_scrubber_heat_kwh": co2_scrubber_heat_kwh,
        "co2_scrubber_power_used_kw": co2_scrubber_power_used_kw,
        "co2_scrubber_energy_used_kwh": co2_scrubber_energy_used_kwh
    }