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
ar_low_storage_kg = 300.0
hysteresis_kg = 1.5    # placeholder

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
        


#--------------------isru process--------------------♡
def run_isru_atm(state, dt_min):
    hours_per_step = dt_min / 60.0
 
    #--------------default isru values--------------♡
    isru_atm_mode = "offline"
    n2_added_kg = 0.0
    ar_added_kg = 0.0
    co2_added_kg = 0.0
    power_used_kw = 0.0
    heat_added_kw = 0.0

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

#------------------isru running-----------------♡
        else:
            isru_atm_mode = "running"
            active_extracting = [comp for comp in new_compressors if comp["status"] == "extracting"]

            raw_intake_kg = base_intake_rate_kg_per_hour * compressors_extracting * hours_per_step
            usable_intake_kg = raw_intake_kg * compressor_efficiency 

            n2_extracted_kg = usable_intake_kg * mars_n2_ratio
            ar_extracted_kg = usable_intake_kg * mars_ar_ratio
            co2_extracted_kg = usable_intake_kg * mars_co2_ratio
 
            n2_room_left_kg = state.n2_storage_capacity_kg - state.n2_stored_kg
            ar_room_left_kg = state.ar_storage_capacity_kg - state.ar_stored_kg
            co2_room_left_kg = state.co2_storage_capacity_kg - state.co2_stored_kg

            n2_added_kg = min(n2_extracted_kg, n2_room_left_kg)
            ar_added_kg = min(ar_extracted_kg, ar_room_left_kg)
            co2_added_kg = min(co2_extracted_kg, co2_room_left_kg)
 
            new_n2_stored_kg = state.n2_stored_kg + n2_added_kg
            new_ar_stored_kg = state.ar_stored_kg + ar_added_kg
            new_co2_stored_kg = state.co2_stored_kg + co2_added_kg

            power_used_kw = base_compressor_power_kw * compressors_extracting
            heat_added_kw = power_used_kw * 0.6

#------------dict for updating state-------------♡
    isru_atm_updates = {
        "isru_compressors": new_compressors,
        "n2_stored_kg": new_n2_stored_kg,
        "ar_stored_kg": new_ar_stored_kg,
        "co2_stored_kg": new_co2_stored_kg,
    }

#-----------dict for printing outputs------------♡
    isru_atm_outputs = {
        "isru_atm_mode": isru_atm_mode,
        "isru_n2_added_kg": n2_added_kg,
        "isru_ar_added_kg": ar_added_kg,
        "isru_co2_added_kg": co2_added_kg,
        "isru_atm_power_used_kw": power_used_kw,
        "isru_atm_power_used_kwh": power_used_kw * hours_per_step,
        "isru_atm_heat_added_kw": heat_added_kw,
        "isru_atm_heat_added_kwh": heat_added_kw * hours_per_step,
        "compressors_extracting": compressors_extracting,
    }
 
    return isru_atm_updates, isru_atm_outputs