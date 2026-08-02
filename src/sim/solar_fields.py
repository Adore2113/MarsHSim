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

#----------block targets-----------♡
target_summer_blocks_online = 35
target_spring_autumn_blocks_online = 38
target_winter_blocks_online = 43

flip_energy_per_block_kwh = 0.365
cover_energy_per_block_kwh = 0.0135
cleaning_energy_per_block_kwh = 0.365

default_tilt_deg = 30.0
summer_tilt_deg = 20.0  # placeholder
winter_tilt_deg = 40.0  # placeholder

#-----------dust buildup-----------♡
base_block_dust_rate_per_sol = 0.006    # open panels
min_operating_efficiency = 0.55    # when cleaning becomes mandatory
cleaning_trigger_dust_factor = 0.75


#---------------------------------------------------♡