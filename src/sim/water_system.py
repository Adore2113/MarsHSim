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

potable_water_tank_capacity_kg = 5000.0    #placeholder
gray_water_tank_capacity_kg = 500.0    # placeholder!
black_water_tank_capacity_kg = 300.0    # placeholder
#----------------------------------------------------♡



#------------calculate crew water changes------------♡
def get_crew_water_usage(state, crew_results, dt_min):
    hours_per_step = dt_min / 60

    potable_water_used_kg = crew_results.get("potable_water_used_kg", 0.0)
    gray_water_added_kg = crew_results.get("gray_water_added_kg", 0.0)
    black_water_added_kg = crew_results.get("black_water_added_kg", 0.0)

    new_potable_water_used_kg = max(0.0, state.potable_water_tank_kg - potable_water_used_kg)
    new_gray_water_added_kg = min(state.gray_water_tank_kg * gray_water_added_kg, gray_water_tank_capacity_kg)    # placeholder!
    new_black_water_added_kg = min(state.black_water_tank_kg * black_water_added_kg, black_water_tank_capacity_kg)








#------------run urine processor assembly------------♡
def run_upa(state, dt_min):
    hours_per_step = dt_min / 60
    ...


#------------run brine processor assembly------------♡
def run_bpa(state, dt_min):
    hours_per_step = dt_min / 60
    ...


#------------run water processor assembly------------♡
def run_wpa(state, dt_min):
    hours_per_step = dt_min / 60
    ...


#---------------update water storage-----------------♡
def update_water_tanks_kg(state, total_crew_water_usage_kg):
    ...