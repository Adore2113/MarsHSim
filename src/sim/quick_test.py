#--------------------imports-------------------------♡
from .state import Habitat_State
from .engine import step
from .alerts import get_alerts
from .print import print_sim
from .mars_time import seconds_per_sol, get_sol_time
#----------------------------------------------------♡

#-------------------habitat state--------------------♡
s0 = Habitat_State(
    hab_vol_m3 = 2000.0,
    power_mode = "normal",
  
    #-------time and daylight------♡
    mission_time_s = 0,

    daylight_m2_kw = 0.0,
    peak_sunlight_today = 0.0,
    low_sunlight_streak_sols = 0,
    
    #------------lights------------♡
    light_level = 0.0,
    wellness_lights_on = False,

    #-------------crew-------------♡
    crew_count = 30,
    crew_activity = "normal",

    #----------greenhouse----------♡
    greenhouse_vol_m3 = 1007.0,

    greenhouse_floor_area_m2 = 265.0,
    greenhouse_height_m = 3.8,
    
    structural_area_m2 = 95.0,
    container_area_m2 = 110.0,
    
    rack_area_m2 = 35.0,
    rack_bonus_area_m2 = 180.0,
    
    usable_floor_grow_area_m2 = 220.0,
    helix_walkway_area_m2 = 45.0,
    
    ceiling_hanging_area_m2 = 70.0,
    ceiling_bonus_area_m2 = 45.0,
    
    total_effective_grow_area_m2 = 515.0,

    greenhouse_zones = [
        #------------structural zone-----------------♡
        {
        "zone": "structural",
        "grow_method": "hydroponic_large_crop_mix",
        "floor_area_m2": 90.0,
        "effective_grow_area_m2": 90.0,  

        #-----------targets------------♡
        "ideal_temp_c": 26.0,
        "light_target_kw_per_m2": 0.75,

        #------------biology-----------♡
        "base_growth_rate_per_sol": 0.011,
        "base_light_absorption_pct": 0.75,
        "base_water_needed_per_m2_kg_per_sol": 3.4,
        
        "food_yield_per_m2_kg_per_sol": 0.25,
        "co2_consumed_per_m2_kpa_per_sol": 0.025,
        "o2_produced_per_m2_kpa_per_sol": 0.022,

        #----------hydroponics---------♡
        "water_recirculation_efficiency": 0.82,

        #----------modifiers-----------♡
        "water_multiplier": 1.15,
        "growth_rate_multiplier": 0.85,
        "food_yield_multiplier": 1.25,

        #-----------runtime------------♡
        "light_exposure": 0.60,
        "health": 0.98,
        "growth_progress": 0.35,
        "harvest_ready": False,
        },
        #-------------container zone-----------------♡
        {
        "zone": "container",
        "grow_method": "hydroponic_medium_crop_mix",
        "floor_area_m2": 110.0,
        "effective_grow_area_m2": 110.0,

        #-----------targets------------♡
        "ideal_temp_c": 24.0,
        "light_target_kw_per_m2": 0.70,

        #------------biology-----------♡
        "base_growth_rate_per_sol": 0.016,
        "base_light_absorption_pct": 0.70,
        "base_water_needed_per_m2_kg_per_sol": 2.6,
        
        "food_yield_per_m2_kg_per_sol": 0.29,
        "co2_consumed_per_m2_kpa_per_sol": 0.025,
        "o2_produced_per_m2_kpa_per_sol": 0.020,

        #----------hydroponics---------♡
        "water_recirculation_efficiency": 0.88,

        #----------modifiers-----------♡
        "water_multiplier": 1.0,
        "growth_rate_multiplier": 0.75,
        "food_yield_multiplier": 1.0,

        #-----------runtime------------♡
        "light_exposure": 0.65,
        "health": 0.98,
        "growth_progress": 0.42,
        "harvest_ready": False,
        },
        #----------------rack zone-------------------♡
        {
        "zone": "rack",
        "grow_method": "hydroponic_small_crop_mix",
        "floor_area_m2": 35.0,
        "effective_grow_area_m2": 124.0,

        #-----------targets------------♡
        "ideal_temp_c": 22.0,
        "light_target_kw_per_m2": 0.60,

        #------------biology-----------♡
        "base_growth_rate_per_sol": 0.030,
        "base_light_absorption_pct": 0.65,
        "base_water_needed_per_m2_kg_per_sol": 1.95,
        
        "food_yield_per_m2_kg_per_sol": 0.21,
        "co2_consumed_per_m2_kpa_per_sol": 0.018,
        "o2_produced_per_m2_kpa_per_sol": 0.015,

        #----------hydroponics---------♡
        "water_recirculation_efficiency": 0.94,

        #----------modifiers-----------♡
        "water_multiplier": 0.9,
        "growth_rate_multiplier": 0.95,
        "food_yield_multiplier": 0.95,

        #-----------runtime------------♡
        "light_exposure": 0.75,
        "health": 0.98,
        "growth_progress": 0.28,
        "harvest_ready": False,
        }
    ],
    
    greenhouse_on = True,
    greenhouse_stage = "starter",
    food_support_level = "partial",
    stored_food_still_needed = True,

    #--------------------thermal---------------------♡
    hab_temp_c = 23.0,
    target_temp_c = 23.0,
    min_comfort_temp_c = 20.0,
    max_comfort_temp_c = 25.0,

    mars_temp_c = -20.0,

    current_humidity_pct = 48.0,
    target_humidity_pct = 48.0,

    insulation_strength_kw_per_c = 0.65,
    thermal_mass_kwh_per_c = 95.0,

    radiators = [
        {"id": 1, "status": "standby", "area_m2": 68, "efficiency": 0.95, "dust_factor": 1.0, "type": "primary"},
        {"id": 2, "status": "standby", "area_m2": 68, "efficiency": 0.95, "dust_factor": 1.0, "type": "primary"},
        {"id": 3, "status": "standby", "area_m2": 68, "efficiency": 0.95, "dust_factor": 1.0, "type": "primary"},
        {"id": 4, "status": "standby", "area_m2": 68, "efficiency": 0.95, "dust_factor": 1.0, "type": "primary"},
        {"id": 5, "status": "standby", "area_m2": 68, "efficiency": 0.95, "dust_factor": 1.0, "type": "primary"},
       
        {"id": 6, "status": "standby", "area_m2": 55, "efficiency": 0.85, "dust_factor": 1.0, "type": "backup"},
        {"id": 7, "status": "standby", "area_m2": 55, "efficiency": 0.85, "dust_factor": 1.0, "type": "backup"},
    ],

    heaters = [
        {"id": 1, "status": "standby", "power_kw": 9.0, "efficiency": 1.0, "type": "primary"},
        {"id": 2, "status": "standby", "power_kw": 9.0, "efficiency": 1.0, "type": "primary"},
        {"id": 3, "status": "standby", "power_kw": 9.0, "efficiency": 1.0, "type": "primary"},
        {"id": 4, "status": "standby", "power_kw": 9.0, "efficiency": 1.0, "type": "primary"},
        
        {"id": 5, "status": "standby", "power_kw": 8.0, "efficiency": 0.98, "type": "backup"},
        {"id": 6, "status": "standby", "power_kw": 8.0, "efficiency": 0.98, "type": "backup"},
    ],

#-------------------atmosphere-------------------♡
    oga_on = True,
    base_gas_leak_kpa_per_hour = 0.004,

     #-------gas leak rates---------♡
    o2_leak_rate_kpa_per_hr = 0.006,
    n2_leak_rate_kpa_per_hr = 0.007,
    ar_leak_rate_kpa_per_hr = 0.005,
    ch4_leak_rate_kpa_per_hr = 0.0,    # figure this out, if I want to have a ch4 leak at all or not
    h2_leak_rate_kpa_per_hr = 0.025,
    co2_leak_rate_kpa_per_hr = 0.005,

    #---------gas targets----------♡    
    target_pressure_kpa = 65.0,
    
    target_ar_kpa = 22.6,
    target_ch4_kpa = 0.05,    
    target_co2_kpa = 0.4,
    target_h2_kpa = 0.0,
    target_n2_kpa = 22.0,
    target_o2_kpa = 20.0,

    #-------min safe levels--------♡
    min_safe_pressure_kpa = 55.0,

    min_safe_ar_kpa = 10.0,
    min_safe_ch4_kpa = 0.0,
    min_safe_co2_kpa = 0.0,
    min_safe_h2_kpa = 0.0,
    min_safe_n2_kpa = 10.0,
    min_safe_o2_kpa = 18.0,

    #--------max safe levels-------♡
    max_safe_pressure_kpa = 70.0,

    max_safe_ar_kpa = 30.0,
    max_safe_ch4_kpa = 0.8,       # fire risk!
    max_safe_co2_kpa = 1.0,
    max_safe_h2_kpa = 0.4,
    max_safe_n2_kpa = 30.0,    
    max_safe_o2_kpa = 25.0,

    #------current gas levels------♡
    ar_kpa = 21.6,
    ch4_kpa = 0.0,
    co2_kpa = 0.6,
    h2_kpa = 0.0,    
    n2_kpa = 18.0,
    o2_kpa = 20.0,

    #--------gas in storage--------♡
    ar_stored_kg = 400.0,
    ch4_stored_kg = 0.0,
    co2_stored_kg = 20.0, 
    h2_stored_kg = 50.0,    # starting with this for Sabatier testing
    n2_stored_kg = 800.0,
    o2_stored_kg = 680.0,

    #------gas storage limits------♡
    ar_storage_capacity_kg = 1200.0,
    ch4_storage_capacity_kg = 400.0,
    co2_storage_capacity_kg = 500.0,    
    h2_storage_capacity_kg = 300.0,
    n2_storage_capacity_kg = 2000.0,
    o2_storage_capacity_kg = 1500.0,

    #------------------amine_beds--------------------♡
    amine_beds = [
        {"id": 1, "status": "standby", "capacity": 3.0, "co2_load": 0.0, "type": "primary"},
        {"id": 2, "status": "standby", "capacity": 3.0, "co2_load": 0.0, "type": "primary"},
        {"id": 3, "status": "standby", "capacity": 3.0, "co2_load": 0.0, "type": "primary"},
        {"id": 4, "status": "standby", "capacity": 3.0, "co2_load": 0.0, "type": "primary"},
        
        {"id": 5, "status": "standby", "capacity": 3.0, "co2_load": 0.0, "type": "backup"},
        {"id": 6, "status": "standby", "capacity": 3.0, "co2_load": 0.0, "type": "backup"},
    ],
    scrub_per_bed_kpa = 0.0035,

    #-----------------power / solar------------------♡
    battery_max_capacity_kwh = 1300.0,
    battery_stored_kwh = 1100.0,
    
    solar_arrays = [
        {"id": 1, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},
        {"id": 2, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},
        {"id": 3, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},
        {"id": 4, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},
        {"id": 5, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},
        {"id": 6, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},
        {"id": 7, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},
        {"id": 8, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},

        {"id": 9, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "backup"},
        {"id": 10,"status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "backup"}
    ], 
    
    solar_absorptivity = 0.68,
    
    #---------------------water----------------------♡
    potable_water_storage_kg = 5000.0,
    gray_water_storage_kg = 0.0,
    black_water_storage_kg = 0.0,
    condensate_storage_kg = 0.0,
    brine_storage_kg = 0.0,

    potable_water_storage_capacity_kg = 6500.0,
    gray_water_storage_capacity_kg = 1200.0,
    black_water_storage_capacity_kg = 800.0,
    condensate_storage_capacity_kg = 250.0,
    brine_storage_capacity_kg = 400.0,

    upa_on = True,
    bpa_on = True,
    wpa_on = True,

    #------------------placeholders------------------♡
    leak_rate_kpa_per_hr = 0.0,
    smoke_ppm = 0.0,
    radiation_msv_per_day = 0.7,

    #--------------------sabatier--------------------♡
    sabatier_on = True,
   
    #----------------------isru----------------------♡
    isru_on = True,

    isru_pipes = [
        {"id": 1, "status": "offline", "dust_factor": 1.0, "condition": 0.98, "type": "primary"},
        {"id": 2, "status": "offline", "dust_factor": 1.0, "condition": 0.97, "type": "primary"},
        {"id": 3, "status": "offline", "dust_factor": 1.0, "condition": 0.97, "type": "primary"},
        
        {"id": 4, "status": "offline", "dust_factor": 1.0, "condition": 0.99, "type": "backup"},
        {"id": 5, "status": "offline", "dust_factor": 1.0, "condition": 0.99, "type": "backup"},
        {"id": 6, "status": "offline", "dust_factor": 1.0, "condition": 0.99, "type": "backup"},
    ],

    raw_isru_water_storage_kg = 0.0,
    raw_isru_water_storage_capacity_kg = 1000.0,
    )


state = s0
last_printed_sol = -1

for i in range(30000):

    state, outputs = step(state)
    alerts = get_alerts(state, outputs)

    current_sol = int(state.mission_time_s // seconds_per_sol)

    _, sol_hour, minutes = get_sol_time(state)
    if 38 <= current_sol <= 43 and sol_hour in (6, 12):
        print_sim(state, outputs, alerts)
    # if sol_hour == 12 and current_sol != last_printed_sol:
    #     print_sim(state, outputs, alerts)
    #     last_printed_sol = current_sol
# ---------------------
# previous_sol = -1
# last_print_hour = None

# for i in range(12000):    # 12000 = ~40 sols, 30000 = ~100

#     state, outputs = step(state)
#     alerts = get_alerts(state, outputs)

#     current_sol = int(state.mission_time_s // seconds_per_sol)

#     #if current_sol != previous_sol:
#     _, sol_hour, minutes = get_sol_time(state)

#     if sol_hour in (12,) and sol_hour != last_print_hour:
#         print_sim(state, outputs, alerts)
#         last_print_hour = sol_hour