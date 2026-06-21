# file for handling in-situ resource utilization for Ar and N2 extraction

#--------------------constants-----------------------♡
base_compressor_power_kw = 4.0    # per active compressor
base_intake_rate_kg_per_hour = 20.0   # raw atmosphere processed per compressor
compressor_efficiency = 0.78
 
compressor_deploy_time_min = 15.0
compressor_retract_time_min = 20.0
 
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
 
        elif comp["status"] == "deploying":
            deploying_count += 1
 
        elif comp["status"] == "retracting":
            retracting_count += 1

    #-----how many compressors (c) needed online-----♡
    if state.n2_stored_kg < n2_low_storage_kg or state.ar_stored_kg < ar_low_storage_kg:
        target_comps_online = max_compressors_online

    elif state.n2_stored_kg < n2_low_storage_kg * hysteresis_kg or state.ar_stored_kg < ar_low_storage_kg * hysteresis_kg:
        target_comps_online = 2
 
    else:
        target_comps_online = 0 