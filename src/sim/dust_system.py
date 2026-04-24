from dataclasses import replace
from .state import Habitat_State
from .mars_time import seconds_per_sol

# file for all things Mars dust

#--------------------constants-----------------------♡
dust_rate_per_sol = 0.007

primary_radiator_dust_mulitplier = 1.1   # placeholder
backup_radiator_dust_multiplier = 0.9   # placeholder
solar_dust_miltiplier = 0.40   # placeholder

min_raditor_efficiency = 0.35   # placeholder
min_solar_effiency = 0.40   # placeholder
#----------------------------------------------------♡


#-----------------dust accumulation------------------♡
def get_total_dust_accumulation(state, ... ):
    ...