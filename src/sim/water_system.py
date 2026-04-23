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

potable_water_storage_capacity_kg = 5000.0    # placeholder
gray_water_storage_capacity_kg = 500.0    # placeholder
black_water_storage_capacity_kg = 300.0    # placeholder
condensate_storage_capacity_kg = 80.0    # placeholder
#----------------------------------------------------♡



#------------calculate crew water changes------------♡
def crew_water_usage(state, crew_results, dt_min):
    potable_water_used_kg = crew_results.get("potable_water_used_kg", 0.0)
    gray_water_added_kg = crew_results.get("gray_water_added_kg", 0.0)
    black_water_added_kg = crew_results.get("black_water_added_kg", 0.0)

    new_potable_water_storage_kg = max(0.0, state.potable_water_storage_kg - potable_water_used_kg)
    new_gray_water_storage_kg = min(state.gray_water_storage_kg + gray_water_added_kg, gray_water_storage_capacity_kg)    # placeholder!
    new_black_water_storage_kg = min(state.black_water_storage_kg + black_water_added_kg, black_water_storage_capacity_kg)

    return {
        "potable_water_used_kg": potable_water_used_kg,
        "gray_water_added_kg": gray_water_added_kg,
        "black_water_added_kg": black_water_added_kg,

        "new_potable_water_storage_kg": new_potable_water_storage_kg,
        "new_gray_water_storage_kg": new_gray_water_storage_kg,
        "new_black_water_storage_kg": new_black_water_storage_kg,
    }


#------------run urine processor assembly------------♡
def run_upa(state, dt_min):
    hours_per_step = dt_min / 60
    
    if state.black_water_storage_kg <= 0.1:
        return {"recovered_water_kg" : 0.0, "brine_added_kg" : 0.0, "black_water_removed_kg": 0.0, "upa_power_used_kw" : 0.0, "upa_energy_used_kwh" : 0.0}
    
    black_water_removed_kg = min(state.black_water_storage_kg, upa_handling_capacity_per_hour_kg * hours_per_step)
    
    recovered_water_kg = black_water_removed_kg * upa_recovery_rate
    brine_added_kg = black_water_removed_kg  * (1 - upa_recovery_rate)

    if black_water_removed_kg > 0:
        upa_power_used_kw = base_upa_power_kw
    
    else:
        upa_power_used_kw = 0.0

    upa_energy_used_kwh = upa_power_used_kw * hours_per_step

    return {
    "recovered_water_kg": recovered_water_kg,
    "brine_added_kg": brine_added_kg,

    "black_water_removed_kg": black_water_removed_kg,

    "upa_power_used_kw": upa_power_used_kw,
    "upa_energy_used_kwh" : upa_energy_used_kwh
    }


#------------run brine processor assembly------------♡
def run_bpa(state, dt_min):
    hours_per_step = dt_min / 60

    if state.brine_storage_kg <= 0.1:
        return {"recovered_water_kg" : 0.0, "water_processed_kg": 0.0,  "bpa_power_used_kw" : 0.0, "bpa_energy_used_kwh" : 0.0}

    water_processed_kg = min(state.brine_storage_kg, bpa_handling_capacity_per_hour_kg * hours_per_step)
    recovered_water_kg = water_processed_kg * bpa_recovery_rate

    if water_processed_kg > 0:
        bpa_power_used_kw = base_bpa_power_kw
    
    else:
        bpa_power_used_kw = 0.0

    bpa_energy_used_kwh = bpa_power_used_kw * hours_per_step

    return {
        "recovered_water_kg": recovered_water_kg,
        "water_processed_kg": water_processed_kg,
        "bpa_power_used_kw": bpa_power_used_kw,
        "bpa_energy_used_kwh": bpa_energy_used_kwh,
    }


#------------run water processor assembly------------♡
def run_wpa(state, dt_min):
    hours_per_step = dt_min / 60
    total_water_input_kg = state.gray_water_storage_kg + state.condensate_storage_kg
    
    if total_water_input_kg <= 0.1:
        return {"recovered_water_kg" : 0.0, "water_processed_kg": 0.0, "condensate_removed_kg":0.0, "gray_water_removed_kg": 0.0, "wpa_power_used_kw" : 0.0, "wpa_energy_used_kwh" : 0.0}

    water_processed_kg = min(total_water_input_kg, wpa_handling_capacity_per_hour_kg * hours_per_step)
    condensate_removed_kg = min(state.condensate_storage_kg, water_processed_kg)
    remaining_wpa_capacity_kg = water_processed_kg - condensate_removed_kg
    gray_water_removed_kg = min(state.gray_water_storage_kg, remaining_wpa_capacity_kg)
    
    recovered_water_kg = water_processed_kg * wpa_recovery_rate

    if water_processed_kg > 0:
        wpa_power_used_kw = base_wpa_power_kw
    
    else:
        wpa_power_used_kw = 0.0

    wpa_energy_used_kwh = wpa_power_used_kw * hours_per_step

    return {
        "recovered_water_kg": recovered_water_kg,
        "water_processed_kg": water_processed_kg,
        "condensate_removed_kg": condensate_removed_kg,
        "gray_water_removed_kg": gray_water_removed_kg,

        "wpa_power_used_kw": wpa_power_used_kw,
        "wpa_energy_used_kwh": wpa_energy_used_kwh,
    }



#---------------update water storage-----------------♡
def update_water_storages_kg(state, total_crew_water_usage_kg):
    ...