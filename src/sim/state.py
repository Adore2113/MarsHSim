from dataclasses import dataclass

#creating habitat class
@dataclass
class Habitat_State:
    
    crew_count: int
    hab_vol_m3: float

    # Time
    mission_time_s: int

    # Atmosphere
    o2_kpa: float # oxygen
    co2_kpa: float # carbon dioxide
    n2_kpa: float # nitrogen 
    ar_kpa: float # argon

    n2_stored_kpa: float
    ar_stored_kpa: float
    min_pressure_kpa: float
    max_pressure_kpa: float

    # CO2 Scrubbers
    amine_beds: list

    # Dalton's Law
    @property
    def total_pressure_kpa(self) -> float:
        return self.o2_kpa + self.co2_kpa + self.n2_kpa + self.ar_kpa

    @property
    def o2_percent(self):
        if self.total_pressure_kpa == 0:
            return 0
        return 100 * self.o2_kpa / self.total_pressure_kpa

    @property
    def co2_percent(self):
        if self.total_pressure_kpa == 0:
            return 0
        return 100 * self.co2_kpa / self.total_pressure_kpa
    
    @property
    def n2_percent(self):
        if self.total_pressure_kpa == 0:
            return 0
        return 100 * self.n2_kpa / self.total_pressure_kpa

    @property
    def ar_percent(self):
        if self.total_pressure_kpa == 0:
            return 0
        return 100 * self.ar_kpa / self.total_pressure_kpa

    water_for_oga_kg: float







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

    # Hydogen Byproduct
    h2_stored_kg: float = 0.0