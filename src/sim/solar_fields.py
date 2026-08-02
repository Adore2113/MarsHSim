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
panel_efficiency = 0.20
solar_conversion_ratio = 0.20
min_irradiance_w_per_m2 = 20.0
clear_sy_peak_irradiance_w_per_m2 = 350.0   # clear sol average ~ 112 W/m2

#-----dust buildup------♡
base_block_dust_rate_per_sol = 0.006    # open panels
min_operating_efficiency = 0.55    # when cleaning becomes mandatory
cleaning_trigger_dust_factor = 0.75

dust_factor_restored = 0.35
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


#------------flip blocks to match target------------♡
def manage_block_flips(state, dt_min):
    hours_per_step = dt_min / 60.0

    new_blocks = [block.copy() for block in state.solar_blocks]
    blocks_up_count = sum(1 for block in new_blocks if block["flip_position"] == "up")

    target_blocks_online = get_target_blocks_online(state)
    flips_this_step = 0

    if blocks_up_count < target_blocks_online:
        blocks_needed_up = target_blocks_online - blocks_up_count

        for block in new_blocks:
            if blocks_needed_up > 0 and block["flip_position"] == "down":
                block["flip_position"] = "up"
                blocks_needed_up -= 1
                blocks_up_count += 1
                flips_this_step += 1
    
    elif blocks_up_count > target_blocks_online:
        blocks_needed_down = blocks_up_count - target_blocks_online

        for block in new_blocks:
            if blocks_needed_down > 0 and block["flip_position"] == "up":
                block["flip_position"] = "down"
                blocks_needed_down -= 1
                blocks_up_count -= 1
                flips_this_step += 1

    flip_energy_used_kwh = flips_this_step * (flip_energy_per_block_kwh + cover_energy_per_block_kwh)
    if hours_per_step > 0:
        flip_power_used_kw = flip_energy_used_kwh / hours_per_step
    
    else:
        flip_power_used_kw = 0.0

    return new_blocks, blocks_up_count, flips_this_step, flip_energy_used_kwh, flip_power_used_kw


#------------dust build up and cleaning-------------♡
def dust_and_cleaning(new_blocks, dt_min):
    hours_per_step = dt_min / 60.0
    seconds_per_step = dt_min * 60.0
    sols_per_step = seconds_per_step / 88775.244

    cleaned_this_step = 0

    for block in new_blocks:
        if block["flip_position"] == "up":
            dust_loss = base_block_dust_rate_per_sol * sols_per_step
            block["dust_factor"] = max(min_irradiance_w_per_m2, block["dust_factor"] - dust_loss)

            if block["dust_factor"] <= cleaning_trigger_dust_factor:
                block["dust_factor"] = min(1.0, block["dust_factor"] + dust_factor_restored)
                cleaned_this_step += 1

    cleaning_energy_used_kwh = cleaned_this_step * cleaning_energy_per_block_kwh
    if hours_per_step > 0:
        cleaning_power_used_kw  = cleaning_energy_used_kwh / hours_per_step
    
    else:
        cleaning_power_used_kw  = 0.0
    
    return new_blocks, cleaned_this_step, cleaning_energy_used_kwh, cleaning_power_used_kw


#------------field power generation-----------------♡
def get_block_generation(state, new_blocks, dt_min):
    hours_per_step = dt_min / 60.0
    sunlight_amount = get_sunlight_amount(state)

    base_irradiance_w_per_m2 = clear_sy_peak_irradiance_w_per_m2 * sunlight_amount

    if sunlight_amount > 0.0:
        irradiance_w_per_m2 = max(base_irradiance_w_per_m2, min_irradiance_w_per_m2)
    
    else:
        irradiance_w_per_m2 = 0.0

    total_field_power_generated_kw = 0.0

    for block in new_blocks:
        if block["flip_position"] == "up":
            block_power_kw = ((irradiance_w_per_m2 / 1000.0) * block_area_m2 * panel_efficiency * block["dust_factor"])
            total_field_power_generated_kw += block_power_kw

    total_field_energy_generated_kwh = total_field_power_generated_kw * hours_per_step

    return total_field_power_generated_kw, total_field_energy_generated_kwh

#---------------------------------------------------♡