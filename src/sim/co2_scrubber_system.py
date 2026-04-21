from dataclasses import replace
from .state import Habitat_State

# file for co2 removal and amine bed functions
#--------------------constants-----------------------♡
scrub_per_bed_kpa = 0.012
min_beds_online = 2

base_power_per_bed_kw = 0.65
power_per_kpa_removed_kw = 45.0

base_heat_per_bed_kpa = 0.35
heat_per_kpa_removed_kw = 8.0

bed_switch_interval_s = 3300
bed_switch_power_multiplier = 1.25

co2_efficiency_change_levels = {
    0.0 : 0.55,
    0.2 : 0.55,
    0.4 : 0.85,
    0.5 : 1.00
}
#----------------------------------------------------♡


#---------which beds and how many are online---------♡
def amine_bed_control_and_count(amine_beds):
    new_beds = []
    beds_online_count = sum(1 for bed in amine_beds if bed["status"] == "online")

    for bed in amine_beds:
        new_bed = bed.copy()

        if beds_online_count < min_beds_online and new_bed["status"] == "standby":
            new_bed["status"] = "online"
            beds_online_count += 1

        new_beds.append(new_bed)

    return new_beds, beds_online_count


#--------------co2 scrubbing efficiency--------------♡
def get_co2_scrub_efficiency(co2_kpa):
    if co2_kpa <= 0.2:
        co2_scrub_efficiency = co2_efficiency_change_levels[0.0]

    elif co2_kpa <= 0.4:
        co2_scrub_efficiency = co2_efficiency_change_levels[0.2] + (co2_kpa - 0.2) / 0.2 * (co2_efficiency_change_levels[0.4] - co2_efficiency_change_levels[0.2])

    elif co2_kpa <= 0.5:
        co2_scrub_efficiency = co2_efficiency_change_levels[0.4] + (co2_kpa - 0.4) / 0.1 * (co2_efficiency_change_levels[0.5] - co2_efficiency_change_levels[0.4])

    else:
        co2_scrub_efficiency = co2_efficiency_change_levels[0.5]

    return co2_scrub_efficiency


#-------------co2 removal limit per step-------------♡
def co2_scrub_capacity_kpa(state, co2_after_crew_kpa, next_time_s):
    beds_after_control, beds_online_count = amine_bed_control_and_count(state.amine_beds)
    regen_rate_kpa = 0.01    # how fast a bed is venting co2 outside during regen
    
    max_scrub_removal_kpa = beds_online_count * state.scrub_per_bed_kpa
    efficiency = get_co2_scrub_efficiency(co2_after_crew_kpa)

    max_scrub_removal_kpa *= efficiency
    
    if next_time_s % 3300 == 0 and next_time_s != 0:    # every 55min switch beds w. a brief co2 spike
        max_scrub_removal_kpa *= 0.80

    return max_scrub_removal_kpa, beds_online_count, beds_after_control


#---------caculate removal / update storage ---------♡
def co2_removed_and_storage_update(state, co2_after_crew_kpa, max_scrub_removal_kpa):
    co2_above_target_kpa = co2_after_crew_kpa - state.target_co2_kpa

    co2_removed_kpa = min(max_scrub_removal_kpa, max(0.0, co2_above_target_kpa))
    co2_after_scrub_kpa = co2_after_crew_kpa - co2_removed_kpa
    
    new_co2_stored_kpa = co2_removed_kpa + state.co2_stored_kpa

    return co2_after_scrub_kpa, co2_removed_kpa, new_co2_stored_kpa


#-----system power consumption and heat produced-----♡
def co2_scrub_power_and_heat(co2_removed_kpa, beds_online_count, next_time_s, dt_min):
    hours_per_step = dt_min / 60
    
    base_power_per_bed_kw = 0.65
    power_per_kpa_removed_kw = 45.0

    base_heat_per_bed_kpa = 0.35
    heat_per_kpa_removed_kw = 8.0

    co2_scrubber_heat_added_kw = 0.0
    co2_scrubber_heat_added_kwh = 0.0
    co2_scrubber_power_used_kw = 0.0
    co2_scrubber_energy_used_kwh = 0.0

    if co2_removed_kpa > 0:
        baseline_power_kw = beds_online_count * base_power_per_bed_kw
        baseline_heat_kw = beds_online_count * base_heat_per_bed_kpa

        actual_co2_removal_power_used_kw = co2_removed_kpa * power_per_kpa_removed_kw
        actual_co2_scrubber_heat_added_kw = co2_removed_kpa * heat_per_kpa_removed_kw

        co2_scrubber_power_used_kw = baseline_power_kw + power_per_kpa_removed_kw
        co2_scrubber_heat_added_kw = baseline_heat_kw + base_heat_per_bed_kpa

        if next_time_s % bed_switch_interval_s == 0 and next_time_s != 0:    # temporary power increase when beds switch
            co2_scrubber_power_used_kw *= bed_switch_power_multiplier

        co2_scrubber_energy_used_kwh = co2_scrubber_power_used_kw * hours_per_step
        co2_scrubber_heat_added_kwh = co2_scrubber_heat_added_kw * hours_per_step

    return co2_scrubber_heat_added_kw, co2_scrubber_heat_added_kwh, co2_scrubber_power_used_kw, co2_scrubber_energy_used_kwh


#------------co2 removal info per timestep-----------♡
def run_co2_scrub(state, co2_after_crew_kpa, next_time_s, dt_min):
    max_scrub_removal_kpa, beds_online_count, beds_after_control = co2_scrub_capacity_kpa(state, co2_after_crew_kpa, next_time_s)
    co2_after_scrub_kpa, co2_removed_kpa, new_co2_stored_kpa = co2_removed_and_storage_update(state, co2_after_crew_kpa, max_scrub_removal_kpa)
    co2_scrubber_heat_kw, co2_scrubber_heat_kwh, co2_scrubber_power_used_kw, co2_scrubber_energy_used_kwh = co2_scrub_power_and_heat(co2_removed_kpa, beds_online_count, next_time_s, dt_min)

    return {
        "co2_after_scrub_kpa": co2_after_scrub_kpa,
        "co2_removed_kpa": co2_removed_kpa,
        "new_co2_stored_kpa": new_co2_stored_kpa,
        "co2_scrubber_heat_kw": co2_scrubber_heat_kw,
        "co2_scrubber_heat_kwh": co2_scrubber_heat_kwh,
        "co2_scrubber_power_used_kw": co2_scrubber_power_used_kw,
        "co2_scrubber_energy_used_kwh": co2_scrubber_energy_used_kwh,
        "amine_beds": beds_after_control
    }