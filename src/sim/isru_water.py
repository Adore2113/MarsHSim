# file for handling in-situ resource utilization for water extraction

#--------------------constants-----------------------♡
base_heated_pipe_power_kw = 8.5    # per active pipe
base_extract_rate_kg_per_hour = 15.0    # per pipe when ice is good
pipe_retract_time_min = 45    # time to retract
pipe_efficiency = 0.82

max_pipes_online = 6
water_to_auto_activate_kg = 1500.0
#----------------------------------------------------♡


#--------which pipes are online and how many---------♡
def pipes_in_use(state):
    new_pipes = []
    pipes_online_count = sum(1 for pipe in state.isru_pipes if pipe["status"] == "online")

    #----------how many pipes needed online----------♡ 
    if state.potable_water_storage_kg < water_to_auto_activate_kg:
        target_pipes_online = max_pipes_online
    
    elif state.potable_water_storage_kg < 2600.0:
        target_pipes_online = 4
   
    elif state.potable_water_storage_kg < 3900.0:
        target_pipes_online = 3
    
    elif state.potable_water_storage_kg < 5200.0:
        target_pipes_online = 2
    
    else:
        target_pipes_online = 0

    #---------handling primary pipes first----------♡  
    primary_pipes_needed = target_pipes_online

    for pipe in state.isru_pipes:
        new_pipe = pipe.copy()

    if pipes_online_count < target_pipes_online and new_pipe["status"] == "offline":
        if new_pipe["type"] == "primary" and primary_pipes_needed > 0:
            new_pipe["status"] = "online"
            primary_pipes_needed -= 1
            pipes_online_count += 1

        elif new_pipe["type"] == "backup":
                new_pipe["status"] = "online"
                pipes_online_count += 1
    
    elif pipes_online_count > target_pipes_online and new_pipe["status"] == "online":
        if new_pipe["type"] == "backup" or pipes_online_count > target_pipes_online:
            new_pipe["status"] = "offline"
            pipes_online_count -= 1

        new_pipes.append(new_pipe)
    
    return new_pipes, pipes_online_count


#--------------------isru process--------------------♡
def run_isru(state, dt_min):
    hours_per_step = dt_min / 60.0
    new_pipes, pipes_online_count = pipes_in_use(state)

    water_produced_kg = 0.0
    power_used_kw = 0.0
    heat_added_kw = 0.0

    if pipes_online_count > 0:
        ice_melted_kg = base_extract_rate_kg_per_hour * pipes_online_count
        water_produced_kg = ice_melted_kg * pipe_efficiency

        power_used_kw = base_heated_pipe_power_kw * pipes_online_count
        heat_added_kw = power_used_kw * 0.85


    #------------dict for updating state-------------♡ 
    isru_updates = {
        "isru_pipes": new_pipes,
        "isru_water_produced_kg": water_produced_kg,
    }
    
    #-----------dict for printing outputs------------♡ 
    isru_outputs = {
        "isru_water_produced_kg": water_produced_kg,
        "isru_power_used_kw": power_used_kw,
        "isru_power_used_kwh": power_used_kw * hours_per_step,

        "isru_heat_added_kw": heat_added_kw,
        "isru_heat_added_kwh": heat_added_kw * hours_per_step,
        "pipes_online_count": pipes_online_count,
    }

    return isru_updates, isru_outputs
