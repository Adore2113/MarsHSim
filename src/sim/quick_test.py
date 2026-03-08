from src.sim.state import Habitat_State
from src.sim.engine import step


s0 = Habitat_State(
    mission_time_s = 0,

    crew_count = 30,
    hab_vol_m3 = 2000.0,

    o2_kpa = 21.0,
    co2_kpa = 0.4,
    n2_kpa = 19.5,
    ar_kpa = 25.1,   

    cabin_temp_c=23.0,
    #from here down these are placeholders
    relative_humidity=40.0,

    potable_water_l=5000.0,
    grey_water_l=0.0,
    waste_brine_l=0.0,

    battery_kwh=1000.0,
    solar_input_kw=50.0,
    load_kw=20.0,

    leak_rate_kpa_per_hr=0.0,
    smoke_ppm=0.0,
    radiation_msv_per_day=0.7
)

state = s0
#12 steps = 1 hours b/c each step is 5min
for i in range(12):
    state = step(state)
    print(f"mission_time_s: {state.mission_time_s}")
    print(f"o2_kpa: {state.o2_kpa}")
    print(f"co2_kpa: {state.co2_kpa}")
    print(f"n2_kpa: {state.n2_kpa}")
    print(f"ar_kpa: {state.ar_kpa}")
    print()