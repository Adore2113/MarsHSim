# file for handling in-situ resource utilization for Ar and N2 extraction

#--------------------constants-----------------------♡
base_compressor_power_kw = 4.0    # per active compressor
base_intake_rate_kg_per_hour = 20.0   # raw atmosphere processed per compressor
compressor_efficiency = 0.78
 
# compressor_regen_time_min = 0.0

max_compressors_online = 4
mars_atm_co2_ratio = 0.95
mars_atm_n2_ratio = 0.027
mars_atm_ar_ratio = 0.016

n2_low_storage_kg = 600.0
ar_low_storage_kg = 300.0
hysteresis_kg = 1.5    # placeholder
#----------------------------------------------------♡


#----which compressors are online and how many-------♡
def compressors_in_use(state, dt_min):
    new_compressors = []
    extracting_count = 0
    deploying_count = 0
    retracting_count = 0

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
            online_count += 1
 
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
