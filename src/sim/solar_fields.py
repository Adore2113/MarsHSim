#--------------------imports-------------------------♡
from .mars_time import get_sunlight_amount, current_mars_season
#----------------------------------------------------♡

#--------------------constants-----------------------♡
land_area_acres = 50.0
land_area_hectares = 20.23
land_area_m2 = 202300.0
block_area_m2 = 4046.0

total_panels = 101,250
area_per_panel_m2 = 2.0

total_arrays = 2,250
panels_per_array = 45
area_per_panel_m2 = 89.9

total_blocks = 50
arrays_per_block = 45

#-----block targets-----♡
target_seasonal_blocks_online = 38
target_summer_blocks_online = 35
target_winter_blocks_online = 43

flip_energy_per_block_kwh = 0.365
cover_energy_per_block_kwh = 0.0135
cleaning_energy_per_block_kwh = 0.365

default_tilt_deg = 30.0
summer_tilt_deg = 20.0  # placeholder
winter_tilt_deg = 40.0  # placeholder

#---panel performance---♡
solar_conversion_ratio = 0.20
min_irradiance_w_per_m2 = 20.0
clear_sy_peak_irradiance_w_per_m2 = 350.0   # clear sol average ~ 112 W/m2

#-----dust buildup------♡
base_block_dust_rate_per_sol = 0.006    # open panels
min_operating_efficiency = 0.55    # when cleaning becomes mandatory
cleaning_trigger_dust_factor = 0.75
#---------------------------------------------------♡


#---------------target blocks online----------------♡
def get_target_blocks_online(state):
    is_daytime = get_sunlight_amount(state) > 0.0

    if not is_daytime:
        return 0

    season = current_mars_season(state)
    if season == "northern_summer":
        return target_summer_blocks_online

    elif season == "northern_winter":
        return target_winter_blocks_online

    else:
        return target_seasonal_blocks_online


#----------flip blocks to match target----------♡
def manage_block_flips(state, dt_min):
    hours_per_step = dt_min / 60.0

    new_blocks_online = [block.copy() for block in state.solar_blocks]
    blocks_up_count = sum(1 for block in new_blocks_online if block["flip_position"] == "up")

    target_blocks_online = get_target_blocks_online(state)
    flips_this_step = 0

    if blocks_up_count < target_blocks_online:
        blocks_needed_up = target_blocks_online - blocks_up_count

        for block in new_blocks_online:
            if blocks_needed_up > 0 and block["flip_position"] == "down":
                block["flip_position"] = "up"
                blocks_needed_up -= 1
                blocks_up_count += 1
                flips_this_step += 1
    
    elif blocks_up_count > target_blocks_online:
        blocks_needed_down = blocks_up_count - target_blocks_online

        for block in new_blocks_online:
            if blocks_needed_down > 0 and block["flip_position"] == "up":
                block["flip_position"] = "down"
                blocks_needed_down -= 1
                blocks_up_count -= 1
                flips_this_step += 1

# -------------------------------------------♡




#---------------------------------------------------♡
