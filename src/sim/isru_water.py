# file for handling in-situ resource utilization for water extraction

#--------------------constants-----------------------♡
base_heated_pipe_power_kw = 8.5    # per active pipe
base_extract_rate_kg_per_hour = 12.0    # per pipe when ice is good
pipe_efficiency = 0.78
pipe_retract_time_min = 45    # time to retract

max_pipes = 3
min_water_to_trigger_isru_kg = 800    # low water amount to auto activate
#----------------------------------------------------♡

#--------------------isru process--------------------♡
def run_isru(state, dt_min, isru_mode):
    hours_per_step = dt_min / 60.0

    water_extracted_kg = 0.0
    power_used_kw = 0.0
    heat_added_kw = 0.0
    pipes_active = 0

    if isru_mode == "auto":
        if state.potable_water_storage_kg < min_water_to_trigger_isru_kg:
            pipes_active = max_pipes

        else:
            pipes_active = 0
    
    elif isru_mode == "manual":
        pipes_active = max_pipes

    if pipes_active > 0:
        raw_water_kg = base_extract_rate_kg_per_hour * pipes_active
        water_extracted_kg = raw_water_kg * pipe_efficiency

    #----------power usage / heat per mode----------♡  
        power_used_kw = base_heated_pipe_power_kw * pipes_active
        heat_added_kw = power_used_kw * 0.85
   
    #------------dict for updating state-------------♡ 
    isru_updates = {
        "isru_water_extracted_kg": water_extracted_kg,
        "pipes_active": pipes_active,
    }
    
    #-----------dict for printing outputs------------♡ 
    isru_outputs = {
        "isru_water_extracted_kg": water_extracted_kg,
        "isru_power_used_kw": power_used_kw,
        "isru_power_used_kwh": power_used_kw * hours_per_step,
        "isru_heat_added_kw": heat_added_kw,
        "isru_heat_added_kwh": heat_added_kw * hours_per_step,
        "pipes_active": pipes_active,
        "isru_mode": isru_mode,
    }

    return isru_updates, isru_outputs
