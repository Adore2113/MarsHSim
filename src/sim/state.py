#--------------------imports-------------------------♡
from dataclasses import dataclass
#----------------------------------------------------♡


@dataclass
class Habitat_State:
    #---------------time and daylight----------------♡
    mission_time_s: int

    daylight_m2_kw: float
    
    peak_sunlight_today: float
    low_sunlight_streak_sols: int

    #--------------------lights----------------------♡
    light_level: float

    #---------------------crew-----------------------♡
    crew_count: int
    crew_activity: str

    #--------------------habitat---------------------♡
    hab_vol_m3: float

    #--------------------thermal---------------------♡
    hab_temp_c: float
    target_temp_c: float
    min_comfort_temp_c: float
    max_comfort_temp_c: float

    mars_temp_c: float

    target_humidity_pct: float
    current_humidity_pct: float

    insulation_strength_kw_per_c: float
    thermal_mass_kwh_per_c: float

    radiators: list
    heaters: list
    #---------------current atmosphere---------------♡
    
    #---------------current atmosphere---------------♡
    #---------gas targets----------♡
    target_pressure_kpa: float
    target_o2_kpa: float
    target_co2_kpa: float
    target_n2_kpa: float
    target_ar_kpa: float
    target_ch2_kpa: float

    min_safe_pressure_kpa: float
    min_safe_o2_kpa: float
    min_safe_co2_kpa: float
    min_safe_n2_kpa: float
     min_safe_ar_kpa: float
       
    max_safe_pressure_kpa: float
    max_safe_o2_kpa: float
    max_safe_co2_kpa: float
    max_safe_n2_kpa: float
    max_safe_ar_kpa: float

    #---------------current atmosphere---------------♡
    o2_kpa: float
    co2_kpa: float
    n2_kpa: float
    ar_kpa: float
    ch4_kpa: float

    #------------------gas storage-------------------♡
    n2_stored_kpa: float
    ar_stored_kpa: float
    co2_stored_kpa: float
    h2_stored_kg: float
    ch4_stored_kg: float 

    #------pressure percentages w. Dalton's Law------♡
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

    #------------------amine_beds--------------------♡
    amine_beds: list
    scrub_per_bed_kpa: float

    #-----------------power / solar------------------♡
    battery_max_capacity_kwh: float
    battery_stored_kwh: float 
    
    solar_arrays: list
    solar_absorptivity: int

    #---------------------water----------------------♡
    potable_water_storage_kg: float
    gray_water_storage_kg: float
    black_water_storage_kg: float   
    condensate_storage_kg: float   
    brine_storage_kg: float

    potable_water_storage_capacity_kg: float
    gray_water_storage_capacity_kg: float
    black_water_storage_capacity_kg: float
    condensate_storage_capacity_kg: float
    brine_storage_capacity_kg: float 
    
    #------------------placeholders------------------♡
    leak_rate_kpa_per_hr: float
    smoke_ppm: float
    radiation_msv_per_day: float

    #----------------wellness lights-----------------♡
    wellness_lights_on: bool = False