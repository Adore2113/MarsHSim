from dataclasses import dataclass

@dataclass
class Habitat_State:
# ------time----------------------------------------♡
    mission_time_s: int

# ------lights--------------------------------------♡
    light_level: float

# ------crew----------------------------------------♡
    crew_count: int
    crew_activity: str

# ------habitat-------------------------------------♡
    hab_vol_m3: float
    hab_temp_c: float

# ------atmosphere targets and limits---------------♡ 
    target_pressure_kpa: float
    min_safe_pressure_kpa: float
    max_safe_pressure_kpa: float

    target_o2_kpa: float
    target_co2_kpa: float
    target_n2_kpa: float
    target_ar_kpa: float

# ------current atmosphere--------------------------♡
    o2_kpa: float
    co2_kpa: float
    n2_kpa: float
    ar_kpa: float

# ------gas storage---------------------------------♡
    n2_stored_kpa: float
    ar_stored_kpa: float
    co2_stored_kpa: float
    h2_stored_kg: float

# ------OGA water-----------------------------------♡
    water_for_oga_kg: float

# ------pressure percentages using Dalton's Law-----♡
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

# ------amine beds----------------------------------♡
    amine_beds: list
    scrub_per_bed_kpa: float

# ------power---------------------------------------♡
    battery_max_capacity_kwh: float
    battery_stored_kwh: float 
    solar_arrays: list
    daylight_m2_kw: float

# ------placeholders for future plans---------------♡
    relative_humidity: float

    # ♡ water ♡
    potable_water_l: float
    grey_water_l: float
    waste_brine_l: float

    # ♡ Integrity / safety ♡
    leak_rate_kpa_per_hr: float
    smoke_ppm: float
    radiation_msv_per_day: float