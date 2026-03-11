from src.sim.state import Habitat_State
from src.sim.engine import step, gas_alert

s0 = Habitat_State(
    mission_time_s = 0,

    crew_count = 30,
    hab_vol_m3 = 2000.0,

    o2_kpa = 20.0,
    co2_kpa = 0.4,
    n2_kpa = 18.0,
    ar_kpa = 21.6,   

    amine_beds = [
        {"status": "online", "capacity": 3.0, "co2_load": 0.0},
        {"status": "regenerating", "capacity": 3.0, "co2_load": 1.0},
        {"status": "standby", "capacity": 3.0, "co2_load": 0.0},
        {"status": "standby", "capacity": 3.0, "co2_load": 0.0}
    ],

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


def sol_time(seconds):
    # one mars sol is 24h 39min 35sec
    total_sol_seconds = 88775
    sol_seconds = seconds % total_sol_seconds

    hour_24 = sol_seconds // 3600
    # 1h = 60min, 1min = 60 sec, 60*60 = 3600
    minutes = (sol_seconds % 3600) // 60
    
    meridiem = "AM"
    hour_12 = hour_24

    if hour_24 >= 12:
        meridiem = "PM"
    if hour_24 > 12:
        hour_12 = hour_24 - 12
    if hour_24 == 0:
        hour_12 = 12

    return hour_12, minutes, meridiem

    
def print_state(state, scrubbed_amount): 
    hour, minutes, meridiem = sol_time(state.mission_time_s)
    # LMST = Local Mean Solar Time
    print(f"Sol: n/a | {hour}:{minutes:02d} {meridiem} LMST")
    print(f"Oxygen: {state.o2_kpa}")
    print(f"Hydrogen stored: {state.h2_stored_kg}")    
    print(f"Carbon Dioxide Scrubbed: {scrubbed_amount:.4f}")
    print(f"Carbon Dioxide: {state.co2_kpa}")
    print(f"Alert: {alerts}")
    print(f"Nitrogen: {state.n2_kpa}")
    print(f"Argon: {state.ar_kpa}")
    print(f"Total Pressure: {state.total_pressure_kpa}")
    print()


state = s0
for i in range(12):
    state, scrubbed_amount = step(state)
    alerts = gas_alert(state)
    print_state(state, scrubbed_amount)