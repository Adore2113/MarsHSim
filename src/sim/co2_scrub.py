# file for co2 removal and amine bed functions


#--------------------constants-----------------------♡
kelvin_offset = 273.15   # add to celsius to convert to kelvin
pa_per_kpa = 1000.0   # kilopascals to pascals
r_kpa = 0.008314   # universal gas constant, 8.314 / 1000
kg_per_g = 0.001
co2_molar_mass = 0.04401    # kg per mole

min_beds_online = 2
max_beds_online = 6
bed_switch_interval_s = 3300
bed_switch_power_multiplier = 1.25

base_power_per_bed_kw = 0.65
base_heat_per_bed_kw = 0.35

power_per_kpa_removed_kw = 4.2
heat_per_kpa_removed_kw = 1.8

co2_hysteresis_for_on = 0.05
co2_hysteresis_for_off = 0.03
#----------------------------------------------------♡


#--------------co2 scrubbing efficiency--------------♡
def get_co2_scrub_efficiency(co2_kpa):
    if co2_kpa <= 0.2:
        co2_scrub_efficiency = 0.55
    
    elif co2_kpa <= 0.4:
        co2_scrub_efficiency = 0.55 + (co2_kpa - 0.2) / 0.2 * 0.30

    elif co2_kpa <= 0.5:
        co2_scrub_efficiency = 0.85 + (co2_kpa - 0.4) / 0.1 * 0.15

    else:
        co2_scrub_efficiency = 1.00

    return co2_scrub_efficiency


#-------------------co2 scrubing---------------------♡
def run_co2_scrub(state, co2_afer_crew_kpa, co2_after_greenhouse_kpa, next_time_s, dt_min):
    hours_per_step = dt_min / 60

    if co2_after_greenhouse_kpa is not None and co2_after_greenhouse_kpa >= 0:
        co2_for_scrub = co2_after_greenhouse_kpa
    
    else:
        co2_for_scrub = co2_afer_crew_kpa


    #--------------amine bed handling----------------♡ 
    new_beds = []
    beds_online_count = sum(1 for bed in state.amine_beds if bed["status"] == "online")
    
    co2_above_target_kpa = co2_for_scrub - state.target_co2_kpa

    if co2_above_target_kpa <= 0.0:
        target_beds_online = 0

    elif co2_above_target_kpa > 0.50:
        target_beds_online = max_beds_online

    elif co2_above_target_kpa > 0.25:
        target_beds_online = 5

    elif co2_above_target_kpa > 0.10:
        target_beds_online = 4

    elif co2_above_target_kpa > 0.03:
        target_beds_online = 3

    else:
        target_beds_online = min_beds_online

    #-------------changing bed status----------------♡ 
    if beds_online_count < target_beds_online and co2_above_target_kpa > co2_hysteresis_for_on:
        beds_needed_online = target_beds_online - beds_online_count
        
        for bed in state.amine_beds:
            new_bed = bed.copy()
            
            if beds_needed_online > 0 and new_bed["status"] == "standby":
                    new_bed["status"] = "online"
                    beds_needed_online -= 1
                    beds_online_count += 1

            new_beds.append(new_bed)

    #---------------switch to standby----------------♡ 
    elif beds_online_count > target_beds_online and co2_above_target_kpa < co2_hysteresis_for_off:
        beds_not_needed = beds_online_count - target_beds_online
        
        for bed in state.amine_beds:
            new_bed = bed.copy()

            if beds_not_needed > 0 and new_bed["status"] == "online":
                if new_bed["type"] == "backup" or beds_not_needed > 0:
                    new_bed["status"] = "standby"
                    beds_not_needed -= 1
                    beds_online_count -= 1

            new_beds.append(new_bed)
            
    else:
        new_beds = [bed.copy() for bed in state.amine_beds]

    return new_beds, beds_online_count


#-------------co2 removal limit per step-------------♡
def co2_scrub_capacity_kpa(state, co2_after_crew_kpa, next_time_s):
    beds_after_control, beds_online_count = amine_beds_online(state)
    regen_rate_kpa = 0.01    # how fast a bed is venting co2 outside during regen
    
    max_scrub_removal_kpa = beds_online_count * state.scrub_per_bed_kpa
    efficiency = get_co2_scrub_efficiency(co2_after_crew_kpa)

    max_scrub_removal_kpa *= efficiency
    
    if next_time_s % bed_switch_interval_s == 0 and next_time_s != 0:    # every 55min switch beds w. a brief co2 spike
        max_scrub_removal_kpa *= 0.80

    return max_scrub_removal_kpa, beds_online_count, beds_after_control


