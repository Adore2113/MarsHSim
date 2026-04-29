## Time:
    mission_time_s

## Light System:
    light_level

## Crew:
    crew_count
    crew_activity

## Habitat:
    hab_vol_m3

## Thermal:
    hab_temp_c
    target_temp_c
    min_comfort_temp_c
    max_comfort_temp_c

    mars_temp_c

    target_humidity_pct
    current_humidity_pct

    insulation_strength_kw_per_c
    thermal_mass_kwh_per_c

    radiators
    heaters
    
## Atmosphere:
#### ♡---------gas targets----------♡
    target_pressure_kpa: float
    target_o2_kpa: float
    target_co2_kpa: float
    target_n2_kpa: float
    target_ar_kpa: float
    target_ch2_kpa: float

#### ♡-------min safe levels--------♡
    min_safe_pressure_kpa: float
    #min_safe_o2_kpa: float
    #min_safe_co2_kpa: float
    #min_safe_n2_kpa: float
    #min_safe_ar_kpa: float
    min_safe_ch4_kpa: float

#### ♡--------max safe levels-------♡
    max_safe_pressure_kpa: float
    #max_safe_o2_kpa: float
    #max_safe_co2_kpa: float
    #max_safe_n2_kpa: float
    #max_safe_ar_kpa: float
    max_safe_ch4_kpa: float

#### ♡------current gas levels------♡
    o2_kpa: float
    co2_kpa: float
    n2_kpa: float
    ar_kpa: float
    ch4_kpa: float

#### ♡--------gas in storage--------♡
    n2_stored_kpa: float
    ar_stored_kpa: float
    co2_stored_kpa: float
    h2_stored_kg: float
    ch4_stored_kg: float 


## Amine Beds:
    amine_beds
    scrub_per_bed_kpa

## Power:
    battery_max_capacity_kwh
    battery_stored_kwh 
    
    solar_arrays
    daylight_m2_kw

    peak_sunlight_today
    low_sunlight_streak_sols
    solar_absorptivity

## Water:
#### ♡-------water in storage-------♡

    potable_water_storage_kg
    gray_water_storage_kg
    black_water_storage_kg   
    condensate_storage_kg   
    brine_storage_kg
#### ♡------water storage limits----♡
    potable_water_storage_capacity_kg
    gray_water_storage_capacity_kg
    black_water_storage_capacity_kg
    condensate_storage_capacity_kg
    brine_storage_capacity_kg 

## Wellness Lights:
    wellness_lights_on