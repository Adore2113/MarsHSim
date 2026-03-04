from dataclasses import dataclass

#creating habitat class
@dataclass
class Habitat_State:
    # Time
    mission_time_s: int

    # Atmosphere
    o2_kpa: float
    co2_kpa: float
    n2_kpa: float

    @property
    def total_pressure_kpa(self) -> float:
        return self.o2_kpa + self.co2_kpa + self.n2_kpa

    @property
    def o2_percent(self):
        if self.total_pressure_kpa == 0:
            return 0
        return self.o2_kpa / self.total_pressure_kpa

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