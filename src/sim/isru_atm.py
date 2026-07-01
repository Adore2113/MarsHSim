# file for handling in-situ resource utilization for Ar and N2 extraction

#--------------------constants-----------------------♡
base_compressor_power_kw = 4.0    # per active compressor
base_intake_rate_kg_per_hour = 20.0   # raw atmosphere processed per compressor
compressor_efficiency = 0.78
 
# compressor_regen_time_min = 0.0

max_compressors_online = 4
mars_co2_ratio = 0.95
mars_n2_ratio = 0.027
mars_ar_ratio = 0.016

n2_low_storage_kg = 600.0
ar_low_storage_kg = 400.0
hysteresis_kg = 1.5

max_sorbent_beds_adsorbing = 2
sorbent_regen_time_min = 60.0
sorbent_capture_efficiency = 0.85    # ratio of co2 that actually gets trapped on the absorbing bed
#----------------------------------------------------♡


#----which compressors are online and how many-------♡
def compressors_in_use(state):
    new_compressors = []
    extracting_count = 0

    for comp in state.isru_compressors:
        if comp["status"] == "extracting":
            extracting_count += 1

    #-----how many compressors (c) needed online-----♡
    if state.n2_stored_kg < n2_low_storage_kg or state.ar_stored_kg < ar_low_storage_kg:
        target_comps_online = max_compressors_online

    elif state.n2_stored_kg < n2_low_storage_kg * hysteresis_kg or state.ar_stored_kg < ar_low_storage_kg * hysteresis_kg:
        target_comps_online = 2
 
    else:
        target_comps_online = 0

    if state.power_mode == "low":
        target_comps_online = min(target_comps_online, 1)
 
    elif state.power_mode == "critical":
        target_comps_online = 0
 
    online_comp_count = 0
 
    for comp in state.isru_compressors:
        new_comp= comp.copy()
 
    
    #-------------changing compressor status----------♡
        if online_comp_count < target_comps_online:
            new_comp["status"] = "extracting"
            online_comp_count += 1
 
        else:
            new_comp["status"] = "offline"
 
        new_compressors.append(new_comp)
 
    final_extracting_count = sum(1 for comp in new_compressors if comp["status"] == "extracting")
 
    return new_compressors, final_extracting_count
#----------------------------------------------------♡


