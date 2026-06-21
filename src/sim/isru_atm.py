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
#----------------------------------------------------♡


#----which compressors are online and how many-------♡
def compressors_in_use(state, dt_min):
    new_compressors = []
    extracting_count = 0
    deploying_count = 0
    retracting_count = 0

    for compressor in state.isru_compressors:
        if compressor["status"] == "extracting":
            extracting_count += 1
 
        elif compressor["status"] == "deploying":
            deploying_count += 1
 
        elif compressor["status"] == "retracting":
            retracting_count += 1