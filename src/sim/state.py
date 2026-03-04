from dataclasses import dataclass

#creating habitat class
@dataclass
class Habitat_State:
    # Atmosphere
    total_pressure_kpa: float
    o2_kpa: float
    co2_kpa: float
    n2_kpa: float

    # Thermal
    cabin_temp_c: float
    relative_humidity: float

    # Water
    potable_water_l: float
    grey_water_l: float
    waste_brine_l: float

    # Power
    battery_kwh: float
    solar_input_kw: float
    load_kw: float

    # Integrity / safety
    leak_rate_kpa_per_hr: float
    smoke_ppm: float
    radiation_msv_per_day: float