#----------------sorbent bed handling----------------♡
def run_sorbent_beds(state, dt_min, co2_intake_kg):
    new_beds = []
    beds_needed_online = 0
    co2_absorbed_kg = 0.0
    co2_released_kg = 0.0

    beds_adsorbing_count = sum(1 for bed in state.isru_atm_sorbent_beds if bed["status"] == "adsorbing")
 
    if co2_intake_kg <= 0.0:
        target_beds_adsorbing = 0
 
    else:
        target_beds_adsorbing = max_sorbent_beds_adsorbing
 
    #-------------changing bed status----------------♡
    if beds_adsorbing_count < target_beds_adsorbing:
        beds_needed_online = target_beds_adsorbing - beds_adsorbing_count
 
    for bed in state.isru_atm_sorbent_beds:
        new_bed = bed.copy()
 
        if beds_needed_online > 0 and new_bed["status"] == "standby":
            new_bed["status"] = "adsorbing"
            beds_needed_online -= 1
 
        new_beds.append(new_bed)
 
    beds_adsorbing_count = sum(1 for bed in new_beds if bed["status"] == "adsorbing")

    #--------------co2 capture / release-------------♡
    co2_per_bed_kg = co2_intake_kg / beds_adsorbing_count if beds_adsorbing_count > 0 else 0.0
    final_beds = []
 
    for bed in new_beds:
        status = bed["status"]

    #-----------------adsorbing bed CO2--------------♡
        if status == "adsorbing":
            room_left_kg = bed["capacity"] - bed["gas_load"]
            offered_kg = co2_per_bed_kg * sorbent_capture_efficiency
            absorbed_this_bed = min(offered_kg, max(0.0, room_left_kg))
 
            bed["gas_load"] += absorbed_this_bed
            co2_absorbed_kg += absorbed_this_bed
 
            if bed["gas_load"] >= bed["capacity"]:
                bed["status"] = "regenerating"
                bed["regen_timer_min"] = sorbent_regen_time_min

    #-------------------bed regen--------------------♡
        elif status == "regenerating":
            timer = bed.get("regen_timer_min", sorbent_regen_time_min)
 
            release_fraction = min(1.0, dt_min / sorbent_regen_time_min)
            released_this_step = bed["gas_load"] * release_fraction
 
            bed["gas_load"] = max(0.0, bed["gas_load"] - released_this_step)
            co2_released_kg += released_this_step
 
            timer -= dt_min
 
            if timer <= 0:
                bed["status"] = "standby"
                co2_released_kg += bed["gas_load"]    # release whatever's left
                bed["gas_load"] = 0.0
                bed["regen_timer_min"] = 0.0
            else:
                bed["regen_timer_min"] = timer
 
        final_beds.append(bed)
    
    co2_bypassed_kg = max(0.0, co2_intake_kg - co2_absorbed_kg)

    #------------dict for updating state-------------♡
    sorbent_updates = {
        "isru_atm_sorbent_beds": final_beds,
    }
 
    #-----------dict for printing outputs------------♡
    sorbent_outputs = {
        "sorbent_co2_absorbed_kg": co2_absorbed_kg,
        "sorbent_co2_released_kg": co2_released_kg,
        "sorbent_co2_bypassed_kg": co2_bypassed_kg,
         }
 
    return sorbent_updates, sorbent_outputs
#----------------------------------------------------♡


#--------------------isru process--------------------♡
def run_isru_atm(state, dt_min):
    hours_per_step = dt_min / 60.0
 
    #--------------default isru values---------------♡
    isru_atm_mode = "offline"
    n2_added_kg = 0.0
    ar_added_kg = 0.0
    co2_added_kg = 0.0
    co2_absorbed_kg = 0.0
    co2_released_kg = 0.0
    co2_bypassed_kg = 0.0
    sorbent_bed_list = state.isru_atm_sorbent_beds
    power_used_kw = 0.0
    heat_added_kw = 0.0
    sorbent_beds_adsorbing = sum(1 for bed in sorbent_bed_list if bed["status"] == "adsorbing")
    sorbent_beds_regenerating = sum(1 for bed in sorbent_bed_list if bed["status"] == "regenerating")
    sorbent_beds_standby = sum(1 for bed in sorbent_bed_list if bed["status"] == "standby")

    new_n2_stored_kg = state.n2_stored_kg
    new_ar_stored_kg = state.ar_stored_kg
    new_co2_stored_kg = state.co2_stored_kg

    new_compressors, compressors_extracting = compressors_in_use(state)

    if not state.isru_atm_on:
        isru_atm_mode = "offline"
        for comp in new_compressors:
            comp["status"] = "offline"
        compressors_extracting = 0
 
    else:
        if compressors_extracting == 0:
            isru_atm_mode = "idle"

