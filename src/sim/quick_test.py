from src.sim.state import Habitat_State
from src.sim.engine import step


s0 = Habitat_State(
    mission_time_s=0,
    o2_kpa=21.0,
    co2_kpa=0.6,
    n2_kpa=48.4,
    cabin_temp_c=22.0,
    relative_humidity=40.0,
    potable_water_l=400.0,
    grey_water_l=50.0,
    waste_brine_l=10.0,
    battery_kwh=20.0,
    solar_input_kw=3.0,
    load_kw=2.5,
    leak_rate_kpa_per_hr=0.0,
    smoke_ppm=0.0,
    radiation_msv_per_day=0.7,
)

s1 = step(s0)
print(s0.mission_time_s, s1.mission_time_s)
print(s0.total_pressure_kpa)