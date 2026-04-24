from dataclasses import replace
from .state import Habitat_State
from .mars_time import seconds_per_sol

# file for all things Mars dust

#--------------------constants-----------------------♡
base_dust_rate_per_sol = 0.007

primary_rad_dust_multiplier = 1.12   # placeholder
backup_rad_dust_multiplier = 0.885   # placeholder
solar_dust_miltiplier = 1.15   # placeholder
online_multiplier = 1.25    # online systems get dusty a bit faster

min_raditor_efficiency = 0.35   # placeholder
min_solar_effiency = 0.40   # placeholder
#----------------------------------------------------♡


#-----------------dust accumulation------------------♡
def get_dust_accumulation(state, dt_min):
    seconds_per_step = dt_min * 60
    sols_per_step = seconds_per_step / seconds_per_sol

    new_radiators = []
    new_solar_arrays = []

    #-------------------radiators--------------------♡
    for rad in state.radiators:
        new_rad = rad.copy()

        if new_rad["type"] == "primary":
            dust_multiplier = primary_rad_dust_multiplier

        else:
            dust_multiplier = backup_rad_dust_multiplier

        
        if new_rad["status"] == "online":
            dust_multiplier *= online_multiplier

        efficiency_loss = base_dust_rate_per_sol * dust_multiplier * sols_per_step
        
        new_rad["dust_factor"] = max(min_raditor_efficiency, new_rad["dust_factor"] - efficiency_loss)
        new_radiators.append(new_rad)
    
    #------------------solar arrays------------------♡
    for array in state.solar_arrays:
        new_array = array.copy()
        
        dust_rate = base_dust_rate_per_sol * solar_dust_miltiplier

        if new_array["status"] == "online":
            efficiency_loss *= online_multiplier

        efficiency_loss = dust_rate * sols_per_step
        
        new_array["dust_factor"] = max(min_solar_effiency, new_array["dust_factor"] - efficiency_loss)
        new_solar_arrays.append(new_array)
    
    return {
        "new_radiators" : new_radiators,
        "new_solar_arrays" : new_solar_arrays,
    }



