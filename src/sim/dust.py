#--------------------imports-------------------------♡
import math
import random
from .mars_time import seconds_per_sol
#----------------------------------------------------♡


#--------------------constants-----------------------♡
base_dust_rate_per_sol = 0.007

primary_rad_dust_multiplier = 1.12
backup_rad_dust_multiplier = 0.885
solar_dust_multiplier = 1.15
compressor_dust_multiplier = 1.05
pipe_dust_multiplier = 1.08
online_multiplier = 1.25    # online systems get dusty a bit faster

min_radiator_efficiency = 0.35
min_solar_efficiency = 0.40
min_compressor_efficiency = 0.45
min_pipe_efficiency = 0.50

clear_sky_tau = 0.35
storm_season_tau = 1.15

storm_season_ls_start_deg = 180.0
storm_season_ls_end_deg = 330.0

base_clear_opacity_tau = 0.35
base_storm_season_opacity_tau = 1.15

dusty_threshold_tau = 0.65    # between low and medium
storm_threshold_tau = 1.75    # between medium and high
max_storm_tau = 5.0

base_storm_probability = 0.001
seasonal_probability_bonus = 0.02
#----------------------------------------------------♡


#-----------storm probability for seasons------------♡
def get_storm_season_probability(ls_deg):
    if ls_deg < storm_season_ls_start_deg or ls_deg > storm_season_ls_end_deg:
        return 0.0

    degrees_into_season = ls_deg - storm_season_ls_start_deg
    season_length_deg = storm_season_ls_end_deg - storm_season_ls_start_deg
    percent_through_season = degrees_into_season / season_length_deg

    storm_season_probability = math.sin(math.pi * percent_through_season)

    return storm_season_probability


#--------------storm likelihood per sol--------------♡
def get_storm_chance_today(ls_deg):
    season_probability = get_storm_season_probability(ls_deg)
    storm_chance_today = base_storm_probability + seasonal_probability_bonus * season_probability
    
    return storm_chance_today


#--------------did a storm start today---------------♡
def roll_for_storm(ls_deg):
    storm_chance_today = get_storm_chance_today(ls_deg)
    roll = random.random()
    
    storm_started = roll < storm_chance_today

    return storm_started


#-----------get atmospheric dust opacity-------------♡
def get_dust_opacity(ls_deg):
    storm_probability = get_storm_season_probability(ls_deg)
    opacity_tau = base_clear_opacity_tau + (base_storm_season_opacity_tau - base_clear_opacity_tau) * storm_probability

    return opacity_tau

#-------------------storm status---------------------♡




#-----------------dust accumulation------------------♡
def get_dust_accumulation(state, dt_min):
    seconds_per_step = dt_min * 60
    sols_per_step = seconds_per_step / seconds_per_sol

    new_radiators = []
    new_solar_arrays = []
    new_compressors = []
    new_pipes = []

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
        
        new_rad["dust_factor"] = max(min_radiator_efficiency, new_rad["dust_factor"] - efficiency_loss)
        new_radiators.append(new_rad)
    
    #------------------solar arrays------------------♡
    for array in state.solar_arrays:
        new_array = array.copy()
        
        dust_rate = base_dust_rate_per_sol * solar_dust_multiplier

        if new_array["status"] == "online":
            dust_rate *= online_multiplier

        efficiency_loss = dust_rate * sols_per_step
        
        new_array["dust_factor"] = max(min_solar_efficiency, new_array["dust_factor"] - efficiency_loss)
        new_solar_arrays.append(new_array)

    #----------------isru compressors----------------♡
    for compressor in state.isru_compressors:
        new_compressor = compressor.copy()

        dust_rate = base_dust_rate_per_sol * compressor_dust_multiplier

        if new_compressor["status"] == "extracting":
            dust_rate *= online_multiplier

        efficiency_loss = dust_rate * sols_per_step

        new_compressor["dust_factor"] = max(min_compressor_efficiency, new_compressor["dust_factor"] - efficiency_loss)
        new_compressors.append(new_compressor)

    #----------------isru water pipes----------------♡
    for pipe in state.isru_pipes:
        new_pipe = pipe.copy()

        dust_rate = base_dust_rate_per_sol * pipe_dust_multiplier

        if new_pipe["status"] == "extracting":
            dust_rate *= online_multiplier

        efficiency_loss = dust_rate * sols_per_step

        new_pipe["dust_factor"] = max(min_pipe_efficiency, new_pipe.get("dust_factor", 1.0) - efficiency_loss)
        new_pipes.append(new_pipe)

    return {
        "new_radiators": new_radiators,
        "new_solar_arrays": new_solar_arrays,
        "new_compressors": new_compressors,
        "new_pipes": new_pipes,
    }
    