#--------------------isru running--------------------♡
        else:
            isru_atm_mode = "running"
            active_extracting = [comp for comp in new_compressors if comp["status"] == "extracting"]

            dust_impact = sum(comp.get("dust_factor", 1.0) for comp in active_extracting) / len(active_extracting)

            current_adsorbing = sum(1 for beds in state.isru_atm_sorbent_beds if beds["status"] == "adsorbing")
            standby_beds = sum(1 for beds in state.isru_atm_sorbent_beds if beds["status"] == "standby" and beds["type"] == "primary")
            beds_available_this_step = min(max_sorbent_beds_adsorbing, current_adsorbing + standby_beds)
            effective_extracting = min(compressors_extracting, beds_available_this_step)
 
            raw_intake_kg = base_intake_rate_kg_per_hour * effective_extracting * hours_per_step
            usable_intake_kg = raw_intake_kg * compressor_efficiency * dust_impact

            #---------------extracted----------------♡
            n2_extracted_kg = usable_intake_kg * mars_n2_ratio
            ar_extracted_kg = usable_intake_kg * mars_ar_ratio
            co2_extracted_kg = usable_intake_kg * mars_co2_ratio

            #--------------bed updates---------------♡
            sorbent_updates, sorbent_outputs = run_sorbent_beds(state, dt_min, co2_extracted_kg)
            sorbent_bed_list = sorbent_updates["isru_atm_sorbent_beds"]
            sorbent_beds_adsorbing = sum(1 for bed in sorbent_bed_list if bed["status"] == "adsorbing")
            sorbent_beds_regenerating = sum(1 for bed in sorbent_bed_list if bed["status"] == "regenerating")
            sorbent_beds_standby = sum(1 for bed in sorbent_bed_list if bed["status"] == "standby")

            #------------------n2--------------------♡
            n2_room_left_kg = state.n2_storage_capacity_kg - state.n2_stored_kg
            n2_added_kg = min(n2_extracted_kg, n2_room_left_kg)
            new_n2_stored_kg = state.n2_stored_kg + n2_added_kg

            #------------------ar--------------------♡
            ar_room_left_kg = state.ar_storage_capacity_kg - state.ar_stored_kg
            ar_added_kg = min(ar_extracted_kg, ar_room_left_kg)
            new_ar_stored_kg = state.ar_stored_kg + ar_added_kg

            #------------------co2-------------------♡
            co2_released_kg = sorbent_outputs["sorbent_co2_released_kg"]
            co2_absorbed_kg = sorbent_outputs["sorbent_co2_absorbed_kg"]
            co2_bypassed_kg = sorbent_outputs["sorbent_co2_bypassed_kg"]
            co2_room_left_kg = state.co2_storage_capacity_kg - state.co2_stored_kg
            co2_added_kg = min(co2_released_kg, co2_room_left_kg)
            new_co2_stored_kg = state.co2_stored_kg + co2_added_kg

            #--------------power / heat--------------♡
            power_used_kw = base_compressor_power_kw * compressors_extracting
            heat_added_kw = power_used_kw * 0.6

#--------------dict for updating state---------------♡
    isru_atm_updates = {
        "isru_compressors": new_compressors,
        "isru_atm_sorbent_beds": sorbent_bed_list,
        "n2_stored_kg": new_n2_stored_kg,
        "ar_stored_kg": new_ar_stored_kg,
        "co2_stored_kg": new_co2_stored_kg,
    }

#--------------dict for printing outputs-------------♡
    isru_atm_outputs = {
        "isru_atm_mode": isru_atm_mode,
        "isru_atm_n2_added_kg": n2_added_kg,
        "isru_atm_ar_added_kg": ar_added_kg,
        "isru_atm_co2_added_kg": co2_added_kg,
        "isru_atm_power_used_kw": power_used_kw,
        "isru_atm_energy_used_kwh": power_used_kw * hours_per_step,
        "isru_atm_heat_added_kw": heat_added_kw,
        "isru_atm_heat_added_kwh": heat_added_kw * hours_per_step,
        "compressors_extracting": compressors_extracting,
        "sorbent_co2_absorbed_kg": co2_absorbed_kg,
        "sorbent_co2_released_kg": co2_released_kg,
        "sorbent_co2_bypassed_kg": co2_bypassed_kg,
        "sorbent_beds_adsorbing": sorbent_beds_adsorbing,
        "sorbent_beds_regenerating": sorbent_beds_regenerating,
        "sorbent_beds_standby": sorbent_beds_standby
    }
 
    return isru_atm_updates, isru_atm_outputs