### Habitat:
    - hab_vol_m3

### Time / Daylight:
    - mission_time_s
    - daylight_m2_kw
    - peak_sunlight_today
    - low_sunlight_streak_sols

### Lights:
    - light_level

### Crew:
    - crew_count
    - crew_activity

### Greenhouse:
    - greenhouse_floor_area_m2
    - structural_floor_area_m2
    - container_floor_area_m2
    - rack_floor_area_m2
    - rack_bonus_area_m2
    - usable_floor_grow_area_m2
    - walkway_area_m2
    - ceiling_hanging_area_m2
    - ceiling_bonus_area_m2
    - total_effective_grow_area_m2
    - greenhouse_zones
    - greenhouse_on
    - greenhouse_stage
    - food_support_level
    - stored_food_still_needed

### Thermal:
    - hab_temp_c
    - target_temp_c
    - min_comfort_temp_c
    - max_comfort_temp_c
    - mars_temp_c
    - target_humidity_pct
    - current_humidity_pct
    - insulation_strength_kw_per_c
    - thermal_mass_kwh_per_c
    - radiators
    - heaters

### Atmosphere:
    - base_gas_leak_kpa_per_hour

#### Gas Leak Rates:
    - o2_leak_rate_kpa_per_hr
    - n2_leak_rate_kpa_per_hr
    - ar_leak_rate_kpa_per_hr
    - ch4_leak_rate_kpa_per_hr
    - h2_leak_rate_kpa_per_hr
    - co2_leak_rate_kpa_per_hr

#### Gas Targets:
    - target_pressure_kpa
    - target_o2_kpa
    - target_co2_kpa
    - target_n2_kpa
    - target_ar_kpa
    - target_ch4_kpa
    - target_h2_kpa

#### Min Safe Gas Levels:
    - min_safe_pressure_kpa
    - min_safe_o2_kpa
    - min_safe_co2_kpa
    - min_safe_n2_kpa
    - min_safe_ar_kpa
    - min_safe_ch4_kpa
    - min_safe_h2_kpa
    - 
#### Max Safe Gas Levels:
    - max_safe_pressure_kpa
    - max_safe_o2_kpa
    - max_safe_co2_kpa
    - max_safe_n2_kpa
    - max_safe_ar_kpa
    - max_safe_ch4_kpa
    - max_safe_h2_kpa
 
#### Current Gas Levels:
    - o2_kpa
    - co2_kpa
    - n2_kpa
    - ar_kpa
    - ch4_kpa
    - h2_kpa
 
#### Gas in Storage:
    - o2_stored_kg
    - co2_stored_kg
    - n2_stored_kg
    - ar_stored_kg
    - h2_stored_kg
    - ch4_stored_kg

#### Gas Storage Limits:
    - o2_storage_capacity_kg 
    - co2_storage_capacity_kg 
    - n2_storage_capacity_kg 
    - ar_storage_capacity_kg 
    - ch4_storage_capacity_kg
    - h2_storage_capacity_kg

#### Amine Beds:
    - amine_beds
    - scrub_per_bed_kpa

#### Power and Solar:
    - battery_max_capacity_kwh
    - battery_stored_kwh 
    - solar_arrays
    - solar_absorptivity

### Water:
#### Water in Storage:
    - potable_water_storage_kg
    - gray_water_storage_kg
    - black_water_storage_kg   
    - condensate_storage_kg   
    - brine_storage_kg
    - 
#### Water Storage Limits:
    - potable_water_storage_capacity_kg
    - gray_water_storage_capacity_kg
    - black_water_storage_capacity_kg
    - condensate_storage_capacity_kg
    - brine_storage_capacity_kg 
    - upa_on
    - bpa_on
    - wpa_on

### Placeholders:
    - radiation_msv_per_day

### Wellness Lights:
    - wellness_lights_on

### Sabatier:
    - sabatier_on

### Isru Water:
    - isru_on
    - isru_pipes
    - raw_isru_water_storage_kg: float
    - raw_isru_water_storage_capacity_kg: float

### Isru Atmosphere:
    - isru_atm_on
    - isru_compressors
    - isru_atm_sorbent_beds