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

    if state.power_mode == "low":
        target_pipes_online = min(target_pipes_online, 2)

    elif state.power_mode == "critical":
        target_pipes_online = 0

    for pipe in state.isru_pipes:
        new_pipe = pipe.copy()
        status = new_pipe.get("status", "offline")
        
        timer = new_pipe.get("timer", 0.0)
        if timer > 0:
            timer -= dt_min
            new_pipe["timer"] = max(0.0, timer)

    #--------------changing pipe status--------------♡ 
        if status == "deploying" and new_pipe["timer"] <= 0:
            new_pipe["status"] = "extracting"
            new_pipe["timer"] = 0.0

        elif status == "retracting" and new_pipe["timer"] <= 0:
            new_pipe["status"] = "offline"
            new_pipe["timer"] = 0.0

        elif status in ("offline", "retracting") and (extracting_count + deploying_count) < target_pipes_online:
                if new_pipe["type"] == "primary" or (new_pipe["type"] == "backup" and extracting_count == 0):
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
def run_isru_water(state, dt_min):
    hours_per_step = dt_min / 60.0

    #--------------default isru values--------------♡
    isru_water_mode = "offline"
    water_added_kg = 0.0
    power_used_kw = 0.0
    heat_added_kw = 0.0

    new_raw_isru_water_storage_kg = state.raw_isru_water_storage_kg + water_added_kg
    new_pipes, pipes_extracting = pipes_in_use(state, dt_min)

    pipes_deploying = sum(1 for p in new_pipes if p["status"] == "deploying")
    pipes_retracting = sum(1 for p in new_pipes if p["status"] == "retracting")

    if not state.isru_water_on:
        isru_water_mode = "offline"
        for pipe in new_pipes:
            if pipe["status"] in ("deploying", "extracting"):
                pipe["status"] = "retracting"
                pipe["timer"] = pipe_retract_time_min

    else:
        if pipes_extracting == 0 and pipes_deploying == 0:
            isru_water_mode = "idle"

    #------------------isru running-----------------♡  
        else:
            isru_water_mode = "running"
        
        if pipes_extracting > 0:
            active_extracting = [pipe for pipe in new_pipes if pipe["status"] == "extracting"]
            dust_impact = sum(pipe.get("dust_factor", 1.0) for pipe in active_extracting) / len(active_extracting)

            ice_melted_kg = base_extract_rate_kg_per_hour * pipes_extracting * hours_per_step
            raw_water_added_kg = ice_melted_kg * pipe_efficiency * dust_impact
            
            storage_room_left_kg = state.raw_isru_water_storage_capacity_kg - state.raw_isru_water_storage_kg
            water_added_kg = min(raw_water_added_kg, storage_room_left_kg)
            new_raw_isru_water_storage_kg = state.raw_isru_water_storage_kg + water_added_kg
            
            active_pipes = pipes_extracting + pipes_deploying
            power_used_kw = base_heated_pipe_power_kw * active_pipes
            heat_added_kw = power_used_kw * 0.85

    #------------dict for updating state-------------♡ 
    isru_water_updates = {
        "isru_pipes": new_pipes,
        "raw_isru_water_storage_kg": new_raw_isru_water_storage_kg,
    }
    
    #-----------dict for printing outputs------------♡ 
    isru_water_outputs = {
        "isru_water_mode": isru_water_mode,
        "isru_raw_water_added_kg": water_added_kg,
        "isru_water_power_used_kw": power_used_kw,
        "isru_water_energy_used_kwh": power_used_kw * hours_per_step,
        "isru_water_heat_added_kw": heat_added_kw,
        "isru_water_heat_added_kwh": heat_added_kw * hours_per_step,
        "pipes_extracting": pipes_extracting,
        "pipes_deploying": pipes_deploying,
        "pipes_retracting": pipes_retracting,
        "total_pipes_active": pipes_extracting + pipes_deploying,
    }

    return isru_water_updates, isru_water_outputs
