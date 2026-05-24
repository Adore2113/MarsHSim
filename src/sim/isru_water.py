# file for handling in-situ resource utilization for water extraction

#--------------------constants-----------------------♡
base_heated_pipe_power_kw = 8.5    # per active pipe
base_extract_rate_kg_per_hour = 15.0    # per pipe when ice is good
pipe_retract_time_min = 45.0
pipe_deploy_time_min = 25.0
pipe_efficiency = 0.82

max_pipes_online = 6
water_to_auto_activate_kg = 1500.0
#----------------------------------------------------♡


#--------which pipes are online and how many---------♡
def pipes_in_use(state, dt_min):
    new_pipes = []
    extracting_count = 0
    deploying_count = 0
    retracting_count = 0

    for pipe in state.isru_pipes:
        if pipe["status"] == "extracting":
            extracting_count += 1
        
        elif pipe["status"] == "deploying":
            deploying_count += 1
        
        elif pipe["status"] == "retracting":
            retracting_count += 1

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

    for pipe in state.isru_pipes:
        new_pipe = pipe.copy()
        status = new_pipe.get("status", "offline")
        
        timer = new_pipe.get("timer", 0.0)
        if timer > 0:
            timer -= dt_min
            new_pipe["timer"] = max(0.0, timer)
        
        elif status == "deploying" and new_pipe["timer"] <= 0:
            new_pipe["status"] = "extracting"
            new_pipe["timer"] = max(0.0, timer)

        elif status == "offline" and (extracting_count + deploying_count) < target_pipes_online:
                new_pipe["status"] = "deploying"
                new_pipe["timer"] = pipe_deploy_time_min
                deploying_count += 1

        elif status in ("extracting", "deploying") and (extracting_count + deploying_count) > target_pipes_online:
            if new_pipe["type"] == "backup" or extracting_count > target_pipes_online:
                new_pipe["status"] = "retracting"
                new_pipe["timer"] = pipe_retract_time_min
                
                if status == "extracting":
                    extracting_count -= 1
        
        new_pipes.append(new_pipe)

    final_extracting_count = sum(1 for p in new_pipes if p["status"] == "extracting")

    return new_pipes, final_extracting_count


#--------------------isru process--------------------♡
def run_isru(state, dt_min):
    hours_per_step = dt_min / 60.0
    new_pipes, pipes_online_count = pipes_in_use(state)

    water_added_kg = 0.0
    power_used_kw = 0.0
    heat_added_kw = 0.0
    new_raw_isru_water_storage_kg = state.raw_isru_water_storage_kg + water_added_kg

    if state.isru_on and pipes_online_count > 0:
        ice_melted_kg = base_extract_rate_kg_per_hour * pipes_online_count * hours_per_step
        raw_water_added_kg = ice_melted_kg * pipe_efficiency

        storage_room_left_kg = state.raw_isru_water_storage_capacity_kg - state.raw_isru_water_storage_kg
        water_added_kg = min(raw_water_added_kg, storage_room_left_kg)
        new_raw_isru_water_storage_kg = state.raw_isru_water_storage_kg + water_added_kg
        
        power_used_kw = base_heated_pipe_power_kw * pipes_online_count
        heat_added_kw = power_used_kw * 0.85
    
    if not state.isru_on:
        pipes_online_count = 0

    #------------dict for updating state-------------♡ 
    isru_updates = {
        "isru_pipes": new_pipes,
        "raw_isru_water_storage_kg": new_raw_isru_water_storage_kg,
    }
    
    #-----------dict for printing outputs------------♡ 
    isru_outputs = {
        "isru_raw_water_added_kg": water_added_kg,
        "isru_power_used_kw": power_used_kw,
        "isru_power_used_kwh": power_used_kw * hours_per_step,

        "isru_heat_added_kw": heat_added_kw,
        "isru_heat_added_kwh": heat_added_kw * hours_per_step,
        "pipes_online_count": pipes_online_count,
    }

    return isru_updates, isru_outputs