#---------caculate removal / update storage ---------♡
def co2_removed_and_storage_update(state, co2_after_crew_kpa, max_scrub_removal_kpa):
    co2_above_target_kpa = co2_after_crew_kpa - state.target_co2_kpa

    co2_removed_kpa = min(max_scrub_removal_kpa, max(0.0, co2_above_target_kpa))
    co2_after_scrub_kpa = co2_after_crew_kpa - co2_removed_kpa
    
    if co2_removed_kpa > 0.0:
        co2_removed_moles = (co2_removed_kpa * state.hab_vol_m3) / (r_kpa * (state.hab_temp_c + kelvin_offset))
        co2_removed_kg = co2_removed_moles * co2_molar_mass
    
    else:
        co2_removed_kg = 0.0
    
    new_co2_stored_kg = state.co2_stored_kg + co2_removed_kg 

    return co2_after_scrub_kpa, co2_removed_kpa, co2_removed_kg, new_co2_stored_kg


#-----system power consumption and heat produced-----♡
def co2_scrub_power_and_heat(co2_removed_kpa, beds_online_count, next_time_s, dt_min):
    hours_per_step = dt_min / 60

    co2_scrubber_heat_added_kw = 0.0
    co2_scrubber_heat_added_kwh = 0.0
    co2_scrubber_power_used_kw = 0.0
    co2_scrubber_energy_used_kwh = 0.0

    if beds_online_count > 0:
        baseline_power_kw = beds_online_count * base_power_per_bed_kw
        baseline_heat_kw = beds_online_count * base_heat_per_bed_kw

        actual_co2_removal_power_used_kw = co2_removed_kpa * power_per_kpa_removed_kw
        actual_co2_scrubber_heat_added_kw = co2_removed_kpa * heat_per_kpa_removed_kw

        co2_scrubber_power_used_kw = baseline_power_kw + actual_co2_removal_power_used_kw
        co2_scrubber_heat_added_kw = baseline_heat_kw + actual_co2_scrubber_heat_added_kw

        if next_time_s % bed_switch_interval_s == 0 and next_time_s != 0:    # temporary power increase when beds switch
            co2_scrubber_power_used_kw *= bed_switch_power_multiplier

        co2_scrubber_energy_used_kwh = co2_scrubber_power_used_kw * hours_per_step
        co2_scrubber_heat_added_kwh = co2_scrubber_heat_added_kw * hours_per_step

    return co2_scrubber_heat_added_kw, co2_scrubber_heat_added_kwh, co2_scrubber_power_used_kw, co2_scrubber_energy_used_kwh


#------------co2 removal info per timestep-----------♡
def run_co2_scrub(state, co2_after_crew_kpa, co2_after_greenhouse_kpa, next_time_s, dt_min):
    if co2_after_greenhouse_kpa is not None and co2_after_greenhouse_kpa >= 0:
        co2_for_scrub = co2_after_greenhouse_kpa
    
    else:
        co2_for_scrub = co2_after_crew_kpa

    max_scrub_removal_kpa, beds_online_count, beds_after_control = co2_scrub_capacity_kpa(state, co2_for_scrub, next_time_s)
    co2_after_scrub_kpa, co2_removed_kpa, co2_removed_kg, new_co2_stored_kg = co2_removed_and_storage_update(state, co2_for_scrub, max_scrub_removal_kpa)
    co2_scrubber_heat_kw, co2_scrubber_heat_kwh, co2_scrubber_power_used_kw, co2_scrubber_energy_used_kwh = co2_scrub_power_and_heat(co2_removed_kpa, beds_online_count, next_time_s, dt_min)

    #------------dict for updating state-------------♡ 
    co2_scrubber_updates = {
        "co2_kpa": co2_after_scrub_kpa,
        "co2_stored_kg": new_co2_stored_kg,
        "amine_beds": beds_after_control,
    }
    
    #-----------dict for printing outputs------------♡ 
    co2_scrubber_outputs = {
        "co2_removed_kpa": co2_removed_kpa,
        "co2_removed_kg": co2_removed_kg,
        "co2_scrubber_heat_kw": co2_scrubber_heat_kw,
        "co2_scrubber_heat_kwh": co2_scrubber_heat_kwh,
        "co2_scrubber_power_used_kw": co2_scrubber_power_used_kw,
        "co2_scrubber_energy_used_kwh": co2_scrubber_energy_used_kwh,
        "beds_online_count": beds_online_count,
        "co2_for_scrub_kpa": co2_for_scrub
    }

    return co2_scrubber_updates, co2_scrubber_outputs