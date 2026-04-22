from dataclasses import replace
from .state import Habitat_State

# file for managing water, water recycling and generation

#--------------------constants-----------------------♡
upa_recovery_rate = 0.85    # urine processor assembly
wpa_recovery_rate = 0.95    # water processor assembly
bpa_recovery_rate = 0.60    # brine processor assembly

base_upa_power_kw = 0.45
base_wpa_power_kw = 0.35
base_bpa_power_kw = 0.75

upa_handling_capacity_per_hour_kg = 6.0
wpa_handling_capacity_per_hour_kg = 10.0
bpa_handling_capacity_per_hour_kg = 0.15
#----------------------------------------------------♡



#-------calculate how much water crew has used-------♡
def crew_water_usage_kg(state):
    total_crew_water_usage_kg = crew_gray_water_kg + laundry_wastewater_kg + hygiene_wastewater_kg + crew_Water_consumed_kg

    return total_crew_water_usage_kg

#------------run urine processor assembly------------♡
def run_upa(state, dt_min):
    hours_per_step = dt_min / 60
    upa_base_power_kw = ...
    total_wastewater_produced_kg = crew.wastewater_added_kg * hours_per_step
    ...


#------------run brine processor assembly------------♡
def run_bpa(state, dt_min):
    hours_per_step = dt_min / 60
    bpa_base_power_kw = ...
    ...


#------------run water processor assembly------------♡
def run_wpa(state, dt_min):
    hours_per_step = dt_min / 60
    wpa_base_power_kw = ...
    ...


#---------------update water storage-----------------♡
def update_water_tanks_kg(state, total_crew_water_usage_kg):
    total_water_usage_kg = oga_water_consumed + 

    new_water_stored = state.water_tank_kg - total_water_usage_kg

    return new_water_stored