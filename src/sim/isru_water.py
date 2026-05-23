# file for handling in-situ resource utilization for water extraction

#--------------------constants-----------------------♡
base_heated_pipe_power_kw = 8.5    # per active pipe
base_extract_rate_kg_per_hour = 15.0    # per pipe when ice is good
pipe_retract_time_min = 45    # time to retract
pipe_efficiency = 0.78

max_pipes_online = 6
#----------------------------------------------------♡



#--------which pipes are online and how many---------♡
def pipes_in_use(state):
    new_pipes = []
    pipes_online_count = sum(1 for pipe in state.isru_pipes if pipe["status"] == "online" )

    water_needed_kg = state.potable_water_storage_kg - state.potable_water_storage_capacity_kg

    #----------how many pipes needed online----------♡ 
    if water_needed_kg > 6490.0:
        target_pipes_online = max_pipes_online

    elif water_needed_kg > 5200.0:
        target_pipes_online = 5

    elif water_needed_kg > 3900.0:
        target_pipes_online = 4

    elif water_needed_kg > 2600.0:
        target_pipes_online = 3

    elif water_needed_kg > 1300.0:
        target_pipes_online = 2

    else:
        target_pipes_online = 0


#--------------------isru process--------------------♡
def run_isru(state, dt_min):
    hours_per_step = dt_min / 60.0
    isru_mode = state.isru_mode


    #------------dict for updating state-------------♡ 
    isru_updates = {
        ...,
    }
    
    #-----------dict for printing outputs------------♡ 
    isru_outputs = {
        ...,
    }

    return isru_updates, isru_outputs
