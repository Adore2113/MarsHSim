#### ------time--------------------------------♡
    mission_time_s

#### ------lights------------------------------♡
    light_level

#### ------crew--------------------------------♡
    crew_count
    crew_activity: str

#### ------habitat-----------------------------♡
    hab_vol_m3

# ------thermal control-----------------------------♡
    hab_temp_c
    insulation_strength_kw_per_c
    thermal_mass_kwh_per_c
    radiators
    
#### ------atmosphere targets and limits-------♡ 
    target_pressure_kpa
    min_safe_pressure_kpa
    max_safe_pressure_kpa

    target_o2_kpa
    target_co2_kpa
    target_n2_kpa
    target_ar_kpa

#### ------current atmosphere------------------♡
    o2_kpa
    co2_kpa
    n2_kpa
    ar_kpa

#### ------gas storage-------------------------♡
    n2_stored_kpa
    ar_stored_kpa
    co2_stored_kpa
    h2_stored_kg

#### ------OGA water---------------------------♡
    water_for_oga_kg


#### ------amine beds--------------------------♡
    amine_beds: list
    scrub_per_bed_kpa

#### ------power-------------------------------♡
    battery_max_capacity_kwh
    battery_stored_kwh 
    solar_arrays: list
    daylight_m2_kw
    peak_sunlight_today
    low_sunlight_streak_sols

#### ------placeholders for future plans-------♡
    relative_humidity

    # ------------ ♡ water ♡------------
    potable_water_l
    grey_water_l
    waste_brine_l

    #----- ♡ Integrity / safety ♡ -----
    leak_rate_kpa_per_hr
    smoke_ppm
    radiation_msv_per_day